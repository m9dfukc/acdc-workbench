# Report B4y-3d-end-r1: B4y-3d-end-r1 – acdc1 3d-end-open-inputs-4y, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d (zurückgeflasht) |
| test | Build-4y-Sitzung: 3d-Endkontrolle nach fx3j/noD, Eingänge offen |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-4y-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-3d-end-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -69.1 | -73.4 | -71.1 | -72.1 | -85.2 | -71.5 | – | -71.1 | 67 % | -75.8 | 4.8 |
| Kanal 2 | -7.1 | -70.2 | -75.4 | -71.8 | -72.9 | -87.1 | -72.2 | – | -71.8 | 72 % | -77.3 | 5.5 |
| Kanal 3 | -5.4 | -71.5 | -76.2 | -73.2 | -74.4 | -91.3 | -73.5 | – | -73.2 | 81 % | -80.5 | 7.3 |
| Kanal 4 | -6.2 | -70.0 | -77.3 | -70.9 | -71.8 | -87.4 | -71.2 | – | -70.9 | 74 % | -76.7 | 5.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.4 | 18.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.7 | 43.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0012 | 10/10 | k=2: 4641.088 Hz, -117.5 dB | -112.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0000 | 0.0032 | 2/19 | k=1: 49.996 Hz, -96.3 dB | -99.0 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0010 | 148 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.2 | 22.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -75.4 | 43.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0009 | 10/10 | k=9: 20884.904 Hz, -114.7 dB | -110.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9998 | 0.0077 | 3/19 | k=1: 49.996 Hz, -97.0 dB | -99.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0008 | 155 | k=8·f1+1·f2: 13998.941 Hz, -94.6 dB | -84.7 | 5.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.5 | 29.4 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -76.7 | 45.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0010 | 10/10 | k=2: 4641.088 Hz, -117.5 dB | -113.0 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9999 | 0.0067 | 3/19 | k=1: 49.996 Hz, -97.8 dB | -100.3 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0008 | 160 | k=8·f1+1·f2: 13998.941 Hz, -94.8 dB | -85.0 | 6.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.3 dB | -78.4 | 17.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -73.8 | 51.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0008 | 10/10 | k=2: 4641.089 Hz, -116.3 dB | -111.8 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9999 | 0.0079 | 3/19 | k=1: 49.996 Hz, -97.7 dB | -100.2 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0010 | 151 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.9 | 4.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 57.6 | usb1k·1 |
| 6000.000 | -78.2 | 56.3 | fs8·1 |
| 12000.000 | -81.6 | 54.0 | fs8·2 |
| 18000.000 | -81.6 | 54.5 | fs8·3 |
| 1999.735 | -81.5 | 50.7 | usb1k·2 |
| 2999.603 | -81.8 | 51.1 | usb1k·3 |
| 6999.073 | -86.7 | 48.3 | usb1k·7 |
| 15997.881 | -91.1 | 45.4 | usb1k·16 |
| 9998.676 | -91.2 | 43.9 | usb1k·10 |
| 5999.206 | -93.1 | 41.4 | usb1k·6 |
| 4999.338 | -93.9 | 40.4 | usb1k·5 |
| 10998.543 | -93.8 | 41.6 | usb1k·11 |
| 14998.013 | -94.9 | 41.0 | usb1k·15 |
| 15999.471 | -95.5 | 41.0 | imd·4·f1+2·f2 |
| 9999.470 | -95.5 | 39.5 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 41.5 | imd·8·f1+1·f2 |
| 49.996 | -96.3 | 25.6 | mains50·1 |
| 12999.868 | -96.9 | 39.5 | imd·1·f1+2·f2 |
| 20997.219 | -96.8 | 39.6 | usb1k·21 |
| 12999.073 | -96.2 | 40.2 | imd·7·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 58.3 | usb1k·1 |
| 6000.000 | -78.0 | 57.8 | fs8·1 |
| 12000.000 | -81.4 | 56.0 | fs8·2 |
| 18000.000 | -81.5 | 56.1 | fs8·3 |
| 2999.603 | -82.3 | 52.1 | usb1k·3 |
| 1999.735 | -82.4 | 51.4 | usb1k·2 |
| 6999.073 | -87.0 | 49.4 | usb1k·7 |
| 15997.881 | -91.5 | 46.2 | usb1k·16 |
| 9998.676 | -91.4 | 45.1 | usb1k·10 |
| 5999.206 | -93.8 | 42.1 | usb1k·6 |
| 14998.013 | -94.5 | 43.0 | usb1k·15 |
| 10998.543 | -93.9 | 42.9 | usb1k·11 |
| 9999.470 | -95.4 | 41.1 | imd·4·f1+1·f2 |
| 15999.470 | -95.4 | 42.3 | imd·4·f1+2·f2 |
| 13998.941 | -94.6 | 43.0 | imd·8·f1+1·f2 |
| 4999.338 | -95.8 | 39.7 | usb1k·5 |
| 12999.868 | -96.8 | 40.8 | imd·1·f1+2·f2 |
| 12999.073 | -96.0 | 41.6 | imd·7·f1+1·f2 |
| 19998.941 | -95.8 | 41.9 | imd·8·f1+2·f2 |
| 14999.603 | -97.0 | 40.5 | imd·3·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 61.5 | usb1k·1 |
| 6000.000 | -78.5 | 61.2 | fs8·1 |
| 12000.000 | -81.4 | 58.7 | fs8·2 |
| 18000.000 | -81.7 | 58.1 | fs8·3 |
| 2999.603 | -83.3 | 54.9 | usb1k·3 |
| 1999.735 | -84.1 | 53.9 | usb1k·2 |
| 6999.073 | -87.4 | 52.2 | usb1k·7 |
| 15997.881 | -92.1 | 47.4 | usb1k·16 |
| 9998.676 | -92.0 | 47.8 | usb1k·10 |
| 14998.013 | -94.9 | 45.2 | usb1k·15 |
| 10998.543 | -94.3 | 45.2 | usb1k·11 |
| 15999.471 | -95.5 | 44.0 | imd·4·f1+2·f2 |
| 9999.470 | -95.7 | 44.1 | imd·4·f1+1·f2 |
| 13998.941 | -94.8 | 45.5 | imd·8·f1+1·f2 |
| 5999.206 | -95.5 | 44.2 | usb1k·6 |
| 12999.867 | -96.9 | 43.4 | imd·1·f1+2·f2 |
| 12999.073 | -96.3 | 44.0 | imd·7·f1+1·f2 |
| 19998.941 | -96.1 | 44.0 | imd·8·f1+2·f2 |
| 14999.603 | -97.4 | 42.7 | imd·3·f1+2·f2 |
| 11998.410 | -96.7 | 43.4 | usb1k·12 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 59.7 | usb1k·1 |
| 6000.000 | -78.3 | 57.0 | fs8·1 |
| 1999.735 | -80.0 | 53.4 | usb1k·2 |
| 2999.603 | -81.3 | 52.8 | usb1k·3 |
| 12000.000 | -81.5 | 54.4 | fs8·2 |
| 18000.000 | -81.7 | 54.7 | fs8·3 |
| 6999.073 | -86.5 | 49.1 | usb1k·7 |
| 15997.881 | -90.5 | 46.3 | usb1k·16 |
| 4999.338 | -91.2 | 43.5 | usb1k·5 |
| 5999.206 | -91.4 | 43.9 | usb1k·6 |
| 9998.676 | -90.7 | 44.7 | usb1k·10 |
| 10998.543 | -93.4 | 42.3 | usb1k·11 |
| 14998.013 | -94.8 | 41.4 | usb1k·15 |
| 9999.470 | -95.5 | 39.9 | imd·4·f1+1·f2 |
| 15999.470 | -95.5 | 41.3 | imd·4·f1+2·f2 |
| 13998.941 | -94.7 | 41.6 | imd·8·f1+1·f2 |
| 20997.219 | -96.1 | 40.8 | usb1k·21 |
| 11998.410 | -96.0 | 39.9 | usb1k·12 |
| 12999.868 | -96.9 | 40.0 | imd·1·f1+2·f2 |
| 12999.073 | -96.2 | 40.7 | imd·7·f1+1·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.11 | 0.15 | 0.13 |
| led | Kanal 1 | 11/11 | 3.65 | -3.41 | 1.42 |
| mains50 | Kanal 1 | 11/11 | 202.34 | 244.24 | 1.40 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.11 | 0.18 | 0.13 |
| led | Kanal 2 | 11/11 | 0.33 | 0.40 | 0.45 |
| mains50 | Kanal 2 | 11/11 | 51.10 | -52.07 | 1.30 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.07 | 0.07 | 0.12 |
| led | Kanal 3 | 11/11 | 0.62 | 0.37 | 0.44 |
| mains50 | Kanal 3 | 11/11 | 31.99 | -53.40 | 0.71 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.10 | 0.16 | 0.17 |
| led | Kanal 4 | 11/11 | 1.68 | 1.68 | 0.75 |
| mains50 | Kanal 4 | 11/11 | 66.48 | -51.52 | 1.17 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.72 | 0.31 s (3.20 Hz) | 21.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 31.4 |
| Kanal 2 | breitbandig | 1.46 | 0.31 s (3.20 Hz) | 22.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 32.5 |
| Kanal 3 | breitbandig | 1.55 | 15.00 s (0.07 Hz) | 23.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 1.25 s (0.80 Hz) | 36.4 |
| Kanal 4 | breitbandig | 1.00 | 0.31 s (3.20 Hz) | 22.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 31.9 |

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
| Kanal 2 | 0.97 | 1.00 | 0.96 | 0.96 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.1 | +0.1 | 67 % | 68 % |
| Kanal 2 | -71.8 | -71.9 | +0.1 | 72 % | 73 % |
| Kanal 3 | -73.2 | -73.1 | -0.1 | 81 % | 82 % |
| Kanal 4 | -70.9 | -71.0 | +0.0 | 74 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-3d-end-r1_psd.png)

### Kammprofile

![Kammprofile](B4y-3d-end-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-3d-end-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:27:58. Stream-Meldungen: 0. owl_read: reports/owl_read/B4y-3d-end-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
