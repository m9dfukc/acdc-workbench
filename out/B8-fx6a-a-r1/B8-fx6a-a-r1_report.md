# Report B8-fx6a-a-r1: B8-fx6a-a-r1 – acdc1 fx6a-open-inputs-8a, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 8 v22.4.r-fx6a, LED-Modus normal, ins Case geschraubt |
| test | Build-8-Sitzung: fx6a (fx5a + Patch 17) am Anfang, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx6a-open-inputs-8a-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B8-fx6a-a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.7 | -72.1 | -83.6 | -72.4 | -73.5 | -86.3 | -72.8 | -90.1 | -72.5 | 55 % | -76.0 | 3.5 |
| Kanal 2 | -7.1 | -72.8 | -85.0 | -73.1 | -73.9 | -88.3 | -73.4 | -95.4 | -73.1 | 64 % | -77.5 | 4.4 |
| Kanal 3 | -5.4 | -74.5 | -89.7 | -74.7 | -75.4 | -93.0 | -74.9 | -96.1 | -74.7 | 75 % | -80.8 | 6.1 |
| Kanal 4 | -6.2 | -71.6 | -85.0 | -71.8 | -72.5 | -88.1 | -72.1 | -95.7 | -71.8 | 66 % | -76.5 | 4.7 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -82.6 dB | -82.7 | 9.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -75.9 | 45.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0030 | 10/10 | k=1: 2320.541 Hz, -115.4 dB | -112.1 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9385 | 0.0033 | 2/19 | k=2: 99.881 Hz, -109.2 dB | -111.5 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.5 dB | -99.6 | 0.2 % |
| stärkste übrige Linie (500.00 Hz) | Kanal 1 | 500.0001 | 0.0006 | 40/47 | k=1: 500.001 Hz, -100.8 dB | -90.6 | 1.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -82.7 dB | -82.8 | 10.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -75.9 | 52.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0019 | 10/10 | k=8: 18564.358 Hz, -114.3 dB | -110.0 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9384 | 0.0026 | 2/19 | k=2: 99.880 Hz, -108.8 dB | -111.1 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0005 | 1 | k=-3·f1+4·f2: 21000.397 Hz, -121.4 dB | -124.6 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.9 dB | -99.9 | 0.2 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 2 | 2500.0003 | 0.0003 | 8/9 | k=1: 2500.000 Hz, -100.9 dB | -97.3 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -83.3 | 13.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.7 dB | -76.8 | 61.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5449 | 0.0013 | 10/10 | k=1: 2320.543 Hz, -115.7 dB | -112.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9381 | 0.0026 | 3/19 | k=2: 99.878 Hz, -112.5 dB | -113.1 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0018 | 4 | k=8·f1+2·f2: 19998.942 Hz, -123.1 dB | -120.7 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -101.3 dB | -100.8 | 0.2 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 3 | 2500.0003 | 0.0002 | 8/9 | k=1: 2500.000 Hz, -101.6 dB | -97.9 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.0 dB | -83.0 | 7.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -74.1 | 58.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0019 | 10/10 | k=1: 2320.543 Hz, -115.4 dB | -111.9 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9358 | 0.0078 | 3/19 | k=2: 99.878 Hz, -104.9 dB | -107.4 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0015 | 4 | k=1·f1+2·f2: 12999.868 Hz, -117.2 dB | -115.9 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.1 dB | -100.0 | 0.1 % |
| stärkste übrige Linie (2500.00 Hz) | Kanal 4 | 2500.0003 | 0.0004 | 8/9 | k=1: 2500.000 Hz, -101.3 dB | -97.6 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 55.0 | usb1k·1 |
| 1999.735 | -82.0 | 50.4 | usb1k·2 |
| 6000.000 | -82.6 | 52.2 | fs8·1 |
| 12000.000 | -84.7 | 51.5 | fs8·2 |
| 2999.603 | -84.9 | 49.2 | usb1k·3 |
| 18000.000 | -87.1 | 48.9 | fs8·3 |
| 3999.471 | -87.8 | 45.6 | usb1k·4 |
| 4999.339 | -89.2 | 44.5 | usb1k·5 |
| 9998.676 | -88.8 | 46.5 | usb1k·10 |
| 15997.883 | -91.4 | 45.0 | usb1k·16 |
| 8998.809 | -90.7 | 44.6 | usb1k·9 |
| 18997.486 | -92.9 | 42.7 | usb1k·19 |
| 16997.750 | -93.8 | 42.1 | usb1k·17 |
| 6999.074 | -93.6 | 41.1 | usb1k·7 |
| 12998.280 | -95.7 | 40.1 | usb1k·13 |
| 5999.206 | -95.4 | 39.4 | usb1k·6 |
| 11998.412 | -95.9 | 40.3 | usb1k·12 |
| 20997.221 | -96.2 | 39.4 | usb1k·21 |
| 19997.354 | -97.9 | 37.7 | usb1k·20 |
| 14998.015 | -98.9 | 37.0 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 57.0 | usb1k·1 |
| 1999.735 | -82.4 | 51.6 | usb1k·2 |
| 6000.000 | -82.7 | 53.4 | fs8·1 |
| 2999.603 | -84.4 | 51.3 | usb1k·3 |
| 12000.000 | -85.0 | 52.8 | fs8·2 |
| 18000.000 | -87.0 | 50.6 | fs8·3 |
| 3999.471 | -87.5 | 47.5 | usb1k·4 |
| 9998.677 | -88.7 | 48.5 | usb1k·10 |
| 4999.339 | -89.8 | 45.5 | usb1k·5 |
| 15997.883 | -91.4 | 46.7 | usb1k·16 |
| 8998.809 | -91.3 | 45.5 | usb1k·9 |
| 18997.486 | -92.9 | 44.6 | usb1k·19 |
| 16997.750 | -93.6 | 44.2 | usb1k·17 |
| 6999.074 | -93.1 | 43.3 | usb1k·7 |
| 12998.280 | -96.0 | 41.8 | usb1k·13 |
| 11998.412 | -95.8 | 41.9 | usb1k·12 |
| 20997.221 | -96.4 | 41.3 | usb1k·21 |
| 5999.206 | -96.1 | 40.1 | usb1k·6 |
| 19997.354 | -98.0 | 39.6 | usb1k·20 |
| 17997.618 | -98.9 | 38.7 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.7 | 60.3 | usb1k·1 |
| 6000.000 | -83.2 | 56.7 | fs8·1 |
| 1999.735 | -83.9 | 54.6 | usb1k·2 |
| 2999.603 | -84.9 | 54.3 | usb1k·3 |
| 12000.000 | -85.7 | 55.0 | fs8·2 |
| 18000.000 | -87.4 | 53.0 | fs8·3 |
| 3999.471 | -88.0 | 50.9 | usb1k·4 |
| 9998.677 | -88.9 | 51.2 | usb1k·10 |
| 4999.339 | -90.7 | 48.3 | usb1k·5 |
| 15997.883 | -91.9 | 49.0 | usb1k·16 |
| 18997.486 | -93.2 | 46.5 | usb1k·19 |
| 16997.750 | -93.7 | 46.1 | usb1k·17 |
| 8998.809 | -92.5 | 47.3 | usb1k·9 |
| 6999.074 | -93.5 | 46.0 | usb1k·7 |
| 11998.412 | -96.1 | 44.5 | usb1k·12 |
| 12998.280 | -96.5 | 43.9 | usb1k·13 |
| 20997.221 | -97.3 | 42.4 | usb1k·21 |
| 5999.206 | -97.1 | 42.8 | usb1k·6 |
| 19997.354 | -98.5 | 41.3 | usb1k·20 |
| 17997.618 | -99.0 | 41.5 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 58.8 | usb1k·1 |
| 1999.735 | -80.2 | 53.0 | usb1k·2 |
| 6000.000 | -83.0 | 52.3 | fs8·1 |
| 2999.603 | -82.9 | 51.9 | usb1k·3 |
| 12000.000 | -85.2 | 51.1 | fs8·2 |
| 18000.000 | -87.0 | 49.0 | fs8·3 |
| 3999.471 | -86.7 | 47.5 | usb1k·4 |
| 4999.339 | -88.8 | 45.3 | usb1k·5 |
| 9998.677 | -89.0 | 47.2 | usb1k·10 |
| 15997.883 | -90.7 | 45.2 | usb1k·16 |
| 8998.809 | -90.5 | 44.6 | usb1k·9 |
| 6999.074 | -91.5 | 43.4 | usb1k·7 |
| 16997.751 | -92.9 | 43.4 | usb1k·17 |
| 18997.486 | -93.1 | 42.9 | usb1k·19 |
| 5999.206 | -93.7 | 41.6 | usb1k·6 |
| 11998.412 | -94.8 | 41.4 | usb1k·12 |
| 7998.941 | -94.7 | 40.5 | usb1k·8 |
| 20997.221 | -95.8 | 40.2 | usb1k·21 |
| 12998.280 | -96.9 | 39.5 | usb1k·13 |
| 13998.147 | -97.5 | 38.4 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.02 | 0.07 |
| usb1k | Kanal 1 | 11/11 | 0.17 | -0.12 | 0.03 |
| led | Kanal 1 | 11/11 | 1.91 | -0.58 | 0.65 |
| mains50 | Kanal 1 | 10/11 | 824.02 | -297.26 | 1.19 |
| other1 | Kanal 1 | 11/11 | 0.35 | -0.32 | 0.31 |
| other2 | Kanal 1 | 11/11 | 40.81 | 19.19 | 0.03 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.08 |
| usb1k | Kanal 2 | 11/11 | 0.14 | -0.05 | 0.02 |
| led | Kanal 2 | 11/11 | 0.50 | -0.52 | 0.55 |
| mains50 | Kanal 2 | 11/11 | 642.41 | -626.90 | 1.19 |
| other1 | Kanal 2 | 11/11 | 0.28 | -0.02 | 0.29 |
| other2 | Kanal 2 | 11/11 | 0.30 | -0.09 | 0.16 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.03 | 0.08 |
| usb1k | Kanal 3 | 11/11 | 0.15 | 0.03 | 0.02 |
| led | Kanal 3 | 11/11 | 1.16 | -0.91 | 0.44 |
| mains50 | Kanal 3 | 11/11 | 255.92 | -250.89 | 0.62 |
| other1 | Kanal 3 | 11/11 | 0.14 | 0.02 | 0.17 |
| other2 | Kanal 3 | 11/11 | 0.27 | -0.22 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.00 | 0.09 |
| usb1k | Kanal 4 | 11/11 | 0.14 | -0.03 | 0.02 |
| led | Kanal 4 | 11/11 | 1.68 | -2.65 | 0.65 |
| mains50 | Kanal 4 | 11/11 | 217.88 | 535.97 | 1.23 |
| other1 | Kanal 4 | 11/11 | 0.26 | -0.21 | 0.28 |
| other2 | Kanal 4 | 11/11 | 0.46 | -0.33 | 0.19 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.57 | 7.50 s (0.13 Hz) | 17.5 |
| Kanal 1 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 35.3 |
| Kanal 2 | breitbandig | 0.50 | 7.50 s (0.13 Hz) | 20.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 36.7 |
| Kanal 3 | breitbandig | 0.35 | 7.50 s (0.13 Hz) | 25.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 40.7 |
| Kanal 4 | breitbandig | 0.43 | 7.50 s (0.13 Hz) | 20.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 36.1 |

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
| Kanal 1 | 1.00 | 0.95 | 0.91 | 0.92 |
| Kanal 2 | 0.95 | 1.00 | 0.93 | 0.95 |
| Kanal 3 | 0.91 | 0.93 | 1.00 | 0.91 |
| Kanal 4 | 0.92 | 0.95 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B8-fx6a-a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B8-fx6a-a-r1_psd.png)

### Kammprofile

![Kammprofile](B8-fx6a-a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B8-fx6a-a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:00:05. Stream-Meldungen: 0. owl_read: out/owl_read/B8-fx6a-a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
