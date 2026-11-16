"""Check the sensitivity of the click detector (analysis.timing.clicks) on a real recording.

Cuts a section out of the recording, injects artificial USB faults and reports whether the detector finds them:
  dropN  N samples missing (buffer underrun, frame lost)
  dupN   N samples duplicated (buffer overrun, frame repeated)
  zeroN  N samples zero (gap filled with silence)
Optionally a sine is added (--sine Hz --level dBFS) to emulate a loopback Out → In.

Usage:
  UV_CACHE_DIR=.uv-cache uv run python tools/click_sensitivity.py <wav> [--start 60] [--dur 60] [--sine 440 --level -12]
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analysis import timing  # noqa: E402

FAULTS = ["drop48", "dup48", "zero48", "drop1", "dup1", "zero8"]


def inject(y, p, name):
    n = int(name.lstrip("adeoprupz"))
    if name.startswith("drop"):
        return np.concatenate([y[:p], y[p + n:], np.zeros(n)])
    if name.startswith("dup"):
        return np.concatenate([y[:p], y[p - n:p], y[p:-n]])
    y = y.copy()
    y[p:p + n] = 0
    return y


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("wav", type=Path)
    ap.add_argument("--start", type=float, default=60.0, help="start time of the section [s]")
    ap.add_argument("--dur", type=float, default=60.0, help="length of the section [s]")
    ap.add_argument("--sine", type=float, help="add a sine [Hz] (emulate a loopback)")
    ap.add_argument("--level", type=float, default=-12.0, help="level of the sine [dBFS peak]")
    a = ap.parse_args()

    info = sf.info(str(a.wav))
    fs = info.samplerate
    x, _ = sf.read(str(a.wav), start=int(a.start * fs), frames=int(a.dur * fs), dtype="float64", always_2d=True)
    t = np.arange(len(x)) / fs
    p = len(x) // 2 + 12345
    for ch in range(x.shape[1]):
        base = x[:, ch].copy()
        if a.sine:
            base += 10 ** (a.level / 20) * np.sin(2 * np.pi * a.sine * t)
        n0 = timing.clicks(base, fs)[0]["n"]
        res = []
        for name in FAULTS:
            c = timing.clicks(inject(base, p, name), fs)[0]
            hit = [e for e in c["events"] if abs(e["t"] - p / fs) < 0.01]
            res.append(f"{name}:" + (f"yes ({hit[0]['peak_over_median_db']:.0f} dB)" if hit else "NO"))
        print(f"Channel {ch + 1} (false alarms without injection: {n0}): " + "  ".join(res))


if __name__ == "__main__":
    main()
