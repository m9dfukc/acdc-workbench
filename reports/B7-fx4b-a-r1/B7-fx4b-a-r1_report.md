# Report B7-fx4b-a-r1: B7-fx4b-a-r1 – acdc1 fx4b-open-inputs-7a, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-7-Sitzung: fx4b-Kontrolle am Anfang, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx4b-open-inputs-7a-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx4b-a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.6 | -78.2 | -72.6 | -73.4 | -85.5 | -73.0 | -94.3 | -72.6 | 64 % | -77.1 | 4.4 |
| Kanal 2 | -7.5 | -72.5 | -79.3 | -73.6 | -74.4 | -87.4 | -73.9 | -94.6 | -73.6 | 68 % | -78.5 | 4.9 |
| Kanal 3 | -5.7 | -74.1 | -84.4 | -74.5 | -75.1 | -92.1 | -74.7 | -95.5 | -74.6 | 83 % | -82.2 | 7.6 |
| Kanal 4 | -6.5 | -71.9 | -79.6 | -72.7 | -73.4 | -87.7 | -73.0 | -94.9 | -72.8 | 71 % | -78.1 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.7 dB | -83.0 | 9.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.3 | 54.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.545 Hz, -112.7 dB | -108.6 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0002 | 0.0141 | 3/19 | k=1: 50.006 Hz, -97.2 dB | -98.3 | 0.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0023 | 9 | k=3·f1+2·f2: 14999.602 Hz, -120.7 dB | -115.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -96.2 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -98.8 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.9 dB | -83.1 | 11.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.1 | 56.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0005 | 10/10 | k=9: 20884.904 Hz, -112.7 dB | -107.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0002 | 0.0118 | 4/19 | k=1: 50.006 Hz, -97.6 dB | -98.6 | 0.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0044 | 18 | k=-1·f1+1·f2: 5000.130 Hz, -120.4 dB | -113.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -96.5 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.6 dB | -99.2 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.7 dB | -83.7 | 12.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -76.1 | 70.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0008 | 10/10 | k=2: 4641.089 Hz, -113.7 dB | -109.0 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0001 | 0.0109 | 6/19 | k=1: 50.006 Hz, -98.8 dB | -99.4 | 0.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0028 | 36 | k=-1·f1+2·f2: 11000.134 Hz, -121.2 dB | -111.9 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.7 dB | -100.0 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.7 dB | -97.4 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.0 dB | -83.3 | 8.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -74.9 | 61.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.545 Hz, -112.3 dB | -108.0 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0002 | 0.0109 | 4/19 | k=1: 50.006 Hz, -98.2 dB | -99.0 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0018 | 15 | k=-1·f1+1·f2: 5000.133 Hz, -117.0 dB | -112.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.5 dB | -96.8 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -98.9 dB | -99.5 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 57.0 | usb1k·1 |
| 1999.735 | -82.0 | 49.9 | usb1k·2 |
| 2999.603 | -83.4 | 50.8 | usb1k·3 |
| 12000.000 | -83.7 | 54.7 | fs8·2 |
| 6000.000 | -84.3 | 52.1 | fs8·1 |
| 18000.000 | -86.8 | 51.9 | fs8·3 |
| 3999.471 | -87.2 | 47.7 | usb1k·4 |
| 9998.677 | -88.4 | 49.3 | usb1k·10 |
| 4999.339 | -89.8 | 45.7 | usb1k·5 |
| 15997.883 | -90.6 | 47.9 | usb1k·16 |
| 6999.074 | -90.7 | 45.8 | usb1k·7 |
| 8998.809 | -91.1 | 46.2 | usb1k·9 |
| 16997.750 | -93.6 | 45.0 | usb1k·17 |
| 18997.486 | -93.8 | 44.7 | usb1k·19 |
| 20997.221 | -94.6 | 44.3 | usb1k·21 |
| 5999.206 | -94.7 | 41.9 | usb1k·6 |
| 12998.280 | -96.9 | 41.0 | usb1k·13 |
| 11998.412 | -96.8 | 41.6 | usb1k·12 |
| 2000.000 | -97.6 | 34.4 | other1·1 |
| 7998.941 | -96.4 | 40.3 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 57.2 | usb1k·1 |
| 1999.735 | -83.1 | 50.6 | usb1k·2 |
| 12000.000 | -83.9 | 55.9 | fs8·2 |
| 2999.603 | -84.0 | 52.2 | usb1k·3 |
| 6000.000 | -84.4 | 53.6 | fs8·1 |
| 18000.000 | -86.7 | 53.0 | fs8·3 |
| 3999.471 | -87.4 | 48.8 | usb1k·4 |
| 9998.677 | -88.4 | 50.9 | usb1k·10 |
| 15997.883 | -90.8 | 48.6 | usb1k·16 |
| 4999.339 | -90.3 | 46.5 | usb1k·5 |
| 6999.074 | -91.1 | 46.6 | usb1k·7 |
| 8998.809 | -91.6 | 46.5 | usb1k·9 |
| 16997.750 | -93.8 | 45.7 | usb1k·17 |
| 18997.486 | -93.7 | 45.8 | usb1k·19 |
| 20997.221 | -94.9 | 44.6 | usb1k·21 |
| 5999.206 | -95.8 | 42.2 | usb1k·6 |
| 12998.280 | -97.1 | 42.3 | usb1k·13 |
| 11998.412 | -97.0 | 42.8 | usb1k·12 |
| 17997.618 | -97.9 | 41.7 | usb1k·18 |
| 2000.000 | -98.1 | 35.6 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 62.8 | usb1k·1 |
| 1999.735 | -83.6 | 54.9 | usb1k·2 |
| 2999.603 | -84.1 | 56.2 | usb1k·3 |
| 12000.000 | -84.7 | 57.9 | fs8·2 |
| 6000.000 | -84.8 | 56.6 | fs8·1 |
| 18000.000 | -87.3 | 54.9 | fs8·3 |
| 3999.471 | -87.7 | 52.9 | usb1k·4 |
| 9998.677 | -88.7 | 53.7 | usb1k·10 |
| 15997.883 | -91.2 | 50.6 | usb1k·16 |
| 4999.339 | -91.0 | 50.0 | usb1k·5 |
| 6999.074 | -91.5 | 50.3 | usb1k·7 |
| 8998.809 | -92.2 | 49.6 | usb1k·9 |
| 16997.750 | -93.8 | 48.9 | usb1k·17 |
| 18997.486 | -94.1 | 48.0 | usb1k·19 |
| 20997.221 | -95.5 | 46.4 | usb1k·21 |
| 5999.206 | -96.1 | 45.4 | usb1k·6 |
| 11998.412 | -97.2 | 45.4 | usb1k·12 |
| 12998.279 | -97.5 | 44.8 | usb1k·13 |
| 7998.941 | -96.5 | 45.4 | usb1k·8 |
| 17997.618 | -98.4 | 43.9 | usb1k·18 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 58.3 | usb1k·1 |
| 1999.736 | -81.3 | 52.6 | usb1k·2 |
| 2999.603 | -83.2 | 52.5 | usb1k·3 |
| 12000.000 | -84.0 | 54.7 | fs8·2 |
| 6000.000 | -84.7 | 52.4 | fs8·1 |
| 18000.000 | -87.0 | 51.9 | fs8·3 |
| 3999.471 | -87.1 | 48.7 | usb1k·4 |
| 4999.339 | -89.0 | 47.4 | usb1k·5 |
| 9998.677 | -88.6 | 49.6 | usb1k·10 |
| 15997.883 | -90.3 | 48.1 | usb1k·16 |
| 6999.074 | -90.4 | 46.9 | usb1k·7 |
| 8998.809 | -90.6 | 47.0 | usb1k·9 |
| 16997.750 | -93.6 | 45.4 | usb1k·17 |
| 18997.486 | -93.9 | 45.1 | usb1k·19 |
| 5999.206 | -93.4 | 43.6 | usb1k·6 |
| 20997.221 | -94.5 | 44.1 | usb1k·21 |
| 11998.412 | -96.1 | 42.4 | usb1k·12 |
| 7998.941 | -95.3 | 41.9 | usb1k·8 |
| 12998.280 | -97.1 | 41.5 | usb1k·13 |
| 13998.147 | -97.4 | 41.1 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.04 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.22 | 0.05 | 0.03 |
| led | Kanal 1 | 11/11 | 0.71 | 0.77 | 0.69 |
| mains50 | Kanal 1 | 11/11 | 34.80 | -71.48 | 0.79 |
| other1 | Kanal 1 | 11/11 | 0.25 | -0.04 | 0.06 |
| other2 | Kanal 1 | 11/11 | 0.30 | -0.01 | 0.22 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.23 | 0.02 | 0.04 |
| led | Kanal 2 | 11/11 | 0.47 | 0.23 | 0.51 |
| mains50 | Kanal 2 | 11/11 | 27.67 | -57.92 | 0.61 |
| other1 | Kanal 2 | 11/11 | 0.15 | 0.02 | 0.06 |
| other2 | Kanal 2 | 11/11 | 0.26 | -0.22 | 0.19 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.02 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.19 | 0.07 | 0.02 |
| led | Kanal 3 | 11/11 | 0.45 | 0.23 | 0.33 |
| mains50 | Kanal 3 | 11/11 | 27.91 | -83.00 | 0.38 |
| other1 | Kanal 3 | 11/11 | 0.19 | -0.10 | 0.12 |
| other2 | Kanal 3 | 11/11 | 0.73 | 1.13 | 0.04 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.16 | 0.03 | 0.05 |
| led | Kanal 4 | 11/11 | 0.94 | 0.65 | 0.56 |
| mains50 | Kanal 4 | 11/11 | 28.40 | -63.74 | 0.64 |
| other1 | Kanal 4 | 11/11 | 0.73 | -0.48 | 0.06 |
| other2 | Kanal 4 | 11/11 | 0.33 | -0.35 | 0.21 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.07 | 0.31 s (3.20 Hz) | 25.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 37.7 |
| Kanal 2 | breitbandig | 0.99 | 0.16 s (6.40 Hz) | 26.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 38.9 |
| Kanal 3 | breitbandig | 0.56 | 0.31 s (3.20 Hz) | 27.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.8 |
| Kanal 4 | breitbandig | 0.82 | 0.16 s (6.40 Hz) | 26.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 36.5 |

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
| Kanal 1 | 1.00 | 0.97 | 0.92 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.92 | 0.96 |
| Kanal 3 | 0.92 | 0.92 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.96 | 0.91 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx4b-a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx4b-a-r1_psd.png)

### Kammprofile

![Kammprofile](B7-fx4b-a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx4b-a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 15:45:48. Stream-Meldungen: 0. owl_read: reports/owl_read/B7-fx4b-a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
