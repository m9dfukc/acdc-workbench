# Report C1-acdc-r1: C1-acdc-r1 – acdc1 case-acdc-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a, ins Case geschraubt |
| test | Case-Sitzung, Kontrolle: Eingänge offen, rohe ADC-Daten, Default-Patch läuft. Regler wie C1-schliere |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_case-acdc-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis C1-acdc-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.7 | -77.3 | -71.7 | -72.3 | -86.7 | -72.0 | -97.3 | -71.8 | 70 % | -76.9 | 5.2 |
| Kanal 2 | -7.4 | -71.8 | -78.3 | -72.9 | -73.5 | -88.8 | -73.2 | -97.4 | -72.9 | 71 % | -78.4 | 5.4 |
| Kanal 3 | -5.5 | -74.2 | -83.1 | -74.8 | -75.3 | -93.3 | -75.0 | -94.2 | -74.8 | 82 % | -82.2 | 7.3 |
| Kanal 4 | -6.5 | -70.7 | -76.9 | -71.9 | -72.3 | -88.9 | -72.1 | -97.7 | -71.9 | 75 % | -77.9 | 6.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -83.2 | 7.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.8 | 62.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0009 | 10/10 | k=2: 4641.090 Hz, -112.2 dB | -108.6 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9936 | 0.0009 | 2/19 | k=3: 149.982 Hz, -110.5 dB | -108.6 | 0.0 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0046 | 5 | k=1·f1+1·f2: 6999.861 Hz, -118.1 dB | -116.9 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 1 | 4000.0004 | 0.0001 | 4/5 | k=1: 4000.000 Hz, -100.9 dB | -100.3 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.9 dB | -100.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.1 dB | -83.3 | 9.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.0 | 61.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.090 Hz, -113.2 dB | -107.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9935 | 0.0017 | 2/19 | k=3: 149.983 Hz, -112.0 dB | -110.1 | 0.0 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0032 | 5 | k=1·f1+1·f2: 6999.863 Hz, -119.9 dB | -118.4 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 2 | 4000.0004 | 0.0001 | 4/5 | k=1: 4000.000 Hz, -101.0 dB | -100.4 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -101.1 dB | -100.4 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.7 dB | -83.9 | 12.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.4 | 69.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0006 | 10/10 | k=2: 4641.090 Hz, -113.2 dB | -108.9 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9937 | 0.0052 | 4/19 | k=1: 49.983 Hz, -116.5 dB | -110.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0032 | 14 | k=-3·f1+4·f2: 21000.396 Hz, -123.7 dB | -117.0 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 3 | 4000.0004 | 0.0000 | 4/5 | k=1: 4000.000 Hz, -101.7 dB | -101.0 | 0.2 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0004 | 16/23 | k=1: 999.999 Hz, -101.8 dB | -95.2 | 0.9 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -83.5 | 7.0 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.1 dB | -73.6 | 68.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0009 | 10/10 | k=2: 4641.090 Hz, -112.1 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9935 | 0.0012 | 2/19 | k=3: 149.982 Hz, -112.2 dB | -110.1 | 0.0 % |
| Mischprodukte n·999.8676 + m·5999.9999 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0123 | 1 | k=1·f1+1·f2: 6999.855 Hz, -119.5 dB | -121.7 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 4 | 4000.0005 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -101.3 dB | -100.7 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -101.4 dB | -100.8 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 57.8 | usb1k·1 |
| 1999.735 | -80.4 | 52.2 | usb1k·2 |
| 2999.603 | -82.2 | 51.5 | usb1k·3 |
| 6000.000 | -83.2 | 52.8 | fs8·1 |
| 12000.000 | -85.4 | 52.4 | fs8·2 |
| 3999.470 | -86.9 | 47.8 | usb1k·4 |
| 18000.000 | -87.3 | 50.8 | fs8·3 |
| 4999.339 | -89.1 | 44.7 | usb1k·5 |
| 9998.676 | -88.8 | 49.0 | usb1k·10 |
| 15997.882 | -90.1 | 47.3 | usb1k·16 |
| 6999.074 | -90.5 | 45.5 | usb1k·7 |
| 8998.808 | -90.6 | 46.5 | usb1k·9 |
| 16997.749 | -92.6 | 45.6 | usb1k·17 |
| 18997.485 | -93.9 | 42.8 | usb1k·19 |
| 5999.206 | -93.3 | 42.6 | usb1k·6 |
| 20997.220 | -94.4 | 44.0 | usb1k·21 |
| 11998.411 | -95.4 | 42.2 | usb1k·12 |
| 7998.941 | -94.6 | 41.6 | usb1k·8 |
| 13998.146 | -96.5 | 41.4 | usb1k·14 |
| 12998.278 | -96.4 | 41.3 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 58.1 | usb1k·1 |
| 1999.735 | -82.1 | 52.1 | usb1k·2 |
| 6000.000 | -83.1 | 54.2 | fs8·1 |
| 2999.603 | -83.3 | 52.4 | usb1k·3 |
| 12000.000 | -85.6 | 53.3 | fs8·2 |
| 18000.000 | -87.4 | 52.0 | fs8·3 |
| 3999.470 | -87.5 | 48.8 | usb1k·4 |
| 9998.676 | -88.8 | 50.2 | usb1k·10 |
| 4999.339 | -90.2 | 45.4 | usb1k·5 |
| 15997.882 | -90.8 | 48.2 | usb1k·16 |
| 6999.074 | -91.7 | 45.9 | usb1k·7 |
| 8998.808 | -91.3 | 47.2 | usb1k·9 |
| 16997.749 | -93.1 | 45.8 | usb1k·17 |
| 18997.485 | -93.8 | 43.4 | usb1k·19 |
| 20997.220 | -95.1 | 44.9 | usb1k·21 |
| 5999.206 | -95.0 | 42.3 | usb1k·6 |
| 11998.411 | -96.1 | 42.7 | usb1k·12 |
| 12998.278 | -96.7 | 42.6 | usb1k·13 |
| 7998.941 | -96.3 | 41.0 | usb1k·8 |
| 17997.617 | -98.6 | 40.9 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 61.2 | usb1k·1 |
| 1999.735 | -83.2 | 55.2 | usb1k·2 |
| 6000.000 | -83.7 | 57.9 | fs8·1 |
| 2999.603 | -84.6 | 55.5 | usb1k·3 |
| 12000.000 | -86.4 | 55.8 | fs8·2 |
| 18000.000 | -87.8 | 54.2 | fs8·3 |
| 3999.471 | -88.2 | 52.2 | usb1k·4 |
| 9998.676 | -89.3 | 53.0 | usb1k·10 |
| 15997.882 | -91.4 | 50.1 | usb1k·16 |
| 4999.339 | -91.1 | 48.5 | usb1k·5 |
| 8998.808 | -91.9 | 50.0 | usb1k·9 |
| 6999.074 | -92.6 | 48.7 | usb1k·7 |
| 16997.749 | -94.0 | 48.0 | usb1k·17 |
| 18997.485 | -94.1 | 47.2 | usb1k·19 |
| 20997.220 | -95.8 | 46.1 | usb1k·21 |
| 11998.411 | -96.8 | 45.4 | usb1k·12 |
| 12998.278 | -97.1 | 45.1 | usb1k·13 |
| 5999.206 | -97.1 | 44.4 | usb1k·6 |
| 17997.617 | -98.6 | 43.2 | usb1k·18 |
| 7998.941 | -97.7 | 43.7 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.1 | 59.1 | usb1k·1 |
| 1999.735 | -79.9 | 53.8 | usb1k·2 |
| 2999.603 | -82.4 | 52.8 | usb1k·3 |
| 6000.000 | -83.2 | 53.3 | fs8·1 |
| 12000.000 | -85.8 | 52.5 | fs8·2 |
| 3999.470 | -87.0 | 48.7 | usb1k·4 |
| 18000.000 | -87.7 | 50.9 | fs8·3 |
| 4999.338 | -88.7 | 46.3 | usb1k·5 |
| 15997.882 | -90.2 | 47.8 | usb1k·16 |
| 9998.676 | -89.0 | 49.0 | usb1k·10 |
| 8998.808 | -90.2 | 47.7 | usb1k·9 |
| 6999.074 | -91.0 | 46.0 | usb1k·7 |
| 16997.749 | -92.8 | 45.7 | usb1k·17 |
| 5999.206 | -92.5 | 44.0 | usb1k·6 |
| 18997.485 | -94.1 | 41.9 | usb1k·19 |
| 20997.220 | -94.3 | 44.0 | usb1k·21 |
| 7998.941 | -94.3 | 42.2 | usb1k·8 |
| 11998.411 | -95.4 | 42.9 | usb1k·12 |
| 12998.279 | -96.2 | 41.9 | usb1k·13 |
| 13998.146 | -96.6 | 42.2 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | 0.03 | 0.04 |
| usb1k | Kanal 1 | 11/11 | 0.21 | 0.05 | 0.03 |
| led | Kanal 1 | 11/11 | 0.72 | 0.75 | 0.56 |
| mains50 | Kanal 1 | 9/11 | 946.19 | 402.51 | 4.31 |
| other1 | Kanal 1 | 11/11 | 0.35 | 0.63 | 0.17 |
| other2 | Kanal 1 | 11/11 | 0.19 | 0.24 | 0.30 |
| fs8 | Kanal 2 | 11/11 | 0.03 | -0.00 | 0.04 |
| usb1k | Kanal 2 | 11/11 | 0.25 | 0.09 | 0.02 |
| led | Kanal 2 | 11/11 | 0.43 | 0.81 | 0.39 |
| mains50 | Kanal 2 | 9/11 | 977.46 | 536.32 | 4.64 |
| other1 | Kanal 2 | 11/11 | 0.22 | 0.40 | 0.16 |
| other2 | Kanal 2 | 11/11 | 0.21 | -0.01 | 0.23 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.22 | 0.12 | 0.03 |
| led | Kanal 3 | 11/11 | 0.70 | 1.09 | 0.29 |
| mains50 | Kanal 3 | 11/11 | 81.25 | -24.59 | 0.46 |
| other1 | Kanal 3 | 11/11 | 0.15 | 0.35 | 0.09 |
| other2 | Kanal 3 | 11/11 | 11.32 | 3.15 | 0.04 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.22 | 0.06 | 0.03 |
| led | Kanal 4 | 11/11 | 1.40 | 2.02 | 0.35 |
| mains50 | Kanal 4 | 9/11 | 997.53 | 537.10 | 4.44 |
| other1 | Kanal 4 | 11/11 | 0.22 | 0.63 | 0.19 |
| other2 | Kanal 4 | 11/11 | 0.15 | -0.11 | 0.25 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.06 | 0.31 s (3.22 Hz) | 26.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 36.1 |
| Kanal 2 | breitbandig | 1.07 | 0.31 s (3.22 Hz) | 27.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 37.5 |
| Kanal 3 | breitbandig | 0.68 | 0.31 s (3.22 Hz) | 25.6 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 42.5 |
| Kanal 4 | breitbandig | 1.08 | 0.31 s (3.22 Hz) | 28.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 36.9 |

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

### Langzeit-Spektrum

![Langzeit-Spektrum](C1-acdc-r1_psd.png)

### Kammprofile

![Kammprofile](C1-acdc-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](C1-acdc-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:30:19. Stream-Meldungen: 0. owl_read: reports/owl_read/C1-acdc-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Out 1 steckt am zweiten Interface. messlog D69
