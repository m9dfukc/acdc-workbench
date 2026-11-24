# Report D90b-nach-r2: D90b-nach-r2 – acdc1 gnd-nach-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-24 |
| device | acdc1 |
| test | gnd-nach-open-inputs |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261124_acdc1_gnd-nach-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis D90b-nach-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -4.5 | -72.4 | -74.0 | -77.4 | -78.5 | -89.4 | -77.9 | -101.3 | -77.4 | 36 % | -79.4 | 2.0 |
| Kanal 2 | -4.7 | -75.9 | -79.7 | -78.2 | -79.0 | -92.0 | -78.7 | -103.3 | -78.3 | 51 % | -81.3 | 3.1 |
| Kanal 3 | -3.2 | -76.9 | -78.2 | -82.7 | -84.0 | -97.4 | -83.3 | -110.8 | -82.7 | 42 % | -85.1 | 2.4 |
| Kanal 4 | -3.8 | -76.4 | -84.0 | -77.2 | -77.9 | -91.6 | -77.6 | -102.6 | -77.2 | 53 % | -80.4 | 3.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9998 | 0.0005 | 3/3 | k=2: 12000.000 Hz, -101.3 dB | -101.1 | 0.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8652 | 0.0024 | 23/23 | k=1: 999.865 Hz, -80.6 dB | -81.9 | 36.0 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 1 | 7384.6154 | 0.0004 | 3/3 | k=1: 7384.615 Hz, -103.4 dB | -104.6 | 0.2 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 1 | 1215.1899 | 0.0018 | 12/19 | k=1: 1215.190 Hz, -103.1 dB | -104.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0004 | 3/3 | k=2: 12000.000 Hz, -102.1 dB | -101.5 | 0.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8652 | 0.0019 | 23/23 | k=1: 999.865 Hz, -80.1 dB | -81.2 | 50.4 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 2 | 7384.6154 | 0.0003 | 3/3 | k=1: 7384.615 Hz, -105.1 dB | -106.5 | 0.1 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 2 | 1215.1900 | 0.0022 | 11/19 | k=1: 1215.190 Hz, -105.1 dB | -106.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -102.6 dB | -101.6 | 1.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8652 | 0.0006 | 23/23 | k=1: 999.865 Hz, -85.4 dB | -86.6 | 40.9 % |
| stärkste übrige Linie (18673.58 Hz) | Kanal 3 | 18673.5776 | 0.0000 | 1/1 | k=1: 18673.578 Hz, -110.1 dB | -113.2 | 0.1 % |
| stärkste übrige Linie (6551.45 Hz) | Kanal 3 | 6551.4473 | 0.0000 | 1/3 | k=1: 6551.447 Hz, -111.5 dB | -114.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -101.4 dB | -100.8 | 0.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8652 | 0.0009 | 23/23 | k=1: 999.865 Hz, -78.9 dB | -80.0 | 52.1 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 4 | 7384.6155 | 0.0005 | 3/3 | k=1: 7384.616 Hz, -104.2 dB | -105.6 | 0.1 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1899 | 0.0014 | 10/19 | k=1: 1215.190 Hz, -104.6 dB | -105.6 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -80.6 | 53.7 | usb1k·1 |
| 1999.730 | -85.9 | 50.0 | usb1k·2 |
| 2999.596 | -93.2 | 42.8 | usb1k·3 |
| 4999.326 | -94.3 | 43.3 | usb1k·5 |
| 3999.460 | -98.2 | 38.9 | usb1k·4 |
| 5999.191 | -98.2 | 39.5 | usb1k·6 |
| 8998.787 | -100.2 | 39.2 | usb1k·9 |
| 7998.922 | -100.4 | 38.4 | usb1k·8 |
| 9998.653 | -101.0 | 38.1 | usb1k·10 |
| 12000.000 | -101.3 | 38.6 | fs8·2 |
| 15997.844 | -100.8 | 39.4 | usb1k·16 |
| 11998.382 | -101.8 | 38.1 | usb1k·12 |
| 12998.248 | -102.5 | 36.9 | usb1k·13 |
| 6000.000 | -103.0 | 34.7 | fs8·1 |
| 16997.709 | -102.1 | 38.5 | usb1k·17 |
| 7384.615 | -103.4 | 35.0 | other1·1 |
| 1215.190 | -103.1 | 31.5 | other2·1 |
| 19997.305 | -104.4 | 36.0 | usb1k·20 |
| 6620.690 | -103.8 | 34.3 | – |
| 18997.439 | -104.4 | 35.7 | usb1k·19 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -80.1 | 56.8 | usb1k·1 |
| 1999.730 | -84.9 | 53.1 | usb1k·2 |
| 2999.595 | -92.7 | 45.8 | usb1k·3 |
| 4999.326 | -93.2 | 46.6 | usb1k·5 |
| 3999.460 | -97.7 | 41.8 | usb1k·4 |
| 5999.191 | -97.4 | 42.6 | usb1k·6 |
| 8998.787 | -99.1 | 41.9 | usb1k·9 |
| 7998.922 | -99.8 | 40.9 | usb1k·8 |
| 9998.653 | -100.5 | 40.6 | usb1k·10 |
| 15997.844 | -100.0 | 41.6 | usb1k·16 |
| 11998.382 | -101.0 | 40.4 | usb1k·12 |
| 12998.248 | -101.6 | 39.7 | usb1k·13 |
| 12000.000 | -102.1 | 39.5 | fs8·2 |
| 6000.000 | -103.1 | 36.8 | fs8·1 |
| 16997.709 | -101.9 | 39.7 | usb1k·17 |
| 18997.439 | -103.9 | 37.1 | usb1k·19 |
| 19997.305 | -104.1 | 37.9 | usb1k·20 |
| 17999.999 | -104.9 | 36.9 | fs8·3 |
| 7384.615 | -105.1 | 35.0 | other1·1 |
| 6999.057 | -104.2 | 36.5 | usb1k·7 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -85.4 | 56.3 | usb1k·1 |
| 1999.730 | -90.4 | 52.5 | usb1k·2 |
| 2999.596 | -98.4 | 44.4 | usb1k·3 |
| 4999.326 | -99.3 | 44.9 | usb1k·5 |
| 6000.000 | -102.6 | 40.4 | fs8·1 |
| 3999.460 | -101.8 | 42.5 | usb1k·4 |
| 12000.000 | -102.9 | 41.5 | fs8·2 |
| 8998.787 | -103.4 | 41.2 | usb1k·9 |
| 18000.000 | -104.7 | 39.4 | fs8·3 |
| 5999.191 | -103.3 | 39.8 | usb1k·6 |
| 15997.843 | -104.4 | 39.8 | usb1k·16 |
| 9998.653 | -106.0 | 38.2 | usb1k·10 |
| 11998.383 | -106.4 | 38.1 | usb1k·12 |
| 7998.922 | -106.1 | 38.0 | usb1k·8 |
| 18997.439 | -106.2 | 37.7 | usb1k·19 |
| 16997.709 | -105.9 | 37.9 | usb1k·17 |
| 12998.248 | -107.4 | 36.9 | usb1k·13 |
| 19997.305 | -108.6 | 35.0 | usb1k·20 |
| 18673.578 | -110.1 | 33.9 | other1·1 |
| 22996.901 | -111.2 | 33.1 | usb1k·23 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.865 | -78.9 | 57.0 | usb1k·1 |
| 1999.730 | -83.5 | 53.7 | usb1k·2 |
| 2999.595 | -91.7 | 45.8 | usb1k·3 |
| 4999.326 | -91.6 | 47.0 | usb1k·5 |
| 5999.192 | -95.4 | 43.4 | usb1k·6 |
| 3999.461 | -96.9 | 41.7 | usb1k·4 |
| 8998.787 | -97.5 | 42.6 | usb1k·9 |
| 7998.922 | -98.7 | 41.2 | usb1k·8 |
| 9998.652 | -99.4 | 40.4 | usb1k·10 |
| 11998.382 | -99.7 | 40.9 | usb1k·12 |
| 15997.844 | -99.0 | 41.4 | usb1k·16 |
| 12998.249 | -100.0 | 40.2 | usb1k·13 |
| 12000.000 | -101.4 | 39.1 | fs8·2 |
| 16997.709 | -100.8 | 40.1 | usb1k·17 |
| 6000.000 | -102.3 | 36.5 | fs8·1 |
| 18997.438 | -103.1 | 37.2 | usb1k·19 |
| 19997.305 | -103.2 | 37.7 | usb1k·20 |
| 7384.616 | -104.2 | 35.2 | other1·1 |
| 18000.000 | -104.6 | 36.2 | fs8·3 |
| 6999.057 | -103.5 | 36.0 | usb1k·7 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.11 | 0.13 | 0.18 |
| usb1k | Kanal 1 | 11/11 | 0.36 | 0.43 | 0.12 |
| other1 | Kanal 1 | 11/11 | 0.18 | -0.13 | 0.26 |
| other2 | Kanal 1 | 11/11 | 0.42 | -0.40 | 0.32 |
| fs8 | Kanal 2 | 11/11 | 0.12 | 0.07 | 0.14 |
| usb1k | Kanal 2 | 11/11 | 0.30 | 0.60 | 0.07 |
| other1 | Kanal 2 | 11/11 | 0.19 | -0.24 | 0.27 |
| other2 | Kanal 2 | 11/11 | 0.41 | -0.78 | 0.27 |
| fs8 | Kanal 3 | 11/11 | 0.04 | -0.03 | 0.12 |
| usb1k | Kanal 3 | 11/11 | 0.34 | 0.61 | 0.09 |
| other1 | Kanal 3 | 11/11 | 0.19 | -0.02 | 0.40 |
| other2 | Kanal 3 | 11/11 | 0.41 | 0.03 | 0.30 |
| fs8 | Kanal 4 | 11/11 | 0.12 | 0.12 | 0.11 |
| usb1k | Kanal 4 | 11/11 | 0.20 | 0.12 | 0.11 |
| other1 | Kanal 4 | 11/11 | 0.15 | -0.03 | 0.16 |
| other2 | Kanal 4 | 11/11 | 0.41 | -0.66 | 0.31 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.93 | 0.31 s (3.20 Hz) | 22.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.96 | 0.14 s (7.17 Hz) | 20.6 |
| Kanal 2 | breitbandig | 1.75 | 0.31 s (3.20 Hz) | 22.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 23.0 |
| Kanal 3 | breitbandig | 3.34 | 15.00 s (0.07 Hz) | 24.4 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 28.0 |
| Kanal 4 | breitbandig | 0.90 | 0.31 s (3.20 Hz) | 19.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 22.0 |

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
| Kanal 1 | 1.00 | 0.91 | 0.92 | 0.74 |
| Kanal 2 | 0.91 | 1.00 | 0.83 | 0.87 |
| Kanal 3 | 0.92 | 0.83 | 1.00 | 0.64 |
| Kanal 4 | 0.74 | 0.87 | 0.64 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](D90b-nach-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D90b-nach-r2_psd.png)

### Kammprofile

![Kammprofile](D90b-nach-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](D90b-nach-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:11:04. Stream-Meldungen: 0. owl_read: out/owl_read/D90b-nach-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. D90b nachher: Draht Pin 15 (GND) ↔ Pin 33 (AGND) auf der Rückseite des Xibeca-Moduls, acdc1 im Case, Regler 63/64/71/50, keine Kabel, Slot 1
