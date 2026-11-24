# Report D90b-nach-r1: D90b-nach-r1 – acdc1 gnd-nach-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-24 |
| device | acdc1 |
| test | gnd-nach-open-inputs |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261124_acdc1_gnd-nach-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis D90b-nach-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -4.3 | -64.4 | -64.6 | -77.5 | -78.8 | -88.8 | -78.1 | -101.4 | -77.5 | 30 % | -79.1 | 1.6 |
| Kanal 2 | -4.7 | -69.4 | -70.0 | -78.1 | -79.0 | -91.6 | -78.6 | -103.3 | -78.2 | 49 % | -81.1 | 2.9 |
| Kanal 3 | -3.2 | -69.6 | -69.8 | -82.5 | -83.9 | -96.6 | -83.1 | -111.0 | -82.5 | 39 % | -84.7 | 2.2 |
| Kanal 4 | -3.8 | -70.2 | -71.2 | -77.1 | -77.9 | -91.3 | -77.5 | -102.6 | -77.1 | 50 % | -80.1 | 3.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -101.0 dB | -100.9 | 0.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8641 | 0.0038 | 23/23 | k=1: 999.863 Hz, -81.4 dB | -82.8 | 29.8 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 1 | 7384.6153 | 0.0002 | 3/3 | k=1: 7384.615 Hz, -103.4 dB | -104.6 | 0.2 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 1 | 1215.1899 | 0.0011 | 10/19 | k=1: 1215.190 Hz, -103.2 dB | -104.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=2: 12000.000 Hz, -101.8 dB | -101.2 | 0.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8641 | 0.0009 | 23/23 | k=1: 999.864 Hz, -80.1 dB | -81.3 | 48.4 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 2 | 7384.6153 | 0.0003 | 3/3 | k=1: 7384.616 Hz, -105.0 dB | -106.3 | 0.2 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 2 | 1215.1899 | 0.0024 | 10/19 | k=1: 1215.190 Hz, -105.2 dB | -106.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -102.7 dB | -101.4 | 1.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8640 | 0.0006 | 23/23 | k=1: 999.863 Hz, -85.5 dB | -86.7 | 37.9 % |
| stärkste übrige Linie (18673.58 Hz) | Kanal 3 | 18673.5764 | 0.0000 | 1/1 | k=1: 18673.576 Hz, -110.1 dB | -113.5 | 0.1 % |
| stärkste übrige Linie (6551.45 Hz) | Kanal 3 | 6551.4472 | 0.0000 | 1/3 | k=1: 6551.447 Hz, -111.6 dB | -114.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -101.2 dB | -100.5 | 0.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8640 | 0.0008 | 23/23 | k=1: 999.864 Hz, -79.1 dB | -80.2 | 49.1 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 4 | 7384.6152 | 0.0001 | 3/3 | k=1: 7384.615 Hz, -104.1 dB | -105.5 | 0.1 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1899 | 0.0017 | 9/19 | k=1: 1215.190 Hz, -104.4 dB | -105.7 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.863 | -81.4 | 51.8 | usb1k·1 |
| 1999.728 | -87.1 | 48.6 | usb1k·2 |
| 2999.592 | -93.3 | 42.8 | usb1k·3 |
| 4999.320 | -95.4 | 42.1 | usb1k·5 |
| 3999.456 | -98.7 | 38.3 | usb1k·4 |
| 5999.186 | -99.6 | 38.6 | usb1k·6 |
| 12000.000 | -101.0 | 38.1 | fs8·2 |
| 7998.912 | -101.1 | 37.3 | usb1k·8 |
| 11998.368 | -101.8 | 37.2 | usb1k·12 |
| 8998.777 | -101.5 | 37.4 | usb1k·9 |
| 15997.825 | -101.5 | 37.9 | usb1k·16 |
| 6000.000 | -103.1 | 35.2 | fs8·1 |
| 9998.641 | -101.9 | 37.0 | usb1k·10 |
| 7384.615 | -103.4 | 35.6 | other1·1 |
| 16997.690 | -102.6 | 37.4 | usb1k·17 |
| 12998.233 | -104.0 | 35.6 | usb1k·13 |
| 1215.190 | -103.2 | 30.0 | other2·1 |
| 18997.416 | -104.6 | 35.4 | usb1k·19 |
| 6999.049 | -104.7 | 33.2 | usb1k·7 |
| 6620.689 | -104.0 | 34.2 | – |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -80.1 | 55.6 | usb1k·1 |
| 1999.728 | -85.2 | 53.1 | usb1k·2 |
| 4999.320 | -93.5 | 46.0 | usb1k·5 |
| 2999.592 | -92.5 | 46.0 | usb1k·3 |
| 5999.185 | -97.5 | 42.4 | usb1k·6 |
| 3999.456 | -97.7 | 41.4 | usb1k·4 |
| 7998.912 | -99.7 | 40.8 | usb1k·8 |
| 8998.776 | -99.3 | 41.2 | usb1k·9 |
| 11998.369 | -100.6 | 40.0 | usb1k·12 |
| 15997.824 | -100.3 | 41.0 | usb1k·16 |
| 12000.000 | -101.8 | 38.9 | fs8·2 |
| 9998.641 | -100.6 | 40.2 | usb1k·10 |
| 12998.233 | -102.0 | 39.0 | usb1k·13 |
| 16997.689 | -101.8 | 39.4 | usb1k·17 |
| 6000.000 | -103.0 | 37.0 | fs8·1 |
| 18997.417 | -103.7 | 37.9 | usb1k·19 |
| 19997.281 | -104.2 | 37.3 | usb1k·20 |
| 18000.000 | -104.6 | 36.7 | fs8·3 |
| 6999.048 | -104.7 | 35.2 | usb1k·7 |
| 7384.616 | -105.0 | 35.8 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.863 | -85.5 | 55.2 | usb1k·1 |
| 1999.728 | -90.7 | 51.9 | usb1k·2 |
| 2999.592 | -97.7 | 45.3 | usb1k·3 |
| 4999.320 | -99.6 | 44.2 | usb1k·5 |
| 3999.456 | -101.6 | 42.0 | usb1k·4 |
| 12000.000 | -102.7 | 41.4 | fs8·2 |
| 6000.000 | -102.8 | 41.0 | fs8·1 |
| 5999.186 | -104.1 | 39.8 | usb1k·6 |
| 18000.000 | -104.3 | 39.6 | fs8·3 |
| 8998.776 | -103.7 | 40.3 | usb1k·9 |
| 15997.824 | -104.4 | 39.6 | usb1k·16 |
| 11998.368 | -105.7 | 38.3 | usb1k·12 |
| 18997.417 | -106.1 | 37.1 | usb1k·19 |
| 7998.912 | -105.7 | 38.5 | usb1k·8 |
| 16997.689 | -106.1 | 37.6 | usb1k·17 |
| 9998.640 | -105.8 | 38.2 | usb1k·10 |
| 12998.233 | -108.0 | 36.3 | usb1k·13 |
| 19997.282 | -108.8 | 35.2 | usb1k·20 |
| 6999.048 | -109.5 | 34.3 | usb1k·7 |
| 22996.873 | -110.5 | 33.2 | usb1k·23 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.864 | -79.1 | 55.8 | usb1k·1 |
| 1999.728 | -83.6 | 53.8 | usb1k·2 |
| 4999.320 | -92.0 | 46.4 | usb1k·5 |
| 2999.592 | -91.8 | 45.7 | usb1k·3 |
| 5999.184 | -95.8 | 42.9 | usb1k·6 |
| 3999.456 | -96.9 | 41.0 | usb1k·4 |
| 8998.776 | -97.5 | 41.7 | usb1k·9 |
| 7998.912 | -98.6 | 40.7 | usb1k·8 |
| 11998.369 | -99.5 | 40.0 | usb1k·12 |
| 12998.233 | -100.4 | 39.2 | usb1k·13 |
| 15997.824 | -99.3 | 40.6 | usb1k·16 |
| 9998.641 | -99.5 | 40.0 | usb1k·10 |
| 12000.000 | -101.2 | 38.4 | fs8·2 |
| 16997.689 | -101.1 | 39.1 | usb1k·17 |
| 6000.000 | -102.0 | 36.7 | fs8·1 |
| 18997.417 | -102.7 | 38.0 | usb1k·19 |
| 19997.281 | -103.1 | 37.6 | usb1k·20 |
| 7384.615 | -104.1 | 35.6 | other1·1 |
| 18000.000 | -104.3 | 35.8 | fs8·3 |
| 6999.049 | -104.4 | 34.2 | usb1k·7 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.14 | 0.14 | 0.12 |
| usb1k | Kanal 1 | 11/11 | 0.64 | 1.52 | 0.19 |
| other1 | Kanal 1 | 11/11 | 0.19 | -0.27 | 0.20 |
| other2 | Kanal 1 | 11/11 | 0.60 | -0.21 | 0.40 |
| fs8 | Kanal 2 | 11/11 | 0.13 | 0.11 | 0.15 |
| usb1k | Kanal 2 | 11/11 | 0.53 | 1.55 | 0.10 |
| other1 | Kanal 2 | 11/11 | 0.18 | -0.08 | 0.19 |
| other2 | Kanal 2 | 11/11 | 0.56 | -0.22 | 0.40 |
| fs8 | Kanal 3 | 11/11 | 0.07 | -0.01 | 0.08 |
| usb1k | Kanal 3 | 11/11 | 0.51 | 1.49 | 0.09 |
| other1 | Kanal 3 | 11/11 | 0.23 | -0.27 | 0.42 |
| other2 | Kanal 3 | 11/11 | 0.42 | 0.26 | 0.40 |
| fs8 | Kanal 4 | 11/11 | 0.15 | 0.14 | 0.19 |
| usb1k | Kanal 4 | 11/11 | 0.68 | 2.09 | 0.06 |
| other1 | Kanal 4 | 11/11 | 0.15 | -0.05 | 0.15 |
| other2 | Kanal 4 | 11/11 | 0.51 | 0.05 | 0.42 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 5.01 | 0.31 s (3.20 Hz) | 36.9 |
| Kanal 1 | 999.9 Hz ± 10 | 1.02 | 0.31 s (3.20 Hz) | 27.8 |
| Kanal 2 | breitbandig | 4.02 | 0.31 s (3.20 Hz) | 37.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 0.31 s (3.20 Hz) | 24.8 |
| Kanal 3 | breitbandig | 4.92 | 0.31 s (3.20 Hz) | 34.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.97 | 0.31 s (3.22 Hz) | 30.2 |
| Kanal 4 | breitbandig | 3.50 | 0.31 s (3.20 Hz) | 37.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 0.31 s (3.18 Hz) | 24.6 |

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
| Kanal 1 | 1.00 | 0.97 | 0.98 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.98 | 0.95 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.97 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](D90b-nach-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D90b-nach-r1_psd.png)

### Kammprofile

![Kammprofile](D90b-nach-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](D90b-nach-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:09:51. Stream-Meldungen: 0. owl_read: out/owl_read/D90b-nach-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. D90b nachher: Draht Pin 15 (GND) ↔ Pin 33 (AGND) auf der Rückseite des Xibeca-Moduls, acdc1 im Case, Regler 63/64/71/50, keine Kabel, Slot 1
