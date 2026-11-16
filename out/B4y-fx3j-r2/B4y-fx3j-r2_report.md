# Report B4y-fx3j-r2: B4y-fx3j-r2 – acdc1 fx3j-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4y v22.4.r-fx3j (ITCM ohne USB + RX-Warten) |
| test | Build-4y-Sitzung: fx3j gegen 3d-Kontrolle, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3j-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-fx3j-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -68.0 | -78.0 | -68.4 | -69.7 | -86.3 | -68.7 | -94.8 | -68.5 | 85 % | -76.6 | 8.2 |
| Kanal 2 | -7.5 | -68.4 | -79.2 | -68.8 | -70.1 | -88.3 | -69.0 | -95.0 | -68.8 | 88 % | -78.0 | 9.1 |
| Kanal 3 | -5.7 | -69.4 | -82.1 | -69.7 | -71.0 | -92.6 | -69.9 | -95.9 | -69.7 | 93 % | -81.2 | 11.5 |
| Kanal 4 | -6.5 | -68.3 | -80.3 | -68.5 | -69.6 | -88.6 | -68.7 | -95.3 | -68.6 | 88 % | -77.6 | 9.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.2 dB | -72.9 | 35.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -71.6 | 48.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0011 | 10/10 | k=1: 2320.543 Hz, -112.4 dB | -108.5 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0000 | 0.0032 | 3/19 | k=1: 50.003 Hz, -98.0 dB | -98.5 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0012 | 128 | k=15·f1+1·f2: 20998.014 Hz, -105.5 dB | -94.8 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.9 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0004 | 4/7 | k=1: 3000.001 Hz, -98.4 dB | -99.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.3 dB | -73.0 | 38.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.6 dB | -71.9 | 49.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.543 Hz, -112.9 dB | -107.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9937 | 0.0085 | 5/19 | k=1: 50.003 Hz, -98.8 dB | -100.4 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0019 | 140 | k=15·f1+1·f2: 20998.014 Hz, -105.7 dB | -94.7 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.3 dB | -97.0 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0004 | 4/7 | k=1: 3000.001 Hz, -98.9 dB | -99.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.7 dB | -73.5 | 42.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.6 dB | -72.7 | 50.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -112.9 dB | -108.9 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9936 | 0.0093 | 5/19 | k=1: 50.003 Hz, -99.4 dB | -101.2 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0015 | 152 | k=15·f1+1·f2: 20998.014 Hz, -106.5 dB | -95.2 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.8 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -100.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.5 dB | -73.2 | 34.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -71.3 | 53.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0010 | 10/10 | k=1: 2320.544 Hz, -112.2 dB | -107.9 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9937 | 0.0090 | 5/19 | k=1: 50.003 Hz, -99.3 dB | -100.8 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0025 | 137 | k=15·f1+1·f2: 20998.014 Hz, -106.0 dB | -94.8 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -97.3 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0005 | 4/7 | k=1: 3000.001 Hz, -99.2 dB | -99.7 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -73.2 | 62.3 | fs8·1 |
| 999.868 | -73.8 | 57.4 | usb1k·1 |
| 12000.000 | -75.1 | 62.5 | fs8·2 |
| 18000.000 | -76.3 | 61.6 | fs8·3 |
| 2999.603 | -77.1 | 56.7 | usb1k·3 |
| 1999.735 | -77.7 | 55.5 | usb1k·2 |
| 6999.074 | -78.3 | 57.8 | usb1k·7 |
| 14998.014 | -81.6 | 56.0 | usb1k·15 |
| 9998.676 | -81.5 | 55.2 | usb1k·10 |
| 4999.338 | -82.3 | 52.7 | usb1k·5 |
| 13998.147 | -84.0 | 53.4 | usb1k·14 |
| 21997.088 | -84.4 | 53.1 | usb1k·22 |
| 11998.411 | -85.2 | 52.5 | usb1k·12 |
| 7998.941 | -84.4 | 51.8 | usb1k·8 |
| 19997.353 | -85.8 | 52.4 | usb1k·20 |
| 20997.221 | -86.6 | 48.5 | usb1k·21 |
| 16997.750 | -87.2 | 51.2 | usb1k·17 |
| 18997.485 | -87.1 | 50.7 | usb1k·19 |
| 5999.206 | -88.8 | 46.6 | usb1k·6 |
| 8998.809 | -88.8 | 48.3 | usb1k·9 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -73.3 | 63.7 | fs8·1 |
| 999.868 | -74.6 | 58.1 | usb1k·1 |
| 12000.000 | -75.2 | 63.4 | fs8·2 |
| 18000.000 | -76.3 | 62.4 | fs8·3 |
| 2999.603 | -77.4 | 57.9 | usb1k·3 |
| 1999.735 | -78.4 | 56.2 | usb1k·2 |
| 6999.074 | -78.5 | 58.8 | usb1k·7 |
| 14998.014 | -81.6 | 57.1 | usb1k·15 |
| 4999.338 | -81.8 | 54.4 | usb1k·5 |
| 9998.676 | -81.5 | 56.6 | usb1k·10 |
| 13998.147 | -84.1 | 54.6 | usb1k·14 |
| 21997.088 | -84.5 | 54.5 | usb1k·22 |
| 11998.411 | -85.0 | 53.6 | usb1k·12 |
| 7998.941 | -84.2 | 53.5 | usb1k·8 |
| 19997.353 | -85.7 | 53.2 | usb1k·20 |
| 20997.221 | -86.8 | 50.3 | usb1k·21 |
| 18997.485 | -87.1 | 51.6 | usb1k·19 |
| 16997.750 | -87.2 | 52.1 | usb1k·17 |
| 5999.206 | -89.5 | 47.5 | usb1k·6 |
| 8998.809 | -89.1 | 49.4 | usb1k·9 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -73.7 | 67.0 | fs8·1 |
| 999.868 | -75.6 | 62.2 | usb1k·1 |
| 12000.000 | -75.8 | 66.2 | fs8·2 |
| 18000.000 | -76.8 | 65.2 | fs8·3 |
| 2999.603 | -78.1 | 61.9 | usb1k·3 |
| 1999.735 | -79.5 | 59.7 | usb1k·2 |
| 6999.074 | -79.1 | 62.3 | usb1k·7 |
| 14998.014 | -82.0 | 59.2 | usb1k·15 |
| 4999.338 | -82.2 | 58.6 | usb1k·5 |
| 9998.676 | -81.9 | 59.5 | usb1k·10 |
| 13998.147 | -84.8 | 57.0 | usb1k·14 |
| 21997.088 | -85.0 | 56.2 | usb1k·22 |
| 11998.411 | -85.4 | 56.5 | usb1k·12 |
| 7998.941 | -84.5 | 56.7 | usb1k·8 |
| 19997.353 | -86.1 | 55.2 | usb1k·20 |
| 16997.750 | -87.5 | 54.2 | usb1k·17 |
| 18997.485 | -87.7 | 53.6 | usb1k·19 |
| 20997.221 | -87.5 | 52.3 | usb1k·21 |
| 17997.618 | -91.2 | 50.8 | usb1k·18 |
| 5999.206 | -90.7 | 49.9 | usb1k·6 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 59.4 | usb1k·1 |
| 6000.000 | -73.5 | 62.5 | fs8·1 |
| 12000.000 | -75.4 | 62.4 | fs8·2 |
| 18000.000 | -76.5 | 61.7 | fs8·3 |
| 1999.735 | -76.9 | 57.4 | usb1k·2 |
| 2999.603 | -77.0 | 57.6 | usb1k·3 |
| 6999.074 | -78.3 | 58.6 | usb1k·7 |
| 14998.014 | -81.9 | 56.1 | usb1k·15 |
| 9998.676 | -81.7 | 55.3 | usb1k·10 |
| 4999.338 | -83.2 | 52.2 | usb1k·5 |
| 13998.147 | -83.8 | 54.0 | usb1k·14 |
| 21997.088 | -84.6 | 53.7 | usb1k·22 |
| 11998.411 | -85.7 | 52.0 | usb1k·12 |
| 19997.353 | -86.3 | 51.8 | usb1k·20 |
| 7998.941 | -85.0 | 52.1 | usb1k·8 |
| 20997.221 | -86.5 | 50.6 | usb1k·21 |
| 16997.750 | -87.5 | 50.6 | usb1k·17 |
| 18997.485 | -87.4 | 50.6 | usb1k·19 |
| 5999.206 | -87.8 | 48.2 | usb1k·6 |
| 8998.809 | -88.1 | 49.5 | usb1k·9 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.10 | -0.02 | 0.04 |
| led | Kanal 1 | 11/11 | 1.17 | 1.57 | 0.28 |
| mains50 | Kanal 1 | 11/11 | 39.72 | -44.40 | 0.59 |
| other1 | Kanal 1 | 11/11 | 0.44 | -0.87 | 0.09 |
| other2 | Kanal 1 | 11/11 | 0.15 | -0.11 | 0.12 |
| fs8 | Kanal 2 | 11/11 | 0.00 | -0.00 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.10 | -0.01 | 0.03 |
| led | Kanal 2 | 11/11 | 0.40 | -0.14 | 0.22 |
| mains50 | Kanal 2 | 11/11 | 44.51 | -68.17 | 0.53 |
| other1 | Kanal 2 | 11/11 | 0.52 | -0.76 | 0.08 |
| other2 | Kanal 2 | 11/11 | 0.14 | -0.12 | 0.11 |
| fs8 | Kanal 3 | 11/11 | 0.00 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.03 | 0.02 | 0.04 |
| led | Kanal 3 | 11/11 | 1.16 | 0.13 | 0.33 |
| mains50 | Kanal 3 | 11/11 | 17.49 | -36.27 | 0.34 |
| other1 | Kanal 3 | 11/11 | 0.33 | -0.53 | 0.07 |
| other2 | Kanal 3 | 11/11 | 0.10 | -0.06 | 0.09 |
| fs8 | Kanal 4 | 11/11 | 0.00 | -0.01 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.07 | -0.06 | 0.04 |
| led | Kanal 4 | 11/11 | 1.05 | 1.35 | 0.31 |
| mains50 | Kanal 4 | 11/11 | 33.33 | -25.79 | 0.54 |
| other1 | Kanal 4 | 11/11 | 0.58 | -0.81 | 0.10 |
| other2 | Kanal 4 | 11/11 | 0.10 | -0.09 | 0.11 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.61 | 0.31 s (3.18 Hz) | 26.5 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.0 |
| Kanal 2 | breitbandig | 0.54 | 1.25 s (0.80 Hz) | 28.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 38.9 |
| Kanal 3 | breitbandig | 0.40 | 0.63 s (1.58 Hz) | 35.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 43.7 |
| Kanal 4 | breitbandig | 0.45 | 1.25 s (0.80 Hz) | 30.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 38.2 |

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
| Kanal 1 | 1.00 | 0.98 | 0.96 | 0.97 |
| Kanal 2 | 0.98 | 1.00 | 0.97 | 0.98 |
| Kanal 3 | 0.96 | 0.97 | 1.00 | 0.96 |
| Kanal 4 | 0.97 | 0.98 | 0.96 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -68.4 | -71.1 | +2.7 | 85 % | 68 % |
| Kanal 2 | -68.8 | -71.9 | +3.0 | 88 % | 73 % |
| Kanal 3 | -69.7 | -73.1 | +3.4 | 93 % | 82 % |
| Kanal 4 | -68.5 | -71.0 | +2.4 | 88 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-fx3j-r2_psd.png)

### Kammprofile

![Kammprofile](B4y-fx3j-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-fx3j-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:18:41. Stream-Meldungen: 0. owl_read: out/owl_read/B4y-fx3j-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
