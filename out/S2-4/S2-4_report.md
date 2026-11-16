# Report S2-4: S2-4 – acdc1, Eingänge offen, Gain 12 Uhr, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc1, Firmware v22.5.0 |
| test | Eingänge offen (nichts gesteckt) |
| gain | g12 |
| usb | usb-stream |
| patch | Slot 1: ACDC (9,93 KB, Default-Patch) – laut Device-Status vom 2026-11-13 |
| Datei(en) | `20261114_acdc1_open-inputs_g12_usb-stream.4chan.000.wav` |
| Format | 96000 Hz, 120.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis S2-4 --ref S2-1` |

**Hinweise:**

- Datei hat 96000 Hz, oberhalb 24000 Hz ist nichts drin (-169 dB) → von 48000 Hz hochgerechnet.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.9 | -63.1 | -64.2 | -69.7 | -70.9 | -81.5 | -70.1 | -89.9 | -69.8 | 60 % | -73.8 | 4.0 |
| Kanal 2 | -5.5 | -68.6 | -70.6 | -73.1 | -74.2 | -85.4 | -73.4 | -93.1 | -73.1 | 67 % | -78.0 | 4.9 |
| Kanal 3 | -4.7 | -67.7 | -69.0 | -73.7 | -74.9 | -87.9 | -73.9 | -95.8 | -73.7 | 81 % | -80.8 | 7.1 |
| Kanal 4 | -4.5 | -69.6 | -72.1 | -73.2 | -74.1 | -86.3 | -73.5 | -96.4 | -73.2 | 67 % | -78.0 | 4.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -77.0 dB | -76.6 | 20.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8663 | 0.0003 | 23/23 | k=1: 999.866 Hz, -72.4 dB | -74.0 | 37.9 % |
| Netz 50 Hz | Kanal 1 | 50.0248 | 0.0001 | 2/19 | k=1: 50.025 Hz, -88.8 dB | -91.5 | 0.7 % |
| Mischprodukte n·999.8663 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8663 | 0.0008 | 141 | k=7·f1+2·f2: 18999.064 Hz, -99.3 dB | -89.7 | 1.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7212 | 0.0002 | 2/315 | k=1: 75.721 Hz, -87.5 dB | -90.6 | 0.8 % |
| stärkste übrige Linie (13.79 Hz) | Kanal 1 | 13.7931 | 0.0008 | 17/1731 | k=1: 13.794 Hz, -97.9 dB | -98.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.7 dB | -79.3 | 24.1 % |
| 1-kHz-Kamm | Kanal 2 | 999.8663 | 0.0003 | 23/23 | k=1: 999.866 Hz, -75.4 dB | -77.0 | 41.5 % |
| Netz 50 Hz | Kanal 2 | 50.0248 | 0.0001 | 2/19 | k=1: 50.025 Hz, -92.5 dB | -95.1 | 0.6 % |
| Mischprodukte n·999.8663 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8663 | 0.0006 | 148 | k=7·f1+2·f2: 18999.064 Hz, -102.1 dB | -92.5 | 1.2 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7193 | 0.0011 | 2/315 | k=1: 75.721 Hz, -90.4 dB | -93.5 | 0.9 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 2 | 89.5173 | 0.0013 | 2/266 | k=1: 89.515 Hz, -99.8 dB | -102.9 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.0 | 37.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8663 | 0.0003 | 23/23 | k=1: 999.866 Hz, -76.2 dB | -77.6 | 40.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0005 | 10/10 | k=1: 2320.545 Hz, -124.5 dB | -120.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0264 | 0.0046 | 3/19 | k=1: 50.025 Hz, -91.7 dB | -94.1 | 0.9 % |
| Mischprodukte n·999.8663 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8663 | 0.0007 | 161 | k=7·f1+2·f2: 18999.064 Hz, -100.7 dB | -91.1 | 1.8 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7200 | 0.0006 | 2/315 | k=1: 75.721 Hz, -93.4 dB | -96.5 | 0.5 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 3 | 89.5151 | 0.0007 | 3/266 | k=1: 89.515 Hz, -101.3 dB | -104.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.6 dB | -80.1 | 20.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8663 | 0.0004 | 23/23 | k=1: 999.866 Hz, -75.2 dB | -76.6 | 45.1 % |
| Netz 50 Hz | Kanal 4 | 50.0247 | 0.0000 | 2/19 | k=1: 50.025 Hz, -93.7 dB | -96.2 | 0.5 % |
| Mischprodukte n·999.8663 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8663 | 0.0006 | 140 | k=7·f1+2·f2: 18999.064 Hz, -102.8 dB | -93.3 | 1.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7206 | 0.0002 | 2/315 | k=1: 75.721 Hz, -94.9 dB | -98.0 | 0.3 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 4 | 89.5174 | 0.0014 | 2/266 | k=1: 89.515 Hz, -98.4 dB | -101.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -72.4 | 58.6 | usb1k·1 |
| 6000.000 | -77.0 | 58.3 | fs8·1 |
| 12000.000 | -79.2 | 58.1 | fs8·2 |
| 18000.000 | -79.3 | 58.7 | fs8·3 |
| 2999.599 | -81.4 | 52.1 | usb1k·3 |
| 1999.733 | -80.4 | 52.2 | usb1k·2 |
| 75.721 | -87.5 | 36.0 | other1·1 |
| 6999.064 | -87.8 | 48.0 | usb1k·7 |
| 50.025 | -88.8 | 32.1 | mains50·1 |
| 4999.332 | -90.0 | 44.8 | usb1k·5 |
| 9998.663 | -89.6 | 47.4 | usb1k·10 |
| 13998.128 | -91.2 | 46.2 | usb1k·14 |
| 3999.465 | -93.0 | 40.7 | usb1k·4 |
| 5999.198 | -91.7 | 43.5 | usb1k·6 |
| 16997.727 | -93.9 | 43.7 | usb1k·17 |
| 20997.192 | -94.0 | 44.6 | usb1k·21 |
| 15997.860 | -94.3 | 43.3 | usb1k·16 |
| 8998.797 | -94.2 | 42.1 | usb1k·9 |
| 21997.058 | -94.1 | 45.4 | usb1k·22 |
| 14997.994 | -95.5 | 41.9 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -75.4 | 59.6 | usb1k·1 |
| 6000.000 | -79.7 | 59.6 | fs8·1 |
| 12000.000 | -81.9 | 59.7 | fs8·2 |
| 18000.000 | -82.0 | 60.1 | fs8·3 |
| 2999.599 | -84.5 | 53.3 | usb1k·3 |
| 1999.733 | -83.3 | 53.1 | usb1k·2 |
| 75.721 | -90.4 | 37.7 | other1·1 |
| 6999.064 | -90.9 | 49.1 | usb1k·7 |
| 50.025 | -92.5 | 33.3 | mains50·1 |
| 4999.332 | -93.0 | 45.9 | usb1k·5 |
| 9998.663 | -92.6 | 48.3 | usb1k·10 |
| 13998.128 | -94.3 | 47.3 | usb1k·14 |
| 3999.465 | -96.2 | 41.7 | usb1k·4 |
| 5999.198 | -94.7 | 44.7 | usb1k·6 |
| 20997.192 | -96.9 | 46.1 | usb1k·21 |
| 16997.727 | -96.9 | 45.2 | usb1k·17 |
| 15997.861 | -97.2 | 44.8 | usb1k·16 |
| 8998.797 | -97.0 | 43.6 | usb1k·9 |
| 21997.058 | -97.0 | 46.6 | usb1k·22 |
| 14997.994 | -98.2 | 43.5 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -76.2 | 62.6 | usb1k·1 |
| 6000.000 | -78.5 | 63.8 | fs8·1 |
| 12000.000 | -80.3 | 63.7 | fs8·2 |
| 18000.000 | -80.6 | 63.7 | fs8·3 |
| 2999.599 | -84.6 | 56.2 | usb1k·3 |
| 1999.733 | -84.3 | 55.8 | usb1k·2 |
| 6999.064 | -90.4 | 52.4 | usb1k·7 |
| 50.025 | -91.7 | 36.6 | mains50·1 |
| 9998.663 | -92.3 | 51.3 | usb1k·10 |
| 75.721 | -93.4 | 37.8 | other1·1 |
| 13998.128 | -94.0 | 50.0 | usb1k·14 |
| 4999.332 | -95.2 | 46.6 | usb1k·5 |
| 20997.192 | -95.9 | 48.7 | usb1k·21 |
| 14997.994 | -96.2 | 47.9 | usb1k·15 |
| 16997.727 | -96.7 | 47.1 | usb1k·17 |
| 21997.058 | -96.0 | 49.2 | usb1k·22 |
| 5999.198 | -95.6 | 46.7 | usb1k·6 |
| 3999.465 | -97.4 | 43.9 | usb1k·4 |
| 15997.860 | -97.4 | 46.2 | usb1k·16 |
| 8998.797 | -97.2 | 46.1 | usb1k·9 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -75.2 | 60.1 | usb1k·1 |
| 6000.000 | -80.6 | 58.5 | fs8·1 |
| 12000.000 | -82.7 | 58.4 | fs8·2 |
| 18000.000 | -82.7 | 58.9 | fs8·3 |
| 1999.733 | -82.1 | 54.3 | usb1k·2 |
| 2999.599 | -84.7 | 53.1 | usb1k·3 |
| 6999.064 | -91.2 | 48.3 | usb1k·7 |
| 4999.332 | -91.4 | 47.2 | usb1k·5 |
| 9998.663 | -92.8 | 47.8 | usb1k·10 |
| 50.025 | -93.7 | 32.3 | mains50·1 |
| 5999.198 | -93.7 | 45.4 | usb1k·6 |
| 75.721 | -94.9 | 33.5 | other1·1 |
| 3999.465 | -95.6 | 42.5 | usb1k·4 |
| 13998.128 | -94.5 | 46.6 | usb1k·14 |
| 8998.797 | -96.0 | 44.1 | usb1k·9 |
| 15997.861 | -96.7 | 45.0 | usb1k·16 |
| 16997.727 | -97.1 | 44.3 | usb1k·17 |
| 20997.192 | -97.2 | 45.0 | usb1k·21 |
| 89.515 | -98.4 | 30.6 | other2·1 |
| 13.794 | -98.1 | 20.2 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.01 | 0.01 | 0.04 |
| usb1k | Kanal 1 | 23/23 | 0.28 | 0.37 | 0.06 |
| mains50 | Kanal 1 | 23/23 | 540.20 | 107.22 | 0.48 |
| other1 | Kanal 1 | 23/23 | 54.80 | 13.51 | 0.32 |
| other2 | Kanal 1 | 23/23 | 1.72 | 0.40 | 0.09 |
| fs8 | Kanal 2 | 23/23 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 2 | 23/23 | 0.27 | 0.38 | 0.06 |
| mains50 | Kanal 2 | 23/23 | 148.93 | -6.60 | 0.53 |
| other1 | Kanal 2 | 23/23 | 42.99 | -10.43 | 0.24 |
| other2 | Kanal 2 | 23/23 | 12.85 | 6.05 | 0.71 |
| fs8 | Kanal 3 | 23/23 | 0.01 | 0.00 | 0.03 |
| usb1k | Kanal 3 | 23/23 | 0.25 | 0.35 | 0.05 |
| led | Kanal 3 | 23/23 | 8.76 | -0.90 | 1.25 |
| mains50 | Kanal 3 | 23/23 | 234.87 | 44.42 | 0.38 |
| other1 | Kanal 3 | 23/23 | 37.53 | 8.36 | 0.25 |
| other2 | Kanal 3 | 23/23 | 21.14 | -4.60 | 0.99 |
| fs8 | Kanal 4 | 23/23 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 23/23 | 0.26 | 0.39 | 0.05 |
| mains50 | Kanal 4 | 23/23 | 159.72 | 2.12 | 0.71 |
| other1 | Kanal 4 | 23/23 | 53.69 | 28.29 | 0.46 |
| other2 | Kanal 4 | 23/23 | 30.24 | -5.67 | 0.48 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.50 | 0.31 s (3.18 Hz) | 34.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.62 | 7.52 s (0.13 Hz) | 29.6 |
| Kanal 2 | breitbandig | 2.72 | 0.31 s (3.18 Hz) | 34.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.61 | 7.52 s (0.13 Hz) | 30.8 |
| Kanal 3 | breitbandig | 3.29 | 0.31 s (3.18 Hz) | 34.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.58 | 7.52 s (0.13 Hz) | 36.4 |
| Kanal 4 | breitbandig | 2.36 | 0.31 s (3.20 Hz) | 32.7 |
| Kanal 4 | 999.9 Hz ± 10 | 0.59 | 7.52 s (0.13 Hz) | 27.8 |

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
| Kanal 1 | 1.00 | 0.96 | 0.98 | 0.93 |
| Kanal 2 | 0.96 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.98 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz S2-1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -69.7 | -72.0 | +2.3 | 60 % | 79 % |
| Kanal 2 | -73.1 | -69.2 | -3.9 | 67 % | 87 % |
| Kanal 3 | -73.7 | -69.3 | -4.4 | 81 % | 84 % |
| Kanal 4 | -73.2 | -69.9 | -3.3 | 67 % | 90 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S2-4_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S2-4_psd.png)

### Kammprofile

![Kammprofile](S2-4_combs.png)

### Zeitverlauf

![Zeitverlauf](S2-4_timeline.png)
