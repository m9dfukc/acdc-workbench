# Report S3-c-in: S3-c-in – acdc1 Eingänge offen, Aufnahmeprogramm, Mac-Port, 130 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | S3-c, Gegenseite: AC/DC-Eingänge 1–4 (offen) per Aufnahmeprogramm, nur Eingang geöffnet, Out 1 am Startup |
| gain | g12 |
| usb | usb-stream (nur AC/DC → Mac), Mac-Port |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_s3c-in-audacity_g12_usb-stream.wav` |
| Format | 48000 Hz, 130.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-c-in --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -3.2 | -69.5 | -74.2 | -71.3 | -74.9 | -75.3 | -73.6 | -80.7 | -71.8 | 5 % | -72.0 | 0.2 |
| Kanal 2 | -3.4 | -69.7 | -74.4 | -71.5 | -75.2 | -75.5 | -73.9 | -80.9 | -72.0 | 5 % | -72.3 | 0.2 |
| Kanal 3 | -2.5 | -70.6 | -75.3 | -72.3 | -76.0 | -76.2 | -74.7 | -82.0 | -72.8 | 8 % | -73.2 | 0.4 |
| Kanal 4 | -2.6 | -71.1 | -75.8 | -72.9 | -76.5 | -77.0 | -75.2 | -82.9 | -73.4 | 7 % | -73.7 | 0.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -87.1 dB | -87.4 | 2.8 % |
| 1-kHz-Kamm | Kanal 1 | 1000.0345 | 0.0080 | 17/23 | k=1: 1000.035 Hz, -88.2 dB | -89.7 | 1.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0006 | 9/10 | k=2: 4641.091 Hz, -127.2 dB | -123.2 | 0.0 % |
| Mischprodukte n·1000.0345 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 1000.0345 | 0.0051 | 16 | k=-4·f1+3·f2: 13999.856 Hz, -100.8 dB | -101.1 | 0.1 % |
| stärkste übrige Linie (59.97 Hz) | Kanal 1 | 59.9720 | 0.0013 | 81/398 | k=1: 59.973 Hz, -82.9 dB | -81.8 | 8.9 % |
| stärkste übrige Linie (999.99 Hz) | Kanal 1 | 999.9897 | 0.0001 | 22/23 | k=1: 999.990 Hz, -88.1 dB | -87.0 | 2.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -86.9 dB | -87.3 | 3.0 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0344 | 0.0063 | 17/23 | k=1: 1000.035 Hz, -88.2 dB | -89.8 | 1.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0005 | 9/10 | k=9: 20884.903 Hz, -121.3 dB | -117.7 | 0.0 % |
| Mischprodukte n·1000.0344 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 1000.0344 | 0.0049 | 19 | k=-4·f1+3·f2: 13999.856 Hz, -100.9 dB | -100.9 | 0.1 % |
| stärkste übrige Linie (59.97 Hz) | Kanal 2 | 59.9720 | 0.0013 | 86/398 | k=1: 59.973 Hz, -83.1 dB | -82.0 | 9.0 % |
| stärkste übrige Linie (999.99 Hz) | Kanal 2 | 999.9897 | 0.0001 | 22/23 | k=1: 999.990 Hz, -88.5 dB | -87.3 | 2.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -87.3 dB | -87.4 | 3.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.9897 | 0.0001 | 23/23 | k=1: 999.990 Hz, -88.5 dB | -87.2 | 3.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 9/10 | k=2: 4641.091 Hz, -127.6 dB | -123.4 | 0.0 % |
| Mischprodukte n·999.9897 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.9897 | 0.0008 | 155 | k=4·f1+2·f2: 15999.959 Hz, -105.0 dB | -94.0 | 0.8 % |
| stärkste übrige Linie (59.97 Hz) | Kanal 3 | 59.9720 | 0.0012 | 103/398 | k=1: 59.973 Hz, -83.8 dB | -82.7 | 9.2 % |
| stärkste übrige Linie (1000.03 Hz) | Kanal 3 | 1000.0344 | 0.0089 | 17/23 | k=1: 1000.035 Hz, -89.1 dB | -90.6 | 1.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -88.2 dB | -88.5 | 3.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.9897 | 0.0001 | 23/23 | k=1: 999.990 Hz, -89.3 dB | -88.1 | 3.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0006 | 9/10 | k=3: 6961.635 Hz, -126.9 dB | -122.3 | 0.0 % |
| Mischprodukte n·999.9897 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.9897 | 0.0008 | 150 | k=7·f1+1·f2: 12999.928 Hz, -106.1 dB | -95.0 | 0.7 % |
| stärkste übrige Linie (59.97 Hz) | Kanal 4 | 59.9720 | 0.0013 | 80/398 | k=1: 59.973 Hz, -84.6 dB | -83.5 | 8.7 % |
| stärkste übrige Linie (1000.03 Hz) | Kanal 4 | 1000.0344 | 0.0066 | 15/23 | k=1: 1000.035 Hz, -89.7 dB | -91.3 | 1.5 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.973 | -82.9 | 33.1 | other1·1 |
| 119.945 | -85.5 | 33.9 | other1·2 |
| 179.917 | -88.1 | 31.2 | other1·3 |
| 6000.000 | -87.1 | 54.6 | fs8·1 |
| 1000.035 | -88.2 | 39.1 | usb1k·1 |
| 999.990 | -88.1 | 39.2 | other2·1 |
| 125.000 | -89.8 | 30.1 | – |
| 1999.979 | -90.4 | 41.4 | other2·2 |
| 12000.000 | -91.0 | 55.0 | fs8·2 |
| 18000.000 | -89.7 | 57.1 | fs8·3 |
| 29.218 | -90.9 | 24.5 | – |
| 299.861 | -91.6 | 30.9 | other1·5 |
| 419.804 | -91.9 | 32.0 | other1·7 |
| 359.833 | -91.4 | 31.4 | other1·6 |
| 2000.069 | -93.1 | 38.8 | usb1k·2 |
| 50.311 | -93.6 | 22.7 | – |
| 12.003 | -93.9 | 15.5 | – |
| 2999.969 | -93.9 | 41.1 | other2·3 |
| 14.001 | -94.2 | 16.1 | – |
| 4999.949 | -94.8 | 45.6 | other2·5 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.973 | -83.1 | 33.1 | other1·1 |
| 119.945 | -85.7 | 33.9 | other1·2 |
| 179.917 | -88.2 | 31.2 | other1·3 |
| 6000.000 | -86.9 | 55.4 | fs8·1 |
| 1000.035 | -88.2 | 39.2 | usb1k·1 |
| 999.990 | -88.5 | 38.9 | other2·1 |
| 125.000 | -89.9 | 30.1 | – |
| 12000.000 | -90.7 | 56.9 | fs8·2 |
| 1999.979 | -91.1 | 41.0 | other2·2 |
| 18000.000 | -89.6 | 58.8 | fs8·3 |
| 29.218 | -90.9 | 24.7 | – |
| 299.861 | -91.6 | 30.9 | other1·5 |
| 419.804 | -92.0 | 32.1 | other1·7 |
| 359.833 | -91.5 | 31.6 | other1·6 |
| 2000.069 | -93.2 | 38.9 | usb1k·2 |
| 12.002 | -93.9 | 15.7 | – |
| 50.311 | -93.9 | 22.6 | – |
| 2999.969 | -94.1 | 41.1 | other2·3 |
| 14.001 | -94.6 | 16.0 | – |
| 4999.948 | -95.2 | 45.9 | other2·5 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.973 | -83.8 | 33.3 | other1·1 |
| 119.945 | -86.3 | 34.1 | other1·2 |
| 6000.000 | -87.3 | 56.9 | fs8·1 |
| 179.917 | -89.0 | 31.2 | other1·3 |
| 999.990 | -88.5 | 39.7 | usb1k·1 |
| 1000.035 | -89.1 | 39.2 | other2·1 |
| 12000.000 | -90.5 | 59.9 | fs8·2 |
| 1999.979 | -90.8 | 42.2 | usb1k·2 |
| 125.000 | -90.7 | 30.3 | – |
| 18000.000 | -89.8 | 61.3 | fs8·3 |
| 29.218 | -91.7 | 24.7 | – |
| 299.861 | -92.4 | 31.0 | other1·5 |
| 419.804 | -92.8 | 32.1 | other1·7 |
| 359.833 | -92.3 | 31.5 | other1·6 |
| 2000.069 | -93.9 | 39.1 | other2·2 |
| 50.311 | -94.6 | 22.8 | – |
| 12.002 | -94.9 | 15.5 | – |
| 2999.969 | -94.4 | 41.9 | usb1k·3 |
| 4999.948 | -95.2 | 47.5 | usb1k·5 |
| 14.001 | -95.3 | 16.1 | – |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.973 | -84.6 | 33.1 | other1·1 |
| 119.945 | -87.2 | 33.8 | other1·2 |
| 179.917 | -89.7 | 31.2 | other1·3 |
| 6000.000 | -88.2 | 55.1 | fs8·1 |
| 999.990 | -89.3 | 39.6 | usb1k·1 |
| 1000.035 | -89.7 | 39.2 | other2·1 |
| 12000.000 | -91.8 | 55.6 | fs8·2 |
| 1999.979 | -91.7 | 41.8 | usb1k·2 |
| 125.000 | -91.6 | 29.9 | – |
| 18000.000 | -91.0 | 57.6 | fs8·3 |
| 29.218 | -92.5 | 24.6 | – |
| 299.861 | -93.1 | 31.0 | other1·5 |
| 419.804 | -93.5 | 32.1 | other1·7 |
| 359.833 | -92.9 | 31.7 | other1·6 |
| 2000.069 | -94.7 | 38.8 | other2·2 |
| 50.311 | -95.5 | 22.7 | – |
| 2999.969 | -95.1 | 41.5 | usb1k·3 |
| 4999.948 | -96.1 | 46.2 | usb1k·5 |
| 14.001 | -95.9 | 16.1 | – |
| 249.999 | -96.0 | 28.1 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 24/24 | 0.60 | -0.12 | 0.85 |
| usb1k | Kanal 1 | 24/24 | 2.74 | 0.23 | 1.24 |
| led | Kanal 1 | 24/24 | 6.38 | -1.78 | 1.75 |
| other1 | Kanal 1 | 24/24 | 65.49 | 19.29 | 0.96 |
| other2 | Kanal 1 | 24/24 | 1.27 | 0.39 | 0.92 |
| fs8 | Kanal 2 | 24/24 | 0.58 | -0.12 | 0.82 |
| usb1k | Kanal 2 | 24/24 | 2.72 | -0.03 | 1.23 |
| led | Kanal 2 | 24/24 | 0.35 | -0.02 | 0.70 |
| other1 | Kanal 2 | 24/24 | 65.24 | 20.05 | 0.97 |
| other2 | Kanal 2 | 24/24 | 1.28 | 0.48 | 0.90 |
| fs8 | Kanal 3 | 24/24 | 0.58 | -0.12 | 0.82 |
| usb1k | Kanal 3 | 24/24 | 1.30 | 0.46 | 0.85 |
| led | Kanal 3 | 24/24 | 2.31 | 0.68 | 1.05 |
| other1 | Kanal 3 | 24/24 | 65.33 | 19.44 | 0.97 |
| other2 | Kanal 3 | 24/24 | 2.81 | 0.60 | 1.20 |
| fs8 | Kanal 4 | 24/24 | 0.59 | -0.12 | 0.86 |
| usb1k | Kanal 4 | 24/24 | 1.33 | 0.47 | 0.89 |
| led | Kanal 4 | 24/24 | 3.44 | 2.50 | 1.23 |
| other1 | Kanal 4 | 24/24 | 65.20 | 20.44 | 0.99 |
| other2 | Kanal 4 | 24/24 | 2.69 | 0.23 | 1.26 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.02 | 14.44 s (0.07 Hz) | 21.4 |
| Kanal 1 | 60.0 Hz ± 10 | 5.72 | 0.63 s (1.58 Hz) | 24.8 |
| Kanal 2 | breitbandig | 3.05 | 14.44 s (0.07 Hz) | 21.4 |
| Kanal 2 | 60.0 Hz ± 10 | 5.75 | 0.63 s (1.58 Hz) | 25.1 |
| Kanal 3 | breitbandig | 3.06 | 14.44 s (0.07 Hz) | 21.3 |
| Kanal 3 | 60.0 Hz ± 10 | 5.70 | 0.63 s (1.58 Hz) | 25.0 |
| Kanal 4 | breitbandig | 3.02 | 14.44 s (0.07 Hz) | 21.4 |
| Kanal 4 | 60.0 Hz ± 10 | 5.75 | 0.63 s (1.58 Hz) | 25.3 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| Kanal 1 | 7 | 3.2 | 16.402 | 0.77 |
| Kanal 2 | 14 | 6.5 | 7.622 | 1.05 |
| Kanal 3 | 45 | 20.8 | 1.209 | 1.24 |
| Kanal 4 | 8 | 3.7 | 15.107 | 0.73 |

## Korrelation zwischen Kanälen

| | Kanal 1 | Kanal 2 | Kanal 3 | Kanal 4 |
|---|---|---|---|---|
| Kanal 1 | 1.00 | 0.99 | 0.99 | 0.98 |
| Kanal 2 | 0.99 | 1.00 | 0.99 | 0.99 |
| Kanal 3 | 0.99 | 0.99 | 1.00 | 0.98 |
| Kanal 4 | 0.98 | 0.99 | 0.98 | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.3 | -56.5 | -14.8 | 5 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-c-in_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-c-in_psd.png)

### Kammprofile

![Kammprofile](S3-c-in_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-c-in_timeline.png)

## Notiz aus dem Manifest

> Aufnahmeprogramm 32 Bit float, OHNE Host-Faktor (Datei-dBFS = Geräte-dBFS). Läuft länger als S3-c, nicht synchron.
