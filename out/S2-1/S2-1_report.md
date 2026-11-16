# Report S2-1: S2-1 – acdc2, Eingänge offen, Gain 12 Uhr, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc2 (DIY), Firmware v22.4.q |
| test | Eingänge offen (nichts gesteckt) |
| gain | g12 |
| usb | usb-stream |
| patch | Slot 1: ACDC (Default-Patch, Knob = digitaler Gain) |
| Datei(en) | `20261114_acdc2_open-inputs_g12_usb-stream.4chan.000.wav` |
| Format | 96000 Hz, 121.9 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis S2-1` |

**Hinweise:**

- Datei hat 96000 Hz, oberhalb 24000 Hz ist nichts drin (-168 dB) → von 48000 Hz hochgerechnet.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +8.5 | -71.8 | -85.4 | -72.0 | -73.3 | -82.9 | -72.5 | -94.5 | -72.0 | 79 % | -78.8 | 6.8 |
| Kanal 2 | +9.4 | -69.1 | -85.6 | -69.2 | -69.9 | -82.0 | -69.6 | -94.0 | -69.2 | 87 % | -78.0 | 8.7 |
| Kanal 3 | +4.1 | -69.2 | -86.2 | -69.3 | -70.1 | -82.4 | -69.6 | – | -69.3 | 84 % | -77.3 | 8.0 |
| Kanal 4 | +6.2 | -69.8 | -85.7 | -69.9 | -70.3 | -83.8 | -70.2 | -94.8 | -69.9 | 90 % | -79.8 | 9.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -77.8 dB | -77.7 | 27.0 % |
| 1-kHz-Kamm | Kanal 1 | 1000.0528 | 0.0001 | 23/23 | k=1: 1000.053 Hz, -75.9 dB | -75.7 | 42.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.9763 | 0.0003 | 10/10 | k=1: 2320.976 Hz, -110.9 dB | -106.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0336 | 0.0050 | 8/19 | k=1: 50.037 Hz, -83.8 dB | -85.6 | 4.4 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 1000.0528 | 0.0004 | 171 | k=8·f1+1·f2: 14000.423 Hz, -94.1 dB | -84.7 | 5.4 % |
| stärkste übrige Linie (35.38 Hz) | Kanal 1 | 35.3745 | 0.0029 | 4/675 | k=1: 35.375 Hz, -93.5 dB | -96.7 | 0.3 % |
| stärkste übrige Linie (55.85 Hz) | Kanal 1 | 55.8518 | 0.0094 | 5/427 | k=1: 55.852 Hz, -95.5 dB | -98.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -76.9 dB | -76.9 | 17.1 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0528 | 0.0001 | 23/23 | k=1: 1000.053 Hz, -70.6 dB | -71.2 | 63.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.9763 | 0.0003 | 10/10 | k=1: 2320.976 Hz, -109.3 dB | -105.1 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0337 | 0.0047 | 7/19 | k=1: 50.037 Hz, -82.9 dB | -84.6 | 2.9 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 1000.0528 | 0.0004 | 172 | k=8·f1+1·f2: 14000.423 Hz, -93.3 dB | -83.8 | 3.5 % |
| stärkste übrige Linie (55.85 Hz) | Kanal 2 | 55.8512 | 0.0006 | 2/427 | k=1: 55.852 Hz, -94.5 dB | -97.5 | 0.1 % |
| stärkste übrige Linie (35.37 Hz) | Kanal 2 | 35.3746 | 0.0025 | 5/675 | k=1: 35.375 Hz, -93.3 dB | -96.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -76.0 dB | -76.0 | 21.2 % |
| 1-kHz-Kamm | Kanal 3 | 1000.0528 | 0.0001 | 23/23 | k=1: 1000.053 Hz, -71.5 dB | -71.9 | 55.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.9763 | 0.0003 | 10/10 | k=1: 2320.976 Hz, -109.0 dB | -105.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0341 | 0.0064 | 7/19 | k=1: 50.037 Hz, -81.7 dB | -83.5 | 3.8 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 1000.0528 | 0.0004 | 171 | k=8·f1+1·f2: 14000.423 Hz, -92.5 dB | -83.0 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.8 dB | -78.7 | 13.1 % |
| 1-kHz-Kamm | Kanal 4 | 1000.0528 | 0.0001 | 23/23 | k=1: 1000.053 Hz, -70.6 dB | -71.4 | 71.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.9763 | 0.0002 | 10/10 | k=1: 2320.976 Hz, -110.7 dB | -106.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0337 | 0.0057 | 7/19 | k=1: 50.037 Hz, -84.8 dB | -86.6 | 2.2 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 1000.0528 | 0.0004 | 173 | k=8·f1+1·f2: 14000.423 Hz, -95.2 dB | -85.6 | 2.7 % |
| stärkste übrige Linie (35.38 Hz) | Kanal 4 | 35.3746 | 0.0024 | 6/675 | k=1: 35.375 Hz, -93.3 dB | -96.4 | 0.2 % |
| stärkste übrige Linie (55.85 Hz) | Kanal 4 | 55.8530 | 0.0040 | 3/427 | k=1: 55.852 Hz, -97.0 dB | -100.0 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -75.9 | 58.9 | usb1k·1 |
| 6000.000 | -77.8 | 62.6 | fs8·1 |
| 2000.106 | -78.5 | 58.9 | usb1k·2 |
| 18000.000 | -80.5 | 60.0 | fs8·3 |
| 12000.000 | -80.1 | 60.7 | fs8·2 |
| 3000.158 | -82.7 | 57.1 | usb1k·3 |
| 50.037 | -83.8 | 46.0 | mains50·1 |
| 7000.370 | -86.7 | 53.9 | usb1k·7 |
| 6000.317 | -89.9 | 50.4 | usb1k·6 |
| 12000.634 | -90.0 | 50.9 | usb1k·12 |
| 15000.792 | -90.6 | 50.1 | usb1k·15 |
| 8000.423 | -91.9 | 48.7 | usb1k·8 |
| 21001.109 | -91.4 | 48.7 | usb1k·21 |
| 11000.581 | -93.4 | 47.7 | usb1k·11 |
| 4000.211 | -92.9 | 47.2 | usb1k·4 |
| 20001.056 | -94.5 | 45.5 | usb1k·20 |
| 35.375 | -93.5 | 35.2 | other1·1 |
| 16000.845 | -94.0 | 46.8 | usb1k·16 |
| 10000.528 | -93.5 | 47.3 | usb1k·10 |
| 14000.423 | -94.1 | 46.7 | imd·8·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -70.6 | 63.3 | usb1k·1 |
| 2000.106 | -74.0 | 62.3 | usb1k·2 |
| 6000.000 | -76.9 | 62.7 | fs8·1 |
| 3000.158 | -79.0 | 59.8 | usb1k·3 |
| 18000.000 | -79.7 | 60.1 | fs8·3 |
| 12000.000 | -79.4 | 60.6 | fs8·2 |
| 50.037 | -82.9 | 44.9 | mains50·1 |
| 6000.317 | -85.4 | 54.2 | usb1k·6 |
| 7000.370 | -84.4 | 55.5 | usb1k·7 |
| 12000.634 | -89.5 | 50.5 | usb1k·12 |
| 21001.109 | -89.0 | 50.3 | usb1k·21 |
| 15000.792 | -89.9 | 49.9 | usb1k·15 |
| 13000.687 | -89.9 | 50.3 | usb1k·13 |
| 11000.581 | -91.2 | 48.9 | usb1k·11 |
| 5000.264 | -90.9 | 48.9 | usb1k·5 |
| 9000.475 | -91.2 | 48.8 | usb1k·9 |
| 16000.845 | -90.5 | 49.7 | usb1k·16 |
| 20001.056 | -91.6 | 47.6 | usb1k·20 |
| 10000.528 | -90.4 | 49.6 | usb1k·10 |
| 14000.739 | -92.7 | 47.1 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -71.5 | 61.2 | usb1k·1 |
| 2000.106 | -74.6 | 60.6 | usb1k·2 |
| 6000.000 | -76.0 | 62.7 | fs8·1 |
| 3000.158 | -79.3 | 58.5 | usb1k·3 |
| 18000.000 | -79.0 | 59.9 | fs8·3 |
| 12000.000 | -78.6 | 60.4 | fs8·2 |
| 50.037 | -81.7 | 48.3 | mains50·1 |
| 7000.370 | -84.2 | 54.5 | usb1k·7 |
| 6000.317 | -86.2 | 52.5 | usb1k·6 |
| 12000.634 | -88.6 | 50.4 | usb1k·12 |
| 15000.792 | -89.1 | 49.6 | usb1k·15 |
| 21001.109 | -89.0 | 49.4 | usb1k·21 |
| 11000.581 | -91.2 | 48.0 | usb1k·11 |
| 8000.423 | -91.1 | 47.9 | usb1k·8 |
| 20001.056 | -92.0 | 46.4 | usb1k·20 |
| 16000.845 | -91.1 | 47.8 | usb1k·16 |
| 9000.475 | -91.9 | 47.1 | usb1k·9 |
| 13000.687 | -90.9 | 48.2 | usb1k·13 |
| 10000.528 | -91.1 | 47.6 | usb1k·10 |
| 4000.211 | -92.6 | 45.7 | usb1k·4 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -70.6 | 65.1 | usb1k·1 |
| 2000.106 | -74.2 | 63.6 | usb1k·2 |
| 6000.000 | -78.8 | 62.6 | fs8·1 |
| 3000.158 | -79.5 | 60.9 | usb1k·3 |
| 18000.000 | -81.4 | 60.4 | fs8·3 |
| 12000.000 | -81.4 | 60.4 | fs8·2 |
| 50.037 | -84.8 | 44.5 | mains50·1 |
| 6000.317 | -85.4 | 56.0 | usb1k·6 |
| 7000.370 | -85.6 | 56.0 | usb1k·7 |
| 5000.264 | -88.9 | 52.3 | usb1k·5 |
| 21001.109 | -89.6 | 51.6 | usb1k·21 |
| 13000.687 | -90.2 | 51.6 | usb1k·13 |
| 9000.475 | -91.2 | 50.6 | usb1k·9 |
| 10000.528 | -90.2 | 51.6 | usb1k·10 |
| 12000.634 | -91.8 | 50.0 | usb1k·12 |
| 16000.845 | -91.3 | 50.8 | usb1k·16 |
| 20001.056 | -92.5 | 48.5 | usb1k·20 |
| 11000.581 | -92.4 | 49.3 | usb1k·11 |
| 15000.792 | -91.9 | 49.8 | usb1k·15 |
| 14000.739 | -92.7 | 49.2 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.03 | -0.00 | 0.02 |
| usb1k | Kanal 1 | 23/23 | 0.06 | 0.02 | 0.04 |
| led | Kanal 1 | 23/23 | 0.82 | -0.08 | 0.31 |
| mains50 | Kanal 1 | 23/23 | 399.63 | 207.40 | 0.16 |
| other1 | Kanal 1 | 23/23 | 43.73 | 6.10 | 0.27 |
| other2 | Kanal 1 | 23/23 | 10.62 | 11.25 | 0.58 |
| fs8 | Kanal 2 | 23/23 | 0.04 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 23/23 | 0.06 | 0.02 | 0.03 |
| led | Kanal 2 | 23/23 | 0.72 | -0.33 | 0.29 |
| mains50 | Kanal 2 | 23/23 | 436.12 | 89.44 | 0.20 |
| other1 | Kanal 2 | 23/23 | 1572.03 | 196.57 | 0.57 |
| other2 | Kanal 2 | 23/23 | 4.60 | 1.81 | 0.33 |
| fs8 | Kanal 3 | 23/23 | 0.04 | -0.00 | 0.02 |
| usb1k | Kanal 3 | 23/23 | 0.06 | 0.02 | 0.03 |
| led | Kanal 3 | 23/23 | 0.71 | -0.38 | 0.31 |
| mains50 | Kanal 3 | 23/23 | 169.68 | 173.20 | 0.15 |
| fs8 | Kanal 4 | 23/23 | 0.03 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 23/23 | 0.07 | 0.02 | 0.02 |
| led | Kanal 4 | 23/23 | 0.57 | -0.18 | 0.36 |
| mains50 | Kanal 4 | 23/23 | 172.36 | 158.08 | 0.21 |
| other1 | Kanal 4 | 23/23 | 3.01 | 1.70 | 0.45 |
| other2 | Kanal 4 | 23/23 | 17.50 | -0.69 | 0.79 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, 0,2–20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.53 | 3.13 s (0.32 Hz) | 32.9 |
| Kanal 1 | 1000.1 Hz ± 10 | 0.76 | 3.13 s (0.32 Hz) | 32.7 |
| Kanal 2 | breitbandig | 0.42 | 3.13 s (0.32 Hz) | 34.3 |
| Kanal 2 | 1000.1 Hz ± 10 | 0.67 | 3.13 s (0.32 Hz) | 32.3 |
| Kanal 3 | breitbandig | 0.43 | 3.13 s (0.32 Hz) | 35.5 |
| Kanal 3 | 1000.1 Hz ± 10 | 0.70 | 3.13 s (0.32 Hz) | 32.1 |
| Kanal 4 | breitbandig | 0.39 | 3.13 s (0.32 Hz) | 34.6 |
| Kanal 4 | 1000.1 Hz ± 10 | 0.65 | 3.13 s (0.32 Hz) | 32.7 |

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
| Kanal 1 | 1.00 | 0.92 | 0.95 | 0.88 |
| Kanal 2 | 0.92 | 1.00 | 0.97 | 0.95 |
| Kanal 3 | 0.95 | 0.97 | 1.00 | 0.94 |
| Kanal 4 | 0.88 | 0.95 | 0.94 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](S2-1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S2-1_psd.png)

### Kammprofile

![Kammprofile](S2-1_combs.png)

### Zeitverlauf

![Zeitverlauf](S2-1_timeline.png)
