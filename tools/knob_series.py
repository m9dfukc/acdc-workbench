"""Guided series of recordings with the knobs of acdc1 in given positions.

For each step the tool says where the knobs belong, reads them over MIDI (CC 20-23 from
the settings request) and waits until they are there. Then it records with
tools/acdc_rec.py (open inputs, zeros on the outputs, --owl-read) and goes on to the next
step. At the end tools/line_levels.py measures the lines in all recordings and the tool
writes reports/<series>-session-table.md with the knob readings and the line levels.

Positions per knob: L = left stop, R = right stop, M = 12 o'clock, or a number 0-127.
A step is four positions, e.g. LMMM or 32,M,M,M. The default series is: all at 12 o'clock,
then each knob alone at the left and at the right stop, then all at 12 o'clock again.

Runs only outside the sandbox (CoreMIDI, CoreAudio) and with Python 3.12 like owl_read.py:
  uv run --no-project --python 3.12 --with mido --with python-rtmidi \\
      python tools/knob_series.py --series K1

Test without a module (any Python with numpy and soundfile, e.g. plain "uv run python"):
  UV_CACHE_DIR=.uv-cache uv run python tools/knob_series.py --series T1 --simulate --duration 2
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ACDC1_UUID = "0039001c:31315101:39333437"
DEFAULT_STEPS = ["MMMM", "LMMM", "RMMM", "MLMM", "MRMM", "MMLM", "MMRM", "MMML", "MMMR", "MMMM"]
WORDS = {"L": "left stop", "R": "right stop", "M": "12 o'clock"}


def parse_step(s: str) -> list[str]:
    parts = [p.strip().upper() for p in s.split(",")] if "," in s else list(s.strip().upper())
    if len(parts) != 4 or not all(p in WORDS or (p.isdigit() and 0 <= int(p) <= 127) for p in parts):
        raise argparse.ArgumentTypeError(f"not a step of four positions (L, R, M or 0-127): {s}")
    return parts


def in_place(pos: str, cc: int, a) -> bool:
    if pos == "L":
        return cc <= a.left_max
    if pos == "R":
        return cc >= a.right_min
    if pos == "M":
        return a.mid[0] <= cc <= a.mid[1]
    return abs(cc - int(pos)) <= a.tol


def describe(step: list[str]) -> str:
    """Kurze Anweisung: nur nennen, was nicht auf 12 Uhr steht."""
    odd = [f"knob {i + 1} to {WORDS.get(p, 'value ' + p)}" for i, p in enumerate(step) if p != "M"]
    if not odd:
        return "all four knobs to 12 o'clock"
    return ", ".join(odd) + (", the others to 12 o'clock" if len(odd) < 4 else "")


class Device:
    """Regler lesen und Slot wählen. Echt über owl_read.Owl, simuliert ohne Gerät."""

    def __init__(self, simulate: bool, port: str):
        self.simulate = simulate
        self.port = port
        self.owl = None
        self._sim = [64, 64, 64, 64]
        self._sim_target: list[str] | None = None

    def open(self):
        if self.simulate or self.owl is not None:
            return
        import mido
        from owl_read import Owl
        ins = [n for n in mido.get_input_names() if self.port in n]
        if len(ins) != 1:
            raise SystemExit(f"MIDI port not found or ambiguous: {ins}. Are OWL web pages closed?")
        self.owl = Owl(ins[0])

    def close(self):
        if self.owl is not None:
            self.owl.close()
            self.owl = None

    def identify(self) -> tuple[str | None, str | None]:
        if self.simulate:
            return ACDC1_UUID, "AC/DC v0.0.0-sim"
        from owl_read import parse
        uuid = next((e["text"] for e in parse(self.owl.request(0x21)) if e.get("cmd") == "DEVICE_ID"), None)
        ver = next((e["text"] for e in parse(self.owl.request(127, quiet=1.0))
                    if e.get("cmd") == "FIRMWARE_VERSION"), None)
        return uuid, ver

    def slots(self) -> dict[int, str]:
        if self.simulate:
            return {0: "ACDC", 1: "ACDC"}
        from owl_read import parse
        return {e["index"]: e["name"] for e in parse(self.owl.request(0x01, quiet=1.0))
                if e.get("cmd") == "PRESET_NAME"}

    def program(self, slot: int):
        if not self.simulate:
            self.owl.program_change(slot)
            time.sleep(1.0)

    def knobs(self) -> list[int] | None:
        if self.simulate:
            # Attrappe: die Regler wandern in zwei Schritten zum Ziel
            if self._sim_target:
                goal = [{"L": 2, "R": 127, "M": 64}.get(p, int(p) if p.isdigit() else 64) for p in self._sim_target]
                self._sim = [g if abs(g - v) < 40 else (g + v) // 2 for g, v in zip(goal, self._sim)]
            return list(self._sim)
        from owl_read import parse
        cc = {e["control"]: e["value"] for e in parse(self.owl.request(0x03, quiet=0.25))
              if e.get("type") == "control_change"}
        return [cc[c] for c in (20, 21, 22, 23)] if all(c in cc for c in (20, 21, 22, 23)) else None


def wait_for(dev: Device, step: list[str], a) -> list[int]:
    """Wartet, bis alle vier Regler --hold Sekunden lang am Ziel stehen."""
    dev._sim_target = step
    since = None
    while True:
        v = dev.knobs()
        if v is None:
            print("\r  no answer from the module …" + " " * 30, end="", flush=True)
            time.sleep(1.0)
            continue
        ok = [in_place(p, c, a) for p, c in zip(step, v)]
        print("\r  knobs now: " + "  ".join(f"{c:3d} {'ok' if o else '<<'}" for c, o in zip(v, ok)) + "   ",
              end="", flush=True)
        if all(ok):
            since = since or time.monotonic()
            if time.monotonic() - since >= a.hold:
                print()
                return v
        else:
            since = None
        time.sleep(0.3)


def child_env() -> dict:
    """Umgebung für acdc_rec.py und line_levels.py: ohne das VIRTUAL_ENV dieses uv-Laufs,
    sonst warnt das innere "uv run" bei jedem Aufruf."""
    env = dict(os.environ)
    env.pop("VIRTUAL_ENV", None)
    return env


def record(a, mid: str, test: str, gain: str, version: str, step: list[str], rec_dir: Path) -> tuple[int, Path]:
    wav = rec_dir / f"{a.date}_acdc1_{test}_{gain}_usb-stream.wav"
    code = "".join(step) if all(p in WORDS for p in step) else ",".join(step)
    cmd = [*a.rec_cmd.split(), str(ROOT / "tools" / "acdc_rec.py"),
           "--id", mid, "--test", test, "--gain", gain, "--date", a.date,
           "--duration", str(a.duration), "--dir", str(rec_dir),
           "--device-desc", f"acdc1, Firmware {version}",
           "--test-desc", f"Reglerserie {a.series}: offene Eingänge, Regler 1–4 = {code} "
                          "(L = Linksanschlag, R = Rechtsanschlag, M = 12 Uhr), tools/knob_series.py",
           "--patch", f"Slot {a.slot}, wirkt nicht auf die USB-Aufnahme"]
    cmd += ["--simulate", "--no-manifest"] if a.simulate else ["--owl-read"]
    r = subprocess.run(cmd, cwd=ROOT, env=child_env())
    return r.returncode, wav


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--series", required=True, help="name of the series, prefix of the manifest IDs, e.g. K1")
    ap.add_argument("--steps", nargs="+", type=parse_step, help="steps, e.g. MMMM LMMM 32,M,M,M (default: see above)")
    ap.add_argument("--from-step", type=int, default=1, help="start with this step (to continue a series)")
    ap.add_argument("--duration", type=float, default=30.0, help="seconds per recording (default 30)")
    ap.add_argument("--slot", type=int, default=1, help="patch slot to run during the series (default 1, 0 = leave as is)")
    ap.add_argument("--freqs", type=float, nargs="+", default=[2200.95, 4401.90, 6602.85, 6000.0],
                    help="lines for the table at the end")
    ap.add_argument("--left-max", type=int, default=6, help="L: CC value at most (default 6)")
    ap.add_argument("--right-min", type=int, default=122, help="R: CC value at least (default 122)")
    ap.add_argument("--mid", type=int, nargs=2, default=[54, 74], metavar=("LO", "HI"), help="M: CC range (default 54 74)")
    ap.add_argument("--tol", type=int, default=3, help="tolerance for numeric positions (default 3)")
    ap.add_argument("--hold", type=float, default=1.5, help="seconds the knobs must stay in place (default 1.5)")
    ap.add_argument("--port", default="OWL-ACDC", help="MIDI port name (substring)")
    ap.add_argument("--date", default=dt.date.today().strftime("%Y%m%d"))
    ap.add_argument("--rec-cmd", default="uv run python", help="interpreter for acdc_rec.py and line_levels.py")
    ap.add_argument("--no-prompt", action="store_true", help="do not wait for Enter at the start")
    ap.add_argument("--simulate", action="store_true", help="no module: simulated knobs and recordings in a temporary folder")
    a = ap.parse_args(argv)
    steps = a.steps or [parse_step(s) for s in DEFAULT_STEPS]

    dev = Device(a.simulate, a.port)
    dev.open()
    uuid, version = dev.identify()
    if uuid != ACDC1_UUID:
        print(f"Aborted: the connected module is not acdc1 ({uuid})", file=sys.stderr)
        return 5
    fw = (version or "fw").rsplit("-", 1)[-1].split()[-1].replace("/", "")
    names = dev.slots()
    print(f"acdc1, {version}. Running: {names.get(0)}. Series {a.series}: {len(steps)} recordings of {a.duration:g} s.")
    print("Inputs open (no cables in the inputs), rack and cabling unchanged during the series.")
    if a.slot and a.slot not in names:
        print(f"Aborted: slot {a.slot} is empty: {names}", file=sys.stderr)
        return 3
    if not a.no_prompt:
        sw = f"switches to slot {a.slot} ({names[a.slot]}), this interrupts what you hear" if a.slot else "keeps the running patch"
        input(f"Press Enter to start ({sw}). Ctrl-C ends the series early. ")
    if a.slot:
        dev.program(a.slot)
        print(f"Slot {a.slot}: {dev.slots().get(0)} is running.")

    rec_dir = Path(tempfile.mkdtemp(prefix="knob_series_")) if a.simulate else ROOT / "recordings"
    done: list[dict] = []
    try:
        for n, step in enumerate(steps, start=1):
            if n < a.from_step:
                continue
            code = "".join(step) if all(p in WORDS for p in step) else "-".join(step)   # Zahlen immer mit Trennstrich
            mid = f"{a.series}-{n:02d}-{code}"
            test = f"{fw}-open-inputs-{mid}"
            gain = "g12" if all(p == "M" for p in step) else "gvar"
            print(f"\a\n== {n}/{len(steps)}  {mid}: {describe(step)}")
            before = wait_for(dev, step, a)
            print(f"  In place. Hands off, recording {a.duration:g} s …", flush=True)
            dev.close()                      # der Port gehört während der Aufnahme owl_read.py
            rc, wav = record(a, mid, test, gain, version or "?", step, rec_dir)
            dev.open()
            after = dev.knobs() or before
            moved = not all(in_place(p, c, a) for p, c in zip(step, after))
            if rc != 0 or not wav.is_file():
                print(f"  Recording failed (rc {rc}). Fix the cause and continue with --from-step {n}", file=sys.stderr)
                return 1
            if moved:
                print(f"  WARNING: knobs moved during the recording: {after}", file=sys.stderr)
            done.append({"id": mid, "step": step, "wav": str(wav), "knobs_before": before,
                         "knobs_after": after, "moved": moved})
    except KeyboardInterrupt:
        print("\nStopped by Ctrl-C.")
    finally:
        dev.close()
    if not done:
        return 1

    # Auswertung: Linienpegel je Aufnahme, davor die gelesenen Reglerwerte
    print(f"\a\n== Done: {len(done)} recordings. You can set the knobs as you like again. Measuring the lines …")
    out = (rec_dir if a.simulate else ROOT / "reports") / f"{a.series}-session-table.md"
    lines_md = out.with_name(out.stem + ".lines.tmp")
    cmd = [*a.rec_cmd.split(), str(ROOT / "tools" / "line_levels.py"), *[f"{d['id']}={d['wav']}" for d in done],
           "--freqs", *[str(f) for f in a.freqs], "--out", str(lines_md),
           "--json", str(out.with_name(f"{a.series}-lines.json"))]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=child_env())
    if r.returncode != 0:
        print(r.stdout + r.stderr, file=sys.stderr)
        return 1
    head = [f"# Reglerserie {a.series} – {a.date}, acdc1, {version}", "",
            f"Offene Eingänge, Slot {a.slot}, je {a.duration:g} s, `tools/knob_series.py`. "
            "Regler als CC-Wert 0–127 (CC 20–23), gelesen vor und nach der Aufnahme.", "",
            "| Aufnahme | Soll (Regler 1–4) | gelesen vorher | gelesen nachher |", "|---|---|---|---|"]
    for d in done:
        head.append(f"| `{d['id']}` | {' '.join(d['step'])} | {' / '.join(map(str, d['knobs_before']))} | "
                    f"{' / '.join(map(str, d['knobs_after']))}{' (bewegt!)' if d['moved'] else ''} |")
    out.write_text("\n".join(head) + "\n\n" + lines_md.read_text())
    lines_md.unlink()
    out.with_name(f"{a.series}-knobs.json").write_text(json.dumps(done, indent=2))
    print(out.read_text())
    print(f"Table: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
