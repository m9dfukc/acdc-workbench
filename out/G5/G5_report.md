# Report G5: G5 – acdc1 Eingänge offen, AC/DC direkt am TB-Hub, 60 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | G5: A/B zu G4-in-no-out-2 – AC/DC-USB direkt am TB-Hub (wie A5), Eingänge offen, Ausgänge frei, UMC-Ausgänge an Boxen/Kopfhörer |
| gain | g12 |
| usb | usb-duplex, TB-Hub direkt |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g5-in-tbhub-direct_g12_usb-duplex.4chan.000.wav` |
| Format | 48000 Hz, 60.2 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis G5 --ref G4-in-no-out-2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -71.2 | -78.8 | -72.0 | -73.3 | -84.6 | -72.6 | -91.8 | -72.1 | 63 % | -76.4 | 4.4 |
| Kanal 2 | -6.5 | -71.9 | -79.7 | -72.7 | -74.0 | -86.1 | -73.2 | -91.9 | -72.8 | 70 % | -78.0 | 5.2 |
| Kanal 3 | -4.8 | -73.6 | -85.1 | -73.9 | -75.1 | -89.5 | -74.3 | -95.0 | -73.9 | 81 % | -81.2 | 7.3 |
| Kanal 4 | -4.9 | -72.7 | -80.3 | -73.5 | -74.7 | -87.6 | -74.0 | -94.9 | -73.6 | 69 % | -78.6 | 5.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0003 | 0.0003 | 3/3 | k=1: 6000.000 Hz, -79.6 dB | -79.6 | 17.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.9970 | 0.0135 | 22/23 | k=1: 999.996 Hz, -74.5 dB | -75.7 | 43.4 % |
| Netz 50 Hz | Kanal 1 | 49.9714 | 0.0019 | 3/19 | k=1: 49.973 Hz, -95.2 dB | -98.0 | 0.3 % |
| Mischprodukte n·999.9970 + m·6000.0003 Hz (m = ±1…±4) | Kanal 1 | 999.9970 | 0.0078 | 26 | k=32·f1-2·f2: 19999.919 Hz, -94.8 dB | -89.2 | 1.9 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7208 | 0.0028 | 4/315 | k=1: 75.720 Hz, -90.5 dB | -93.8 | 0.7 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 1 | 44.7552 | 0.0025 | 6/533 | k=1: 44.757 Hz, -94.1 dB | -96.2 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0003 | 0.0004 | 3/3 | k=1: 6000.001 Hz, -79.6 dB | -79.6 | 20.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.9970 | 0.0135 | 22/23 | k=1: 999.996 Hz, -74.9 dB | -76.1 | 46.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2322.9091 | 0.0000 | 1/10 | k=3: 6968.727 Hz, -122.4 dB | -124.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9715 | 0.0018 | 3/19 | k=1: 49.973 Hz, -96.1 dB | -98.7 | 0.3 % |
| Mischprodukte n·999.9970 + m·6000.0003 Hz (m = ±1…±4) | Kanal 2 | 999.9970 | 0.0090 | 28 | k=32·f1-2·f2: 19999.919 Hz, -95.2 dB | -89.2 | 2.3 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7228 | 0.0017 | 2/315 | k=1: 75.720 Hz, -90.3 dB | -93.5 | 0.8 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 2 | 44.7552 | 0.0020 | 6/533 | k=1: 44.755 Hz, -96.1 dB | -97.0 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0003 | 0.0004 | 3/3 | k=1: 6000.001 Hz, -79.9 dB | -79.8 | 25.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.9970 | 0.0135 | 22/23 | k=1: 999.996 Hz, -75.6 dB | -76.8 | 52.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5450 | 0.0021 | 9/10 | k=1: 2320.546 Hz, -124.8 dB | -120.6 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9716 | 0.0026 | 6/19 | k=1: 49.972 Hz, -97.2 dB | -99.7 | 0.3 % |
| Mischprodukte n·999.9970 + m·6000.0003 Hz (m = ±1…±4) | Kanal 3 | 999.9970 | 0.0092 | 29 | k=10·f1+1·f2: 15999.981 Hz, -95.1 dB | -88.8 | 3.3 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7208 | 0.0042 | 8/315 | k=1: 75.720 Hz, -94.3 dB | -97.4 | 0.4 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 3 | 44.7562 | 0.0019 | 5/533 | k=1: 44.757 Hz, -95.9 dB | -98.6 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0002 | 0.0003 | 3/3 | k=1: 6000.000 Hz, -81.1 dB | -80.9 | 18.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.9964 | 0.0099 | 22/23 | k=1: 999.996 Hz, -75.6 dB | -76.8 | 47.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2322.9090 | 0.0000 | 1/10 | k=3: 6968.727 Hz, -122.7 dB | -125.2 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9718 | 0.0011 | 3/19 | k=1: 49.972 Hz, -97.9 dB | -100.6 | 0.2 % |
| Mischprodukte n·999.9964 + m·6000.0002 Hz (m = ±1…±4) | Kanal 4 | 999.9964 | 0.0089 | 39 | k=7·f1+2·f2: 18999.987 Hz, -97.9 dB | -89.9 | 2.3 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7209 | 0.0170 | 7/315 | k=1: 75.721 Hz, -95.4 dB | -98.5 | 0.3 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 4 | 44.7552 | 0.0022 | 6/533 | k=1: 44.755 Hz, -96.4 dB | -97.4 | 0.4 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.996 | -74.5 | 57.6 | usb1k·1 |
| 6000.000 | -79.6 | 55.7 | fs8·1 |
| 1999.993 | -82.1 | 51.5 | usb1k·2 |
| 18000.001 | -82.4 | 54.2 | fs8·3 |
| 12000.000 | -82.9 | 54.8 | fs8·2 |
| 2999.990 | -82.8 | 51.1 | usb1k·3 |
| 6999.975 | -89.2 | 46.3 | usb1k·7 |
| 4999.981 | -89.8 | 45.3 | usb1k·5 |
| 75.720 | -90.5 | 34.0 | other1·1 |
| 9999.969 | -92.0 | 45.0 | usb1k·10 |
| 15999.936 | -93.4 | 44.2 | usb1k·16 |
| 11999.952 | -94.1 | 43.5 | usb1k·12 |
| 44.757 | -94.1 | 28.6 | other2·1 |
| 13999.958 | -95.0 | 42.7 | usb1k·14 |
| 10999.960 | -95.1 | 41.9 | usb1k·11 |
| 49.973 | -95.2 | 26.7 | mains50·1 |
| 19999.919 | -94.8 | 42.6 | imd·32·f1-2·f2 |
| 12999.988 | -96.1 | 41.2 | usb1k·13 |
| 9000.002 | -96.3 | 38.8 | usb1k·9 |
| 19999.959 | -96.8 | 40.6 | usb1k·20 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.996 | -74.9 | 58.9 | usb1k·1 |
| 6000.001 | -79.6 | 57.5 | fs8·1 |
| 18000.001 | -82.3 | 56.4 | fs8·3 |
| 12000.000 | -82.6 | 56.5 | fs8·2 |
| 1999.993 | -83.2 | 52.2 | usb1k·2 |
| 2999.989 | -83.0 | 52.5 | usb1k·3 |
| 6999.975 | -89.2 | 48.6 | usb1k·7 |
| 75.720 | -90.3 | 36.1 | other1·1 |
| 4999.981 | -90.6 | 46.2 | usb1k·5 |
| 9999.969 | -91.8 | 47.1 | usb1k·10 |
| 15999.936 | -93.5 | 46.0 | usb1k·16 |
| 11999.952 | -94.0 | 45.2 | usb1k·12 |
| 13999.957 | -94.7 | 44.8 | usb1k·14 |
| 10999.960 | -95.0 | 43.8 | usb1k·11 |
| 19999.919 | -95.2 | 44.5 | imd·32·f1-2·f2 |
| 12999.987 | -96.0 | 43.2 | usb1k·13 |
| 49.973 | -96.1 | 27.8 | mains50·1 |
| 9000.002 | -96.1 | 40.6 | usb1k·9 |
| 44.755 | -96.1 | 28.4 | other2·1 |
| 18999.986 | -96.7 | 43.0 | imd·7·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.996 | -75.6 | 62.9 | usb1k·1 |
| 6000.001 | -79.9 | 61.3 | fs8·1 |
| 18000.001 | -82.6 | 59.0 | fs8·3 |
| 12000.000 | -82.7 | 59.8 | fs8·2 |
| 1999.992 | -83.8 | 56.1 | usb1k·2 |
| 2999.989 | -83.8 | 56.5 | usb1k·3 |
| 6999.975 | -89.7 | 51.5 | usb1k·7 |
| 4999.982 | -91.2 | 49.5 | usb1k·5 |
| 9999.970 | -92.2 | 50.1 | usb1k·10 |
| 15999.936 | -93.9 | 48.4 | usb1k·16 |
| 75.720 | -94.3 | 35.9 | other1·1 |
| 11999.952 | -94.4 | 48.1 | usb1k·12 |
| 10999.960 | -95.2 | 47.4 | usb1k·11 |
| 13999.958 | -95.2 | 47.5 | usb1k·14 |
| 15999.981 | -95.1 | 47.2 | imd·10·f1+1·f2 |
| 19999.919 | -95.4 | 47.0 | imd·32·f1-2·f2 |
| 12999.987 | -96.4 | 46.0 | usb1k·13 |
| 9000.002 | -96.5 | 44.7 | usb1k·9 |
| 44.757 | -95.9 | 32.3 | other2·1 |
| 19999.959 | -97.0 | 45.5 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.996 | -75.6 | 59.0 | usb1k·1 |
| 6000.000 | -81.1 | 56.5 | fs8·1 |
| 1999.992 | -82.7 | 53.2 | usb1k·2 |
| 18000.001 | -83.6 | 55.0 | fs8·3 |
| 12000.000 | -83.9 | 55.1 | fs8·2 |
| 2999.989 | -84.1 | 52.5 | usb1k·3 |
| 6999.975 | -90.2 | 47.6 | usb1k·7 |
| 4999.981 | -90.4 | 47.0 | usb1k·5 |
| 9999.969 | -93.3 | 45.5 | usb1k·10 |
| 15999.936 | -94.0 | 45.4 | usb1k·16 |
| 11999.952 | -95.2 | 43.8 | usb1k·12 |
| 75.721 | -95.4 | 32.2 | other1·1 |
| 13999.958 | -96.1 | 43.1 | usb1k·14 |
| 10999.960 | -96.3 | 42.3 | usb1k·11 |
| 19999.919 | -95.9 | 43.9 | usb1k·20 |
| 44.755 | -96.4 | 28.3 | other2·1 |
| 12999.988 | -97.2 | 42.0 | usb1k·13 |
| 9000.002 | -97.3 | 39.1 | – |
| 49.972 | -97.9 | 26.6 | mains50·1 |
| 18999.987 | -97.9 | 41.4 | imd·7·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.40 | -0.08 | 1.25 |
| usb1k | Kanal 1 | 11/11 | 1.42 | -1.00 | 0.21 |
| mains50 | Kanal 1 | 11/11 | 645.33 | 323.31 | 0.69 |
| other1 | Kanal 1 | 11/11 | 35.39 | 28.11 | 1.06 |
| other2 | Kanal 1 | 11/11 | 0.53 | -0.52 | 1.23 |
| fs8 | Kanal 2 | 11/11 | 0.40 | -0.08 | 1.24 |
| usb1k | Kanal 2 | 11/11 | 1.31 | 0.25 | 0.21 |
| led | Kanal 2 | 8/11 | 9.11 | -7.79 | 1.85 |
| mains50 | Kanal 2 | 11/11 | 153.75 | 366.76 | 0.57 |
| other1 | Kanal 2 | 11/11 | 58.86 | -70.47 | 0.90 |
| other2 | Kanal 2 | 11/11 | 0.50 | -0.52 | 0.76 |
| fs8 | Kanal 3 | 11/11 | 0.39 | -0.06 | 1.22 |
| usb1k | Kanal 3 | 11/11 | 1.36 | 0.25 | 0.21 |
| led | Kanal 3 | 11/11 | 4.08 | 5.03 | 1.00 |
| mains50 | Kanal 3 | 11/11 | 489.01 | 989.99 | 0.49 |
| other1 | Kanal 3 | 11/11 | 2.56 | -0.70 | 0.91 |
| other2 | Kanal 3 | 11/11 | 3.97 | 2.28 | 1.14 |
| fs8 | Kanal 4 | 11/11 | 0.41 | -0.08 | 1.28 |
| usb1k | Kanal 4 | 11/11 | 1.46 | -1.04 | 0.20 |
| led | Kanal 4 | 10/11 | 14.84 | 13.49 | 1.77 |
| mains50 | Kanal 4 | 11/11 | 177.46 | 279.73 | 0.90 |
| other1 | Kanal 4 | 11/11 | 3.51 | 3.63 | 0.96 |
| other2 | Kanal 4 | 11/11 | 0.51 | -0.70 | 0.93 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.91 | 0.16 s (6.38 Hz) | 22.9 |
| Kanal 1 | 1000.0 Hz ± 10 | 0.72 | 1.09 s (0.91 Hz) | 18.7 |
| Kanal 2 | breitbandig | 0.86 | 0.16 s (6.40 Hz) | 24.7 |
| Kanal 2 | 1000.0 Hz ± 10 | 0.71 | 0.17 s (5.77 Hz) | 18.9 |
| Kanal 3 | breitbandig | 0.47 | 0.16 s (6.40 Hz) | 21.2 |
| Kanal 3 | 1000.0 Hz ± 10 | 0.69 | 15.04 s (0.07 Hz) | 20.2 |
| Kanal 4 | breitbandig | 0.86 | 0.16 s (6.40 Hz) | 23.2 |
| Kanal 4 | 1000.0 Hz ± 10 | 0.71 | 0.31 s (3.19 Hz) | 26.8 |

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
| Kanal 1 | 1.00 | 0.94 | 0.92 | 0.92 |
| Kanal 2 | 0.94 | 1.00 | 0.92 | 0.95 |
| Kanal 3 | 0.92 | 0.92 | 1.00 | 0.90 |
| Kanal 4 | 0.92 | 0.95 | 0.90 | 1.00 |

## Vergleich mit Referenz G4-in-no-out-2

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.0 | -66.5 | -5.6 | 63 % | 15 % |
| Kanal 2 | -72.7 | -66.4 | -6.3 | 70 % | 13 % |
| Kanal 3 | -73.9 | -68.7 | -5.2 | 81 % | 19 % |
| Kanal 4 | -73.5 | -68.3 | -5.2 | 69 % | 18 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G5_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G5_psd.png)

### Kammprofile

![Kammprofile](G5_combs.png)

### Zeitverlauf

![Zeitverlauf](G5_timeline.png)

## Notiz aus dem Manifest

> Datei-Werte mit Host-Faktor 2. Direkt vor G6 aufgenommen.
