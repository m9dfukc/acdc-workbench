# Report A5-b1d-r1-60s: 

| Feld | Wert |
|---|---|
| Datei(en) | `_tmp_A5-b1d-r1-60s.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis reports/_tmp_A5-b1d-r1-60s.wav --name A5-b1d-r1-60s --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -70.8 | -76.4 | -72.1 | -73.4 | -85.1 | -72.7 | -93.4 | -72.2 | 63 % | -76.5 | 4.3 |
| Kanal 2 | -6.5 | -71.6 | -77.1 | -73.0 | -74.4 | -86.2 | -73.6 | -93.2 | -73.1 | 68 % | -78.1 | 5.0 |
| Kanal 3 | -4.8 | -74.0 | -83.0 | -74.6 | -76.0 | -89.9 | -75.0 | -97.1 | -74.6 | 79 % | -81.3 | 6.7 |
| Kanal 4 | -4.9 | -72.1 | -78.0 | -73.4 | -74.4 | -87.6 | -73.8 | -96.6 | -73.4 | 70 % | -78.6 | 5.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.4 | 19.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.2 | 39.5 % |
| Netz 50 Hz | Kanal 1 | 49.9731 | 0.0000 | 2/19 | k=1: 49.973 Hz, -93.7 dB | -96.2 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0008 | 143 | k=8·f1+1·f2: 13998.941 Hz, -96.5 dB | -86.1 | 4.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7175 | 0.0025 | 2/315 | k=1: 75.721 Hz, -90.0 dB | -93.4 | 0.8 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.3 | 23.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.9 dB | -77.2 | 39.1 % |
| Netz 50 Hz | Kanal 2 | 49.9731 | 0.0002 | 2/19 | k=1: 49.973 Hz, -94.4 dB | -96.9 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0009 | 152 | k=8·f1+1·f2: 13998.941 Hz, -96.4 dB | -86.0 | 5.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7174 | 0.0216 | 5/315 | k=1: 75.721 Hz, -89.8 dB | -93.2 | 1.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.6 dB | -79.6 | 31.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -77.4 dB | -78.6 | 39.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5449 | 0.0021 | 8/10 | k=1: 2320.547 Hz, -124.9 dB | -121.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9736 | 0.0228 | 6/19 | k=1: 49.973 Hz, -95.0 dB | -97.5 | 0.5 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0010 | 166 | k=8·f1+1·f2: 13998.941 Hz, -96.8 dB | -86.3 | 6.8 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7175 | 0.0250 | 5/315 | k=1: 75.721 Hz, -93.8 dB | -97.1 | 0.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.9 dB | -80.7 | 18.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.7 | 47.0 % |
| Netz 50 Hz | Kanal 4 | 49.9726 | 0.0008 | 2/19 | k=1: 49.973 Hz, -95.9 dB | -98.5 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0010 | 147 | k=8·f1+1·f2: 13998.941 Hz, -97.5 dB | -87.3 | 4.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7174 | 0.0210 | 5/315 | k=1: 75.721 Hz, -94.6 dB | -97.9 | 0.3 % |
| stärkste übrige Linie (13.79 Hz) | Kanal 4 | 13.7944 | 0.0006 | 3/1731 | k=1: 13.794 Hz, -99.3 dB | -102.3 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 56.7 | usb1k·1 |
| 6000.000 | -79.3 | 55.9 | fs8·1 |
| 18000.000 | -82.3 | 54.5 | fs8·3 |
| 12000.000 | -82.7 | 53.7 | fs8·2 |
| 1999.735 | -82.9 | 49.8 | usb1k·2 |
| 2999.603 | -83.3 | 50.9 | usb1k·3 |
| 6999.073 | -88.4 | 47.8 | usb1k·7 |
| 75.721 | -90.0 | 35.6 | other1·1 |
| 9998.676 | -92.3 | 44.0 | usb1k·10 |
| 15997.882 | -92.3 | 43.1 | usb1k·16 |
| 49.973 | -93.7 | 29.2 | mains50·1 |
| 10998.544 | -94.6 | 42.2 | usb1k·11 |
| 14998.014 | -95.1 | 41.2 | usb1k·15 |
| 5999.205 | -95.6 | 39.5 | usb1k·6 |
| 4999.339 | -96.4 | 38.3 | usb1k·5 |
| 13998.941 | -96.5 | 40.3 | imd·8·f1+1·f2 |
| 15999.470 | -96.9 | 38.5 | imd·4·f1+2·f2 |
| 9999.470 | -97.3 | 39.0 | imd·4·f1+1·f2 |
| 19998.941 | -97.3 | 40.3 | imd·8·f1+2·f2 |
| 16998.544 | -97.4 | 38.7 | imd·11·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.9 | 58.0 | usb1k·1 |
| 6000.000 | -79.3 | 57.2 | fs8·1 |
| 18000.000 | -82.2 | 56.6 | fs8·3 |
| 12000.000 | -82.5 | 55.4 | fs8·2 |
| 1999.735 | -83.9 | 50.5 | usb1k·2 |
| 2999.603 | -84.0 | 52.1 | usb1k·3 |
| 6999.073 | -88.7 | 49.0 | usb1k·7 |
| 75.721 | -89.8 | 37.3 | other1·1 |
| 9998.676 | -92.7 | 45.2 | usb1k·10 |
| 15997.882 | -92.8 | 43.7 | usb1k·16 |
| 10998.544 | -94.9 | 43.2 | usb1k·11 |
| 49.973 | -94.4 | 29.7 | mains50·1 |
| 14998.014 | -95.0 | 43.1 | usb1k·15 |
| 13998.941 | -96.4 | 41.8 | imd·8·f1+1·f2 |
| 15999.470 | -96.7 | 39.6 | imd·4·f1+2·f2 |
| 5999.205 | -96.8 | 39.8 | usb1k·6 |
| 9999.470 | -97.3 | 40.6 | imd·4·f1+1·f2 |
| 19998.941 | -97.3 | 41.9 | imd·8·f1+2·f2 |
| 16998.544 | -97.5 | 40.6 | imd·11·f1+1·f2 |
| 12999.073 | -97.7 | 40.6 | imd·7·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -77.4 | 60.2 | usb1k·1 |
| 6000.000 | -79.6 | 60.6 | fs8·1 |
| 18000.000 | -82.5 | 58.6 | fs8·3 |
| 12000.000 | -82.6 | 58.6 | fs8·2 |
| 2999.603 | -85.2 | 54.6 | usb1k·3 |
| 1999.735 | -85.6 | 53.5 | usb1k·2 |
| 6999.073 | -89.6 | 51.7 | usb1k·7 |
| 9998.676 | -93.3 | 47.5 | usb1k·10 |
| 15997.882 | -93.8 | 46.8 | usb1k·16 |
| 75.721 | -93.8 | 37.4 | other1·1 |
| 14998.014 | -95.1 | 46.1 | usb1k·15 |
| 10998.544 | -95.7 | 45.5 | usb1k·11 |
| 49.973 | -95.0 | 33.2 | mains50·1 |
| 13998.941 | -96.8 | 44.3 | imd·8·f1+1·f2 |
| 15999.470 | -97.1 | 43.3 | imd·4·f1+2·f2 |
| 9999.470 | -97.5 | 43.3 | imd·4·f1+1·f2 |
| 19998.941 | -97.6 | 44.4 | imd·8·f1+2·f2 |
| 16998.544 | -97.6 | 43.1 | imd·11·f1+1·f2 |
| 12999.073 | -97.8 | 43.7 | imd·7·f1+1·f2 |
| 5999.205 | -98.2 | 42.0 | usb1k·6 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 59.3 | usb1k·1 |
| 6000.000 | -80.9 | 56.4 | fs8·1 |
| 1999.735 | -82.3 | 52.8 | usb1k·2 |
| 18000.000 | -83.5 | 54.6 | fs8·3 |
| 12000.000 | -83.7 | 53.6 | fs8·2 |
| 2999.603 | -84.2 | 52.3 | usb1k·3 |
| 6999.073 | -89.2 | 48.5 | usb1k·7 |
| 15997.882 | -92.8 | 43.8 | usb1k·16 |
| 9998.676 | -93.3 | 44.8 | usb1k·10 |
| 4999.339 | -94.4 | 42.0 | usb1k·5 |
| 5999.205 | -95.4 | 41.8 | usb1k·6 |
| 10998.544 | -95.5 | 42.6 | usb1k·11 |
| 75.721 | -94.6 | 32.7 | other1·1 |
| 49.973 | -95.9 | 28.9 | mains50·1 |
| 14998.014 | -96.5 | 41.7 | usb1k·15 |
| 13998.941 | -97.5 | 40.5 | imd·8·f1+1·f2 |
| 15999.470 | -97.9 | 38.6 | imd·4·f1+2·f2 |
| 13998.146 | -98.1 | 40.0 | usb1k·14 |
| 9999.470 | -98.7 | 39.3 | imd·4·f1+1·f2 |
| 18997.485 | -98.2 | 40.2 | usb1k·19 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.01 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.05 | -0.06 | 0.04 |
| mains50 | Kanal 1 | 11/11 | 200.33 | 551.55 | 0.71 |
| other1 | Kanal 1 | 11/11 | 39.81 | 40.59 | 0.31 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.06 | -0.04 | 0.04 |
| mains50 | Kanal 2 | 11/11 | 189.25 | 574.52 | 0.61 |
| other1 | Kanal 2 | 11/11 | 5.17 | -9.72 | 0.29 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.05 | 0.02 | 0.03 |
| led | Kanal 3 | 11/11 | 5.24 | 4.14 | 1.89 |
| mains50 | Kanal 3 | 11/11 | 509.48 | 638.23 | 0.40 |
| other1 | Kanal 3 | 11/11 | 5.49 | 2.98 | 0.31 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.01 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.08 | -0.02 | 0.04 |
| mains50 | Kanal 4 | 11/11 | 217.67 | 590.34 | 0.52 |
| other1 | Kanal 4 | 11/11 | 6.00 | -13.51 | 0.38 |
| other2 | Kanal 4 | 11/11 | 167.87 | -111.26 | 4.78 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.15 | 0.16 s (6.40 Hz) | 28.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 1.26 s (0.80 Hz) | 30.2 |
| Kanal 2 | breitbandig | 1.12 | 0.16 s (6.40 Hz) | 29.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.91 | 1.26 s (0.80 Hz) | 31.9 |
| Kanal 3 | breitbandig | 0.61 | 0.16 s (6.40 Hz) | 25.2 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 1.26 s (0.80 Hz) | 35.8 |
| Kanal 4 | breitbandig | 1.08 | 0.16 s (6.40 Hz) | 28.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.89 | 1.26 s (0.80 Hz) | 31.5 |

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
| Kanal 1 | 1.00 | 0.95 | 0.91 | 0.92 |
| Kanal 2 | 0.95 | 1.00 | 0.91 | 0.95 |
| Kanal 3 | 0.91 | 0.91 | 1.00 | 0.89 |
| Kanal 4 | 0.92 | 0.95 | 0.89 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](A5-b1d-r1-60s_psd.png)

### Kammprofile

![Kammprofile](A5-b1d-r1-60s_combs.png)

### Zeitverlauf

![Zeitverlauf](A5-b1d-r1-60s_timeline.png)
