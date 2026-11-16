# Report S3-b2: S3-b2 – acdc1 Out 1, USB gesteckt ohne Stream (Wiederholung), 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | S3-b2: Wiederholung von S3-b am Serienende (USB wieder gesteckt, selber Mac-Port, kein Stream) |
| gain | g12 |
| usb | usb-plugged, Mac-Port (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_s3b2-out-via-umc_g12_usb-plugged.2chan.000.wav` |
| Format | 48000 Hz, 120.2 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-b2 --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -54.7 | -58.3 | -57.2 | -60.3 | -60.5 | -59.8 | -67.4 | -57.6 | 2 % | -57.7 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | acdc1 Out 1 → Startup → UMC In 1 | 6000.0002 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -97.8 dB | -100.2 | 0.0 % |
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.2197 | 0.0005 | 22/23 | k=1: 1000.219 Hz, -75.6 dB | -75.5 | 1.6 % |
| Mischprodukte n·1000.2197 + m·6000.0002 Hz (m = ±1…±4) | acdc1 Out 1 → Startup → UMC In 1 | 1000.2197 | 0.0023 | 1 | k=-1·f1+2·f2: 10999.783 Hz, -118.2 dB | -121.4 | 0.0 % |
| stärkste übrige Linie (59.99 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 59.9831 | 0.0041 | 127/398 | k=1: 59.985 Hz, -69.9 dB | -69.4 | 6.1 % |
| stärkste übrige Linie (29.18 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 29.1829 | 0.0128 | 25/818 | k=1: 29.178 Hz, -72.7 dB | -71.8 | 3.5 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.985 | -69.9 | 31.3 | other1·1 |
| 29.178 | -72.7 | 24.5 | other2·1 |
| 119.970 | -73.6 | 29.7 | other1·2 |
| 12.003 | -74.1 | 17.3 | – |
| 16.001 | -75.5 | 17.7 | – |
| 1000.219 | -75.6 | 38.6 | usb1k·1 |
| 2000.439 | -76.8 | 35.3 | usb1k·2 |
| 58.355 | -77.4 | 23.6 | other2·2 |
| 20.004 | -78.3 | 16.3 | – |
| 89.163 | -78.6 | 24.7 | – |
| 58.325 | -78.9 | 22.2 | – |
| 28.005 | -78.9 | 18.1 | – |
| 30.806 | -78.5 | 19.0 | – |
| 179.957 | -78.2 | 26.8 | other1·3 |
| 24.005 | -79.5 | 16.6 | – |
| 90.789 | -78.8 | 24.6 | – |
| 26.004 | -79.4 | 17.2 | – |
| 22.004 | -79.0 | 16.4 | – |
| 187.500 | -80.4 | 25.7 | – |
| 562.500 | -80.4 | 29.2 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.94 | 0.15 | 2.04 |
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 1.34 | 1.76 | 0.56 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 84.72 | 33.49 | 1.39 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 587.10 | -248.54 | 0.90 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 4.90 | 3.08 s (0.32 Hz) | 24.4 |
| acdc1 Out 1 → Startup → UMC In 1 | 60.0 Hz ± 10 | 6.04 | 0.61 s (1.63 Hz) | 28.2 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 5772 | 2881.5 | 0.018 | 0.57 |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -57.2 | -56.5 | -0.7 | 2 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-b2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-b2_psd.png)

### Kammprofile

![Kammprofile](S3-b2_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-b2_timeline.png)

## Notiz aus dem Manifest

> Host-Software mit Mehrkanal-Recorder, nur UMC. Datei-Werte mit Host-Faktor 2.
