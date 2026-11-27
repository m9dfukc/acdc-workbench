# Report B7-fx4b-b-r1: B7-fx4b-b-r1 – acdc1 fx4b-open-inputs-7b, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-7-Sitzung: fx4b-Kontrolle am Ende, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx4b-open-inputs-7b-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx4b-b-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.3 | -74.3 | -72.6 | -73.4 | -85.6 | -72.9 | -94.5 | -72.6 | 64 % | -77.0 | 4.4 |
| Kanal 2 | -7.4 | -71.5 | -75.7 | -73.5 | -74.3 | -87.5 | -73.8 | -94.8 | -73.6 | 68 % | -78.5 | 4.9 |
| Kanal 3 | -5.6 | -72.8 | -77.3 | -74.7 | -75.3 | -92.1 | -74.9 | -95.7 | -74.7 | 81 % | -82.0 | 7.3 |
| Kanal 4 | -6.4 | -71.5 | -78.0 | -72.6 | -73.2 | -87.7 | -72.8 | -95.1 | -72.6 | 71 % | -78.0 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.5 | 8.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.9 dB | -75.2 | 55.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0008 | 10/10 | k=1: 2320.544 Hz, -112.4 dB | -108.4 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9853 | 0.0000 | 1/19 | k=1: 49.985 Hz, -100.1 dB | -101.8 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0020 | 4 | k=8·f1+2·f2: 19998.940 Hz, -121.1 dB | -119.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.0 dB | -96.5 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.0 dB | -98.9 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0003 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.6 | 9.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.0 | 57.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.544 Hz, -112.8 dB | -107.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9766 | 0.0059 | 3/19 | k=1: 49.986 Hz, -100.1 dB | -101.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0029 | 10 | k=-1·f1+1·f2: 5000.127 Hz, -119.2 dB | -115.5 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.3 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.6 dB | -96.8 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -85.1 dB | -84.2 | 11.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.3 | 69.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.544 Hz, -113.2 dB | -109.3 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9855 | 0.0075 | 4/19 | k=1: 49.986 Hz, -100.9 dB | -102.3 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0024 | 15 | k=8·f1+2·f2: 19998.941 Hz, -122.6 dB | -116.3 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.8 dB | -100.2 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -100.1 dB | -97.7 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0003 | 3/3 | k=2: 12000.000 Hz, -84.6 dB | -83.7 | 7.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.6 | 63.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -112.1 dB | -108.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9821 | 0.0064 | 2/19 | k=1: 49.987 Hz, -100.3 dB | -101.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0035 | 10 | k=-1·f1+1·f2: 5000.128 Hz, -116.0 dB | -112.8 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0005 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.6 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.0 dB | -97.1 | 0.4 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.9 | 57.4 | usb1k·1 |
| 1999.735 | -81.6 | 50.9 | usb1k·2 |
| 2999.603 | -83.2 | 51.0 | usb1k·3 |
| 12000.000 | -84.2 | 53.9 | fs8·2 |
| 6000.000 | -84.9 | 51.4 | fs8·1 |
| 18000.000 | -87.4 | 51.2 | fs8·3 |
| 3999.471 | -87.9 | 46.9 | usb1k·4 |
| 9998.676 | -88.9 | 48.7 | usb1k·10 |
| 15997.882 | -90.9 | 47.5 | usb1k·16 |
| 4999.338 | -90.8 | 44.4 | usb1k·5 |
| 6999.074 | -91.4 | 45.0 | usb1k·7 |
| 8998.808 | -91.3 | 46.1 | usb1k·9 |
| 16997.749 | -93.7 | 44.6 | usb1k·17 |
| 18997.485 | -94.1 | 44.2 | usb1k·19 |
| 20997.220 | -94.6 | 43.4 | usb1k·21 |
| 5999.206 | -95.7 | 40.6 | usb1k·6 |
| 11998.411 | -96.7 | 41.3 | usb1k·12 |
| 13998.146 | -97.2 | 41.2 | usb1k·14 |
| 7998.941 | -96.3 | 41.2 | usb1k·8 |
| 12998.278 | -97.1 | 41.9 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 58.0 | usb1k·1 |
| 1999.735 | -82.7 | 51.4 | usb1k·2 |
| 2999.603 | -83.7 | 51.7 | usb1k·3 |
| 12000.000 | -84.4 | 54.9 | fs8·2 |
| 6000.000 | -84.9 | 52.9 | fs8·1 |
| 18000.000 | -87.3 | 52.0 | fs8·3 |
| 3999.471 | -88.2 | 48.2 | usb1k·4 |
| 9998.676 | -88.9 | 49.5 | usb1k·10 |
| 15997.882 | -91.2 | 48.3 | usb1k·16 |
| 4999.338 | -91.6 | 45.2 | usb1k·5 |
| 6999.074 | -91.8 | 46.2 | usb1k·7 |
| 8998.808 | -91.9 | 46.9 | usb1k·9 |
| 16997.749 | -94.0 | 45.6 | usb1k·17 |
| 18997.485 | -94.1 | 45.1 | usb1k·19 |
| 20997.220 | -94.9 | 44.3 | usb1k·21 |
| 11998.411 | -97.0 | 42.2 | usb1k·12 |
| 12998.278 | -97.2 | 42.4 | usb1k·13 |
| 5999.206 | -97.3 | 40.5 | usb1k·6 |
| 14998.014 | -98.0 | 41.1 | usb1k·15 |
| 17997.617 | -98.2 | 41.3 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 62.6 | usb1k·1 |
| 1999.735 | -83.6 | 55.4 | usb1k·2 |
| 2999.603 | -84.0 | 56.1 | usb1k·3 |
| 12000.000 | -85.1 | 57.3 | fs8·2 |
| 6000.000 | -85.4 | 56.2 | fs8·1 |
| 18000.000 | -87.8 | 54.3 | fs8·3 |
| 3999.471 | -88.5 | 52.2 | usb1k·4 |
| 9998.676 | -89.2 | 53.0 | usb1k·10 |
| 15997.882 | -91.5 | 50.6 | usb1k·16 |
| 4999.338 | -92.1 | 49.0 | usb1k·5 |
| 6999.074 | -92.3 | 49.3 | usb1k·7 |
| 16997.749 | -94.0 | 48.3 | usb1k·17 |
| 18997.485 | -94.3 | 47.4 | usb1k·19 |
| 8998.808 | -92.7 | 49.5 | usb1k·9 |
| 20997.220 | -95.7 | 45.8 | usb1k·21 |
| 11998.411 | -96.9 | 45.5 | usb1k·12 |
| 7998.941 | -96.6 | 45.8 | usb1k·8 |
| 5999.206 | -97.4 | 44.3 | usb1k·6 |
| 12998.279 | -97.7 | 44.7 | usb1k·13 |
| 17997.617 | -98.6 | 43.5 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 59.4 | usb1k·1 |
| 1999.735 | -80.5 | 53.2 | usb1k·2 |
| 2999.603 | -83.0 | 52.3 | usb1k·3 |
| 12000.000 | -84.6 | 53.9 | fs8·2 |
| 6000.000 | -85.0 | 52.0 | fs8·1 |
| 18000.000 | -87.4 | 51.2 | fs8·3 |
| 3999.470 | -87.6 | 48.3 | usb1k·4 |
| 9998.676 | -89.2 | 48.7 | usb1k·10 |
| 4999.338 | -90.0 | 46.3 | usb1k·5 |
| 15997.882 | -90.6 | 47.9 | usb1k·16 |
| 6999.074 | -91.0 | 46.7 | usb1k·7 |
| 8998.808 | -90.7 | 47.2 | usb1k·9 |
| 16997.750 | -93.9 | 44.6 | usb1k·17 |
| 20997.220 | -94.2 | 44.3 | usb1k·21 |
| 18997.485 | -94.5 | 44.5 | usb1k·19 |
| 5999.206 | -94.7 | 42.3 | usb1k·6 |
| 13998.146 | -96.4 | 42.0 | usb1k·14 |
| 7998.941 | -95.2 | 42.7 | usb1k·8 |
| 11998.411 | -96.3 | 42.3 | usb1k·12 |
| 12998.278 | -97.2 | 41.6 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.01 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.18 | -0.28 | 0.12 |
| led | Kanal 1 | 11/11 | 1.03 | -0.51 | 0.55 |
| mains50 | Kanal 1 | 11/11 | 315.38 | 661.96 | 1.38 |
| other1 | Kanal 1 | 11/11 | 1.72 | -1.44 | 0.09 |
| other2 | Kanal 1 | 11/11 | 0.25 | -0.04 | 0.18 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.00 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.18 | -0.25 | 0.14 |
| led | Kanal 2 | 11/11 | 0.40 | -0.13 | 0.40 |
| mains50 | Kanal 2 | 11/11 | 785.90 | 1623.31 | 1.15 |
| other1 | Kanal 2 | 11/11 | 0.27 | 0.18 | 0.16 |
| other2 | Kanal 2 | 11/11 | 1.93 | 0.07 | 0.06 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.19 | -0.17 | 0.05 |
| led | Kanal 3 | 11/11 | 0.49 | 0.33 | 0.23 |
| mains50 | Kanal 3 | 11/11 | 282.96 | 964.51 | 0.49 |
| other1 | Kanal 3 | 11/11 | 0.26 | 0.07 | 0.13 |
| other2 | Kanal 3 | 11/11 | 0.17 | 0.13 | 0.10 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.16 | -0.25 | 0.15 |
| led | Kanal 4 | 11/11 | 0.86 | -0.00 | 0.50 |
| mains50 | Kanal 4 | 11/11 | 1071.94 | 2640.56 | 1.17 |
| other1 | Kanal 4 | 11/11 | 0.27 | -0.02 | 0.17 |
| other2 | Kanal 4 | 11/11 | 2.13 | -1.38 | 0.07 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.84 | 0.31 s (3.18 Hz) | 27.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 37.5 |
| Kanal 2 | breitbandig | 1.72 | 0.31 s (3.18 Hz) | 29.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 38.7 |
| Kanal 3 | breitbandig | 1.52 | 0.31 s (3.18 Hz) | 28.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.2 |
| Kanal 4 | breitbandig | 1.15 | 0.31 s (3.18 Hz) | 28.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 37.9 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.93 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.95 |
| Kanal 3 | 0.94 | 0.94 | 1.00 | 0.91 |
| Kanal 4 | 0.93 | 0.95 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx4b-b-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx4b-b-r1_psd.png)

### Kammprofile

![Kammprofile](B7-fx4b-b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx4b-b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:07:19. Stream-Meldungen: 0. owl_read: reports/owl_read/B7-fx4b-b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
