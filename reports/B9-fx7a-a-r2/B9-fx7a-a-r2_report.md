# Report B9-fx7a-a-r2: B9-fx7a-a-r2 – acdc1 fx7a-open-inputs-9a, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 9 v22.4.r-fx7a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx7a (fx6a + Patch 18, LED-PWM 48 kHz) am Anfang, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx7a-open-inputs-9a-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx7a-a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.9 | -69.7 | -75.4 | -71.0 | -72.0 | -86.3 | -71.3 | -92.2 | -71.0 | 49 % | -74.0 | 3.0 |
| Kanal 2 | -7.3 | -70.8 | -76.3 | -72.3 | -73.2 | -88.4 | -72.6 | -92.5 | -72.3 | 55 % | -75.8 | 3.5 |
| Kanal 3 | -5.5 | -73.3 | -81.6 | -74.0 | -74.9 | -92.8 | -74.3 | -93.0 | -74.1 | 67 % | -78.9 | 4.8 |
| Kanal 4 | -6.4 | -69.9 | -75.9 | -71.1 | -72.1 | -88.2 | -71.4 | -96.0 | -71.2 | 52 % | -74.4 | 3.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -82.9 | 6.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.7 | 42.9 % |
| stärkste übrige Linie (10.50 Hz) | Kanal 1 | 10.4980 | 0.0106 | 11/2273 | k=1: 10.501 Hz, -98.4 dB | -98.6 | 0.2 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 1 | 1000.0001 | 0.0005 | 20/23 | k=1: 1000.001 Hz, -99.9 dB | -93.3 | 0.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.5 dB | -83.1 | 8.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.3 dB | -75.6 | 47.1 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 2 | 1000.0001 | 0.0004 | 20/23 | k=1: 1000.000 Hz, -100.2 dB | -93.4 | 0.8 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 2 | 2500.0002 | 0.0001 | 5/9 | k=1: 2500.000 Hz, -100.6 dB | -99.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -83.6 | 11.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.5 dB | -76.7 | 55.5 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0014 | 6 | k=-1·f1+2·f2: 11000.132 Hz, -120.9 dB | -117.4 | 0.0 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0003 | 20/23 | k=1: 1000.000 Hz, -101.0 dB | -93.9 | 1.0 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 3 | 2500.0003 | 0.0002 | 5/9 | k=1: 2500.000 Hz, -101.2 dB | -100.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.7 dB | -83.3 | 6.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.5 | 46.1 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 4 | 4000.0005 | 0.0004 | 4/5 | k=1: 4000.000 Hz, -100.9 dB | -100.2 | 0.1 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 4 | 2500.0002 | 0.0004 | 8/9 | k=1: 2500.000 Hz, -100.9 dB | -98.0 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 56.5 | usb1k·1 |
| 1999.736 | -81.5 | 49.2 | usb1k·2 |
| 2999.603 | -83.2 | 48.3 | usb1k·3 |
| 6000.000 | -83.4 | 48.6 | fs8·1 |
| 12000.000 | -85.4 | 48.1 | fs8·2 |
| 18000.000 | -85.6 | 47.9 | fs8·3 |
| 3999.471 | -87.0 | 44.6 | usb1k·4 |
| 9998.677 | -88.9 | 44.0 | usb1k·10 |
| 4999.339 | -89.5 | 42.9 | usb1k·5 |
| 15997.883 | -90.8 | 42.5 | usb1k·16 |
| 8998.809 | -91.3 | 41.5 | usb1k·9 |
| 16997.751 | -92.7 | 40.8 | usb1k·17 |
| 6999.074 | -91.6 | 40.8 | usb1k·7 |
| 18997.487 | -93.9 | 39.5 | usb1k·19 |
| 5999.206 | -94.1 | 37.9 | usb1k·6 |
| 20997.222 | -94.4 | 39.1 | usb1k·21 |
| 11998.412 | -96.0 | 37.6 | usb1k·12 |
| 13998.148 | -97.2 | 36.3 | usb1k·14 |
| 12998.280 | -97.1 | 36.2 | usb1k·13 |
| 7998.942 | -96.3 | 36.7 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.3 | 57.2 | usb1k·1 |
| 1999.736 | -82.6 | 50.2 | usb1k·2 |
| 6000.000 | -83.5 | 50.4 | fs8·1 |
| 2999.603 | -83.9 | 49.4 | usb1k·3 |
| 12000.000 | -85.6 | 49.7 | fs8·2 |
| 18000.000 | -85.7 | 49.7 | fs8·3 |
| 3999.471 | -87.3 | 46.3 | usb1k·4 |
| 9998.677 | -88.9 | 45.6 | usb1k·10 |
| 4999.339 | -90.0 | 44.0 | usb1k·5 |
| 15997.883 | -91.1 | 44.2 | usb1k·16 |
| 8998.809 | -91.6 | 43.1 | usb1k·9 |
| 16997.751 | -93.2 | 42.2 | usb1k·17 |
| 6999.074 | -92.2 | 42.0 | usb1k·7 |
| 18997.487 | -93.9 | 41.0 | usb1k·19 |
| 20997.222 | -94.9 | 40.6 | usb1k·21 |
| 5999.206 | -95.3 | 38.7 | usb1k·6 |
| 11998.412 | -96.4 | 39.1 | usb1k·12 |
| 12998.280 | -97.1 | 38.2 | usb1k·13 |
| 17997.619 | -98.2 | 37.2 | usb1k·18 |
| 13998.148 | -98.4 | 36.9 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.5 | 60.1 | usb1k·1 |
| 6000.000 | -84.0 | 52.8 | fs8·1 |
| 1999.736 | -84.0 | 52.2 | usb1k·2 |
| 2999.603 | -84.8 | 51.7 | usb1k·3 |
| 18000.000 | -86.1 | 51.4 | fs8·3 |
| 12000.000 | -86.5 | 51.5 | fs8·2 |
| 3999.471 | -87.9 | 48.8 | usb1k·4 |
| 9998.677 | -89.2 | 48.1 | usb1k·10 |
| 4999.339 | -90.9 | 46.1 | usb1k·5 |
| 15997.883 | -91.7 | 45.8 | usb1k·16 |
| 8998.809 | -92.5 | 45.2 | usb1k·9 |
| 16997.751 | -93.8 | 43.7 | usb1k·17 |
| 6999.074 | -92.9 | 44.2 | usb1k·7 |
| 18997.487 | -94.2 | 43.8 | usb1k·19 |
| 20997.222 | -95.6 | 42.0 | usb1k·21 |
| 11998.412 | -97.0 | 41.0 | usb1k·12 |
| 12998.280 | -97.6 | 40.2 | usb1k·13 |
| 5999.206 | -96.9 | 40.0 | usb1k·6 |
| 17997.619 | -98.4 | 39.0 | usb1k·18 |
| 14998.016 | -99.5 | 37.8 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 57.1 | usb1k·1 |
| 1999.736 | -81.1 | 50.2 | usb1k·2 |
| 2999.603 | -83.3 | 48.5 | usb1k·3 |
| 6000.000 | -83.7 | 48.8 | fs8·1 |
| 12000.000 | -85.8 | 47.3 | fs8·2 |
| 18000.000 | -85.9 | 47.8 | fs8·3 |
| 3999.471 | -87.1 | 45.0 | usb1k·4 |
| 4999.339 | -89.0 | 43.2 | usb1k·5 |
| 9998.677 | -89.1 | 44.0 | usb1k·10 |
| 15997.883 | -90.7 | 42.9 | usb1k·16 |
| 8998.809 | -90.8 | 42.3 | usb1k·9 |
| 16997.751 | -92.9 | 40.9 | usb1k·17 |
| 6999.074 | -91.8 | 41.0 | usb1k·7 |
| 5999.206 | -93.1 | 39.4 | usb1k·6 |
| 18997.487 | -94.1 | 39.4 | usb1k·19 |
| 20997.222 | -94.5 | 39.3 | usb1k·21 |
| 11998.412 | -95.8 | 37.4 | usb1k·12 |
| 12998.280 | -97.0 | 36.5 | usb1k·13 |
| 13998.148 | -97.1 | 36.6 | usb1k·14 |
| 7998.942 | -95.8 | 37.2 | usb1k·8 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.04 | -0.01 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.25 | 0.05 | 0.03 |
| other1 | Kanal 1 | 11/11 | 1286.64 | -3796.36 | 1.77 |
| other2 | Kanal 1 | 11/11 | 8.95 | 3.60 | 0.03 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.00 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.25 | -0.01 | 0.04 |
| other1 | Kanal 2 | 11/11 | 7.03 | 3.94 | 0.05 |
| other2 | Kanal 2 | 11/11 | 0.48 | -0.02 | 0.21 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.00 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.24 | 0.05 | 0.04 |
| other1 | Kanal 3 | 11/11 | 5.53 | 2.31 | 0.04 |
| other2 | Kanal 3 | 11/11 | 0.33 | -0.33 | 0.17 |
| fs8 | Kanal 4 | 11/11 | 0.04 | 0.02 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.26 | -0.02 | 0.04 |
| other1 | Kanal 4 | 11/11 | 0.33 | -0.35 | 0.24 |
| other2 | Kanal 4 | 11/11 | 0.81 | 0.81 | 0.22 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.22 | 0.16 s (6.40 Hz) | 28.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 36.2 |
| Kanal 2 | breitbandig | 1.28 | 0.16 s (6.40 Hz) | 30.1 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 38.1 |
| Kanal 3 | breitbandig | 0.77 | 0.16 s (6.40 Hz) | 26.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 41.0 |
| Kanal 4 | breitbandig | 1.15 | 0.16 s (6.40 Hz) | 30.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 36.2 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.93 | 0.97 |
| Kanal 3 | 0.94 | 0.93 | 1.00 | 0.91 |
| Kanal 4 | 0.95 | 0.97 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx7a-a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx7a-a-r2_psd.png)

### Kammprofile

![Kammprofile](B9-fx7a-a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx7a-a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:07:06. Stream-Meldungen: 0. owl_read: reports/owl_read/B9-fx7a-a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Oszillator im Case abgesteckt (Nutzer). messlog D79.
