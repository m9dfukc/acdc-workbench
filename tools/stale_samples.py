#!/usr/bin/env python3
"""Einzelne falsche Samples in einer Loop-Aufnahme (Out n → In n, Sinus je Kanal) finden.

Ergänzt tools/phase_slips.py: Slips verschieben die Phase, ein einzelner falscher Sample
(z. B. veralteter DMA-Puffer) kaum. Pro Kanal wird ein Sinus (Frequenz fein gesucht) plus
Gleichanteil robust angepasst; Samples mit |Rest| > k · Median(|Rest|) gelten als falsch.

Ausgabe je Kanal:
  - Amplitude aus allen Samples und aus den sauberen Samples (Δ = Pegelverlust durch Fehler)
  - Anzahl falscher Samples und ihre Lage im Block-Raster (Index mod --block)
  - Welcher Abstand die falschen Werte am besten erklärt: Wert ≈ Modell[n + lag]
    (lag = −2·Block → veralteter Wert aus dem vorigen Umlauf des Doppelpuffers)

Befund D40: fx3i/noD, Kanal 4, ein Sample pro 8-Frame-Block = Wert von 16 Frames vorher.

Aufruf:
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
    ap.add_argument("--freqs", type=float, nargs="+", required=True, help="Ton je Kanal (In 1, In 2, …)")
    ap.add_argument("--skip", type=float, default=3.0, help="Anfang überspringen [s] (Einblenden)")
    ap.add_argument("--dur", type=float, default=2.0, help="ausgewertete Länge [s]")
    ap.add_argument("--block", type=int, default=8, help="Audio-Blockgröße [Frames] für das Raster")
    ap.add_argument("--k", type=float, default=8.0, help="Schwelle in Vielfachen des Median-Rests")
    ap.add_argument("--json", help="Ergebnis zusätzlich als JSON")
    a = ap.parse_args()
    K = a.k
    x, fs = sf.read(a.wav, dtype="float64", always_2d=True)
    i0 = int(a.skip * fs)
    x = x[i0:i0 + int(a.dur * fs)]
    lags = sorted({0, -a.block, -2 * a.block, -3 * a.block, -4 * a.block, a.block, 2 * a.block, -1, 1})
    out = []
    print(f"{a.wav}: {len(x)} Frames ab {a.skip} s, Block {a.block}, Schwelle {a.k}×Median")
    for ch, f0 in enumerate(a.freqs[: x.shape[1]]):
        s = x[:, ch]
        f, model, c, c_all, good = fit(s, fs, f0)
        bad = np.nonzero(~good)[0]
        amp_good = 20 * np.log10(np.hypot(c[0], c[1]))
        amp_all = 20 * np.log10(np.hypot(c_all[0], c_all[1]))
        hist = np.bincount(bad % a.block, minlength=a.block).tolist()
        row = dict(channel=ch + 1, freq=round(f, 4), amp_all_dbfs=round(amp_all, 2), amp_good_dbfs=round(amp_good, 2),
                   bad=len(bad), blocks=len(s) // a.block, bad_per_block_pos=hist)
        line = (f"Kanal {ch + 1} ({f:.4f} Hz): Amplitude {amp_all:.2f} dBFS (sauber {amp_good:.2f}, Δ {amp_all - amp_good:+.2f} dB), "
                f"falsche Samples {len(bad)} von {len(s)} ({100 * len(bad) / max(1, len(s) // a.block):.1f} % der Blöcke), "
                f"Lage mod {a.block}: {hist}")
        if len(bad):
            errs = {lag: float(np.mean(np.abs(s[bad] - model[np.clip(bad + lag, 0, len(s) - 1)]))) for lag in lags}
            best = min(errs, key=errs.get)
            noise = float(np.median(np.abs(s[good] - model[good])))
            row.update(best_lag=best, best_lag_err=errs[best], lag_err=errs, resid_median=noise)
            line += (f"\n    Wert ≈ Modell[n{best:+d}] (mittl. Fehler {errs[best]:.5f}, Rauschen {noise:.5f}; "
                     f"n+0: {errs[0]:.4f}) → " + ("veralteter Wert" if best < 0 and errs[best] < 5 * noise + 1e-4 else "unklar"))
        print(line)
        out.append(row)
    if a.json:
        with open(a.json, "w") as fh:
            json.dump(dict(wav=a.wav, skip=a.skip, dur=a.dur, block=a.block, k=a.k, channels=out), fh, indent=1)
    return 0


K = 8.0
if __name__ == "__main__":
    sys.exit(main())
