# Report S2-3: S2-3 – acdc2, Eingänge offen, Gain 7 Uhr, 60 s

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc2 (DIY), Firmware v22.4.q |
| test | Eingänge offen (nichts gesteckt) |
| gain | g07 (Linksanschlag) |
| usb | usb-stream |
| patch | Slot 1: ACDC (Default-Patch, Knob = digitaler Gain) |
| Datei(en) | `20261114_acdc2_open-inputs_g7_usb-stream.4chan.000.wav` |
| Format | 96000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis S2-3 --ref S2-1` |

**Hinweise:**

- Datei ist digital stumm (< −150 dB). Beim Default-Patch heißt das: Gain auf 0, nach dem Patch kommt nichts mehr hinzu.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +0.0 | -194.0 | – | -194.0 | -218.1 | -300.0 | -300.0 | – | -194.0 | 0 % | -194.0 | 0.0 |
| Kanal 2 | +0.0 | -194.0 | – | -194.0 | -218.1 | -300.0 | -300.0 | – | -194.0 | 0 % | -194.0 | 0.0 |
| Kanal 3 | +0.0 | -300.0 | – | -300.0 | -300.0 | -300.0 | -300.0 | – | -300.0 | 0 % | -300.0 | 0.0 |
| Kanal 4 | +0.0 | -194.0 | – | -194.0 | -218.1 | -300.0 | -300.0 | – | -194.0 | 0 % | -194.0 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, 0,2–20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.00 | 3.02 s (0.33 Hz) | 50.2 |
| Kanal 1 | breitbandig | 0.00 | 3.02 s (0.33 Hz) | 50.2 |
| Kanal 2 | breitbandig | 0.00 | 3.02 s (0.33 Hz) | 50.2 |
| Kanal 2 | breitbandig | 0.00 | 3.02 s (0.33 Hz) | 50.2 |
| Kanal 3 | breitbandig | 0.00 | 2.87 s (0.35 Hz) | 48.6 |
| Kanal 3 | breitbandig | 0.00 | 2.87 s (0.35 Hz) | 48.6 |
| Kanal 4 | breitbandig | 0.00 | 3.02 s (0.33 Hz) | 50.2 |
| Kanal 4 | breitbandig | 0.00 | 3.02 s (0.33 Hz) | 50.2 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| Kanal 1 | 0 | 0.0 | – | – |
| Kanal 2 | 0 | 0.0 | – | – |
| Kanal 3 | 0 | 0.0 | – | – |
| Kanal 4 | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | Kanal 1 | Kanal 2 | Kanal 3 | Kanal 4 |
|---|---|---|---|---|
| Kanal 1 | 1.00 | 1.00 | 0.00 | 1.00 |
| Kanal 2 | 1.00 | 1.00 | 0.00 | 1.00 |
| Kanal 3 | 0.00 | 0.00 | 0.00 | 0.00 |
| Kanal 4 | 1.00 | 1.00 | 0.00 | 1.00 |

## Vergleich mit Referenz S2-1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -194.0 | -72.0 | -122.0 | 0 % | 79 % |
| Kanal 2 | -194.0 | -69.2 | -124.8 | 0 % | 87 % |
| Kanal 3 | -300.0 | -69.3 | -230.7 | 0 % | 84 % |
| Kanal 4 | -194.0 | -69.9 | -124.1 | 0 % | 90 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S2-3_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S2-3_psd.png)

### Zeitverlauf

![Zeitverlauf](S2-3_timeline.png)
