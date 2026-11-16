# Report G4-in-no-out-2: G4-in-no-out-2 – acdc1 Eingänge offen, Alltags-Aufbau, Ausgänge frei, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | G4-in-no-out (Wiederholung): AC/DC-Eingänge 1–4 offen, Alltags-USB-Kette, Ausgänge frei, UMC-Ausgänge an Boxen/Kopfhörer |
| gain | g12 |
| usb | usb-duplex, passiver Hub → Monitor-Hub → TB-Hub |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g4-in-daily-no-out-2_g12_usb-duplex.4chan.000.wav` |
| Format | 48000 Hz, 120.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis G4-in-no-out-2 --ref A5-b1d` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -66.0 | -76.1 | -66.5 | -70.9 | -71.8 | -69.3 | -89.3 | -66.5 | 15 % | -67.2 | 0.7 |
| Kanal 2 | -6.4 | -66.0 | -76.6 | -66.4 | -71.2 | -71.5 | -69.4 | -90.0 | -66.4 | 13 % | -67.0 | 0.6 |
| Kanal 3 | -4.8 | -68.4 | -79.2 | -68.7 | -73.2 | -74.2 | -71.5 | -92.1 | -68.8 | 19 % | -69.7 | 0.9 |
| Kanal 4 | -4.9 | -67.9 | -78.5 | -68.3 | -72.4 | -73.9 | -70.9 | -88.8 | -68.3 | 18 % | -69.2 | 0.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0001 | 0.0052 | 3/3 | k=1: 5999.996 Hz, -80.2 dB | -79.6 | 4.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0043 | 23/23 | k=1: 999.873 Hz, -79.4 dB | -77.1 | 8.7 % |
| Netz 50 Hz | Kanal 1 | 49.9812 | 0.0000 | 1/19 | k=1: 49.981 Hz, -99.7 dB | -99.8 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0040 | 144 | k=8·f1+2·f2: 19998.942 Hz, -97.8 dB | -86.3 | 1.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7174 | 0.0030 | 3/315 | k=1: 75.718 Hz, -91.0 dB | -93.5 | 0.2 % |
| stärkste übrige Linie (999.91 Hz) | Kanal 1 | 999.9089 | 0.0099 | 8/23 | k=1: 999.914 Hz, -93.0 dB | -91.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0001 | 0.0052 | 3/3 | k=1: 5999.996 Hz, -80.1 dB | -79.6 | 4.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0045 | 23/23 | k=1: 999.873 Hz, -80.4 dB | -77.9 | 7.0 % |
| Netz 50 Hz | Kanal 2 | 49.9814 | 0.0000 | 1/19 | k=1: 49.981 Hz, -100.3 dB | -100.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0041 | 142 | k=8·f1+2·f2: 19998.942 Hz, -97.8 dB | -86.3 | 1.0 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7174 | 0.0043 | 4/315 | k=1: 75.718 Hz, -91.7 dB | -93.8 | 0.2 % |
| stärkste übrige Linie (999.91 Hz) | Kanal 2 | 999.9155 | 0.0063 | 7/23 | k=1: 999.914 Hz, -93.9 dB | -92.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0001 | 0.0052 | 3/3 | k=1: 5999.996 Hz, -80.5 dB | -79.8 | 7.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0045 | 23/23 | k=1: 999.873 Hz, -81.6 dB | -79.1 | 9.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0048 | 9/10 | k=4: 9282.181 Hz, -126.6 dB | -121.5 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9821 | 0.0015 | 2/19 | k=1: 49.981 Hz, -101.3 dB | -100.7 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0042 | 153 | k=8·f1+2·f2: 19998.942 Hz, -98.1 dB | -86.5 | 1.7 % |
| stärkste übrige Linie (999.91 Hz) | Kanal 3 | 999.9130 | 0.0107 | 9/23 | k=1: 999.914 Hz, -95.1 dB | -93.6 | 0.3 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7180 | 0.0001 | 2/315 | k=1: 75.718 Hz, -95.0 dB | -97.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0001 | 0.0052 | 3/3 | k=1: 5999.996 Hz, -81.6 dB | -80.9 | 5.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0045 | 23/23 | k=1: 999.873 Hz, -80.0 dB | -77.7 | 11.7 % |
| Netz 50 Hz | Kanal 4 | 49.9811 | 0.0000 | 1/19 | k=1: 49.981 Hz, -102.7 dB | -102.7 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0041 | 143 | k=8·f1+2·f2: 19998.942 Hz, -99.3 dB | -87.6 | 1.2 % |
| stärkste übrige Linie (999.91 Hz) | Kanal 4 | 999.9176 | 0.0110 | 8/23 | k=1: 999.913 Hz, -93.6 dB | -92.1 | 0.4 % |
| stärkste übrige Linie (999.83 Hz) | Kanal 4 | 999.8222 | 0.0052 | 5/23 | k=1: 999.825 Hz, -95.5 dB | -91.6 | 0.5 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.873 | -79.4 | 47.7 | usb1k·1 |
| 5999.996 | -80.2 | 54.7 | fs8·1 |
| 18000.004 | -83.4 | 54.4 | fs8·3 |
| 1999.733 | -84.4 | 45.5 | usb1k·2 |
| 2999.608 | -85.2 | 47.1 | usb1k·3 |
| 12000.007 | -86.3 | 49.2 | – |
| 6999.076 | -89.4 | 46.8 | usb1k·7 |
| 75.718 | -91.0 | 30.4 | other1·1 |
| 999.914 | -93.0 | 34.1 | other2·1 |
| 999.825 | -94.9 | 32.3 | – |
| 15997.885 | -94.4 | 43.8 | usb1k·16 |
| 10998.543 | -95.7 | 43.3 | usb1k·11 |
| 14998.010 | -96.1 | 43.3 | usb1k·15 |
| 9998.668 | -95.9 | 41.7 | usb1k·10 |
| 5999.201 | -96.9 | 37.8 | usb1k·6 |
| 999.948 | -97.7 | 29.4 | – |
| 12999.072 | -98.1 | 40.9 | imd·7·f1+1·f2 |
| 19998.942 | -97.8 | 41.7 | imd·8·f1+2·f2 |
| 16998.538 | -98.3 | 40.6 | imd·11·f1+1·f2 |
| 44.765 | -98.7 | 21.4 | – |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.873 | -80.4 | 46.9 | usb1k·1 |
| 5999.996 | -80.1 | 55.8 | fs8·1 |
| 18000.004 | -83.3 | 55.6 | fs8·3 |
| 2999.608 | -85.9 | 46.9 | usb1k·3 |
| 1999.733 | -85.5 | 44.4 | usb1k·2 |
| 12000.007 | -86.1 | 50.3 | – |
| 6999.076 | -89.7 | 47.1 | usb1k·7 |
| 75.718 | -91.7 | 30.3 | other1·1 |
| 999.914 | -93.9 | 33.4 | other2·1 |
| 15997.885 | -94.9 | 44.5 | usb1k·16 |
| 999.825 | -95.9 | 31.4 | – |
| 10998.543 | -95.8 | 44.5 | usb1k·11 |
| 14998.010 | -95.8 | 45.1 | usb1k·15 |
| 9998.668 | -96.1 | 42.8 | – |
| 5999.201 | -97.8 | 37.9 | usb1k·6 |
| 12999.072 | -98.1 | 42.4 | imd·7·f1+1·f2 |
| 19998.942 | -97.8 | 43.1 | imd·8·f1+2·f2 |
| 999.948 | -98.6 | 28.6 | – |
| 16998.538 | -98.2 | 41.7 | imd·11·f1+1·f2 |
| 5999.960 | -98.6 | 37.3 | – |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.873 | -81.6 | 48.3 | usb1k·1 |
| 5999.996 | -80.5 | 57.8 | fs8·1 |
| 18000.004 | -83.6 | 57.1 | fs8·3 |
| 12000.007 | -86.1 | 52.2 | – |
| 2999.608 | -86.8 | 49.0 | usb1k·3 |
| 1999.733 | -86.9 | 45.7 | usb1k·2 |
| 6999.076 | -90.3 | 49.5 | usb1k·7 |
| 999.914 | -95.1 | 34.7 | other1·1 |
| 75.718 | -95.0 | 29.9 | other2·1 |
| 14998.010 | -96.0 | 47.7 | usb1k·15 |
| 10998.543 | -96.3 | 46.9 | usb1k·11 |
| 15997.885 | -95.6 | 46.1 | usb1k·16 |
| 999.825 | -97.2 | 32.8 | – |
| 9998.668 | -96.6 | 44.8 | – |
| 12999.072 | -98.2 | 45.1 | imd·7·f1+1·f2 |
| 19998.942 | -98.1 | 45.5 | imd·8·f1+2·f2 |
| 16998.538 | -98.5 | 44.3 | imd·11·f1+1·f2 |
| 5999.201 | -98.9 | 39.1 | usb1k·6 |
| 5999.960 | -98.9 | 39.4 | – |
| 14999.600 | -99.2 | 44.5 | imd·3·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.873 | -80.0 | 49.2 | usb1k·1 |
| 5999.996 | -81.6 | 55.4 | fs8·1 |
| 1999.733 | -84.2 | 47.7 | usb1k·2 |
| 18000.004 | -84.6 | 54.8 | fs8·3 |
| 2999.608 | -86.3 | 48.1 | usb1k·3 |
| 12000.007 | -87.4 | 49.8 | – |
| 6999.076 | -90.5 | 47.6 | usb1k·7 |
| 999.913 | -93.6 | 35.6 | other1·1 |
| 999.825 | -95.5 | 33.7 | other2·1 |
| 15997.885 | -95.2 | 44.4 | usb1k·16 |
| 10998.543 | -96.6 | 44.2 | usb1k·11 |
| 5999.201 | -97.1 | 39.7 | usb1k·6 |
| 14998.010 | -97.3 | 43.7 | usb1k·15 |
| 75.718 | -96.7 | 27.3 | – |
| 9998.668 | -97.0 | 42.4 | – |
| 4999.342 | -97.5 | 41.3 | usb1k·5 |
| 999.948 | -98.3 | 30.8 | – |
| 19998.942 | -99.3 | 42.0 | imd·8·f1+2·f2 |
| 12999.071 | -99.6 | 41.3 | imd·7·f1+1·f2 |
| 999.774 | -99.7 | 29.5 | – |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.92 | -0.16 | 0.46 |
| usb1k | Kanal 1 | 23/23 | 5.38 | -0.30 | 0.63 |
| mains50 | Kanal 1 | 22/23 | 597.44 | -278.97 | 0.98 |
| other1 | Kanal 1 | 22/23 | 24.35 | -16.29 | 0.43 |
| other2 | Kanal 1 | 23/23 | 5.38 | -0.30 | 0.65 |
| fs8 | Kanal 2 | 23/23 | 0.92 | -0.16 | 0.46 |
| usb1k | Kanal 2 | 23/23 | 5.35 | -0.31 | 0.62 |
| mains50 | Kanal 2 | 22/23 | 643.06 | -8.78 | 0.95 |
| other1 | Kanal 2 | 23/23 | 31.89 | 3.04 | 5.18 |
| other2 | Kanal 2 | 23/23 | 5.35 | -0.31 | 0.65 |
| fs8 | Kanal 3 | 23/23 | 0.92 | -0.16 | 0.46 |
| usb1k | Kanal 3 | 23/23 | 5.38 | -0.24 | 0.62 |
| led | Kanal 3 | 23/23 | 4.99 | -1.40 | 1.46 |
| mains50 | Kanal 3 | 22/23 | 615.32 | 128.28 | 0.81 |
| other1 | Kanal 3 | 23/23 | 5.38 | -0.24 | 0.64 |
| other2 | Kanal 3 | 22/23 | 34.43 | -24.02 | 0.42 |
| fs8 | Kanal 4 | 23/23 | 0.92 | -0.16 | 0.46 |
| usb1k | Kanal 4 | 23/23 | 5.40 | -0.24 | 0.63 |
| mains50 | Kanal 4 | 22/23 | 655.91 | -34.88 | 0.86 |
| other1 | Kanal 4 | 23/23 | 5.40 | -0.24 | 0.66 |
| other2 | Kanal 4 | 23/23 | 5.40 | -0.24 | 0.65 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.15 | 1.26 s (0.79 Hz) | 17.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.73 | 1.26 s (0.79 Hz) | 28.5 |
| Kanal 2 | breitbandig | 1.08 | 1.26 s (0.79 Hz) | 17.1 |
| Kanal 2 | 999.9 Hz ± 10 | 0.76 | 1.26 s (0.79 Hz) | 29.1 |
| Kanal 3 | breitbandig | 0.96 | 1.26 s (0.79 Hz) | 20.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.71 | 1.26 s (0.79 Hz) | 31.2 |
| Kanal 4 | breitbandig | 1.02 | 1.26 s (0.79 Hz) | 18.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.68 | 1.26 s (0.79 Hz) | 28.8 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| Kanal 1 | 5 | 2.5 | 14.377 | 1.10 |
| Kanal 2 | 5 | 2.5 | 14.377 | 1.10 |
| Kanal 3 | 5 | 2.5 | 14.377 | 1.10 |
| Kanal 4 | 5 | 2.5 | 14.377 | 1.10 |

