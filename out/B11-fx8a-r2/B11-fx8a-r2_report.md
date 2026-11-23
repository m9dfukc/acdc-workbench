# Report B11-fx8a-r2: B11-fx8a-r2 – acdc1 fx8a-open-inputs-11, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | fx8a-open-inputs-11 |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-11-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B11-fx8a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.5 | -80.3 | -72.2 | -72.9 | -86.4 | -72.5 | -93.7 | -72.2 | 69 % | -77.3 | 5.1 |
| Kanal 2 | -7.5 | -72.3 | -81.5 | -72.9 | -73.6 | -88.5 | -73.1 | -94.0 | -72.9 | 73 % | -78.6 | 5.7 |
| Kanal 3 | -5.7 | -74.1 | -85.6 | -74.4 | -75.0 | -92.9 | -74.6 | -94.8 | -74.4 | 83 % | -82.1 | 7.7 |
| Kanal 4 | -6.5 | -71.5 | -81.7 | -71.9 | -72.4 | -88.6 | -72.1 | -94.3 | -71.9 | 76 % | -78.2 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -82.8 dB | -82.1 | 10.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.5 | 58.6 % |
| Netz 50 Hz | Kanal 1 | 50.1223 | 0.0006 | 2/19 | k=3: 150.368 Hz, -111.4 dB | -108.0 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0019 | 14 | k=1·f1+1·f2: 6999.870 Hz, -115.8 dB | -110.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.2 dB | -95.5 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -97.9 dB | -98.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.0 dB | -82.2 | 11.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.0 | 61.1 % |
| Netz 50 Hz | Kanal 2 | 50.1225 | 0.0026 | 2/19 | k=3: 150.371 Hz, -112.4 dB | -109.3 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0020 | 18 | k=1·f1+1·f2: 6999.870 Hz, -118.0 dB | -111.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.9 dB | -95.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.2 dB | -98.7 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.7 dB | -82.8 | 14.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.1 | 68.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0020 | 32 | k=-3·f1+4·f2: 21000.398 Hz, -120.7 dB | -112.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.1 dB | -96.5 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.4 dB | -99.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.3 dB | -82.4 | 9.0 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.2 dB | -73.6 | 67.2 % |
| Netz 50 Hz | Kanal 4 | 50.1227 | 0.0066 | 2/19 | k=3: 150.376 Hz, -112.1 dB | -109.4 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0020 | 15 | k=1·f1+1·f2: 6999.869 Hz, -114.6 dB | -110.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.2 dB | -96.1 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.0 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 58.3 | usb1k·1 |
| 1999.735 | -81.9 | 51.1 | usb1k·2 |
| 2999.603 | -82.4 | 51.8 | usb1k·3 |
| 12000.000 | -82.8 | 55.2 | fs8·2 |
| 6000.000 | -83.3 | 52.5 | fs8·1 |
| 18000.000 | -86.2 | 52.6 | fs8·3 |
| 3999.470 | -86.6 | 47.1 | usb1k·4 |
| 9998.675 | -87.7 | 49.8 | usb1k·10 |
| 4999.338 | -89.4 | 46.0 | usb1k·5 |
| 15997.880 | -90.3 | 48.5 | usb1k·16 |
| 6999.073 | -89.9 | 46.6 | usb1k·7 |
| 16997.748 | -92.3 | 46.0 | usb1k·17 |
| 8998.808 | -91.1 | 46.3 | usb1k·9 |
| 18997.483 | -93.8 | 44.9 | usb1k·19 |
| 5999.205 | -93.5 | 42.4 | usb1k·6 |
| 20997.218 | -94.3 | 44.7 | usb1k·21 |
| 13998.145 | -96.4 | 41.6 | usb1k·14 |
| 11998.410 | -96.1 | 41.9 | usb1k·12 |
| 2000.000 | -97.2 | 35.8 | other1·1 |
| 17997.615 | -97.4 | 41.2 | usb1k·18 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 59.1 | usb1k·1 |
| 1999.735 | -82.8 | 51.6 | usb1k·2 |
| 2999.603 | -82.9 | 52.7 | usb1k·3 |
| 12000.000 | -83.0 | 56.1 | fs8·2 |
| 6000.000 | -83.3 | 54.0 | fs8·1 |
| 18000.000 | -86.2 | 53.5 | fs8·3 |
| 3999.470 | -86.9 | 48.5 | usb1k·4 |
| 9998.675 | -87.7 | 51.1 | usb1k·10 |
| 4999.338 | -89.9 | 47.0 | usb1k·5 |
| 15997.880 | -90.6 | 49.5 | usb1k·16 |
| 6999.073 | -90.3 | 47.7 | usb1k·7 |
| 16997.748 | -92.6 | 47.4 | usb1k·17 |
| 8998.808 | -91.5 | 47.5 | usb1k·9 |
| 18997.483 | -93.8 | 45.8 | usb1k·19 |
| 20997.218 | -94.7 | 45.2 | usb1k·21 |
| 5999.205 | -94.3 | 43.0 | usb1k·6 |
| 17997.615 | -97.3 | 42.5 | usb1k·18 |
| 11998.410 | -96.5 | 42.6 | usb1k·12 |
| 13998.145 | -97.3 | 42.1 | usb1k·14 |
| 2000.000 | -97.9 | 36.6 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 62.5 | usb1k·1 |
| 12000.000 | -83.7 | 58.5 | fs8·2 |
| 1999.735 | -83.7 | 55.3 | usb1k·2 |
| 6000.000 | -83.9 | 57.9 | fs8·1 |
| 2999.603 | -83.8 | 56.2 | usb1k·3 |
| 18000.000 | -86.6 | 55.8 | fs8·3 |
| 3999.470 | -87.5 | 52.3 | usb1k·4 |
| 9998.675 | -88.1 | 53.6 | usb1k·10 |
| 4999.338 | -90.6 | 49.9 | usb1k·5 |
| 15997.880 | -90.9 | 51.3 | usb1k·16 |
| 6999.073 | -90.9 | 50.3 | usb1k·7 |
| 16997.748 | -93.2 | 49.2 | usb1k·17 |
| 8998.808 | -92.1 | 50.1 | usb1k·9 |
| 18997.483 | -94.0 | 48.1 | usb1k·19 |
| 20997.218 | -95.1 | 46.9 | usb1k·21 |
| 5999.205 | -95.8 | 46.0 | usb1k·6 |
| 17997.615 | -97.4 | 44.9 | usb1k·18 |
| 11998.410 | -96.9 | 45.1 | usb1k·12 |
| 14998.012 | -97.7 | 44.7 | usb1k·15 |
| 12998.277 | -97.5 | 44.7 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.2 | 60.3 | usb1k·1 |
| 1999.735 | -80.8 | 53.1 | usb1k·2 |
| 2999.603 | -81.9 | 53.3 | usb1k·3 |
| 12000.000 | -83.3 | 55.1 | fs8·2 |
| 6000.000 | -83.4 | 53.4 | fs8·1 |
| 18000.000 | -86.4 | 52.6 | fs8·3 |
| 3999.470 | -86.4 | 48.5 | usb1k·4 |
| 4999.338 | -88.7 | 47.7 | usb1k·5 |
| 9998.675 | -87.8 | 50.0 | usb1k·10 |
| 15997.880 | -90.0 | 48.8 | usb1k·16 |
| 6999.073 | -89.6 | 47.6 | usb1k·7 |
| 8998.808 | -90.6 | 47.5 | usb1k·9 |
| 16997.748 | -92.2 | 46.7 | usb1k·17 |
| 5999.205 | -92.1 | 44.7 | usb1k·6 |
| 18997.483 | -94.2 | 44.5 | usb1k·19 |
| 20997.218 | -94.2 | 44.7 | usb1k·21 |
| 13998.145 | -95.6 | 42.8 | usb1k·14 |
| 7998.941 | -94.9 | 41.9 | usb1k·8 |
| 11998.410 | -95.8 | 42.5 | usb1k·12 |
| 21997.085 | -97.9 | 41.1 | usb1k·22 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.03 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.24 | -0.26 | 0.10 |
| mains50 | Kanal 1 | 11/11 | 539.22 | 1920.24 | 0.54 |
| other1 | Kanal 1 | 11/11 | 1.80 | -0.86 | 0.11 |
| other2 | Kanal 1 | 11/11 | 0.25 | -0.06 | 0.18 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.20 | -0.21 | 0.09 |
| mains50 | Kanal 2 | 11/11 | 544.78 | 1930.73 | 0.62 |
| other1 | Kanal 2 | 11/11 | 2.17 | 0.81 | 0.11 |
| other2 | Kanal 2 | 11/11 | 0.24 | -0.04 | 0.14 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.03 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.20 | -0.24 | 0.08 |
| other1 | Kanal 3 | 11/11 | 1.23 | 1.64 | 0.10 |
| other2 | Kanal 3 | 11/11 | 0.11 | 0.01 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.17 | -0.21 | 0.10 |
| mains50 | Kanal 4 | 11/11 | 541.36 | 1923.64 | 0.70 |
| other1 | Kanal 4 | 11/11 | 2.19 | 0.91 | 0.11 |
| other2 | Kanal 4 | 11/11 | 0.28 | -0.07 | 0.22 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.78 | 0.31 s (3.18 Hz) | 21.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 38.1 |
| Kanal 2 | breitbandig | 0.70 | 0.31 s (3.18 Hz) | 21.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 39.3 |
| Kanal 3 | breitbandig | 0.49 | 7.50 s (0.13 Hz) | 26.2 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 44.0 |
| Kanal 4 | breitbandig | 0.58 | 0.31 s (3.18 Hz) | 20.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 38.3 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.96 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B11-fx8a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B11-fx8a-r2_psd.png)

### Kammprofile

![Kammprofile](B11-fx8a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B11-fx8a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:19:25. Stream-Meldungen: 0. owl_read: out/owl_read/B11-fx8a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 10 v22.4.r-fx8a (Kontrolle), Sandwich Mitte. Eingänge offen, keine Kabel, Slot 1 vor dem Stream per Program Change, Regler 69/56/72/56 von 127, acdc1 im Case. Zustand des Oszillators im Case nicht erfragt. messlog D89.
