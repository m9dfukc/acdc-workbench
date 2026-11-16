# Report A6-b1b: A6-b1b – acdc1 Build 1b, Rückführung, 4 Sinustöne, Gain 12 Uhr, 10 min

| Feld | Wert |
|---|---|
| date | 2026-11-14 |
| device | acdc1, Firmware Build 1b v22.4.r-thru1 (db9d3dd + Revert 237c63d) |
| test | Abnahme A6: Rückführung Out n → In n wie E7-ref-loop, Host-Sinus 440/530/670/790 Hz, 10 min |
| gain | g12 |
| usb | usb-rxtx, Thunderbolt-Hub, Host-Software 48 kHz |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261114_acdc1_b1b-loop-10min_g12_usb-rxtx.4chan.000.wav` |
| Format | 48000 Hz, 600.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis A6-b1b --ref E7-ref-loop --no-spectrogram` |

**Hinweise:**

- Ein Nutzsignal (übrige Linien) dominiert. Störanteil und Notch-Gewinn sind dann nicht aussagekräftig, Störlinien in absoluten dBFS vergleichen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | -6.4 | -8.8 | – | -8.8 | -12.9 | -85.3 | -8.8 | -8.8 | -27.9 | 0 % | -27.9 | 0.0 |
| In 2 ← Out 2 (530 Hz) | -6.6 | -8.8 | – | -8.8 | -11.6 | -85.2 | -8.8 | -8.8 | -26.2 | 0 % | -26.2 | 0.0 |
| In 3 ← Out 3 (670 Hz) | -4.6 | -8.8 | – | -8.8 | -10.4 | -88.3 | -8.8 | -9.0 | -24.5 | 0 % | -24.5 | 0.0 |
| In 4 ← Out 4 (790 Hz) | -5.8 | -8.9 | – | -8.9 | -9.8 | -85.3 | -8.9 | -9.1 | -23.5 | 0 % | -23.5 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | In 1 ← Out 1 (440 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.5 dB | -77.5 | 0.0 % |
| 1-kHz-Kamm | In 1 ← Out 1 (440 Hz) | 999.8675 | 0.0000 | 23/23 | k=1: 999.868 Hz, -71.5 dB | -73.2 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | In 1 ← Out 1 (440 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -68.3 dB | -67.2 | 0.0 % |
| Netz 50 Hz | In 1 ← Out 1 (440 Hz) | 49.9909 | 0.0009 | 3/19 | k=1: 49.991 Hz, -99.6 dB | -99.0 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 1 ← Out 1 (440 Hz) | 999.8675 | 0.0001 | 135 | k=8·f1+2·f2: 19998.940 Hz, -100.8 dB | -90.2 | 0.0 % |
| stärkste übrige Linie (440.00 Hz) | In 1 ← Out 1 (440 Hz) | 439.9992 | 0.0008 | 23/54 | k=1: 439.999 Hz, -5.8 dB | -8.9 | 97.9 % |
| stärkste übrige Linie (440.01 Hz) | In 1 ← Out 1 (440 Hz) | 440.0066 | 0.0011 | 12/54 | k=1: 440.007 Hz, -28.0 dB | -29.6 | 0.8 % |
| fs/8 (6000 Hz, sample-synchron) | In 2 ← Out 2 (530 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.9 dB | -76.9 | 0.0 % |
| 1-kHz-Kamm | In 2 ← Out 2 (530 Hz) | 999.8675 | 0.0000 | 23/23 | k=1: 999.868 Hz, -71.8 dB | -73.5 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | In 2 ← Out 2 (530 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -69.3 dB | -68.0 | 0.0 % |
| Netz 50 Hz | In 2 ← Out 2 (530 Hz) | 49.9907 | 0.0001 | 3/19 | k=1: 49.991 Hz, -97.7 dB | -97.0 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 2 ← Out 2 (530 Hz) | 999.8675 | 0.0001 | 114 | k=8·f1+2·f2: 19998.940 Hz, -100.4 dB | -89.8 | 0.0 % |
| stärkste übrige Linie (530.00 Hz) | In 2 ← Out 2 (530 Hz) | 530.0011 | 0.0014 | 23/45 | k=1: 530.001 Hz, -6.1 dB | -8.9 | 97.2 % |
| stärkste übrige Linie (530.01 Hz) | In 2 ← Out 2 (530 Hz) | 530.0084 | 0.0011 | 10/45 | k=1: 530.009 Hz, -26.0 dB | -28.5 | 1.1 % |
| fs/8 (6000 Hz, sample-synchron) | In 3 ← Out 3 (670 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.2 | 0.0 % |
| 1-kHz-Kamm | In 3 ← Out 3 (670 Hz) | 999.8675 | 0.0000 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.8 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | In 3 ← Out 3 (670 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -69.6 dB | -68.4 | 0.0 % |
| Netz 50 Hz | In 3 ← Out 3 (670 Hz) | 49.9905 | 0.0017 | 4/19 | k=1: 49.991 Hz, -97.5 dB | -96.8 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 3 ← Out 3 (670 Hz) | 999.8675 | 0.0001 | 138 | k=8·f1+2·f2: 19998.940 Hz, -100.8 dB | -90.0 | 0.0 % |
| stärkste übrige Linie (670.00 Hz) | In 3 ← Out 3 (670 Hz) | 669.9995 | 0.0012 | 19/35 | k=1: 669.999 Hz, -6.4 dB | -9.0 | 95.5 % |
| stärkste übrige Linie (670.01 Hz) | In 3 ← Out 3 (670 Hz) | 670.0069 | 0.0009 | 11/35 | k=1: 670.007 Hz, -23.9 dB | -26.4 | 1.7 % |
| fs/8 (6000 Hz, sample-synchron) | In 4 ← Out 4 (790 Hz) | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.2 dB | -77.2 | 0.0 % |
| 1-kHz-Kamm | In 4 ← Out 4 (790 Hz) | 999.8675 | 0.0000 | 23/23 | k=1: 999.868 Hz, -71.1 dB | -72.7 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | In 4 ← Out 4 (790 Hz) | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -69.8 dB | -68.6 | 0.0 % |
| Netz 50 Hz | In 4 ← Out 4 (790 Hz) | 49.9907 | 0.0001 | 3/19 | k=1: 49.991 Hz, -98.8 dB | -98.1 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | In 4 ← Out 4 (790 Hz) | 999.8675 | 0.0002 | 127 | k=8·f1+2·f2: 19998.940 Hz, -100.7 dB | -90.0 | 0.0 % |
| stärkste übrige Linie (790.00 Hz) | In 4 ← Out 4 (790 Hz) | 789.9967 | 0.0009 | 17/30 | k=1: 789.997 Hz, -6.5 dB | -9.2 | 93.7 % |
| stärkste übrige Linie (790.00 Hz) | In 4 ← Out 4 (790 Hz) | 790.0043 | 0.0014 | 13/30 | k=1: 790.005 Hz, -22.7 dB | -24.5 | 2.8 % |

## Stärkste Linien (Kanal für Kanal)

### In 1 ← Out 1 (440 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 439.999 | -5.8 | 86.9 | other1·1 |
| 440.007 | -28.0 | 64.7 | other2·1 |
| 439.991 | -29.6 | 63.1 | – |
| 1319.998 | -36.2 | 75.9 | other1·3 |
| 440.012 | -36.1 | 56.6 | – |
| 440.020 | -36.7 | 56.0 | – |
| 439.978 | -36.3 | 56.4 | – |
| 439.969 | -38.2 | 54.5 | – |
| 440.028 | -39.9 | 52.8 | – |
| 439.983 | -39.9 | 52.8 | – |
| 440.037 | -43.9 | 48.8 | – |
| 439.961 | -43.2 | 49.5 | – |
| 439.948 | -44.4 | 48.3 | – |
| 439.940 | -46.1 | 46.6 | – |
| 440.042 | -46.2 | 46.5 | – |
| 439.956 | -46.3 | 46.4 | – |
| 440.050 | -46.9 | 45.8 | – |
| 1320.005 | -46.7 | 65.4 | – |
| 440.058 | -49.1 | 43.6 | – |
| 1319.993 | -49.5 | 62.6 | – |

### In 2 ← Out 2 (530 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 530.001 | -6.1 | 85.0 | other1·1 |
| 530.009 | -26.0 | 65.1 | other2·1 |
| 529.993 | -27.6 | 63.5 | – |
| 529.988 | -34.3 | 56.8 | – |
| 529.979 | -35.0 | 56.1 | – |
| 530.014 | -35.7 | 55.4 | – |
| 530.022 | -35.6 | 55.5 | – |
| 1590.003 | -36.7 | 74.0 | other1·3 |
| 529.971 | -37.1 | 54.0 | – |
| 530.030 | -38.1 | 53.0 | – |
| 529.963 | -41.7 | 49.4 | – |
| 530.039 | -42.4 | 48.7 | – |
| 529.950 | -42.7 | 48.4 | – |
| 529.958 | -43.8 | 47.3 | – |
| 529.942 | -44.7 | 46.4 | – |
| 1590.011 | -45.0 | 65.7 | – |
| 530.052 | -45.3 | 45.8 | – |
| 530.044 | -45.5 | 45.6 | – |
| 530.060 | -47.3 | 43.8 | – |
| 529.928 | -48.2 | 42.9 | – |

### In 3 ← Out 3 (670 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 669.999 | -6.4 | 82.7 | other1·1 |
| 670.007 | -23.9 | 65.3 | other2·1 |
| 669.991 | -26.2 | 63.0 | – |
| 669.986 | -32.3 | 56.8 | – |
| 670.016 | -33.4 | 55.8 | – |
| 669.978 | -33.2 | 56.0 | – |
| 669.969 | -35.2 | 54.0 | – |
| 670.029 | -36.4 | 52.7 | – |
| 2009.999 | -36.4 | 72.8 | other1·3 |
| 669.961 | -39.8 | 49.4 | – |
| 669.948 | -40.7 | 48.5 | – |
| 670.037 | -40.6 | 48.6 | – |
| 669.956 | -42.0 | 47.2 | – |
| 669.940 | -42.5 | 46.6 | – |
| 2010.006 | -42.8 | 66.4 | – |
| 670.045 | -44.3 | 44.9 | – |
| 670.050 | -43.8 | 45.4 | – |
| 670.059 | -45.4 | 43.8 | – |
| 669.926 | -46.1 | 43.1 | – |
| 670.082 | -46.4 | 42.8 | – |

### In 4 ← Out 4 (790 Hz)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 789.997 | -6.5 | 81.5 | other1·1 |
| 790.005 | -22.7 | 65.3 | other2·1 |
| 789.988 | -25.6 | 62.4 | – |
| 790.010 | -31.2 | 56.7 | – |
| 790.018 | -32.5 | 55.5 | – |
| 789.975 | -32.0 | 55.9 | – |
| 789.967 | -33.8 | 54.2 | – |
| 790.026 | -36.0 | 52.0 | – |
| 2369.990 | -36.6 | 71.5 | other1·3 |
| 790.034 | -39.2 | 48.8 | – |
| 789.959 | -38.5 | 49.5 | – |
| 789.945 | -39.2 | 48.8 | – |
| 789.937 | -40.6 | 47.3 | – |
| 2369.997 | -41.2 | 66.9 | – |
| 789.954 | -40.8 | 47.2 | – |
| 790.042 | -41.7 | 46.3 | – |
| 790.048 | -43.4 | 44.6 | – |
| 790.057 | -43.4 | 44.6 | – |
| 790.079 | -44.4 | 43.5 | – |
| 789.916 | -44.6 | 43.4 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | In 1 ← Out 1 (440 Hz) | 119/119 | 0.02 | 0.00 | 0.07 |
| usb1k | In 1 ← Out 1 (440 Hz) | 119/119 | 0.31 | -0.00 | 0.03 |
| led | In 1 ← Out 1 (440 Hz) | 119/119 | 0.02 | -0.00 | 0.07 |
| mains50 | In 1 ← Out 1 (440 Hz) | 119/119 | 425.30 | -27.71 | 0.89 |
| other1 | In 1 ← Out 1 (440 Hz) | 119/119 | 7.84 | -0.10 | 0.01 |
| other2 | In 1 ← Out 1 (440 Hz) | 119/119 | 7.84 | -0.10 | 0.01 |
| fs8 | In 2 ← Out 2 (530 Hz) | 119/119 | 0.02 | -0.00 | 0.07 |
| usb1k | In 2 ← Out 2 (530 Hz) | 119/119 | 0.31 | -0.00 | 0.06 |
| led | In 2 ← Out 2 (530 Hz) | 119/119 | 0.03 | -0.00 | 0.06 |
| mains50 | In 2 ← Out 2 (530 Hz) | 119/119 | 399.37 | -18.87 | 0.54 |
| other1 | In 2 ← Out 2 (530 Hz) | 119/119 | 7.89 | -0.09 | 0.01 |
| other2 | In 2 ← Out 2 (530 Hz) | 119/119 | 7.89 | -0.09 | 0.01 |
| fs8 | In 3 ← Out 3 (670 Hz) | 119/119 | 0.01 | -0.00 | 0.07 |
| usb1k | In 3 ← Out 3 (670 Hz) | 119/119 | 0.40 | 0.01 | 0.11 |
| led | In 3 ← Out 3 (670 Hz) | 119/119 | 0.04 | -0.00 | 0.03 |
| mains50 | In 3 ← Out 3 (670 Hz) | 119/119 | 392.01 | -17.37 | 0.41 |
| other1 | In 3 ← Out 3 (670 Hz) | 119/119 | 3.24 | 0.01 | 0.02 |
| other2 | In 3 ← Out 3 (670 Hz) | 119/119 | 3.24 | 0.01 | 0.02 |
| fs8 | In 4 ← Out 4 (790 Hz) | 119/119 | 0.01 | -0.00 | 0.08 |
| usb1k | In 4 ← Out 4 (790 Hz) | 119/119 | 0.24 | -0.00 | 0.13 |
| led | In 4 ← Out 4 (790 Hz) | 119/119 | 0.05 | -0.00 | 0.05 |
| mains50 | In 4 ← Out 4 (790 Hz) | 119/119 | 428.93 | -14.73 | 0.70 |
| other1 | In 4 ← Out 4 (790 Hz) | 119/119 | 0.60 | -0.01 | 0.04 |
| other2 | In 4 ← Out 4 (790 Hz) | 119/119 | 0.60 | -0.01 | 0.04 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | breitbandig | 0.06 | 0.05 s (20.00 Hz) | 50.5 |
| In 1 ← Out 1 (440 Hz) | 440.0 Hz ± 10 | 0.20 | 0.05 s (20.00 Hz) | 54.2 |
| In 2 ← Out 2 (530 Hz) | breitbandig | 0.08 | 0.14 s (6.90 Hz) | 28.4 |
| In 2 ← Out 2 (530 Hz) | 530.0 Hz ± 10 | 0.21 | 0.14 s (6.90 Hz) | 29.6 |
| In 3 ← Out 3 (670 Hz) | breitbandig | 0.06 | 0.05 s (19.99 Hz) | 27.1 |
| In 3 ← Out 3 (670 Hz) | 670.0 Hz ± 10 | 0.21 | 0.14 s (6.90 Hz) | 25.0 |
| In 4 ← Out 4 (790 Hz) | breitbandig | 0.03 | 0.05 s (20.00 Hz) | 46.3 |
| In 4 ← Out 4 (790 Hz) | 790.0 Hz ± 10 | 0.20 | 0.05 s (20.00 Hz) | 46.2 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| In 1 ← Out 1 (440 Hz) | 12 | 1.2 | 0.384 | 1.52 |
| In 2 ← Out 2 (530 Hz) | 12 | 1.2 | 0.380 | 1.52 |
| In 3 ← Out 3 (670 Hz) | 12 | 1.2 | 0.384 | 1.52 |
| In 4 ← Out 4 (790 Hz) | 12 | 1.2 | 0.372 | 1.52 |

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
| In 1 ← Out 1 (440 Hz) | -8.8 | -3.1 | -5.7 | 0 % | 1 % |
| In 2 ← Out 2 (530 Hz) | -8.8 | -4.1 | -4.6 | 0 % | 1 % |
| In 3 ← Out 3 (670 Hz) | -8.8 | -3.9 | -4.9 | 0 % | 1 % |
| In 4 ← Out 4 (790 Hz) | -8.9 | -4.5 | -4.4 | 0 % | 1 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](A6-b1b_psd.png)

### Kammprofile

![Kammprofile](A6-b1b_combs.png)

### Zeitverlauf

![Zeitverlauf](A6-b1b_timeline.png)

## Notiz aus dem Manifest

> Gleicher Host-Patch wie E7-ref-loop. Ausgang 5,5 dB leiser als mit alter Firmware (Vorgabe audio_output_gain 114 statt 125, messlog D11). Datei-Werte mit Host-Faktor 2.
