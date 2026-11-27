# Report D8-loop: D8-loop – acdc1 Rückführung, 4 Sinustöne, 30 s (Paar mit D8-osc)

| Feld | Wert |
|---|---|
| date | 2026-11-14 |
| device | acdc1, Firmware wie Readback 20261114 (meldet v22.5.0, enthält 237c63d) |
| test | Rückführung Out n → In n wie E7-ref-loop, 30 s, gleichzeitig mit D8-osc (Oszillatoren direkt) |
| gain | g12 |
| usb | usb-rxtx, Thunderbolt-Hub, Host-Software 48 kHz |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261114_acdc1_loop-30s_g12_usb-rxtx.4chan.000.wav` |
| Format | 48000 Hz, 34.8 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis D8-loop --no-spectrogram` |

**Hinweise:**

- Clipping: Samples an der Vollaussteuerung.
- Ein Nutzsignal (übrige Linien) dominiert. Störanteil und Notch-Gewinn sind dann nicht aussagekräftig, Störlinien in absoluten dBFS vergleichen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | -6.4 | -3.2 | – | -3.2 | -7.3 | -81.7 | -3.2 | -3.2 | -37.3 | 0 % | -37.3 | 0.0 |
| In 2 ← Out 2 (530 Hz) | -6.7 | -3.3 | – | -3.3 | -6.1 | -82.9 | -3.3 | -3.3 | -43.8 | 1 % | -43.9 | 0.0 |
| In 3 ← Out 3 (670 Hz) | -4.7 | -3.3 | – | -3.3 | -4.9 | -84.2 | -3.3 | -3.3 | -45.8 | 2 % | -45.8 | 0.1 |
| In 4 ← Out 4 (790 Hz) | -5.9 | -3.5 | – | -3.5 | -4.4 | -82.8 | -3.5 | -3.5 | -35.1 | 0 % | -35.1 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | In 1 ← Out 1 (440 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.6 dB | -77.6 | 0.0 % |
| 1-kHz-Kamm | In 1 ← Out 1 (440 Hz) | 999.8677 | 0.0004 | 23/23 | k=1: 999.867 Hz, -72.2 dB | -73.7 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | In 1 ← Out 1 (440 Hz) | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -63.7 dB | -63.3 | 0.3 % |
| Netz 50 Hz | In 1 ← Out 1 (440 Hz) | 50.0381 | 0.0073 | 3/19 | k=1: 50.034 Hz, -90.9 dB | -93.6 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | In 1 ← Out 1 (440 Hz) | 999.8677 | 0.0022 | 129 | k=15·f1+1·f2: 20998.015 Hz, -100.3 dB | -90.8 | 0.0 % |
| stärkste übrige Linie (440.00 Hz) | In 1 ← Out 1 (440 Hz) | 439.9998 | 0.0020 | 53/54 | k=1: 440.000 Hz, -0.0 dB | -3.2 | 100.0 % |
| stärkste übrige Linie (515.72 Hz) | In 1 ← Out 1 (440 Hz) | 515.7122 | 0.0170 | 3/46 | k=1: 515.721 Hz, -72.3 dB | -75.4 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 2 ← Out 2 (530 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.0 dB | -77.0 | 0.0 % |
| 1-kHz-Kamm | In 2 ← Out 2 (530 Hz) | 999.8677 | 0.0004 | 23/23 | k=1: 999.867 Hz, -72.5 dB | -73.9 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 2 ← Out 2 (530 Hz) | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -64.3 dB | -64.0 | 1.0 % |
| Netz 50 Hz | In 2 ← Out 2 (530 Hz) | 50.0363 | 0.0221 | 6/19 | k=1: 50.034 Hz, -91.0 dB | -91.7 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | In 2 ← Out 2 (530 Hz) | 999.8677 | 0.0020 | 140 | k=15·f1+1·f2: 20998.014 Hz, -100.1 dB | -90.4 | 0.0 % |
| stärkste übrige Linie (530.00 Hz) | In 2 ← Out 2 (530 Hz) | 530.0017 | 0.0014 | 44/45 | k=1: 530.002 Hz, -0.1 dB | -3.3 | 100.0 % |
| stärkste übrige Linie (605.72 Hz) | In 2 ← Out 2 (530 Hz) | 605.7087 | 0.0274 | 3/39 | k=1: 605.723 Hz, -72.5 dB | -75.5 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 3 ← Out 3 (670 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.2 | 0.1 % |
| 1-kHz-Kamm | In 3 ← Out 3 (670 Hz) | 999.8676 | 0.0004 | 23/23 | k=1: 999.867 Hz, -73.9 dB | -75.4 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 3 ← Out 3 (670 Hz) | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -64.6 dB | -64.2 | 1.4 % |
| Netz 50 Hz | In 3 ← Out 3 (670 Hz) | 50.0359 | 0.0231 | 4/19 | k=1: 50.033 Hz, -91.6 dB | -94.2 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | In 3 ← Out 3 (670 Hz) | 999.8676 | 0.0020 | 147 | k=15·f1+1·f2: 20998.014 Hz, -100.3 dB | -90.6 | 0.0 % |
| stärkste übrige Linie (670.00 Hz) | In 3 ← Out 3 (670 Hz) | 670.0003 | 0.0012 | 32/35 | k=1: 670.001 Hz, -0.2 dB | -3.3 | 100.0 % |
| stärkste übrige Linie (745.72 Hz) | In 3 ← Out 3 (670 Hz) | 745.7214 | 0.0000 | 1/32 | k=1: 745.721 Hz, -74.0 dB | -77.0 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 4 ← Out 4 (790 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.4 dB | -77.4 | 0.0 % |
| 1-kHz-Kamm | In 4 ← Out 4 (790 Hz) | 999.8677 | 0.0005 | 23/23 | k=1: 999.867 Hz, -71.6 dB | -73.1 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | In 4 ← Out 4 (790 Hz) | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -64.3 dB | -64.0 | 0.1 % |
| Netz 50 Hz | In 4 ← Out 4 (790 Hz) | 50.0344 | 0.0071 | 4/19 | k=14: 700.482 Hz, -78.8 dB | -81.6 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | In 4 ← Out 4 (790 Hz) | 999.8677 | 0.0020 | 135 | k=15·f1+1·f2: 20998.014 Hz, -100.4 dB | -90.8 | 0.0 % |
| stärkste übrige Linie (790.00 Hz) | In 4 ← Out 4 (790 Hz) | 789.9977 | 0.0012 | 28/30 | k=1: 789.997 Hz, -0.4 dB | -3.5 | 99.9 % |
| stärkste übrige Linie (714.28 Hz) | In 4 ← Out 4 (790 Hz) | 714.2857 | 0.0048 | 5/33 | k=1: 714.277 Hz, -77.0 dB | -80.0 | 0.0 % |

## Stärkste Linien (Kanal für Kanal)

### In 1 ← Out 1 (440 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 440.000 | -0.0 | 96.0 | other1·1 |
| 1320.000 | -28.7 | 95.5 | other1·3 |
| 2199.999 | -42.1 | 90.9 | other1·5 |
| 3079.998 | -50.8 | 84.4 | other1·7 |
| 3959.998 | -57.3 | 77.7 | other1·9 |
| 879.999 | -58.7 | 71.9 | other1·2 |
| 4839.998 | -62.7 | 71.8 | other1·11 |
| 2320.545 | -63.7 | 70.5 | led·1 |
| 4641.089 | -65.5 | 69.6 | led·2 |
| 5719.997 | -67.1 | 68.1 | other1·13 |
| 6961.635 | -68.2 | 67.5 | led·3 |
| 6599.996 | -70.8 | 65.0 | other1·15 |
| 9282.179 | -71.9 | 63.8 | led·4 |
| 515.721 | -72.3 | 40.6 | other2·1 |
| 999.867 | -72.2 | 59.8 | usb1k·1 |
| 364.278 | -72.2 | 40.5 | – |
| 7479.996 | -74.1 | 61.6 | other1·17 |
| 11602.724 | -75.6 | 59.8 | led·5 |
| 8359.996 | -77.3 | 58.0 | other1·19 |
| 6000.000 | -77.6 | 57.8 | fs8·1 |

### In 2 ← Out 2 (530 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 530.002 | -0.1 | 95.7 | other1·1 |
| 1590.005 | -28.8 | 94.9 | other1·3 |
| 2650.008 | -42.1 | 91.7 | other1·5 |
| 3710.012 | -50.8 | 85.1 | other1·7 |
| 4770.016 | -57.5 | 79.5 | other1·9 |
| 1060.003 | -60.5 | 73.5 | other1·2 |
| 5830.019 | -62.9 | 73.5 | other1·11 |
| 2320.545 | -64.3 | 71.6 | led·1 |
| 4641.089 | -66.2 | 70.5 | led·2 |
| 6890.022 | -67.2 | 69.7 | other1·13 |
| 6961.635 | -69.1 | 68.2 | led·3 |
| 605.723 | -72.5 | 40.4 | other2·1 |
| 7950.026 | -70.9 | 66.1 | other1·15 |
| 999.867 | -72.5 | 60.2 | usb1k·1 |
| 454.280 | -72.3 | 40.3 | – |
| 9282.179 | -73.0 | 64.2 | led·4 |
| 9010.030 | -74.5 | 61.9 | other1·17 |
| 6000.000 | -77.0 | 59.7 | fs8·1 |
| 11602.724 | -76.5 | 61.2 | led·5 |
| 10070.033 | -77.5 | 59.4 | other1·19 |

### In 3 ← Out 3 (670 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 670.001 | -0.2 | 96.9 | other1·1 |
| 2010.001 | -28.9 | 96.4 | other1·3 |
| 3350.001 | -42.0 | 93.5 | other1·5 |
| 4690.002 | -51.2 | 87.4 | other1·7 |
| 6030.002 | -57.7 | 81.5 | other1·9 |
| 7370.004 | -62.9 | 75.9 | other1·11 |
| 2320.545 | -64.6 | 73.8 | led·1 |
| 4641.089 | -66.3 | 72.7 | led·2 |
| 1340.000 | -66.4 | 70.0 | other1·2 |
| 8710.004 | -67.6 | 72.0 | other1·13 |
| 6961.635 | -69.1 | 70.8 | led·3 |
| 10050.004 | -71.2 | 67.9 | other1·15 |
| 9282.179 | -73.1 | 67.0 | led·4 |
| 745.721 | -74.0 | 38.8 | other2·1 |
| 669.685 | -73.9 | 23.2 | – |
| 999.867 | -73.9 | 55.0 | usb1k·1 |
| 594.279 | -73.8 | 38.8 | – |
| 11390.005 | -74.9 | 65.0 | other1·17 |
| 670.323 | -75.4 | 21.7 | – |
| 6000.000 | -77.3 | 62.0 | fs8·1 |

### In 4 ← Out 4 (790 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 789.997 | -0.4 | 93.1 | other1·1 |
| 2369.993 | -29.0 | 92.7 | other1·3 |
| 3949.988 | -42.5 | 90.4 | other1·5 |
| 5529.984 | -51.2 | 83.2 | other1·7 |
| 7109.979 | -58.0 | 78.2 | other1·9 |
| 1579.995 | -61.7 | 72.7 | other1·2 |
| 8689.974 | -63.0 | 73.2 | other1·11 |
| 2320.545 | -64.3 | 67.5 | led·1 |
| 4641.089 | -66.2 | 70.2 | led·2 |
| 10269.970 | -67.9 | 68.4 | other1·13 |
| 6961.635 | -69.1 | 67.3 | led·3 |
| 999.867 | -71.6 | 50.2 | usb1k·1 |
| 11849.965 | -71.5 | 63.0 | other1·15 |
| 9282.179 | -73.2 | 63.4 | led·4 |
| 13429.961 | -75.2 | 61.9 | other1·17 |
| 714.277 | -77.0 | 34.0 | other2·1 |
| 6000.000 | -77.4 | 58.1 | fs8·1 |
| 11602.724 | -77.1 | 59.3 | led·5 |
| 865.719 | -76.7 | 34.6 | – |
| 15009.955 | -78.2 | 58.2 | other1·19 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | In 1 ← Out 1 (440 Hz) | 5/5 | 0.01 | 0.01 | 0.01 |
| usb1k | In 1 ← Out 1 (440 Hz) | 5/5 | 0.08 | 0.17 | 0.03 |
| led | In 1 ← Out 1 (440 Hz) | 5/5 | 0.00 | -0.00 | 0.00 |
| mains50 | In 1 ← Out 1 (440 Hz) | 5/5 | 43.34 | 117.59 | 0.29 |
| other1 | In 1 ← Out 1 (440 Hz) | 5/5 | 0.00 | 0.00 | 0.00 |
| other2 | In 1 ← Out 1 (440 Hz) | 5/5 | 2.44 | -15.77 | 0.15 |
| fs8 | In 2 ← Out 2 (530 Hz) | 5/5 | 0.01 | 0.03 | 0.01 |
| usb1k | In 2 ← Out 2 (530 Hz) | 5/5 | 0.07 | -0.31 | 0.01 |
| led | In 2 ← Out 2 (530 Hz) | 5/5 | 0.00 | -0.00 | 0.00 |
| mains50 | In 2 ← Out 2 (530 Hz) | 5/5 | 27.36 | -3.91 | 0.30 |
| other1 | In 2 ← Out 2 (530 Hz) | 5/5 | 0.00 | -0.00 | 0.00 |
| other2 | In 2 ← Out 2 (530 Hz) | 5/5 | 2.76 | -15.48 | 0.10 |
| fs8 | In 3 ← Out 3 (670 Hz) | 5/5 | 0.01 | 0.01 | 0.01 |
| usb1k | In 3 ← Out 3 (670 Hz) | 5/5 | 0.13 | -0.36 | 0.02 |
| led | In 3 ← Out 3 (670 Hz) | 5/5 | 0.00 | -0.01 | 0.00 |
| mains50 | In 3 ← Out 3 (670 Hz) | 5/5 | 9.29 | 13.05 | 0.21 |
| other1 | In 3 ← Out 3 (670 Hz) | 5/5 | 0.00 | 0.00 | 0.00 |
| other2 | In 3 ← Out 3 (670 Hz) | 5/5 | 1.86 | 3.07 | 0.09 |
| fs8 | In 4 ← Out 4 (790 Hz) | 5/5 | 0.01 | 0.01 | 0.01 |
| usb1k | In 4 ← Out 4 (790 Hz) | 5/5 | 0.07 | -0.09 | 0.03 |
| led | In 4 ← Out 4 (790 Hz) | 5/5 | 0.00 | 0.01 | 0.00 |
| mains50 | In 4 ← Out 4 (790 Hz) | 5/5 | 6.80 | -42.68 | 0.14 |
| other1 | In 4 ← Out 4 (790 Hz) | 5/5 | 0.00 | -0.00 | 0.00 |
| other2 | In 4 ← Out 4 (790 Hz) | 5/5 | 0.34 | 0.63 | 0.39 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | breitbandig | 0.06 | 0.05 s (19.99 Hz) | 51.1 |
| In 1 ← Out 1 (440 Hz) | 440.0 Hz ± 10 | 1.04 | 0.05 s (19.99 Hz) | 58.7 |
| In 2 ← Out 2 (530 Hz) | breitbandig | 0.08 | 0.05 s (19.99 Hz) | 17.2 |
| In 2 ← Out 2 (530 Hz) | 530.0 Hz ± 10 | 1.04 | 0.49 s (2.04 Hz) | 23.4 |
| In 3 ← Out 3 (670 Hz) | breitbandig | 0.06 | 0.05 s (19.99 Hz) | 20.9 |
| In 3 ← Out 3 (670 Hz) | 670.0 Hz ± 10 | 1.04 | 8.71 s (0.11 Hz) | 27.6 |
| In 4 ← Out 4 (790 Hz) | breitbandig | 0.03 | 0.05 s (19.99 Hz) | 42.5 |
| In 4 ← Out 4 (790 Hz) | 790.0 Hz ± 10 | 1.03 | 0.05 s (19.99 Hz) | 51.0 |

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

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](D8-loop_psd.png)

### Kammprofile

![Kammprofile](D8-loop_combs.png)

### Zeitverlauf

![Zeitverlauf](D8-loop_timeline.png)

## Notiz aus dem Manifest

> Gleicher Host-Patch und gleiche Pegel wie E7-ref-loop. Datei-Werte enthalten den Host-Faktor 2 (messlog D7/D8).
