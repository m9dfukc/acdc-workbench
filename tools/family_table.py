#!/usr/bin/env python3
"""Family levels of several measurements as a Markdown table (evaluation as in D34/D35).

Reads out/<ID>/<ID>.json (python -m analysis) and averages each quantity over the 4 channels
in power: RMS >= 20 Hz, residual without interference lines ("Rest"), comb ("Kamm", usb1k),
fs/8, intermodulation products ("Mischprod.", imd). Values in file dBFS (like the analysis).
Optional --ref: Δ in parentheses against the mean of the reference IDs (e.g. the control
of the same session). The table text is German because it goes into the project reports.

Usage:
  uv run python tools/family_table.py B4-3d-r1 B4-3d-r2 B4-fx3i-r1 … [--ref B4-3d-r1 B4-3d-r2]
                                       [--group B4-3d=B4-3d-r1,B4-3d-r2 …] [--out file.md]
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLS = [("rms", "RMS ≥ 20 Hz"), ("rest", "Rest"), ("usb1k", "Kamm"), ("fs8", "fs/8"), ("imd", "Mischprod.")]


def pmean(dbs: list[float]) -> float:
    return 10 * math.log10(sum(10 ** (d / 10) for d in dbs) / len(dbs))


def levels(mid: str) -> dict[str, float]:
    d = json.loads((ROOT / "out" / mid / f"{mid}.json").read_text())
    acc: dict[str, list[float]] = {k: [] for k, _ in COLS}
    for ch in d["channels"]:
        r = ch["result"]
        acc["rms"].append(r["rms_db"])
        acc["rest"].append(r["rest_rms_db"])
        fam = {f["key"]: f for f in r["families"]}
        for k in ("usb1k", "fs8", "imd"):
            if k in fam and fam[k].get("rms_db") is not None:
                acc[k].append(fam[k]["rms_db"])
    out = {k: pmean(v) for k, v in acc.items() if v}
    fam0 = {f["key"]: f for f in d["channels"][0]["result"]["families"]}
    out["f_comb"] = fam0.get("usb1k", {}).get("f0")
    return out


def mean_of(ids: list[str]) -> dict[str, float]:
    ls = [levels(i) for i in ids]
    return {k: pmean([l[k] for l in ls]) for k, _ in COLS}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="+", help="manifest IDs (out/<ID>/<ID>.json)")
    ap.add_argument("--ref", nargs="+", help="reference IDs for Δ (mean in power)")
    ap.add_argument("--group", action="append", default=[], help="NAME=ID1,ID2: additional row with the mean")
    ap.add_argument("--out", help="also write the Markdown to this file")
    a = ap.parse_args()
    ref = mean_of(a.ref) if a.ref else None
    head = "| Messung | " + " | ".join(t for _, t in COLS) + " | Kamm-f0 Hz |"
    lines = [head, "|" + "---|" * (len(COLS) + 2)]

    def row(name: str, lv: dict, fc) -> str:
        cells = []
        for k, _ in COLS:
            c = f"{lv[k]:.2f}"
            if ref:
                c += f" ({lv[k] - ref[k]:+.2f})"
            cells.append(c)
        return f"| {name} | " + " | ".join(cells) + f" | {fc:.4f} |" if fc else f"| {name} | " + " | ".join(cells) + " | |"

    for i in a.ids:
        lv = levels(i)
        lines.append(row(i, lv, lv.get("f_comb")))
    for g in a.group:
        name, ids = g.split("=", 1)
        lines.append(row(f"**{name}** (Mittel)", mean_of(ids.split(",")), None))
    if ref:
        lines.append("")
        lines.append(f"Δ in Klammern gegen Mittel von {', '.join(a.ref)}. Datei-dBFS (Geräte-dBFS = −6,02 dB).")
    text = "\n".join(lines)
    print(text)
    if a.out:
        Path(a.out).write_text(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
