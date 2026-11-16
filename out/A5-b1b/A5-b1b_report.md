# Report A5-b1b: A5-b1b – acdc1 Build 1b, Eingänge offen, Gain 12 Uhr, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-14 |
| device | acdc1, Firmware Build 1b v22.4.r-thru1 (db9d3dd + Revert 237c63d) |
| test | Abnahme A5: Eingänge offen (nichts gesteckt), Vergleich mit S2-4 (alte Firmware) |
| gain | g12 |
| usb | usb-stream, Thunderbolt-Hub, Host-Software 48 kHz, Audio-Modul ohne Playback (Stille an die Ausgänge) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261114_acdc1_b1b-open-inputs_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 120.5 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis A5-b1b --ref S2-4` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.1 | -71.0 | -81.9 | -71.4 | -72.6 | -83.6 | -71.9 | -91.5 | -71.4 | 68 % | -76.4 | 4.9 |
| Kanal 2 | -6.4 | -71.8 | -83.1 | -72.2 | -73.3 | -85.3 | -72.6 | -92.1 | -72.2 | 73 % | -77.9 | 5.7 |
| Kanal 3 | -4.7 | -73.5 | -86.9 | -73.7 | -75.0 | -88.2 | -74.2 | -94.8 | -73.8 | 82 % | -81.3 | 7.5 |
| Kanal 4 | -5.6 | -71.1 | -82.5 | -71.4 | -72.4 | -85.2 | -71.8 | -95.3 | -71.4 | 74 % | -77.3 | 5.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.1 | 21.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8674 | 0.0001 | 23/23 | k=1: 999.867 Hz, -73.3 dB | -75.0 | 44.2 % |
| Netz 50 Hz | Kanal 1 | 50.0133 | 0.0066 | 5/19 | k=1: 50.015 Hz, -87.5 dB | -90.2 | 1.3 % |
| Mischprodukte n·999.8674 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8674 | 0.0004 | 147 | k=15·f1+1·f2: 20998.012 Hz, -101.0 dB | -91.0 | 1.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7194 | 0.0013 | 2/315 | k=1: 75.721 Hz, -89.4 dB | -92.6 | 0.8 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 1 | 44.7577 | 0.0002 | 3/533 | k=1: 44.758 Hz, -95.5 dB | -97.9 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.1 | 25.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8674 | 0.0001 | 23/23 | k=1: 999.867 Hz, -74.1 dB | -75.6 | 45.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0005 | 9/10 | k=8: 18564.359 Hz, -117.3 dB | -114.0 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0126 | 0.0063 | 5/19 | k=1: 50.015 Hz, -89.4 dB | -92.1 | 1.0 % |
| Mischprodukte n·999.8674 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8674 | 0.0004 | 154 | k=15·f1+1·f2: 20998.012 Hz, -101.0 dB | -91.0 | 1.3 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7220 | 0.0048 | 3/315 | k=1: 75.721 Hz, -89.5 dB | -92.6 | 0.9 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 2 | 89.5153 | 0.0060 | 4/266 | k=1: 89.516 Hz, -98.6 dB | -101.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.4 dB | -78.4 | 34.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8674 | 0.0001 | 23/23 | k=1: 999.867 Hz, -75.9 dB | -77.3 | 44.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.090 Hz, -124.4 dB | -120.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0147 | 0.0014 | 5/19 | k=1: 50.015 Hz, -90.7 dB | -93.4 | 1.1 % |
| Mischprodukte n·999.8674 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8674 | 0.0004 | 165 | k=15·f1+1·f2: 20998.012 Hz, -101.2 dB | -91.3 | 1.8 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7220 | 0.0054 | 3/315 | k=1: 75.721 Hz, -93.2 dB | -96.3 | 0.6 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 3 | 44.7583 | 0.0006 | 6/533 | k=1: 44.758 Hz, -97.9 dB | -100.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.3 | 20.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8674 | 0.0001 | 23/23 | k=1: 999.867 Hz, -72.6 dB | -74.3 | 51.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0010 | 10/10 | k=2: 4641.089 Hz, -123.6 dB | -118.7 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0148 | 0.0023 | 7/19 | k=1: 50.015 Hz, -87.5 dB | -90.2 | 1.3 % |
| Mischprodukte n·999.8674 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8674 | 0.0005 | 152 | k=15·f1+1·f2: 20998.012 Hz, -101.5 dB | -91.2 | 1.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7220 | 0.0040 | 5/315 | k=1: 75.721 Hz, -93.7 dB | -96.8 | 0.3 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 4 | 89.5166 | 0.0075 | 4/266 | k=1: 89.516 Hz, -97.7 dB | -100.6 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.3 | 61.4 | usb1k·1 |
| 6000.000 | -78.0 | 60.1 | fs8·1 |
| 12000.000 | -81.2 | 58.7 | fs8·2 |
| 18000.000 | -81.4 | 59.2 | fs8·3 |
| 1999.735 | -82.7 | 53.3 | usb1k·2 |
| 3999.470 | -84.3 | 53.4 | usb1k·4 |
| 4999.337 | -86.2 | 51.3 | usb1k·5 |
| 50.015 | -87.5 | 36.7 | mains50·1 |
| 7998.939 | -87.5 | 51.5 | usb1k·8 |
| 2999.602 | -89.8 | 45.9 | usb1k·3 |
| 75.721 | -89.4 | 36.3 | other1·1 |
| 11998.409 | -90.7 | 49.3 | usb1k·12 |
| 15997.879 | -91.2 | 49.1 | usb1k·16 |
| 18997.481 | -91.5 | 48.3 | usb1k·19 |
| 8998.807 | -92.6 | 46.8 | usb1k·9 |
| 10998.542 | -92.6 | 47.3 | usb1k·11 |
| 22996.951 | -95.2 | 47.0 | usb1k·23 |
| 44.758 | -95.5 | 27.4 | other2·1 |
| 16997.746 | -96.2 | 44.0 | usb1k·17 |
| 14998.012 | -96.5 | 43.9 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.1 | 62.3 | usb1k·1 |
| 6000.000 | -78.0 | 62.0 | fs8·1 |
| 12000.000 | -81.0 | 60.8 | fs8·2 |
| 18000.000 | -81.5 | 60.4 | fs8·3 |
| 1999.735 | -83.6 | 54.0 | usb1k·2 |
| 3999.470 | -84.6 | 54.7 | usb1k·4 |
| 4999.337 | -86.7 | 52.3 | usb1k·5 |
| 7998.939 | -87.8 | 53.1 | usb1k·8 |
| 50.015 | -89.4 | 36.8 | mains50·1 |
| 75.721 | -89.5 | 38.8 | other1·1 |
| 2999.602 | -90.9 | 46.6 | usb1k·3 |
| 11998.409 | -90.9 | 50.9 | usb1k·12 |
| 15997.879 | -91.5 | 50.4 | usb1k·16 |
| 18997.481 | -91.6 | 50.2 | usb1k·19 |
| 8998.807 | -93.0 | 48.1 | usb1k·9 |
| 10998.542 | -92.5 | 48.9 | usb1k·11 |
| 22996.951 | -95.5 | 48.3 | usb1k·23 |
| 14998.012 | -96.5 | 45.6 | usb1k·15 |
| 16997.746 | -96.6 | 45.4 | usb1k·17 |
| 19997.348 | -97.8 | 43.1 | usb1k·20 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.9 | 65.3 | usb1k·1 |
| 6000.000 | -78.4 | 65.3 | fs8·1 |
| 12000.000 | -81.1 | 63.9 | fs8·2 |
| 18000.000 | -81.7 | 63.4 | fs8·3 |
| 3999.470 | -85.5 | 57.8 | usb1k·4 |
| 1999.735 | -85.9 | 56.4 | usb1k·2 |
| 4999.337 | -88.3 | 55.0 | usb1k·5 |
| 7998.939 | -88.8 | 55.8 | usb1k·8 |
| 50.015 | -90.7 | 39.1 | mains50·1 |
| 18997.481 | -92.0 | 52.7 | usb1k·19 |
| 11998.409 | -91.6 | 53.4 | usb1k·12 |
| 15997.879 | -92.1 | 52.8 | usb1k·16 |
| 2999.602 | -93.1 | 49.0 | usb1k·3 |
| 10998.542 | -92.4 | 52.4 | usb1k·11 |
| 75.721 | -93.2 | 38.5 | other1·1 |
| 8998.807 | -94.0 | 50.6 | usb1k·9 |
| 22996.951 | -96.0 | 50.4 | usb1k·23 |
| 44.758 | -97.9 | 30.7 | other2·1 |
| 14998.012 | -97.3 | 47.9 | usb1k·15 |
| 16997.746 | -97.7 | 46.9 | usb1k·17 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.6 | 63.2 | usb1k·1 |
| 6000.000 | -78.2 | 60.9 | fs8·1 |
| 12000.000 | -81.2 | 59.2 | fs8·2 |
| 18000.000 | -81.9 | 58.9 | fs8·3 |
| 1999.735 | -81.2 | 55.9 | usb1k·2 |
| 3999.470 | -84.4 | 54.2 | usb1k·4 |
| 4999.337 | -85.3 | 52.6 | usb1k·5 |
| 50.015 | -87.5 | 38.8 | mains50·1 |
| 7998.939 | -86.9 | 53.1 | usb1k·8 |
| 2999.602 | -89.5 | 47.7 | usb1k·3 |
| 11998.409 | -90.4 | 50.1 | usb1k·12 |
| 15997.879 | -91.0 | 49.8 | usb1k·16 |
| 18997.481 | -91.5 | 49.1 | usb1k·19 |
| 8998.807 | -91.8 | 48.2 | usb1k·9 |
| 10998.542 | -92.9 | 47.6 | usb1k·11 |
| 75.721 | -93.7 | 34.8 | other1·1 |
| 22996.951 | -95.4 | 47.0 | usb1k·23 |
| 14998.012 | -95.6 | 45.2 | usb1k·15 |
| 16997.746 | -96.4 | 44.1 | usb1k·17 |
| 89.516 | -97.7 | 30.6 | other2·1 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 1 | 23/23 | 0.12 | 0.05 | 0.02 |
| mains50 | Kanal 1 | 23/23 | 274.30 | -15.04 | 0.48 |
| other1 | Kanal 1 | 23/23 | 38.71 | 4.68 | 0.51 |
| other2 | Kanal 1 | 23/23 | 110.23 | 2.39 | 1.00 |
| fs8 | Kanal 2 | 23/23 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 2 | 23/23 | 0.11 | 0.04 | 0.02 |
| led | Kanal 2 | 23/23 | 0.66 | -0.08 | 0.71 |
| mains50 | Kanal 2 | 23/23 | 295.14 | 63.96 | 0.49 |
| other1 | Kanal 2 | 23/23 | 19.18 | 6.69 | 0.41 |
| other2 | Kanal 2 | 23/23 | 257.25 | -4.47 | 0.66 |
| fs8 | Kanal 3 | 23/23 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 23/23 | 0.09 | 0.04 | 0.02 |
| led | Kanal 3 | 23/23 | 5.50 | -1.21 | 0.89 |
| mains50 | Kanal 3 | 23/23 | 150.23 | 24.52 | 0.39 |
| other1 | Kanal 3 | 23/23 | 9.65 | -2.67 | 0.36 |
| other2 | Kanal 3 | 23/23 | 0.65 | 0.28 | 0.49 |
| fs8 | Kanal 4 | 23/23 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 23/23 | 0.10 | 0.03 | 0.03 |
| led | Kanal 4 | 23/23 | 6.34 | -0.55 | 1.80 |
| mains50 | Kanal 4 | 23/23 | 120.74 | 40.01 | 0.38 |
| other1 | Kanal 4 | 23/23 | 75.41 | -7.51 | 0.48 |
| other2 | Kanal 4 | 23/23 | 223.25 | -90.29 | 0.51 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.59 | 0.63 s (1.59 Hz) | 18.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.45 | 7.53 s (0.13 Hz) | 31.9 |
| Kanal 2 | breitbandig | 0.54 | 0.63 s (1.59 Hz) | 22.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.44 | 7.53 s (0.13 Hz) | 32.7 |
| Kanal 3 | breitbandig | 0.40 | 0.63 s (1.59 Hz) | 27.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.42 | 7.53 s (0.13 Hz) | 36.5 |
| Kanal 4 | breitbandig | 0.52 | 0.63 s (1.59 Hz) | 21.7 |
| Kanal 4 | 999.9 Hz ± 10 | 0.43 | 7.53 s (0.13 Hz) | 33.5 |

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
| Kanal 1 | 1.00 | 0.94 | 0.93 | 0.92 |
| Kanal 2 | 0.94 | 1.00 | 0.92 | 0.95 |
| Kanal 3 | 0.93 | 0.92 | 1.00 | 0.90 |
| Kanal 4 | 0.92 | 0.95 | 0.90 | 1.00 |

## Vergleich mit Referenz S2-4

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.4 | -69.7 | -1.6 | 68 % | 60 % |
| Kanal 2 | -72.2 | -73.1 | +0.9 | 73 % | 67 % |
| Kanal 3 | -73.7 | -73.7 | -0.1 | 82 % | 81 % |
| Kanal 4 | -71.4 | -73.2 | +1.8 | 74 % | 67 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](A5-b1b_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](A5-b1b_psd.png)

### Kammprofile

![Kammprofile](A5-b1b_combs.png)

### Zeitverlauf

![Zeitverlauf](A5-b1b_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float nativ, Mehrkanal-Recorder. Datei-Werte enthalten den Host-Faktor 2 (messlog D7/D8), wie S2-4 und E7-ref.
