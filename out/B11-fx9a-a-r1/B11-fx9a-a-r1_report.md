# Report B11-fx9a-a-r1: B11-fx9a-a-r1 – acdc1 fx9a-open-inputs-11a, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | fx9a-open-inputs-11a |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx9a-open-inputs-11a-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B11-fx9a-a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -72.0 | -80.9 | -72.6 | -73.3 | -87.5 | -72.9 | -97.3 | -72.6 | 70 % | -77.8 | 5.2 |
| Kanal 2 | -7.5 | -72.7 | -81.6 | -73.3 | -74.0 | -89.1 | -73.6 | -95.7 | -73.3 | 74 % | -79.1 | 5.8 |
| Kanal 3 | -5.7 | -74.5 | -87.1 | -74.7 | -75.3 | -94.0 | -74.9 | -95.5 | -74.7 | 85 % | -82.9 | 8.2 |
| Kanal 4 | -6.5 | -71.8 | -81.1 | -72.3 | -72.8 | -89.2 | -72.5 | -101.2 | -72.3 | 77 % | -78.7 | 6.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -82.7 | 9.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -74.8 | 60.0 % |
| Netz 50 Hz | Kanal 1 | 49.9653 | 0.0140 | 3/19 | k=3: 149.880 Hz, -108.7 dB | -106.8 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0043 | 16 | k=36·f1-4·f2: 11995.236 Hz, -114.8 dB | -109.1 | 0.0 % |
| stärkste übrige Linie (51.16 Hz) | Kanal 1 | 51.1848 | 0.0171 | 8/466 | k=1: 51.157 Hz, -100.2 dB | -99.7 | 0.2 % |
| stärkste übrige Linie (18.74 Hz) | Kanal 1 | 18.7290 | 0.0158 | 11/1274 | k=1: 18.736 Hz, -102.6 dB | -101.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -82.8 | 11.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.4 | 62.4 % |
| Netz 50 Hz | Kanal 2 | 49.9652 | 0.0134 | 3/19 | k=3: 149.880 Hz, -109.8 dB | -107.5 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0039 | 19 | k=-23·f1+4·f2: 1003.063 Hz, -115.7 dB | -110.3 | 0.0 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 2 | 1000.0001 | 0.0005 | 20/23 | k=1: 1000.001 Hz, -103.0 dB | -96.4 | 0.5 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 2 | 1215.1899 | 0.0010 | 10/19 | k=1: 1215.190 Hz, -102.6 dB | -103.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -83.3 | 13.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.1 dB | -76.2 | 71.0 % |
| Netz 50 Hz | Kanal 3 | 49.9641 | 0.0265 | 5/19 | k=3: 149.879 Hz, -115.2 dB | -111.5 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0037 | 30 | k=36·f1-4·f2: 11995.237 Hz, -121.3 dB | -111.9 | 0.0 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0004 | 20/23 | k=1: 1000.002 Hz, -104.0 dB | -96.9 | 0.6 % |
| stärkste übrige Linie (1500.00 Hz) | Kanal 3 | 1500.0002 | 0.0003 | 8/15 | k=1: 1500.001 Hz, -104.7 dB | -101.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.5 dB | -83.0 | 8.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.6 dB | -74.0 | 68.4 % |
| Netz 50 Hz | Kanal 4 | 49.9651 | 0.0134 | 3/19 | k=3: 149.879 Hz, -109.8 dB | -107.7 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0044 | 17 | k=-23·f1+4·f2: 1003.063 Hz, -112.4 dB | -109.2 | 0.0 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1899 | 0.0019 | 11/19 | k=1: 1215.190 Hz, -102.5 dB | -103.5 | 0.1 % |
| stärkste übrige Linie (7384.62 Hz) | Kanal 4 | 7384.6154 | 0.0002 | 3/3 | k=1: 7384.615 Hz, -103.8 dB | -105.0 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 58.2 | usb1k·1 |
| 1999.735 | -82.1 | 51.6 | usb1k·2 |
| 2999.603 | -82.9 | 51.7 | usb1k·3 |
| 6000.000 | -83.4 | 52.5 | fs8·1 |
| 12000.000 | -84.4 | 52.6 | fs8·2 |
| 18000.000 | -86.1 | 52.6 | fs8·3 |
| 3999.470 | -86.6 | 48.8 | usb1k·4 |
| 9998.675 | -88.0 | 49.2 | usb1k·10 |
| 4999.338 | -89.9 | 45.3 | usb1k·5 |
| 15997.879 | -90.2 | 48.2 | usb1k·16 |
| 6999.073 | -90.0 | 46.7 | usb1k·7 |
| 8998.807 | -91.4 | 45.8 | usb1k·9 |
| 16997.747 | -92.6 | 45.9 | usb1k·17 |
| 18997.482 | -93.6 | 44.9 | usb1k·19 |
| 20997.217 | -94.4 | 43.7 | usb1k·21 |
| 5999.205 | -94.6 | 41.2 | usb1k·6 |
| 13998.144 | -96.6 | 41.2 | usb1k·14 |
| 7998.940 | -96.5 | 40.6 | usb1k·8 |
| 17997.614 | -97.3 | 41.2 | usb1k·18 |
| 11998.409 | -96.2 | 40.4 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 58.8 | usb1k·1 |
| 1999.735 | -83.0 | 52.1 | usb1k·2 |
| 6000.000 | -83.4 | 53.9 | fs8·1 |
| 2999.603 | -83.3 | 52.5 | usb1k·3 |
| 12000.000 | -84.7 | 53.8 | fs8·2 |
| 18000.000 | -86.1 | 53.5 | fs8·3 |
| 3999.470 | -86.8 | 49.9 | usb1k·4 |
| 9998.675 | -87.9 | 50.6 | usb1k·10 |
| 4999.338 | -90.3 | 46.5 | usb1k·5 |
| 15997.879 | -90.5 | 48.8 | usb1k·16 |
| 6999.073 | -90.5 | 47.2 | usb1k·7 |
| 16997.747 | -92.7 | 46.9 | usb1k·17 |
| 8998.807 | -91.7 | 46.5 | usb1k·9 |
| 18997.482 | -93.6 | 46.3 | usb1k·19 |
| 20997.217 | -94.9 | 44.2 | usb1k·21 |
| 5999.205 | -95.1 | 42.1 | usb1k·6 |
| 17997.614 | -97.3 | 42.1 | usb1k·18 |
| 11998.409 | -96.5 | 41.6 | usb1k·12 |
| 7998.940 | -97.0 | 41.4 | usb1k·8 |
| 12998.277 | -97.2 | 41.4 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.1 | 62.5 | usb1k·1 |
| 6000.000 | -83.8 | 57.2 | fs8·1 |
| 1999.735 | -83.8 | 55.4 | usb1k·2 |
| 2999.603 | -84.2 | 56.2 | usb1k·3 |
| 12000.000 | -85.4 | 56.3 | fs8·2 |
| 18000.000 | -86.5 | 55.8 | fs8·3 |
| 3999.470 | -87.4 | 53.3 | usb1k·4 |
| 9998.675 | -88.3 | 53.9 | usb1k·10 |
| 15997.879 | -90.9 | 51.3 | usb1k·16 |
| 4999.337 | -91.0 | 50.0 | usb1k·5 |
| 6999.073 | -91.3 | 50.2 | usb1k·7 |
| 16997.747 | -93.3 | 48.8 | usb1k·17 |
| 8998.807 | -92.2 | 49.5 | usb1k·9 |
| 18997.482 | -93.9 | 48.0 | usb1k·19 |
| 20997.217 | -95.3 | 46.2 | usb1k·21 |
| 5999.205 | -96.6 | 44.4 | usb1k·6 |
| 17997.614 | -97.5 | 44.7 | usb1k·18 |
| 12998.277 | -97.3 | 44.8 | usb1k·13 |
| 11998.409 | -96.9 | 44.4 | usb1k·12 |
| 7998.940 | -97.7 | 44.0 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.6 | 60.2 | usb1k·1 |
| 1999.735 | -81.0 | 53.9 | usb1k·2 |
| 2999.603 | -82.3 | 52.9 | usb1k·3 |
| 6000.000 | -83.5 | 53.0 | fs8·1 |
| 12000.000 | -84.9 | 52.8 | fs8·2 |
| 18000.000 | -86.2 | 52.6 | fs8·3 |
| 3999.470 | -86.4 | 49.7 | usb1k·4 |
| 4999.338 | -88.9 | 47.5 | usb1k·5 |
| 9998.675 | -88.1 | 50.1 | usb1k·10 |
| 15997.879 | -89.8 | 48.9 | usb1k·16 |
| 6999.073 | -89.7 | 47.7 | usb1k·7 |
| 8998.807 | -90.7 | 46.8 | usb1k·9 |
| 16997.747 | -92.4 | 46.8 | usb1k·17 |
| 5999.205 | -92.7 | 43.8 | usb1k·6 |
| 18997.482 | -93.8 | 45.3 | usb1k·19 |
| 20997.217 | -94.5 | 44.2 | usb1k·21 |
| 7998.940 | -94.7 | 43.1 | usb1k·8 |
| 11998.409 | -95.5 | 41.8 | usb1k·12 |
| 13998.144 | -96.0 | 42.4 | usb1k·14 |
| 12998.277 | -97.2 | 40.5 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.03 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.13 | 0.03 | 0.03 |
| mains50 | Kanal 1 | 11/11 | 263.21 | -288.49 | 0.67 |
| other1 | Kanal 1 | 11/11 | 9.34 | -0.21 | 1.57 |
| other2 | Kanal 1 | 11/11 | 276.07 | -393.09 | 1.26 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.15 | -0.02 | 0.03 |
| mains50 | Kanal 2 | 11/11 | 262.79 | -291.84 | 0.63 |
| other1 | Kanal 2 | 11/11 | 9.93 | -24.63 | 0.03 |
| other2 | Kanal 2 | 11/11 | 0.45 | -0.13 | 0.39 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.02 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.12 | -0.08 | 0.02 |
| mains50 | Kanal 3 | 11/11 | 260.23 | -387.07 | 0.95 |
| other1 | Kanal 3 | 11/11 | 6.81 | -16.13 | 0.02 |
| other2 | Kanal 3 | 11/11 | 0.35 | -0.31 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.12 | -0.02 | 0.03 |
| mains50 | Kanal 4 | 11/11 | 248.77 | -153.60 | 0.62 |
| other1 | Kanal 4 | 11/11 | 0.45 | 0.26 | 0.34 |
| other2 | Kanal 4 | 11/11 | 0.10 | -0.15 | 0.29 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.74 | 0.16 s (6.40 Hz) | 19.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 36.6 |
| Kanal 2 | breitbandig | 0.70 | 0.16 s (6.40 Hz) | 21.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.3 |
| Kanal 3 | breitbandig | 0.41 | 7.50 s (0.13 Hz) | 22.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 40.5 |
| Kanal 4 | breitbandig | 0.63 | 0.16 s (6.40 Hz) | 22.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 35.9 |

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
| Kanal 1 | 1.00 | 0.96 | 0.93 | 0.95 |
| Kanal 2 | 0.96 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.93 | 0.93 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.96 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B11-fx9a-a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B11-fx9a-a-r1_psd.png)

### Kammprofile

![Kammprofile](B11-fx9a-a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B11-fx9a-a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:15:13. Stream-Meldungen: 0. owl_read: out/owl_read/B11-fx9a-a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 11 v22.4.r-fx9a (D-Cache an), Sandwich Anfang. Eingänge offen, keine Kabel, Slot 1 vor dem Stream per Program Change, Regler 69/56/72/56 von 127, acdc1 im Case. Zustand des Oszillators im Case nicht erfragt. messlog D89.
