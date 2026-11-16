#!/usr/bin/env python3
"""Mehrkanal-Aufnahme vom AC/DC (oder einem anderen Audiogerät): Ersatz für eine Host-Software mit Mehrkanal-Recorder.

Standard-Aufnahmewerkzeug des Projekts (CLAUDE.md, „Aufnahmen“). Bildet den früheren Ablauf mit einer Host-Software nach:
- Gerät per Namen öffnen (Standard „OWL-ACDC-FX“), 48 kHz, Blockgröße 256,
- **duplex**: Der Ausgang bekommt Nullen, wie das Audio-Modul einer Host-Software ohne Kabel. Das Gerät ist also im selben
  Zustand wie bei allen Host-Messungen (mit Stream = Ausgang ist USB-Playback). `--input-only` lässt den
  Ausgang zu (macOS kann ihn trotzdem starten),
- mehrere Wiederholungen, zwischen denen der Stream geschlossen und neu geöffnet wird (Ersatz für den
  Neustart der Host-Software),
- vor dem Schreiben `--settle` Sekunden verwerfen (Einschwingen nach dem Öffnen),
- optional **Testsignale an die Ausgänge** statt Nullen (Ersatz für Software-Oszillatoren): `--sine F1 F2 F3 F4`
  = Sinus je Ausgang (0 = still), Pegel `--sine-level` in Geräte-dBFS (Standard −6 dBFS = 0,5 wie der
  Software-Oszillator mit 5 V Spitze), weiches Einblenden `--sine-fade`. Echter Sinus (der Software-Oszillator war parabolisch,
  ungerade Obertöne ≈ −29 dBc, messlog D8). Beispiel USB-Loop-Test (Patchkabel Out n → In n):
  `--sine 440 530 670 790 --duration 600` und danach `tools/phase_slips.py <wav> --freqs 440 530 670 790`.
- **Gleichanteil je Ausgang** `--dc V1 V2 …` in Vollausschlag (−1…1, 1 = 0 dBFS ≈ 10 V am Ausgang), allein oder
  zusammen mit `--sine`. `--dc-ramp SEK` fährt ihn langsam von 0 hoch (z. B. Clip-Schwelle suchen),
  sehr langsame Wechselsignale gehen mit `--sine 0.05 …`. Beispiel Clip-Test (Out n → In n):
  `--sine 440 440 440 440 --sine-level -3 -1 -0.3 0` oder `--dc 0.9 0.95 0.98 1.0 --dc-ramp 20`.

Ausgabe: eine Mehrkanal-WAV je Wiederholung, Name nach Konvention
`YYYYMMDD_<geraet>_<test>[-rN]_<gain>_<usb>.wav` in `recordings/`, plus Eintrag in
`recordings/manifest.toml`. Standardformat 16 Bit PCM = genau die USB-Daten. Der Manifest-Eintrag bekommt
`scale = 2.0`, die Analyse rechnet damit in dieselben Datei-dBFS wie Host-Aufnahmen um (Host-Faktor 2).
Geräte-dBFS = Datei-dBFS − 6,02 dB, wie bisher.

Läuft wegen CoreAudio nur außerhalb des Sandbox. Aufruf:
    uv run python tools/acdc_rec.py --list
    uv run python tools/acdc_rec.py --id B4-fx3i --test fx3i-open-inputs --reps 2 --duration 60 \\
        --device-desc "acdc1, Build v22.4.r-fx3i" --test-desc "A/B gegen 3d" --owl-read --analyze --ref B3-fx2d-r1
Ohne Gerät testen: `--simulate` (Rauschen + 1-kHz-Ton statt Gerät, mit `--manifest` auf eine Kopie). Mit
`--sine` landet das Ausgangssignal im simulierten Eingang (wie Patchkabel Out n → In n).
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
        why = "nicht gefunden" if not ok else "mehrdeutig"
        raise SystemExit(f"Gerät „{name}“ mit ≥ {n_in} in / ≥ {n_out} out {why}. Vorhanden:\n{lst}")
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
            raise SystemExit(f"--sine/--dc: mehr Werte als {n_out} Ausgänge")
        if freqs and len(levels_db) not in (1, len(freqs)):
            raise SystemExit("--sine-level: ein Wert für alle oder einer je Frequenz")
        for f in freqs:
            if not 0 <= f < fs / 2:
                raise SystemExit(f"--sine {f:g} Hz: erlaubt 0 (still) bis < fs/2")
        lv = (levels_db * len(freqs) if len(levels_db) == 1 else levels_db) if freqs else []
        if lv and max(lv) > 0:
            raise SystemExit("--sine-level über 0 dBFS")
        self.f = np.array(freqs + [0.0] * (n_out - len(freqs)))
        self.amp = np.array([10 ** (l / 20) if f > 0 else 0.0 for f, l in zip(freqs, lv)] + [0.0] * (n_out - len(freqs)))
        self.dc = np.array(dc + [0.0] * (n_out - len(dc)), dtype=float)
        peak = self.amp + np.abs(self.dc)
        if np.any(peak > 1.0 + 1e-9):
            bad = [f"Out {i + 1}: {p:.3f}" for i, p in enumerate(peak) if p > 1.0 + 1e-9]
            raise SystemExit(f"Sinus + Gleichanteil über Vollausschlag ({', '.join(bad)})")
        self.fs, self.fade, self.n = fs, max(1, int(round(fade_s * fs))), 0
        self.ramp = int(round(dc_ramp_s * fs))

    def describe(self) -> str:
        parts = []
        for i, (f, a, d) in enumerate(zip(self.f, self.amp, self.dc)):
            p = []
            if a > 0:
                p.append(f"Sinus {f:g} Hz @ {20 * np.log10(a):.1f} dBFS")
            if d != 0:
                p.append(f"DC {d:+.3f} FS" + (f" (Rampe {self.ramp / self.fs:g} s)" if self.ramp else ""))
            if p:
                parts.append(f"Out {i + 1} " + " + ".join(p))
        return "Testsignal " + ", ".join(parts)

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
                        raise SystemExit("Keine Daten vom Gerät seit 5 s – Stream hängt?")
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
        print(f"  owl_read → {out_dir} (Stream bleibt offen)", flush=True)
        r = subprocess.run(OWL_READ + ["--out", str(out_dir)], cwd=ROOT, capture_output=True, text=True)
        tail = (r.stdout + r.stderr).strip().splitlines()[-8:]
        for line in tail:
            print("    " + line)
        return {"rc": r.returncode, "out": str(out_dir)}
    return hook


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    g = ap.add_argument_group("Gerät und Stream")
    g.add_argument("--list", action="store_true", help="Audiogeräte auflisten und beenden")
    g.add_argument("--device", default="OWL-ACDC-FX", help="Gerätename (exakt oder Teilstring)")
    g.add_argument("--channels", type=int, default=4, help="Eingangskanäle")
    g.add_argument("--out-channels", type=int, default=4, help="Ausgangskanäle (bekommen Nullen)")
    g.add_argument("--input-only", action="store_true", help="nur Eingang öffnen (kein Duplex)")
    g.add_argument("--fs", type=int, default=48000)
    g.add_argument("--blocksize", type=int, default=256, help="Blockgröße (256, wie bei den frühen Aufnahmen)")
    g.add_argument("--latency", default="high", help="PortAudio-Latenz: low/high oder Sekunden")
    g.add_argument("--format", choices=sorted(FORMATS), default="pcm16")
    g.add_argument("--simulate", action="store_true", help="kein Gerät, synthetische Daten (Test)")
    o = ap.add_argument_group("Testsignal an die Ausgänge (statt Nullen)")
    o.add_argument("--sine", type=float, nargs="+", metavar="HZ",
                   help="Sinus je Ausgang in Reihenfolge Out 1, Out 2, …; 0 = still, fehlende = still")
    o.add_argument("--sine-level", type=float, nargs="+", default=[-6.0], metavar="DBFS",
                   help="Pegel in Geräte-dBFS, einer für alle oder einer je Frequenz (Standard −6 ≙ 5 V Spitze am Ausgang)")
    o.add_argument("--sine-fade", type=float, default=0.05, help="Einblenden in Sekunden")
    o.add_argument("--dc", type=float, nargs="+", metavar="FS",
                   help="Gleichanteil je Ausgang in Vollausschlag (−1…1, 1 = 0 dBFS ≈ 10 V), auch zusammen mit --sine; "
                        "sehr langsame Signale: --sine 0.05 …")
    o.add_argument("--dc-ramp", type=float, default=0.0, metavar="SEK",
                   help="Gleichanteil linear über SEK Sekunden von 0 hochfahren (Schwelle suchen), sonst wie --sine-fade")

    t = ap.add_argument_group("Ablauf")
    t.add_argument("--duration", type=float, default=60.0, help="Sekunden je Aufnahme")
    t.add_argument("--settle", type=float, default=3.0, help="Sekunden nach dem Öffnen verwerfen")
    t.add_argument("--reps", type=int, default=1, help="Anzahl Wiederholungen")
    t.add_argument("--first-rep", type=int, default=1, help="Nummer der ersten Wiederholung (Suffix -rN)")
    t.add_argument("--pause", type=float, default=5.0, help="Sekunden Pause zwischen Wiederholungen (Stream zu)")
    t.add_argument("--prompt", action="store_true", help="vor jeder Aufnahme auf Enter warten")
    t.add_argument("--owl-read", action="store_true", help="nach jeder Aufnahme, vor dem Schließen, owl_read.py")

    n = ap.add_argument_group("Name und Manifest")
    n.add_argument("--id", help="Manifest-ID (bei mehreren Wiederholungen + -rN)")
    n.add_argument("--test", help="Test-Teil des Dateinamens, z. B. fx3i-open-inputs")
    n.add_argument("--label", default="acdc1", help="Geräte-Teil des Dateinamens")
    n.add_argument("--gain", default="g12", help="Gain-Teil des Dateinamens")
    n.add_argument("--usb", default="usb-stream", help="USB-Teil des Dateinamens")
    n.add_argument("--date", default=dt.date.today().strftime("%Y%m%d"), help="Datum YYYYMMDD")
    n.add_argument("--dir", type=Path, default=ROOT / "recordings")
    n.add_argument("--manifest", type=Path, default=ROOT / "recordings" / "manifest.toml")
    n.add_argument("--no-manifest", action="store_true")
    n.add_argument("--device-desc", help="Manifest „device“ (Gerät + Firmware)")
    n.add_argument("--test-desc", help="Manifest „test“")
    n.add_argument("--usb-desc", help="Manifest „usb“ (Standard: Alltags-Kette + Stream-Art automatisch)")
    n.add_argument("--patch", default="Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme")
    n.add_argument("--title", help="Manifest „title“ (Standard: automatisch)")
    n.add_argument("--note", default="", help="zusätzlicher Notiztext")
    n.add_argument("--scale", type=float, default=2.0, help="Manifest „scale“ (2.0 = Datei-dBFS wie die frühen Aufnahmen, Host-Faktor 2)")

    x = ap.add_argument_group("Analyse")
    x.add_argument("--analyze", action="store_true", help="danach python -m analysis je Aufnahme")
    x.add_argument("--ref", nargs="+", help="Referenz für die Analyse (Manifest-ID oder Dateien)")
    x.add_argument("--spectrogram", action="store_true", help="Spektrogramm nicht überspringen")
    a = ap.parse_args()

    sd = None
    if not a.simulate or a.list:
        import sounddevice as sd  # erst hier: braucht CoreAudio (außerhalb des Sandbox)
    if a.list:
        print(sd.query_devices())
        return
    if not a.test:
        ap.error("--test fehlt (Test-Teil des Dateinamens)")
    if not a.no_manifest and not a.id:
        ap.error("--id fehlt (oder --no-manifest)")
    for part in (a.label, a.test, a.gain, a.usb, a.date):
        if not part or any(c in part for c in "/_ "):
            ap.error(f"Namensteil „{part}“: keine Leerzeichen, '/' oder '_'")

    signal = bool(a.sine or a.dc)
    if signal and a.input_only:
        ap.error("--sine/--dc brauchen den Ausgang, vertragen sich nicht mit --input-only")

    def make_gen():
        return SineOut(a.sine, a.sine_level, a.fs, a.out_channels, a.sine_fade, a.dc, a.dc_ramp) if signal else None

    make_gen()  # früh prüfen
    out_desc = ("nur Eingang" if a.input_only else "duplex, Ausgang "
                + (make_gen().describe() if signal else "Nullen"))
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
            raise SystemExit(f"{path} existiert schon – nie überschreiben")
        if mid in existing:
            raise SystemExit(f"Manifest-ID {mid} gibt es schon in {a.manifest}")

    dev = None
    if not a.simulate:
        dev = find_device(sd, a.device, a.channels, 0 if a.input_only else a.out_channels)
        info = sd.query_devices(dev)
        print(f"Gerät [{dev}] {info['name']}, {a.fs} Hz, Block {a.blocksize}, {a.format}, "
              f"{out_desc}")
    a.dir.mkdir(parents=True, exist_ok=True)

    done = []
    for i, (k, mid, path) in enumerate(plan):
        if i and a.pause > 0:
            print(f"Pause {a.pause:g} s (Stream geschlossen)")
            time.sleep(a.pause)
        if a.prompt:
            input(f"Enter startet Aufnahme {mid or path.name} … ")
        print(f"Aufnahme {mid or ''} → {path.name} ({a.duration:g} s + {a.settle:g} s Einschwingen)", flush=True)
        hook = owl_read_hook(ROOT / "out" / "owl_read" / (mid or path.stem)) if a.owl_read and not a.simulate else None
        gen = make_gen()
        take = Take(a, path, gen)
        try:
            res = take.run(sd, dev, hook)
        except KeyboardInterrupt:
            print(f"\nAbgebrochen. Unvollständige Datei bleibt liegen: {path} (kein Manifest-Eintrag)")
            sys.exit(130)
        flags = res["status"]
        print(f"  fertig: {res['frames']} Frames, Stream-Meldungen: {len(flags)}"
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
            print("Analyse:", " ".join(cmd[1:]), flush=True)
            subprocess.run(cmd, cwd=ROOT, check=False)


if __name__ == "__main__":
    main()
