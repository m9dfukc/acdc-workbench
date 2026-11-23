# Report B10-fx7a-r2: B10-fx7a-r2 – acdc1 fx7a-open-inputs-10, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | Build-10-Sitzung: fx7a als Kontrolle in der Mitte, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx7a-open-inputs-10-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B10-fx7a-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -71.1 | -79.4 | -71.8 | -72.4 | -86.4 | -72.1 | -94.1 | -71.8 | 72 % | -77.4 | 5.5 |
| Kanal 2 | -7.5 | -72.0 | -80.5 | -72.7 | -73.3 | -88.3 | -73.0 | -94.3 | -72.8 | 74 % | -78.7 | 5.9 |
| Kanal 3 | -5.7 | -73.8 | -83.8 | -74.2 | -74.8 | -92.9 | -74.4 | -95.0 | -74.3 | 84 % | -82.3 | 8.1 |
| Kanal 4 | -6.6 | -71.3 | -80.5 | -71.8 | -72.3 | -88.4 | -72.0 | -94.5 | -71.9 | 77 % | -78.2 | 6.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -82.7 | 8.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.8 | 63.6 % |
| Netz 50 Hz | Kanal 1 | 50.1935 | 0.0056 | 3/19 | k=3: 150.588 Hz, -111.1 dB | -108.8 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0031 | 7 | k=-1·f1+3·f2: 17000.129 Hz, -118.1 dB | -115.5 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.4 dB | -98.1 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -96.3 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -82.8 | 10.0 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.7 | 64.3 % |
| Netz 50 Hz | Kanal 2 | 50.1934 | 0.0038 | 3/19 | k=3: 150.584 Hz, -112.8 dB | -110.7 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0030 | 10 | k=1·f1+3·f2: 18999.867 Hz, -121.4 dB | -116.5 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -97.8 dB | -98.4 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -96.4 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -83.3 | 12.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.7 | 72.0 % |
| Netz 50 Hz | Kanal 3 | 50.1934 | 0.0058 | 3/19 | k=3: 150.588 Hz, -117.3 dB | -115.4 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0018 | 17 | k=-7·f1+4·f2: 17000.926 Hz, -123.3 dB | -116.0 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.1 dB | -99.3 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.3 dB | -97.0 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -82.9 | 7.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.0 dB | -73.5 | 69.0 % |
| Netz 50 Hz | Kanal 4 | 50.1933 | 0.0035 | 3/19 | k=3: 150.580 Hz, -112.2 dB | -110.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0032 | 8 | k=1·f1+1·f2: 6999.872 Hz, -121.2 dB | -117.2 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -98.6 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -96.6 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 59.4 | usb1k·1 |
| 1999.736 | -81.1 | 50.9 | usb1k·2 |
| 2999.603 | -82.1 | 52.5 | usb1k·3 |
| 6000.000 | -83.9 | 51.9 | fs8·1 |
| 12000.000 | -84.4 | 53.2 | fs8·2 |
| 18000.000 | -85.2 | 53.5 | fs8·3 |
| 3999.471 | -86.3 | 47.0 | usb1k·4 |
| 9998.676 | -88.1 | 49.4 | usb1k·10 |
| 4999.338 | -88.9 | 46.7 | usb1k·5 |
| 15997.882 | -89.9 | 47.9 | usb1k·16 |
| 6999.073 | -90.3 | 46.4 | usb1k·7 |
| 16997.749 | -92.3 | 46.1 | usb1k·17 |
| 8998.809 | -91.1 | 46.0 | usb1k·9 |
| 18997.485 | -93.7 | 45.1 | usb1k·19 |
| 5999.206 | -93.1 | 42.6 | usb1k·6 |
| 20997.220 | -94.0 | 44.3 | usb1k·21 |
| 13998.146 | -96.1 | 42.2 | usb1k·14 |
| 11998.411 | -95.6 | 42.0 | usb1k·12 |
| 7998.941 | -95.3 | 41.4 | usb1k·8 |
| 3000.000 | -97.4 | 37.2 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 59.4 | usb1k·1 |
| 1999.736 | -82.2 | 51.0 | usb1k·2 |
| 2999.603 | -82.8 | 53.2 | usb1k·3 |
| 6000.000 | -83.8 | 53.3 | fs8·1 |
| 12000.000 | -84.7 | 54.6 | fs8·2 |
| 18000.000 | -85.2 | 54.4 | fs8·3 |
| 3999.471 | -86.6 | 48.5 | usb1k·4 |
| 9998.676 | -88.1 | 50.8 | usb1k·10 |
| 4999.338 | -89.7 | 47.3 | usb1k·5 |
| 15997.882 | -90.4 | 48.9 | usb1k·16 |
| 6999.073 | -90.9 | 46.7 | usb1k·7 |
| 16997.749 | -92.8 | 47.0 | usb1k·17 |
| 8998.809 | -91.5 | 47.1 | usb1k·9 |
| 18997.485 | -93.7 | 46.1 | usb1k·19 |
| 20997.220 | -94.5 | 44.9 | usb1k·21 |
| 5999.206 | -94.4 | 42.8 | usb1k·6 |
| 11998.411 | -96.1 | 43.2 | usb1k·12 |
| 17997.617 | -97.3 | 42.1 | usb1k·18 |
| 13998.146 | -97.3 | 42.4 | usb1k·14 |
| 7998.941 | -96.4 | 41.8 | usb1k·8 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 63.3 | usb1k·1 |
| 1999.736 | -83.2 | 54.3 | usb1k·2 |
| 2999.603 | -83.7 | 56.5 | usb1k·3 |
| 6000.000 | -84.4 | 56.6 | fs8·1 |
| 12000.000 | -85.3 | 56.8 | fs8·2 |
| 18000.000 | -85.5 | 57.1 | fs8·3 |
| 3999.471 | -87.1 | 52.4 | usb1k·4 |
| 9998.676 | -88.5 | 53.3 | usb1k·10 |
| 15997.882 | -90.7 | 51.2 | usb1k·16 |
| 4999.338 | -90.3 | 50.3 | usb1k·5 |
| 6999.073 | -91.5 | 50.1 | usb1k·7 |
| 16997.749 | -93.3 | 49.1 | usb1k·17 |
| 8998.809 | -92.2 | 49.9 | usb1k·9 |
| 18997.485 | -93.8 | 48.4 | usb1k·19 |
| 20997.220 | -95.0 | 47.0 | usb1k·21 |
| 5999.206 | -95.8 | 45.2 | usb1k·6 |
| 11998.411 | -96.5 | 45.6 | usb1k·12 |
| 17997.617 | -97.6 | 44.9 | usb1k·18 |
| 12998.279 | -97.9 | 44.7 | usb1k·13 |
| 7998.941 | -97.1 | 44.4 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.0 | 60.5 | usb1k·1 |
| 1999.736 | -80.4 | 52.4 | usb1k·2 |
| 2999.603 | -81.9 | 53.7 | usb1k·3 |
| 6000.000 | -84.0 | 52.5 | fs8·1 |
| 12000.000 | -84.9 | 53.4 | fs8·2 |
| 18000.000 | -85.3 | 53.9 | fs8·3 |
| 3999.471 | -86.2 | 48.6 | usb1k·4 |
| 4999.338 | -88.6 | 47.8 | usb1k·5 |
| 9998.676 | -88.3 | 49.6 | usb1k·10 |
| 15997.882 | -89.8 | 48.5 | usb1k·16 |
| 6999.073 | -90.1 | 47.1 | usb1k·7 |
| 8998.809 | -90.7 | 47.3 | usb1k·9 |
| 16997.750 | -92.4 | 46.4 | usb1k·17 |
| 5999.206 | -92.6 | 44.0 | usb1k·6 |
| 18997.485 | -94.0 | 45.4 | usb1k·19 |
| 20997.220 | -94.0 | 44.6 | usb1k·21 |
| 13998.146 | -95.5 | 43.1 | usb1k·14 |
| 7998.941 | -94.6 | 42.8 | usb1k·8 |
| 11998.411 | -95.4 | 42.7 | usb1k·12 |
| 12998.279 | -97.4 | 41.1 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.26 | -0.12 | 0.04 |
| mains50 | Kanal 1 | 11/11 | 266.64 | 461.68 | 1.86 |
| other1 | Kanal 1 | 11/11 | 0.21 | -0.32 | 0.11 |
| other2 | Kanal 1 | 11/11 | 0.45 | 0.64 | 0.15 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.26 | -0.09 | 0.06 |
| mains50 | Kanal 2 | 11/11 | 493.72 | 1741.71 | 1.89 |
| other1 | Kanal 2 | 11/11 | 0.22 | -0.35 | 0.07 |
| other2 | Kanal 2 | 11/11 | 0.47 | 0.44 | 0.15 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.26 | -0.11 | 0.06 |
| mains50 | Kanal 3 | 11/11 | 241.43 | 688.84 | 1.78 |
| other1 | Kanal 3 | 11/11 | 0.17 | -0.16 | 0.07 |
| other2 | Kanal 3 | 11/11 | 0.31 | 0.12 | 0.17 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.19 | -0.05 | 0.04 |
| mains50 | Kanal 4 | 11/11 | 505.38 | 946.31 | 1.53 |
| other1 | Kanal 4 | 11/11 | 0.22 | -0.35 | 0.10 |
| other2 | Kanal 4 | 11/11 | 0.47 | 0.63 | 0.12 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.83 | 0.31 s (3.18 Hz) | 22.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.8 |
| Kanal 2 | breitbandig | 0.80 | 0.16 s (6.40 Hz) | 23.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 39.2 |
| Kanal 3 | breitbandig | 0.57 | 0.31 s (3.18 Hz) | 25.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 44.1 |
| Kanal 4 | breitbandig | 0.68 | 0.16 s (6.40 Hz) | 24.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 38.6 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.96 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.97 |
| Kanal 3 | 0.94 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.96 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B10-fx7a-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B10-fx7a-r2_psd.png)

### Kammprofile

![Kammprofile](B10-fx7a-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B10-fx7a-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 14:57:29. Stream-Meldungen: 0. owl_read: out/owl_read/B10-fx7a-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 9 v22.4.r-fx7a, geflasht aus fx8a (firmware/flashlog/20261123_build9-fx7a-ab10/), Start über dfu-util :leave. Regler etwa 12 Uhr. Oszillator im Case abgesteckt (Nutzer). messlog D85.
