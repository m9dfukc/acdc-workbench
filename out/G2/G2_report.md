# Report G2: G2 – acdc1 Out 1, ohne Monitor, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d, Out 1 über Startup → UMC |
| test | G2: wie G0, Monitor-Kabel am Hub abgezogen |
| gain | g12 |
| usb | usb-plugged, Mac-Port (UMC am Hub) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g2-no-monitor_g12_usb-plugged.2chan.000.wav` |
| Format | 48000 Hz, 120.5 s, 1 Kanäle |
| Erzeugt mit | `uv run python -m analysis G2 --ref G0` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | +0.0 | -55.4 | -64.8 | -56.0 | -59.8 | -58.3 | -59.7 | -62.9 | -57.0 | 12 % | -57.5 | 0.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | acdc1 Out 1 → Startup → UMC In 1 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -94.0 dB | -96.7 | 0.0 % |
| 1-kHz-Kamm | acdc1 Out 1 → Startup → UMC In 1 | 1000.2199 | 0.0003 | 20/23 | k=2: 2000.440 Hz, -65.8 dB | -66.1 | 12.3 % |
| LED-PWM (≈ 2,32 kHz) | acdc1 Out 1 → Startup → UMC In 1 | 2320.3328 | 0.0000 | 1/10 | k=1: 2320.333 Hz, -102.1 dB | -104.8 | 0.0 % |
| Mischprodukte n·1000.2199 + m·6000.0000 Hz (m = ±1…±4) | acdc1 Out 1 → Startup → UMC In 1 | 1000.2199 | 0.0006 | 4 | k=-1·f1+1·f2: 4999.780 Hz, -104.1 dB | -104.2 | 0.0 % |
| stärkste übrige Linie (29.20 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 29.1944 | 0.0102 | 58/817 | k=1: 29.196 Hz, -63.5 dB | -63.9 | 16.0 % |
| stärkste übrige Linie (61.62 Hz) | acdc1 Out 1 → Startup → UMC In 1 | 61.6150 | 0.0041 | 4/387 | k=1: 61.616 Hz, -70.4 dB | -69.8 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### acdc1 Out 1 → Startup → UMC In 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 29.196 | -63.5 | 37.1 | other1·1 |
| 2000.440 | -65.8 | 47.8 | usb1k·2 |
| 1000.220 | -69.3 | 46.9 | usb1k·1 |
| 58.392 | -70.1 | 28.9 | other1·2 |
| 61.616 | -70.4 | 28.7 | other2·1 |
| 87.585 | -70.8 | 32.2 | other1·3 |
| 61.641 | -71.9 | 27.2 | – |
| 3000.660 | -71.9 | 46.6 | usb1k·3 |
| 87.497 | -73.5 | 29.5 | – |
| 87.647 | -73.7 | 29.3 | – |
| 116.694 | -74.0 | 29.8 | – |
| 120.008 | -74.6 | 30.4 | – |
| 120.035 | -74.2 | 30.8 | – |
| 210.847 | -74.7 | 33.7 | – |
| 61.588 | -75.8 | 23.2 | – |
| 61.730 | -76.2 | 22.9 | – |
| 149.231 | -76.4 | 28.4 | – |
| 116.775 | -76.1 | 27.8 | other1·4 |
| 4000.879 | -75.5 | 43.1 | usb1k·4 |
| 149.204 | -76.8 | 27.9 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 2.53 | 1.54 | 1.74 |
| usb1k | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 0.91 | 0.18 | 0.75 |
| led | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 52.04 | -33.45 | 1.39 |
| other1 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 651.99 | 156.57 | 0.91 |
| other2 | acdc1 Out 1 → Startup → UMC In 1 | 23/23 | 21.60 | -0.99 | 1.53 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| acdc1 Out 1 → Startup → UMC In 1 | breitbandig | 2.71 | 17.21 s (0.06 Hz) | 18.2 |
| acdc1 Out 1 → Startup → UMC In 1 | 29.2 Hz ± 10 | 5.20 | 0.45 s (2.23 Hz) | 21.6 |

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
| acdc1 Out 1 → Startup → UMC In 1 | -56.0 | -57.4 | +1.4 | 12 % | 2 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G2_psd.png)

### Kammprofile

![Kammprofile](G2_combs.png)

### Zeitverlauf

![Zeitverlauf](G2_timeline.png)
