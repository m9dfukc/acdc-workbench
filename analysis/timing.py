"""Zeitverhalten: f0-Drift und Pegel in Fenstern, periodische Modulation, Klicks."""

from __future__ import annotations

import numpy as np
from scipy import signal

from .spectra import Spectrum, pow_db


def window_length(duration, win_s):
    """Bei kurzen Dateien das Fenster verkleinern, damit mindestens ≈ 4 Fenster entstehen."""
    return win_s if duration >= 3 * win_s else max(1.0, duration / 4)


def stability(x, fs, families, win_s=10.0):
    """f0 und Pegel jeder Familie in überlappenden Fenstern (50 %)."""
    win = window_length(len(x) / fs, win_s)
    n, hop = int(win * fs), int(win * fs / 2)
    families = [f for f in families if f["key"] != "imd"]  # Mischprodukte haben kein einfaches Raster
    res = {fam["key"]: {"t": [], "f0": [], "rms_db": []} for fam in families}
    for start in range(0, len(x) - n + 1, hop):
        spec = Spectrum(x[start : start + n], fs)
        t = (start + n / 2) / fs
        for fam in families:
            hits = []
            for h in fam["harmonics"]:
                r = spec.search(h["k"] * fam["f0"], 3 * spec.df)
                if r and r["snr_db"] >= 6:
                    hits.append((h["k"], r))
            r_ = res[fam["key"]]
            r_["t"].append(t)
            if hits:
                top = sorted(hits, key=lambda kr: -kr[1]["level_db"])[:3]
                ks = np.array([k for k, _ in top], float)
                fr = np.array([r["freq"] for _, r in top])
                r_["f0"].append(float((ks * fr).sum() / (ks**2).sum()))
                r_["rms_db"].append(float(pow_db(sum(10 ** (r["level_db"] / 10) / 2 for _, r in hits))))
            else:
                r_["f0"].append(float("nan"))
                r_["rms_db"].append(float("nan"))
    summary = {}
    for key, r_ in res.items():
        f0 = np.array(r_["f0"])
        lv = np.array(r_["rms_db"])
        ok = np.isfinite(f0)
        s = {"windows": int(len(f0)), "valid": int(ok.sum()), "win_s": win}
        if ok.sum() >= 2:
            ppm = (f0[ok] / np.mean(f0[ok]) - 1) * 1e6
            t = np.array(r_["t"])[ok]
            s.update(f0_mean=float(np.mean(f0[ok])), f0_std_ppm=float(np.std(ppm)),
                     f0_slope_ppm_per_min=float(np.polyfit(t / 60, ppm, 1)[0]),
                     level_std_db=float(np.nanstd(lv)), level_range_db=float(np.nanmax(lv) - np.nanmin(lv)))
        summary[key] = s
    return res, summary


def level_envelope(x, fs, frame_s=0.01, band=None):
    """Kurzzeitpegel in dB (Rahmen frame_s), optional nur in einem Band ± 10 Hz."""
    y = x
    if band is not None and 20 < band < fs / 2 - 20:
        sos = signal.butter(4, [band - 10, band + 10], btype="bandpass", fs=fs, output="sos")
        y = signal.sosfiltfilt(sos, x)
    n = int(frame_s * fs)
    m = len(y) // n
    return np.arange(m) * frame_s + frame_s / 2, pow_db(np.mean(y[: m * n].reshape(m, n) ** 2, axis=1))


def modulation(x, fs, band=None, frame_s=0.01, fmin=None, fmax=20.0):
    """Periodische Pegelschwankung (z. B. 0,8 s laut antisvin): Spektrum der Hüllkurve.

    fmin: Standard = 4 Perioden pro Aufnahme, mindestens 0,02 Hz (lange Musterperioden, z. B. 18 s).
    """
    if fmin is None:
        fmin = max(0.02, 4 * fs / len(x))
    t, lvl = level_envelope(x, fs, frame_s, band)
    if len(lvl) < 50:
        return None
    fr, p = signal.periodogram(signal.detrend(lvl), fs=1 / frame_s, window="hann")
    sel = (fr >= fmin) & (fr <= fmax)
    if sel.sum() < 3:
        return None
    i = int(np.argmax(p[sel]))
    peak = float(fr[sel][i])
    return {"band_hz": band, "depth_std_db": float(np.std(lvl)), "peak_hz": peak,
            "period_s": 1 / peak, "prominence_db": float(pow_db(p[sel][i] / np.median(p[sel])))}


def clicks(x, fs, hp_hz=5000.0, thresh=8.0, smooth_ms=0.5, merge_ms=5.0, skip_s=0.05):
    """Klick-Detektor: Hochpass, geglättete Hüllkurve, Schwelle = Median + thresh·MAD."""
    hp_hz = min(hp_hz, 0.4 * fs)
    y = signal.sosfilt(signal.butter(4, hp_hz, btype="highpass", fs=fs, output="sos"), x)
    k = max(1, int(smooth_ms * 1e-3 * fs))
    env = np.convolve(np.abs(y), np.ones(k) / k, mode="same")
    skip = int(skip_s * fs)
    env[:skip] = 0
    env[-skip:] = 0
    core = env[skip:-skip]
    med = float(np.median(core))
    mad = float(np.median(np.abs(core - med))) * 1.4826
    thr = med + thresh * mad
    idx = np.flatnonzero(env > thr)
    events = []
    if len(idx):
        groups = np.split(idx, np.flatnonzero(np.diff(idx) > merge_ms * 1e-3 * fs) + 1)
        for g in groups:
            j = g[np.argmax(env[g])]
            events.append({"t": float(j / fs), "peak_over_median_db": float(pow_db((env[j] / med) ** 2))})
    times = np.array([e["t"] for e in events])
    iv = np.diff(times)
    return {
        "hp_hz": hp_hz, "threshold": thr, "median": med, "n": len(events),
        "per_min": len(events) / (len(x) / fs / 60),
        "interval_median_s": float(np.median(iv)) if len(iv) else None,
        "interval_cv": float(np.std(iv) / np.mean(iv)) if len(iv) > 1 else None,
        "events": events[:200],
    }, (np.arange(len(env)) / fs, env)
