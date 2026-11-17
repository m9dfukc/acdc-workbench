# Report B6b-fx4b-end-r1: B6b-fx4b-end-r1 – acdc1 fx4b-open-inputs-6-end, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-6-Sitzung: fx4b am Ende (nach der fx3l-Kontrolle), Eingänge offen, rohe ADC-Daten |
| gain | gvar |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch, per Program Change), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261117_acdc1_fx4b-open-inputs-6-end-r1_gvar_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-fx4b-end-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B6b-fx3l-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -69.8 | -73.9 | -71.9 | -72.6 | -85.3 | -72.2 | -92.9 | -71.9 | 66 % | -76.6 | 4.7 |
| Kanal 2 | -7.3 | -71.2 | -75.8 | -73.0 | -73.7 | -87.3 | -73.3 | -93.4 | -73.0 | 69 % | -78.1 | 5.1 |
| Kanal 3 | -5.4 | -72.8 | -77.9 | -74.4 | -74.9 | -91.6 | -74.6 | -95.5 | -74.4 | 82 % | -81.8 | 7.4 |
| Kanal 4 | -6.4 | -70.7 | -76.6 | -72.0 | -72.5 | -87.8 | -72.2 | -95.2 | -72.0 | 73 % | -77.7 | 5.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.7 dB | -83.1 | 7.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.3 | 58.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0013 | 10/10 | k=1: 2320.545 Hz, -113.5 dB | -109.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9820 | 0.0032 | 4/19 | k=1: 49.981 Hz, -96.7 dB | -99.1 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0026 | 7 | k=3·f1+2·f2: 14999.601 Hz, -121.1 dB | -116.9 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 1 | 4401.9003 | 0.0003 | 2/5 | k=1: 4401.900 Hz, -91.8 dB | -94.8 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 1 | 2200.9501 | 0.0001 | 2/10 | k=1: 2200.950 Hz, -96.6 dB | -97.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.0 dB | -83.3 | 9.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.3 | 59.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=9: 20884.904 Hz, -114.0 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9821 | 0.0023 | 4/19 | k=1: 49.981 Hz, -97.5 dB | -99.9 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0047 | 11 | k=27·f1-4·f2: 2996.416 Hz, -118.9 dB | -114.9 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 2 | 4401.9002 | 0.0001 | 2/5 | k=1: 4401.900 Hz, -93.5 dB | -96.5 | 0.4 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.0 dB | -96.3 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.7 dB | -83.9 | 11.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -75.9 | 70.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0004 | 10/10 | k=1: 2320.545 Hz, -114.3 dB | -109.6 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9821 | 0.0027 | 4/19 | k=1: 49.981 Hz, -98.2 dB | -100.7 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0038 | 31 | k=28·f1-4·f2: 3996.281 Hz, -120.0 dB | -112.4 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 3 | 4401.9003 | 0.0004 | 2/5 | k=1: 4401.900 Hz, -97.3 dB | -100.3 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.5 dB | -97.3 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.4 | 7.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.9 | 65.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0013 | 10/10 | k=1: 2320.544 Hz, -113.4 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9820 | 0.0027 | 4/19 | k=1: 49.981 Hz, -98.2 dB | -100.6 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0082 | 12 | k=25·f1-4·f2: 996.683 Hz, -111.1 dB | -110.7 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 4 | 4401.9001 | 0.0000 | 2/5 | k=1: 4401.900 Hz, -93.5 dB | -96.4 | 0.4 % |
| stärkste übrige Linie (6602.85 Hz) | Kanal 4 | 6602.8504 | 0.0000 | 1/3 | k=1: 6602.850 Hz, -98.5 dB | -101.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 55.7 | usb1k·1 |
| 1999.735 | -80.8 | 48.9 | usb1k·2 |
| 2999.603 | -82.4 | 51.4 | usb1k·3 |
| 12000.000 | -83.7 | 54.1 | fs8·2 |
| 6000.000 | -84.5 | 51.0 | fs8·1 |
| 18000.000 | -87.1 | 51.1 | fs8·3 |
| 3999.471 | -87.1 | 44.9 | usb1k·4 |
| 9998.677 | -88.3 | 48.7 | usb1k·10 |
| 4999.338 | -89.6 | 45.1 | usb1k·5 |
| 15997.883 | -90.2 | 47.3 | usb1k·16 |
| 6999.074 | -90.5 | 46.1 | usb1k·7 |
| 4401.900 | -91.8 | 42.1 | other1·1 |
| 8998.809 | -90.5 | 46.3 | usb1k·9 |
| 16997.751 | -92.8 | 45.8 | usb1k·17 |
| 18997.486 | -93.9 | 44.6 | usb1k·19 |
| 5999.206 | -94.0 | 41.6 | usb1k·6 |
| 20997.222 | -94.7 | 44.0 | usb1k·21 |
| 7998.942 | -94.2 | 40.7 | usb1k·8 |
| 11998.412 | -95.9 | 41.9 | usb1k·12 |
| 2200.950 | -96.6 | 34.8 | other2·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 56.3 | usb1k·1 |
| 1999.735 | -82.3 | 49.4 | usb1k·2 |
| 2999.603 | -83.1 | 52.1 | usb1k·3 |
| 12000.000 | -84.0 | 54.9 | fs8·2 |
| 6000.000 | -84.5 | 52.3 | fs8·1 |
| 18000.000 | -87.1 | 52.2 | fs8·3 |
| 3999.471 | -87.6 | 46.0 | usb1k·4 |
| 9998.676 | -88.4 | 50.1 | usb1k·10 |
| 15997.883 | -90.7 | 47.3 | usb1k·16 |
| 4999.338 | -90.7 | 45.5 | usb1k·5 |
| 6999.074 | -91.3 | 46.3 | usb1k·7 |
| 8998.809 | -91.4 | 46.7 | usb1k·9 |
| 16997.751 | -93.2 | 46.3 | usb1k·17 |
| 4401.900 | -93.5 | 41.9 | other1·1 |
| 18997.486 | -93.9 | 45.6 | usb1k·19 |
| 20997.222 | -95.4 | 44.2 | usb1k·21 |
| 5999.205 | -95.3 | 41.5 | usb1k·6 |
| 11998.412 | -96.5 | 42.3 | usb1k·12 |
| 12998.279 | -96.7 | 42.5 | usb1k·13 |
| 7998.942 | -95.5 | 40.7 | usb1k·8 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 60.8 | usb1k·1 |
| 1999.735 | -82.4 | 54.0 | usb1k·2 |
| 2999.603 | -84.0 | 55.8 | usb1k·3 |
| 12000.000 | -84.7 | 57.7 | fs8·2 |
| 6000.000 | -85.2 | 56.2 | fs8·1 |
| 18000.000 | -87.5 | 54.6 | fs8·3 |
| 3999.471 | -88.0 | 49.8 | usb1k·4 |
| 9998.677 | -89.0 | 53.3 | usb1k·10 |
| 15997.883 | -90.8 | 50.8 | usb1k·16 |
| 4999.338 | -90.9 | 49.5 | usb1k·5 |
| 8998.809 | -91.4 | 49.9 | usb1k·9 |
| 6999.074 | -91.9 | 50.1 | usb1k·7 |
| 16997.751 | -93.9 | 48.3 | usb1k·17 |
| 18997.486 | -94.0 | 48.0 | usb1k·19 |
| 20997.222 | -95.6 | 46.3 | usb1k·21 |
| 5999.206 | -96.1 | 45.3 | usb1k·6 |
| 11998.412 | -96.5 | 45.9 | usb1k·12 |
| 12998.280 | -96.9 | 45.7 | usb1k·13 |
| 4401.900 | -97.3 | 42.9 | other1·1 |
| 7998.942 | -95.8 | 44.9 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 57.1 | usb1k·1 |
| 1999.735 | -81.0 | 50.7 | usb1k·2 |
| 2999.603 | -82.2 | 52.0 | usb1k·3 |
| 12000.000 | -84.2 | 54.0 | fs8·2 |
| 6000.000 | -84.4 | 51.6 | fs8·1 |
| 18000.000 | -87.5 | 51.0 | fs8·3 |
| 3999.471 | -87.1 | 46.3 | usb1k·4 |
| 9998.676 | -88.3 | 49.2 | usb1k·10 |
| 4999.339 | -89.6 | 46.1 | usb1k·5 |
| 15997.883 | -90.6 | 47.3 | usb1k·16 |
| 6999.073 | -90.9 | 46.1 | usb1k·7 |
| 8998.809 | -90.9 | 46.9 | usb1k·9 |
| 16997.750 | -92.7 | 45.4 | usb1k·17 |
| 4401.900 | -93.5 | 41.5 | other1·1 |
| 5999.206 | -93.3 | 42.7 | usb1k·6 |
| 18997.486 | -94.2 | 44.3 | usb1k·19 |
| 7998.942 | -93.4 | 42.2 | usb1k·8 |
| 20997.222 | -95.0 | 43.5 | usb1k·21 |
| 11998.412 | -96.1 | 42.0 | usb1k·12 |
| 12998.279 | -96.3 | 41.5 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.21 | 0.01 | 0.05 |
| led | Kanal 1 | 11/11 | 1.85 | 3.32 | 0.39 |
| mains50 | Kanal 1 | 11/11 | 476.34 | 698.35 | 0.98 |
| other1 | Kanal 1 | 11/11 | 1.14 | -0.05 | 0.14 |
| other2 | Kanal 1 | 11/11 | 0.21 | 0.14 | 0.17 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.24 | 0.07 | 0.07 |
| led | Kanal 2 | 11/11 | 0.31 | 0.43 | 0.31 |
| mains50 | Kanal 2 | 11/11 | 448.45 | 854.27 | 0.80 |
| other1 | Kanal 2 | 11/11 | 1.24 | -0.23 | 0.14 |
| other2 | Kanal 2 | 11/11 | 1.54 | -3.91 | 0.20 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.18 | 0.09 | 0.03 |
| led | Kanal 3 | 11/11 | 0.83 | 1.38 | 0.24 |
| mains50 | Kanal 3 | 11/11 | 519.25 | 1115.84 | 0.69 |
| other1 | Kanal 3 | 11/11 | 0.98 | 1.35 | 0.15 |
| other2 | Kanal 3 | 11/11 | 0.75 | -0.41 | 0.12 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.21 | 0.12 | 0.07 |
| led | Kanal 4 | 11/11 | 1.84 | 2.87 | 0.45 |
| mains50 | Kanal 4 | 11/11 | 323.93 | 860.90 | 0.81 |
| other1 | Kanal 4 | 11/11 | 1.13 | 0.19 | 0.15 |
| other2 | Kanal 4 | 11/11 | 0.31 | 0.05 | 0.21 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.74 | 0.31 s (3.18 Hz) | 29.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.99 | 7.50 s (0.13 Hz) | 34.1 |
| Kanal 2 | breitbandig | 1.59 | 0.31 s (3.18 Hz) | 30.1 |
| Kanal 2 | 999.9 Hz ± 10 | 1.00 | 7.50 s (0.13 Hz) | 36.7 |
| Kanal 3 | breitbandig | 1.31 | 0.31 s (3.18 Hz) | 31.6 |
| Kanal 3 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 41.5 |
| Kanal 4 | breitbandig | 1.21 | 0.31 s (3.18 Hz) | 29.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.98 | 7.50 s (0.13 Hz) | 35.4 |

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

## Vergleich mit Referenz B6b-fx3l-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.9 | -72.0 | +0.1 | 66 % | 66 % |
| Kanal 2 | -73.0 | -73.1 | +0.1 | 69 % | 68 % |
| Kanal 3 | -74.4 | -74.5 | +0.1 | 82 % | 82 % |
| Kanal 4 | -72.0 | -72.1 | +0.1 | 73 % | 72 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-fx4b-end-r1_psd.png)

### Kammprofile

![Kammprofile](B6b-fx4b-end-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-fx4b-end-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:16:48. Stream-Meldungen: 0. owl_read: out/owl_read/B6b-fx4b-end-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
