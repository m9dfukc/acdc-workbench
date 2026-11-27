# Report S3-a: S3-a – acdc1 Out 1, USB ab, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | S3-a: USB des AC/DC abgezogen (kein SOF, kein Verkehr), Durchleitung offene Eingänge → Out 1 |
| gain | g12 |
| usb | usb-off (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_s3a-out-via-umc_g12_usb-off.2chan.000.wav` |
| Format | 48000 Hz, 120.6 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-a --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -75.5 | -86.3 | -75.9 | -78.3 | -86.0 | -76.6 | -91.4 | -76.0 | 37 % | -78.0 | 2.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.1852 | 0.0012 | 23/23 | k=6: 6001.111 Hz, -80.5 dB | -80.5 | 35.3 % |
| LED-PWM (≈ 2,32 kHz) | acdc1 Out 1 → Startup → UMC In 1 | 2320.9744 | 0.0003 | 10/10 | k=2: 4641.949 Hz, -113.6 dB | -109.3 | 0.0 % |
| Netz 50 Hz | acdc1 Out 1 → Startup → UMC In 1 | 50.0050 | 0.0128 | 12/19 | k=1: 50.012 Hz, -91.5 dB | -93.0 | 2.0 % |
| stärkste übrige Linie (75.74 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 75.7352 | 0.0000 | 1/315 | k=1: 75.735 Hz, -89.2 dB | -92.3 | 2.3 % |
| stärkste übrige Linie (44.77 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 44.7651 | 0.0104 | 6/533 | k=1: 44.766 Hz, -97.2 dB | -98.4 | 0.6 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6001.111 | -80.5 | 58.7 | usb1k·6 |
| 18003.333 | -83.4 | 57.6 | usb1k·18 |
| 12002.222 | -83.8 | 56.8 | usb1k·12 |
| 75.735 | -89.2 | 43.5 | other1·1 |
| 50.012 | -91.5 | 38.7 | mains50·1 |
| 44.766 | -97.2 | 32.6 | other2·1 |
| 18.017 | -98.0 | 25.5 | – |
| 10.010 | -98.2 | 22.5 | – |
| 12.012 | -98.8 | 22.5 | – |
| 14.015 | -99.5 | 22.7 | – |
| 22.022 | -100.2 | 24.6 | – |
| 89.532 | -100.0 | 32.4 | other2·2 |
| 16.017 | -100.0 | 22.8 | – |
| 13.798 | -100.5 | 21.6 | – |
| 20.020 | -100.9 | 23.3 | – |
| 26.025 | -102.4 | 23.6 | – |
| 1215.415 | -102.4 | 35.4 | – |
| 10.362 | -102.1 | 18.6 | – |
| 24.024 | -102.3 | 23.1 | – |
| 82.634 | -102.9 | 29.0 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.01 | 0.01 | 0.02 |
| led | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.88 | 0.19 | 0.49 |
| mains50 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 188.85 | 161.09 | 0.48 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 18.14 | 6.65 | 0.18 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 427.80 | -254.44 | 0.79 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 0.82 | 0.25 s (4.00 Hz) | 24.9 |
| acdc1 Out 1 → Startup → UMC In 1 | 6001.1 Hz ± 10 | 0.50 | 2.04 s (0.49 Hz) | 20.7 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -75.9 | -56.5 | -19.4 | 37 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-a_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-a_psd.png)

### Kammprofile

![Kammprofile](S3-a_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-a_timeline.png)

## Notiz aus dem Manifest

> Host-Software mit Mehrkanal-Recorder, nur UMC. Datei-Werte mit Host-Faktor 2.
