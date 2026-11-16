# Report B4z-fx3k-r1: B4z-fx3k-r1 – acdc1 fx3k-open-inputs-4z, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4z v22.4.r-fx3k |
| test | Build-4z-Sitzung: fx3k (ITCM ohne USB, Patch 11f + 12b), Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3k-open-inputs-4z-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4z-fx3k-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -69.8 | -81.0 | -70.1 | -71.0 | -86.8 | -70.4 | -94.9 | -70.1 | 78 % | -76.8 | 6.6 |
| Kanal 2 | -7.5 | -70.4 | -82.7 | -70.6 | -71.5 | -88.8 | -70.9 | -95.1 | -70.6 | 82 % | -78.1 | 7.4 |
| Kanal 3 | -5.7 | -71.5 | -86.2 | -71.7 | -72.5 | -93.1 | -71.9 | -95.9 | -71.7 | 89 % | -81.3 | 9.6 |
| Kanal 4 | -6.6 | -69.9 | -82.8 | -70.1 | -70.9 | -89.1 | -70.4 | -95.4 | -70.2 | 83 % | -77.8 | 7.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.5 | 4.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -71.5 | 73.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0009 | 10/10 | k=1: 2320.546 Hz, -113.1 dB | -108.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9860 | 0.0001 | 2/19 | k=1: 49.986 Hz, -100.1 dB | -102.7 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0014 | 56 | k=15·f1+1·f2: 20998.012 Hz, -114.8 dB | -104.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.001 Hz, -97.7 dB | -96.9 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.3 dB | -99.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.1 dB | -83.6 | 5.1 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -71.8 | 76.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5447 | 0.0007 | 10/10 | k=9: 20884.903 Hz, -113.0 dB | -107.5 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9855 | 0.0003 | 2/19 | k=1: 49.986 Hz, -100.7 dB | -103.2 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0012 | 67 | k=-5·f1+4·f2: 19000.661 Hz, -114.5 dB | -103.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.001 Hz, -98.3 dB | -97.1 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.7 dB | -84.2 | 5.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -72.5 | 83.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0005 | 10/10 | k=2: 4641.091 Hz, -113.7 dB | -109.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9933 | 0.0083 | 5/19 | k=1: 49.986 Hz, -101.0 dB | -102.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0018 | 94 | k=-7·f1+4·f2: 17000.926 Hz, -114.8 dB | -103.9 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.8 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -100.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.3 dB | -83.7 | 4.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -71.2 | 78.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0008 | 10/10 | k=1: 2320.545 Hz, -112.7 dB | -108.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9850 | 0.0005 | 2/19 | k=1: 49.985 Hz, -101.3 dB | -103.5 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0018 | 69 | k=15·f1+1·f2: 20998.014 Hz, -114.9 dB | -103.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.001 Hz, -98.6 dB | -97.3 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.1 dB | -99.8 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 58.5 | usb1k·1 |
| 2999.603 | -76.9 | 56.8 | usb1k·3 |
| 1999.735 | -77.6 | 55.7 | usb1k·2 |
| 6999.073 | -78.2 | 57.7 | usb1k·7 |
| 14998.014 | -81.4 | 55.3 | usb1k·15 |
| 9998.676 | -81.3 | 56.0 | usb1k·10 |
| 4999.338 | -82.4 | 53.0 | usb1k·5 |
| 6000.000 | -84.2 | 51.5 | fs8·1 |
| 13998.146 | -84.0 | 53.3 | usb1k·14 |
| 21997.087 | -84.3 | 54.0 | usb1k·22 |
| 19997.352 | -85.5 | 52.4 | usb1k·20 |
| 7998.941 | -84.4 | 52.2 | usb1k·8 |
| 12000.000 | -85.8 | 51.8 | fs8·2 |
| 11998.411 | -85.0 | 52.6 | usb1k·12 |
| 18000.000 | -86.0 | 52.1 | fs8·3 |
| 20997.219 | -86.8 | 50.8 | usb1k·21 |
| 16997.749 | -87.0 | 51.1 | usb1k·17 |
| 18997.484 | -87.3 | 49.6 | usb1k·19 |
| 5999.206 | -89.0 | 46.8 | usb1k·6 |
| 8998.808 | -88.4 | 48.3 | usb1k·9 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 59.3 | usb1k·1 |
| 2999.603 | -77.2 | 57.9 | usb1k·3 |
| 1999.735 | -78.3 | 56.5 | usb1k·2 |
| 6999.073 | -78.4 | 58.9 | usb1k·7 |
| 14998.014 | -81.4 | 56.7 | usb1k·15 |
| 4999.338 | -81.9 | 55.0 | usb1k·5 |
| 9998.676 | -81.2 | 57.3 | usb1k·10 |
| 6000.000 | -84.1 | 53.3 | fs8·1 |
| 13998.146 | -84.3 | 54.5 | usb1k·14 |
| 21997.087 | -84.3 | 54.7 | usb1k·22 |
| 19997.352 | -85.3 | 53.9 | usb1k·20 |
| 7998.941 | -84.1 | 53.7 | usb1k·8 |
| 11998.411 | -84.9 | 53.8 | usb1k·12 |
| 18000.000 | -86.0 | 53.1 | fs8·3 |
| 12000.000 | -86.1 | 52.6 | fs8·2 |
| 16997.749 | -87.1 | 52.2 | usb1k·17 |
| 20997.219 | -87.1 | 51.8 | usb1k·21 |
| 18997.484 | -87.3 | 50.3 | usb1k·19 |
| 17997.616 | -90.3 | 49.0 | usb1k·18 |
| 5999.206 | -89.6 | 47.7 | usb1k·6 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 63.3 | usb1k·1 |
| 2999.603 | -78.0 | 61.9 | usb1k·3 |
| 1999.735 | -79.3 | 59.8 | usb1k·2 |
| 6999.073 | -78.9 | 61.8 | usb1k·7 |
| 14998.014 | -81.8 | 59.0 | usb1k·15 |
| 4999.338 | -82.3 | 58.2 | usb1k·5 |
| 9998.676 | -81.6 | 60.2 | usb1k·10 |
| 6000.000 | -84.7 | 56.2 | fs8·1 |
| 21997.087 | -84.8 | 56.6 | usb1k·22 |
| 13998.146 | -84.8 | 56.5 | usb1k·14 |
| 19997.352 | -85.7 | 55.3 | usb1k·20 |
| 7998.941 | -84.5 | 56.8 | usb1k·8 |
| 11998.411 | -85.2 | 56.0 | usb1k·12 |
| 18000.000 | -86.4 | 55.0 | fs8·3 |
| 12000.000 | -86.9 | 54.3 | fs8·2 |
| 16997.749 | -87.4 | 54.3 | usb1k·17 |
| 18997.484 | -87.7 | 53.1 | usb1k·19 |
| 20997.219 | -87.6 | 53.5 | usb1k·21 |
| 17997.616 | -90.7 | 50.8 | usb1k·18 |
| 8998.808 | -89.7 | 51.5 | usb1k·9 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 60.6 | usb1k·1 |
| 1999.735 | -77.0 | 57.4 | usb1k·2 |
| 2999.603 | -76.9 | 58.2 | usb1k·3 |
| 6999.073 | -78.2 | 58.6 | usb1k·7 |
| 14998.014 | -81.6 | 56.2 | usb1k·15 |
| 9998.676 | -81.4 | 56.6 | usb1k·10 |
| 4999.338 | -83.4 | 53.3 | usb1k·5 |
| 6000.000 | -84.3 | 52.5 | fs8·1 |
| 13998.146 | -84.0 | 54.0 | usb1k·14 |
| 21997.087 | -84.4 | 53.7 | usb1k·22 |
| 19997.352 | -85.9 | 52.2 | usb1k·20 |
| 7998.941 | -84.8 | 52.6 | usb1k·8 |
| 18000.000 | -86.2 | 52.0 | fs8·3 |
| 12000.000 | -86.3 | 51.8 | fs8·2 |
| 11998.411 | -85.6 | 52.6 | usb1k·12 |
| 20997.219 | -86.9 | 51.4 | usb1k·21 |
| 16997.749 | -87.2 | 50.7 | usb1k·17 |
| 18997.484 | -87.6 | 49.9 | usb1k·19 |
| 5999.206 | -88.0 | 48.8 | usb1k·6 |
| 8998.808 | -87.9 | 50.0 | usb1k·9 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.02 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.12 | 0.02 | 0.03 |
| led | Kanal 1 | 11/11 | 1.04 | 1.42 | 0.47 |
| mains50 | Kanal 1 | 11/11 | 800.56 | -411.31 | 1.34 |
| other1 | Kanal 1 | 11/11 | 0.41 | -0.36 | 0.05 |
| other2 | Kanal 1 | 11/11 | 0.19 | -0.00 | 0.36 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.14 | -0.04 | 0.03 |
| led | Kanal 2 | 11/11 | 0.30 | -0.03 | 0.33 |
| mains50 | Kanal 2 | 11/11 | 539.42 | -1100.92 | 1.05 |
| other1 | Kanal 2 | 11/11 | 0.34 | -0.15 | 0.05 |
| other2 | Kanal 2 | 11/11 | 0.20 | 0.04 | 0.34 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.00 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.04 | -0.01 | 0.03 |
| led | Kanal 3 | 11/11 | 0.69 | -0.04 | 0.21 |
| mains50 | Kanal 3 | 11/11 | 15.63 | -38.48 | 0.57 |
| other1 | Kanal 3 | 11/11 | 0.39 | -0.11 | 0.05 |
| other2 | Kanal 3 | 11/11 | 0.13 | 0.11 | 0.28 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.12 | -0.07 | 0.03 |
| led | Kanal 4 | 11/11 | 1.21 | 1.00 | 0.39 |
| mains50 | Kanal 4 | 11/11 | 547.24 | -1139.53 | 1.20 |
| other1 | Kanal 4 | 11/11 | 0.42 | -0.08 | 0.05 |
| other2 | Kanal 4 | 11/11 | 0.18 | 0.03 | 0.35 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.54 | 7.50 s (0.13 Hz) | 18.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 37.6 |
| Kanal 2 | breitbandig | 0.44 | 7.50 s (0.13 Hz) | 21.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 39.2 |
| Kanal 3 | breitbandig | 0.34 | 0.63 s (1.58 Hz) | 26.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 44.2 |
| Kanal 4 | breitbandig | 0.40 | 7.50 s (0.13 Hz) | 20.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 38.8 |

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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.96 |
| Kanal 2 | 0.97 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.94 |
| Kanal 4 | 0.96 | 0.97 | 0.94 | 1.00 |

## Vergleich mit Referenz B4z-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -70.1 | -71.2 | +1.1 | 78 % | 67 % |
| Kanal 2 | -70.6 | -71.7 | +1.1 | 82 % | 73 % |
| Kanal 3 | -71.7 | -72.9 | +1.2 | 89 % | 83 % |
| Kanal 4 | -70.1 | -71.0 | +0.9 | 83 % | 73 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4z-fx3k-r1_psd.png)

### Kammprofile

![Kammprofile](B4z-fx3k-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4z-fx3k-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 19:13:30. Stream-Meldungen: 0. owl_read: out/owl_read/B4z-fx3k-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
