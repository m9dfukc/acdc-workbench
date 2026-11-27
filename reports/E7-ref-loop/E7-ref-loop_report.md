# Report E7-ref-loop: E7-ref-loop – acdc1 alte Firmware, Rückführung Out → In, 4 Sinustöne, Gain 12 Uhr, 10 min

| Feld | Wert |
|---|---|
| date | 2026-11-14 |
| device | acdc1, Firmware wie Readback 20261114 (meldet v22.5.0, enthält 237c63d), nach Generalprobe D5 |
| test | Referenz für Sample-Slips vor Build 1 (E7/A6): Kabel Out n → In n, Host-Playback Sinus 440/530/670/790 Hz auf Out 1…4 |
| gain | g12 |
| usb | usb-rxtx, Thunderbolt-Hub, Host-Software 48 kHz |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261114_acdc1_ref-loop-10min_g12_usb-rxtx.4chan.000.wav` |
| Format | 48000 Hz, 600.4 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis E7-ref-loop --ref E7-ref --no-spectrogram` |

**Hinweise:**

- Clipping: Samples an der Vollaussteuerung.
- Ein Nutzsignal (übrige Linien) dominiert. Störanteil und Notch-Gewinn sind dann nicht aussagekräftig, Störlinien in absoluten dBFS vergleichen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | -6.5 | -3.1 | – | -3.1 | -7.2 | -82.1 | -3.1 | -3.1 | -43.9 | 1 % | -43.9 | 0.1 |
| In 2 ← Out 2 (530 Hz) | -6.0 | -4.1 | – | -4.1 | -7.0 | -84.4 | -4.1 | -4.1 | -41.9 | 1 % | -41.9 | 0.0 |
| In 3 ← Out 3 (670 Hz) | -4.4 | -3.9 | – | -3.9 | -5.5 | -85.6 | -3.9 | -3.9 | -43.4 | 1 % | -43.5 | 0.0 |
| In 4 ← Out 4 (790 Hz) | -5.2 | -4.5 | – | -4.5 | -5.3 | -84.1 | -4.5 | -4.5 | -41.7 | 1 % | -41.7 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | In 1 ← Out 1 (440 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.7 dB | -77.6 | 0.0 % |
| 1-kHz-Kamm | In 1 ← Out 1 (440 Hz) | 999.8677 | 0.0000 | 23/23 | k=1: 999.868 Hz, -72.0 dB | -73.6 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 1 ← Out 1 (440 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -64.3 dB | -63.4 | 1.1 % |
| Netz 50 Hz | In 1 ← Out 1 (440 Hz) | 50.0413 | 0.0009 | 2/19 | k=1: 50.041 Hz, -95.2 dB | -95.2 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | In 1 ← Out 1 (440 Hz) | 999.8677 | 0.0001 | 178 | k=15·f1+1·f2: 20998.016 Hz, -100.3 dB | -90.7 | 0.0 % |
| stärkste übrige Linie (440.00 Hz) | In 1 ← Out 1 (440 Hz) | 439.9998 | 0.0000 | 54/54 | k=1: 440.000 Hz, -0.1 dB | -3.1 | 100.0 % |
| stärkste übrige Linie (515.72 Hz) | In 1 ← Out 1 (440 Hz) | 515.7208 | 0.0000 | 1/46 | k=1: 515.721 Hz, -72.7 dB | -75.7 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 2 ← Out 2 (530 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -77.9 | 0.0 % |
| 1-kHz-Kamm | In 2 ← Out 2 (530 Hz) | 999.8677 | 0.0000 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.8 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 2 ← Out 2 (530 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -65.9 dB | -65.1 | 0.5 % |
| Netz 50 Hz | In 2 ← Out 2 (530 Hz) | 50.0407 | 0.0024 | 3/19 | k=1: 50.041 Hz, -96.3 dB | -96.2 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | In 2 ← Out 2 (530 Hz) | 999.8677 | 0.0001 | 177 | k=15·f1+1·f2: 20998.016 Hz, -101.0 dB | -91.3 | 0.0 % |
| stärkste übrige Linie (530.00 Hz) | In 2 ← Out 2 (530 Hz) | 530.0017 | 0.0001 | 45/45 | k=1: 530.002 Hz, -0.8 dB | -4.1 | 100.0 % |
| stärkste übrige Linie (605.72 Hz) | In 2 ← Out 2 (530 Hz) | 605.7227 | 0.0000 | 1/39 | k=1: 605.723 Hz, -73.8 dB | -77.0 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 3 ← Out 3 (670 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -77.9 | 0.0 % |
| 1-kHz-Kamm | In 3 ← Out 3 (670 Hz) | 999.8677 | 0.0000 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -76.0 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 3 ← Out 3 (670 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -65.9 dB | -65.1 | 0.7 % |
| Netz 50 Hz | In 3 ← Out 3 (670 Hz) | 50.0406 | 0.0041 | 4/19 | k=1: 50.041 Hz, -96.6 dB | -96.6 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | In 3 ← Out 3 (670 Hz) | 999.8677 | 0.0000 | 172 | k=15·f1+1·f2: 20998.016 Hz, -100.8 dB | -91.2 | 0.0 % |
| stärkste übrige Linie (670.00 Hz) | In 3 ← Out 3 (670 Hz) | 670.0003 | 0.0000 | 35/35 | k=1: 670.000 Hz, -0.9 dB | -3.9 | 100.0 % |
| stärkste übrige Linie (745.72 Hz) | In 3 ← Out 3 (670 Hz) | 745.7214 | 0.0000 | 1/32 | k=1: 745.721 Hz, -74.3 dB | -77.3 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 4 ← Out 4 (790 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.6 dB | -78.4 | 0.0 % |
| 1-kHz-Kamm | In 4 ← Out 4 (790 Hz) | 999.8677 | 0.0000 | 23/23 | k=1: 999.868 Hz, -72.5 dB | -74.1 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 4 ← Out 4 (790 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -66.1 dB | -65.3 | 0.4 % |
| Netz 50 Hz | In 4 ← Out 4 (790 Hz) | 50.0404 | 0.0040 | 3/19 | k=1: 50.041 Hz, -97.2 dB | -97.1 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | In 4 ← Out 4 (790 Hz) | 999.8677 | 0.0001 | 172 | k=15·f1+1·f2: 20998.016 Hz, -101.5 dB | -91.8 | 0.0 % |
| stärkste übrige Linie (790.00 Hz) | In 4 ← Out 4 (790 Hz) | 789.9977 | 0.0000 | 30/30 | k=1: 789.998 Hz, -1.4 dB | -4.5 | 100.0 % |
| stärkste übrige Linie (714.28 Hz) | In 4 ← Out 4 (790 Hz) | 714.2766 | 0.0000 | 1/33 | k=1: 714.277 Hz, -76.5 dB | -79.6 | 0.0 % |

## Stärkste Linien (Kanal für Kanal)

### In 1 ← Out 1 (440 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 440.000 | -0.1 | 109.3 | other1·1 |
| 1319.999 | -28.5 | 107.1 | other1·3 |
| 2199.999 | -41.7 | 104.4 | other1·5 |
| 3079.998 | -50.8 | 96.6 | other1·7 |
| 3959.998 | -57.4 | 90.0 | other1·9 |
| 879.999 | -58.6 | 84.9 | other1·2 |
| 4839.997 | -62.7 | 84.0 | other1·11 |
| 2320.545 | -64.3 | 82.9 | led·1 |
| 4641.090 | -65.5 | 82.2 | led·2 |
| 5719.997 | -66.9 | 80.3 | other1·13 |
| 6961.634 | -68.1 | 79.7 | led·3 |
| 9282.179 | -71.5 | 76.6 | led·4 |
| 6599.996 | -70.6 | 76.8 | other1·15 |
| 515.721 | -72.7 | 53.4 | other2·1 |
| 364.279 | -72.7 | 53.6 | – |
| 999.868 | -72.0 | 73.0 | usb1k·1 |
| 7479.996 | -74.2 | 73.7 | other1·17 |
| 11602.724 | -75.2 | 73.0 | led·5 |
| 8359.995 | -77.2 | 71.0 | other1·19 |
| 6000.000 | -77.7 | 69.6 | fs8·1 |

### In 2 ← Out 2 (530 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 530.002 | -0.8 | 109.6 | other1·1 |
| 1590.005 | -29.4 | 109.1 | other1·3 |
| 2650.009 | -42.8 | 105.2 | other1·5 |
| 3710.012 | -51.7 | 98.1 | other1·7 |
| 4770.015 | -58.3 | 91.2 | other1·9 |
| 1060.003 | -61.5 | 85.5 | other1·2 |
| 5830.019 | -63.6 | 86.4 | other1·11 |
| 2320.545 | -65.9 | 84.2 | led·1 |
| 4641.090 | -67.1 | 83.2 | led·2 |
| 6890.022 | -68.0 | 82.3 | other1·13 |
| 6961.634 | -69.9 | 80.4 | led·3 |
| 7950.026 | -71.9 | 78.9 | other1·15 |
| 9282.179 | -73.5 | 77.3 | led·4 |
| 999.868 | -73.2 | 72.8 | usb1k·1 |
| 605.723 | -73.8 | 53.4 | other2·1 |
| 454.281 | -73.8 | 53.4 | – |
| 9010.029 | -75.3 | 75.6 | other1·17 |
| 11602.724 | -77.1 | 73.6 | led·5 |
| 6000.000 | -78.1 | 71.8 | fs8·1 |
| 10070.033 | -78.3 | 71.9 | other1·19 |

### In 3 ← Out 3 (670 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 670.000 | -0.9 | 109.4 | other1·1 |
| 2010.001 | -29.4 | 109.3 | other1·3 |
| 3350.001 | -42.6 | 106.7 | other1·5 |
| 4690.002 | -51.6 | 100.3 | other1·7 |
| 6030.003 | -58.4 | 94.3 | other1·9 |
| 7370.003 | -63.7 | 89.4 | other1·11 |
| 2320.545 | -65.9 | 86.3 | led·1 |
| 1340.001 | -67.2 | 79.0 | other1·2 |
| 4641.090 | -67.0 | 85.7 | led·2 |
| 8710.004 | -68.0 | 85.2 | other1·13 |
| 6961.634 | -69.7 | 83.1 | led·3 |
| 9282.179 | -73.3 | 80.0 | led·4 |
| 10050.004 | -71.7 | 81.1 | other1·15 |
| 745.721 | -74.3 | 53.0 | other2·1 |
| 594.279 | -74.2 | 53.1 | – |
| 999.868 | -74.4 | 68.1 | usb1k·1 |
| 11390.005 | -75.4 | 77.7 | other1·17 |
| 11602.724 | -77.3 | 75.8 | led·5 |
| 6000.000 | -78.1 | 74.5 | fs8·1 |
| 12730.006 | -78.5 | 74.6 | other1·19 |

### In 4 ← Out 4 (790 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 789.998 | -1.4 | 105.8 | other1·1 |
| 2369.993 | -30.0 | 105.6 | other1·3 |
| 3949.988 | -43.4 | 102.8 | other1·5 |
| 5529.984 | -52.2 | 96.1 | other1·7 |
| 7109.979 | -59.0 | 90.5 | other1·9 |
| 1579.995 | -62.7 | 84.8 | other1·2 |
| 8689.974 | -64.1 | 86.1 | other1·11 |
| 2320.545 | -66.1 | 80.1 | led·1 |
| 4641.090 | -67.2 | 82.5 | led·2 |
| 10269.970 | -68.8 | 80.9 | other1·13 |
| 6961.634 | -70.1 | 79.5 | led·3 |
| 11849.965 | -72.5 | 77.8 | other1·15 |
| 9282.179 | -73.7 | 76.5 | led·4 |
| 999.868 | -72.5 | 62.1 | usb1k·1 |
| 13429.960 | -76.2 | 73.9 | other1·17 |
| 714.277 | -76.5 | 47.7 | other2·1 |
| 865.719 | -76.3 | 47.9 | – |
| 11602.724 | -77.7 | 72.5 | led·5 |
| 6000.000 | -78.6 | 70.7 | fs8·1 |
| 700.482 | -79.3 | 46.4 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | In 1 ← Out 1 (440 Hz) | 119/119 | 0.01 | 0.00 | 0.04 |
| usb1k | In 1 ← Out 1 (440 Hz) | 119/119 | 0.11 | -0.00 | 0.04 |
| led | In 1 ← Out 1 (440 Hz) | 119/119 | 0.01 | 0.00 | 0.02 |
| mains50 | In 1 ← Out 1 (440 Hz) | 119/119 | 308.43 | -58.88 | 0.28 |
| other1 | In 1 ← Out 1 (440 Hz) | 119/119 | 0.00 | 0.00 | 0.00 |
| other2 | In 1 ← Out 1 (440 Hz) | 119/119 | 2.74 | -0.02 | 0.15 |
| fs8 | In 2 ← Out 2 (530 Hz) | 119/119 | 0.01 | 0.00 | 0.03 |
| usb1k | In 2 ← Out 2 (530 Hz) | 119/119 | 0.08 | -0.00 | 0.04 |
| led | In 2 ← Out 2 (530 Hz) | 119/119 | 0.01 | 0.00 | 0.02 |
| mains50 | In 2 ← Out 2 (530 Hz) | 119/119 | 55.82 | -3.46 | 0.32 |
| other1 | In 2 ← Out 2 (530 Hz) | 119/119 | 0.00 | 0.00 | 0.00 |
| other2 | In 2 ← Out 2 (530 Hz) | 119/119 | 2.20 | 0.04 | 0.14 |
| fs8 | In 3 ← Out 3 (670 Hz) | 119/119 | 0.01 | -0.00 | 0.03 |
| usb1k | In 3 ← Out 3 (670 Hz) | 119/119 | 0.13 | -0.00 | 0.04 |
| led | In 3 ← Out 3 (670 Hz) | 119/119 | 0.00 | 0.00 | 0.02 |
| mains50 | In 3 ← Out 3 (670 Hz) | 119/119 | 421.06 | -56.43 | 0.25 |
| other1 | In 3 ← Out 3 (670 Hz) | 119/119 | 0.00 | -0.00 | 0.00 |
| other2 | In 3 ← Out 3 (670 Hz) | 119/119 | 1.91 | 0.02 | 0.16 |
| fs8 | In 4 ← Out 4 (790 Hz) | 119/119 | 0.01 | 0.00 | 0.03 |
| usb1k | In 4 ← Out 4 (790 Hz) | 119/119 | 0.08 | -0.00 | 0.05 |
| led | In 4 ← Out 4 (790 Hz) | 119/119 | 0.01 | 0.00 | 0.02 |
| mains50 | In 4 ← Out 4 (790 Hz) | 119/119 | 343.80 | -52.43 | 0.33 |
| other1 | In 4 ← Out 4 (790 Hz) | 119/119 | 0.00 | -0.00 | 0.00 |
| other2 | In 4 ← Out 4 (790 Hz) | 119/119 | 3.55 | -0.04 | 0.27 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | breitbandig | 0.06 | 0.05 s (20.00 Hz) | 64.1 |
| In 1 ← Out 1 (440 Hz) | 440.0 Hz ± 10 | 0.20 | 0.05 s (20.00 Hz) | 73.5 |
| In 2 ← Out 2 (530 Hz) | breitbandig | 0.08 | 0.14 s (6.90 Hz) | 28.0 |
| In 2 ← Out 2 (530 Hz) | 530.0 Hz ± 10 | 0.21 | 0.14 s (6.90 Hz) | 36.1 |
| In 3 ← Out 3 (670 Hz) | breitbandig | 0.06 | 0.05 s (20.00 Hz) | 32.5 |
| In 3 ← Out 3 (670 Hz) | 670.0 Hz ± 10 | 0.21 | 0.14 s (6.90 Hz) | 34.0 |
| In 4 ← Out 4 (790 Hz) | breitbandig | 0.03 | 0.07 s (13.79 Hz) | 29.0 |
| In 4 ← Out 4 (790 Hz) | 790.0 Hz ± 10 | 0.19 | 0.14 s (6.90 Hz) | 36.2 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | 0 | 0.0 | – | – |
| In 2 ← Out 2 (530 Hz) | 0 | 0.0 | – | – |
| In 3 ← Out 3 (670 Hz) | 0 | 0.0 | – | – |
| In 4 ← Out 4 (790 Hz) | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | In 1 ← Out 1 (440 Hz) | In 2 ← Out 2 (530 Hz) | In 3 ← Out 3 (670 Hz) | In 4 ← Out 4 (790 Hz) |
|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | 1.00 | 0.00 | 0.00 | 0.00 |
| In 2 ← Out 2 (530 Hz) | 0.00 | 1.00 | 0.00 | 0.00 |
| In 3 ← Out 3 (670 Hz) | 0.00 | 0.00 | 1.00 | 0.00 |
| In 4 ← Out 4 (790 Hz) | 0.00 | 0.00 | 0.00 | 1.00 |

## Vergleich mit Referenz E7-ref

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | -3.1 | -65.0 | +61.9 | 1 % | 87 % |
| In 2 ← Out 2 (530 Hz) | -4.1 | -69.9 | +65.7 | 1 % | 88 % |
| In 3 ← Out 3 (670 Hz) | -3.9 | -68.6 | +64.6 | 1 % | 93 % |
| In 4 ← Out 4 (790 Hz) | -4.5 | -70.9 | +66.4 | 1 % | 87 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](E7-ref-loop_psd.png)

### Kammprofile

![Kammprofile](E7-ref-loop_combs.png)

### Zeitverlauf

![Zeitverlauf](E7-ref-loop_timeline.png)

## Notiz aus dem Manifest

> Aufgenommen in der Host-Software, 48 kHz / 32 Bit float. In der Host-Software kein Eingang auf einen Ausgang. Playback-Pegel nicht notiert. Pegel in der Datei sehr hoch: In 1 übersteuert (≈ 2,1 Mio. Samples ≥ 0,999), In 2–4 Spitze −0,7…−1,2 dBFS.
