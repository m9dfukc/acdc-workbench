"""Empfindlichkeit des Klick-Detektors (analysis.timing.clicks) an einer echten Aufnahme prüfen.

Schneidet ein Stück aus der Aufnahme, baut künstliche USB-Fehler ein und meldet, ob der Detektor sie findet:
  dropN  N Samples fehlen (Puffer-Unterlauf, Frame verloren)
  dupN   N Samples doppelt (Puffer-Überlauf, Frame wiederholt)
  zeroN  N Samples Null (Lücke mit Stille)
Optional wird ein Sinus addiert (--sine Hz --level dBFS), um eine Rückführung Out → In nachzubilden.

Aufruf:
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
    ap.add_argument("--start", type=float, default=60.0, help="Startzeit des Ausschnitts [s]")
    ap.add_argument("--dur", type=float, default=60.0, help="Länge des Ausschnitts [s]")
    ap.add_argument("--sine", type=float, help="Sinus addieren [Hz] (Rückführung nachbilden)")
    ap.add_argument("--level", type=float, default=-12.0, help="Pegel des Sinus [dBFS Spitze]")
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
            res.append(f"{name}:" + (f"ja ({hit[0]['peak_over_median_db']:.0f} dB)" if hit else "NEIN"))
        print(f"Kanal {ch + 1} (Fehlalarme ohne Eingriff: {n0}): " + "  ".join(res))


if __name__ == "__main__":
    main()
