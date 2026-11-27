# Report S3-0: S3-0 – Messkette Startup → UMC allein, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | UMC202HD + MTM Startup (Messkette allein), acdc1 Build 1d am Mac-Port, USB gesteckt |
| test | S3-0: Messkette ohne AC/DC-Signal (Kabel acdc1 Out 1 → Startup gezogen) |
| gain | g12 |
| usb | acdc1: usb-plugged (kein Stream), Mac-Port. UMC: Hub |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_umc_s3-0-chain-only_g12_usb-plugged.2chan.000.wav` |
| Format | 48000 Hz, 120.2 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis S3-0 --ref S3-b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UMC In 1 ← Startup (ohne AC/DC) | +0.0 | -85.9 | -93.2 | -86.7 | -90.2 | -92.3 | -88.5 | -99.9 | -87.0 | 18 % | -87.8 | 0.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | UMC In 1 ← Startup (ohne AC/DC) | 6000.0477 | 0.0000 | 1/3 | k=2: 12000.095 Hz, -135.5 dB | -137.8 | 0.0 % |
| 1-kHz-Kamm | UMC In 1 ← Startup (ohne AC/DC) | 1000.2205 | 0.0009 | 11/23 | k=8: 8001.764 Hz, -105.4 dB | -107.0 | 1.0 % |
| LED-PWM (≈ 2,32 kHz) | UMC In 1 ← Startup (ohne AC/DC) | 2318.7672 | 0.0004 | 2/10 | k=3: 6956.301 Hz, -122.0 dB | -124.9 | 0.0 % |
| Netz 50 Hz | UMC In 1 ← Startup (ohne AC/DC) | 49.9968 | 0.0080 | 17/19 | k=1: 50.000 Hz, -94.1 dB | -94.8 | 16.6 % |
| stärkste übrige Linie (10.02 Hz) | UMC In 1 ← Startup (ohne AC/DC) | 10.0170 | 0.0140 | 20/2383 | k=1: 10.019 Hz, -103.5 dB | -101.8 | 3.1 % |
| stärkste übrige Linie (16.03 Hz) | UMC In 1 ← Startup (ohne AC/DC) | 16.0352 | 0.0090 | 12/1489 | k=1: 16.030 Hz, -103.3 dB | -104.4 | 1.7 % |

## Stärkste Linien (Kanal für Kanal)

### UMC In 1 ← Startup (ohne AC/DC)

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 50.000 | -94.1 | 43.9 | mains50·1 |
| 249.977 | -102.5 | 39.4 | mains50·5 |
| 100.000 | -103.6 | 35.3 | mains50·2 |
| 10.019 | -103.5 | 28.2 | other1·1 |
| 16.030 | -103.3 | 31.2 | other2·1 |
| 14.026 | -102.7 | 31.1 | – |
| 12.022 | -104.1 | 28.7 | – |
| 18.034 | -103.9 | 31.0 | – |
| 20.038 | -104.4 | 30.9 | other1·2 |
| 8001.764 | -105.4 | 45.5 | usb1k·8 |
| 22.042 | -105.4 | 30.3 | – |
| 479.745 | -104.9 | 38.4 | – |
| 250.023 | -106.4 | 35.5 | – |
| 24.045 | -106.2 | 29.9 | – |
| 719.617 | -106.3 | 38.4 | – |
| 449.954 | -106.5 | 36.9 | – |
| 26.050 | -107.4 | 28.9 | – |
| 419.777 | -107.7 | 35.3 | – |
| 28.054 | -107.9 | 28.5 | – |
| 899.522 | -106.8 | 38.9 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | UMC In 1 ← Startup (ohne AC/DC) | 13/23 | 2.71 | -1.08 | 1.80 |
| usb1k | UMC In 1 ← Startup (ohne AC/DC) | 23/23 | 0.12 | -0.06 | 0.17 |
| led | UMC In 1 ← Startup (ohne AC/DC) | 23/23 | 4.85 | 2.08 | 0.75 |
| mains50 | UMC In 1 ← Startup (ohne AC/DC) | 23/23 | 140.24 | -172.60 | 0.25 |
| other1 | UMC In 1 ← Startup (ohne AC/DC) | 23/23 | 163.31 | -199.50 | 0.28 |
| other2 | UMC In 1 ← Startup (ohne AC/DC) | 23/23 | 566.16 | -27.15 | 0.34 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| UMC In 1 ← Startup (ohne AC/DC) | breitbandig | 1.78 | 0.50 s (2.00 Hz) | 31.9 |
| UMC In 1 ← Startup (ohne AC/DC) | 50.0 Hz ± 10 | 2.57 | 0.17 s (5.91 Hz) | 24.9 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| UMC In 1 ← Startup (ohne AC/DC) | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | UMC In 1 ← Startup (ohne AC/DC) |
|---|---|
| UMC In 1 ← Startup (ohne AC/DC) | 1.00 |

## Vergleich mit Referenz S3-b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| UMC In 1 ← Startup (ohne AC/DC) | -86.7 | -56.5 | -30.2 | 18 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S3-0_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S3-0_psd.png)

### Kammprofile

![Kammprofile](S3-0_combs.png)

### Zeitverlauf

![Zeitverlauf](S3-0_timeline.png)

## Notiz aus dem Manifest

> Host-Software mit Mehrkanal-Recorder, Datei-Werte mit Host-Faktor 2.
