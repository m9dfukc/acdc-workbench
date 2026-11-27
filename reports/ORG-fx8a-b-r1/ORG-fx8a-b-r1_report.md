# Report ORG-fx8a-b-r1: ORG-fx8a-b-r1 – acdc1 fx8a-open-inputs-orgb, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1, Build 10 v22.4.r-fx8a |
| test | Original-Sitzung: fx8a am Ende, Eingänge offen, Regler 12 Uhr (69/56/72/56, nicht bewegt), rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-orgb-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis ORG-fx8a-b-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.0 | -70.3 | -74.9 | -72.1 | -72.8 | -85.9 | -72.4 | -93.7 | -72.1 | 68 % | -77.2 | 5.0 |
| Kanal 2 | -7.4 | -71.2 | -76.2 | -72.9 | -73.5 | -88.1 | -73.1 | -93.9 | -72.9 | 73 % | -78.5 | 5.7 |
| Kanal 3 | -5.6 | -72.6 | -77.4 | -74.4 | -75.0 | -92.5 | -74.6 | -94.8 | -74.4 | 83 % | -82.0 | 7.6 |
| Kanal 4 | -6.5 | -70.9 | -77.7 | -71.9 | -72.4 | -88.3 | -72.1 | -94.2 | -71.9 | 76 % | -78.1 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -82.9 dB | -82.1 | 10.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.5 | 58.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0024 | 11 | k=-1·f1+1·f2: 5000.128 Hz, -118.8 dB | -114.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -96.9 dB | -95.5 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.8 dB | -98.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.0 dB | -82.2 | 11.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.0 | 61.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0024 | 14 | k=-1·f1+1·f2: 5000.125 Hz, -118.8 dB | -114.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -95.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -98.6 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.8 dB | -82.7 | 14.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -76.1 | 68.1 % |
| Netz 50 Hz | Kanal 3 | 50.0168 | 0.0029 | 3/19 | k=1: 50.017 Hz, -114.9 dB | -113.9 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0018 | 33 | k=-3·f1+4·f2: 21000.397 Hz, -121.7 dB | -112.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.0 dB | -96.6 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0003 | 3/3 | k=2: 12000.000 Hz, -83.2 dB | -82.3 | 9.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -73.7 | 66.9 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0025 | 16 | k=-1·f1+1·f2: 5000.132 Hz, -116.2 dB | -111.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.0 dB | -96.0 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -98.3 dB | -98.9 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 57.6 | usb1k·1 |
| 1999.735 | -81.3 | 51.4 | usb1k·2 |
| 2999.603 | -82.0 | 51.7 | usb1k·3 |
| 12000.000 | -82.9 | 55.0 | fs8·2 |
| 6000.000 | -83.3 | 52.8 | fs8·1 |
| 18000.000 | -86.0 | 52.6 | fs8·3 |
| 3999.471 | -87.4 | 47.7 | usb1k·4 |
| 9998.677 | -88.2 | 48.1 | usb1k·10 |
| 15997.883 | -90.3 | 48.1 | usb1k·16 |
| 4999.339 | -90.7 | 44.4 | usb1k·5 |
| 6999.074 | -90.3 | 45.9 | usb1k·7 |
| 16997.751 | -92.6 | 46.1 | usb1k·17 |
| 8998.809 | -91.2 | 45.9 | usb1k·9 |
| 18997.487 | -93.5 | 45.1 | usb1k·19 |
| 20997.222 | -94.3 | 45.3 | usb1k·21 |
| 11998.412 | -95.7 | 42.0 | usb1k·12 |
| 13998.148 | -96.3 | 41.8 | usb1k·14 |
| 5999.206 | -95.8 | 40.3 | usb1k·6 |
| 2000.000 | -96.9 | 35.7 | other1·1 |
| 12998.280 | -96.7 | 41.3 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 58.0 | usb1k·1 |
| 1999.735 | -82.1 | 52.1 | usb1k·2 |
| 2999.603 | -82.3 | 53.0 | usb1k·3 |
| 12000.000 | -83.0 | 56.3 | fs8·2 |
| 6000.000 | -83.3 | 54.3 | fs8·1 |
| 18000.000 | -86.1 | 53.6 | fs8·3 |
| 3999.471 | -87.6 | 48.8 | usb1k·4 |
| 9998.677 | -88.2 | 49.0 | usb1k·10 |
| 15997.883 | -90.7 | 49.2 | usb1k·16 |
| 4999.338 | -91.2 | 45.3 | usb1k·5 |
| 6999.074 | -90.8 | 46.6 | usb1k·7 |
| 16997.751 | -92.8 | 46.8 | usb1k·17 |
| 8998.809 | -91.7 | 46.6 | usb1k·9 |
| 18997.487 | -93.4 | 46.5 | usb1k·19 |
| 20997.222 | -94.6 | 45.5 | usb1k·21 |
| 11998.412 | -96.0 | 43.3 | usb1k·12 |
| 12998.280 | -96.7 | 42.2 | usb1k·13 |
| 13998.148 | -97.2 | 42.1 | usb1k·14 |
| 17997.619 | -97.2 | 42.4 | usb1k·18 |
| 14998.015 | -97.3 | 42.3 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 60.6 | usb1k·1 |
| 1999.735 | -83.3 | 55.4 | usb1k·2 |
| 2999.603 | -83.3 | 56.4 | usb1k·3 |
| 12000.000 | -83.8 | 58.6 | fs8·2 |
| 6000.000 | -83.8 | 57.7 | fs8·1 |
| 18000.000 | -86.4 | 55.8 | fs8·3 |
| 3999.471 | -88.3 | 52.3 | usb1k·4 |
| 9998.677 | -88.6 | 51.4 | usb1k·10 |
| 15997.883 | -91.1 | 51.3 | usb1k·16 |
| 4999.338 | -91.7 | 48.6 | usb1k·5 |
| 6999.074 | -91.7 | 49.7 | usb1k·7 |
| 16997.751 | -93.3 | 49.4 | usb1k·17 |
| 8998.809 | -92.4 | 49.7 | usb1k·9 |
| 18997.487 | -93.6 | 48.7 | usb1k·19 |
| 20997.222 | -95.4 | 46.4 | usb1k·21 |
| 11998.412 | -96.3 | 46.0 | usb1k·12 |
| 12998.280 | -96.9 | 45.4 | usb1k·13 |
| 17997.619 | -97.5 | 44.8 | usb1k·18 |
| 14998.016 | -97.8 | 44.7 | usb1k·15 |
| 5999.206 | -98.0 | 43.5 | usb1k·6 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 59.2 | usb1k·1 |
| 1999.735 | -80.3 | 53.8 | usb1k·2 |
| 2999.604 | -81.5 | 53.7 | usb1k·3 |
| 12000.000 | -83.2 | 55.3 | fs8·2 |
| 6000.000 | -83.3 | 53.7 | fs8·1 |
| 18000.000 | -86.4 | 52.6 | fs8·3 |
| 3999.471 | -87.0 | 49.0 | usb1k·4 |
| 9998.677 | -88.2 | 48.6 | usb1k·10 |
| 15997.883 | -90.3 | 48.9 | usb1k·16 |
| 4999.339 | -90.2 | 45.7 | usb1k·5 |
| 6999.074 | -90.1 | 46.8 | usb1k·7 |
| 8998.809 | -90.9 | 46.8 | usb1k·9 |
| 16997.751 | -92.4 | 46.6 | usb1k·17 |
| 18997.487 | -93.7 | 45.3 | usb1k·19 |
| 20997.222 | -93.9 | 45.3 | usb1k·21 |
| 13998.148 | -95.3 | 43.3 | usb1k·14 |
| 5999.206 | -94.7 | 42.3 | usb1k·6 |
| 11998.412 | -95.5 | 42.9 | usb1k·12 |
| 7998.942 | -94.9 | 42.0 | usb1k·8 |
| 12998.279 | -96.9 | 41.5 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.02 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.21 | 0.06 | 0.10 |
| other1 | Kanal 1 | 11/11 | 1.57 | 4.06 | 0.06 |
| other2 | Kanal 1 | 11/11 | 0.21 | 0.14 | 0.19 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.22 | 0.08 | 0.11 |
| other1 | Kanal 2 | 11/11 | 2.16 | 4.23 | 0.07 |
| other2 | Kanal 2 | 11/11 | 0.17 | 0.02 | 0.14 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.21 | 0.03 | 0.09 |
| mains50 | Kanal 3 | 11/11 | 251.16 | -304.75 | 2.94 |
| other1 | Kanal 3 | 11/11 | 0.22 | -0.15 | 0.10 |
| other2 | Kanal 3 | 11/11 | 0.09 | -0.02 | 0.12 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.03 | 0.06 |
| usb1k | Kanal 4 | 11/11 | 0.19 | 0.08 | 0.15 |
| other1 | Kanal 4 | 11/11 | 1.83 | 2.93 | 0.06 |
| other2 | Kanal 4 | 11/11 | 0.20 | -0.00 | 0.18 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.63 | 0.31 s (3.18 Hz) | 23.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 37.3 |
| Kanal 2 | breitbandig | 1.44 | 0.31 s (3.18 Hz) | 24.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 38.1 |
| Kanal 3 | breitbandig | 1.49 | 0.31 s (3.18 Hz) | 23.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 41.8 |
| Kanal 4 | breitbandig | 1.05 | 0.31 s (3.18 Hz) | 22.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 37.9 |

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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.96 | 0.96 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.96 | 0.93 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](ORG-fx8a-b-r1_psd.png)

### Kammprofile

![Kammprofile](ORG-fx8a-b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](ORG-fx8a-b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:03:21. Stream-Meldungen: 0. owl_read: reports/owl_read/ORG-fx8a-b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. acdc1 im Case. Flash firmware/flashlog/20261123_build10-fx8a-nach-original, :leave, A1, danach Program Change auf Slot 1. Messlog D86.
