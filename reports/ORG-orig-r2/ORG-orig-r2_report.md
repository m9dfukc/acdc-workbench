# Report ORG-orig-r2: ORG-orig-r2 – acdc1 original-open-inputs-orga, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1, Werks-Firmware AC/DC v22.5.0 (Hack-Branch, Readback 433b3fd3) |
| test | Original-Sitzung: Werks-Firmware in der Mitte, Eingänge offen, Regler 12 Uhr (69/56/72/56, nicht bewegt), Aufnahme nach dem VCA des Default-Patches |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), VCA wirkt auf die USB-Aufnahme, Gain-Korrektur über den DC-Offset (D26) |
| Datei(en) | `20261123_acdc1_original-open-inputs-orga-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis ORG-orig-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.8 | -68.7 | -76.2 | -69.6 | -70.8 | -82.3 | -70.0 | -91.9 | -69.6 | 59 % | -73.5 | 3.9 |
| Kanal 2 | -5.5 | -72.9 | -80.6 | -73.7 | -75.0 | -86.9 | -74.2 | -95.0 | -73.8 | 63 % | -78.1 | 4.4 |
| Kanal 3 | -6.9 | -70.7 | -81.7 | -71.0 | -72.3 | -87.5 | -71.4 | -95.7 | -71.0 | 79 % | -77.8 | 6.8 |
| Kanal 4 | -4.8 | -72.1 | -79.9 | -72.8 | -73.9 | -87.1 | -73.3 | -99.3 | -72.9 | 65 % | -77.5 | 4.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.6 dB | -76.3 | 21.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.9 | 37.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0020 | 10/10 | k=1: 2320.542 Hz, -114.6 dB | -111.5 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0021 | 127 | k=15·f1+1·f2: 20998.015 Hz, -99.2 dB | -89.6 | 1.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7235 | 0.0014 | 5/315 | k=1: 75.721 Hz, -90.6 dB | -93.6 | 0.4 % |
| stärkste übrige Linie (51.09 Hz) | Kanal 1 | 51.0949 | 0.0146 | 5/467 | k=1: 51.093 Hz, -96.3 dB | -96.9 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.9 dB | -79.7 | 25.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0004 | 23/23 | k=1: 999.868 Hz, -76.5 dB | -78.1 | 36.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0014 | 10/10 | k=1: 2320.543 Hz, -118.7 dB | -115.0 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0010 | 132 | k=15·f1+1·f2: 20998.015 Hz, -102.9 dB | -93.1 | 1.2 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7235 | 0.0013 | 3/315 | k=1: 75.721 Hz, -92.4 dB | -95.5 | 0.7 % |
| stärkste übrige Linie (89.51 Hz) | Kanal 2 | 89.5105 | 0.0027 | 3/266 | k=1: 89.514 Hz, -102.1 dB | -104.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -75.9 dB | -75.5 | 35.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.4 dB | -74.8 | 41.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5449 | 0.0013 | 10/10 | k=1: 2320.543 Hz, -114.6 dB | -109.9 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0017 | 152 | k=15·f1+1·f2: 20998.015 Hz, -98.4 dB | -88.8 | 1.7 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7235 | 0.0089 | 4/315 | k=1: 75.721 Hz, -93.9 dB | -96.9 | 0.3 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9261 | 0.0000 | 1/1 | k=1: 23000.926 Hz, -98.9 dB | -102.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.0 dB | -79.8 | 20.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.4 | 44.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0021 | 10/10 | k=1: 2320.543 Hz, -118.3 dB | -114.0 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0012 | 123 | k=7·f1+2·f2: 18999.074 Hz, -103.0 dB | -93.2 | 0.9 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7235 | 0.0018 | 4/315 | k=1: 75.721 Hz, -98.5 dB | -101.7 | 0.1 % |
| stärkste übrige Linie (89.51 Hz) | Kanal 4 | 89.5105 | 0.0025 | 3/266 | k=1: 89.515 Hz, -100.4 dB | -103.0 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 55.4 | usb1k·1 |
| 6000.000 | -76.6 | 55.5 | fs8·1 |
| 12000.000 | -78.9 | 55.2 | fs8·2 |
| 18000.000 | -79.3 | 55.2 | fs8·3 |
| 2999.603 | -81.1 | 49.3 | usb1k·3 |
| 1999.735 | -81.2 | 47.6 | usb1k·2 |
| 6999.074 | -87.0 | 44.8 | usb1k·7 |
| 9998.677 | -89.7 | 43.4 | usb1k·10 |
| 75.721 | -90.6 | 30.9 | other1·1 |
| 4999.339 | -90.5 | 40.8 | usb1k·5 |
| 13998.148 | -91.7 | 42.3 | usb1k·14 |
| 21997.089 | -92.5 | 42.5 | usb1k·22 |
| 5999.206 | -93.0 | 39.0 | usb1k·6 |
| 15997.883 | -93.8 | 40.4 | usb1k·16 |
| 14998.015 | -94.0 | 40.6 | usb1k·15 |
| 3999.471 | -94.1 | 36.5 | usb1k·4 |
| 20997.221 | -94.4 | 40.8 | usb1k·21 |
| 16997.750 | -95.0 | 39.7 | usb1k·17 |
| 8998.809 | -93.7 | 39.5 | usb1k·9 |
| 17997.619 | -95.9 | 38.7 | usb1k·18 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -76.5 | 55.9 | usb1k·1 |
| 6000.000 | -79.9 | 57.0 | fs8·1 |
| 12000.000 | -82.3 | 56.5 | fs8·2 |
| 18000.000 | -82.8 | 55.8 | fs8·3 |
| 2999.603 | -85.1 | 50.0 | usb1k·3 |
| 1999.735 | -86.0 | 47.7 | usb1k·2 |
| 6999.074 | -91.1 | 45.7 | usb1k·7 |
| 75.721 | -92.4 | 34.6 | other1·1 |
| 9998.677 | -93.7 | 43.8 | usb1k·10 |
| 13998.147 | -95.9 | 43.0 | usb1k·14 |
| 4999.339 | -95.7 | 40.8 | usb1k·5 |
| 21997.089 | -96.1 | 43.0 | usb1k·22 |
| 14998.015 | -97.2 | 42.0 | usb1k·15 |
| 15997.883 | -98.4 | 40.2 | usb1k·16 |
| 5999.206 | -97.7 | 39.2 | usb1k·6 |
| 20997.222 | -98.4 | 41.0 | usb1k·21 |
| 3999.471 | -98.6 | 36.9 | usb1k·4 |
| 16997.750 | -99.1 | 39.9 | usb1k·17 |
| 17997.619 | -99.5 | 39.1 | usb1k·18 |
| 8998.809 | -98.1 | 39.7 | usb1k·9 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.4 | 59.3 | usb1k·1 |
| 6000.000 | -75.9 | 61.1 | fs8·1 |
| 12000.000 | -77.8 | 60.6 | fs8·2 |
| 18000.000 | -78.5 | 59.4 | fs8·3 |
| 2999.603 | -81.7 | 53.8 | usb1k·3 |
| 1999.735 | -82.7 | 50.5 | usb1k·2 |
| 6999.074 | -87.2 | 49.2 | usb1k·7 |
| 9998.677 | -90.0 | 46.4 | usb1k·10 |
| 13998.147 | -92.1 | 45.8 | usb1k·14 |
| 21997.089 | -92.2 | 46.7 | usb1k·22 |
| 14998.015 | -93.0 | 45.9 | usb1k·15 |
| 4999.339 | -92.9 | 43.4 | usb1k·5 |
| 75.721 | -93.9 | 32.9 | other1·1 |
| 15997.883 | -94.7 | 43.5 | usb1k·16 |
| 20997.222 | -94.2 | 44.2 | usb1k·21 |
| 17997.618 | -95.2 | 42.7 | usb1k·18 |
| 5999.206 | -94.7 | 42.3 | usb1k·6 |
| 16997.750 | -95.6 | 43.1 | usb1k·17 |
| 3999.471 | -95.5 | 40.3 | usb1k·4 |
| 8998.809 | -94.4 | 43.6 | usb1k·9 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 57.1 | usb1k·1 |
| 6000.000 | -80.0 | 56.2 | fs8·1 |
| 12000.000 | -82.5 | 55.5 | fs8·2 |
| 18000.000 | -82.7 | 55.0 | fs8·3 |
| 1999.735 | -83.3 | 49.6 | usb1k·2 |
| 2999.603 | -84.0 | 50.7 | usb1k·3 |
| 6999.074 | -90.3 | 45.7 | usb1k·7 |
| 4999.339 | -92.0 | 43.6 | usb1k·5 |
| 9998.676 | -92.7 | 44.3 | usb1k·10 |
| 13998.147 | -94.7 | 43.0 | usb1k·14 |
| 5999.206 | -95.0 | 41.2 | usb1k·6 |
| 3999.471 | -96.1 | 38.8 | usb1k·4 |
| 15997.883 | -96.6 | 40.9 | usb1k·16 |
| 21997.089 | -95.8 | 42.4 | usb1k·22 |
| 16997.750 | -97.9 | 40.3 | usb1k·17 |
| 8998.809 | -96.3 | 40.7 | usb1k·9 |
| 14998.015 | -97.9 | 40.2 | usb1k·15 |
| 20997.222 | -97.7 | 41.1 | usb1k·21 |
| 75.721 | -98.5 | 27.5 | other1·1 |
| 17997.619 | -99.6 | 38.0 | usb1k·18 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.22 | 0.19 | 0.04 |
| led | Kanal 1 | 11/11 | 1.84 | -0.85 | 1.01 |
| other1 | Kanal 1 | 11/11 | 15.29 | -4.44 | 0.45 |
| other2 | Kanal 1 | 11/11 | 0.74 | -0.99 | 2.15 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.23 | 0.21 | 0.04 |
| led | Kanal 2 | 11/11 | 2.10 | -1.76 | 0.84 |
| other1 | Kanal 2 | 11/11 | 8.15 | 6.56 | 0.23 |
| other2 | Kanal 2 | 11/11 | 5.29 | 14.51 | 0.89 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.16 | 0.16 | 0.03 |
| led | Kanal 3 | 11/11 | 1.24 | 0.35 | 0.40 |
| other1 | Kanal 3 | 11/11 | 3.86 | 7.76 | 0.44 |
| other2 | Kanal 3 | 11/11 | 0.05 | 0.02 | 0.08 |
| fs8 | Kanal 4 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.20 | 0.21 | 0.04 |
| led | Kanal 4 | 11/11 | 0.94 | -2.11 | 0.89 |
| other1 | Kanal 4 | 11/11 | 26.30 | -41.39 | 0.56 |
| other2 | Kanal 4 | 11/11 | 3.64 | 6.26 | 0.61 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.92 | 0.16 s (6.40 Hz) | 19.5 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 0.31 s (3.20 Hz) | 27.1 |
| Kanal 2 | breitbandig | 0.87 | 0.16 s (6.40 Hz) | 21.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 26.9 |
| Kanal 3 | breitbandig | 0.50 | 1.25 s (0.80 Hz) | 20.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 31.7 |
| Kanal 4 | breitbandig | 0.82 | 0.16 s (6.40 Hz) | 21.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 26.1 |

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
| Kanal 1 | 1.00 | 0.95 | 0.92 | 0.93 |
| Kanal 2 | 0.95 | 1.00 | 0.92 | 0.94 |
| Kanal 3 | 0.92 | 0.92 | 1.00 | 0.91 |
| Kanal 4 | 0.93 | 0.94 | 0.91 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](ORG-orig-r2_psd.png)

### Kammprofile

![Kammprofile](ORG-orig-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](ORG-orig-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:01:18. Stream-Meldungen: 0. owl_read: reports/owl_read/ORG-orig-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. acdc1 im Case. Flash firmware/flashlog/20261123_original-orga, :leave, A1. Messlog D86.
