# Report S3-d: S3-d – acdc1 Out 1, Duplex-Stream mit Nullen an den DAC, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | S3-d: Duplex-Stream (Host-Software öffnet AC/DC, Nullen an die Ausgänge → keine Durchleitung) |
| gain | g12 |
| usb | usb-duplex, Mac-Port (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_s3d-out-via-umc_g12_usb-duplex.2chan.000.wav` |
| Format | 48000 Hz, 120.5 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-d --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -54.9 | -60.2 | -56.4 | -58.6 | -61.2 | -58.1 | -67.4 | -56.8 | 2 % | -56.9 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | acdc1 Out 1 → Startup → UMC In 1 | 5999.9999 | 0.0003 | 3/3 | k=1: 6000.000 Hz, -94.2 dB | -97.2 | 0.0 % |
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.2197 | 0.0003 | 22/23 | k=1: 1000.220 Hz, -71.6 dB | -73.1 | 2.3 % |
| Mischprodukte n·1000.2197 + m·5999.9999 Hz (m = ±1…±4) | acdc1 Out 1 → Startup → UMC In 1 | 1000.2197 | 0.0006 | 1 | k=-1·f1+1·f2: 4999.780 Hz, -105.7 dB | -107.8 | 0.0 % |
| stärkste übrige Linie (59.98 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 59.9831 | 0.0045 | 147/398 | k=1: 59.984 Hz, -71.6 dB | -69.4 | 5.1 % |
| stärkste übrige Linie (375.00 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 375.0000 | 0.0004 | 57/63 | k=1: 375.000 Hz, -73.4 dB | -71.9 | 2.9 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.984 | -71.6 | 30.3 | other1·1 |
| 1000.220 | -71.6 | 39.0 | usb1k·1 |
| 375.000 | -73.4 | 34.7 | other2·1 |
| 187.500 | -74.1 | 31.2 | – |
| 119.966 | -74.9 | 28.7 | other1·2 |
| 58.393 | -74.3 | 27.3 | – |
| 562.500 | -74.8 | 35.7 | – |
| 12.002 | -74.0 | 19.0 | – |
| 14.001 | -74.8 | 19.0 | – |
| 29.175 | -76.6 | 22.4 | – |
| 29.199 | -76.8 | 22.2 | – |
| 2000.439 | -76.8 | 35.4 | usb1k·2 |
| 750.000 | -75.6 | 35.2 | other2·2 |
| 16.002 | -76.5 | 18.1 | – |
| 937.500 | -76.4 | 34.7 | – |
| 1125.000 | -77.3 | 34.8 | other2·3 |
| 1312.500 | -77.9 | 34.2 | – |
| 24.003 | -78.2 | 20.0 | – |
| 1500.000 | -78.7 | 34.3 | other2·4 |
| 18.004 | -79.2 | 16.3 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.80 | -0.36 | 1.36 |
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 4.07 | 0.56 | 0.49 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 32.62 | 5.33 | 1.16 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 11.61 | 0.62 | 1.01 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 4.02 | 3.01 s (0.33 Hz) | 23.0 |
| acdc1 Out 1 → Startup → UMC In 1 | 60.0 Hz ± 10 | 5.76 | 0.63 s (1.59 Hz) | 30.8 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 6512 | 3242.0 | 0.016 | 0.57 |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -56.4 | -56.5 | +0.1 | 2 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-d_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-d_psd.png)

### Kammprofile

![Kammprofile](S3-d_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-d_timeline.png)

## Notiz aus dem Manifest

> Host-Software: Audio-Modul A = UMC → Mehrkanal-Recorder, Audio-Modul B = AC/DC ohne Ausgänge gepatcht. Datei-Werte mit Host-Faktor 2.
