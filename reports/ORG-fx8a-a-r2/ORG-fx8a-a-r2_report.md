# Report ORG-fx8a-a-r2: ORG-fx8a-a-r2 – acdc1 fx8a-open-inputs-orga, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1, Build 10 v22.4.r-fx8a |
| test | Original-Sitzung: fx8a am Anfang, Eingänge offen, Regler 12 Uhr (69/56/72/56, nicht bewegt), rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-orga-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis ORG-fx8a-a-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.5 | -79.5 | -72.2 | -72.9 | -87.9 | -72.4 | -94.1 | -72.2 | 71 % | -77.6 | 5.4 |
| Kanal 2 | -7.5 | -72.1 | -80.2 | -72.9 | -73.5 | -89.4 | -73.1 | -94.3 | -72.9 | 75 % | -78.8 | 5.9 |
| Kanal 3 | -5.8 | -74.0 | -85.9 | -74.3 | -74.9 | -94.3 | -74.5 | -95.0 | -74.4 | 84 % | -82.4 | 8.0 |
| Kanal 4 | -6.6 | -71.3 | -79.9 | -71.9 | -72.4 | -89.5 | -72.1 | -94.5 | -71.9 | 78 % | -78.5 | 6.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.0 dB | -82.0 | 10.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.4 | 60.5 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0026 | 7 | k=1·f1+3·f2: 18999.865 Hz, -121.0 dB | -117.0 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -97.8 dB | -98.3 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -96.2 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.0 dB | -82.0 | 12.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -75.0 | 62.1 % |
| Netz 50 Hz | Kanal 2 | 49.9998 | 0.0169 | 3/19 | k=10: 500.000 Hz, -99.7 dB | -102.4 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0020 | 15 | k=5·f1+3·f2: 22999.341 Hz, -122.4 dB | -114.9 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.2 dB | -98.6 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.8 dB | -96.3 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.6 dB | -82.6 | 15.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.0 | 68.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2322.6088 | 0.0008 | 2/10 | k=3: 6967.826 Hz, -127.4 dB | -130.7 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9997 | 0.0189 | 5/19 | k=10: 500.000 Hz, -100.4 dB | -102.9 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0017 | 29 | k=34·f1-2·f2: 21995.496 Hz, -122.5 dB | -113.3 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.3 dB | -99.4 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.7 dB | -96.9 | 0.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.0 dB | -82.2 | 9.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.1 dB | -73.6 | 68.3 % |
| Netz 50 Hz | Kanal 4 | 49.9998 | 0.0174 | 3/19 | k=10: 500.000 Hz, -100.1 dB | -102.7 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0028 | 15 | k=1·f1+1·f2: 6999.867 Hz, -119.1 dB | -112.9 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.4 dB | -98.8 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -99.3 dB | -96.6 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 59.1 | usb1k·1 |
| 1999.735 | -81.7 | 52.4 | usb1k·2 |
| 2999.603 | -82.3 | 52.2 | usb1k·3 |
| 6000.000 | -83.0 | 53.1 | fs8·1 |
| 12000.000 | -83.5 | 54.5 | fs8·2 |
| 18000.000 | -84.8 | 53.7 | fs8·3 |
| 3999.471 | -86.7 | 48.5 | usb1k·4 |
| 9998.676 | -87.8 | 49.6 | usb1k·10 |
| 4999.338 | -89.7 | 46.1 | usb1k·5 |
| 15997.881 | -90.4 | 48.1 | usb1k·16 |
| 6999.073 | -90.2 | 46.6 | usb1k·7 |
| 16997.749 | -92.4 | 45.9 | usb1k·17 |
| 8998.808 | -91.3 | 45.9 | usb1k·9 |
| 18997.484 | -93.8 | 45.0 | usb1k·19 |
| 20997.219 | -94.2 | 44.9 | usb1k·21 |
| 5999.206 | -93.9 | 42.3 | usb1k·6 |
| 13998.146 | -96.3 | 42.1 | usb1k·14 |
| 17997.616 | -97.0 | 41.5 | usb1k·18 |
| 11998.411 | -96.3 | 41.8 | usb1k·12 |
| 14998.013 | -97.1 | 41.3 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 59.8 | usb1k·1 |
| 1999.735 | -82.5 | 52.8 | usb1k·2 |
| 2999.603 | -82.8 | 52.8 | usb1k·3 |
| 6000.000 | -83.0 | 54.4 | fs8·1 |
| 12000.000 | -83.8 | 55.7 | fs8·2 |
| 18000.000 | -84.8 | 54.7 | fs8·3 |
| 3999.471 | -86.9 | 49.7 | usb1k·4 |
| 9998.676 | -87.8 | 50.8 | usb1k·10 |
| 4999.338 | -90.2 | 47.0 | usb1k·5 |
| 15997.881 | -90.7 | 48.9 | usb1k·16 |
| 6999.073 | -90.6 | 47.5 | usb1k·7 |
| 16997.749 | -92.7 | 46.9 | usb1k·17 |
| 8998.808 | -91.7 | 46.6 | usb1k·9 |
| 18997.484 | -93.9 | 46.0 | usb1k·19 |
| 20997.219 | -94.6 | 45.4 | usb1k·21 |
| 5999.206 | -94.9 | 42.4 | usb1k·6 |
| 17997.616 | -96.8 | 42.7 | usb1k·18 |
| 14998.013 | -96.9 | 42.4 | usb1k·15 |
| 11998.411 | -96.7 | 42.7 | usb1k·12 |
| 13998.146 | -97.1 | 42.1 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 63.2 | usb1k·1 |
| 6000.000 | -83.6 | 57.8 | fs8·1 |
| 1999.735 | -83.6 | 56.3 | usb1k·2 |
| 2999.603 | -83.6 | 56.6 | usb1k·3 |
| 12000.000 | -84.4 | 57.9 | fs8·2 |
| 18000.000 | -85.2 | 56.7 | fs8·3 |
| 3999.471 | -87.5 | 53.4 | usb1k·4 |
| 9998.676 | -88.2 | 53.9 | usb1k·10 |
| 15997.881 | -91.0 | 51.1 | usb1k·16 |
| 4999.338 | -90.7 | 50.5 | usb1k·5 |
| 6999.073 | -91.2 | 50.5 | usb1k·7 |
| 16997.749 | -93.2 | 49.2 | usb1k·17 |
| 8998.808 | -92.2 | 49.8 | usb1k·9 |
| 18997.484 | -94.0 | 48.1 | usb1k·19 |
| 20997.219 | -95.1 | 46.9 | usb1k·21 |
| 5999.206 | -96.0 | 45.4 | usb1k·6 |
| 17997.616 | -97.1 | 44.7 | usb1k·18 |
| 11998.411 | -96.9 | 45.4 | usb1k·12 |
| 14998.013 | -97.6 | 44.8 | usb1k·15 |
| 12998.278 | -97.5 | 44.9 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.1 | 60.9 | usb1k·1 |
| 1999.735 | -80.5 | 54.4 | usb1k·2 |
| 2999.603 | -81.8 | 53.7 | usb1k·3 |
| 6000.000 | -83.0 | 53.8 | fs8·1 |
| 12000.000 | -84.0 | 54.7 | fs8·2 |
| 18000.000 | -84.9 | 53.9 | fs8·3 |
| 3999.471 | -86.4 | 49.8 | usb1k·4 |
| 9998.676 | -88.0 | 50.2 | usb1k·10 |
| 4999.338 | -89.1 | 47.4 | usb1k·5 |
| 15997.881 | -90.2 | 48.9 | usb1k·16 |
| 6999.073 | -89.9 | 47.5 | usb1k·7 |
| 8998.808 | -90.8 | 46.6 | usb1k·9 |
| 16997.748 | -92.4 | 46.3 | usb1k·17 |
| 5999.206 | -92.8 | 43.9 | usb1k·6 |
| 20997.219 | -93.9 | 45.5 | usb1k·21 |
| 18997.484 | -94.3 | 44.9 | usb1k·19 |
| 13998.146 | -95.3 | 43.5 | usb1k·14 |
| 7998.941 | -95.5 | 41.9 | usb1k·8 |
| 11998.411 | -95.9 | 42.8 | usb1k·12 |
| 17997.616 | -97.5 | 41.3 | usb1k·18 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.01 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.17 | -0.16 | 0.02 |
| other1 | Kanal 1 | 11/11 | 0.13 | -0.12 | 0.21 |
| other2 | Kanal 1 | 11/11 | 0.50 | -0.08 | 0.06 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.17 | -0.16 | 0.02 |
| mains50 | Kanal 2 | 11/11 | 76.99 | 104.68 | 0.49 |
| other1 | Kanal 2 | 11/11 | 0.09 | -0.13 | 0.17 |
| other2 | Kanal 2 | 11/11 | 0.43 | -0.21 | 0.06 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.18 | -0.08 | 0.02 |
| led | Kanal 3 | 10/11 | 12.11 | 32.82 | 2.25 |
| mains50 | Kanal 3 | 11/11 | 33.21 | 23.42 | 0.30 |
| other1 | Kanal 3 | 11/11 | 0.13 | -0.06 | 0.12 |
| other2 | Kanal 3 | 11/11 | 0.37 | 0.06 | 0.04 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.15 | -0.15 | 0.02 |
| mains50 | Kanal 4 | 11/11 | 88.25 | -60.96 | 0.47 |
| other1 | Kanal 4 | 11/11 | 0.12 | -0.13 | 0.22 |
| other2 | Kanal 4 | 11/11 | 0.56 | -0.03 | 0.05 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.78 | 0.16 s (6.40 Hz) | 24.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 39.4 |
| Kanal 2 | breitbandig | 0.74 | 0.16 s (6.40 Hz) | 26.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 41.0 |
| Kanal 3 | breitbandig | 0.42 | 7.50 s (0.13 Hz) | 25.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 44.7 |
| Kanal 4 | breitbandig | 0.64 | 0.16 s (6.40 Hz) | 26.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 40.4 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.96 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.97 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.96 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](ORG-fx8a-a-r2_psd.png)

### Kammprofile

![Kammprofile](ORG-fx8a-a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](ORG-fx8a-a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 15:57:45. Stream-Meldungen: 0. owl_read: reports/owl_read/ORG-fx8a-a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. acdc1 im Case. Messlog D86.
