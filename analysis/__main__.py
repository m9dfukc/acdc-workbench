"""CLI: uv run python -m analysis <Manifest-ID | WAV-Dateien …> [Optionen]

Beispiele:
  uv run python -m analysis M1
  uv run python -m analysis M2 --ref M1
  uv run python -m analysis recordings/20261120_acdc1_open-inputs_g12_usb-stream.wav
"""

from __future__ import annotations

import argparse
import shlex
import sys
from pathlib import Path

import numpy as np

from . import plots, timing
from .audio_io import resolve
from .lines import analyse_channel, upsampling_check
from .report import write_json, write_markdown


def analyse(rec, device_fs, top, win_s, mains=50.0, with_timing=True):
    channels = []
    for c in range(rec.n_channels):
        x = rec.data[:, c]
        res = analyse_channel(x, rec.fs, device_fs, top=top, mains=mains)
        entry = {"label": rec.labels[c], "dc": float(rec.dc[c]), "result": res}
        if with_timing:
            series, summary = timing.stability(x, rec.fs, res["families"], win_s)
            strongest = max(res["families"], key=lambda f: f["ms"], default=None)
            band = max(strongest["harmonics"], key=lambda h: h["level_db"])["freq"] if strongest else None
            clk, env = timing.clicks(x, rec.fs)
            entry.update(stability=summary, stability_series=series, clicks=clk, _env=env,
                         modulation=[timing.modulation(x, rec.fs), timing.modulation(x, rec.fs, band)])
        channels.append(entry)
    return channels


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m analysis", description="AC/DC noise analysis (docs/03).")
    ap.add_argument("inputs", nargs="+", help="Manifest ID (e.g. M1) or one or more WAV files")
    ap.add_argument("--manifest", type=Path, default=Path("recordings/manifest.toml"))
    ap.add_argument("--out", type=Path, default=Path("reports"), help="Base directory, results go to <out>/<name>/")
    ap.add_argument("--name", help="Name of the result directory (default: manifest ID or file name)")
    ap.add_argument("--ref", nargs="+", help="Reference (manifest ID or files) to overlay and compare")
    ap.add_argument("--device-fs", type=float, default=48000.0, help="Nominal sample rate of the AC/DC [Hz]")
    ap.add_argument("--mains", type=float, default=50.0, help="Mains frequency [Hz]")
    ap.add_argument("--top", type=int, default=40, help="Number of lines in the peak list")
    ap.add_argument("--win", type=float, default=10.0,
                    help="Window length for the time behaviour [s]. ≥ 10 s keeps lines 0.3 Hz apart separated")
    ap.add_argument("--vmin", type=float, help="Lower limit of the spectrogram colour scale [dBFS]")
    ap.add_argument("--vmax", type=float, help="Upper limit of the spectrogram colour scale [dBFS]")
    ap.add_argument("--no-spectrogram", action="store_true", help="Skip the spectrogram (faster)")
    a = ap.parse_args(argv)

    rec = resolve(a.inputs, a.manifest)
    name = a.name or rec.name
    out = a.out / name
    out.mkdir(parents=True, exist_ok=True)
    print(f"{name}: {rec.n_channels} channels, {rec.fs} Hz, {rec.duration:.1f} s → {out}/")

    warnings = []
    up = upsampling_check(rec.data[:, 0], rec.fs, a.device_fs)
    if up and up["resampled"]:
        warnings.append(f"Datei hat {rec.fs} Hz, oberhalb {a.device_fs / 2:g} Hz ist nichts drin "
                        f"({up['above_device_nyquist_db']:.0f} dB) → von {a.device_fs:g} Hz hochgerechnet.")
    if rec.duration < 30:
        warnings.append(f"Nur {rec.duration:.1f} s. Für Zeitverhalten und Klicks sind ≥ 60 s vorgesehen.")
    if np.max(np.abs(rec.data + rec.dc)) >= 0.999:
        warnings.append("Clipping: Samples an der Vollaussteuerung.")

    channels = analyse(rec, a.device_fs, a.top, a.win, a.mains)
    ref_data = None
    ref = None
    if a.ref:
        ref = resolve(a.ref, a.manifest)
        ref_data = {"name": ref.name, "channels": analyse(ref, a.device_fs, a.top, a.win, a.mains, with_timing=False)}

    results = [c["result"] for c in channels]
    silent = all(r["rms_total_db"] < -150 for r in results)
    if silent:
        warnings.append("Datei ist digital stumm (< −150 dB). Beim Default-Patch heißt das: Gain auf 0, "
                        "nach dem Patch kommt nichts mehr hinzu.")
    elif any(r["other_rms_db"] > r["rms_db"] - 3 for r in results):
        warnings.append("Ein Nutzsignal (übrige Linien) dominiert. Störanteil und Notch-Gewinn sind dann nicht "
                        "aussagekräftig, Störlinien in absoluten dBFS vergleichen.")
    images = {
        "Spektrogramm": None if a.no_spectrogram else plots.spectrogram_grid(
            rec, results, out / f"{name}_spectrogram.png", a.vmin, a.vmax),
        "Langzeit-Spektrum": plots.psd_plot(rec, results, out / f"{name}_psd.png", ref,
                                            [c["result"] for c in ref_data["channels"]] if ref_data else None),
        "Kammprofile": plots.comb_profile(rec, results, out / f"{name}_combs.png"),
        "Zeitverlauf": plots.timeline(rec, [(c["stability_series"], c["stability"]) for c in channels],
                                      [c["_env"] for c in channels], [c["clicks"] for c in channels],
                                      out / f"{name}_timeline.png"),
    }
    with np.errstate(invalid="ignore", divide="ignore"):
        corr = np.nan_to_num(np.corrcoef(rec.data.T)) if rec.n_channels > 1 else np.ones((1, 1))
    data = {
        "name": name, "meta": rec.meta, "files": [str(f) for f in rec.files], "fs": rec.fs,
        "duration_s": rec.duration, "device_fs": a.device_fs,
        "command": "uv run python -m analysis " + shlex.join(sys.argv[1:] if argv is None else argv),
        "warnings": warnings, "upsampling": up, "correlation": corr,
        "stability_win_s": timing.window_length(rec.duration, a.win),
        "channels": [{k: v for k, v in c.items() if not k.startswith("_") and k != "stability_series"}
                     for c in channels],
        "ref": ref_data,
    }
    write_json(data, out / f"{name}.json")
    write_markdown(data, out / f"{name}_report.md", images)

    for w in warnings:
        print("  Note:", w)
    for c in channels:
        r = c["result"]
        fams = ", ".join(f"{f['key']} {f['f0']:.4f} Hz ({f['n']}×, {f['share'] * 100:.0f} %)" for f in r["families"])
        print(f"  {c['label']}: RMS {r['rms_db']:.1f} dB, interference share {r['lines_share'] * 100:.0f} %, "
              f"notch gain {r['notch_gain_db']:.1f} dB, clicks {c['clicks']['n']} | {fams}")
    print(f"  Report: {out / f'{name}_report.md'}")


if __name__ == "__main__":
    main()
