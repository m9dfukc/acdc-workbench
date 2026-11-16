"""Measure the level of test tones and their intermodulation products per input (crosstalk outputs → inputs).

Averaged Hann FFT (segments of 2^22 samples), level as sine amplitude in dBFS, plus the distance to the
local floor (median ±20 Hz). Checked are the fundamentals, their 2nd harmonics and all sums/differences.

Usage:
  UV_CACHE_DIR=.uv-cache uv run python tools/crosstalk_lines.py <wav> --freqs 220 330 470 590
"""
import argparse
from itertools import combinations

import numpy as np
import soundfile as sf


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("wav")
    ap.add_argument("--freqs", type=float, nargs="+", required=True, help="test tones per output (Out 1, Out 2, …)")
    ap.add_argument("--nfft", type=int, default=2**22)
    a = ap.parse_args()

    x, fs = sf.read(a.wav, dtype="float64", always_2d=True)
    n = min(a.nfft, len(x))
    w = np.hanning(n)
    cg = w.sum() / 2
    P, k = 0.0, 0
    for s in range(0, len(x) - n + 1, n):
        P = P + (np.abs(np.fft.rfft(x[s:s + n].T * w, axis=1)) / cg) ** 2
        k += 1
    P /= k

    def lvl(ch, f):
        i = int(round(f * n / fs))
        return 10 * np.log10(P[ch, i - 3:i + 4].sum() / 1.5 + 1e-30)

    def floor(ch, f):
        return 10 * np.log10(np.median(P[ch, int((f - 20) * n / fs):int((f + 20) * n / fs)]) + 1e-30)

    rows = [(f"Out{i + 1} {f:g}", f) for i, f in enumerate(a.freqs)]
    rows += [(f"2·{f:g}={2 * f:g}", 2 * f) for f in a.freqs]
    for (i, f1), (j, f2) in combinations(enumerate(a.freqs), 2):
        lo, hi = sorted((f1, f2))
        rows += [(f"{hi:g}−{lo:g}={hi - lo:g} (O{i + 1}/O{j + 1})", hi - lo), (f"{f1:g}+{f2:g}={f1 + f2:g} (O{i + 1}/O{j + 1})", f1 + f2)]
    print(f"{'Line':<28}" + "".join(f"{'In' + str(c + 1):>14}" for c in range(x.shape[1])) + "   dBFS (distance to floor)")
    for name, f in rows:
        print(f"{name:<28}" + "".join(f"{lvl(c, f):8.1f} ({lvl(c, f) - floor(c, f):+3.0f})" for c in range(x.shape[1])))


if __name__ == "__main__":
    main()
