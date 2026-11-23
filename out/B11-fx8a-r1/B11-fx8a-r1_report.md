# Report B11-fx8a-r1: B11-fx8a-r1 – acdc1 fx8a-open-inputs-11, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | fx8a-open-inputs-11 |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-11-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B11-fx8a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.1 | -74.2 | -72.3 | -73.1 | -86.1 | -72.6 | -93.7 | -72.3 | 67 % | -77.2 | 4.9 |
| Kanal 2 | -7.5 | -71.0 | -75.2 | -73.0 | -73.8 | -88.0 | -73.3 | -94.0 | -73.1 | 71 % | -78.5 | 5.5 |
| Kanal 3 | -5.7 | -72.7 | -77.3 | -74.5 | -75.2 | -92.6 | -74.7 | -94.8 | -74.5 | 82 % | -82.0 | 7.5 |
| Kanal 4 | -6.5 | -70.6 | -75.8 | -72.1 | -72.7 | -88.1 | -72.3 | -94.2 | -72.1 | 75 % | -78.1 | 6.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -82.8 dB | -82.1 | 10.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.8 | 56.7 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0069 | 12 | k=25·f1-4·f2: 996.676 Hz, -115.1 dB | -112.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.001 Hz, -97.0 dB | -95.4 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.0 dB | -98.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.0 dB | -82.2 | 12.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.3 | 59.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0063 | 12 | k=25·f1-4·f2: 996.675 Hz, -115.9 dB | -113.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.001 Hz, -97.6 dB | -95.7 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -98.8 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.7 dB | -82.7 | 15.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.3 | 66.9 % |
| Netz 50 Hz | Kanal 3 | 50.0276 | 0.0000 | 1/19 | k=2: 100.055 Hz, -115.3 dB | -119.4 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0038 | 34 | k=25·f1-4·f2: 996.676 Hz, -120.3 dB | -112.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -96.5 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.4 dB | -99.6 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=2: 12000.000 Hz, -83.2 dB | -82.3 | 9.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.6 dB | -74.0 | 65.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0051 | 10 | k=26·f1-4·f2: 1996.543 Hz, -117.5 dB | -113.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.001 Hz, -97.8 dB | -96.0 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.7 dB | -99.1 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 58.2 | usb1k·1 |
| 1999.735 | -81.9 | 50.9 | usb1k·2 |
| 12000.000 | -82.8 | 55.3 | fs8·2 |
| 2999.603 | -82.7 | 51.1 | usb1k·3 |
| 6000.000 | -83.3 | 52.8 | fs8·1 |
| 18000.000 | -85.8 | 53.1 | fs8·3 |
| 3999.470 | -86.8 | 48.4 | usb1k·4 |
| 9998.676 | -88.0 | 49.9 | usb1k·10 |
| 4999.338 | -89.8 | 45.2 | usb1k·5 |
| 15997.881 | -90.4 | 47.7 | usb1k·16 |
| 6999.073 | -90.0 | 46.7 | usb1k·7 |
| 16997.749 | -92.4 | 46.1 | usb1k·17 |
| 8998.808 | -91.4 | 45.7 | usb1k·9 |
| 18997.484 | -93.7 | 45.3 | usb1k·19 |
| 20997.219 | -94.1 | 43.9 | usb1k·21 |
| 5999.206 | -94.6 | 41.6 | usb1k·6 |
| 13998.146 | -95.8 | 42.6 | usb1k·14 |
| 2000.001 | -97.0 | 35.9 | other1·1 |
| 17997.616 | -97.0 | 41.8 | usb1k·18 |
| 11998.411 | -96.3 | 41.7 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 59.1 | usb1k·1 |
| 1999.736 | -82.9 | 51.4 | usb1k·2 |
| 12000.000 | -83.0 | 56.2 | fs8·2 |
| 2999.603 | -83.1 | 52.3 | usb1k·3 |
| 6000.000 | -83.3 | 54.1 | fs8·1 |
| 18000.000 | -85.9 | 53.9 | fs8·3 |
| 3999.471 | -87.0 | 49.4 | usb1k·4 |
| 9998.676 | -87.9 | 51.4 | usb1k·10 |
| 4999.338 | -90.2 | 46.2 | usb1k·5 |
| 15997.881 | -90.6 | 48.6 | usb1k·16 |
| 6999.073 | -90.4 | 47.7 | usb1k·7 |
| 16997.749 | -92.6 | 47.1 | usb1k·17 |
| 8998.808 | -91.8 | 46.5 | usb1k·9 |
| 18997.484 | -93.7 | 46.1 | usb1k·19 |
| 20997.219 | -94.6 | 44.7 | usb1k·21 |
| 5999.206 | -95.2 | 42.2 | usb1k·6 |
| 17997.616 | -97.0 | 42.7 | usb1k·18 |
| 13998.146 | -96.7 | 42.5 | usb1k·14 |
| 11998.411 | -96.5 | 42.8 | usb1k·12 |
| 14998.014 | -97.3 | 41.9 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 62.2 | usb1k·1 |
| 12000.000 | -83.7 | 59.1 | fs8·2 |
| 6000.000 | -83.8 | 57.9 | fs8·1 |
| 1999.735 | -83.8 | 54.9 | usb1k·2 |
| 2999.603 | -84.0 | 55.2 | usb1k·3 |
| 18000.000 | -86.3 | 55.9 | fs8·3 |
| 3999.470 | -87.5 | 53.1 | usb1k·4 |
| 9998.676 | -88.3 | 54.6 | usb1k·10 |
| 15997.881 | -91.1 | 51.4 | usb1k·16 |
| 4999.338 | -90.8 | 49.7 | usb1k·5 |
| 6999.073 | -91.2 | 50.5 | usb1k·7 |
| 16997.749 | -93.3 | 49.6 | usb1k·17 |
| 18997.484 | -94.0 | 48.6 | usb1k·19 |
| 8998.808 | -92.3 | 49.5 | usb1k·9 |
| 20997.219 | -95.0 | 47.0 | usb1k·21 |
| 17997.616 | -97.3 | 44.8 | usb1k·18 |
| 5999.206 | -96.6 | 45.0 | usb1k·6 |
| 14998.014 | -97.6 | 44.9 | usb1k·15 |
| 11998.411 | -97.1 | 45.8 | usb1k·12 |
| 13998.146 | -98.0 | 44.4 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.6 | 60.0 | usb1k·1 |
| 1999.735 | -80.9 | 53.0 | usb1k·2 |
| 2999.603 | -82.2 | 52.9 | usb1k·3 |
| 12000.000 | -83.2 | 55.1 | fs8·2 |
| 6000.000 | -83.5 | 53.3 | fs8·1 |
| 18000.000 | -86.0 | 53.2 | fs8·3 |
| 3999.471 | -86.5 | 49.4 | usb1k·4 |
| 4999.338 | -89.0 | 47.0 | usb1k·5 |
| 9998.676 | -88.1 | 50.0 | usb1k·10 |
| 15997.881 | -90.0 | 48.2 | usb1k·16 |
| 6999.073 | -89.7 | 47.5 | usb1k·7 |
| 16997.749 | -92.3 | 47.1 | usb1k·17 |
| 8998.808 | -90.7 | 46.7 | usb1k·9 |
| 5999.206 | -92.8 | 44.0 | usb1k·6 |
| 18997.484 | -94.0 | 45.1 | usb1k·19 |
| 20997.219 | -94.1 | 44.5 | usb1k·21 |
| 13998.146 | -95.1 | 43.4 | usb1k·14 |
| 11998.411 | -95.6 | 42.6 | usb1k·12 |
| 7998.941 | -95.6 | 42.3 | usb1k·8 |
| 17997.616 | -97.7 | 41.3 | usb1k·18 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.22 | -0.12 | 0.06 |
| other1 | Kanal 1 | 11/11 | 1.72 | 1.50 | 0.07 |
| other2 | Kanal 1 | 11/11 | 0.16 | -0.11 | 0.15 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.18 | -0.06 | 0.09 |
| other1 | Kanal 2 | 11/11 | 1.32 | -1.15 | 0.05 |
| other2 | Kanal 2 | 11/11 | 0.16 | -0.10 | 0.16 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.19 | -0.05 | 0.05 |
| mains50 | Kanal 3 | 8/11 | 614.49 | -407.03 | 1.87 |
| other1 | Kanal 3 | 11/11 | 0.34 | -0.10 | 0.08 |
| other2 | Kanal 3 | 11/11 | 0.13 | -0.12 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.12 | -0.06 | 0.12 |
| other1 | Kanal 4 | 11/11 | 1.49 | -0.95 | 0.06 |
| other2 | Kanal 4 | 11/11 | 0.13 | -0.13 | 0.15 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.88 | 0.31 s (3.18 Hz) | 28.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 38.4 |
| Kanal 2 | breitbandig | 1.81 | 0.31 s (3.18 Hz) | 29.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 40.1 |
| Kanal 3 | breitbandig | 1.63 | 0.31 s (3.18 Hz) | 30.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 43.7 |
| Kanal 4 | breitbandig | 1.46 | 0.31 s (3.18 Hz) | 29.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 39.0 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.96 |
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.93 |
| Kanal 4 | 0.96 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B11-fx8a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B11-fx8a-r1_psd.png)

### Kammprofile

![Kammprofile](B11-fx8a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B11-fx8a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:18:12. Stream-Meldungen: 0. owl_read: out/owl_read/B11-fx8a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 10 v22.4.r-fx8a (Kontrolle), Sandwich Mitte. Eingänge offen, keine Kabel, Slot 1 vor dem Stream per Program Change, Regler 69/56/72/56 von 127, acdc1 im Case. Zustand des Oszillators im Case nicht erfragt. messlog D89.
