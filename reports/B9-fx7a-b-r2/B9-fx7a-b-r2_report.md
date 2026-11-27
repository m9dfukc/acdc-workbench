# Report B9-fx7a-b-r2: B9-fx7a-b-r2 – acdc1 fx7a-open-inputs-9b, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 9 v22.4.r-fx7a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx7a am Ende, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx7a-open-inputs-9b-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx7a-b-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -68.6 | -74.2 | -70.1 | -70.8 | -85.4 | -70.4 | -94.6 | -70.1 | 61 % | -74.2 | 4.1 |
| Kanal 2 | -7.1 | -70.1 | -76.4 | -71.2 | -71.8 | -87.5 | -71.5 | -94.8 | -71.2 | 68 % | -76.1 | 4.9 |
| Kanal 3 | -5.4 | -72.0 | -77.7 | -73.4 | -74.0 | -91.9 | -73.6 | -95.6 | -73.4 | 73 % | -79.1 | 5.7 |
| Kanal 4 | -6.2 | -69.5 | -77.7 | -70.2 | -70.8 | -87.2 | -70.5 | -95.1 | -70.2 | 65 % | -74.7 | 4.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -84.3 dB | -83.0 | 5.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8674 | 0.0003 | 23/23 | k=1: 999.868 Hz, -71.2 dB | -72.6 | 56.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0003 | 0.0004 | 8/11 | k=1: 2000.001 Hz, -97.6 dB | -96.5 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0005 | 4/7 | k=1: 3000.001 Hz, -98.1 dB | -98.9 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -84.3 dB | -83.1 | 6.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8674 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.0 dB | -73.4 | 61.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.001 Hz, -98.2 dB | -96.8 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.6 dB | -99.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.9 dB | -83.7 | 9.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8674 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.4 | 63.7 % |
| Mischprodukte n·999.8674 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8674 | 0.0002 | 3 | k=-3·f1+4·f2: 21000.398 Hz, -122.2 dB | -121.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.001 Hz, -99.7 dB | -97.5 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -99.9 dB | -100.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.5 dB | -83.3 | 4.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8674 | 0.0004 | 23/23 | k=1: 999.868 Hz, -71.2 dB | -72.5 | 59.7 % |
| Mischprodukte n·999.8674 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8674 | 0.0051 | 2 | k=-1·f1+2·f2: 11000.128 Hz, -117.4 dB | -117.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.001 Hz, -98.4 dB | -97.0 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0002 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -71.2 | 57.2 | usb1k·1 |
| 1999.735 | -78.3 | 52.0 | usb1k·2 |
| 2999.602 | -81.5 | 50.0 | usb1k·3 |
| 6000.000 | -84.3 | 47.8 | fs8·1 |
| 12000.000 | -84.8 | 48.8 | fs8·2 |
| 18000.000 | -85.4 | 49.3 | fs8·3 |
| 3999.470 | -86.7 | 44.3 | usb1k·4 |
| 4999.337 | -87.8 | 43.6 | usb1k·5 |
| 15997.878 | -89.1 | 45.2 | usb1k·16 |
| 9998.674 | -88.9 | 44.2 | usb1k·10 |
| 8998.806 | -89.7 | 43.4 | usb1k·9 |
| 16997.745 | -91.6 | 42.9 | usb1k·17 |
| 18997.480 | -92.0 | 42.9 | usb1k·19 |
| 6999.072 | -91.9 | 40.3 | usb1k·7 |
| 5999.204 | -92.7 | 39.2 | usb1k·6 |
| 7998.939 | -92.4 | 39.8 | usb1k·8 |
| 11998.408 | -92.6 | 41.1 | usb1k·12 |
| 20997.215 | -94.4 | 40.6 | usb1k·21 |
| 12998.275 | -94.6 | 39.7 | usb1k·13 |
| 2000.001 | -97.6 | 32.7 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.0 | 58.3 | usb1k·1 |
| 1999.735 | -79.3 | 52.6 | usb1k·2 |
| 2999.602 | -82.2 | 51.0 | usb1k·3 |
| 6000.000 | -84.3 | 49.6 | fs8·1 |
| 12000.000 | -85.1 | 50.3 | fs8·2 |
| 18000.000 | -85.5 | 51.1 | fs8·3 |
| 3999.470 | -87.2 | 45.7 | usb1k·4 |
| 4999.337 | -88.8 | 44.7 | usb1k·5 |
| 9998.674 | -89.1 | 46.0 | usb1k·10 |
| 15997.878 | -89.6 | 46.5 | usb1k·16 |
| 8998.806 | -90.2 | 45.1 | usb1k·9 |
| 18997.480 | -92.3 | 44.5 | usb1k·19 |
| 16997.745 | -92.0 | 43.8 | usb1k·17 |
| 6999.072 | -92.6 | 41.5 | usb1k·7 |
| 7998.939 | -93.3 | 40.8 | usb1k·8 |
| 5999.204 | -93.9 | 40.0 | usb1k·6 |
| 11998.408 | -93.2 | 42.2 | usb1k·12 |
| 20997.215 | -95.1 | 41.5 | usb1k·21 |
| 12998.275 | -94.9 | 40.9 | usb1k·13 |
| 2000.001 | -98.2 | 33.6 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 60.3 | usb1k·1 |
| 1999.735 | -81.3 | 54.3 | usb1k·2 |
| 2999.602 | -83.8 | 53.2 | usb1k·3 |
| 6000.000 | -84.9 | 52.1 | fs8·1 |
| 12000.000 | -85.8 | 52.1 | fs8·2 |
| 18000.000 | -85.8 | 53.0 | fs8·3 |
| 3999.470 | -88.4 | 47.8 | usb1k·4 |
| 4999.337 | -90.3 | 45.9 | usb1k·5 |
| 9998.674 | -89.6 | 48.3 | usb1k·10 |
| 15997.878 | -90.6 | 47.8 | usb1k·16 |
| 8998.806 | -91.3 | 46.5 | usb1k·9 |
| 18997.480 | -92.6 | 46.3 | usb1k·19 |
| 16997.745 | -93.2 | 45.2 | usb1k·17 |
| 6999.072 | -93.9 | 43.2 | usb1k·7 |
| 11998.408 | -94.3 | 43.8 | usb1k·12 |
| 7998.939 | -95.4 | 41.7 | usb1k·8 |
| 20997.215 | -96.4 | 42.9 | usb1k·21 |
| 12998.276 | -95.8 | 42.7 | usb1k·13 |
| 5999.204 | -97.0 | 39.9 | usb1k·6 |
| 10998.541 | -98.0 | 39.4 | usb1k·11 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -71.2 | 58.4 | usb1k·1 |
| 1999.735 | -77.5 | 53.3 | usb1k·2 |
| 2999.603 | -81.8 | 49.9 | usb1k·3 |
| 6000.000 | -84.5 | 48.1 | fs8·1 |
| 12000.000 | -85.3 | 48.5 | fs8·2 |
| 18000.000 | -85.6 | 49.4 | fs8·3 |
| 3999.470 | -86.8 | 44.7 | usb1k·4 |
| 4999.337 | -87.3 | 44.6 | usb1k·5 |
| 15997.878 | -88.8 | 45.4 | usb1k·16 |
| 8998.806 | -89.1 | 44.1 | usb1k·9 |
| 9998.674 | -89.4 | 44.4 | usb1k·10 |
| 16997.745 | -92.0 | 42.7 | usb1k·17 |
| 5999.204 | -92.2 | 40.3 | usb1k·6 |
| 18997.480 | -92.4 | 42.9 | usb1k·19 |
| 6999.072 | -92.0 | 40.3 | usb1k·7 |
| 7998.939 | -92.4 | 40.6 | usb1k·8 |
| 20997.215 | -94.1 | 41.3 | usb1k·21 |
| 11998.409 | -92.6 | 41.2 | usb1k·12 |
| 12998.275 | -94.4 | 39.8 | usb1k·13 |
| 13998.143 | -96.5 | 37.8 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.00 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.15 | 0.30 | 0.10 |
| other1 | Kanal 1 | 11/11 | 0.52 | -0.60 | 0.11 |
| other2 | Kanal 1 | 11/11 | 0.24 | 0.23 | 0.43 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.16 | 0.34 | 0.11 |
| other1 | Kanal 2 | 11/11 | 0.41 | -0.66 | 0.08 |
| other2 | Kanal 2 | 11/11 | 0.21 | 0.13 | 0.31 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.18 | 0.31 | 0.09 |
| other1 | Kanal 3 | 11/11 | 0.32 | -0.47 | 0.18 |
| other2 | Kanal 3 | 11/11 | 0.12 | 0.13 | 0.28 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.00 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.12 | 0.29 | 0.15 |
| other1 | Kanal 4 | 11/11 | 0.62 | -1.12 | 0.11 |
| other2 | Kanal 4 | 11/11 | 0.21 | 0.25 | 0.37 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.14 | 0.31 s (3.18 Hz) | 21.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 34.4 |
| Kanal 2 | breitbandig | 0.97 | 0.31 s (3.18 Hz) | 22.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 36.7 |
| Kanal 3 | breitbandig | 1.06 | 0.31 s (3.18 Hz) | 22.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 40.3 |
| Kanal 4 | breitbandig | 0.71 | 0.31 s (3.18 Hz) | 21.7 |
| Kanal 4 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 35.4 |

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
| Kanal 1 | 1.00 | 0.97 | 0.96 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.96 | 0.96 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.97 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx7a-b-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx7a-b-r2_psd.png)

### Kammprofile

![Kammprofile](B9-fx7a-b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx7a-b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:22:27. Stream-Meldungen: 0. owl_read: reports/owl_read/B9-fx7a-b-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Start über dfu-util :leave nach dem Readback, kein Kaltstart (Case blieb an). Oszillator im Case abgesteckt (Nutzer). messlog D79.
