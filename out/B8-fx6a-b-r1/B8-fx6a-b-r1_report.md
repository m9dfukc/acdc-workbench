# Report B8-fx6a-b-r1: B8-fx6a-b-r1 – acdc1 fx6a-open-inputs-8b, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 8 v22.4.r-fx6a, LED-Modus normal, ins Case geschraubt |
| test | Build-8-Sitzung: fx6a (fx5a + Patch 17) am Ende, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten, Oszillator im Case vom Strom getrennt |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx6a-open-inputs-8b-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B8-fx6a-b-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -67.8 | -71.9 | -70.0 | -70.6 | -85.6 | -70.3 | -94.6 | -70.0 | 60 % | -74.0 | 4.0 |
| Kanal 2 | -7.0 | -69.3 | -74.0 | -71.1 | -71.7 | -87.8 | -71.3 | -94.8 | -71.1 | 67 % | -75.9 | 4.8 |
| Kanal 3 | -5.3 | -71.6 | -76.6 | -73.3 | -73.9 | -92.1 | -73.5 | -95.6 | -73.4 | 72 % | -78.9 | 5.6 |
| Kanal 4 | -6.1 | -68.7 | -74.6 | -70.0 | -70.5 | -87.7 | -70.2 | -95.0 | -70.0 | 65 % | -74.5 | 4.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.1 dB | -82.9 | 5.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8673 | 0.0003 | 23/23 | k=1: 999.867 Hz, -71.2 dB | -72.6 | 55.2 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8673 | 0.0028 | 1 | k=3·f1+2·f2: 14999.599 Hz, -119.5 dB | -122.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.001 Hz, -97.9 dB | -96.7 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -97.9 dB | -98.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.1 dB | -83.0 | 6.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8673 | 0.0002 | 23/23 | k=1: 999.867 Hz, -72.0 dB | -73.3 | 60.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5449 | 0.0014 | 10/10 | k=9: 20884.905 Hz, -113.8 dB | -109.9 | 0.0 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8673 | 0.0019 | 2 | k=3·f1+2·f2: 14999.600 Hz, -120.5 dB | -121.4 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -98.9 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.001 Hz, -98.4 dB | -96.9 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.8 dB | -83.6 | 9.4 % |
| 1-kHz-Kamm | Kanal 3 | 999.8673 | 0.0003 | 23/23 | k=1: 999.867 Hz, -74.2 dB | -75.4 | 62.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5449 | 0.0013 | 10/10 | k=2: 4641.089 Hz, -116.9 dB | -111.9 | 0.0 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8673 | 0.0009 | 6 | k=3·f1+2·f2: 14999.601 Hz, -121.5 dB | -118.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.6 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.9 dB | -99.9 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.2 | 4.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8673 | 0.0003 | 23/23 | k=1: 999.867 Hz, -70.8 dB | -72.2 | 59.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5450 | 0.0023 | 10/10 | k=2: 4641.088 Hz, -115.8 dB | -111.1 | 0.0 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8673 | 0.0105 | 2 | k=26·f1-4·f2: 1996.538 Hz, -114.8 dB | -116.1 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.1 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.001 Hz, -98.9 dB | -97.2 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -71.2 | 57.2 | usb1k·1 |
| 1999.735 | -78.1 | 51.4 | usb1k·2 |
| 2999.602 | -81.8 | 48.5 | usb1k·3 |
| 6000.000 | -84.1 | 47.6 | fs8·1 |
| 12000.000 | -84.6 | 49.0 | fs8·2 |
| 18000.000 | -85.3 | 50.2 | fs8·3 |
| 3999.470 | -86.3 | 44.9 | usb1k·4 |
| 4999.337 | -87.1 | 44.3 | usb1k·5 |
| 15997.877 | -88.9 | 45.8 | usb1k·16 |
| 9998.674 | -88.8 | 44.4 | usb1k·10 |
| 8998.806 | -89.5 | 43.0 | usb1k·9 |
| 6999.071 | -91.1 | 40.8 | usb1k·7 |
| 16997.744 | -91.2 | 44.3 | usb1k·17 |
| 5999.204 | -91.7 | 40.0 | usb1k·6 |
| 18997.479 | -92.3 | 43.3 | usb1k·19 |
| 7998.939 | -92.8 | 39.5 | usb1k·8 |
| 20997.214 | -94.0 | 41.3 | usb1k·21 |
| 11998.408 | -92.6 | 41.0 | usb1k·12 |
| 12998.275 | -94.9 | 39.0 | usb1k·13 |
| 13998.143 | -96.3 | 37.6 | usb1k·14 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.0 | 58.5 | usb1k·1 |
| 1999.735 | -79.2 | 52.3 | usb1k·2 |
| 2999.602 | -82.4 | 49.8 | usb1k·3 |
| 6000.000 | -84.1 | 49.2 | fs8·1 |
| 12000.000 | -84.9 | 50.9 | fs8·2 |
| 18000.000 | -85.4 | 51.5 | fs8·3 |
| 3999.470 | -86.7 | 46.5 | usb1k·4 |
| 4999.337 | -87.9 | 45.7 | usb1k·5 |
| 9998.673 | -88.9 | 46.4 | usb1k·10 |
| 15997.877 | -89.4 | 47.2 | usb1k·16 |
| 8998.806 | -90.0 | 44.6 | usb1k·9 |
| 6999.071 | -91.9 | 42.0 | usb1k·7 |
| 16997.744 | -91.6 | 45.1 | usb1k·17 |
| 5999.204 | -92.4 | 40.9 | usb1k·6 |
| 18997.479 | -92.5 | 44.7 | usb1k·19 |
| 7998.939 | -93.5 | 40.7 | usb1k·8 |
| 20997.214 | -94.7 | 42.3 | usb1k·21 |
| 11998.408 | -93.3 | 42.5 | usb1k·12 |
| 12998.275 | -95.2 | 40.4 | usb1k·13 |
| 3000.000 | -98.4 | 33.8 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.2 | 59.9 | usb1k·1 |
| 1999.735 | -81.3 | 53.7 | usb1k·2 |
| 2999.602 | -84.2 | 51.2 | usb1k·3 |
| 6000.000 | -84.8 | 51.7 | fs8·1 |
| 12000.000 | -85.7 | 52.3 | fs8·2 |
| 18000.000 | -85.7 | 53.7 | fs8·3 |
| 3999.470 | -87.8 | 48.5 | usb1k·4 |
| 4999.337 | -89.8 | 46.7 | usb1k·5 |
| 9998.674 | -89.5 | 48.6 | usb1k·10 |
| 15997.877 | -90.5 | 48.1 | usb1k·16 |
| 8998.807 | -91.2 | 46.2 | usb1k·9 |
| 18997.479 | -93.1 | 46.5 | usb1k·19 |
| 16997.744 | -92.8 | 46.1 | usb1k·17 |
| 6999.071 | -93.1 | 43.7 | usb1k·7 |
| 5999.204 | -95.5 | 41.0 | usb1k·6 |
| 20997.214 | -96.0 | 43.2 | usb1k·21 |
| 11998.408 | -94.5 | 43.5 | usb1k·12 |
| 7998.939 | -95.7 | 41.0 | usb1k·8 |
| 12998.275 | -96.4 | 41.8 | usb1k·13 |
| 17997.612 | -99.3 | 40.1 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -70.8 | 58.3 | usb1k·1 |
| 1999.735 | -77.9 | 52.6 | usb1k·2 |
| 2999.602 | -81.8 | 48.8 | usb1k·3 |
| 6000.000 | -84.2 | 47.7 | fs8·1 |
| 12000.000 | -85.1 | 48.6 | fs8·2 |
| 18000.000 | -85.8 | 49.5 | fs8·3 |
| 3999.470 | -86.4 | 45.3 | usb1k·4 |
| 4999.337 | -86.7 | 45.0 | usb1k·5 |
| 15997.877 | -89.0 | 46.0 | usb1k·16 |
| 9998.673 | -88.9 | 44.7 | usb1k·10 |
| 8998.806 | -89.3 | 43.8 | usb1k·9 |
| 5999.204 | -90.5 | 41.3 | usb1k·6 |
| 16997.744 | -91.2 | 44.0 | usb1k·17 |
| 6999.071 | -91.7 | 40.8 | usb1k·7 |
| 7998.939 | -92.2 | 40.1 | usb1k·8 |
| 18997.479 | -92.6 | 42.6 | usb1k·19 |
| 20997.214 | -94.1 | 41.5 | usb1k·21 |
| 11998.408 | -92.7 | 41.1 | usb1k·12 |
| 12998.275 | -94.3 | 39.9 | usb1k·13 |
| 13998.143 | -96.7 | 37.7 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.01 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.26 | 0.18 | 0.04 |
| other1 | Kanal 1 | 11/11 | 1.05 | -2.20 | 0.13 |
| other2 | Kanal 1 | 11/11 | 0.19 | -0.23 | 0.29 |
| fs8 | Kanal 2 | 11/11 | 0.03 | -0.01 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.23 | 0.27 | 0.04 |
| led | Kanal 2 | 11/11 | 0.50 | 0.58 | 0.96 |
| other1 | Kanal 2 | 11/11 | 0.18 | -0.15 | 0.22 |
| other2 | Kanal 2 | 11/11 | 0.51 | 0.64 | 0.15 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.05 |
| usb1k | Kanal 3 | 11/11 | 0.24 | 0.23 | 0.03 |
| led | Kanal 3 | 11/11 | 1.17 | -0.71 | 0.80 |
| other1 | Kanal 3 | 11/11 | 0.43 | 0.36 | 0.09 |
| other2 | Kanal 3 | 11/11 | 0.12 | 0.01 | 0.17 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.02 | 0.04 |
| usb1k | Kanal 4 | 11/11 | 0.22 | 0.26 | 0.05 |
| led | Kanal 4 | 11/11 | 1.32 | -3.09 | 1.31 |
| other1 | Kanal 4 | 11/11 | 0.26 | -0.17 | 0.30 |
| other2 | Kanal 4 | 11/11 | 0.54 | 0.83 | 0.22 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.74 | 0.31 s (3.18 Hz) | 32.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 34.5 |
| Kanal 2 | breitbandig | 1.54 | 0.31 s (3.18 Hz) | 32.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 36.6 |
| Kanal 3 | breitbandig | 1.39 | 0.31 s (3.18 Hz) | 33.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 40.4 |
| Kanal 4 | breitbandig | 1.19 | 0.31 s (3.18 Hz) | 31.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 34.7 |

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
| Kanal 3 | 0.96 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.97 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B8-fx6a-b-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B8-fx6a-b-r1_psd.png)

### Kammprofile

![Kammprofile](B8-fx6a-b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B8-fx6a-b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:19:46. Stream-Meldungen: 0. owl_read: out/owl_read/B8-fx6a-b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
