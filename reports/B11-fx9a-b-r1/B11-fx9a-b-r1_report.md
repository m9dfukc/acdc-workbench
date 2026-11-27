# Report B11-fx9a-b-r1: B11-fx9a-b-r1 – acdc1 fx9a-open-inputs-11b, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | fx9a-open-inputs-11b |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx9a-open-inputs-11b-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B11-fx9a-b-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.5 | -75.0 | -72.4 | -73.1 | -85.9 | -72.7 | -96.4 | -72.4 | 67 % | -77.3 | 4.9 |
| Kanal 2 | -7.4 | -71.5 | -76.5 | -73.2 | -73.9 | -87.9 | -73.5 | -96.8 | -73.2 | 72 % | -78.7 | 5.5 |
| Kanal 3 | -5.7 | -72.8 | -77.4 | -74.7 | -75.3 | -92.6 | -74.9 | -97.6 | -74.7 | 83 % | -82.3 | 7.7 |
| Kanal 4 | -6.5 | -71.1 | -77.2 | -72.3 | -72.8 | -88.0 | -72.5 | -97.0 | -72.3 | 75 % | -78.3 | 6.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -82.8 | 9.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.7 | 58.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0018 | 5 | k=1·f1+2·f2: 12999.871 Hz, -121.5 dB | -119.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -98.2 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.1 dB | -101.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -82.9 | 10.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.3 | 60.9 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0021 | 6 | k=-3·f1+4·f2: 21000.400 Hz, -121.4 dB | -118.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -98.6 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.5 dB | -101.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.3 dB | -83.4 | 13.4 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.1 dB | -76.3 | 69.5 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0031 | 26 | k=34·f1-2·f2: 21995.497 Hz, -122.6 dB | -114.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -101.3 dB | -99.4 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -101.7 dB | -102.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.1 | 8.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.7 dB | -74.0 | 66.7 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0071 | 9 | k=-1·f1+3·f2: 17000.123 Hz, -119.9 dB | -115.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.9 dB | -98.8 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.9 dB | -101.6 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 58.2 | usb1k·1 |
| 1999.735 | -81.9 | 50.7 | usb1k·2 |
| 2999.603 | -82.6 | 51.3 | usb1k·3 |
| 6000.000 | -83.9 | 52.4 | fs8·1 |
| 12000.000 | -84.0 | 54.2 | fs8·2 |
| 18000.000 | -86.1 | 52.7 | fs8·3 |
| 3999.471 | -87.1 | 47.8 | usb1k·4 |
| 9998.676 | -87.7 | 50.1 | usb1k·10 |
| 15997.881 | -90.3 | 47.9 | usb1k·16 |
| 4999.338 | -90.1 | 45.7 | usb1k·5 |
| 6999.073 | -89.6 | 46.8 | usb1k·7 |
| 16997.749 | -92.8 | 46.1 | usb1k·17 |
| 8998.808 | -91.2 | 46.2 | usb1k·9 |
| 18997.484 | -93.8 | 44.9 | usb1k·19 |
| 20997.220 | -94.1 | 45.6 | usb1k·21 |
| 5999.206 | -94.6 | 41.7 | usb1k·6 |
| 13998.146 | -96.7 | 41.7 | usb1k·14 |
| 17997.617 | -97.3 | 41.3 | usb1k·18 |
| 12998.279 | -96.8 | 41.0 | usb1k·13 |
| 14998.014 | -97.1 | 41.8 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 58.9 | usb1k·1 |
| 1999.735 | -82.8 | 51.3 | usb1k·2 |
| 2999.603 | -83.0 | 52.6 | usb1k·3 |
| 6000.000 | -83.9 | 54.1 | fs8·1 |
| 12000.000 | -84.2 | 55.2 | fs8·2 |
| 18000.000 | -86.1 | 53.8 | fs8·3 |
| 3999.471 | -87.3 | 49.3 | usb1k·4 |
| 9998.676 | -87.7 | 51.7 | usb1k·10 |
| 15997.881 | -90.6 | 49.0 | usb1k·16 |
| 6999.073 | -90.0 | 47.9 | usb1k·7 |
| 4999.338 | -90.5 | 46.6 | usb1k·5 |
| 16997.749 | -92.9 | 47.3 | usb1k·17 |
| 8998.808 | -91.6 | 47.2 | usb1k·9 |
| 18997.484 | -93.6 | 46.4 | usb1k·19 |
| 20997.220 | -94.6 | 46.2 | usb1k·21 |
| 5999.206 | -95.2 | 42.8 | usb1k·6 |
| 17997.617 | -97.1 | 42.7 | usb1k·18 |
| 12998.279 | -96.8 | 42.6 | usb1k·13 |
| 14998.014 | -97.2 | 42.6 | usb1k·15 |
| 11998.411 | -96.9 | 42.4 | usb1k·12 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.1 | 62.6 | usb1k·1 |
| 1999.735 | -83.9 | 54.9 | usb1k·2 |
| 2999.603 | -83.9 | 55.9 | usb1k·3 |
| 6000.000 | -84.3 | 57.5 | fs8·1 |
| 12000.000 | -84.9 | 57.8 | fs8·2 |
| 18000.000 | -86.6 | 56.3 | fs8·3 |
| 3999.471 | -87.8 | 53.2 | usb1k·4 |
| 9998.676 | -88.0 | 54.6 | usb1k·10 |
| 15997.881 | -91.1 | 51.7 | usb1k·16 |
| 4999.338 | -91.2 | 49.9 | usb1k·5 |
| 6999.073 | -90.9 | 51.1 | usb1k·7 |
| 16997.749 | -93.5 | 49.3 | usb1k·17 |
| 8998.808 | -92.2 | 50.2 | usb1k·9 |
| 18997.484 | -93.9 | 48.2 | usb1k·19 |
| 20997.220 | -95.1 | 47.6 | usb1k·21 |
| 12998.278 | -96.8 | 45.7 | usb1k·13 |
| 5999.206 | -96.6 | 45.2 | usb1k·6 |
| 17997.617 | -97.4 | 45.3 | usb1k·18 |
| 14998.014 | -97.4 | 45.1 | usb1k·15 |
| 11998.411 | -97.3 | 45.4 | usb1k·12 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.7 | 60.2 | usb1k·1 |
| 1999.735 | -80.9 | 53.1 | usb1k·2 |
| 2999.603 | -82.1 | 53.1 | usb1k·3 |
| 6000.000 | -84.2 | 53.4 | fs8·1 |
| 12000.000 | -84.4 | 54.5 | fs8·2 |
| 18000.000 | -86.2 | 53.2 | fs8·3 |
| 3999.471 | -86.8 | 49.8 | usb1k·4 |
| 9998.676 | -87.9 | 50.8 | usb1k·10 |
| 4999.338 | -89.1 | 47.7 | usb1k·5 |
| 15997.881 | -89.9 | 49.2 | usb1k·16 |
| 6999.073 | -89.1 | 48.4 | usb1k·7 |
| 8998.808 | -90.5 | 47.6 | usb1k·9 |
| 16997.749 | -92.7 | 46.8 | usb1k·17 |
| 5999.206 | -93.0 | 44.6 | usb1k·6 |
| 18997.484 | -93.9 | 45.2 | usb1k·19 |
| 20997.220 | -93.9 | 45.2 | usb1k·21 |
| 13998.146 | -95.8 | 43.0 | usb1k·14 |
| 7998.941 | -94.9 | 42.9 | usb1k·8 |
| 11998.411 | -96.2 | 42.6 | usb1k·12 |
| 12998.279 | -96.9 | 41.7 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.02 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.17 | 0.01 | 0.03 |
| other1 | Kanal 1 | 11/11 | 1.16 | 1.84 | 0.09 |
| other2 | Kanal 1 | 11/11 | 0.18 | -0.50 | 0.14 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.02 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.19 | 0.01 | 0.03 |
| other1 | Kanal 2 | 11/11 | 1.13 | 0.13 | 0.09 |
| other2 | Kanal 2 | 11/11 | 0.17 | -0.37 | 0.10 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.14 | 0.03 | 0.02 |
| other1 | Kanal 3 | 11/11 | 1.04 | -0.55 | 0.08 |
| other2 | Kanal 3 | 11/11 | 0.12 | -0.22 | 0.07 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.04 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.19 | -0.01 | 0.06 |
| other1 | Kanal 4 | 11/11 | 0.92 | 0.14 | 0.12 |
| other2 | Kanal 4 | 11/11 | 0.22 | -0.59 | 0.16 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.63 | 0.31 s (3.18 Hz) | 23.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 35.4 |
| Kanal 2 | breitbandig | 1.48 | 0.31 s (3.18 Hz) | 24.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.0 |
| Kanal 3 | breitbandig | 1.58 | 0.31 s (3.18 Hz) | 26.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 41.1 |
| Kanal 4 | breitbandig | 1.18 | 0.31 s (3.20 Hz) | 24.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 36.6 |

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
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B11-fx9a-b-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B11-fx9a-b-r1_psd.png)

### Kammprofile

![Kammprofile](B11-fx9a-b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B11-fx9a-b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:21:11. Stream-Meldungen: 0. owl_read: reports/owl_read/B11-fx9a-b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 11 v22.4.r-fx9a (D-Cache an), Sandwich Ende. Eingänge offen, keine Kabel, Slot 1 vor dem Stream per Program Change, Regler 69/56/72/56 von 127, acdc1 im Case. Zustand des Oszillators im Case nicht erfragt. messlog D89.
