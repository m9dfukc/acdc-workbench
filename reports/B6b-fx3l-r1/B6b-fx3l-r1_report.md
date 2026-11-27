# Report B6b-fx3l-r1: B6b-fx3l-r1 – acdc1 fx3l-open-inputs-6, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 5c v22.4.r-fx3l |
| test | Build-6-Sitzung: fx3l als Kontrolle in der Mitte, Eingänge offen, rohe ADC-Daten |
| gain | gvar |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261117_acdc1_fx3l-open-inputs-6-r1_gvar_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-fx3l-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B6b-fx4b-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -69.9 | -74.0 | -72.0 | -72.7 | -85.3 | -72.3 | -92.9 | -72.0 | 66 % | -76.7 | 4.6 |
| Kanal 2 | -7.3 | -71.2 | -75.7 | -73.1 | -73.8 | -87.2 | -73.4 | -94.6 | -73.1 | 68 % | -78.0 | 4.9 |
| Kanal 3 | -5.5 | -72.9 | -77.9 | -74.5 | -75.0 | -91.6 | -74.7 | -95.7 | -74.5 | 82 % | -81.9 | 7.4 |
| Kanal 4 | -6.4 | -70.9 | -77.0 | -72.1 | -72.7 | -87.5 | -72.3 | -95.3 | -72.1 | 72 % | -77.6 | 5.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.9 dB | -83.1 | 7.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.4 | 57.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0011 | 10/10 | k=1: 2320.544 Hz, -113.4 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0126 | 0.0024 | 2/19 | k=1: 50.014 Hz, -96.1 dB | -98.8 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0024 | 8 | k=-2·f1+4·f2: 22000.259 Hz, -121.3 dB | -116.6 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 1 | 4401.9002 | 0.0001 | 2/5 | k=1: 4401.900 Hz, -91.9 dB | -94.9 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 1 | 2200.9502 | 0.0010 | 3/10 | k=1: 2200.950 Hz, -96.6 dB | -97.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.3 | 9.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.5 | 58.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0007 | 10/10 | k=9: 20884.904 Hz, -113.9 dB | -108.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0129 | 0.0021 | 2/19 | k=1: 50.014 Hz, -97.1 dB | -99.7 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0044 | 10 | k=28·f1-4·f2: 3996.285 Hz, -119.3 dB | -115.6 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 2 | 4401.9001 | 0.0002 | 2/5 | k=1: 4401.900 Hz, -93.6 dB | -96.6 | 0.4 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 2 | 2200.9501 | 0.0001 | 3/10 | k=1: 2200.950 Hz, -98.0 dB | -99.1 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.9 dB | -83.9 | 11.4 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -76.1 | 69.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0008 | 10/10 | k=1: 2320.544 Hz, -113.8 dB | -109.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0137 | 0.0025 | 4/19 | k=1: 50.014 Hz, -97.9 dB | -100.4 | 0.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0032 | 27 | k=28·f1-4·f2: 3996.284 Hz, -120.4 dB | -113.2 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 3 | 4401.9004 | 0.0006 | 2/5 | k=1: 4401.900 Hz, -97.3 dB | -100.2 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.7 dB | -97.5 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.4 | 7.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.5 dB | -74.0 | 64.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0011 | 10/10 | k=1: 2320.544 Hz, -113.2 dB | -109.6 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0128 | 0.0030 | 2/19 | k=1: 50.015 Hz, -97.9 dB | -100.5 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0080 | 20 | k=25·f1-4·f2: 996.678 Hz, -110.7 dB | -107.8 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 4 | 4401.9003 | 0.0003 | 2/5 | k=1: 4401.900 Hz, -93.6 dB | -96.5 | 0.4 % |
| stärkste übrige Linie (6602.85 Hz) | Kanal 4 | 6602.8505 | 0.0000 | 1/3 | k=1: 6602.851 Hz, -98.4 dB | -101.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 55.4 | usb1k·1 |
| 1999.736 | -81.0 | 48.9 | usb1k·2 |
| 2999.603 | -82.2 | 51.5 | usb1k·3 |
| 12000.000 | -83.9 | 54.0 | fs8·2 |
| 6000.000 | -84.6 | 51.2 | fs8·1 |
| 18000.000 | -86.7 | 51.8 | fs8·3 |
| 3999.471 | -87.6 | 45.5 | usb1k·4 |
| 9998.677 | -88.4 | 48.7 | usb1k·10 |
| 15997.883 | -90.5 | 47.4 | usb1k·16 |
| 4999.338 | -90.5 | 44.1 | usb1k·5 |
| 6999.074 | -90.3 | 46.0 | usb1k·7 |
| 4401.900 | -91.9 | 42.5 | other1·1 |
| 8998.809 | -91.0 | 45.6 | usb1k·9 |
| 16997.751 | -93.0 | 45.0 | usb1k·17 |
| 18997.487 | -93.9 | 44.5 | usb1k·19 |
| 20997.222 | -94.7 | 44.0 | usb1k·21 |
| 5999.206 | -94.6 | 41.2 | usb1k·6 |
| 7998.941 | -94.7 | 41.2 | usb1k·8 |
| 50.014 | -96.1 | 25.3 | mains50·1 |
| 2200.950 | -96.6 | 35.5 | other2·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 55.9 | usb1k·1 |
| 1999.736 | -82.6 | 49.0 | usb1k·2 |
| 2999.603 | -82.9 | 52.0 | usb1k·3 |
| 12000.000 | -84.2 | 54.9 | fs8·2 |
| 6000.000 | -84.6 | 52.1 | fs8·1 |
| 18000.000 | -86.8 | 52.6 | fs8·3 |
| 3999.471 | -88.1 | 46.3 | usb1k·4 |
| 9998.677 | -88.4 | 49.7 | usb1k·10 |
| 15997.883 | -91.1 | 48.4 | usb1k·16 |
| 4999.338 | -91.8 | 44.3 | usb1k·5 |
| 6999.074 | -91.2 | 46.6 | usb1k·7 |
| 16997.751 | -93.3 | 45.3 | usb1k·17 |
| 8998.809 | -92.0 | 45.9 | usb1k·9 |
| 4401.900 | -93.6 | 42.6 | other1·1 |
| 18997.487 | -94.0 | 45.1 | usb1k·19 |
| 20997.222 | -95.5 | 44.3 | usb1k·21 |
| 12998.280 | -96.8 | 42.0 | usb1k·13 |
| 5999.206 | -96.3 | 40.3 | usb1k·6 |
| 50.014 | -97.1 | 26.1 | mains50·1 |
| 11998.412 | -96.8 | 42.4 | usb1k·12 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 60.4 | usb1k·1 |
| 1999.736 | -82.6 | 53.5 | usb1k·2 |
| 2999.603 | -83.8 | 56.1 | usb1k·3 |
| 12000.000 | -84.9 | 57.5 | fs8·2 |
| 6000.000 | -85.3 | 56.0 | fs8·1 |
| 18000.000 | -87.2 | 55.1 | fs8·3 |
| 3999.471 | -88.6 | 50.9 | usb1k·4 |
| 9998.677 | -89.1 | 52.8 | usb1k·10 |
| 15997.883 | -91.1 | 50.9 | usb1k·16 |
| 4999.338 | -91.6 | 48.4 | usb1k·5 |
| 8998.809 | -91.8 | 50.0 | usb1k·9 |
| 6999.074 | -91.8 | 49.6 | usb1k·7 |
| 16997.751 | -93.9 | 48.0 | usb1k·17 |
| 18997.487 | -94.1 | 47.8 | usb1k·19 |
| 20997.222 | -95.6 | 46.3 | usb1k·21 |
| 11998.412 | -96.7 | 45.7 | usb1k·12 |
| 12998.280 | -97.0 | 45.8 | usb1k·13 |
| 4401.900 | -97.3 | 43.2 | other1·1 |
| 5999.206 | -96.8 | 44.5 | usb1k·6 |
| 7998.941 | -96.4 | 45.0 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.5 | 57.2 | usb1k·1 |
| 1999.735 | -81.0 | 50.5 | usb1k·2 |
| 2999.604 | -82.1 | 52.3 | usb1k·3 |
| 12000.000 | -84.4 | 53.6 | fs8·2 |
| 6000.000 | -84.5 | 51.5 | fs8·1 |
| 18000.000 | -87.1 | 51.4 | fs8·3 |
| 3999.471 | -87.6 | 46.7 | usb1k·4 |
| 9998.677 | -88.4 | 48.5 | usb1k·10 |
| 15997.883 | -90.8 | 47.7 | usb1k·16 |
| 4999.339 | -90.6 | 44.9 | usb1k·5 |
| 6999.074 | -90.7 | 46.5 | usb1k·7 |
| 8998.809 | -91.3 | 45.9 | usb1k·9 |
| 16997.751 | -93.0 | 45.0 | usb1k·17 |
| 4401.900 | -93.6 | 41.7 | other1·1 |
| 18997.487 | -94.3 | 44.2 | usb1k·19 |
| 5999.206 | -94.2 | 41.8 | usb1k·6 |
| 7998.941 | -93.9 | 42.3 | usb1k·8 |
| 20997.222 | -94.9 | 43.9 | usb1k·21 |
| 12998.280 | -96.5 | 41.4 | usb1k·13 |
| 13998.147 | -96.7 | 41.4 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.12 | 0.28 | 0.05 |
| led | Kanal 1 | 11/11 | 1.89 | 0.13 | 0.62 |
| mains50 | Kanal 1 | 11/11 | 403.36 | 324.43 | 1.12 |
| other1 | Kanal 1 | 11/11 | 1.08 | 0.91 | 0.10 |
| other2 | Kanal 1 | 11/11 | 3.19 | 4.57 | 0.16 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.12 | 0.27 | 0.07 |
| led | Kanal 2 | 11/11 | 0.38 | -0.27 | 0.41 |
| mains50 | Kanal 2 | 11/11 | 415.39 | 384.35 | 1.04 |
| other1 | Kanal 2 | 11/11 | 0.75 | 0.23 | 0.11 |
| other2 | Kanal 2 | 11/11 | 4.29 | -1.55 | 0.15 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.15 | 0.11 | 0.03 |
| led | Kanal 3 | 11/11 | 0.67 | 0.59 | 0.34 |
| mains50 | Kanal 3 | 11/11 | 509.44 | -525.47 | 0.75 |
| other1 | Kanal 3 | 11/11 | 1.19 | 1.71 | 0.11 |
| other2 | Kanal 3 | 11/11 | 1.25 | -1.73 | 0.10 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.10 | 0.26 | 0.11 |
| led | Kanal 4 | 11/11 | 1.24 | -0.64 | 0.65 |
| mains50 | Kanal 4 | 11/11 | 424.53 | 326.70 | 0.95 |
| other1 | Kanal 4 | 11/11 | 1.24 | 1.89 | 0.16 |
| other2 | Kanal 4 | 11/11 | 0.14 | -0.02 | 0.14 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.72 | 0.31 s (3.22 Hz) | 28.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 34.1 |
| Kanal 2 | breitbandig | 1.58 | 0.31 s (3.22 Hz) | 29.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 35.7 |
| Kanal 3 | breitbandig | 1.34 | 0.31 s (3.22 Hz) | 30.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 40.2 |
| Kanal 4 | breitbandig | 1.11 | 0.31 s (3.22 Hz) | 26.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 35.1 |

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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.95 | 0.94 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B6b-fx4b-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.0 | -72.2 | +0.3 | 66 % | 66 % |
| Kanal 2 | -73.1 | -73.4 | +0.3 | 68 % | 68 % |
| Kanal 3 | -74.5 | -74.5 | +0.0 | 82 % | 82 % |
| Kanal 4 | -72.1 | -72.5 | +0.4 | 72 % | 70 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-fx3l-r1_psd.png)

### Kammprofile

![Kammprofile](B6b-fx3l-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-fx3l-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:12:22. Stream-Meldungen: 0. owl_read: reports/owl_read/B6b-fx3l-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
