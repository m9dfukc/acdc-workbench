# Report B9-fx7a-a-r1: B9-fx7a-a-r1 – acdc1 fx7a-open-inputs-9a, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 9 v22.4.r-fx7a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx7a (fx6a + Patch 18, LED-PWM 48 kHz) am Anfang, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx7a-open-inputs-9a-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx7a-a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.0 | -69.7 | -74.7 | -71.3 | -72.2 | -86.3 | -71.6 | -96.2 | -71.3 | 53 % | -74.6 | 3.3 |
| Kanal 2 | -7.3 | -71.4 | -77.7 | -72.5 | -73.4 | -88.4 | -72.8 | -96.3 | -72.5 | 59 % | -76.4 | 3.9 |
| Kanal 3 | -5.5 | -73.6 | -82.4 | -74.2 | -75.0 | -92.8 | -74.4 | -93.4 | -74.3 | 70 % | -79.5 | 5.2 |
| Kanal 4 | -6.4 | -70.6 | -78.1 | -71.5 | -72.3 | -88.4 | -71.7 | -95.4 | -71.5 | 57 % | -75.2 | 3.7 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -83.0 | 6.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.7 | 46.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0035 | 1 | k=5·f1+3·f2: 22999.342 Hz, -121.3 dB | -124.4 | 0.0 % |
| stärkste übrige Linie (3500.00 Hz) | Kanal 1 | 3500.0004 | 0.0003 | 6/6 | k=1: 3500.000 Hz, -100.6 dB | -98.8 | 0.2 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 1 | 4000.0005 | 0.0004 | 4/5 | k=1: 4000.000 Hz, -100.6 dB | -99.7 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.3 dB | -83.1 | 8.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.5 | 50.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0017 | 1 | k=5·f1+3·f2: 22999.340 Hz, -122.7 dB | -126.3 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 2 | 4000.0005 | 0.0004 | 4/5 | k=1: 4000.000 Hz, -100.6 dB | -99.9 | 0.2 % |
| stärkste übrige Linie (3500.00 Hz) | Kanal 2 | 3500.0004 | 0.0003 | 6/6 | k=1: 3500.000 Hz, -100.7 dB | -98.8 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -83.7 | 11.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.6 | 58.7 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0025 | 7 | k=2·f1+1·f2: 7999.737 Hz, -121.2 dB | -118.0 | 0.0 % |
| stärkste übrige Linie (3500.00 Hz) | Kanal 3 | 3500.0004 | 0.0002 | 6/6 | k=1: 3500.000 Hz, -101.3 dB | -99.4 | 0.3 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0003 | 17/23 | k=1: 1000.000 Hz, -101.4 dB | -94.7 | 0.9 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -83.3 | 6.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.4 | 50.6 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0024 | 1 | k=5·f1+3·f2: 22999.341 Hz, -121.0 dB | -123.8 | 0.0 % |
| stärkste übrige Linie (3500.00 Hz) | Kanal 4 | 3500.0004 | 0.0004 | 6/6 | k=1: 3500.000 Hz, -101.0 dB | -99.0 | 0.2 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 4 | 2500.0003 | 0.0004 | 8/9 | k=1: 2500.000 Hz, -101.1 dB | -97.9 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 57.3 | usb1k·1 |
| 1999.736 | -81.5 | 49.8 | usb1k·2 |
| 6000.000 | -83.2 | 49.1 | fs8·1 |
| 2999.603 | -83.1 | 48.5 | usb1k·3 |
| 12000.000 | -85.5 | 48.5 | fs8·2 |
| 18000.000 | -86.2 | 48.7 | fs8·3 |
| 3999.471 | -87.1 | 45.1 | usb1k·4 |
| 9998.677 | -88.9 | 44.7 | usb1k·10 |
| 4999.339 | -89.8 | 42.5 | usb1k·5 |
| 15997.883 | -90.7 | 43.5 | usb1k·16 |
| 8998.809 | -91.2 | 42.2 | usb1k·9 |
| 6999.074 | -91.4 | 41.5 | usb1k·7 |
| 16997.751 | -92.9 | 41.1 | usb1k·17 |
| 18997.487 | -94.0 | 40.6 | usb1k·19 |
| 20997.222 | -94.3 | 41.1 | usb1k·21 |
| 5999.206 | -94.0 | 38.3 | usb1k·6 |
| 11998.412 | -96.1 | 37.8 | usb1k·12 |
| 13998.148 | -96.6 | 37.7 | usb1k·14 |
| 12998.280 | -97.4 | 36.6 | usb1k·13 |
| 7998.941 | -96.4 | 36.7 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 57.9 | usb1k·1 |
| 1999.736 | -82.5 | 50.6 | usb1k·2 |
| 6000.000 | -83.3 | 51.0 | fs8·1 |
| 2999.603 | -83.8 | 49.9 | usb1k·3 |
| 12000.000 | -85.8 | 50.3 | fs8·2 |
| 18000.000 | -86.3 | 50.4 | fs8·3 |
| 3999.471 | -87.5 | 46.7 | usb1k·4 |
| 9998.677 | -88.9 | 46.2 | usb1k·10 |
| 4999.339 | -90.3 | 43.7 | usb1k·5 |
| 15997.883 | -91.0 | 45.1 | usb1k·16 |
| 8998.809 | -91.5 | 43.7 | usb1k·9 |
| 6999.074 | -92.0 | 43.0 | usb1k·7 |
| 16997.751 | -93.4 | 42.6 | usb1k·17 |
| 18997.487 | -94.0 | 42.4 | usb1k·19 |
| 20997.222 | -94.7 | 42.7 | usb1k·21 |
| 5999.206 | -95.1 | 39.2 | usb1k·6 |
| 11998.412 | -96.6 | 39.5 | usb1k·12 |
| 12998.280 | -97.4 | 38.4 | usb1k·13 |
| 13998.148 | -97.9 | 38.2 | usb1k·14 |
| 17997.619 | -98.4 | 38.2 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 60.3 | usb1k·1 |
| 6000.000 | -83.8 | 53.6 | fs8·1 |
| 1999.735 | -83.8 | 52.8 | usb1k·2 |
| 2999.603 | -84.8 | 52.3 | usb1k·3 |
| 12000.000 | -86.7 | 51.4 | fs8·2 |
| 18000.000 | -86.7 | 52.3 | fs8·3 |
| 3999.471 | -88.1 | 49.3 | usb1k·4 |
| 9998.677 | -89.3 | 48.5 | usb1k·10 |
| 15997.883 | -91.6 | 47.1 | usb1k·16 |
| 4999.339 | -91.1 | 46.2 | usb1k·5 |
| 8998.809 | -92.3 | 45.7 | usb1k·9 |
| 16997.751 | -93.9 | 44.7 | usb1k·17 |
| 6999.074 | -92.8 | 44.8 | usb1k·7 |
| 18997.487 | -94.3 | 44.5 | usb1k·19 |
| 20997.222 | -95.5 | 43.9 | usb1k·21 |
| 5999.206 | -96.6 | 40.8 | usb1k·6 |
| 11998.412 | -97.1 | 41.0 | usb1k·12 |
| 12998.280 | -97.8 | 40.6 | usb1k·13 |
| 17997.619 | -98.6 | 40.4 | usb1k·18 |
| 14998.015 | -99.2 | 39.6 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 57.8 | usb1k·1 |
| 1999.736 | -80.9 | 51.0 | usb1k·2 |
| 6000.000 | -83.4 | 49.5 | fs8·1 |
| 2999.603 | -83.2 | 49.0 | usb1k·3 |
| 12000.000 | -86.0 | 48.3 | fs8·2 |
| 18000.000 | -86.5 | 48.6 | fs8·3 |
| 3999.471 | -87.2 | 45.5 | usb1k·4 |
| 4999.339 | -89.3 | 43.3 | usb1k·5 |
| 9998.677 | -89.1 | 44.4 | usb1k·10 |
| 15997.883 | -90.7 | 43.7 | usb1k·16 |
| 8998.809 | -90.8 | 42.7 | usb1k·9 |
| 6999.074 | -91.6 | 42.1 | usb1k·7 |
| 16997.751 | -93.1 | 40.8 | usb1k·17 |
| 5999.206 | -93.1 | 39.8 | usb1k·6 |
| 18997.487 | -94.4 | 40.9 | usb1k·19 |
| 20997.222 | -94.2 | 41.5 | usb1k·21 |
| 11998.412 | -96.1 | 38.2 | usb1k·12 |
| 13998.148 | -96.7 | 37.5 | usb1k·14 |
| 7998.941 | -96.0 | 37.3 | usb1k·8 |
| 12998.280 | -97.4 | 36.5 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.04 | 0.01 | 0.06 |
| usb1k | Kanal 1 | 11/11 | 0.18 | -0.17 | 0.04 |
| other1 | Kanal 1 | 11/11 | 0.60 | -0.38 | 0.35 |
| other2 | Kanal 1 | 11/11 | 0.16 | -0.29 | 0.29 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.01 | 0.06 |
| usb1k | Kanal 2 | 11/11 | 0.18 | -0.12 | 0.05 |
| other1 | Kanal 2 | 11/11 | 0.21 | -0.03 | 0.24 |
| other2 | Kanal 2 | 11/11 | 0.39 | -0.26 | 0.30 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.00 | 0.07 |
| usb1k | Kanal 3 | 11/11 | 0.16 | 0.02 | 0.04 |
| other1 | Kanal 3 | 11/11 | 0.30 | -0.19 | 0.20 |
| other2 | Kanal 3 | 11/11 | 5.79 | -0.48 | 0.05 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.01 | 0.07 |
| usb1k | Kanal 4 | 11/11 | 0.15 | -0.08 | 0.04 |
| other1 | Kanal 4 | 11/11 | 0.45 | -0.46 | 0.31 |
| other2 | Kanal 4 | 11/11 | 0.65 | 0.45 | 0.19 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.45 | 0.31 s (3.22 Hz) | 29.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 36.5 |
| Kanal 2 | breitbandig | 1.17 | 0.31 s (3.22 Hz) | 28.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 38.1 |
| Kanal 3 | breitbandig | 0.76 | 0.31 s (3.22 Hz) | 27.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 41.2 |
| Kanal 4 | breitbandig | 0.97 | 0.32 s (3.17 Hz) | 26.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 35.6 |

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
| Kanal 1 | 1.00 | 0.96 | 0.92 | 0.92 |
| Kanal 2 | 0.96 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.92 | 0.94 | 1.00 | 0.91 |
| Kanal 4 | 0.92 | 0.96 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx7a-a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx7a-a-r1_psd.png)

### Kammprofile

![Kammprofile](B9-fx7a-a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx7a-a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:05:52. Stream-Meldungen: 0. owl_read: reports/owl_read/B9-fx7a-a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Oszillator im Case abgesteckt (Nutzer). messlog D79.
