#!/usr/bin/env python3
"""Find single wrong samples in a loopback recording (Out n → In n, one sine per channel).

Complements tools/phase_slips.py: slips shift the phase, a single wrong sample
(e.g. a stale DMA buffer) hardly does. Per channel a sine (frequency searched finely) plus
DC offset is fitted robustly; samples with |residual| > k · median(|residual|) count as wrong.

Output per channel:
  - amplitude from all samples and from the clean samples (Δ = level loss caused by the errors)
  - number of wrong samples and their position in the block grid (index mod --block)
  - which lag explains the wrong values best: value ≈ model[n + lag]
    (lag = −2·block → stale value from the previous pass of the double buffer)

Finding D40: fx3i/noD, channel 4, one sample per 8-frame block = value from 16 frames earlier.

Usage:
  UV_CACHE_DIR=.uv-cache uv run python tools/stale_samples.py <wav> --freqs 440 530 670 790 \
      [--skip 3] [--dur 2] [--block 8] [--k 8] [--json out.json]
"""
from __future__ import annotations

import argparse
import json
import sys

import numpy as np
import soundfile as sf


def fit(s: np.ndarray, fs: int, f0: float, span: float = 0.2, steps: int = 401):
    t = np.arange(len(s)) / fs
    best = None
    for f in np.linspace(f0 - span, f0 + span, steps):
        A = np.c_[np.cos(2 * np.pi * f * t), np.sin(2 * np.pi * f * t), np.ones(len(s))]
        c, *_ = np.linalg.lstsq(A, s, rcond=None)
        e = float(np.sum((s - A @ c) ** 2))
        if best is None or e < best[0]:
            best = (e, f, A)
    _, f, A = best
    good = np.ones(len(s), bool)
    for _ in range(3):  # robust: falsche Samples aus der Anpassung nehmen
        c, *_ = np.linalg.lstsq(A[good], s[good], rcond=None)
        r = s - A @ c
        good = np.abs(r) <= K * np.median(np.abs(r)) + 1e-12
    c_all, *_ = np.linalg.lstsq(A, s, rcond=None)
    return f, A @ c, c, c_all, good


def main() -> int:
    global K
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("wav")
    ap.add_argument("--freqs", type=float, nargs="+", required=True, help="tone per channel (In 1, In 2, …)")
    ap.add_argument("--skip", type=float, default=3.0, help="skip the beginning [s] (fade-in)")
    ap.add_argument("--dur", type=float, default=2.0, help="analysed length [s]")
    ap.add_argument("--block", type=int, default=8, help="audio block size [frames] for the grid")
    ap.add_argument("--k", type=float, default=8.0, help="threshold in multiples of the median residual")
    ap.add_argument("--json", help="also write the result as JSON")
    a = ap.parse_args()
    K = a.k
    x, fs = sf.read(a.wav, dtype="float64", always_2d=True)
    i0 = int(a.skip * fs)
    x = x[i0:i0 + int(a.dur * fs)]
    lags = sorted({0, -a.block, -2 * a.block, -3 * a.block, -4 * a.block, a.block, 2 * a.block, -1, 1})
    out = []
    print(f"{a.wav}: {len(x)} frames from {a.skip} s, block {a.block}, threshold {a.k}×median")
    for ch, f0 in enumerate(a.freqs[: x.shape[1]]):
        s = x[:, ch]
        f, model, c, c_all, good = fit(s, fs, f0)
        bad = np.nonzero(~good)[0]
        amp_good = 20 * np.log10(np.hypot(c[0], c[1]))
        amp_all = 20 * np.log10(np.hypot(c_all[0], c_all[1]))
        hist = np.bincount(bad % a.block, minlength=a.block).tolist()
        row = dict(channel=ch + 1, freq=round(f, 4), amp_all_dbfs=round(amp_all, 2), amp_good_dbfs=round(amp_good, 2),
                   bad=len(bad), blocks=len(s) // a.block, bad_per_block_pos=hist)
        line = (f"Channel {ch + 1} ({f:.4f} Hz): amplitude {amp_all:.2f} dBFS (clean {amp_good:.2f}, Δ {amp_all - amp_good:+.2f} dB), "
                f"wrong samples {len(bad)} of {len(s)} ({100 * len(bad) / max(1, len(s) // a.block):.1f} % of blocks), "
                f"position mod {a.block}: {hist}")
        if len(bad):
            errs = {lag: float(np.mean(np.abs(s[bad] - model[np.clip(bad + lag, 0, len(s) - 1)]))) for lag in lags}
            best = min(errs, key=errs.get)
            noise = float(np.median(np.abs(s[good] - model[good])))
            row.update(best_lag=best, best_lag_err=errs[best], lag_err=errs, resid_median=noise)
            line += (f"\n    value ≈ model[n{best:+d}] (mean error {errs[best]:.5f}, noise {noise:.5f}; "
                     f"n+0: {errs[0]:.4f}) → " + ("stale value" if best < 0 and errs[best] < 5 * noise + 1e-4 else "unclear"))
        print(line)
        out.append(row)
    if a.json:
        with open(a.json, "w") as fh:
            json.dump(dict(wav=a.wav, skip=a.skip, dur=a.dur, block=a.block, k=a.k, channels=out), fh, indent=1)
    return 0


K = 8.0
if __name__ == "__main__":
    sys.exit(main())
