# Report S3-b: S3-b – acdc1 Out 1, USB gesteckt ohne Stream, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | S3-b: USB gesteckt, kein Stream (keine App öffnet das AC/DC), Durchleitung offene Eingänge → Out 1 |
| gain | g12 |
| usb | usb-plugged, Mac-Port (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_s3b-out-via-umc_g12_usb-plugged.2chan.000.wav` |
| Format | 48000 Hz, 120.3 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-b --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -54.2 | -58.1 | -56.5 | -59.7 | -59.8 | -59.1 | -66.4 | -57.0 | 2 % | -57.1 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | acdc1 Out 1 → Startup → UMC In 1 | 5999.9997 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -100.2 dB | -102.8 | 0.0 % |
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.2202 | 0.0006 | 21/23 | k=1: 1000.220 Hz, -73.9 dB | -74.6 | 1.7 % |
| Mischprodukte n·1000.2202 + m·5999.9997 Hz (m = ±1…±4) | acdc1 Out 1 → Startup → UMC In 1 | 1000.2202 | 0.0008 | 1 | k=-1·f1+2·f2: 10999.780 Hz, -118.0 dB | -121.4 | 0.0 % |
| stärkste übrige Linie (59.98 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 59.9831 | 0.0013 | 113/398 | k=1: 59.983 Hz, -68.5 dB | -67.4 | 8.1 % |
| stärkste übrige Linie (12.00 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 12.0000 | 0.0058 | 21/1989 | k=1: 12.003 Hz, -72.4 dB | -73.1 | 2.2 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.983 | -68.5 | 33.7 | other1·1 |
| 12.003 | -72.4 | 19.3 | other2·1 |
| 1000.220 | -73.9 | 39.7 | usb1k·1 |
| 119.966 | -74.1 | 30.9 | other1·2 |
| 29.201 | -75.1 | 21.9 | – |
| 58.398 | -75.3 | 26.7 | – |
| 58.430 | -76.2 | 25.8 | – |
| 30.786 | -75.8 | 21.4 | – |
| 29.227 | -76.5 | 20.5 | – |
| 239.933 | -76.4 | 33.5 | other1·4 |
| 2000.440 | -76.7 | 35.1 | usb1k·2 |
| 16.002 | -77.5 | 15.4 | – |
| 22.004 | -77.8 | 17.5 | – |
| 18.003 | -77.6 | 16.1 | – |
| 90.767 | -77.8 | 26.5 | – |
| 24.004 | -77.0 | 19.0 | other2·2 |
| 89.182 | -77.6 | 26.5 | – |
| 179.950 | -77.8 | 29.6 | other1·3 |
| 599.832 | -78.3 | 30.9 | other1·10 |
| 30.756 | -78.3 | 18.9 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 2.53 | -0.23 | 1.36 |
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 1.17 | -1.03 | 0.33 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 56.14 | 21.77 | 4.31 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 503.87 | -128.83 | 1.85 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 5.01 | 1.52 s (0.66 Hz) | 25.2 |
| acdc1 Out 1 → Startup → UMC In 1 | 60.0 Hz ± 10 | 5.48 | 0.63 s (1.59 Hz) | 29.1 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 6581 | 3282.3 | 0.017 | 0.48 |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -56.5 | -56.5 | +0.0 | 2 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-b_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-b_psd.png)

### Kammprofile

![Kammprofile](S3-b_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-b_timeline.png)

## Notiz aus dem Manifest

> Host-Software mit Mehrkanal-Recorder, nur UMC geöffnet. Datei-Werte mit Host-Faktor 2.
