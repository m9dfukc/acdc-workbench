# Report D90b-vor-r2: D90b-vor-r2 – acdc1 gnd-vor-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-24 |
| device | acdc1 |
| test | gnd-vor-open-inputs |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261124_acdc1_gnd-vor-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis D90b-vor-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.0 | -63.4 | -64.1 | -72.0 | -72.8 | -85.7 | -72.3 | -96.1 | -72.0 | 67 % | -76.8 | 4.8 |
| Kanal 2 | -6.7 | -65.8 | -67.0 | -72.3 | -72.9 | -87.7 | -72.6 | -96.5 | -72.4 | 73 % | -78.0 | 5.6 |
| Kanal 3 | -4.9 | -67.1 | -68.0 | -74.6 | -75.2 | -92.4 | -74.8 | -97.4 | -74.6 | 82 % | -82.0 | 7.4 |
| Kanal 4 | -5.9 | -65.9 | -67.2 | -71.8 | -72.4 | -87.4 | -72.0 | -96.7 | -71.8 | 71 % | -77.2 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.3 dB | -82.5 | 8.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8652 | 0.0003 | 23/23 | k=1: 999.865 Hz, -73.2 dB | -74.4 | 57.7 % |
| Mischprodukte n·999.8652 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8652 | 0.0016 | 7 | k=-3·f1+4·f2: 21000.404 Hz, -120.3 dB | -116.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.0 dB | -97.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.3 dB | -101.0 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.6 dB | -82.7 | 9.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8652 | 0.0004 | 23/23 | k=1: 999.865 Hz, -73.2 dB | -74.3 | 63.3 % |
| Mischprodukte n·999.8652 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8652 | 0.0015 | 7 | k=8·f1+2·f2: 19998.924 Hz, -121.8 dB | -117.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -98.2 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.7 dB | -101.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.3 dB | -83.2 | 13.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8652 | 0.0004 | 23/23 | k=1: 999.865 Hz, -75.3 dB | -76.3 | 68.0 % |
| Netz 50 Hz | Kanal 3 | 49.9924 | 0.0049 | 3/19 | k=1: 49.991 Hz, -110.5 dB | -110.3 | 0.0 % |
| Mischprodukte n·999.8652 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8652 | 0.0024 | 23 | k=-3·f1+4·f2: 21000.406 Hz, -120.1 dB | -114.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -101.5 dB | -99.2 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -102.0 dB | -102.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.8 dB | -82.9 | 7.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8652 | 0.0004 | 23/23 | k=1: 999.865 Hz, -72.6 dB | -73.8 | 63.3 % |
| Mischprodukte n·999.8652 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8652 | 0.0026 | 6 | k=-3·f1+4·f2: 21000.404 Hz, -121.7 dB | -117.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0006 | 8/11 | k=1: 2000.001 Hz, -99.8 dB | -98.4 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0005 | 4/7 | k=1: 3000.000 Hz, -100.9 dB | -101.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -73.2 | 56.4 | usb1k·1 |
| 1999.730 | -80.7 | 51.3 | usb1k·2 |
| 2999.595 | -82.6 | 51.3 | usb1k·3 |
| 12000.000 | -83.3 | 54.3 | fs8·2 |
| 6000.000 | -83.8 | 51.6 | fs8·1 |
| 18000.000 | -86.3 | 51.8 | fs8·3 |
| 3999.460 | -87.1 | 46.1 | usb1k·4 |
| 9998.652 | -88.3 | 48.5 | usb1k·10 |
| 4999.326 | -88.7 | 46.6 | usb1k·5 |
| 8998.787 | -91.2 | 45.5 | usb1k·9 |
| 16997.708 | -90.2 | 48.1 | usb1k·17 |
| 6999.056 | -90.8 | 44.8 | usb1k·7 |
| 15997.842 | -90.4 | 47.8 | usb1k·16 |
| 18997.438 | -91.8 | 46.5 | usb1k·19 |
| 11998.382 | -92.4 | 45.2 | usb1k·12 |
| 5999.192 | -93.5 | 41.9 | usb1k·6 |
| 7998.921 | -94.8 | 41.1 | usb1k·8 |
| 13998.112 | -95.9 | 41.8 | usb1k·14 |
| 19997.303 | -96.8 | 42.2 | usb1k·20 |
| 12998.247 | -97.8 | 40.0 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -73.2 | 58.1 | usb1k·1 |
| 1999.730 | -80.3 | 53.3 | usb1k·2 |
| 2999.595 | -82.7 | 52.6 | usb1k·3 |
| 12000.000 | -83.6 | 55.6 | fs8·2 |
| 6000.000 | -84.0 | 52.8 | fs8·1 |
| 18000.000 | -86.3 | 52.9 | fs8·3 |
| 3999.460 | -87.0 | 47.8 | usb1k·4 |
| 9998.652 | -88.6 | 49.6 | usb1k·10 |
| 4999.326 | -88.3 | 48.1 | usb1k·5 |
| 8998.787 | -90.9 | 47.0 | usb1k·9 |
| 15997.842 | -90.2 | 48.6 | usb1k·16 |
| 6999.056 | -90.9 | 46.1 | usb1k·7 |
| 16997.708 | -90.4 | 48.9 | usb1k·17 |
| 18997.438 | -91.8 | 47.5 | usb1k·19 |
| 11998.382 | -92.4 | 46.7 | usb1k·12 |
| 5999.192 | -93.6 | 43.2 | usb1k·6 |
| 7998.921 | -94.6 | 42.7 | usb1k·8 |
| 13998.112 | -96.0 | 42.4 | usb1k·14 |
| 19997.303 | -97.1 | 42.7 | usb1k·20 |
| 20997.168 | -98.0 | 41.7 | usb1k·21 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -75.3 | 60.8 | usb1k·1 |
| 1999.730 | -82.8 | 55.3 | usb1k·2 |
| 12000.000 | -84.3 | 57.8 | fs8·2 |
| 6000.000 | -84.4 | 56.3 | fs8·1 |
| 2999.595 | -84.4 | 55.5 | usb1k·3 |
| 18000.000 | -86.7 | 55.3 | fs8·3 |
| 9998.652 | -88.9 | 52.7 | usb1k·10 |
| 3999.460 | -88.1 | 51.2 | usb1k·4 |
| 4999.326 | -90.1 | 50.6 | usb1k·5 |
| 8998.787 | -92.2 | 49.6 | usb1k·9 |
| 16997.708 | -91.2 | 50.0 | usb1k·17 |
| 18997.438 | -92.2 | 49.5 | usb1k·19 |
| 15997.842 | -91.3 | 50.7 | usb1k·16 |
| 11998.382 | -93.3 | 48.7 | usb1k·12 |
| 6999.056 | -92.6 | 48.1 | usb1k·7 |
| 5999.192 | -95.6 | 45.0 | usb1k·6 |
| 19997.303 | -96.9 | 45.1 | usb1k·20 |
| 7998.921 | -96.7 | 44.2 | usb1k·8 |
| 12998.247 | -97.7 | 44.4 | usb1k·13 |
| 13998.112 | -98.8 | 42.9 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -72.6 | 57.8 | usb1k·1 |
| 1999.730 | -79.3 | 53.4 | usb1k·2 |
| 2999.595 | -82.5 | 52.1 | usb1k·3 |
| 12000.000 | -83.8 | 54.5 | fs8·2 |
| 6000.000 | -84.2 | 51.4 | fs8·1 |
| 18000.000 | -86.6 | 51.7 | fs8·3 |
| 3999.461 | -86.9 | 47.5 | usb1k·4 |
| 4999.326 | -87.4 | 47.9 | usb1k·5 |
| 9998.652 | -88.8 | 48.0 | usb1k·10 |
| 8998.787 | -90.2 | 46.7 | usb1k·9 |
| 15997.842 | -89.9 | 48.1 | usb1k·16 |
| 6999.056 | -90.8 | 45.6 | usb1k·7 |
| 16997.708 | -90.4 | 47.9 | usb1k·17 |
| 11998.381 | -92.1 | 46.0 | usb1k·12 |
| 18997.438 | -92.0 | 46.5 | usb1k·19 |
| 5999.192 | -92.6 | 43.0 | usb1k·6 |
| 7998.921 | -93.8 | 42.6 | usb1k·8 |
| 13998.112 | -95.7 | 42.0 | usb1k·14 |
| 19997.304 | -97.4 | 41.1 | usb1k·20 |
| 20997.168 | -97.7 | 41.0 | usb1k·21 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.00 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.31 | 0.92 | 0.17 |
| other1 | Kanal 1 | 11/11 | 1.62 | -2.43 | 0.25 |
| other2 | Kanal 1 | 11/11 | 0.33 | -0.03 | 0.31 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.29 | 0.80 | 0.16 |
| other1 | Kanal 2 | 11/11 | 0.25 | 0.14 | 0.14 |
| other2 | Kanal 2 | 11/11 | 0.25 | 0.09 | 0.24 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.04 |
| usb1k | Kanal 3 | 11/11 | 0.32 | 0.97 | 0.14 |
| mains50 | Kanal 3 | 11/11 | 38.18 | 10.13 | 0.70 |
| other1 | Kanal 3 | 11/11 | 2.24 | -1.64 | 0.32 |
| other2 | Kanal 3 | 11/11 | 0.15 | 0.07 | 0.20 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.01 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.27 | 0.75 | 0.22 |
| other1 | Kanal 4 | 11/11 | 0.38 | -0.05 | 0.17 |
| other2 | Kanal 4 | 11/11 | 0.30 | -0.08 | 0.27 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 4.19 | 15.00 s (0.07 Hz) | 35.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 34.3 |
| Kanal 2 | breitbandig | 3.39 | 15.00 s (0.07 Hz) | 33.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 34.3 |
| Kanal 3 | breitbandig | 3.70 | 15.00 s (0.07 Hz) | 36.4 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 39.8 |
| Kanal 4 | breitbandig | 3.27 | 15.00 s (0.07 Hz) | 34.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 32.8 |

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
| Kanal 1 | 1.00 | 0.98 | 0.98 | 0.98 |
| Kanal 2 | 0.98 | 1.00 | 0.98 | 0.99 |
| Kanal 3 | 0.98 | 0.98 | 1.00 | 0.97 |
| Kanal 4 | 0.98 | 0.99 | 0.97 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](D90b-vor-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D90b-vor-r2_psd.png)

### Kammprofile

![Kammprofile](D90b-vor-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](D90b-vor-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 10:36:01. Stream-Meldungen: 0. owl_read: out/owl_read/D90b-vor-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. D90b vorher: vor der Masse-Brücke Pin 15 ↔ Pin 33, acdc1 im Case, Regler 63/64/71/50, keine Kabel, Slot 1
