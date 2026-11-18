# Report B7-fx4b-a-r2: B7-fx4b-a-r2 – acdc1 fx4b-open-inputs-7a, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-7-Sitzung: fx4b-Kontrolle am Anfang, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx4b-open-inputs-7a-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx4b-a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.9 | -81.1 | -72.5 | -73.3 | -85.7 | -72.8 | -94.5 | -72.5 | 64 % | -77.0 | 4.5 |
| Kanal 2 | -7.5 | -72.9 | -82.4 | -73.4 | -74.2 | -87.8 | -73.7 | -94.8 | -73.5 | 68 % | -78.5 | 5.0 |
| Kanal 3 | -5.7 | -74.2 | -86.6 | -74.4 | -75.0 | -92.2 | -74.6 | -95.6 | -74.5 | 83 % | -82.0 | 7.6 |
| Kanal 4 | -6.5 | -72.2 | -82.9 | -72.6 | -73.2 | -88.2 | -72.9 | -95.0 | -72.6 | 72 % | -78.2 | 5.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.9 dB | -82.9 | 9.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.9 dB | -75.1 | 54.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.547 Hz, -113.4 dB | -109.3 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0064 | 0.0006 | 3/19 | k=1: 50.005 Hz, -97.9 dB | -101.0 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0020 | 7 | k=3·f1+2·f2: 14999.604 Hz, -121.2 dB | -116.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.6 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.9 dB | -98.8 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.1 dB | -83.0 | 11.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -75.9 | 57.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0011 | 10/10 | k=9: 20884.904 Hz, -113.1 dB | -107.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0062 | 0.0063 | 4/19 | k=1: 50.006 Hz, -98.3 dB | -101.2 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0013 | 10 | k=5·f1+2·f2: 16999.338 Hz, -120.3 dB | -115.7 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -99.1 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -96.8 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.7 dB | -83.5 | 12.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.0 | 70.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.545 Hz, -113.3 dB | -109.4 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0063 | 0.0035 | 6/19 | k=1: 50.006 Hz, -98.9 dB | -101.6 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0016 | 35 | k=2·f1+2·f2: 13999.735 Hz, -120.7 dB | -111.8 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.7 dB | -100.0 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.9 dB | -97.5 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.1 | 8.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.4 dB | -74.6 | 63.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0008 | 10/10 | k=1: 2320.547 Hz, -112.6 dB | -108.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0063 | 0.0062 | 4/19 | k=1: 50.006 Hz, -98.7 dB | -101.5 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0020 | 10 | k=-1·f1+3·f2: 17000.132 Hz, -118.5 dB | -114.2 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.7 dB | -99.3 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -97.0 | 0.4 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.9 | 57.7 | usb1k·1 |
| 1999.735 | -81.8 | 51.1 | usb1k·2 |
| 2999.603 | -83.3 | 50.9 | usb1k·3 |
| 12000.000 | -83.9 | 54.1 | fs8·2 |
| 6000.000 | -84.2 | 51.7 | fs8·1 |
| 18000.000 | -86.1 | 52.0 | fs8·3 |
| 3999.471 | -87.0 | 47.1 | usb1k·4 |
| 9998.676 | -88.5 | 49.0 | usb1k·10 |
| 4999.338 | -89.5 | 45.7 | usb1k·5 |
| 15997.882 | -90.5 | 47.8 | usb1k·16 |
| 6999.074 | -90.7 | 45.9 | usb1k·7 |
| 8998.809 | -90.9 | 45.5 | usb1k·9 |
| 16997.750 | -93.6 | 44.6 | usb1k·17 |
| 18997.485 | -94.0 | 44.3 | usb1k·19 |
| 20997.220 | -94.7 | 44.4 | usb1k·21 |
| 5999.206 | -94.3 | 41.6 | usb1k·6 |
| 12998.279 | -97.1 | 40.8 | usb1k·13 |
| 11998.411 | -97.0 | 40.9 | usb1k·12 |
| 7998.941 | -96.3 | 40.1 | usb1k·8 |
| 2000.000 | -97.8 | 35.1 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 58.0 | usb1k·1 |
| 1999.735 | -82.9 | 51.5 | usb1k·2 |
| 2999.603 | -83.9 | 51.9 | usb1k·3 |
| 12000.000 | -84.1 | 55.2 | fs8·2 |
| 6000.000 | -84.3 | 53.2 | fs8·1 |
| 18000.000 | -86.1 | 53.4 | fs8·3 |
| 3999.471 | -87.2 | 48.8 | usb1k·4 |
| 9998.676 | -88.4 | 50.6 | usb1k·10 |
| 4999.338 | -90.1 | 46.8 | usb1k·5 |
| 15997.882 | -90.7 | 48.7 | usb1k·16 |
| 6999.074 | -91.1 | 46.8 | usb1k·7 |
| 8998.809 | -91.4 | 46.5 | usb1k·9 |
| 16997.750 | -93.7 | 45.6 | usb1k·17 |
| 18997.485 | -93.8 | 45.7 | usb1k·19 |
| 20997.221 | -95.1 | 44.8 | usb1k·21 |
| 5999.206 | -95.3 | 42.1 | usb1k·6 |
| 12998.279 | -97.2 | 42.3 | usb1k·13 |
| 11998.411 | -97.1 | 42.1 | usb1k·12 |
| 17997.617 | -98.0 | 41.3 | usb1k·18 |
| 3000.000 | -98.4 | 37.4 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 63.5 | usb1k·1 |
| 1999.735 | -83.3 | 55.8 | usb1k·2 |
| 2999.603 | -84.0 | 55.9 | usb1k·3 |
| 6000.000 | -84.7 | 57.0 | fs8·1 |
| 12000.000 | -84.9 | 57.3 | fs8·2 |
| 18000.000 | -86.5 | 55.6 | fs8·3 |
| 3999.471 | -87.5 | 52.8 | usb1k·4 |
| 9998.676 | -88.7 | 53.5 | usb1k·10 |
| 15997.882 | -91.1 | 51.2 | usb1k·16 |
| 4999.338 | -90.9 | 50.1 | usb1k·5 |
| 6999.074 | -91.4 | 50.2 | usb1k·7 |
| 8998.809 | -92.1 | 49.9 | usb1k·9 |
| 16997.750 | -93.8 | 48.4 | usb1k·17 |
| 18997.485 | -94.2 | 47.7 | usb1k·19 |
| 20997.220 | -95.5 | 46.4 | usb1k·21 |
| 5999.206 | -95.8 | 45.9 | usb1k·6 |
| 11998.411 | -97.2 | 45.0 | usb1k·12 |
| 7998.941 | -96.4 | 45.2 | usb1k·8 |
| 12998.279 | -97.7 | 44.8 | usb1k·13 |
| 17997.617 | -98.4 | 43.6 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.4 | 59.4 | usb1k·1 |
| 1999.735 | -81.1 | 53.5 | usb1k·2 |
| 2999.603 | -83.0 | 52.4 | usb1k·3 |
| 12000.000 | -84.2 | 54.0 | fs8·2 |
| 6000.000 | -84.4 | 52.9 | fs8·1 |
| 18000.000 | -86.4 | 52.4 | fs8·3 |
| 3999.471 | -86.9 | 48.7 | usb1k·4 |
| 4999.338 | -88.8 | 47.8 | usb1k·5 |
| 9998.676 | -88.5 | 50.0 | usb1k·10 |
| 15997.882 | -90.2 | 48.5 | usb1k·16 |
| 6999.074 | -90.4 | 47.2 | usb1k·7 |
| 8998.809 | -90.4 | 47.1 | usb1k·9 |
| 16997.750 | -93.5 | 45.3 | usb1k·17 |
| 5999.206 | -93.1 | 44.2 | usb1k·6 |
| 18997.485 | -94.0 | 44.5 | usb1k·19 |
| 20997.221 | -94.5 | 44.5 | usb1k·21 |
| 7998.941 | -95.1 | 42.3 | usb1k·8 |
| 11998.411 | -96.3 | 41.8 | usb1k·12 |
| 12998.279 | -97.0 | 41.5 | usb1k·13 |
| 13998.147 | -97.3 | 41.0 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.14 | -0.13 | 0.02 |
| led | Kanal 1 | 11/11 | 1.25 | 1.59 | 0.79 |
| mains50 | Kanal 1 | 11/11 | 240.40 | 616.27 | 1.29 |
| other1 | Kanal 1 | 11/11 | 1.36 | -2.00 | 0.05 |
| other2 | Kanal 1 | 11/11 | 0.15 | 0.26 | 0.11 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.15 | -0.11 | 0.03 |
| led | Kanal 2 | 11/11 | 0.41 | 0.23 | 0.50 |
| mains50 | Kanal 2 | 11/11 | 215.71 | 648.35 | 1.13 |
| other1 | Kanal 2 | 11/11 | 0.17 | 0.27 | 0.10 |
| other2 | Kanal 2 | 11/11 | 1.77 | -4.16 | 0.06 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.10 | -0.10 | 0.01 |
| led | Kanal 3 | 11/11 | 1.11 | 0.14 | 0.38 |
| mains50 | Kanal 3 | 11/11 | 217.60 | 641.02 | 0.71 |
| other1 | Kanal 3 | 11/11 | 0.16 | 0.05 | 0.07 |
| other2 | Kanal 3 | 11/11 | 0.29 | 0.03 | 0.05 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.09 | -0.09 | 0.03 |
| led | Kanal 4 | 11/11 | 1.04 | 0.35 | 0.61 |
| mains50 | Kanal 4 | 11/11 | 233.29 | 734.79 | 1.14 |
| other1 | Kanal 4 | 11/11 | 0.19 | 0.51 | 0.12 |
| other2 | Kanal 4 | 11/11 | 2.14 | -4.37 | 0.05 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.73 | 0.31 s (3.20 Hz) | 20.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 37.5 |
| Kanal 2 | breitbandig | 0.68 | 0.31 s (3.18 Hz) | 20.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 39.7 |
| Kanal 3 | breitbandig | 0.41 | 7.50 s (0.13 Hz) | 26.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 44.5 |
| Kanal 4 | breitbandig | 0.55 | 0.31 s (3.18 Hz) | 20.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.7 |

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
| Kanal 1 | 1.00 | 0.96 | 0.92 | 0.94 |
| Kanal 2 | 0.96 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.92 | 0.93 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx4b-a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx4b-a-r2_psd.png)

### Kammprofile

![Kammprofile](B7-fx4b-a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx4b-a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 15:47:02. Stream-Meldungen: 0. owl_read: out/owl_read/B7-fx4b-a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
