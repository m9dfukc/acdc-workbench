# Report B3-fx2b-r1: B3-fx2b-r1 – acdc1 Build 3b, rohe Eingänge offen, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 3b v22.4.r-fx2b (Build 2 + Patch 07 v2, Eingangs-LEDs roh bei TX) |
| test | A/B gegen B3 1/2: Eingänge offen, rohe ADC-Daten (vor dem Patch), wie B3-fx1d-r1 (D26) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx2b-open-inputs-r1_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx2b-r1 --ref B3-fx1d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -70.5 | -79.3 | -71.1 | -72.2 | -85.6 | -71.4 | -98.9 | -71.1 | 69 % | -76.3 | 5.1 |
| Kanal 2 | -6.9 | -71.4 | -80.4 | -71.9 | -73.0 | -87.7 | -72.2 | -100.9 | -71.9 | 75 % | -78.0 | 6.1 |
| Kanal 3 | -5.1 | -73.0 | -85.8 | -73.2 | -74.3 | -91.5 | -73.4 | -101.3 | -73.2 | 86 % | -81.6 | 8.4 |
| Kanal 4 | -6.0 | -70.8 | -80.7 | -71.2 | -72.2 | -88.0 | -71.5 | -100.2 | -71.2 | 76 % | -77.4 | 6.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.8 dB | -77.6 | 22.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0006 | 23/23 | k=1: 999.867 Hz, -72.8 dB | -74.6 | 45.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0021 | 9/10 | k=1: 2320.544 Hz, -117.5 dB | -114.1 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0006 | 0.0150 | 4/19 | k=1: 49.997 Hz, -93.3 dB | -95.8 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0011 | 120 | k=8·f1+2·f2: 19998.940 Hz, -99.7 dB | -89.6 | 1.4 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 1 | 21000.0001 | 0.0000 | 1/1 | k=1: 21000.000 Hz, -100.3 dB | -103.3 | 0.1 % |
| stärkste übrige Linie (51.13 Hz) | Kanal 1 | 51.1364 | 0.0075 | 6/467 | k=1: 51.128 Hz, -100.8 dB | -100.9 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.8 dB | -77.6 | 27.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.7 dB | -75.3 | 45.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0014 | 10/10 | k=8: 18564.357 Hz, -115.3 dB | -110.5 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0005 | 0.0145 | 4/19 | k=1: 49.997 Hz, -93.9 dB | -96.4 | 0.4 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0010 | 133 | k=8·f1+2·f2: 19998.940 Hz, -99.7 dB | -89.5 | 1.8 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 2 | 21000.0002 | 0.0000 | 1/1 | k=1: 21000.000 Hz, -100.1 dB | -103.1 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 2 | 23000.9275 | 0.0000 | 1/1 | k=1: 23000.928 Hz, -102.0 dB | -105.0 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -77.8 | 34.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0003 | 23/23 | k=1: 999.867 Hz, -74.8 dB | -76.4 | 48.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0016 | 10/10 | k=1: 2320.544 Hz, -117.8 dB | -114.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9996 | 0.0095 | 5/19 | k=1: 49.997 Hz, -94.7 dB | -97.2 | 0.4 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0010 | 148 | k=8·f1+2·f2: 19998.940 Hz, -99.7 dB | -89.7 | 2.3 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 3 | 21000.0000 | 0.0000 | 1/1 | k=1: 21000.000 Hz, -100.4 dB | -103.4 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9275 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -102.5 dB | -105.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -77.8 | 22.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0004 | 23/23 | k=1: 999.867 Hz, -72.4 dB | -74.1 | 51.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0014 | 10/10 | k=1: 2320.544 Hz, -116.8 dB | -112.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0005 | 0.0149 | 4/19 | k=1: 49.997 Hz, -94.6 dB | -97.1 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0012 | 129 | k=15·f1+1·f2: 20998.013 Hz, -100.0 dB | -89.6 | 1.5 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 4 | 21000.0003 | 0.0000 | 1/1 | k=1: 21000.000 Hz, -100.2 dB | -103.2 | 0.1 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1898 | 0.0015 | 9/19 | k=1: 1215.189 Hz, -102.1 dB | -103.2 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.8 | 58.0 | usb1k·1 |
| 6000.000 | -77.8 | 57.8 | fs8·1 |
| 12000.000 | -80.3 | 56.4 | fs8·2 |
| 18000.000 | -80.8 | 55.3 | fs8·3 |
| 1999.735 | -83.3 | 49.0 | usb1k·2 |
| 3999.470 | -83.9 | 50.2 | usb1k·4 |
| 4999.338 | -85.8 | 48.7 | usb1k·5 |
| 7998.940 | -87.5 | 47.6 | usb1k·8 |
| 2999.603 | -89.1 | 44.6 | usb1k·3 |
| 15997.880 | -90.4 | 45.9 | usb1k·16 |
| 11998.411 | -91.0 | 45.6 | usb1k·12 |
| 8998.808 | -92.1 | 43.4 | usb1k·9 |
| 18997.483 | -92.3 | 41.6 | usb1k·19 |
| 49.997 | -93.3 | 30.2 | mains50·1 |
| 22996.953 | -94.2 | 43.7 | usb1k·23 |
| 10998.543 | -94.0 | 41.8 | usb1k·11 |
| 16997.748 | -95.0 | 40.9 | usb1k·17 |
| 9998.675 | -96.3 | 39.8 | usb1k·10 |
| 12998.278 | -98.2 | 38.1 | usb1k·13 |
| 19997.350 | -97.8 | 38.7 | usb1k·20 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.7 | 59.1 | usb1k·1 |
| 6000.000 | -77.8 | 59.4 | fs8·1 |
| 12000.000 | -80.1 | 58.2 | fs8·2 |
| 18000.000 | -80.7 | 57.3 | fs8·3 |
| 3999.470 | -84.2 | 51.5 | usb1k·4 |
| 1999.735 | -84.2 | 49.8 | usb1k·2 |
| 4999.338 | -86.3 | 49.8 | usb1k·5 |
| 7998.940 | -88.0 | 48.8 | usb1k·8 |
| 2999.602 | -90.5 | 44.9 | usb1k·3 |
| 15997.880 | -90.4 | 47.7 | usb1k·16 |
| 11998.411 | -91.1 | 47.1 | usb1k·12 |
| 18997.483 | -92.2 | 44.0 | usb1k·19 |
| 8998.808 | -92.1 | 44.9 | usb1k·9 |
| 49.997 | -93.9 | 31.2 | mains50·1 |
| 22996.953 | -94.1 | 45.3 | usb1k·23 |
| 10998.543 | -93.5 | 44.2 | usb1k·11 |
| 16997.748 | -95.4 | 42.2 | usb1k·17 |
| 9998.675 | -96.6 | 40.8 | usb1k·10 |
| 12998.278 | -98.5 | 39.6 | usb1k·13 |
| 19997.350 | -97.9 | 40.2 | usb1k·20 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.8 | 62.2 | usb1k·1 |
| 6000.000 | -78.0 | 62.8 | fs8·1 |
| 12000.000 | -80.3 | 61.2 | fs8·2 |
| 18000.000 | -80.9 | 59.5 | fs8·3 |
| 3999.470 | -84.8 | 54.9 | usb1k·4 |
| 1999.735 | -86.1 | 52.3 | usb1k·2 |
| 4999.338 | -87.4 | 52.7 | usb1k·5 |
| 7998.940 | -88.4 | 51.6 | usb1k·8 |
| 15997.880 | -91.0 | 49.8 | usb1k·16 |
| 2999.603 | -91.8 | 47.7 | usb1k·3 |
| 11998.411 | -91.6 | 49.8 | usb1k·12 |
| 18997.483 | -92.4 | 46.6 | usb1k·19 |
| 8998.808 | -93.0 | 47.1 | usb1k·9 |
| 49.997 | -94.7 | 35.4 | mains50·1 |
| 10998.543 | -93.4 | 47.4 | usb1k·11 |
| 22996.953 | -94.6 | 47.4 | usb1k·23 |
| 16997.748 | -95.9 | 44.7 | usb1k·17 |
| 9998.675 | -96.9 | 43.6 | usb1k·10 |
| 19997.350 | -98.2 | 42.6 | usb1k·20 |
| 12998.278 | -99.1 | 41.4 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.4 | 60.4 | usb1k·1 |
| 6000.000 | -78.2 | 58.4 | fs8·1 |
| 12000.000 | -80.2 | 57.2 | fs8·2 |
| 18000.000 | -80.8 | 55.9 | fs8·3 |
| 1999.735 | -81.3 | 52.6 | usb1k·2 |
| 3999.470 | -84.0 | 51.2 | usb1k·4 |
| 4999.338 | -84.7 | 50.7 | usb1k·5 |
| 7998.940 | -87.4 | 48.7 | usb1k·8 |
| 2999.603 | -88.7 | 46.0 | usb1k·3 |
| 15997.880 | -89.8 | 47.1 | usb1k·16 |
| 11998.411 | -90.5 | 46.8 | usb1k·12 |
| 8998.808 | -90.9 | 45.0 | usb1k·9 |
| 18997.483 | -92.2 | 43.0 | usb1k·19 |
| 22996.953 | -93.8 | 44.2 | usb1k·23 |
| 49.997 | -94.6 | 31.0 | mains50·1 |
| 10998.543 | -94.1 | 42.4 | usb1k·11 |
| 16997.748 | -95.0 | 41.9 | usb1k·17 |
| 9998.675 | -96.2 | 40.2 | usb1k·10 |
| 12998.278 | -96.8 | 40.3 | usb1k·13 |
| 5999.205 | -97.4 | 39.2 | usb1k·6 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.02 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.13 | 0.02 | 0.05 |
| led | Kanal 1 | 11/11 | 2.56 | 0.27 | 0.99 |
| mains50 | Kanal 1 | 11/11 | 222.40 | 397.39 | 0.61 |
| other1 | Kanal 1 | 11/11 | 0.11 | 0.08 | 0.18 |
| other2 | Kanal 1 | 11/11 | 0.66 | -0.47 | 1.68 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.12 | 0.00 | 0.04 |
| led | Kanal 2 | 11/11 | 0.41 | 0.07 | 0.51 |
| mains50 | Kanal 2 | 11/11 | 224.35 | 327.66 | 0.53 |
| other1 | Kanal 2 | 11/11 | 0.12 | 0.12 | 0.16 |
| other2 | Kanal 2 | 11/11 | 0.18 | -0.03 | 0.26 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.08 | 0.00 | 0.03 |
| led | Kanal 3 | 11/11 | 1.09 | -1.53 | 0.58 |
| mains50 | Kanal 3 | 11/11 | 34.25 | -28.92 | 0.35 |
| other1 | Kanal 3 | 11/11 | 0.11 | 0.08 | 0.17 |
| other2 | Kanal 3 | 11/11 | 0.18 | 0.02 | 0.17 |
| fs8 | Kanal 4 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.12 | 0.04 | 0.05 |
| led | Kanal 4 | 11/11 | 1.33 | -1.27 | 1.03 |
| mains50 | Kanal 4 | 11/11 | 227.31 | 333.44 | 0.48 |
| other1 | Kanal 4 | 11/11 | 0.14 | 0.04 | 0.19 |
| other2 | Kanal 4 | 11/11 | 0.49 | -0.43 | 0.40 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.71 | 0.16 s (6.40 Hz) | 23.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.82 | 7.54 s (0.13 Hz) | 28.9 |
| Kanal 2 | breitbandig | 0.66 | 0.16 s (6.40 Hz) | 24.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.80 | 7.54 s (0.13 Hz) | 30.8 |
| Kanal 3 | breitbandig | 0.39 | 0.63 s (1.59 Hz) | 28.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.78 | 7.54 s (0.13 Hz) | 33.8 |
| Kanal 4 | breitbandig | 0.56 | 0.16 s (6.40 Hz) | 24.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.79 | 1.26 s (0.80 Hz) | 30.7 |

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
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.98 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.94 |
| Kanal 4 | 0.96 | 0.98 | 0.94 | 1.00 |

## Vergleich mit Referenz B3-fx1d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.9 | +0.7 | 69 % | 63 % |
| Kanal 2 | -71.9 | -72.7 | +0.7 | 75 % | 70 % |
| Kanal 3 | -73.2 | -74.3 | +1.0 | 86 % | 80 % |
| Kanal 4 | -71.2 | -71.8 | +0.6 | 76 % | 70 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx2b-r1_psd.png)

### Kammprofile

![Kammprofile](B3-fx2b-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx2b-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 17:42–17:43, Host-Software frisch gestartet.
