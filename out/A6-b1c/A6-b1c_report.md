# Report A6-b1c: A6-b1c – acdc1 Build 1c, Rückführung, 4 Sinustöne, Gain 12 Uhr, 10 min

| Feld | Wert |
|---|---|
| date | 2026-11-14 |
| device | acdc1, Firmware Build 1c v22.4.r-thru1c (db9d3dd + Revert 237c63d + Ausgang 125 + atomarer RX-Zähler) |
| test | Abnahme A6: Rückführung Out n → In n wie E7-ref-loop, Host-Sinus 440/530/670/790 Hz, 10 min |
| gain | g12 |
| usb | usb-rxtx, Thunderbolt-Hub, Host-Software 48 kHz |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261114_acdc1_b1c-loop-10min_g12_usb-rxtx.4chan.000.wav` |
| Format | 48000 Hz, 604.5 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis A6-b1c --ref E7-ref-loop` |

**Hinweise:**

- Clipping: Samples an der Vollaussteuerung.
- Ein Nutzsignal (übrige Linien) dominiert. Störanteil und Notch-Gewinn sind dann nicht aussagekräftig, Störlinien in absoluten dBFS vergleichen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | -6.3 | -3.3 | – | -3.3 | -7.3 | -81.9 | -3.3 | -3.3 | -45.3 | 1 % | -45.4 | 0.1 |
| In 2 ← Out 2 (530 Hz) | -6.5 | -3.3 | – | -3.3 | -6.1 | -83.6 | -3.3 | -3.3 | -47.3 | 2 % | -47.4 | 0.1 |
| In 3 ← Out 3 (670 Hz) | -4.6 | -3.3 | – | -3.3 | -4.9 | -85.0 | -3.3 | -3.3 | -45.3 | 1 % | -45.4 | 0.1 |
| In 4 ← Out 4 (790 Hz) | -5.7 | -3.6 | – | -3.6 | -4.4 | -83.3 | -3.6 | -3.6 | -46.5 | 2 % | -46.6 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | In 1 ← Out 1 (440 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.2 | 0.0 % |
| 1-kHz-Kamm | In 1 ← Out 1 (440 Hz) | 999.8675 | 0.0000 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.4 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 1 ← Out 1 (440 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -64.6 dB | -64.1 | 1.3 % |
| Netz 50 Hz | In 1 ← Out 1 (440 Hz) | 49.9891 | 0.0002 | 2/19 | k=1: 49.989 Hz, -99.2 dB | -98.1 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 1 ← Out 1 (440 Hz) | 999.8675 | 0.0001 | 176 | k=8·f1+1·f2: 13998.940 Hz, -96.0 dB | -85.9 | 0.0 % |
| stärkste übrige Linie (440.00 Hz) | In 1 ← Out 1 (440 Hz) | 439.9998 | 0.0000 | 54/54 | k=1: 440.000 Hz, 0.0 dB | -3.3 | 100.0 % |
| stärkste übrige Linie (364.28 Hz) | In 1 ← Out 1 (440 Hz) | 364.2789 | 0.0004 | 2/65 | k=1: 364.279 Hz, -72.4 dB | -75.6 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 2 ← Out 2 (530 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.6 | 0.1 % |
| 1-kHz-Kamm | In 2 ← Out 2 (530 Hz) | 999.8675 | 0.0000 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.6 | 0.2 % |
| LED-PWM (≈ 2,32 kHz) | In 2 ← Out 2 (530 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -65.2 dB | -64.9 | 1.8 % |
| Netz 50 Hz | In 2 ← Out 2 (530 Hz) | 49.9894 | 0.0024 | 3/19 | k=1: 49.989 Hz, -99.5 dB | -98.3 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 2 ← Out 2 (530 Hz) | 999.8675 | 0.0001 | 176 | k=8·f1+1·f2: 13998.940 Hz, -95.4 dB | -85.3 | 0.0 % |
| stärkste übrige Linie (530.00 Hz) | In 2 ← Out 2 (530 Hz) | 530.0017 | 0.0000 | 45/45 | k=1: 530.002 Hz, -0.1 dB | -3.3 | 100.0 % |
| stärkste übrige Linie (454.28 Hz) | In 2 ← Out 2 (530 Hz) | 454.2809 | 0.0004 | 2/52 | k=1: 454.281 Hz, -72.9 dB | -76.0 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 3 ← Out 3 (670 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.8 dB | -78.8 | 0.0 % |
| 1-kHz-Kamm | In 3 ← Out 3 (670 Hz) | 999.8675 | 0.0001 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -76.1 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | In 3 ← Out 3 (670 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -65.5 dB | -65.1 | 1.1 % |
| Netz 50 Hz | In 3 ← Out 3 (670 Hz) | 49.9899 | 0.0023 | 4/19 | k=1: 49.989 Hz, -100.3 dB | -99.1 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 3 ← Out 3 (670 Hz) | 999.8675 | 0.0001 | 175 | k=8·f1+1·f2: 13998.940 Hz, -95.6 dB | -85.6 | 0.0 % |
| stärkste übrige Linie (670.00 Hz) | In 3 ← Out 3 (670 Hz) | 670.0003 | 0.0000 | 35/35 | k=1: 670.000 Hz, -0.0 dB | -3.3 | 100.0 % |
| stärkste übrige Linie (594.28 Hz) | In 3 ← Out 3 (670 Hz) | 594.2797 | 0.0012 | 3/40 | k=1: 594.279 Hz, -74.3 dB | -77.6 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | In 4 ← Out 4 (790 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.9 dB | -79.0 | 0.1 % |
| 1-kHz-Kamm | In 4 ← Out 4 (790 Hz) | 999.8675 | 0.0000 | 23/23 | k=1: 999.868 Hz, -72.6 dB | -73.9 | 0.2 % |
| LED-PWM (≈ 2,32 kHz) | In 4 ← Out 4 (790 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -65.3 dB | -65.0 | 1.4 % |
| Netz 50 Hz | In 4 ← Out 4 (790 Hz) | 49.9898 | 0.0022 | 4/19 | k=1: 49.989 Hz, -100.3 dB | -99.1 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 4 ← Out 4 (790 Hz) | 999.8675 | 0.0001 | 172 | k=8·f1+1·f2: 13998.940 Hz, -95.8 dB | -85.7 | 0.0 % |
| stärkste übrige Linie (790.00 Hz) | In 4 ← Out 4 (790 Hz) | 789.9977 | 0.0000 | 29/30 | k=1: 789.998 Hz, -0.5 dB | -3.6 | 100.0 % |
| stärkste übrige Linie (714.28 Hz) | In 4 ← Out 4 (790 Hz) | 714.2763 | 0.0003 | 2/33 | k=1: 714.277 Hz, -77.6 dB | -80.6 | 0.0 % |

## Stärkste Linien (Kanal für Kanal)

### In 1 ← Out 1 (440 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 440.000 | 0.0 | 107.6 | other1·1 |
| 1319.999 | -28.6 | 107.2 | other1·3 |
| 2199.999 | -42.0 | 102.8 | other1·5 |
| 3079.998 | -50.9 | 96.6 | other1·7 |
| 3959.998 | -57.5 | 90.0 | other1·9 |
| 880.000 | -58.9 | 84.1 | other1·2 |
| 4839.997 | -62.7 | 85.0 | other1·11 |
| 2320.545 | -64.6 | 82.9 | led·1 |
| 4641.090 | -66.2 | 81.3 | led·2 |
| 5719.997 | -67.1 | 80.9 | other1·13 |
| 6961.634 | -69.3 | 78.5 | led·3 |
| 6599.996 | -70.9 | 76.9 | other1·15 |
| 9282.179 | -72.8 | 75.2 | led·4 |
| 364.279 | -72.4 | 52.7 | other2·1 |
| 999.868 | -73.1 | 71.6 | usb1k·1 |
| 515.721 | -72.3 | 52.7 | – |
| 7479.996 | -74.4 | 73.1 | other1·17 |
| 8359.995 | -77.4 | 70.5 | other1·19 |
| 11602.724 | -76.5 | 71.2 | led·5 |
| 484.757 | -78.0 | 42.3 | – |

### In 2 ← Out 2 (530 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 530.002 | -0.1 | 107.0 | other1·1 |
| 1590.005 | -28.8 | 106.6 | other1·3 |
| 2650.009 | -41.9 | 104.1 | other1·5 |
| 3710.012 | -51.1 | 97.8 | other1·7 |
| 4770.016 | -57.5 | 91.4 | other1·9 |
| 1060.003 | -60.5 | 85.8 | other1·2 |
| 5830.019 | -62.8 | 87.0 | other1·11 |
| 2320.545 | -65.2 | 83.7 | led·1 |
| 6890.022 | -67.2 | 82.0 | other1·13 |
| 4641.090 | -66.9 | 82.3 | led·2 |
| 6961.634 | -70.3 | 79.0 | led·3 |
| 7950.026 | -71.0 | 78.6 | other1·15 |
| 454.281 | -72.9 | 52.9 | other2·1 |
| 999.868 | -73.3 | 72.0 | usb1k·1 |
| 605.723 | -72.8 | 53.1 | – |
| 9282.179 | -74.0 | 75.6 | led·4 |
| 9010.029 | -74.6 | 69.4 | other1·17 |
| 6000.000 | -78.5 | 71.1 | fs8·1 |
| 11602.724 | -77.4 | 71.6 | led·5 |
| 10070.033 | -77.3 | 72.8 | other1·19 |

### In 3 ← Out 3 (670 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 670.000 | -0.0 | 107.7 | other1·1 |
| 2010.001 | -28.7 | 107.4 | other1·3 |
| 3350.001 | -42.1 | 105.5 | other1·5 |
| 4690.002 | -51.0 | 99.5 | other1·7 |
| 6030.003 | -57.6 | 94.5 | other1·9 |
| 7370.003 | -62.9 | 89.2 | other1·11 |
| 2320.545 | -65.5 | 85.5 | led·1 |
| 1340.001 | -67.0 | 82.0 | other1·2 |
| 4641.090 | -67.1 | 84.2 | led·2 |
| 8710.004 | -67.5 | 85.0 | other1·13 |
| 6961.634 | -70.3 | 81.5 | led·3 |
| 10050.004 | -71.3 | 81.3 | other1·15 |
| 9282.179 | -74.0 | 78.2 | led·4 |
| 11390.005 | -74.8 | 77.5 | other1·17 |
| 999.868 | -74.9 | 66.4 | usb1k·1 |
| 594.279 | -74.3 | 51.2 | other2·1 |
| 745.721 | -74.3 | 51.3 | – |
| 714.758 | -77.2 | 43.6 | – |
| 625.243 | -77.2 | 43.6 | – |
| 12730.006 | -77.9 | 74.7 | other1·19 |

### In 4 ← Out 4 (790 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 789.998 | -0.5 | 105.4 | other1·1 |
| 2369.993 | -29.1 | 105.3 | other1·3 |
| 3949.988 | -42.3 | 102.7 | other1·5 |
| 5529.984 | -51.2 | 96.9 | other1·7 |
| 7109.979 | -57.9 | 90.3 | other1·9 |
| 1579.995 | -62.1 | 84.8 | other1·2 |
| 8689.974 | -63.4 | 85.4 | other1·11 |
| 2320.545 | -65.3 | 79.9 | led·1 |
| 4641.090 | -67.0 | 81.4 | led·2 |
| 10269.970 | -67.9 | 81.1 | other1·13 |
| 6961.634 | -70.3 | 78.1 | led·3 |
| 11849.965 | -71.8 | 77.1 | other1·15 |
| 999.868 | -72.6 | 61.6 | usb1k·1 |
| 9282.179 | -74.1 | 74.7 | led·4 |
| 13429.960 | -75.2 | 74.2 | other1·17 |
| 714.277 | -77.6 | 46.1 | other2·1 |
| 865.719 | -77.5 | 46.2 | – |
| 6000.000 | -78.9 | 69.8 | fs8·1 |
| 11602.724 | -78.2 | 70.2 | led·5 |
| 15009.956 | -78.1 | 71.0 | other1·19 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | In 1 ← Out 1 (440 Hz) | 119/119 | 0.02 | 0.00 | 0.04 |
| usb1k | In 1 ← Out 1 (440 Hz) | 119/119 | 0.12 | 0.02 | 0.08 |
| led | In 1 ← Out 1 (440 Hz) | 119/119 | 0.01 | 0.00 | 0.05 |
| mains50 | In 1 ← Out 1 (440 Hz) | 119/119 | 316.23 | 48.14 | 0.39 |
| other1 | In 1 ← Out 1 (440 Hz) | 119/119 | 0.00 | -0.00 | 0.00 |
| other2 | In 1 ← Out 1 (440 Hz) | 119/119 | 9.51 | 0.23 | 0.17 |
| fs8 | In 2 ← Out 2 (530 Hz) | 119/119 | 0.02 | 0.00 | 0.04 |
| usb1k | In 2 ← Out 2 (530 Hz) | 119/119 | 0.11 | 0.02 | 0.06 |
| led | In 2 ← Out 2 (530 Hz) | 119/119 | 0.01 | 0.00 | 0.04 |
| mains50 | In 2 ← Out 2 (530 Hz) | 119/119 | 469.39 | 2.07 | 0.33 |
| other1 | In 2 ← Out 2 (530 Hz) | 119/119 | 0.00 | -0.00 | 0.00 |
| other2 | In 2 ← Out 2 (530 Hz) | 119/119 | 6.13 | -0.26 | 0.18 |
| fs8 | In 3 ← Out 3 (670 Hz) | 119/119 | 0.02 | 0.00 | 0.04 |
| usb1k | In 3 ← Out 3 (670 Hz) | 119/119 | 0.16 | 0.02 | 0.06 |
| led | In 3 ← Out 3 (670 Hz) | 119/119 | 0.01 | 0.00 | 0.01 |
| mains50 | In 3 ← Out 3 (670 Hz) | 119/119 | 41.61 | 3.87 | 0.26 |
| other1 | In 3 ← Out 3 (670 Hz) | 119/119 | 0.00 | -0.00 | 0.00 |
| other2 | In 3 ← Out 3 (670 Hz) | 119/119 | 9.27 | 0.28 | 0.19 |
| fs8 | In 4 ← Out 4 (790 Hz) | 119/119 | 0.02 | 0.00 | 0.04 |
| usb1k | In 4 ← Out 4 (790 Hz) | 119/119 | 0.12 | 0.02 | 0.06 |
| led | In 4 ← Out 4 (790 Hz) | 119/119 | 0.01 | 0.00 | 0.02 |
| mains50 | In 4 ← Out 4 (790 Hz) | 119/119 | 446.40 | 34.67 | 0.41 |
| other1 | In 4 ← Out 4 (790 Hz) | 119/119 | 0.00 | 0.00 | 0.00 |
| other2 | In 4 ← Out 4 (790 Hz) | 119/119 | 5.84 | 0.06 | 0.32 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | breitbandig | 0.06 | 0.05 s (20.00 Hz) | 58.9 |
| In 1 ← Out 1 (440 Hz) | 440.0 Hz ± 10 | 0.23 | 0.05 s (20.00 Hz) | 68.2 |
| In 2 ← Out 2 (530 Hz) | breitbandig | 0.08 | 0.14 s (6.90 Hz) | 23.5 |
| In 2 ← Out 2 (530 Hz) | 530.0 Hz ± 10 | 0.24 | 0.14 s (6.90 Hz) | 31.6 |
| In 3 ← Out 3 (670 Hz) | breitbandig | 0.06 | 0.05 s (20.00 Hz) | 32.0 |
| In 3 ← Out 3 (670 Hz) | 670.0 Hz ± 10 | 0.23 | 0.14 s (6.90 Hz) | 29.9 |
| In 4 ← Out 4 (790 Hz) | breitbandig | 0.03 | 0.18 s (5.41 Hz) | 27.0 |
| In 4 ← Out 4 (790 Hz) | 790.0 Hz ± 10 | 0.23 | 0.18 s (5.41 Hz) | 35.4 |

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

## Vergleich mit Referenz E7-ref-loop

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | -3.3 | -3.1 | -0.1 | 1 % | 1 % |
| In 2 ← Out 2 (530 Hz) | -3.3 | -4.1 | +0.9 | 2 % | 1 % |
| In 3 ← Out 3 (670 Hz) | -3.3 | -3.9 | +0.6 | 1 % | 1 % |
| In 4 ← Out 4 (790 Hz) | -3.6 | -4.5 | +1.0 | 2 % | 1 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](A6-b1c_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](A6-b1c_psd.png)

### Kammprofile

![Kammprofile](A6-b1c_combs.png)

### Zeitverlauf

![Zeitverlauf](A6-b1c_timeline.png)

## Notiz aus dem Manifest

> Gleicher Host-Patch wie E7-ref-loop und A6-b1b. Ausgangspegel laut Nutzer am Scope wieder wie alte Firmware, Durchleitung ohne USB geprüft (messlog D14/D15). Datei-Werte mit Host-Faktor 2.
