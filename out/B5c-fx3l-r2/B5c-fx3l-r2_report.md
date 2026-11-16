# Report B5c-fx3l-r2: B5c-fx3l-r2 – acdc1 fx3l-open-inputs-5, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 5c v22.4.r-fx3l |
| test | Build-5-Sitzung: fx3l (alle Gruppen im ITCM, Patch 11g + 12b + 14), Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3l-open-inputs-5-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B5c-fx3l-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-end-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -71.3 | -79.7 | -72.0 | -72.7 | -86.4 | -72.3 | -94.8 | -72.0 | 68 % | -77.0 | 5.0 |
| Kanal 2 | -7.6 | -72.2 | -81.0 | -72.9 | -73.5 | -88.4 | -73.1 | -95.0 | -72.9 | 72 % | -78.4 | 5.5 |
| Kanal 3 | -5.8 | -73.7 | -82.1 | -74.4 | -74.9 | -92.7 | -74.5 | -95.8 | -74.4 | 83 % | -82.0 | 7.6 |
| Kanal 4 | -6.6 | -71.5 | -82.3 | -71.8 | -72.3 | -88.8 | -72.0 | -95.3 | -71.9 | 76 % | -78.1 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.3 dB | -83.1 | 7.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -74.2 | 60.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -113.5 dB | -109.3 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0433 | 0.0000 | 1/19 | k=1: 50.043 Hz, -98.9 dB | -101.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0027 | 2 | k=-3·f1+4·f2: 21000.399 Hz, -122.6 dB | -122.9 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.9 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.1 dB | -99.0 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.2 | 9.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -74.9 | 62.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0007 | 10/10 | k=9: 20884.903 Hz, -113.5 dB | -107.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0432 | 0.0000 | 1/19 | k=1: 50.043 Hz, -99.7 dB | -102.3 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0027 | 3 | k=-3·f1+4·f2: 21000.402 Hz, -122.2 dB | -121.3 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0002 | 0.0005 | 4/7 | k=1: 3000.000 Hz, -98.5 dB | -99.2 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.5 dB | -97.1 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.9 dB | -83.8 | 11.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.6 dB | -75.9 | 70.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0005 | 10/10 | k=1: 2320.544 Hz, -113.9 dB | -109.3 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0426 | 0.0004 | 2/19 | k=1: 50.043 Hz, -100.4 dB | -103.0 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0029 | 16 | k=-3·f1+4·f2: 21000.397 Hz, -122.7 dB | -116.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -99.9 dB | -97.8 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.9 dB | -100.2 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -83.3 | 7.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.0 dB | -73.5 | 68.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -112.8 dB | -108.6 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0433 | 0.0000 | 1/19 | k=1: 50.043 Hz, -100.1 dB | -102.7 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0035 | 2 | k=-3·f1+4·f2: 21000.402 Hz, -123.0 dB | -122.9 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0005 | 4/7 | k=1: 3000.000 Hz, -98.8 dB | -99.5 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -97.4 | 0.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 59.3 | usb1k·1 |
| 1999.735 | -80.8 | 52.5 | usb1k·2 |
| 2999.603 | -82.5 | 51.6 | usb1k·3 |
| 6000.000 | -84.3 | 51.9 | fs8·1 |
| 12000.000 | -85.0 | 53.2 | fs8·2 |
| 18000.000 | -85.4 | 53.5 | fs8·3 |
| 3999.471 | -87.0 | 47.9 | usb1k·4 |
| 9998.676 | -88.5 | 49.2 | usb1k·10 |
| 4999.338 | -89.5 | 46.6 | usb1k·5 |
| 15997.881 | -90.7 | 47.5 | usb1k·16 |
| 6999.073 | -90.1 | 46.4 | usb1k·7 |
| 8998.808 | -90.7 | 45.7 | usb1k·9 |
| 16997.749 | -93.3 | 45.2 | usb1k·17 |
| 5999.206 | -93.5 | 42.6 | usb1k·6 |
| 18997.484 | -94.4 | 44.4 | usb1k·19 |
| 20997.219 | -94.3 | 44.5 | usb1k·21 |
| 13998.146 | -96.2 | 41.9 | usb1k·14 |
| 11998.411 | -96.6 | 41.5 | usb1k·12 |
| 12998.278 | -97.1 | 41.1 | usb1k·13 |
| 7998.941 | -96.3 | 40.3 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 60.0 | usb1k·1 |
| 1999.735 | -81.9 | 52.9 | usb1k·2 |
| 2999.603 | -83.1 | 52.7 | usb1k·3 |
| 6000.000 | -84.2 | 53.3 | fs8·1 |
| 12000.000 | -85.2 | 53.9 | fs8·2 |
| 18000.000 | -85.5 | 54.2 | fs8·3 |
| 3999.471 | -87.3 | 49.1 | usb1k·4 |
| 9998.676 | -88.5 | 50.1 | usb1k·10 |
| 4999.338 | -90.3 | 47.1 | usb1k·5 |
| 15997.881 | -91.0 | 48.2 | usb1k·16 |
| 6999.073 | -90.8 | 47.0 | usb1k·7 |
| 8998.808 | -91.2 | 46.5 | usb1k·9 |
| 16997.749 | -93.6 | 46.5 | usb1k·17 |
| 18997.484 | -94.3 | 45.3 | usb1k·19 |
| 20997.219 | -94.8 | 44.9 | usb1k·21 |
| 5999.206 | -94.7 | 42.7 | usb1k·6 |
| 13998.146 | -97.3 | 42.0 | usb1k·14 |
| 12998.278 | -97.2 | 41.9 | usb1k·13 |
| 11998.411 | -97.0 | 42.0 | usb1k·12 |
| 17997.617 | -97.8 | 41.6 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.6 | 63.7 | usb1k·1 |
| 1999.735 | -83.1 | 56.4 | usb1k·2 |
| 2999.603 | -84.0 | 56.1 | usb1k·3 |
| 6000.000 | -84.9 | 56.4 | fs8·1 |
| 18000.000 | -85.9 | 56.4 | fs8·3 |
| 12000.000 | -86.0 | 56.4 | fs8·2 |
| 3999.471 | -87.9 | 53.2 | usb1k·4 |
| 9998.676 | -88.9 | 53.3 | usb1k·10 |
| 15997.881 | -91.4 | 50.4 | usb1k·16 |
| 4999.338 | -91.0 | 50.2 | usb1k·5 |
| 6999.073 | -91.5 | 50.0 | usb1k·7 |
| 8998.808 | -92.0 | 49.6 | usb1k·9 |
| 16997.749 | -94.0 | 48.5 | usb1k·17 |
| 18997.484 | -94.5 | 48.4 | usb1k·19 |
| 20997.219 | -95.4 | 46.8 | usb1k·21 |
| 5999.206 | -96.0 | 45.2 | usb1k·6 |
| 11998.411 | -97.3 | 45.1 | usb1k·12 |
| 17997.616 | -98.1 | 44.2 | usb1k·18 |
| 12998.278 | -97.8 | 44.8 | usb1k·13 |
| 14998.013 | -98.4 | 42.3 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.0 | 61.4 | usb1k·1 |
| 1999.735 | -79.8 | 54.8 | usb1k·2 |
| 2999.603 | -82.2 | 53.2 | usb1k·3 |
| 6000.000 | -84.4 | 52.9 | fs8·1 |
| 12000.000 | -85.4 | 52.9 | fs8·2 |
| 18000.000 | -85.6 | 53.4 | fs8·3 |
| 3999.471 | -86.8 | 49.4 | usb1k·4 |
| 4999.338 | -88.5 | 47.8 | usb1k·5 |
| 9998.676 | -88.6 | 49.7 | usb1k·10 |
| 15997.881 | -90.4 | 48.5 | usb1k·16 |
| 6999.073 | -90.1 | 47.1 | usb1k·7 |
| 8998.808 | -90.0 | 47.1 | usb1k·9 |
| 5999.206 | -91.9 | 45.3 | usb1k·6 |
| 16997.749 | -93.2 | 45.6 | usb1k·17 |
| 20997.219 | -94.1 | 45.2 | usb1k·21 |
| 18997.484 | -94.6 | 44.4 | usb1k·19 |
| 13998.146 | -95.8 | 43.1 | usb1k·14 |
| 7998.941 | -94.9 | 42.5 | usb1k·8 |
| 11998.411 | -96.0 | 42.2 | usb1k·12 |
| 12998.278 | -96.5 | 42.0 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.15 | 0.14 | 0.04 |
| led | Kanal 1 | 11/11 | 1.29 | -0.40 | 0.64 |
| mains50 | Kanal 1 | 11/11 | 221.61 | 350.97 | 0.93 |
| other1 | Kanal 1 | 11/11 | 0.57 | 0.12 | 0.06 |
| other2 | Kanal 1 | 11/11 | 0.21 | -0.06 | 0.12 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.19 | 0.14 | 0.02 |
| led | Kanal 2 | 11/11 | 0.21 | -0.29 | 0.51 |
| mains50 | Kanal 2 | 11/11 | 234.66 | 341.05 | 0.99 |
| other1 | Kanal 2 | 11/11 | 0.13 | -0.09 | 0.13 |
| other2 | Kanal 2 | 11/11 | 0.47 | -0.13 | 0.06 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.14 | 0.05 | 0.05 |
| led | Kanal 3 | 11/11 | 0.77 | -0.07 | 0.28 |
| mains50 | Kanal 3 | 11/11 | 790.04 | 474.06 | 0.52 |
| other1 | Kanal 3 | 11/11 | 0.33 | -0.00 | 0.03 |
| other2 | Kanal 3 | 11/11 | 0.10 | -0.04 | 0.09 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.04 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.14 | 0.15 | 0.03 |
| led | Kanal 4 | 11/11 | 0.87 | -0.60 | 0.63 |
| mains50 | Kanal 4 | 11/11 | 260.83 | 377.42 | 0.98 |
| other1 | Kanal 4 | 11/11 | 0.21 | -0.14 | 0.15 |
| other2 | Kanal 4 | 11/11 | 0.58 | -0.38 | 0.06 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.80 | 7.50 s (0.13 Hz) | 21.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.6 |
| Kanal 2 | breitbandig | 0.74 | 7.50 s (0.13 Hz) | 19.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 39.5 |
| Kanal 3 | breitbandig | 0.69 | 7.50 s (0.13 Hz) | 27.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.8 |
| Kanal 4 | breitbandig | 0.53 | 7.50 s (0.13 Hz) | 21.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 7.50 s (0.13 Hz) | 39.3 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4z-3d-end-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.0 | -71.0 | -1.0 | 68 % | 67 % |
| Kanal 2 | -72.9 | -71.8 | -1.1 | 72 % | 73 % |
| Kanal 3 | -74.4 | -73.1 | -1.3 | 83 % | 82 % |
| Kanal 4 | -71.8 | -70.9 | -0.9 | 76 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B5c-fx3l-r2_psd.png)

### Kammprofile

![Kammprofile](B5c-fx3l-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B5c-fx3l-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 21:56:36. Stream-Meldungen: 0. owl_read: out/owl_read/B5c-fx3l-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
