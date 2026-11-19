# Report C1-schliere-r2: C1-schliere-r2 – acdc1 case-schliere-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a, ins Case geschraubt |
| test | Case-Sitzung: Eingänge offen, rohe ADC-Daten, Schliere Fassung 2 läuft aus dem RAM (28 % CPU). Regler 68 / 57 / 58 / 73 von 127 |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | RAM: Schliere Fassung 2, wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_case-schliere-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis C1-schliere-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -70.5 | -77.7 | -71.5 | -72.1 | -86.4 | -71.7 | -95.4 | -71.5 | 72 % | -77.0 | 5.5 |
| Kanal 2 | -7.4 | -71.6 | -79.0 | -72.5 | -73.1 | -88.5 | -72.7 | -97.2 | -72.5 | 74 % | -78.3 | 5.8 |
| Kanal 3 | -5.6 | -73.8 | -84.3 | -74.2 | -74.7 | -93.0 | -74.3 | -94.0 | -74.2 | 84 % | -82.2 | 8.0 |
| Kanal 4 | -6.5 | -70.7 | -78.1 | -71.6 | -72.1 | -88.5 | -71.8 | -97.5 | -71.6 | 76 % | -77.8 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -79.6 | 15.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.6 dB | -74.0 | 56.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -112.8 dB | -108.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.1045 | 0.0148 | 3/19 | k=2: 100.193 Hz, -107.6 dB | -105.7 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0021 | 48 | k=1·f1+1·f2: 6999.865 Hz, -113.0 dB | -104.4 | 0.1 % |
| stärkste übrige Linie (51.20 Hz) | Kanal 1 | 51.2000 | 0.0013 | 7/466 | k=1: 51.197 Hz, -97.6 dB | -97.3 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0006 | 0.0260 | 6/7 | k=1: 3000.000 Hz, -100.0 dB | -99.9 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.6 dB | -79.6 | 19.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.2 | 54.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0010 | 10/10 | k=9: 20884.904 Hz, -113.3 dB | -107.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9556 | 0.0066 | 3/19 | k=3: 149.868 Hz, -112.5 dB | -109.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0017 | 59 | k=1·f1+1·f2: 6999.866 Hz, -114.0 dB | -104.2 | 0.1 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 2 | 4000.0007 | 0.0198 | 5/5 | k=1: 4000.000 Hz, -100.4 dB | -100.2 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0193 | 5/7 | k=1: 3000.000 Hz, -100.5 dB | -100.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.1 dB | -80.1 | 25.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.5 | 58.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0004 | 10/10 | k=2: 4641.090 Hz, -113.4 dB | -109.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9592 | 0.0243 | 4/19 | k=2: 99.920 Hz, -116.4 dB | -111.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0023 | 87 | k=8·f1+1·f2: 13998.941 Hz, -114.2 dB | -104.4 | 0.1 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 3 | 4000.0004 | 0.0003 | 4/5 | k=1: 4000.000 Hz, -101.2 dB | -100.7 | 0.2 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0148 | 18/23 | k=1: 1000.000 Hz, -101.3 dB | -95.0 | 0.8 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -79.8 | 15.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -73.7 | 61.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0008 | 10/10 | k=1: 2320.544 Hz, -112.7 dB | -108.6 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9556 | 0.0067 | 3/19 | k=3: 149.868 Hz, -112.1 dB | -109.0 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0018 | 51 | k=8·f1+1·f2: 13998.940 Hz, -114.9 dB | -104.4 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0002 | 0.0188 | 5/7 | k=1: 3000.000 Hz, -100.7 dB | -100.4 | 0.1 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 4 | 4000.0004 | 0.0003 | 4/5 | k=1: 4000.000 Hz, -100.8 dB | -100.6 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.6 | 58.6 | usb1k·1 |
| 6000.000 | -78.7 | 56.4 | fs8·1 |
| 1999.736 | -80.5 | 52.5 | usb1k·2 |
| 12000.000 | -81.7 | 55.6 | fs8·2 |
| 2999.603 | -82.3 | 51.9 | usb1k·3 |
| 3999.471 | -87.0 | 47.0 | usb1k·4 |
| 18000.000 | -88.1 | 49.3 | fs8·3 |
| 9998.676 | -88.8 | 48.7 | usb1k·10 |
| 4999.339 | -89.4 | 45.8 | usb1k·5 |
| 15997.882 | -90.3 | 47.2 | usb1k·16 |
| 6999.074 | -90.5 | 46.0 | usb1k·7 |
| 8998.808 | -90.6 | 46.0 | usb1k·9 |
| 16997.749 | -92.9 | 44.5 | usb1k·17 |
| 18997.485 | -93.8 | 44.7 | usb1k·19 |
| 5999.206 | -93.4 | 41.6 | usb1k·6 |
| 20997.220 | -94.5 | 44.0 | usb1k·21 |
| 11998.411 | -95.8 | 41.5 | usb1k·12 |
| 7998.941 | -95.2 | 40.7 | usb1k·8 |
| 13998.146 | -96.7 | 41.1 | usb1k·14 |
| 12998.279 | -96.7 | 41.1 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 58.8 | usb1k·1 |
| 6000.000 | -78.6 | 57.7 | fs8·1 |
| 12000.000 | -81.9 | 56.4 | fs8·2 |
| 1999.736 | -82.2 | 52.3 | usb1k·2 |
| 2999.603 | -83.3 | 52.1 | usb1k·3 |
| 3999.471 | -87.6 | 47.4 | usb1k·4 |
| 18000.000 | -88.2 | 50.1 | fs8·3 |
| 9998.676 | -88.8 | 49.7 | usb1k·10 |
| 15997.882 | -90.9 | 47.7 | usb1k·16 |
| 4999.339 | -90.4 | 46.1 | usb1k·5 |
| 6999.074 | -91.5 | 45.7 | usb1k·7 |
| 8998.808 | -91.3 | 46.3 | usb1k·9 |
| 16997.749 | -93.4 | 45.6 | usb1k·17 |
| 18997.485 | -93.8 | 45.9 | usb1k·19 |
| 20997.220 | -95.1 | 44.2 | usb1k·21 |
| 5999.206 | -95.0 | 41.2 | usb1k·6 |
| 11998.411 | -96.6 | 41.6 | usb1k·12 |
| 12998.279 | -97.0 | 42.4 | usb1k·13 |
| 7998.941 | -96.9 | 40.4 | usb1k·8 |
| 17997.617 | -98.5 | 39.8 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 62.1 | usb1k·1 |
| 6000.000 | -79.1 | 60.8 | fs8·1 |
| 12000.000 | -82.5 | 59.2 | fs8·2 |
| 1999.736 | -83.4 | 55.8 | usb1k·2 |
| 2999.603 | -84.5 | 55.3 | usb1k·3 |
| 18000.000 | -88.6 | 53.3 | fs8·3 |
| 3999.471 | -88.3 | 51.7 | usb1k·4 |
| 9998.676 | -89.3 | 53.2 | usb1k·10 |
| 15997.882 | -91.5 | 49.9 | usb1k·16 |
| 4999.339 | -91.2 | 49.2 | usb1k·5 |
| 6999.074 | -92.4 | 49.3 | usb1k·7 |
| 8998.808 | -91.9 | 49.5 | usb1k·9 |
| 18997.485 | -94.1 | 48.4 | usb1k·19 |
| 16997.749 | -94.2 | 47.3 | usb1k·17 |
| 20997.220 | -95.8 | 46.1 | usb1k·21 |
| 5999.206 | -97.0 | 42.9 | usb1k·6 |
| 12998.279 | -97.4 | 45.2 | usb1k·13 |
| 11998.411 | -97.2 | 44.3 | usb1k·12 |
| 17997.617 | -98.6 | 43.2 | usb1k·18 |
| 14998.014 | -99.1 | 43.3 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 59.5 | usb1k·1 |
| 6000.000 | -78.7 | 56.8 | fs8·1 |
| 1999.736 | -80.0 | 54.0 | usb1k·2 |
| 12000.000 | -82.1 | 55.4 | fs8·2 |
| 2999.603 | -82.4 | 52.8 | usb1k·3 |
| 3999.471 | -87.1 | 47.6 | usb1k·4 |
| 18000.000 | -88.5 | 48.9 | fs8·3 |
| 4999.339 | -89.0 | 46.7 | usb1k·5 |
| 9998.676 | -89.0 | 48.8 | usb1k·10 |
| 15997.882 | -90.3 | 47.1 | usb1k·16 |
| 8998.809 | -90.3 | 46.8 | usb1k·9 |
| 6999.074 | -90.8 | 46.2 | usb1k·7 |
| 16997.749 | -93.1 | 45.5 | usb1k·17 |
| 5999.206 | -92.7 | 42.9 | usb1k·6 |
| 18997.485 | -94.2 | 44.5 | usb1k·19 |
| 20997.220 | -94.3 | 44.8 | usb1k·21 |
| 7998.941 | -94.9 | 41.4 | usb1k·8 |
| 11998.411 | -95.9 | 41.6 | usb1k·12 |
| 12998.279 | -96.5 | 41.9 | usb1k·13 |
| 13998.147 | -96.7 | 41.3 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.04 | -0.01 | 0.06 |
| usb1k | Kanal 1 | 11/11 | 0.22 | -0.05 | 0.11 |
| led | Kanal 1 | 11/11 | 0.88 | -0.19 | 0.57 |
| mains50 | Kanal 1 | 8/11 | 649.02 | -1492.12 | 6.13 |
| other1 | Kanal 1 | 11/11 | 0.79 | 0.26 | 1.86 |
| other2 | Kanal 1 | 11/11 | 0.10 | -0.05 | 0.08 |
| fs8 | Kanal 2 | 11/11 | 0.03 | -0.01 | 0.07 |
| usb1k | Kanal 2 | 11/11 | 0.24 | -0.06 | 0.10 |
| led | Kanal 2 | 11/11 | 0.25 | 0.29 | 0.40 |
| mains50 | Kanal 2 | 11/11 | 344.27 | -697.58 | 2.81 |
| other1 | Kanal 2 | 11/11 | 0.14 | 0.25 | 0.03 |
| other2 | Kanal 2 | 11/11 | 0.16 | 0.10 | 0.11 |
| fs8 | Kanal 3 | 11/11 | 0.03 | -0.00 | 0.06 |
| usb1k | Kanal 3 | 11/11 | 0.21 | -0.05 | 0.09 |
| led | Kanal 3 | 11/11 | 0.81 | 0.09 | 0.30 |
| mains50 | Kanal 3 | 11/11 | 470.28 | -587.27 | 3.87 |
| other1 | Kanal 3 | 11/11 | 0.11 | 0.09 | 0.18 |
| other2 | Kanal 3 | 11/11 | 0.12 | -0.04 | 0.06 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.04 | 0.06 |
| usb1k | Kanal 4 | 11/11 | 0.19 | -0.01 | 0.13 |
| led | Kanal 4 | 11/11 | 0.94 | 0.77 | 0.60 |
| mains50 | Kanal 4 | 11/11 | 710.57 | -1157.01 | 2.78 |
| other1 | Kanal 4 | 11/11 | 0.32 | -0.06 | 0.09 |
| other2 | Kanal 4 | 11/11 | 0.18 | 0.22 | 0.30 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.03 | 15.00 s (0.07 Hz) | 23.4 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 36.7 |
| Kanal 2 | breitbandig | 0.99 | 0.31 s (3.22 Hz) | 23.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.4 |
| Kanal 3 | breitbandig | 0.60 | 7.50 s (0.13 Hz) | 25.4 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 42.7 |
| Kanal 4 | breitbandig | 1.01 | 15.00 s (0.07 Hz) | 24.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 37.0 |

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

![Langzeit-Spektrum](C1-schliere-r2_psd.png)

### Kammprofile

![Kammprofile](C1-schliere-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](C1-schliere-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:28:54. Stream-Meldungen: 0. owl_read: out/owl_read/C1-schliere-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Out 1 steckt am zweiten Interface. messlog D69
