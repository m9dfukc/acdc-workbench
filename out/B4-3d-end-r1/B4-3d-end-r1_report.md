# Report B4-3d-end-r1: B4-3d-end-r1 – acdc1 3d-end-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4-Sitzung (Q3): 3d-Endkontrolle nach fx3i (zurückgeflasht), Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4-3d-end-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -70.2 | -77.1 | -71.2 | -72.3 | -86.0 | -71.6 | – | -71.2 | 65 % | -75.7 | 4.5 |
| Kanal 2 | -7.1 | -71.0 | -77.9 | -72.0 | -73.1 | -87.9 | -72.3 | – | -72.0 | 71 % | -77.4 | 5.4 |
| Kanal 3 | -5.3 | -72.3 | -79.0 | -73.3 | -74.5 | -91.9 | -73.6 | – | -73.3 | 81 % | -80.4 | 7.1 |
| Kanal 4 | -6.2 | -70.4 | -78.4 | -71.2 | -72.1 | -88.2 | -71.5 | – | -71.2 | 73 % | -76.8 | 5.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.4 dB | -78.5 | 18.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.1 | 41.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0019 | 10/10 | k=1: 2320.544 Hz, -115.2 dB | -112.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0079 | 0.0009 | 2/19 | k=1: 50.008 Hz, -94.6 dB | -97.6 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0012 | 148 | k=8·f1+1·f2: 13998.941 Hz, -94.8 dB | -84.9 | 4.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.3 dB | -78.3 | 23.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.7 | 42.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0009 | 10/10 | k=10: 23205.448 Hz, -115.4 dB | -110.2 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0082 | 0.0003 | 2/19 | k=1: 50.008 Hz, -95.3 dB | -98.3 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0010 | 156 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 5.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.6 dB | -78.6 | 29.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.5 dB | -76.8 | 44.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0016 | 10/10 | k=1: 2320.544 Hz, -116.4 dB | -112.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0081 | 0.0004 | 2/19 | k=1: 50.008 Hz, -96.0 dB | -98.9 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0015 | 164 | k=8·f1+1·f2: 13998.941 Hz, -94.8 dB | -85.0 | 6.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.5 | 18.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -74.2 | 50.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0017 | 10/10 | k=1: 2320.544 Hz, -114.9 dB | -111.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0081 | 0.0005 | 2/19 | k=1: 50.008 Hz, -95.9 dB | -99.0 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0011 | 152 | k=8·f1+1·f2: 13998.941 Hz, -94.9 dB | -84.9 | 4.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 57.6 | usb1k·1 |
| 6000.000 | -78.4 | 55.9 | fs8·1 |
| 18000.000 | -81.5 | 54.5 | fs8·3 |
| 12000.000 | -81.6 | 54.2 | fs8·2 |
| 1999.735 | -81.8 | 50.5 | usb1k·2 |
| 2999.603 | -82.1 | 51.2 | usb1k·3 |
| 6999.074 | -86.7 | 47.8 | usb1k·7 |
| 15997.882 | -91.1 | 44.9 | usb1k·16 |
| 9998.676 | -91.4 | 44.2 | usb1k·10 |
| 5999.206 | -93.5 | 40.7 | usb1k·6 |
| 10998.544 | -93.6 | 41.9 | usb1k·11 |
| 14998.014 | -94.8 | 41.0 | usb1k·15 |
| 4999.338 | -94.4 | 39.5 | usb1k·5 |
| 15999.471 | -95.4 | 40.5 | imd·4·f1+2·f2 |
| 9999.471 | -95.7 | 39.9 | imd·4·f1+1·f2 |
| 50.008 | -94.6 | 28.4 | mains50·1 |
| 13998.941 | -94.8 | 40.6 | imd·8·f1+1·f2 |
| 12999.868 | -96.8 | 39.4 | imd·1·f1+2·f2 |
| 20997.220 | -97.0 | 38.8 | usb1k·21 |
| 19998.941 | -96.0 | 40.0 | imd·8·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 58.5 | usb1k·1 |
| 6000.000 | -78.3 | 57.4 | fs8·1 |
| 18000.000 | -81.4 | 56.1 | fs8·3 |
| 12000.000 | -81.4 | 56.2 | fs8·2 |
| 1999.735 | -82.5 | 51.6 | usb1k·2 |
| 2999.603 | -82.6 | 52.6 | usb1k·3 |
| 6999.074 | -86.9 | 49.5 | usb1k·7 |
| 15997.882 | -91.4 | 46.2 | usb1k·16 |
| 9998.676 | -91.6 | 45.4 | usb1k·10 |
| 10998.544 | -93.7 | 43.6 | usb1k·11 |
| 14998.014 | -94.5 | 43.1 | usb1k·15 |
| 5999.206 | -94.3 | 41.5 | usb1k·6 |
| 15999.471 | -95.3 | 42.3 | imd·4·f1+2·f2 |
| 9999.471 | -95.5 | 41.6 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 42.4 | imd·8·f1+1·f2 |
| 12999.868 | -96.6 | 40.9 | imd·1·f1+2·f2 |
| 4999.338 | -96.2 | 39.2 | usb1k·5 |
| 50.008 | -95.3 | 29.6 | mains50·1 |
| 14999.603 | -97.0 | 40.7 | imd·3·f1+2·f2 |
| 19998.941 | -95.8 | 41.7 | imd·8·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.5 | 61.5 | usb1k·1 |
| 6000.000 | -78.6 | 60.3 | fs8·1 |
| 12000.000 | -81.4 | 58.9 | fs8·2 |
| 18000.000 | -81.6 | 58.4 | fs8·3 |
| 2999.603 | -83.4 | 55.2 | usb1k·3 |
| 1999.735 | -84.5 | 53.5 | usb1k·2 |
| 6999.074 | -87.4 | 51.9 | usb1k·7 |
| 15997.882 | -92.1 | 47.5 | usb1k·16 |
| 9998.676 | -92.0 | 47.9 | usb1k·10 |
| 14998.014 | -94.8 | 44.7 | usb1k·15 |
| 10998.544 | -94.0 | 45.8 | usb1k·11 |
| 15999.471 | -95.5 | 44.1 | imd·4·f1+2·f2 |
| 9999.471 | -95.8 | 44.0 | imd·4·f1+1·f2 |
| 13998.941 | -94.8 | 45.0 | imd·8·f1+1·f2 |
| 5999.206 | -95.9 | 43.1 | usb1k·6 |
| 12999.868 | -96.8 | 43.0 | imd·1·f1+2·f2 |
| 11998.411 | -96.9 | 43.5 | usb1k·12 |
| 19998.941 | -96.1 | 43.9 | imd·8·f1+2·f2 |
| 8999.603 | -97.4 | 42.4 | imd·3·f1+1·f2 |
| 50.008 | -96.0 | 33.3 | mains50·1 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 59.8 | usb1k·1 |
| 6000.000 | -78.5 | 56.7 | fs8·1 |
| 1999.735 | -80.1 | 53.7 | usb1k·2 |
| 12000.000 | -81.5 | 54.9 | fs8·2 |
| 18000.000 | -81.5 | 55.2 | fs8·3 |
| 2999.603 | -81.6 | 53.0 | usb1k·3 |
| 6999.074 | -86.5 | 49.0 | usb1k·7 |
| 15997.882 | -90.4 | 46.1 | usb1k·16 |
| 4999.338 | -91.6 | 43.0 | usb1k·5 |
| 9998.676 | -91.1 | 45.2 | usb1k·10 |
| 5999.206 | -91.7 | 43.4 | usb1k·6 |
| 10998.544 | -93.2 | 42.7 | usb1k·11 |
| 14998.014 | -94.7 | 41.7 | usb1k·15 |
| 15999.471 | -95.5 | 41.1 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 40.7 | imd·4·f1+1·f2 |
| 20997.220 | -96.1 | 40.0 | usb1k·21 |
| 13998.941 | -94.9 | 40.8 | imd·8·f1+1·f2 |
| 13998.147 | -96.4 | 39.3 | usb1k·14 |
| 11998.411 | -96.1 | 40.3 | usb1k·12 |
| 12999.868 | -96.9 | 39.5 | imd·1·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.08 | -0.06 | 0.05 |
| led | Kanal 1 | 11/11 | 9.08 | 20.65 | 0.94 |
| mains50 | Kanal 1 | 11/11 | 203.14 | 623.30 | 0.80 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.07 | -0.03 | 0.06 |
| led | Kanal 2 | 11/11 | 0.30 | 0.50 | 0.43 |
| mains50 | Kanal 2 | 11/11 | 170.36 | 575.08 | 0.66 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.07 | -0.09 | 0.06 |
| led | Kanal 3 | 11/11 | 0.77 | -0.15 | 0.46 |
| mains50 | Kanal 3 | 11/11 | 147.34 | 510.92 | 0.35 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.06 | -0.00 | 0.08 |
| led | Kanal 4 | 11/11 | 2.23 | 1.01 | 0.62 |
| mains50 | Kanal 4 | 11/11 | 173.57 | 580.48 | 0.71 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.05 | 0.31 s (3.22 Hz) | 24.8 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 31.3 |
| Kanal 2 | breitbandig | 1.04 | 0.31 s (3.22 Hz) | 26.1 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 32.9 |
| Kanal 3 | breitbandig | 1.09 | 0.31 s (3.22 Hz) | 26.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 1.25 s (0.80 Hz) | 36.4 |
| Kanal 4 | breitbandig | 0.85 | 0.31 s (3.22 Hz) | 25.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 1.25 s (0.80 Hz) | 32.9 |

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
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.96 |
| Kanal 3 | 0.93 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.2 | -71.7 | +0.4 | 65 % | 64 % |
| Kanal 2 | -72.0 | -72.6 | +0.6 | 71 % | 69 % |
| Kanal 3 | -73.3 | -73.8 | +0.5 | 81 % | 80 % |
| Kanal 4 | -71.2 | -71.6 | +0.5 | 73 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4-3d-end-r1_psd.png)

### Kammprofile

![Kammprofile](B4-3d-end-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4-3d-end-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:28:59. Stream-Meldungen: 0. owl_read: out/owl_read/B4-3d-end-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
