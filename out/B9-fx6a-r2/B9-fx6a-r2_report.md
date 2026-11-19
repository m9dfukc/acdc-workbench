# Report B9-fx6a-r2: B9-fx6a-r2 – acdc1 fx6a-open-inputs-9, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 8 v22.4.r-fx6a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx6a in der Mitte, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx6a-open-inputs-9-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx6a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -67.2 | -70.3 | -70.1 | -70.9 | -85.4 | -70.4 | -94.4 | -70.2 | 61 % | -74.3 | 4.1 |
| Kanal 2 | -7.0 | -69.1 | -73.4 | -71.2 | -71.8 | -87.5 | -71.4 | -94.7 | -71.2 | 68 % | -76.1 | 4.9 |
| Kanal 3 | -5.2 | -70.7 | -74.0 | -73.5 | -74.1 | -92.0 | -73.7 | -95.5 | -73.5 | 73 % | -79.2 | 5.7 |
| Kanal 4 | -6.1 | -68.9 | -75.1 | -70.1 | -70.8 | -87.4 | -70.4 | -95.0 | -70.1 | 65 % | -74.8 | 4.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -82.9 | 5.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8669 | 0.0002 | 23/23 | k=1: 999.867 Hz, -71.4 dB | -72.7 | 56.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -97.4 dB | -96.4 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.001 Hz, -98.3 dB | -98.8 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.1 | 6.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8669 | 0.0002 | 23/23 | k=1: 999.867 Hz, -72.0 dB | -73.3 | 61.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0010 | 10/10 | k=9: 20884.904 Hz, -114.7 dB | -110.5 | 0.0 % |
| Mischprodukte n·999.8669 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8669 | 0.0047 | 2 | k=-1·f1+4·f2: 23000.129 Hz, -122.1 dB | -122.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.0 dB | -96.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -98.7 dB | -99.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.8 dB | -83.6 | 9.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8669 | 0.0002 | 23/23 | k=1: 999.867 Hz, -74.4 dB | -75.5 | 63.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.544 Hz, -116.7 dB | -112.8 | 0.0 % |
| Mischprodukte n·999.8669 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8669 | 0.0035 | 6 | k=1·f1+1·f2: 6999.873 Hz, -119.9 dB | -117.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -99.5 dB | -97.4 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -100.1 dB | -100.0 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -83.3 | 4.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8669 | 0.0002 | 23/23 | k=1: 999.867 Hz, -71.0 dB | -72.3 | 60.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0025 | 9/10 | k=1: 2320.543 Hz, -115.9 dB | -113.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0007 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -97.0 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -71.4 | 58.5 | usb1k·1 |
| 1999.734 | -78.1 | 52.7 | usb1k·2 |
| 2999.601 | -82.1 | 49.3 | usb1k·3 |
| 6000.000 | -84.2 | 48.2 | fs8·1 |
| 12000.000 | -84.7 | 49.4 | fs8·2 |
| 18000.000 | -85.2 | 49.2 | fs8·3 |
| 3999.468 | -86.2 | 45.1 | usb1k·4 |
| 4999.335 | -86.8 | 44.8 | usb1k·5 |
| 9998.669 | -88.9 | 43.9 | usb1k·10 |
| 15997.870 | -89.1 | 44.8 | usb1k·16 |
| 8998.802 | -89.4 | 43.1 | usb1k·9 |
| 6999.068 | -91.0 | 41.0 | usb1k·7 |
| 5999.201 | -91.5 | 40.9 | usb1k·6 |
| 16997.737 | -91.5 | 43.1 | usb1k·17 |
| 18997.471 | -92.7 | 41.5 | usb1k·19 |
| 11998.403 | -93.1 | 41.1 | usb1k·12 |
| 7998.935 | -93.3 | 39.7 | usb1k·8 |
| 20997.204 | -93.7 | 40.9 | usb1k·21 |
| 12998.269 | -95.4 | 38.0 | usb1k·13 |
| 13998.136 | -96.0 | 37.6 | usb1k·14 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.0 | 59.6 | usb1k·1 |
| 1999.734 | -79.0 | 53.4 | usb1k·2 |
| 2999.601 | -82.6 | 50.6 | usb1k·3 |
| 6000.000 | -84.2 | 49.8 | fs8·1 |
| 12000.000 | -85.0 | 50.6 | fs8·2 |
| 18000.000 | -85.3 | 50.6 | fs8·3 |
| 3999.468 | -86.5 | 46.8 | usb1k·4 |
| 4999.334 | -87.5 | 45.9 | usb1k·5 |
| 9998.669 | -89.0 | 45.8 | usb1k·10 |
| 15997.870 | -89.5 | 46.3 | usb1k·16 |
| 8998.802 | -89.9 | 44.8 | usb1k·9 |
| 6999.068 | -91.6 | 42.6 | usb1k·7 |
| 5999.201 | -92.0 | 42.0 | usb1k·6 |
| 16997.737 | -91.8 | 44.6 | usb1k·17 |
| 18997.471 | -92.7 | 43.2 | usb1k·19 |
| 11998.403 | -93.6 | 42.1 | usb1k·12 |
| 7998.935 | -93.9 | 40.6 | usb1k·8 |
| 20997.204 | -94.4 | 42.2 | usb1k·21 |
| 12998.269 | -95.7 | 39.5 | usb1k·13 |
| 13998.136 | -97.0 | 38.5 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.4 | 61.5 | usb1k·1 |
| 1999.734 | -81.1 | 55.1 | usb1k·2 |
| 2999.601 | -84.7 | 51.9 | usb1k·3 |
| 6000.000 | -84.8 | 52.4 | fs8·1 |
| 18000.000 | -85.7 | 52.7 | fs8·3 |
| 12000.000 | -85.8 | 52.8 | fs8·2 |
| 3999.467 | -87.7 | 49.0 | usb1k·4 |
| 4999.335 | -89.2 | 47.1 | usb1k·5 |
| 9998.669 | -89.6 | 47.8 | usb1k·10 |
| 15997.870 | -90.6 | 47.8 | usb1k·16 |
| 8998.802 | -90.9 | 46.3 | usb1k·9 |
| 6999.068 | -93.3 | 43.6 | usb1k·7 |
| 16997.737 | -93.2 | 45.5 | usb1k·17 |
| 18997.471 | -93.2 | 45.4 | usb1k·19 |
| 5999.201 | -94.9 | 42.3 | usb1k·6 |
| 11998.403 | -94.9 | 43.7 | usb1k·12 |
| 20997.204 | -95.7 | 42.7 | usb1k·21 |
| 7998.935 | -96.3 | 40.6 | usb1k·8 |
| 12998.269 | -96.5 | 41.5 | usb1k·13 |
| 19997.338 | -99.0 | 39.8 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -71.0 | 59.6 | usb1k·1 |
| 1999.734 | -77.7 | 53.4 | usb1k·2 |
| 2999.600 | -82.0 | 49.9 | usb1k·3 |
| 6000.000 | -84.4 | 47.9 | fs8·1 |
| 12000.000 | -85.3 | 48.5 | fs8·2 |
| 18000.000 | -85.6 | 48.8 | fs8·3 |
| 4999.334 | -86.3 | 45.7 | usb1k·5 |
| 3999.468 | -86.3 | 45.8 | usb1k·4 |
| 9998.669 | -89.0 | 44.0 | usb1k·10 |
| 8998.802 | -89.1 | 44.3 | usb1k·9 |
| 15997.870 | -89.1 | 45.1 | usb1k·16 |
| 5999.201 | -90.1 | 42.3 | usb1k·6 |
| 6999.068 | -91.4 | 41.3 | usb1k·7 |
| 16997.737 | -91.5 | 43.0 | usb1k·17 |
| 7998.935 | -92.6 | 40.2 | usb1k·8 |
| 11998.403 | -92.9 | 40.9 | usb1k·12 |
| 18997.471 | -92.8 | 41.9 | usb1k·19 |
| 20997.204 | -93.9 | 41.1 | usb1k·21 |
| 12998.269 | -94.7 | 39.0 | usb1k·13 |
| 13998.136 | -96.4 | 37.3 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.09 |
| usb1k | Kanal 1 | 11/11 | 0.26 | 0.36 | 0.03 |
| other1 | Kanal 1 | 11/11 | 0.50 | -0.12 | 0.14 |
| other2 | Kanal 1 | 11/11 | 0.17 | 0.11 | 0.25 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.02 | 0.10 |
| usb1k | Kanal 2 | 11/11 | 0.24 | 0.34 | 0.05 |
| led | Kanal 2 | 11/11 | 0.62 | -0.69 | 0.72 |
| other1 | Kanal 2 | 11/11 | 0.36 | -0.08 | 0.10 |
| other2 | Kanal 2 | 11/11 | 0.18 | 0.10 | 0.20 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.01 | 0.10 |
| usb1k | Kanal 3 | 11/11 | 0.21 | 0.37 | 0.04 |
| led | Kanal 3 | 11/11 | 1.33 | -0.95 | 0.82 |
| other1 | Kanal 3 | 11/11 | 0.29 | 0.04 | 0.16 |
| other2 | Kanal 3 | 11/11 | 0.12 | 0.01 | 0.13 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.02 | 0.13 |
| usb1k | Kanal 4 | 11/11 | 0.24 | 0.43 | 0.10 |
| led | Kanal 4 | 11/11 | 2.41 | -0.08 | 1.30 |
| other1 | Kanal 4 | 11/11 | 0.42 | -0.19 | 0.13 |
| other2 | Kanal 4 | 11/11 | 0.20 | 0.21 | 0.16 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.95 | 0.32 s (3.17 Hz) | 23.4 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 35.7 |
| Kanal 2 | breitbandig | 1.51 | 0.31 s (3.20 Hz) | 24.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 36.9 |
| Kanal 3 | breitbandig | 1.85 | 0.32 s (3.17 Hz) | 23.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 41.4 |
| Kanal 4 | breitbandig | 1.06 | 0.31 s (3.20 Hz) | 24.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 35.3 |

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
| Kanal 1 | 1.00 | 0.97 | 0.97 | 0.93 |
| Kanal 2 | 0.97 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.97 | 0.96 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.97 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx6a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx6a-r2_psd.png)

### Kammprofile

![Kammprofile](B9-fx6a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx6a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:19:07. Stream-Meldungen: 0. owl_read: out/owl_read/B9-fx6a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Start über dfu-util :leave nach dem Readback, kein Kaltstart (Case blieb an). Oszillator im Case abgesteckt (Nutzer). messlog D79.
