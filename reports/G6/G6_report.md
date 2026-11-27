# Report G6: G6 – acdc1 Eingänge offen, Alltags-USB-Kette (Wiederholung), 60 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | G6: wie G5, AC/DC-USB wieder an der Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| gain | g12 |
| usb | usb-duplex, passiver Hub → Monitor-Hub → TB-Hub |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g6-in-daily-chain-again_g12_usb-duplex.4chan.000.wav` |
| Format | 48000 Hz, 60.2 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis G6 --ref G4-in-no-out-2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -71.7 | -81.2 | -72.2 | -73.6 | -84.7 | -72.8 | -91.8 | -72.3 | 61 % | -76.3 | 4.1 |
| Kanal 2 | -6.5 | -72.7 | -82.4 | -73.2 | -74.7 | -86.3 | -73.8 | -92.6 | -73.3 | 67 % | -78.0 | 4.8 |
| Kanal 3 | -4.8 | -74.3 | -86.1 | -74.6 | -76.0 | -89.6 | -75.1 | -95.4 | -74.6 | 78 % | -81.2 | 6.5 |
| Kanal 4 | -4.9 | -73.2 | -82.8 | -73.7 | -74.9 | -87.7 | -74.1 | -96.6 | -73.7 | 68 % | -78.6 | 4.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.4 | 19.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0003 | 23/23 | k=1: 999.867 Hz, -75.1 dB | -76.6 | 36.7 % |
| Netz 50 Hz | Kanal 1 | 49.9775 | 0.0010 | 3/19 | k=1: 49.977 Hz, -95.4 dB | -98.3 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0010 | 139 | k=8·f1+1·f2: 13998.940 Hz, -96.4 dB | -86.1 | 4.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7175 | 0.0026 | 2/315 | k=1: 75.721 Hz, -90.2 dB | -93.2 | 0.8 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 1 | 44.7583 | 0.0074 | 5/533 | k=1: 44.757 Hz, -94.8 dB | -97.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.3 | 25.0 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0003 | 23/23 | k=1: 999.867 Hz, -76.3 dB | -77.7 | 36.0 % |
| Netz 50 Hz | Kanal 2 | 49.9777 | 0.0010 | 3/19 | k=1: 49.977 Hz, -96.2 dB | -99.0 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0009 | 151 | k=8·f1+1·f2: 13998.940 Hz, -96.3 dB | -86.0 | 5.3 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7175 | 0.0026 | 2/315 | k=1: 75.721 Hz, -90.0 dB | -93.1 | 1.0 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 2 | 89.5152 | 0.0009 | 2/266 | k=1: 89.516 Hz, -99.4 dB | -102.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.6 dB | -79.6 | 32.0 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0002 | 23/23 | k=1: 999.867 Hz, -77.4 dB | -78.7 | 38.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5449 | 0.0031 | 10/10 | k=2: 4641.085 Hz, -123.4 dB | -119.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9778 | 0.0044 | 6/19 | k=1: 49.977 Hz, -97.0 dB | -99.6 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0008 | 163 | k=8·f1+1·f2: 13998.940 Hz, -96.6 dB | -86.3 | 6.7 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7179 | 0.0102 | 3/315 | k=1: 75.721 Hz, -94.2 dB | -97.2 | 0.5 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 3 | 44.7592 | 0.0018 | 4/533 | k=1: 44.757 Hz, -97.8 dB | -100.1 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -80.8 dB | -80.7 | 19.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0003 | 23/23 | k=1: 999.867 Hz, -75.9 dB | -77.3 | 43.3 % |
| Netz 50 Hz | Kanal 4 | 49.9776 | 0.0006 | 3/19 | k=1: 49.977 Hz, -97.5 dB | -100.1 | 0.2 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0009 | 145 | k=8·f1+1·f2: 13998.940 Hz, -97.5 dB | -87.3 | 4.3 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7217 | 0.0017 | 3/315 | k=1: 75.721 Hz, -94.9 dB | -97.9 | 0.4 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 4 | 89.5182 | 0.0025 | 3/266 | k=1: 89.516 Hz, -99.6 dB | -102.6 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.1 | 54.1 | usb1k·1 |
| 6000.000 | -79.3 | 55.8 | fs8·1 |
| 18000.000 | -82.2 | 54.7 | fs8·3 |
| 12000.000 | -82.7 | 54.3 | fs8·2 |
| 2999.603 | -83.5 | 49.8 | usb1k·3 |
| 1999.735 | -83.6 | 43.1 | usb1k·2 |
| 6999.073 | -88.6 | 46.9 | usb1k·7 |
| 75.721 | -90.2 | 34.4 | other1·1 |
| 9998.675 | -92.5 | 43.1 | usb1k·10 |
| 15997.881 | -92.5 | 43.5 | usb1k·16 |
| 10998.543 | -94.5 | 41.0 | usb1k·11 |
| 44.757 | -94.8 | 27.7 | other2·1 |
| 49.977 | -95.4 | 27.2 | mains50·1 |
| 14998.013 | -94.9 | 41.6 | usb1k·15 |
| 5999.206 | -96.7 | 38.4 | usb1k·6 |
| 15999.470 | -96.9 | 39.4 | imd·4·f1+2·f2 |
| 9999.470 | -97.3 | 38.3 | imd·4·f1+1·f2 |
| 13998.940 | -96.4 | 40.6 | imd·8·f1+1·f2 |
| 18997.484 | -97.1 | 39.9 | usb1k·19 |
| 13998.145 | -97.6 | 39.2 | usb1k·14 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -76.3 | 55.7 | usb1k·1 |
| 6000.000 | -79.3 | 57.4 | fs8·1 |
| 18000.000 | -82.2 | 56.2 | fs8·3 |
| 12000.000 | -82.4 | 56.0 | fs8·2 |
| 2999.603 | -84.2 | 50.8 | usb1k·3 |
| 1999.735 | -84.8 | 44.8 | usb1k·2 |
| 6999.073 | -88.9 | 48.3 | usb1k·7 |
| 75.721 | -90.0 | 36.8 | other1·1 |
| 9998.675 | -92.8 | 44.6 | usb1k·10 |
| 15997.881 | -93.0 | 45.0 | usb1k·16 |
| 10998.543 | -94.8 | 42.0 | usb1k·11 |
| 14998.013 | -94.8 | 43.4 | usb1k·15 |
| 49.977 | -96.2 | 28.0 | mains50·1 |
| 15999.470 | -96.7 | 41.4 | imd·4·f1+2·f2 |
| 13998.940 | -96.3 | 42.2 | imd·8·f1+1·f2 |
| 9999.470 | -97.2 | 40.1 | imd·4·f1+1·f2 |
| 12999.073 | -97.8 | 41.1 | imd·7·f1+1·f2 |
| 5999.206 | -97.8 | 39.0 | usb1k·6 |
| 18997.484 | -97.5 | 41.0 | usb1k·19 |
| 16998.543 | -97.5 | 40.2 | imd·11·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -77.4 | 57.9 | usb1k·1 |
| 6000.000 | -79.6 | 60.0 | fs8·1 |
| 18000.000 | -82.5 | 58.3 | fs8·3 |
| 12000.000 | -82.5 | 59.1 | fs8·2 |
| 2999.603 | -85.2 | 53.6 | usb1k·3 |
| 1999.735 | -85.8 | 47.5 | usb1k·2 |
| 6999.073 | -89.6 | 50.8 | usb1k·7 |
| 9998.676 | -93.3 | 47.1 | usb1k·10 |
| 15997.881 | -93.7 | 46.9 | usb1k·16 |
| 75.721 | -94.2 | 35.9 | other1·1 |
| 10998.543 | -95.4 | 45.3 | usb1k·11 |
| 14998.013 | -94.9 | 45.9 | usb1k·15 |
| 15999.470 | -97.1 | 43.8 | imd·4·f1+2·f2 |
| 49.977 | -97.0 | 31.6 | mains50·1 |
| 13998.940 | -96.6 | 44.5 | imd·8·f1+1·f2 |
| 9999.470 | -97.6 | 42.7 | imd·4·f1+1·f2 |
| 12999.073 | -98.0 | 43.5 | imd·7·f1+1·f2 |
| 16998.543 | -97.7 | 43.0 | imd·11·f1+1·f2 |
| 18997.484 | -97.9 | 43.0 | usb1k·19 |
| 44.757 | -97.8 | 30.5 | other2·1 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.9 | 57.4 | usb1k·1 |
| 6000.000 | -80.8 | 56.7 | fs8·1 |
| 18000.000 | -83.5 | 55.2 | fs8·3 |
| 12000.000 | -83.6 | 54.7 | fs8·2 |
| 1999.735 | -83.2 | 47.9 | usb1k·2 |
| 2999.603 | -84.5 | 51.3 | usb1k·3 |
| 6999.073 | -89.4 | 47.7 | usb1k·7 |
| 15997.881 | -93.1 | 44.7 | usb1k·16 |
| 9998.675 | -93.5 | 44.7 | usb1k·10 |
| 75.721 | -94.9 | 32.6 | other1·1 |
| 10998.543 | -95.4 | 41.4 | usb1k·11 |
| 5999.206 | -96.6 | 41.0 | usb1k·6 |
| 4999.338 | -95.8 | 40.8 | usb1k·5 |
| 14998.013 | -96.2 | 42.4 | usb1k·15 |
| 49.977 | -97.5 | 27.3 | mains50·1 |
| 15999.470 | -97.9 | 40.0 | imd·4·f1+2·f2 |
| 13998.145 | -98.3 | 40.0 | usb1k·14 |
| 13998.940 | -97.5 | 40.8 | imd·8·f1+1·f2 |
| 18997.484 | -98.2 | 40.4 | usb1k·19 |
| 9999.470 | -98.6 | 39.5 | imd·4·f1+1·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.05 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.20 | 0.02 | 0.04 |
| mains50 | Kanal 1 | 11/11 | 201.56 | -14.59 | 0.45 |
| other1 | Kanal 1 | 11/11 | 50.23 | -55.22 | 0.33 |
| other2 | Kanal 1 | 11/11 | 136.95 | -142.00 | 0.56 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.04 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.19 | 0.01 | 0.03 |
| mains50 | Kanal 2 | 11/11 | 511.66 | 459.17 | 0.81 |
| other1 | Kanal 2 | 11/11 | 31.19 | -35.04 | 0.20 |
| other2 | Kanal 2 | 11/11 | 2.19 | 3.08 | 0.71 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.04 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.17 | 0.10 | 0.02 |
| led | Kanal 3 | 11/11 | 3.62 | 3.97 | 0.93 |
| mains50 | Kanal 3 | 11/11 | 176.37 | -168.45 | 0.38 |
| other1 | Kanal 3 | 11/11 | 27.28 | 58.17 | 0.26 |
| other2 | Kanal 3 | 11/11 | 216.04 | -479.56 | 0.47 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.05 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.18 | -0.01 | 0.02 |
| mains50 | Kanal 4 | 11/11 | 148.52 | 33.98 | 0.66 |
| other1 | Kanal 4 | 11/11 | 364.51 | 734.34 | 0.30 |
| other2 | Kanal 4 | 11/11 | 201.71 | 51.15 | 0.45 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.72 | 1.25 s (0.80 Hz) | 17.8 |
| Kanal 1 | 999.9 Hz ± 10 | 0.75 | 1.25 s (0.80 Hz) | 26.6 |
| Kanal 2 | breitbandig | 0.69 | 0.31 s (3.18 Hz) | 17.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.74 | 1.25 s (0.80 Hz) | 29.6 |
| Kanal 3 | breitbandig | 0.48 | 0.31 s (3.18 Hz) | 22.6 |
| Kanal 3 | 999.9 Hz ± 10 | 0.72 | 1.25 s (0.80 Hz) | 32.6 |
| Kanal 4 | breitbandig | 0.67 | 0.10 s (9.59 Hz) | 14.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.71 | 1.25 s (0.80 Hz) | 29.2 |

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
| Kanal 1 | 1.00 | 0.93 | 0.92 | 0.90 |
| Kanal 2 | 0.93 | 1.00 | 0.91 | 0.93 |
| Kanal 3 | 0.92 | 0.91 | 1.00 | 0.89 |
| Kanal 4 | 0.90 | 0.93 | 0.89 | 1.00 |

## Vergleich mit Referenz G4-in-no-out-2

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.2 | -66.5 | -5.8 | 61 % | 15 % |
| Kanal 2 | -73.2 | -66.4 | -6.8 | 67 % | 13 % |
| Kanal 3 | -74.6 | -68.7 | -5.8 | 78 % | 19 % |
| Kanal 4 | -73.7 | -68.3 | -5.4 | 68 % | 18 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G6_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G6_psd.png)

### Kammprofile

![Kammprofile](G6_combs.png)

### Zeitverlauf

![Zeitverlauf](G6_timeline.png)

## Notiz aus dem Manifest

> Datei-Werte mit Host-Faktor 2. Direkt nach G5 aufgenommen.
