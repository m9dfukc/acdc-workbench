# Report B9-fx7a-c-r2: B9-fx7a-c-r2 – acdc1 fx7a-open-inputs-9c, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 9 v22.4.r-fx7a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx7a nach Kaltstart, direkt nach B9-fx7a-b (Trennung Drift gegen Start über :leave), Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx7a-open-inputs-9c-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx7a-c-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -69.1 | -78.9 | -69.6 | -70.3 | -85.8 | -69.9 | -94.5 | -69.6 | 61 % | -73.7 | 4.1 |
| Kanal 2 | -7.2 | -70.4 | -80.2 | -70.9 | -71.6 | -87.8 | -71.2 | -94.8 | -70.9 | 66 % | -75.6 | 4.7 |
| Kanal 3 | -5.4 | -72.6 | -84.5 | -72.9 | -73.6 | -92.4 | -73.1 | -95.6 | -72.9 | 73 % | -78.6 | 5.6 |
| Kanal 4 | -6.2 | -69.3 | -80.0 | -69.7 | -70.4 | -87.5 | -70.0 | -95.1 | -69.7 | 63 % | -74.1 | 4.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.1 dB | -83.1 | 4.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -70.7 dB | -72.1 | 56.5 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -97.7 dB | -96.5 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0005 | 4/7 | k=1: 3000.000 Hz, -97.8 dB | -98.9 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.2 | 5.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -71.7 dB | -73.1 | 60.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.3 dB | -96.8 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -99.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.7 dB | -83.8 | 8.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.9 | 64.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -99.6 dB | -100.0 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -83.4 | 4.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -70.6 dB | -72.0 | 59.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -97.0 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0007 | 4/7 | k=1: 3000.000 Hz, -98.7 dB | -99.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -70.7 | 57.3 | usb1k·1 |
| 1999.736 | -77.8 | 50.5 | usb1k·2 |
| 2999.603 | -81.2 | 49.2 | usb1k·3 |
| 6000.000 | -84.1 | 47.7 | fs8·1 |
| 12000.000 | -84.9 | 48.1 | fs8·2 |
| 18000.000 | -85.6 | 48.5 | fs8·3 |
| 3999.471 | -86.0 | 44.1 | usb1k·4 |
| 4999.339 | -87.0 | 44.3 | usb1k·5 |
| 15997.883 | -89.0 | 44.4 | usb1k·16 |
| 9998.676 | -88.7 | 44.1 | usb1k·10 |
| 8998.809 | -89.0 | 43.7 | usb1k·9 |
| 16997.750 | -91.5 | 42.3 | usb1k·17 |
| 5999.206 | -91.3 | 40.4 | usb1k·6 |
| 18997.486 | -92.1 | 41.9 | usb1k·19 |
| 6999.074 | -91.4 | 40.6 | usb1k·7 |
| 11998.412 | -92.6 | 40.3 | usb1k·12 |
| 7998.941 | -91.8 | 39.9 | usb1k·8 |
| 20997.221 | -93.9 | 39.9 | usb1k·21 |
| 12998.279 | -94.4 | 39.2 | usb1k·13 |
| 13998.147 | -97.1 | 36.6 | usb1k·14 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -71.7 | 58.1 | usb1k·1 |
| 1999.736 | -79.0 | 51.4 | usb1k·2 |
| 2999.603 | -82.1 | 50.3 | usb1k·3 |
| 6000.000 | -84.2 | 49.8 | fs8·1 |
| 12000.000 | -85.2 | 49.8 | fs8·2 |
| 18000.000 | -85.6 | 50.5 | fs8·3 |
| 3999.471 | -86.6 | 45.8 | usb1k·4 |
| 4999.339 | -88.2 | 45.3 | usb1k·5 |
| 15997.883 | -89.5 | 45.5 | usb1k·16 |
| 9998.676 | -89.0 | 45.4 | usb1k·10 |
| 8998.809 | -89.6 | 44.7 | usb1k·9 |
| 16997.750 | -92.1 | 43.8 | usb1k·17 |
| 18997.486 | -92.2 | 43.8 | usb1k·19 |
| 6999.074 | -92.1 | 41.7 | usb1k·7 |
| 5999.206 | -92.8 | 41.1 | usb1k·6 |
| 11998.412 | -93.3 | 41.6 | usb1k·12 |
| 7998.941 | -93.1 | 40.8 | usb1k·8 |
| 20997.221 | -94.6 | 40.8 | usb1k·21 |
| 12998.279 | -94.9 | 40.4 | usb1k·13 |
| 2000.000 | -98.3 | 32.2 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 60.4 | usb1k·1 |
| 1999.736 | -81.1 | 53.1 | usb1k·2 |
| 2999.603 | -83.5 | 52.4 | usb1k·3 |
| 6000.000 | -84.7 | 52.2 | fs8·1 |
| 12000.000 | -85.9 | 51.7 | fs8·2 |
| 18000.000 | -86.0 | 52.3 | fs8·3 |
| 3999.471 | -87.6 | 48.2 | usb1k·4 |
| 4999.339 | -89.9 | 46.7 | usb1k·5 |
| 9998.676 | -89.4 | 47.8 | usb1k·10 |
| 15997.883 | -90.6 | 47.1 | usb1k·16 |
| 8998.809 | -91.0 | 46.6 | usb1k·9 |
| 18997.486 | -92.8 | 45.4 | usb1k·19 |
| 16997.750 | -93.1 | 44.9 | usb1k·17 |
| 6999.074 | -93.3 | 43.8 | usb1k·7 |
| 11998.412 | -94.4 | 43.2 | usb1k·12 |
| 7998.941 | -94.7 | 41.7 | usb1k·8 |
| 12998.279 | -96.0 | 42.0 | usb1k·13 |
| 5999.206 | -95.5 | 41.3 | usb1k·6 |
| 20997.221 | -96.0 | 42.0 | usb1k·21 |
| 10998.544 | -98.2 | 39.6 | usb1k·11 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -70.6 | 58.3 | usb1k·1 |
| 1999.736 | -77.4 | 51.6 | usb1k·2 |
| 2999.603 | -81.3 | 49.8 | usb1k·3 |
| 6000.000 | -84.4 | 48.0 | fs8·1 |
| 12000.000 | -85.4 | 47.6 | fs8·2 |
| 18000.000 | -85.8 | 48.5 | fs8·3 |
| 3999.471 | -86.2 | 45.0 | usb1k·4 |
| 4999.339 | -86.6 | 45.2 | usb1k·5 |
| 15997.883 | -88.9 | 44.4 | usb1k·16 |
| 8998.809 | -88.7 | 43.8 | usb1k·9 |
| 9998.676 | -89.0 | 44.1 | usb1k·10 |
| 5999.206 | -90.6 | 41.8 | usb1k·6 |
| 16997.750 | -91.6 | 42.5 | usb1k·17 |
| 18997.486 | -92.2 | 42.1 | usb1k·19 |
| 6999.074 | -91.4 | 40.8 | usb1k·7 |
| 11998.412 | -92.4 | 40.6 | usb1k·12 |
| 7998.941 | -91.5 | 40.5 | usb1k·8 |
| 12998.279 | -94.3 | 39.6 | usb1k·13 |
| 20997.221 | -94.1 | 39.9 | usb1k·21 |
| 13998.147 | -97.4 | 36.2 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.04 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.18 | 0.13 | 0.02 |
| other1 | Kanal 1 | 11/11 | 0.57 | 0.23 | 0.04 |
| other2 | Kanal 1 | 11/11 | 0.39 | -0.27 | 0.28 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.04 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.18 | 0.18 | 0.02 |
| other1 | Kanal 2 | 11/11 | 0.45 | 0.01 | 0.04 |
| other2 | Kanal 2 | 11/11 | 0.39 | -0.09 | 0.25 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.05 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.18 | 0.13 | 0.02 |
| other1 | Kanal 3 | 11/11 | 0.30 | -0.12 | 0.21 |
| other2 | Kanal 3 | 11/11 | 0.27 | -0.10 | 0.03 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.06 | 0.04 |
| usb1k | Kanal 4 | 11/11 | 0.17 | 0.23 | 0.02 |
| other1 | Kanal 4 | 11/11 | 0.89 | -0.57 | 0.04 |
| other2 | Kanal 4 | 11/11 | 0.29 | 0.14 | 0.32 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.64 | 0.31 s (3.18 Hz) | 22.8 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 35.3 |
| Kanal 2 | breitbandig | 0.60 | 0.31 s (3.18 Hz) | 22.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 37.4 |
| Kanal 3 | breitbandig | 0.45 | 7.50 s (0.13 Hz) | 25.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 40.2 |
| Kanal 4 | breitbandig | 0.52 | 0.16 s (6.38 Hz) | 22.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 35.6 |

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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx7a-c-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx7a-c-r2_psd.png)

### Kammprofile

![Kammprofile](B9-fx7a-c-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx7a-c-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:32:07. Stream-Meldungen: 0. owl_read: reports/owl_read/B9-fx7a-c-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Kaltstart durch den Nutzer (Case aus, USB ab, Case an, USB an). Oszillator im Case abgesteckt. messlog D79.
