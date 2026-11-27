# Report B11-fx9a-a-r2: B11-fx9a-a-r2 – acdc1 fx9a-open-inputs-11a, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | fx9a-open-inputs-11a |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx9a-open-inputs-11a-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B11-fx9a-a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -72.1 | -81.5 | -72.6 | -73.3 | -87.7 | -72.9 | -95.2 | -72.7 | 69 % | -77.8 | 5.1 |
| Kanal 2 | -7.5 | -72.9 | -83.0 | -73.4 | -74.0 | -89.3 | -73.6 | -95.7 | -73.4 | 73 % | -79.1 | 5.7 |
| Kanal 3 | -5.7 | -74.5 | -87.6 | -74.8 | -75.3 | -94.1 | -74.9 | -95.8 | -74.8 | 84 % | -82.8 | 8.0 |
| Kanal 4 | -6.5 | -72.0 | -83.3 | -72.4 | -72.9 | -89.3 | -72.6 | -101.3 | -72.4 | 76 % | -78.6 | 6.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -83.0 | 9.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -74.9 | 60.0 % |
| Netz 50 Hz | Kanal 1 | 49.9453 | 0.0053 | 3/19 | k=3: 149.829 Hz, -107.6 dB | -104.9 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0020 | 10 | k=1·f1+1·f2: 6999.866 Hz, -118.7 dB | -114.4 | 0.0 % |
| stärkste übrige Linie (51.17 Hz) | Kanal 1 | 51.1658 | 0.0046 | 3/466 | k=1: 51.167 Hz, -102.7 dB | -101.8 | 0.1 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 1 | 1000.0001 | 0.0005 | 20/23 | k=1: 1000.002 Hz, -103.4 dB | -96.3 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -83.0 | 10.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.4 | 62.2 % |
| Netz 50 Hz | Kanal 2 | 49.9454 | 0.0051 | 3/19 | k=3: 149.830 Hz, -108.8 dB | -106.3 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0018 | 12 | k=1·f1+1·f2: 6999.867 Hz, -119.4 dB | -114.8 | 0.0 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 2 | 1000.0001 | 0.0004 | 20/23 | k=1: 1000.001 Hz, -103.5 dB | -96.3 | 0.5 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 2 | 7384.6153 | 0.0002 | 3/3 | k=1: 7384.616 Hz, -103.8 dB | -105.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -83.6 | 13.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.3 | 70.9 % |
| Netz 50 Hz | Kanal 3 | 49.9454 | 0.0055 | 3/19 | k=3: 149.830 Hz, -114.1 dB | -111.7 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0014 | 16 | k=-1·f1+1·f2: 5000.132 Hz, -121.3 dB | -115.8 | 0.0 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0004 | 20/23 | k=1: 1000.001 Hz, -104.3 dB | -96.7 | 0.6 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 3 | 2500.0003 | 0.0003 | 5/9 | k=1: 2500.000 Hz, -104.7 dB | -103.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.5 dB | -83.2 | 8.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.7 dB | -74.0 | 68.0 % |
| Netz 50 Hz | Kanal 4 | 49.9454 | 0.0049 | 3/19 | k=3: 149.831 Hz, -109.1 dB | -106.7 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0040 | 13 | k=1·f1+1·f2: 6999.868 Hz, -116.1 dB | -111.9 | 0.0 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 4 | 7384.6153 | 0.0001 | 3/3 | k=1: 7384.615 Hz, -103.8 dB | -105.0 | 0.1 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1899 | 0.0016 | 9/19 | k=1: 1215.190 Hz, -102.9 dB | -103.7 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 58.5 | usb1k·1 |
| 1999.735 | -82.1 | 51.7 | usb1k·2 |
| 2999.603 | -82.9 | 51.9 | usb1k·3 |
| 6000.000 | -83.4 | 52.6 | fs8·1 |
| 12000.000 | -84.7 | 52.4 | fs8·2 |
| 18000.000 | -86.6 | 50.8 | fs8·3 |
| 3999.470 | -86.6 | 48.9 | usb1k·4 |
| 9998.675 | -88.1 | 49.9 | usb1k·10 |
| 4999.338 | -90.0 | 45.5 | usb1k·5 |
| 15997.879 | -90.3 | 48.2 | usb1k·16 |
| 6999.073 | -90.2 | 46.4 | usb1k·7 |
| 16997.747 | -92.6 | 46.0 | usb1k·17 |
| 8998.807 | -91.5 | 44.9 | usb1k·9 |
| 18997.482 | -93.6 | 45.0 | usb1k·19 |
| 20997.217 | -94.4 | 42.8 | usb1k·21 |
| 5999.205 | -94.8 | 41.0 | usb1k·6 |
| 13998.145 | -96.1 | 42.0 | usb1k·14 |
| 11998.410 | -96.0 | 40.6 | usb1k·12 |
| 17997.614 | -97.2 | 40.3 | usb1k·18 |
| 7998.940 | -96.8 | 40.2 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 59.1 | usb1k·1 |
| 1999.735 | -83.1 | 52.0 | usb1k·2 |
| 6000.000 | -83.4 | 53.8 | fs8·1 |
| 2999.603 | -83.3 | 53.1 | usb1k·3 |
| 12000.000 | -84.9 | 53.5 | fs8·2 |
| 18000.000 | -86.7 | 51.6 | fs8·3 |
| 3999.470 | -86.8 | 50.2 | usb1k·4 |
| 9998.675 | -88.1 | 51.3 | usb1k·10 |
| 4999.338 | -90.3 | 46.5 | usb1k·5 |
| 15997.879 | -90.5 | 49.4 | usb1k·16 |
| 6999.073 | -90.7 | 46.9 | usb1k·7 |
| 16997.747 | -92.8 | 46.9 | usb1k·17 |
| 8998.807 | -91.8 | 45.8 | usb1k·9 |
| 18997.482 | -93.6 | 46.4 | usb1k·19 |
| 20997.217 | -94.9 | 43.6 | usb1k·21 |
| 5999.205 | -95.3 | 41.9 | usb1k·6 |
| 17997.614 | -97.2 | 41.0 | usb1k·18 |
| 11998.410 | -96.3 | 41.9 | usb1k·12 |
| 13998.144 | -97.2 | 42.0 | usb1k·14 |
| 14998.012 | -97.7 | 41.9 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 62.6 | usb1k·1 |
| 6000.000 | -83.9 | 57.1 | fs8·1 |
| 1999.735 | -83.9 | 55.6 | usb1k·2 |
| 2999.603 | -84.2 | 56.3 | usb1k·3 |
| 12000.000 | -85.6 | 56.2 | fs8·2 |
| 18000.000 | -87.0 | 54.9 | fs8·3 |
| 3999.470 | -87.4 | 53.6 | usb1k·4 |
| 9998.675 | -88.4 | 54.3 | usb1k·10 |
| 15997.879 | -91.0 | 51.6 | usb1k·16 |
| 4999.338 | -91.0 | 50.1 | usb1k·5 |
| 6999.073 | -91.5 | 50.1 | usb1k·7 |
| 16997.747 | -93.4 | 49.5 | usb1k·17 |
| 8998.807 | -92.4 | 49.2 | usb1k·9 |
| 18997.482 | -93.9 | 48.4 | usb1k·19 |
| 20997.217 | -95.3 | 45.9 | usb1k·21 |
| 5999.205 | -96.7 | 44.2 | usb1k·6 |
| 17997.614 | -97.4 | 44.6 | usb1k·18 |
| 11998.410 | -96.8 | 44.6 | usb1k·12 |
| 12998.277 | -97.7 | 44.5 | usb1k·13 |
| 14998.012 | -98.1 | 44.2 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.7 | 60.2 | usb1k·1 |
| 1999.735 | -81.1 | 53.6 | usb1k·2 |
| 2999.603 | -82.3 | 53.6 | usb1k·3 |
| 6000.000 | -83.5 | 53.1 | fs8·1 |
| 12000.000 | -85.1 | 52.8 | fs8·2 |
| 3999.470 | -86.3 | 50.2 | usb1k·4 |
| 18000.000 | -86.8 | 50.5 | fs8·3 |
| 4999.338 | -88.9 | 47.7 | usb1k·5 |
| 9998.675 | -88.3 | 50.2 | usb1k·10 |
| 15997.879 | -89.8 | 49.0 | usb1k·16 |
| 6999.073 | -89.9 | 47.2 | usb1k·7 |
| 8998.807 | -90.9 | 46.1 | usb1k·9 |
| 16997.747 | -92.4 | 46.6 | usb1k·17 |
| 5999.205 | -92.8 | 43.8 | usb1k·6 |
| 18997.482 | -93.8 | 45.6 | usb1k·19 |
| 20997.217 | -94.5 | 43.4 | usb1k·21 |
| 7998.940 | -95.0 | 42.4 | usb1k·8 |
| 13998.144 | -95.4 | 43.4 | usb1k·14 |
| 11998.410 | -95.3 | 42.3 | usb1k·12 |
| 21997.084 | -97.8 | 41.7 | usb1k·22 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.02 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.16 | 0.06 | 0.02 |
| mains50 | Kanal 1 | 11/11 | 204.98 | 530.21 | 0.59 |
| other1 | Kanal 1 | 11/11 | 22.26 | -17.46 | 3.13 |
| other2 | Kanal 1 | 11/11 | 11.68 | 22.05 | 0.02 |
| fs8 | Kanal 2 | 11/11 | 0.03 | -0.02 | 0.05 |
| usb1k | Kanal 2 | 11/11 | 0.16 | 0.13 | 0.02 |
| mains50 | Kanal 2 | 11/11 | 204.76 | 527.53 | 0.57 |
| other1 | Kanal 2 | 11/11 | 11.34 | 10.79 | 0.02 |
| other2 | Kanal 2 | 11/11 | 0.14 | 0.09 | 0.24 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.02 | 0.05 |
| usb1k | Kanal 3 | 11/11 | 0.16 | 0.09 | 0.01 |
| mains50 | Kanal 3 | 11/11 | 212.18 | 552.88 | 0.65 |
| other1 | Kanal 3 | 11/11 | 9.13 | 3.54 | 0.01 |
| other2 | Kanal 3 | 11/11 | 0.39 | -0.04 | 0.13 |
| fs8 | Kanal 4 | 11/11 | 0.04 | 0.00 | 0.04 |
| usb1k | Kanal 4 | 11/11 | 0.13 | 0.06 | 0.02 |
| mains50 | Kanal 4 | 11/11 | 201.18 | 518.94 | 0.74 |
| other1 | Kanal 4 | 11/11 | 0.15 | 0.18 | 0.34 |
| other2 | Kanal 4 | 11/11 | 0.33 | -0.66 | 0.29 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.73 | 0.31 s (3.22 Hz) | 17.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 36.1 |
| Kanal 2 | breitbandig | 0.64 | 1.25 s (0.80 Hz) | 15.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 37.7 |
| Kanal 3 | breitbandig | 0.40 | 1.25 s (0.80 Hz) | 20.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.89 | 7.50 s (0.13 Hz) | 40.4 |
| Kanal 4 | breitbandig | 0.53 | 1.25 s (0.80 Hz) | 17.7 |
| Kanal 4 | 999.9 Hz ± 10 | 0.88 | 7.50 s (0.13 Hz) | 35.5 |

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

![Spektrogramm](B11-fx9a-a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B11-fx9a-a-r2_psd.png)

### Kammprofile

![Kammprofile](B11-fx9a-a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B11-fx9a-a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:16:27. Stream-Meldungen: 0. owl_read: reports/owl_read/B11-fx9a-a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 11 v22.4.r-fx9a (D-Cache an), Sandwich Anfang. Eingänge offen, keine Kabel, Slot 1 vor dem Stream per Program Change, Regler 69/56/72/56 von 127, acdc1 im Case. Zustand des Oszillators im Case nicht erfragt. messlog D89.
