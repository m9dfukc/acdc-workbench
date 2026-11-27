# Report B4y-noD-r1: B4y-noD-r1 – acdc1 fx3i-noD-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4x v22.4.r-fx3i-noD (ITCM ohne USB, ohne RX-Fix) |
| test | Build-4y-Sitzung: noD gegen 3d-Kontrolle (trennt Warteschleife Patch 12 und USB-Lage), Eingänge offen |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3i-noD-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-noD-r1 --manifest recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -67.8 | -71.3 | -70.4 | -71.3 | -85.5 | -70.8 | -94.5 | -70.4 | 76 % | -76.7 | 6.2 |
| Kanal 2 | -7.4 | -68.7 | -72.7 | -70.9 | -71.9 | -87.4 | -71.3 | -94.8 | -71.0 | 80 % | -78.0 | 7.1 |
| Kanal 3 | -5.6 | -70.0 | -74.1 | -72.1 | -73.0 | -91.8 | -72.4 | -95.7 | -72.1 | 88 % | -81.4 | 9.3 |
| Kanal 4 | -6.5 | -68.9 | -74.2 | -70.5 | -71.7 | -87.7 | -70.9 | -95.3 | -70.5 | 79 % | -77.2 | 6.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.5 | 4.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -71.9 | 71.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -112.8 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0000 | 0.0057 | 3/19 | k=1: 50.003 Hz, -97.4 dB | -98.5 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0017 | 54 | k=7·f1+2·f2: 18999.075 Hz, -113.6 dB | -104.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.5 dB | -96.3 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -99.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.6 | 5.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -72.2 | 74.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -112.9 dB | -107.5 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0000 | 0.0052 | 3/19 | k=1: 50.003 Hz, -98.1 dB | -98.9 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0016 | 68 | k=7·f1+2·f2: 18999.074 Hz, -113.8 dB | -103.7 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -96.5 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -85.1 dB | -84.2 | 6.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.8 dB | -73.0 | 81.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -113.8 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0001 | 0.0057 | 3/19 | k=1: 50.004 Hz, -98.8 dB | -99.5 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0020 | 90 | k=7·f1+2·f2: 18999.074 Hz, -114.4 dB | -103.9 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -97.5 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -100.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.5 dB | -83.9 | 4.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -72.8 | 58.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0010 | 10/10 | k=1: 2320.545 Hz, -112.9 dB | -109.2 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0001 | 0.0049 | 3/19 | k=1: 50.003 Hz, -98.5 dB | -99.6 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0009 | 174 | k=-1·f1+2·f2: 11000.132 Hz, -87.3 dB | -78.5 | 15.9 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 4 | 23000.9261 | 0.0000 | 1/1 | k=1: 23000.926 Hz, -92.0 dB | -95.3 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 57.6 | usb1k·1 |
| 2999.603 | -77.5 | 56.2 | usb1k·3 |
| 1999.736 | -78.0 | 54.8 | usb1k·2 |
| 6999.074 | -78.7 | 57.7 | usb1k·7 |
| 14998.015 | -82.1 | 56.0 | usb1k·15 |
| 9998.676 | -81.9 | 55.4 | usb1k·10 |
| 4999.339 | -83.0 | 52.2 | usb1k·5 |
| 12000.000 | -84.2 | 53.3 | fs8·2 |
| 13998.147 | -84.1 | 53.6 | usb1k·14 |
| 6000.000 | -84.8 | 50.7 | fs8·1 |
| 21997.089 | -84.3 | 53.9 | usb1k·22 |
| 11998.412 | -85.5 | 51.9 | usb1k·12 |
| 19997.354 | -86.2 | 51.5 | usb1k·20 |
| 7998.941 | -85.0 | 51.5 | usb1k·8 |
| 18997.486 | -86.9 | 51.4 | usb1k·19 |
| 16997.750 | -87.1 | 50.6 | usb1k·17 |
| 20997.221 | -86.8 | 51.4 | usb1k·21 |
| 18000.000 | -87.4 | 50.9 | fs8·3 |
| 8998.809 | -88.7 | 47.8 | usb1k·9 |
| 5999.206 | -89.6 | 45.9 | usb1k·6 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 58.4 | usb1k·1 |
| 2999.603 | -77.8 | 57.7 | usb1k·3 |
| 1999.735 | -78.6 | 55.9 | usb1k·2 |
| 6999.074 | -78.8 | 58.8 | usb1k·7 |
| 14998.015 | -82.1 | 57.0 | usb1k·15 |
| 9998.676 | -81.9 | 56.5 | usb1k·10 |
| 4999.339 | -82.6 | 54.0 | usb1k·5 |
| 12000.000 | -84.4 | 54.3 | fs8·2 |
| 13998.147 | -84.3 | 54.9 | usb1k·14 |
| 6000.000 | -84.9 | 52.2 | fs8·1 |
| 21997.089 | -84.5 | 55.1 | usb1k·22 |
| 11998.412 | -85.3 | 53.2 | usb1k·12 |
| 19997.354 | -86.0 | 53.2 | usb1k·20 |
| 7998.941 | -84.8 | 53.0 | usb1k·8 |
| 18997.486 | -87.0 | 52.2 | usb1k·19 |
| 16997.750 | -87.2 | 51.6 | usb1k·17 |
| 18000.000 | -87.4 | 51.6 | fs8·3 |
| 20997.221 | -87.0 | 52.1 | usb1k·21 |
| 8998.809 | -89.1 | 49.1 | usb1k·9 |
| 5999.206 | -90.3 | 46.7 | usb1k·6 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.8 | 62.3 | usb1k·1 |
| 2999.603 | -78.5 | 61.2 | usb1k·3 |
| 1999.736 | -79.8 | 59.0 | usb1k·2 |
| 6999.074 | -79.4 | 62.2 | usb1k·7 |
| 14998.015 | -82.5 | 59.3 | usb1k·15 |
| 9998.676 | -82.3 | 59.5 | usb1k·10 |
| 4999.339 | -82.9 | 57.6 | usb1k·5 |
| 12000.000 | -85.1 | 56.9 | fs8·2 |
| 13998.147 | -85.0 | 57.2 | usb1k·14 |
| 6000.000 | -85.4 | 56.0 | fs8·1 |
| 21997.089 | -84.9 | 56.6 | usb1k·22 |
| 11998.412 | -85.7 | 56.3 | usb1k·12 |
| 19997.354 | -86.4 | 55.5 | usb1k·20 |
| 7998.941 | -85.1 | 56.1 | usb1k·8 |
| 16997.750 | -87.5 | 54.6 | usb1k·17 |
| 18997.486 | -87.5 | 54.2 | usb1k·19 |
| 18000.000 | -87.8 | 53.7 | fs8·3 |
| 20997.221 | -87.6 | 53.6 | usb1k·21 |
| 8998.809 | -89.9 | 51.6 | usb1k·9 |
| 17997.618 | -92.0 | 49.6 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 58.8 | usb1k·1 |
| 2999.603 | -77.5 | 57.3 | usb1k·3 |
| 1999.735 | -78.7 | 55.9 | usb1k·2 |
| 6999.074 | -80.2 | 56.4 | usb1k·7 |
| 14998.015 | -82.4 | 56.1 | usb1k·15 |
| 12000.000 | -84.5 | 53.0 | fs8·2 |
| 9998.676 | -83.8 | 53.4 | usb1k·10 |
| 6000.000 | -85.3 | 51.2 | fs8·1 |
| 13998.147 | -85.7 | 52.2 | usb1k·14 |
| 4999.338 | -85.5 | 50.0 | usb1k·5 |
| 11998.412 | -85.7 | 51.7 | usb1k·12 |
| 21997.089 | -86.6 | 51.2 | usb1k·22 |
| 11000.132 | -87.3 | 49.8 | imd·-1·f1+2·f2 |
| 18999.868 | -87.3 | 50.5 | imd·1·f1+3·f2 |
| 23000.132 | -87.4 | 50.6 | imd·-1·f1+4·f2 |
| 5000.132 | -87.4 | 48.1 | imd·-1·f1+1·f2 |
| 6999.868 | -87.5 | 49.2 | imd·1·f1+1·f2 |
| 17000.132 | -87.5 | 50.2 | imd·-1·f1+3·f2 |
| 12999.868 | -87.5 | 49.8 | imd·1·f1+2·f2 |
| 20997.221 | -87.0 | 51.0 | usb1k·21 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.15 | 0.08 | 0.01 |
| led | Kanal 1 | 11/11 | 1.74 | 0.80 | 0.43 |
| mains50 | Kanal 1 | 11/11 | 19.98 | -40.44 | 0.71 |
| other1 | Kanal 1 | 11/11 | 0.23 | -0.26 | 0.04 |
| other2 | Kanal 1 | 11/11 | 0.27 | 0.10 | 0.26 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.17 | 0.06 | 0.01 |
| led | Kanal 2 | 11/11 | 0.36 | 0.56 | 0.38 |
| mains50 | Kanal 2 | 11/11 | 34.41 | -49.30 | 0.46 |
| other1 | Kanal 2 | 11/11 | 0.17 | -0.04 | 0.05 |
| other2 | Kanal 2 | 11/11 | 0.24 | 0.07 | 0.21 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.04 | 0.06 | 0.01 |
| led | Kanal 3 | 11/11 | 0.88 | 0.88 | 0.33 |
| mains50 | Kanal 3 | 11/11 | 15.06 | -36.14 | 0.40 |
| other1 | Kanal 3 | 11/11 | 0.29 | 0.02 | 0.03 |
| other2 | Kanal 3 | 11/11 | 0.15 | 0.06 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.03 | 0.04 |
| usb1k | Kanal 4 | 11/11 | 0.12 | 0.03 | 0.01 |
| led | Kanal 4 | 11/11 | 1.31 | 0.51 | 0.30 |
| mains50 | Kanal 4 | 11/11 | 33.87 | -41.35 | 0.57 |
| other1 | Kanal 4 | 11/11 | 0.04 | -0.02 | 0.13 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.99 | 0.31 s (3.18 Hz) | 31.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 37.5 |
| Kanal 2 | breitbandig | 1.79 | 0.31 s (3.18 Hz) | 32.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 39.6 |
| Kanal 3 | breitbandig | 1.63 | 0.31 s (3.22 Hz) | 33.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 43.5 |
| Kanal 4 | breitbandig | 1.36 | 0.31 s (3.18 Hz) | 31.7 |
| Kanal 4 | 999.9 Hz ± 10 | 1.25 | 1.25 s (0.80 Hz) | 44.4 |

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
| Kanal 1 | 1.00 | 0.98 | 0.96 | 0.88 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.89 |
| Kanal 3 | 0.96 | 0.96 | 1.00 | 0.85 |
| Kanal 4 | 0.88 | 0.89 | 0.85 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -70.4 | -71.1 | +0.7 | 76 % | 68 % |
| Kanal 2 | -70.9 | -71.9 | +0.9 | 80 % | 73 % |
| Kanal 3 | -72.1 | -73.1 | +1.0 | 88 % | 82 % |
| Kanal 4 | -70.5 | -71.0 | +0.5 | 79 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-noD-r1_psd.png)

### Kammprofile

![Kammprofile](B4y-noD-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-noD-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:23:59. Stream-Meldungen: 0. owl_read: reports/owl_read/B4y-noD-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
