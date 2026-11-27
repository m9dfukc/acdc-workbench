# Report B5c-fx3l-r1: B5c-fx3l-r1 – acdc1 fx3l-open-inputs-5, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 5c v22.4.r-fx3l |
| test | Build-5-Sitzung: fx3l (alle Gruppen im ITCM, Patch 11g + 12b + 14), Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3l-open-inputs-5-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B5c-fx3l-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-end-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -70.7 | -76.4 | -72.0 | -72.7 | -86.8 | -72.3 | -94.6 | -72.1 | 68 % | -77.0 | 4.9 |
| Kanal 2 | -7.5 | -71.9 | -78.6 | -73.0 | -73.6 | -88.7 | -73.2 | -94.9 | -73.0 | 71 % | -78.4 | 5.4 |
| Kanal 3 | -5.7 | -73.2 | -79.1 | -74.4 | -75.0 | -93.1 | -74.6 | -95.8 | -74.5 | 83 % | -82.1 | 7.6 |
| Kanal 4 | -6.6 | -71.3 | -79.4 | -72.0 | -72.5 | -89.0 | -72.2 | -95.1 | -72.0 | 75 % | -78.1 | 6.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.1 | 7.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.9 dB | -74.3 | 59.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0009 | 10/10 | k=2: 4641.090 Hz, -112.9 dB | -108.6 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0267 | 0.0019 | 2/19 | k=1: 50.028 Hz, -99.4 dB | -101.8 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0011 | 2 | k=-3·f1+4·f2: 21000.396 Hz, -121.8 dB | -123.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -96.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.9 dB | -98.7 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.5 dB | -83.2 | 9.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.1 | 61.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0007 | 10/10 | k=8: 18564.358 Hz, -113.3 dB | -107.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0266 | 0.0019 | 2/19 | k=1: 50.028 Hz, -100.0 dB | -102.5 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0021 | 5 | k=-3·f1+4·f2: 21000.394 Hz, -122.0 dB | -119.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.2 dB | -96.9 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -99.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -85.1 dB | -83.8 | 11.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -76.0 | 70.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0004 | 10/10 | k=2: 4641.090 Hz, -113.4 dB | -109.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0277 | 0.0009 | 2/19 | k=1: 50.028 Hz, -100.7 dB | -103.3 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0025 | 10 | k=-3·f1+4·f2: 21000.398 Hz, -122.0 dB | -118.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.7 dB | -97.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.8 dB | -100.1 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.7 dB | -83.4 | 7.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -73.7 | 67.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.545 Hz, -112.6 dB | -108.0 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0270 | 0.0017 | 2/19 | k=1: 50.028 Hz, -100.2 dB | -102.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0036 | 5 | k=-2·f1+1·f2: 4000.271 Hz, -120.4 dB | -117.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.6 dB | -97.2 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.7 dB | -99.3 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.9 | 59.1 | usb1k·1 |
| 1999.735 | -81.1 | 52.4 | usb1k·2 |
| 2999.603 | -82.6 | 52.1 | usb1k·3 |
| 12000.000 | -84.4 | 53.4 | fs8·2 |
| 6000.000 | -84.5 | 51.7 | fs8·1 |
| 18000.000 | -85.9 | 51.5 | fs8·3 |
| 3999.471 | -86.9 | 48.2 | usb1k·4 |
| 9998.676 | -88.4 | 49.5 | usb1k·10 |
| 4999.338 | -89.5 | 45.6 | usb1k·5 |
| 15997.881 | -90.7 | 47.4 | usb1k·16 |
| 6999.073 | -90.3 | 46.2 | usb1k·7 |
| 8998.808 | -90.9 | 45.8 | usb1k·9 |
| 16997.749 | -93.3 | 45.3 | usb1k·17 |
| 5999.206 | -93.7 | 42.5 | usb1k·6 |
| 20997.220 | -94.2 | 45.0 | usb1k·21 |
| 18997.485 | -94.4 | 44.5 | usb1k·19 |
| 13998.146 | -96.2 | 42.3 | usb1k·14 |
| 11998.411 | -96.7 | 41.1 | usb1k·12 |
| 2000.000 | -97.6 | 36.0 | other1·1 |
| 7998.941 | -96.4 | 40.2 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 59.8 | usb1k·1 |
| 1999.735 | -82.2 | 52.7 | usb1k·2 |
| 2999.603 | -83.2 | 52.8 | usb1k·3 |
| 6000.000 | -84.5 | 52.8 | fs8·1 |
| 12000.000 | -84.7 | 54.8 | fs8·2 |
| 18000.000 | -85.9 | 52.7 | fs8·3 |
| 3999.471 | -87.2 | 49.4 | usb1k·4 |
| 9998.676 | -88.5 | 50.1 | usb1k·10 |
| 4999.338 | -90.2 | 45.8 | usb1k·5 |
| 15997.881 | -91.0 | 48.1 | usb1k·16 |
| 6999.073 | -90.9 | 47.2 | usb1k·7 |
| 8998.808 | -91.4 | 46.9 | usb1k·9 |
| 16997.749 | -93.5 | 46.0 | usb1k·17 |
| 18997.485 | -94.3 | 45.7 | usb1k·19 |
| 20997.220 | -94.7 | 45.1 | usb1k·21 |
| 5999.206 | -94.8 | 42.4 | usb1k·6 |
| 13998.146 | -97.4 | 41.8 | usb1k·14 |
| 17997.617 | -97.8 | 40.9 | usb1k·18 |
| 11998.411 | -97.0 | 42.4 | usb1k·12 |
| 14998.014 | -97.7 | 41.4 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 63.4 | usb1k·1 |
| 1999.735 | -83.4 | 56.1 | usb1k·2 |
| 2999.603 | -84.0 | 56.5 | usb1k·3 |
| 6000.000 | -85.1 | 56.9 | fs8·1 |
| 12000.000 | -85.5 | 56.8 | fs8·2 |
| 18000.000 | -86.4 | 55.6 | fs8·3 |
| 3999.471 | -87.8 | 53.2 | usb1k·4 |
| 9998.676 | -88.9 | 53.3 | usb1k·10 |
| 15997.882 | -91.4 | 50.7 | usb1k·16 |
| 4999.338 | -91.0 | 49.7 | usb1k·5 |
| 6999.073 | -91.6 | 50.0 | usb1k·7 |
| 8998.808 | -92.1 | 49.7 | usb1k·9 |
| 16997.749 | -94.0 | 48.4 | usb1k·17 |
| 18997.485 | -94.6 | 48.1 | usb1k·19 |
| 20997.220 | -95.3 | 46.6 | usb1k·21 |
| 5999.206 | -96.1 | 45.8 | usb1k·6 |
| 17997.617 | -98.1 | 43.9 | usb1k·18 |
| 11998.411 | -97.4 | 44.9 | usb1k·12 |
| 12998.279 | -97.8 | 42.6 | usb1k·13 |
| 14998.014 | -98.5 | 43.8 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 60.7 | usb1k·1 |
| 1999.735 | -80.0 | 54.7 | usb1k·2 |
| 2999.603 | -82.3 | 53.2 | usb1k·3 |
| 6000.000 | -84.7 | 51.7 | fs8·1 |
| 12000.000 | -84.9 | 53.5 | fs8·2 |
| 18000.000 | -86.2 | 52.4 | fs8·3 |
| 3999.471 | -86.8 | 49.3 | usb1k·4 |
| 4999.338 | -88.6 | 46.4 | usb1k·5 |
| 9998.676 | -88.6 | 49.2 | usb1k·10 |
| 15997.882 | -90.5 | 48.0 | usb1k·16 |
| 6999.073 | -90.1 | 46.8 | usb1k·7 |
| 8998.808 | -90.1 | 47.7 | usb1k·9 |
| 5999.206 | -92.3 | 44.1 | usb1k·6 |
| 16997.749 | -93.2 | 46.1 | usb1k·17 |
| 20997.220 | -94.0 | 45.1 | usb1k·21 |
| 18997.485 | -94.5 | 44.3 | usb1k·19 |
| 13998.146 | -95.6 | 43.5 | usb1k·14 |
| 7998.941 | -95.1 | 42.3 | usb1k·8 |
| 11998.411 | -96.0 | 42.3 | usb1k·12 |
| 12998.279 | -96.9 | 39.8 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.03 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.12 | -0.12 | 0.03 |
| led | Kanal 1 | 11/11 | 0.67 | -1.03 | 0.69 |
| mains50 | Kanal 1 | 11/11 | 397.21 | 79.88 | 1.38 |
| other1 | Kanal 1 | 11/11 | 0.53 | 0.06 | 0.07 |
| other2 | Kanal 1 | 11/11 | 0.21 | 0.20 | 0.16 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.11 | -0.06 | 0.05 |
| led | Kanal 2 | 11/11 | 0.43 | 0.36 | 0.39 |
| mains50 | Kanal 2 | 11/11 | 309.25 | 33.46 | 0.96 |
| other1 | Kanal 2 | 11/11 | 0.35 | -0.16 | 0.05 |
| other2 | Kanal 2 | 11/11 | 0.21 | 0.19 | 0.13 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.09 | -0.02 | 0.03 |
| led | Kanal 3 | 11/11 | 0.80 | 1.60 | 0.47 |
| mains50 | Kanal 3 | 11/11 | 215.09 | 106.94 | 0.75 |
| other1 | Kanal 3 | 11/11 | 0.26 | -0.05 | 0.11 |
| other2 | Kanal 3 | 11/11 | 0.11 | 0.03 | 0.09 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.00 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.13 | -0.12 | 0.04 |
| led | Kanal 4 | 11/11 | 1.19 | 1.40 | 0.55 |
| mains50 | Kanal 4 | 11/11 | 244.88 | -36.40 | 1.08 |
| other1 | Kanal 4 | 11/11 | 0.47 | -0.07 | 0.07 |
| other2 | Kanal 4 | 11/11 | 0.21 | 0.23 | 0.14 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.22 | 0.31 s (3.18 Hz) | 27.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 38.2 |
| Kanal 2 | breitbandig | 1.03 | 0.31 s (3.18 Hz) | 26.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 40.5 |
| Kanal 3 | breitbandig | 1.04 | 0.31 s (3.18 Hz) | 30.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.6 |
| Kanal 4 | breitbandig | 0.78 | 0.31 s (3.18 Hz) | 26.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 39.3 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.94 | 0.93 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.96 | 0.91 | 1.00 |

## Vergleich mit Referenz B4z-3d-end-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.0 | -71.0 | -1.0 | 68 % | 67 % |
| Kanal 2 | -73.0 | -71.8 | -1.2 | 71 % | 73 % |
| Kanal 3 | -74.4 | -73.1 | -1.4 | 83 % | 82 % |
| Kanal 4 | -72.0 | -70.9 | -1.0 | 75 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B5c-fx3l-r1_psd.png)

### Kammprofile

![Kammprofile](B5c-fx3l-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B5c-fx3l-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 21:55:23. Stream-Meldungen: 0. owl_read: reports/owl_read/B5c-fx3l-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
