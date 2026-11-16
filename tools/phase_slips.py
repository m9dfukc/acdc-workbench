"""Sample-Slips über die Phase bekannter Sinustöne finden (Rückführung Out → In).

Pro Kanal wird der Ton per Hann-Fenster (Länge --win) im Raster --hop komplex demoduliert. Die Phase wird
abgewickelt und linear bereinigt. Ein fehlender oder doppelter Sample springt die Phase um 2π·f/fs.
Gesucht werden Sprünge zwischen zwei sich nicht überlappenden Fenstern über der Schwelle Median + k·MAD.
Ein echter USB-Slip trifft alle Kanäle zur selben Zeit mit derselben Sample-Zahl.

--inject N baut zum Test bei der halben Dauer einen Slip von N Samples ein (negativ: Samples fehlen).

Aufruf:
  UV_CACHE_DIR=.uv-cache uv run python tools/phase_slips.py <wav> --freqs 440 530 670 790 [--inject 1]
"""
import argparse
import json
from pathlib import Path

import numpy as np
import soundfile as sf


def demod_phase(x, fs, f, win, hop):
    n = len(x)
    w = np.hanning(win)
    starts = np.arange(0, n - win, hop)
    t = np.arange(win) / fs
    ph = np.empty(len(starts))
    amp = np.empty(len(starts))
    base = np.exp(-2j * np.pi * f * t) * w
    for i, s in enumerate(starts):
        z = np.dot(x[s:s + win], base) * np.exp(-2j * np.pi * f * s / fs)
        ph[i] = np.angle(z)
        amp[i] = np.abs(z) * 2 / w.sum()
    return (starts + win / 2) / fs, np.unwrap(ph), amp


def find_slips(tc, ph, f, fs, step, k):
    res = ph - np.polyval(np.polyfit(tc, ph, 2), tc)
    d = res[step:] - res[:-step]
    med = np.median(d)
    mad = np.median(np.abs(d - med)) * 1.4826
    thr = k * mad
    idx = np.flatnonzero(np.abs(d - med) > thr)
    events = []
    if len(idx):
        for g in np.split(idx, np.flatnonzero(np.diff(idx) > step) + 1):
            j = g[np.argmax(np.abs(d[g] - med))]
            events.append({"t": float(tc[j] + (tc[j + step] - tc[j]) / 2),
                           "slip_samples": float((d[j] - med) / (2 * np.pi * f / fs))})
    one = 2 * np.pi * f / fs
    return events, {"mad_rad": float(mad), "one_sample_rad": float(one), "snr_one_sample": float(one / mad),
                    "res_rms_rad": float(res.std())}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("wav", type=Path)
    ap.add_argument("--freqs", type=float, nargs="+", required=True, help="Ton je Kanal (In 1, In 2, …)")
    ap.add_argument("--win", type=int, default=2400, help="Fensterlänge [Samples]")
    ap.add_argument("--hop", type=int, default=480, help="Raster [Samples]")
    ap.add_argument("--k", type=float, default=10.0, help="Schwelle in MAD")
    ap.add_argument("--inject", type=int, default=0, help="Test-Slip in Samples (negativ = fehlen)")
    ap.add_argument("--json", type=Path, help="Ergebnis zusätzlich als JSON")
    a = ap.parse_args()

    x, fs = sf.read(str(a.wav), dtype="float64", always_2d=True)
    if a.inject:
        p = len(x) // 2 + 12345
        n = abs(a.inject)
        x = np.concatenate([x[:p], x[p + n:]]) if a.inject < 0 else np.concatenate([x[:p], x[p - n:p], x[p:]])
        print(f"Test-Slip {a.inject:+d} Samples bei t = {p / fs:.3f} s eingebaut")
    step = int(np.ceil(a.win / a.hop))
    out = {}
    for ch, f in enumerate(a.freqs):
        tc, ph, amp = demod_phase(x[:, ch], fs, f, a.win, a.hop)
        ev, st = find_slips(tc, ph, f, fs, step, a.k)
        amp_db = 20 * np.log10(np.median(amp))
        amp_spread = float(np.ptp(20 * np.log10(np.percentile(amp, [0.1, 99.9]))))
        print(f"Kanal {ch + 1} ({f:g} Hz): Amplitude {amp_db:.1f} dBFS (Spanne 0,1–99,9 % {amp_spread:.2f} dB), "
              f"1 Sample = {st['one_sample_rad'] * 1e3:.1f} mrad, Phasenrauschen (MAD) {st['mad_rad'] * 1e3:.2f} mrad "
              f"→ 1-Sample-Slip {st['snr_one_sample']:.0f}× über Rauschen. Ereignisse: {len(ev)}")
        for e in ev[:20]:
            print(f"    t = {e['t']:8.3f} s  Sprung {e['slip_samples']:+.2f} Samples")
        out[f"ch{ch + 1}"] = {"freq": f, "amp_dbfs": amp_db, **st, "events": ev}
    if a.json:
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
