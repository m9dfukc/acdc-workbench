"""Upload an OWL patch to the AC/DC: run it from RAM or store it in a slot.

Counterpart to the read-only `owl_read.py`. Protocol taken from the OpenWare
source of the running firmware (`Source/MidiHandler.cpp`, `FirmwareLoader.hpp`):

  1. SysEx 0x10 (FIRMWARE_UPLOAD): packet 0 carries the size, packets 1..n the
     data (210 bytes each, 7-bit encoded), the last packet the CRC32.
  2. then either SysEx 0x12 (FIRMWARE_RUN): run from RAM, nothing is stored,
     or SysEx 0x11 + slot (FIRMWARE_STORE): write to the patch flash.

Safety:
  - Only for acdc1 (device UUID is checked first). acdc2 is refused.
  - The tool cannot send erase (0x14), firmware flash (0x13), settings
    store/reset (0x15/0x16), device reset or the bootloader command.
  - --store needs --yes. Slot 1 (the patch that starts at power-on) needs
    --allow-slot1 in addition.
  - An occupied target slot is saved first. If that backup fails, nothing is
    written. With --backup-file FILE the tool takes a local copy instead of a
    download: it must have the size and CRC the device reports for the slot.
  - After a store, name, size and CRC of the slot are read back.
    --download-check also downloads the slot again and compares the bytes.

Downloads while a patch is running are not reliable (messlog D53/D54): the
firmware sends a slot back from the main loop while the audio task also drives
the MIDI transmitter. Bytes can get lost, and once the device stopped sending
MIDI until a power cycle. So prefer --backup-file, and use --download-check
only when you accept that risk. Uploads and the short replies are not affected.
  - After a store the firmware starts the stored slot (RAM only). At the next
    power-on slot 1 starts again. --program-after N switches back.

Input: a raw patch binary (.bin, e.g. OwlProgram `Build/patch.bin`) or a .syx
with upload packets (patch library download, `make sysex`, owl_read.py dump).

Usage (CoreMIDI is not available inside a sandbox, rtmidi needs Python 3.12):
  UV_CACHE_DIR=.uv-cache UV_NO_BUILD=1 uv run --no-project --python 3.12 \
      --with mido --with python-rtmidi python tools/owl_write.py PATCH --run
  ... python tools/owl_write.py PATCH --store 2 --yes
  python3 tools/owl_write.py PATCH --info            (offline, no MIDI needed)
  python3 tools/owl_write.py PATCH --syx-out x.syx   (offline)

Output: <out>/<device>/<YYYYMMDD>/owl_write_<HHMMSS>.json (default out:
out/owl_write). Backups of overwritten slots go to
<backup>/<device>/<YYYYMMDD>/owl_write_<HHMMSS>/ (default backup: backup).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import struct
import sys
import time
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from owl_read import (  # noqa: E402
    KNOWN_DEVICES, MANUFACTURER, OMNI_DEVICE, data_to_sysex, decode_int,
    encode_int, sysex_to_data,
)

SYSEX_FIRMWARE_UPLOAD = 0x10
SYSEX_FIRMWARE_STORE = 0x11
SYSEX_FIRMWARE_RUN = 0x12
SYSEX_PROGRAM_ERROR = 0x30

PATCH_MAGIC = 0xDADAC0DE
CHUNK = 210                      # Datenbytes je Paket (240 SysEx-Bytes), wie FirmwareSender
MAX_PROGRAM_SIZE = 144 * 1024    # MAX_SYSEX_PROGRAM_SIZE (Source/device.h)
MAX_SLOT = 39
MENU_SLOTS = 15                  # das Boot-Menü zeigt die Slots 1..15
# Ladebereiche der AC/DC-Firmware (Hardware/xibeca.ld, PatchDefinition.hpp)
LOAD_REGIONS = {
    0x2000C000: ("PATCHRAM", 80 * 1024),
    0x24000000: ("PLUSRAM", 512 * 1024),
}


# --- Datei lesen ------------------------------------------------------------
def split_sysex(raw: bytes) -> list[bytes]:
    """Datei mit mehreren SysEx-Nachrichten -> Liste ohne F0/F7."""
    out = []
    i = 0
    while i < len(raw):
        if raw[i] != 0xF0:
            raise ValueError(f"byte {i}: expected F0, got {raw[i]:02x}")
        j = raw.index(0xF7, i)
        out.append(raw[i + 1:j])
        i = j + 1
    return out


def syx_to_data(raw: bytes) -> bytes:
    """Upload-Pakete (0x10) einer .syx-Datei -> Patch-Binary, mit Prüfung."""
    pkts = [m for m in split_sysex(raw)
            if len(m) > 3 and m[0] == MANUFACTURER and m[2] == SYSEX_FIRMWARE_UPLOAD]
    if len(pkts) < 3:
        raise ValueError("no upload packets (0x10) in the file")
    if decode_int(pkts[0][3:8]) != 0:
        raise ValueError("first packet does not have index 0")
    size = decode_int(pkts[0][8:13])
    data = bytearray()
    crc = None
    for i, p in enumerate(pkts[1:], start=1):
        if decode_int(p[3:8]) != i:
            raise ValueError(f"packet {i} is out of sequence")
        if len(data) < size:
            data += sysex_to_data(p[8:])
        else:
            crc = decode_int(p[8:13])
    data = bytes(data[:size])
    if len(data) != size:
        raise ValueError(f"file is incomplete: {len(data)} of {size} bytes")
    if crc is None or crc != zlib.crc32(data):
        raise ValueError("checksum in the file does not match the data")
    return data


def load_patch(path: Path) -> bytes:
    raw = path.read_bytes()
    if raw[:1] == b"\xf0":
        return syx_to_data(raw)
    return raw


def describe(data: bytes) -> dict:
    """ProgramHeader lesen (Source/ProgramHeader.h) und gegen die Firmware prüfen."""
    if len(data) < 52:
        raise ValueError("too short for a patch")
    magic, link, end, jump, _sb, _se, _pv = struct.unpack("<7I", data[:28])
    name = data[28:52].split(b"\0")[0].decode("latin-1")
    info = {
        "name": name, "size": len(data), "crc": f"0x{zlib.crc32(data):08x}",
        "magic": f"0x{magic:08x}", "link": f"0x{link:08x}", "end": f"0x{end:08x}",
        "program_size": end - link, "problems": [],
    }
    if magic != PATCH_MAGIC:
        info["problems"].append(f"magic is {magic:#010x}, not {PATCH_MAGIC:#010x}: not an OWL patch")
        return info
    region = LOAD_REGIONS.get(link)
    if region is None:
        info["problems"].append(f"link address {link:#010x} is not a patch region of the AC/DC firmware "
                                f"({', '.join(f'{a:#010x} {n}' for a, (n, _) in LOAD_REGIONS.items())})")
    else:
        info["region"] = region[0]
        if end - link > region[1]:
            info["problems"].append(f"program needs {end - link} B, {region[0]} has {region[1]} B")
    if len(data) > MAX_PROGRAM_SIZE:
        info["problems"].append(f"binary has {len(data)} B, the firmware stores at most {MAX_PROGRAM_SIZE} B")
    if not name:
        info["problems"].append("empty patch name")
    return info


# --- Pakete bauen -----------------------------------------------------------
def build_packets(data: bytes) -> list[bytes]:
    """Upload-Pakete ohne F0/F7. Bytegleich mit FirmwareSender bzw. der Library-.syx."""
    head = bytes([MANUFACTURER, OMNI_DEVICE, SYSEX_FIRMWARE_UPLOAD])
    pkts = [head + encode_int(0) + encode_int(len(data))]
    idx = 1
    for off in range(0, len(data), CHUNK):
        pkts.append(head + encode_int(idx) + data_to_sysex(data[off:off + CHUNK]))
        idx += 1
    pkts.append(head + encode_int(idx) + encode_int(zlib.crc32(data)))
    return pkts


def packets_to_syx(pkts: list[bytes]) -> bytes:
    return b"".join(b"\xf0" + p + b"\xf7" for p in pkts)


# --- Gerät ------------------------------------------------------------------
def owl_errors(msgs) -> list[str]:
    out = []
    for m in msgs:
        if m.type == "sysex" and len(m.data) > 3 and m.data[0] == MANUFACTURER \
                and m.data[2] == SYSEX_PROGRAM_ERROR:
            out.append(bytes(m.data[3:]).decode("latin-1"))
    return out


def patch_names(owl) -> dict[int, dict]:
    from owl_read import parse
    return {e["index"]: e for e in parse(owl.request(0x01, quiet=1.0))
            if e.get("cmd") == "PRESET_NAME"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("patch", type=Path, help="patch binary (.bin) or SysEx file (.syx)")
    act = ap.add_mutually_exclusive_group(required=True)
    act.add_argument("--info", action="store_true", help="only check and describe the file (offline)")
    act.add_argument("--syx-out", type=Path, help="only write the upload packets as .syx (offline)")
    act.add_argument("--run", action="store_true", help="upload and run from RAM, nothing is stored")
    act.add_argument("--store", type=int, metavar="SLOT", help="upload and store in this slot (needs --yes)")
    ap.add_argument("--yes", action="store_true", help="confirmation for --store")
    ap.add_argument("--allow-slot1", action="store_true", help="allow --store 1 (the power-on patch)")
    ap.add_argument("--program-after", type=int, metavar="SLOT",
                    help="after a store, send a Program Change to this slot (RAM only)")
    ap.add_argument("--download-check", action="store_true",
                    help="after a store, download the slot and compare the bytes (not reliable while a patch runs)")
    ap.add_argument("--backup-file", type=Path, metavar="FILE",
                    help="local copy (.bin or .syx) of the patch in the target slot, used instead of a download "
                         "if its size and CRC match the slot")
    ap.add_argument("--port", default="OWL-ACDC", help="MIDI port name (substring)")
    ap.add_argument("--delay", type=float, default=0.01, help="pause between upload packets in seconds")
    ap.add_argument("--out", type=Path, default=Path("out/owl_write"), help="base folder for the log")
    ap.add_argument("--backup", type=Path, default=Path("backup"), help="base folder for slot backups")
    args = ap.parse_args(argv)

    try:
        data = load_patch(args.patch)
        info = describe(data)
    except (OSError, ValueError) as e:
        print(f"Cannot read {args.patch}: {e}", file=sys.stderr)
        return 2
    print(f"Patch: {info['name']!r}, {info['size']} B, CRC {info['crc']}, "
          f"link {info['link']} ({info.get('region', '?')}), program size {info['program_size']} B")
    for p in info["problems"]:
        print(f"  problem: {p}", file=sys.stderr)
    pkts = build_packets(data)
    if args.info:
        print(f"Upload: {len(pkts)} packets")
        return 1 if info["problems"] else 0
    if info["problems"]:
        print("Aborted: the file is not a patch this firmware can load.", file=sys.stderr)
        return 2
    if args.syx_out:
        args.syx_out.write_bytes(packets_to_syx(pkts))
        print(f"Wrote {args.syx_out} ({len(pkts)} packets)")
        return 0

    if args.store is not None:
        if not args.yes:
            print("--store needs --yes", file=sys.stderr)
            return 4
        if not (1 <= args.store <= MAX_SLOT):
            print(f"Invalid slot {args.store} (1..{MAX_SLOT})", file=sys.stderr)
            return 2
        if args.store == 1 and not args.allow_slot1:
            print("Slot 1 is the power-on patch: --store 1 needs --allow-slot1", file=sys.stderr)
            return 4
        if args.store > MENU_SLOTS:
            print(f"Note: the boot menu only reaches slots 1..{MENU_SLOTS}.")

    import mido
    from owl_read import Owl, parse, reassemble

    ins = [n for n in mido.get_input_names() if args.port in n]
    outs = [n for n in mido.get_output_names() if args.port in n]
    if len(ins) != 1 or len(outs) != 1:
        print(f"MIDI port not found or ambiguous: in={ins} out={outs}", file=sys.stderr)
        return 2
    owl = Owl(ins[0])
    now = dt.datetime.now()
    log: dict = {"time": now.isoformat(timespec="seconds"), "port": ins[0], "file": str(args.patch),
                 "patch": info, "action": "run" if args.run else f"store {args.store}", "steps": []}
    rc = 0
    try:
        dev = parse(owl.request(0x21))
        uuid = next((e["text"] for e in dev if e.get("cmd") == "DEVICE_ID"), None)
        name = KNOWN_DEVICES.get(uuid or "", "unknown")
        log.update(device_id=uuid, device=name)
        print(f"Device: {name} ({uuid})")
        if name != "acdc1":
            print(f"Aborted: writing is only allowed for acdc1, connected device is {name}", file=sys.stderr)
            return 5
        fw = next((e["text"] for e in parse(owl.request(0x20)) if e.get("cmd") == "FIRMWARE_VERSION"), None)
        log["firmware"] = fw
        before = patch_names(owl)
        log["slots_before"] = {k: {"name": v["name"], "size": v["size"], "crc": v["crc"]}
                               for k, v in sorted(before.items())}
        print("Slots before: " + ", ".join(f"{k}={v['name']!r}" for k, v in sorted(before.items()) if k))

        # Belegten Ziel-Slot vorher sichern
        if args.store is not None and args.store in before:
            old = before[args.store]
            if old["size"] == len(data) and old["crc"] == info["crc"]:
                print(f"Slot {args.store} already holds this patch ({old['name']!r}, same size and CRC). Nothing to do.")
                log["steps"].append("identical, nothing written")
                return 0
            bdir = args.backup / name / now.strftime("%Y%m%d") / now.strftime("owl_write_%H%M%S")
            safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in old["name"])
            base = bdir / f"slot{args.store:02d}_{safe}"
            if args.backup_file is not None:
                # lokale Kopie statt Download: muss genau der Inhalt des Slots sein
                try:
                    copy = load_patch(args.backup_file)
                except (OSError, ValueError) as e:
                    print(f"Aborted: cannot read --backup-file {args.backup_file}: {e}. Nothing was written.",
                          file=sys.stderr)
                    return 6
                crc = f"0x{zlib.crc32(copy):08x}"
                if len(copy) != old["size"] or crc != old["crc"]:
                    print(f"Aborted: --backup-file has {len(copy)} B, CRC {crc}; slot {args.store} holds "
                          f"{old['size']} B, CRC {old['crc']}. Nothing was written.", file=sys.stderr)
                    return 6
                bdir.mkdir(parents=True, exist_ok=False)
                base.with_suffix(".bin").write_bytes(copy)
                log["backup"] = {"slot": args.store, "name": old["name"], "size": len(copy), "crc": crc,
                                 "source": str(args.backup_file), "files": [str(base.with_suffix(".bin"))]}
                print(f"Backup of slot {args.store} ({old['name']!r}, {len(copy)} B) from {args.backup_file}: "
                      f"{base.with_suffix('.bin')}")
            else:
                res = reassemble(owl.download(args.store))
                if not res.get("ok"):
                    detail = {k: res.get(k) for k in ("error", "packets", "size", "received", "crc_device", "crc_zlib")}
                    log["steps"].append({"backup_failed": detail})
                    print(f"Aborted: backup of slot {args.store} failed ({detail}). Nothing was written. "
                          "A local copy with the same size and CRC can stand in: --backup-file FILE.",
                          file=sys.stderr)
                    return 6
                bdir.mkdir(parents=True, exist_ok=False)
                base.with_suffix(".bin").write_bytes(res["data"])
                with open(base.with_suffix(".syx"), "wb") as f:
                    for m in res["sysex"]:
                        f.write(bytes(m.bin()))
                log["backup"] = {"slot": args.store, "name": old["name"], "size": res["size"],
                                 "crc": res["crc_zlib"], "files": [str(base.with_suffix(".bin")),
                                                                   str(base.with_suffix(".syx"))]}
                print(f"Backup of slot {args.store} ({old['name']!r}, {res['size']} B): {base.with_suffix('.bin')}")

        # Hochladen
        owl.drain()
        errors: list[str] = []
        t0 = time.monotonic()
        for i, p in enumerate(pkts):
            owl.out.send(mido.Message("sysex", data=list(p)))
            time.sleep(args.delay)
            errors += owl_errors(owl.inp.iter_pending())
            if errors:
                break
        errors += owl_errors(owl.collect(quiet=0.3, timeout=2.0))
        log["steps"].append({"upload_packets": len(pkts), "sent": i + 1,
                             "seconds": round(time.monotonic() - t0, 2), "errors": errors})
        if errors:
            print(f"Aborted: the device reported an error during the upload: {errors}. "
                  "Nothing was run or stored.", file=sys.stderr)
            return 7
        print(f"Upload ok: {len(pkts)} packets in {time.monotonic() - t0:.1f} s")

        head = [MANUFACTURER, OMNI_DEVICE]
        if args.run:
            owl.out.send(mido.Message("sysex", data=head + [SYSEX_FIRMWARE_RUN]))
            errors = owl_errors(owl.collect(quiet=1.0, timeout=5.0))
            running = patch_names(owl).get(0, {})
            log["steps"].append({"run": True, "errors": errors, "running": running.get("name")})
            if errors:
                print(f"The device reported: {errors}", file=sys.stderr)
                rc = 7
            print(f"Now running from RAM: {running.get('name')!r}. Nothing was stored, "
                  "a power cycle brings back the stored patch.")
        else:
            owl.out.send(mido.Message("sysex", data=head + [SYSEX_FIRMWARE_STORE, *encode_int(args.store)]))
            errors = []
            got = None
            t0 = time.monotonic()
            while time.monotonic() - t0 < 30.0:
                errors += owl_errors(owl.collect(quiet=0.5, timeout=2.0))
                got = patch_names(owl).get(args.store)
                if got and got["size"] == len(data) and got["crc"] == info["crc"]:
                    break
                if errors:
                    break
            ok = bool(got) and got["size"] == len(data) and got["crc"] == info["crc"] and not errors
            log["steps"].append({"store": args.store, "errors": errors, "seconds": round(time.monotonic() - t0, 2),
                                 "slot_after": None if not got else
                                 {"name": got["name"], "size": got["size"], "crc": got["crc"]}})
            if not ok:
                print(f"Store FAILED: slot {args.store} reads back as {got}, errors {errors}", file=sys.stderr)
                rc = 8
            else:
                print(f"Stored in slot {args.store}: {got['name']!r}, {got['size']} B, CRC {got['crc']}")
                if args.download_check:
                    res = reassemble(owl.download(args.store))
                    same = res.get("ok") and res.get("data") == data
                    log["steps"].append({"download_check": bool(same)})
                    if same:
                        print("Download check ok: the slot is byte-identical with the file.")
                    else:
                        print(f"Download check FAILED: {res.get('error', 'data differs')}", file=sys.stderr)
                        rc = 8
            if args.program_after is not None and rc == 0:
                after = patch_names(owl)
                if args.program_after in after and args.program_after >= 1:
                    owl.program_change(args.program_after)
                    time.sleep(1.0)
                    running = patch_names(owl).get(0, {})
                    log["steps"].append({"program_after": args.program_after, "running": running.get("name")})
                    print(f"Program Change -> slot {args.program_after}, now running: {running.get('name')!r}")
                else:
                    print(f"Slot {args.program_after} is empty, no Program Change sent", file=sys.stderr)
        after = patch_names(owl)
        log["slots_after"] = {k: {"name": v["name"], "size": v["size"], "crc": v["crc"]}
                              for k, v in sorted(after.items())}
    finally:
        owl.close()
        if log.get("device"):
            odir = args.out / log["device"] / now.strftime("%Y%m%d")
            odir.mkdir(parents=True, exist_ok=True)
            lf = odir / now.strftime("owl_write_%H%M%S.json")
            lf.write_text(json.dumps(log, indent=2, ensure_ascii=False))
            print(f"Log: {lf}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
