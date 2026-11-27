# Report B7-fx5a-b-r1: B7-fx5a-b-r1 – acdc1 fx5a-open-inputs-7b, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a |
| test | Build-7-Sitzung: fx5a (fx4b + Patch 16) am Ende, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx5a-open-inputs-7b-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx5a-b-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -65.9 | -67.0 | -72.3 | -73.1 | -85.3 | -72.7 | -94.5 | -72.3 | 63 % | -76.7 | 4.4 |
| Kanal 2 | -7.0 | -68.2 | -70.0 | -72.9 | -73.6 | -87.3 | -73.2 | -94.9 | -73.0 | 70 % | -78.2 | 5.2 |
| Kanal 3 | -5.2 | -69.0 | -70.4 | -74.9 | -75.6 | -91.6 | -75.1 | -95.8 | -74.9 | 80 % | -81.9 | 7.0 |
| Kanal 4 | -6.2 | -68.8 | -71.6 | -72.1 | -72.7 | -87.6 | -72.4 | -95.2 | -72.1 | 72 % | -77.6 | 5.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.8 dB | -83.2 | 8.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8665 | 0.0002 | 23/23 | k=1: 999.866 Hz, -73.7 dB | -74.9 | 55.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0018 | 10/10 | k=2: 4641.090 Hz, -115.6 dB | -111.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9751 | 0.0005 | 2/19 | k=1: 49.975 Hz, -97.0 dB | -99.6 | 0.2 % |
| Mischprodukte n·999.8665 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8665 | 0.0011 | 6 | k=-3·f1+4·f2: 21000.401 Hz, -119.5 dB | -116.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0004 | 8/11 | k=1: 1999.999 Hz, -97.7 dB | -96.2 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.1 dB | -83.4 | 9.1 % |
| 1-kHz-Kamm | Kanal 2 | 999.8665 | 0.0002 | 23/23 | k=1: 999.867 Hz, -73.9 dB | -75.1 | 60.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0011 | 10/10 | k=9: 20884.904 Hz, -114.4 dB | -109.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9753 | 0.0003 | 2/19 | k=1: 49.976 Hz, -97.8 dB | -100.5 | 0.2 % |
| Mischprodukte n·999.8665 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8665 | 0.0032 | 12 | k=-7·f1+4·f2: 17000.933 Hz, -120.2 dB | -114.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -96.7 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.9 dB | -84.0 | 12.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8665 | 0.0002 | 23/23 | k=1: 999.867 Hz, -75.6 dB | -76.6 | 67.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0009 | 10/10 | k=2: 4641.089 Hz, -117.6 dB | -112.9 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9735 | 0.0033 | 3/19 | k=1: 49.976 Hz, -98.3 dB | -100.9 | 0.3 % |
| Mischprodukte n·999.8665 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8665 | 0.0034 | 22 | k=-3·f1+4·f2: 21000.402 Hz, -120.4 dB | -113.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -100.0 dB | -97.6 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.3 dB | -100.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.3 dB | -83.6 | 7.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8665 | 0.0002 | 23/23 | k=1: 999.867 Hz, -72.8 dB | -74.1 | 64.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0014 | 10/10 | k=2: 4641.090 Hz, -115.8 dB | -111.3 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9748 | 0.0007 | 2/19 | k=1: 49.975 Hz, -98.6 dB | -101.2 | 0.1 % |
| Mischprodukte n·999.8665 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8665 | 0.0058 | 10 | k=-23·f1+4·f2: 1003.083 Hz, -113.4 dB | -111.5 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -97.0 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.8 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -73.7 | 56.9 | usb1k·1 |
| 1999.733 | -81.4 | 51.2 | usb1k·2 |
| 2999.600 | -83.2 | 49.9 | usb1k·3 |
| 12000.000 | -83.8 | 53.5 | fs8·2 |
| 6000.000 | -84.6 | 50.9 | fs8·1 |
| 18000.000 | -87.1 | 50.5 | fs8·3 |
| 3999.466 | -87.3 | 47.2 | usb1k·4 |
| 9998.665 | -88.6 | 48.4 | usb1k·10 |
| 4999.333 | -89.8 | 45.7 | usb1k·5 |
| 15997.864 | -90.8 | 46.8 | usb1k·16 |
| 6999.066 | -91.6 | 44.4 | usb1k·7 |
| 8998.798 | -91.7 | 45.0 | usb1k·9 |
| 18997.464 | -92.9 | 45.6 | usb1k·19 |
| 16997.731 | -92.9 | 45.5 | usb1k·17 |
| 5999.199 | -94.6 | 41.0 | usb1k·6 |
| 7998.932 | -95.3 | 41.3 | usb1k·8 |
| 11998.398 | -95.3 | 42.0 | usb1k·12 |
| 12998.265 | -96.5 | 41.6 | usb1k·13 |
| 20997.197 | -96.4 | 42.3 | usb1k·21 |
| 1999.999 | -97.7 | 34.9 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.9 | 58.3 | usb1k·1 |
| 1999.733 | -81.4 | 52.6 | usb1k·2 |
| 2999.600 | -83.6 | 50.8 | usb1k·3 |
| 12000.000 | -84.1 | 54.6 | fs8·2 |
| 6000.000 | -84.7 | 51.9 | fs8·1 |
| 18000.000 | -87.1 | 52.0 | fs8·3 |
| 3999.466 | -87.5 | 48.6 | usb1k·4 |
| 9998.665 | -88.8 | 49.8 | usb1k·10 |
| 4999.333 | -89.7 | 47.0 | usb1k·5 |
| 15997.864 | -90.8 | 48.2 | usb1k·16 |
| 8998.798 | -91.5 | 46.5 | usb1k·9 |
| 6999.066 | -92.2 | 45.5 | usb1k·7 |
| 18997.464 | -92.9 | 46.5 | usb1k·19 |
| 16997.731 | -93.2 | 46.1 | usb1k·17 |
| 5999.198 | -94.9 | 41.7 | usb1k·6 |
| 11998.398 | -95.4 | 43.4 | usb1k·12 |
| 7998.932 | -95.6 | 42.6 | usb1k·8 |
| 12998.265 | -96.3 | 42.9 | usb1k·13 |
| 20997.197 | -96.5 | 43.3 | usb1k·21 |
| 2000.000 | -98.4 | 35.7 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.6 | 61.5 | usb1k·1 |
| 1999.733 | -83.2 | 55.5 | usb1k·2 |
| 2999.600 | -84.8 | 54.2 | usb1k·3 |
| 12000.000 | -84.9 | 56.7 | fs8·2 |
| 6000.000 | -85.4 | 55.4 | fs8·1 |
| 18000.000 | -87.5 | 53.9 | fs8·3 |
| 3999.466 | -88.3 | 51.7 | usb1k·4 |
| 9998.665 | -89.2 | 52.5 | usb1k·10 |
| 4999.333 | -90.9 | 49.9 | usb1k·5 |
| 15997.865 | -91.4 | 50.1 | usb1k·16 |
| 8998.798 | -92.6 | 48.8 | usb1k·9 |
| 6999.066 | -93.2 | 48.0 | usb1k·7 |
| 18997.464 | -93.1 | 48.6 | usb1k·19 |
| 16997.731 | -93.8 | 47.9 | usb1k·17 |
| 11998.398 | -96.0 | 45.5 | usb1k·12 |
| 12998.265 | -96.6 | 45.6 | usb1k·13 |
| 5999.199 | -96.7 | 44.1 | usb1k·6 |
| 7998.932 | -96.9 | 44.6 | usb1k·8 |
| 20997.197 | -97.5 | 44.4 | usb1k·21 |
| 19997.331 | -99.0 | 42.5 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.8 | 59.0 | usb1k·1 |
| 1999.733 | -79.9 | 53.7 | usb1k·2 |
| 2999.600 | -83.0 | 51.1 | usb1k·3 |
| 12000.000 | -84.3 | 53.3 | fs8·2 |
| 6000.000 | -84.8 | 51.0 | fs8·1 |
| 3999.466 | -87.1 | 48.3 | usb1k·4 |
| 18000.000 | -87.5 | 51.1 | fs8·3 |
| 4999.333 | -88.6 | 47.7 | usb1k·5 |
| 9998.665 | -88.9 | 48.5 | usb1k·10 |
| 15997.865 | -90.4 | 47.6 | usb1k·16 |
| 8998.798 | -90.7 | 46.5 | usb1k·9 |
| 6999.066 | -91.7 | 45.0 | usb1k·7 |
| 5999.199 | -92.9 | 42.9 | usb1k·6 |
| 18997.464 | -93.0 | 45.5 | usb1k·19 |
| 16997.731 | -93.0 | 45.1 | usb1k·17 |
| 7998.932 | -94.1 | 42.5 | usb1k·8 |
| 11998.398 | -94.8 | 42.7 | usb1k·12 |
| 20997.197 | -96.0 | 42.7 | usb1k·21 |
| 12998.265 | -96.1 | 41.8 | usb1k·13 |
| 13998.131 | -98.3 | 40.2 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.24 | 0.64 | 0.10 |
| led | Kanal 1 | 11/11 | 1.62 | 0.56 | 0.57 |
| mains50 | Kanal 1 | 11/11 | 753.03 | 628.04 | 1.08 |
| other1 | Kanal 1 | 11/11 | 0.16 | -0.04 | 0.18 |
| other2 | Kanal 1 | 11/11 | 0.23 | -0.17 | 0.12 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.23 | 0.59 | 0.05 |
| led | Kanal 2 | 11/11 | 0.26 | 0.13 | 0.40 |
| mains50 | Kanal 2 | 11/11 | 356.79 | -423.80 | 1.06 |
| other1 | Kanal 2 | 11/11 | 1.87 | 2.47 | 0.12 |
| other2 | Kanal 2 | 11/11 | 0.25 | -0.21 | 0.15 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.23 | 0.57 | 0.10 |
| led | Kanal 3 | 11/11 | 0.88 | 0.04 | 0.42 |
| mains50 | Kanal 3 | 11/11 | 75.69 | 231.37 | 0.45 |
| other1 | Kanal 3 | 11/11 | 1.27 | 1.63 | 0.15 |
| other2 | Kanal 3 | 11/11 | 0.18 | -0.05 | 0.10 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.22 | 0.61 | 0.04 |
| led | Kanal 4 | 11/11 | 1.39 | 0.76 | 0.54 |
| mains50 | Kanal 4 | 11/11 | 428.54 | -868.25 | 1.11 |
| other1 | Kanal 4 | 11/11 | 1.98 | 0.81 | 0.09 |
| other2 | Kanal 4 | 11/11 | 0.25 | -0.31 | 0.22 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.53 | 0.31 s (3.22 Hz) | 34.4 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 35.3 |
| Kanal 2 | breitbandig | 2.89 | 0.31 s (3.22 Hz) | 35.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 37.3 |
| Kanal 3 | breitbandig | 3.18 | 0.31 s (3.22 Hz) | 35.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 42.3 |
| Kanal 4 | breitbandig | 2.30 | 0.31 s (3.22 Hz) | 35.0 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 35.6 |

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
| Kanal 1 | 1.00 | 0.98 | 0.98 | 0.93 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.98 | 0.96 | 1.00 | 0.91 |
| Kanal 4 | 0.93 | 0.97 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx5a-b-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx5a-b-r1_psd.png)

### Kammprofile

![Kammprofile](B7-fx5a-b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx5a-b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:22:50. Stream-Meldungen: 0. owl_read: reports/owl_read/B7-fx5a-b-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
