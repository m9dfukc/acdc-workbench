# Report B3-fx2c-r2: B3-fx2c-r2 – acdc1 Build 3c, rohe Eingänge offen, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 3c v22.4.r-fx2c (Build 2 + Patch 07c, Eingangs-LEDs roh bei TX, Messung in onLoop) |
| test | A/B gegen Kontrolle D31 2/2: Eingänge offen, rohe ADC-Daten (vor dem Patch) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx2c-open-inputs-r2_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx2c-r2 --ref B3-fx1d-k-r2 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -69.4 | -74.6 | -70.9 | -72.0 | -85.6 | -71.3 | -99.6 | -70.9 | 70 % | -76.2 | 5.2 |
| Kanal 2 | -6.9 | -70.2 | -75.8 | -71.6 | -72.7 | -87.5 | -72.0 | -101.0 | -71.6 | 76 % | -77.8 | 6.1 |
| Kanal 3 | -5.1 | -72.2 | -80.2 | -73.0 | -74.1 | -91.7 | -73.2 | -105.3 | -73.0 | 85 % | -81.3 | 8.3 |
| Kanal 4 | -6.0 | -69.8 | -76.2 | -70.9 | -71.8 | -87.7 | -71.2 | -101.0 | -70.9 | 76 % | -77.1 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.9 dB | -77.1 | 24.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.867 Hz, -72.7 dB | -74.5 | 43.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0019 | 10/10 | k=2: 4641.093 Hz, -116.0 dB | -112.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0004 | 0.0060 | 3/19 | k=1: 50.005 Hz, -94.6 dB | -97.6 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0010 | 130 | k=15·f1+1·f2: 20998.014 Hz, -100.4 dB | -89.9 | 1.3 % |
| stärkste übrige Linie (51.26 Hz) | Kanal 1 | 51.2610 | 0.0036 | 3/465 | k=1: 51.262 Hz, -100.4 dB | -102.7 | 0.1 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 1 | 1215.1898 | 0.0013 | 9/19 | k=1: 1215.190 Hz, -101.6 dB | -102.5 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.9 dB | -77.0 | 29.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.4 dB | -75.2 | 44.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0013 | 10/10 | k=9: 20884.904 Hz, -115.0 dB | -110.3 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0003 | 0.0061 | 3/19 | k=1: 50.005 Hz, -95.3 dB | -98.3 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0010 | 140 | k=15·f1+1·f2: 20998.014 Hz, -100.3 dB | -89.8 | 1.5 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 2 | 23000.9268 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -101.9 dB | -105.0 | 0.0 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 2 | 1215.1898 | 0.0014 | 11/19 | k=1: 1215.190 Hz, -102.3 dB | -103.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.2 | 37.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0005 | 23/23 | k=1: 999.867 Hz, -74.8 dB | -76.4 | 45.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0013 | 10/10 | k=2: 4641.092 Hz, -117.5 dB | -113.7 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0056 | 0.0013 | 3/19 | k=1: 50.005 Hz, -95.8 dB | -98.9 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0008 | 154 | k=15·f1+1·f2: 20998.014 Hz, -100.5 dB | -90.0 | 2.0 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9269 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -102.2 dB | -105.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.2 dB | -77.2 | 23.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.867 Hz, -72.1 dB | -73.8 | 51.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0015 | 10/10 | k=2: 4641.092 Hz, -114.9 dB | -111.3 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0003 | 0.0063 | 3/19 | k=1: 50.005 Hz, -95.8 dB | -98.7 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0017 | 132 | k=15·f1+1·f2: 20998.014 Hz, -100.4 dB | -89.9 | 1.3 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1898 | 0.0015 | 9/19 | k=1: 1215.190 Hz, -102.1 dB | -103.1 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 4 | 23000.9268 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -102.1 dB | -105.2 | 0.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.7 | 58.2 | usb1k·1 |
| 6000.000 | -76.9 | 58.5 | fs8·1 |
| 12000.000 | -79.9 | 56.7 | fs8·2 |
| 18000.000 | -80.6 | 55.8 | fs8·3 |
| 1999.735 | -82.9 | 49.3 | usb1k·2 |
| 3999.470 | -84.2 | 49.0 | usb1k·4 |
| 4999.338 | -85.7 | 49.0 | usb1k·5 |
| 2999.603 | -88.4 | 45.4 | usb1k·3 |
| 7998.941 | -87.6 | 47.9 | usb1k·8 |
| 15997.881 | -90.7 | 45.8 | usb1k·16 |
| 11998.411 | -91.2 | 45.3 | usb1k·12 |
| 8998.808 | -92.2 | 43.3 | usb1k·9 |
| 18997.484 | -92.8 | 44.3 | usb1k·19 |
| 16997.749 | -94.7 | 41.8 | usb1k·17 |
| 9998.676 | -95.7 | 40.1 | usb1k·10 |
| 22996.954 | -95.4 | 43.1 | usb1k·23 |
| 10998.543 | -94.7 | 42.0 | usb1k·11 |
| 50.005 | -94.6 | 27.4 | mains50·1 |
| 12998.279 | -98.0 | 38.2 | usb1k·13 |
| 5999.206 | -98.0 | 37.5 | usb1k·6 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.4 | 59.2 | usb1k·1 |
| 6000.000 | -76.9 | 60.4 | fs8·1 |
| 12000.000 | -79.7 | 58.3 | fs8·2 |
| 18000.000 | -80.6 | 57.8 | fs8·3 |
| 1999.735 | -83.6 | 50.3 | usb1k·2 |
| 3999.470 | -84.4 | 50.8 | usb1k·4 |
| 4999.338 | -86.2 | 50.0 | usb1k·5 |
| 2999.603 | -89.5 | 46.2 | usb1k·3 |
| 7998.941 | -88.0 | 49.3 | usb1k·8 |
| 15997.881 | -90.8 | 47.0 | usb1k·16 |
| 11998.411 | -91.3 | 46.6 | usb1k·12 |
| 8998.808 | -92.2 | 45.1 | usb1k·9 |
| 18997.484 | -92.7 | 45.9 | usb1k·19 |
| 10998.543 | -94.2 | 44.3 | usb1k·11 |
| 16997.749 | -95.1 | 43.2 | usb1k·17 |
| 22996.954 | -95.5 | 44.5 | usb1k·23 |
| 9998.676 | -96.1 | 41.3 | usb1k·10 |
| 50.005 | -95.3 | 28.6 | mains50·1 |
| 12998.279 | -98.1 | 39.6 | usb1k·13 |
| 5999.206 | -99.1 | 38.2 | usb1k·6 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.8 | 62.5 | usb1k·1 |
| 6000.000 | -77.3 | 63.7 | fs8·1 |
| 12000.000 | -79.8 | 61.6 | fs8·2 |
| 18000.000 | -80.7 | 60.4 | fs8·3 |
| 3999.470 | -85.1 | 54.0 | usb1k·4 |
| 1999.735 | -85.4 | 52.9 | usb1k·2 |
| 4999.338 | -87.3 | 53.0 | usb1k·5 |
| 7998.941 | -88.7 | 51.9 | usb1k·8 |
| 2999.603 | -91.2 | 48.3 | usb1k·3 |
| 15997.881 | -91.3 | 49.8 | usb1k·16 |
| 11998.411 | -91.8 | 49.5 | usb1k·12 |
| 18997.484 | -92.9 | 48.4 | usb1k·19 |
| 8998.808 | -92.9 | 47.5 | usb1k·9 |
| 10998.543 | -93.9 | 46.9 | usb1k·11 |
| 22996.954 | -95.9 | 47.0 | usb1k·23 |
| 16997.749 | -95.7 | 45.6 | usb1k·17 |
| 9998.676 | -96.7 | 44.2 | usb1k·10 |
| 50.005 | -95.8 | 32.6 | mains50·1 |
| 12998.279 | -99.0 | 42.1 | usb1k·13 |
| 19997.351 | -98.9 | 42.8 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.1 | 59.8 | usb1k·1 |
| 6000.000 | -77.2 | 59.0 | fs8·1 |
| 12000.000 | -79.8 | 56.8 | fs8·2 |
| 18000.000 | -80.8 | 56.1 | fs8·3 |
| 1999.735 | -81.1 | 52.4 | usb1k·2 |
| 3999.470 | -84.2 | 50.4 | usb1k·4 |
| 4999.338 | -84.7 | 50.5 | usb1k·5 |
| 2999.603 | -87.7 | 47.3 | usb1k·3 |
| 7998.941 | -87.2 | 48.8 | usb1k·8 |
| 15997.881 | -90.3 | 46.4 | usb1k·16 |
| 11998.411 | -90.7 | 45.7 | usb1k·12 |
| 8998.808 | -91.2 | 45.0 | usb1k·9 |
| 18997.484 | -92.7 | 44.6 | usb1k·19 |
| 16997.749 | -94.6 | 42.3 | usb1k·17 |
| 9998.676 | -95.5 | 41.1 | usb1k·10 |
| 22996.954 | -95.3 | 43.4 | usb1k·23 |
| 5999.206 | -96.0 | 40.2 | usb1k·6 |
| 10998.544 | -94.9 | 42.0 | usb1k·11 |
| 12998.279 | -96.5 | 40.6 | usb1k·13 |
| 50.005 | -95.8 | 28.6 | mains50·1 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.16 | 0.08 | 0.04 |
| led | Kanal 1 | 11/11 | 6.09 | -3.50 | 1.04 |
| mains50 | Kanal 1 | 11/11 | 222.80 | 111.28 | 1.05 |
| other1 | Kanal 1 | 11/11 | 1412.36 | 2439.50 | 3.01 |
| other2 | Kanal 1 | 11/11 | 0.37 | -0.68 | 0.26 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.14 | 0.09 | 0.04 |
| led | Kanal 2 | 11/11 | 0.44 | 0.27 | 0.45 |
| mains50 | Kanal 2 | 11/11 | 132.56 | 189.05 | 0.99 |
| other1 | Kanal 2 | 11/11 | 0.12 | -0.04 | 0.16 |
| other2 | Kanal 2 | 11/11 | 0.38 | -0.47 | 0.28 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.11 | 0.05 | 0.05 |
| led | Kanal 3 | 11/11 | 1.07 | 0.19 | 0.56 |
| mains50 | Kanal 3 | 11/11 | 193.49 | -175.29 | 0.50 |
| other1 | Kanal 3 | 11/11 | 0.07 | -0.02 | 0.18 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.17 | 0.05 | 0.05 |
| led | Kanal 4 | 11/11 | 0.72 | 0.89 | 0.60 |
| mains50 | Kanal 4 | 11/11 | 83.20 | -34.64 | 0.97 |
| other1 | Kanal 4 | 11/11 | 0.44 | -0.49 | 0.30 |
| other2 | Kanal 4 | 11/11 | 0.15 | -0.10 | 0.23 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.35 | 0.16 s (6.39 Hz) | 29.1 |
| Kanal 1 | 999.9 Hz ± 10 | 0.79 | 7.54 s (0.13 Hz) | 25.9 |
| Kanal 2 | breitbandig | 1.18 | 0.16 s (6.39 Hz) | 30.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.78 | 1.26 s (0.80 Hz) | 28.0 |
| Kanal 3 | breitbandig | 0.80 | 0.31 s (3.19 Hz) | 29.0 |
| Kanal 3 | 999.9 Hz ± 10 | 0.76 | 7.54 s (0.13 Hz) | 33.6 |
| Kanal 4 | breitbandig | 0.94 | 0.16 s (6.39 Hz) | 31.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.77 | 0.31 s (3.20 Hz) | 30.6 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.95 |
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.98 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.98 | 0.93 | 1.00 |

## Vergleich mit Referenz B3-fx1d-k-r2

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -70.9 | -71.8 | +0.8 | 70 % | 62 % |
| Kanal 2 | -71.6 | -72.7 | +1.0 | 76 % | 68 % |
| Kanal 3 | -73.0 | -74.2 | +1.3 | 85 % | 79 % |
| Kanal 4 | -70.9 | -71.8 | +0.8 | 76 % | 70 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx2c-r2_psd.png)

### Kammprofile

![Kammprofile](B3-fx2c-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx2c-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 18:05–18:08, Host-Software vor jedem Lauf neu gestartet.
