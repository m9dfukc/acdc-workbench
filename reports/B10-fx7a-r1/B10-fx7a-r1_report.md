# Report B10-fx7a-r1: B10-fx7a-r1 – acdc1 fx7a-open-inputs-10, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | Build-10-Sitzung: fx7a als Kontrolle in der Mitte, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx7a-open-inputs-10-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B10-fx7a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.1 | -74.6 | -72.0 | -72.7 | -86.1 | -72.3 | -94.0 | -72.0 | 70 % | -77.2 | 5.2 |
| Kanal 2 | -7.5 | -71.2 | -76.0 | -72.9 | -73.6 | -88.2 | -73.2 | -94.2 | -73.0 | 73 % | -78.6 | 5.7 |
| Kanal 3 | -5.7 | -72.7 | -77.5 | -74.4 | -75.0 | -92.6 | -74.6 | -95.0 | -74.4 | 83 % | -82.1 | 7.7 |
| Kanal 4 | -6.5 | -70.9 | -77.2 | -72.0 | -72.6 | -88.3 | -72.3 | -94.4 | -72.1 | 76 % | -78.3 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.9 dB | -82.7 | 8.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -74.1 | 61.4 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0041 | 7 | k=-3·f1+4·f2: 21000.398 Hz, -121.2 dB | -117.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.1 dB | -95.9 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0002 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.8 dB | -98.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.1 dB | -82.8 | 10.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.0 | 62.5 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0021 | 9 | k=-3·f1+4·f2: 21000.396 Hz, -121.1 dB | -117.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.7 dB | -96.2 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -98.7 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.6 dB | -83.3 | 12.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.0 | 69.9 % |
| Netz 50 Hz | Kanal 3 | 49.9931 | 0.0073 | 5/19 | k=1: 49.991 Hz, -111.9 dB | -108.9 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0024 | 26 | k=25·f1-4·f2: 996.686 Hz, -118.6 dB | -113.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.1 dB | -96.9 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0000 | 4/7 | k=1: 3000.000 Hz, -99.3 dB | -99.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.3 dB | -83.0 | 8.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -73.7 | 68.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0047 | 6 | k=-1·f1+1·f2: 5000.122 Hz, -119.8 dB | -117.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.4 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -98.9 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 57.8 | usb1k·1 |
| 1999.736 | -81.3 | 50.6 | usb1k·2 |
| 2999.603 | -82.4 | 51.9 | usb1k·3 |
| 12000.000 | -83.9 | 54.7 | fs8·2 |
| 6000.000 | -84.2 | 52.0 | fs8·1 |
| 18000.000 | -85.6 | 53.2 | fs8·3 |
| 3999.471 | -86.3 | 48.8 | usb1k·4 |
| 9998.677 | -88.3 | 49.3 | usb1k·10 |
| 15997.883 | -89.9 | 48.4 | usb1k·16 |
| 4999.339 | -89.2 | 46.2 | usb1k·5 |
| 6999.074 | -90.1 | 46.5 | usb1k·7 |
| 16997.751 | -92.5 | 46.7 | usb1k·17 |
| 8998.809 | -91.3 | 46.2 | usb1k·9 |
| 18997.487 | -93.6 | 45.4 | usb1k·19 |
| 20997.222 | -93.9 | 44.9 | usb1k·21 |
| 5999.207 | -94.0 | 42.2 | usb1k·6 |
| 13998.148 | -96.0 | 42.6 | usb1k·14 |
| 11998.412 | -95.6 | 42.9 | usb1k·12 |
| 2000.000 | -97.1 | 34.9 | other1·1 |
| 7998.942 | -95.6 | 41.5 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 58.2 | usb1k·1 |
| 1999.736 | -82.5 | 51.0 | usb1k·2 |
| 2999.603 | -83.1 | 52.7 | usb1k·3 |
| 12000.000 | -84.1 | 55.4 | fs8·2 |
| 6000.000 | -84.2 | 53.5 | fs8·1 |
| 18000.000 | -85.6 | 54.3 | fs8·3 |
| 3999.471 | -86.6 | 50.2 | usb1k·4 |
| 9998.677 | -88.3 | 50.3 | usb1k·10 |
| 15997.883 | -90.3 | 49.0 | usb1k·16 |
| 4999.339 | -89.9 | 46.8 | usb1k·5 |
| 6999.074 | -90.7 | 47.4 | usb1k·7 |
| 16997.751 | -92.8 | 46.8 | usb1k·17 |
| 8998.809 | -91.8 | 47.0 | usb1k·9 |
| 18997.487 | -93.5 | 46.8 | usb1k·19 |
| 20997.222 | -94.5 | 45.2 | usb1k·21 |
| 5999.207 | -95.1 | 42.6 | usb1k·6 |
| 11998.412 | -96.1 | 43.4 | usb1k·12 |
| 17997.619 | -97.1 | 42.8 | usb1k·18 |
| 13998.148 | -97.3 | 41.8 | usb1k·14 |
| 2000.000 | -97.7 | 35.9 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 60.7 | usb1k·1 |
| 1999.736 | -83.6 | 53.3 | usb1k·2 |
| 2999.603 | -84.0 | 56.1 | usb1k·3 |
| 6000.000 | -84.6 | 56.7 | fs8·1 |
| 12000.000 | -84.8 | 57.7 | fs8·2 |
| 18000.000 | -86.0 | 56.6 | fs8·3 |
| 3999.471 | -87.2 | 53.6 | usb1k·4 |
| 9998.677 | -88.6 | 53.8 | usb1k·10 |
| 15997.883 | -90.8 | 51.7 | usb1k·16 |
| 4999.339 | -90.6 | 50.0 | usb1k·5 |
| 6999.074 | -91.5 | 49.7 | usb1k·7 |
| 16997.751 | -93.3 | 49.5 | usb1k·17 |
| 8998.809 | -92.4 | 49.6 | usb1k·9 |
| 18997.487 | -93.8 | 48.6 | usb1k·19 |
| 20997.222 | -95.1 | 47.1 | usb1k·21 |
| 11998.412 | -96.7 | 45.9 | usb1k·12 |
| 17997.619 | -97.4 | 45.2 | usb1k·18 |
| 5999.207 | -96.6 | 44.7 | usb1k·6 |
| 12998.280 | -98.0 | 44.5 | usb1k·13 |
| 14998.016 | -98.3 | 43.9 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 59.6 | usb1k·1 |
| 1999.736 | -80.6 | 52.8 | usb1k·2 |
| 2999.603 | -82.2 | 53.3 | usb1k·3 |
| 12000.000 | -84.3 | 54.3 | fs8·2 |
| 6000.000 | -84.3 | 52.7 | fs8·1 |
| 18000.000 | -85.8 | 53.2 | fs8·3 |
| 3999.471 | -86.2 | 50.3 | usb1k·4 |
| 4999.339 | -88.6 | 47.5 | usb1k·5 |
| 9998.677 | -88.5 | 49.6 | usb1k·10 |
| 15997.883 | -89.7 | 48.8 | usb1k·16 |
| 6999.074 | -89.9 | 47.2 | usb1k·7 |
| 8998.809 | -90.8 | 47.1 | usb1k·9 |
| 16997.751 | -92.6 | 46.1 | usb1k·17 |
| 5999.207 | -92.9 | 44.1 | usb1k·6 |
| 18997.487 | -93.8 | 45.7 | usb1k·19 |
| 20997.222 | -93.9 | 45.4 | usb1k·21 |
| 13998.148 | -95.6 | 43.1 | usb1k·14 |
| 11998.412 | -95.4 | 43.3 | usb1k·12 |
| 7998.942 | -94.6 | 42.9 | usb1k·8 |
| 2000.000 | -97.8 | 35.6 | other1·1 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.03 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.15 | -0.14 | 0.10 |
| other1 | Kanal 1 | 11/11 | 1.88 | -3.38 | 0.05 |
| other2 | Kanal 1 | 11/11 | 0.18 | -0.08 | 0.17 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.02 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.15 | -0.13 | 0.11 |
| other1 | Kanal 2 | 11/11 | 1.68 | -3.16 | 0.04 |
| other2 | Kanal 2 | 11/11 | 0.16 | 0.09 | 0.10 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.00 | 0.04 |
| usb1k | Kanal 3 | 11/11 | 0.17 | -0.15 | 0.10 |
| mains50 | Kanal 3 | 11/11 | 104.20 | -8.84 | 0.46 |
| other1 | Kanal 3 | 11/11 | 0.62 | 0.16 | 0.05 |
| other2 | Kanal 3 | 11/11 | 0.15 | -0.00 | 0.10 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.01 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.13 | -0.13 | 0.10 |
| other1 | Kanal 4 | 11/11 | 1.99 | -2.88 | 0.09 |
| other2 | Kanal 4 | 11/11 | 0.19 | 0.21 | 0.11 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.65 | 0.31 s (3.18 Hz) | 28.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 37.5 |
| Kanal 2 | breitbandig | 1.55 | 0.31 s (3.18 Hz) | 29.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 38.6 |
| Kanal 3 | breitbandig | 1.44 | 0.31 s (3.18 Hz) | 30.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 42.1 |
| Kanal 4 | breitbandig | 1.15 | 0.31 s (3.18 Hz) | 28.0 |
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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.96 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.96 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B10-fx7a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B10-fx7a-r1_psd.png)

### Kammprofile

![Kammprofile](B10-fx7a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B10-fx7a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 14:56:16. Stream-Meldungen: 0. owl_read: reports/owl_read/B10-fx7a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 9 v22.4.r-fx7a, geflasht aus fx8a (firmware/flashlog/20261123_build9-fx7a-ab10/), Start über dfu-util :leave. Regler etwa 12 Uhr. Oszillator im Case abgesteckt (Nutzer). messlog D85.
