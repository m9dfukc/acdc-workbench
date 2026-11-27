# Report B7-fx5a-b-r2: B7-fx5a-b-r2 – acdc1 fx5a-open-inputs-7b, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a |
| test | Build-7-Sitzung: fx5a (fx4b + Patch 16) am Ende, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_fx5a-open-inputs-7b-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B7-fx5a-b-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.7 | -67.9 | -69.8 | -72.3 | -73.1 | -85.5 | -72.6 | -94.5 | -72.3 | 64 % | -76.8 | 4.5 |
| Kanal 2 | -7.1 | -69.8 | -72.5 | -73.1 | -73.8 | -87.4 | -73.4 | -94.9 | -73.1 | 69 % | -78.3 | 5.1 |
| Kanal 3 | -5.3 | -70.8 | -73.0 | -74.9 | -75.5 | -92.0 | -75.1 | -95.8 | -74.9 | 80 % | -82.0 | 7.1 |
| Kanal 4 | -6.2 | -70.2 | -74.4 | -72.3 | -72.9 | -87.3 | -72.6 | -95.2 | -72.4 | 71 % | -77.7 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.0 dB | -83.4 | 7.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8671 | 0.0002 | 23/23 | k=1: 999.867 Hz, -73.5 dB | -74.8 | 56.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0014 | 10/10 | k=1: 2320.543 Hz, -116.5 dB | -111.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0009 | 0.0232 | 3/19 | k=1: 50.004 Hz, -96.8 dB | -98.6 | 0.2 % |
| Mischprodukte n·999.8671 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8671 | 0.0036 | 5 | k=-3·f1+4·f2: 21000.401 Hz, -120.7 dB | -117.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.3 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.3 dB | -99.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.5 | 9.1 % |
| 1-kHz-Kamm | Kanal 2 | 999.8671 | 0.0002 | 23/23 | k=1: 999.867 Hz, -74.1 dB | -75.3 | 60.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0009 | 10/10 | k=9: 20884.904 Hz, -114.0 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0007 | 0.0230 | 3/19 | k=1: 50.004 Hz, -97.6 dB | -99.2 | 0.2 % |
| Mischprodukte n·999.8671 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8671 | 0.0028 | 9 | k=-3·f1+4·f2: 21000.401 Hz, -120.3 dB | -115.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.5 dB | -96.7 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -85.0 dB | -84.1 | 12.0 % |
| 1-kHz-Kamm | Kanal 3 | 999.8671 | 0.0002 | 23/23 | k=1: 999.867 Hz, -75.4 dB | -76.6 | 67.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0007 | 10/10 | k=2: 4641.089 Hz, -116.3 dB | -111.9 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0017 | 0.0208 | 7/19 | k=1: 50.005 Hz, -98.4 dB | -99.7 | 0.3 % |
| Mischprodukte n·999.8671 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8671 | 0.0033 | 26 | k=-3·f1+4·f2: 21000.401 Hz, -121.4 dB | -113.1 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -100.1 dB | -100.4 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -100.2 dB | -97.7 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.8 | 7.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8671 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.1 dB | -74.3 | 63.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0013 | 10/10 | k=1: 2320.544 Hz, -115.6 dB | -111.0 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0007 | 0.0234 | 3/19 | k=1: 50.004 Hz, -97.9 dB | -99.5 | 0.2 % |
| Mischprodukte n·999.8671 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8671 | 0.0070 | 9 | k=1·f1+2·f2: 12999.881 Hz, -119.9 dB | -115.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -97.0 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.8 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.5 | 56.1 | usb1k·1 |
| 1999.734 | -81.5 | 50.2 | usb1k·2 |
| 2999.602 | -82.9 | 50.9 | usb1k·3 |
| 12000.000 | -84.0 | 53.4 | fs8·2 |
| 6000.000 | -84.8 | 50.8 | fs8·1 |
| 18000.000 | -87.3 | 51.0 | fs8·3 |
| 3999.468 | -87.8 | 45.1 | usb1k·4 |
| 9998.671 | -88.9 | 48.6 | usb1k·10 |
| 4999.335 | -90.6 | 45.3 | usb1k·5 |
| 15997.874 | -90.7 | 47.3 | usb1k·16 |
| 8998.804 | -91.8 | 45.4 | usb1k·9 |
| 6999.070 | -92.2 | 43.6 | usb1k·7 |
| 16997.741 | -92.7 | 45.3 | usb1k·17 |
| 18997.475 | -92.5 | 46.0 | usb1k·19 |
| 7998.937 | -94.8 | 40.8 | usb1k·8 |
| 11998.405 | -95.0 | 42.3 | usb1k·12 |
| 5999.203 | -95.6 | 39.9 | usb1k·6 |
| 12998.272 | -96.3 | 41.2 | usb1k·13 |
| 50.004 | -96.8 | 26.0 | mains50·1 |
| 2000.000 | -97.8 | 33.9 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.1 | 57.3 | usb1k·1 |
| 1999.734 | -81.8 | 51.3 | usb1k·2 |
| 2999.602 | -83.4 | 51.7 | usb1k·3 |
| 12000.000 | -84.2 | 54.6 | fs8·2 |
| 6000.000 | -84.9 | 52.1 | fs8·1 |
| 18000.000 | -87.3 | 51.8 | fs8·3 |
| 3999.468 | -88.1 | 46.6 | usb1k·4 |
| 9998.671 | -89.1 | 49.7 | usb1k·10 |
| 4999.335 | -90.7 | 46.5 | usb1k·5 |
| 15997.874 | -90.8 | 48.2 | usb1k·16 |
| 8998.804 | -91.8 | 46.7 | usb1k·9 |
| 6999.070 | -92.6 | 44.6 | usb1k·7 |
| 18997.475 | -92.6 | 46.8 | usb1k·19 |
| 16997.741 | -93.1 | 46.2 | usb1k·17 |
| 7998.937 | -95.5 | 41.9 | usb1k·8 |
| 11998.405 | -95.1 | 43.6 | usb1k·12 |
| 5999.202 | -96.4 | 40.5 | usb1k·6 |
| 12998.272 | -96.3 | 42.7 | usb1k·13 |
| 50.004 | -97.6 | 27.0 | mains50·1 |
| 20997.209 | -96.9 | 42.4 | usb1k·21 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.4 | 60.6 | usb1k·1 |
| 1999.734 | -83.6 | 54.6 | usb1k·2 |
| 2999.602 | -84.4 | 55.4 | usb1k·3 |
| 12000.000 | -85.0 | 56.9 | fs8·2 |
| 6000.000 | -85.4 | 55.6 | fs8·1 |
| 18000.000 | -87.8 | 54.2 | fs8·3 |
| 3999.468 | -88.9 | 50.4 | usb1k·4 |
| 9998.671 | -89.4 | 52.4 | usb1k·10 |
| 4999.335 | -91.9 | 49.3 | usb1k·5 |
| 15997.874 | -91.4 | 50.4 | usb1k·16 |
| 8998.804 | -93.0 | 48.7 | usb1k·9 |
| 6999.070 | -93.8 | 47.4 | usb1k·7 |
| 18997.475 | -92.8 | 49.0 | usb1k·19 |
| 16997.741 | -93.4 | 48.6 | usb1k·17 |
| 11998.405 | -95.7 | 46.2 | usb1k·12 |
| 7998.937 | -96.3 | 44.3 | usb1k·8 |
| 12998.272 | -96.5 | 45.6 | usb1k·13 |
| 5999.202 | -98.0 | 43.0 | usb1k·6 |
| 50.005 | -98.4 | 31.3 | mains50·1 |
| 20997.209 | -97.8 | 43.8 | usb1k·21 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.1 | 58.0 | usb1k·1 |
| 1999.734 | -79.9 | 52.7 | usb1k·2 |
| 2999.602 | -82.9 | 52.0 | usb1k·3 |
| 12000.000 | -84.4 | 53.5 | fs8·2 |
| 6000.000 | -85.3 | 51.3 | fs8·1 |
| 18000.000 | -87.4 | 50.8 | fs8·3 |
| 3999.468 | -87.6 | 46.9 | usb1k·4 |
| 4999.336 | -89.3 | 47.2 | usb1k·5 |
| 9998.671 | -89.5 | 48.7 | usb1k·10 |
| 8998.804 | -90.6 | 46.8 | usb1k·9 |
| 15997.874 | -90.1 | 47.6 | usb1k·16 |
| 6999.070 | -91.7 | 44.7 | usb1k·7 |
| 7998.937 | -94.1 | 42.8 | usb1k·8 |
| 18997.475 | -92.7 | 45.7 | usb1k·19 |
| 16997.741 | -93.2 | 45.2 | usb1k·17 |
| 5999.202 | -94.6 | 41.9 | usb1k·6 |
| 11998.405 | -94.5 | 43.4 | usb1k·12 |
| 12998.272 | -96.4 | 42.0 | usb1k·13 |
| 20997.209 | -96.2 | 41.7 | usb1k·21 |
| 50.004 | -97.9 | 26.7 | mains50·1 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.03 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.27 | 0.71 | 0.04 |
| led | Kanal 1 | 11/11 | 0.90 | 0.67 | 1.46 |
| mains50 | Kanal 1 | 11/11 | 50.21 | 0.07 | 0.71 |
| other1 | Kanal 1 | 11/11 | 1.45 | -1.99 | 0.13 |
| other2 | Kanal 1 | 11/11 | 0.21 | 0.12 | 0.18 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.26 | 0.66 | 0.07 |
| led | Kanal 2 | 11/11 | 0.34 | -0.40 | 0.95 |
| mains50 | Kanal 2 | 11/11 | 43.11 | -1.66 | 0.59 |
| other1 | Kanal 2 | 11/11 | 1.54 | -0.46 | 0.16 |
| other2 | Kanal 2 | 11/11 | 0.24 | -0.20 | 0.17 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.03 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.27 | 0.70 | 0.03 |
| led | Kanal 3 | 11/11 | 0.89 | 0.77 | 1.31 |
| mains50 | Kanal 3 | 11/11 | 15.26 | 1.64 | 0.40 |
| other1 | Kanal 3 | 11/11 | 0.19 | -0.04 | 0.07 |
| other2 | Kanal 3 | 11/11 | 0.81 | 1.34 | 0.15 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.02 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.22 | 0.56 | 0.09 |
| led | Kanal 4 | 11/11 | 0.97 | 1.96 | 1.22 |
| mains50 | Kanal 4 | 11/11 | 45.46 | -14.21 | 0.64 |
| other1 | Kanal 4 | 11/11 | 1.38 | -1.50 | 0.15 |
| other2 | Kanal 4 | 11/11 | 0.21 | -0.14 | 0.16 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.62 | 0.31 s (3.18 Hz) | 25.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 34.5 |
| Kanal 2 | breitbandig | 2.16 | 0.31 s (3.18 Hz) | 26.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.95 | 7.50 s (0.13 Hz) | 36.8 |
| Kanal 3 | breitbandig | 2.43 | 0.31 s (3.18 Hz) | 25.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 41.3 |
| Kanal 4 | breitbandig | 1.59 | 0.31 s (3.18 Hz) | 26.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 35.7 |

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
| Kanal 1 | 1.00 | 0.98 | 0.97 | 0.93 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.96 |
| Kanal 3 | 0.97 | 0.96 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.96 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B7-fx5a-b-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B7-fx5a-b-r2_psd.png)

### Kammprofile

![Kammprofile](B7-fx5a-b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B7-fx5a-b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:24:03. Stream-Meldungen: 0. owl_read: reports/owl_read/B7-fx5a-b-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
