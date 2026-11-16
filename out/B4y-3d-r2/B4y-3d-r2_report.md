# Report B4y-3d-r2: B4y-3d-r2 – acdc1 3d-open-inputs-4y, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4y-Sitzung: Startkontrolle 3d vor fx3j/fx3jp, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-open-inputs-4y-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-3d-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -70.7 | -81.4 | -71.1 | -72.1 | -86.6 | -71.5 | – | -71.1 | 68 % | -76.1 | 5.0 |
| Kanal 2 | -7.1 | -71.5 | -82.7 | -71.8 | -72.9 | -88.6 | -72.2 | – | -71.8 | 73 % | -77.6 | 5.8 |
| Kanal 3 | -5.4 | -73.0 | -88.6 | -73.1 | -74.2 | -92.6 | -73.4 | – | -73.1 | 82 % | -80.6 | 7.5 |
| Kanal 4 | -6.2 | -70.7 | -83.1 | -70.9 | -71.8 | -89.0 | -71.2 | – | -70.9 | 75 % | -77.0 | 6.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -78.3 | 19.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.6 | 44.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0010 | 10/10 | k=3: 6961.634 Hz, -116.5 dB | -112.3 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9996 | 0.0062 | 3/19 | k=1: 49.995 Hz, -95.5 dB | -97.4 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0009 | 150 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.7 | 4.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -78.2 | 23.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -75.3 | 44.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5449 | 0.0011 | 10/10 | k=8: 18564.358 Hz, -115.5 dB | -110.1 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9938 | 0.0017 | 3/19 | k=1: 49.995 Hz, -96.6 dB | -98.7 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0008 | 155 | k=8·f1+1·f2: 13998.941 Hz, -94.5 dB | -84.5 | 5.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.4 | 29.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.5 | 46.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0008 | 10/10 | k=3: 6961.634 Hz, -116.8 dB | -112.5 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9938 | 0.0014 | 3/19 | k=1: 49.995 Hz, -97.2 dB | -99.4 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0007 | 162 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 6.8 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.3 dB | -78.4 | 18.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -73.7 | 52.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0012 | 10/10 | k=2: 4641.088 Hz, -116.2 dB | -111.3 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9938 | 0.0015 | 3/19 | k=1: 49.995 Hz, -97.4 dB | -99.4 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0009 | 153 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.7 | 4.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 58.2 | usb1k·1 |
| 6000.000 | -78.1 | 56.7 | fs8·1 |
| 1999.735 | -81.1 | 51.9 | usb1k·2 |
| 18000.000 | -81.3 | 54.9 | fs8·3 |
| 12000.000 | -81.6 | 54.7 | fs8·2 |
| 2999.603 | -81.5 | 51.6 | usb1k·3 |
| 6999.074 | -86.7 | 48.3 | usb1k·7 |
| 15997.882 | -91.1 | 45.4 | usb1k·16 |
| 9998.676 | -91.3 | 44.3 | usb1k·10 |
| 5999.206 | -93.4 | 41.5 | usb1k·6 |
| 10998.544 | -93.8 | 42.2 | usb1k·11 |
| 14998.014 | -94.9 | 41.5 | usb1k·15 |
| 4999.339 | -94.4 | 40.2 | usb1k·5 |
| 15999.471 | -95.1 | 41.3 | imd·4·f1+2·f2 |
| 9999.471 | -95.5 | 40.1 | imd·4·f1+1·f2 |
| 49.995 | -95.5 | 27.0 | mains50·1 |
| 13998.941 | -94.7 | 41.6 | imd·8·f1+1·f2 |
| 12999.868 | -96.6 | 39.5 | imd·1·f1+2·f2 |
| 19998.941 | -95.5 | 40.8 | imd·8·f1+2·f2 |
| 20997.220 | -96.8 | 38.7 | usb1k·21 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 58.9 | usb1k·1 |
| 6000.000 | -78.1 | 58.4 | fs8·1 |
| 18000.000 | -81.1 | 56.2 | fs8·3 |
| 12000.000 | -81.4 | 56.3 | fs8·2 |
| 2999.603 | -82.0 | 52.7 | usb1k·3 |
| 1999.735 | -82.2 | 52.5 | usb1k·2 |
| 6999.074 | -86.9 | 49.7 | usb1k·7 |
| 15997.882 | -91.5 | 46.1 | usb1k·16 |
| 9998.676 | -91.5 | 45.8 | usb1k·10 |
| 14998.014 | -94.6 | 43.0 | usb1k·15 |
| 10998.544 | -93.9 | 43.5 | usb1k·11 |
| 5999.206 | -94.3 | 42.2 | usb1k·6 |
| 15999.471 | -95.0 | 42.6 | imd·4·f1+2·f2 |
| 9999.471 | -95.3 | 42.0 | imd·4·f1+1·f2 |
| 13998.941 | -94.5 | 43.1 | imd·8·f1+1·f2 |
| 12999.868 | -96.4 | 41.6 | imd·1·f1+2·f2 |
| 19998.941 | -95.4 | 42.3 | imd·8·f1+2·f2 |
| 49.995 | -96.6 | 27.9 | mains50·1 |
| 14999.603 | -96.8 | 40.8 | imd·3·f1+2·f2 |
| 16998.544 | -96.2 | 42.1 | imd·11·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 62.3 | usb1k·1 |
| 6000.000 | -78.5 | 61.0 | fs8·1 |
| 12000.000 | -81.4 | 58.7 | fs8·2 |
| 18000.000 | -81.4 | 58.4 | fs8·3 |
| 2999.603 | -82.9 | 55.9 | usb1k·3 |
| 1999.735 | -83.6 | 54.7 | usb1k·2 |
| 6999.074 | -87.4 | 52.3 | usb1k·7 |
| 15997.882 | -92.0 | 48.1 | usb1k·16 |
| 9998.676 | -91.9 | 48.3 | usb1k·10 |
| 14998.014 | -94.8 | 45.4 | usb1k·15 |
| 10998.544 | -94.3 | 45.7 | usb1k·11 |
| 15999.471 | -95.2 | 45.0 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 44.6 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 45.4 | imd·8·f1+1·f2 |
| 5999.206 | -95.6 | 43.9 | usb1k·6 |
| 12999.868 | -96.8 | 43.2 | imd·1·f1+2·f2 |
| 19998.941 | -95.6 | 44.3 | imd·8·f1+2·f2 |
| 14999.603 | -97.1 | 43.3 | imd·3·f1+2·f2 |
| 16998.544 | -96.5 | 43.4 | imd·11·f1+1·f2 |
| 12999.074 | -96.2 | 43.7 | imd·7·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 60.6 | usb1k·1 |
| 6000.000 | -78.3 | 57.2 | fs8·1 |
| 1999.735 | -79.7 | 54.4 | usb1k·2 |
| 2999.603 | -81.1 | 53.4 | usb1k·3 |
| 18000.000 | -81.4 | 54.9 | fs8·3 |
| 12000.000 | -81.5 | 55.0 | fs8·2 |
| 6999.074 | -86.4 | 49.4 | usb1k·7 |
| 15997.882 | -90.6 | 45.9 | usb1k·16 |
| 9998.676 | -90.9 | 45.3 | usb1k·10 |
| 4999.338 | -91.6 | 43.9 | usb1k·5 |
| 5999.206 | -91.8 | 43.6 | usb1k·6 |
| 10998.544 | -93.4 | 42.9 | usb1k·11 |
| 14998.014 | -94.8 | 41.6 | usb1k·15 |
| 15999.471 | -95.2 | 41.3 | imd·4·f1+2·f2 |
| 9999.471 | -95.4 | 40.7 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 41.7 | imd·8·f1+1·f2 |
| 12999.868 | -96.3 | 40.2 | imd·1·f1+2·f2 |
| 20997.220 | -96.1 | 40.1 | usb1k·21 |
| 11998.411 | -96.1 | 40.4 | usb1k·12 |
| 19998.941 | -95.6 | 41.0 | imd·8·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.01 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.11 | 0.04 | 0.02 |
| led | Kanal 1 | 11/11 | 1.76 | 1.47 | 0.81 |
| mains50 | Kanal 1 | 11/11 | 69.37 | -49.48 | 1.35 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.12 | 0.03 | 0.02 |
| led | Kanal 2 | 11/11 | 0.53 | 0.84 | 0.40 |
| mains50 | Kanal 2 | 11/11 | 206.48 | 206.36 | 0.97 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.10 | 0.05 | 0.01 |
| led | Kanal 3 | 11/11 | 1.00 | 0.79 | 0.70 |
| mains50 | Kanal 3 | 11/11 | 32.74 | -0.82 | 0.86 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.00 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.11 | -0.00 | 0.02 |
| led | Kanal 4 | 11/11 | 1.68 | 2.45 | 0.99 |
| mains50 | Kanal 4 | 11/11 | 202.29 | -25.40 | 0.89 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.57 | 1.25 s (0.80 Hz) | 22.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 28.5 |
| Kanal 2 | breitbandig | 0.50 | 1.25 s (0.80 Hz) | 23.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 30.5 |
| Kanal 3 | breitbandig | 0.31 | 1.25 s (0.80 Hz) | 28.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.88 | 1.25 s (0.80 Hz) | 34.5 |
| Kanal 4 | breitbandig | 0.42 | 1.25 s (0.80 Hz) | 25.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.88 | 1.25 s (0.80 Hz) | 31.1 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.94 | 0.96 | 0.93 | 1.00 |

## Vergleich mit Referenz B4-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.7 | +0.6 | 68 % | 64 % |
| Kanal 2 | -71.8 | -72.6 | +0.7 | 73 % | 69 % |
| Kanal 3 | -73.1 | -73.8 | +0.7 | 82 % | 80 % |
| Kanal 4 | -70.9 | -71.6 | +0.7 | 75 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-3d-r2_psd.png)

### Kammprofile

![Kammprofile](B4y-3d-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-3d-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:12:36. Stream-Meldungen: 0. owl_read: out/owl_read/B4y-3d-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
