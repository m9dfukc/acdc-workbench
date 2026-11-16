"""Linien finden, zu Familien (Kämmen) zusammenfassen, f0 per Least Squares fitten."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import signal

from .spectra import Spectrum, a_weighting, band_ms, pow_db, welch_density

SNR_START_DB = 15.0  # erste Harmonische einer Familie / freie Peak-Liste
SNR_TRACK_DB = 12.0  # weitere Harmonische an vorhergesagter Stelle (Fehlalarm ≈ 2e-5 pro Bin)


@dataclass
class Candidate:
    key: str
    label: str
    f0: float  # Startwert
    tol: float  # Suchbreite ± Hz für die erste Harmonische (wächst mit k)
    kmax: int | None = None


def default_candidates(device_fs: float, mains: float = 50.0) -> list[Candidate]:
    """Reihenfolge = Priorität beim Zuordnen. Sample-synchrone Linie zuerst, weil sie exakt sitzt.

    fs/8 = Blockrate bei AUDIO_BLOCK_SIZE 8 (Firmware v22.4.q). Bei Blockgröße 16 wäre es fs/16.
    """
    return [
        Candidate("fs8", f"fs/8 ({device_fs / 8:g} Hz, sample-synchron)", device_fs / 8, 0.3),
        Candidate("usb1k", "1-kHz-Kamm", 1000.0, 2.0),
        Candidate("led", "LED-PWM (≈ 2,32 kHz)", 2320.4, 6.0),
        # Netz nur bis < 1 kHz, sonst kollidiert k=20 mit dem 1-kHz-Kamm. Netzfrequenz ±0,2 Hz
        Candidate(f"mains{mains:g}", f"Netz {mains:g} Hz", mains, 0.2, int(990 // mains)),
    ]


def fit_f0(ks, freqs, weights=None):
    """Gewichtete Least Squares durch den Ursprung: f_k ≈ k·f0."""
    k = np.asarray(ks, float)
    fr = np.asarray(freqs, float)
    w = np.ones_like(k) if weights is None else np.asarray(weights, float)
    f0 = float((w * k * fr).sum() / (w * k**2).sum())
    return f0, fr - k * f0


def _weights(hits, ks):
    """Gewicht = Amplituden-SNR (linear), damit starke Linien den Fit bestimmen."""
    return [10 ** (min(hits[q]["snr_db"], 60) / 20) for q in ks]


def find_family(spec: Spectrum, cand: Candidate, fmax: float):
    kmax = int(fmax // cand.f0)
    if cand.kmax:
        kmax = min(kmax, cand.kmax)
    if kmax < 1:
        return None
    # Einstieg über die erste deutliche Harmonische k ≤ 3 (Grundton kann fehlen)
    hits = {}
    for k in range(1, min(3, kmax) + 1):
        r = spec.search(k * cand.f0, k * cand.tol)
        if r and r["snr_db"] >= SNR_START_DB:
            hits[k] = r
            break
    if not hits:
        return None
    for k in range(1, kmax + 1):
        if k in hits:
            continue
        ks = sorted(hits)
        f0, resid = fit_f0(ks, [hits[q]["freq"] for q in ks], _weights(hits, ks))
        # Unsicherheit einer Linie: ≥ 0,05 Bin, aus den Residuen, aber gedeckelt, damit ein
        # einzelner Fehltreffer das Suchfenster nicht aufbläht
        resid_rms = float(np.sqrt(np.mean(resid**2))) if len(ks) > 1 else 0.0
        sig_line = min(max(0.05 * spec.df, resid_rms), 0.5 * spec.df)
        sig_f0 = sig_line / np.sqrt(sum(q * q for q in ks))
        r = spec.search(k * f0, max(3 * spec.df, 5 * k * sig_f0), min_snr=SNR_TRACK_DB, closest=True)
        if r:
            hits[k] = r
    for r in hits.values():
        spec.claim(r["bin"])
    ks = sorted(hits)
    f0, resid = fit_f0(ks, [hits[q]["freq"] for q in ks], _weights(hits, ks))
    harmonics = [dict(k=k, **{n: hits[k][n] for n in ("bin", "freq", "level_db", "snr_db")},
                      resid_hz=float(resid[i])) for i, k in enumerate(ks)]
    return {
        "key": cand.key,
        "label": cand.label,
        "f0": f0,
        "resid_rms_hz": float(np.sqrt(np.mean(resid**2))),
        "n": len(harmonics),
        "kmax_searched": kmax,
        "harmonics": harmonics,
    }


def find_imd(spec: Spectrum, f1: float, f2: float, fmax: float, mmax: int = 4, key="imd"):
    """Mischprodukte n·f1 + m·f2 (m ≠ 0). Entstehen, wenn zwei periodische Störer
    nichtlinear zusammenwirken, z. B. 1-kHz-Takt × 6-kHz-Blockrate."""
    hits = []
    for m in range(-mmax, mmax + 1):
        if m == 0:
            continue
        for n in range(-int(mmax * f2 // f1) - 1, int((fmax - m * f2) // f1) + 2):
            f = n * f1 + m * f2
            if n == 0 or not (10 < f < fmax):
                continue
            r = spec.search(f, 2 * spec.df, min_snr=SNR_START_DB, closest=True)
            if r and abs(r["freq"] - f) < 1.0 * spec.df:
                spec.claim(r["bin"])
                hits.append(dict(k=f"{n}·f1{m:+d}·f2", n=n, m=m, bin=r["bin"], freq=r["freq"],
                                 level_db=r["level_db"], snr_db=r["snr_db"], resid_hz=r["freq"] - f))
    if not hits:
        return None
    return {"key": key, "label": f"Mischprodukte n·{f1:.4f} + m·{f2:.4f} Hz (m = ±1…±{mmax})", "f0": f1,
            "f2": f2, "resid_rms_hz": float(np.sqrt(np.mean([h["resid_hz"] ** 2 for h in hits]))),
            "n": len(hits), "kmax_searched": None, "harmonics": sorted(hits, key=lambda h: h["freq"])}


def assign_power(spec: Spectrum, families, half=3):
    """Leistung jeder Linie nach Parseval. Bins im Überlapp zweier Linien gehören der näheren,
    damit dicht benachbarte Linien (z. B. 6000,00 vs. 6000,32 Hz) nicht doppelt zählen."""
    owner = {}
    lines = [h for fam in families for h in fam["harmonics"]]
    for n, h in enumerate(lines):
        for b in range(h["bin"] - half, h["bin"] + half + 1):
            d = abs(b - h["bin"])
            if b not in owner or d < owner[b][1]:
                owner[b] = (n, d)
    ms = np.zeros(len(lines))
    for b, (n, _) in owner.items():
        if 0 <= b < len(spec.db):
            mean_noise = 10 ** (spec.floor[b] / 10) / np.log(2)
            ms[n] += (10 ** (spec.db[b] / 10) - mean_noise) / 2 / 1.5
    for h, v in zip(lines, ms):
        h["ms"] = float(max(v, 0.0))
    for fam in families:
        fam["ms"] = float(sum(h["ms"] for h in fam["harmonics"]))
        fam["rms_db"] = float(pow_db(fam["ms"]))
        for h in fam["harmonics"]:
            h.pop("bin")


def peak_list(spec: Spectrum, fmin: float, fmax: float, top: int = 40):
    lo, hi = max(1, spec.idx(fmin)), spec.idx(fmax)
    d = spec.db[lo:hi]
    idx, _ = signal.find_peaks(d, distance=3)
    idx = idx[(d[idx] - spec.floor[lo:hi][idx]) >= SNR_START_DB]
    idx = idx[np.argsort(d[idx])[::-1]][:top]
    peaks = []
    for i in idx + lo:
        r = spec.search(spec.f[i], spec.df, allow_claimed=True)
        if r:
            peaks.append(r)
    return peaks


def analyse_channel(x, fs, device_fs, top=40, extra_families=2, mains=50.0):
    """Komplette Linien- und Pegelanalyse eines Kanals."""
    spec = Spectrum(x, fs)
    fmax = min(fs, device_fs) / 2 * 0.995
    families = []
    for cand in default_candidates(device_fs, mains):
        fam = find_family(spec, cand, fmax)
        if fam:
            families.append(fam)
    fk = {f["key"]: f for f in families}
    if "usb1k" in fk and "fs8" in fk:
        imd = find_imd(spec, fk["usb1k"]["f0"], fk["fs8"]["f0"], fmax)
        if imd:
            families.append(imd)
    peaks = peak_list(spec, 10.0, fmax, top)
    # stärkste noch nicht erklärte Linie als eigene Familie prüfen
    for _ in range(extra_families):
        free = [p for p in peaks if not spec.claimed[p["bin"]]]
        if not free:
            break
        p = free[0]
        fam = find_family(spec, Candidate("other", f"stärkste übrige Linie ({p['freq']:.2f} Hz)",
                                          p["freq"], 3 * spec.df), fmax)
        if fam:
            fam["key"] = f"other{len([f for f in families if f['key'].startswith('other')]) + 1}"
            families.append(fam)
    # Peaks den Familien zuordnen (gleicher Bin)
    by_bin = {}
    for fam in families:
        for h in fam["harmonics"]:
            by_bin[h["bin"]] = f"{fam['key']}·{h['k']}"
    assign_power(spec, families)
    for p in peaks:
        p["family"] = next((by_bin[b] for b in range(p["bin"] - 1, p["bin"] + 2) if b in by_bin), None)

    # Pegel. Rauschleistung im Hörband (Hochpass 20 Hz, 4. Ordnung): Offene, DC-gekoppelte
    # Eingänge driften unter 1 Hz, das soll Störanteil und Notch-Gewinn nicht verfälschen.
    total = float(np.mean(x**2))
    x_ac = signal.sosfiltfilt(signal.butter(4, 20.0, btype="highpass", fs=fs, output="sos"), x)
    var = float(np.mean(x_ac**2))
    fd, psd = welch_density(x, fs)
    ms_a = float(np.trapezoid(psd * a_weighting(fd) ** 2, fd))
    bands = {name: pow_db(band_ms(fd, psd, lo, hi)) for name, lo, hi in
             [("<20 Hz", 0.0, 20), ("20–200 Hz", 20, 200), ("200 Hz–20 kHz", 200, 20000),
              (">20 kHz", 20000, fs / 2 + 1)]}
    # Bekannte Störfamilien vs. „übrige Linien“ (other*: Nutzsignal, unbekannte Töne).
    # Störanteil und Notch-Gewinn beziehen sich auf alles außer den übrigen Linien.
    ms_other = sum(f["ms"] for f in families if f["key"].startswith("other"))
    ms_lines = sum(f["ms"] for f in families if not f["key"].startswith("other"))
    noise = max(var - ms_other, 1e-30)
    for f in families:
        f["share"] = f["ms"] / (var if f["key"].startswith("other") else noise)
    rest = max(noise - ms_lines, 1e-30)
    return {
        "df_hz": spec.df,
        "rms_total_db": float(pow_db(total)),
        "drift_db": float(pow_db(max(total - var, 0.0))),
        "rms_db": float(pow_db(var)),
        "rms_a_db": float(pow_db(ms_a)),
        "bands_db": bands,
        "other_rms_db": float(pow_db(ms_other)),
        "noise_rms_db": float(pow_db(noise)),
        "lines_share": ms_lines / noise,
        "rest_rms_db": float(pow_db(rest)),
        "notch_gain_db": float(pow_db(noise) - pow_db(rest)),
        "families": families,
        "peaks": [{k: v for k, v in p.items() if k != "bin"} for p in peaks],
    }


def upsampling_check(x, fs, device_fs):
    """Liegt fs über der Geräterate und ist oberhalb device_fs/2 nichts drin → hochgerechnet."""
    if fs <= device_fs or np.mean(x**2) < 1e-15:  # Geräterate oder digital stumm
        return None
    fd, psd = welch_density(x, fs, 8192)
    lvl = pow_db(band_ms(fd, psd, device_fs / 2 * 1.05, fs / 2 * 0.98))
    return {"above_device_nyquist_db": float(lvl), "resampled": bool(lvl < -130)}
