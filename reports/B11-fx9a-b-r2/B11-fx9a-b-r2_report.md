# Report B11-fx9a-b-r2: B11-fx9a-b-r2 – acdc1 fx9a-open-inputs-11b, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | fx9a-open-inputs-11b |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx9a-open-inputs-11b-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B11-fx9a-b-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -71.7 | -80.1 | -72.4 | -73.1 | -86.4 | -72.7 | -96.4 | -72.4 | 68 % | -77.3 | 4.9 |
| Kanal 2 | -7.5 | -72.6 | -82.0 | -73.1 | -73.8 | -88.5 | -73.4 | -96.7 | -73.2 | 73 % | -78.8 | 5.6 |
| Kanal 3 | -5.7 | -74.2 | -84.8 | -74.6 | -75.2 | -92.9 | -74.8 | -97.7 | -74.7 | 83 % | -82.4 | 7.8 |
| Kanal 4 | -6.5 | -71.8 | -82.4 | -72.2 | -72.7 | -88.7 | -72.4 | -97.0 | -72.2 | 76 % | -78.4 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.7 dB | -82.8 | 9.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.4 dB | -74.7 | 58.8 % |
| Netz 50 Hz | Kanal 1 | 50.0236 | 0.0157 | 4/19 | k=2: 100.019 Hz, -110.9 dB | -106.1 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0033 | 15 | k=1·f1+1·f2: 6999.873 Hz, -117.9 dB | -112.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -98.1 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.1 dB | -101.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -82.9 | 10.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -75.2 | 61.9 % |
| Netz 50 Hz | Kanal 2 | 50.0237 | 0.0148 | 4/19 | k=3: 150.074 Hz, -112.0 dB | -107.5 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0023 | 13 | k=1·f1+1·f2: 6999.870 Hz, -120.3 dB | -115.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -98.5 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.5 dB | -101.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -83.5 | 13.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.1 dB | -76.2 | 70.1 % |
| Netz 50 Hz | Kanal 3 | 50.0235 | 0.0132 | 5/19 | k=2: 100.021 Hz, -114.6 dB | -111.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0028 | 27 | k=-7·f1+4·f2: 17000.926 Hz, -121.6 dB | -113.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -101.3 dB | -99.5 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -101.7 dB | -102.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.1 dB | -83.1 | 8.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.5 dB | -73.9 | 67.8 % |
| Netz 50 Hz | Kanal 4 | 50.0236 | 0.0143 | 4/19 | k=2: 100.020 Hz, -112.4 dB | -108.1 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0027 | 10 | k=1·f1+1·f2: 6999.870 Hz, -118.4 dB | -114.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.9 dB | -98.8 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0000 | 4/7 | k=1: 3000.000 Hz, -100.8 dB | -101.7 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.4 | 58.8 | usb1k·1 |
| 1999.735 | -81.8 | 51.2 | usb1k·2 |
| 2999.603 | -82.7 | 51.8 | usb1k·3 |
| 12000.000 | -83.7 | 54.2 | fs8·2 |
| 6000.000 | -83.9 | 51.9 | fs8·1 |
| 18000.000 | -86.6 | 52.2 | fs8·3 |
| 3999.470 | -87.0 | 47.1 | usb1k·4 |
| 9998.675 | -87.7 | 49.7 | usb1k·10 |
| 15997.881 | -90.3 | 48.1 | usb1k·16 |
| 6999.073 | -89.5 | 46.1 | usb1k·7 |
| 4999.338 | -90.1 | 45.0 | usb1k·5 |
| 16997.748 | -92.4 | 46.4 | usb1k·17 |
| 8998.808 | -91.2 | 46.2 | usb1k·9 |
| 18997.483 | -93.6 | 45.5 | usb1k·19 |
| 20997.219 | -94.4 | 44.0 | usb1k·21 |
| 5999.206 | -94.4 | 41.4 | usb1k·6 |
| 13998.146 | -96.4 | 41.7 | usb1k·14 |
| 17997.616 | -97.2 | 41.7 | usb1k·18 |
| 14998.013 | -97.1 | 41.5 | usb1k·15 |
| 12998.278 | -96.8 | 41.4 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 59.4 | usb1k·1 |
| 1999.735 | -82.8 | 51.6 | usb1k·2 |
| 2999.603 | -83.1 | 52.8 | usb1k·3 |
| 6000.000 | -83.9 | 53.4 | fs8·1 |
| 12000.000 | -84.0 | 55.5 | fs8·2 |
| 18000.000 | -86.7 | 53.0 | fs8·3 |
| 3999.470 | -87.2 | 48.7 | usb1k·4 |
| 9998.675 | -87.7 | 51.1 | usb1k·10 |
| 15997.881 | -90.5 | 49.4 | usb1k·16 |
| 6999.073 | -90.0 | 47.2 | usb1k·7 |
| 4999.338 | -90.5 | 46.5 | usb1k·5 |
| 16997.748 | -92.6 | 47.2 | usb1k·17 |
| 8998.808 | -91.6 | 46.5 | usb1k·9 |
| 18997.483 | -93.7 | 46.6 | usb1k·19 |
| 20997.219 | -94.8 | 44.3 | usb1k·21 |
| 5999.206 | -94.9 | 42.4 | usb1k·6 |
| 17997.616 | -97.1 | 42.4 | usb1k·18 |
| 12998.278 | -96.8 | 42.8 | usb1k·13 |
| 14998.013 | -97.2 | 42.4 | usb1k·15 |
| 11998.410 | -96.8 | 42.7 | usb1k·12 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.1 | 63.0 | usb1k·1 |
| 1999.735 | -83.7 | 55.2 | usb1k·2 |
| 2999.603 | -84.0 | 56.4 | usb1k·3 |
| 6000.000 | -84.4 | 57.0 | fs8·1 |
| 12000.000 | -84.7 | 58.0 | fs8·2 |
| 18000.000 | -87.0 | 55.5 | fs8·3 |
| 3999.470 | -87.8 | 52.4 | usb1k·4 |
| 9998.675 | -88.1 | 54.2 | usb1k·10 |
| 15997.881 | -91.0 | 51.5 | usb1k·16 |
| 4999.338 | -91.1 | 49.8 | usb1k·5 |
| 6999.073 | -90.8 | 50.5 | usb1k·7 |
| 16997.748 | -93.3 | 49.5 | usb1k·17 |
| 8998.808 | -92.1 | 49.7 | usb1k·9 |
| 18997.484 | -94.0 | 48.7 | usb1k·19 |
| 20997.219 | -95.2 | 46.9 | usb1k·21 |
| 5999.206 | -96.3 | 45.0 | usb1k·6 |
| 17997.616 | -97.3 | 45.2 | usb1k·18 |
| 12998.278 | -96.9 | 46.0 | usb1k·13 |
| 14998.013 | -97.5 | 45.1 | usb1k·15 |
| 11998.410 | -97.3 | 45.2 | usb1k·12 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.5 | 60.6 | usb1k·1 |
| 1999.735 | -80.7 | 53.1 | usb1k·2 |
| 2999.603 | -82.1 | 53.6 | usb1k·3 |
| 6000.000 | -84.1 | 52.7 | fs8·1 |
| 12000.000 | -84.2 | 54.0 | fs8·2 |
| 18000.000 | -86.8 | 52.0 | fs8·3 |
| 3999.470 | -86.8 | 48.8 | usb1k·4 |
| 9998.675 | -87.9 | 50.3 | usb1k·10 |
| 4999.338 | -89.1 | 47.4 | usb1k·5 |
| 15997.881 | -89.9 | 49.0 | usb1k·16 |
| 6999.073 | -89.2 | 47.5 | usb1k·7 |
| 8998.808 | -90.5 | 47.2 | usb1k·9 |
| 16997.748 | -92.4 | 46.8 | usb1k·17 |
| 5999.206 | -92.7 | 44.0 | usb1k·6 |
| 18997.483 | -94.0 | 45.1 | usb1k·19 |
| 20997.219 | -94.3 | 44.9 | usb1k·21 |
| 7998.941 | -94.9 | 42.5 | usb1k·8 |
| 13998.145 | -95.8 | 42.7 | usb1k·14 |
| 11998.410 | -95.9 | 42.1 | usb1k·12 |
| 12998.278 | -96.8 | 42.0 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.21 | 0.05 | 0.04 |
| mains50 | Kanal 1 | 11/11 | 462.41 | 1585.95 | 1.10 |
| other1 | Kanal 1 | 11/11 | 0.86 | 2.30 | 0.09 |
| other2 | Kanal 1 | 11/11 | 0.39 | -0.03 | 0.21 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.19 | 0.06 | 0.05 |
| mains50 | Kanal 2 | 11/11 | 510.37 | 1804.09 | 0.99 |
| other1 | Kanal 2 | 11/11 | 1.21 | 1.13 | 0.06 |
| other2 | Kanal 2 | 11/11 | 0.29 | 0.11 | 0.16 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.14 | 0.08 | 0.03 |
| mains50 | Kanal 3 | 11/11 | 544.89 | 1880.90 | 1.05 |
| other1 | Kanal 3 | 11/11 | 1.37 | -1.61 | 0.05 |
| other2 | Kanal 3 | 11/11 | 0.20 | 0.00 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.04 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.16 | 0.08 | 0.05 |
| mains50 | Kanal 4 | 11/11 | 370.49 | 1198.87 | 1.14 |
| other1 | Kanal 4 | 11/11 | 1.60 | -1.61 | 0.04 |
| other2 | Kanal 4 | 11/11 | 0.36 | 0.00 | 0.15 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.82 | 0.31 s (3.18 Hz) | 19.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.89 | 7.50 s (0.13 Hz) | 36.2 |
| Kanal 2 | breitbandig | 0.69 | 0.31 s (3.18 Hz) | 21.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.89 | 7.50 s (0.13 Hz) | 37.2 |
| Kanal 3 | breitbandig | 0.52 | 7.50 s (0.13 Hz) | 22.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.88 | 7.50 s (0.13 Hz) | 40.8 |
| Kanal 4 | breitbandig | 0.57 | 0.31 s (3.18 Hz) | 20.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.87 | 7.50 s (0.13 Hz) | 36.1 |

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
| Kanal 1 | 1.00 | 0.96 | 0.93 | 0.95 |
| Kanal 2 | 0.96 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.96 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B11-fx9a-b-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B11-fx9a-b-r2_psd.png)

### Kammprofile

![Kammprofile](B11-fx9a-b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B11-fx9a-b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:22:24. Stream-Meldungen: 0. owl_read: reports/owl_read/B11-fx9a-b-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 11 v22.4.r-fx9a (D-Cache an), Sandwich Ende. Eingänge offen, keine Kabel, Slot 1 vor dem Stream per Program Change, Regler 69/56/72/56 von 127, acdc1 im Case. Zustand des Oszillators im Case nicht erfragt. messlog D89.
