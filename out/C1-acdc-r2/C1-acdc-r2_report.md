# Report C1-acdc-r2: C1-acdc-r2 – acdc1 case-acdc-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-18 |
| device | acdc1, Firmware Build 7 v22.4.r-fx5a, ins Case geschraubt |
| test | Case-Sitzung, Kontrolle: Eingänge offen, rohe ADC-Daten, Default-Patch läuft. Regler wie C1-schliere |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261118_acdc1_case-acdc-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis C1-acdc-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -71.3 | -80.8 | -71.8 | -72.3 | -86.8 | -72.0 | -97.0 | -71.8 | 70 % | -76.9 | 5.2 |
| Kanal 2 | -7.4 | -72.4 | -81.8 | -73.0 | -73.6 | -88.9 | -73.2 | -93.6 | -73.0 | 72 % | -78.5 | 5.5 |
| Kanal 3 | -5.5 | -74.5 | -86.9 | -74.8 | -75.3 | -93.4 | -75.0 | -90.9 | -74.9 | 83 % | -82.5 | 7.6 |
| Kanal 4 | -6.5 | -71.5 | -81.8 | -71.9 | -72.4 | -89.1 | -72.1 | -97.4 | -71.9 | 75 % | -78.0 | 6.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -83.3 | 7.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.8 | 62.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5446 | 0.0010 | 10/10 | k=1: 2320.543 Hz, -112.5 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9081 | 0.0101 | 3/19 | k=3: 149.713 Hz, -109.1 dB | -105.9 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0025 | 5 | k=1·f1+1·f2: 6999.870 Hz, -117.7 dB | -117.0 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 1 | 4000.0004 | 0.0004 | 4/5 | k=1: 4000.000 Hz, -100.6 dB | -99.9 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.001 Hz, -100.7 dB | -100.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.3 dB | -83.3 | 9.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.1 | 62.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.543 Hz, -113.5 dB | -108.0 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9080 | 0.0109 | 3/19 | k=3: 149.711 Hz, -109.9 dB | -107.3 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0016 | 7 | k=1·f1+1·f2: 6999.869 Hz, -117.5 dB | -115.8 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 2 | 4000.0004 | 0.0004 | 4/5 | k=1: 4000.000 Hz, -100.8 dB | -100.0 | 0.2 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 2 | 1000.0001 | 0.0003 | 16/23 | k=1: 1000.000 Hz, -100.9 dB | -94.7 | 0.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -83.9 | 12.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -76.4 | 70.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0005 | 10/10 | k=1: 2320.544 Hz, -113.2 dB | -109.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9080 | 0.0101 | 3/19 | k=3: 149.713 Hz, -115.5 dB | -112.5 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0047 | 13 | k=-7·f1+4·f2: 17000.926 Hz, -122.0 dB | -116.5 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 3 | 4000.0004 | 0.0003 | 4/5 | k=1: 4000.000 Hz, -101.6 dB | -100.8 | 0.3 % |
| stärkste übrige Linie (500.00 Hz) | Kanal 3 | 500.0001 | 0.0002 | 40/47 | k=1: 500.000 Hz, -101.7 dB | -91.3 | 2.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -83.5 | 6.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.1 dB | -73.6 | 68.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0006 | 10/10 | k=1: 2320.544 Hz, -112.8 dB | -108.7 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9080 | 0.0109 | 3/19 | k=3: 149.712 Hz, -109.6 dB | -107.2 | 0.0 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0028 | 3 | k=1·f1+1·f2: 6999.870 Hz, -119.0 dB | -119.0 | 0.0 % |
| stärkste übrige Linie (4000.00 Hz) | Kanal 4 | 4000.0004 | 0.0002 | 4/5 | k=1: 4000.000 Hz, -101.1 dB | -100.3 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -101.2 dB | -100.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 59.6 | usb1k·1 |
| 1999.735 | -80.4 | 52.8 | usb1k·2 |
| 2999.603 | -82.3 | 51.4 | usb1k·3 |
| 6000.000 | -83.4 | 52.4 | fs8·1 |
| 12000.000 | -85.6 | 52.2 | fs8·2 |
| 18000.000 | -86.7 | 51.5 | fs8·3 |
| 3999.471 | -86.8 | 48.0 | usb1k·4 |
| 4999.338 | -89.0 | 46.2 | usb1k·5 |
| 9998.676 | -88.7 | 48.3 | usb1k·10 |
| 15997.882 | -90.2 | 47.6 | usb1k·16 |
| 6999.073 | -90.6 | 46.2 | usb1k·7 |
| 8998.809 | -90.6 | 46.2 | usb1k·9 |
| 16997.750 | -92.6 | 45.8 | usb1k·17 |
| 18997.485 | -93.8 | 44.8 | usb1k·19 |
| 5999.206 | -93.3 | 42.5 | usb1k·6 |
| 20997.220 | -94.4 | 43.9 | usb1k·21 |
| 11998.411 | -95.2 | 42.4 | usb1k·12 |
| 7998.941 | -94.7 | 42.6 | usb1k·8 |
| 13998.146 | -96.5 | 41.2 | usb1k·14 |
| 12998.279 | -96.6 | 41.1 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 59.6 | usb1k·1 |
| 1999.735 | -82.1 | 52.7 | usb1k·2 |
| 6000.000 | -83.3 | 53.7 | fs8·1 |
| 2999.603 | -83.3 | 52.2 | usb1k·3 |
| 12000.000 | -85.9 | 52.9 | fs8·2 |
| 18000.000 | -86.8 | 52.4 | fs8·3 |
| 3999.471 | -87.4 | 48.7 | usb1k·4 |
| 9998.676 | -88.8 | 49.5 | usb1k·10 |
| 4999.338 | -90.1 | 46.5 | usb1k·5 |
| 15997.882 | -90.9 | 48.3 | usb1k·16 |
| 6999.073 | -91.7 | 46.8 | usb1k·7 |
| 8998.809 | -91.2 | 47.1 | usb1k·9 |
| 16997.750 | -93.1 | 46.3 | usb1k·17 |
| 18997.485 | -93.8 | 45.5 | usb1k·19 |
| 20997.220 | -95.1 | 44.3 | usb1k·21 |
| 5999.206 | -94.9 | 42.1 | usb1k·6 |
| 11998.411 | -96.0 | 42.8 | usb1k·12 |
| 12998.279 | -96.8 | 42.1 | usb1k·13 |
| 7998.941 | -96.3 | 42.3 | usb1k·8 |
| 17997.617 | -98.4 | 40.8 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 63.2 | usb1k·1 |
| 1999.735 | -83.2 | 56.4 | usb1k·2 |
| 6000.000 | -83.9 | 57.3 | fs8·1 |
| 2999.603 | -84.6 | 55.2 | usb1k·3 |
| 12000.000 | -86.7 | 55.8 | fs8·2 |
| 18000.000 | -87.1 | 55.1 | fs8·3 |
| 3999.471 | -88.1 | 52.4 | usb1k·4 |
| 9998.676 | -89.3 | 52.7 | usb1k·10 |
| 15997.882 | -91.5 | 50.8 | usb1k·16 |
| 4999.338 | -91.1 | 49.9 | usb1k·5 |
| 8998.809 | -91.9 | 49.9 | usb1k·9 |
| 6999.073 | -92.7 | 49.4 | usb1k·7 |
| 16997.750 | -94.1 | 48.3 | usb1k·17 |
| 18997.485 | -94.1 | 48.0 | usb1k·19 |
| 20997.220 | -95.8 | 46.5 | usb1k·21 |
| 11998.411 | -96.7 | 45.7 | usb1k·12 |
| 12998.279 | -97.1 | 45.2 | usb1k·13 |
| 5999.206 | -97.2 | 44.1 | usb1k·6 |
| 17997.617 | -98.6 | 43.8 | usb1k·18 |
| 7998.941 | -97.7 | 44.7 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.1 | 60.7 | usb1k·1 |
| 1999.735 | -80.0 | 54.7 | usb1k·2 |
| 2999.603 | -82.3 | 52.6 | usb1k·3 |
| 6000.000 | -83.4 | 52.9 | fs8·1 |
| 12000.000 | -86.1 | 52.3 | fs8·2 |
| 18000.000 | -87.1 | 51.8 | fs8·3 |
| 3999.471 | -86.9 | 48.6 | usb1k·4 |
| 4999.338 | -88.6 | 47.0 | usb1k·5 |
| 9998.676 | -88.9 | 48.7 | usb1k·10 |
| 15997.882 | -90.3 | 48.2 | usb1k·16 |
| 8998.808 | -90.2 | 47.8 | usb1k·9 |
| 6999.073 | -91.1 | 46.5 | usb1k·7 |
| 16997.750 | -92.8 | 45.6 | usb1k·17 |
| 5999.206 | -92.4 | 43.9 | usb1k·6 |
| 18997.485 | -94.1 | 44.1 | usb1k·19 |
| 20997.220 | -94.3 | 44.5 | usb1k·21 |
| 7998.941 | -94.3 | 43.4 | usb1k·8 |
| 11998.411 | -95.2 | 43.2 | usb1k·12 |
| 12998.279 | -96.2 | 41.7 | usb1k·13 |
| 13998.146 | -96.7 | 41.7 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | -0.02 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.15 | -0.04 | 0.03 |
| led | Kanal 1 | 11/11 | 1.53 | 1.52 | 0.35 |
| mains50 | Kanal 1 | 11/11 | 239.73 | 684.52 | 0.80 |
| other1 | Kanal 1 | 11/11 | 0.11 | -0.12 | 0.22 |
| other2 | Kanal 1 | 11/11 | 0.27 | -0.24 | 0.23 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.02 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.16 | -0.06 | 0.04 |
| led | Kanal 2 | 11/11 | 0.54 | -0.33 | 0.32 |
| mains50 | Kanal 2 | 11/11 | 239.58 | 686.91 | 0.76 |
| other1 | Kanal 2 | 11/11 | 0.13 | -0.23 | 0.19 |
| other2 | Kanal 2 | 11/11 | 10.21 | 6.77 | 0.04 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.15 | -0.10 | 0.04 |
| led | Kanal 3 | 11/11 | 0.98 | 0.12 | 0.25 |
| mains50 | Kanal 3 | 11/11 | 239.35 | 702.82 | 0.82 |
| other1 | Kanal 3 | 11/11 | 0.09 | -0.05 | 0.11 |
| other2 | Kanal 3 | 11/11 | 36.91 | -29.11 | 0.04 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.04 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.13 | -0.09 | 0.05 |
| led | Kanal 4 | 11/11 | 1.48 | -0.69 | 0.29 |
| mains50 | Kanal 4 | 11/11 | 236.98 | 660.43 | 0.72 |
| other1 | Kanal 4 | 11/11 | 0.28 | -0.09 | 0.19 |
| other2 | Kanal 4 | 11/11 | 0.20 | 0.05 | 0.18 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.67 | 0.31 s (3.18 Hz) | 21.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 39.2 |
| Kanal 2 | breitbandig | 0.67 | 0.16 s (6.40 Hz) | 22.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 40.1 |
| Kanal 3 | breitbandig | 0.42 | 7.50 s (0.13 Hz) | 24.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.9 |
| Kanal 4 | breitbandig | 0.56 | 0.16 s (6.40 Hz) | 22.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 38.7 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.96 | 0.93 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](C1-acdc-r2_psd.png)

### Kammprofile

![Kammprofile](C1-acdc-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](C1-acdc-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:31:32. Stream-Meldungen: 0. owl_read: out/owl_read/C1-acdc-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Out 1 steckt am zweiten Interface. messlog D69
