# Report B8-fx5a-r1: B8-fx5a-r1 – acdc1 fx5a-open-inputs-8, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a, ins Case geschraubt |
| test | Build-8-Sitzung: fx5a als Vergleich, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten, Oszillator im Case vom Strom getrennt |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx5a-open-inputs-8-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B8-fx5a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.4 | -65.6 | -66.9 | -71.3 | -72.1 | -85.3 | -71.6 | -94.8 | -71.3 | 56 % | -74.9 | 3.6 |
| Kanal 2 | -7.0 | -67.4 | -69.5 | -71.6 | -72.2 | -87.4 | -71.8 | -95.1 | -71.6 | 69 % | -76.7 | 5.1 |
| Kanal 3 | -5.1 | -69.5 | -71.2 | -74.3 | -75.0 | -91.8 | -74.5 | -95.9 | -74.3 | 71 % | -79.7 | 5.4 |
| Kanal 4 | -6.1 | -66.7 | -69.0 | -70.6 | -71.2 | -87.2 | -70.9 | -95.3 | -70.6 | 67 % | -75.5 | 4.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.8 dB | -83.2 | 6.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8664 | 0.0003 | 23/23 | k=1: 999.866 Hz, -73.0 dB | -74.4 | 49.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0016 | 10/10 | k=2: 4641.089 Hz, -115.7 dB | -112.4 | 0.0 % |
| Mischprodukte n·999.8664 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8664 | 0.0075 | 2 | k=25·f1-4·f2: 996.670 Hz, -114.3 dB | -115.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -96.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.1 dB | -83.4 | 6.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8664 | 0.0002 | 23/23 | k=1: 999.866 Hz, -72.2 dB | -73.6 | 62.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0013 | 10/10 | k=9: 20884.903 Hz, -114.1 dB | -109.9 | 0.0 % |
| Mischprodukte n·999.8664 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8664 | 0.0032 | 3 | k=-5·f1+4·f2: 19000.671 Hz, -121.2 dB | -120.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.8 dB | -97.0 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.8 dB | -84.0 | 10.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8664 | 0.0003 | 23/23 | k=1: 999.866 Hz, -75.5 dB | -76.5 | 60.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.089 Hz, -116.3 dB | -112.3 | 0.0 % |
| Mischprodukte n·999.8664 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8664 | 0.0055 | 8 | k=25·f1-4·f2: 996.673 Hz, -116.2 dB | -114.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -100.2 dB | -97.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -100.4 dB | -100.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.5 | 5.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8664 | 0.0002 | 23/23 | k=1: 999.866 Hz, -71.4 dB | -72.7 | 62.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0011 | 10/10 | k=2: 4641.090 Hz, -115.0 dB | -111.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.2 dB | -97.3 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.3 dB | -99.7 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -73.0 | 57.1 | usb1k·1 |
| 1999.733 | -81.3 | 50.0 | usb1k·2 |
| 2999.599 | -82.7 | 49.1 | usb1k·3 |
| 12000.000 | -83.8 | 50.9 | fs8·2 |
| 6000.000 | -84.7 | 48.2 | fs8·1 |
| 3999.466 | -86.8 | 45.1 | usb1k·4 |
| 18000.000 | -86.9 | 49.3 | fs8·3 |
| 9998.664 | -88.6 | 45.6 | usb1k·10 |
| 4999.332 | -89.4 | 43.1 | usb1k·5 |
| 15997.862 | -90.5 | 44.9 | usb1k·16 |
| 6999.064 | -91.0 | 42.7 | usb1k·7 |
| 8998.798 | -92.0 | 42.0 | usb1k·9 |
| 16997.728 | -91.7 | 43.8 | usb1k·17 |
| 18997.462 | -93.0 | 43.0 | usb1k·19 |
| 5999.199 | -93.9 | 39.0 | usb1k·6 |
| 7998.931 | -94.7 | 39.0 | usb1k·8 |
| 11998.397 | -94.7 | 39.9 | usb1k·12 |
| 20997.195 | -95.7 | 41.2 | usb1k·21 |
| 13998.130 | -96.6 | 38.3 | usb1k·14 |
| 12998.263 | -97.2 | 37.7 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -72.2 | 59.8 | usb1k·1 |
| 1999.733 | -80.1 | 52.9 | usb1k·2 |
| 2999.599 | -82.4 | 51.0 | usb1k·3 |
| 12000.000 | -84.1 | 52.3 | fs8·2 |
| 6000.000 | -84.7 | 50.2 | fs8·1 |
| 3999.466 | -86.5 | 47.4 | usb1k·4 |
| 18000.000 | -87.0 | 50.5 | fs8·3 |
| 4999.332 | -88.4 | 46.1 | usb1k·5 |
| 9998.664 | -88.7 | 46.6 | usb1k·10 |
| 15997.862 | -90.1 | 47.0 | usb1k·16 |
| 8998.797 | -91.0 | 44.4 | usb1k·9 |
| 6999.064 | -91.1 | 44.4 | usb1k·7 |
| 16997.728 | -91.7 | 45.1 | usb1k·17 |
| 5999.199 | -92.8 | 42.1 | usb1k·6 |
| 18997.461 | -93.0 | 44.4 | usb1k·19 |
| 7998.931 | -93.8 | 41.1 | usb1k·8 |
| 11998.397 | -94.3 | 42.0 | usb1k·12 |
| 20997.194 | -95.2 | 43.0 | usb1k·21 |
| 13998.129 | -96.3 | 40.2 | usb1k·14 |
| 12998.263 | -96.8 | 39.8 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -75.5 | 60.4 | usb1k·1 |
| 1999.733 | -82.7 | 53.8 | usb1k·2 |
| 12000.000 | -84.8 | 54.2 | fs8·2 |
| 2999.599 | -85.3 | 51.8 | usb1k·3 |
| 6000.000 | -85.4 | 52.8 | fs8·1 |
| 18000.000 | -87.4 | 52.4 | fs8·3 |
| 3999.466 | -88.1 | 48.9 | usb1k·4 |
| 9998.664 | -89.5 | 49.1 | usb1k·10 |
| 4999.332 | -90.0 | 47.8 | usb1k·5 |
| 15997.862 | -91.1 | 48.5 | usb1k·16 |
| 8998.798 | -91.8 | 46.6 | usb1k·9 |
| 6999.064 | -93.5 | 44.7 | usb1k·7 |
| 18997.462 | -93.2 | 46.1 | usb1k·19 |
| 16997.728 | -93.4 | 46.1 | usb1k·17 |
| 11998.397 | -95.7 | 43.3 | usb1k·12 |
| 5999.199 | -95.9 | 42.2 | usb1k·6 |
| 12998.263 | -96.7 | 42.5 | usb1k·13 |
| 20997.194 | -96.4 | 43.5 | usb1k·21 |
| 7998.931 | -97.3 | 41.5 | usb1k·8 |
| 19997.328 | -99.2 | 41.0 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -71.4 | 59.7 | usb1k·1 |
| 1999.733 | -78.0 | 53.8 | usb1k·2 |
| 2999.599 | -82.4 | 49.6 | usb1k·3 |
| 12000.000 | -84.4 | 50.7 | fs8·2 |
| 6000.000 | -84.8 | 48.6 | fs8·1 |
| 3999.466 | -86.5 | 46.1 | usb1k·4 |
| 4999.332 | -86.6 | 46.5 | usb1k·5 |
| 18000.000 | -87.3 | 48.9 | fs8·3 |
| 9998.664 | -89.0 | 45.0 | usb1k·10 |
| 8998.797 | -89.3 | 45.1 | usb1k·9 |
| 15997.862 | -89.6 | 46.0 | usb1k·16 |
| 5999.198 | -90.5 | 42.8 | usb1k·6 |
| 6999.064 | -91.4 | 42.6 | usb1k·7 |
| 16997.729 | -91.9 | 43.3 | usb1k·17 |
| 7998.931 | -93.1 | 40.5 | usb1k·8 |
| 18997.462 | -93.1 | 42.7 | usb1k·19 |
| 11998.397 | -93.8 | 41.3 | usb1k·12 |
| 20997.194 | -94.3 | 42.6 | usb1k·21 |
| 12998.263 | -95.2 | 39.6 | usb1k·13 |
| 13998.129 | -96.3 | 38.7 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.02 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.31 | 0.41 | 0.18 |
| led | Kanal 1 | 11/11 | 3.24 | 2.32 | 0.89 |
| other1 | Kanal 1 | 11/11 | 2.31 | -5.46 | 0.20 |
| other2 | Kanal 1 | 11/11 | 0.20 | 0.17 | 0.24 |
| fs8 | Kanal 2 | 11/11 | 0.03 | -0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.26 | 0.50 | 0.13 |
| led | Kanal 2 | 11/11 | 0.25 | 0.18 | 0.58 |
| other1 | Kanal 2 | 11/11 | 2.25 | -5.29 | 0.17 |
| other2 | Kanal 2 | 11/11 | 0.15 | -0.06 | 0.24 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.25 | 0.35 | 0.16 |
| led | Kanal 3 | 11/11 | 2.02 | -1.70 | 0.40 |
| other1 | Kanal 3 | 11/11 | 1.44 | -2.87 | 0.18 |
| other2 | Kanal 3 | 11/11 | 0.15 | 0.16 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.04 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.24 | 0.63 | 0.12 |
| led | Kanal 4 | 11/11 | 3.09 | 3.33 | 1.00 |
| other1 | Kanal 4 | 11/11 | 2.36 | -2.09 | 0.17 |
| other2 | Kanal 4 | 11/11 | 0.24 | -0.10 | 0.26 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.45 | 0.31 s (3.18 Hz) | 32.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 35.3 |
| Kanal 2 | breitbandig | 2.93 | 0.31 s (3.18 Hz) | 33.1 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.3 |
| Kanal 3 | breitbandig | 2.98 | 0.31 s (3.18 Hz) | 32.4 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 40.9 |
| Kanal 4 | breitbandig | 2.97 | 0.31 s (3.18 Hz) | 33.7 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 35.8 |

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
| Kanal 1 | 1.00 | 0.97 | 0.97 | 0.92 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.97 | 0.95 | 1.00 | 0.89 |
| Kanal 4 | 0.92 | 0.97 | 0.89 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B8-fx5a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B8-fx5a-r1_psd.png)

### Kammprofile

![Kammprofile](B8-fx5a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B8-fx5a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:09:30. Stream-Meldungen: 0. owl_read: reports/owl_read/B8-fx5a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
