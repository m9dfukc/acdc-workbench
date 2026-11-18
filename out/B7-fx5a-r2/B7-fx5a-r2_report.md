# Report B7-fx5a-r2: B7-fx5a-r2 – acdc1 fx5a-open-inputs-7, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a |
| test | Build-7-Sitzung: fx5a (fx4b + Patch 16), Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx5a-open-inputs-7-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx5a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.1 | -77.1 | -72.4 | -73.2 | -85.4 | -72.8 | -94.6 | -72.4 | 64 % | -76.9 | 4.5 |
| Kanal 2 | -7.5 | -72.3 | -78.7 | -73.4 | -74.1 | -87.8 | -73.7 | -94.8 | -73.4 | 69 % | -78.5 | 5.1 |
| Kanal 3 | -5.7 | -73.7 | -82.3 | -74.3 | -74.9 | -91.8 | -74.5 | -95.7 | -74.4 | 83 % | -82.0 | 7.6 |
| Kanal 4 | -6.5 | -71.6 | -79.0 | -72.5 | -73.1 | -88.3 | -72.8 | -95.1 | -72.5 | 73 % | -78.3 | 5.7 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -82.7 | 9.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.0 | 55.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0005 | 10/10 | k=1: 2320.546 Hz, -113.2 dB | -108.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9492 | 0.0000 | 1/19 | k=1: 49.949 Hz, -98.1 dB | -101.0 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0023 | 10 | k=3·f1+3·f2: 20999.602 Hz, -119.1 dB | -114.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.7 dB | -96.7 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.9 dB | -98.8 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -82.8 | 11.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -75.8 | 57.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0006 | 10/10 | k=9: 20884.904 Hz, -112.5 dB | -107.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9464 | 0.0035 | 3/19 | k=1: 49.949 Hz, -98.6 dB | -101.4 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0023 | 13 | k=1·f1+3·f2: 18999.866 Hz, -120.1 dB | -114.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -98.3 dB | -96.9 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.1 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.4 | 12.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -75.9 | 69.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0004 | 10/10 | k=2: 4641.090 Hz, -113.5 dB | -109.0 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9470 | 0.0018 | 4/19 | k=1: 49.949 Hz, -99.1 dB | -101.8 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0018 | 29 | k=3·f1+3·f2: 20999.603 Hz, -120.9 dB | -112.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.6 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.9 dB | -100.1 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -83.0 | 9.0 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.5 | 64.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.089 Hz, -112.7 dB | -108.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9488 | 0.0000 | 2/19 | k=1: 49.949 Hz, -99.2 dB | -102.1 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0014 | 12 | k=1·f1+3·f2: 18999.867 Hz, -118.0 dB | -113.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -98.6 dB | -97.1 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.4 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 58.2 | usb1k·1 |
| 1999.735 | -81.4 | 51.9 | usb1k·2 |
| 2999.603 | -83.2 | 50.1 | usb1k·3 |
| 6000.000 | -83.8 | 52.5 | fs8·1 |
| 12000.000 | -84.7 | 52.3 | fs8·2 |
| 18000.000 | -85.1 | 53.3 | fs8·3 |
| 3999.471 | -87.2 | 47.6 | usb1k·4 |
| 9998.676 | -88.5 | 46.1 | usb1k·10 |
| 4999.338 | -89.5 | 44.4 | usb1k·5 |
| 15997.881 | -90.5 | 47.4 | usb1k·16 |
| 6999.073 | -90.5 | 46.1 | usb1k·7 |
| 8998.808 | -90.6 | 46.4 | usb1k·9 |
| 16997.749 | -93.6 | 45.0 | usb1k·17 |
| 18997.484 | -94.1 | 43.9 | usb1k·19 |
| 20997.219 | -94.6 | 43.8 | usb1k·21 |
| 5999.206 | -94.4 | 41.9 | usb1k·6 |
| 11998.411 | -96.8 | 40.0 | usb1k·12 |
| 12998.278 | -97.1 | 40.3 | usb1k·13 |
| 2000.000 | -97.7 | 35.6 | other1·1 |
| 7998.941 | -96.5 | 40.6 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 58.9 | usb1k·1 |
| 1999.735 | -82.6 | 52.3 | usb1k·2 |
| 6000.000 | -83.8 | 54.1 | fs8·1 |
| 2999.603 | -83.7 | 51.4 | usb1k·3 |
| 12000.000 | -84.9 | 53.6 | fs8·2 |
| 18000.000 | -85.1 | 54.6 | fs8·3 |
| 3999.471 | -87.5 | 48.7 | usb1k·4 |
| 9998.676 | -88.4 | 48.4 | usb1k·10 |
| 4999.338 | -90.2 | 44.9 | usb1k·5 |
| 15997.881 | -90.8 | 48.8 | usb1k·16 |
| 6999.073 | -91.0 | 46.9 | usb1k·7 |
| 8998.808 | -91.3 | 47.2 | usb1k·9 |
| 16997.749 | -93.7 | 46.1 | usb1k·17 |
| 18997.484 | -94.0 | 45.4 | usb1k·19 |
| 20997.219 | -95.1 | 44.7 | usb1k·21 |
| 5999.206 | -95.4 | 42.5 | usb1k·6 |
| 12998.278 | -97.1 | 41.9 | usb1k·13 |
| 11998.411 | -96.9 | 41.4 | usb1k·12 |
| 17997.616 | -97.8 | 41.8 | usb1k·18 |
| 14998.013 | -97.8 | 41.6 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 63.8 | usb1k·1 |
| 1999.735 | -83.1 | 56.3 | usb1k·2 |
| 2999.603 | -83.9 | 55.6 | usb1k·3 |
| 6000.000 | -84.2 | 57.6 | fs8·1 |
| 18000.000 | -85.5 | 56.4 | fs8·3 |
| 12000.000 | -85.7 | 55.7 | fs8·2 |
| 3999.471 | -87.7 | 52.9 | usb1k·4 |
| 9998.676 | -88.7 | 51.3 | usb1k·10 |
| 15997.881 | -91.1 | 50.9 | usb1k·16 |
| 4999.338 | -91.0 | 49.1 | usb1k·5 |
| 6999.073 | -91.3 | 50.5 | usb1k·7 |
| 8998.808 | -92.0 | 49.9 | usb1k·9 |
| 16997.749 | -93.8 | 48.0 | usb1k·17 |
| 18997.484 | -94.3 | 47.3 | usb1k·19 |
| 20997.219 | -95.6 | 46.4 | usb1k·21 |
| 5999.206 | -96.0 | 45.8 | usb1k·6 |
| 11998.411 | -97.2 | 44.2 | usb1k·12 |
| 7998.941 | -96.7 | 45.1 | usb1k·8 |
| 17997.616 | -98.1 | 43.7 | usb1k·18 |
| 12998.278 | -97.6 | 44.2 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 60.2 | usb1k·1 |
| 1999.735 | -80.7 | 54.1 | usb1k·2 |
| 2999.603 | -82.9 | 51.9 | usb1k·3 |
| 6000.000 | -84.0 | 53.7 | fs8·1 |
| 12000.000 | -85.0 | 53.1 | fs8·2 |
| 18000.000 | -85.3 | 53.4 | fs8·3 |
| 3999.471 | -87.1 | 48.9 | usb1k·4 |
| 4999.338 | -88.8 | 46.1 | usb1k·5 |
| 9998.676 | -88.6 | 47.7 | usb1k·10 |
| 15997.881 | -90.2 | 48.7 | usb1k·16 |
| 6999.073 | -90.3 | 47.3 | usb1k·7 |
| 8998.808 | -90.2 | 47.9 | usb1k·9 |
| 16997.749 | -93.5 | 45.4 | usb1k·17 |
| 5999.206 | -93.0 | 44.7 | usb1k·6 |
| 18997.484 | -94.1 | 44.8 | usb1k·19 |
| 20997.219 | -94.5 | 44.3 | usb1k·21 |
| 7998.941 | -95.2 | 43.1 | usb1k·8 |
| 11998.411 | -96.3 | 41.8 | usb1k·12 |
| 13998.146 | -97.0 | 41.5 | usb1k·14 |
| 12998.278 | -96.9 | 41.3 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.02 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.19 | -0.08 | 0.03 |
| led | Kanal 1 | 11/11 | 1.32 | 0.97 | 0.45 |
| mains50 | Kanal 1 | 11/11 | 202.20 | -527.65 | 1.60 |
| other1 | Kanal 1 | 11/11 | 0.50 | -0.22 | 0.07 |
| other2 | Kanal 1 | 11/11 | 0.13 | 0.09 | 0.15 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.19 | -0.06 | 0.03 |
| led | Kanal 2 | 11/11 | 0.30 | -0.16 | 0.29 |
| mains50 | Kanal 2 | 11/11 | 165.46 | -187.86 | 1.06 |
| other1 | Kanal 2 | 11/11 | 0.53 | -0.34 | 0.06 |
| other2 | Kanal 2 | 11/11 | 0.14 | 0.00 | 0.13 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.16 | -0.12 | 0.03 |
| led | Kanal 3 | 11/11 | 0.81 | 0.48 | 0.24 |
| mains50 | Kanal 3 | 11/11 | 108.13 | -203.20 | 0.74 |
| other1 | Kanal 3 | 11/11 | 0.37 | -0.26 | 0.08 |
| other2 | Kanal 3 | 11/11 | 0.11 | 0.03 | 0.08 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.14 | -0.10 | 0.03 |
| led | Kanal 4 | 11/11 | 1.34 | -1.25 | 0.31 |
| mains50 | Kanal 4 | 11/11 | 171.50 | -443.13 | 1.09 |
| other1 | Kanal 4 | 11/11 | 0.54 | -0.28 | 0.07 |
| other2 | Kanal 4 | 11/11 | 0.18 | 0.03 | 0.16 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.20 | 0.31 s (3.18 Hz) | 26.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 39.0 |
| Kanal 2 | breitbandig | 1.02 | 0.16 s (6.40 Hz) | 26.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 39.6 |
| Kanal 3 | breitbandig | 0.72 | 0.31 s (3.18 Hz) | 29.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 45.0 |
| Kanal 4 | breitbandig | 0.81 | 0.16 s (6.40 Hz) | 27.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 39.2 |

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
| Kanal 2 | 0.96 | 1.00 | 0.92 | 0.96 |
| Kanal 3 | 0.92 | 0.92 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.96 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx5a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx5a-r2_psd.png)

### Kammprofile

![Kammprofile](B7-fx5a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx5a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 15:54:45. Stream-Meldungen: 0. owl_read: out/owl_read/B7-fx5a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
