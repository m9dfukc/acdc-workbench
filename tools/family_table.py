#!/usr/bin/env python3
"""Family levels of several measurements as a Markdown table (evaluation as in D34/D35).

Reads reports/<ID>/<ID>.json (python -m analysis) and averages each quantity over the 4 channels
in power: RMS >= 20 Hz, residual without interference lines ("Rest"), comb ("Kamm", usb1k),
fs/8, intermodulation products ("Mischprod.", imd). Values in file dBFS (like the analysis).
Optional --ref: Δ in parentheses against the mean of the reference IDs (e.g. the control
of the same session). The table text is German because it goes into the project reports.

Optional --dc-ref/--dc-correct (gain probe from D26): firmware that records after the patch
(the original firmware, build 1d and older) scales the USB stream with the gain knobs. The
DC offset of the open inputs passes through the same gain, so the ratio of the DC per channel
against raw recordings (--dc-ref, e.g. fx8a in the same session) measures that gain. Every
level of the --dc-correct IDs is corrected by it per channel before the channel mean.

Usage:
  uv run python tools/family_table.py B4-3d-r1 B4-3d-r2 B4-fx3i-r1 … [--ref B4-3d-r1 B4-3d-r2]
                                       [--group B4-3d=B4-3d-r1,B4-3d-r2 …] [--out file.md]
                                       [--dc-ref RAW-r1 RAW-r2 --dc-correct POST-r1 POST-r2]
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


# Gain-Korrektur je Kanal in dB (aus dem DC-Verhältnis), nur für die IDs aus --dc-correct.
DC_GAIN: dict[str, list[float]] = {}


def load(mid: str) -> dict:
    return json.loads((ROOT / "reports" / mid / f"{mid}.json").read_text())


def dc_gain_db(mid: str, ref_dc: list[float]) -> list[float]:
    """Gain der Aufnahme `mid` je Kanal gegen die rohen Referenzaufnahmen, aus dem DC-Offset."""
    dcs = [ch["dc"] for ch in load(mid)["channels"]]
    if len(dcs) != len(ref_dc):
        raise SystemExit(f"{mid}: {len(dcs)} channels, reference has {len(ref_dc)}")
    out = []
    for c, (x, r) in enumerate(zip(dcs, ref_dc), 1):
        if x * r <= 0 or min(abs(x), abs(r)) < 0.005:
            raise SystemExit(f"{mid} channel {c}: DC {x:+.5f} against reference {r:+.5f} is no usable gain probe")
        out.append(20 * math.log10(x / r))
    return out


def levels(mid: str) -> dict[str, float]:
    d = load(mid)
    gain = DC_GAIN.get(mid, [0.0] * len(d["channels"]))
    acc: dict[str, list[float]] = {k: [] for k, _ in COLS}
    for ch, g in zip(d["channels"], gain):
        r = ch["result"]
        acc["rms"].append(r["rms_db"] - g)
        acc["rest"].append(r["rest_rms_db"] - g)
        fam = {f["key"]: f for f in r["families"]}
        for k in ("usb1k", "fs8", "imd"):
            if k in fam and fam[k].get("rms_db") is not None:
                acc[k].append(fam[k]["rms_db"] - g)
    out = {k: pmean(v) for k, v in acc.items() if v}
    fam0 = {f["key"]: f for f in d["channels"][0]["result"]["families"]}
    out["f_comb"] = fam0.get("usb1k", {}).get("f0")
    return out


def mean_of(ids: list[str]) -> dict[str, float]:
    ls = [levels(i) for i in ids]
    # Eine Familie, die die Analyse in einer Aufnahme nicht findet, fehlt dort: Mittel über den Rest.
    return {k: pmean([l[k] for l in ls if k in l]) for k, _ in COLS if any(k in l for l in ls)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="+", help="manifest IDs (reports/<ID>/<ID>.json)")
    ap.add_argument("--ref", nargs="+", help="reference IDs for Δ (mean in power)")
    ap.add_argument("--group", action="append", default=[], help="NAME=ID1,ID2: additional row with the mean")
    ap.add_argument("--out", help="also write the Markdown to this file")
    ap.add_argument("--dc-ref", nargs="+", help="raw recordings (before the patch) whose DC per channel is the reference")
    ap.add_argument("--dc-correct", nargs="+", default=[],
                    help="IDs recorded after the patch: correct their levels by the gain from the DC ratio")
    a = ap.parse_args()
    if bool(a.dc_ref) != bool(a.dc_correct):
        ap.error("--dc-ref and --dc-correct go together")
    gain_notes = []
    if a.dc_ref:
        refs = [[ch["dc"] for ch in load(i)["channels"]] for i in a.dc_ref]
        ref_dc = [sum(v) / len(v) for v in zip(*refs)]
        for i in a.dc_correct:
            DC_GAIN[i] = dc_gain_db(i, ref_dc)
            gain_notes.append(f"{i}: " + " / ".join(f"{g:+.2f}" for g in DC_GAIN[i]) + " dB")
    ref = mean_of(a.ref) if a.ref else None
    head = "| Messung | " + " | ".join(t for _, t in COLS) + " | Kamm-f0 Hz |"
    lines = [head, "|" + "---|" * (len(COLS) + 2)]

    def row(name: str, lv: dict, fc) -> str:
        cells = []
        for k, _ in COLS:
            if k not in lv:
                cells.append("–")  # Familie nicht gefunden
                continue
            c = f"{lv[k]:.2f}"
            if ref and k in ref:
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
    if gain_notes:
        lines.append("")
        lines.append(f"Gain-Korrektur aus dem DC-Verhältnis gegen {', '.join(a.dc_ref)} (Kanal 1 / 2 / 3 / 4, "
                     "abgezogen vor dem Kanalmittel): " + "; ".join(gain_notes) + ".")
    text = "\n".join(lines)
    print(text)
    if a.out:
        Path(a.out).write_text(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
