# Report C1-schliere-r1: C1-schliere-r1 – acdc1 case-schliere-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a, ins Case geschraubt |
| test | Case-Sitzung: Eingänge offen, rohe ADC-Daten, Schliere Fassung 2 läuft aus dem RAM (28 % CPU). Regler 68 / 57 / 58 / 73 von 127 |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | RAM: Schliere Fassung 2, wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_case-schliere-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis C1-schliere-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.8 | -79.1 | -71.5 | -72.1 | -86.3 | -71.8 | -97.3 | -71.5 | 71 % | -76.9 | 5.4 |
| Kanal 2 | -7.4 | -71.8 | -80.2 | -72.5 | -73.2 | -88.5 | -72.8 | -97.5 | -72.5 | 73 % | -78.3 | 5.8 |
| Kanal 3 | -5.6 | -73.9 | -85.9 | -74.2 | -74.8 | -92.9 | -74.3 | -98.1 | -74.2 | 83 % | -82.0 | 7.8 |
| Kanal 4 | -6.5 | -71.1 | -80.0 | -71.7 | -72.2 | -88.6 | -71.9 | -97.7 | -71.7 | 76 % | -77.8 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.6 dB | -79.4 | 16.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.7 dB | -74.1 | 54.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0011 | 10/10 | k=2: 4641.089 Hz, -112.6 dB | -108.4 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9745 | 0.0117 | 3/19 | k=3: 149.914 Hz, -108.4 dB | -106.5 | 0.0 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0045 | 51 | k=1·f1+1·f2: 6999.869 Hz, -111.6 dB | -103.9 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.8 dB | -100.2 | 0.1 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 1 | 4000.0005 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -100.5 dB | -100.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -79.4 | 20.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -75.3 | 52.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=2: 4641.089 Hz, -113.0 dB | -107.7 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9706 | 0.0084 | 3/19 | k=3: 149.913 Hz, -109.5 dB | -108.0 | 0.0 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0032 | 68 | k=24·f1-3·f2: 5996.807 Hz, -112.1 dB | -103.7 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.3 dB | -100.3 | 0.2 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 2 | 4000.0005 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -100.8 dB | -100.6 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -80.0 | 26.4 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.5 dB | -76.6 | 56.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.089 Hz, -113.2 dB | -109.0 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9745 | 0.0118 | 3/19 | k=3: 149.914 Hz, -114.4 dB | -112.7 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0036 | 98 | k=24·f1-3·f2: 5996.807 Hz, -113.5 dB | -103.9 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -101.4 dB | -101.2 | 0.2 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 3 | 4000.0005 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -101.5 dB | -101.0 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -79.6 | 16.0 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.5 dB | -73.9 | 59.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.089 Hz, -112.5 dB | -108.3 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9706 | 0.0086 | 3/19 | k=3: 149.913 Hz, -109.0 dB | -107.7 | 0.0 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0035 | 59 | k=24·f1-3·f2: 5996.808 Hz, -112.9 dB | -104.0 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.5 dB | -100.5 | 0.1 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 4 | 4000.0006 | 0.0004 | 4/5 | k=1: 4000.000 Hz, -101.0 dB | -100.9 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.7 | 58.9 | usb1k·1 |
| 6000.000 | -78.6 | 57.3 | fs8·1 |
| 1999.735 | -80.7 | 52.4 | usb1k·2 |
| 12000.000 | -81.4 | 55.9 | fs8·2 |
| 2999.603 | -82.5 | 51.7 | usb1k·3 |
| 3999.471 | -86.9 | 47.9 | usb1k·4 |
| 18000.000 | -87.8 | 50.2 | fs8·3 |
| 4999.338 | -89.4 | 46.1 | usb1k·5 |
| 9998.676 | -88.9 | 48.7 | usb1k·10 |
| 15997.882 | -90.4 | 47.1 | usb1k·16 |
| 6999.074 | -90.9 | 45.3 | usb1k·7 |
| 8998.808 | -90.7 | 46.1 | usb1k·9 |
| 16997.749 | -92.8 | 45.5 | usb1k·17 |
| 18997.485 | -93.9 | 44.7 | usb1k·19 |
| 5999.206 | -93.4 | 42.4 | usb1k·6 |
| 20997.220 | -94.4 | 43.9 | usb1k·21 |
| 11998.411 | -95.9 | 41.4 | usb1k·12 |
| 13998.146 | -96.7 | 41.6 | usb1k·14 |
| 7998.941 | -95.7 | 40.8 | usb1k·8 |
| 12998.279 | -97.1 | 40.1 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 59.2 | usb1k·1 |
| 6000.000 | -78.5 | 58.3 | fs8·1 |
| 12000.000 | -81.6 | 57.3 | fs8·2 |
| 1999.735 | -82.4 | 52.3 | usb1k·2 |
| 2999.603 | -83.4 | 52.0 | usb1k·3 |
| 3999.471 | -87.5 | 48.6 | usb1k·4 |
| 18000.000 | -87.9 | 51.3 | fs8·3 |
| 9998.676 | -88.9 | 49.9 | usb1k·10 |
| 4999.338 | -90.3 | 46.6 | usb1k·5 |
| 15997.882 | -91.0 | 48.4 | usb1k·16 |
| 6999.074 | -91.9 | 45.6 | usb1k·7 |
| 8998.808 | -91.4 | 46.9 | usb1k·9 |
| 16997.749 | -93.4 | 45.8 | usb1k·17 |
| 18997.485 | -93.9 | 46.1 | usb1k·19 |
| 20997.220 | -95.1 | 44.6 | usb1k·21 |
| 5999.206 | -95.2 | 41.6 | usb1k·6 |
| 11998.411 | -96.7 | 42.2 | usb1k·12 |
| 12998.279 | -97.1 | 41.5 | usb1k·13 |
| 17997.617 | -98.5 | 40.6 | usb1k·18 |
| 13998.146 | -98.5 | 40.8 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.5 | 62.4 | usb1k·1 |
| 6000.000 | -79.0 | 62.1 | fs8·1 |
| 12000.000 | -82.1 | 59.8 | fs8·2 |
| 1999.735 | -83.5 | 55.9 | usb1k·2 |
| 2999.603 | -84.6 | 55.3 | usb1k·3 |
| 18000.000 | -88.3 | 53.7 | fs8·3 |
| 3999.471 | -88.2 | 52.7 | usb1k·4 |
| 9998.676 | -89.4 | 53.3 | usb1k·10 |
| 15997.882 | -91.5 | 50.2 | usb1k·16 |
| 4999.338 | -91.1 | 49.8 | usb1k·5 |
| 8998.809 | -92.0 | 49.9 | usb1k·9 |
| 6999.074 | -92.7 | 48.7 | usb1k·7 |
| 18997.485 | -94.1 | 48.4 | usb1k·19 |
| 16997.749 | -94.3 | 48.0 | usb1k·17 |
| 20997.220 | -95.8 | 46.5 | usb1k·21 |
| 5999.206 | -97.1 | 44.0 | usb1k·6 |
| 11998.411 | -97.3 | 44.7 | usb1k·12 |
| 12998.279 | -97.6 | 44.2 | usb1k·13 |
| 17997.617 | -98.5 | 43.2 | usb1k·18 |
| 14998.014 | -99.1 | 42.9 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.5 | 60.2 | usb1k·1 |
| 6000.000 | -78.7 | 57.5 | fs8·1 |
| 1999.735 | -80.2 | 54.1 | usb1k·2 |
| 12000.000 | -81.8 | 56.3 | fs8·2 |
| 2999.603 | -82.6 | 52.6 | usb1k·3 |
| 3999.471 | -87.1 | 48.3 | usb1k·4 |
| 18000.000 | -88.2 | 50.4 | fs8·3 |
| 4999.338 | -89.1 | 47.5 | usb1k·5 |
| 9998.676 | -89.1 | 48.7 | usb1k·10 |
| 15997.882 | -90.5 | 48.0 | usb1k·16 |
| 8998.809 | -90.4 | 47.0 | usb1k·9 |
| 6999.074 | -91.2 | 45.9 | usb1k·7 |
| 16997.749 | -93.2 | 44.8 | usb1k·17 |
| 5999.206 | -92.8 | 43.3 | usb1k·6 |
| 18997.485 | -94.2 | 45.0 | usb1k·19 |
| 20997.220 | -94.3 | 44.6 | usb1k·21 |
| 11998.411 | -96.0 | 42.1 | usb1k·12 |
| 13998.146 | -96.7 | 42.0 | usb1k·14 |
| 7998.941 | -95.5 | 41.7 | usb1k·8 |
| 12998.279 | -96.8 | 40.9 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.04 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.12 | 0.11 | 0.03 |
| led | Kanal 1 | 11/11 | 0.69 | -0.05 | 0.53 |
| mains50 | Kanal 1 | 11/11 | 217.25 | 588.96 | 0.51 |
| other1 | Kanal 1 | 11/11 | 0.23 | -0.04 | 0.17 |
| other2 | Kanal 1 | 11/11 | 0.23 | -0.14 | 0.20 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.03 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.12 | 0.15 | 0.02 |
| led | Kanal 2 | 11/11 | 0.45 | -0.96 | 0.43 |
| mains50 | Kanal 2 | 11/11 | 254.29 | 690.41 | 0.57 |
| other1 | Kanal 2 | 11/11 | 0.20 | 0.08 | 0.20 |
| other2 | Kanal 2 | 11/11 | 0.14 | -0.07 | 0.13 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.03 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.12 | 0.11 | 0.02 |
| led | Kanal 3 | 11/11 | 0.68 | 0.17 | 0.27 |
| mains50 | Kanal 3 | 11/11 | 215.76 | 584.64 | 0.64 |
| other1 | Kanal 3 | 11/11 | 0.15 | -0.25 | 0.12 |
| other2 | Kanal 3 | 11/11 | 0.15 | 0.01 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.03 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.12 | 0.08 | 0.02 |
| led | Kanal 4 | 11/11 | 0.74 | 0.24 | 0.62 |
| mains50 | Kanal 4 | 11/11 | 252.53 | 683.20 | 0.54 |
| other1 | Kanal 4 | 11/11 | 0.22 | 0.00 | 0.23 |
| other2 | Kanal 4 | 11/11 | 0.19 | -0.09 | 0.21 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.73 | 0.16 s (6.38 Hz) | 21.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.1 |
| Kanal 2 | breitbandig | 0.70 | 0.16 s (6.38 Hz) | 23.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.5 |
| Kanal 3 | breitbandig | 0.41 | 7.50 s (0.13 Hz) | 23.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.2 |
| Kanal 4 | breitbandig | 0.62 | 0.16 s (6.38 Hz) | 24.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 38.1 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.96 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.97 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.96 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](C1-schliere-r1_psd.png)

### Kammprofile

![Kammprofile](C1-schliere-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](C1-schliere-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:27:41. Stream-Meldungen: 0. owl_read: out/owl_read/C1-schliere-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Out 1 steckt am zweiten Interface. messlog D69
