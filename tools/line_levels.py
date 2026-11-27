"""Level of single lines per channel, measured right at the line frequency, for several recordings.

For each recording, channel and frequency: Hann window over the whole recording, the
spectrum on a fine grid (a quarter of the bin width), and the highest value within
±0.05 Hz (--search) of the nominal frequency counts. Level as sine amplitude in file dBFS
(no scaling from the manifest). The floor is the same measure taken at 42 places 5…25 Hz
beside the line, of these the median. Noise alone therefore gives a distance of ≈ 0 dB.

Recordings are WAV files, manifest IDs (recordings/manifest.toml, first file of the entry)
or <name>=<wav> to set the name in the table.

Usage:
  UV_CACHE_DIR=.uv-cache uv run python tools/line_levels.py B6b-osc-detuned B6b-knobs-12 \\
      --freqs 2200.95 4401.90 6602.85 6000 [--out reports/K1-session-table.md] [--json …]
"""
from __future__ import annotations

import argparse
import json
import tomllib
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.fft import next_fast_len

ROOT = Path(__file__).resolve().parent.parent


def resolve(arg: str, manifest: Path) -> tuple[str, Path]:
    """Manifest-ID oder WAV-Pfad → (Name, Pfad)."""
    if "=" in arg:                       # Name=Pfad
        name, _, path = arg.partition("=")
        return name, Path(path)
    p = Path(arg)
    if p.suffix.lower() == ".wav":
        return p.stem, p
    with open(manifest, "rb") as f:
        for m in tomllib.load(f).get("measurement", []):
            if m.get("id") == arg:
                return arg, manifest.parent / m["files"][0]
    raise SystemExit(f"Not a WAV file and not a manifest ID: {arg}")


def measure(path: Path, freqs: list[float], search: float, start: float, dur: float | None) -> dict:
    x, fs = sf.read(path, dtype="float64", always_2d=True)
    a = int(start * fs)
    x = x[a:a + int(dur * fs)] if dur else x[a:]
    n = len(x)
    w = np.hanning(n)
    cg = w.sum() / 2                       # Sinus der Amplitude 1 → 1
    nfft = next_fast_len(4 * n, real=True)  # Zero-Padding: Raster = ein Viertel der Bin-Breite
    mag = np.abs(np.fft.rfft(x * w[:, None], n=nfft, axis=0)) / cg   # (Raster, Kanäle)
    df = fs / nfft
    h = max(1, int(round(search / df)))

    def peak(f: float) -> tuple[np.ndarray, np.ndarray]:
        k = int(round(f / df))
        seg = mag[k - h:k + h + 1]
        i = seg.argmax(axis=0)
        return seg.max(axis=0), (k - h + i) * df

    out = {"file": str(path), "fs": fs, "seconds": n / fs, "search_hz": h * df, "lines": []}
    for f in freqs:
        lv, fp = peak(f)
        # Grundrauschen: dieselbe Messung (Maximum im gleichen Fenster) an 42 Stellen
        # 5…25 Hz neben der Linie, davon der Median. Rauschen allein ergibt so ≈ 0 dB Abstand.
        side = np.stack([peak(f + sgn * d)[0] for sgn in (-1, 1) for d in np.arange(5.0, 25.5, 1.0)])
        fl = np.median(side, axis=0)
        out["lines"].append({
            "f_nominal": f,
            "f_peak": [float(v) for v in fp],
            "level_db": [float(v) for v in 20 * np.log10(lv + 1e-30)],
            "floor_db": [float(v) for v in 20 * np.log10(fl + 1e-30)],
        })
    return out


def table(results: dict[str, dict], freqs: list[float], above: bool) -> str:
    """Markdown-Tabelle (deutsch, wie die anderen Tabellen in reports/)."""
    nch = len(next(iter(results.values()))["lines"][0]["level_db"])
    head = "| Aufnahme | Kanal | " + " | ".join(f"{f:g} Hz".replace(".", ",") for f in freqs) + " |"
    rows = [head, "|---|---|" + "---|" * len(freqs)]
    for name, r in results.items():
        for c in range(nch):
            cells = []
            for ln in r["lines"]:
                v = f"{ln['level_db'][c]:.1f}"
                if above:
                    v += f" ({int(round(ln['level_db'][c] - ln['floor_db'][c])):+d})"
                cells.append(v.replace(".", ",").replace("-", "−"))
            rows.append(f"| {'`' + name + '`' if c == 0 else ''} | {c + 1} | " + " | ".join(cells) + " |")
    return "\n".join(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("recordings", nargs="+", help="WAV files or manifest IDs")
    ap.add_argument("--freqs", type=float, nargs="+", required=True, help="line frequencies in Hz")
    ap.add_argument("--search", type=float, default=0.05, help="search range around each frequency in Hz (default 0.05)")
    ap.add_argument("--start", type=float, default=0.0, help="skip this many seconds at the start")
    ap.add_argument("--dur", type=float, help="use only this many seconds")
    ap.add_argument("--no-floor", action="store_true", help="do not add the distance to the floor in brackets")
    ap.add_argument("--manifest", type=Path, default=ROOT / "recordings" / "manifest.toml")
    ap.add_argument("--out", type=Path, help="write the table as Markdown")
    ap.add_argument("--json", type=Path, help="write all values as JSON")
    a = ap.parse_args(argv)

    results = {}
    for arg in a.recordings:
        name, path = resolve(arg, a.manifest)
        results[name] = measure(path, a.freqs, a.search, a.start, a.dur)
    txt = table(results, a.freqs, not a.no_floor)
    note = ("Pegel in Datei-dBFS direkt bei der Linienfrequenz (Hann über die ganze Aufnahme, "
            f"Maximum in ±{a.search:g} Hz)".replace(".", ",")
            + ("" if a.no_floor else ", in Klammern der Abstand zum Grundrauschen in dB") + ".")
    print(txt + "\n\n" + note)
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(txt + "\n\n" + note + "\n")
        print(f"Table: {a.out}")
    if a.json:
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
