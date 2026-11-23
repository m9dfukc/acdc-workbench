# Report B10-fx8a-a-r2: B10-fx8a-a-r2 – acdc1 fx8a-open-inputs-10a, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | Build-10-Sitzung: fx8a am Anfang, LED-Modus wie gemerkt, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-10a-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B10-fx8a-a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -71.2 | -78.6 | -72.1 | -72.9 | -86.0 | -72.4 | -93.8 | -72.2 | 68 % | -77.2 | 5.0 |
| Kanal 2 | -7.4 | -72.2 | -79.4 | -73.1 | -73.8 | -88.0 | -73.3 | -94.1 | -73.1 | 71 % | -78.5 | 5.4 |
| Kanal 3 | -5.7 | -73.8 | -81.8 | -74.5 | -75.2 | -92.6 | -74.7 | -94.8 | -74.5 | 82 % | -82.0 | 7.5 |
| Kanal 4 | -6.5 | -71.5 | -79.9 | -72.2 | -72.8 | -88.1 | -72.5 | -94.3 | -72.3 | 74 % | -78.1 | 5.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -82.9 dB | -82.2 | 10.0 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.5 | 58.3 % |
| Netz 50 Hz | Kanal 1 | 49.8154 | 0.0075 | 3/19 | k=3: 149.448 Hz, -111.5 dB | -107.7 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0025 | 9 | k=-3·f1+4·f2: 21000.398 Hz, -120.2 dB | -115.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.3 dB | -95.6 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -97.8 dB | -98.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.1 dB | -82.2 | 12.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.4 | 59.0 % |
| Netz 50 Hz | Kanal 2 | 49.8150 | 0.0075 | 3/19 | k=3: 149.447 Hz, -112.3 dB | -108.8 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0031 | 20 | k=-3·f1+4·f2: 21000.400 Hz, -120.3 dB | -112.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -95.9 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.2 dB | -98.7 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.8 dB | -82.8 | 15.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.3 | 66.9 % |
| Netz 50 Hz | Kanal 3 | 49.8153 | 0.0064 | 3/19 | k=3: 149.446 Hz, -117.1 dB | -114.4 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0029 | 31 | k=-3·f1+4·f2: 21000.397 Hz, -121.1 dB | -112.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.2 dB | -96.7 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.3 dB | -99.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.2 dB | -82.4 | 9.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.9 dB | -74.2 | 64.3 % |
| Netz 50 Hz | Kanal 4 | 49.8147 | 0.0069 | 3/19 | k=3: 149.449 Hz, -112.0 dB | -109.0 | 0.0 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0048 | 20 | k=-2·f1+1·f2: 4000.268 Hz, -115.8 dB | -110.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.0 dB | -96.1 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.0 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 57.8 | usb1k·1 |
| 1999.736 | -81.2 | 51.3 | usb1k·2 |
| 2999.603 | -82.6 | 51.4 | usb1k·3 |
| 12000.000 | -82.9 | 55.0 | fs8·2 |
| 6000.000 | -83.4 | 51.6 | fs8·1 |
| 18000.000 | -86.0 | 52.5 | fs8·3 |
| 3999.471 | -86.8 | 46.1 | usb1k·4 |
| 9998.677 | -88.1 | 49.6 | usb1k·10 |
| 4999.339 | -88.8 | 45.7 | usb1k·5 |
| 15997.883 | -89.7 | 48.7 | usb1k·16 |
| 6999.074 | -89.7 | 46.6 | usb1k·7 |
| 16997.751 | -93.1 | 45.5 | usb1k·17 |
| 8998.809 | -92.0 | 44.3 | usb1k·9 |
| 18997.487 | -93.3 | 46.0 | usb1k·19 |
| 20997.222 | -93.6 | 45.0 | usb1k·21 |
| 13998.148 | -95.2 | 42.8 | usb1k·14 |
| 14998.016 | -95.8 | 42.4 | usb1k·15 |
| 11998.412 | -96.3 | 41.6 | usb1k·12 |
| 17997.619 | -96.8 | 41.7 | usb1k·18 |
| 2000.000 | -97.3 | 35.3 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 58.2 | usb1k·1 |
| 1999.736 | -82.5 | 51.5 | usb1k·2 |
| 12000.000 | -83.1 | 56.1 | fs8·2 |
| 6000.000 | -83.4 | 53.4 | fs8·1 |
| 2999.603 | -83.3 | 52.0 | usb1k·3 |
| 18000.000 | -86.0 | 53.6 | fs8·3 |
| 3999.471 | -87.2 | 47.6 | usb1k·4 |
| 9998.677 | -88.1 | 50.4 | usb1k·10 |
| 4999.339 | -89.4 | 46.6 | usb1k·5 |
| 15997.883 | -90.2 | 49.2 | usb1k·16 |
| 6999.074 | -90.3 | 47.3 | usb1k·7 |
| 16997.751 | -93.3 | 45.9 | usb1k·17 |
| 18997.487 | -93.2 | 47.2 | usb1k·19 |
| 8998.809 | -92.5 | 45.6 | usb1k·9 |
| 20997.222 | -94.1 | 45.5 | usb1k·21 |
| 14998.016 | -95.8 | 43.4 | usb1k·15 |
| 13998.148 | -96.3 | 42.7 | usb1k·14 |
| 17997.619 | -96.7 | 43.1 | usb1k·18 |
| 11998.412 | -96.6 | 42.5 | usb1k·12 |
| 12998.280 | -97.4 | 42.2 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 61.0 | usb1k·1 |
| 1999.735 | -83.6 | 55.3 | usb1k·2 |
| 12000.000 | -83.8 | 58.6 | fs8·2 |
| 6000.000 | -83.8 | 56.3 | fs8·1 |
| 2999.603 | -84.2 | 55.4 | usb1k·3 |
| 18000.000 | -86.5 | 55.9 | fs8·3 |
| 3999.471 | -87.8 | 51.2 | usb1k·4 |
| 9998.677 | -88.4 | 53.5 | usb1k·10 |
| 15997.883 | -90.8 | 51.3 | usb1k·16 |
| 4999.339 | -90.0 | 49.7 | usb1k·5 |
| 6999.074 | -91.2 | 50.2 | usb1k·7 |
| 18997.487 | -93.6 | 48.7 | usb1k·19 |
| 16997.751 | -93.8 | 48.8 | usb1k·17 |
| 8998.809 | -93.1 | 48.2 | usb1k·9 |
| 20997.222 | -94.8 | 47.3 | usb1k·21 |
| 14998.015 | -96.3 | 45.4 | usb1k·15 |
| 17997.619 | -97.1 | 45.2 | usb1k·18 |
| 11998.412 | -97.1 | 45.2 | usb1k·12 |
| 12998.280 | -97.5 | 45.1 | usb1k·13 |
| 13998.148 | -97.7 | 44.0 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.9 | 59.0 | usb1k·1 |
| 1999.736 | -80.6 | 52.6 | usb1k·2 |
| 2999.603 | -82.4 | 52.6 | usb1k·3 |
| 12000.000 | -83.2 | 55.4 | fs8·2 |
| 6000.000 | -83.7 | 52.5 | fs8·1 |
| 18000.000 | -86.2 | 52.7 | fs8·3 |
| 3999.471 | -86.7 | 47.7 | usb1k·4 |
| 4999.339 | -88.3 | 46.9 | usb1k·5 |
| 9998.677 | -88.2 | 49.7 | usb1k·10 |
| 15997.883 | -89.5 | 48.8 | usb1k·16 |
| 6999.074 | -89.4 | 47.6 | usb1k·7 |
| 8998.809 | -91.6 | 45.3 | usb1k·9 |
| 16997.751 | -93.1 | 45.5 | usb1k·17 |
| 18997.487 | -93.4 | 45.7 | usb1k·19 |
| 20997.222 | -93.6 | 45.6 | usb1k·21 |
| 13998.148 | -94.6 | 43.4 | usb1k·14 |
| 14998.016 | -96.0 | 42.3 | usb1k·15 |
| 11998.412 | -95.8 | 42.8 | usb1k·12 |
| 5999.206 | -95.4 | 40.6 | usb1k·6 |
| 17997.619 | -97.1 | 41.8 | usb1k·18 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.02 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.25 | -0.03 | 0.03 |
| mains50 | Kanal 1 | 11/11 | 534.11 | 1563.14 | 1.50 |
| other1 | Kanal 1 | 11/11 | 0.26 | -0.10 | 0.06 |
| other2 | Kanal 1 | 11/11 | 0.21 | -0.25 | 0.18 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.25 | -0.06 | 0.02 |
| mains50 | Kanal 2 | 11/11 | 539.17 | 1651.18 | 1.47 |
| other1 | Kanal 2 | 11/11 | 1.79 | 0.04 | 0.11 |
| other2 | Kanal 2 | 11/11 | 0.20 | -0.05 | 0.18 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.22 | -0.04 | 0.02 |
| mains50 | Kanal 3 | 11/11 | 877.39 | 3165.48 | 1.71 |
| other1 | Kanal 3 | 11/11 | 0.33 | -0.06 | 0.05 |
| other2 | Kanal 3 | 11/11 | 0.18 | -0.03 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.23 | -0.07 | 0.03 |
| mains50 | Kanal 4 | 11/11 | 529.76 | 1644.87 | 1.49 |
| other1 | Kanal 4 | 11/11 | 1.62 | 1.91 | 0.17 |
| other2 | Kanal 4 | 11/11 | 0.21 | -0.16 | 0.26 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.96 | 0.31 s (3.22 Hz) | 24.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.5 |
| Kanal 2 | breitbandig | 0.95 | 0.31 s (3.22 Hz) | 25.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.5 |
| Kanal 3 | breitbandig | 0.75 | 0.31 s (3.22 Hz) | 25.4 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 41.2 |
| Kanal 4 | breitbandig | 0.80 | 0.31 s (3.22 Hz) | 24.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 37.2 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.94 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.96 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B10-fx8a-a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B10-fx8a-a-r2_psd.png)

### Kammprofile

![Kammprofile](B10-fx8a-a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B10-fx8a-a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 14:54:12. Stream-Meldungen: 0. owl_read: out/owl_read/B10-fx8a-a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 10 v22.4.r-fx8a (I-Cache an), acdc1 im Case. Vor der Aufnahme lief wieder der gemerkte Slot 12, acdc1 wurde vermutlich beim Umstecken neu gestartet. Regler 69/55/72/56 von 127. Oszillator im Case abgesteckt (Nutzer). messlog D85.
