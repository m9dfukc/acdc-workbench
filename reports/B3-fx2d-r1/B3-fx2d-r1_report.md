# Report B3-fx2d-r1: B3-fx2d-r1 – acdc1 Build 3d, rohe Eingänge offen, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d (Build 2 + Patch 07d: LED-Code in .late_text, Adressen wie Build 2) |
| test | A/B gegen Kontrolle D31 1/2: Eingänge offen, rohe ADC-Daten (vor dem Patch) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx2d-open-inputs-r1_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx2d-r1 --ref B3-fx1d-k-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -70.2 | -75.6 | -71.7 | -72.8 | -85.6 | -72.1 | – | -71.7 | 64 % | -76.1 | 4.4 |
| Kanal 2 | -6.9 | -71.2 | -76.9 | -72.6 | -73.7 | -87.6 | -73.0 | – | -72.6 | 69 % | -77.7 | 5.1 |
| Kanal 3 | -5.2 | -73.1 | -80.2 | -74.0 | -75.2 | -91.8 | -74.3 | – | -74.0 | 81 % | -81.2 | 7.2 |
| Kanal 4 | -6.0 | -70.8 | -77.8 | -71.7 | -72.7 | -87.9 | -72.1 | – | -71.7 | 71 % | -77.1 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.8 dB | -79.0 | 18.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.9 dB | -75.6 | 40.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0022 | 10/10 | k=1: 2320.546 Hz, -117.1 dB | -113.0 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9930 | 0.0014 | 2/19 | k=1: 49.994 Hz, -96.0 dB | -98.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0017 | 147 | k=8·f1+1·f2: 13998.941 Hz, -95.3 dB | -85.5 | 4.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.8 dB | -78.9 | 23.4 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.867 Hz, -75.0 dB | -76.5 | 40.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0010 | 10/10 | k=9: 20884.904 Hz, -114.9 dB | -110.4 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9932 | 0.0011 | 2/19 | k=1: 49.994 Hz, -96.5 dB | -98.9 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0017 | 155 | k=8·f1+1·f2: 13998.941 Hz, -95.2 dB | -85.4 | 5.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.2 | 30.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.867 Hz, -76.2 dB | -77.7 | 43.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.545 Hz, -118.3 dB | -113.4 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9927 | 0.0055 | 5/19 | k=1: 49.994 Hz, -97.3 dB | -99.6 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0009 | 162 | k=8·f1+1·f2: 13998.941 Hz, -95.4 dB | -85.6 | 6.9 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.1 dB | -79.1 | 18.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.3 dB | -74.9 | 48.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0010 | 10/10 | k=1: 2320.546 Hz, -116.4 dB | -111.7 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9931 | 0.0008 | 3/19 | k=1: 49.994 Hz, -97.4 dB | -99.7 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0023 | 153 | k=8·f1+1·f2: 13998.941 Hz, -95.3 dB | -85.5 | 4.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.9 | 56.2 | usb1k·1 |
| 6000.000 | -78.8 | 55.1 | fs8·1 |
| 18000.000 | -82.2 | 54.2 | fs8·3 |
| 12000.000 | -82.3 | 53.9 | fs8·2 |
| 2999.603 | -82.7 | 50.0 | usb1k·3 |
| 1999.735 | -82.4 | 49.3 | usb1k·2 |
| 6999.073 | -87.4 | 47.3 | usb1k·7 |
| 15997.882 | -91.7 | 44.2 | usb1k·16 |
| 9998.676 | -92.1 | 43.3 | usb1k·10 |
| 5999.206 | -94.4 | 39.5 | usb1k·6 |
| 10998.543 | -94.2 | 41.7 | usb1k·11 |
| 14998.014 | -95.3 | 40.6 | usb1k·15 |
| 49.994 | -96.0 | 22.8 | mains50·1 |
| 4999.338 | -95.1 | 39.0 | usb1k·5 |
| 15999.470 | -96.0 | 40.1 | imd·4·f1+2·f2 |
| 9999.470 | -96.2 | 39.1 | imd·4·f1+1·f2 |
| 13998.941 | -95.3 | 41.1 | imd·8·f1+1·f2 |
| 12999.073 | -96.9 | 39.3 | imd·7·f1+1·f2 |
| 14999.603 | -97.5 | 38.7 | imd·3·f1+2·f2 |
| 11998.411 | -97.1 | 39.1 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.0 | 57.2 | usb1k·1 |
| 6000.000 | -78.8 | 57.0 | fs8·1 |
| 12000.000 | -82.0 | 55.8 | fs8·2 |
| 18000.000 | -82.1 | 55.7 | fs8·3 |
| 2999.603 | -83.4 | 51.1 | usb1k·3 |
| 1999.735 | -83.4 | 50.2 | usb1k·2 |
| 6999.073 | -87.8 | 48.8 | usb1k·7 |
| 15997.882 | -92.2 | 45.4 | usb1k·16 |
| 9998.676 | -92.5 | 44.6 | usb1k·10 |
| 5999.206 | -95.3 | 40.5 | usb1k·6 |
| 10998.543 | -94.4 | 42.8 | usb1k·11 |
| 14998.014 | -95.0 | 42.6 | usb1k·15 |
| 15999.470 | -95.9 | 41.7 | imd·4·f1+2·f2 |
| 9999.470 | -96.1 | 40.9 | imd·4·f1+1·f2 |
| 49.994 | -96.5 | 24.8 | mains50·1 |
| 13998.941 | -95.2 | 42.7 | imd·8·f1+1·f2 |
| 12999.073 | -96.9 | 40.8 | imd·7·f1+1·f2 |
| 14999.603 | -97.5 | 40.3 | imd·3·f1+2·f2 |
| 11998.412 | -97.1 | 40.8 | usb1k·12 |
| 12999.868 | -97.1 | 40.7 | imd·1·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -76.2 | 60.6 | usb1k·1 |
| 6000.000 | -79.2 | 60.0 | fs8·1 |
| 12000.000 | -82.1 | 58.6 | fs8·2 |
| 18000.000 | -82.3 | 58.4 | fs8·3 |
| 2999.603 | -84.4 | 54.4 | usb1k·3 |
| 1999.735 | -84.8 | 53.0 | usb1k·2 |
| 6999.073 | -88.4 | 51.3 | usb1k·7 |
| 15997.882 | -92.9 | 47.3 | usb1k·16 |
| 9998.676 | -93.0 | 47.3 | usb1k·10 |
| 14998.014 | -95.3 | 45.6 | usb1k·15 |
| 10998.543 | -94.9 | 45.8 | usb1k·11 |
| 15999.470 | -96.1 | 44.2 | imd·4·f1+2·f2 |
| 9999.470 | -96.3 | 43.9 | imd·4·f1+1·f2 |
| 5999.206 | -96.7 | 42.5 | usb1k·6 |
| 13998.941 | -95.4 | 45.7 | imd·8·f1+1·f2 |
| 12999.073 | -97.1 | 43.5 | imd·7·f1+1·f2 |
| 49.994 | -97.3 | 28.4 | mains50·1 |
| 12999.867 | -97.2 | 43.5 | imd·1·f1+2·f2 |
| 14999.603 | -97.9 | 43.2 | imd·3·f1+2·f2 |
| 11998.411 | -97.5 | 43.3 | usb1k·12 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.3 | 58.5 | usb1k·1 |
| 6000.000 | -79.1 | 56.0 | fs8·1 |
| 1999.735 | -80.8 | 52.2 | usb1k·2 |
| 12000.000 | -82.1 | 54.6 | fs8·2 |
| 18000.000 | -82.3 | 54.3 | fs8·3 |
| 2999.603 | -82.4 | 51.9 | usb1k·3 |
| 6999.073 | -87.2 | 48.2 | usb1k·7 |
| 15997.882 | -91.2 | 45.3 | usb1k·16 |
| 9998.676 | -91.9 | 44.1 | usb1k·10 |
| 5999.206 | -92.9 | 42.2 | usb1k·6 |
| 4999.338 | -92.5 | 42.7 | usb1k·5 |
| 10998.543 | -93.9 | 42.6 | usb1k·11 |
| 14998.014 | -95.4 | 41.3 | usb1k·15 |
| 15999.470 | -96.0 | 40.5 | imd·4·f1+2·f2 |
| 9999.470 | -96.3 | 39.6 | imd·4·f1+1·f2 |
| 13998.941 | -95.3 | 41.5 | imd·8·f1+1·f2 |
| 11998.412 | -96.5 | 40.2 | usb1k·12 |
| 12999.073 | -97.1 | 40.0 | imd·7·f1+1·f2 |
| 49.994 | -97.4 | 24.3 | mains50·1 |
| 14999.603 | -97.7 | 39.1 | imd·3·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.00 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.11 | -0.07 | 0.06 |
| led | Kanal 1 | 11/11 | 2.32 | -1.90 | 0.80 |
| mains50 | Kanal 1 | 11/11 | 906.12 | -1413.67 | 0.34 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.10 | -0.06 | 0.06 |
| led | Kanal 2 | 11/11 | 0.26 | 0.58 | 0.28 |
| mains50 | Kanal 2 | 11/11 | 204.01 | -386.61 | 0.24 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.07 | -0.01 | 0.07 |
| led | Kanal 3 | 11/11 | 1.42 | -1.76 | 0.51 |
| mains50 | Kanal 3 | 11/11 | 45.38 | -60.97 | 0.18 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.07 | 0.00 | 0.08 |
| led | Kanal 4 | 11/11 | 1.20 | 0.04 | 0.53 |
| mains50 | Kanal 4 | 11/11 | 269.01 | -655.04 | 0.30 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.37 | 0.31 s (3.19 Hz) | 27.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.90 | 1.26 s (0.80 Hz) | 29.3 |
| Kanal 2 | breitbandig | 1.26 | 0.16 s (6.39 Hz) | 29.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.90 | 1.26 s (0.80 Hz) | 30.5 |
| Kanal 3 | breitbandig | 0.98 | 0.31 s (3.19 Hz) | 29.6 |
| Kanal 3 | 999.9 Hz ± 10 | 0.88 | 1.26 s (0.80 Hz) | 35.4 |
| Kanal 4 | breitbandig | 0.93 | 0.16 s (6.39 Hz) | 29.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.89 | 0.31 s (3.20 Hz) | 32.5 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.94 |
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz B3-fx1d-k-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.7 | -71.8 | +0.1 | 64 % | 62 % |
| Kanal 2 | -72.6 | -72.7 | +0.1 | 69 % | 68 % |
| Kanal 3 | -74.0 | -74.3 | +0.3 | 81 % | 79 % |
| Kanal 4 | -71.7 | -71.9 | +0.2 | 71 % | 69 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx2d-r1_psd.png)

### Kammprofile

![Kammprofile](B3-fx2d-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx2d-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 18:27–18:30, Host-Software vor jedem Lauf neu gestartet.
