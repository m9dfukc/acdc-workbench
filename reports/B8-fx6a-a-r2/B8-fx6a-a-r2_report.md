# Report B8-fx6a-a-r2: B8-fx6a-a-r2 – acdc1 fx6a-open-inputs-8a, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 8 v22.4.r-fx6a, LED-Modus normal, ins Case geschraubt |
| test | Build-8-Sitzung: fx6a (fx5a + Patch 17) am Anfang, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx6a-open-inputs-8a-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B8-fx6a-a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.7 | -71.5 | -78.9 | -72.4 | -73.4 | -85.6 | -72.8 | -97.1 | -72.4 | 54 % | -75.8 | 3.3 |
| Kanal 2 | -7.1 | -72.2 | -79.7 | -73.1 | -73.9 | -87.8 | -73.4 | -97.2 | -73.1 | 63 % | -77.4 | 4.3 |
| Kanal 3 | -5.4 | -74.3 | -85.7 | -74.7 | -75.4 | -92.3 | -74.9 | -97.8 | -74.7 | 75 % | -80.6 | 5.9 |
| Kanal 4 | -6.2 | -71.1 | -79.3 | -71.8 | -72.5 | -87.7 | -72.1 | -97.5 | -71.8 | 66 % | -76.4 | 4.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -82.8 dB | -82.9 | 8.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -75.9 | 44.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0020 | 10/10 | k=1: 2320.547 Hz, -114.0 dB | -112.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9303 | 0.0037 | 2/19 | k=2: 99.856 Hz, -108.0 dB | -109.7 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.0 dB | -99.7 | 0.2 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 1 | 4000.0005 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -100.7 dB | -100.7 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -82.9 dB | -83.1 | 10.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -75.9 | 52.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.546 Hz, -115.1 dB | -110.0 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9306 | 0.0021 | 3/19 | k=2: 99.859 Hz, -108.4 dB | -109.1 | 0.0 % |
| Mischprodukte n·999.8677 + m·5999.9999 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0047 | 2 | k=5·f1+3·f2: 22999.341 Hz, -122.9 dB | -122.8 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.3 dB | -99.9 | 0.2 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 2 | 4000.0005 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -100.8 dB | -100.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -83.6 | 12.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.7 dB | -76.8 | 61.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0010 | 10/10 | k=1: 2320.545 Hz, -114.7 dB | -111.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9301 | 0.0022 | 5/19 | k=2: 99.860 Hz, -111.2 dB | -110.8 | 0.0 % |
| Mischprodukte n·999.8677 + m·5999.9999 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0025 | 5 | k=-7·f1+4·f2: 17000.924 Hz, -122.7 dB | -119.7 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 3 | 4000.0004 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -101.3 dB | -100.9 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -101.5 dB | -100.7 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -83.3 | 7.0 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -74.1 | 58.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0011 | 10/10 | k=1: 2320.546 Hz, -113.9 dB | -111.6 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9299 | 0.0025 | 3/19 | k=2: 99.860 Hz, -104.8 dB | -107.2 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -100.5 dB | -100.1 | 0.1 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 4 | 4000.0004 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -101.2 dB | -100.9 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 55.6 | usb1k·1 |
| 1999.735 | -82.0 | 50.6 | usb1k·2 |
| 6000.000 | -82.8 | 51.4 | fs8·1 |
| 2999.603 | -84.8 | 47.9 | usb1k·3 |
| 12000.000 | -85.2 | 50.3 | fs8·2 |
| 18000.000 | -87.4 | 49.1 | fs8·3 |
| 3999.471 | -87.7 | 45.6 | usb1k·4 |
| 4999.339 | -89.2 | 45.1 | usb1k·5 |
| 9998.676 | -88.8 | 46.1 | usb1k·10 |
| 15997.883 | -91.4 | 45.2 | usb1k·16 |
| 8998.809 | -90.7 | 44.5 | usb1k·9 |
| 18997.486 | -92.8 | 43.1 | usb1k·19 |
| 16997.751 | -93.9 | 42.2 | usb1k·17 |
| 6999.074 | -93.6 | 40.3 | usb1k·7 |
| 12998.279 | -95.5 | 39.7 | usb1k·13 |
| 5999.206 | -95.4 | 38.7 | usb1k·6 |
| 11998.412 | -96.0 | 39.4 | usb1k·12 |
| 20997.221 | -96.2 | 40.2 | usb1k·21 |
| 19997.354 | -97.9 | 38.4 | usb1k·20 |
| 17997.618 | -99.0 | 37.6 | usb1k·18 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 57.7 | usb1k·1 |
| 1999.735 | -82.4 | 52.0 | usb1k·2 |
| 6000.000 | -82.9 | 53.2 | fs8·1 |
| 2999.603 | -84.3 | 50.1 | usb1k·3 |
| 12000.000 | -85.5 | 51.9 | fs8·2 |
| 18000.000 | -87.3 | 50.6 | fs8·3 |
| 3999.471 | -87.6 | 47.5 | usb1k·4 |
| 9998.676 | -88.7 | 48.2 | usb1k·10 |
| 4999.339 | -89.8 | 45.9 | usb1k·5 |
| 15997.883 | -91.4 | 46.7 | usb1k·16 |
| 8998.809 | -91.2 | 45.7 | usb1k·9 |
| 18997.486 | -92.8 | 44.6 | usb1k·19 |
| 16997.751 | -93.6 | 44.0 | usb1k·17 |
| 6999.074 | -93.1 | 42.5 | usb1k·7 |
| 12998.279 | -95.9 | 41.2 | usb1k·13 |
| 11998.412 | -96.0 | 41.3 | usb1k·12 |
| 20997.221 | -96.5 | 41.2 | usb1k·21 |
| 5999.206 | -96.1 | 40.0 | usb1k·6 |
| 19997.354 | -98.0 | 40.3 | usb1k·20 |
| 17997.618 | -98.7 | 39.4 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.7 | 60.6 | usb1k·1 |
| 6000.000 | -83.4 | 55.9 | fs8·1 |
| 1999.735 | -83.9 | 54.1 | usb1k·2 |
| 2999.603 | -84.8 | 53.2 | usb1k·3 |
| 12000.000 | -86.2 | 53.8 | fs8·2 |
| 18000.000 | -87.8 | 52.4 | fs8·3 |
| 3999.471 | -88.0 | 50.5 | usb1k·4 |
| 9998.676 | -88.9 | 50.9 | usb1k·10 |
| 4999.339 | -90.7 | 48.2 | usb1k·5 |
| 15997.883 | -91.9 | 48.2 | usb1k·16 |
| 18997.486 | -93.1 | 46.7 | usb1k·19 |
| 16997.751 | -93.7 | 46.4 | usb1k·17 |
| 8998.809 | -92.5 | 47.5 | usb1k·9 |
| 6999.074 | -93.5 | 45.4 | usb1k·7 |
| 12998.279 | -96.4 | 43.7 | usb1k·13 |
| 11998.412 | -96.2 | 43.6 | usb1k·12 |
| 20997.221 | -97.4 | 42.8 | usb1k·21 |
| 5999.206 | -97.2 | 42.0 | usb1k·6 |
| 19997.354 | -98.5 | 41.9 | usb1k·20 |
| 17997.618 | -98.9 | 41.4 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 59.1 | usb1k·1 |
| 1999.735 | -80.2 | 53.1 | usb1k·2 |
| 2999.603 | -82.8 | 50.9 | usb1k·3 |
| 6000.000 | -83.2 | 51.6 | fs8·1 |
| 12000.000 | -85.7 | 50.4 | fs8·2 |
| 3999.471 | -86.8 | 47.2 | usb1k·4 |
| 18000.000 | -87.4 | 49.1 | fs8·3 |
| 4999.339 | -88.7 | 45.8 | usb1k·5 |
| 9998.677 | -88.9 | 46.6 | usb1k·10 |
| 15997.883 | -90.6 | 45.7 | usb1k·16 |
| 8998.809 | -90.5 | 45.1 | usb1k·9 |
| 6999.074 | -91.4 | 42.6 | usb1k·7 |
| 16997.751 | -93.0 | 43.6 | usb1k·17 |
| 18997.486 | -93.0 | 43.8 | usb1k·19 |
| 5999.206 | -93.6 | 41.2 | usb1k·6 |
| 11998.412 | -94.9 | 41.1 | usb1k·12 |
| 7998.941 | -94.7 | 41.1 | usb1k·8 |
| 20997.221 | -95.9 | 40.8 | usb1k·21 |
| 12998.279 | -96.6 | 39.3 | usb1k·13 |
| 13998.147 | -97.9 | 38.3 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.04 | 0.04 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.28 | -0.09 | 0.03 |
| led | Kanal 1 | 11/11 | 6.36 | 0.28 | 0.90 |
| mains50 | Kanal 1 | 11/11 | 757.55 | -738.96 | 2.08 |
| other1 | Kanal 1 | 11/11 | 0.23 | -0.35 | 0.18 |
| other2 | Kanal 1 | 11/11 | 0.32 | -0.08 | 0.38 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.03 | 0.05 |
| usb1k | Kanal 2 | 11/11 | 0.24 | -0.09 | 0.03 |
| led | Kanal 2 | 11/11 | 0.44 | 0.34 | 0.35 |
| mains50 | Kanal 2 | 11/11 | 238.39 | -742.68 | 2.17 |
| other1 | Kanal 2 | 11/11 | 0.15 | -0.21 | 0.16 |
| other2 | Kanal 2 | 11/11 | 0.20 | -0.13 | 0.30 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.02 | 0.05 |
| usb1k | Kanal 3 | 11/11 | 0.20 | -0.04 | 0.03 |
| led | Kanal 3 | 11/11 | 0.63 | 0.28 | 0.52 |
| mains50 | Kanal 3 | 11/11 | 125.06 | -302.68 | 1.16 |
| other1 | Kanal 3 | 11/11 | 0.18 | -0.22 | 0.17 |
| other2 | Kanal 3 | 11/11 | 0.10 | 0.03 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.02 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.20 | -0.13 | 0.03 |
| led | Kanal 4 | 11/11 | 0.98 | -0.66 | 0.86 |
| mains50 | Kanal 4 | 11/11 | 160.95 | 153.47 | 2.11 |
| other1 | Kanal 4 | 11/11 | 0.15 | 0.00 | 0.16 |
| other2 | Kanal 4 | 11/11 | 0.29 | 0.24 | 0.31 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.93 | 0.16 s (6.40 Hz) | 21.7 |
| Kanal 1 | 999.9 Hz ± 10 | 1.00 | 7.50 s (0.13 Hz) | 37.3 |
| Kanal 2 | breitbandig | 0.87 | 0.16 s (6.40 Hz) | 23.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 38.5 |
| Kanal 3 | breitbandig | 0.45 | 7.50 s (0.13 Hz) | 22.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 42.5 |
| Kanal 4 | breitbandig | 0.75 | 0.16 s (6.40 Hz) | 23.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.5 |

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
| Kanal 1 | 1.00 | 0.96 | 0.91 | 0.93 |
| Kanal 2 | 0.96 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.91 | 0.93 | 1.00 | 0.91 |
| Kanal 4 | 0.93 | 0.96 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B8-fx6a-a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B8-fx6a-a-r2_psd.png)

### Kammprofile

![Kammprofile](B8-fx6a-a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B8-fx6a-a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:01:18. Stream-Meldungen: 0. owl_read: reports/owl_read/B8-fx6a-a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
