# Report B9-fx7a-c-r1: B9-fx7a-c-r1 – acdc1 fx7a-open-inputs-9c, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 9 v22.4.r-fx7a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx7a nach Kaltstart, direkt nach B9-fx7a-b (Trennung Drift gegen Start über :leave), Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx7a-open-inputs-9c-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx7a-c-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.7 | -68.8 | -76.4 | -69.7 | -70.3 | -85.6 | -69.9 | -94.7 | -69.7 | 62 % | -73.8 | 4.2 |
| Kanal 2 | -7.1 | -70.3 | -78.7 | -70.9 | -71.5 | -87.6 | -71.2 | -94.8 | -71.0 | 66 % | -75.7 | 4.7 |
| Kanal 3 | -5.4 | -72.4 | -81.6 | -73.0 | -73.6 | -92.1 | -73.2 | -95.7 | -73.0 | 73 % | -78.7 | 5.7 |
| Kanal 4 | -6.2 | -69.4 | -79.5 | -69.9 | -70.5 | -87.2 | -70.1 | -95.0 | -69.9 | 64 % | -74.3 | 4.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -83.1 | 4.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -70.7 dB | -72.1 | 57.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -96.6 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0005 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.0 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.5 dB | -83.3 | 5.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -71.8 dB | -73.1 | 60.5 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.5 dB | -96.8 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -85.0 dB | -83.9 | 8.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -74.9 | 64.6 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0006 | 2 | k=1·f1+3·f2: 18999.867 Hz, -122.9 dB | -123.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -100.0 dB | -97.5 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -100.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -84.8 dB | -83.5 | 4.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -70.8 dB | -72.2 | 59.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -96.9 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.0 dB | -99.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -70.7 | 57.4 | usb1k·1 |
| 1999.735 | -77.8 | 51.9 | usb1k·2 |
| 2999.603 | -81.3 | 49.3 | usb1k·3 |
| 6000.000 | -84.4 | 47.1 | fs8·1 |
| 12000.000 | -84.5 | 49.0 | fs8·2 |
| 18000.000 | -86.0 | 48.4 | fs8·3 |
| 3999.471 | -86.0 | 44.9 | usb1k·4 |
| 4999.338 | -86.8 | 44.6 | usb1k·5 |
| 15997.882 | -88.9 | 45.5 | usb1k·16 |
| 9998.676 | -88.5 | 44.6 | usb1k·10 |
| 8998.809 | -89.1 | 43.5 | usb1k·9 |
| 16997.750 | -91.4 | 42.8 | usb1k·17 |
| 5999.206 | -90.9 | 40.5 | usb1k·6 |
| 6999.074 | -91.1 | 41.0 | usb1k·7 |
| 18997.485 | -92.2 | 42.8 | usb1k·19 |
| 7998.941 | -91.8 | 40.5 | usb1k·8 |
| 11998.412 | -92.8 | 40.9 | usb1k·12 |
| 20997.220 | -93.8 | 41.3 | usb1k·21 |
| 12998.279 | -94.3 | 39.0 | usb1k·13 |
| 13998.147 | -97.3 | 36.1 | usb1k·14 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -71.8 | 58.2 | usb1k·1 |
| 1999.735 | -79.0 | 52.8 | usb1k·2 |
| 2999.603 | -82.2 | 50.4 | usb1k·3 |
| 6000.000 | -84.5 | 49.0 | fs8·1 |
| 12000.000 | -84.7 | 50.8 | fs8·2 |
| 18000.000 | -86.0 | 50.3 | fs8·3 |
| 3999.471 | -86.5 | 46.4 | usb1k·4 |
| 4999.338 | -87.9 | 45.4 | usb1k·5 |
| 15997.882 | -89.5 | 46.7 | usb1k·16 |
| 9998.676 | -88.8 | 45.9 | usb1k·10 |
| 8998.809 | -89.7 | 44.7 | usb1k·9 |
| 16997.750 | -92.1 | 43.9 | usb1k·17 |
| 18997.485 | -92.4 | 44.1 | usb1k·19 |
| 6999.074 | -91.9 | 41.9 | usb1k·7 |
| 5999.206 | -92.5 | 40.9 | usb1k·6 |
| 11998.412 | -93.5 | 42.2 | usb1k·12 |
| 7998.941 | -93.0 | 41.2 | usb1k·8 |
| 20997.221 | -94.4 | 42.6 | usb1k·21 |
| 12998.279 | -95.0 | 40.4 | usb1k·13 |
| 2000.000 | -98.5 | 33.3 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 60.4 | usb1k·1 |
| 1999.735 | -81.2 | 54.0 | usb1k·2 |
| 2999.603 | -83.6 | 52.2 | usb1k·3 |
| 6000.000 | -85.0 | 51.5 | fs8·1 |
| 12000.000 | -85.4 | 52.4 | fs8·2 |
| 18000.000 | -86.5 | 52.4 | fs8·3 |
| 3999.471 | -87.5 | 48.5 | usb1k·4 |
| 4999.338 | -89.5 | 47.0 | usb1k·5 |
| 9998.676 | -89.3 | 48.3 | usb1k·10 |
| 15997.882 | -90.6 | 48.3 | usb1k·16 |
| 8998.809 | -91.0 | 46.3 | usb1k·9 |
| 18997.485 | -92.9 | 46.1 | usb1k·19 |
| 16997.750 | -93.1 | 45.4 | usb1k·17 |
| 6999.074 | -93.1 | 43.7 | usb1k·7 |
| 11998.411 | -94.7 | 43.2 | usb1k·12 |
| 5999.206 | -94.9 | 41.5 | usb1k·6 |
| 7998.941 | -94.7 | 42.2 | usb1k·8 |
| 20997.220 | -95.9 | 43.0 | usb1k·21 |
| 12998.279 | -96.0 | 41.7 | usb1k·13 |
| 17997.618 | -99.5 | 39.5 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -70.8 | 58.1 | usb1k·1 |
| 1999.735 | -77.3 | 53.1 | usb1k·2 |
| 2999.603 | -81.5 | 49.7 | usb1k·3 |
| 6000.000 | -84.8 | 47.4 | fs8·1 |
| 12000.000 | -84.9 | 48.7 | fs8·2 |
| 18000.000 | -86.1 | 48.5 | fs8·3 |
| 3999.471 | -86.1 | 45.5 | usb1k·4 |
| 4999.338 | -86.4 | 45.1 | usb1k·5 |
| 15997.882 | -88.7 | 45.8 | usb1k·16 |
| 9998.676 | -89.0 | 44.2 | usb1k·10 |
| 8998.809 | -88.7 | 43.8 | usb1k·9 |
| 5999.206 | -90.7 | 41.4 | usb1k·6 |
| 16997.750 | -91.8 | 42.8 | usb1k·17 |
| 6999.074 | -91.1 | 41.1 | usb1k·7 |
| 18997.485 | -92.5 | 42.1 | usb1k·19 |
| 11998.412 | -92.6 | 41.1 | usb1k·12 |
| 7998.941 | -91.8 | 40.9 | usb1k·8 |
| 20997.221 | -93.7 | 42.0 | usb1k·21 |
| 12998.279 | -94.3 | 39.5 | usb1k·13 |
| 13998.147 | -97.0 | 36.5 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.04 | 0.01 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.19 | 0.08 | 0.03 |
| other1 | Kanal 1 | 11/11 | 0.84 | 0.29 | 0.05 |
| other2 | Kanal 1 | 11/11 | 0.29 | 0.53 | 0.32 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.01 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.19 | 0.03 | 0.03 |
| other1 | Kanal 2 | 11/11 | 0.68 | 0.06 | 0.04 |
| other2 | Kanal 2 | 11/11 | 0.30 | 0.41 | 0.31 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.21 | 0.08 | 0.03 |
| other1 | Kanal 3 | 11/11 | 0.80 | 0.07 | 0.04 |
| other2 | Kanal 3 | 11/11 | 0.21 | 0.31 | 0.21 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.04 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.19 | 0.06 | 0.03 |
| other1 | Kanal 4 | 11/11 | 2.09 | 0.72 | 0.04 |
| other2 | Kanal 4 | 11/11 | 0.30 | 0.44 | 0.34 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.93 | 0.31 s (3.18 Hz) | 23.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 35.5 |
| Kanal 2 | breitbandig | 0.82 | 0.31 s (3.18 Hz) | 24.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 36.8 |
| Kanal 3 | breitbandig | 0.67 | 7.50 s (0.13 Hz) | 23.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 40.6 |
| Kanal 4 | breitbandig | 0.64 | 0.31 s (3.18 Hz) | 23.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 34.9 |

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
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.96 | 0.95 | 1.00 | 0.93 |
| Kanal 4 | 0.94 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx7a-c-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx7a-c-r1_psd.png)

### Kammprofile

![Kammprofile](B9-fx7a-c-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx7a-c-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:30:54. Stream-Meldungen: 0. owl_read: out/owl_read/B9-fx7a-c-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Kaltstart durch den Nutzer (Case aus, USB ab, Case an, USB an). Oszillator im Case abgesteckt. messlog D79.
