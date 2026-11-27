# Report G4: G4 – acdc1 Out 1, Alltags-USB-Kette, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | G4: wie G1, AC/DC im Alltags-Aufbau: passiver USB-Hub → USB-Hub im Monitor → TB-Hub |
| gain | g12 |
| usb | usb-plugged, passiver Hub → Monitor-Hub → TB-Hub (UMC am TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g4-daily-hub-chain_g12_usb-plugged.2chan.000.wav` |
| Format | 48000 Hz, 120.0 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis G4 --ref G1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -75.7 | -86.9 | -76.1 | -78.4 | -86.9 | -76.7 | -80.9 | -77.8 | 3 % | -77.9 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.0531 | 0.0005 | 23/23 | k=5: 5000.265 Hz, -103.8 dB | -99.2 | 0.7 % |
| LED-PWM (≈ 2,32 kHz) | acdc1 Out 1 → Startup → UMC In 1 | 2320.9753 | 0.0005 | 10/10 | k=1: 2320.975 Hz, -113.9 dB | -109.9 | 0.1 % |
| Netz 50 Hz | acdc1 Out 1 → Startup → UMC In 1 | 50.0222 | 0.0138 | 15/19 | k=1: 50.021 Hz, -93.6 dB | -94.5 | 2.2 % |
| stärkste übrige Linie (6001.11 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 6001.1132 | 0.0001 | 3/3 | k=1: 6001.113 Hz, -81.1 dB | -81.2 | 31.1 % |
| stärkste übrige Linie (75.74 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 75.7352 | 0.0000 | 1/315 | k=1: 75.735 Hz, -89.9 dB | -93.1 | 2.0 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6001.113 | -81.1 | 58.5 | other1·1 |
| 12002.227 | -84.1 | 56.4 | other1·2 |
| 18003.340 | -83.7 | 56.7 | other1·3 |
| 75.735 | -89.9 | 42.7 | other2·1 |
| 50.021 | -93.6 | 36.4 | mains50·1 |
| 10.019 | -97.0 | 24.4 | – |
| 44.766 | -97.6 | 31.6 | – |
| 8001.759 | -99.1 | 38.7 | – |
| 16003.519 | -99.4 | 40.5 | – |
| 12.021 | -99.6 | 22.6 | – |
| 14.025 | -100.3 | 22.7 | – |
| 16.029 | -100.7 | 23.1 | – |
| 89.532 | -101.4 | 31.9 | – |
| 250.109 | -100.9 | 35.8 | mains50·5 |
| 20.032 | -100.3 | 24.5 | – |
| 18.032 | -101.6 | 22.7 | – |
| 22.038 | -101.4 | 24.1 | – |
| 13.797 | -101.1 | 21.8 | – |
| 24.042 | -102.6 | 23.5 | – |
| 82.633 | -102.8 | 29.9 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 22/22 | 12.57 | -1.07 | 0.43 |
| led | acdc1 Out 1 → Startup → UMC In 1 | 22/22 | 2.16 | 0.65 | 0.46 |
| mains50 | acdc1 Out 1 → Startup → UMC In 1 | 22/22 | 175.72 | -142.66 | 0.52 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 22/22 | 0.02 | -0.01 | 0.06 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 22/22 | 25.11 | 4.57 | 0.25 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 0.78 | 0.17 s (6.01 Hz) | 25.1 |
| acdc1 Out 1 → Startup → UMC In 1 | 6001.1 Hz ± 10 | 0.56 | 1.26 s (0.79 Hz) | 35.8 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | acdc1 Out 1 → Startup → UMC In 1 |
|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | 1.00 |

## Vergleich mit Referenz G1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | -76.1 | -75.1 | -0.9 | 3 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G4_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G4_psd.png)

### Kammprofile

![Kammprofile](G4_combs.png)

### Zeitverlauf

![Zeitverlauf](G4_timeline.png)

## Notiz aus dem Manifest

> Host-Software nur UMC. Datei-Werte mit Host-Faktor 2.
