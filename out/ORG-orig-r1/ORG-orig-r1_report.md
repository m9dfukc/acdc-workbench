# Report ORG-orig-r1: ORG-orig-r1 – acdc1 original-open-inputs-orga, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1, Werks-Firmware AC/DC v22.5.0 (Hack-Branch, Readback 433b3fd3) |
| test | Original-Sitzung: Werks-Firmware in der Mitte, Eingänge offen, Regler 12 Uhr (69/56/72/56, nicht bewegt), Aufnahme nach dem VCA des Default-Patches |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), VCA wirkt auf die USB-Aufnahme, Gain-Korrektur über den DC-Offset (D26) |
| Datei(en) | `20261123_acdc1_original-open-inputs-orga-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis ORG-orig-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.8 | -68.1 | -73.4 | -69.6 | -70.8 | -82.2 | -70.1 | -93.5 | -69.6 | 59 % | -73.5 | 3.9 |
| Kanal 2 | -5.5 | -72.2 | -77.5 | -73.7 | -75.0 | -86.7 | -74.3 | -94.0 | -73.8 | 64 % | -78.2 | 4.4 |
| Kanal 3 | -6.9 | -70.3 | -78.7 | -71.0 | -72.3 | -87.3 | -71.4 | -96.4 | -71.0 | 79 % | -77.8 | 6.7 |
| Kanal 4 | -4.8 | -71.5 | -77.0 | -72.9 | -74.0 | -86.9 | -73.3 | -98.1 | -72.9 | 66 % | -77.5 | 4.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.5 dB | -76.3 | 21.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0008 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.9 | 37.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0017 | 10/10 | k=1: 2320.548 Hz, -114.8 dB | -110.9 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0019 | 127 | k=15·f1+1·f2: 20998.016 Hz, -99.3 dB | -89.6 | 1.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7205 | 0.0171 | 4/315 | k=1: 75.722 Hz, -91.3 dB | -94.3 | 0.3 % |
| stärkste übrige Linie (89.51 Hz) | Kanal 1 | 89.5105 | 0.0051 | 3/266 | k=1: 89.514 Hz, -99.4 dB | -101.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.9 dB | -79.7 | 25.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0008 | 23/23 | k=1: 999.868 Hz, -76.5 dB | -78.1 | 36.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5449 | 0.0016 | 10/10 | k=1: 2320.547 Hz, -118.7 dB | -114.8 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0011 | 133 | k=15·f1+1·f2: 20998.015 Hz, -102.9 dB | -93.1 | 1.2 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7171 | 0.0034 | 2/315 | k=1: 75.721 Hz, -91.9 dB | -95.0 | 0.8 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 2 | 44.7608 | 0.0142 | 7/533 | k=1: 44.758 Hz, -100.0 dB | -101.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -75.8 dB | -75.5 | 35.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0013 | 23/23 | k=1: 999.868 Hz, -73.4 dB | -74.9 | 41.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0008 | 10/10 | k=1: 2320.546 Hz, -115.0 dB | -110.1 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0015 | 151 | k=15·f1+1·f2: 20998.015 Hz, -98.5 dB | -88.8 | 1.7 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7220 | 0.0030 | 3/315 | k=1: 75.722 Hz, -94.5 dB | -97.7 | 0.2 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9262 | 0.0000 | 1/1 | k=1: 23000.926 Hz, -99.0 dB | -102.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.0 dB | -79.8 | 20.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0008 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -76.4 | 44.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0014 | 10/10 | k=1: 2320.547 Hz, -117.5 dB | -113.5 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0012 | 128 | k=15·f1+1·f2: 20998.015 Hz, -103.0 dB | -93.2 | 0.9 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7161 | 0.0076 | 3/315 | k=1: 75.721 Hz, -97.5 dB | -100.5 | 0.2 % |
| stärkste übrige Linie (13.79 Hz) | Kanal 4 | 13.7970 | 0.0186 | 6/1731 | k=1: 13.795 Hz, -98.6 dB | -101.9 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 55.4 | usb1k·1 |
| 6000.000 | -76.5 | 55.6 | fs8·1 |
| 12000.000 | -78.9 | 55.5 | fs8·2 |
| 18000.000 | -79.4 | 55.6 | fs8·3 |
| 2999.603 | -81.0 | 49.3 | usb1k·3 |
| 1999.736 | -81.3 | 47.6 | usb1k·2 |
| 6999.074 | -87.1 | 45.4 | usb1k·7 |
| 9998.676 | -89.7 | 43.7 | usb1k·10 |
| 4999.339 | -91.0 | 40.7 | usb1k·5 |
| 75.722 | -91.3 | 29.1 | other1·1 |
| 13998.148 | -91.7 | 42.7 | usb1k·14 |
| 21997.089 | -92.7 | 42.8 | usb1k·22 |
| 5999.206 | -92.8 | 39.3 | usb1k·6 |
| 14998.015 | -93.7 | 41.0 | usb1k·15 |
| 15997.883 | -93.9 | 40.8 | usb1k·16 |
| 3999.471 | -93.7 | 37.6 | usb1k·4 |
| 20997.222 | -94.1 | 40.9 | usb1k·21 |
| 8998.809 | -93.6 | 39.5 | usb1k·9 |
| 16997.751 | -95.3 | 39.5 | usb1k·17 |
| 17997.618 | -95.5 | 39.4 | usb1k·18 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -76.5 | 56.2 | usb1k·1 |
| 6000.000 | -79.9 | 57.0 | fs8·1 |
| 12000.000 | -82.4 | 56.4 | fs8·2 |
| 18000.000 | -82.9 | 56.6 | fs8·3 |
| 2999.603 | -85.1 | 50.1 | usb1k·3 |
| 1999.735 | -86.0 | 47.8 | usb1k·2 |
| 75.721 | -91.9 | 33.7 | other1·1 |
| 6999.074 | -91.2 | 46.2 | usb1k·7 |
| 9998.676 | -93.7 | 44.2 | usb1k·10 |
| 13998.148 | -95.9 | 43.5 | usb1k·14 |
| 4999.339 | -96.2 | 40.7 | usb1k·5 |
| 14998.015 | -96.9 | 42.3 | usb1k·15 |
| 21997.089 | -96.2 | 43.2 | usb1k·22 |
| 5999.206 | -97.4 | 39.4 | usb1k·6 |
| 15997.883 | -98.5 | 40.9 | usb1k·16 |
| 3999.471 | -98.1 | 38.1 | usb1k·4 |
| 20997.222 | -98.2 | 40.7 | usb1k·21 |
| 17997.618 | -99.0 | 40.5 | usb1k·18 |
| 8998.809 | -98.0 | 40.1 | usb1k·9 |
| 16997.751 | -99.5 | 39.7 | usb1k·17 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.4 | 59.6 | usb1k·1 |
| 6000.000 | -75.8 | 61.1 | fs8·1 |
| 12000.000 | -77.9 | 60.6 | fs8·2 |
| 18000.000 | -78.6 | 59.9 | fs8·3 |
| 2999.603 | -81.6 | 53.6 | usb1k·3 |
| 1999.735 | -82.8 | 50.7 | usb1k·2 |
| 6999.074 | -87.3 | 49.8 | usb1k·7 |
| 9998.676 | -90.0 | 47.1 | usb1k·10 |
| 13998.148 | -92.1 | 46.4 | usb1k·14 |
| 14998.015 | -92.8 | 46.2 | usb1k·15 |
| 21997.089 | -92.3 | 46.1 | usb1k·22 |
| 4999.339 | -93.4 | 43.2 | usb1k·5 |
| 20997.222 | -94.0 | 43.8 | usb1k·21 |
| 15997.883 | -94.8 | 43.8 | usb1k·16 |
| 17997.618 | -94.9 | 43.7 | usb1k·18 |
| 75.722 | -94.5 | 31.3 | other1·1 |
| 5999.206 | -94.5 | 42.3 | usb1k·6 |
| 3999.471 | -95.1 | 41.1 | usb1k·4 |
| 8998.809 | -94.3 | 43.7 | usb1k·9 |
| 16997.751 | -95.9 | 42.6 | usb1k·17 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 57.4 | usb1k·1 |
| 6000.000 | -80.0 | 56.0 | fs8·1 |
| 12000.000 | -82.5 | 55.6 | fs8·2 |
| 18000.000 | -82.9 | 55.2 | fs8·3 |
| 1999.736 | -83.4 | 49.9 | usb1k·2 |
| 2999.603 | -83.9 | 50.5 | usb1k·3 |
| 6999.074 | -90.5 | 45.8 | usb1k·7 |
| 4999.339 | -92.4 | 43.6 | usb1k·5 |
| 9998.677 | -92.7 | 44.6 | usb1k·10 |
| 13998.147 | -94.7 | 43.4 | usb1k·14 |
| 5999.206 | -94.8 | 41.2 | usb1k·6 |
| 3999.471 | -95.8 | 39.8 | usb1k·4 |
| 15997.883 | -96.6 | 41.3 | usb1k·16 |
| 21997.089 | -96.0 | 42.4 | usb1k·22 |
| 8998.809 | -96.3 | 40.8 | usb1k·9 |
| 14998.015 | -97.7 | 40.3 | usb1k·15 |
| 75.721 | -97.5 | 28.2 | other1·1 |
| 20997.222 | -97.6 | 40.3 | usb1k·21 |
| 16997.751 | -98.2 | 39.7 | usb1k·17 |
| 17997.618 | -99.2 | 38.9 | usb1k·18 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.02 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.13 | 0.13 | 0.03 |
| led | Kanal 1 | 11/11 | 4.27 | -8.11 | 0.91 |
| other1 | Kanal 1 | 11/11 | 114.63 | 101.21 | 0.57 |
| other2 | Kanal 1 | 11/11 | 0.41 | -0.78 | 1.66 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.02 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.13 | 0.13 | 0.02 |
| led | Kanal 2 | 11/11 | 4.42 | 2.60 | 0.72 |
| other1 | Kanal 2 | 11/11 | 145.45 | 296.98 | 0.31 |
| other2 | Kanal 2 | 11/11 | 174.46 | 96.28 | 0.86 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.10 | 0.05 | 0.02 |
| led | Kanal 3 | 11/11 | 0.95 | 0.14 | 0.45 |
| other1 | Kanal 3 | 11/11 | 47.02 | -59.23 | 0.44 |
| other2 | Kanal 3 | 11/11 | 0.07 | 0.02 | 0.23 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.03 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.09 | 0.12 | 0.02 |
| led | Kanal 4 | 11/11 | 2.23 | -0.93 | 0.63 |
| other1 | Kanal 4 | 11/11 | 99.26 | 206.32 | 0.58 |
| other2 | Kanal 4 | 11/11 | 1.28 | 0.45 | 3.85 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.29 | 0.16 s (6.38 Hz) | 29.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 0.31 s (3.20 Hz) | 27.4 |
| Kanal 2 | breitbandig | 1.25 | 0.16 s (6.38 Hz) | 31.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 27.0 |
| Kanal 3 | breitbandig | 0.70 | 0.16 s (6.38 Hz) | 28.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 31.4 |
| Kanal 4 | breitbandig | 1.19 | 0.16 s (6.38 Hz) | 30.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 25.5 |

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
| Kanal 1 | 1.00 | 0.95 | 0.93 | 0.94 |
| Kanal 2 | 0.95 | 1.00 | 0.92 | 0.95 |
| Kanal 3 | 0.93 | 0.92 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.95 | 0.91 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](ORG-orig-r1_psd.png)

### Kammprofile

![Kammprofile](ORG-orig-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](ORG-orig-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:00:05. Stream-Meldungen: 0. owl_read: out/owl_read/ORG-orig-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. acdc1 im Case. Flash firmware/flashlog/20261123_original-orga, :leave, A1. Messlog D86.
