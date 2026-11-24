# Report D91-slot1-umc-r2: D91-slot1-umc-r2 – acdc1 gnd-slot1-out1-via-umc, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-24 |
| device | UMC202HD In 1+2 ← acdc1 Out 1, acdc1 fx9a mit Masse-Draht Pin 15 ↔ Pin 33, ins Case geschraubt |
| test | Basislinie Ausgang mit Masse-Draht, AC/DC-Eingänge offen, Regler 63/64/71/50 |
| gain | g12 |
| usb | acdc1: usb-plugged, kein Stream. UMC: Hub |
| patch | Slot 1: ACDC (Default-Patch, Durchleitung In 1 → Out 1) |
| Datei(en) | `20261124_acdc1_gnd-slot1-out1-via-umc-r2_g12_usb-plugged.wav` |
| Format | 48000 Hz, 60.0 s, 2 Kanäle |
| Erzeugt mit | `uv run python -m analysis D91-slot1-umc-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +0.0 | -43.1 | -54.9 | -43.4 | -45.8 | -52.3 | -44.4 | -55.5 | -43.6 | 1 % | -43.7 | 0.0 |
| Kanal 2 | +0.0 | -43.7 | -55.4 | -44.0 | -46.4 | -53.0 | -45.0 | -56.1 | -44.2 | 1 % | -44.3 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| 1-kHz-Kamm | Kanal 1 | 1000.0528 | 0.0014 | 21/23 | k=16: 16000.845 Hz, -69.1 dB | -65.3 | 0.7 % |
| Netz 50 Hz | Kanal 1 | 50.0134 | 0.0027 | 6/19 | k=1: 50.013 Hz, -74.8 dB | -75.3 | 0.1 % |
| stärkste übrige Linie (75.74 Hz) | Kanal 1 | 75.7352 | 0.0000 | 2/315 | k=1: 75.735 Hz, -53.0 dB | -56.0 | 5.5 % |
| stärkste übrige Linie (13.79 Hz) | Kanal 1 | 13.7941 | 0.0010 | 3/1731 | k=1: 13.794 Hz, -62.9 dB | -65.9 | 0.6 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0528 | 0.0011 | 20/23 | k=16: 16000.845 Hz, -69.6 dB | -66.1 | 0.7 % |
| Netz 50 Hz | Kanal 2 | 50.0134 | 0.0031 | 6/19 | k=1: 50.013 Hz, -76.3 dB | -76.6 | 0.1 % |
| stärkste übrige Linie (75.74 Hz) | Kanal 2 | 75.7352 | 0.0000 | 2/315 | k=1: 75.735 Hz, -53.6 dB | -56.6 | 5.5 % |
| stärkste übrige Linie (13.79 Hz) | Kanal 2 | 13.7941 | 0.0008 | 3/1731 | k=1: 13.794 Hz, -63.4 dB | -66.4 | 0.6 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 75.735 | -53.0 | 33.0 | other1·1 |
| 13.794 | -62.9 | 22.2 | other2·1 |
| 89.532 | -65.0 | 32.3 | – |
| 7385.985 | -65.4 | 36.3 | – |
| 1215.415 | -66.0 | 32.9 | – |
| 6621.918 | -66.8 | 35.6 | – |
| 12002.225 | -65.8 | 37.0 | – |
| 18003.339 | -67.5 | 36.3 | – |
| 6001.113 | -68.8 | 33.5 | – |
| 6552.662 | -68.7 | 33.5 | – |
| 16000.845 | -69.1 | 33.9 | usb1k·16 |
| 7681.424 | -68.8 | 33.6 | – |
| 3840.712 | -70.1 | 32.1 | – |
| 18677.041 | -69.3 | 34.4 | – |
| 9635.600 | -71.3 | 31.0 | – |
| 8000.424 | -70.4 | 31.9 | usb1k·8 |
| 12154.153 | -71.5 | 32.1 | – |
| 4000.211 | -71.0 | 30.6 | usb1k·4 |
| 14498.254 | -71.5 | 31.9 | – |
| 2000.106 | -71.2 | 30.1 | usb1k·2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 75.735 | -53.6 | 33.0 | other1·1 |
| 13.794 | -63.4 | 22.5 | other2·1 |
| 89.532 | -65.6 | 32.3 | – |
| 7385.985 | -66.0 | 36.3 | – |
| 1215.415 | -66.6 | 32.9 | – |
| 6621.918 | -67.4 | 35.7 | – |
| 18003.339 | -67.9 | 36.5 | – |
| 12002.225 | -67.9 | 35.6 | – |
| 6552.662 | -69.3 | 33.6 | – |
| 16000.845 | -69.6 | 33.8 | usb1k·16 |
| 7681.424 | -69.4 | 33.6 | – |
| 3840.712 | -70.7 | 32.1 | – |
| 18677.041 | -69.9 | 34.3 | – |
| 9635.600 | -71.9 | 30.9 | – |
| 8000.424 | -70.9 | 31.9 | usb1k·8 |
| 12154.153 | -72.1 | 32.1 | – |
| 14498.254 | -72.1 | 32.0 | – |
| 28.147 | -72.3 | 16.7 | – |
| 82.633 | -72.9 | 21.7 | – |
| 14771.970 | -72.7 | 31.6 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| usb1k | Kanal 1 | 11/11 | 0.27 | 0.01 | 0.16 |
| mains50 | Kanal 1 | 11/11 | 187.39 | -142.23 | 0.46 |
| other1 | Kanal 1 | 11/11 | 15.11 | 15.50 | 0.62 |
| other2 | Kanal 1 | 11/11 | 1117.13 | 628.79 | 1.50 |
| usb1k | Kanal 2 | 11/11 | 0.69 | -0.22 | 0.19 |
| mains50 | Kanal 2 | 11/11 | 183.22 | -217.90 | 0.37 |
| other1 | Kanal 2 | 11/11 | 14.62 | 15.67 | 0.63 |
| other2 | Kanal 2 | 11/11 | 1101.43 | 938.15 | 1.45 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.64 | 0.07 s (13.78 Hz) | 12.5 |
| Kanal 1 | 75.7 Hz ± 10 | 4.69 | 1.76 s (0.57 Hz) | 23.6 |
| Kanal 2 | breitbandig | 0.64 | 0.07 s (13.78 Hz) | 12.3 |
| Kanal 2 | 75.7 Hz ± 10 | 4.71 | 0.14 s (6.90 Hz) | 23.4 |

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

![Spektrogramm](D91-slot1-umc-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D91-slot1-umc-r2_psd.png)

### Kammprofile

![Kammprofile](D91-slot1-umc-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](D91-slot1-umc-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm24, tools/acdc_rec.py (Gerät UMC202HD 192k, nur Eingang, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:42:19. Stream-Meldungen: 0. Stream zwischen den Wiederholungen geschlossen und neu geöffnet. messlog D91
