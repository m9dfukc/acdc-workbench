# Report B4z-3d-r2: B4z-3d-r2 – acdc1 3d-open-inputs-4z, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4z-Sitzung: Startkontrolle 3d vor fx3k/fx3kp, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-open-inputs-4z-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4z-3d-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -70.8 | -82.5 | -71.1 | -72.3 | -86.3 | -71.5 | – | -71.1 | 67 % | -75.9 | 4.8 |
| Kanal 2 | -7.1 | -71.4 | -84.0 | -71.7 | -72.9 | -88.1 | -72.0 | – | -71.7 | 73 % | -77.4 | 5.7 |
| Kanal 3 | -5.1 | -72.6 | -86.4 | -72.8 | -74.1 | -92.5 | -73.1 | – | -72.8 | 82 % | -80.4 | 7.6 |
| Kanal 4 | -6.4 | -70.8 | -84.1 | -71.0 | -72.0 | -88.2 | -71.3 | – | -71.0 | 74 % | -76.8 | 5.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0001 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -77.9 dB | -78.0 | 20.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -75.0 | 41.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0009 | 10/10 | k=2: 4641.090 Hz, -112.8 dB | -108.1 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0158 | 0.0000 | 2/19 | k=1: 50.016 Hz, -98.0 dB | -100.7 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0009 | 148 | k=8·f1+1·f2: 13998.941 Hz, -94.1 dB | -84.3 | 4.8 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.4 | 26.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0006 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.6 | 40.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0010 | 10/10 | k=1: 2320.543 Hz, -112.7 dB | -107.0 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0156 | 0.0001 | 2/19 | k=1: 50.015 Hz, -97.9 dB | -100.5 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0007 | 159 | k=8·f1+1·f2: 13998.941 Hz, -93.4 dB | -83.7 | 6.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.6 dB | -77.6 | 33.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0007 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -76.6 | 41.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.545 Hz, -113.0 dB | -108.4 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0149 | 0.0004 | 3/19 | k=1: 50.015 Hz, -98.6 dB | -101.2 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0006 | 162 | k=8·f1+1·f2: 13998.941 Hz, -93.9 dB | -84.0 | 7.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.7 dB | -77.6 | 21.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -72.9 dB | -74.3 | 46.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0008 | 10/10 | k=2: 4641.089 Hz, -112.2 dB | -107.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0156 | 0.0002 | 2/19 | k=1: 50.015 Hz, -98.0 dB | -100.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0008 | 155 | k=8·f1+1·f2: 13998.941 Hz, -93.4 dB | -83.9 | 5.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 57.2 | usb1k·1 |
| 6000.000 | -77.9 | 56.8 | fs8·1 |
| 18000.000 | -80.8 | 54.8 | fs8·3 |
| 12000.000 | -81.4 | 54.8 | fs8·2 |
| 2999.603 | -81.8 | 51.5 | usb1k·3 |
| 1999.735 | -82.6 | 50.1 | usb1k·2 |
| 6999.074 | -86.6 | 48.2 | usb1k·7 |
| 15997.882 | -91.0 | 45.1 | usb1k·16 |
| 9998.676 | -91.1 | 44.3 | usb1k·10 |
| 14998.014 | -94.1 | 40.7 | usb1k·15 |
| 10998.543 | -93.3 | 42.6 | usb1k·11 |
| 15999.471 | -94.7 | 41.4 | imd·4·f1+2·f2 |
| 9999.471 | -95.2 | 40.2 | imd·4·f1+1·f2 |
| 13998.941 | -94.1 | 42.4 | imd·8·f1+1·f2 |
| 12999.868 | -96.1 | 39.8 | imd·1·f1+2·f2 |
| 19998.941 | -95.0 | 41.3 | imd·8·f1+2·f2 |
| 5999.206 | -95.6 | 39.1 | usb1k·6 |
| 18999.868 | -96.7 | 39.5 | imd·1·f1+3·f2 |
| 7998.941 | -95.3 | 39.7 | usb1k·8 |
| 20997.220 | -96.6 | 39.3 | usb1k·21 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 58.4 | usb1k·1 |
| 6000.000 | -77.3 | 58.8 | fs8·1 |
| 18000.000 | -80.4 | 56.4 | fs8·3 |
| 12000.000 | -80.5 | 56.9 | fs8·2 |
| 2999.603 | -81.9 | 52.9 | usb1k·3 |
| 1999.735 | -83.8 | 50.3 | usb1k·2 |
| 6999.074 | -86.2 | 50.1 | usb1k·7 |
| 15997.882 | -91.0 | 46.5 | usb1k·16 |
| 9998.676 | -91.1 | 45.6 | usb1k·10 |
| 14998.014 | -93.6 | 43.3 | usb1k·15 |
| 10998.544 | -93.0 | 44.5 | usb1k·11 |
| 15999.471 | -94.2 | 43.3 | imd·4·f1+2·f2 |
| 9999.471 | -94.5 | 42.3 | imd·4·f1+1·f2 |
| 13998.941 | -93.4 | 44.6 | imd·8·f1+1·f2 |
| 12999.868 | -95.6 | 41.6 | imd·1·f1+2·f2 |
| 7998.941 | -94.4 | 42.4 | usb1k·8 |
| 19998.941 | -94.6 | 43.4 | imd·8·f1+2·f2 |
| 11998.411 | -95.4 | 41.9 | usb1k·12 |
| 8999.603 | -96.2 | 38.6 | imd·3·f1+1·f2 |
| 18999.868 | -96.4 | 41.0 | imd·1·f1+3·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 61.0 | usb1k·1 |
| 6000.000 | -77.6 | 61.6 | fs8·1 |
| 12000.000 | -80.7 | 58.9 | fs8·2 |
| 18000.000 | -80.7 | 58.6 | fs8·3 |
| 2999.603 | -82.7 | 55.4 | usb1k·3 |
| 1999.735 | -85.7 | 52.2 | usb1k·2 |
| 6999.074 | -86.9 | 52.2 | usb1k·7 |
| 15997.882 | -91.8 | 47.9 | usb1k·16 |
| 9998.676 | -91.5 | 47.8 | usb1k·10 |
| 14998.014 | -93.7 | 45.4 | usb1k·15 |
| 10998.544 | -93.6 | 46.1 | usb1k·11 |
| 15999.471 | -94.5 | 45.1 | imd·4·f1+2·f2 |
| 9999.471 | -94.7 | 44.5 | imd·4·f1+1·f2 |
| 13998.941 | -93.9 | 46.2 | imd·8·f1+1·f2 |
| 12999.868 | -95.7 | 43.7 | imd·1·f1+2·f2 |
| 7998.941 | -94.6 | 44.9 | usb1k·8 |
| 19998.941 | -94.8 | 44.7 | imd·8·f1+2·f2 |
| 11998.411 | -95.8 | 43.6 | usb1k·12 |
| 12999.074 | -95.6 | 43.8 | imd·7·f1+1·f2 |
| 8999.603 | -96.6 | 42.1 | imd·3·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.9 | 59.5 | usb1k·1 |
| 6000.000 | -77.7 | 58.0 | fs8·1 |
| 12000.000 | -80.5 | 56.1 | fs8·2 |
| 18000.000 | -80.6 | 55.3 | fs8·3 |
| 1999.735 | -81.1 | 52.7 | usb1k·2 |
| 2999.603 | -81.1 | 53.1 | usb1k·3 |
| 6999.074 | -85.4 | 49.9 | usb1k·7 |
| 15997.882 | -90.0 | 46.4 | usb1k·16 |
| 9998.676 | -90.8 | 45.2 | usb1k·10 |
| 10998.543 | -92.4 | 44.0 | usb1k·11 |
| 14998.014 | -94.0 | 41.8 | usb1k·15 |
| 15999.471 | -94.2 | 42.4 | imd·4·f1+2·f2 |
| 9999.471 | -94.6 | 41.4 | imd·4·f1+1·f2 |
| 13998.941 | -93.4 | 43.0 | imd·8·f1+1·f2 |
| 5999.206 | -94.4 | 41.3 | usb1k·6 |
| 11998.411 | -95.0 | 41.5 | usb1k·12 |
| 4999.338 | -95.3 | 39.2 | usb1k·5 |
| 12999.868 | -96.2 | 40.3 | imd·1·f1+2·f2 |
| 20997.220 | -96.0 | 40.1 | usb1k·21 |
| 19998.941 | -94.9 | 41.9 | imd·8·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.00 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.13 | -0.14 | 0.05 |
| led | Kanal 1 | 11/11 | 0.77 | 1.78 | 0.44 |
| mains50 | Kanal 1 | 11/11 | 746.37 | 1343.34 | 1.15 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.10 | -0.15 | 0.05 |
| led | Kanal 2 | 11/11 | 0.42 | 0.86 | 0.33 |
| mains50 | Kanal 2 | 11/11 | 276.38 | 249.31 | 0.96 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.08 | -0.09 | 0.03 |
| led | Kanal 3 | 11/11 | 0.80 | -0.78 | 0.25 |
| mains50 | Kanal 3 | 11/11 | 339.32 | 710.58 | 0.45 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.10 | -0.21 | 0.04 |
| led | Kanal 4 | 11/11 | 1.25 | -0.54 | 0.35 |
| mains50 | Kanal 4 | 11/11 | 750.38 | 1219.26 | 1.00 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.50 | 1.25 s (0.80 Hz) | 20.5 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 31.8 |
| Kanal 2 | breitbandig | 0.43 | 1.25 s (0.80 Hz) | 21.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 34.1 |
| Kanal 3 | breitbandig | 0.32 | 1.25 s (0.80 Hz) | 26.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 1.25 s (0.80 Hz) | 37.1 |
| Kanal 4 | breitbandig | 0.39 | 1.25 s (0.80 Hz) | 23.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 34.3 |

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
| Kanal 1 | 1.00 | 0.96 | 0.92 | 0.94 |
| Kanal 2 | 0.96 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.92 | 0.94 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.1 | -0.0 | 67 % | 68 % |
| Kanal 2 | -71.7 | -71.9 | +0.2 | 73 % | 73 % |
| Kanal 3 | -72.8 | -73.1 | +0.3 | 82 % | 82 % |
| Kanal 4 | -71.0 | -71.0 | -0.0 | 74 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4z-3d-r2_psd.png)

### Kammprofile

![Kammprofile](B4z-3d-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4z-3d-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 19:05:00. Stream-Meldungen: 0. owl_read: out/owl_read/B4z-3d-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
