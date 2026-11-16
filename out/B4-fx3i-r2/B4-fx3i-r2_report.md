# Report B4-fx3i-r2: B4-fx3i-r2 – acdc1 fx3i-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4 v22.4.r-fx3i (ITCM) |
| test | Build-4-Sitzung (Q3): fx3i nach Kontrolle B4-3d, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3i-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4-fx3i-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.0 | -71.0 | -77.1 | -72.3 | -73.0 | -86.0 | -72.6 | -95.0 | -72.3 | 65 % | -76.9 | 4.6 |
| Kanal 2 | -7.3 | -72.1 | -78.5 | -73.2 | -73.9 | -88.1 | -73.5 | -95.3 | -73.2 | 69 % | -78.4 | 5.1 |
| Kanal 3 | -5.5 | -73.9 | -81.0 | -74.8 | -75.4 | -92.3 | -75.0 | -96.3 | -74.8 | 81 % | -82.0 | 7.1 |
| Kanal 4 | -6.3 | -71.6 | -80.1 | -72.3 | -73.5 | -88.5 | -72.7 | -95.6 | -72.3 | 72 % | -77.9 | 5.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.3 | 7.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.7 | 57.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0017 | 10/10 | k=2: 4641.089 Hz, -113.2 dB | -109.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0232 | 0.0000 | 1/19 | k=1: 50.023 Hz, -96.9 dB | -100.3 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0037 | 11 | k=-1·f1+1·f2: 5000.133 Hz, -119.7 dB | -113.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -97.1 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.001 Hz, -98.4 dB | -99.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.7 dB | -83.5 | 9.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.5 | 59.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0012 | 10/10 | k=9: 20884.904 Hz, -113.6 dB | -108.1 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0234 | 0.0000 | 1/19 | k=1: 50.023 Hz, -97.8 dB | -101.2 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0039 | 10 | k=3·f1+2·f2: 14999.604 Hz, -120.8 dB | -115.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -97.4 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -98.9 dB | -99.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -85.1 dB | -84.1 | 12.0 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.5 | 68.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0009 | 10/10 | k=2: 4641.090 Hz, -114.1 dB | -109.6 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0226 | 0.0004 | 3/19 | k=1: 50.023 Hz, -98.5 dB | -101.5 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0036 | 33 | k=-7·f1+4·f2: 17000.923 Hz, -121.0 dB | -112.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -100.3 dB | -98.2 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.3 dB | -100.6 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.8 dB | -83.8 | 7.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.6 | 46.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0012 | 10/10 | k=3: 6961.634 Hz, -115.2 dB | -110.0 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0233 | 0.0000 | 1/19 | k=1: 50.023 Hz, -98.2 dB | -101.5 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0013 | 167 | k=1·f1+2·f2: 12999.868 Hz, -86.3 dB | -79.8 | 18.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.001 Hz, -99.3 dB | -99.8 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0001 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -100.4 dB | -97.7 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 57.3 | usb1k·1 |
| 1999.736 | -82.1 | 50.5 | usb1k·2 |
| 2999.603 | -83.2 | 50.8 | usb1k·3 |
| 12000.000 | -84.4 | 52.7 | fs8·2 |
| 6000.000 | -84.5 | 50.6 | fs8·1 |
| 18000.000 | -86.8 | 51.4 | fs8·3 |
| 3999.471 | -87.0 | 46.3 | usb1k·4 |
| 9998.677 | -89.0 | 48.4 | usb1k·10 |
| 4999.339 | -89.6 | 45.4 | usb1k·5 |
| 15997.883 | -90.9 | 46.6 | usb1k·16 |
| 8998.809 | -91.8 | 44.7 | usb1k·9 |
| 18997.486 | -92.9 | 45.3 | usb1k·19 |
| 6999.074 | -92.2 | 43.7 | usb1k·7 |
| 16997.751 | -93.5 | 44.0 | usb1k·17 |
| 5999.207 | -94.6 | 40.5 | usb1k·6 |
| 11998.412 | -95.7 | 41.4 | usb1k·12 |
| 7998.942 | -94.8 | 41.4 | usb1k·8 |
| 12998.280 | -96.6 | 41.5 | usb1k·13 |
| 20997.222 | -96.6 | 41.6 | usb1k·21 |
| 50.023 | -96.9 | 25.4 | mains50·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 58.4 | usb1k·1 |
| 1999.735 | -82.9 | 50.9 | usb1k·2 |
| 2999.603 | -83.8 | 51.6 | usb1k·3 |
| 6000.000 | -84.7 | 51.9 | fs8·1 |
| 12000.000 | -84.7 | 54.3 | fs8·2 |
| 18000.000 | -86.8 | 52.6 | fs8·3 |
| 3999.471 | -87.3 | 48.0 | usb1k·4 |
| 9998.677 | -89.1 | 49.6 | usb1k·10 |
| 4999.339 | -90.3 | 46.2 | usb1k·5 |
| 15997.883 | -91.1 | 48.0 | usb1k·16 |
| 18997.486 | -92.8 | 46.5 | usb1k·19 |
| 8998.809 | -92.2 | 45.8 | usb1k·9 |
| 6999.074 | -92.6 | 44.8 | usb1k·7 |
| 16997.751 | -93.9 | 45.2 | usb1k·17 |
| 11998.412 | -96.0 | 43.0 | usb1k·12 |
| 12998.280 | -96.7 | 42.4 | usb1k·13 |
| 5999.207 | -96.0 | 40.5 | usb1k·6 |
| 7998.942 | -95.7 | 42.1 | usb1k·8 |
| 20997.222 | -97.0 | 42.0 | usb1k·21 |
| 2000.000 | -98.7 | 35.0 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 61.6 | usb1k·1 |
| 1999.736 | -84.4 | 54.2 | usb1k·2 |
| 2999.603 | -84.7 | 55.4 | usb1k·3 |
| 6000.000 | -85.1 | 55.3 | fs8·1 |
| 12000.000 | -85.4 | 56.3 | fs8·2 |
| 18000.000 | -87.2 | 54.7 | fs8·3 |
| 3999.471 | -88.0 | 51.2 | usb1k·4 |
| 9998.677 | -89.4 | 52.7 | usb1k·10 |
| 15997.883 | -91.7 | 50.1 | usb1k·16 |
| 4999.339 | -91.2 | 49.1 | usb1k·5 |
| 18997.486 | -93.2 | 48.7 | usb1k·19 |
| 8998.809 | -93.1 | 47.9 | usb1k·9 |
| 16997.751 | -94.3 | 46.7 | usb1k·17 |
| 6999.074 | -93.5 | 47.5 | usb1k·7 |
| 11998.412 | -96.5 | 45.2 | usb1k·12 |
| 12998.280 | -97.0 | 44.7 | usb1k·13 |
| 7998.942 | -96.2 | 45.1 | usb1k·8 |
| 5999.207 | -97.2 | 43.1 | usb1k·6 |
| 20997.222 | -97.8 | 43.7 | usb1k·21 |
| 50.023 | -98.5 | 30.3 | mains50·1 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 58.5 | usb1k·1 |
| 1999.736 | -82.1 | 51.9 | usb1k·2 |
| 2999.603 | -83.0 | 51.8 | usb1k·3 |
| 12000.000 | -84.8 | 53.1 | fs8·2 |
| 6000.000 | -85.0 | 50.8 | fs8·1 |
| 12999.868 | -86.3 | 51.0 | imd·1·f1+2·f2 |
| 11000.132 | -86.3 | 51.1 | imd·-1·f1+2·f2 |
| 23000.132 | -86.4 | 51.1 | imd·-1·f1+4·f2 |
| 6999.868 | -86.4 | 49.9 | imd·1·f1+1·f2 |
| 17000.132 | -86.5 | 50.7 | imd·-1·f1+3·f2 |
| 18999.868 | -86.5 | 51.1 | imd·1·f1+3·f2 |
| 5000.132 | -86.6 | 48.9 | imd·-1·f1+1·f2 |
| 18000.000 | -87.1 | 51.3 | fs8·3 |
| 3999.471 | -88.2 | 46.9 | usb1k·4 |
| 4999.339 | -90.4 | 45.1 | usb1k·5 |
| 8998.810 | -90.3 | 46.7 | usb1k·9 |
| 9998.677 | -90.9 | 46.5 | usb1k·10 |
| 15997.883 | -92.1 | 45.2 | usb1k·16 |
| 6999.074 | -92.9 | 43.4 | usb1k·7 |
| 19999.736 | -94.1 | 43.3 | imd·2·f1+3·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.07 |
| usb1k | Kanal 1 | 11/11 | 0.14 | -0.01 | 0.07 |
| led | Kanal 1 | 11/11 | 1.26 | -0.26 | 0.38 |
| mains50 | Kanal 1 | 11/11 | 223.43 | -531.14 | 0.76 |
| other1 | Kanal 1 | 11/11 | 1.23 | -1.98 | 0.08 |
| other2 | Kanal 1 | 11/11 | 0.23 | -0.19 | 0.18 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.01 | 0.07 |
| usb1k | Kanal 2 | 11/11 | 0.15 | -0.01 | 0.05 |
| led | Kanal 2 | 11/11 | 0.57 | 0.96 | 0.35 |
| mains50 | Kanal 2 | 11/11 | 215.43 | -545.98 | 0.65 |
| other1 | Kanal 2 | 11/11 | 1.27 | -1.79 | 0.09 |
| other2 | Kanal 2 | 11/11 | 0.19 | -0.00 | 0.14 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.08 |
| usb1k | Kanal 3 | 11/11 | 0.16 | -0.07 | 0.07 |
| led | Kanal 3 | 11/11 | 0.69 | 0.88 | 0.32 |
| mains50 | Kanal 3 | 11/11 | 464.73 | -211.92 | 0.36 |
| other1 | Kanal 3 | 11/11 | 0.32 | -0.08 | 0.07 |
| other2 | Kanal 3 | 11/11 | 0.17 | -0.07 | 0.10 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.00 | 0.07 |
| usb1k | Kanal 4 | 11/11 | 0.16 | -0.02 | 0.05 |
| led | Kanal 4 | 11/11 | 0.81 | 0.41 | 0.51 |
| mains50 | Kanal 4 | 11/11 | 250.99 | -509.64 | 0.70 |
| other1 | Kanal 4 | 11/11 | 0.16 | -0.29 | 0.19 |
| other2 | Kanal 4 | 11/11 | 11.89 | -40.84 | 0.15 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.24 | 0.31 s (3.22 Hz) | 23.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 33.2 |
| Kanal 2 | breitbandig | 1.17 | 0.31 s (3.22 Hz) | 25.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 35.3 |
| Kanal 3 | breitbandig | 0.94 | 0.31 s (3.22 Hz) | 23.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 38.9 |
| Kanal 4 | breitbandig | 0.84 | 0.31 s (3.22 Hz) | 24.0 |
| Kanal 4 | 999.9 Hz ± 10 | 1.01 | 1.25 s (0.80 Hz) | 38.2 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.83 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.85 |
| Kanal 3 | 0.94 | 0.94 | 1.00 | 0.81 |
| Kanal 4 | 0.83 | 0.85 | 0.81 | 1.00 |

## Vergleich mit Referenz B4-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.3 | -71.7 | -0.6 | 65 % | 64 % |
| Kanal 2 | -73.2 | -72.6 | -0.7 | 69 % | 69 % |
| Kanal 3 | -74.8 | -73.8 | -1.0 | 81 % | 80 % |
| Kanal 4 | -72.3 | -71.6 | -0.7 | 72 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4-fx3i-r2_psd.png)

### Kammprofile

![Kammprofile](B4-fx3i-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4-fx3i-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:19:02. Stream-Meldungen: 0. owl_read: out/owl_read/B4-fx3i-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
