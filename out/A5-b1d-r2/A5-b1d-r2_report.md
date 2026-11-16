# Report A5-b1d-r2: A5-b1d-r2 – acdc1 Build 1d, Eingänge offen, Gain 12 Uhr, 120 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | A5-Wiederholung 2/2: wie r1, nach Neustart der Host-Software |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul ohne Playback |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_b1d-open-inputs-r2_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 120.1 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis A5-b1d-r2 --ref A5-b1d` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -71.0 | -77.5 | -72.1 | -73.4 | -84.9 | -72.7 | -92.2 | -72.2 | 63 % | -76.5 | 4.3 |
| Kanal 2 | -6.5 | -71.9 | -78.4 | -73.0 | -74.4 | -86.2 | -73.6 | -92.7 | -73.1 | 68 % | -78.1 | 5.0 |
| Kanal 3 | -4.8 | -74.1 | -84.1 | -74.6 | -76.0 | -89.6 | -75.0 | -95.7 | -74.6 | 78 % | -81.3 | 6.7 |
| Kanal 4 | -4.9 | -72.4 | -79.4 | -73.4 | -74.4 | -87.6 | -73.8 | -96.6 | -73.4 | 70 % | -78.5 | 5.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.4 | 19.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.2 | 39.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0013 | 8/10 | k=1: 2320.542 Hz, -121.7 dB | -119.0 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9682 | 0.0002 | 2/19 | k=1: 49.968 Hz, -94.0 dB | -96.2 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0005 | 161 | k=4·f1+2·f2: 15999.471 Hz, -96.6 dB | -86.1 | 4.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7195 | 0.0011 | 2/315 | k=1: 75.721 Hz, -90.0 dB | -93.2 | 0.8 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 1 | 44.7576 | 0.0031 | 6/533 | k=1: 44.758 Hz, -96.5 dB | -99.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.3 | 23.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -75.9 dB | -77.2 | 38.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=9: 20884.903 Hz, -117.2 dB | -113.7 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9652 | 0.0084 | 5/19 | k=1: 49.968 Hz, -94.8 dB | -96.9 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0004 | 165 | k=8·f1+1·f2: 13998.941 Hz, -96.4 dB | -86.0 | 5.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7195 | 0.0049 | 3/315 | k=1: 75.721 Hz, -89.9 dB | -93.1 | 1.0 % |
| stärkste übrige Linie (89.51 Hz) | Kanal 2 | 89.5152 | 0.0040 | 4/266 | k=1: 89.515 Hz, -99.9 dB | -102.9 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.6 dB | -79.6 | 31.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -77.5 dB | -78.7 | 39.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.544 Hz, -124.0 dB | -119.9 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9698 | 0.0043 | 5/19 | k=1: 49.968 Hz, -95.4 dB | -97.6 | 0.5 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0003 | 170 | k=8·f1+1·f2: 13998.941 Hz, -96.9 dB | -86.3 | 6.7 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7200 | 0.0008 | 2/315 | k=1: 75.721 Hz, -93.8 dB | -97.1 | 0.6 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 3 | 44.7570 | 0.0015 | 4/533 | k=1: 44.758 Hz, -99.2 dB | -101.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.8 dB | -80.7 | 18.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.7 | 46.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0011 | 9/10 | k=1: 2320.543 Hz, -122.3 dB | -118.9 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9682 | 0.0003 | 2/19 | k=1: 49.969 Hz, -96.5 dB | -98.6 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0004 | 163 | k=8·f1+1·f2: 13998.941 Hz, -97.6 dB | -87.4 | 4.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7202 | 0.0082 | 4/315 | k=1: 75.721 Hz, -94.7 dB | -97.9 | 0.3 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 4 | 89.5182 | 0.0039 | 5/266 | k=1: 89.515 Hz, -99.5 dB | -102.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 60.0 | usb1k·1 |
| 6000.000 | -79.2 | 59.0 | fs8·1 |
| 18000.000 | -82.3 | 57.9 | fs8·3 |
| 12000.000 | -82.7 | 57.3 | fs8·2 |
| 1999.735 | -82.8 | 53.8 | usb1k·2 |
| 2999.603 | -83.2 | 53.8 | usb1k·3 |
| 6999.073 | -88.4 | 50.3 | usb1k·7 |
| 75.721 | -90.0 | 37.9 | other1·1 |
| 9998.676 | -92.4 | 47.4 | usb1k·10 |
| 15997.882 | -92.2 | 47.6 | usb1k·16 |
| 49.968 | -94.0 | 31.8 | mains50·1 |
| 10998.544 | -94.6 | 45.1 | usb1k·11 |
| 14998.014 | -94.8 | 44.5 | usb1k·15 |
| 5999.206 | -95.6 | 42.6 | usb1k·6 |
| 13998.941 | -96.7 | 43.4 | imd·8·f1+1·f2 |
| 18997.485 | -97.4 | 42.6 | usb1k·19 |
| 16998.544 | -97.4 | 42.7 | imd·11·f1+1·f2 |
| 19998.941 | -97.3 | 42.9 | imd·8·f1+2·f2 |
| 4999.338 | -96.1 | 42.1 | usb1k·5 |
| 15999.471 | -96.6 | 43.3 | imd·4·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.9 | 60.8 | usb1k·1 |
| 6000.000 | -79.3 | 60.7 | fs8·1 |
| 18000.000 | -82.2 | 59.6 | fs8·3 |
| 12000.000 | -82.5 | 59.1 | fs8·2 |
| 1999.735 | -83.9 | 54.3 | usb1k·2 |
| 2999.603 | -83.9 | 54.6 | usb1k·3 |
| 6999.073 | -88.7 | 51.6 | usb1k·7 |
| 75.721 | -89.9 | 39.6 | other1·1 |
| 9998.676 | -92.7 | 48.5 | usb1k·10 |
| 15997.882 | -92.7 | 48.9 | usb1k·16 |
| 49.968 | -94.8 | 32.3 | mains50·1 |
| 10998.544 | -94.8 | 46.6 | usb1k·11 |
| 14998.014 | -94.7 | 46.4 | usb1k·15 |
| 13998.941 | -96.4 | 45.3 | imd·8·f1+1·f2 |
| 19998.941 | -97.3 | 44.7 | imd·8·f1+2·f2 |
| 16998.544 | -97.4 | 44.3 | imd·11·f1+1·f2 |
| 15999.471 | -96.5 | 45.2 | imd·4·f1+2·f2 |
| 18997.485 | -97.7 | 44.0 | usb1k·19 |
| 5999.206 | -96.8 | 43.3 | usb1k·6 |
| 12999.868 | -98.2 | 43.2 | imd·1·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -77.5 | 63.5 | usb1k·1 |
| 6000.000 | -79.6 | 63.9 | fs8·1 |
| 18000.000 | -82.5 | 62.1 | fs8·3 |
| 12000.000 | -82.5 | 62.5 | fs8·2 |
| 2999.603 | -85.1 | 57.5 | usb1k·3 |
| 1999.735 | -85.6 | 57.2 | usb1k·2 |
| 6999.073 | -89.6 | 54.5 | usb1k·7 |
| 9998.676 | -93.4 | 51.1 | usb1k·10 |
| 15997.882 | -93.7 | 50.9 | usb1k·16 |
| 75.721 | -93.8 | 40.2 | other1·1 |
| 49.968 | -95.4 | 35.9 | mains50·1 |
| 10998.544 | -95.7 | 49.2 | usb1k·11 |
| 14998.014 | -94.9 | 49.5 | usb1k·15 |
| 13998.941 | -96.9 | 48.1 | imd·8·f1+1·f2 |
| 19998.941 | -97.5 | 47.2 | imd·8·f1+2·f2 |
| 16998.544 | -97.7 | 47.0 | imd·11·f1+1·f2 |
| 15999.471 | -96.9 | 47.8 | imd·4·f1+2·f2 |
| 18997.485 | -98.2 | 46.2 | usb1k·19 |
| 12999.073 | -97.9 | 46.6 | imd·7·f1+1·f2 |
| 9999.471 | -97.3 | 47.1 | imd·4·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 62.1 | usb1k·1 |
| 6000.000 | -80.8 | 59.6 | fs8·1 |
| 1999.735 | -82.2 | 56.6 | usb1k·2 |
| 18000.000 | -83.5 | 58.2 | fs8·3 |
| 12000.000 | -83.7 | 58.0 | fs8·2 |
| 2999.603 | -84.2 | 54.9 | usb1k·3 |
| 6999.073 | -89.2 | 51.0 | usb1k·7 |
| 9998.676 | -93.3 | 48.3 | usb1k·10 |
| 15997.882 | -92.6 | 48.7 | usb1k·16 |
| 10998.544 | -95.4 | 45.9 | usb1k·11 |
| 4999.338 | -94.2 | 45.5 | usb1k·5 |
| 75.721 | -94.7 | 35.4 | other1·1 |
| 5999.206 | -95.3 | 45.1 | usb1k·6 |
| 49.969 | -96.5 | 31.2 | mains50·1 |
| 14998.014 | -96.2 | 44.9 | usb1k·15 |
| 13998.941 | -97.6 | 43.7 | imd·8·f1+1·f2 |
| 18997.485 | -98.4 | 43.2 | usb1k·19 |
| 15999.471 | -97.7 | 43.8 | imd·4·f1+2·f2 |
| 16998.544 | -98.8 | 43.3 | imd·11·f1+1·f2 |
| 19998.941 | -98.8 | 43.1 | imd·8·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.02 | -0.00 | 0.04 |
| usb1k | Kanal 1 | 23/23 | 0.16 | 0.04 | 0.03 |
| led | Kanal 1 | 23/23 | 10.02 | 1.92 | 1.68 |
| mains50 | Kanal 1 | 23/23 | 238.50 | 178.05 | 0.41 |
| other1 | Kanal 1 | 23/23 | 43.63 | 1.94 | 0.29 |
| other2 | Kanal 1 | 23/23 | 7.49 | 3.53 | 0.73 |
| fs8 | Kanal 2 | 23/23 | 0.02 | -0.00 | 0.03 |
| usb1k | Kanal 2 | 23/23 | 0.13 | 0.03 | 0.05 |
| led | Kanal 2 | 23/23 | 0.44 | 0.09 | 0.49 |
| mains50 | Kanal 2 | 23/23 | 613.83 | 537.83 | 0.37 |
| other1 | Kanal 2 | 23/23 | 21.42 | 6.99 | 0.25 |
| other2 | Kanal 2 | 23/23 | 6.80 | 1.17 | 0.93 |
| fs8 | Kanal 3 | 23/23 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 3 | 23/23 | 0.10 | 0.03 | 0.03 |
| led | Kanal 3 | 23/23 | 3.59 | 0.53 | 0.94 |
| mains50 | Kanal 3 | 23/23 | 306.55 | 200.57 | 0.26 |
| other1 | Kanal 3 | 23/23 | 40.03 | -15.87 | 0.24 |
| other2 | Kanal 3 | 23/23 | 54.94 | 7.98 | 0.78 |
| fs8 | Kanal 4 | 23/23 | 0.02 | -0.00 | 0.03 |
| usb1k | Kanal 4 | 23/23 | 0.12 | 0.04 | 0.05 |
| led | Kanal 4 | 23/23 | 7.68 | 1.70 | 1.61 |
| mains50 | Kanal 4 | 23/23 | 220.28 | 186.85 | 0.75 |
| other1 | Kanal 4 | 23/23 | 374.38 | 144.00 | 0.32 |
| other2 | Kanal 4 | 23/23 | 211.54 | 53.48 | 0.69 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.07 | 0.16 s (6.40 Hz) | 30.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.70 | 1.26 s (0.79 Hz) | 32.9 |
| Kanal 2 | breitbandig | 1.02 | 0.16 s (6.40 Hz) | 31.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.69 | 1.26 s (0.79 Hz) | 34.6 |
| Kanal 3 | breitbandig | 0.56 | 0.16 s (6.40 Hz) | 27.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.67 | 1.26 s (0.79 Hz) | 38.6 |
| Kanal 4 | breitbandig | 0.95 | 0.16 s (6.40 Hz) | 30.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.67 | 1.26 s (0.79 Hz) | 33.6 |

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
| Kanal 2 | 0.94 | 1.00 | 0.91 | 0.94 |
| Kanal 3 | 0.92 | 0.91 | 1.00 | 0.89 |
| Kanal 4 | 0.92 | 0.94 | 0.89 | 1.00 |

## Vergleich mit Referenz A5-b1d

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.1 | -72.5 | +0.3 | 63 % | 57 % |
| Kanal 2 | -73.0 | -73.0 | -0.1 | 68 % | 66 % |
| Kanal 3 | -74.6 | -75.0 | +0.4 | 78 % | 74 % |
| Kanal 4 | -73.4 | -72.6 | -0.7 | 70 % | 64 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](A5-b1d-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](A5-b1d-r2_psd.png)

### Kammprofile

![Kammprofile](A5-b1d-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](A5-b1d-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float nativ, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 15:55–15:57, Host-Software vorher neu gestartet.
