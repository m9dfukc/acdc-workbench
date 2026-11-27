# Report B8-fx6a-b-r2: B8-fx6a-b-r2 – acdc1 fx6a-open-inputs-8b, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-19 |
| device | acdc1, Firmware Build 8 v22.4.r-fx6a, LED-Modus normal, ins Case geschraubt |
| test | Build-8-Sitzung: fx6a (fx5a + Patch 17) am Ende, LED-Modus normal, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten, Oszillator im Case vom Strom getrennt |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261119_acdc1_fx6a-open-inputs-8b-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B8-fx6a-b-r2` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -68.8 | -75.8 | -69.8 | -70.5 | -85.4 | -70.1 | -94.6 | -69.8 | 59 % | -73.6 | 3.8 |
| Kanal 2 | -7.1 | -70.2 | -78.0 | -71.0 | -71.7 | -87.8 | -71.3 | -94.9 | -71.0 | 65 % | -75.5 | 4.5 |
| Kanal 3 | -5.3 | -72.4 | -80.4 | -73.1 | -73.8 | -91.9 | -73.4 | -95.7 | -73.2 | 70 % | -78.5 | 5.3 |
| Kanal 4 | -6.2 | -69.3 | -78.6 | -69.9 | -70.6 | -87.6 | -70.2 | -95.2 | -69.9 | 62 % | -74.1 | 4.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -83.1 | 4.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -71.1 dB | -72.4 | 53.9 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.001 Hz, -97.9 dB | -98.8 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -96.7 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.1 dB | -83.2 | 6.1 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.0 dB | -73.4 | 58.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0013 | 10/10 | k=9: 20884.904 Hz, -114.7 dB | -110.2 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.001 Hz, -98.4 dB | -99.1 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -98.6 dB | -96.9 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.6 dB | -83.8 | 8.7 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -75.2 | 61.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0015 | 10/10 | k=2: 4641.090 Hz, -117.0 dB | -112.8 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0004 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -99.8 dB | -100.0 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -100.0 dB | -97.7 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.2 dB | -83.4 | 4.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -71.0 dB | -72.3 | 57.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0026 | 8/10 | k=2: 4641.091 Hz, -116.7 dB | -112.2 | 0.0 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0003 | 4/7 | k=1: 3000.001 Hz, -98.7 dB | -99.4 | 0.1 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -97.2 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -71.1 | 58.3 | usb1k·1 |
| 1999.735 | -78.0 | 52.6 | usb1k·2 |
| 2999.603 | -81.7 | 48.7 | usb1k·3 |
| 6000.000 | -84.0 | 47.4 | fs8·1 |
| 12000.000 | -85.3 | 47.6 | fs8·2 |
| 18000.000 | -85.3 | 48.2 | fs8·3 |
| 3999.470 | -86.0 | 45.0 | usb1k·4 |
| 4999.338 | -86.8 | 44.4 | usb1k·5 |
| 15997.880 | -88.9 | 44.6 | usb1k·16 |
| 9998.675 | -88.6 | 44.1 | usb1k·10 |
| 8998.808 | -89.2 | 43.7 | usb1k·9 |
| 16997.747 | -91.5 | 42.0 | usb1k·17 |
| 6999.073 | -90.9 | 41.2 | usb1k·7 |
| 5999.205 | -91.2 | 40.3 | usb1k·6 |
| 18997.483 | -92.3 | 41.0 | usb1k·19 |
| 7998.940 | -92.3 | 40.4 | usb1k·8 |
| 11998.410 | -92.8 | 40.0 | usb1k·12 |
| 20997.218 | -94.3 | 39.3 | usb1k·21 |
| 12998.277 | -95.0 | 38.2 | usb1k·13 |
| 13998.145 | -96.3 | 37.0 | usb1k·14 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.0 | 59.3 | usb1k·1 |
| 1999.735 | -79.0 | 53.4 | usb1k·2 |
| 2999.603 | -82.5 | 49.7 | usb1k·3 |
| 6000.000 | -84.1 | 49.4 | fs8·1 |
| 18000.000 | -85.4 | 50.2 | fs8·3 |
| 12000.000 | -85.6 | 49.6 | fs8·2 |
| 3999.470 | -86.5 | 46.4 | usb1k·4 |
| 4999.338 | -87.8 | 45.4 | usb1k·5 |
| 15997.880 | -89.5 | 46.1 | usb1k·16 |
| 9998.675 | -88.8 | 46.0 | usb1k·10 |
| 8998.808 | -89.8 | 45.1 | usb1k·9 |
| 16997.747 | -92.1 | 43.1 | usb1k·17 |
| 18997.483 | -92.5 | 42.9 | usb1k·19 |
| 6999.073 | -91.7 | 42.6 | usb1k·7 |
| 5999.205 | -92.5 | 40.9 | usb1k·6 |
| 7998.940 | -93.4 | 41.2 | usb1k·8 |
| 11998.410 | -93.4 | 41.8 | usb1k·12 |
| 20997.218 | -94.9 | 40.6 | usb1k·21 |
| 12998.277 | -95.5 | 39.6 | usb1k·13 |
| 13998.145 | -97.5 | 37.7 | usb1k·14 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 60.9 | usb1k·1 |
| 1999.735 | -81.5 | 54.2 | usb1k·2 |
| 2999.603 | -84.1 | 51.6 | usb1k·3 |
| 6000.000 | -84.6 | 51.7 | fs8·1 |
| 18000.000 | -85.8 | 52.0 | fs8·3 |
| 12000.000 | -86.4 | 51.1 | fs8·2 |
| 3999.470 | -87.5 | 48.7 | usb1k·4 |
| 4999.338 | -89.5 | 46.5 | usb1k·5 |
| 15997.880 | -90.6 | 47.7 | usb1k·16 |
| 9998.675 | -89.3 | 48.3 | usb1k·10 |
| 8998.808 | -91.2 | 46.4 | usb1k·9 |
| 18997.483 | -92.9 | 44.9 | usb1k·19 |
| 16997.747 | -93.1 | 44.8 | usb1k·17 |
| 6999.073 | -93.1 | 43.9 | usb1k·7 |
| 11998.410 | -94.6 | 42.9 | usb1k·12 |
| 5999.206 | -95.1 | 41.3 | usb1k·6 |
| 7998.940 | -95.2 | 41.7 | usb1k·8 |
| 20997.218 | -96.5 | 40.8 | usb1k·21 |
| 12998.277 | -96.5 | 41.3 | usb1k·13 |
| 19997.350 | -99.2 | 38.8 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -71.0 | 58.8 | usb1k·1 |
| 1999.735 | -77.5 | 53.5 | usb1k·2 |
| 2999.603 | -81.9 | 49.1 | usb1k·3 |
| 6000.000 | -84.2 | 47.7 | fs8·1 |
| 18000.000 | -85.5 | 48.1 | fs8·3 |
| 12000.000 | -85.8 | 47.6 | fs8·2 |
| 3999.470 | -86.1 | 45.2 | usb1k·4 |
| 4999.338 | -86.4 | 45.2 | usb1k·5 |
| 15997.880 | -88.9 | 45.1 | usb1k·16 |
| 8998.808 | -88.9 | 44.3 | usb1k·9 |
| 9998.675 | -88.9 | 44.2 | usb1k·10 |
| 5999.205 | -90.8 | 41.2 | usb1k·6 |
| 16997.747 | -91.8 | 41.6 | usb1k·17 |
| 6999.073 | -91.1 | 41.3 | usb1k·7 |
| 18997.483 | -92.5 | 41.1 | usb1k·19 |
| 7998.940 | -92.2 | 40.5 | usb1k·8 |
| 11998.410 | -92.7 | 40.8 | usb1k·12 |
| 20997.218 | -94.1 | 39.5 | usb1k·21 |
| 12998.277 | -94.8 | 38.7 | usb1k·13 |
| 13998.145 | -96.3 | 37.3 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | 0.01 | 0.05 |
| usb1k | Kanal 1 | 11/11 | 0.22 | -0.03 | 0.04 |
| other1 | Kanal 1 | 11/11 | 0.27 | 0.39 | 0.26 |
| other2 | Kanal 1 | 11/11 | 0.66 | 0.83 | 0.06 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.01 | 0.05 |
| usb1k | Kanal 2 | 11/11 | 0.22 | -0.03 | 0.02 |
| led | Kanal 2 | 11/11 | 1.02 | 1.51 | 0.66 |
| other1 | Kanal 2 | 11/11 | 0.28 | 0.41 | 0.25 |
| other2 | Kanal 2 | 11/11 | 0.52 | 0.61 | 0.07 |
| fs8 | Kanal 3 | 11/11 | 0.02 | 0.01 | 0.04 |
| usb1k | Kanal 3 | 11/11 | 0.20 | 0.10 | 0.05 |
| led | Kanal 3 | 11/11 | 0.77 | -0.47 | 0.74 |
| other1 | Kanal 3 | 11/11 | 0.15 | 0.19 | 0.19 |
| other2 | Kanal 3 | 11/11 | 0.36 | 0.31 | 0.08 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.01 | 0.06 |
| usb1k | Kanal 4 | 11/11 | 0.20 | -0.11 | 0.03 |
| led | Kanal 4 | 11/11 | 5.95 | 14.39 | 1.41 |
| other1 | Kanal 4 | 11/11 | 0.29 | 0.47 | 0.35 |
| other2 | Kanal 4 | 11/11 | 1.73 | 2.77 | 0.05 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.02 | 0.31 s (3.18 Hz) | 26.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 34.9 |
| Kanal 2 | breitbandig | 0.88 | 0.31 s (3.18 Hz) | 25.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 37.2 |
| Kanal 3 | breitbandig | 0.78 | 0.31 s (3.22 Hz) | 26.4 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 40.6 |
| Kanal 4 | breitbandig | 0.68 | 0.31 s (3.22 Hz) | 24.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 35.2 |

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
| Kanal 1 | 1.00 | 0.97 | 0.96 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.96 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.97 | 0.92 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B8-fx6a-b-r2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B8-fx6a-b-r2_psd.png)

### Kammprofile

![Kammprofile](B8-fx6a-b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B8-fx6a-b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 11:21:00. Stream-Meldungen: 0. owl_read: reports/owl_read/B8-fx6a-b-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
