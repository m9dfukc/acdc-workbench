# Report G1: G1 – acdc1 Out 1, AC/DC am Hub, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | G1: wie G0, AC/DC-USB am Hub statt am Mac-Port (Monitor wieder dran) |
| gain | g12 |
| usb | usb-plugged, Hub (wie UMC) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g1-acdc-at-hub_g12_usb-plugged.2chan.000.wav` |
| Format | 48000 Hz, 120.3 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis G1 --ref G0` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -73.4 | -78.1 | -75.1 | -78.3 | -81.0 | -76.6 | -80.7 | -76.5 | 2 % | -76.6 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | acdc1 Out 1 → Startup → UMC In 1 | 6000.0387 | 0.0000 | 1/3 | k=2: 12000.077 Hz, -124.2 dB | -127.2 | 0.0 % |
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.1815 | 0.0012 | 22/23 | k=3: 3000.544 Hz, -105.1 dB | -99.5 | 0.5 % |
| LED-PWM (≈ 2,32 kHz) | acdc1 Out 1 → Startup → UMC In 1 | 2320.9752 | 0.0005 | 10/10 | k=1: 2320.975 Hz, -114.0 dB | -109.8 | 0.0 % |
| Netz 50 Hz | acdc1 Out 1 → Startup → UMC In 1 | 49.9812 | 0.0047 | 12/19 | k=1: 49.985 Hz, -93.1 dB | -94.9 | 1.5 % |
| stärkste übrige Linie (6001.11 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 6001.1127 | 0.0001 | 3/3 | k=1: 6001.113 Hz, -81.1 dB | -81.0 | 26.0 % |
| stärkste übrige Linie (75.74 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 75.7366 | 0.0008 | 2/315 | k=1: 75.735 Hz, -90.2 dB | -93.3 | 1.5 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6001.113 | -81.1 | 58.6 | other1·1 |
| 12002.225 | -84.0 | 56.3 | other1·2 |
| 18003.338 | -83.2 | 57.4 | other1·3 |
| 75.735 | -90.2 | 32.7 | other2·1 |
| 49.985 | -93.1 | 23.2 | mains50·1 |
| 16003.518 | -97.5 | 43.2 | – |
| 8001.759 | -96.8 | 42.3 | – |
| 44.767 | -98.4 | 17.1 | – |
| 89.532 | -100.6 | 27.9 | – |
| 1215.415 | -102.8 | 36.5 | – |
| 4000.026 | -103.9 | 33.4 | – |
| 82.634 | -104.6 | 21.4 | – |
| 7385.985 | -104.2 | 35.9 | – |
| 6621.918 | -105.0 | 35.2 | – |
| 2000.367 | -106.1 | 29.4 | usb1k·2 |
| 239.872 | -105.8 | 29.0 | – |
| 299.841 | -105.7 | 30.3 | – |
| 249.910 | -106.4 | 28.7 | mains50·5 |
| 5000.908 | -106.4 | 33.3 | usb1k·5 |
| 3000.544 | -105.1 | 33.9 | usb1k·3 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | acdc1 Out 1 → Startup → UMC In 1 | 16/23 | 10.21 | 10.24 | 1.65 |
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.10 | 0.01 | 0.14 |
| led | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 1.01 | -0.38 | 0.57 |
| mains50 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 87.91 | -6.43 | 1.04 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.10 | 0.01 | 0.15 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 33.25 | -22.79 | 0.38 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 1.41 | 24.06 s (0.04 Hz) | 22.4 |
| acdc1 Out 1 → Startup → UMC In 1 | 6001.1 Hz ± 10 | 0.58 | 30.07 s (0.03 Hz) | 26.6 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1 | 0.5 | – | – |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz G0

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -75.1 | -57.4 | -17.8 | 2 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G1_psd.png)

### Kammprofile

![Kammprofile](G1_combs.png)

### Zeitverlauf

![Zeitverlauf](G1_timeline.png)
