"""Flash a firmware build to acdc1 over the ROM DFU and keep a flash log.

The steps are the flash procedure from CLAUDE.md:
  1. Offline checks of the binary (size, vector table, version string, BUILD_INFO.txt,
     check_itcm.json). Without --yes the tool stops here and touches no device.
  2. tools/owl_read.py -> <log>/owl_read_before, the device must be acdc1
  3. tools/owl_read.py --reset-to-dfu --yes, wait for the DFU device of acdc1
  4. dfu-util -D to 0x08000000 (internal flash only, never option bytes, never ":leave")
  5. Readback of the 128 KB, compared with the binary, the rest must be 0xFF
  6. You restart the module: case off, USB unplugged, case on, USB plugged in
  7. --a1 <log>: tools/owl_read.py -> <log>/owl_read_after, checks the firmware version,
     sample rate 48000, block size 8 and that the slots are unchanged

Writes to firmware/flashlog/<date>_<name>/: owl_read_before/, dfu-util_download.txt,
dfu-util_upload.txt, readback_after.bin, sha256.txt, flash_report.json, owl_read_after/.
An existing log folder is never reused. If the tool stops before anything was written to
the flash, it renames the folder to <date>_<name>-abgebrochen-<time>.

Only acdc1 is flashed: the MIDI device ID and the DFU serial number are both checked.
Settings and patch slots are not written. The device steps need USB and CoreMIDI, so
they only run outside the sandbox. Standard library only, owl_read.py runs through uv.

Usage:
  python3 tools/flash_acdc.py <build>                    offline checks only
  python3 tools/flash_acdc.py <build> --yes              flash acdc1
  python3 tools/flash_acdc.py <build> --yes --from-dfu   acdc1 is already in DFU mode
  python3 tools/flash_acdc.py --a1 <log folder>          after the restart
  python3 tools/flash_acdc.py --a1 <log folder> --reuse  evaluate the stored reports again

<build> is a .bin file, a build folder or the name of a folder in firmware/builds/.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDS = Path("firmware/builds")
FLASHLOG = Path("firmware/flashlog")

ACDC1_UUID = "0039001c:31315101:39333437"
ACDC1_DFU_SERIAL = "200364500000"
DFU_ID = "0483:df11"          # STM32-ROM-DFU
FLASH_ADDR = 0x08000000
FLASH_LEN = 131072            # STM32H750: 128 KB internes Flash
EXPECT_FS, EXPECT_BS = 48000, 8

OWL_READ = ["uv", "run", "--no-project", "--python", "3.12", "--with", "mido",
            "--with", "python-rtmidi", "python", "tools/owl_read.py"]


class Abort(Exception):
    """Abbruch mit Meldung und Exit-Code."""

    def __init__(self, msg: str, code: int = 1):
        super().__init__(msg)
        self.code = code


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------- Offline-Prüfungen

def resolve_build(arg: str) -> Path:
    """<build> → Pfad der .bin: Datei, Build-Ordner oder Ordnername in firmware/builds/."""
    for p in (Path(arg), BUILDS / arg):
        if p.is_file():
            return p
        if p.is_dir():
            bins = sorted(p.glob("*.bin"))
            if len(bins) == 1:
                return bins[0]
            raise Abort(f"{p}: expected exactly one .bin, found {[b.name for b in bins]}", 2)
    raise Abort(f"Build not found: {arg} (also tried {BUILDS / arg})", 2)


def firmware_version(b: bytes) -> str | None:
    m = re.search(rb"AC/DC v\d+\.\d+[\x21-\x7e]*", b)
    return m.group().decode() if m else None


def check_binary(path: Path) -> dict:
    """Prüft die .bin ohne Gerät. Rückgabe: Befund mit 'fails' und 'notes'."""
    b = path.read_bytes()
    fails: list[str] = []
    notes: list[str] = []
    info = {"bin": str(path), "size": len(b), "sha256": sha256(b), "version": firmware_version(b)}

    if not 1024 <= len(b) <= FLASH_LEN:
        fails.append(f"size {len(b)} is outside 1024..{FLASH_LEN} bytes")
    if len(b) >= 8:
        sp, reset = struct.unpack("<II", b[:8])
        info.update(initial_sp=f"0x{sp:08x}", reset_handler=f"0x{reset:08x}")
        # Reset-Handler: Thumb-Adresse innerhalb des Abbilds
        if not (reset & 1 and FLASH_ADDR + 8 <= reset < FLASH_ADDR + len(b)):
            fails.append(f"reset handler 0x{reset:08x} does not point into the image")
        if sp in (0, 0xFFFFFFFF):
            fails.append(f"initial stack pointer 0x{sp:08x} is not plausible")
    if info["version"] is None:
        fails.append("no version string 'AC/DC v…' in the binary")

    # BUILD_INFO.txt von tools/build_acdc.sh: SHA muss passen
    bi = path.parent / "BUILD_INFO.txt"
    if bi.is_file():
        m = re.search(r"^bin_sha256:\s*([0-9a-f]{64})", bi.read_text(), re.M)
        if not m:
            notes.append("BUILD_INFO.txt has no bin_sha256")
        elif m.group(1) != info["sha256"]:
            fails.append(f"SHA-256 differs from BUILD_INFO.txt ({m.group(1)[:8]}…)")
        else:
            info["build_info"] = "sha256 matches"
    else:
        notes.append("no BUILD_INFO.txt next to the binary, SHA-256 not cross-checked")

    # ITCM-Builds: check_itcm.py muss bestanden sein und zum ELF daneben gehören
    ci = path.parent / "check_itcm.json"
    if ci.is_file():
        passed = json.loads(ci.read_text()).get("passed")
        info["check_itcm"] = bool(passed)
        if not passed:
            fails.append("check_itcm.json says passed = false")
        elf = path.parent / (path.stem + ".elf")
        if elf.is_file() and elf.stat().st_mtime > ci.stat().st_mtime + 1:
            fails.append("check_itcm.json is older than the ELF, run tools/check_itcm.py again")
    else:
        notes.append("no check_itcm.json: fine for builds without ITCM (3d and older), "
                     "an ITCM build needs tools/check_itcm.py first")

    info.update(fails=fails, notes=notes)
    return info


def check_readback(b: bytes, rb: bytes) -> dict:
    """Readback gegen das Binary: Anfang bytegleich, Rest 0xFF."""
    n = len(b)
    first_diff = next((i for i in range(min(n, len(rb))) if b[i] != rb[i]), None)
    return {
        "readback_size": len(rb),
        "identical": len(rb) >= n and rb[:n] == b,
        "rest_ff": len(rb) == FLASH_LEN and all(x == 0xFF for x in rb[n:]),
        "first_difference": None if first_diff is None else f"0x{first_diff:05x}",
        "sha256_readback": sha256(rb),
        "sha256_readback_head": sha256(rb[:n]),
    }


# ---------------------------------------------------------------- A1-Auswertung

def _slots(report: dict) -> dict:
    """Slots 1…n und Ressourcen als {index: (name, size, crc)}. Index 0 ist der laufende Patch."""
    out = {}
    for e in report.get("patch_names", []) + report.get("resource_names", []):
        if e.get("cmd") in ("PRESET_NAME", "RESOURCE_NAME") and e.get("index", 0) >= 1:
            out[e["index"]] = (e.get("name"), e.get("size"), e.get("crc"))
    return out


def _config(report: dict, key: str):
    return next((e.get("value") for e in report.get("settings_cc", [])
                 if e.get("cmd") == "CONFIGURATION" and e.get("key") == key), None)


def _info(report: dict, cmd: str):
    return next((e.get("text") for e in report.get("info", []) if e.get("cmd") == cmd), None)


def a1_check(after: dict, before: dict | None, expect_version: str | None) -> dict:
    """A1: Gerät, Version, Abtastrate, Blockgröße, Slots unverändert."""
    rows: list[tuple[str, bool | None, str]] = []
    rows.append(("device is acdc1", after.get("device_id") == ACDC1_UUID, str(after.get("device_id"))))
    ver = _info(after, "FIRMWARE_VERSION")
    if expect_version:
        rows.append(("firmware version", ver == expect_version, f"{ver} (expected {expect_version})"))
    else:
        rows.append(("firmware version", None, f"{ver} (no expected version given)"))
    fs, bs = _config(after, "FS"), _config(after, "BS")
    rows.append(("sample rate", fs == EXPECT_FS, str(fs)))
    rows.append(("block size", bs == EXPECT_BS, str(bs)))
    sa = _slots(after)
    if before is None:
        rows.append(("slots unchanged", None, f"no report from before the flash, now: {_fmt_slots(sa)}"))
    else:
        sb = _slots(before)
        diff = sorted(k for k in set(sa) | set(sb) if sa.get(k) != sb.get(k))
        rows.append(("slots unchanged", not diff and bool(sa),
                     _fmt_slots(sa) if not diff else f"differ in {diff}: before {sb}, after {sa}"))
    msg = _info(after, "PROGRAM_MESSAGE") or _info(after, "PROGRAM_STATS")
    passed = all(ok is not False for _, ok, _ in rows) and any(ok for _, ok, _ in rows)
    return {"passed": passed, "complete": all(ok is not None for _, ok, _ in rows),
            "rows": [{"check": c, "ok": ok, "detail": d} for c, ok, d in rows],
            "storage": _info(after, "DEVICE_STATS"), "program": msg}


def _fmt_slots(s: dict) -> str:
    return ", ".join(f"{i} {v[0]}" for i, v in sorted(s.items())) or "none"


def newest_report(folder: Path) -> Path | None:
    reps = sorted(folder.glob("*/*/device_report.json"), key=lambda p: p.stat().st_mtime)
    return reps[-1] if reps else None


# ---------------------------------------------------------------- Geräte-Schritte

def run(cmd: list[str], log: Path | None = None, timeout: float = 120, env: dict | None = None) -> tuple[int, str]:
    """Führt einen Befehl aus, schreibt die Ausgabe optional in eine Datei."""
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout, env=env)
        rc, out = p.returncode, p.stdout.decode(errors="replace")
    except subprocess.TimeoutExpired as e:
        rc, out = 124, (e.stdout or b"").decode(errors="replace") + f"\n[timeout after {timeout:.0f} s]\n"
    if log is not None:
        log.write_text(out)
    return rc, out


def owl_read(*args: str) -> tuple[int, str]:
    env = dict(os.environ)
    env.setdefault("UV_CACHE_DIR", ".uv-cache")
    # wie im Ablauf vom 2026-11-17: uv soll keine Pakete aus Quellen bauen
    env.setdefault("UV_NO_BUILD", "1")
    rc, out = run(OWL_READ + list(args), timeout=90, env=env)
    for line in out.strip().splitlines()[-3:]:
        print(f"   {line}")
    return rc, out


def dfu_alt() -> int | None:
    """Alt-Setting 'Internal Flash' des DFU-Geräts von acdc1, None = nicht da."""
    _, out = run(["dfu-util", "-l"], timeout=20)
    for line in out.splitlines():
        if f"[{DFU_ID}]" in line and f'serial="{ACDC1_DFU_SERIAL}"' in line and "Internal Flash" in line:
            m = re.search(r"alt=(\d+)", line)
            if m:
                return int(m.group(1))
    return None


def wait_for_dfu(seconds: int) -> int:
    for _ in range(seconds):
        alt = dfu_alt()
        if alt is not None:
            return alt
        time.sleep(1)
    raise Abort(f"No DFU device {DFU_ID} with serial {ACDC1_DFU_SERIAL} after {seconds} s. "
                "Check with 'dfu-util -l'. If acdc1 is in DFU mode, run again with --from-dfu.", 3)


def flash(args) -> int:
    path = resolve_build(args.build)
    info = check_binary(path)
    name = args.name or re.sub(r"^acdc1-", "", path.parent.name)
    log = Path(args.log_dir) / f"{dt.date.today():%Y%m%d}_{name}"

    print(f"Build:    {path}")
    print(f"Version:  {info['version']}")
    print(f"Size:     {info['size']} bytes, SHA-256 {info['sha256']}")
    print(f"Vectors:  SP {info.get('initial_sp')}, reset {info.get('reset_handler')}")
    if "build_info" in info:
        print(f"Info:     BUILD_INFO.txt, {info['build_info']}")
    if "check_itcm" in info:
        print(f"ITCM:     check_itcm.json {'passed' if info['check_itcm'] else 'FAILED'}")
    for n in info["notes"]:
        print(f"Note:     {n}")
    print(f"Log:      {log}")
    if log.exists():
        info["fails"].append(f"{log} already exists, choose another --name (e.g. {name}-zurueck)")
    if shutil.which("dfu-util") is None:
        info["fails"].append("dfu-util not found")
    if info["fails"]:
        for f in info["fails"]:
            print(f"FAIL:     {f}", file=sys.stderr)
        return 1
    if not args.yes:
        print("\nOffline checks passed. Nothing was sent to a device. Add --yes to flash acdc1.")
        return 0

    b = path.read_bytes()
    log.mkdir(parents=True)
    report = {"time": dt.datetime.now().isoformat(timespec="seconds"), "name": name, "binary": info,
              "device_uuid": None, "dfu_serial": ACDC1_DFU_SERIAL, "from_dfu": bool(args.from_dfu)}

    def save():
        (log / "flash_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))

    try:
        if args.from_dfu:
            print("== 1/4 acdc1 is expected in DFU mode, no owl_read before the flash")
            alt = wait_for_dfu(3)
        else:
            print("== 1/4 Reading the device (owl_read_before)")
            rc, _ = owl_read("--out", str(log / "owl_read_before"))
            rep = newest_report(log / "owl_read_before")
            if rc != 0 or rep is None:
                raise Abort("owl_read.py failed. Is the module connected, are OWL web pages closed? "
                            "Nothing was changed.", 3)
            before = json.loads(rep.read_text())
            report["device_uuid"] = before.get("device_id")
            if before.get("device_id") != ACDC1_UUID:
                raise Abort(f"Connected device is {before.get('device')} ({before.get('device_id')}), "
                            "not acdc1. Nothing was changed.", 5)
            print(f"   {_info(before, 'FIRMWARE_VERSION')}, slots: {_fmt_slots(_slots(before))}")
            report["before"] = {"version": _info(before, "FIRMWARE_VERSION"), "report": str(rep)}
            save()

            print("== 2/4 Restart into the DFU bootloader")
            rc, _ = owl_read("--reset-to-dfu", "--yes")
            if rc != 0:
                raise Abort("The DFU reset failed. Nothing was written.", 3)
            alt = wait_for_dfu(args.dfu_wait)
        report["dfu_alt"] = alt

        print(f"== 3/4 Writing {info['size']} bytes to 0x{FLASH_ADDR:08x} (alt {alt})")
        sel = ["dfu-util", "-d", DFU_ID, "-S", ACDC1_DFU_SERIAL, "-a", str(alt)]
        rc, out = run(sel + ["-s", f"0x{FLASH_ADDR:08x}", "-D", str(path)],
                      log / "dfu-util_download.txt", timeout=300)
        report["download_ok"] = rc == 0 and "File downloaded successfully" in out
        save()
        print(f"   {out.strip().splitlines()[-1] if out.strip() else '(no output)'}")
        if not report["download_ok"]:
            # trotzdem zurücklesen: der Vergleich zeigt, was im Flash steht
            print("   dfu-util reported an error, reading back anyway", file=sys.stderr)

        print(f"== 4/4 Readback of {FLASH_LEN} bytes")
        rbf = log / "readback_after.bin"
        rc, out = run(sel + ["-s", f"0x{FLASH_ADDR:08x}:{FLASH_LEN}", "-U", str(rbf)],
                      log / "dfu-util_upload.txt", timeout=300)
        if rc != 0 or not rbf.is_file():
            raise Abort("Readback failed, the flash content is unknown. acdc1 is still in DFU mode: "
                        "do not restart, run again with --from-dfu and a new --name.", 4)
        res = check_readback(b, rbf.read_bytes())
        report["readback"] = res
        (log / "sha256.txt").write_text(
            f"{info['sha256']}  {path}\n{res['sha256_readback']}  {rbf}\n"
            f"{res['sha256_readback_head']}  {rbf.name}[0:{info['size']}]\n")
        report["flash_ok"] = bool(report["download_ok"] and res["identical"] and res["rest_ff"])
        save()
        print(f"   Readback identical: {res['identical']} | rest 0xFF: {res['rest_ff']}")
    except Abort:
        save()
        if "download_ok" not in report:
            # Nichts geschrieben: Ordner umbenennen, damit der Name für den nächsten Versuch frei ist
            kept = log.with_name(f"{log.name}-abgebrochen-{dt.datetime.now():%H%M%S}")
            log.rename(kept)
            print(f"Nothing was written to the flash. Log of this attempt: {kept}", file=sys.stderr)
        raise

    if not report["flash_ok"]:
        if res["first_difference"]:
            print(f"   First difference at offset {res['first_difference']}", file=sys.stderr)
        print("FAILED. acdc1 is still in DFU mode: do not restart. Flash the fallback build with\n"
              f"  python3 tools/flash_acdc.py <build> --yes --from-dfu --name {name}-zurueck", file=sys.stderr)
        return 1
    print(f"\nFlash OK: {info['version']} is in the internal flash of acdc1.\n"
          "Now restart the module: case off, USB unplugged, case on, USB plugged in.\n"
          f"Then: python3 tools/flash_acdc.py --a1 {log}")
    return 0


def a1(args) -> int:
    log = Path(args.a1)
    if not log.is_dir():
        raise Abort(f"Flash log folder not found: {log}", 2)
    rf = log / "flash_report.json"
    report = json.loads(rf.read_text()) if rf.is_file() else {}
    expect = args.expect_version or report.get("binary", {}).get("version")
    if not args.reuse:
        print("== Reading the device (owl_read_after)")
        rc, _ = owl_read("--out", str(log / "owl_read_after"))
        if rc != 0:
            raise Abort("owl_read.py failed. Did the module restart (case off, USB unplugged)? "
                        "Are OWL web pages closed?", 3)
    rep_after = newest_report(log / "owl_read_after")
    if rep_after is None:
        raise Abort(f"No device report in {log / 'owl_read_after'}", 2)
    rep_before = newest_report(log / "owl_read_before")
    res = a1_check(json.loads(rep_after.read_text()),
                   json.loads(rep_before.read_text()) if rep_before else None, expect)
    for r in res["rows"]:
        mark = {True: "ok  ", False: "FAIL", None: "--  "}[r["ok"]]
        print(f"  {mark} {r['check']:18} {r['detail']}")
    print(f"       {res['storage']} | {res['program']}")
    if rf.is_file() and not args.reuse:
        report["a1"] = dict(res, report=str(rep_after), time=dt.datetime.now().isoformat(timespec="seconds"))
        rf.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    if not res["passed"]:
        print("A1 FAILED", file=sys.stderr)
        return 1
    print("A1 passed" if res["complete"] else "A1 passed, but not every check could be made (--)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("build", nargs="?", help=".bin file, build folder or folder name in firmware/builds/")
    ap.add_argument("--name", help="name of the flash log folder after the date "
                                   "(default: build folder name without 'acdc1-')")
    ap.add_argument("--log-dir", default=str(FLASHLOG), help=f"base folder of the flash logs (default {FLASHLOG})")
    ap.add_argument("--yes", action="store_true", help="really flash acdc1 (without it: offline checks only)")
    ap.add_argument("--from-dfu", action="store_true",
                    help="acdc1 is already in DFU mode: skip owl_read and the DFU reset")
    ap.add_argument("--dfu-wait", type=int, default=20, help="seconds to wait for the DFU device (default 20)")
    ap.add_argument("--a1", metavar="LOG", help="after the restart: read the device and check it against the flash log")
    ap.add_argument("--reuse", action="store_true", help="with --a1: evaluate the stored reports, ask no device")
    ap.add_argument("--expect-version", help="with --a1: expected version string, e.g. 'AC/DC v22.4.r-fx4b' "
                                             "(default: from flash_report.json)")
    args = ap.parse_args(argv)
    if bool(args.build) == bool(args.a1):
        ap.error("give either <build> or --a1 <log folder>")

    os.chdir(ROOT)  # relative Pfade wie in den Docs, owl_read.py liegt in tools/
    try:
        return a1(args) if args.a1 else flash(args)
    except Abort as e:
        print(f"Aborted: {e}", file=sys.stderr)
        return e.code


if __name__ == "__main__":
    sys.exit(main())
