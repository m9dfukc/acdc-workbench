# Report S3-d-in: S3-d-in – acdc1 Eingänge offen, Host-Software Duplex, Mac-Port, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | S3-d, Gegenseite: AC/DC-Eingänge 1–4 (offen) in der Host-Software, Duplex, Out 1 am Startup |
| gain | g12 |
| usb | usb-duplex, Mac-Port |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_s3d-in-vcv_g12_usb-duplex.4chan.000.wav` |
| Format | 48000 Hz, 120.5 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-d-in --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -64.2 | -69.0 | -66.0 | -69.1 | -70.9 | -67.9 | -79.1 | -66.2 | 6 % | -66.5 | 0.3 |
| Kanal 2 | -6.8 | -64.4 | -69.3 | -66.1 | -69.2 | -71.0 | -68.0 | -79.2 | -66.3 | 6 % | -66.6 | 0.3 |
| Kanal 3 | -5.0 | -65.5 | -70.3 | -67.3 | -70.4 | -72.0 | -69.2 | -79.9 | -67.5 | 8 % | -67.9 | 0.4 |
| Kanal 4 | -5.2 | -65.9 | -70.7 | -67.7 | -70.7 | -72.6 | -69.6 | -80.7 | -67.9 | 7 % | -68.2 | 0.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0044 | 0.0004 | 3/3 | k=1: 6000.005 Hz, -82.5 dB | -81.8 | 2.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.9895 | 0.0059 | 23/23 | k=1: 999.987 Hz, -82.4 dB | -81.1 | 3.2 % |
| Mischprodukte n·999.9895 + m·6000.0044 Hz (m = ±1…±4) | Kanal 1 | 999.9895 | 0.0044 | 62 | k=-9·f1+2·f2: 3000.098 Hz, -98.6 dB | -88.9 | 0.5 % |
| stärkste übrige Linie (59.96 Hz) | Kanal 1 | 59.9720 | 0.0078 | 50/398 | k=1: 59.965 Hz, -83.5 dB | -80.3 | 3.7 % |
| stärkste übrige Linie (1000.03 Hz) | Kanal 1 | 1000.0304 | 0.0094 | 13/23 | k=1: 1000.032 Hz, -83.7 dB | -85.2 | 1.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0044 | 0.0004 | 3/3 | k=1: 6000.005 Hz, -82.3 dB | -81.7 | 2.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.9895 | 0.0060 | 23/23 | k=1: 999.987 Hz, -82.8 dB | -81.5 | 3.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5441 | 0.0054 | 9/10 | k=10: 23205.451 Hz, -117.5 dB | -111.7 | 0.0 % |
| Mischprodukte n·999.9895 + m·6000.0044 Hz (m = ±1…±4) | Kanal 2 | 999.9895 | 0.0045 | 68 | k=-9·f1+2·f2: 3000.098 Hz, -98.7 dB | -88.8 | 0.6 % |
| stärkste übrige Linie (59.96 Hz) | Kanal 2 | 59.9720 | 0.0078 | 51/398 | k=1: 59.965 Hz, -83.7 dB | -80.4 | 3.7 % |
| stärkste übrige Linie (1000.03 Hz) | Kanal 2 | 1000.0305 | 0.0095 | 13/23 | k=1: 1000.032 Hz, -83.7 dB | -85.3 | 1.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0044 | 0.0004 | 3/3 | k=1: 6000.005 Hz, -82.7 dB | -81.9 | 3.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.9895 | 0.0059 | 23/23 | k=1: 999.987 Hz, -82.8 dB | -81.5 | 4.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5450 | 0.0061 | 9/10 | k=2: 4641.085 Hz, -120.6 dB | -117.2 | 0.0 % |
| Mischprodukte n·999.9895 + m·6000.0044 Hz (m = ±1…±4) | Kanal 3 | 999.9895 | 0.0046 | 70 | k=4·f1+2·f2: 15999.959 Hz, -98.9 dB | -89.0 | 0.7 % |
| stärkste übrige Linie (59.96 Hz) | Kanal 3 | 59.9720 | 0.0074 | 56/398 | k=1: 59.965 Hz, -84.5 dB | -81.2 | 4.1 % |
| stärkste übrige Linie (1000.03 Hz) | Kanal 3 | 1000.0340 | 0.0098 | 14/23 | k=1: 1000.032 Hz, -84.6 dB | -86.0 | 1.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0044 | 0.0004 | 3/3 | k=1: 6000.005 Hz, -83.5 dB | -82.9 | 3.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.9895 | 0.0058 | 23/23 | k=1: 999.987 Hz, -83.3 dB | -82.2 | 3.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0058 | 9/10 | k=2: 4641.085 Hz, -119.2 dB | -116.0 | 0.0 % |
| Mischprodukte n·999.9895 + m·6000.0044 Hz (m = ±1…±4) | Kanal 4 | 999.9895 | 0.0046 | 68 | k=-9·f1+2·f2: 3000.098 Hz, -100.1 dB | -90.0 | 0.6 % |
| stärkste übrige Linie (1000.03 Hz) | Kanal 4 | 1000.0340 | 0.0100 | 14/23 | k=1: 1000.032 Hz, -85.1 dB | -86.6 | 1.3 % |
| stärkste übrige Linie (59.96 Hz) | Kanal 4 | 59.9720 | 0.0079 | 51/398 | k=1: 59.965 Hz, -85.3 dB | -82.0 | 3.7 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.987 | -82.4 | 39.5 | usb1k·1 |
| 6000.005 | -82.5 | 50.3 | fs8·1 |
| 59.965 | -83.5 | 26.4 | other1·1 |
| 1000.032 | -83.7 | 38.2 | other2·1 |
| 374.926 | -85.7 | 28.3 | – |
| 17999.995 | -84.9 | 52.4 | – |
| 14.001 | -85.3 | 18.0 | – |
| 187.463 | -84.8 | 27.2 | – |
| 12.002 | -85.2 | 17.2 | – |
| 29.152 | -86.2 | 21.5 | – |
| 1999.975 | -85.8 | 39.0 | usb1k·2 |
| 119.947 | -86.8 | 24.5 | other1·2 |
| 29.199 | -87.7 | 20.0 | – |
| 58.396 | -87.6 | 22.0 | – |
| 16.002 | -87.4 | 16.7 | – |
| 12000.008 | -88.7 | 46.9 | fs8·2 |
| 58.373 | -88.7 | 21.0 | – |
| 359.825 | -89.1 | 25.1 | other1·6 |
| 87.548 | -89.7 | 22.1 | – |
| 179.917 | -89.7 | 21.9 | other1·3 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.987 | -82.8 | 39.2 | usb1k·1 |
| 6000.005 | -82.3 | 50.8 | fs8·1 |
| 59.965 | -83.7 | 26.2 | other1·1 |
| 1000.032 | -83.7 | 38.3 | other2·1 |
| 374.926 | -85.7 | 28.1 | – |
| 17999.995 | -84.9 | 53.3 | – |
| 14.001 | -85.4 | 18.1 | – |
| 12.002 | -85.3 | 17.3 | – |
| 187.463 | -85.0 | 26.8 | – |
| 29.152 | -86.3 | 21.4 | – |
| 119.948 | -86.9 | 24.2 | other1·2 |
| 1999.975 | -86.7 | 38.3 | usb1k·2 |
| 29.199 | -87.9 | 19.7 | – |
| 58.396 | -87.8 | 21.9 | – |
| 16.002 | -87.4 | 16.9 | – |
| 12000.008 | -88.4 | 47.7 | fs8·2 |
| 58.373 | -88.7 | 21.0 | – |
| 359.825 | -89.2 | 24.8 | other1·6 |
| 1124.794 | -89.7 | 33.2 | – |
| 87.548 | -89.9 | 21.9 | – |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.987 | -82.8 | 40.1 | usb1k·1 |
| 6000.005 | -82.7 | 52.2 | fs8·1 |
| 59.965 | -84.5 | 26.8 | other1·1 |
| 1000.032 | -84.6 | 38.4 | other2·1 |
| 17999.995 | -85.0 | 54.6 | – |
| 374.926 | -86.5 | 29.2 | – |
| 1999.975 | -86.2 | 39.6 | usb1k·2 |
| 12.002 | -85.9 | 17.5 | – |
| 187.463 | -85.7 | 28.0 | – |
| 14.001 | -86.5 | 17.9 | – |
| 29.152 | -87.0 | 21.9 | – |
| 119.948 | -87.6 | 25.2 | other1·2 |
| 12000.008 | -88.2 | 49.5 | fs8·2 |
| 58.396 | -88.5 | 22.5 | – |
| 29.198 | -88.8 | 20.0 | – |
| 16.002 | -88.2 | 17.0 | – |
| 58.373 | -89.4 | 21.6 | – |
| 359.825 | -90.0 | 26.0 | other1·6 |
| 179.916 | -90.5 | 22.7 | other1·3 |
| 1124.794 | -90.5 | 33.7 | – |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.987 | -83.3 | 40.1 | usb1k·1 |
| 6000.005 | -83.5 | 51.0 | fs8·1 |
| 1000.032 | -85.1 | 38.4 | other1·1 |
| 59.965 | -85.3 | 26.4 | other2·1 |
| 374.926 | -87.2 | 28.6 | – |
| 17999.995 | -86.2 | 52.6 | – |
| 1999.975 | -87.0 | 39.5 | usb1k·2 |
| 12.002 | -86.7 | 17.2 | – |
| 14.001 | -87.0 | 17.9 | – |
| 187.463 | -86.5 | 27.3 | – |
| 29.152 | -87.9 | 21.5 | – |
| 119.948 | -88.5 | 24.6 | other2·2 |
| 12000.008 | -89.6 | 47.5 | fs8·2 |
| 29.198 | -89.6 | 19.8 | – |
| 58.397 | -89.4 | 22.1 | – |
| 16.002 | -89.0 | 16.7 | – |
| 58.373 | -90.3 | 21.2 | – |
| 359.825 | -90.7 | 25.4 | other2·6 |
| 1124.794 | -91.2 | 33.4 | – |
| 179.917 | -91.4 | 22.1 | other2·3 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.63 | -0.24 | 0.91 |
| usb1k | Kanal 1 | 23/23 | 1.61 | 0.66 | 1.01 |
| other1 | Kanal 1 | 23/23 | 35.01 | 10.63 | 1.22 |
| other2 | Kanal 1 | 23/23 | 3.25 | -1.39 | 1.55 |
| fs8 | Kanal 2 | 23/23 | 0.61 | -0.23 | 0.87 |
| usb1k | Kanal 2 | 23/23 | 1.32 | 0.31 | 0.99 |
| led | Kanal 2 | 23/23 | 0.96 | 0.58 | 0.86 |
| other1 | Kanal 2 | 23/23 | 37.17 | 12.61 | 1.22 |
| other2 | Kanal 2 | 23/23 | 3.36 | -1.42 | 1.53 |
| fs8 | Kanal 3 | 23/23 | 0.61 | -0.23 | 0.88 |
| usb1k | Kanal 3 | 23/23 | 1.53 | 0.42 | 0.96 |
| led | Kanal 3 | 23/23 | 1.07 | 0.02 | 2.07 |
| other1 | Kanal 3 | 23/23 | 33.69 | 10.88 | 1.21 |
| other2 | Kanal 3 | 23/23 | 3.23 | -1.40 | 1.51 |
| fs8 | Kanal 4 | 23/23 | 0.63 | -0.24 | 0.93 |
| usb1k | Kanal 4 | 23/23 | 1.57 | 0.50 | 1.01 |
| led | Kanal 4 | 23/23 | 4.65 | 0.09 | 1.58 |
| other1 | Kanal 4 | 23/23 | 3.27 | -1.37 | 1.56 |
| other2 | Kanal 4 | 23/23 | 36.32 | 12.29 | 1.22 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.30 | 13.39 s (0.07 Hz) | 18.7 |
| Kanal 1 | 60.0 Hz ± 10 | 5.67 | 0.63 s (1.59 Hz) | 29.9 |
| Kanal 2 | breitbandig | 3.37 | 13.39 s (0.07 Hz) | 18.8 |
| Kanal 2 | 60.0 Hz ± 10 | 5.69 | 0.63 s (1.59 Hz) | 30.1 |
| Kanal 3 | breitbandig | 3.39 | 30.13 s (0.03 Hz) | 18.4 |
| Kanal 3 | 60.0 Hz ± 10 | 5.73 | 0.63 s (1.59 Hz) | 30.6 |
| Kanal 4 | breitbandig | 3.30 | 13.39 s (0.07 Hz) | 18.6 |
| Kanal 4 | 60.0 Hz ± 10 | 5.78 | 0.63 s (1.59 Hz) | 30.4 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| Kanal 1 | 10 | 5.0 | 5.697 | 1.00 |
| Kanal 2 | 24 | 11.9 | 3.060 | 1.21 |
| Kanal 3 | 66 | 32.9 | 0.858 | 1.25 |
| Kanal 4 | 11 | 5.5 | 7.253 | 1.05 |

## Korrelation zwischen Kanälen

| | Kanal 1 | Kanal 2 | Kanal 3 | Kanal 4 |
|---|---|---|---|---|
| Kanal 1 | 1.00 | 0.99 | 0.98 | 0.98 |
| Kanal 2 | 0.99 | 1.00 | 0.98 | 0.99 |
| Kanal 3 | 0.98 | 0.98 | 1.00 | 0.98 |
| Kanal 4 | 0.98 | 0.99 | 0.98 | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -66.0 | -56.5 | -9.5 | 6 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-d-in_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-d-in_psd.png)

### Kammprofile

![Kammprofile](S3-d-in_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-d-in_timeline.png)

## Notiz aus dem Manifest

> Zweites Audio-Modul in der Host-Software (zwei Gerätetakte). Datei-Werte mit Host-Faktor 2.
