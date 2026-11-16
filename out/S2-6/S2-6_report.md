# Report S2-6: S2-6 – acdc1, Eingänge offen, Gain 12 Uhr, USB direkt am Mac (ohne Hub)

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc1, Firmware v22.5.0 |
| test | Eingänge offen (nichts gesteckt), USB direkt am Mac (ohne Thunderbolt-Hub) |
| gain | g12 |
| usb | usb-stream, direkt am Mac |
| patch | Slot 1: ACDC (9,93 KB, Default-Patch) |
| Datei(en) | `20261114_acdc1_nohub_open-inputs_g12_usb-stream.4chan.000.4chan.000.wav` |
| Format | 96000 Hz, 119.4 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis S2-6 --ref S2-4` |

**Hinweise:**

- Datei hat 96000 Hz, oberhalb 24000 Hz ist nichts drin (-168 dB) → von 48000 Hz hochgerechnet.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.6 | -65.6 | -69.9 | -67.6 | -69.7 | -73.9 | -68.7 | -80.1 | -67.8 | 33 % | -69.5 | 1.7 |
| Kanal 2 | -5.8 | -68.8 | -73.1 | -70.8 | -73.0 | -76.9 | -72.0 | -83.0 | -71.0 | 34 % | -72.9 | 1.8 |
| Kanal 3 | -5.1 | -68.6 | -73.6 | -70.2 | -72.5 | -76.4 | -71.4 | -82.2 | -70.5 | 41 % | -72.8 | 2.3 |
| Kanal 4 | -4.7 | -69.4 | -73.7 | -71.4 | -73.5 | -77.8 | -72.5 | -83.9 | -71.6 | 35 % | -73.5 | 1.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.6 dB | -76.5 | 13.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.9908 | 0.0001 | 23/23 | k=1: 999.991 Hz, -75.3 dB | -75.2 | 18.2 % |
| Netz 50 Hz | Kanal 1 | 50.0206 | 0.0001 | 2/19 | k=1: 50.021 Hz, -90.6 dB | -92.8 | 0.3 % |
| Mischprodukte n·999.9908 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.9908 | 0.0012 | 126 | k=-4·f1+4·f2: 20000.037 Hz, -98.2 dB | -89.7 | 0.6 % |
| stärkste übrige Linie (119.94 Hz) | Kanal 1 | 119.9441 | 0.0068 | 17/199 | k=1: 119.943 Hz, -80.3 dB | -81.2 | 4.4 % |
| stärkste übrige Linie (179.92 Hz) | Kanal 1 | 179.9157 | 0.0119 | 6/132 | k=1: 179.915 Hz, -86.6 dB | -86.9 | 1.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.4 dB | -79.2 | 15.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.9908 | 0.0001 | 23/23 | k=1: 999.991 Hz, -78.6 dB | -78.5 | 18.1 % |
| Netz 50 Hz | Kanal 2 | 50.0207 | 0.0000 | 2/19 | k=1: 50.021 Hz, -94.1 dB | -96.2 | 0.3 % |
| Mischprodukte n·999.9908 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.9908 | 0.0011 | 134 | k=-4·f1+4·f2: 20000.037 Hz, -101.0 dB | -92.4 | 0.7 % |
| stärkste übrige Linie (119.94 Hz) | Kanal 2 | 119.9441 | 0.0063 | 23/199 | k=1: 119.943 Hz, -83.1 dB | -84.0 | 4.7 % |
| stärkste übrige Linie (179.92 Hz) | Kanal 2 | 179.9162 | 0.0083 | 6/132 | k=1: 179.915 Hz, -89.4 dB | -89.7 | 1.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -77.8 | 18.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.9908 | 0.0001 | 23/23 | k=1: 999.991 Hz, -77.5 dB | -77.3 | 21.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0012 | 9/10 | k=2: 4641.089 Hz, -123.4 dB | -120.0 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0206 | 0.0001 | 2/19 | k=1: 50.021 Hz, -93.3 dB | -95.4 | 0.3 % |
| Mischprodukte n·999.9908 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.9908 | 0.0011 | 142 | k=-4·f1+4·f2: 20000.037 Hz, -99.7 dB | -91.1 | 0.9 % |
| stärkste übrige Linie (119.94 Hz) | Kanal 3 | 119.9441 | 0.0056 | 28/199 | k=1: 119.943 Hz, -82.3 dB | -83.2 | 5.1 % |
| stärkste übrige Linie (179.92 Hz) | Kanal 3 | 179.9162 | 0.0072 | 8/132 | k=1: 179.916 Hz, -88.6 dB | -88.9 | 1.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.2 dB | -80.0 | 14.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.9908 | 0.0001 | 23/23 | k=1: 999.991 Hz, -78.9 dB | -78.7 | 19.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0016 | 8/10 | k=2: 4641.090 Hz, -124.1 dB | -121.2 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0206 | 0.0000 | 2/19 | k=1: 50.021 Hz, -95.5 dB | -97.5 | 0.3 % |
| Mischprodukte n·999.9908 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.9908 | 0.0012 | 132 | k=-4·f1+4·f2: 20000.037 Hz, -101.8 dB | -93.1 | 0.7 % |
| stärkste übrige Linie (119.94 Hz) | Kanal 4 | 119.9441 | 0.0065 | 20/199 | k=1: 119.943 Hz, -84.0 dB | -85.0 | 4.4 % |
| stärkste übrige Linie (179.92 Hz) | Kanal 4 | 179.9162 | 0.0084 | 6/132 | k=1: 179.915 Hz, -90.4 dB | -90.6 | 1.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -76.6 | 57.7 | fs8·1 |
| 999.991 | -75.3 | 48.7 | usb1k·1 |
| 1999.982 | -78.6 | 49.2 | usb1k·2 |
| 12000.000 | -79.2 | 57.8 | fs8·2 |
| 18000.000 | -79.5 | 58.8 | fs8·3 |
| 119.943 | -80.3 | 34.4 | other1·1 |
| 2999.972 | -82.5 | 47.9 | usb1k·3 |
| 4999.954 | -84.6 | 49.3 | usb1k·5 |
| 5999.945 | -85.5 | 48.8 | usb1k·6 |
| 179.915 | -86.6 | 29.8 | other2·1 |
| 299.859 | -87.7 | 30.4 | – |
| 75.721 | -87.2 | 29.2 | – |
| 6999.935 | -89.0 | 46.8 | usb1k·7 |
| 359.831 | -89.1 | 29.3 | other1·3 |
| 187.499 | -91.1 | 25.8 | – |
| 50.021 | -90.6 | 23.5 | mains50·1 |
| 8999.917 | -91.4 | 45.2 | usb1k·9 |
| 15999.853 | -91.5 | 46.6 | usb1k·16 |
| 19999.816 | -91.2 | 46.7 | usb1k·20 |
| 11999.889 | -91.8 | 45.3 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -79.4 | 58.8 | fs8·1 |
| 999.991 | -78.6 | 48.6 | usb1k·1 |
| 12000.000 | -81.9 | 59.4 | fs8·2 |
| 1999.982 | -82.0 | 49.2 | usb1k·2 |
| 18000.000 | -82.2 | 60.2 | fs8·3 |
| 119.943 | -83.1 | 34.5 | other1·1 |
| 2999.972 | -85.7 | 48.3 | usb1k·3 |
| 4999.954 | -87.9 | 50.0 | usb1k·5 |
| 5999.945 | -88.7 | 49.5 | usb1k·6 |
| 179.915 | -89.4 | 29.9 | other2·1 |
| 299.859 | -90.6 | 30.5 | – |
| 75.721 | -90.6 | 28.9 | – |
| 6999.935 | -92.1 | 47.8 | usb1k·7 |
| 359.831 | -92.0 | 29.5 | other1·3 |
| 187.499 | -94.0 | 25.9 | – |
| 15999.853 | -94.6 | 47.4 | usb1k·16 |
| 8999.917 | -94.8 | 45.9 | usb1k·9 |
| 50.021 | -94.1 | 23.1 | mains50·1 |
| 19999.816 | -94.2 | 48.0 | usb1k·20 |
| 59.992 | -95.0 | 22.0 | – |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -78.2 | 62.3 | fs8·1 |
| 999.991 | -77.5 | 49.4 | usb1k·1 |
| 12000.000 | -80.3 | 63.4 | fs8·2 |
| 18000.000 | -80.8 | 63.4 | fs8·3 |
| 1999.982 | -80.8 | 50.3 | usb1k·2 |
| 119.943 | -82.3 | 34.7 | other1·1 |
| 2999.972 | -84.7 | 49.5 | usb1k·3 |
| 4999.954 | -86.6 | 52.9 | usb1k·5 |
| 5999.945 | -87.5 | 53.0 | usb1k·6 |
| 179.916 | -88.6 | 30.0 | other2·1 |
| 299.859 | -89.7 | 30.6 | – |
| 6999.935 | -90.8 | 51.0 | usb1k·7 |
| 359.831 | -91.2 | 29.8 | other1·3 |
| 187.500 | -93.1 | 26.1 | – |
| 15999.853 | -93.3 | 50.6 | usb1k·16 |
| 8999.917 | -93.4 | 49.6 | usb1k·9 |
| 19999.816 | -93.0 | 50.8 | usb1k·20 |
| 11999.889 | -93.6 | 50.0 | usb1k·12 |
| 75.721 | -93.3 | 25.6 | – |
| 50.021 | -93.3 | 23.5 | mains50·1 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.991 | -78.9 | 49.1 | usb1k·1 |
| 6000.000 | -80.2 | 58.2 | fs8·1 |
| 1999.982 | -81.8 | 50.0 | usb1k·2 |
| 12000.000 | -82.5 | 58.2 | fs8·2 |
| 18000.000 | -82.9 | 58.9 | fs8·3 |
| 119.943 | -84.0 | 34.4 | other1·1 |
| 2999.972 | -86.0 | 48.6 | usb1k·3 |
| 4999.954 | -88.0 | 50.0 | usb1k·5 |
| 5999.945 | -88.8 | 49.6 | usb1k·6 |
| 179.915 | -90.4 | 29.9 | other2·1 |
| 299.859 | -91.5 | 30.4 | – |
| 6999.935 | -92.5 | 47.1 | usb1k·7 |
| 359.831 | -92.9 | 29.5 | other1·3 |
| 8999.917 | -94.5 | 45.9 | usb1k·9 |
| 187.500 | -94.9 | 25.9 | – |
| 15999.853 | -94.9 | 46.6 | usb1k·16 |
| 19999.816 | -94.7 | 47.1 | usb1k·20 |
| 11999.889 | -95.3 | 45.4 | usb1k·12 |
| 75.721 | -95.5 | 25.0 | – |
| 59.992 | -95.8 | 21.9 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 22/22 | 0.48 | -0.08 | 0.95 |
| usb1k | Kanal 1 | 22/22 | 1.86 | 0.12 | 0.41 |
| mains50 | Kanal 1 | 22/22 | 738.61 | 161.97 | 1.17 |
| other1 | Kanal 1 | 22/22 | 79.16 | 6.84 | 2.65 |
| other2 | Kanal 1 | 22/22 | 76.16 | 1.18 | 2.94 |
| fs8 | Kanal 2 | 22/22 | 0.46 | -0.07 | 0.89 |
| usb1k | Kanal 2 | 22/22 | 1.51 | -0.00 | 0.40 |
| mains50 | Kanal 2 | 22/22 | 919.48 | -242.69 | 1.23 |
| other1 | Kanal 2 | 22/22 | 79.66 | 6.96 | 2.64 |
| other2 | Kanal 2 | 22/22 | 88.88 | 9.44 | 2.95 |
| fs8 | Kanal 3 | 22/22 | 0.46 | -0.07 | 0.87 |
| usb1k | Kanal 3 | 22/22 | 1.40 | 0.28 | 0.40 |
| led | Kanal 3 | 22/22 | 3.16 | 1.52 | 1.41 |
| mains50 | Kanal 3 | 22/22 | 731.30 | 123.86 | 1.22 |
| other1 | Kanal 3 | 22/22 | 79.99 | 7.12 | 2.63 |
| other2 | Kanal 3 | 22/22 | 86.92 | 28.26 | 2.99 |
| fs8 | Kanal 4 | 22/22 | 0.48 | -0.08 | 0.94 |
| usb1k | Kanal 4 | 22/22 | 1.92 | 0.13 | 0.40 |
| led | Kanal 4 | 22/22 | 16.56 | -0.23 | 2.32 |
| mains50 | Kanal 4 | 22/22 | 724.71 | 13.17 | 1.32 |
| other1 | Kanal 4 | 22/22 | 78.45 | 6.44 | 2.64 |
| other2 | Kanal 4 | 22/22 | 87.84 | 7.39 | 2.96 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.38 | 0.16 s (6.39 Hz) | 21.5 |
| Kanal 1 | 1000.0 Hz ± 10 | 1.16 | 23.88 s (0.04 Hz) | 17.9 |
| Kanal 2 | breitbandig | 2.49 | 0.16 s (6.39 Hz) | 21.1 |
| Kanal 2 | 1000.0 Hz ± 10 | 1.17 | 0.31 s (3.19 Hz) | 18.9 |
| Kanal 3 | breitbandig | 2.50 | 4.26 s (0.23 Hz) | 20.9 |
| Kanal 3 | 1000.0 Hz ± 10 | 1.08 | 23.88 s (0.04 Hz) | 18.2 |
| Kanal 4 | breitbandig | 2.41 | 0.16 s (6.39 Hz) | 21.5 |
| Kanal 4 | 1000.0 Hz ± 10 | 1.10 | 0.30 s (3.30 Hz) | 18.1 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.97 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.98 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.94 |
| Kanal 4 | 0.97 | 0.98 | 0.94 | 1.00 |

## Vergleich mit Referenz S2-4

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -67.6 | -69.7 | +2.2 | 33 % | 60 % |
| Kanal 2 | -70.8 | -73.1 | +2.3 | 34 % | 67 % |
| Kanal 3 | -70.2 | -73.7 | +3.4 | 41 % | 81 % |
| Kanal 4 | -71.4 | -73.2 | +1.8 | 35 % | 67 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S2-6_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S2-6_psd.png)

### Kammprofile

![Kammprofile](S2-6_combs.png)

### Zeitverlauf

![Zeitverlauf](S2-6_timeline.png)

## Notiz aus dem Manifest

> Vergleich mit S2-4 (gleiches Modul, gleiche Einstellungen, aber am Thunderbolt-Hub).
