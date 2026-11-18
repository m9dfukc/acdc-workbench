# Report B7-fx5a-r1: B7-fx5a-r1 – acdc1 fx5a-open-inputs-7, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a |
| test | Build-7-Sitzung: fx5a (fx4b + Patch 16), Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx5a-open-inputs-7-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx5a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.0 | -76.3 | -72.5 | -73.3 | -85.6 | -72.8 | -94.6 | -72.5 | 65 % | -77.1 | 4.6 |
| Kanal 2 | -7.5 | -71.9 | -77.2 | -73.4 | -74.2 | -87.8 | -73.7 | -94.8 | -73.4 | 69 % | -78.5 | 5.1 |
| Kanal 3 | -5.7 | -73.8 | -82.7 | -74.4 | -75.0 | -92.1 | -74.6 | -95.7 | -74.4 | 83 % | -82.1 | 7.6 |
| Kanal 4 | -6.5 | -71.3 | -77.4 | -72.6 | -73.2 | -88.1 | -72.8 | -95.1 | -72.6 | 72 % | -78.1 | 5.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -82.7 | 9.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.9 dB | -75.1 | 55.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0008 | 10/10 | k=1: 2320.543 Hz, -112.1 dB | -108.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9726 | 0.0005 | 3/19 | k=1: 49.973 Hz, -97.5 dB | -100.7 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0010 | 7 | k=3·f1+3·f2: 20999.602 Hz, -120.6 dB | -116.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -96.6 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0002 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.2 dB | -98.9 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -82.8 | 11.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -75.9 | 56.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.543 Hz, -112.9 dB | -107.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9726 | 0.0024 | 4/19 | k=1: 49.973 Hz, -97.8 dB | -100.9 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0046 | 18 | k=26·f1-4·f2: 1996.542 Hz, -117.3 dB | -113.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.2 dB | -96.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.7 dB | -99.2 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -83.3 | 12.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -76.0 | 69.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0005 | 10/10 | k=1: 2320.544 Hz, -113.4 dB | -109.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9727 | 0.0010 | 5/19 | k=1: 49.973 Hz, -98.5 dB | -101.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0042 | 35 | k=3·f1+3·f2: 20999.601 Hz, -120.9 dB | -111.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.7 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.0 dB | -100.2 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.3 dB | -83.0 | 9.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.4 dB | -74.6 | 62.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0009 | 10/10 | k=1: 2320.543 Hz, -112.2 dB | -108.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9726 | 0.0021 | 4/19 | k=1: 49.973 Hz, -98.2 dB | -101.4 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0049 | 14 | k=-1·f1+3·f2: 17000.128 Hz, -116.8 dB | -112.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.5 dB | -97.0 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0002 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.0 dB | -99.5 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.9 | 57.9 | usb1k·1 |
| 1999.735 | -81.6 | 51.8 | usb1k·2 |
| 2999.603 | -83.3 | 51.5 | usb1k·3 |
| 6000.000 | -84.0 | 52.7 | fs8·1 |
| 12000.000 | -84.2 | 53.8 | fs8·2 |
| 18000.000 | -85.3 | 52.7 | fs8·3 |
| 3999.471 | -87.2 | 47.2 | usb1k·4 |
| 9998.676 | -88.4 | 49.1 | usb1k·10 |
| 4999.338 | -89.4 | 46.2 | usb1k·5 |
| 15997.882 | -90.5 | 47.4 | usb1k·16 |
| 6999.073 | -90.6 | 45.6 | usb1k·7 |
| 8998.808 | -90.7 | 45.6 | usb1k·9 |
| 16997.749 | -93.6 | 44.8 | usb1k·17 |
| 18997.484 | -94.1 | 44.3 | usb1k·19 |
| 20997.220 | -94.6 | 44.0 | usb1k·21 |
| 5999.206 | -94.2 | 42.5 | usb1k·6 |
| 12998.278 | -96.8 | 41.3 | usb1k·13 |
| 2000.000 | -97.6 | 35.8 | other1·1 |
| 11998.411 | -97.0 | 41.1 | usb1k·12 |
| 7998.941 | -96.4 | 39.3 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 58.0 | usb1k·1 |
| 1999.735 | -82.8 | 52.1 | usb1k·2 |
| 6000.000 | -84.0 | 53.7 | fs8·1 |
| 2999.603 | -83.9 | 52.2 | usb1k·3 |
| 12000.000 | -84.4 | 55.1 | fs8·2 |
| 18000.000 | -85.3 | 53.7 | fs8·3 |
| 3999.471 | -87.5 | 48.3 | usb1k·4 |
| 9998.676 | -88.3 | 50.3 | usb1k·10 |
| 4999.338 | -90.0 | 46.8 | usb1k·5 |
| 15997.882 | -90.8 | 48.5 | usb1k·16 |
| 6999.073 | -90.9 | 46.5 | usb1k·7 |
| 8998.808 | -91.3 | 47.1 | usb1k·9 |
| 16997.749 | -93.8 | 45.8 | usb1k·17 |
| 18997.485 | -94.0 | 45.5 | usb1k·19 |
| 20997.220 | -95.2 | 44.6 | usb1k·21 |
| 5999.206 | -95.4 | 42.4 | usb1k·6 |
| 12998.279 | -97.0 | 42.0 | usb1k·13 |
| 17997.617 | -97.8 | 41.1 | usb1k·18 |
| 11998.411 | -97.1 | 42.4 | usb1k·12 |
| 14998.014 | -97.8 | 41.0 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 63.3 | usb1k·1 |
| 1999.735 | -83.3 | 56.3 | usb1k·2 |
| 2999.603 | -84.0 | 56.9 | usb1k·3 |
| 6000.000 | -84.4 | 56.9 | fs8·1 |
| 12000.000 | -85.2 | 57.0 | fs8·2 |
| 18000.000 | -85.8 | 55.9 | fs8·3 |
| 3999.471 | -87.7 | 52.4 | usb1k·4 |
| 9998.676 | -88.6 | 53.9 | usb1k·10 |
| 15997.882 | -91.1 | 51.2 | usb1k·16 |
| 4999.338 | -90.8 | 50.1 | usb1k·5 |
| 6999.073 | -91.3 | 50.2 | usb1k·7 |
| 8998.808 | -92.1 | 49.5 | usb1k·9 |
| 16997.749 | -93.8 | 48.4 | usb1k·17 |
| 18997.485 | -94.3 | 47.6 | usb1k·19 |
| 20997.220 | -95.6 | 46.5 | usb1k·21 |
| 5999.206 | -95.9 | 45.4 | usb1k·6 |
| 12998.278 | -97.5 | 44.8 | usb1k·13 |
| 11998.411 | -97.3 | 44.9 | usb1k·12 |
| 7998.941 | -96.6 | 44.8 | usb1k·8 |
| 17997.617 | -98.1 | 43.7 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.4 | 58.7 | usb1k·1 |
| 1999.735 | -80.9 | 53.5 | usb1k·2 |
| 2999.603 | -83.0 | 52.9 | usb1k·3 |
| 6000.000 | -84.3 | 53.0 | fs8·1 |
| 12000.000 | -84.5 | 53.9 | fs8·2 |
| 18000.000 | -85.5 | 52.9 | fs8·3 |
| 3999.471 | -87.1 | 48.1 | usb1k·4 |
| 4999.338 | -88.6 | 47.9 | usb1k·5 |
| 9998.676 | -88.5 | 49.6 | usb1k·10 |
| 15997.882 | -90.2 | 48.2 | usb1k·16 |
| 6999.073 | -90.2 | 46.6 | usb1k·7 |
| 8998.808 | -90.2 | 47.2 | usb1k·9 |
| 16997.749 | -93.6 | 45.2 | usb1k·17 |
| 5999.206 | -92.9 | 44.4 | usb1k·6 |
| 18997.484 | -94.1 | 45.0 | usb1k·19 |
| 20997.220 | -94.5 | 44.5 | usb1k·21 |
| 7998.941 | -95.2 | 41.9 | usb1k·8 |
| 11998.411 | -96.3 | 42.0 | usb1k·12 |
| 12998.278 | -96.8 | 41.9 | usb1k·13 |
| 13998.146 | -97.1 | 41.3 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.00 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.13 | -0.03 | 0.03 |
| led | Kanal 1 | 11/11 | 1.35 | -3.18 | 0.61 |
| mains50 | Kanal 1 | 11/11 | 270.48 | 217.08 | 1.49 |
| other1 | Kanal 1 | 11/11 | 0.65 | -0.60 | 0.09 |
| other2 | Kanal 1 | 11/11 | 0.18 | 0.01 | 0.20 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.13 | -0.03 | 0.05 |
| led | Kanal 2 | 11/11 | 0.25 | -0.40 | 0.33 |
| mains50 | Kanal 2 | 11/11 | 270.20 | -147.40 | 1.15 |
| other1 | Kanal 2 | 11/11 | 0.53 | -0.76 | 0.07 |
| other2 | Kanal 2 | 11/11 | 0.12 | 0.11 | 0.17 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.00 | 0.04 |
| usb1k | Kanal 3 | 11/11 | 0.13 | 0.02 | 0.03 |
| led | Kanal 3 | 11/11 | 0.66 | -1.26 | 0.27 |
| mains50 | Kanal 3 | 11/11 | 57.69 | 16.92 | 0.76 |
| other1 | Kanal 3 | 11/11 | 0.37 | -0.22 | 0.08 |
| other2 | Kanal 3 | 11/11 | 0.09 | -0.01 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.02 | 0.04 |
| usb1k | Kanal 4 | 11/11 | 0.09 | 0.01 | 0.05 |
| led | Kanal 4 | 11/11 | 0.80 | -2.12 | 0.41 |
| mains50 | Kanal 4 | 11/11 | 237.66 | -220.27 | 1.12 |
| other1 | Kanal 4 | 11/11 | 0.57 | -0.32 | 0.07 |
| other2 | Kanal 4 | 11/11 | 0.19 | 0.16 | 0.21 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.30 | 0.16 s (6.40 Hz) | 28.5 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 37.4 |
| Kanal 2 | breitbandig | 1.28 | 0.16 s (6.40 Hz) | 30.1 |
| Kanal 2 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 38.6 |
| Kanal 3 | breitbandig | 0.65 | 0.31 s (3.22 Hz) | 27.4 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 43.6 |
| Kanal 4 | breitbandig | 1.06 | 0.16 s (6.40 Hz) | 30.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 37.5 |

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
| Kanal 1 | 1.00 | 0.97 | 0.92 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.92 | 0.96 |
| Kanal 3 | 0.92 | 0.92 | 1.00 | 0.91 |
| Kanal 4 | 0.95 | 0.96 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx5a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx5a-r1_psd.png)

### Kammprofile

![Kammprofile](B7-fx5a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx5a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 15:53:32. Stream-Meldungen: 0. owl_read: out/owl_read/B7-fx5a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
