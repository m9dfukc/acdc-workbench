# Report B6b-fx4b-r1: B6b-fx4b-r1 – acdc1 fx4b-open-inputs-6, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-6-Sitzung: fx4b (fx3l + Boot-Menü 15b) am Anfang, Eingänge offen, rohe ADC-Daten |
| gain | gvar |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261117_acdc1_fx4b-open-inputs-6-r1_gvar_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-fx4b-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B5c-fx3l-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.0 | -71.2 | -77.7 | -72.2 | -72.9 | -86.7 | -72.5 | -92.8 | -72.3 | 66 % | -77.0 | 4.7 |
| Kanal 2 | -7.4 | -72.2 | -78.6 | -73.4 | -74.1 | -88.4 | -73.7 | -94.7 | -73.4 | 68 % | -78.3 | 4.9 |
| Kanal 3 | -5.5 | -73.9 | -82.9 | -74.5 | -75.0 | -92.9 | -74.7 | -97.4 | -74.5 | 82 % | -82.0 | 7.5 |
| Kanal 4 | -6.5 | -71.6 | -78.7 | -72.5 | -73.1 | -88.5 | -72.8 | -95.5 | -72.5 | 70 % | -77.8 | 5.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -83.6 | 7.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.6 | 58.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.544 Hz, -114.2 dB | -110.1 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9925 | 0.0016 | 4/19 | k=1: 49.991 Hz, -96.0 dB | -98.8 | 0.2 % |
| Mischprodukte n·999.8677 + m·5999.9999 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0016 | 4 | k=-4·f1+4·f2: 20000.532 Hz, -123.1 dB | -120.7 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 1 | 4401.9001 | 0.0001 | 2/5 | k=1: 4401.900 Hz, -91.8 dB | -94.8 | 0.6 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 1 | 2200.9501 | 0.0001 | 2/10 | k=1: 2200.950 Hz, -96.5 dB | -97.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -83.8 | 9.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.5 dB | -75.8 | 58.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0004 | 10/10 | k=9: 20884.904 Hz, -113.8 dB | -108.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9924 | 0.0015 | 4/19 | k=1: 49.991 Hz, -96.9 dB | -99.7 | 0.2 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0015 | 11 | k=-1·f1+3·f2: 17000.131 Hz, -122.4 dB | -116.2 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 2 | 4401.9003 | 0.0007 | 2/5 | k=1: 4401.900 Hz, -93.6 dB | -96.6 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 2 | 2200.9501 | 0.0002 | 2/10 | k=1: 2200.950 Hz, -98.0 dB | -99.1 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -84.4 | 10.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -76.0 | 71.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0005 | 10/10 | k=1: 2320.544 Hz, -114.5 dB | -109.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9924 | 0.0015 | 5/19 | k=1: 49.992 Hz, -97.4 dB | -100.4 | 0.3 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0037 | 26 | k=26·f1-4·f2: 1996.543 Hz, -119.8 dB | -114.0 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 3 | 4401.8999 | 0.0007 | 2/5 | k=1: 4401.900 Hz, -97.3 dB | -100.3 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.5 dB | -100.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -83.9 | 7.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.6 | 62.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0008 | 10/10 | k=1: 2320.545 Hz, -114.1 dB | -109.9 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9920 | 0.0024 | 4/19 | k=1: 49.991 Hz, -97.4 dB | -100.1 | 0.2 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0026 | 6 | k=-1·f1+3·f2: 17000.129 Hz, -121.0 dB | -117.9 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 4 | 4401.9002 | 0.0005 | 2/5 | k=1: 4401.900 Hz, -93.8 dB | -96.8 | 0.4 % |
| stärkste übrige Linie (6602.85 Hz) | Kanal 4 | 6602.8503 | 0.0000 | 1/3 | k=1: 6602.850 Hz, -98.4 dB | -101.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 58.1 | usb1k·1 |
| 1999.735 | -81.5 | 51.4 | usb1k·2 |
| 2999.603 | -82.8 | 51.1 | usb1k·3 |
| 6000.000 | -83.8 | 52.2 | fs8·1 |
| 12000.000 | -85.5 | 52.3 | fs8·2 |
| 3999.471 | -86.8 | 48.2 | usb1k·4 |
| 18000.000 | -87.9 | 50.3 | fs8·3 |
| 9998.676 | -88.3 | 48.7 | usb1k·10 |
| 4999.339 | -89.5 | 45.7 | usb1k·5 |
| 15997.882 | -90.4 | 47.9 | usb1k·16 |
| 4401.900 | -91.8 | 43.0 | other1·1 |
| 6999.074 | -90.8 | 45.7 | usb1k·7 |
| 8998.809 | -91.2 | 46.2 | usb1k·9 |
| 16997.750 | -93.2 | 45.1 | usb1k·17 |
| 18997.486 | -93.6 | 45.1 | usb1k·19 |
| 20997.221 | -94.7 | 43.6 | usb1k·21 |
| 5999.206 | -94.4 | 41.5 | usb1k·6 |
| 7998.942 | -94.4 | 41.6 | usb1k·8 |
| 11998.412 | -95.8 | 41.9 | usb1k·12 |
| 2200.950 | -96.5 | 37.2 | other2·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.5 | 58.2 | usb1k·1 |
| 1999.735 | -83.4 | 50.8 | usb1k·2 |
| 2999.603 | -83.6 | 51.6 | usb1k·3 |
| 6000.000 | -83.8 | 53.5 | fs8·1 |
| 12000.000 | -85.8 | 53.1 | fs8·2 |
| 3999.471 | -87.3 | 49.0 | usb1k·4 |
| 18000.000 | -88.0 | 51.5 | fs8·3 |
| 9998.676 | -88.4 | 50.4 | usb1k·10 |
| 15997.882 | -90.9 | 48.7 | usb1k·16 |
| 4999.339 | -90.6 | 45.6 | usb1k·5 |
| 6999.074 | -91.7 | 46.2 | usb1k·7 |
| 16997.750 | -93.5 | 45.8 | usb1k·17 |
| 4401.900 | -93.6 | 42.6 | other1·1 |
| 18997.486 | -93.6 | 46.4 | usb1k·19 |
| 8998.809 | -92.1 | 46.6 | usb1k·9 |
| 20997.221 | -95.5 | 44.4 | usb1k·21 |
| 5999.206 | -96.1 | 41.2 | usb1k·6 |
| 11998.412 | -96.4 | 42.5 | usb1k·12 |
| 7998.942 | -95.6 | 41.8 | usb1k·8 |
| 12998.279 | -97.0 | 41.9 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 62.5 | usb1k·1 |
| 1999.735 | -83.0 | 56.1 | usb1k·2 |
| 2999.603 | -84.1 | 55.8 | usb1k·3 |
| 6000.000 | -84.4 | 57.1 | fs8·1 |
| 12000.000 | -86.7 | 55.4 | fs8·2 |
| 3999.471 | -87.6 | 52.9 | usb1k·4 |
| 18000.000 | -88.3 | 53.9 | fs8·3 |
| 9998.676 | -88.9 | 53.1 | usb1k·10 |
| 15997.882 | -90.9 | 51.1 | usb1k·16 |
| 4999.339 | -90.7 | 49.7 | usb1k·5 |
| 6999.074 | -92.1 | 49.7 | usb1k·7 |
| 8998.809 | -92.0 | 50.6 | usb1k·9 |
| 18997.485 | -93.8 | 48.2 | usb1k·19 |
| 16997.750 | -93.9 | 48.4 | usb1k·17 |
| 20997.221 | -95.5 | 46.6 | usb1k·21 |
| 11998.412 | -96.4 | 45.9 | usb1k·12 |
| 5999.206 | -96.4 | 45.0 | usb1k·6 |
| 4401.900 | -97.3 | 43.7 | other1·1 |
| 7998.942 | -95.5 | 45.7 | usb1k·8 |
| 12998.279 | -97.3 | 45.0 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 59.2 | usb1k·1 |
| 1999.735 | -81.8 | 52.2 | usb1k·2 |
| 2999.603 | -82.8 | 51.8 | usb1k·3 |
| 6000.000 | -83.9 | 52.8 | fs8·1 |
| 12000.000 | -86.0 | 52.1 | fs8·2 |
| 3999.471 | -86.9 | 48.7 | usb1k·4 |
| 18000.000 | -88.2 | 50.2 | fs8·3 |
| 9998.676 | -88.4 | 49.5 | usb1k·10 |
| 4999.339 | -89.7 | 46.0 | usb1k·5 |
| 15997.882 | -90.5 | 48.0 | usb1k·16 |
| 6999.074 | -91.0 | 46.1 | usb1k·7 |
| 8998.809 | -91.5 | 46.2 | usb1k·9 |
| 16997.750 | -93.3 | 44.8 | usb1k·17 |
| 4401.900 | -93.8 | 41.5 | other1·1 |
| 18997.485 | -93.9 | 45.3 | usb1k·19 |
| 5999.206 | -94.4 | 42.3 | usb1k·6 |
| 20997.221 | -95.0 | 44.1 | usb1k·21 |
| 7998.942 | -94.0 | 43.1 | usb1k·8 |
| 11998.412 | -95.9 | 42.2 | usb1k·12 |
| 12998.279 | -97.1 | 41.3 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.01 | 0.08 |
| usb1k | Kanal 1 | 11/11 | 0.18 | 0.21 | 0.07 |
| led | Kanal 1 | 11/11 | 1.72 | 2.17 | 0.68 |
| mains50 | Kanal 1 | 11/11 | 288.83 | -680.27 | 1.08 |
| other1 | Kanal 1 | 11/11 | 1.57 | 0.30 | 0.10 |
| other2 | Kanal 1 | 11/11 | 0.32 | -0.31 | 0.17 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.01 | 0.08 |
| usb1k | Kanal 2 | 11/11 | 0.21 | 0.25 | 0.07 |
| led | Kanal 2 | 11/11 | 0.13 | 0.21 | 0.43 |
| mains50 | Kanal 2 | 11/11 | 192.92 | -508.25 | 0.97 |
| other1 | Kanal 2 | 11/11 | 1.67 | 0.07 | 0.15 |
| other2 | Kanal 2 | 11/11 | 0.36 | -0.21 | 0.19 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.07 |
| usb1k | Kanal 3 | 11/11 | 0.17 | 0.12 | 0.06 |
| led | Kanal 3 | 11/11 | 0.95 | 0.41 | 0.32 |
| mains50 | Kanal 3 | 11/11 | 163.68 | -512.88 | 0.56 |
| other1 | Kanal 3 | 11/11 | 1.42 | -0.76 | 0.10 |
| other2 | Kanal 3 | 11/11 | 0.07 | 0.11 | 0.13 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.03 | 0.08 |
| usb1k | Kanal 4 | 11/11 | 0.21 | 0.21 | 0.07 |
| led | Kanal 4 | 11/11 | 1.53 | 1.02 | 0.45 |
| mains50 | Kanal 4 | 11/11 | 195.13 | -460.37 | 0.97 |
| other1 | Kanal 4 | 11/11 | 1.64 | -0.37 | 0.17 |
| other2 | Kanal 4 | 11/11 | 0.22 | -0.20 | 0.15 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.05 | 0.16 s (6.40 Hz) | 25.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 36.9 |
| Kanal 2 | breitbandig | 1.04 | 0.16 s (6.40 Hz) | 26.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 39.5 |
| Kanal 3 | breitbandig | 0.65 | 0.31 s (3.18 Hz) | 28.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 43.1 |
| Kanal 4 | breitbandig | 0.87 | 0.16 s (6.40 Hz) | 27.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 38.7 |

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
| Kanal 2 | 0.97 | 1.00 | 0.92 | 0.96 |
| Kanal 3 | 0.93 | 0.92 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B5c-fx3l-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.2 | -72.0 | -0.2 | 66 % | 68 % |
| Kanal 2 | -73.4 | -73.0 | -0.4 | 68 % | 71 % |
| Kanal 3 | -74.5 | -74.4 | -0.0 | 82 % | 83 % |
| Kanal 4 | -72.5 | -72.0 | -0.6 | 70 % | 75 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-fx4b-r1_psd.png)

### Kammprofile

![Kammprofile](B6b-fx4b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-fx4b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:07:35. Stream-Meldungen: 0. owl_read: out/owl_read/B6b-fx4b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
