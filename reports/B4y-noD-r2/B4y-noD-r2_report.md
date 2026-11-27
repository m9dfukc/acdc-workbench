# Report B4y-noD-r2: B4y-noD-r2 – acdc1 fx3i-noD-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4x v22.4.r-fx3i-noD (ITCM ohne USB, ohne RX-Fix) |
| test | Build-4y-Sitzung: noD gegen 3d-Kontrolle (trennt Warteschleife Patch 12 und USB-Lage), Eingänge offen |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3i-noD-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-noD-r2 --manifest recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -69.3 | -75.8 | -70.4 | -71.3 | -85.6 | -70.8 | -94.7 | -70.4 | 76 % | -76.7 | 6.3 |
| Kanal 2 | -7.5 | -70.0 | -76.9 | -70.9 | -71.9 | -87.5 | -71.3 | -95.0 | -71.0 | 80 % | -78.0 | 7.1 |
| Kanal 3 | -5.7 | -71.4 | -80.1 | -72.1 | -73.0 | -92.0 | -72.4 | -95.8 | -72.1 | 88 % | -81.4 | 9.3 |
| Kanal 4 | -6.5 | -69.7 | -77.5 | -70.5 | -71.7 | -87.8 | -70.9 | -95.2 | -70.5 | 79 % | -77.2 | 6.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.5 | 4.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.9 dB | -71.9 | 71.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0010 | 10/10 | k=2: 4641.089 Hz, -113.6 dB | -108.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9830 | 0.0007 | 2/19 | k=1: 49.984 Hz, -98.1 dB | -100.6 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0015 | 51 | k=7·f1+2·f2: 18999.073 Hz, -114.9 dB | -104.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0006 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -96.7 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.3 dB | -99.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.6 dB | -83.6 | 5.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -72.2 | 74.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=9: 20884.902 Hz, -113.0 dB | -107.7 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9835 | 0.0001 | 2/19 | k=1: 49.984 Hz, -98.7 dB | -101.1 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0016 | 69 | k=-7·f1+4·f2: 17000.926 Hz, -114.7 dB | -104.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -98.2 dB | -96.9 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -85.3 dB | -84.2 | 6.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.6 dB | -72.9 | 82.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0007 | 10/10 | k=1: 2320.545 Hz, -113.8 dB | -109.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9837 | 0.0004 | 2/19 | k=1: 49.984 Hz, -99.3 dB | -101.9 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0014 | 84 | k=-7·f1+4·f2: 17000.926 Hz, -114.6 dB | -104.2 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -97.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -100.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.7 dB | -83.9 | 4.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -72.8 | 58.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0010 | 10/10 | k=1: 2320.544 Hz, -114.0 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9835 | 0.0002 | 2/19 | k=1: 49.983 Hz, -99.1 dB | -101.4 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0012 | 175 | k=1·f1+1·f2: 6999.868 Hz, -87.1 dB | -78.4 | 16.0 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 4 | 23000.9261 | 0.0000 | 1/1 | k=1: 23000.926 Hz, -91.9 dB | -95.2 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.9 | 57.7 | usb1k·1 |
| 2999.603 | -77.5 | 57.0 | usb1k·3 |
| 1999.736 | -78.1 | 54.5 | usb1k·2 |
| 6999.074 | -78.6 | 57.2 | usb1k·7 |
| 14998.015 | -82.1 | 55.5 | usb1k·15 |
| 9998.677 | -82.0 | 55.3 | usb1k·10 |
| 4999.339 | -83.1 | 51.8 | usb1k·5 |
| 13998.147 | -84.1 | 53.2 | usb1k·14 |
| 12000.000 | -84.4 | 53.2 | fs8·2 |
| 6000.000 | -84.8 | 51.0 | fs8·1 |
| 21997.089 | -84.4 | 53.2 | usb1k·22 |
| 11998.412 | -85.5 | 52.3 | usb1k·12 |
| 19997.354 | -86.2 | 51.9 | usb1k·20 |
| 7998.941 | -85.0 | 51.5 | usb1k·8 |
| 18000.000 | -87.0 | 51.5 | fs8·3 |
| 18997.486 | -87.0 | 51.3 | usb1k·19 |
| 16997.750 | -87.2 | 50.5 | usb1k·17 |
| 20997.221 | -86.8 | 51.1 | usb1k·21 |
| 8998.809 | -88.7 | 48.6 | usb1k·9 |
| 5999.206 | -89.5 | 46.2 | usb1k·6 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 58.4 | usb1k·1 |
| 2999.603 | -77.8 | 58.0 | usb1k·3 |
| 1999.736 | -78.8 | 55.3 | usb1k·2 |
| 6999.074 | -78.7 | 58.5 | usb1k·7 |
| 14998.015 | -82.1 | 56.7 | usb1k·15 |
| 9998.676 | -81.9 | 56.6 | usb1k·10 |
| 4999.339 | -82.6 | 53.8 | usb1k·5 |
| 13998.147 | -84.3 | 54.3 | usb1k·14 |
| 12000.000 | -84.6 | 54.1 | fs8·2 |
| 6000.000 | -84.9 | 52.4 | fs8·1 |
| 21997.089 | -84.5 | 54.1 | usb1k·22 |
| 11998.412 | -85.3 | 53.6 | usb1k·12 |
| 19997.354 | -86.1 | 53.0 | usb1k·20 |
| 7998.941 | -84.8 | 53.2 | usb1k·8 |
| 18000.000 | -87.0 | 52.4 | fs8·3 |
| 18997.486 | -87.0 | 52.1 | usb1k·19 |
| 16997.750 | -87.3 | 51.9 | usb1k·17 |
| 20997.221 | -87.0 | 52.2 | usb1k·21 |
| 8998.809 | -89.0 | 49.3 | usb1k·9 |
| 5999.206 | -90.2 | 47.1 | usb1k·6 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.6 | 62.6 | usb1k·1 |
| 2999.603 | -78.6 | 61.7 | usb1k·3 |
| 1999.736 | -79.8 | 59.0 | usb1k·2 |
| 6999.074 | -79.4 | 61.8 | usb1k·7 |
| 14998.015 | -82.5 | 59.1 | usb1k·15 |
| 9998.676 | -82.3 | 59.7 | usb1k·10 |
| 4999.339 | -83.0 | 57.5 | usb1k·5 |
| 13998.147 | -85.0 | 56.9 | usb1k·14 |
| 12000.000 | -85.3 | 56.7 | fs8·2 |
| 6000.000 | -85.3 | 55.7 | fs8·1 |
| 21997.089 | -85.0 | 56.3 | usb1k·22 |
| 11998.412 | -85.7 | 56.3 | usb1k·12 |
| 19997.353 | -86.4 | 55.3 | usb1k·20 |
| 7998.941 | -85.2 | 56.0 | usb1k·8 |
| 18000.000 | -87.4 | 54.4 | fs8·3 |
| 16997.750 | -87.6 | 54.2 | usb1k·17 |
| 18997.486 | -87.5 | 54.1 | usb1k·19 |
| 20997.221 | -87.6 | 53.5 | usb1k·21 |
| 8998.809 | -89.9 | 52.4 | usb1k·9 |
| 17997.618 | -92.1 | 49.8 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 58.3 | usb1k·1 |
| 2999.603 | -77.6 | 57.6 | usb1k·3 |
| 1999.736 | -78.8 | 55.3 | usb1k·2 |
| 6999.074 | -80.1 | 56.0 | usb1k·7 |
| 14998.015 | -82.5 | 55.4 | usb1k·15 |
| 12000.000 | -84.7 | 53.1 | fs8·2 |
| 9998.677 | -83.9 | 53.4 | usb1k·10 |
| 6000.000 | -85.4 | 50.7 | fs8·1 |
| 13998.147 | -85.7 | 51.6 | usb1k·14 |
| 4999.339 | -85.5 | 50.3 | usb1k·5 |
| 11998.412 | -85.6 | 52.2 | usb1k·12 |
| 6999.868 | -87.1 | 49.0 | imd·1·f1+1·f2 |
| 23000.132 | -87.2 | 50.8 | imd·-1·f1+4·f2 |
| 18000.000 | -87.2 | 51.0 | fs8·3 |
| 18999.868 | -87.3 | 50.4 | imd·1·f1+3·f2 |
| 11000.132 | -87.3 | 50.0 | imd·-1·f1+2·f2 |
| 21997.089 | -86.7 | 51.0 | usb1k·22 |
| 12999.868 | -87.4 | 49.5 | imd·1·f1+2·f2 |
| 17000.132 | -87.4 | 50.1 | imd·-1·f1+3·f2 |
| 20997.221 | -87.0 | 51.1 | usb1k·21 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | -0.02 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.18 | -0.25 | 0.03 |
| led | Kanal 1 | 11/11 | 1.69 | -0.44 | 0.27 |
| mains50 | Kanal 1 | 11/11 | 1005.00 | 122.02 | 0.95 |
| other1 | Kanal 1 | 11/11 | 0.57 | 0.01 | 0.06 |
| other2 | Kanal 1 | 11/11 | 0.17 | -0.13 | 0.21 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.18 | -0.24 | 0.03 |
| led | Kanal 2 | 11/11 | 0.31 | -0.04 | 0.25 |
| mains50 | Kanal 2 | 11/11 | 739.80 | 115.58 | 0.62 |
| other1 | Kanal 2 | 11/11 | 0.60 | -0.06 | 0.06 |
| other2 | Kanal 2 | 11/11 | 0.21 | -0.06 | 0.19 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.05 | -0.05 | 0.01 |
| led | Kanal 3 | 11/11 | 0.84 | 0.20 | 0.24 |
| mains50 | Kanal 3 | 11/11 | 855.23 | 1093.67 | 0.33 |
| other1 | Kanal 3 | 11/11 | 0.37 | -0.03 | 0.05 |
| other2 | Kanal 3 | 11/11 | 0.13 | -0.12 | 0.13 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.12 | -0.15 | 0.04 |
| led | Kanal 4 | 11/11 | 0.74 | -0.33 | 0.29 |
| mains50 | Kanal 4 | 11/11 | 704.46 | -105.13 | 0.47 |
| other1 | Kanal 4 | 11/11 | 0.04 | 0.05 | 0.10 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.08 | 0.31 s (3.18 Hz) | 26.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 37.1 |
| Kanal 2 | breitbandig | 0.98 | 0.31 s (3.18 Hz) | 27.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.7 |
| Kanal 3 | breitbandig | 0.67 | 0.31 s (3.18 Hz) | 29.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.7 |
| Kanal 4 | breitbandig | 0.80 | 0.16 s (6.40 Hz) | 26.4 |
| Kanal 4 | 999.9 Hz ± 10 | 1.23 | 1.25 s (0.80 Hz) | 43.7 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.86 |
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.87 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.83 |
| Kanal 4 | 0.86 | 0.87 | 0.83 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -70.4 | -71.1 | +0.7 | 76 % | 68 % |
| Kanal 2 | -70.9 | -71.9 | +0.9 | 80 % | 73 % |
| Kanal 3 | -72.1 | -73.1 | +1.1 | 88 % | 82 % |
| Kanal 4 | -70.5 | -71.0 | +0.5 | 79 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-noD-r2_psd.png)

### Kammprofile

![Kammprofile](B4y-noD-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-noD-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:25:13. Stream-Meldungen: 0. owl_read: reports/owl_read/B4y-noD-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
