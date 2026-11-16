#!/usr/bin/env python3
"""Multichannel recording from the AC/DC (or another audio device): replaces host software with a multichannel recorder.

Standard recording tool of this project (CLAUDE.md, section on recordings). It reproduces the earlier workflow with
host software:
- open the device by name (default "OWL-ACDC-FX"), 48 kHz, block size 256,
- **duplex**: the output gets zeros, like the audio module of host software with no cable connected. The device is
  therefore in the same state as in all host measurements (with a stream, the output is USB playback).
  `--input-only` leaves the output closed (macOS may start it anyway),
- several repetitions, with the stream closed and reopened in between (replaces restarting the
  host software),
- discard `--settle` seconds before writing (settling after opening),
- optional **test signals to the outputs** instead of zeros (replaces software oscillators): `--sine F1 F2 F3 F4`
  = one sine per output (0 = silent), level `--sine-level` in device dBFS (default −6 dBFS = 0.5, like the
  software oscillator with 5 V peak), soft fade-in `--sine-fade`. A true sine (the software oscillator was parabolic,
  odd harmonics ≈ −29 dBc, messlog D8). Example USB loop test (patch cable Out n → In n):
  `--sine 440 530 670 790 --duration 600` and afterwards `tools/phase_slips.py <wav> --freqs 440 530 670 790`.
- **DC offset per output** `--dc V1 V2 …` in full scale (−1…1, 1 = 0 dBFS ≈ 10 V at the output), alone or
  together with `--sine`. `--dc-ramp SEC` ramps it up slowly from 0 (e.g. to find the clip threshold),
  very slow AC signals work with `--sine 0.05 …`. Example clip test (Out n → In n):
  `--sine 440 440 440 440 --sine-level -3 -1 -0.3 0` or `--dc 0.9 0.95 0.98 1.0 --dc-ramp 20`.

Output: one multichannel WAV per repetition, named by the convention
`YYYYMMDD_<device>_<test>[-rN]_<gain>_<usb>.wav` in `recordings/`, plus an entry in
`recordings/manifest.toml`. Default format 16-bit PCM = exactly the USB data. The manifest entry gets
`scale = 2.0`; the analysis uses it to convert to the same file dBFS as host recordings (host factor 2).
Device dBFS = file dBFS − 6.02 dB, as before.

Needs CoreAudio, so it does not run inside a sandbox. Usage:
    uv run python tools/acdc_rec.py --list
    uv run python tools/acdc_rec.py --id B4-fx3i --test fx3i-open-inputs --reps 2 --duration 60 \\
        --device-desc "acdc1, Build v22.4.r-fx3i" --test-desc "A/B against 3d" --owl-read --analyze --ref B3-fx2d-r1
Testing without a device: `--simulate` (noise + 1 kHz tone instead of a device, with `--manifest` pointing to a
copy). With `--sine` the output signal ends up in the simulated input (like patch cables Out n → In n).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import queue
import subprocess
import sys
import time
import tomllib
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
FORMATS = {"pcm16": ("int16", "PCM_16"), "pcm24": ("int32", "PCM_24"), "float32": ("float32", "FLOAT")}
OWL_READ = ["uv", "run", "--no-project", "--python", "3.12", "--with", "mido", "--with", "python-rtmidi",
            str(ROOT / "tools" / "owl_read.py")]


def toml_str(v) -> str:
    """TOML-Wert (Strings, Zahlen, Listen von Strings)."""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(toml_str(x) for x in v) + "]"
    return json.dumps(str(v), ensure_ascii=False)


def find_device(sd, name: str, n_in: int, n_out: int) -> int:
    devs = list(enumerate(sd.query_devices()))
    ok = [(i, d) for i, d in devs
          if name.lower() in d["name"].lower() and d["max_input_channels"] >= n_in and d["max_output_channels"] >= n_out]
    exact = [m for m in ok if m[1]["name"].lower() == name.lower()]
    ok = exact or ok
    if len(ok) != 1:
        lst = "\n".join(f"  [{i}] {d['name']} ({d['max_input_channels']} in / {d['max_output_channels']} out)" for i, d in devs)
        why = "not found" if not ok else "ambiguous"
        raise SystemExit(f"Device \"{name}\" with ≥ {n_in} in / ≥ {n_out} out {why}. Available:\n{lst}")
    return ok[0][0]


class SineOut:
    """Testsignal je Ausgangskanal: Sinus (phasenstetig über Blöcke) plus Gleichanteil, mit Einblenden.

    `dc` in Vollausschlag-Einheiten (−1…1, 1,0 = 0 dBFS, am Ausgang ≈ 10 V). Ohne `dc_ramp` werden Sinus
    und Gleichanteil über `fade_s` eingeblendet, mit `dc_ramp` steigt der Gleichanteil linear über so viele
    Sekunden von 0 auf den Zielwert (Schwelle suchen), der Sinus blendet weiter über `fade_s` ein.
    Liefert float64 (frames, kanäle)."""

    def __init__(self, freqs, levels_db, fs, n_out, fade_s, dc=None, dc_ramp_s=0.0):
        freqs = list(freqs or [])
        dc = list(dc or [])
        if len(freqs) > n_out or len(dc) > n_out:
            raise SystemExit(f"--sine/--dc: more values than the {n_out} outputs")
        if freqs and len(levels_db) not in (1, len(freqs)):
            raise SystemExit("--sine-level: one value for all or one per frequency")
        for f in freqs:
            if not 0 <= f < fs / 2:
                raise SystemExit(f"--sine {f:g} Hz: allowed range is 0 (silent) to < fs/2")
        lv = (levels_db * len(freqs) if len(levels_db) == 1 else levels_db) if freqs else []
        if lv and max(lv) > 0:
            raise SystemExit("--sine-level above 0 dBFS")
        self.f = np.array(freqs + [0.0] * (n_out - len(freqs)))
        self.amp = np.array([10 ** (l / 20) if f > 0 else 0.0 for f, l in zip(freqs, lv)] + [0.0] * (n_out - len(freqs)))
        self.dc = np.array(dc + [0.0] * (n_out - len(dc)), dtype=float)
        peak = self.amp + np.abs(self.dc)
        if np.any(peak > 1.0 + 1e-9):
            bad = [f"Out {i + 1}: {p:.3f}" for i, p in enumerate(peak) if p > 1.0 + 1e-9]
            raise SystemExit(f"Sine + DC offset above full scale ({', '.join(bad)})")
        self.fs, self.fade, self.n = fs, max(1, int(round(fade_s * fs))), 0
        self.ramp = int(round(dc_ramp_s * fs))

    def describe(self, console: bool = False) -> str:
        """Beschreibung des Testsignals. Standard: deutscher Text fürs Manifest (nicht ändern).
        `console=True`: englischer Text für die Konsole."""
        sine, ramp, head = ("sine", "ramp", "test signal") if console else ("Sinus", "Rampe", "Testsignal")
        parts = []
        for i, (f, a, d) in enumerate(zip(self.f, self.amp, self.dc)):
            p = []
            if a > 0:
                p.append(f"{sine} {f:g} Hz @ {20 * np.log10(a):.1f} dBFS")
            if d != 0:
                p.append(f"DC {d:+.3f} FS" + (f" ({ramp} {self.ramp / self.fs:g} s)" if self.ramp else ""))
            if p:
                parts.append(f"Out {i + 1} " + " + ".join(p))
        return f"{head} " + ", ".join(parts)

    def next(self, frames: int) -> np.ndarray:
        idx = self.n + np.arange(frames)
        fade = np.minimum(1.0, idx / self.fade)[:, None]
        x = self.amp[None, :] * np.sin(2 * np.pi * (idx[:, None] * self.f[None, :] / self.fs)) * fade
        dcw = np.minimum(1.0, idx / self.ramp)[:, None] if self.ramp else fade
        x = x + self.dc[None, :] * dcw
        self.n += frames
        return x


def to_dtype(x: np.ndarray, dtype: str) -> np.ndarray:
    if dtype == "int16":
        return np.clip(np.round(x * 32768), -32768, 32767).astype(np.int16)
    if dtype == "int32":
        return np.clip(np.round(x * 2**31), -2**31, 2**31 - 1).astype(np.int32)
    return x.astype(np.float32)


class Take:
    """Eine Aufnahme: Stream öffnen, `settle` verwerfen, `frames` schreiben, optional Hook bei offenem Stream."""

    def __init__(self, a, path: Path, gen: SineOut | None = None):
        self.a, self.path, self.gen = a, path, gen
        self.q: queue.Queue = queue.Queue()
        self.status: list[str] = []
        self.started = None

    def _callback(self, indata, outdata, frames, time_info, status):
        if status:
            self.status.append(str(status))
        self.q.put(indata.copy())
        if outdata is not None:
            if self.gen is None:
                outdata.fill(0)
            else:
                outdata[:] = to_dtype(self.gen.next(frames), FORMATS[self.a.format][0])

    def _in_callback(self, indata, frames, time_info, status):
        self._callback(indata, None, frames, time_info, status)

    def _stream(self, sd, dev):
        a, dtype = self.a, FORMATS[self.a.format][0]
        kw = dict(device=dev, samplerate=a.fs, blocksize=a.blocksize, dtype=dtype, latency=a.latency)
        if a.input_only:
            return sd.InputStream(channels=a.channels, callback=self._in_callback, **kw)
        return sd.Stream(device=(dev, dev), samplerate=a.fs, blocksize=a.blocksize, dtype=dtype,
                         latency=a.latency, channels=(a.channels, a.out_channels), callback=self._callback)

    def _simulated(self):
        """Erzeugt Blöcke wie ein Gerät (ohne Echtzeit-Takt): Rauschen + 1000,05-Hz-Ton, Kanal k skaliert."""
        a, dtype = self.a, FORMATS[self.a.format][0]
        rng, n = np.random.default_rng(0), 0
        while True:
            t = (n + np.arange(a.blocksize)) / a.fs
            x = 1e-4 * rng.standard_normal((a.blocksize, a.channels)) + 1e-3 * np.sin(2 * np.pi * 1000.05 * t)[:, None]
            x *= (1 + np.arange(a.channels))[None, :]
            if self.gen is not None:  # Loopback Out n → In n
                y = self.gen.next(a.blocksize)
                m = min(a.channels, y.shape[1])
                x[:, :m] += y[:, :m]
            n += a.blocksize
            yield to_dtype(x, dtype)

    def run(self, sd, dev, hook=None) -> dict:
        a = self.a
        skip, need = int(round(a.settle * a.fs)), int(round(a.duration * a.fs))
        written, last_report = 0, 0.0
        subtype = FORMATS[a.format][1]
        with sf.SoundFile(self.path, "x", samplerate=a.fs, channels=a.channels, subtype=subtype) as f:
            if a.simulate:
                src = self._simulated()
                get = lambda: next(src)  # noqa: E731
                ctx = None
            else:
                ctx = self._stream(sd, dev)
                ctx.start()
                get = lambda: self.q.get(timeout=5.0)  # noqa: E731
            try:
                t0 = time.monotonic()
                while written < need:
                    try:
                        blk = get()
                    except queue.Empty:
                        raise SystemExit("No data from the device for 5 s – stream stalled?")
                    if skip:
                        drop = min(skip, len(blk))
                        blk, skip = blk[drop:], skip - drop
                        if not len(blk):
                            continue
                    if self.started is None:
                        self.started = dt.datetime.now().astimezone()
                        t0 = time.monotonic()  # Fortschritt ab Schreibbeginn, ohne Einschwingzeit
                    blk = blk[: need - written]
                    f.write(blk)
                    written += len(blk)
                    now = time.monotonic() - t0
                    if not a.simulate and now - last_report >= 10:
                        last_report = now
                        print(f"  {written / a.fs:5.1f} / {a.duration:g} s", flush=True)
                hook_result = hook() if hook else None
            finally:
                if ctx is not None:
                    ctx.stop()
                    ctx.close()
        return {"frames": written, "status": self.status, "hook": hook_result, "start": self.started}


def manifest_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with open(path, "rb") as fh:
        return {e["id"] for e in tomllib.load(fh).get("measurement", [])}


def append_manifest(path: Path, entry: dict) -> None:
    lines = ["", "[[measurement]]"] + [f"{k} = {toml_str(v)}" for k, v in entry.items() if v is not None]
    with open(path, "a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(path, "rb") as fh:  # Gegenprobe: Datei muss lesbar bleiben
        tomllib.load(fh)


def owl_read_hook(out_dir: Path):
    def hook():
        print(f"  owl_read → {out_dir} (stream stays open)", flush=True)
        r = subprocess.run(OWL_READ + ["--out", str(out_dir)], cwd=ROOT, capture_output=True, text=True)
        tail = (r.stdout + r.stderr).strip().splitlines()[-8:]
        for line in tail:
            print("    " + line)
        return {"rc": r.returncode, "out": str(out_dir)}
    return hook


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    g = ap.add_argument_group("Device and stream")
    g.add_argument("--list", action="store_true", help="list audio devices and exit")
    g.add_argument("--device", default="OWL-ACDC-FX", help="device name (exact or substring)")
    g.add_argument("--channels", type=int, default=4, help="input channels")
    g.add_argument("--out-channels", type=int, default=4, help="output channels (get zeros)")
    g.add_argument("--input-only", action="store_true", help="open the input only (no duplex)")
    g.add_argument("--fs", type=int, default=48000)
    g.add_argument("--blocksize", type=int, default=256, help="block size (256, as in the early recordings)")
    g.add_argument("--latency", default="high", help="PortAudio latency: low/high or seconds")
    g.add_argument("--format", choices=sorted(FORMATS), default="pcm16")
    g.add_argument("--simulate", action="store_true", help="no device, synthetic data (for testing)")
    o = ap.add_argument_group("Test signal to the outputs (instead of zeros)")
    o.add_argument("--sine", type=float, nargs="+", metavar="HZ",
                   help="sine per output in the order Out 1, Out 2, …; 0 = silent, missing = silent")
    o.add_argument("--sine-level", type=float, nargs="+", default=[-6.0], metavar="DBFS",
                   help="level in device dBFS, one for all or one per frequency (default −6 ≙ 5 V peak at the output)")
    o.add_argument("--sine-fade", type=float, default=0.05, help="fade-in in seconds")
    o.add_argument("--dc", type=float, nargs="+", metavar="FS",
                   help="DC offset per output in full scale (−1…1, 1 = 0 dBFS ≈ 10 V), also together with --sine; "
                        "very slow signals: --sine 0.05 …")
    o.add_argument("--dc-ramp", type=float, default=0.0, metavar="SEC",
                   help="ramp the DC offset up linearly from 0 over SEC seconds (to find a threshold), otherwise like --sine-fade")

    t = ap.add_argument_group("Sequence")
    t.add_argument("--duration", type=float, default=60.0, help="seconds per recording")
    t.add_argument("--settle", type=float, default=3.0, help="seconds to discard after opening")
    t.add_argument("--reps", type=int, default=1, help="number of repetitions")
    t.add_argument("--first-rep", type=int, default=1, help="number of the first repetition (suffix -rN)")
    t.add_argument("--pause", type=float, default=5.0, help="seconds to pause between repetitions (stream closed)")
    t.add_argument("--prompt", action="store_true", help="wait for Enter before each recording")
    t.add_argument("--owl-read", action="store_true", help="run owl_read.py after each recording, before closing the stream")

    n = ap.add_argument_group("Name and manifest")
    n.add_argument("--id", help="manifest ID (with several repetitions + -rN)")
    n.add_argument("--test", help="test part of the file name, e.g. fx3i-open-inputs")
    n.add_argument("--label", default="acdc1", help="device part of the file name")
    n.add_argument("--gain", default="g12", help="gain part of the file name")
    n.add_argument("--usb", default="usb-stream", help="USB part of the file name")
    n.add_argument("--date", default=dt.date.today().strftime("%Y%m%d"), help="date YYYYMMDD")
    n.add_argument("--dir", type=Path, default=ROOT / "recordings")
    n.add_argument("--manifest", type=Path, default=ROOT / "recordings" / "manifest.toml")
    n.add_argument("--no-manifest", action="store_true")
    n.add_argument("--device-desc", help="manifest \"device\" (device + firmware)")
    n.add_argument("--test-desc", help="manifest \"test\"")
    n.add_argument("--usb-desc", help="manifest \"usb\" (default: everyday USB chain + stream type, filled in automatically)")
    n.add_argument("--patch", default="Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme")
    n.add_argument("--title", help="manifest \"title\" (default: generated)")
    n.add_argument("--note", default="", help="additional note text")
    n.add_argument("--scale", type=float, default=2.0, help="manifest \"scale\" (2.0 = file dBFS as in the early recordings, host factor 2)")

    x = ap.add_argument_group("Analysis")
    x.add_argument("--analyze", action="store_true", help="afterwards run python -m analysis for each recording")
    x.add_argument("--ref", nargs="+", help="reference for the analysis (manifest ID or files)")
    x.add_argument("--spectrogram", action="store_true", help="do not skip the spectrogram")
    a = ap.parse_args()

    sd = None
    if not a.simulate or a.list:
        import sounddevice as sd  # erst hier: braucht CoreAudio (außerhalb des Sandbox)
    if a.list:
        print(sd.query_devices())
        return
    if not a.test:
        ap.error("--test is missing (test part of the file name)")
    if not a.no_manifest and not a.id:
        ap.error("--id is missing (or use --no-manifest)")
    for part in (a.label, a.test, a.gain, a.usb, a.date):
        if not part or any(c in part for c in "/_ "):
            ap.error(f"name part \"{part}\": no spaces, '/' or '_'")

    signal = bool(a.sine or a.dc)
    if signal and a.input_only:
        ap.error("--sine/--dc need the output and cannot be combined with --input-only")

    def make_gen():
        return SineOut(a.sine, a.sine_level, a.fs, a.out_channels, a.sine_fade, a.dc, a.dc_ramp) if signal else None

    make_gen()  # früh prüfen
    # out_desc geht ins Manifest (deutsch, nicht ändern), out_desc_en nur auf die Konsole
    out_desc = ("nur Eingang" if a.input_only else "duplex, Ausgang "
                + (make_gen().describe() if signal else "Nullen"))
    out_desc_en = ("input only" if a.input_only else "duplex, output "
                   + (make_gen().describe(console=True) if signal else "zeros"))
    usb_desc = a.usb_desc or f"usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py {out_desc}"

    reps = list(range(a.first_rep, a.first_rep + a.reps))
    suffix = len(reps) > 1 or a.first_rep > 1
    plan = []
    for k in reps:
        rs = f"-r{k}" if suffix else ""
        path = a.dir / f"{a.date}_{a.label}_{a.test}{rs}_{a.gain}_{a.usb}.wav"
        mid = f"{a.id}{rs}" if a.id else None
        plan.append((k, mid, path))

    # Früh scheitern: Dateien und IDs dürfen noch nicht existieren
    existing = set() if a.no_manifest else manifest_ids(a.manifest)
    for k, mid, path in plan:
        if path.exists():
            raise SystemExit(f"{path} already exists – never overwrite")
        if mid in existing:
            raise SystemExit(f"Manifest ID {mid} already exists in {a.manifest}")

    dev = None
    if not a.simulate:
        dev = find_device(sd, a.device, a.channels, 0 if a.input_only else a.out_channels)
        info = sd.query_devices(dev)
        print(f"Device [{dev}] {info['name']}, {a.fs} Hz, block {a.blocksize}, {a.format}, "
              f"{out_desc_en}")
    a.dir.mkdir(parents=True, exist_ok=True)

    done = []
    for i, (k, mid, path) in enumerate(plan):
        if i and a.pause > 0:
            print(f"Pause {a.pause:g} s (stream closed)")
            time.sleep(a.pause)
        if a.prompt:
            input(f"Press Enter to start recording {mid or path.name} … ")
        print(f"Recording {mid or ''} → {path.name} ({a.duration:g} s + {a.settle:g} s settling)", flush=True)
        hook = owl_read_hook(ROOT / "out" / "owl_read" / (mid or path.stem)) if a.owl_read and not a.simulate else None
        gen = make_gen()
        take = Take(a, path, gen)
        try:
            res = take.run(sd, dev, hook)
        except KeyboardInterrupt:
            print(f"\nAborted. The incomplete file is left in place: {path} (no manifest entry)")
            sys.exit(130)
        flags = res["status"]
        print(f"  done: {res['frames']} frames, stream status messages: {len(flags)}"
              + (f" ({sorted(set(flags))})" if flags else ""))
        if not a.no_manifest:
            start = res["start"].strftime("%H:%M:%S") if res["start"] else "?"
            note = (f"{a.fs / 1000:g} kHz / {a.format}, tools/acdc_rec.py "
                    f"({'simuliert' if a.simulate else 'Gerät ' + sd.query_devices(dev)['name']}, "
                    f"{out_desc}, Block {a.blocksize}, "
                    f"{a.settle:g} s verworfen). scale = {a.scale:g} → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start {start}. "
                    f"Stream-Meldungen: {len(flags)}{' ' + str(sorted(set(flags))) if flags else ''}.")
            if res["hook"]:
                note += f" owl_read: {Path(res['hook']['out']).relative_to(ROOT)} (rc {res['hook']['rc']})."
            if len(plan) > 1:
                note += " Stream zwischen den Wiederholungen geschlossen und neu geöffnet."
            if a.note:
                note += " " + a.note
            entry = {
                "id": mid,
                "date": dt.datetime.strptime(a.date, "%Y%m%d").strftime("%Y-%m-%d"),
                "device": a.device_desc or a.label,
                "test": a.test_desc or a.test,
                "gain": a.gain,
                "usb": usb_desc,
                "patch": a.patch,
                "title": a.title or f"{mid} – {a.label} {a.test}, {a.duration:g} s"
                         + (f" (Wiederholung {k})" if suffix else ""),
                "files": [str(path.relative_to(a.manifest.parent)) if path.is_relative_to(a.manifest.parent)
                          else str(path)],
                "scale": a.scale,
                "recorder": "tools/acdc_rec.py",
                "note": note,
            }
            append_manifest(a.manifest, entry)
            print(f"  Manifest: {mid}")
        done.append((mid, path))

    if a.analyze:
        for mid, path in done:
            cmd = [sys.executable, "-m", "analysis", mid or str(path), "--manifest", str(a.manifest)]
            if a.ref:
                cmd += ["--ref", *a.ref]
            if not a.spectrogram:
                cmd.append("--no-spectrogram")
            print("Analysis:", " ".join(cmd[1:]), flush=True)
            subprocess.run(cmd, cwd=ROOT, check=False)


if __name__ == "__main__":
    main()
