# Report G2a: G2a – acdc1 Out 1, ohne Monitor und ohne USB, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | G2a: wie G2, aber versehentlich ohne AC/DC-USB (Monitor ab, USB ab) – Gegenstück zu S3-a |
| gain | g12 |
| usb | usb-off (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g2a-no-monitor_g12_usb-off.2chan.000.wav` |
| Format | 48000 Hz, 120.2 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis G2a --ref G0` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -75.4 | -85.7 | -75.8 | -78.1 | -86.1 | -76.5 | -91.8 | -75.9 | 40 % | -78.1 | 2.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.1853 | 0.0015 | 23/23 | k=6: 6001.112 Hz, -79.7 dB | -80.1 | 37.7 % |
| LED-PWM (≈ 2,32 kHz) | acdc1 Out 1 → Startup → UMC In 1 | 2320.9748 | 0.0003 | 10/10 | k=2: 4641.950 Hz, -113.9 dB | -109.8 | 0.0 % |
| Netz 50 Hz | acdc1 Out 1 → Startup → UMC In 1 | 49.9976 | 0.0075 | 12/19 | k=1: 49.994 Hz, -91.1 dB | -92.7 | 2.1 % |
| stärkste übrige Linie (75.74 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 75.7355 | 0.0003 | 2/315 | k=1: 75.735 Hz, -89.6 dB | -92.8 | 2.0 % |
| stärkste übrige Linie (44.77 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 44.7658 | 0.0015 | 4/533 | k=1: 44.766 Hz, -98.3 dB | -98.7 | 0.5 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6001.112 | -79.7 | 59.7 | usb1k·6 |
| 18003.336 | -83.5 | 57.4 | usb1k·18 |
| 12002.224 | -83.3 | 57.1 | usb1k·12 |
| 75.735 | -89.6 | 42.9 | other1·1 |
| 49.994 | -91.1 | 38.6 | mains50·1 |
| 44.766 | -98.3 | 30.6 | other2·1 |
| 89.532 | -99.1 | 33.9 | other2·2 |
| 10.007 | -99.6 | 20.7 | – |
| 14.010 | -100.0 | 21.8 | – |
| 12.008 | -99.4 | 21.7 | – |
| 18.012 | -100.5 | 22.7 | – |
| 13.796 | -100.8 | 21.0 | – |
| 99.993 | -101.5 | 32.4 | mains50·2 |
| 16.011 | -102.2 | 20.4 | – |
| 1215.415 | -102.6 | 36.6 | – |
| 82.633 | -102.3 | 30.2 | – |
| 20.016 | -102.9 | 20.9 | – |
| 10.556 | -103.0 | 17.6 | – |
| 22.020 | -103.4 | 20.9 | – |
| 1859.793 | -103.8 | 35.7 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.02 | -0.00 | 0.07 |
| led | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 1.49 | 0.05 | 0.46 |
| mains50 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 147.26 | 0.86 | 0.49 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 40.05 | -17.14 | 0.17 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 591.77 | 84.43 | 0.52 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 0.88 | 0.25 s (4.00 Hz) | 26.0 |
| acdc1 Out 1 → Startup → UMC In 1 | 6001.1 Hz ± 10 | 0.61 | 2.04 s (0.49 Hz) | 26.5 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz G0

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -75.8 | -57.4 | -18.4 | 40 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G2a_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G2a_psd.png)

### Kammprofile

![Kammprofile](G2a_combs.png)

### Zeitverlauf

![Zeitverlauf](G2a_timeline.png)
