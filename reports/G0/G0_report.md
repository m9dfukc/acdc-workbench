# Report G0: G0 – acdc1 Out 1, Referenz Masseschleife, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | G0: Referenz Masseschleife = S3-b neu (AC/DC am Mac-Port, UMC + Monitor am Hub, Mac über Hub versorgt) |
| gain | g12 |
| usb | usb-plugged, Mac-Port (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g0-loop-ref_g12_usb-plugged.2chan.000.wav` |
| Format | 48000 Hz, 120.3 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis G0 --ref G0` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -54.9 | -58.5 | -57.4 | -60.4 | -60.8 | -59.9 | -68.7 | -57.7 | 2 % | -57.8 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | acdc1 Out 1 → Startup → UMC In 1 | 6000.0002 | 0.0007 | 3/3 | k=1: 6000.001 Hz, -99.2 dB | -101.8 | 0.0 % |
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.2198 | 0.0006 | 20/23 | k=1: 1000.220 Hz, -74.8 dB | -75.5 | 1.7 % |
| Mischprodukte n·1000.2198 + m·6000.0002 Hz (m = ±1…±4) | acdc1 Out 1 → Startup → UMC In 1 | 1000.2198 | 0.0009 | 1 | k=-1·f1+2·f2: 10999.781 Hz, -119.1 dB | -122.6 | 0.0 % |
| stärkste übrige Linie (59.98 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 59.9831 | 0.0036 | 106/398 | k=1: 59.984 Hz, -70.2 dB | -69.6 | 5.9 % |
| stärkste übrige Linie (12.00 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 12.0056 | 0.0074 | 12/1989 | k=1: 12.001 Hz, -75.0 dB | -75.6 | 1.5 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 59.984 | -70.2 | 31.2 | other1·1 |
| 1000.220 | -74.8 | 38.7 | usb1k·1 |
| 119.969 | -75.1 | 29.4 | other1·2 |
| 12.001 | -75.0 | 16.9 | other2·1 |
| 29.204 | -76.1 | 21.6 | – |
| 14.001 | -75.8 | 16.8 | – |
| 58.391 | -76.5 | 24.7 | – |
| 16.003 | -76.9 | 16.5 | – |
| 29.173 | -76.5 | 21.2 | – |
| 2000.440 | -77.7 | 34.6 | usb1k·2 |
| 24.004 | -77.8 | 18.9 | other2·2 |
| 18.004 | -78.9 | 15.3 | – |
| 30.808 | -79.3 | 18.6 | – |
| 20.004 | -78.2 | 16.9 | – |
| 58.423 | -79.1 | 22.1 | – |
| 187.501 | -79.9 | 29.1 | – |
| 562.500 | -80.3 | 29.8 | – |
| 30.781 | -80.4 | 17.5 | – |
| 31.432 | -80.4 | 17.6 | – |
| 116.701 | -81.0 | 23.3 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 1.23 | -0.14 | 1.53 |
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 1.14 | -1.35 | 0.50 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 60.11 | 4.27 | 0.79 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 552.97 | -19.17 | 1.43 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 4.88 | 1.01 s (0.99 Hz) | 24.4 |
| acdc1 Out 1 → Startup → UMC In 1 | 60.0 Hz ± 10 | 5.97 | 0.64 s (1.56 Hz) | 29.3 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 6400 | 3192.1 | 0.017 | 0.51 |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz G0

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -57.4 | -57.4 | +0.0 | 2 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G0_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G0_psd.png)

### Kammprofile

![Kammprofile](G0_combs.png)

### Zeitverlauf

![Zeitverlauf](G0_timeline.png)
