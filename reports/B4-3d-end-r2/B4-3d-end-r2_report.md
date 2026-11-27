# Report B4-3d-end-r2: B4-3d-end-r2 – acdc1 3d-end-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4-Sitzung (Q3): 3d-Endkontrolle nach fx3i (zurückgeflasht), Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4-3d-end-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -69.8 | -75.5 | -71.2 | -72.3 | -86.2 | -71.6 | – | -71.2 | 65 % | -75.8 | 4.6 |
| Kanal 2 | -7.1 | -70.6 | -76.5 | -71.9 | -73.0 | -88.0 | -72.3 | – | -71.9 | 71 % | -77.3 | 5.4 |
| Kanal 3 | -5.3 | -72.1 | -78.4 | -73.3 | -74.4 | -92.0 | -73.6 | – | -73.3 | 81 % | -80.5 | 7.2 |
| Kanal 4 | -6.2 | -70.2 | -77.5 | -71.1 | -71.9 | -88.2 | -71.4 | – | -71.1 | 73 % | -76.7 | 5.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.5 | 18.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.9 | 42.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0014 | 10/10 | k=3: 6961.633 Hz, -116.7 dB | -112.4 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0252 | 0.0001 | 2/19 | k=1: 50.025 Hz, -94.3 dB | -96.8 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0009 | 144 | k=8·f1+1·f2: 13998.941 Hz, -94.8 dB | -84.9 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.3 dB | -78.4 | 22.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.6 | 43.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0012 | 10/10 | k=8: 18564.357 Hz, -115.4 dB | -109.7 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0252 | 0.0002 | 2/19 | k=1: 50.025 Hz, -95.0 dB | -97.5 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0009 | 155 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 5.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -78.6 | 29.0 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.7 | 44.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5449 | 0.0011 | 10/10 | k=2: 4641.089 Hz, -117.8 dB | -112.7 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0250 | 0.0002 | 2/19 | k=1: 50.025 Hz, -95.7 dB | -98.4 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0010 | 162 | k=8·f1+1·f2: 13998.941 Hz, -94.8 dB | -85.0 | 6.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.5 | 17.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.6 dB | -74.0 | 50.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0016 | 10/10 | k=2: 4641.088 Hz, -116.5 dB | -111.3 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0254 | 0.0002 | 2/19 | k=1: 50.025 Hz, -95.5 dB | -98.0 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0010 | 150 | k=8·f1+1·f2: 13998.941 Hz, -94.9 dB | -84.9 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 57.1 | usb1k·1 |
| 6000.000 | -78.5 | 55.8 | fs8·1 |
| 18000.000 | -81.5 | 54.8 | fs8·3 |
| 1999.735 | -81.6 | 50.6 | usb1k·2 |
| 12000.000 | -81.7 | 53.9 | fs8·2 |
| 2999.603 | -82.0 | 51.0 | usb1k·3 |
| 6999.074 | -86.7 | 48.3 | usb1k·7 |
| 15997.882 | -91.0 | 45.2 | usb1k·16 |
| 9998.676 | -91.3 | 44.3 | usb1k·10 |
| 5999.206 | -93.4 | 40.8 | usb1k·6 |
| 10998.544 | -93.6 | 39.1 | usb1k·11 |
| 4999.338 | -94.1 | 39.9 | usb1k·5 |
| 14998.014 | -94.8 | 41.1 | usb1k·15 |
| 50.025 | -94.3 | 28.5 | mains50·1 |
| 15999.471 | -95.4 | 40.6 | imd·4·f1+2·f2 |
| 9999.471 | -95.7 | 39.9 | imd·4·f1+1·f2 |
| 13998.941 | -94.8 | 41.3 | imd·8·f1+1·f2 |
| 12999.868 | -96.7 | 39.3 | imd·1·f1+2·f2 |
| 20997.220 | -96.8 | 39.5 | usb1k·21 |
| 11998.411 | -96.5 | 39.1 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 57.9 | usb1k·1 |
| 6000.000 | -78.3 | 57.0 | fs8·1 |
| 18000.000 | -81.4 | 56.3 | fs8·3 |
| 12000.000 | -81.5 | 55.5 | fs8·2 |
| 1999.736 | -82.4 | 51.5 | usb1k·2 |
| 2999.603 | -82.5 | 51.7 | usb1k·3 |
| 6999.074 | -86.9 | 49.7 | usb1k·7 |
| 15997.882 | -91.3 | 46.3 | usb1k·16 |
| 9998.676 | -91.5 | 45.3 | usb1k·10 |
| 10998.544 | -93.6 | 41.1 | usb1k·11 |
| 14998.014 | -94.5 | 42.6 | usb1k·15 |
| 5999.206 | -94.1 | 41.2 | usb1k·6 |
| 15999.471 | -95.3 | 42.4 | imd·4·f1+2·f2 |
| 9999.471 | -95.5 | 41.3 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 42.9 | imd·8·f1+1·f2 |
| 50.025 | -95.0 | 29.6 | mains50·1 |
| 4999.338 | -95.9 | 39.3 | usb1k·5 |
| 12999.868 | -96.7 | 40.8 | imd·1·f1+2·f2 |
| 11998.411 | -96.4 | 40.5 | usb1k·12 |
| 14999.603 | -97.0 | 40.2 | imd·3·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 61.3 | usb1k·1 |
| 6000.000 | -78.7 | 60.3 | fs8·1 |
| 12000.000 | -81.5 | 58.3 | fs8·2 |
| 18000.000 | -81.5 | 57.9 | fs8·3 |
| 2999.603 | -83.3 | 55.1 | usb1k·3 |
| 1999.735 | -84.3 | 53.2 | usb1k·2 |
| 6999.074 | -87.3 | 52.2 | usb1k·7 |
| 15997.882 | -91.9 | 48.2 | usb1k·16 |
| 9998.676 | -92.0 | 47.9 | usb1k·10 |
| 10998.544 | -94.0 | 44.3 | usb1k·11 |
| 14998.014 | -94.9 | 44.7 | usb1k·15 |
| 15999.471 | -95.5 | 44.6 | imd·4·f1+2·f2 |
| 9999.471 | -95.9 | 44.0 | imd·4·f1+1·f2 |
| 13998.941 | -94.8 | 44.6 | imd·8·f1+1·f2 |
| 5999.206 | -95.7 | 43.4 | usb1k·6 |
| 12999.868 | -96.8 | 43.6 | imd·1·f1+2·f2 |
| 50.025 | -95.7 | 33.5 | mains50·1 |
| 11998.411 | -96.8 | 43.1 | usb1k·12 |
| 19998.941 | -96.2 | 43.5 | imd·8·f1+2·f2 |
| 12999.074 | -96.6 | 43.8 | imd·7·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.6 | 59.1 | usb1k·1 |
| 6000.000 | -78.5 | 56.1 | fs8·1 |
| 1999.736 | -80.0 | 53.4 | usb1k·2 |
| 18000.000 | -81.6 | 54.6 | fs8·3 |
| 12000.000 | -81.6 | 54.6 | fs8·2 |
| 2999.603 | -81.5 | 52.4 | usb1k·3 |
| 6999.074 | -86.5 | 49.0 | usb1k·7 |
| 15997.882 | -90.4 | 45.8 | usb1k·16 |
| 4999.338 | -91.5 | 43.1 | usb1k·5 |
| 9998.676 | -90.9 | 44.9 | usb1k·10 |
| 5999.206 | -91.6 | 43.0 | usb1k·6 |
| 10998.544 | -93.2 | 41.0 | usb1k·11 |
| 14998.015 | -94.6 | 41.4 | usb1k·15 |
| 15999.471 | -95.6 | 40.8 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 40.2 | imd·4·f1+1·f2 |
| 20997.220 | -96.0 | 40.4 | usb1k·21 |
| 13998.941 | -94.9 | 41.5 | imd·8·f1+1·f2 |
| 11998.411 | -96.0 | 40.2 | usb1k·12 |
| 13998.147 | -96.5 | 39.9 | usb1k·14 |
| 12999.868 | -96.8 | 39.7 | imd·1·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.09 | 0.03 | 0.10 |
| led | Kanal 1 | 11/11 | 2.59 | -0.99 | 1.11 |
| mains50 | Kanal 1 | 11/11 | 1089.04 | 2136.34 | 0.72 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.09 | -0.00 | 0.11 |
| led | Kanal 2 | 11/11 | 0.85 | 0.09 | 0.77 |
| mains50 | Kanal 2 | 11/11 | 178.44 | 406.59 | 0.58 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.04 | 0.03 | 0.09 |
| led | Kanal 3 | 11/11 | 1.55 | -0.72 | 0.48 |
| mains50 | Kanal 3 | 11/11 | 149.75 | 410.71 | 0.35 |
| fs8 | Kanal 4 | 11/11 | 0.01 | -0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.07 | 0.08 | 0.13 |
| led | Kanal 4 | 11/11 | 1.82 | -1.06 | 0.97 |
| mains50 | Kanal 4 | 11/11 | 809.25 | 1459.98 | 0.60 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.25 | 0.31 s (3.22 Hz) | 29.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 0.31 s (3.20 Hz) | 30.5 |
| Kanal 2 | breitbandig | 1.19 | 0.31 s (3.22 Hz) | 30.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 30.5 |
| Kanal 3 | breitbandig | 0.97 | 0.31 s (3.22 Hz) | 31.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 34.2 |
| Kanal 4 | breitbandig | 0.91 | 0.31 s (3.22 Hz) | 29.0 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 0.31 s (3.20 Hz) | 32.2 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.96 |
| Kanal 3 | 0.94 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.2 | -71.7 | +0.5 | 65 % | 64 % |
| Kanal 2 | -71.9 | -72.6 | +0.6 | 71 % | 69 % |
| Kanal 3 | -73.3 | -73.8 | +0.5 | 81 % | 80 % |
| Kanal 4 | -71.1 | -71.6 | +0.6 | 73 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4-3d-end-r2_psd.png)

### Kammprofile

![Kammprofile](B4-3d-end-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4-3d-end-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:30:12. Stream-Meldungen: 0. owl_read: reports/owl_read/B4-3d-end-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
