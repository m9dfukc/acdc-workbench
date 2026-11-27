# Report ORG-fx8a-a-r1: ORG-fx8a-a-r1 – acdc1 fx8a-open-inputs-orga, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1, Build 10 v22.4.r-fx8a |
| test | Original-Sitzung: fx8a am Anfang, Eingänge offen, Regler 12 Uhr (69/56/72/56, nicht bewegt), rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-orga-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis ORG-fx8a-a-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.8 | -82.4 | -72.2 | -72.9 | -88.0 | -72.5 | -94.4 | -72.3 | 72 % | -77.8 | 5.5 |
| Kanal 2 | -7.5 | -72.5 | -82.9 | -72.9 | -73.5 | -89.5 | -73.1 | -92.4 | -72.9 | 75 % | -79.0 | 6.1 |
| Kanal 3 | -5.8 | -74.2 | -88.9 | -74.3 | -74.9 | -94.4 | -74.5 | -92.9 | -74.4 | 85 % | -82.5 | 8.1 |
| Kanal 4 | -6.6 | -71.6 | -82.6 | -71.9 | -72.4 | -89.5 | -72.1 | -92.6 | -71.9 | 78 % | -78.6 | 6.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.1 dB | -82.1 | 10.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.4 | 61.4 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0015 | 8 | k=1·f1+3·f2: 18999.866 Hz, -120.4 dB | -115.3 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.7 dB | -98.3 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.0 dB | -96.6 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.1 dB | -82.1 | 12.1 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -74.9 | 63.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0017 | 17 | k=-1·f1+1·f2: 5000.133 Hz, -120.0 dB | -113.4 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -98.6 | 0.3 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 2 | 1000.0001 | 0.0003 | 16/23 | k=1: 1000.000 Hz, -99.1 dB | -93.5 | 0.9 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.7 dB | -82.7 | 14.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -75.9 | 69.8 % |
| Netz 50 Hz | Kanal 3 | 49.9889 | 0.0015 | 5/19 | k=2: 99.978 Hz, -114.8 dB | -115.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0021 | 28 | k=1·f1+3·f2: 18999.867 Hz, -121.8 dB | -113.4 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.3 | 0.3 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0003 | 16/23 | k=1: 1000.000 Hz, -100.0 dB | -94.0 | 1.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -82.3 | 9.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.1 dB | -73.6 | 68.9 % |
| Netz 50 Hz | Kanal 4 | 49.9886 | 0.0013 | 2/19 | k=2: 99.979 Hz, -111.5 dB | -113.8 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0016 | 19 | k=1·f1+1·f2: 6999.867 Hz, -116.1 dB | -110.6 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -98.9 | 0.2 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 4 | 1000.0001 | 0.0003 | 16/23 | k=1: 1000.000 Hz, -99.5 dB | -93.8 | 0.6 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 59.4 | usb1k·1 |
| 1999.735 | -81.7 | 52.7 | usb1k·2 |
| 2999.603 | -82.2 | 52.6 | usb1k·3 |
| 6000.000 | -83.1 | 53.6 | fs8·1 |
| 12000.000 | -83.2 | 55.3 | fs8·2 |
| 18000.000 | -85.6 | 53.2 | fs8·3 |
| 3999.471 | -86.8 | 48.9 | usb1k·4 |
| 9998.676 | -87.8 | 49.8 | usb1k·10 |
| 4999.338 | -89.8 | 46.3 | usb1k·5 |
| 15997.881 | -90.5 | 48.2 | usb1k·16 |
| 6999.073 | -90.3 | 46.8 | usb1k·7 |
| 16997.749 | -92.4 | 46.2 | usb1k·17 |
| 8998.808 | -91.2 | 46.4 | usb1k·9 |
| 18997.484 | -93.8 | 44.7 | usb1k·19 |
| 20997.219 | -94.2 | 44.7 | usb1k·21 |
| 5999.206 | -94.0 | 42.8 | usb1k·6 |
| 13998.146 | -96.3 | 42.6 | usb1k·14 |
| 17997.616 | -96.9 | 41.9 | usb1k·18 |
| 11998.411 | -96.2 | 42.3 | usb1k·12 |
| 14998.013 | -97.0 | 41.6 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 59.9 | usb1k·1 |
| 1999.735 | -82.4 | 53.1 | usb1k·2 |
| 2999.603 | -82.7 | 53.6 | usb1k·3 |
| 6000.000 | -83.1 | 54.7 | fs8·1 |
| 12000.000 | -83.4 | 56.6 | fs8·2 |
| 18000.000 | -85.5 | 53.9 | fs8·3 |
| 3999.471 | -87.0 | 49.7 | usb1k·4 |
| 9998.676 | -87.8 | 50.8 | usb1k·10 |
| 4999.338 | -90.3 | 47.1 | usb1k·5 |
| 15997.881 | -90.7 | 49.5 | usb1k·16 |
| 6999.073 | -90.7 | 47.6 | usb1k·7 |
| 16997.749 | -92.8 | 46.5 | usb1k·17 |
| 8998.808 | -91.6 | 47.0 | usb1k·9 |
| 18997.484 | -93.9 | 46.0 | usb1k·19 |
| 20997.219 | -94.5 | 45.9 | usb1k·21 |
| 5999.206 | -95.0 | 42.8 | usb1k·6 |
| 17997.616 | -96.7 | 42.7 | usb1k·18 |
| 14998.013 | -96.8 | 42.7 | usb1k·15 |
| 11998.411 | -96.7 | 43.4 | usb1k·12 |
| 13998.146 | -97.2 | 42.5 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 63.4 | usb1k·1 |
| 1999.735 | -83.5 | 56.7 | usb1k·2 |
| 6000.000 | -83.7 | 57.8 | fs8·1 |
| 2999.603 | -83.6 | 57.0 | usb1k·3 |
| 12000.000 | -84.0 | 58.8 | fs8·2 |
| 18000.000 | -85.9 | 56.1 | fs8·3 |
| 3999.471 | -87.6 | 53.8 | usb1k·4 |
| 9998.676 | -88.1 | 53.8 | usb1k·10 |
| 15997.881 | -91.0 | 51.6 | usb1k·16 |
| 4999.338 | -90.8 | 50.4 | usb1k·5 |
| 6999.073 | -91.2 | 51.0 | usb1k·7 |
| 16997.749 | -93.2 | 48.9 | usb1k·17 |
| 8998.808 | -92.2 | 50.1 | usb1k·9 |
| 18997.484 | -94.0 | 48.4 | usb1k·19 |
| 20997.219 | -95.1 | 47.3 | usb1k·21 |
| 5999.206 | -96.1 | 45.5 | usb1k·6 |
| 17997.616 | -97.0 | 45.0 | usb1k·18 |
| 11998.411 | -96.8 | 46.0 | usb1k·12 |
| 14998.013 | -97.6 | 45.1 | usb1k·15 |
| 12998.278 | -97.4 | 44.9 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.1 | 61.2 | usb1k·1 |
| 1999.735 | -80.5 | 54.7 | usb1k·2 |
| 2999.603 | -81.7 | 54.1 | usb1k·3 |
| 6000.000 | -83.2 | 54.2 | fs8·1 |
| 12000.000 | -83.6 | 55.1 | fs8·2 |
| 18000.000 | -85.7 | 53.5 | fs8·3 |
| 3999.471 | -86.5 | 50.0 | usb1k·4 |
| 9998.676 | -87.9 | 50.1 | usb1k·10 |
| 4999.338 | -89.2 | 47.4 | usb1k·5 |
| 15997.881 | -90.3 | 49.2 | usb1k·16 |
| 6999.073 | -89.8 | 48.0 | usb1k·7 |
| 8998.808 | -90.7 | 47.4 | usb1k·9 |
| 16997.749 | -92.5 | 46.4 | usb1k·17 |
| 5999.206 | -92.9 | 44.4 | usb1k·6 |
| 20997.219 | -93.9 | 45.2 | usb1k·21 |
| 18997.484 | -94.2 | 45.5 | usb1k·19 |
| 13998.146 | -95.3 | 43.4 | usb1k·14 |
| 11998.411 | -95.9 | 42.9 | usb1k·12 |
| 7998.941 | -95.5 | 41.8 | usb1k·8 |
| 17997.616 | -97.5 | 41.7 | usb1k·18 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.00 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.14 | -0.00 | 0.03 |
| other1 | Kanal 1 | 11/11 | 0.16 | 0.09 | 0.19 |
| other2 | Kanal 1 | 11/11 | 0.24 | 0.09 | 0.06 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.15 | -0.01 | 0.03 |
| other1 | Kanal 2 | 11/11 | 0.16 | 0.32 | 0.18 |
| other2 | Kanal 2 | 11/11 | 0.62 | 0.08 | 0.03 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.14 | -0.01 | 0.03 |
| mains50 | Kanal 3 | 11/11 | 406.66 | 563.58 | 1.50 |
| other1 | Kanal 3 | 11/11 | 0.09 | 0.15 | 0.15 |
| other2 | Kanal 3 | 11/11 | 0.45 | 0.01 | 0.03 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.02 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.11 | -0.01 | 0.03 |
| mains50 | Kanal 4 | 11/11 | 627.66 | 1138.89 | 2.32 |
| other1 | Kanal 4 | 11/11 | 0.23 | 0.06 | 0.18 |
| other2 | Kanal 4 | 11/11 | 0.64 | -0.14 | 0.03 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.58 | 7.50 s (0.13 Hz) | 21.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 40.3 |
| Kanal 2 | breitbandig | 0.57 | 0.31 s (3.20 Hz) | 22.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 41.6 |
| Kanal 3 | breitbandig | 0.35 | 7.50 s (0.13 Hz) | 28.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 45.2 |
| Kanal 4 | breitbandig | 0.49 | 7.50 s (0.13 Hz) | 23.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 41.7 |

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
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.96 | 0.93 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](ORG-fx8a-a-r1_psd.png)

### Kammprofile

![Kammprofile](ORG-fx8a-a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](ORG-fx8a-a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 15:56:32. Stream-Meldungen: 0. owl_read: reports/owl_read/ORG-fx8a-a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. acdc1 im Case. Messlog D86.
