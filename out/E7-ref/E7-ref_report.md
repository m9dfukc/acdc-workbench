# Report E7-ref: E7-ref – acdc1 alte Firmware, Eingänge offen, Gain 12 Uhr, Playback auf 4 Ausgänge, 10 min

| Feld | Wert |
|---|---|
| date | 2026-11-14 |
| device | acdc1, Firmware wie Readback 20261114 (meldet v22.5.0, enthält 237c63d), nach Generalprobe D5 |
| test | Referenz für Klicks und Ausfälle vor Build 1 (E7, Aufbau wie A6): Eingänge offen, gleichzeitig Host-Playback (Sinus) auf Out 1–4 |
| gain | g12 |
| usb | usb-rxtx, Thunderbolt-Hub, Host-Software 48 kHz |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261114_acdc1_ref-10min_g12_usb-rxtx.4chan.000.wav` |
| Format | 48000 Hz, 600.9 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis E7-ref --ref S2-4` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.5 | -64.1 | -71.1 | -65.0 | -65.2 | -81.9 | -65.2 | -81.8 | -65.1 | 87 % | -74.1 | 8.9 |
| Kanal 2 | -5.4 | -69.1 | -77.4 | -69.9 | -70.1 | -85.0 | -70.1 | -83.0 | -70.1 | 88 % | -79.4 | 9.3 |
| Kanal 3 | -5.0 | -67.6 | -74.5 | -68.6 | -68.7 | -87.8 | -68.7 | -92.5 | -68.6 | 93 % | -80.4 | 11.8 |
| Kanal 4 | -4.2 | -70.5 | -81.6 | -70.9 | -71.1 | -85.8 | -71.1 | -84.1 | -71.1 | 87 % | -79.8 | 8.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.7 dB | -76.7 | 7.0 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0001 | 23/23 | k=1: 999.868 Hz, -71.6 dB | -73.4 | 14.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -68.4 dB | -67.0 | 64.8 % |
| Netz 50 Hz | Kanal 1 | 49.9933 | 0.0012 | 6/19 | k=1: 49.993 Hz, -95.4 dB | -94.5 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0001 | 174 | k=7·f1+2·f2: 18999.073 Hz, -99.9 dB | -89.8 | 0.3 % |
| stärkste übrige Linie (1060.00 Hz) | Kanal 1 | 1060.0024 | 0.0006 | 16/22 | k=1: 1060.002 Hz, -84.1 dB | -87.1 | 0.6 % |
| stärkste übrige Linie (330.00 Hz) | Kanal 1 | 329.9992 | 0.0006 | 71/72 | k=1: 329.999 Hz, -84.9 dB | -83.3 | 1.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -80.1 dB | -79.9 | 10.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0000 | 23/23 | k=1: 999.868 Hz, -75.8 dB | -77.6 | 17.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -73.6 dB | -72.3 | 59.5 % |
| Netz 50 Hz | Kanal 2 | 49.9933 | 0.0014 | 6/19 | k=1: 49.993 Hz, -99.2 dB | -98.3 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0001 | 175 | k=7·f1+2·f2: 18999.073 Hz, -103.1 dB | -93.1 | 0.5 % |
| stärkste übrige Linie (110.00 Hz) | Kanal 2 | 109.9997 | 0.0022 | 153/217 | k=5: 550.000 Hz, -87.2 dB | -83.8 | 4.0 % |
| stärkste übrige Linie (1060.00 Hz) | Kanal 2 | 1060.0024 | 0.0006 | 17/22 | k=1: 1060.002 Hz, -87.9 dB | -90.8 | 0.8 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -77.9 | 11.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0000 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.9 | 14.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -71.7 dB | -70.3 | 66.4 % |
| Netz 50 Hz | Kanal 3 | 49.9934 | 0.0014 | 8/19 | k=1: 49.993 Hz, -97.6 dB | -96.7 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0001 | 177 | k=7·f1+2·f2: 18999.073 Hz, -101.2 dB | -91.1 | 0.6 % |
| stärkste übrige Linie (1060.00 Hz) | Kanal 3 | 1060.0024 | 0.0001 | 13/22 | k=1: 1060.002 Hz, -92.5 dB | -95.4 | 0.2 % |
| stärkste übrige Linie (120.00 Hz) | Kanal 3 | 120.0033 | 0.0010 | 23/198 | k=1: 120.003 Hz, -92.3 dB | -95.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -81.2 dB | -81.0 | 10.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0000 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.9 | 26.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -75.4 dB | -74.1 | 49.6 % |
| Netz 50 Hz | Kanal 4 | 49.9933 | 0.0013 | 7/19 | k=1: 49.993 Hz, -100.6 dB | -99.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0001 | 174 | k=7·f1+2·f2: 18999.073 Hz, -104.0 dB | -94.0 | 0.5 % |
| stärkste übrige Linie (110.00 Hz) | Kanal 4 | 109.9997 | 0.0020 | 151/217 | k=5: 550.000 Hz, -87.7 dB | -85.0 | 3.9 % |
| stärkste übrige Linie (1060.00 Hz) | Kanal 4 | 1060.0024 | 0.0005 | 16/22 | k=1: 1060.002 Hz, -88.3 dB | -91.3 | 0.9 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 2320.545 | -68.4 | 76.9 | led·1 |
| 4641.090 | -69.3 | 76.9 | led·2 |
| 6961.634 | -71.3 | 75.1 | led·3 |
| 999.868 | -71.6 | 72.9 | usb1k·1 |
| 9282.179 | -74.0 | 72.4 | led·4 |
| 6000.000 | -76.7 | 69.7 | fs8·1 |
| 11602.724 | -77.4 | 69.4 | led·5 |
| 12000.000 | -79.5 | 67.2 | fs8·2 |
| 18000.000 | -79.7 | 66.5 | fs8·3 |
| 1999.735 | -80.0 | 63.6 | usb1k·2 |
| 2999.603 | -81.5 | 64.6 | usb1k·3 |
| 13923.269 | -82.3 | 64.6 | led·6 |
| 1060.002 | -84.1 | 60.8 | other1·1 |
| 329.999 | -84.9 | 59.0 | other2·1 |
| 1879.998 | -84.5 | 59.1 | – |
| 120.003 | -83.9 | 51.1 | – |
| 23205.448 | -86.0 | 62.8 | led·10 |
| 2360.011 | -85.0 | 60.1 | – |
| 109.999 | -86.0 | 49.7 | – |
| 550.000 | -85.6 | 54.2 | – |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 2320.545 | -73.6 | 76.7 | led·1 |
| 4641.090 | -74.6 | 76.8 | led·2 |
| 6961.634 | -76.7 | 74.8 | led·3 |
| 999.868 | -75.8 | 74.4 | usb1k·1 |
| 6000.000 | -80.1 | 71.3 | fs8·1 |
| 9282.179 | -79.5 | 72.0 | led·4 |
| 12000.000 | -82.6 | 69.2 | fs8·2 |
| 18000.000 | -82.9 | 68.5 | fs8·3 |
| 11602.724 | -83.0 | 69.1 | led·5 |
| 1999.735 | -84.3 | 64.7 | usb1k·2 |
| 2999.603 | -85.5 | 65.9 | usb1k·3 |
| 109.999 | -87.4 | 54.0 | other1·1 |
| 1060.002 | -87.9 | 62.3 | other2·1 |
| 550.000 | -87.2 | 58.6 | other1·5 |
| 120.003 | -87.6 | 53.4 | – |
| 13923.269 | -88.0 | 64.1 | led·6 |
| 1879.998 | -89.8 | 59.4 | – |
| 329.999 | -91.0 | 58.0 | other1·3 |
| 2360.011 | -90.0 | 60.0 | – |
| 23205.448 | -91.5 | 62.4 | led·10 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 2320.545 | -71.7 | 80.0 | led·1 |
| 4641.090 | -72.6 | 79.7 | led·2 |
| 6961.634 | -74.7 | 77.9 | led·3 |
| 999.868 | -75.2 | 75.4 | usb1k·1 |
| 9282.179 | -77.4 | 75.0 | led·4 |
| 6000.000 | -78.2 | 74.0 | fs8·1 |
| 12000.000 | -80.4 | 72.1 | fs8·2 |
| 18000.000 | -81.0 | 71.3 | fs8·3 |
| 11602.724 | -81.0 | 71.8 | led·5 |
| 1999.735 | -83.8 | 66.5 | usb1k·2 |
| 2999.603 | -84.6 | 67.5 | usb1k·3 |
| 13923.269 | -86.0 | 66.8 | led·6 |
| 23205.448 | -90.1 | 64.4 | led·10 |
| 20884.903 | -90.4 | 62.4 | led·9 |
| 6999.073 | -90.6 | 61.5 | usb1k·7 |
| 1060.002 | -92.5 | 58.6 | other1·1 |
| 4999.338 | -92.9 | 59.1 | usb1k·5 |
| 9998.676 | -92.0 | 60.2 | usb1k·10 |
| 120.003 | -92.3 | 49.9 | other2·1 |
| 75.721 | -92.6 | 46.8 | – |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 2320.545 | -75.4 | 74.8 | led·1 |
| 4641.090 | -76.3 | 74.7 | led·2 |
| 999.868 | -75.2 | 75.0 | usb1k·1 |
| 6961.634 | -78.4 | 72.9 | led·3 |
| 6000.000 | -81.2 | 70.0 | fs8·1 |
| 9282.179 | -81.3 | 69.8 | led·4 |
| 1999.735 | -82.6 | 66.6 | usb1k·2 |
| 12000.000 | -83.6 | 67.9 | fs8·2 |
| 18000.000 | -83.9 | 67.3 | fs8·3 |
| 11602.724 | -84.9 | 66.7 | led·5 |
| 2999.603 | -85.4 | 65.6 | usb1k·3 |
| 109.999 | -87.8 | 54.4 | other1·1 |
| 1060.002 | -88.3 | 61.7 | other2·1 |
| 550.000 | -87.7 | 59.0 | other1·5 |
| 120.003 | -88.0 | 53.9 | – |
| 4999.338 | -91.0 | 59.8 | usb1k·5 |
| 13923.269 | -90.1 | 61.6 | led·6 |
| 2360.011 | -90.9 | 59.0 | – |
| 6999.073 | -92.2 | 58.8 | usb1k·7 |
| 1879.998 | -91.5 | 57.9 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 119/119 | 0.01 | 0.00 | 0.07 |
| usb1k | Kanal 1 | 119/119 | 0.12 | 0.01 | 0.57 |
| led | Kanal 1 | 119/119 | 0.01 | -0.00 | 0.09 |
| mains50 | Kanal 1 | 119/119 | 265.16 | 29.56 | 0.30 |
| other1 | Kanal 1 | 119/119 | 1.25 | -0.00 | 0.06 |
| other2 | Kanal 1 | 119/119 | 1.55 | -0.09 | 0.66 |
| fs8 | Kanal 2 | 119/119 | 0.01 | 0.00 | 0.06 |
| usb1k | Kanal 2 | 119/119 | 0.09 | 0.01 | 0.19 |
| led | Kanal 2 | 119/119 | 0.01 | -0.00 | 0.10 |
| mains50 | Kanal 2 | 119/119 | 235.07 | 26.69 | 0.30 |
| other1 | Kanal 2 | 119/119 | 1.50 | -0.09 | 0.22 |
| other2 | Kanal 2 | 119/119 | 1.12 | -0.01 | 0.05 |
| fs8 | Kanal 3 | 119/119 | 0.01 | 0.00 | 0.05 |
| usb1k | Kanal 3 | 119/119 | 0.09 | 0.01 | 0.56 |
| led | Kanal 3 | 119/119 | 0.01 | -0.00 | 0.03 |
| mains50 | Kanal 3 | 119/119 | 240.41 | 23.70 | 0.24 |
| other1 | Kanal 3 | 119/119 | 1.67 | 0.00 | 0.08 |
| other2 | Kanal 3 | 119/119 | 1.99 | -0.13 | 0.87 |
| fs8 | Kanal 4 | 119/119 | 0.01 | 0.00 | 0.05 |
| usb1k | Kanal 4 | 119/119 | 0.09 | 0.01 | 0.12 |
| led | Kanal 4 | 119/119 | 0.01 | -0.00 | 0.12 |
| mains50 | Kanal 4 | 119/119 | 262.26 | 23.13 | 0.35 |
| other1 | Kanal 4 | 119/119 | 1.08 | -0.05 | 0.20 |
| other2 | Kanal 4 | 119/119 | 1.18 | -0.00 | 0.06 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.88 | 0.10 s (9.87 Hz) | 29.5 |
| Kanal 1 | 2320.5 Hz ± 10 | 0.24 | 0.09 s (10.55 Hz) | 36.9 |
| Kanal 2 | breitbandig | 0.74 | 1.26 s (0.79 Hz) | 30.0 |
| Kanal 2 | 2320.5 Hz ± 10 | 0.24 | 0.09 s (10.55 Hz) | 36.8 |
| Kanal 3 | breitbandig | 0.88 | 1.26 s (0.79 Hz) | 31.2 |
| Kanal 3 | 2320.5 Hz ± 10 | 0.21 | 0.09 s (10.55 Hz) | 30.8 |
| Kanal 4 | breitbandig | 0.51 | 1.26 s (0.79 Hz) | 31.5 |
| Kanal 4 | 2320.5 Hz ± 10 | 0.26 | 0.09 s (10.55 Hz) | 36.3 |

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
| Kanal 1 | 1.00 | 0.98 | 0.98 | 0.93 |
| Kanal 2 | 0.98 | 1.00 | 0.97 | 0.96 |
| Kanal 3 | 0.98 | 0.97 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz S2-4

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -65.0 | -69.7 | +4.7 | 87 % | 60 % |
| Kanal 2 | -69.9 | -73.1 | +3.2 | 88 % | 67 % |
| Kanal 3 | -68.6 | -73.7 | +5.1 | 93 % | 81 % |
| Kanal 4 | -70.9 | -73.2 | +2.3 | 87 % | 67 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](E7-ref_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](E7-ref_psd.png)

### Kammprofile

![Kammprofile](E7-ref_combs.png)

### Zeitverlauf

![Zeitverlauf](E7-ref_timeline.png)

## Notiz aus dem Manifest

> Aufgenommen in der Host-Software, 48 kHz / 32 Bit float nativ. Ausgänge nicht auf Eingänge gepatcht. Playback-Frequenzen je Ausgang nicht notiert, aus dem Spektrum bestimmt (siehe messlog).
