# Report B5-3d-end-r1: B5-3d-end-r1 – acdc1 3d-end-open-inputs-5, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-5-Sitzung: Endkontrolle 3d nach fx3l/fx3lp, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-5-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B5-3d-end-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-end-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -69.3 | -74.4 | -70.9 | -72.0 | -85.3 | -71.3 | – | -70.9 | 67 % | -75.7 | 4.8 |
| Kanal 2 | -7.1 | -70.4 | -76.4 | -71.7 | -72.8 | -87.2 | -72.1 | – | -71.7 | 72 % | -77.2 | 5.5 |
| Kanal 3 | -5.4 | -72.0 | -78.4 | -73.1 | -74.2 | -91.5 | -73.4 | – | -73.1 | 81 % | -80.4 | 7.3 |
| Kanal 4 | -6.2 | -70.1 | -78.2 | -70.8 | -71.7 | -87.4 | -71.1 | – | -70.8 | 74 % | -76.6 | 5.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -78.3 | 18.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.5 | 44.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0009 | 10/10 | k=1: 2320.545 Hz, -115.6 dB | -112.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9606 | 0.0000 | 1/19 | k=1: 49.961 Hz, -97.8 dB | -100.9 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0010 | 148 | k=8·f1+1·f2: 13998.940 Hz, -94.6 dB | -84.8 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.2 | 22.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0005 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.3 | 44.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=9: 20884.904 Hz, -114.8 dB | -110.1 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9607 | 0.0000 | 1/19 | k=1: 49.961 Hz, -98.7 dB | -101.8 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0008 | 155 | k=8·f1+1·f2: 13998.940 Hz, -94.5 dB | -84.7 | 5.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.4 dB | -78.4 | 29.4 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -76.6 | 45.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0011 | 10/10 | k=1: 2320.545 Hz, -116.9 dB | -112.4 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9602 | 0.0004 | 2/19 | k=1: 49.960 Hz, -99.2 dB | -102.1 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0008 | 160 | k=8·f1+1·f2: 13998.940 Hz, -94.7 dB | -84.9 | 6.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.4 | 17.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0005 | 23/23 | k=1: 999.868 Hz, -72.2 dB | -73.7 | 52.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0011 | 10/10 | k=1: 2320.544 Hz, -115.1 dB | -111.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9605 | 0.0000 | 1/19 | k=1: 49.961 Hz, -99.3 dB | -102.4 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0010 | 150 | k=8·f1+1·f2: 13998.940 Hz, -94.6 dB | -84.8 | 4.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 57.0 | usb1k·1 |
| 6000.000 | -78.1 | 56.2 | fs8·1 |
| 1999.735 | -81.2 | 51.2 | usb1k·2 |
| 12000.000 | -81.5 | 54.4 | fs8·2 |
| 18000.000 | -81.5 | 54.4 | fs8·3 |
| 2999.603 | -81.5 | 51.3 | usb1k·3 |
| 6999.073 | -86.8 | 48.0 | usb1k·7 |
| 15997.879 | -91.0 | 44.5 | usb1k·16 |
| 9998.675 | -91.2 | 44.1 | usb1k·10 |
| 5999.205 | -93.3 | 41.0 | usb1k·6 |
| 4999.338 | -94.6 | 38.9 | usb1k·5 |
| 10998.542 | -93.5 | 42.3 | usb1k·11 |
| 14998.012 | -95.0 | 40.8 | usb1k·15 |
| 13998.940 | -94.6 | 41.1 | imd·8·f1+1·f2 |
| 9999.470 | -95.4 | 39.9 | imd·4·f1+1·f2 |
| 15999.470 | -95.5 | 40.1 | imd·4·f1+2·f2 |
| 12999.073 | -96.0 | 40.1 | imd·7·f1+1·f2 |
| 12999.868 | -96.9 | 39.3 | imd·1·f1+2·f2 |
| 20997.217 | -97.0 | 38.5 | usb1k·21 |
| 19998.940 | -96.0 | 39.5 | imd·8·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 57.9 | usb1k·1 |
| 6000.000 | -78.0 | 57.5 | fs8·1 |
| 12000.000 | -81.3 | 56.2 | fs8·2 |
| 18000.000 | -81.4 | 55.8 | fs8·3 |
| 2999.603 | -82.0 | 52.5 | usb1k·3 |
| 1999.735 | -82.2 | 51.7 | usb1k·2 |
| 6999.073 | -87.1 | 49.7 | usb1k·7 |
| 15997.879 | -91.4 | 45.8 | usb1k·16 |
| 9998.675 | -91.4 | 45.4 | usb1k·10 |
| 5999.205 | -94.2 | 41.3 | usb1k·6 |
| 14998.012 | -94.7 | 42.4 | usb1k·15 |
| 10998.542 | -93.7 | 43.5 | usb1k·11 |
| 13998.940 | -94.5 | 43.1 | imd·8·f1+1·f2 |
| 9999.470 | -95.3 | 41.6 | imd·4·f1+1·f2 |
| 15999.470 | -95.3 | 42.0 | imd·4·f1+2·f2 |
| 12999.868 | -96.6 | 40.6 | imd·1·f1+2·f2 |
| 12999.072 | -95.9 | 41.3 | imd·7·f1+1·f2 |
| 19998.940 | -95.9 | 41.0 | imd·8·f1+2·f2 |
| 7998.940 | -95.8 | 40.4 | usb1k·8 |
| 14999.603 | -96.9 | 40.2 | imd·3·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 60.8 | usb1k·1 |
| 6000.000 | -78.4 | 60.6 | fs8·1 |
| 12000.000 | -81.3 | 58.8 | fs8·2 |
| 18000.000 | -81.6 | 57.9 | fs8·3 |
| 2999.603 | -83.0 | 55.3 | usb1k·3 |
| 1999.735 | -83.5 | 54.4 | usb1k·2 |
| 6999.073 | -87.6 | 52.1 | usb1k·7 |
| 15997.879 | -92.0 | 47.7 | usb1k·16 |
| 9998.675 | -92.1 | 47.5 | usb1k·10 |
| 14998.012 | -94.9 | 44.6 | usb1k·15 |
| 13998.940 | -94.7 | 45.5 | imd·8·f1+1·f2 |
| 15999.470 | -95.5 | 44.3 | imd·4·f1+2·f2 |
| 10998.542 | -94.3 | 45.2 | usb1k·11 |
| 9999.470 | -95.6 | 44.0 | imd·4·f1+1·f2 |
| 5999.205 | -95.7 | 43.4 | usb1k·6 |
| 12999.073 | -96.1 | 44.3 | imd·7·f1+1·f2 |
| 12999.868 | -97.0 | 43.4 | imd·1·f1+2·f2 |
| 19998.940 | -96.1 | 43.4 | imd·8·f1+2·f2 |
| 7998.940 | -96.1 | 43.5 | usb1k·8 |
| 14999.602 | -97.2 | 42.4 | imd·3·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.2 | 59.0 | usb1k·1 |
| 6000.000 | -78.2 | 56.2 | fs8·1 |
| 1999.735 | -79.8 | 53.5 | usb1k·2 |
| 2999.603 | -81.1 | 52.9 | usb1k·3 |
| 12000.000 | -81.5 | 54.8 | fs8·2 |
| 18000.000 | -81.6 | 54.8 | fs8·3 |
| 6999.073 | -86.6 | 49.2 | usb1k·7 |
| 15997.879 | -90.5 | 45.5 | usb1k·16 |
| 4999.338 | -91.8 | 42.0 | usb1k·5 |
| 5999.205 | -91.7 | 42.7 | usb1k·6 |
| 9998.675 | -90.8 | 44.9 | usb1k·10 |
| 10998.542 | -93.3 | 42.6 | usb1k·11 |
| 14998.012 | -95.0 | 40.9 | usb1k·15 |
| 9999.470 | -95.3 | 40.3 | imd·4·f1+1·f2 |
| 13998.940 | -94.6 | 41.8 | imd·8·f1+1·f2 |
| 15999.470 | -95.5 | 40.6 | imd·4·f1+2·f2 |
| 20997.217 | -96.2 | 39.8 | usb1k·21 |
| 12999.868 | -96.5 | 39.7 | imd·1·f1+2·f2 |
| 19998.940 | -96.0 | 40.2 | imd·8·f1+2·f2 |
| 12999.073 | -96.2 | 40.1 | imd·7·f1+1·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.15 | 0.17 | 0.04 |
| led | Kanal 1 | 11/11 | 1.54 | 0.76 | 1.15 |
| mains50 | Kanal 1 | 11/11 | 265.97 | -121.39 | 2.08 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.17 | 0.22 | 0.04 |
| led | Kanal 2 | 11/11 | 0.41 | 0.24 | 0.40 |
| mains50 | Kanal 2 | 11/11 | 272.94 | -276.66 | 1.40 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.09 | 0.11 | 0.04 |
| led | Kanal 3 | 11/11 | 1.28 | 0.22 | 0.78 |
| mains50 | Kanal 3 | 11/11 | 243.33 | 0.50 | 1.00 |
| fs8 | Kanal 4 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.13 | 0.27 | 0.07 |
| led | Kanal 4 | 11/11 | 1.59 | 2.59 | 0.66 |
| mains50 | Kanal 4 | 11/11 | 287.23 | -349.48 | 1.28 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.49 | 0.31 s (3.18 Hz) | 28.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 28.4 |
| Kanal 2 | breitbandig | 1.26 | 0.31 s (3.18 Hz) | 29.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 30.0 |
| Kanal 3 | breitbandig | 1.15 | 0.31 s (3.18 Hz) | 30.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 33.8 |
| Kanal 4 | breitbandig | 0.81 | 0.31 s (3.18 Hz) | 27.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 1.25 s (0.80 Hz) | 29.7 |

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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.93 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.96 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4z-3d-end-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -70.9 | -71.0 | +0.1 | 67 % | 67 % |
| Kanal 2 | -71.7 | -71.8 | +0.1 | 72 % | 73 % |
| Kanal 3 | -73.1 | -73.1 | -0.0 | 81 % | 82 % |
| Kanal 4 | -70.8 | -70.9 | +0.1 | 74 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B5-3d-end-r1_psd.png)

### Kammprofile

![Kammprofile](B5-3d-end-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B5-3d-end-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 22:03:57. Stream-Meldungen: 0. owl_read: out/owl_read/B5-3d-end-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
