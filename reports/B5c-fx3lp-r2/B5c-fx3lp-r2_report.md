# Report B5c-fx3lp-r2: B5c-fx3lp-r2 – acdc1 fx3lp-open-inputs-5, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 5c v22.4.r-fx3lp (Füllvariante) |
| test | Build-5-Sitzung: fx3lp (fx3l + Patch 91, Flash-Code +0x150), Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3lp-open-inputs-5-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B5c-fx3lp-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B5c-fx3l-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -69.6 | -73.3 | -72.0 | -72.7 | -85.7 | -72.3 | -94.5 | -72.0 | 67 % | -76.8 | 4.8 |
| Kanal 2 | -7.5 | -70.6 | -74.5 | -72.9 | -73.6 | -87.8 | -73.2 | -94.8 | -72.9 | 71 % | -78.3 | 5.3 |
| Kanal 3 | -5.7 | -72.8 | -77.7 | -74.5 | -75.0 | -92.1 | -74.7 | -95.6 | -74.5 | 82 % | -81.9 | 7.4 |
| Kanal 4 | -6.6 | -70.2 | -75.1 | -71.9 | -72.4 | -88.1 | -72.1 | -95.0 | -71.9 | 75 % | -78.0 | 6.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.9 dB | -83.3 | 7.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -74.3 | 59.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0006 | 10/10 | k=2: 4641.090 Hz, -113.3 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9794 | 0.0000 | 1/19 | k=1: 49.979 Hz, -99.0 dB | -102.0 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0006 | 3 | k=-7·f1+4·f2: 17000.926 Hz, -120.1 dB | -120.2 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -96.2 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0005 | 4/7 | k=1: 3000.000 Hz, -98.3 dB | -99.2 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.1 dB | -83.4 | 8.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.0 | 61.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0005 | 10/10 | k=9: 20884.903 Hz, -113.0 dB | -107.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9791 | 0.0000 | 1/19 | k=1: 49.979 Hz, -99.9 dB | -102.8 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0083 | 4 | k=-23·f1+4·f2: 1003.061 Hz, -117.4 dB | -117.4 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -98.2 dB | -96.5 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.9 dB | -84.0 | 11.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -76.0 | 70.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=2: 4641.090 Hz, -113.9 dB | -109.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9774 | 0.0019 | 3/19 | k=1: 49.979 Hz, -100.4 dB | -103.1 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0071 | 11 | k=25·f1-4·f2: 996.675 Hz, -113.2 dB | -113.1 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.4 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -100.0 dB | -100.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.3 dB | -83.6 | 6.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.2 dB | -73.6 | 68.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0005 | 10/10 | k=2: 4641.090 Hz, -113.0 dB | -108.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9791 | 0.0000 | 1/19 | k=1: 49.979 Hz, -100.6 dB | -103.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0096 | 4 | k=-23·f1+4·f2: 1003.058 Hz, -114.6 dB | -115.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.6 dB | -96.8 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.7 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 58.8 | usb1k·1 |
| 1999.735 | -81.3 | 50.6 | usb1k·2 |
| 2999.603 | -82.6 | 51.6 | usb1k·3 |
| 12000.000 | -83.9 | 53.8 | fs8·2 |
| 6000.000 | -84.7 | 50.7 | fs8·1 |
| 3999.471 | -86.8 | 46.3 | usb1k·4 |
| 18000.000 | -87.3 | 51.5 | fs8·3 |
| 9998.676 | -88.4 | 48.5 | usb1k·10 |
| 4999.339 | -89.4 | 45.6 | usb1k·5 |
| 15997.882 | -90.7 | 47.5 | usb1k·16 |
| 6999.074 | -90.2 | 45.6 | usb1k·7 |
| 8998.809 | -90.8 | 45.7 | usb1k·9 |
| 16997.749 | -93.0 | 45.1 | usb1k·17 |
| 5999.206 | -93.4 | 42.1 | usb1k·6 |
| 20997.220 | -94.1 | 44.8 | usb1k·21 |
| 18997.485 | -94.4 | 43.8 | usb1k·19 |
| 13998.146 | -96.1 | 42.0 | usb1k·14 |
| 11998.411 | -96.5 | 41.2 | usb1k·12 |
| 7998.941 | -96.1 | 40.8 | usb1k·8 |
| 2000.000 | -97.6 | 34.3 | other1·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 59.7 | usb1k·1 |
| 1999.735 | -82.1 | 51.4 | usb1k·2 |
| 2999.603 | -83.3 | 52.6 | usb1k·3 |
| 12000.000 | -84.1 | 54.9 | fs8·2 |
| 6000.000 | -84.8 | 52.4 | fs8·1 |
| 18000.000 | -87.2 | 52.2 | fs8·3 |
| 3999.471 | -87.1 | 47.8 | usb1k·4 |
| 9998.676 | -88.6 | 49.8 | usb1k·10 |
| 4999.339 | -89.9 | 46.3 | usb1k·5 |
| 15997.882 | -90.9 | 48.3 | usb1k·16 |
| 6999.074 | -90.8 | 46.4 | usb1k·7 |
| 8998.809 | -91.1 | 46.8 | usb1k·9 |
| 16997.749 | -93.4 | 45.9 | usb1k·17 |
| 18997.485 | -94.3 | 45.6 | usb1k·19 |
| 20997.220 | -94.5 | 45.3 | usb1k·21 |
| 5999.206 | -94.4 | 42.7 | usb1k·6 |
| 13998.147 | -97.2 | 41.6 | usb1k·14 |
| 11998.411 | -96.8 | 42.2 | usb1k·12 |
| 17997.617 | -98.1 | 41.5 | usb1k·18 |
| 12998.279 | -97.7 | 41.2 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 63.3 | usb1k·1 |
| 1999.735 | -83.6 | 54.7 | usb1k·2 |
| 2999.603 | -84.1 | 55.9 | usb1k·3 |
| 12000.000 | -84.9 | 56.8 | fs8·2 |
| 6000.000 | -85.3 | 55.5 | fs8·1 |
| 18000.000 | -87.7 | 54.8 | fs8·3 |
| 3999.471 | -87.7 | 51.8 | usb1k·4 |
| 9998.676 | -88.8 | 52.8 | usb1k·10 |
| 15997.882 | -91.4 | 50.7 | usb1k·16 |
| 4999.339 | -91.0 | 49.5 | usb1k·5 |
| 6999.074 | -91.6 | 49.6 | usb1k·7 |
| 16997.750 | -93.8 | 48.4 | usb1k·17 |
| 8998.809 | -92.2 | 49.4 | usb1k·9 |
| 18997.485 | -94.6 | 47.7 | usb1k·19 |
| 20997.220 | -95.3 | 46.8 | usb1k·21 |
| 5999.206 | -96.0 | 44.8 | usb1k·6 |
| 11998.411 | -97.3 | 44.3 | usb1k·12 |
| 17997.617 | -98.4 | 44.0 | usb1k·18 |
| 12998.279 | -98.0 | 44.2 | usb1k·13 |
| 13998.147 | -98.5 | 43.5 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.2 | 60.6 | usb1k·1 |
| 1999.735 | -79.9 | 53.4 | usb1k·2 |
| 2999.603 | -82.3 | 53.5 | usb1k·3 |
| 12000.000 | -84.3 | 53.9 | fs8·2 |
| 6000.000 | -85.0 | 51.6 | fs8·1 |
| 3999.471 | -86.6 | 48.2 | usb1k·4 |
| 18000.000 | -87.5 | 50.8 | fs8·3 |
| 4999.338 | -88.2 | 47.7 | usb1k·5 |
| 9998.676 | -88.6 | 49.0 | usb1k·10 |
| 15997.882 | -90.2 | 48.2 | usb1k·16 |
| 6999.074 | -89.9 | 46.6 | usb1k·7 |
| 8998.809 | -89.9 | 47.6 | usb1k·9 |
| 5999.206 | -91.8 | 44.9 | usb1k·6 |
| 16997.749 | -93.1 | 45.4 | usb1k·17 |
| 20997.220 | -93.8 | 45.4 | usb1k·21 |
| 18997.485 | -94.6 | 44.5 | usb1k·19 |
| 13998.147 | -95.6 | 42.6 | usb1k·14 |
| 7998.941 | -94.7 | 42.7 | usb1k·8 |
| 11998.411 | -95.7 | 42.6 | usb1k·12 |
| 12998.279 | -97.1 | 41.6 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.16 | -0.00 | 0.06 |
| led | Kanal 1 | 11/11 | 1.74 | 1.40 | 0.45 |
| mains50 | Kanal 1 | 11/11 | 331.30 | 159.96 | 1.16 |
| other1 | Kanal 1 | 11/11 | 1.13 | 0.37 | 0.14 |
| other2 | Kanal 1 | 11/11 | 0.27 | 0.04 | 0.20 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.02 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.16 | 0.03 | 0.06 |
| led | Kanal 2 | 11/11 | 0.28 | -0.12 | 0.26 |
| mains50 | Kanal 2 | 11/11 | 302.21 | 202.48 | 1.09 |
| other1 | Kanal 2 | 11/11 | 1.61 | 1.53 | 0.12 |
| other2 | Kanal 2 | 11/11 | 0.19 | 0.12 | 0.16 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.13 | 0.03 | 0.07 |
| led | Kanal 3 | 11/11 | 1.11 | -0.26 | 0.30 |
| mains50 | Kanal 3 | 11/11 | 698.48 | 1393.73 | 0.64 |
| other1 | Kanal 3 | 11/11 | 1.28 | 1.75 | 0.14 |
| other2 | Kanal 3 | 11/11 | 0.11 | 0.03 | 0.13 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.12 | -0.00 | 0.08 |
| led | Kanal 4 | 11/11 | 1.15 | -0.12 | 0.40 |
| mains50 | Kanal 4 | 11/11 | 328.81 | 188.04 | 1.13 |
| other1 | Kanal 4 | 11/11 | 0.14 | -0.08 | 0.08 |
| other2 | Kanal 4 | 11/11 | 0.17 | 0.20 | 0.17 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.92 | 0.31 s (3.18 Hz) | 31.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 37.1 |
| Kanal 2 | breitbandig | 1.80 | 0.31 s (3.18 Hz) | 31.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 38.3 |
| Kanal 3 | breitbandig | 1.49 | 0.31 s (3.18 Hz) | 34.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 42.9 |
| Kanal 4 | breitbandig | 1.39 | 0.16 s (6.38 Hz) | 31.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.89 | 7.50 s (0.13 Hz) | 38.2 |

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
| Kanal 1 | 1.00 | 0.98 | 0.94 | 0.95 |
| Kanal 2 | 0.98 | 1.00 | 0.94 | 0.97 |
| Kanal 3 | 0.94 | 0.94 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz B5c-fx3l-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.0 | -72.0 | +0.1 | 67 % | 68 % |
| Kanal 2 | -72.9 | -73.0 | +0.1 | 71 % | 71 % |
| Kanal 3 | -74.5 | -74.4 | -0.0 | 82 % | 83 % |
| Kanal 4 | -71.9 | -72.0 | +0.1 | 75 % | 75 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B5c-fx3lp-r2_psd.png)

### Kammprofile

![Kammprofile](B5c-fx3lp-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B5c-fx3lp-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 22:01:38. Stream-Meldungen: 0. owl_read: reports/owl_read/B5c-fx3lp-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
