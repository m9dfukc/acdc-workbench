# Report B6b-fx3l-r2: B6b-fx3l-r2 – acdc1 fx3l-open-inputs-6, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 5c v22.4.r-fx3l |
| test | Build-6-Sitzung: fx3l als Kontrolle in der Mitte, Eingänge offen, rohe ADC-Daten |
| gain | gvar |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261117_acdc1_fx3l-open-inputs-6-r2_gvar_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-fx3l-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B6b-fx4b-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.9 | -71.4 | -80.2 | -72.0 | -72.8 | -85.3 | -72.4 | -92.8 | -72.1 | 64 % | -76.5 | 4.4 |
| Kanal 2 | -7.3 | -72.7 | -82.4 | -73.2 | -74.0 | -87.4 | -73.6 | -94.7 | -73.3 | 66 % | -78.0 | 4.7 |
| Kanal 3 | -5.5 | -74.2 | -86.3 | -74.5 | -75.1 | -91.7 | -74.7 | -95.7 | -74.5 | 81 % | -81.7 | 7.2 |
| Kanal 4 | -6.4 | -72.1 | -83.2 | -72.4 | -73.1 | -87.6 | -72.7 | -95.5 | -72.5 | 70 % | -77.6 | 5.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.1 | 8.0 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.6 | 55.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0018 | 10/10 | k=1: 2320.543 Hz, -113.5 dB | -110.1 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0162 | 0.0000 | 2/19 | k=1: 50.016 Hz, -97.0 dB | -99.9 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0021 | 5 | k=-2·f1+4·f2: 22000.265 Hz, -122.5 dB | -119.3 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 1 | 4401.9002 | 0.0002 | 2/5 | k=1: 4401.900 Hz, -91.7 dB | -94.7 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 1 | 2200.9500 | 0.0002 | 2/10 | k=1: 2200.950 Hz, -96.8 dB | -97.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.5 dB | -83.2 | 10.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.6 dB | -75.8 | 55.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0014 | 10/10 | k=8: 18564.359 Hz, -113.5 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0161 | 0.0008 | 4/19 | k=1: 50.016 Hz, -97.5 dB | -100.3 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0018 | 14 | k=-1·f1+2·f2: 11000.130 Hz, -118.8 dB | -113.5 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 2 | 4401.9003 | 0.0006 | 2/5 | k=1: 4401.900 Hz, -93.6 dB | -96.6 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 2 | 2200.9501 | 0.0000 | 2/10 | k=1: 2200.950 Hz, -98.2 dB | -99.2 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -85.1 dB | -83.8 | 11.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -76.1 | 68.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0006 | 10/10 | k=1: 2320.544 Hz, -114.1 dB | -109.7 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0159 | 0.0018 | 6/19 | k=1: 50.016 Hz, -98.4 dB | -101.1 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0015 | 24 | k=-3·f1+1·f2: 3000.397 Hz, -120.5 dB | -113.4 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 3 | 4401.9001 | 0.0003 | 2/5 | k=1: 4401.900 Hz, -97.2 dB | -100.2 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.7 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.6 dB | -83.3 | 8.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.6 | 61.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0016 | 10/10 | k=1: 2320.543 Hz, -113.4 dB | -109.8 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0162 | 0.0002 | 3/19 | k=1: 50.016 Hz, -97.8 dB | -100.5 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0021 | 18 | k=-1·f1+2·f2: 11000.131 Hz, -111.6 dB | -107.2 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 4 | 4401.9003 | 0.0004 | 2/5 | k=1: 4401.900 Hz, -93.8 dB | -96.8 | 0.4 % |
| stärkste übrige Linie (6602.85 Hz) | Kanal 4 | 6602.8503 | 0.0000 | 1/3 | k=1: 6602.850 Hz, -98.4 dB | -101.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 57.1 | usb1k·1 |
| 1999.735 | -81.4 | 50.7 | usb1k·2 |
| 2999.603 | -82.4 | 51.8 | usb1k·3 |
| 12000.000 | -84.2 | 53.2 | fs8·2 |
| 6000.000 | -84.4 | 51.1 | fs8·1 |
| 18000.000 | -86.1 | 51.7 | fs8·3 |
| 3999.471 | -88.0 | 45.3 | usb1k·4 |
| 9998.677 | -88.5 | 48.2 | usb1k·10 |
| 15997.883 | -90.8 | 47.6 | usb1k·16 |
| 4999.339 | -91.0 | 43.3 | usb1k·5 |
| 4401.900 | -91.7 | 41.1 | other1·1 |
| 6999.074 | -90.5 | 45.6 | usb1k·7 |
| 8998.809 | -91.5 | 44.5 | usb1k·9 |
| 16997.751 | -93.1 | 44.9 | usb1k·17 |
| 18997.486 | -93.5 | 44.5 | usb1k·19 |
| 20997.221 | -95.0 | 43.5 | usb1k·21 |
| 11998.412 | -95.8 | 41.6 | usb1k·12 |
| 5999.207 | -95.4 | 40.1 | usb1k·6 |
| 7998.941 | -95.0 | 40.8 | usb1k·8 |
| 2200.950 | -96.8 | 34.6 | other2·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.6 | 57.4 | usb1k·1 |
| 1999.735 | -82.8 | 50.8 | usb1k·2 |
| 2999.603 | -83.2 | 52.2 | usb1k·3 |
| 12000.000 | -84.5 | 54.5 | fs8·2 |
| 6000.000 | -84.5 | 52.6 | fs8·1 |
| 18000.000 | -86.1 | 52.8 | fs8·3 |
| 3999.471 | -88.6 | 46.6 | usb1k·4 |
| 9998.677 | -88.6 | 49.6 | usb1k·10 |
| 15997.883 | -91.4 | 48.3 | usb1k·16 |
| 6999.074 | -91.3 | 46.2 | usb1k·7 |
| 4999.339 | -92.5 | 43.4 | usb1k·5 |
| 16997.750 | -93.6 | 45.3 | usb1k·17 |
| 4401.900 | -93.6 | 41.6 | other1·1 |
| 18997.486 | -93.6 | 45.4 | usb1k·19 |
| 8998.809 | -92.5 | 45.0 | usb1k·9 |
| 20997.221 | -95.6 | 43.6 | usb1k·21 |
| 11998.412 | -96.5 | 42.5 | usb1k·12 |
| 12998.279 | -96.9 | 42.3 | usb1k·13 |
| 50.016 | -97.5 | 27.4 | mains50·1 |
| 14998.015 | -98.1 | 40.9 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 61.9 | usb1k·1 |
| 1999.735 | -83.0 | 55.1 | usb1k·2 |
| 2999.603 | -83.8 | 56.1 | usb1k·3 |
| 6000.000 | -85.1 | 56.0 | fs8·1 |
| 12000.000 | -85.3 | 56.5 | fs8·2 |
| 18000.000 | -86.5 | 55.1 | fs8·3 |
| 3999.471 | -88.9 | 50.4 | usb1k·4 |
| 9998.677 | -89.0 | 52.6 | usb1k·10 |
| 15997.883 | -91.4 | 51.0 | usb1k·16 |
| 4999.339 | -91.9 | 48.0 | usb1k·5 |
| 6999.074 | -92.2 | 49.5 | usb1k·7 |
| 8998.809 | -92.3 | 48.9 | usb1k·9 |
| 16997.750 | -93.9 | 47.7 | usb1k·17 |
| 18997.486 | -93.8 | 48.1 | usb1k·19 |
| 20997.221 | -96.0 | 46.0 | usb1k·21 |
| 11998.412 | -96.3 | 45.5 | usb1k·12 |
| 4401.900 | -97.2 | 42.2 | other1·1 |
| 12998.279 | -97.1 | 45.0 | usb1k·13 |
| 7998.941 | -96.3 | 45.1 | usb1k·8 |
| 5999.207 | -97.3 | 43.7 | usb1k·6 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 58.4 | usb1k·1 |
| 1999.735 | -80.9 | 52.4 | usb1k·2 |
| 2999.603 | -82.5 | 52.5 | usb1k·3 |
| 6000.000 | -84.6 | 51.7 | fs8·1 |
| 12000.000 | -84.7 | 53.6 | fs8·2 |
| 18000.000 | -86.2 | 52.1 | fs8·3 |
| 3999.471 | -88.0 | 46.8 | usb1k·4 |
| 9998.677 | -88.7 | 49.0 | usb1k·10 |
| 15997.883 | -91.0 | 47.5 | usb1k·16 |
| 6999.074 | -90.4 | 46.4 | usb1k·7 |
| 4999.339 | -91.4 | 44.0 | usb1k·5 |
| 8998.809 | -91.7 | 45.4 | usb1k·9 |
| 16997.750 | -93.4 | 44.4 | usb1k·17 |
| 4401.900 | -93.8 | 41.3 | other1·1 |
| 18997.486 | -93.8 | 44.6 | usb1k·19 |
| 20997.221 | -94.9 | 43.4 | usb1k·21 |
| 7998.941 | -94.7 | 42.2 | usb1k·8 |
| 13998.147 | -96.2 | 42.0 | usb1k·14 |
| 11998.412 | -96.0 | 42.4 | usb1k·12 |
| 5999.207 | -96.1 | 40.1 | usb1k·6 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.19 | -0.02 | 0.04 |
| led | Kanal 1 | 11/11 | 1.40 | -1.96 | 0.63 |
| mains50 | Kanal 1 | 11/11 | 205.11 | 314.78 | 0.80 |
| other1 | Kanal 1 | 11/11 | 0.91 | 0.25 | 0.16 |
| other2 | Kanal 1 | 11/11 | 0.27 | 0.01 | 0.15 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.23 | 0.02 | 0.06 |
| led | Kanal 2 | 11/11 | 0.23 | 0.04 | 0.28 |
| mains50 | Kanal 2 | 11/11 | 229.19 | 386.77 | 0.80 |
| other1 | Kanal 2 | 11/11 | 1.07 | 0.30 | 0.21 |
| other2 | Kanal 2 | 11/11 | 0.27 | 0.21 | 0.19 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.19 | -0.04 | 0.03 |
| led | Kanal 3 | 11/11 | 0.87 | -1.43 | 0.34 |
| mains50 | Kanal 3 | 11/11 | 245.25 | 343.52 | 0.41 |
| other1 | Kanal 3 | 11/11 | 1.26 | 0.01 | 0.15 |
| other2 | Kanal 3 | 11/11 | 0.41 | 0.02 | 0.10 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.19 | 0.03 | 0.07 |
| led | Kanal 4 | 11/11 | 1.64 | -0.26 | 0.49 |
| mains50 | Kanal 4 | 11/11 | 337.51 | 269.19 | 0.89 |
| other1 | Kanal 4 | 11/11 | 1.04 | 0.76 | 0.20 |
| other2 | Kanal 4 | 11/11 | 0.28 | 0.29 | 0.26 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.82 | 7.50 s (0.13 Hz) | 17.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 36.6 |
| Kanal 2 | breitbandig | 0.72 | 7.50 s (0.13 Hz) | 19.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.98 | 7.50 s (0.13 Hz) | 38.6 |
| Kanal 3 | breitbandig | 0.47 | 7.50 s (0.13 Hz) | 25.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 42.7 |
| Kanal 4 | breitbandig | 0.58 | 7.50 s (0.13 Hz) | 20.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 38.0 |

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
| Kanal 1 | 1.00 | 0.96 | 0.93 | 0.94 |
| Kanal 2 | 0.96 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.93 | 0.93 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B6b-fx4b-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.0 | -72.2 | +0.2 | 64 % | 66 % |
| Kanal 2 | -73.2 | -73.4 | +0.1 | 66 % | 68 % |
| Kanal 3 | -74.5 | -74.5 | -0.0 | 81 % | 82 % |
| Kanal 4 | -72.4 | -72.5 | +0.1 | 70 % | 70 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-fx3l-r2_psd.png)

### Kammprofile

![Kammprofile](B6b-fx3l-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-fx3l-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:13:36. Stream-Meldungen: 0. owl_read: out/owl_read/B6b-fx3l-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
