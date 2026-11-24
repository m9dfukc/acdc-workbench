# Report D91-slot1-umc-r1: D91-slot1-umc-r1 – acdc1 gnd-slot1-out1-via-umc, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-24 |
| device | UMC202HD In 1+2 ← acdc1 Out 1, acdc1 fx9a mit Masse-Draht Pin 15 ↔ Pin 33, ins Case geschraubt |
| test | Basislinie Ausgang mit Masse-Draht, AC/DC-Eingänge offen, Regler 63/64/71/50 |
| gain | g12 |
| usb | acdc1: usb-plugged, kein Stream. UMC: Hub |
| patch | Slot 1: ACDC (Default-Patch, Durchleitung In 1 → Out 1) |
| Datei(en) | `20261124_acdc1_gnd-slot1-out1-via-umc-r1_g12_usb-plugged.wav` |
| Format | 48000 Hz, 60.0 s, 2 Kanäle |
| Erzeugt mit | `uv run python -m analysis D91-slot1-umc-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +0.0 | -43.0 | -54.7 | -43.3 | -45.7 | -52.2 | -44.2 | -55.1 | -43.6 | 1 % | -43.6 | 0.0 |
| Kanal 2 | +0.0 | -43.6 | -55.2 | -43.9 | -46.3 | -52.9 | -44.8 | -55.7 | -44.2 | 1 % | -44.2 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| 1-kHz-Kamm | Kanal 1 | 1000.0528 | 0.0008 | 20/23 | k=16: 16000.845 Hz, -69.0 dB | -65.1 | 0.7 % |
| Netz 50 Hz | Kanal 1 | 50.0148 | 0.0016 | 7/19 | k=1: 50.013 Hz, -74.5 dB | -74.5 | 0.1 % |
| stärkste übrige Linie (75.74 Hz) | Kanal 1 | 75.7322 | 0.0025 | 2/315 | k=1: 75.736 Hz, -52.8 dB | -55.6 | 5.8 % |
| stärkste übrige Linie (13.80 Hz) | Kanal 1 | 13.7756 | 0.0176 | 8/1730 | k=1: 13.798 Hz, -62.5 dB | -64.5 | 0.8 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0528 | 0.0006 | 20/23 | k=16: 16000.845 Hz, -69.5 dB | -65.9 | 0.7 % |
| Netz 50 Hz | Kanal 2 | 50.0147 | 0.0015 | 6/19 | k=1: 50.014 Hz, -76.1 dB | -75.9 | 0.1 % |
| stärkste übrige Linie (75.74 Hz) | Kanal 2 | 75.7322 | 0.0026 | 2/315 | k=1: 75.736 Hz, -53.4 dB | -56.2 | 5.8 % |
| stärkste übrige Linie (13.80 Hz) | Kanal 2 | 13.7701 | 0.0217 | 6/1730 | k=1: 13.798 Hz, -63.0 dB | -64.9 | 0.8 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 75.736 | -52.8 | 41.7 | other1·1 |
| 13.798 | -62.5 | 22.9 | other2·1 |
| 7385.987 | -65.6 | 35.9 | – |
| 89.533 | -66.0 | 27.0 | – |
| 1215.415 | -66.1 | 35.0 | – |
| 12002.228 | -66.0 | 37.1 | – |
| 6621.920 | -66.7 | 35.6 | – |
| 18003.343 | -67.4 | 36.2 | – |
| 6001.115 | -69.0 | 33.4 | – |
| 3840.713 | -69.1 | 29.1 | – |
| 6552.664 | -69.4 | 33.4 | – |
| 16000.845 | -69.0 | 33.7 | usb1k·16 |
| 11.421 | -69.5 | 15.4 | – |
| 14.056 | -69.2 | 16.2 | – |
| 7681.426 | -68.7 | 33.5 | – |
| 18677.045 | -70.1 | 33.8 | – |
| 18.220 | -70.4 | 16.1 | – |
| 4000.211 | -70.4 | 27.9 | usb1k·4 |
| 8000.422 | -70.8 | 31.0 | usb1k·8 |
| 14498.257 | -70.9 | 31.9 | – |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 75.736 | -53.4 | 41.8 | other1·1 |
| 13.798 | -63.0 | 23.0 | other2·1 |
| 7385.987 | -66.2 | 36.0 | – |
| 89.533 | -66.5 | 27.1 | – |
| 1215.415 | -66.7 | 34.9 | – |
| 6621.920 | -67.4 | 35.4 | – |
| 12002.228 | -68.1 | 35.4 | – |
| 18003.343 | -68.0 | 36.2 | – |
| 3840.713 | -69.7 | 29.1 | – |
| 6552.664 | -70.0 | 33.5 | – |
| 16000.845 | -69.5 | 33.9 | usb1k·16 |
| 14.056 | -69.6 | 16.4 | – |
| 11.421 | -70.2 | 15.3 | – |
| 7681.426 | -69.2 | 33.5 | – |
| 18677.045 | -70.7 | 33.8 | – |
| 18.220 | -71.0 | 16.3 | – |
| 8000.422 | -71.3 | 31.0 | usb1k·8 |
| 14498.257 | -71.5 | 32.0 | – |
| 1000.053 | -72.4 | 26.5 | usb1k·1 |
| 9635.604 | -72.4 | 31.0 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| usb1k | Kanal 1 | 11/11 | 0.24 | -0.06 | 0.22 |
| mains50 | Kanal 1 | 11/11 | 317.13 | 1017.91 | 0.80 |
| other1 | Kanal 1 | 11/11 | 45.52 | 82.90 | 0.88 |
| other2 | Kanal 1 | 11/11 | 492.87 | -607.26 | 1.89 |
| usb1k | Kanal 2 | 11/11 | 0.23 | -0.04 | 0.19 |
| mains50 | Kanal 2 | 11/11 | 316.24 | 1013.95 | 0.80 |
| other1 | Kanal 2 | 11/11 | 45.56 | 89.65 | 0.87 |
| other2 | Kanal 2 | 11/11 | 482.26 | -391.91 | 1.96 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.66 | 0.07 s (13.80 Hz) | 12.6 |
| Kanal 1 | 75.7 Hz ± 10 | 2.91 | 0.14 s (6.90 Hz) | 22.6 |
| Kanal 2 | breitbandig | 0.67 | 0.07 s (13.80 Hz) | 12.4 |
| Kanal 2 | 75.7 Hz ± 10 | 2.91 | 0.14 s (6.90 Hz) | 22.6 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| Kanal 1 | 0 | 0.0 | – | – |
| Kanal 2 | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | Kanal 1 | Kanal 2 |
|---|---|---|
| Kanal 1 | 1.00 | 1.00 |
| Kanal 2 | 1.00 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](D91-slot1-umc-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D91-slot1-umc-r1_psd.png)

### Kammprofile

![Kammprofile](D91-slot1-umc-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](D91-slot1-umc-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm24, tools/acdc_rec.py (Gerät UMC202HD 192k, nur Eingang, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:41:10. Stream-Meldungen: 0. Stream zwischen den Wiederholungen geschlossen und neu geöffnet. messlog D91
