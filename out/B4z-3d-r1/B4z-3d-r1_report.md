# Report B4z-3d-r1: B4z-3d-r1 – acdc1 3d-open-inputs-4z, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4z-Sitzung: Startkontrolle 3d vor fx3k/fx3kp, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-open-inputs-4z-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4z-3d-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -70.7 | -80.2 | -71.2 | -72.4 | -86.2 | -71.6 | – | -71.2 | 67 % | -76.0 | 4.8 |
| Kanal 2 | -7.1 | -71.1 | -80.0 | -71.7 | -72.9 | -88.0 | -72.0 | – | -71.7 | 73 % | -77.4 | 5.7 |
| Kanal 3 | -5.1 | -72.2 | -80.7 | -72.9 | -74.1 | -92.4 | -73.2 | – | -72.9 | 83 % | -80.5 | 7.6 |
| Kanal 4 | -6.4 | -70.5 | -80.1 | -71.0 | -72.0 | -88.1 | -71.3 | – | -71.0 | 73 % | -76.8 | 5.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -77.9 dB | -78.0 | 21.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -75.1 | 41.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -112.9 dB | -107.4 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0000 | 0.0038 | 2/19 | k=1: 50.005 Hz, -98.0 dB | -100.8 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0010 | 150 | k=8·f1+1·f2: 13998.941 Hz, -94.1 dB | -84.2 | 5.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.4 | 27.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0006 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.7 | 39.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0006 | 10/10 | k=9: 20884.904 Hz, -112.6 dB | -106.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0059 | 0.0003 | 2/19 | k=1: 50.006 Hz, -98.0 dB | -100.9 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0009 | 159 | k=8·f1+1·f2: 13998.941 Hz, -93.4 dB | -83.7 | 6.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.6 dB | -77.6 | 33.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0008 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.7 | 41.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.090 Hz, -112.9 dB | -107.9 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0059 | 0.0004 | 3/19 | k=1: 50.006 Hz, -98.4 dB | -101.2 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0009 | 165 | k=8·f1+1·f2: 13998.941 Hz, -93.8 dB | -84.0 | 7.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.7 dB | -77.6 | 22.0 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.4 | 46.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.544 Hz, -112.3 dB | -107.2 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0060 | 0.0002 | 2/19 | k=1: 50.006 Hz, -98.0 dB | -100.9 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0011 | 156 | k=8·f1+1·f2: 13998.941 Hz, -93.4 dB | -83.8 | 5.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 57.1 | usb1k·1 |
| 6000.000 | -77.9 | 56.4 | fs8·1 |
| 18000.000 | -80.7 | 55.7 | fs8·3 |
| 12000.000 | -81.3 | 54.4 | fs8·2 |
| 2999.603 | -81.9 | 51.0 | usb1k·3 |
| 1999.735 | -82.6 | 50.4 | usb1k·2 |
| 6999.073 | -86.5 | 49.1 | usb1k·7 |
| 15997.882 | -90.9 | 45.5 | usb1k·16 |
| 9998.676 | -91.2 | 44.5 | usb1k·10 |
| 14998.014 | -94.0 | 41.4 | usb1k·15 |
| 10998.544 | -93.2 | 42.2 | usb1k·11 |
| 15999.471 | -94.8 | 41.6 | imd·4·f1+2·f2 |
| 9999.471 | -95.1 | 40.7 | imd·4·f1+1·f2 |
| 13998.941 | -94.1 | 41.9 | imd·8·f1+1·f2 |
| 12999.868 | -95.8 | 39.0 | imd·1·f1+2·f2 |
| 19998.941 | -95.0 | 41.4 | imd·8·f1+2·f2 |
| 5999.206 | -95.6 | 38.7 | usb1k·6 |
| 18999.868 | -96.7 | 39.9 | imd·1·f1+3·f2 |
| 20997.220 | -96.5 | 39.2 | usb1k·21 |
| 11998.411 | -96.1 | 39.6 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 57.7 | usb1k·1 |
| 6000.000 | -77.3 | 58.4 | fs8·1 |
| 18000.000 | -80.3 | 57.3 | fs8·3 |
| 12000.000 | -80.5 | 56.7 | fs8·2 |
| 2999.603 | -82.0 | 52.2 | usb1k·3 |
| 1999.735 | -83.8 | 50.2 | usb1k·2 |
| 6999.073 | -86.1 | 50.6 | usb1k·7 |
| 15997.882 | -90.9 | 46.4 | usb1k·16 |
| 9998.676 | -91.2 | 46.0 | usb1k·10 |
| 14998.014 | -93.5 | 43.1 | usb1k·15 |
| 10998.544 | -92.9 | 43.8 | usb1k·11 |
| 15999.471 | -94.2 | 43.2 | imd·4·f1+2·f2 |
| 9999.471 | -94.4 | 42.8 | imd·4·f1+1·f2 |
| 13998.941 | -93.4 | 43.9 | imd·8·f1+1·f2 |
| 12999.868 | -95.5 | 41.0 | imd·1·f1+2·f2 |
| 11998.411 | -95.2 | 42.0 | usb1k·12 |
| 7998.941 | -94.5 | 42.1 | usb1k·8 |
| 19998.941 | -94.7 | 42.8 | imd·8·f1+2·f2 |
| 8999.603 | -96.3 | 40.7 | imd·3·f1+1·f2 |
| 18999.868 | -96.4 | 41.0 | imd·1·f1+3·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 60.8 | usb1k·1 |
| 6000.000 | -77.6 | 61.1 | fs8·1 |
| 12000.000 | -80.7 | 59.3 | fs8·2 |
| 18000.000 | -80.7 | 59.4 | fs8·3 |
| 2999.603 | -82.9 | 55.0 | usb1k·3 |
| 1999.735 | -85.7 | 52.8 | usb1k·2 |
| 6999.073 | -86.9 | 52.9 | usb1k·7 |
| 15997.882 | -91.7 | 47.7 | usb1k·16 |
| 9998.676 | -91.6 | 48.2 | usb1k·10 |
| 14998.014 | -93.6 | 45.9 | usb1k·15 |
| 10998.544 | -93.4 | 45.8 | usb1k·11 |
| 15999.471 | -94.5 | 44.9 | imd·4·f1+2·f2 |
| 9999.471 | -94.8 | 44.9 | imd·4·f1+1·f2 |
| 13998.941 | -93.8 | 45.7 | imd·8·f1+1·f2 |
| 12999.868 | -95.6 | 43.5 | imd·1·f1+2·f2 |
| 7998.941 | -94.6 | 44.4 | usb1k·8 |
| 19998.941 | -94.9 | 44.7 | imd·8·f1+2·f2 |
| 11998.411 | -95.6 | 44.3 | usb1k·12 |
| 8999.603 | -96.6 | 43.1 | imd·3·f1+1·f2 |
| 12999.073 | -95.7 | 43.3 | imd·7·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 59.0 | usb1k·1 |
| 6000.000 | -77.7 | 57.7 | fs8·1 |
| 12000.000 | -80.5 | 55.7 | fs8·2 |
| 18000.000 | -80.5 | 55.9 | fs8·3 |
| 1999.735 | -81.2 | 52.5 | usb1k·2 |
| 2999.603 | -81.1 | 52.8 | usb1k·3 |
| 6999.073 | -85.4 | 50.0 | usb1k·7 |
| 15997.882 | -89.9 | 46.3 | usb1k·16 |
| 9998.676 | -90.8 | 45.5 | usb1k·10 |
| 10998.543 | -92.4 | 43.6 | usb1k·11 |
| 14998.014 | -93.8 | 42.1 | usb1k·15 |
| 15999.471 | -94.2 | 42.1 | imd·4·f1+2·f2 |
| 9999.471 | -94.5 | 41.8 | imd·4·f1+1·f2 |
| 13998.941 | -93.4 | 42.8 | imd·8·f1+1·f2 |
| 5999.206 | -94.2 | 41.1 | usb1k·6 |
| 11998.411 | -94.9 | 41.4 | usb1k·12 |
| 4999.338 | -95.1 | 39.7 | usb1k·5 |
| 12999.868 | -96.0 | 39.3 | imd·1·f1+2·f2 |
| 20997.220 | -95.8 | 40.4 | usb1k·21 |
| 19998.941 | -95.0 | 41.3 | imd·8·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.16 | 0.31 | 0.06 |
| led | Kanal 1 | 11/11 | 1.22 | 1.30 | 0.55 |
| mains50 | Kanal 1 | 11/11 | 242.96 | -229.71 | 1.02 |
| fs8 | Kanal 2 | 11/11 | 0.03 | -0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.13 | 0.25 | 0.06 |
| led | Kanal 2 | 11/11 | 0.51 | -0.12 | 0.38 |
| mains50 | Kanal 2 | 11/11 | 747.69 | -345.38 | 0.86 |
| fs8 | Kanal 3 | 11/11 | 0.03 | 0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.13 | 0.21 | 0.05 |
| led | Kanal 3 | 11/11 | 0.47 | 0.61 | 0.41 |
| mains50 | Kanal 3 | 11/11 | 642.45 | 125.19 | 0.45 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.00 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.11 | 0.21 | 0.03 |
| led | Kanal 4 | 11/11 | 1.20 | 1.62 | 0.44 |
| mains50 | Kanal 4 | 11/11 | 739.14 | -329.92 | 0.86 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.69 | 0.31 s (3.18 Hz) | 19.8 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 1.25 s (0.80 Hz) | 31.2 |
| Kanal 2 | breitbandig | 0.74 | 0.31 s (3.18 Hz) | 22.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.91 | 1.25 s (0.80 Hz) | 33.6 |
| Kanal 3 | breitbandig | 0.76 | 12.00 s (0.08 Hz) | 25.2 |
| Kanal 3 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 36.5 |
| Kanal 4 | breitbandig | 0.66 | 0.31 s (3.18 Hz) | 23.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 33.1 |

