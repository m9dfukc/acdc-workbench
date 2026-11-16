"""Markdown-Report und JSON-Export."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


def _f(v, fmt="{:.1f}", none="–"):
    return none if v is None or (isinstance(v, float) and not np.isfinite(v)) else fmt.format(v)


def write_json(data: dict, path: Path):
    def conv(o):
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, Path):
            return str(o)
        raise TypeError(type(o))

    path.write_text(json.dumps(data, indent=1, ensure_ascii=False, default=conv))


def write_markdown(d: dict, path: Path, images: dict[str, Path]):
    m, ch = d["meta"], d["channels"]
    labels = [c["label"] for c in ch]
    L = [f"# Report {d['name']}: {m.get('title', '')}", ""]
    L += ["| Feld | Wert |", "|---|---|"]
    for k in ("date", "device", "test", "gain", "usb", "patch"):
        if m.get(k):
            L.append(f"| {k} | {m[k]} |")
    L.append(f"| Datei(en) | {', '.join('`' + Path(f).name + '`' for f in d['files'])} |")
    L.append(f"| Format | {d['fs']} Hz, {d['duration_s']:.1f} s, {len(ch)} Kanäle |")
    L.append(f"| Erzeugt mit | `{d['command']}` |")
    L.append("")
    if d["warnings"]:
        L += ["**Hinweise:**", ""] + [f"- {w}" for w in d["warnings"]] + [""]
    L += ["Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). "
          "Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. "
          "RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). "
          "Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / "
          "Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). "
          "Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.", ""]

    L += ["## Kennzahlen pro Kanal", "",
          "| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | "
          "Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in ch:
        r = c["result"]
        lf = r["bands_db"]["20–200 Hz"]
        L.append(f"| {c['label']} | {c['dc'] * 100:+.1f} | {r['rms_total_db']:.1f} | {_f(r['drift_db'] if r['drift_db'] > -250 else None)} | "
                 f"{r['rms_db']:.1f} | {r['rms_a_db']:.1f} | "
                 f"{lf:.1f} | {r['bands_db']['200 Hz–20 kHz']:.1f} | {_f(r['other_rms_db'] if r['other_rms_db'] > -250 else None)} | "
                 f"{r['noise_rms_db']:.1f} | {r['lines_share'] * 100:.0f} % | "
                 f"{r['rest_rms_db']:.1f} | {r['notch_gain_db']:.1f} |")
    L.append("")

    L += ["## Linienfamilien (Kämme)", "",
          "f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom "
          "Raster k·f0.", "",
          "| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |",
          "|---|---|---|---|---|---|---|---|"]
    for c in ch:
        for fam in c["result"]["families"]:
            strongest = max(fam["harmonics"], key=lambda h: h["level_db"])
            L.append(f"| {fam['label']} | {c['label']} | {fam['f0']:.4f} | {fam['resid_rms_hz']:.4f} | "
                     f"{fam['n']}{'/' + str(fam['kmax_searched']) if fam['kmax_searched'] else ''} | k={strongest['k']}: {strongest['freq']:.3f} Hz, "
                     f"{strongest['level_db']:.1f} dB | {fam['rms_db']:.1f} | {fam['share'] * 100:.1f} % |")
    L.append("")

    L += ["## Stärkste Linien (Kanal für Kanal)", ""]
    for c in ch:
        L += [f"### {c['label']}", "", "| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |",
              "|---|---|---|---|"]
        for p in c["result"]["peaks"][:20]:
            L.append(f"| {p['freq']:.3f} | {p['level_db']:.1f} | {p['snr_db']:.1f} | {p['family'] or '–'} |")
        L.append("")

    L += ["## Zeitverhalten", "",
          f"Fensterlänge {_f(d['stability_win_s'])} s, 50 % Überlappung.", "",
          "| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |",
          "|---|---|---|---|---|---|"]
    for c in ch:
        for key, s in c["stability"].items():
            L.append(f"| {key} | {c['label']} | {s['valid']}/{s['windows']} | {_f(s.get('f0_std_ppm'), '{:.2f}')} | "
                     f"{_f(s.get('f0_slope_ppm_per_min'), '{:.2f}')} | {_f(s.get('level_std_db'), '{:.2f}')} |")
    L += ["", "**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):", "",
          "| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |", "|---|---|---|---|---|"]
    for c in ch:
        for mod in c["modulation"]:
            if mod:
                band = "breitbandig" if mod["band_hz"] is None else f"{mod['band_hz']:.1f} Hz ± 10"
                L.append(f"| {c['label']} | {band} | {mod['depth_std_db']:.2f} | {mod['period_s']:.2f} s "
                         f"({mod['peak_hz']:.2f} Hz) | {mod['prominence_db']:.1f} |")
    L += ["", "Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.", "",
          "**Klicks** (Hochpass, Schwelle Median + 8·MAD):", "",
          "| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |", "|---|---|---|---|---|"]
    for c in ch:
        k = c["clicks"]
        L.append(f"| {c['label']} | {k['n']} | {k['per_min']:.1f} | {_f(k['interval_median_s'], '{:.3f}')} | "
                 f"{_f(k['interval_cv'], '{:.2f}')} |")
    L.append("")

    L += ["## Korrelation zwischen Kanälen", "", "| | " + " | ".join(labels) + " |",
          "|---" * (len(labels) + 1) + "|"]
    for i, lab in enumerate(labels):
        L.append(f"| {lab} | " + " | ".join(f"{v:.2f}" for v in d["correlation"][i]) + " |")
    L.append("")

    if d.get("ref"):
        r = d["ref"]
        L += [f"## Vergleich mit Referenz {r['name']}", "",
              "| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |", "|---|---|---|---|---|---|"]
        for c, rc in zip(ch, r["channels"]):
            a, b = c["result"], rc["result"]
            L.append(f"| {c['label']} | {a['rms_db']:.1f} | {b['rms_db']:.1f} | {a['rms_db'] - b['rms_db']:+.1f} | "
                     f"{a['lines_share'] * 100:.0f} % | {b['lines_share'] * 100:.0f} % |")
        L.append("")

    L += ["## Abbildungen", ""]
    for title, p in images.items():
        if p:
            L += [f"### {title}", "", f"![{title}]({p.name})", ""]
    if m.get("note"):
        L += ["## Notiz aus dem Manifest", ""] + [f"> {line}" for line in m["note"].splitlines()] + [""]
    path.write_text("\n".join(L))
