# Report A5-b1d-r2-60s: 

| Feld | Wert |
|---|---|
| Datei(en) | `_tmp_A5-b1d-r2-60s.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis out/_tmp_A5-b1d-r2-60s.wav --name A5-b1d-r2-60s --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -70.9 | -77.1 | -72.1 | -73.4 | -85.0 | -72.7 | -92.0 | -72.2 | 63 % | -76.5 | 4.3 |
| Kanal 2 | -6.5 | -71.8 | -78.0 | -73.0 | -74.4 | -86.2 | -73.5 | -92.6 | -73.1 | 68 % | -78.1 | 5.0 |
| Kanal 3 | -4.8 | -74.1 | -84.0 | -74.6 | -76.0 | -89.6 | -75.1 | -95.5 | -74.6 | 78 % | -81.3 | 6.7 |
| Kanal 4 | -4.9 | -72.3 | -78.8 | -73.4 | -74.4 | -87.6 | -73.8 | -96.4 | -73.4 | 69 % | -78.5 | 5.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.4 | 19.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.2 | 39.3 % |
| Netz 50 Hz | Kanal 1 | 49.9630 | 0.0008 | 2/19 | k=1: 49.964 Hz, -93.4 dB | -96.1 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0010 | 145 | k=8·f1+1·f2: 13998.941 Hz, -96.6 dB | -86.1 | 4.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7175 | 0.0038 | 3/315 | k=1: 75.721 Hz, -89.8 dB | -93.2 | 0.8 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 1 | 44.7566 | 0.0037 | 4/533 | k=1: 44.758 Hz, -96.0 dB | -98.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.3 | 23.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.9 dB | -77.2 | 38.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0025 | 10/10 | k=8: 18564.358 Hz, -117.7 dB | -113.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9628 | 0.0011 | 3/19 | k=1: 49.964 Hz, -94.1 dB | -96.7 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0009 | 155 | k=8·f1+1·f2: 13998.941 Hz, -96.4 dB | -86.0 | 5.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7175 | 0.0036 | 3/315 | k=1: 75.721 Hz, -89.8 dB | -93.0 | 1.0 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 2 | 89.5133 | 0.0096 | 3/266 | k=1: 89.516 Hz, -99.3 dB | -102.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.6 dB | -79.6 | 31.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -77.5 dB | -78.7 | 39.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0027 | 10/10 | k=1: 2320.548 Hz, -123.3 dB | -119.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9641 | 0.0022 | 6/19 | k=1: 49.964 Hz, -95.2 dB | -97.8 | 0.5 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0012 | 165 | k=8·f1+1·f2: 13998.941 Hz, -96.8 dB | -86.3 | 6.8 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7180 | 0.0023 | 2/315 | k=1: 75.721 Hz, -93.7 dB | -97.1 | 0.6 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 3 | 44.7572 | 0.0015 | 4/533 | k=1: 44.757 Hz, -98.2 dB | -100.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.8 dB | -80.7 | 18.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.7 | 46.8 % |
| Netz 50 Hz | Kanal 4 | 49.9629 | 0.0009 | 3/19 | k=1: 49.964 Hz, -96.5 dB | -98.9 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0012 | 154 | k=8·f1+1·f2: 13998.941 Hz, -97.6 dB | -87.3 | 4.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7175 | 0.0042 | 3/315 | k=1: 75.721 Hz, -94.5 dB | -97.7 | 0.4 % |
| stärkste übrige Linie (13.79 Hz) | Kanal 4 | 13.7941 | 0.0235 | 9/1731 | k=1: 13.793 Hz, -99.0 dB | -102.2 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 57.2 | usb1k·1 |
| 6000.000 | -79.3 | 52.9 | fs8·1 |
| 18000.000 | -82.3 | 54.9 | fs8·3 |
| 12000.000 | -82.7 | 52.3 | fs8·2 |
| 1999.735 | -82.8 | 50.6 | usb1k·2 |
| 2999.603 | -83.3 | 50.1 | usb1k·3 |
| 6999.073 | -88.5 | 47.5 | usb1k·7 |
| 75.721 | -89.8 | 35.3 | other1·1 |
| 9998.676 | -92.3 | 44.0 | usb1k·10 |
| 15997.882 | -92.3 | 44.6 | usb1k·16 |
| 49.964 | -93.4 | 29.5 | mains50·1 |
| 10998.544 | -94.6 | 42.1 | usb1k·11 |
| 14998.014 | -95.0 | 41.7 | usb1k·15 |
| 5999.206 | -95.8 | 36.6 | usb1k·6 |
| 44.758 | -96.0 | 27.1 | other2·1 |
| 4999.338 | -96.3 | 38.5 | usb1k·5 |
| 13998.941 | -96.6 | 40.2 | imd·8·f1+1·f2 |
| 15999.471 | -96.8 | 40.0 | imd·4·f1+2·f2 |
| 19998.941 | -97.2 | 39.4 | imd·8·f1+2·f2 |
| 9999.470 | -97.3 | 38.8 | imd·4·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.9 | 57.8 | usb1k·1 |
| 6000.000 | -79.3 | 55.1 | fs8·1 |
| 18000.000 | -82.2 | 56.2 | fs8·3 |
| 12000.000 | -82.5 | 54.8 | fs8·2 |
| 1999.735 | -83.9 | 51.2 | usb1k·2 |
| 2999.603 | -84.1 | 51.3 | usb1k·3 |
| 6999.073 | -88.8 | 48.8 | usb1k·7 |
| 75.721 | -89.8 | 36.5 | other1·1 |
| 9998.676 | -92.7 | 45.3 | usb1k·10 |
| 15997.882 | -92.8 | 45.6 | usb1k·16 |
| 49.964 | -94.1 | 30.1 | mains50·1 |
| 10998.544 | -94.8 | 43.3 | usb1k·11 |
| 14998.014 | -94.9 | 43.4 | usb1k·15 |
| 13998.941 | -96.4 | 42.1 | imd·8·f1+1·f2 |
| 15999.470 | -96.7 | 41.6 | imd·4·f1+2·f2 |
| 5999.206 | -96.9 | 37.6 | usb1k·6 |
| 19998.941 | -97.2 | 41.3 | imd·8·f1+2·f2 |
| 9999.470 | -97.4 | 40.5 | imd·4·f1+1·f2 |
| 16998.544 | -97.5 | 39.9 | imd·11·f1+1·f2 |
| 12999.073 | -97.8 | 40.6 | imd·7·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -77.5 | 60.4 | usb1k·1 |
| 6000.000 | -79.6 | 58.4 | fs8·1 |
| 18000.000 | -82.5 | 59.0 | fs8·3 |
| 12000.000 | -82.6 | 58.0 | fs8·2 |
| 2999.603 | -85.3 | 53.9 | usb1k·3 |
| 1999.735 | -85.6 | 53.8 | usb1k·2 |
| 6999.073 | -89.7 | 51.4 | usb1k·7 |
| 9998.676 | -93.3 | 48.0 | usb1k·10 |
| 15997.882 | -93.8 | 47.8 | usb1k·16 |
| 49.964 | -95.2 | 32.8 | mains50·1 |
| 14998.014 | -95.1 | 46.5 | usb1k·15 |
| 75.721 | -93.7 | 37.0 | other1·1 |
| 10998.544 | -95.6 | 45.9 | usb1k·11 |
| 13998.941 | -96.8 | 44.4 | imd·8·f1+1·f2 |
| 15999.470 | -97.1 | 44.3 | imd·4·f1+2·f2 |
| 9999.470 | -97.5 | 43.8 | imd·4·f1+1·f2 |
| 19998.941 | -97.4 | 43.9 | imd·8·f1+2·f2 |
| 16998.544 | -97.7 | 43.0 | imd·11·f1+1·f2 |
| 12999.073 | -98.0 | 43.5 | imd·7·f1+1·f2 |
| 5999.206 | -98.3 | 39.9 | usb1k·6 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 58.9 | usb1k·1 |
| 6000.000 | -80.8 | 54.7 | fs8·1 |
| 1999.735 | -82.2 | 53.6 | usb1k·2 |
| 18000.000 | -83.5 | 54.8 | fs8·3 |
| 12000.000 | -83.7 | 53.6 | fs8·2 |
| 2999.603 | -84.3 | 51.7 | usb1k·3 |
| 6999.073 | -89.3 | 48.3 | usb1k·7 |
| 15997.882 | -92.8 | 45.5 | usb1k·16 |
| 9998.676 | -93.3 | 44.7 | usb1k·10 |
| 4999.338 | -94.4 | 41.8 | usb1k·5 |
| 5999.206 | -95.5 | 40.1 | usb1k·6 |
| 10998.544 | -95.5 | 42.6 | usb1k·11 |
| 75.721 | -94.5 | 32.9 | other1·1 |
| 49.964 | -96.5 | 28.3 | mains50·1 |
| 14998.014 | -96.4 | 42.2 | usb1k·15 |
| 13998.941 | -97.6 | 40.5 | imd·8·f1+1·f2 |
| 15999.470 | -97.8 | 40.1 | imd·4·f1+2·f2 |
| 13998.147 | -98.2 | 40.0 | usb1k·14 |
| 19998.941 | -98.6 | 40.0 | imd·8·f1+2·f2 |
| 9999.470 | -98.8 | 39.1 | imd·4·f1+1·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.04 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.19 | 0.12 | 0.02 |
| mains50 | Kanal 1 | 11/11 | 199.42 | -356.95 | 0.37 |
| other1 | Kanal 1 | 11/11 | 50.79 | 98.33 | 0.27 |
| other2 | Kanal 1 | 11/11 | 14.58 | 5.19 | 0.50 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.03 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.15 | 0.09 | 0.02 |
| led | Kanal 2 | 11/11 | 0.44 | 0.04 | 0.54 |
| mains50 | Kanal 2 | 11/11 | 459.70 | -1153.37 | 0.41 |
| other1 | Kanal 2 | 11/11 | 4.76 | -6.02 | 0.29 |
| other2 | Kanal 2 | 11/11 | 36.82 | -95.73 | 0.72 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.03 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.12 | 0.11 | 0.02 |
| led | Kanal 3 | 11/11 | 4.09 | 10.57 | 1.11 |
| mains50 | Kanal 3 | 11/11 | 457.87 | 210.85 | 0.22 |
| other1 | Kanal 3 | 11/11 | 48.95 | 8.19 | 0.20 |
| other2 | Kanal 3 | 11/11 | 93.27 | -106.34 | 0.40 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.03 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.12 | 0.14 | 0.02 |
| mains50 | Kanal 4 | 11/11 | 278.85 | -754.13 | 0.58 |
| other1 | Kanal 4 | 11/11 | 6.23 | -12.00 | 0.39 |
| other2 | Kanal 4 | 11/11 | 2.84 | -2.17 | 1.26 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.10 | 0.16 s (6.40 Hz) | 27.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.90 | 1.26 s (0.80 Hz) | 31.2 |
| Kanal 2 | breitbandig | 1.05 | 0.16 s (6.40 Hz) | 28.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.90 | 1.26 s (0.80 Hz) | 33.2 |
| Kanal 3 | breitbandig | 0.57 | 0.16 s (6.40 Hz) | 25.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.89 | 1.26 s (0.80 Hz) | 37.0 |
| Kanal 4 | breitbandig | 1.00 | 0.16 s (6.40 Hz) | 27.7 |
| Kanal 4 | 999.9 Hz ± 10 | 0.88 | 1.26 s (0.80 Hz) | 32.0 |

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
| Kanal 1 | 1.00 | 0.95 | 0.92 | 0.92 |
| Kanal 2 | 0.95 | 1.00 | 0.91 | 0.95 |
| Kanal 3 | 0.92 | 0.91 | 1.00 | 0.89 |
| Kanal 4 | 0.92 | 0.95 | 0.89 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](A5-b1d-r2-60s_psd.png)

### Kammprofile

![Kammprofile](A5-b1d-r2-60s_combs.png)

### Zeitverlauf

![Zeitverlauf](A5-b1d-r2-60s_timeline.png)
