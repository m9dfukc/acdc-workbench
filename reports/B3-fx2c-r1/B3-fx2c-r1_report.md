# Report B3-fx2c-r1: B3-fx2c-r1 – acdc1 Build 3c, rohe Eingänge offen, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 3c v22.4.r-fx2c (Build 2 + Patch 07c, Eingangs-LEDs roh bei TX, Messung in onLoop) |
| test | A/B gegen Kontrolle D31 1/2: Eingänge offen, rohe ADC-Daten (vor dem Patch) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx2c-open-inputs-r1_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx2c-r1 --ref B3-fx1d-k-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -69.5 | -74.7 | -71.0 | -72.1 | -85.6 | -71.4 | -98.5 | -71.0 | 70 % | -76.2 | 5.2 |
| Kanal 2 | -6.9 | -70.4 | -76.3 | -71.7 | -72.8 | -87.5 | -72.0 | -101.1 | -71.7 | 75 % | -77.8 | 6.1 |
| Kanal 3 | -5.1 | -72.1 | -79.1 | -73.1 | -74.2 | -91.7 | -73.3 | -105.0 | -73.1 | 85 % | -81.3 | 8.2 |
| Kanal 4 | -6.0 | -70.1 | -77.0 | -71.0 | -72.0 | -87.7 | -71.3 | -101.1 | -71.0 | 75 % | -77.1 | 6.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -76.9 dB | -77.1 | 24.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0004 | 23/23 | k=1: 999.867 Hz, -72.8 dB | -74.7 | 43.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5446 | 0.0018 | 10/10 | k=2: 4641.086 Hz, -117.3 dB | -113.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0059 | 0.0003 | 2/19 | k=1: 50.006 Hz, -94.7 dB | -97.2 | 0.2 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0015 | 128 | k=8·f1+2·f2: 19998.940 Hz, -100.2 dB | -89.9 | 1.3 % |
| stärkste übrige Linie (51.14 Hz) | Kanal 1 | 51.1364 | 0.0016 | 5/466 | k=1: 51.139 Hz, -101.8 dB | -100.6 | 0.1 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 1 | 1215.1899 | 0.0015 | 9/19 | k=1: 1215.190 Hz, -102.1 dB | -102.8 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.0 dB | -77.0 | 29.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0005 | 23/23 | k=1: 999.867 Hz, -73.6 dB | -75.3 | 44.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5447 | 0.0011 | 10/10 | k=9: 20884.902 Hz, -114.8 dB | -110.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0061 | 0.0000 | 2/19 | k=1: 50.006 Hz, -95.4 dB | -97.8 | 0.2 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0014 | 140 | k=15·f1+1·f2: 20998.013 Hz, -100.1 dB | -89.8 | 1.6 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 2 | 23000.9280 | 0.0000 | 1/1 | k=1: 23000.928 Hz, -101.7 dB | -104.7 | 0.0 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 2 | 1215.1899 | 0.0017 | 9/19 | k=1: 1215.190 Hz, -102.8 dB | -103.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.2 dB | -77.2 | 38.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0005 | 23/23 | k=1: 999.867 Hz, -75.0 dB | -76.6 | 44.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0008 | 10/10 | k=2: 4641.088 Hz, -118.5 dB | -113.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0014 | 0.0145 | 5/19 | k=1: 50.006 Hz, -96.2 dB | -98.5 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0013 | 154 | k=8·f1+2·f2: 19998.940 Hz, -100.4 dB | -90.0 | 2.0 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9279 | 0.0000 | 1/1 | k=1: 23000.928 Hz, -102.0 dB | -105.0 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.3 | 23.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0004 | 23/23 | k=1: 999.867 Hz, -72.4 dB | -74.1 | 50.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0014 | 10/10 | k=1: 2320.544 Hz, -116.8 dB | -111.9 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0063 | 0.0001 | 2/19 | k=1: 50.006 Hz, -95.8 dB | -98.2 | 0.2 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0011 | 131 | k=15·f1+1·f2: 20998.013 Hz, -100.0 dB | -89.9 | 1.3 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 4 | 23000.9280 | 0.0000 | 1/1 | k=1: 23000.928 Hz, -101.8 dB | -104.9 | 0.0 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1899 | 0.0017 | 8/19 | k=1: 1215.190 Hz, -102.5 dB | -103.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.8 | 57.9 | usb1k·1 |
| 6000.000 | -76.9 | 57.6 | fs8·1 |
| 12000.000 | -79.9 | 56.8 | fs8·2 |
| 18000.000 | -80.6 | 56.6 | fs8·3 |
| 1999.735 | -83.3 | 48.1 | usb1k·2 |
| 3999.470 | -84.3 | 49.1 | usb1k·4 |
| 4999.338 | -86.0 | 48.2 | usb1k·5 |
| 2999.602 | -88.3 | 44.9 | usb1k·3 |
| 7998.940 | -87.8 | 47.6 | usb1k·8 |
| 15997.880 | -90.8 | 46.3 | usb1k·16 |
| 11998.410 | -91.2 | 45.6 | usb1k·12 |
| 8998.808 | -92.3 | 43.5 | usb1k·9 |
| 18997.483 | -92.8 | 44.1 | usb1k·19 |
| 50.006 | -94.7 | 24.9 | mains50·1 |
| 16997.748 | -94.9 | 41.7 | usb1k·17 |
| 22996.953 | -95.5 | 43.5 | usb1k·23 |
| 9998.675 | -95.9 | 40.4 | usb1k·10 |
| 10998.543 | -94.5 | 41.7 | usb1k·11 |
| 12998.277 | -98.0 | 38.4 | usb1k·13 |
| 5999.205 | -98.8 | 35.9 | usb1k·6 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.6 | 58.8 | usb1k·1 |
| 6000.000 | -77.0 | 59.4 | fs8·1 |
| 12000.000 | -79.7 | 58.7 | fs8·2 |
| 18000.000 | -80.5 | 58.1 | fs8·3 |
| 1999.735 | -83.8 | 49.3 | usb1k·2 |
| 3999.470 | -84.5 | 50.9 | usb1k·4 |
| 4999.338 | -86.3 | 49.5 | usb1k·5 |
| 2999.602 | -89.4 | 45.9 | usb1k·3 |
| 7998.940 | -88.2 | 49.1 | usb1k·8 |
| 15997.880 | -90.8 | 47.6 | usb1k·16 |
| 11998.410 | -91.3 | 47.2 | usb1k·12 |
| 8998.808 | -92.2 | 45.0 | usb1k·9 |
| 18997.483 | -92.7 | 45.8 | usb1k·19 |
| 50.006 | -95.4 | 26.5 | mains50·1 |
| 10998.543 | -94.0 | 44.1 | usb1k·11 |
| 22996.952 | -95.5 | 45.1 | usb1k·23 |
| 16997.748 | -95.3 | 42.9 | usb1k·17 |
| 9998.675 | -96.3 | 41.7 | usb1k·10 |
| 12998.278 | -98.1 | 39.9 | usb1k·13 |
| 19997.350 | -98.6 | 39.8 | usb1k·20 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.0 | 62.2 | usb1k·1 |
| 6000.000 | -77.2 | 62.6 | fs8·1 |
| 12000.000 | -79.8 | 61.4 | fs8·2 |
| 18000.000 | -80.8 | 61.1 | fs8·3 |
| 3999.470 | -85.3 | 54.0 | usb1k·4 |
| 1999.735 | -85.9 | 51.6 | usb1k·2 |
| 4999.338 | -87.7 | 52.1 | usb1k·5 |
| 7998.940 | -88.7 | 52.0 | usb1k·8 |
| 2999.602 | -91.3 | 47.5 | usb1k·3 |
| 15997.880 | -91.4 | 50.3 | usb1k·16 |
| 11998.410 | -91.8 | 49.4 | usb1k·12 |
| 18997.483 | -92.9 | 48.6 | usb1k·19 |
| 8998.808 | -93.1 | 47.9 | usb1k·9 |
| 10998.543 | -93.8 | 47.5 | usb1k·11 |
| 50.006 | -96.2 | 30.5 | mains50·1 |
| 22996.953 | -96.0 | 47.1 | usb1k·23 |
| 16997.748 | -95.9 | 45.3 | usb1k·17 |
| 9998.675 | -96.8 | 44.5 | usb1k·10 |
| 12998.278 | -98.8 | 42.3 | usb1k·13 |
| 19997.350 | -98.8 | 42.3 | usb1k·20 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -72.4 | 59.6 | usb1k·1 |
| 6000.000 | -77.3 | 59.0 | fs8·1 |
| 12000.000 | -79.8 | 57.2 | fs8·2 |
| 18000.000 | -80.7 | 56.2 | fs8·3 |
| 1999.735 | -81.2 | 51.5 | usb1k·2 |
| 3999.470 | -84.3 | 50.5 | usb1k·4 |
| 4999.338 | -84.8 | 50.0 | usb1k·5 |
| 2999.603 | -87.8 | 46.7 | usb1k·3 |
| 7998.940 | -87.5 | 48.8 | usb1k·8 |
| 15997.880 | -90.1 | 47.2 | usb1k·16 |
| 11998.410 | -90.7 | 46.3 | usb1k·12 |
| 8998.808 | -91.1 | 45.1 | usb1k·9 |
| 18997.483 | -92.7 | 44.6 | usb1k·19 |
| 22996.952 | -95.0 | 43.5 | usb1k·23 |
| 9998.675 | -95.7 | 41.0 | usb1k·10 |
| 50.006 | -95.8 | 26.5 | mains50·1 |
| 16997.747 | -94.9 | 42.3 | usb1k·17 |
| 10998.543 | -94.7 | 42.6 | usb1k·11 |
| 12998.278 | -96.6 | 40.3 | usb1k·13 |
| 5999.205 | -96.8 | 39.5 | usb1k·6 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.17 | 0.14 | 0.03 |
| led | Kanal 1 | 11/11 | 1.99 | 0.54 | 1.01 |
| mains50 | Kanal 1 | 11/11 | 244.81 | -454.99 | 0.93 |
| other1 | Kanal 1 | 11/11 | 1.22 | -0.70 | 2.14 |
| other2 | Kanal 1 | 11/11 | 0.55 | 0.33 | 0.32 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.13 | 0.15 | 0.01 |
| led | Kanal 2 | 11/11 | 0.50 | -0.12 | 0.49 |
| mains50 | Kanal 2 | 11/11 | 221.37 | -453.68 | 0.77 |
| other1 | Kanal 2 | 11/11 | 0.11 | -0.15 | 0.23 |
| other2 | Kanal 2 | 11/11 | 0.54 | 0.27 | 0.29 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.09 | 0.18 | 0.03 |
| led | Kanal 3 | 11/11 | 1.06 | 0.86 | 0.49 |
| mains50 | Kanal 3 | 11/11 | 33.06 | 4.39 | 0.51 |
| other1 | Kanal 3 | 11/11 | 0.07 | -0.13 | 0.19 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.14 | 0.18 | 0.03 |
| led | Kanal 4 | 11/11 | 1.77 | 0.65 | 0.50 |
| mains50 | Kanal 4 | 11/11 | 213.99 | -432.24 | 0.83 |
| other1 | Kanal 4 | 11/11 | 0.15 | -0.12 | 0.28 |
| other2 | Kanal 4 | 11/11 | 0.64 | -0.02 | 0.31 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.44 | 0.31 s (3.19 Hz) | 29.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.87 | 1.26 s (0.80 Hz) | 26.7 |
| Kanal 2 | breitbandig | 1.21 | 0.16 s (6.39 Hz) | 29.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.86 | 1.26 s (0.80 Hz) | 28.9 |
| Kanal 3 | breitbandig | 0.98 | 0.31 s (3.19 Hz) | 30.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.85 | 7.53 s (0.13 Hz) | 33.3 |
| Kanal 4 | breitbandig | 0.93 | 0.16 s (6.39 Hz) | 30.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.85 | 1.26 s (0.80 Hz) | 29.0 |

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
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.98 | 0.92 | 1.00 |

## Vergleich mit Referenz B3-fx1d-k-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.0 | -71.8 | +0.8 | 70 % | 62 % |
| Kanal 2 | -71.7 | -72.7 | +1.0 | 75 % | 68 % |
| Kanal 3 | -73.1 | -74.3 | +1.2 | 85 % | 79 % |
| Kanal 4 | -71.0 | -71.9 | +0.9 | 75 % | 69 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx2c-r1_psd.png)

### Kammprofile

![Kammprofile](B3-fx2c-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx2c-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 18:05–18:08, Host-Software vor jedem Lauf neu gestartet.
