# Report S3-c: S3-c – acdc1 Out 1, Eingangs-Stream über ein Aufnahmeprogramm, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | S3-c: AC/DC-Eingänge streamen (Aufnahmeprogramm nimmt nur auf), Durchleitung offene Eingänge → Out 1 |
| gain | g12 |
| usb | usb-stream (nur AC/DC → Mac), Mac-Port (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_s3c-out-via-umc_g12_usb-stream.2chan.000.wav` |
| Format | 48000 Hz, 120.2 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-c --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -53.5 | -60.0 | -54.6 | -57.3 | -59.0 | -56.6 | -64.5 | -55.1 | 3 % | -55.2 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | acdc1 Out 1 → Startup → UMC In 1 | 6000.0002 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -92.6 dB | -95.3 | 0.0 % |
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.2197 | 0.0005 | 23/23 | k=1: 1000.219 Hz, -70.5 dB | -71.1 | 2.5 % |
| Mischprodukte n·1000.2197 + m·6000.0002 Hz (m = ±1…±4) | acdc1 Out 1 → Startup → UMC In 1 | 1000.2197 | 0.0014 | 1 | k=-1·f1+1·f2: 4999.779 Hz, -105.4 dB | -108.5 | 0.0 % |
| stärkste übrige Linie (59.98 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 59.9831 | 0.0014 | 190/398 | k=1: 59.984 Hz, -66.5 dB | -65.1 | 8.9 % |
| stärkste übrige Linie (29.22 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 29.2259 | 0.0037 | 17/817 | k=1: 29.223 Hz, -74.2 dB | -73.0 | 1.4 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.984 | -66.5 | 32.8 | other1·1 |
| 119.967 | -68.9 | 33.7 | other1·2 |
| 1000.219 | -70.5 | 38.7 | usb1k·1 |
| 179.951 | -71.5 | 31.0 | other1·3 |
| 29.223 | -74.2 | 24.6 | other2·1 |
| 125.023 | -73.0 | 30.3 | – |
| 359.899 | -74.5 | 31.5 | other1·6 |
| 419.882 | -74.9 | 31.9 | other1·7 |
| 2000.439 | -73.5 | 39.1 | usb1k·2 |
| 299.916 | -74.6 | 30.9 | other1·5 |
| 50.320 | -76.9 | 23.0 | – |
| 250.046 | -78.3 | 27.2 | – |
| 14.003 | -78.4 | 15.6 | – |
| 59.674 | -78.8 | 20.5 | – |
| 3000.659 | -78.9 | 35.8 | usb1k·3 |
| 58.406 | -78.8 | 20.6 | – |
| 16.003 | -78.7 | 16.1 | – |
| 375.001 | -79.4 | 26.5 | – |
| 59.906 | -78.9 | 20.4 | – |
| 60.524 | -79.6 | 19.7 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.60 | 0.18 | 1.15 |
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 2.49 | 0.12 | 0.45 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 60.72 | 7.83 | 0.93 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 838.59 | 46.29 | 0.75 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 3.09 | 3.00 s (0.33 Hz) | 24.0 |
| acdc1 Out 1 → Startup → UMC In 1 | 60.0 Hz ± 10 | 5.59 | 0.64 s (1.57 Hz) | 24.8 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 7 | 3.5 | 3.819 | 1.13 |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -54.6 | -56.5 | +1.9 | 3 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-c_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-c_psd.png)

### Kammprofile

![Kammprofile](S3-c_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-c_timeline.png)

## Notiz aus dem Manifest

> Host-Software mit Mehrkanal-Recorder, nur UMC geöffnet. Aufnahme nur über den Eingang lief vor Start bis nach Ende (S3-c-in). Datei-Werte mit Host-Faktor 2.
