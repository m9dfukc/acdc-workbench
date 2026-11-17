# Report B6b-fx4b-r2: B6b-fx4b-r2 – acdc1 fx4b-open-inputs-6, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-6-Sitzung: fx4b (fx3l + Boot-Menü 15b) am Anfang, Eingänge offen, rohe ADC-Daten |
| gain | gvar |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261117_acdc1_fx4b-open-inputs-6-r2_gvar_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-fx4b-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B5c-fx3l-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.0 | -71.4 | -79.5 | -72.2 | -72.8 | -86.8 | -72.5 | -92.9 | -72.2 | 67 % | -77.1 | 4.9 |
| Kanal 2 | -7.4 | -72.5 | -80.3 | -73.3 | -74.0 | -88.5 | -73.6 | -94.7 | -73.3 | 69 % | -78.4 | 5.1 |
| Kanal 3 | -5.6 | -74.0 | -85.0 | -74.4 | -74.9 | -92.9 | -74.6 | -97.4 | -74.4 | 83 % | -82.1 | 7.7 |
| Kanal 4 | -6.5 | -71.8 | -80.3 | -72.5 | -73.0 | -88.5 | -72.7 | -95.5 | -72.5 | 71 % | -77.9 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.6 dB | -83.3 | 7.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.5 | 59.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.545 Hz, -114.0 dB | -110.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0099 | 0.0012 | 3/19 | k=1: 50.009 Hz, -96.0 dB | -99.3 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0146 | 1 | k=-18·f1+4·f2: 6002.397 Hz, -120.6 dB | -123.0 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 1 | 4401.9001 | 0.0005 | 2/5 | k=1: 4401.900 Hz, -91.8 dB | -94.8 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 1 | 2200.9501 | 0.0001 | 2/10 | k=1: 2200.950 Hz, -96.6 dB | -97.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.6 dB | -83.4 | 9.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.7 | 58.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0007 | 10/10 | k=8: 18564.358 Hz, -114.0 dB | -108.7 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0097 | 0.0024 | 4/19 | k=1: 50.009 Hz, -96.9 dB | -100.1 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0071 | 4 | k=-18·f1+4·f2: 6002.397 Hz, -120.1 dB | -119.4 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 2 | 4401.9000 | 0.0004 | 2/5 | k=1: 4401.900 Hz, -93.6 dB | -96.6 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 2 | 2200.9501 | 0.0002 | 2/10 | k=1: 2200.950 Hz, -98.2 dB | -99.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -84.1 | 10.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -75.9 | 71.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0003 | 10/10 | k=1: 2320.545 Hz, -113.9 dB | -109.6 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0095 | 0.0017 | 6/19 | k=1: 50.009 Hz, -97.4 dB | -100.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0041 | 22 | k=4·f1+2·f2: 15999.473 Hz, -124.2 dB | -115.8 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 3 | 4401.8999 | 0.0008 | 2/5 | k=1: 4401.900 Hz, -97.3 dB | -100.2 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.6 dB | -100.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.7 dB | -83.6 | 7.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.5 | 63.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0009 | 10/10 | k=1: 2320.544 Hz, -114.4 dB | -110.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0096 | 0.0029 | 5/19 | k=1: 50.009 Hz, -97.2 dB | -100.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0083 | 7 | k=-22·f1+4·f2: 2002.927 Hz, -115.9 dB | -114.4 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 4 | 4401.9001 | 0.0002 | 2/5 | k=1: 4401.900 Hz, -93.8 dB | -96.8 | 0.4 % |
| stärkste übrige Linie (6602.85 Hz) | Kanal 4 | 6602.8503 | 0.0000 | 1/3 | k=1: 6602.850 Hz, -98.5 dB | -101.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 58.6 | usb1k·1 |
| 1999.735 | -81.4 | 52.0 | usb1k·2 |
| 2999.603 | -82.5 | 51.7 | usb1k·3 |
| 6000.000 | -83.6 | 52.9 | fs8·1 |
| 12000.000 | -85.0 | 53.0 | fs8·2 |
| 3999.471 | -86.9 | 47.9 | usb1k·4 |
| 18000.000 | -87.5 | 51.0 | fs8·3 |
| 9998.676 | -88.3 | 48.8 | usb1k·10 |
| 4999.339 | -89.8 | 45.6 | usb1k·5 |
| 15997.882 | -90.5 | 46.9 | usb1k·16 |
| 4401.900 | -91.8 | 43.8 | other1·1 |
| 6999.074 | -90.8 | 45.9 | usb1k·7 |
| 8998.809 | -91.0 | 46.7 | usb1k·9 |
| 16997.750 | -93.1 | 45.2 | usb1k·17 |
| 18997.485 | -93.7 | 45.1 | usb1k·19 |
| 20997.221 | -94.7 | 43.8 | usb1k·21 |
| 5999.206 | -94.3 | 42.1 | usb1k·6 |
| 7998.941 | -94.2 | 41.2 | usb1k·8 |
| 11998.411 | -95.8 | 42.2 | usb1k·12 |
| 2200.950 | -96.6 | 37.2 | other2·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 58.6 | usb1k·1 |
| 1999.735 | -83.2 | 51.2 | usb1k·2 |
| 2999.603 | -83.3 | 52.2 | usb1k·3 |
| 6000.000 | -83.6 | 54.0 | fs8·1 |
| 12000.000 | -85.4 | 53.7 | fs8·2 |
| 18000.000 | -87.5 | 52.3 | fs8·3 |
| 3999.471 | -87.4 | 48.6 | usb1k·4 |
| 9998.676 | -88.3 | 50.2 | usb1k·10 |
| 15997.882 | -91.0 | 47.6 | usb1k·16 |
| 4999.339 | -91.0 | 45.9 | usb1k·5 |
| 6999.074 | -91.8 | 45.8 | usb1k·7 |
| 16997.750 | -93.4 | 45.4 | usb1k·17 |
| 4401.900 | -93.6 | 43.0 | other1·1 |
| 8998.809 | -92.0 | 46.7 | usb1k·9 |
| 18997.485 | -93.7 | 46.3 | usb1k·19 |
| 20997.220 | -95.5 | 43.9 | usb1k·21 |
| 5999.206 | -95.9 | 41.7 | usb1k·6 |
| 7998.941 | -95.5 | 40.9 | usb1k·8 |
| 11998.411 | -96.4 | 42.6 | usb1k·12 |
| 12998.279 | -96.9 | 41.9 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 63.9 | usb1k·1 |
| 1999.735 | -82.8 | 56.5 | usb1k·2 |
| 2999.603 | -83.9 | 56.3 | usb1k·3 |
| 6000.000 | -84.2 | 57.4 | fs8·1 |
| 12000.000 | -86.2 | 56.0 | fs8·2 |
| 18000.000 | -87.9 | 54.8 | fs8·3 |
| 3999.471 | -87.7 | 52.7 | usb1k·4 |
| 9998.676 | -88.9 | 52.8 | usb1k·10 |
| 15997.882 | -91.0 | 50.8 | usb1k·16 |
| 4999.339 | -90.9 | 50.3 | usb1k·5 |
| 6999.074 | -92.1 | 49.8 | usb1k·7 |
| 8998.809 | -91.8 | 50.5 | usb1k·9 |
| 16997.750 | -93.9 | 48.6 | usb1k·17 |
| 18997.485 | -93.8 | 47.9 | usb1k·19 |
| 20997.221 | -95.6 | 46.7 | usb1k·21 |
| 7998.941 | -95.3 | 45.6 | usb1k·8 |
| 11998.411 | -96.3 | 45.8 | usb1k·12 |
| 5999.206 | -96.2 | 45.4 | usb1k·6 |
| 4401.900 | -97.3 | 44.2 | other1·1 |
| 12998.279 | -97.2 | 45.0 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 59.6 | usb1k·1 |
| 1999.735 | -81.6 | 52.6 | usb1k·2 |
| 2999.603 | -82.6 | 52.4 | usb1k·3 |
| 6000.000 | -83.7 | 53.2 | fs8·1 |
| 12000.000 | -85.5 | 52.7 | fs8·2 |
| 3999.471 | -87.0 | 48.7 | usb1k·4 |
| 18000.000 | -87.7 | 51.1 | fs8·3 |
| 9998.676 | -88.4 | 49.5 | usb1k·10 |
| 4999.338 | -90.0 | 46.5 | usb1k·5 |
| 15997.882 | -90.6 | 47.7 | usb1k·16 |
| 6999.074 | -91.1 | 46.0 | usb1k·7 |
| 8998.809 | -91.3 | 46.5 | usb1k·9 |
| 16997.750 | -93.3 | 44.7 | usb1k·17 |
| 4401.900 | -93.8 | 42.7 | other1·1 |
| 18997.485 | -94.0 | 45.0 | usb1k·19 |
| 5999.206 | -94.2 | 42.7 | usb1k·6 |
| 20997.220 | -95.0 | 43.8 | usb1k·21 |
| 7998.941 | -93.9 | 42.0 | usb1k·8 |
| 11998.411 | -95.9 | 42.4 | usb1k·12 |
| 12998.279 | -97.0 | 41.5 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.10 |
| usb1k | Kanal 1 | 11/11 | 0.10 | -0.02 | 0.02 |
| led | Kanal 1 | 11/11 | 3.12 | -2.44 | 0.63 |
| mains50 | Kanal 1 | 11/11 | 153.16 | -26.88 | 0.95 |
| other1 | Kanal 1 | 11/11 | 1.35 | -0.23 | 0.09 |
| other2 | Kanal 1 | 11/11 | 0.26 | 0.00 | 0.18 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.00 | 0.10 |
| usb1k | Kanal 2 | 11/11 | 0.14 | 0.00 | 0.02 |
| led | Kanal 2 | 11/11 | 0.23 | 0.11 | 0.44 |
| mains50 | Kanal 2 | 11/11 | 174.48 | 28.03 | 0.78 |
| other1 | Kanal 2 | 11/11 | 1.45 | 0.52 | 0.13 |
| other2 | Kanal 2 | 11/11 | 0.24 | -0.04 | 0.22 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.09 |
| usb1k | Kanal 3 | 11/11 | 0.11 | 0.01 | 0.02 |
| led | Kanal 3 | 11/11 | 0.80 | 0.01 | 0.31 |
| mains50 | Kanal 3 | 11/11 | 61.07 | 123.10 | 0.51 |
| other1 | Kanal 3 | 11/11 | 1.35 | -1.19 | 0.12 |
| other2 | Kanal 3 | 11/11 | 0.18 | -0.00 | 0.13 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.01 | 0.10 |
| usb1k | Kanal 4 | 11/11 | 0.13 | 0.02 | 0.02 |
| led | Kanal 4 | 11/11 | 1.46 | -0.96 | 0.54 |
| mains50 | Kanal 4 | 11/11 | 379.52 | -463.06 | 0.75 |
| other1 | Kanal 4 | 11/11 | 1.70 | -0.27 | 0.12 |
| other2 | Kanal 4 | 11/11 | 0.26 | 0.02 | 0.21 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.83 | 0.31 s (3.20 Hz) | 21.4 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.5 |
| Kanal 2 | breitbandig | 0.83 | 0.31 s (3.20 Hz) | 21.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 39.5 |
| Kanal 3 | breitbandig | 0.49 | 7.50 s (0.13 Hz) | 25.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 44.2 |
| Kanal 4 | breitbandig | 0.71 | 0.16 s (6.40 Hz) | 21.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 39.3 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.93 | 0.93 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.96 | 0.93 | 1.00 |

## Vergleich mit Referenz B5c-fx3l-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.2 | -72.0 | -0.1 | 67 % | 68 % |
| Kanal 2 | -73.3 | -73.0 | -0.3 | 69 % | 71 % |
| Kanal 3 | -74.4 | -74.4 | +0.0 | 83 % | 83 % |
| Kanal 4 | -72.5 | -72.0 | -0.5 | 71 % | 75 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-fx4b-r2_psd.png)

### Kammprofile

![Kammprofile](B6b-fx4b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-fx4b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:08:48. Stream-Meldungen: 0. owl_read: out/owl_read/B6b-fx4b-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
