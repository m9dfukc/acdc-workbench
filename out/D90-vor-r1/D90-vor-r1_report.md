# Report D90-vor-r1: D90-vor-r1 – acdc1 gnd-vor-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | gnd-vor-open-inputs |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_gnd-vor-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis D90-vor-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.0 | -63.8 | -64.4 | -72.2 | -73.0 | -85.3 | -72.5 | -96.0 | -72.2 | 65 % | -76.7 | 4.6 |
| Kanal 2 | -6.7 | -65.6 | -66.7 | -72.3 | -72.9 | -87.1 | -72.6 | -96.4 | -72.3 | 74 % | -78.2 | 5.9 |
| Kanal 3 | -4.9 | -66.5 | -67.2 | -74.5 | -75.2 | -91.9 | -74.7 | -97.5 | -74.5 | 81 % | -81.8 | 7.3 |
| Kanal 4 | -5.9 | -66.0 | -67.4 | -71.7 | -72.3 | -86.8 | -71.9 | -96.7 | -71.7 | 75 % | -77.6 | 5.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.3 dB | -82.4 | 9.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8647 | 0.0004 | 23/23 | k=1: 999.864 Hz, -73.5 dB | -74.7 | 55.5 % |
| Netz 50 Hz | Kanal 1 | 50.0433 | 0.0000 | 1/19 | k=1: 50.043 Hz, -107.0 dB | -109.6 | 0.0 % |
| Mischprodukte n·999.8647 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8647 | 0.0024 | 7 | k=-7·f1+4·f2: 17000.948 Hz, -119.9 dB | -115.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.8 dB | -97.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -101.0 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=2: 12000.000 Hz, -83.5 dB | -82.6 | 9.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8647 | 0.0003 | 23/23 | k=1: 999.864 Hz, -73.0 dB | -74.2 | 64.5 % |
| Netz 50 Hz | Kanal 2 | 50.0384 | 0.0026 | 2/19 | k=1: 50.042 Hz, -107.2 dB | -109.2 | 0.0 % |
| Mischprodukte n·999.8647 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8647 | 0.0022 | 12 | k=-3·f1+4·f2: 21000.409 Hz, -120.8 dB | -115.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -98.1 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.6 dB | -101.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.1 | 13.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8647 | 0.0004 | 23/23 | k=1: 999.864 Hz, -75.1 dB | -76.2 | 67.5 % |
| Netz 50 Hz | Kanal 3 | 50.0389 | 0.0032 | 6/19 | k=1: 50.041 Hz, -107.5 dB | -109.1 | 0.0 % |
| Mischprodukte n·999.8647 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8647 | 0.0024 | 25 | k=-3·f1+4·f2: 21000.408 Hz, -121.2 dB | -113.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -101.4 dB | -99.2 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -102.0 dB | -102.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.7 dB | -82.8 | 7.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8647 | 0.0002 | 23/23 | k=1: 999.865 Hz, -72.3 dB | -73.5 | 66.7 % |
| Netz 50 Hz | Kanal 4 | 50.0418 | 0.0000 | 1/19 | k=1: 50.042 Hz, -107.0 dB | -109.5 | 0.0 % |
| Mischprodukte n·999.8647 + m·5999.9999 Hz (m = ±1…±4) | Kanal 4 | 999.8647 | 0.0020 | 4 | k=-7·f1+4·f2: 17000.951 Hz, -120.9 dB | -118.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.7 dB | -98.4 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.9 dB | -101.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -73.5 | 56.7 | usb1k·1 |
| 1999.730 | -82.1 | 49.8 | usb1k·2 |
| 12000.000 | -83.3 | 54.3 | fs8·2 |
| 2999.594 | -82.4 | 51.8 | usb1k·3 |
| 6000.000 | -83.6 | 52.6 | fs8·1 |
| 18000.000 | -86.0 | 52.2 | fs8·3 |
| 9998.647 | -87.3 | 49.7 | usb1k·10 |
| 3999.459 | -86.4 | 48.3 | usb1k·4 |
| 15997.836 | -90.2 | 47.3 | usb1k·16 |
| 4999.324 | -89.2 | 45.8 | usb1k·5 |
| 6999.053 | -91.0 | 45.3 | usb1k·7 |
| 16997.700 | -91.4 | 46.8 | usb1k·17 |
| 18997.429 | -91.1 | 47.3 | usb1k·19 |
| 8998.783 | -92.3 | 44.2 | usb1k·9 |
| 11998.376 | -94.0 | 43.6 | usb1k·12 |
| 7998.918 | -95.2 | 40.6 | usb1k·8 |
| 5999.190 | -94.5 | 41.7 | usb1k·6 |
| 19997.294 | -95.8 | 42.7 | usb1k·20 |
| 12998.242 | -95.3 | 42.7 | usb1k·13 |
| 20997.159 | -96.7 | 41.9 | usb1k·21 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -73.0 | 59.0 | usb1k·1 |
| 1999.729 | -81.0 | 52.8 | usb1k·2 |
| 2999.594 | -82.2 | 53.2 | usb1k·3 |
| 12000.000 | -83.5 | 55.2 | fs8·2 |
| 6000.000 | -83.8 | 53.6 | fs8·1 |
| 18000.000 | -86.0 | 52.8 | fs8·3 |
| 3999.459 | -86.1 | 50.2 | usb1k·4 |
| 9998.647 | -87.6 | 50.8 | usb1k·10 |
| 4999.324 | -88.5 | 47.9 | usb1k·5 |
| 15997.836 | -89.7 | 49.6 | usb1k·16 |
| 6999.053 | -90.7 | 46.7 | usb1k·7 |
| 18997.429 | -91.1 | 48.3 | usb1k·19 |
| 16997.700 | -91.6 | 47.9 | usb1k·17 |
| 8998.782 | -91.6 | 46.1 | usb1k·9 |
| 7998.918 | -94.5 | 42.8 | usb1k·8 |
| 5999.189 | -94.0 | 43.4 | usb1k·6 |
| 11998.376 | -93.6 | 45.1 | usb1k·12 |
| 19997.294 | -96.2 | 43.2 | usb1k·20 |
| 12998.242 | -95.4 | 43.8 | usb1k·13 |
| 20997.159 | -96.3 | 43.3 | usb1k·21 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -75.1 | 60.9 | usb1k·1 |
| 6000.000 | -84.2 | 57.1 | fs8·1 |
| 12000.000 | -84.2 | 57.5 | fs8·2 |
| 2999.594 | -83.6 | 56.5 | usb1k·3 |
| 1999.730 | -84.3 | 53.9 | usb1k·2 |
| 18000.000 | -86.4 | 55.5 | fs8·3 |
| 9998.647 | -87.7 | 54.2 | usb1k·10 |
| 3999.459 | -87.2 | 53.6 | usb1k·4 |
| 15997.836 | -91.0 | 50.9 | usb1k·16 |
| 4999.324 | -90.5 | 50.2 | usb1k·5 |
| 18997.429 | -91.4 | 50.8 | usb1k·19 |
| 16997.700 | -92.0 | 50.0 | usb1k·17 |
| 6999.053 | -92.2 | 49.0 | usb1k·7 |
| 8998.783 | -93.9 | 47.5 | usb1k·9 |
| 11998.376 | -94.7 | 47.1 | usb1k·12 |
| 7998.918 | -96.4 | 44.5 | usb1k·8 |
| 19997.294 | -95.9 | 45.8 | usb1k·20 |
| 5999.190 | -96.1 | 45.1 | usb1k·6 |
| 12998.242 | -95.4 | 46.8 | usb1k·13 |
| 17997.565 | -98.6 | 43.4 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -72.3 | 59.3 | usb1k·1 |
| 1999.729 | -79.1 | 53.7 | usb1k·2 |
| 2999.594 | -82.1 | 52.7 | usb1k·3 |
| 12000.000 | -83.7 | 54.3 | fs8·2 |
| 6000.000 | -84.1 | 52.6 | fs8·1 |
| 18000.000 | -86.3 | 51.8 | fs8·3 |
| 3999.459 | -85.9 | 49.6 | usb1k·4 |
| 9998.647 | -88.0 | 49.4 | usb1k·10 |
| 4999.324 | -87.0 | 48.8 | usb1k·5 |
| 15997.835 | -89.1 | 49.0 | usb1k·16 |
| 8998.782 | -90.1 | 46.8 | usb1k·9 |
| 6999.053 | -90.5 | 45.9 | usb1k·7 |
| 18997.429 | -91.2 | 47.2 | usb1k·19 |
| 16997.700 | -91.8 | 46.8 | usb1k·17 |
| 5999.189 | -92.3 | 44.3 | usb1k·6 |
| 7998.918 | -93.6 | 43.2 | usb1k·8 |
| 11998.376 | -93.0 | 44.9 | usb1k·12 |
| 12998.242 | -95.1 | 43.0 | usb1k·13 |
| 20997.159 | -95.6 | 42.7 | usb1k·21 |
| 19997.294 | -96.9 | 41.4 | usb1k·20 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | 0.01 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.33 | 0.98 | 0.24 |
| mains50 | Kanal 1 | 11/11 | 3508.35 | 931.74 | 2.31 |
| other1 | Kanal 1 | 11/11 | 1.52 | -2.30 | 0.24 |
| other2 | Kanal 1 | 11/11 | 0.36 | 0.25 | 0.25 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.33 | 0.99 | 0.20 |
| mains50 | Kanal 2 | 11/11 | 2450.37 | 824.17 | 1.74 |
| other1 | Kanal 2 | 11/11 | 1.46 | -1.49 | 0.15 |
| other2 | Kanal 2 | 11/11 | 0.28 | 0.22 | 0.19 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.37 | 1.12 | 0.17 |
| mains50 | Kanal 3 | 11/11 | 191.58 | -207.84 | 1.19 |
| other1 | Kanal 3 | 11/11 | 1.71 | -3.10 | 0.22 |
| other2 | Kanal 3 | 11/11 | 0.20 | 0.15 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.03 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.38 | 1.00 | 0.24 |
| mains50 | Kanal 4 | 10/11 | 2516.25 | -2529.29 | 1.56 |
| other1 | Kanal 4 | 11/11 | 1.31 | -1.94 | 0.34 |
| other2 | Kanal 4 | 11/11 | 0.40 | 0.12 | 0.20 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.70 | 15.00 s (0.07 Hz) | 23.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 33.2 |
| Kanal 2 | breitbandig | 3.09 | 12.00 s (0.08 Hz) | 21.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 35.0 |
| Kanal 3 | breitbandig | 3.57 | 15.00 s (0.07 Hz) | 28.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 38.9 |
| Kanal 4 | breitbandig | 2.77 | 0.31 s (3.22 Hz) | 22.0 |
| Kanal 4 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 33.2 |

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
| Kanal 1 | 1.00 | 0.99 | 0.99 | 0.97 |
| Kanal 2 | 0.99 | 1.00 | 0.98 | 0.99 |
| Kanal 3 | 0.99 | 0.98 | 1.00 | 0.96 |
| Kanal 4 | 0.97 | 0.99 | 0.96 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](D90-vor-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D90-vor-r1_psd.png)

### Kammprofile

![Kammprofile](D90-vor-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](D90-vor-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 22:41:04. Stream-Meldungen: 0. owl_read: out/owl_read/D90-vor-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
