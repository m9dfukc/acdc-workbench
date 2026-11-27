# Report B8-fx5a-r2: B8-fx5a-r2 – acdc1 fx5a-open-inputs-8, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a, ins Case geschraubt |
| test | Build-8-Sitzung: fx5a als Vergleich, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten, Oszillator im Case vom Strom getrennt |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx5a-open-inputs-8-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B8-fx5a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -68.3 | -71.2 | -71.5 | -72.3 | -85.2 | -71.8 | -94.6 | -71.5 | 58 % | -75.3 | 3.7 |
| Kanal 2 | -7.1 | -70.0 | -74.8 | -71.8 | -72.3 | -87.5 | -72.0 | -95.0 | -71.8 | 70 % | -77.1 | 5.3 |
| Kanal 3 | -5.2 | -71.8 | -75.1 | -74.4 | -75.1 | -91.7 | -74.7 | -95.9 | -74.5 | 73 % | -80.2 | 5.7 |
| Kanal 4 | -6.2 | -69.8 | -76.6 | -70.8 | -71.3 | -87.5 | -71.1 | -95.2 | -70.9 | 70 % | -76.1 | 5.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.0 dB | -83.0 | 7.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8670 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.1 dB | -74.5 | 50.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0009 | 10/10 | k=2: 4641.089 Hz, -115.3 dB | -112.0 | 0.0 % |
| Mischprodukte n·999.8670 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8670 | 0.0010 | 4 | k=5·f1+2·f2: 16999.334 Hz, -120.2 dB | -117.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.6 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.001 Hz, -98.4 dB | -99.0 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.3 dB | -83.2 | 7.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8670 | 0.0002 | 23/23 | k=1: 999.867 Hz, -72.4 dB | -73.8 | 63.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5447 | 0.0005 | 10/10 | k=8: 18564.358 Hz, -114.5 dB | -109.4 | 0.0 % |
| Mischprodukte n·999.8670 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8670 | 0.0022 | 7 | k=5·f1+2·f2: 16999.335 Hz, -120.6 dB | -116.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.6 dB | -96.9 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -85.1 dB | -83.8 | 11.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8670 | 0.0003 | 23/23 | k=1: 999.867 Hz, -75.6 dB | -76.6 | 61.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.089 Hz, -116.0 dB | -111.5 | 0.0 % |
| Mischprodukte n·999.8670 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8670 | 0.0022 | 15 | k=5·f1+2·f2: 16999.337 Hz, -121.0 dB | -114.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -100.0 dB | -97.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.3 dB | -100.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.6 dB | -83.4 | 5.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8670 | 0.0002 | 23/23 | k=1: 999.867 Hz, -71.5 dB | -72.8 | 64.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0012 | 10/10 | k=2: 4641.088 Hz, -115.1 dB | -111.2 | 0.0 % |
| Mischprodukte n·999.8670 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8670 | 0.0009 | 3 | k=-7·f1+4·f2: 17000.930 Hz, -121.0 dB | -120.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -97.2 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.7 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.1 | 57.4 | usb1k·1 |
| 1999.734 | -81.1 | 50.4 | usb1k·2 |
| 2999.601 | -82.4 | 49.6 | usb1k·3 |
| 12000.000 | -84.0 | 51.0 | fs8·2 |
| 6000.000 | -84.5 | 49.1 | fs8·1 |
| 18000.000 | -86.1 | 50.4 | fs8·3 |
| 3999.468 | -87.3 | 45.3 | usb1k·4 |
| 9998.670 | -89.1 | 45.8 | usb1k·10 |
| 4999.335 | -90.5 | 42.4 | usb1k·5 |
| 15997.872 | -90.6 | 45.4 | usb1k·16 |
| 6999.069 | -92.1 | 42.1 | usb1k·7 |
| 8998.803 | -92.0 | 42.4 | usb1k·9 |
| 16997.739 | -92.0 | 44.4 | usb1k·17 |
| 18997.473 | -92.3 | 44.2 | usb1k·19 |
| 7998.936 | -94.1 | 40.1 | usb1k·8 |
| 11998.404 | -94.1 | 41.0 | usb1k·12 |
| 5999.201 | -95.8 | 37.7 | usb1k·6 |
| 12998.271 | -96.7 | 38.7 | usb1k·13 |
| 20997.207 | -96.5 | 40.2 | usb1k·21 |
| 13998.138 | -97.3 | 38.3 | usb1k·14 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.4 | 59.7 | usb1k·1 |
| 1999.734 | -80.1 | 53.3 | usb1k·2 |
| 2999.601 | -82.1 | 52.1 | usb1k·3 |
| 12000.000 | -84.3 | 52.6 | fs8·2 |
| 6000.000 | -84.5 | 50.8 | fs8·1 |
| 18000.000 | -86.2 | 51.7 | fs8·3 |
| 3999.468 | -87.0 | 47.5 | usb1k·4 |
| 9998.670 | -89.2 | 47.4 | usb1k·10 |
| 4999.335 | -89.5 | 45.2 | usb1k·5 |
| 15997.872 | -90.3 | 47.4 | usb1k·16 |
| 8998.803 | -91.2 | 45.1 | usb1k·9 |
| 6999.069 | -92.1 | 43.8 | usb1k·7 |
| 16997.739 | -92.0 | 45.7 | usb1k·17 |
| 18997.473 | -92.3 | 46.1 | usb1k·19 |
| 7998.936 | -93.3 | 42.5 | usb1k·8 |
| 11998.404 | -93.8 | 43.3 | usb1k·12 |
| 5999.202 | -94.5 | 40.8 | usb1k·6 |
| 12998.271 | -96.5 | 40.8 | usb1k·13 |
| 20997.207 | -96.1 | 42.4 | usb1k·21 |
| 13998.138 | -97.1 | 40.1 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.6 | 60.8 | usb1k·1 |
| 1999.734 | -82.5 | 54.6 | usb1k·2 |
| 2999.601 | -84.8 | 52.8 | usb1k·3 |
| 12000.000 | -85.1 | 54.4 | fs8·2 |
| 6000.000 | -85.1 | 53.4 | fs8·1 |
| 18000.000 | -86.6 | 53.6 | fs8·3 |
| 3999.468 | -88.8 | 49.1 | usb1k·4 |
| 9998.670 | -89.9 | 49.4 | usb1k·10 |
| 4999.335 | -91.0 | 46.9 | usb1k·5 |
| 15997.872 | -91.3 | 48.8 | usb1k·16 |
| 8998.803 | -91.9 | 47.3 | usb1k·9 |
| 18997.473 | -92.6 | 48.0 | usb1k·19 |
| 16997.739 | -93.8 | 46.8 | usb1k·17 |
| 6999.069 | -94.6 | 44.6 | usb1k·7 |
| 11998.404 | -95.1 | 44.5 | usb1k·12 |
| 12998.271 | -96.3 | 43.5 | usb1k·13 |
| 7998.936 | -96.7 | 42.3 | usb1k·8 |
| 5999.202 | -98.3 | 40.3 | usb1k·6 |
| 20997.207 | -97.3 | 43.6 | usb1k·21 |
| 10998.537 | -98.2 | 41.6 | usb1k·11 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -71.5 | 59.8 | usb1k·1 |
| 1999.734 | -77.9 | 54.6 | usb1k·2 |
| 2999.601 | -82.1 | 51.4 | usb1k·3 |
| 12000.000 | -84.6 | 51.0 | fs8·2 |
| 6000.000 | -84.6 | 49.5 | fs8·1 |
| 18000.000 | -86.6 | 50.0 | fs8·3 |
| 3999.468 | -86.7 | 46.9 | usb1k·4 |
| 4999.335 | -87.3 | 46.1 | usb1k·5 |
| 8998.803 | -89.3 | 45.7 | usb1k·9 |
| 9998.670 | -89.5 | 46.0 | usb1k·10 |
| 15997.872 | -89.6 | 46.8 | usb1k·16 |
| 5999.202 | -91.8 | 42.2 | usb1k·6 |
| 6999.068 | -92.3 | 42.1 | usb1k·7 |
| 7998.936 | -92.5 | 41.8 | usb1k·8 |
| 16997.739 | -92.2 | 44.2 | usb1k·17 |
| 18997.473 | -92.4 | 44.7 | usb1k·19 |
| 11998.404 | -93.2 | 42.6 | usb1k·12 |
| 12998.271 | -95.0 | 41.0 | usb1k·13 |
| 20997.207 | -94.9 | 42.2 | usb1k·21 |
| 13998.138 | -96.6 | 39.2 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.02 | 0.08 |
| usb1k | Kanal 1 | 11/11 | 0.34 | 0.47 | 0.04 |
| led | Kanal 1 | 11/11 | 1.63 | 1.73 | 1.57 |
| other1 | Kanal 1 | 11/11 | 1.28 | -2.58 | 0.11 |
| other2 | Kanal 1 | 11/11 | 0.30 | -0.33 | 0.25 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.00 | 0.08 |
| usb1k | Kanal 2 | 11/11 | 0.28 | 0.48 | 0.04 |
| led | Kanal 2 | 11/11 | 0.39 | 0.67 | 0.70 |
| other1 | Kanal 2 | 11/11 | 1.40 | -0.49 | 0.05 |
| other2 | Kanal 2 | 11/11 | 0.27 | -0.06 | 0.16 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.02 | 0.08 |
| usb1k | Kanal 3 | 11/11 | 0.30 | 0.45 | 0.06 |
| led | Kanal 3 | 11/11 | 1.46 | 3.92 | 0.92 |
| other1 | Kanal 3 | 11/11 | 0.73 | 1.08 | 0.11 |
| other2 | Kanal 3 | 11/11 | 0.24 | -0.12 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.00 | 0.08 |
| usb1k | Kanal 4 | 11/11 | 0.24 | 0.43 | 0.05 |
| led | Kanal 4 | 11/11 | 1.23 | 3.28 | 1.68 |
| other1 | Kanal 4 | 11/11 | 1.97 | -2.03 | 0.06 |
| other2 | Kanal 4 | 11/11 | 0.27 | -0.10 | 0.12 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.20 | 0.31 s (3.18 Hz) | 27.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 37.1 |
| Kanal 2 | breitbandig | 1.49 | 0.31 s (3.18 Hz) | 28.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 38.5 |
| Kanal 3 | breitbandig | 1.94 | 0.31 s (3.18 Hz) | 28.2 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 41.3 |
| Kanal 4 | breitbandig | 1.06 | 0.31 s (3.18 Hz) | 26.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.89 | 7.50 s (0.13 Hz) | 36.7 |

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
| Kanal 1 | 1.00 | 0.96 | 0.96 | 0.89 |
| Kanal 2 | 0.96 | 1.00 | 0.95 | 0.96 |
| Kanal 3 | 0.96 | 0.95 | 1.00 | 0.89 |
| Kanal 4 | 0.89 | 0.96 | 0.89 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B8-fx5a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B8-fx5a-r2_psd.png)

### Kammprofile

![Kammprofile](B8-fx5a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B8-fx5a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:10:43. Stream-Meldungen: 0. owl_read: reports/owl_read/B8-fx5a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
