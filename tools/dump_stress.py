"""Stress test for slot downloads over MIDI (D53/D54: race in the MIDI send path).

Downloads the stored slots again and again while a patch is running and counts
how many downloads arrive damaged. Read-only apart from the optional Program
Change (RAM only, not stored). Only acdc1 is accepted.

Each download is checked against the size and CRC from the slot list:
  ok          complete, in order, CRC matches
  order       a packet carries the wrong index (duplicate or reordered data)
  incomplete  bytes or the final CRC packet are missing
  crc         complete and in order, but the data is wrong
  silent      no answer at all

If the device stops answering (the MIDI hang from D53), the run ends there.
Then only a power cycle helps.

Usage (outside the sandbox, CoreMIDI):
  UV_CACHE_DIR=.uv-cache UV_NO_BUILD=1 uv run --no-project --python 3.12 \
      --with mido --with python-rtmidi python tools/dump_stress.py \
      --name D62-fx4b-slot2 --run-slot 2 --restore-slot 1 --rounds 20

Output: out/<name>-session-table.md and out/dump_stress/<name>.json
(nothing is overwritten, an existing name gets the time of day appended).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import owl_read  # noqa: E402
from owl_read import MANUFACTURER, decode_int, parse, sysex_to_data  # noqa: E402


def classify(msgs, size_expected: int | None, crc_expected: int | None) -> dict:
    """Ein Download: Pakete zählen, Reihenfolge, Länge und CRC prüfen."""
    pkts = [bytes(m.data) for m in msgs if m.type == "sysex" and len(m.data) > 3
            and m.data[0] == MANUFACTURER and m.data[2] == 0x10]
    other = len(msgs) - len(pkts)
    if not pkts:
        return {"result": "silent", "packets": 0, "other_messages": other}
    r: dict = {"packets": len(pkts), "other_messages": other}
    idx = [decode_int(p[3:8]) if len(p) >= 8 else -1 for p in pkts]
    r["first_index"] = idx[0]
    size = decode_int(pkts[0][8:13]) if idx[0] == 0 and len(pkts[0]) >= 13 else None
    r["size_announced"] = size
    wrong = [(i, v) for i, v in enumerate(idx) if v != i]
    r["index_errors"] = len(wrong)
    if wrong:
        r["first_index_error"] = {"position": wrong[0][0], "index": wrong[0][1]}
    size_ref = size_expected if size_expected is not None else size
    data = bytearray()
    crc_dev = None
    if size_ref is not None:
        for p in pkts[1:]:
            if len(data) < size_ref:
                data += sysex_to_data(p[8:])
            elif len(p) >= 13:
                crc_dev = decode_int(p[8:13])
        r["received"] = min(len(data), size_ref)
        r["missing"] = size_ref - r["received"]
        data = bytes(data[:size_ref])
        r["crc_data"] = f"0x{zlib.crc32(data):08x}"
    r["crc_device"] = None if crc_dev is None else f"0x{crc_dev:08x}"
    crc_ref = crc_expected if crc_expected is not None else crc_dev
    if wrong:
        r["result"] = "order"
    elif size_ref is None or r["missing"] or crc_dev is None:
        r["result"] = "incomplete"
    elif zlib.crc32(data) != crc_ref or (size is not None and size != size_ref):
        r["result"] = "crc"
    else:
        r["result"] = "ok"
    return r


def text_of(entries, cmd):
    return next((e.get("text") for e in entries if e.get("cmd") == cmd), None)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True, help="name of the series, e.g. D62-fx4b-slot2")
    ap.add_argument("--port", default="OWL-ACDC", help="MIDI port name (substring)")
    ap.add_argument("--rounds", type=int, default=20, help="rounds over all slots (default 20)")
    ap.add_argument("--slots", type=int, nargs="*", help="slots to download (default: all occupied patch slots)")
    ap.add_argument("--run-slot", type=int, help="Program Change to this slot before the test (RAM only)")
    ap.add_argument("--restore-slot", type=int, help="Program Change to this slot after the test")
    ap.add_argument("--quiet", type=float, default=0.6, help="seconds of silence that end one download (default 0.6)")
    ap.add_argument("--out", type=Path, default=Path("out"), help="base folder (default out)")
    args = ap.parse_args(argv)

    mido = owl_read.mido
    if mido is None:
        print("mido is missing (see usage in the module docstring)", file=sys.stderr)
        return 2
    ins = [n for n in mido.get_input_names() if args.port in n]
    outs = [n for n in mido.get_output_names() if args.port in n]
    if len(ins) != 1 or len(outs) != 1:
        print(f"MIDI port not found or ambiguous: in={ins} out={outs}", file=sys.stderr)
        return 2

    table = args.out / f"{args.name}-session-table.md"
    js = args.out / "dump_stress" / f"{args.name}.json"
    if table.exists() or js.exists():
        suffix = dt.datetime.now().strftime("_%H%M%S")
        table = table.with_name(f"{args.name}{suffix}-session-table.md")
        js = js.with_name(f"{args.name}{suffix}.json")
    js.parent.mkdir(parents=True, exist_ok=True)

    owl = owl_read.Owl(ins[0])
    rep: dict = {"name": args.name, "time": dt.datetime.now().isoformat(timespec="seconds"),
                 "rounds": args.rounds, "downloads": [], "hang": False}
    rc = 0
    try:
        uuid = text_of(parse(owl.request(0x21)), "DEVICE_ID")
        device = owl_read.KNOWN_DEVICES.get(uuid or "", "unknown")
        rep.update(device=device, device_id=uuid)
        print(f"Device: {device} ({uuid})")
        if device != "acdc1":
            print("Aborted: this test is only allowed for acdc1", file=sys.stderr)
            return 5
        rep["firmware"] = text_of(parse(owl.request(0x20)), "FIRMWARE_VERSION")
        names = {e["index"]: e for e in parse(owl.request(0x01, quiet=1.0)) if e.get("cmd") == "PRESET_NAME"}
        slots = args.slots or sorted(i for i in names if i >= 1)
        for s in slots:
            if s not in names:
                print(f"Slot {s} is empty", file=sys.stderr)
                return 3
        if args.run_slot is not None:
            if args.run_slot not in names or args.run_slot < 1:
                print(f"Slot {args.run_slot} is empty", file=sys.stderr)
                return 3
            owl.program_change(args.run_slot)
            time.sleep(1.5)
        running = next((e for e in parse(owl.request(0x01, quiet=1.0)) if e.get("index") == 0), None)
        rep["running"] = running and running.get("name")
        rep["stats_before"] = text_of(parse(owl.request(0x24)), "PROGRAM_STATS")
        print(f"Firmware: {rep['firmware']}  running: {rep['running']}  {rep['stats_before']}")

        for rnd in range(1, args.rounds + 1):
            line = []
            for s in slots:
                t0 = time.monotonic()
                msgs = owl.download(s, quiet=args.quiet, timeout=30.0)
                r = classify(msgs, names[s].get("size"), int(names[s]["crc"], 16))
                r.update(round=rnd, slot=s, seconds=round(time.monotonic() - t0 - args.quiet, 2))
                rep["downloads"].append(r)
                line.append(f"{s}:{r['result']}")
                if r["result"] != "ok":
                    # antwortet das Gerät noch? (Hänger aus D53)
                    time.sleep(1.0)
                    if not owl.request(0x21, quiet=0.6, timeout=3.0):
                        rep["hang"] = True
                        break
            print(f"Round {rnd:2d}: " + "  ".join(line))
            if rep["hang"]:
                print("Device no longer answers on MIDI (hang as in D53). Power cycle needed.", file=sys.stderr)
                rc = 6
                break

        if not rep["hang"]:
            rep["stats_after"] = text_of(parse(owl.request(0x24)), "PROGRAM_STATS")
            info = parse(owl.request(127, quiet=1.0))
            rep["program_message"] = text_of(info, "PROGRAM_MESSAGE")
            rep["program_error"] = text_of(info, "PROGRAM_ERROR")
            if args.restore_slot is not None and args.restore_slot in names:
                owl.program_change(args.restore_slot)
                time.sleep(1.0)
                run = next((e for e in parse(owl.request(0x01, quiet=1.0)) if e.get("index") == 0), None)
                rep["running_after"] = run and run.get("name")
    finally:
        owl.close()

    # Auswertung (Dateien deutsch)
    kinds = ["ok", "order", "incomplete", "crc", "silent"]
    dl = rep["downloads"]
    per_slot: dict[int, dict] = {}
    for r in dl:
        c = per_slot.setdefault(r["slot"], dict.fromkeys(kinds, 0))
        c[r["result"]] += 1
    total = dict.fromkeys(kinds, 0)
    for c in per_slot.values():
        for k in kinds:
            total[k] += c[k]
    rep["summary"] = {"downloads": len(dl), **total, "damaged": len(dl) - total["ok"]}
    js.write_text(json.dumps(rep, indent=2, ensure_ascii=False))

    head = {"ok": "in Ordnung", "order": "Reihenfolge", "incomplete": "unvollständig",
            "crc": "CRC falsch", "silent": "keine Antwort"}
    out = [f"# Download-Stresstest {args.name}", "",
           f"- Zeit: {rep['time']}, Gerät: {rep.get('device')}, Firmware: {rep.get('firmware')}",
           f"- Laufender Patch: {rep.get('running')} ({rep.get('stats_before')})",
           f"- Runden: {args.rounds}, Downloads: {len(dl)}, **beschädigt: {len(dl) - total['ok']}**"
           + (", **Gerät antwortet nicht mehr auf MIDI (Hänger)**" if rep["hang"] else ""),
           f"- Geräte-Meldung danach: {rep.get('program_message')}", "",
           "| Slot | Patch | Größe B | " + " | ".join(head[k] for k in kinds) + " |",
           "|---|---|---|" + "---|" * len(kinds)]
    for s in sorted(per_slot):
        c = per_slot[s]
        out.append(f"| {s} | {names[s]['name']} | {names[s].get('size')} | " + " | ".join(str(c[k]) for k in kinds) + " |")
    out.append("| Summe | | | " + " | ".join(str(total[k]) for k in kinds) + " |")
    bad = [r for r in dl if r["result"] != "ok"]
    if bad:
        out += ["", "## Beschädigte Downloads", "",
                "| Runde | Slot | Ergebnis | Pakete | fehlende B | Indexfehler | erster Indexfehler |", "|---|---|---|---|---|---|---|"]
        for r in bad:
            fe = r.get("first_index_error")
            out.append(f"| {r['round']} | {r['slot']} | {head[r['result']]} | {r['packets']} | {r.get('missing', '')} | "
                       f"{r.get('index_errors', '')} | {'Paket %d trägt Index %d' % (fe['position'], fe['index']) if fe else ''} |")
    table.write_text("\n".join(out) + "\n")
    print(f"Downloads: {len(dl)}  damaged: {len(dl) - total['ok']}  " + "  ".join(f"{k}={total[k]}" for k in kinds))
    print(f"Table: {table}\nJSON:  {js}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
