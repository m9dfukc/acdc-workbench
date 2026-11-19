# Report B9-fx6a-r1: B9-fx6a-r1 – acdc1 fx6a-open-inputs-9, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 8 v22.4.r-fx6a, LED-Modus normal, ins Case geschraubt |
| test | Build-9-Sitzung: fx6a in der Mitte, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx6a-open-inputs-9-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B9-fx6a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.3 | -65.4 | -67.1 | -70.2 | -71.0 | -85.7 | -70.5 | -94.4 | -70.2 | 60 % | -74.2 | 4.0 |
| Kanal 2 | -6.9 | -67.4 | -69.8 | -71.2 | -71.9 | -87.6 | -71.4 | -94.7 | -71.2 | 66 % | -75.9 | 4.7 |
| Kanal 3 | -5.1 | -68.5 | -70.1 | -73.6 | -74.3 | -92.2 | -73.8 | -95.5 | -73.6 | 71 % | -78.9 | 5.3 |
| Kanal 4 | -6.1 | -67.7 | -71.1 | -70.3 | -71.0 | -87.3 | -70.5 | -94.9 | -70.3 | 63 % | -74.6 | 4.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.0 | 5.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8662 | 0.0005 | 23/23 | k=1: 999.866 Hz, -71.5 dB | -72.9 | 54.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0027 | 10/10 | k=1: 2320.544 Hz, -115.8 dB | -112.4 | 0.0 % |
| Mischprodukte n·999.8662 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8662 | 0.0026 | 1 | k=29·f1-1·f2: 22996.117 Hz, -121.0 dB | -123.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.7 dB | -96.5 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -98.1 dB | -98.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.5 dB | -83.1 | 6.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8662 | 0.0005 | 23/23 | k=1: 999.866 Hz, -72.1 dB | -73.5 | 59.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0016 | 10/10 | k=9: 20884.903 Hz, -114.4 dB | -109.9 | 0.0 % |
| Mischprodukte n·999.8662 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8662 | 0.0011 | 2 | k=-3·f1+4·f2: 21000.401 Hz, -119.7 dB | -120.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.3 dB | -96.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.6 dB | -98.9 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -85.0 dB | -83.7 | 9.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8662 | 0.0006 | 23/23 | k=1: 999.866 Hz, -74.6 dB | -75.8 | 60.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.545 Hz, -117.2 dB | -112.4 | 0.0 % |
| Mischprodukte n·999.8662 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8662 | 0.0016 | 2 | k=-3·f1+4·f2: 21000.401 Hz, -120.3 dB | -121.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.5 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.9 dB | -99.9 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.8 dB | -83.4 | 4.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8662 | 0.0006 | 23/23 | k=1: 999.866 Hz, -71.4 dB | -72.6 | 58.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0027 | 10/10 | k=1: 2320.544 Hz, -115.5 dB | -111.7 | 0.0 % |
| Mischprodukte n·999.8662 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8662 | 0.0008 | 1 | k=-3·f1+4·f2: 21000.401 Hz, -119.0 dB | -121.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.5 dB | -96.9 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.2 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -71.5 | 58.3 | usb1k·1 |
| 1999.732 | -78.4 | 52.7 | usb1k·2 |
| 2999.598 | -82.4 | 49.4 | usb1k·3 |
| 12000.000 | -84.2 | 49.3 | fs8·2 |
| 6000.000 | -84.4 | 48.5 | fs8·1 |
| 18000.000 | -85.8 | 47.9 | fs8·3 |
| 3999.464 | -86.1 | 46.4 | usb1k·4 |
| 4999.331 | -86.9 | 45.6 | usb1k·5 |
| 9998.662 | -89.2 | 44.6 | usb1k·10 |
| 8998.795 | -89.9 | 43.4 | usb1k·9 |
| 15997.859 | -89.2 | 44.4 | usb1k·16 |
| 16997.725 | -91.0 | 42.4 | usb1k·17 |
| 18997.457 | -91.2 | 42.5 | usb1k·19 |
| 6999.063 | -92.3 | 41.0 | usb1k·7 |
| 11998.394 | -91.8 | 41.6 | usb1k·12 |
| 7998.930 | -92.3 | 40.8 | usb1k·8 |
| 5999.197 | -92.5 | 40.4 | usb1k·6 |
| 12998.261 | -95.2 | 38.5 | usb1k·13 |
| 20997.190 | -96.5 | 37.7 | usb1k·21 |
| 2000.000 | -97.7 | 33.4 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -72.1 | 59.5 | usb1k·1 |
| 1999.732 | -78.9 | 53.9 | usb1k·2 |
| 2999.598 | -83.0 | 50.8 | usb1k·3 |
| 12000.000 | -84.5 | 50.9 | fs8·2 |
| 6000.000 | -84.5 | 50.1 | fs8·1 |
| 18000.000 | -85.8 | 49.6 | fs8·3 |
| 3999.464 | -86.4 | 47.8 | usb1k·4 |
| 4999.331 | -87.3 | 46.7 | usb1k·5 |
| 9998.662 | -89.4 | 46.1 | usb1k·10 |
| 8998.795 | -90.1 | 44.8 | usb1k·9 |
| 15997.859 | -89.5 | 45.3 | usb1k·16 |
| 18997.457 | -91.4 | 44.1 | usb1k·19 |
| 16997.725 | -91.6 | 43.7 | usb1k·17 |
| 6999.063 | -92.8 | 42.1 | usb1k·7 |
| 11998.394 | -92.1 | 43.1 | usb1k·12 |
| 7998.929 | -93.0 | 41.9 | usb1k·8 |
| 5999.197 | -93.3 | 41.3 | usb1k·6 |
| 12998.261 | -95.6 | 39.9 | usb1k·13 |
| 20997.190 | -97.0 | 39.0 | usb1k·21 |
| 19997.324 | -96.8 | 38.9 | usb1k·20 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -74.6 | 61.1 | usb1k·1 |
| 1999.732 | -81.7 | 54.9 | usb1k·2 |
| 6000.000 | -85.0 | 52.6 | fs8·1 |
| 2999.598 | -85.1 | 51.8 | usb1k·3 |
| 12000.000 | -85.2 | 52.8 | fs8·2 |
| 18000.000 | -86.3 | 51.9 | fs8·3 |
| 3999.464 | -87.8 | 49.7 | usb1k·4 |
| 4999.331 | -89.2 | 48.2 | usb1k·5 |
| 9998.662 | -89.9 | 47.9 | usb1k·10 |
| 8998.795 | -91.5 | 46.2 | usb1k·9 |
| 15997.859 | -90.9 | 47.0 | usb1k·16 |
| 18997.457 | -92.0 | 45.6 | usb1k·19 |
| 16997.725 | -92.9 | 44.5 | usb1k·17 |
| 11998.394 | -93.5 | 44.3 | usb1k·12 |
| 6999.064 | -94.9 | 43.2 | usb1k·7 |
| 7998.930 | -95.4 | 42.1 | usb1k·8 |
| 5999.197 | -96.4 | 41.3 | usb1k·6 |
| 12998.261 | -96.3 | 41.3 | usb1k·13 |
| 10998.528 | -97.5 | 40.4 | usb1k·11 |
| 19997.324 | -97.0 | 40.9 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -71.4 | 59.5 | usb1k·1 |
| 1999.732 | -77.6 | 54.3 | usb1k·2 |
| 2999.598 | -82.6 | 49.8 | usb1k·3 |
| 12000.000 | -84.8 | 48.8 | fs8·2 |
| 6000.000 | -84.8 | 48.5 | fs8·1 |
| 18000.000 | -85.9 | 48.1 | fs8·3 |
| 4999.331 | -86.2 | 46.6 | usb1k·5 |
| 3999.464 | -86.2 | 46.9 | usb1k·4 |
| 8998.795 | -89.1 | 44.1 | usb1k·9 |
| 9998.662 | -89.6 | 44.1 | usb1k·10 |
| 15997.859 | -88.9 | 44.4 | usb1k·16 |
| 5999.197 | -91.5 | 41.8 | usb1k·6 |
| 7998.929 | -92.0 | 41.2 | usb1k·8 |
| 11998.394 | -91.6 | 41.9 | usb1k·12 |
| 18997.457 | -91.5 | 42.5 | usb1k·19 |
| 6999.063 | -92.4 | 41.2 | usb1k·7 |
| 16997.725 | -91.5 | 42.0 | usb1k·17 |
| 12998.261 | -94.8 | 38.9 | usb1k·13 |
| 20997.190 | -96.2 | 38.4 | usb1k·21 |
| 19997.325 | -96.6 | 37.6 | usb1k·20 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | 0.02 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.38 | 1.06 | 0.10 |
| led | Kanal 1 | 11/11 | 7.95 | 7.87 | 1.14 |
| other1 | Kanal 1 | 11/11 | 0.49 | 0.45 | 0.21 |
| other2 | Kanal 1 | 11/11 | 0.17 | -0.10 | 0.12 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.01 | 0.06 |
| usb1k | Kanal 2 | 11/11 | 0.37 | 1.05 | 0.15 |
| led | Kanal 2 | 11/11 | 0.27 | 0.18 | 0.63 |
| other1 | Kanal 2 | 11/11 | 0.42 | 0.50 | 0.27 |
| other2 | Kanal 2 | 11/11 | 0.23 | -0.02 | 0.12 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.00 | 0.04 |
| usb1k | Kanal 3 | 11/11 | 0.45 | 1.21 | 0.12 |
| led | Kanal 3 | 11/11 | 1.20 | 0.28 | 0.92 |
| other1 | Kanal 3 | 11/11 | 0.38 | 0.51 | 0.30 |
| other2 | Kanal 3 | 11/11 | 0.13 | -0.02 | 0.09 |
| fs8 | Kanal 4 | 11/11 | 0.04 | 0.03 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.32 | 0.93 | 0.12 |
| led | Kanal 4 | 11/11 | 7.46 | 5.91 | 1.60 |
| other1 | Kanal 4 | 11/11 | 1.90 | 0.85 | 0.26 |
| other2 | Kanal 4 | 11/11 | 0.27 | -0.04 | 0.13 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.86 | 0.31 s (3.18 Hz) | 23.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 34.9 |
| Kanal 2 | breitbandig | 2.46 | 0.31 s (3.18 Hz) | 24.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 36.7 |
| Kanal 3 | breitbandig | 2.86 | 0.31 s (3.18 Hz) | 22.6 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 40.6 |
| Kanal 4 | breitbandig | 1.90 | 0.31 s (3.18 Hz) | 25.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 35.0 |

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
| Kanal 1 | 1.00 | 0.98 | 0.98 | 0.95 |
| Kanal 2 | 0.98 | 1.00 | 0.97 | 0.98 |
| Kanal 3 | 0.98 | 0.97 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.98 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B9-fx6a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B9-fx6a-r1_psd.png)

### Kammprofile

![Kammprofile](B9-fx6a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B9-fx6a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 12:17:54. Stream-Meldungen: 0. owl_read: out/owl_read/B9-fx6a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Start über dfu-util :leave nach dem Readback, kein Kaltstart (Case blieb an). Oszillator im Case abgesteckt (Nutzer). messlog D79.
