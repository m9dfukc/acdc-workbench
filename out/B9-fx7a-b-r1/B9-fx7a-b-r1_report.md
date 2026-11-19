# Report B9-fx7a-b-r1: B9-fx7a-b-r1 – acdc1 fx7a-open-inputs-9b, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 9 v22.4.r-fx7a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx7a am Ende, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx7a-open-inputs-9b-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx7a-b-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -67.2 | -70.5 | -70.0 | -70.7 | -85.4 | -70.3 | -94.4 | -70.0 | 61 % | -74.2 | 4.1 |
| Kanal 2 | -7.1 | -68.8 | -72.6 | -71.1 | -71.7 | -87.4 | -71.4 | -94.7 | -71.1 | 66 % | -75.9 | 4.7 |
| Kanal 3 | -5.3 | -70.6 | -73.9 | -73.3 | -74.0 | -91.8 | -73.5 | -95.5 | -73.4 | 73 % | -79.0 | 5.7 |
| Kanal 4 | -6.2 | -68.7 | -74.2 | -70.1 | -70.7 | -87.1 | -70.3 | -94.9 | -70.1 | 63 % | -74.4 | 4.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0001 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.3 dB | -83.0 | 5.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8672 | 0.0003 | 23/23 | k=1: 999.867 Hz, -71.2 dB | -72.6 | 56.1 % |
| Mischprodukte n·999.8672 + m·6000.0001 Hz (m = ±1…±4) | Kanal 1 | 999.8672 | 0.0010 | 2 | k=5·f1+2·f2: 16999.336 Hz, -119.9 dB | -120.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.5 dB | -96.4 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -98.8 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -84.5 dB | -83.1 | 6.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8672 | 0.0003 | 23/23 | k=1: 999.867 Hz, -72.0 dB | -73.4 | 60.1 % |
| Mischprodukte n·999.8672 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8672 | 0.0006 | 2 | k=5·f1+2·f2: 16999.337 Hz, -119.9 dB | -120.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.2 dB | -96.6 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.6 dB | -99.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0001 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -85.0 dB | -83.7 | 9.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8672 | 0.0003 | 23/23 | k=1: 999.867 Hz, -74.1 dB | -75.3 | 63.6 % |
| Mischprodukte n·999.8672 + m·6000.0001 Hz (m = ±1…±4) | Kanal 3 | 999.8672 | 0.0034 | 7 | k=5·f1+2·f2: 16999.336 Hz, -121.4 dB | -117.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -97.4 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.9 dB | -100.0 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -84.7 dB | -83.4 | 4.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8672 | 0.0004 | 23/23 | k=1: 999.867 Hz, -71.1 dB | -72.4 | 58.5 % |
| Mischprodukte n·999.8672 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8672 | 0.0083 | 2 | k=-1·f1+3·f2: 17000.121 Hz, -119.4 dB | -120.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -96.9 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0005 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -71.2 | 58.0 | usb1k·1 |
| 1999.734 | -78.1 | 52.5 | usb1k·2 |
| 2999.602 | -81.8 | 48.9 | usb1k·3 |
| 12000.000 | -84.3 | 49.4 | fs8·2 |
| 6000.000 | -84.4 | 47.2 | fs8·1 |
| 18000.000 | -85.8 | 49.2 | fs8·3 |
| 3999.469 | -86.2 | 44.9 | usb1k·4 |
| 4999.336 | -87.1 | 44.4 | usb1k·5 |
| 9998.672 | -88.7 | 44.5 | usb1k·10 |
| 8998.805 | -89.4 | 43.5 | usb1k·9 |
| 15997.875 | -88.8 | 45.9 | usb1k·16 |
| 6999.070 | -91.1 | 41.4 | usb1k·7 |
| 5999.203 | -91.4 | 40.2 | usb1k·6 |
| 7998.936 | -92.7 | 40.1 | usb1k·8 |
| 16997.742 | -91.5 | 43.8 | usb1k·17 |
| 18997.476 | -92.0 | 43.3 | usb1k·19 |
| 11998.406 | -93.0 | 40.7 | usb1k·12 |
| 20997.210 | -94.2 | 41.0 | usb1k·21 |
| 12998.273 | -94.6 | 39.3 | usb1k·13 |
| 2000.000 | -97.5 | 33.1 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.0 | 59.1 | usb1k·1 |
| 1999.734 | -79.0 | 53.3 | usb1k·2 |
| 2999.602 | -82.5 | 49.8 | usb1k·3 |
| 6000.000 | -84.5 | 49.1 | fs8·1 |
| 12000.000 | -84.5 | 51.1 | fs8·2 |
| 18000.000 | -85.8 | 50.7 | fs8·3 |
| 3999.469 | -86.6 | 46.3 | usb1k·4 |
| 4999.336 | -88.0 | 45.0 | usb1k·5 |
| 9998.672 | -89.0 | 46.3 | usb1k·10 |
| 8998.805 | -89.9 | 44.6 | usb1k·9 |
| 15997.875 | -89.3 | 47.7 | usb1k·16 |
| 6999.070 | -91.8 | 42.3 | usb1k·7 |
| 5999.203 | -92.7 | 40.8 | usb1k·6 |
| 18997.476 | -92.2 | 44.8 | usb1k·19 |
| 16997.742 | -91.9 | 44.6 | usb1k·17 |
| 7998.937 | -93.7 | 41.0 | usb1k·8 |
| 11998.406 | -93.6 | 42.1 | usb1k·12 |
| 20997.210 | -94.7 | 42.7 | usb1k·21 |
| 12998.273 | -95.1 | 40.2 | usb1k·13 |
| 2000.000 | -98.2 | 34.2 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.1 | 60.7 | usb1k·1 |
| 1999.734 | -81.3 | 54.7 | usb1k·2 |
| 2999.601 | -84.3 | 51.3 | usb1k·3 |
| 6000.000 | -85.0 | 51.5 | fs8·1 |
| 12000.000 | -85.2 | 52.8 | fs8·2 |
| 18000.000 | -86.3 | 52.7 | fs8·3 |
| 3999.469 | -87.8 | 48.3 | usb1k·4 |
| 4999.336 | -89.4 | 46.7 | usb1k·5 |
| 9998.672 | -89.4 | 48.5 | usb1k·10 |
| 8998.805 | -91.0 | 46.3 | usb1k·9 |
| 15997.875 | -90.3 | 48.9 | usb1k·16 |
| 6999.070 | -93.5 | 43.6 | usb1k·7 |
| 18997.476 | -92.6 | 46.7 | usb1k·19 |
| 16997.742 | -93.1 | 46.0 | usb1k·17 |
| 5999.203 | -95.0 | 41.6 | usb1k·6 |
| 11998.406 | -94.7 | 43.4 | usb1k·12 |
| 7998.937 | -95.7 | 41.7 | usb1k·8 |
| 12998.273 | -95.8 | 42.5 | usb1k·13 |
| 20997.210 | -96.1 | 43.5 | usb1k·21 |
| 10998.539 | -98.5 | 39.7 | usb1k·11 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -71.1 | 58.9 | usb1k·1 |
| 1999.734 | -77.6 | 53.2 | usb1k·2 |
| 2999.602 | -82.0 | 49.0 | usb1k·3 |
| 6000.000 | -84.7 | 46.9 | fs8·1 |
| 12000.000 | -84.7 | 49.0 | fs8·2 |
| 18000.000 | -86.0 | 48.6 | fs8·3 |
| 3999.469 | -86.3 | 45.1 | usb1k·4 |
| 4999.335 | -86.7 | 45.0 | usb1k·5 |
| 8998.805 | -89.1 | 43.9 | usb1k·9 |
| 9998.672 | -89.1 | 44.4 | usb1k·10 |
| 15997.875 | -88.7 | 46.2 | usb1k·16 |
| 5999.203 | -90.9 | 40.7 | usb1k·6 |
| 6999.070 | -91.4 | 40.8 | usb1k·7 |
| 7998.937 | -92.6 | 40.6 | usb1k·8 |
| 16997.742 | -91.6 | 43.7 | usb1k·17 |
| 18997.476 | -92.2 | 43.1 | usb1k·19 |
| 11998.406 | -92.9 | 40.9 | usb1k·12 |
| 20997.210 | -94.1 | 41.3 | usb1k·21 |
| 12998.274 | -94.2 | 39.6 | usb1k·13 |
| 13998.141 | -96.6 | 37.8 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.00 | 0.07 |
| usb1k | Kanal 1 | 11/11 | 0.24 | 0.14 | 0.09 |
| other1 | Kanal 1 | 11/11 | 0.75 | 0.47 | 0.16 |
| other2 | Kanal 1 | 11/11 | 0.20 | -0.02 | 0.28 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.00 | 0.08 |
| usb1k | Kanal 2 | 11/11 | 0.22 | 0.05 | 0.17 |
| other1 | Kanal 2 | 11/11 | 0.65 | 0.26 | 0.22 |
| other2 | Kanal 2 | 11/11 | 0.17 | -0.04 | 0.22 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.02 | 0.07 |
| usb1k | Kanal 3 | 11/11 | 0.23 | 0.06 | 0.05 |
| other1 | Kanal 3 | 11/11 | 0.43 | 0.33 | 0.19 |
| other2 | Kanal 3 | 11/11 | 0.17 | 0.02 | 0.15 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.00 | 0.10 |
| usb1k | Kanal 4 | 11/11 | 0.21 | 0.02 | 0.17 |
| other1 | Kanal 4 | 11/11 | 1.51 | 1.39 | 0.23 |
| other2 | Kanal 4 | 11/11 | 0.23 | 0.15 | 0.29 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.05 | 0.31 s (3.18 Hz) | 29.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 35.0 |
| Kanal 2 | breitbandig | 1.85 | 0.31 s (3.18 Hz) | 30.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 37.0 |
| Kanal 3 | breitbandig | 1.94 | 0.31 s (3.22 Hz) | 30.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 40.3 |
| Kanal 4 | breitbandig | 1.31 | 0.31 s (3.18 Hz) | 29.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 35.2 |

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
| Kanal 1 | 1.00 | 0.98 | 0.97 | 0.94 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.97 | 0.96 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.97 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx7a-b-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx7a-b-r1_psd.png)

### Kammprofile

![Kammprofile](B9-fx7a-b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx7a-b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:21:14. Stream-Meldungen: 0. owl_read: out/owl_read/B9-fx7a-b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Start über dfu-util :leave nach dem Readback, kein Kaltstart (Case blieb an). Oszillator im Case abgesteckt (Nutzer). messlog D79.