Prominenz < ≈ 10 dB ist nicht von Zufall zu unterscheiden.

**Klicks** (Hochpass, Schwelle Median + 8·MAD):

| Kanal | Anzahl | pro Minute | Abstand Median [s] | Variationskoeff. |
|---|---|---|---|---|
| Kanal 1 | 0 | 0.0 | – | – |
| Kanal 2 | 0 | 0.0 | – | – |
| Kanal 3 | 0 | 0.0 | – | – |
| Kanal 4 | 0 | 0.0 | – | – |

## Korrelation zwischen Kanälen

| | Kanal 1 | Kanal 2 | Kanal 3 | Kanal 4 |
|---|---|---|---|---|
| Kanal 1 | 1.00 | 0.96 | 0.91 | 0.94 |
| Kanal 2 | 0.96 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.91 | 0.94 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.96 | 0.91 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.2 | -71.1 | -0.1 | 67 % | 68 % |
| Kanal 2 | -71.7 | -71.9 | +0.2 | 73 % | 73 % |
| Kanal 3 | -72.9 | -73.1 | +0.2 | 83 % | 82 % |
| Kanal 4 | -71.0 | -71.0 | -0.0 | 73 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4z-3d-r1_psd.png)

### Kammprofile

![Kammprofile](B4z-3d-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4z-3d-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 19:03:47. Stream-Meldungen: 0. owl_read: out/owl_read/B4z-3d-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
