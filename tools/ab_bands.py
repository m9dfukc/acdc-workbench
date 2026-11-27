#!/usr/bin/env python3
"""A/B/A comparison of recordings: levels per third-octave band, new lines, clicks (D93).

For each comparison three WAVs: A1, B, A2 (e.g. old build -> new build -> old build, same setup).
Per channel the script computes
  - RMS >= 20 Hz (2nd-order Butterworth high-pass),
  - the power per third-octave band 25 Hz ... 20 kHz (Welch PSD, 1 Hz resolution),
  - lines: PSD peaks >= THRESH dB above a running median of the floor (+-50 Hz). A line of B
    counts as new if it is at least DELTA dB stronger than in both A runs,
  - clicks: samples of the high-passed signal above CLICK x the RMS.
B counts as "same" in a band if it lies inside the spread of the two A runs plus TOL dB.

Values in file dBFS (scale, default 2.0 as in acdc_rec.py). The Markdown table is German
because it goes into the project reports (docs/messlog.md).

Usage:
  uv run python tools/ab_bands.py --name TapeDelay A1.wav B.wav A2.wav [--name … A1 B A2 …]
                                  [--out out/D93-ab-bands.md] [--channels 1 2]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal
from scipy.ndimage import median_filter

TOL = 1.0      # dB tolerance beyond the A-A spread
THRESH = 12.0  # dB above the local floor for a line
DELTA = 6.0    # dB a line of B must exceed both A runs to count as new
CLICK = 10.0   # x RMS for a click


def load(path: Path, scale: float) -> tuple[np.ndarray, int]:
    x, fs = sf.read(path, dtype="float64", always_2d=True)
    return x * scale, fs


def db(p: float) -> float:
    return 10 * np.log10(max(p, 1e-30))


def third_octaves() -> list[tuple[float, float, float]]:
    centers = [1000 * 2 ** (k / 3) for k in range(-16, 14)]  # 25 Hz ... 20 kHz
    return [(c, c * 2 ** (-1 / 6), c * 2 ** (1 / 6)) for c in centers if 20 <= c <= 20500]


def analyse(x: np.ndarray, fs: int) -> dict:
    sos = signal.butter(2, 20, "highpass", fs=fs, output="sos")
    y = signal.sosfiltfilt(sos, x)
    rms = float(np.sqrt(np.mean(y ** 2)))
    f, p = signal.welch(x, fs=fs, nperseg=fs, noverlap=fs // 2, window="hann", detrend="constant")
    bands = {}
    for c, lo, hi in third_octaves():
        m = (f >= lo) & (f < hi)
        bands[c] = db(float(np.sum(p[m]) * (f[1] - f[0])))
    floor = median_filter(p, size=101, mode="nearest")
    ratio = 10 * np.log10(np.maximum(p, 1e-30) / np.maximum(floor, 1e-30))
    peaks, _ = signal.find_peaks(ratio, height=THRESH)
    peaks = [k for k in peaks if f[k] >= 20]
    clicks = int(np.sum(np.abs(y) > CLICK * rms)) if rms > 0 else 0
    return {"rms": db(rms ** 2), "bands": bands, "f": f, "p": p, "peaks": peaks, "clicks": clicks,
            "peak": 20 * np.log10(max(float(np.max(np.abs(x))), 1e-15))}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", action="append", nargs=4, metavar=("NAME", "A1", "B", "A2"), required=True)
    ap.add_argument("--channels", type=int, nargs="+", default=[1, 2])
    ap.add_argument("--scale", type=float, default=2.0)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()

    lines = ["| Vergleich | Kanal | RMS A1 / B / A2 | Δ B gegen A | Terzbänder außerhalb A±1 dB | größte Abweichung | neue Linien in B | Knackser A1 / B / A2 |",
             "|---|---|---|---|---|---|---|---|"]
    worst_all = 0.0
    for name, *files in a.name:
        data = [load(Path(fn), a.scale) for fn in files]
        for ch in a.channels:
            r = [analyse(x[:, ch - 1], fs) for x, fs in data]
            a1, b, a2 = r
            amean = db((10 ** (a1["rms"] / 10) + 10 ** (a2["rms"] / 10)) / 2)
            out_bands, worst, worst_c = [], 0.0, None
            for c in a1["bands"]:
                lo = min(a1["bands"][c], a2["bands"][c]) - TOL
                hi = max(a1["bands"][c], a2["bands"][c]) + TOL
                v = b["bands"][c]
                if v < lo or v > hi:
                    dev = v - hi if v > hi else v - lo
                    out_bands.append(f"{c:.0f} Hz ({dev:+.1f})")
                    if abs(dev) > abs(worst):
                        worst, worst_c = dev, c
            worst_all = max(worst_all, abs(worst))
            new = []
            f = b["f"]
            for k in b["peaks"]:
                lb = db(b["p"][k])
                win = slice(max(k - 2, 0), k + 3)
                la = max(db(float(np.max(a1["p"][win]))), db(float(np.max(a2["p"][win]))))
                if lb - la >= DELTA:
                    new.append(f"{f[k]:.0f} Hz (+{lb - la:.0f})")
            lines.append(
                f"| {name} | {ch} | {a1['rms']:.2f} / {b['rms']:.2f} / {a2['rms']:.2f} | {b['rms'] - amean:+.2f} | "
                f"{len(out_bands)} von {len(a1['bands'])}{': ' + ', '.join(out_bands[:4]) if out_bands else ''}"
                f"{' …' if len(out_bands) > 4 else ''} | "
                f"{f'{worst:+.1f} dB bei {worst_c:.0f} Hz' if worst_c else '–'} | "
                f"{', '.join(new[:5]) if new else 'keine'}{' …' if len(new) > 5 else ''} | "
                f"{a1['clicks']} / {b['clicks']} / {a2['clicks']} |")
            print(f"{name} ch{ch}: RMS {a1['rms']:.2f}/{b['rms']:.2f}/{a2['rms']:.2f}, bands outside {len(out_bands)}, "
                  f"new lines {len(new)}, clicks {a1['clicks']}/{b['clicks']}/{a2['clicks']}, peak B {b['peak']:.1f} dBFS")
    text = "\n".join(lines) + "\n"
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(text, encoding="utf-8")
        print(f"Table: {a.out}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
