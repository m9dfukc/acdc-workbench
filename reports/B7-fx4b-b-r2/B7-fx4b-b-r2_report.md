# Report B7-fx4b-b-r2: B7-fx4b-b-r2 – acdc1 fx4b-open-inputs-7b, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-7-Sitzung: fx4b-Kontrolle am Ende, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx4b-open-inputs-7b-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx4b-b-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.7 | -79.0 | -72.6 | -73.4 | -85.9 | -73.0 | -94.7 | -72.7 | 64 % | -77.1 | 4.4 |
| Kanal 2 | -7.5 | -72.8 | -80.8 | -73.6 | -74.4 | -87.9 | -73.9 | -94.9 | -73.6 | 67 % | -78.5 | 4.9 |
| Kanal 3 | -5.7 | -74.2 | -83.9 | -74.7 | -75.3 | -92.5 | -74.9 | -95.8 | -74.7 | 82 % | -82.2 | 7.4 |
| Kanal 4 | -6.5 | -72.2 | -81.7 | -72.7 | -73.3 | -88.1 | -73.0 | -95.2 | -72.7 | 71 % | -78.1 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.3 dB | -83.4 | 8.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -75.3 | 55.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.546 Hz, -113.0 dB | -108.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9910 | 0.0006 | 2/19 | k=1: 49.992 Hz, -98.8 dB | -102.1 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0012 | 3 | k=-3·f1+4·f2: 21000.397 Hz, -121.5 dB | -120.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.7 dB | -96.6 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -99.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.5 dB | -83.5 | 10.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.1 | 56.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=8: 18564.359 Hz, -112.5 dB | -107.5 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9912 | 0.0015 | 4/19 | k=1: 49.992 Hz, -99.0 dB | -102.0 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0020 | 10 | k=1·f1+1·f2: 6999.873 Hz, -120.9 dB | -115.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.3 dB | -96.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -85.2 dB | -84.0 | 11.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.3 | 70.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -114.1 dB | -109.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9911 | 0.0087 | 7/19 | k=1: 49.991 Hz, -99.7 dB | -102.1 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0033 | 17 | k=-3·f1+4·f2: 21000.400 Hz, -122.1 dB | -116.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.9 dB | -97.7 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.1 dB | -100.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.6 dB | -83.6 | 8.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.7 | 62.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0010 | 10/10 | k=1: 2320.546 Hz, -112.5 dB | -108.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9913 | 0.0012 | 3/19 | k=1: 49.991 Hz, -99.3 dB | -102.3 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0032 | 9 | k=1·f1+1·f2: 6999.873 Hz, -117.9 dB | -114.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.6 dB | -97.1 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.7 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 57.6 | usb1k·1 |
| 1999.735 | -81.8 | 50.4 | usb1k·2 |
| 2999.603 | -83.5 | 51.4 | usb1k·3 |
| 12000.000 | -84.3 | 54.3 | fs8·2 |
| 6000.000 | -84.8 | 51.5 | fs8·1 |
| 18000.000 | -86.7 | 51.7 | fs8·3 |
| 3999.470 | -87.6 | 45.2 | usb1k·4 |
| 9998.676 | -88.8 | 48.6 | usb1k·10 |
| 4999.338 | -90.1 | 44.8 | usb1k·5 |
| 15997.881 | -90.8 | 47.2 | usb1k·16 |
| 6999.073 | -91.2 | 45.3 | usb1k·7 |
| 8998.808 | -91.2 | 46.2 | usb1k·9 |
| 16997.748 | -93.8 | 44.8 | usb1k·17 |
| 18997.484 | -94.1 | 44.2 | usb1k·19 |
| 20997.219 | -94.6 | 43.7 | usb1k·21 |
| 5999.205 | -94.9 | 41.3 | usb1k·6 |
| 12998.278 | -97.0 | 41.0 | usb1k·13 |
| 11998.410 | -96.8 | 41.7 | usb1k·12 |
| 2000.000 | -97.7 | 34.5 | other1·1 |
| 7998.941 | -96.5 | 39.7 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 58.0 | usb1k·1 |
| 1999.735 | -82.9 | 50.8 | usb1k·2 |
| 2999.603 | -84.1 | 51.9 | usb1k·3 |
| 12000.000 | -84.5 | 54.9 | fs8·2 |
| 6000.000 | -84.9 | 52.8 | fs8·1 |
| 18000.000 | -86.6 | 53.1 | fs8·3 |
| 3999.470 | -87.8 | 47.0 | usb1k·4 |
| 9998.676 | -88.8 | 50.2 | usb1k·10 |
| 15997.881 | -91.1 | 48.4 | usb1k·16 |
| 4999.338 | -90.8 | 45.8 | usb1k·5 |
| 6999.073 | -91.6 | 45.8 | usb1k·7 |
| 8998.808 | -91.8 | 46.8 | usb1k·9 |
| 18997.484 | -94.0 | 45.1 | usb1k·19 |
| 16997.748 | -94.0 | 45.4 | usb1k·17 |
| 20997.219 | -95.1 | 44.4 | usb1k·21 |
| 5999.206 | -96.5 | 41.1 | usb1k·6 |
| 12998.278 | -97.2 | 42.0 | usb1k·13 |
| 11998.410 | -97.1 | 42.2 | usb1k·12 |
| 17997.616 | -98.2 | 41.5 | usb1k·18 |
| 2000.000 | -98.3 | 35.4 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 63.3 | usb1k·1 |
| 1999.735 | -83.7 | 55.2 | usb1k·2 |
| 2999.603 | -84.2 | 56.5 | usb1k·3 |
| 6000.000 | -85.2 | 56.2 | fs8·1 |
| 12000.000 | -85.3 | 56.8 | fs8·2 |
| 18000.000 | -87.1 | 54.8 | fs8·3 |
| 3999.470 | -88.1 | 50.9 | usb1k·4 |
| 9998.675 | -89.0 | 53.2 | usb1k·10 |
| 15997.881 | -91.4 | 50.8 | usb1k·16 |
| 4999.338 | -91.5 | 49.4 | usb1k·5 |
| 6999.073 | -92.1 | 49.6 | usb1k·7 |
| 16997.748 | -94.1 | 48.0 | usb1k·17 |
| 8998.808 | -92.7 | 49.6 | usb1k·9 |
| 18997.484 | -94.3 | 47.5 | usb1k·19 |
| 20997.219 | -95.7 | 46.4 | usb1k·21 |
| 5999.206 | -96.7 | 44.7 | usb1k·6 |
| 7998.941 | -96.7 | 44.9 | usb1k·8 |
| 11998.410 | -97.2 | 44.9 | usb1k·12 |
| 12998.278 | -97.7 | 44.9 | usb1k·13 |
| 17997.616 | -98.7 | 43.0 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 59.4 | usb1k·1 |
| 1999.735 | -80.7 | 52.5 | usb1k·2 |
| 2999.603 | -83.2 | 52.6 | usb1k·3 |
| 12000.000 | -84.6 | 53.7 | fs8·2 |
| 6000.000 | -85.1 | 52.5 | fs8·1 |
| 18000.000 | -86.8 | 52.3 | fs8·3 |
| 3999.470 | -87.5 | 47.2 | usb1k·4 |
| 4999.338 | -89.3 | 47.2 | usb1k·5 |
| 9998.675 | -89.0 | 49.3 | usb1k·10 |
| 15997.881 | -90.5 | 48.2 | usb1k·16 |
| 6999.073 | -90.7 | 45.9 | usb1k·7 |
| 8998.808 | -90.7 | 47.2 | usb1k·9 |
| 16997.748 | -93.8 | 45.0 | usb1k·17 |
| 18997.484 | -94.2 | 44.5 | usb1k·19 |
| 20997.219 | -94.4 | 44.1 | usb1k·21 |
| 5999.205 | -94.0 | 43.6 | usb1k·6 |
| 7998.941 | -95.4 | 42.2 | usb1k·8 |
| 11998.410 | -96.1 | 42.1 | usb1k·12 |
| 13998.146 | -96.7 | 41.6 | usb1k·14 |
| 12998.278 | -97.2 | 41.2 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | 0.02 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.27 | -0.14 | 0.03 |
| led | Kanal 1 | 11/11 | 0.64 | 0.49 | 0.39 |
| mains50 | Kanal 1 | 11/11 | 120.71 | 5.70 | 1.29 |
| other1 | Kanal 1 | 11/11 | 2.22 | -3.82 | 0.06 |
| other2 | Kanal 1 | 11/11 | 0.17 | -0.05 | 0.18 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.02 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.28 | -0.17 | 0.03 |
| led | Kanal 2 | 11/11 | 0.17 | -0.15 | 0.31 |
| mains50 | Kanal 2 | 11/11 | 149.01 | -93.58 | 0.94 |
| other1 | Kanal 2 | 11/11 | 2.10 | -4.61 | 0.07 |
| other2 | Kanal 2 | 11/11 | 0.15 | 0.02 | 0.15 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.06 |
| usb1k | Kanal 3 | 11/11 | 0.22 | -0.17 | 0.02 |
| led | Kanal 3 | 11/11 | 0.77 | 1.30 | 0.25 |
| mains50 | Kanal 3 | 11/11 | 49.08 | -109.68 | 0.26 |
| other1 | Kanal 3 | 11/11 | 0.15 | 0.12 | 0.04 |
| other2 | Kanal 3 | 11/11 | 0.13 | 0.05 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.03 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.25 | -0.21 | 0.02 |
| led | Kanal 4 | 11/11 | 0.95 | 1.21 | 0.37 |
| mains50 | Kanal 4 | 11/11 | 154.79 | 191.51 | 0.84 |
| other1 | Kanal 4 | 11/11 | 1.92 | -1.84 | 0.07 |
| other2 | Kanal 4 | 11/11 | 0.22 | -0.14 | 0.14 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.00 | 0.31 s (3.22 Hz) | 20.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 37.2 |
| Kanal 2 | breitbandig | 0.88 | 0.31 s (3.22 Hz) | 21.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 38.1 |
| Kanal 3 | breitbandig | 0.59 | 0.31 s (3.22 Hz) | 22.6 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 43.6 |
| Kanal 4 | breitbandig | 0.67 | 0.31 s (3.22 Hz) | 19.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.89 | 7.50 s (0.13 Hz) | 37.1 |

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
| Kanal 1 | 1.00 | 0.96 | 0.92 | 0.94 |
| Kanal 2 | 0.96 | 1.00 | 0.93 | 0.95 |
| Kanal 3 | 0.92 | 0.93 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.95 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx4b-b-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx4b-b-r2_psd.png)

### Kammprofile

![Kammprofile](B7-fx4b-b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx4b-b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:08:33. Stream-Meldungen: 0. owl_read: reports/owl_read/B7-fx4b-b-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
