# Report B10-fx8a-b-r1: B10-fx8a-b-r1 – acdc1 fx8a-open-inputs-10b, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | Build-10-Sitzung: fx8a am Ende, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-10b-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B10-fx8a-b-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -69.6 | -73.6 | -71.9 | -72.5 | -86.1 | -72.2 | -93.6 | -71.9 | 71 % | -77.3 | 5.4 |
| Kanal 2 | -7.5 | -70.4 | -74.1 | -72.8 | -73.5 | -88.1 | -73.1 | -93.9 | -72.8 | 74 % | -78.7 | 5.9 |
| Kanal 3 | -5.7 | -72.0 | -76.0 | -74.3 | -74.9 | -92.6 | -74.4 | -94.7 | -74.3 | 84 % | -82.2 | 7.9 |
| Kanal 4 | -6.5 | -70.4 | -75.5 | -71.9 | -72.5 | -88.2 | -72.2 | -94.1 | -72.0 | 78 % | -78.5 | 6.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -82.9 dB | -82.1 | 9.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.7 dB | -74.0 | 61.5 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0030 | 8 | k=-7·f1+4·f2: 17000.928 Hz, -121.2 dB | -117.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -96.8 dB | -95.3 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -97.7 dB | -98.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.1 dB | -82.2 | 11.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -74.9 | 62.5 % |
| Netz 50 Hz | Kanal 2 | 50.0771 | 0.0064 | 3/19 | k=3: 150.233 Hz, -111.7 dB | -109.0 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0015 | 8 | k=-7·f1+4·f2: 17000.927 Hz, -120.5 dB | -117.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.4 dB | -95.6 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -98.6 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.8 dB | -82.7 | 14.4 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -75.9 | 69.5 % |
| Netz 50 Hz | Kanal 3 | 50.0379 | 0.0094 | 5/19 | k=1: 50.041 Hz, -112.5 dB | -111.6 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0035 | 33 | k=25·f1-4·f2: 996.676 Hz, -115.1 dB | -111.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -96.5 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.1 dB | -99.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=2: 12000.000 Hz, -83.2 dB | -82.3 | 9.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.2 dB | -73.6 | 68.3 % |
| Netz 50 Hz | Kanal 4 | 50.0771 | 0.0062 | 3/19 | k=3: 150.234 Hz, -111.2 dB | -108.8 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0038 | 6 | k=-3·f1+4·f2: 21000.398 Hz, -120.9 dB | -117.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -95.9 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.3 dB | -98.7 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.7 | 58.0 | usb1k·1 |
| 1999.736 | -81.1 | 51.2 | usb1k·2 |
| 2999.603 | -82.1 | 51.8 | usb1k·3 |
| 12000.000 | -82.9 | 54.7 | fs8·2 |
| 6000.000 | -83.4 | 52.6 | fs8·1 |
| 18000.000 | -85.9 | 53.2 | fs8·3 |
| 3999.471 | -86.5 | 48.3 | usb1k·4 |
| 9998.677 | -87.9 | 49.8 | usb1k·10 |
| 15997.883 | -90.1 | 48.3 | usb1k·16 |
| 4999.339 | -89.5 | 45.4 | usb1k·5 |
| 6999.074 | -89.4 | 47.5 | usb1k·7 |
| 16997.751 | -92.3 | 46.4 | usb1k·17 |
| 8998.809 | -91.1 | 45.9 | usb1k·9 |
| 18997.487 | -93.8 | 45.4 | usb1k·19 |
| 20997.222 | -93.7 | 45.0 | usb1k·21 |
| 5999.207 | -93.6 | 42.4 | usb1k·6 |
| 13998.148 | -95.3 | 43.0 | usb1k·14 |
| 11998.412 | -96.0 | 41.6 | usb1k·12 |
| 2000.000 | -96.8 | 35.6 | other1·1 |
| 17997.619 | -97.4 | 41.7 | usb1k·18 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 58.6 | usb1k·1 |
| 1999.736 | -82.3 | 51.4 | usb1k·2 |
| 2999.603 | -82.8 | 52.7 | usb1k·3 |
| 12000.000 | -83.1 | 55.8 | fs8·2 |
| 6000.000 | -83.4 | 54.0 | fs8·1 |
| 18000.000 | -85.9 | 54.0 | fs8·3 |
| 3999.471 | -86.9 | 49.3 | usb1k·4 |
| 9998.677 | -88.0 | 50.7 | usb1k·10 |
| 15997.883 | -90.5 | 49.1 | usb1k·16 |
| 4999.339 | -90.1 | 46.4 | usb1k·5 |
| 6999.074 | -90.0 | 48.3 | usb1k·7 |
| 16997.751 | -92.7 | 46.4 | usb1k·17 |
| 8998.809 | -91.6 | 46.6 | usb1k·9 |
| 18997.487 | -93.7 | 46.1 | usb1k·19 |
| 20997.222 | -94.2 | 45.8 | usb1k·21 |
| 5999.207 | -94.7 | 42.7 | usb1k·6 |
| 13998.148 | -96.5 | 42.7 | usb1k·14 |
| 11998.412 | -96.5 | 42.4 | usb1k·12 |
| 17997.619 | -97.1 | 42.6 | usb1k·18 |
| 2000.000 | -97.4 | 36.3 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 61.1 | usb1k·1 |
| 1999.736 | -83.4 | 54.0 | usb1k·2 |
| 12000.000 | -83.8 | 58.5 | fs8·2 |
| 6000.000 | -83.8 | 57.5 | fs8·1 |
| 2999.603 | -83.7 | 56.0 | usb1k·3 |
| 18000.000 | -86.3 | 56.2 | fs8·3 |
| 3999.471 | -87.4 | 53.2 | usb1k·4 |
| 9998.677 | -88.3 | 53.8 | usb1k·10 |
| 15997.883 | -91.0 | 51.4 | usb1k·16 |
| 4999.339 | -90.8 | 49.7 | usb1k·5 |
| 6999.074 | -90.9 | 50.9 | usb1k·7 |
| 16997.751 | -93.2 | 48.7 | usb1k·17 |
| 8998.809 | -92.3 | 49.4 | usb1k·9 |
| 18997.487 | -94.0 | 48.5 | usb1k·19 |
| 20997.222 | -94.8 | 47.7 | usb1k·21 |
| 5999.207 | -96.2 | 45.2 | usb1k·6 |
| 17997.619 | -97.4 | 45.2 | usb1k·18 |
| 11998.412 | -97.0 | 45.3 | usb1k·12 |
| 14998.016 | -97.7 | 44.3 | usb1k·15 |
| 13998.148 | -97.8 | 44.6 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.2 | 59.9 | usb1k·1 |
| 1999.736 | -80.4 | 52.9 | usb1k·2 |
| 2999.603 | -81.9 | 53.3 | usb1k·3 |
| 12000.000 | -83.2 | 55.0 | fs8·2 |
| 6000.000 | -83.5 | 52.9 | fs8·1 |
| 18000.000 | -86.0 | 53.4 | fs8·3 |
| 3999.471 | -86.4 | 49.4 | usb1k·4 |
| 9998.677 | -88.2 | 49.7 | usb1k·10 |
| 4999.339 | -88.9 | 47.0 | usb1k·5 |
| 15997.883 | -89.9 | 48.7 | usb1k·16 |
| 6999.074 | -89.2 | 48.1 | usb1k·7 |
| 8998.809 | -90.6 | 46.7 | usb1k·9 |
| 16997.751 | -92.4 | 46.6 | usb1k·17 |
| 5999.206 | -92.6 | 43.8 | usb1k·6 |
| 18997.487 | -94.0 | 45.5 | usb1k·19 |
| 20997.222 | -93.7 | 45.4 | usb1k·21 |
| 13998.148 | -95.0 | 43.5 | usb1k·14 |
| 11998.412 | -95.7 | 42.6 | usb1k·12 |
| 7998.942 | -95.1 | 42.4 | usb1k·8 |
| 2000.000 | -97.6 | 35.7 | other1·1 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.00 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.22 | -0.03 | 0.06 |
| other1 | Kanal 1 | 11/11 | 1.79 | 2.73 | 0.16 |
| other2 | Kanal 1 | 11/11 | 0.11 | 0.11 | 0.17 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.25 | -0.02 | 0.07 |
| mains50 | Kanal 2 | 11/11 | 561.43 | 770.67 | 4.15 |
| other1 | Kanal 2 | 11/11 | 1.90 | 5.15 | 0.17 |
| other2 | Kanal 2 | 11/11 | 0.10 | 0.15 | 0.14 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.24 | -0.05 | 0.06 |
| mains50 | Kanal 3 | 11/11 | 750.94 | 2549.01 | 2.30 |
| other1 | Kanal 3 | 11/11 | 0.33 | 0.10 | 0.17 |
| other2 | Kanal 3 | 11/11 | 0.08 | 0.06 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.19 | -0.01 | 0.10 |
| mains50 | Kanal 4 | 11/11 | 536.42 | 682.43 | 4.15 |
| other1 | Kanal 4 | 11/11 | 1.86 | 1.24 | 0.18 |
| other2 | Kanal 4 | 11/11 | 0.15 | 0.12 | 0.17 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.86 | 0.31 s (3.18 Hz) | 29.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 37.2 |
| Kanal 2 | breitbandig | 1.93 | 0.31 s (3.18 Hz) | 31.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 39.0 |
| Kanal 3 | breitbandig | 1.82 | 0.31 s (3.18 Hz) | 31.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 42.8 |
| Kanal 4 | breitbandig | 1.45 | 0.31 s (3.18 Hz) | 30.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 37.7 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.96 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.96 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.93 |
| Kanal 4 | 0.96 | 0.96 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B10-fx8a-b-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B10-fx8a-b-r1_psd.png)

### Kammprofile

![Kammprofile](B10-fx8a-b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B10-fx8a-b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 14:59:22. Stream-Meldungen: 0. owl_read: reports/owl_read/B10-fx8a-b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 10 v22.4.r-fx8a (I-Cache an), geflasht aus fx7a (firmware/flashlog/20261123_build10-fx8a-b/), Start über dfu-util :leave. Regler etwa 12 Uhr. Oszillator im Case abgesteckt (Nutzer). messlog D85.
