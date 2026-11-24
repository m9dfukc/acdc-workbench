# Report D90-vor-r2: D90-vor-r2 – acdc1 gnd-vor-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | gnd-vor-open-inputs |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_gnd-vor-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis D90-vor-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -66.1 | -67.4 | -71.9 | -72.7 | -85.7 | -72.3 | -96.0 | -72.0 | 69 % | -77.0 | 5.1 |
| Kanal 2 | -6.8 | -68.2 | -70.4 | -72.4 | -73.0 | -87.8 | -72.6 | -96.4 | -72.4 | 74 % | -78.3 | 5.9 |
| Kanal 3 | -5.0 | -69.1 | -70.7 | -74.3 | -75.0 | -92.1 | -74.5 | -97.3 | -74.3 | 84 % | -82.3 | 8.0 |
| Kanal 4 | -6.1 | -68.3 | -70.8 | -71.9 | -72.5 | -87.8 | -72.1 | -96.6 | -71.9 | 72 % | -77.5 | 5.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.1 dB | -82.3 | 9.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8657 | 0.0002 | 23/23 | k=1: 999.866 Hz, -73.1 dB | -74.2 | 59.6 % |
| Netz 50 Hz | Kanal 1 | 50.0319 | 0.0027 | 2/19 | k=1: 50.028 Hz, -104.8 dB | -107.2 | 0.0 % |
| Mischprodukte n·999.8657 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8657 | 0.0025 | 6 | k=-7·f1+4·f2: 17000.937 Hz, -119.4 dB | -116.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -98.8 dB | -97.7 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -100.9 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.4 dB | -82.5 | 9.8 % |
| 1-kHz-Kamm | Kanal 2 | 999.8657 | 0.0002 | 23/23 | k=1: 999.866 Hz, -73.1 dB | -74.3 | 64.4 % |
| Netz 50 Hz | Kanal 2 | 50.0292 | 0.0000 | 1/19 | k=1: 50.029 Hz, -105.0 dB | -107.9 | 0.0 % |
| Mischprodukte n·999.8657 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8657 | 0.0021 | 13 | k=-7·f1+4·f2: 17000.937 Hz, -120.0 dB | -113.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -99.6 dB | -98.1 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -100.5 dB | -101.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.1 dB | -83.0 | 13.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8657 | 0.0002 | 23/23 | k=1: 999.866 Hz, -74.9 dB | -75.9 | 70.5 % |
| Netz 50 Hz | Kanal 3 | 50.0313 | 0.0028 | 6/19 | k=1: 50.029 Hz, -106.9 dB | -108.8 | 0.0 % |
| Mischprodukte n·999.8657 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8657 | 0.0044 | 31 | k=-23·f1+4·f2: 1003.078 Hz, -118.8 dB | -111.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -101.3 dB | -99.1 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -101.8 dB | -102.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.6 dB | -82.6 | 8.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8657 | 0.0002 | 23/23 | k=1: 999.866 Hz, -72.6 dB | -73.8 | 64.0 % |
| Netz 50 Hz | Kanal 4 | 50.0291 | 0.0000 | 1/19 | k=1: 50.029 Hz, -105.5 dB | -108.5 | 0.0 % |
| Mischprodukte n·999.8657 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8657 | 0.0040 | 9 | k=-23·f1+4·f2: 1003.081 Hz, -114.3 dB | -112.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0005 | 8/11 | k=1: 1999.999 Hz, -99.8 dB | -98.3 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.7 dB | -101.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -73.1 | 55.1 | usb1k·1 |
| 1999.731 | -80.7 | 50.5 | usb1k·2 |
| 2999.597 | -82.3 | 52.2 | usb1k·3 |
| 12000.000 | -83.1 | 54.9 | fs8·2 |
| 6000.000 | -83.5 | 52.6 | fs8·1 |
| 18000.000 | -86.1 | 52.2 | fs8·3 |
| 3999.462 | -86.5 | 45.8 | usb1k·4 |
| 9998.657 | -87.2 | 50.2 | usb1k·10 |
| 4999.328 | -88.6 | 47.0 | usb1k·5 |
| 15997.851 | -89.8 | 47.0 | usb1k·16 |
| 18997.448 | -91.2 | 46.6 | usb1k·19 |
| 16997.716 | -91.7 | 45.5 | usb1k·17 |
| 6999.059 | -90.8 | 45.5 | usb1k·7 |
| 8998.791 | -90.9 | 46.1 | usb1k·9 |
| 11998.388 | -93.8 | 44.2 | usb1k·12 |
| 5999.194 | -93.7 | 42.4 | usb1k·6 |
| 12998.254 | -95.3 | 42.2 | usb1k·13 |
| 20997.179 | -95.8 | 42.0 | usb1k·21 |
| 19997.313 | -96.2 | 41.7 | usb1k·20 |
| 7998.926 | -95.0 | 40.9 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -73.1 | 57.4 | usb1k·1 |
| 1999.731 | -80.8 | 52.3 | usb1k·2 |
| 2999.597 | -82.4 | 53.1 | usb1k·3 |
| 12000.000 | -83.4 | 55.8 | fs8·2 |
| 6000.000 | -83.6 | 53.9 | fs8·1 |
| 18000.000 | -86.2 | 53.1 | fs8·3 |
| 3999.462 | -86.5 | 47.6 | usb1k·4 |
| 9998.657 | -87.3 | 51.3 | usb1k·10 |
| 4999.328 | -88.8 | 48.0 | usb1k·5 |
| 15997.851 | -89.9 | 48.5 | usb1k·16 |
| 18997.448 | -91.2 | 47.5 | usb1k·19 |
| 16997.716 | -91.8 | 46.8 | usb1k·17 |
| 6999.060 | -91.0 | 46.4 | usb1k·7 |
| 8998.791 | -91.1 | 46.8 | usb1k·9 |
| 11998.388 | -93.9 | 45.3 | usb1k·12 |
| 5999.194 | -94.1 | 43.4 | usb1k·6 |
| 12998.254 | -95.4 | 43.1 | usb1k·13 |
| 20997.179 | -96.0 | 43.4 | usb1k·21 |
| 7998.925 | -94.9 | 42.2 | usb1k·8 |
| 19997.313 | -96.3 | 43.0 | usb1k·20 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -74.9 | 59.5 | usb1k·1 |
| 1999.731 | -82.6 | 54.8 | usb1k·2 |
| 2999.597 | -83.8 | 56.3 | usb1k·3 |
| 12000.000 | -84.1 | 58.1 | fs8·2 |
| 6000.000 | -84.2 | 57.5 | fs8·1 |
| 18000.000 | -86.4 | 55.4 | fs8·3 |
| 3999.463 | -87.4 | 50.8 | usb1k·4 |
| 9998.657 | -87.8 | 54.1 | usb1k·10 |
| 4999.328 | -89.6 | 51.3 | usb1k·5 |
| 15997.851 | -90.4 | 50.8 | usb1k·16 |
| 18997.448 | -91.5 | 50.2 | usb1k·19 |
| 16997.716 | -92.6 | 48.9 | usb1k·17 |
| 8998.791 | -91.8 | 50.0 | usb1k·9 |
| 6999.059 | -92.1 | 49.2 | usb1k·7 |
| 11998.388 | -94.5 | 47.6 | usb1k·12 |
| 12998.254 | -95.4 | 45.9 | usb1k·13 |
| 19997.313 | -96.4 | 45.8 | usb1k·20 |
| 5999.194 | -95.8 | 45.9 | usb1k·6 |
| 20997.179 | -97.0 | 45.0 | usb1k·21 |
| 7998.925 | -96.3 | 44.8 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -72.6 | 57.5 | usb1k·1 |
| 1999.731 | -79.8 | 52.7 | usb1k·2 |
| 2999.597 | -82.4 | 52.4 | usb1k·3 |
| 12000.000 | -83.6 | 54.6 | fs8·2 |
| 6000.000 | -83.7 | 52.7 | fs8·1 |
| 18000.000 | -86.5 | 51.5 | fs8·3 |
| 3999.462 | -86.5 | 46.9 | usb1k·4 |
| 9998.657 | -87.6 | 50.1 | usb1k·10 |
| 4999.328 | -88.2 | 47.9 | usb1k·5 |
| 15997.851 | -89.8 | 47.4 | usb1k·16 |
| 18997.448 | -91.3 | 46.6 | usb1k·19 |
| 8998.791 | -90.4 | 46.8 | usb1k·9 |
| 16997.716 | -91.9 | 45.8 | usb1k·17 |
| 6999.060 | -91.1 | 45.8 | usb1k·7 |
| 5999.194 | -93.0 | 43.3 | usb1k·6 |
| 11998.388 | -93.8 | 44.3 | usb1k·12 |
| 12998.254 | -95.3 | 42.7 | usb1k·13 |
| 7998.925 | -94.2 | 41.7 | usb1k·8 |
| 20997.179 | -95.6 | 42.6 | usb1k·21 |
| 19997.313 | -96.6 | 42.0 | usb1k·20 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.00 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.17 | 0.41 | 0.15 |
| mains50 | Kanal 1 | 11/11 | 1567.92 | -1376.49 | 2.77 |
| other1 | Kanal 1 | 11/11 | 1.84 | 3.36 | 0.20 |
| other2 | Kanal 1 | 11/11 | 0.27 | 0.21 | 0.17 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.19 | 0.38 | 0.04 |
| mains50 | Kanal 2 | 11/11 | 1814.01 | 318.53 | 2.25 |
| other1 | Kanal 2 | 11/11 | 1.80 | 3.35 | 0.14 |
| other2 | Kanal 2 | 11/11 | 0.17 | -0.02 | 0.16 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.14 | 0.23 | 0.14 |
| mains50 | Kanal 3 | 11/11 | 146.05 | 332.23 | 1.28 |
| other1 | Kanal 3 | 11/11 | 1.70 | -2.89 | 0.15 |
| other2 | Kanal 3 | 11/11 | 0.17 | 0.14 | 0.09 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.23 | 0.57 | 0.07 |
| mains50 | Kanal 4 | 11/11 | 1872.19 | 525.54 | 2.10 |
| other1 | Kanal 4 | 11/11 | 2.25 | 2.83 | 0.13 |
| other2 | Kanal 4 | 11/11 | 0.22 | -0.10 | 0.18 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.24 | 0.31 s (3.18 Hz) | 34.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 31.6 |
| Kanal 2 | breitbandig | 2.66 | 0.31 s (3.18 Hz) | 35.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 33.6 |
| Kanal 3 | breitbandig | 2.92 | 0.31 s (3.22 Hz) | 35.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.9 |
| Kanal 4 | breitbandig | 2.49 | 0.31 s (3.18 Hz) | 35.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 31.8 |

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
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.98 |
| Kanal 3 | 0.98 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.98 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](D90-vor-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](D90-vor-r2_psd.png)

### Kammprofile

![Kammprofile](D90-vor-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](D90-vor-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 22:42:18. Stream-Meldungen: 0. owl_read: out/owl_read/D90-vor-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
