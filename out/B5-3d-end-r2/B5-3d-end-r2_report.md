# Report B5-3d-end-r2: B5-3d-end-r2 – acdc1 3d-end-open-inputs-5, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-5-Sitzung: Endkontrolle 3d nach fx3l/fx3lp, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-5-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B5-3d-end-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-end-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -70.3 | -78.5 | -71.0 | -72.0 | -85.5 | -71.3 | -97.2 | -71.0 | 67 % | -75.8 | 4.8 |
| Kanal 2 | -7.2 | -71.1 | -80.1 | -71.7 | -72.8 | -87.6 | -72.1 | – | -71.7 | 72 % | -77.2 | 5.5 |
| Kanal 3 | -5.4 | -72.7 | -83.4 | -73.1 | -74.2 | -91.8 | -73.4 | – | -73.1 | 82 % | -80.4 | 7.3 |
| Kanal 4 | -6.2 | -70.4 | -80.9 | -70.8 | -71.7 | -87.9 | -71.1 | – | -70.8 | 73 % | -76.6 | 5.7 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.2 | 18.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.5 | 44.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0012 | 10/10 | k=1: 2320.546 Hz, -115.2 dB | -111.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9638 | 0.0000 | 1/19 | k=1: 49.964 Hz, -99.0 dB | -101.3 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0012 | 151 | k=8·f1+1·f2: 13998.940 Hz, -94.6 dB | -84.8 | 4.2 % |
| stärkste übrige Linie (10.27 Hz) | Kanal 1 | 10.2740 | 0.0021 | 15/2324 | k=1: 10.271 Hz, -97.6 dB | -97.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.1 | 22.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.9 dB | -75.3 | 43.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0013 | 10/10 | k=9: 20884.903 Hz, -115.0 dB | -109.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9636 | 0.0000 | 1/19 | k=1: 49.964 Hz, -99.8 dB | -102.0 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0010 | 156 | k=8·f1+1·f2: 13998.940 Hz, -94.4 dB | -84.6 | 5.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.4 dB | -78.4 | 29.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.5 | 45.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5449 | 0.0007 | 10/10 | k=1: 2320.545 Hz, -116.7 dB | -112.5 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9622 | 0.0025 | 2/19 | k=1: 49.963 Hz, -100.4 dB | -102.5 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0011 | 163 | k=8·f1+1·f2: 13998.940 Hz, -94.6 dB | -84.9 | 6.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.3 | 17.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -73.7 | 51.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0011 | 10/10 | k=1: 2320.545 Hz, -115.1 dB | -111.2 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9633 | 0.0000 | 1/19 | k=1: 49.963 Hz, -100.3 dB | -102.6 | 0.1 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0016 | 152 | k=8·f1+1·f2: 13998.940 Hz, -94.5 dB | -84.8 | 4.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 57.7 | usb1k·1 |
| 6000.000 | -78.0 | 56.2 | fs8·1 |
| 1999.735 | -81.2 | 51.0 | usb1k·2 |
| 18000.000 | -81.4 | 55.1 | fs8·3 |
| 2999.603 | -81.3 | 52.2 | usb1k·3 |
| 12000.000 | -81.5 | 54.5 | fs8·2 |
| 6999.073 | -86.9 | 47.4 | usb1k·7 |
| 15997.880 | -91.3 | 44.9 | usb1k·16 |
| 9998.675 | -91.3 | 43.9 | usb1k·10 |
| 5999.205 | -93.6 | 40.6 | usb1k·6 |
| 14998.012 | -94.8 | 40.7 | usb1k·15 |
| 10998.542 | -93.8 | 41.5 | usb1k·11 |
| 4999.338 | -95.1 | 39.1 | usb1k·5 |
| 15999.470 | -95.2 | 40.9 | imd·4·f1+2·f2 |
| 13998.940 | -94.6 | 41.2 | imd·8·f1+1·f2 |
| 9999.470 | -95.4 | 39.7 | imd·4·f1+1·f2 |
| 7998.940 | -95.4 | 39.6 | usb1k·8 |
| 12999.868 | -96.5 | 39.3 | imd·1·f1+2·f2 |
| 12999.073 | -96.0 | 39.8 | imd·7·f1+1·f2 |
| 19998.941 | -95.8 | 40.5 | imd·8·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.9 | 58.1 | usb1k·1 |
| 6000.000 | -78.0 | 57.4 | fs8·1 |
| 18000.000 | -81.3 | 56.2 | fs8·3 |
| 12000.000 | -81.3 | 55.9 | fs8·2 |
| 2999.603 | -81.9 | 52.9 | usb1k·3 |
| 1999.735 | -82.2 | 51.7 | usb1k·2 |
| 6999.073 | -87.2 | 49.1 | usb1k·7 |
| 15997.880 | -91.6 | 45.6 | usb1k·16 |
| 9998.675 | -91.6 | 45.0 | usb1k·10 |
| 14998.012 | -94.5 | 42.7 | usb1k·15 |
| 5999.205 | -94.6 | 40.7 | usb1k·6 |
| 10998.542 | -94.0 | 42.9 | usb1k·11 |
| 15999.470 | -95.1 | 42.2 | imd·4·f1+2·f2 |
| 13998.940 | -94.4 | 43.1 | imd·8·f1+1·f2 |
| 9999.470 | -95.3 | 41.3 | imd·4·f1+1·f2 |
| 12999.868 | -96.2 | 40.9 | imd·1·f1+2·f2 |
| 7998.940 | -95.5 | 40.9 | usb1k·8 |
| 12999.073 | -95.9 | 41.3 | imd·7·f1+1·f2 |
| 19998.940 | -95.6 | 42.1 | imd·8·f1+2·f2 |
| 8999.603 | -97.0 | 40.2 | imd·3·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 61.5 | usb1k·1 |
| 6000.000 | -78.4 | 60.6 | fs8·1 |
| 12000.000 | -81.3 | 58.9 | fs8·2 |
| 18000.000 | -81.5 | 58.3 | fs8·3 |
| 2999.603 | -82.8 | 55.9 | usb1k·3 |
| 1999.735 | -83.5 | 54.4 | usb1k·2 |
| 6999.073 | -87.8 | 51.4 | usb1k·7 |
| 15997.880 | -92.2 | 47.5 | usb1k·16 |
| 9998.675 | -92.1 | 48.2 | usb1k·10 |
| 14998.012 | -94.8 | 44.9 | usb1k·15 |
| 15999.470 | -95.4 | 44.3 | imd·4·f1+2·f2 |
| 13998.940 | -94.6 | 44.9 | imd·8·f1+1·f2 |
| 9999.470 | -95.5 | 44.8 | imd·4·f1+1·f2 |
| 10998.543 | -94.5 | 45.1 | usb1k·11 |
| 5999.205 | -95.9 | 43.1 | usb1k·6 |
| 12999.868 | -96.7 | 43.4 | imd·1·f1+2·f2 |
| 12999.073 | -96.0 | 44.0 | imd·7·f1+1·f2 |
| 7998.940 | -95.9 | 43.3 | usb1k·8 |
| 19998.940 | -95.9 | 43.8 | imd·8·f1+2·f2 |
| 8999.603 | -97.2 | 42.9 | imd·3·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 59.4 | usb1k·1 |
| 6000.000 | -78.2 | 56.6 | fs8·1 |
| 1999.735 | -79.7 | 53.5 | usb1k·2 |
| 2999.603 | -81.0 | 53.1 | usb1k·3 |
| 12000.000 | -81.4 | 54.7 | fs8·2 |
| 18000.000 | -81.5 | 55.3 | fs8·3 |
| 6999.073 | -86.7 | 48.7 | usb1k·7 |
| 15997.880 | -90.6 | 45.7 | usb1k·16 |
| 9998.675 | -91.0 | 44.7 | usb1k·10 |
| 4999.338 | -92.2 | 42.5 | usb1k·5 |
| 5999.205 | -92.2 | 42.6 | usb1k·6 |
| 10998.543 | -93.4 | 42.3 | usb1k·11 |
| 14998.012 | -94.8 | 41.3 | usb1k·15 |
| 15999.470 | -95.3 | 41.0 | imd·4·f1+2·f2 |
| 13998.940 | -94.5 | 41.6 | imd·8·f1+1·f2 |
| 9999.471 | -95.4 | 40.2 | imd·4·f1+1·f2 |
| 12999.868 | -96.2 | 39.9 | imd·1·f1+2·f2 |
| 20997.218 | -96.4 | 40.3 | usb1k·21 |
| 7998.940 | -95.5 | 40.2 | usb1k·8 |
| 8998.808 | -95.7 | 40.8 | usb1k·9 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.00 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.13 | 0.12 | 0.04 |
| led | Kanal 1 | 11/11 | 1.29 | -0.42 | 0.76 |
| mains50 | Kanal 1 | 11/11 | 279.81 | 575.75 | 1.18 |
| other1 | Kanal 1 | 11/11 | 299.96 | 334.22 | 1.55 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.13 | 0.10 | 0.05 |
| led | Kanal 2 | 11/11 | 0.69 | -0.04 | 0.37 |
| mains50 | Kanal 2 | 11/11 | 271.84 | 584.28 | 1.14 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.10 | 0.07 | 0.01 |
| led | Kanal 3 | 11/11 | 0.95 | -0.37 | 0.55 |
| mains50 | Kanal 3 | 11/11 | 693.77 | 1748.79 | 0.70 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.10 | 0.07 | 0.05 |
| led | Kanal 4 | 11/11 | 1.62 | 0.81 | 0.59 |
| mains50 | Kanal 4 | 11/11 | 278.44 | 532.24 | 1.21 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.80 | 0.31 s (3.18 Hz) | 21.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 30.8 |
| Kanal 2 | breitbandig | 0.71 | 0.31 s (3.18 Hz) | 22.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 31.6 |
| Kanal 3 | breitbandig | 0.49 | 1.25 s (0.80 Hz) | 27.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 35.6 |
| Kanal 4 | breitbandig | 0.56 | 1.25 s (0.80 Hz) | 23.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 31.4 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.96 |
| Kanal 3 | 0.94 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4z-3d-end-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.0 | -71.0 | +0.1 | 67 % | 67 % |
| Kanal 2 | -71.7 | -71.8 | +0.1 | 72 % | 73 % |
| Kanal 3 | -73.1 | -73.1 | +0.0 | 82 % | 82 % |
| Kanal 4 | -70.8 | -70.9 | +0.1 | 73 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B5-3d-end-r2_psd.png)

### Kammprofile

![Kammprofile](B5-3d-end-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B5-3d-end-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 22:05:10. Stream-Meldungen: 0. owl_read: out/owl_read/B5-3d-end-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
