"""Aufnahmen laden: einzelne WAV-Dateien oder Messungen aus recordings/manifest.toml."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import soundfile as sf


@dataclass
class Recording:
    name: str
    fs: int
    data: np.ndarray  # (Samples, Kanäle), DC-Anteil abgezogen
    dc: np.ndarray  # DC-Anteil pro Kanal (1.0 = Vollaussteuerung)
    labels: list[str]
    files: list[Path]
    meta: dict = field(default_factory=dict)

    @property
    def duration(self) -> float:
        return self.data.shape[0] / self.fs

    @property
    def n_channels(self) -> int:
        return self.data.shape[1]


def load_files(paths, name=None, meta=None, labels=None, channels=None, scale=1.0) -> Recording:
    """Mono-Dateien werden in Reihenfolge zu Kanälen, Mehrkanal-Dateien liefern alle Kanäle.

    channels: optionale Auswahl (1-basiert, nach dem Zusammensetzen), z. B. [1], um leere
    Kanäle wegzulassen. Im Manifest als `channels = [1]`.
    scale: Faktor auf die Samples. Im Manifest als `scale = 2.0` bei Aufnahmen von
    `tools/acdc_rec.py`, damit sie in denselben Datei-dBFS stehen wie die frühen Aufnahmen über eine Host-Software
    (Host-Faktor 2, CLAUDE.md „Pegel-Offset der frühen Aufnahmen“).
    """
    paths = [Path(p) for p in paths]
    cols, fs = [], None
    for p in paths:
        x, sr = sf.read(p, always_2d=True, dtype="float64")
        if fs is None:
            fs = sr
        elif sr != fs:
            raise SystemExit(f"{p}: {sr} Hz, but the other files have {fs} Hz")
        cols.extend(x.T)
    n = min(len(c) for c in cols)
    data = np.stack([c[:n] for c in cols], axis=1)
    if channels:
        bad = [c for c in channels if not 1 <= c <= data.shape[1]]
        if bad:
            raise SystemExit(f"Channel {bad} does not exist, the recording has {data.shape[1]} channels")
        data = data[:, [c - 1 for c in channels]]
    if scale != 1.0:
        data = data * float(scale)
    dc = data.mean(axis=0)
    data = data - dc
    if not labels or len(labels) != data.shape[1]:
        labels = [f"Kanal {i + 1}" for i in range(data.shape[1])]
    return Recording(name or paths[0].stem, int(fs), data, dc, list(labels), paths, dict(meta or {}))


def load_manifest(path: Path) -> dict[str, dict]:
    with open(path, "rb") as fh:
        m = tomllib.load(fh)
    return {e["id"]: e for e in m.get("measurement", [])}


def resolve(inputs: list[str], manifest: Path) -> Recording:
    """Eine Manifest-ID (z. B. "M1") oder eine Liste von WAV-Dateien → Recording."""
    if len(inputs) == 1 and manifest.exists():
        entries = load_manifest(manifest)
        if inputs[0] in entries:
            e = entries[inputs[0]]
            files = [manifest.parent / f for f in e["files"]]
            return load_files(files, name=e["id"], meta=e, labels=e.get("channel_labels"), channels=e.get("channels"),
                              scale=e.get("scale", 1.0))
    missing = [p for p in inputs if not Path(p).exists()]
    if missing:
        raise SystemExit(f"Neither a manifest ID nor a file: {', '.join(missing)} (manifest: {manifest})")
    return load_files(inputs)
