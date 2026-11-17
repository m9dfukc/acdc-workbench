"""Read-only OWL/OpenWare SysEx tool for the AC/DC.

Queries device info, patch and resource names and settings, and downloads stored
slots/resources (e.g. __SETTINGS__) as .syx. Protocol taken from
OpenWare v22.5.0 (`Source/MidiHandler.cpp`, `MidiController.cpp`,
`OpenWareMidiControl.h`).

Safety: the tool can only send
  - CC67 (REQUEST_SETTINGS) with the values in ALLOWED_REQUESTS and
  - SysEx 0x18 (SYSEX_FIRMWARE_SEND, "send slot back") with slot >= 1
  - optionally (--program N) a MIDI Program Change to an occupied slot.
Program Change sets `settings.program_index` in RAM only
(ProgramManager.cpp:730); it is stored only by SysEx 0x16. After a
power cycle the stored slot runs again.
  - optionally (--reset-to-dfu --yes) SysEx 0x7E: restart into the ST ROM DFU
    bootloader (`device_dfu()`, like "Reset to bootloader" on openwarelab).
    Erases nothing. To get back: power-cycle the case. Store, erase, settings store/reset, reset, bootloader,
CC7 (volume), CC26 etc. cannot be reached.

Usage (rtmidi has no wheel for Python 3.14, CoreMIDI is not available inside a sandbox):
  UV_CACHE_DIR=.uv-cache UV_NO_BUILD=1 uv run --no-project --python 3.12 \
      --with mido --with python-rtmidi python tools/owl_read.py [--out DIR] [--dump]

Output: <out>/<device>/<YYYYMMDD>/device_report.json (default out: out/owl_read). With --dump
the report and the slots go to <out>/<device>/<YYYYMMDD>/owl/, so for a backup use `--out backup --dump`
→ backup/acdc1/<date>/owl/. If the target folder is not empty, nothing is overwritten: the folder
name gets the time of day appended (e.g. 20261114_231500 or owl_231500).
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

try:
    import mido
except ImportError:  # die Offline-Modi von owl_write.py brauchen kein MIDI
    mido = None

MANUFACTURER = 0x7D
OMNI_DEVICE = 0x52
REQUEST_SETTINGS = 67

ALLOWED_REQUESTS = {
    127: "device info (firmware, bootloader, program message, stats, status)",
    0x01: "patch names",
    0x03: "settings",
    0x04: "resource names",
    0x20: "firmware version",
    0x21: "device id",
    0x23: "device stats",
    0x24: "program stats",
    0x25: "bootloader version",
}
SYSEX_FIRMWARE_SEND = 0x18
MAX_NUMBER_OF_PATCHES = 40

CMD_NAMES = {
    0x01: "PRESET_NAME", 0x02: "PARAMETER_NAME", 0x03: "CONFIGURATION",
    0x04: "RESOURCE_NAME", 0x10: "FIRMWARE_UPLOAD", 0x20: "FIRMWARE_VERSION",
    0x21: "DEVICE_ID", 0x22: "PROGRAM_MESSAGE", 0x23: "DEVICE_STATS",
    0x24: "PROGRAM_STATS", 0x25: "BOOTLOADER_VERSION", 0x30: "PROGRAM_ERROR",
}

KNOWN_DEVICES = {
    "0039001c:31315101:39333437": "acdc1",
    "00250049:31315102:39333437": "acdc2",
}

CONFIG_KEYS = {
    "FS": "audio_samplingrate", "BD": "audio_bitdepth", "DF": "audio_dataformat",
    "BS": "audio_blocksize", "BY": "audio_codec_bypass", "SW": "audio_codec_swaplr",
    "PC": "program_change_button", "BL": "bootloader_lock",
    "IO": "input_offset", "IS": "input_scalar", "OO": "output_offset", "OS": "output_scalar",
}


# --- 7-bit encoding (Source/sysex.c) ---------------------------------------
def sysex_to_data(sx: bytes) -> bytes:
    out = bytearray()
    bits = 0
    for i, b in enumerate(sx):
        if i % 8 == 0:
            bits = b
        else:
            out.append(b | ((bits & 1) << 7))
            bits >>= 1
    return bytes(out)


def data_to_sysex(data: bytes) -> bytes:
    out = bytearray()
    for i in range(0, len(data), 7):
        chunk = data[i:i + 7]
        msb = 0
        for j, c in enumerate(chunk):
            msb |= (c >> 7) << j
        out.append(msb)
        out.extend(c & 0x7F for c in chunk)
    return bytes(out)


def decode_int(sx5: bytes) -> int:
    return int.from_bytes(sysex_to_data(sx5)[:4], "big")


def encode_int(v: int) -> bytes:
    return data_to_sysex(v.to_bytes(4, "big"))


# --- Nur zur Info: Brown-Tabelle mit Startwert 0. Das Gerät meldet in der
# Praxis Standard-CRC32 (zlib), gemessen an acdc1 2026-11-14. ---------------
_TABLE = []
for n in range(256):
    c = n
    for _ in range(8):
        c = (c >> 1) ^ 0xEDB88320 if c & 1 else c >> 1
    _TABLE.append(c)


def owl_crc32(data: bytes, crc: int = 0) -> int:
    for b in data:
        crc = _TABLE[(crc ^ b) & 0xFF] ^ (crc >> 8)
    return crc


# --- Settings-Struct (Source/ApplicationSettings.h, AC/DC ohne DIGITALBUS) --
SETTINGS_FMT = "<IIBBHBB??B?2xIIIIBB2x"  # 40 Byte


def decode_settings(raw: bytes) -> dict:
    size = struct.calcsize(SETTINGS_FMT)
    if len(raw) < size:
        return {"error": f"zu kurz ({len(raw)} < {size})", "hex": raw.hex()}
    f = struct.unpack(SETTINGS_FMT, raw[:size])
    names = ["checksum", "audio_samplingrate", "audio_bitdepth", "audio_dataformat",
             "audio_blocksize", "audio_input_gain", "audio_output_gain",
             "audio_codec_swaplr", "audio_codec_bypass", "program_index",
             "program_change_button", "input_offset", "input_scalar",
             "output_offset", "output_scalar", "midi_input_channel",
             "midi_output_channel"]
    d = dict(zip(names, f))
    d["checksum_hex"] = f"0x{d['checksum']:08x}"
    d["checksum_expected_v22.5.0"] = f"0x{size ^ 0xF0F0F0F0:08x}"
    d["checksum_ok"] = d["checksum"] == (size ^ 0xF0F0F0F0)
    d["raw_len"] = len(raw)
    d["raw_hex"] = raw.hex()
    return d


# --- MIDI -------------------------------------------------------------------
class Owl:
    def __init__(self, port_name: str):
        self.inp = mido.open_input(port_name)
        self.out = mido.open_output(port_name)
        self.log: list[dict] = []

    def close(self):
        self.inp.close()
        self.out.close()

    def drain(self):
        for _ in self.inp.iter_pending():
            pass

    def collect(self, quiet: float, timeout: float) -> list[mido.Message]:
        msgs: list[mido.Message] = []
        t0 = last = time.monotonic()
        while True:
            m = self.inp.poll()
            now = time.monotonic()
            if m is not None:
                msgs.append(m)
                last = now
                continue
            if now - last > quiet or now - t0 > timeout:
                return msgs
            time.sleep(0.002)

    def program_change(self, slot: int):
        if not (1 <= slot < MAX_NUMBER_OF_PATCHES):
            raise ValueError(f"invalid slot {slot}")
        self.out.send(mido.Message("program_change", channel=0, program=slot))

    def reset_to_dfu(self):
        self.out.send(mido.Message("sysex", data=[MANUFACTURER, OMNI_DEVICE, 0x7E]))

    def request(self, value: int, quiet=0.6, timeout=5.0) -> list[mido.Message]:
        if value not in ALLOWED_REQUESTS:
            raise ValueError(f"CC67={value} not allowed")
        self.drain()
        self.out.send(mido.Message("control_change", channel=0,
                                   control=REQUEST_SETTINGS, value=value))
        return self.collect(quiet, timeout)

    def download(self, slot: int, quiet=1.5, timeout=60.0) -> list[mido.Message]:
        if not (1 <= slot < MAX_NUMBER_OF_PATCHES + 12):
            raise ValueError(f"invalid slot {slot}")
        self.drain()
        self.out.send(mido.Message("sysex", data=[MANUFACTURER, OMNI_DEVICE,
                                                  SYSEX_FIRMWARE_SEND, *encode_int(slot)]))
        return self.collect(quiet, timeout)


def parse(msgs: list[mido.Message]) -> list[dict]:
    out = []
    for m in msgs:
        if m.type != "sysex":
            out.append({"type": m.type, **{k: v for k, v in m.dict().items()
                                            if k not in ("type", "time")}})
            continue
        d = bytes(m.data)
        if len(d) < 3 or d[0] != MANUFACTURER:
            out.append({"type": "sysex_foreign", "hex": d.hex()})
            continue
        cmd, p = d[2], d[3:]
        e: dict = {"type": "owl", "cmd": CMD_NAMES.get(cmd, hex(cmd))}
        if cmd in (0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x30):
            e["text"] = p.decode("latin-1")
        elif cmd == 0x03:
            s = p.decode("latin-1")
            key, val = s[:2], s[2:]
            e["key"] = key
            e["name"] = CONFIG_KEYS.get(key, key)
            e["value_hex"] = val
            try:
                e["value"] = int(val, 16)
            except ValueError:
                pass
        elif cmd in (0x01, 0x04):
            idx = p[0]
            z = p.index(0, 1)
            e.update(index=idx, name=p[1:z].decode("latin-1"),
                     size=decode_int(p[z + 1:z + 6]), crc=f"0x{decode_int(p[z + 6:z + 11]):08x}")
        elif cmd == 0x10:
            e["packet"] = decode_int(p[:5])
            e["payload_len"] = len(p) - 5
        else:
            e["hex"] = p.hex()
        out.append(e)
    return out


def reassemble(msgs: list[mido.Message]) -> dict:
    """0x10-Pakete -> Daten, Größe, CRC-Prüfung."""
    pkts = [bytes(m.data) for m in msgs if m.type == "sysex" and len(m.data) > 3
            and m.data[0] == MANUFACTURER and m.data[2] == 0x10]
    if not pkts:
        return {"ok": False, "error": "keine 0x10-Pakete", "packets": 0}
    size = decode_int(pkts[0][8:13])
    data = bytearray()
    crc_dev = None
    for i, p in enumerate(pkts[1:], start=1):
        idx = decode_int(p[3:8])
        if idx != i:
            return {"ok": False, "error": f"Paket {i} hat Index {idx}", "packets": len(pkts)}
        if len(data) < size:
            data += sysex_to_data(p[8:])
        else:
            crc_dev = decode_int(p[8:13])
    data = bytes(data[:size])
    crc_owl = owl_crc32(data)
    return {
        "ok": len(data) == size and crc_dev is not None and crc_dev == zlib.crc32(data),
        "packets": len(pkts), "size": size, "received": len(data),
        "crc_device": None if crc_dev is None else f"0x{crc_dev:08x}",
        "crc_owl": f"0x{crc_owl:08x}", "crc_zlib": f"0x{zlib.crc32(data):08x}",
        "data": data, "sysex": [m for m in msgs if m.type == "sysex"],
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", default="OWL-ACDC", help="MIDI port name (substring)")
    ap.add_argument("--out", type=Path, default=Path("out/owl_read"), help="base folder (for a backup: backup)")
    ap.add_argument("--dump", action="store_true", help="download all slots and resources")
    ap.add_argument("--slots", type=int, nargs="*", help="download only these slots (1..39, resources 40+n)")
    ap.add_argument("--reset-to-dfu", action="store_true", help="restart into the ROM DFU bootloader (needs --yes)")
    ap.add_argument("--yes", action="store_true", help="confirmation for --reset-to-dfu")
    ap.add_argument("--program", type=int, help="only send a Program Change to this slot (RAM, not stored), then exit")
    args = ap.parse_args(argv)

    ins = [n for n in mido.get_input_names() if args.port in n]
    outs = [n for n in mido.get_output_names() if args.port in n]
    if len(ins) != 1 or len(outs) != 1:
        print(f"MIDI port not found or ambiguous: in={ins} out={outs}", file=sys.stderr)
        return 2
    owl = Owl(ins[0])
    try:
        report: dict = {"port": ins[0], "time": dt.datetime.now().isoformat(timespec="seconds")}
        dev = parse(owl.request(0x21))
        uuid = next((e["text"] for e in dev if e.get("cmd") == "DEVICE_ID"), None)
        name = KNOWN_DEVICES.get(uuid or "", "unknown")
        report.update(device_id=uuid, device=name)
        print(f"Device: {name} ({uuid})")
        if args.reset_to_dfu:
            if not args.yes:
                print("--reset-to-dfu needs --yes", file=sys.stderr)
                return 4
            if name != "acdc1":
                print(f"Aborted: DFU reset is only allowed for acdc1, connected device is {name}", file=sys.stderr)
                return 5
            owl.reset_to_dfu()
            print("SysEx 0x7E sent: acdc1 restarts into the DFU bootloader.")
            return 0
        if args.program is not None:
            names = {e["index"]: e["name"] for e in parse(owl.request(0x01, quiet=1.0))
                     if e.get("cmd") == "PRESET_NAME"}
            if args.program not in names or args.program == 0:
                print(f"Slot {args.program} is empty: {names}", file=sys.stderr)
                return 3
            owl.program_change(args.program)
            time.sleep(1.0)
            run = [e for e in parse(owl.request(0x01, quiet=1.0)) if e.get("index") == 0]
            print(f"Program Change -> slot {args.program} ({names[args.program]}). Now running: {run}")
            return 0

        report["info"] = parse(owl.request(127, quiet=1.0))
        report["settings_cc"] = parse(owl.request(0x03, quiet=1.0))
        report["patch_names"] = parse(owl.request(0x01, quiet=1.0))
        report["resource_names"] = parse(owl.request(0x04, quiet=1.0))

        stamp = dt.date.today().strftime("%Y%m%d")
        outdir = args.out / name / stamp
        if args.dump:
            outdir = outdir / "owl"
        if outdir.exists() and any(outdir.iterdir()):
            # nie etwas Vorhandenes überschreiben (Backups!)
            outdir = outdir.with_name(outdir.name + dt.datetime.now().strftime("_%H%M%S"))
        outdir.mkdir(parents=True, exist_ok=True)

        slots = args.slots
        if slots is None and args.dump:
            slots = [e["index"] for e in report["patch_names"]
                     if e.get("cmd") == "PRESET_NAME" and e["index"] >= 1]
            slots += [e["index"] for e in report["resource_names"] if e.get("cmd") == "RESOURCE_NAME"]
        report["downloads"] = []
        for slot in slots or []:
            res = reassemble(owl.download(slot))
            label = next((e["name"] for e in report["patch_names"] + report["resource_names"]
                          if e.get("index") == slot and e.get("cmd") in ("PRESET_NAME", "RESOURCE_NAME")), f"slot{slot}")
            safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in label)
            entry = {k: v for k, v in res.items() if k not in ("data", "sysex")}
            entry.update(slot=slot, name=label)
            if res.get("data") is not None and "data" in res:
                base = outdir / f"slot{slot:02d}_{safe}"
                base.with_suffix(".bin").write_bytes(res["data"])
                with open(base.with_suffix(".syx"), "wb") as f:
                    for m in res["sysex"]:
                        f.write(bytes(m.bin()))
                entry["files"] = [str(base.with_suffix(".bin")), str(base.with_suffix(".syx"))]
                if label == "__SETTINGS__":
                    entry["decoded"] = decode_settings(res["data"])
            report["downloads"].append(entry)
            print(f"Slot {slot:2d} {label}: ok={entry['ok']} size={entry.get('size')} "
                  f"crc dev={entry.get('crc_device')} owl={entry.get('crc_owl')} zlib={entry.get('crc_zlib')}")

        (outdir / "device_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
        print(f"Report: {outdir / 'device_report.json'}")
    finally:
        owl.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
