# Report M1: M1 – kein Eingangssignal, Eingänge gebrückt 1↔2 / 3↔4, Gain 12 Uhr

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc2 (DIY), Firmware v22.4.q |
| test | kein Eingangssignal, Eingänge gebrückt 1↔2, 3↔4 |
| gain | g12 |
| usb | usb-stream |
| patch | Slot 1: ACDC (9,32 KB, Default-Patch, Knob = digitaler Gain) – laut Device-Status vom 2026-11-13 |
| Datei(en) | `20261113_acdc2_inputs-bridged_g12_usb-stream_ch1.wav`, `20261113_acdc2_inputs-bridged_g12_usb-stream_ch2.wav`, `20261113_acdc2_inputs-bridged_g12_usb-stream_ch3.wav`, `20261113_acdc2_inputs-bridged_g12_usb-stream_ch4.wav` |
| Format | 96000 Hz, 9.6 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis M1` |

**Hinweise:**

- Nur 9.6 s. Für Zeitverhalten und Klicks sind ≥ 60 s vorgesehen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +5.6 | -77.1 | -90.5 | -77.3 | -79.6 | -88.4 | -77.9 | -99.1 | -77.3 | 63 % | -81.6 | 4.3 |
| Kanal 2 | +4.9 | -77.1 | -91.0 | -77.3 | -78.8 | -90.4 | -77.7 | -100.0 | -77.3 | 70 % | -82.5 | 5.2 |
| Kanal 3 | +2.1 | -77.7 | -92.8 | -77.9 | -79.6 | -92.5 | -78.3 | – | -77.9 | 64 % | -82.3 | 4.4 |
| Kanal 4 | +3.4 | -77.5 | -91.3 | -77.7 | -78.6 | -91.6 | -78.0 | -99.4 | -77.7 | 78 % | -84.3 | 6.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0003 | 3/3 | k=1: 6000.000 Hz, -81.7 dB | -81.6 | 36.9 % |
| 1-kHz-Kamm | Kanal 1 | 1000.0527 | 0.0037 | 23/23 | k=3: 3000.157 Hz, -90.6 dB | -86.0 | 13.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.9765 | 0.0018 | 10/10 | k=9: 20888.787 Hz, -98.7 dB | -95.7 | 1.5 % |
| Netz 50 Hz | Kanal 1 | 50.0125 | 0.0118 | 7/19 | k=1: 50.013 Hz, -88.9 dB | -91.8 | 3.6 % |
| Mischprodukte n·1000.0527 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 1000.0527 | 0.0121 | 72 | k=8·f1+1·f2: 14000.423 Hz, -98.5 dB | -88.8 | 7.1 % |
| stärkste übrige Linie (35.38 Hz) | Kanal 1 | 35.3605 | 0.1343 | 5/675 | k=1: 35.376 Hz, -98.6 dB | -101.2 | 0.4 % |
| stärkste übrige Linie (112.02 Hz) | Kanal 1 | 112.0342 | 0.0104 | 4/213 | k=1: 112.022 Hz, -100.3 dB | -103.2 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -82.8 dB | -82.8 | 28.4 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0527 | 0.0037 | 23/23 | k=1: 1000.053 Hz, -82.4 dB | -82.0 | 33.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.9764 | 0.0016 | 10/10 | k=9: 20888.787 Hz, -99.2 dB | -96.1 | 1.3 % |
| Netz 50 Hz | Kanal 2 | 50.0111 | 0.0137 | 5/19 | k=1: 50.011 Hz, -94.7 dB | -97.6 | 0.9 % |
| Mischprodukte n·1000.0527 + m·5999.9999 Hz (m = ±1…±4) | Kanal 2 | 1000.0527 | 0.0111 | 71 | k=8·f1+1·f2: 14000.422 Hz, -99.5 dB | -89.9 | 5.4 % |
| stärkste übrige Linie (35.37 Hz) | Kanal 2 | 35.3605 | 0.0806 | 4/675 | k=1: 35.371 Hz, -99.2 dB | -102.5 | 0.3 % |
| stärkste übrige Linie (112.02 Hz) | Kanal 2 | 112.0027 | 0.0114 | 2/213 | k=1: 112.019 Hz, -100.5 dB | -103.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0004 | 3/3 | k=1: 6000.000 Hz, -82.4 dB | -82.5 | 34.5 % |
| 1-kHz-Kamm | Kanal 3 | 1000.0527 | 0.0031 | 23/23 | k=1: 1000.054 Hz, -86.7 dB | -84.5 | 21.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.9766 | 0.0020 | 10/10 | k=9: 20888.789 Hz, -104.5 dB | -101.1 | 0.5 % |
| Netz 50 Hz | Kanal 3 | 50.0112 | 0.0111 | 5/19 | k=1: 50.011 Hz, -95.9 dB | -98.7 | 0.8 % |
| Mischprodukte n·1000.0527 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 1000.0527 | 0.0122 | 71 | k=8·f1+1·f2: 14000.423 Hz, -99.3 dB | -89.7 | 6.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -84.7 dB | -84.6 | 20.6 % |
| 1-kHz-Kamm | Kanal 4 | 1000.0527 | 0.0077 | 23/23 | k=1: 1000.053 Hz, -80.1 dB | -80.5 | 52.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.9766 | 0.0026 | 10/10 | k=9: 20888.789 Hz, -106.0 dB | -102.6 | 0.3 % |
| Netz 50 Hz | Kanal 4 | 50.0117 | 0.0110 | 4/19 | k=1: 50.007 Hz, -98.3 dB | -101.5 | 0.4 % |
| Mischprodukte n·1000.0527 + m·5999.9999 Hz (m = ±1…±4) | Kanal 4 | 1000.0527 | 0.0091 | 73 | k=8·f1+1·f2: 14000.422 Hz, -101.2 dB | -91.6 | 4.1 % |
| stärkste übrige Linie (35.37 Hz) | Kanal 4 | 35.3604 | 0.0757 | 5/675 | k=1: 35.372 Hz, -98.4 dB | -101.5 | 0.4 % |
| stärkste übrige Linie (112.02 Hz) | Kanal 4 | 112.0028 | 0.0128 | 3/213 | k=1: 112.017 Hz, -100.5 dB | -103.5 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -81.7 | 47.6 | fs8·1 |
| 12000.000 | -84.4 | 44.6 | fs8·2 |
| 18000.000 | -84.8 | 44.3 | fs8·3 |
| 50.013 | -88.9 | 30.5 | mains50·1 |
| 3000.157 | -90.6 | 40.5 | usb1k·3 |
| 8000.420 | -92.3 | 36.0 | usb1k·8 |
| 7000.369 | -91.5 | 35.2 | usb1k·7 |
| 12000.634 | -92.9 | 36.2 | usb1k·12 |
| 4000.212 | -94.9 | 33.2 | usb1k·4 |
| 2000.106 | -95.2 | 35.0 | usb1k·2 |
| 15000.790 | -94.2 | 35.4 | usb1k·15 |
| 5000.262 | -94.0 | 34.3 | usb1k·5 |
| 10000.527 | -95.9 | 33.4 | usb1k·10 |
| 1000.060 | -96.3 | 34.3 | usb1k·1 |
| 14000.423 | -98.5 | 30.8 | imd·8·f1+1·f2 |
| 35.376 | -98.6 | 21.6 | other1·1 |
| 20888.787 | -98.7 | 34.0 | led·9 |
| 20000.421 | -99.2 | 29.8 | imd·8·f1+2·f2 |
| 18567.812 | -99.3 | 34.2 | led·8 |
| 16000.214 | -99.6 | 27.3 | imd·4·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -82.8 | 47.5 | fs8·1 |
| 1000.053 | -82.4 | 49.7 | usb1k·1 |
| 2000.106 | -85.7 | 44.7 | usb1k·2 |
| 12000.000 | -85.7 | 44.7 | fs8·2 |
| 18000.000 | -85.8 | 44.9 | fs8·3 |
| 3000.157 | -88.1 | 44.6 | usb1k·3 |
| 7000.369 | -91.5 | 36.4 | usb1k·7 |
| 12000.633 | -94.5 | 35.7 | usb1k·12 |
| 8000.420 | -94.6 | 34.5 | usb1k·8 |
| 50.011 | -94.7 | 24.8 | mains50·1 |
| 6000.317 | -95.3 | 35.0 | usb1k·6 |
| 15000.790 | -95.5 | 35.1 | usb1k·15 |
| 4000.211 | -97.7 | 31.9 | usb1k·4 |
| 21001.106 | -98.3 | 32.3 | usb1k·21 |
| 20888.787 | -99.2 | 34.3 | led·9 |
| 14000.422 | -99.5 | 31.5 | imd·8·f1+1·f2 |
| 18567.811 | -99.7 | 35.2 | led·8 |
| 11000.580 | -98.7 | 30.5 | usb1k·11 |
| 35.371 | -99.2 | 20.3 | other1·1 |
| 20000.421 | -100.3 | 29.7 | imd·8·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -82.4 | 47.6 | fs8·1 |
| 11999.999 | -85.5 | 44.2 | fs8·2 |
| 18000.000 | -85.8 | 44.9 | fs8·3 |
| 1000.054 | -86.7 | 44.2 | usb1k·1 |
| 2000.106 | -89.9 | 40.7 | usb1k·2 |
| 3000.157 | -89.2 | 42.8 | usb1k·3 |
| 7000.369 | -91.7 | 35.6 | usb1k·7 |
| 8000.420 | -93.7 | 35.5 | usb1k·8 |
| 12000.633 | -94.1 | 35.5 | usb1k·12 |
| 15000.790 | -95.3 | 34.7 | usb1k·15 |
| 4000.211 | -96.4 | 32.5 | usb1k·4 |
| 50.011 | -95.9 | 27.9 | mains50·1 |
| 10000.528 | -98.5 | 31.8 | usb1k·10 |
| 6000.317 | -99.0 | 31.0 | usb1k·6 |
| 14000.423 | -99.3 | 31.6 | imd·8·f1+1·f2 |
| 20000.421 | -100.2 | 29.3 | imd·8·f1+2·f2 |
| 21001.107 | -99.6 | 30.8 | usb1k·21 |
| 5000.262 | -99.2 | 30.1 | usb1k·5 |
| 10000.210 | -100.6 | 29.9 | imd·4·f1+1·f2 |
| 16000.214 | -100.6 | 27.4 | imd·4·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -80.1 | 53.1 | usb1k·1 |
| 2000.105 | -83.7 | 49.0 | usb1k·2 |
| 6000.000 | -84.7 | 48.0 | fs8·1 |
| 18000.000 | -87.4 | 46.1 | fs8·3 |
| 12000.000 | -87.5 | 45.1 | fs8·2 |
| 3000.157 | -87.6 | 46.7 | usb1k·3 |
| 7000.369 | -92.3 | 37.2 | usb1k·7 |
| 6000.317 | -93.8 | 38.9 | usb1k·6 |
| 12000.633 | -96.8 | 35.8 | usb1k·12 |
| 8000.420 | -97.7 | 33.1 | usb1k·8 |
| 15000.790 | -97.7 | 34.9 | usb1k·15 |
| 35.372 | -98.4 | 22.0 | other1·1 |
| 21001.106 | -98.3 | 34.4 | usb1k·21 |
| 50.007 | -98.3 | 23.0 | mains50·1 |
| 11000.579 | -99.2 | 31.5 | usb1k·11 |
| 112.017 | -100.5 | 26.7 | other2·1 |
| 13000.682 | -99.6 | 31.3 | usb1k·13 |
| 20001.057 | -100.7 | 31.7 | usb1k·20 |
| 10000.529 | -101.1 | 31.8 | usb1k·10 |
| 14000.422 | -101.2 | 32.0 | imd·8·f1+1·f2 |

## Zeitverhalten

Fensterlänge 2.4 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 7/7 | 2.23 | -19.62 | 0.26 |
| usb1k | Kanal 1 | 7/7 | 2.23 | -19.62 | 0.18 |
| led | Kanal 1 | 7/7 | 0.44 | 0.48 | 0.15 |
| mains50 | Kanal 1 | 7/7 | 660.81 | -9170.67 | 0.18 |
| other1 | Kanal 1 | 7/7 | 34.65 | 489.54 | 1.00 |
| other2 | Kanal 1 | 7/7 | 4.17 | 29.84 | 0.51 |
| fs8 | Kanal 2 | 7/7 | 1.99 | -14.21 | 0.57 |
| usb1k | Kanal 2 | 7/7 | 7.11 | -4.78 | 0.36 |
| led | Kanal 2 | 7/7 | 0.30 | 0.31 | 0.12 |
| mains50 | Kanal 2 | 7/7 | 542.41 | -3759.07 | 0.46 |
| other1 | Kanal 2 | 7/7 | 6.18 | 38.16 | 1.20 |
| other2 | Kanal 2 | 7/7 | 120.41 | 1978.08 | 0.50 |
| fs8 | Kanal 3 | 7/7 | 2.12 | -16.80 | 0.39 |
| usb1k | Kanal 3 | 7/7 | 2.12 | -16.80 | 0.32 |
| led | Kanal 3 | 7/7 | 0.79 | -1.06 | 0.20 |
| mains50 | Kanal 3 | 7/7 | 319.89 | -474.34 | 0.59 |
| fs8 | Kanal 4 | 7/7 | 1.87 | -11.76 | 0.81 |
| usb1k | Kanal 4 | 7/7 | 10.10 | 35.20 | 0.31 |
| led | Kanal 4 | 7/7 | 0.68 | 3.56 | 0.14 |
| mains50 | Kanal 4 | 7/7 | 539.58 | -5244.66 | 0.78 |
| other1 | Kanal 4 | 7/7 | 5.44 | 4.70 | 0.82 |
| other2 | Kanal 4 | 7/7 | 402.16 | 309.28 | 0.45 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, 0,2–20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.53 | 3.21 s (0.31 Hz) | 13.6 |
| Kanal 1 | 6000.0 Hz ± 10 | 2.04 | 3.21 s (0.31 Hz) | 38.2 |
| Kanal 2 | breitbandig | 0.50 | 3.21 s (0.31 Hz) | 23.1 |
| Kanal 2 | 1000.1 Hz ± 10 | 1.95 | 3.21 s (0.31 Hz) | 25.5 |
| Kanal 3 | breitbandig | 0.41 | 3.21 s (0.31 Hz) | 22.0 |
| Kanal 3 | 6000.0 Hz ± 10 | 2.15 | 3.21 s (0.31 Hz) | 40.9 |
| Kanal 4 | breitbandig | 0.47 | 3.21 s (0.31 Hz) | 23.6 |
| Kanal 4 | 1000.1 Hz ± 10 | 1.93 | 3.21 s (0.31 Hz) | 25.7 |

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
| Kanal 1 | 1.00 | 0.84 | 0.92 | 0.71 |
| Kanal 2 | 0.84 | 1.00 | 0.93 | 0.90 |
| Kanal 3 | 0.92 | 0.93 | 1.00 | 0.85 |
| Kanal 4 | 0.71 | 0.90 | 0.85 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](M1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](M1_psd.png)

### Kammprofile

![Kammprofile](M1_combs.png)

### Zeitverlauf

![Zeitverlauf](M1_timeline.png)

## Notiz aus dem Manifest

> Zu hören: praktisch Stille, erst bei sehr lauter Abhöre ein leises Rauschen mit feinem hohem Pfeifen.
> Aufnahme-Software hat auf 96 kHz / 16 Bit hochgerechnet, nur ≈ 10 s lang. Ursprünglich channel-{1..4}.wav.
