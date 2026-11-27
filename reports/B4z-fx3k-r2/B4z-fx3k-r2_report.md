# Report B4z-fx3k-r2: B4z-fx3k-r2 – acdc1 fx3k-open-inputs-4z, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4z v22.4.r-fx3k |
| test | Build-4z-Sitzung: fx3k (ITCM ohne USB, Patch 11f + 12b), Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3k-open-inputs-4z-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4z-fx3k-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -69.3 | -77.3 | -70.1 | -70.9 | -86.8 | -70.4 | -94.8 | -70.1 | 79 % | -76.9 | 6.8 |
| Kanal 2 | -7.5 | -69.9 | -78.2 | -70.6 | -71.5 | -88.9 | -70.9 | -95.1 | -70.6 | 83 % | -78.2 | 7.6 |
| Kanal 3 | -5.7 | -71.4 | -83.5 | -71.6 | -72.5 | -93.1 | -71.9 | -95.9 | -71.7 | 89 % | -81.3 | 9.7 |
| Kanal 4 | -6.6 | -69.5 | -78.5 | -70.1 | -70.8 | -89.3 | -70.4 | -95.4 | -70.1 | 83 % | -77.9 | 7.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -83.6 | 4.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -71.4 | 74.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -112.4 dB | -108.3 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9846 | 0.0000 | 1/19 | k=1: 49.985 Hz, -98.8 dB | -101.9 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0026 | 65 | k=-7·f1+4·f2: 17000.927 Hz, -114.6 dB | -103.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.8 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.3 dB | -99.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -83.6 | 5.0 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.3 dB | -71.7 | 77.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.545 Hz, -112.6 dB | -107.2 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9838 | 0.0014 | 2/19 | k=1: 49.985 Hz, -99.5 dB | -102.4 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0032 | 76 | k=-7·f1+4·f2: 17000.927 Hz, -114.9 dB | -103.6 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.5 dB | -97.0 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -84.2 | 5.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -72.4 | 83.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0005 | 10/10 | k=1: 2320.544 Hz, -113.2 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9932 | 0.0102 | 5/19 | k=1: 49.985 Hz, -100.2 dB | -102.3 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0037 | 96 | k=-7·f1+4·f2: 17000.927 Hz, -115.0 dB | -103.5 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.8 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -100.2 dB | -100.4 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -83.8 | 4.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -71.1 | 78.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.545 Hz, -112.0 dB | -107.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9834 | 0.0018 | 2/19 | k=1: 49.985 Hz, -100.0 dB | -102.7 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0040 | 64 | k=-3·f1+4·f2: 21000.398 Hz, -114.4 dB | -103.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -97.4 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.8 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 58.8 | usb1k·1 |
| 2999.603 | -76.9 | 57.2 | usb1k·3 |
| 1999.735 | -77.5 | 55.6 | usb1k·2 |
| 6999.073 | -78.2 | 57.8 | usb1k·7 |
| 14998.013 | -81.4 | 55.9 | usb1k·15 |
| 9998.675 | -81.3 | 55.3 | usb1k·10 |
| 4999.338 | -82.4 | 51.3 | usb1k·5 |
| 6000.000 | -83.9 | 51.7 | fs8·1 |
| 13998.145 | -84.0 | 53.8 | usb1k·14 |
| 21997.086 | -84.3 | 54.0 | usb1k·22 |
| 19997.351 | -85.5 | 51.5 | usb1k·20 |
| 7998.940 | -84.4 | 52.2 | usb1k·8 |
| 12000.000 | -86.0 | 51.4 | fs8·2 |
| 11998.410 | -85.0 | 52.2 | usb1k·12 |
| 18000.000 | -86.6 | 51.4 | fs8·3 |
| 20997.219 | -86.8 | 51.7 | usb1k·21 |
| 16997.748 | -87.1 | 50.4 | usb1k·17 |
| 18997.483 | -87.3 | 51.0 | usb1k·19 |
| 5999.206 | -88.8 | 46.8 | usb1k·6 |
| 8998.808 | -88.4 | 48.5 | usb1k·9 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.3 | 59.6 | usb1k·1 |
| 2999.603 | -77.2 | 58.3 | usb1k·3 |
| 1999.735 | -78.3 | 56.2 | usb1k·2 |
| 6999.073 | -78.4 | 59.0 | usb1k·7 |
| 14998.013 | -81.3 | 57.0 | usb1k·15 |
| 4999.338 | -82.0 | 53.1 | usb1k·5 |
| 9998.675 | -81.2 | 56.3 | usb1k·10 |
| 6000.000 | -83.8 | 53.2 | fs8·1 |
| 21997.086 | -84.4 | 54.9 | usb1k·22 |
| 13998.145 | -84.3 | 54.7 | usb1k·14 |
| 19997.351 | -85.3 | 52.6 | usb1k·20 |
| 7998.941 | -84.1 | 53.9 | usb1k·8 |
| 11998.410 | -84.9 | 53.7 | usb1k·12 |
| 12000.000 | -86.2 | 52.4 | fs8·2 |
| 18000.000 | -86.7 | 52.4 | fs8·3 |
| 16997.748 | -87.1 | 51.4 | usb1k·17 |
| 20997.219 | -87.1 | 52.4 | usb1k·21 |
| 18997.483 | -87.3 | 52.0 | usb1k·19 |
| 5999.206 | -89.4 | 47.6 | usb1k·6 |
| 17997.616 | -90.2 | 48.8 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 63.3 | usb1k·1 |
| 2999.603 | -77.9 | 61.4 | usb1k·3 |
| 1999.735 | -79.2 | 59.6 | usb1k·2 |
| 6999.073 | -78.9 | 61.7 | usb1k·7 |
| 14998.013 | -81.8 | 59.3 | usb1k·15 |
| 4999.338 | -82.3 | 57.0 | usb1k·5 |
| 9998.675 | -81.6 | 59.4 | usb1k·10 |
| 6000.000 | -84.4 | 56.3 | fs8·1 |
| 21997.086 | -84.8 | 55.8 | usb1k·22 |
| 13998.145 | -84.8 | 56.1 | usb1k·14 |
| 19997.351 | -85.7 | 54.9 | usb1k·20 |
| 7998.941 | -84.5 | 56.6 | usb1k·8 |
| 11998.410 | -85.2 | 56.0 | usb1k·12 |
| 12000.000 | -87.1 | 54.3 | fs8·2 |
| 18000.000 | -87.1 | 54.2 | fs8·3 |
| 16997.748 | -87.4 | 53.5 | usb1k·17 |
| 20997.219 | -87.6 | 53.6 | usb1k·21 |
| 18997.483 | -87.8 | 53.2 | usb1k·19 |
| 17997.616 | -90.6 | 50.7 | usb1k·18 |
| 8998.808 | -89.6 | 51.7 | usb1k·9 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 60.9 | usb1k·1 |
| 2999.603 | -76.8 | 58.5 | usb1k·3 |
| 1999.735 | -76.9 | 57.3 | usb1k·2 |
| 6999.073 | -78.3 | 58.6 | usb1k·7 |
| 14998.013 | -81.6 | 56.0 | usb1k·15 |
| 9998.675 | -81.4 | 55.5 | usb1k·10 |
| 4999.338 | -83.3 | 51.4 | usb1k·5 |
| 6000.000 | -83.9 | 52.4 | fs8·1 |
| 13998.145 | -84.0 | 54.1 | usb1k·14 |
| 21997.086 | -84.4 | 54.1 | usb1k·22 |
| 19997.351 | -85.9 | 51.6 | usb1k·20 |
| 7998.941 | -84.7 | 52.5 | usb1k·8 |
| 12000.000 | -86.5 | 51.5 | fs8·2 |
| 11998.410 | -85.6 | 52.2 | usb1k·12 |
| 18000.000 | -86.9 | 51.1 | fs8·3 |
| 20997.219 | -86.8 | 51.8 | usb1k·21 |
| 16997.748 | -87.2 | 51.1 | usb1k·17 |
| 18997.483 | -87.6 | 50.9 | usb1k·19 |
| 5999.206 | -87.8 | 48.5 | usb1k·6 |
| 8998.808 | -87.9 | 49.6 | usb1k·9 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.16 | -0.00 | 0.04 |
| led | Kanal 1 | 11/11 | 0.93 | 1.06 | 0.30 |
| mains50 | Kanal 1 | 11/11 | 269.49 | -157.97 | 0.86 |
| other1 | Kanal 1 | 11/11 | 0.35 | -0.28 | 0.10 |
| other2 | Kanal 1 | 11/11 | 0.21 | -0.10 | 0.19 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.18 | -0.03 | 0.04 |
| led | Kanal 2 | 11/11 | 0.46 | 0.07 | 0.26 |
| mains50 | Kanal 2 | 11/11 | 1016.41 | 820.09 | 0.82 |
| other1 | Kanal 2 | 11/11 | 0.28 | -0.37 | 0.09 |
| other2 | Kanal 2 | 11/11 | 0.19 | 0.01 | 0.15 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.05 | -0.08 | 0.04 |
| led | Kanal 3 | 11/11 | 0.68 | 0.20 | 0.20 |
| mains50 | Kanal 3 | 11/11 | 20.49 | -2.49 | 0.39 |
| other1 | Kanal 3 | 11/11 | 0.23 | -0.18 | 0.09 |
| other2 | Kanal 3 | 11/11 | 0.14 | -0.06 | 0.13 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.00 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.15 | -0.03 | 0.04 |
| led | Kanal 4 | 11/11 | 1.32 | 2.24 | 0.20 |
| mains50 | Kanal 4 | 11/11 | 408.19 | -134.64 | 0.97 |
| other1 | Kanal 4 | 11/11 | 0.26 | -0.22 | 0.09 |
| other2 | Kanal 4 | 11/11 | 0.21 | -0.05 | 0.15 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.79 | 0.16 s (6.40 Hz) | 25.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 37.8 |
| Kanal 2 | breitbandig | 0.71 | 0.16 s (6.40 Hz) | 27.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 39.8 |
| Kanal 3 | breitbandig | 0.41 | 0.31 s (3.18 Hz) | 24.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 44.0 |
| Kanal 4 | breitbandig | 0.59 | 0.16 s (6.40 Hz) | 27.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 39.4 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.96 |
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.94 |
| Kanal 4 | 0.96 | 0.97 | 0.94 | 1.00 |

## Vergleich mit Referenz B4z-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -70.1 | -71.2 | +1.1 | 79 % | 67 % |
| Kanal 2 | -70.6 | -71.7 | +1.1 | 83 % | 73 % |
| Kanal 3 | -71.6 | -72.9 | +1.2 | 89 % | 83 % |
| Kanal 4 | -70.1 | -71.0 | +0.9 | 83 % | 73 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4z-fx3k-r2_psd.png)

### Kammprofile

![Kammprofile](B4z-fx3k-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4z-fx3k-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 19:14:44. Stream-Meldungen: 0. owl_read: reports/owl_read/B4z-fx3k-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
