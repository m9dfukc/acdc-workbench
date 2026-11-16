# Report A5-b1d-r1: A5-b1d-r1 – acdc1 Build 1d, Eingänge offen, Gain 12 Uhr, 120 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | A5-Wiederholung 1/2: Eingänge offen (nichts gesteckt), Sitzungsstreuung vor Build 2 |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul ohne Playback |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_b1d-open-inputs-r1_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 120.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis A5-b1d-r1 --ref A5-b1d` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -70.8 | -76.4 | -72.1 | -73.4 | -85.0 | -72.7 | -93.1 | -72.2 | 63 % | -76.5 | 4.3 |
| Kanal 2 | -6.5 | -71.7 | -77.3 | -73.0 | -74.4 | -86.3 | -73.6 | -92.6 | -73.1 | 68 % | -78.1 | 5.0 |
| Kanal 3 | -4.8 | -74.0 | -83.1 | -74.6 | -76.0 | -89.8 | -75.0 | -97.1 | -74.6 | 78 % | -81.3 | 6.7 |
| Kanal 4 | -4.9 | -72.1 | -78.2 | -73.4 | -74.4 | -87.6 | -73.8 | -96.5 | -73.4 | 69 % | -78.5 | 5.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.4 | 19.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -74.6 dB | -76.3 | 39.1 % |
| Netz 50 Hz | Kanal 1 | 49.9858 | 0.0008 | 2/19 | k=1: 49.985 Hz, -94.2 dB | -96.5 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0004 | 158 | k=8·f1+1·f2: 13998.941 Hz, -96.5 dB | -86.0 | 4.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7195 | 0.0013 | 2/315 | k=1: 75.721 Hz, -90.1 dB | -93.1 | 0.8 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.3 | 23.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -75.7 dB | -77.2 | 38.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=9: 20884.904 Hz, -117.2 dB | -114.0 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9857 | 0.0008 | 2/19 | k=1: 49.985 Hz, -94.9 dB | -97.1 | 0.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0003 | 164 | k=8·f1+1·f2: 13998.941 Hz, -96.3 dB | -86.0 | 5.2 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7206 | 0.0013 | 3/315 | k=1: 75.721 Hz, -90.1 dB | -93.1 | 1.0 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 2 | 89.5152 | 0.0021 | 4/266 | k=1: 89.515 Hz, -99.3 dB | -102.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.6 dB | -79.6 | 31.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -77.2 dB | -78.7 | 39.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0009 | 10/10 | k=1: 2320.545 Hz, -123.8 dB | -120.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9864 | 0.0028 | 6/19 | k=1: 49.985 Hz, -95.7 dB | -97.8 | 0.5 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0003 | 171 | k=8·f1+1·f2: 13998.941 Hz, -96.7 dB | -86.3 | 6.8 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7220 | 0.0012 | 3/315 | k=1: 75.721 Hz, -94.0 dB | -97.1 | 0.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.9 dB | -80.7 | 18.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.7 | 46.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0011 | 9/10 | k=1: 2320.545 Hz, -123.2 dB | -120.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9861 | 0.0009 | 3/19 | k=1: 49.985 Hz, -96.3 dB | -98.5 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0004 | 160 | k=8·f1+1·f2: 13998.941 Hz, -97.4 dB | -87.3 | 4.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7215 | 0.0010 | 3/315 | k=1: 75.721 Hz, -95.0 dB | -98.0 | 0.3 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 4 | 89.5152 | 0.0018 | 4/266 | k=1: 89.515 Hz, -99.1 dB | -101.9 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.6 | 59.7 | usb1k·1 |
| 6000.000 | -79.2 | 58.7 | fs8·1 |
| 18000.000 | -82.3 | 58.1 | fs8·3 |
| 12000.000 | -82.7 | 56.9 | fs8·2 |
| 1999.735 | -82.8 | 53.2 | usb1k·2 |
| 2999.603 | -83.3 | 53.3 | usb1k·3 |
| 6999.073 | -88.4 | 50.4 | usb1k·7 |
| 75.721 | -90.1 | 37.9 | other1·1 |
| 9998.676 | -92.4 | 47.2 | usb1k·10 |
| 15997.882 | -92.2 | 48.1 | usb1k·16 |
| 14998.014 | -95.1 | 44.5 | usb1k·15 |
| 49.985 | -94.2 | 31.7 | mains50·1 |
| 10998.544 | -94.4 | 45.4 | usb1k·11 |
| 4999.338 | -96.5 | 41.5 | usb1k·5 |
| 13998.941 | -96.5 | 43.7 | imd·8·f1+1·f2 |
| 5999.206 | -95.7 | 42.3 | usb1k·6 |
| 19998.941 | -97.2 | 43.4 | imd·8·f1+2·f2 |
| 15999.470 | -96.6 | 43.5 | imd·4·f1+2·f2 |
| 12999.073 | -97.6 | 42.5 | imd·7·f1+1·f2 |
| 9999.470 | -97.0 | 42.6 | imd·4·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.7 | 60.8 | usb1k·1 |
| 6000.000 | -79.3 | 60.2 | fs8·1 |
| 18000.000 | -82.2 | 59.9 | fs8·3 |
| 12000.000 | -82.5 | 58.9 | fs8·2 |
| 1999.735 | -83.9 | 54.1 | usb1k·2 |
| 2999.603 | -84.0 | 54.3 | usb1k·3 |
| 6999.073 | -88.7 | 51.6 | usb1k·7 |
| 75.721 | -90.1 | 39.4 | other1·1 |
| 9998.676 | -92.7 | 48.4 | usb1k·10 |
| 15997.882 | -92.6 | 49.2 | usb1k·16 |
| 14998.014 | -95.0 | 46.7 | usb1k·15 |
| 10998.544 | -94.7 | 46.8 | usb1k·11 |
| 49.985 | -94.9 | 32.3 | mains50·1 |
| 13998.941 | -96.3 | 45.5 | imd·8·f1+1·f2 |
| 15999.470 | -96.5 | 45.2 | imd·4·f1+2·f2 |
| 19998.941 | -97.2 | 45.0 | imd·8·f1+2·f2 |
| 12999.073 | -97.7 | 43.9 | imd·7·f1+1·f2 |
| 9999.470 | -97.0 | 44.1 | imd·4·f1+1·f2 |
| 5999.206 | -96.8 | 42.8 | usb1k·6 |
| 18997.484 | -97.6 | 44.6 | usb1k·19 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -77.2 | 63.3 | usb1k·1 |
| 6000.000 | -79.6 | 63.7 | fs8·1 |
| 18000.000 | -82.5 | 62.4 | fs8·3 |
| 12000.000 | -82.6 | 62.2 | fs8·2 |
| 2999.603 | -85.2 | 56.6 | usb1k·3 |
| 1999.735 | -85.6 | 56.8 | usb1k·2 |
| 6999.073 | -89.6 | 54.5 | usb1k·7 |
| 9998.676 | -93.4 | 51.3 | usb1k·10 |
| 75.721 | -94.0 | 39.6 | other1·1 |
| 15997.882 | -93.6 | 51.3 | usb1k·16 |
| 14998.014 | -95.1 | 49.4 | usb1k·15 |
| 10998.544 | -95.5 | 49.3 | usb1k·11 |
| 49.985 | -95.7 | 35.8 | mains50·1 |
| 13998.941 | -96.7 | 48.2 | imd·8·f1+1·f2 |
| 19998.941 | -97.5 | 47.3 | imd·8·f1+2·f2 |
| 15999.470 | -96.9 | 48.0 | imd·4·f1+2·f2 |
| 12999.073 | -97.8 | 47.0 | imd·7·f1+1·f2 |
| 9999.470 | -97.2 | 47.3 | imd·4·f1+1·f2 |
| 16998.544 | -97.5 | 47.1 | imd·11·f1+1·f2 |
| 14999.603 | -98.7 | 45.8 | imd·3·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 62.3 | usb1k·1 |
| 6000.000 | -80.9 | 59.0 | fs8·1 |
| 1999.735 | -82.2 | 56.4 | usb1k·2 |
| 18000.000 | -83.5 | 58.7 | fs8·3 |
| 12000.000 | -83.7 | 57.6 | fs8·2 |
| 2999.603 | -84.2 | 54.5 | usb1k·3 |
| 6999.073 | -89.2 | 51.5 | usb1k·7 |
| 9998.676 | -93.3 | 48.1 | usb1k·10 |
| 15997.882 | -92.6 | 48.9 | usb1k·16 |
| 4999.338 | -94.5 | 45.0 | usb1k·5 |
| 75.721 | -95.0 | 35.1 | other1·1 |
| 14998.014 | -96.5 | 45.4 | usb1k·15 |
| 10998.544 | -95.3 | 46.2 | usb1k·11 |
| 5999.206 | -95.3 | 44.6 | usb1k·6 |
| 49.985 | -96.3 | 31.6 | mains50·1 |
| 13998.941 | -97.4 | 44.2 | imd·8·f1+1·f2 |
| 15999.470 | -97.7 | 43.7 | imd·4·f1+2·f2 |
| 13998.146 | -98.0 | 43.7 | usb1k·14 |
| 19998.941 | -98.7 | 43.3 | imd·8·f1+2·f2 |
| 89.515 | -99.1 | 31.1 | other2·1 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.02 | -0.00 | 0.02 |
| usb1k | Kanal 1 | 23/23 | 0.11 | 0.01 | 0.04 |
| mains50 | Kanal 1 | 23/23 | 257.11 | 326.57 | 0.86 |
| other1 | Kanal 1 | 23/23 | 37.33 | -14.93 | 0.32 |
| fs8 | Kanal 2 | 23/23 | 0.02 | -0.00 | 0.01 |
| usb1k | Kanal 2 | 23/23 | 0.12 | 0.01 | 0.04 |
| led | Kanal 2 | 23/23 | 0.63 | 0.41 | 0.81 |
| mains50 | Kanal 2 | 23/23 | 221.52 | 298.49 | 0.74 |
| other1 | Kanal 2 | 23/23 | 22.37 | 6.05 | 0.26 |
| other2 | Kanal 2 | 23/23 | 6.73 | -1.52 | 1.16 |
| fs8 | Kanal 3 | 23/23 | 0.02 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 23/23 | 0.08 | 0.03 | 0.03 |
| led | Kanal 3 | 23/23 | 5.40 | 4.43 | 1.39 |
| mains50 | Kanal 3 | 23/23 | 495.99 | 165.84 | 0.50 |
| other1 | Kanal 3 | 23/23 | 17.74 | -3.34 | 0.30 |
| fs8 | Kanal 4 | 23/23 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 23/23 | 0.11 | 0.01 | 0.04 |
| led | Kanal 4 | 23/23 | 10.78 | 5.64 | 2.43 |
| mains50 | Kanal 4 | 23/23 | 309.86 | -84.18 | 0.74 |
| other1 | Kanal 4 | 23/23 | 185.08 | 121.11 | 0.35 |
| other2 | Kanal 4 | 23/23 | 14.09 | -3.22 | 0.96 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.18 | 0.16 s (6.39 Hz) | 32.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.56 | 1.25 s (0.80 Hz) | 32.0 |
| Kanal 2 | breitbandig | 1.12 | 0.16 s (6.39 Hz) | 33.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.54 | 1.25 s (0.80 Hz) | 33.7 |
| Kanal 3 | breitbandig | 0.63 | 0.16 s (6.39 Hz) | 28.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.53 | 1.25 s (0.80 Hz) | 37.9 |
| Kanal 4 | breitbandig | 1.07 | 0.16 s (6.39 Hz) | 32.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.52 | 1.25 s (0.80 Hz) | 32.5 |

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
| Kanal 2 | 0.95 | 1.00 | 0.91 | 0.94 |
| Kanal 3 | 0.92 | 0.91 | 1.00 | 0.89 |
| Kanal 4 | 0.92 | 0.94 | 0.89 | 1.00 |

## Vergleich mit Referenz A5-b1d

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.1 | -72.5 | +0.3 | 63 % | 57 % |
| Kanal 2 | -73.0 | -73.0 | -0.1 | 68 % | 66 % |
| Kanal 3 | -74.6 | -75.0 | +0.4 | 78 % | 74 % |
| Kanal 4 | -73.4 | -72.6 | -0.7 | 69 % | 64 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](A5-b1d-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](A5-b1d-r1_psd.png)

### Kammprofile

![Kammprofile](A5-b1d-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](A5-b1d-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float nativ, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 15:53–15:55.