## Korrelation zwischen Kanälen

| | Kanal 1 | Kanal 2 | Kanal 3 | Kanal 4 |
|---|---|---|---|---|
| Kanal 1 | 1.00 | 0.98 | 0.98 | 0.97 |
| Kanal 2 | 0.98 | 1.00 | 0.98 | 0.98 |
| Kanal 3 | 0.98 | 0.98 | 1.00 | 0.97 |
| Kanal 4 | 0.97 | 0.98 | 0.97 | 1.00 |

## Vergleich mit Referenz A5-b1d

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -66.5 | -72.5 | +6.0 | 15 % | 57 % |
| Kanal 2 | -66.4 | -73.0 | +6.6 | 13 % | 66 % |
| Kanal 3 | -68.7 | -75.0 | +6.2 | 19 % | 74 % |
| Kanal 4 | -68.3 | -72.6 | +4.3 | 18 % | 64 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G4-in-no-out-2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G4-in-no-out-2_psd.png)

### Kammprofile

![Kammprofile](G4-in-no-out-2_combs.png)

### Zeitverlauf

![Zeitverlauf](G4-in-no-out-2_timeline.png)

## Notiz aus dem Manifest

> Datei-Werte mit Host-Faktor 2. Vergleich mit A5-b1d (TB-Hub direkt, Host-Software Duplex mit Stille, nichts an den Ausgängen).
