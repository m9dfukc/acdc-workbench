# Report D90b-vor-r1: D90b-vor-r1 – acdc1 gnd-vor-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-24 |
| device | acdc1 |
| test | gnd-vor-open-inputs |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261124_acdc1_gnd-vor-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis D90b-vor-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -5.7 | -62.8 | -63.3 | -72.4 | -73.2 | -85.3 | -72.7 | -96.3 | -72.4 | 64 % | -76.8 | 4.4 |
| Kanal 2 | -6.5 | -65.0 | -65.9 | -72.6 | -73.3 | -87.3 | -72.9 | -96.6 | -72.6 | 71 % | -78.0 | 5.4 |
| Kanal 3 | -4.7 | -66.1 | -66.7 | -74.9 | -75.6 | -91.9 | -75.1 | -97.6 | -74.9 | 79 % | -81.7 | 6.8 |
| Kanal 4 | -5.7 | -65.3 | -66.3 | -72.0 | -72.6 | -87.1 | -72.3 | -96.9 | -72.0 | 70 % | -77.3 | 5.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9999 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.4 dB | -82.6 | 9.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8640 | 0.0007 | 23/23 | k=1: 999.864 Hz, -73.9 dB | -75.1 | 54.0 % |
| Netz 50 Hz | Kanal 1 | 49.9792 | 0.0025 | 2/19 | k=1: 49.982 Hz, -105.0 dB | -106.6 | 0.0 % |
| Mischprodukte n·999.8640 + m·5999.9999 Hz (m = ±1…±4) | Kanal 1 | 999.8640 | 0.0015 | 5 | k=-3·f1+4·f2: 21000.408 Hz, -120.4 dB | -118.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0151 | 9/11 | k=1: 2000.001 Hz, -99.4 dB | -98.0 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -100.3 dB | -101.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.6 dB | -82.7 | 9.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8640 | 0.0006 | 23/23 | k=1: 999.864 Hz, -73.5 dB | -74.7 | 61.4 % |
| Netz 50 Hz | Kanal 2 | 49.9812 | 0.0000 | 1/19 | k=1: 49.981 Hz, -106.1 dB | -108.1 | 0.0 % |
| Mischprodukte n·999.8640 + m·5999.9999 Hz (m = ±1…±4) | Kanal 2 | 999.8640 | 0.0010 | 8 | k=-7·f1+4·f2: 17000.952 Hz, -121.6 dB | -116.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.001 Hz, -100.1 dB | -98.4 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -100.7 dB | -101.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 5999.9999 | 0.0003 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.3 | 14.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8640 | 0.0007 | 23/23 | k=1: 999.864 Hz, -75.9 dB | -76.8 | 64.5 % |
| Netz 50 Hz | Kanal 3 | 49.9795 | 0.0020 | 3/19 | k=1: 49.980 Hz, -107.5 dB | -109.5 | 0.0 % |
| Mischprodukte n·999.8640 + m·5999.9999 Hz (m = ±1…±4) | Kanal 3 | 999.8640 | 0.0041 | 19 | k=-3·f1+4·f2: 21000.409 Hz, -120.2 dB | -114.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -101.9 dB | -99.4 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -102.1 dB | -102.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0003 | 3/3 | k=2: 12000.000 Hz, -83.9 dB | -82.9 | 8.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8640 | 0.0006 | 23/23 | k=1: 999.864 Hz, -72.9 dB | -74.1 | 62.4 % |
| Netz 50 Hz | Kanal 4 | 49.9807 | 0.0000 | 1/19 | k=1: 49.981 Hz, -106.8 dB | -108.7 | 0.0 % |
| Mischprodukte n·999.8640 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8640 | 0.0019 | 4 | k=-3·f1+4·f2: 21000.409 Hz, -121.5 dB | -119.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.001 Hz, -100.4 dB | -98.7 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -100.8 dB | -101.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -73.9 | 56.3 | usb1k·1 |
| 1999.728 | -81.4 | 50.5 | usb1k·2 |
| 12000.000 | -83.4 | 53.7 | fs8·2 |
| 6000.000 | -84.0 | 51.8 | fs8·1 |
| 2999.592 | -83.0 | 50.9 | usb1k·3 |
| 18000.000 | -86.0 | 52.1 | fs8·3 |
| 3999.456 | -87.4 | 47.5 | usb1k·4 |
| 9998.640 | -88.4 | 49.0 | usb1k·10 |
| 4999.321 | -89.5 | 46.3 | usb1k·5 |
| 16997.688 | -90.6 | 47.8 | usb1k·17 |
| 6999.047 | -91.2 | 43.9 | usb1k·7 |
| 15997.823 | -90.8 | 46.2 | usb1k·16 |
| 18997.415 | -92.1 | 46.0 | usb1k·19 |
| 11998.368 | -92.6 | 44.6 | usb1k·12 |
| 8998.776 | -91.6 | 45.3 | usb1k·9 |
| 5999.185 | -94.3 | 41.5 | usb1k·6 |
| 7998.912 | -95.6 | 40.3 | usb1k·8 |
| 13998.095 | -96.2 | 41.0 | usb1k·14 |
| 19997.279 | -96.7 | 41.4 | usb1k·20 |
| 12998.232 | -98.4 | 38.9 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -73.5 | 57.9 | usb1k·1 |
| 1999.728 | -80.8 | 52.6 | usb1k·2 |
| 12000.000 | -83.6 | 54.7 | fs8·2 |
| 6000.000 | -84.1 | 52.7 | fs8·1 |
| 2999.592 | -83.0 | 52.6 | usb1k·3 |
| 18000.000 | -86.1 | 53.1 | fs8·3 |
| 3999.456 | -87.2 | 49.1 | usb1k·4 |
| 4999.320 | -88.8 | 48.1 | usb1k·5 |
| 9998.640 | -88.6 | 50.3 | usb1k·10 |
| 16997.687 | -90.6 | 48.3 | usb1k·17 |
| 6999.047 | -91.4 | 45.2 | usb1k·7 |
| 15997.823 | -90.5 | 48.3 | usb1k·16 |
| 18997.415 | -91.9 | 47.4 | usb1k·19 |
| 8998.776 | -91.1 | 47.0 | usb1k·9 |
| 11998.367 | -92.5 | 46.0 | usb1k·12 |
| 5999.185 | -94.0 | 42.8 | usb1k·6 |
| 7998.911 | -94.9 | 42.2 | usb1k·8 |
| 13998.095 | -96.3 | 42.2 | usb1k·14 |
| 19997.279 | -97.0 | 42.5 | usb1k·20 |
| 12998.232 | -98.4 | 40.2 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -75.9 | 60.5 | usb1k·1 |
| 1999.728 | -83.3 | 54.7 | usb1k·2 |
| 12000.000 | -84.4 | 57.0 | fs8·2 |
| 6000.000 | -84.6 | 56.4 | fs8·1 |
| 2999.592 | -84.7 | 54.8 | usb1k·3 |
| 17999.999 | -86.4 | 55.1 | fs8·3 |
| 3999.456 | -88.4 | 52.0 | usb1k·4 |
| 9998.640 | -89.0 | 52.7 | usb1k·10 |
| 4999.321 | -90.6 | 50.3 | usb1k·5 |
| 16997.688 | -91.5 | 50.5 | usb1k·17 |
| 18997.415 | -92.4 | 49.2 | usb1k·19 |
| 15997.823 | -91.6 | 50.1 | usb1k·16 |
| 6999.047 | -93.0 | 47.3 | usb1k·7 |
| 11998.368 | -93.4 | 48.0 | usb1k·12 |
| 8998.776 | -92.6 | 48.7 | usb1k·9 |
| 5999.185 | -96.2 | 44.8 | usb1k·6 |
| 19997.279 | -96.8 | 45.0 | usb1k·20 |
| 7998.912 | -97.3 | 43.3 | usb1k·8 |
| 12998.231 | -98.1 | 43.2 | usb1k·13 |
| 13998.096 | -98.9 | 42.9 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -72.9 | 57.5 | usb1k·1 |
| 1999.728 | -79.7 | 52.8 | usb1k·2 |
| 12000.000 | -83.9 | 53.9 | fs8·2 |
| 6000.000 | -84.2 | 51.8 | fs8·1 |
| 2999.592 | -82.8 | 51.8 | usb1k·3 |
| 18000.000 | -86.5 | 51.8 | fs8·3 |
| 3999.456 | -87.1 | 48.2 | usb1k·4 |
| 4999.320 | -88.0 | 48.1 | usb1k·5 |
| 9998.640 | -88.8 | 48.8 | usb1k·10 |
| 16997.687 | -90.6 | 47.5 | usb1k·17 |
| 15997.823 | -90.3 | 47.0 | usb1k·16 |
| 6999.047 | -91.4 | 44.3 | usb1k·7 |
| 8998.776 | -90.4 | 47.0 | usb1k·9 |
| 18997.414 | -92.0 | 46.3 | usb1k·19 |
| 11998.367 | -92.3 | 45.6 | usb1k·12 |
| 5999.184 | -92.9 | 43.1 | usb1k·6 |
| 7998.911 | -94.0 | 42.0 | usb1k·8 |
| 13998.095 | -96.0 | 41.7 | usb1k·14 |
| 19997.279 | -97.2 | 41.0 | usb1k·20 |
| 12998.232 | -97.9 | 39.9 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.02 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.46 | 1.54 | 0.22 |
| mains50 | Kanal 1 | 11/11 | 2394.35 | -4888.13 | 2.97 |
| other1 | Kanal 1 | 11/11 | 4.09 | -4.63 | 0.22 |
| other2 | Kanal 1 | 11/11 | 0.25 | -0.43 | 0.25 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.02 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.42 | 1.45 | 0.25 |
| mains50 | Kanal 2 | 11/11 | 2309.20 | 1311.00 | 1.98 |
| other1 | Kanal 2 | 11/11 | 0.76 | 1.48 | 0.28 |
| other2 | Kanal 2 | 11/11 | 0.25 | -0.18 | 0.19 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.02 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.47 | 1.56 | 0.13 |
| mains50 | Kanal 3 | 11/11 | 426.59 | 220.26 | 1.60 |
| other1 | Kanal 3 | 11/11 | 1.92 | 3.05 | 0.45 |
| other2 | Kanal 3 | 11/11 | 0.16 | -0.01 | 0.19 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.43 | 1.37 | 0.26 |
| mains50 | Kanal 4 | 10/11 | 2299.28 | 1214.95 | 1.72 |
| other1 | Kanal 4 | 11/11 | 1.59 | -0.57 | 0.30 |
| other2 | Kanal 4 | 11/11 | 0.27 | -0.38 | 0.23 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 4.39 | 0.31 s (3.22 Hz) | 24.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 33.5 |
| Kanal 2 | breitbandig | 3.76 | 0.31 s (3.22 Hz) | 27.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 35.7 |
| Kanal 3 | breitbandig | 4.10 | 0.31 s (3.22 Hz) | 26.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.9 |
| Kanal 4 | breitbandig | 3.48 | 0.31 s (3.22 Hz) | 28.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 33.3 |

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
| Kanal 1 | 1.00 | 0.99 | 0.99 | 0.98 |
| Kanal 2 | 0.99 | 1.00 | 0.99 | 0.99 |
| Kanal 3 | 0.99 | 0.99 | 1.00 | 0.97 |
| Kanal 4 | 0.98 | 0.99 | 0.97 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](D90b-vor-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D90b-vor-r1_psd.png)

### Kammprofile

![Kammprofile](D90b-vor-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](D90b-vor-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 10:34:48. Stream-Meldungen: 0. owl_read: reports/owl_read/D90b-vor-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. D90b vorher: vor der Masse-Brücke Pin 15 ↔ Pin 33, acdc1 im Case, Regler 63/64/71/50, keine Kabel, Slot 1
