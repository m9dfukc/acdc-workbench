"""Selbsttest mit synthetischem Signal, dessen Linien, Pegel und Klicks bekannt sind.

Aufruf:  uv run python -m analysis.selftest [--seconds 60] [--fs 48000]
Prüft: f0-Genauigkeit (< 0,005 Hz), Linienpegel (± 0,5 dB), Trennung 6000,00 vs. 6·1000,053 Hz,
Leistungsanteil der Linien und Klick-Detektion. Exit-Code 1 bei Fehlern.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np

from . import timing
from .lines import analyse_channel


def synth(seconds, fs, rng):
    t = np.arange(int(seconds * fs)) / fs
    x = rng.normal(0, 10 ** (-90 / 20), len(t))  # breitbandig −90 dB RMS
    truth = {"usb1k": (1000.053, {}), "fs8": (6000.0, {}), "led": (2320.98, {}), "mains50": (50.01, {})}
    for k in range(1, 24):
        if k * 1000.053 < fs / 2 * 0.99:
            lvl = -82 - 0.4 * k
            truth["usb1k"][1][k] = lvl
            x += 10 ** (lvl / 20) * np.sin(2 * np.pi * k * 1000.053 * t + rng.uniform(0, 6.3))
    for k, lvl in [(1, -83.0), (2, -85.0), (3, -86.0)]:
        truth["fs8"][1][k] = lvl
        x += 10 ** (lvl / 20) * np.sin(2 * np.pi * k * 6000.0 * t + rng.uniform(0, 6.3))
    for k, lvl in [(1, -80.0), (2, -79.0), (3, -88.0)]:
        truth["led"][1][k] = lvl
        x += 10 ** (lvl / 20) * np.sin(2 * np.pi * k * 2320.98 * t + rng.uniform(0, 6.3))
    truth["mains50"][1][1] = -95.0
    imd = [(7, -1, -95.0), (8, -1, -93.0), (14, -1, -94.0), (2, 1, -96.0)]  # n·f1 + m·6000
    for n, m, lvl in imd:
        x += 10 ** (lvl / 20) * np.sin(2 * np.pi * (n * 1000.053 + m * 6000.0) * t + rng.uniform(0, 6.3))
    x += 10 ** (-95 / 20) * np.sin(2 * np.pi * 50.01 * t)
    clicks = [tc for tc in (1.234, 4.5, 7.777) if tc < seconds - 0.1]
    for tc in clicks:
        i = int(tc * fs)
        x[i : i + 24] += 10 ** (-50 / 20) * np.hanning(24) * np.sign(np.sin(np.arange(24)))
    x = np.round(x * 32768) / 32768  # 16-Bit-Quantisierung wie USB
    return x, truth, clicks, imd


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=60)
    ap.add_argument("--fs", type=int, default=48000)
    a = ap.parse_args(argv)
    rng = np.random.default_rng(1)
    x, truth, click_t, imd_truth = synth(a.seconds, a.fs, rng)
    res = analyse_channel(x, a.fs, 48000)
    errors = []
    fams = {f["key"]: f for f in res["families"]}
    bin_hz = 1 / a.seconds
    all_lines = [(key, k * f0) for key, (f0, lv) in truth.items() for k in lv]
    all_lines += [("imd", n * 1000.053 + m * 6000.0) for n, m, _ in imd_truth]

    def unresolvable(key, f):
        """Hann trennt zwei Linien erst ab ≈ 4 Bins Abstand."""
        return any(o != key and abs(f - g) < 4 * bin_hz for o, g in all_lines)

    for key, (f0, levels) in truth.items():
        fam = fams.get(key)
        if not fam:
            errors.append(f"{key}: Familie nicht gefunden")
            continue
        df = abs(fam["f0"] - f0)
        print(f"{key:8s} f0 {fam['f0']:.5f} Hz (soll {f0}, Δ {df * 1000:.2f} mHz), {fam['n']} Linien")
        if df > 0.005:
            errors.append(f"{key}: f0-Fehler {df:.4f} Hz")
        found = {h["k"]: h for h in fam["harmonics"]}
        for k, lvl in levels.items():
            h = found.get(k)
            if h is None and unresolvable(key, k * f0):
                print(f"  {key} k={k}: nicht auflösbar bei {bin_hz:.3f} Hz Bin-Breite (erwartet)")
            elif h is None:
                errors.append(f"{key} k={k}: nicht gefunden")
            elif abs(h["level_db"] - lvl) > 0.5 and not unresolvable(key, k * f0):
                errors.append(f"{key} k={k}: Pegel {h['level_db']:.2f} statt {lvl}")
        extra = set(found) - set(levels)
        if extra:
            errors.append(f"{key}: falsche Harmonische {sorted(extra)}")
    got_imd = {(h["n"], h["m"]): h for h in fams.get("imd", {"harmonics": []})["harmonics"]}
    for n, m, lvl in imd_truth:
        f = n * 1000.053 + m * 6000.0
        h = got_imd.get((n, m))
        if h is None and not unresolvable("imd", f):
            errors.append(f"Mischprodukt {n}·f1{m:+d}·f2 ({f:.3f} Hz) nicht gefunden")
        elif h is not None and abs(h["level_db"] - lvl) > 0.7 and not unresolvable("imd", f):
            errors.append(f"Mischprodukt {n},{m}: Pegel {h['level_db']:.2f} statt {lvl}")
    extra_imd = set(got_imd) - {(n, m) for n, m, _ in imd_truth}
    print(f"Mischprodukte gefunden: {sorted(got_imd)}")
    if extra_imd:
        errors.append(f"falsche Mischprodukte {sorted(extra_imd)}")
    ms_true = sum(10 ** (lv / 10) / 2 for _, lv_ in truth.values() for lv in lv_.values())
    ms_true += sum(10 ** (lv / 10) / 2 for *_, lv in imd_truth)
    share_true = ms_true / np.mean(x**2)
    print(f"Linienanteil {res['lines_share'] * 100:.1f} % (soll ≈ {share_true * 100:.1f} %)")
    if abs(res["lines_share"] - share_true) > 0.03:
        errors.append("Linienanteil weicht ab")
    clk, _ = timing.clicks(x, a.fs)
    got = [e["t"] for e in clk["events"]]
    print(f"Klicks bei {[round(t, 3) for t in got]} (soll {click_t})")
    if len(got) != len(click_t) or any(abs(g - c) > 0.002 for g, c in zip(got, click_t)):
        errors.append("Klick-Detektion falsch")
    for e in errors:
        print("FEHLER:", e)
    print("OK" if not errors else f"{len(errors)} Fehler")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
