# Report ORG-fx8a-b-r2: ORG-fx8a-b-r2 – acdc1 fx8a-open-inputs-orgb, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1, Build 10 v22.4.r-fx8a |
| test | Original-Sitzung: fx8a am Ende, Eingänge offen, Regler 12 Uhr (69/56/72/56, nicht bewegt), rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-orgb-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis ORG-fx8a-b-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.5 | -75.1 | -72.3 | -73.1 | -86.1 | -72.6 | -93.6 | -72.3 | 67 % | -77.2 | 4.9 |
| Kanal 2 | -7.4 | -71.2 | -75.8 | -73.0 | -73.8 | -88.1 | -73.3 | -93.9 | -73.1 | 71 % | -78.5 | 5.4 |
| Kanal 3 | -5.7 | -73.6 | -81.1 | -74.5 | -75.2 | -92.8 | -74.7 | -94.8 | -74.6 | 82 % | -82.1 | 7.5 |
| Kanal 4 | -6.5 | -70.5 | -75.5 | -72.2 | -72.7 | -88.2 | -72.4 | -94.2 | -72.2 | 74 % | -78.1 | 5.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -82.9 dB | -82.1 | 10.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.8 | 57.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0054 | 9 | k=-7·f1+4·f2: 17000.928 Hz, -118.8 dB | -114.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.1 dB | -95.5 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -97.6 dB | -98.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.0 dB | -82.2 | 12.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.4 | 59.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0048 | 15 | k=-7·f1+4·f2: 17000.930 Hz, -118.7 dB | -113.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -95.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.0 dB | -98.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.7 dB | -82.8 | 15.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.1 dB | -76.3 | 67.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0054 | 32 | k=-7·f1+4·f2: 17000.929 Hz, -119.2 dB | -112.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.0 dB | -96.6 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.2 dB | -82.4 | 9.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.7 dB | -74.1 | 64.7 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0064 | 19 | k=25·f1-4·f2: 996.679 Hz, -115.7 dB | -110.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.0 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.3 dB | -98.7 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 58.6 | usb1k·1 |
| 1999.735 | -81.8 | 51.2 | usb1k·2 |
| 2999.603 | -82.3 | 52.2 | usb1k·3 |
| 12000.000 | -82.9 | 55.1 | fs8·2 |
| 6000.000 | -83.4 | 52.3 | fs8·1 |
| 18000.000 | -86.0 | 52.8 | fs8·3 |
| 3999.471 | -87.3 | 46.6 | usb1k·4 |
| 9998.677 | -88.2 | 49.1 | usb1k·10 |
| 15997.883 | -90.4 | 48.0 | usb1k·16 |
| 4999.339 | -90.4 | 44.9 | usb1k·5 |
| 6999.074 | -90.4 | 45.4 | usb1k·7 |
| 16997.751 | -92.8 | 45.8 | usb1k·17 |
| 8998.809 | -91.7 | 45.8 | usb1k·9 |
| 18997.486 | -93.5 | 45.2 | usb1k·19 |
| 20997.222 | -94.2 | 44.7 | usb1k·21 |
| 13998.148 | -96.3 | 41.7 | usb1k·14 |
| 11998.412 | -96.0 | 41.9 | usb1k·12 |
| 14998.015 | -96.9 | 41.4 | usb1k·15 |
| 5999.207 | -95.9 | 39.9 | usb1k·6 |
| 2000.000 | -97.1 | 35.9 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 59.1 | usb1k·1 |
| 1999.735 | -82.7 | 51.5 | usb1k·2 |
| 2999.603 | -82.8 | 53.2 | usb1k·3 |
| 12000.000 | -83.0 | 56.2 | fs8·2 |
| 6000.000 | -83.4 | 53.5 | fs8·1 |
| 18000.000 | -86.1 | 53.5 | fs8·3 |
| 3999.471 | -87.6 | 47.9 | usb1k·4 |
| 9998.677 | -88.2 | 50.0 | usb1k·10 |
| 15997.883 | -90.7 | 48.9 | usb1k·16 |
| 4999.339 | -91.0 | 45.7 | usb1k·5 |
| 6999.074 | -90.8 | 46.4 | usb1k·7 |
| 16997.751 | -93.0 | 46.2 | usb1k·17 |
| 8998.809 | -92.1 | 46.2 | usb1k·9 |
| 18997.486 | -93.3 | 46.6 | usb1k·19 |
| 20997.222 | -94.6 | 45.6 | usb1k·21 |
| 14998.015 | -96.7 | 42.7 | usb1k·15 |
| 11998.412 | -96.3 | 42.9 | usb1k·12 |
| 13998.147 | -97.0 | 42.3 | usb1k·14 |
| 17997.619 | -97.1 | 42.5 | usb1k·18 |
| 12998.280 | -97.1 | 41.7 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.1 | 62.2 | usb1k·1 |
| 12000.000 | -83.7 | 58.6 | fs8·2 |
| 6000.000 | -83.8 | 57.1 | fs8·1 |
| 2999.603 | -83.7 | 56.6 | usb1k·3 |
| 1999.735 | -83.8 | 55.3 | usb1k·2 |
| 18000.000 | -86.5 | 55.8 | fs8·3 |
| 3999.471 | -88.2 | 51.6 | usb1k·4 |
| 9998.677 | -88.5 | 52.4 | usb1k·10 |
| 15997.883 | -91.2 | 51.1 | usb1k·16 |
| 4999.339 | -91.4 | 49.4 | usb1k·5 |
| 6999.074 | -91.8 | 49.3 | usb1k·7 |
| 16997.751 | -93.5 | 48.4 | usb1k·17 |
| 18997.486 | -93.7 | 48.8 | usb1k·19 |
| 8998.809 | -92.7 | 48.9 | usb1k·9 |
| 20997.222 | -95.3 | 46.7 | usb1k·21 |
| 11998.412 | -96.7 | 45.6 | usb1k·12 |
| 14998.015 | -97.2 | 45.0 | usb1k·15 |
| 12998.280 | -97.1 | 45.6 | usb1k·13 |
| 17997.619 | -97.4 | 44.6 | usb1k·18 |
| 13998.147 | -98.7 | 43.7 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.7 | 60.2 | usb1k·1 |
| 1999.735 | -80.7 | 52.9 | usb1k·2 |
| 2999.603 | -81.9 | 53.7 | usb1k·3 |
| 12000.000 | -83.2 | 55.1 | fs8·2 |
| 6000.000 | -83.7 | 52.8 | fs8·1 |
| 18000.000 | -86.2 | 52.5 | fs8·3 |
| 3999.471 | -87.0 | 48.5 | usb1k·4 |
| 9998.677 | -88.4 | 49.5 | usb1k·10 |
| 15997.883 | -90.1 | 48.4 | usb1k·16 |
| 4999.339 | -89.9 | 46.4 | usb1k·5 |
| 6999.074 | -89.9 | 46.8 | usb1k·7 |
| 8998.809 | -91.2 | 46.5 | usb1k·9 |
| 16997.751 | -92.7 | 46.2 | usb1k·17 |
| 18997.486 | -93.6 | 45.9 | usb1k·19 |
| 20997.222 | -93.9 | 45.3 | usb1k·21 |
| 13998.148 | -95.0 | 43.5 | usb1k·14 |
| 5999.207 | -94.8 | 41.6 | usb1k·6 |
| 11998.412 | -95.6 | 42.6 | usb1k·12 |
| 14998.015 | -97.2 | 41.7 | usb1k·15 |
| 7998.941 | -96.0 | 40.8 | usb1k·8 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.03 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.18 | -0.11 | 0.04 |
| other1 | Kanal 1 | 11/11 | 1.33 | -2.45 | 0.12 |
| other2 | Kanal 1 | 11/11 | 0.19 | -0.01 | 0.22 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.03 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.17 | -0.04 | 0.05 |
| other1 | Kanal 2 | 11/11 | 1.33 | -2.47 | 0.14 |
| other2 | Kanal 2 | 11/11 | 0.17 | 0.04 | 0.22 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.02 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.21 | -0.02 | 0.04 |
| other1 | Kanal 3 | 11/11 | 0.65 | -1.19 | 0.11 |
| other2 | Kanal 3 | 11/11 | 0.12 | -0.08 | 0.16 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.13 | -0.11 | 0.05 |
| other1 | Kanal 4 | 11/11 | 1.11 | -0.13 | 0.13 |
| other2 | Kanal 4 | 11/11 | 0.22 | 0.13 | 0.23 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.48 | 0.16 s (6.40 Hz) | 30.5 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 37.2 |
| Kanal 2 | breitbandig | 1.44 | 0.16 s (6.40 Hz) | 32.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 38.3 |
| Kanal 3 | breitbandig | 0.88 | 0.31 s (3.18 Hz) | 29.6 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 41.1 |
| Kanal 4 | breitbandig | 1.30 | 0.16 s (6.40 Hz) | 33.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.9 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.96 |
| Kanal 2 | 0.97 | 1.00 | 0.93 | 0.97 |
| Kanal 3 | 0.93 | 0.93 | 1.00 | 0.93 |
| Kanal 4 | 0.96 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](ORG-fx8a-b-r2_psd.png)

### Kammprofile

![Kammprofile](ORG-fx8a-b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](ORG-fx8a-b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:04:35. Stream-Meldungen: 0. owl_read: reports/owl_read/ORG-fx8a-b-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. acdc1 im Case. Flash firmware/flashlog/20261123_build10-fx8a-nach-original, :leave, A1, danach Program Change auf Slot 1. Messlog D86.
