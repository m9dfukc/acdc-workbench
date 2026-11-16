# Report B3-fx2d-r2: B3-fx2d-r2 – acdc1 Build 3d, rohe Eingänge offen, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d (Build 2 + Patch 07d: LED-Code in .late_text, Adressen wie Build 2) |
| test | A/B gegen Kontrolle D31 2/2: Eingänge offen, rohe ADC-Daten (vor dem Patch) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx2d-open-inputs-r2_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 63.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx2d-r2 --ref B3-fx1d-k-r2 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -70.7 | -78.1 | -71.6 | -72.6 | -85.9 | -72.0 | – | -71.6 | 65 % | -76.2 | 4.6 |
| Kanal 2 | -6.9 | -71.7 | -79.1 | -72.5 | -73.6 | -88.0 | -72.9 | – | -72.5 | 71 % | -77.8 | 5.3 |
| Kanal 3 | -5.2 | -73.5 | -83.8 | -73.9 | -75.0 | -92.1 | -74.2 | – | -73.9 | 82 % | -81.3 | 7.4 |
| Kanal 4 | -6.0 | -70.9 | -79.2 | -71.7 | -72.5 | -88.3 | -72.0 | – | -71.7 | 72 % | -77.2 | 5.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.8 dB | -79.0 | 18.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.3 | 42.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0018 | 10/10 | k=2: 4641.090 Hz, -116.4 dB | -112.3 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9829 | 0.0047 | 3/19 | k=1: 49.985 Hz, -96.1 dB | -98.3 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0015 | 154 | k=8·f1+1·f2: 13998.941 Hz, -95.8 dB | -85.5 | 4.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.8 dB | -78.9 | 23.0 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.9 dB | -76.3 | 42.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0006 | 10/10 | k=9: 20884.904 Hz, -115.5 dB | -110.1 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9838 | 0.0039 | 4/19 | k=1: 49.984 Hz, -96.7 dB | -98.8 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0012 | 159 | k=8·f1+1·f2: 13998.941 Hz, -95.6 dB | -85.4 | 5.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.1 dB | -79.1 | 29.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -76.1 dB | -77.4 | 44.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.545 Hz, -117.5 dB | -113.2 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9834 | 0.0031 | 5/19 | k=1: 49.984 Hz, -97.4 dB | -99.6 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0015 | 166 | k=8·f1+1·f2: 13998.941 Hz, -95.8 dB | -85.6 | 6.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.1 dB | -79.2 | 17.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.6 | 50.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0008 | 10/10 | k=1: 2320.544 Hz, -116.0 dB | -111.2 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9838 | 0.0014 | 3/19 | k=1: 49.984 Hz, -97.4 dB | -99.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0015 | 153 | k=8·f1+1·f2: 13998.941 Hz, -95.6 dB | -85.5 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 57.7 | usb1k·1 |
| 6000.000 | -78.8 | 55.7 | fs8·1 |
| 18000.000 | -82.2 | 54.6 | fs8·3 |
| 1999.735 | -82.3 | 50.7 | usb1k·2 |
| 12000.000 | -82.3 | 54.1 | fs8·2 |
| 2999.603 | -82.4 | 51.2 | usb1k·3 |
| 6999.073 | -87.7 | 46.8 | usb1k·7 |
| 15997.882 | -91.8 | 45.3 | usb1k·16 |
| 9998.676 | -92.1 | 43.9 | usb1k·10 |
| 5999.206 | -94.4 | 40.0 | usb1k·6 |
| 10998.544 | -94.6 | 42.3 | usb1k·11 |
| 4999.338 | -95.4 | 38.5 | usb1k·5 |
| 14998.015 | -95.5 | 41.1 | usb1k·15 |
| 13998.941 | -95.8 | 41.0 | imd·8·f1+1·f2 |
| 9999.471 | -96.1 | 39.8 | imd·4·f1+1·f2 |
| 15999.471 | -96.3 | 40.8 | imd·4·f1+2·f2 |
| 49.985 | -96.1 | 26.8 | mains50·1 |
| 12999.073 | -96.9 | 39.5 | imd·7·f1+1·f2 |
| 19998.941 | -96.9 | 40.2 | imd·8·f1+2·f2 |
| 7998.941 | -97.0 | 38.1 | usb1k·8 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.9 | 58.2 | usb1k·1 |
| 6000.000 | -78.8 | 57.5 | fs8·1 |
| 18000.000 | -82.0 | 56.5 | fs8·3 |
| 12000.000 | -82.1 | 56.0 | fs8·2 |
| 2999.603 | -83.1 | 52.1 | usb1k·3 |
| 1999.735 | -83.3 | 51.4 | usb1k·2 |
| 6999.073 | -88.0 | 48.4 | usb1k·7 |
| 15997.882 | -92.2 | 46.6 | usb1k·16 |
| 9998.676 | -92.5 | 45.2 | usb1k·10 |
| 10998.544 | -94.8 | 43.4 | usb1k·11 |
| 14998.015 | -95.2 | 43.2 | usb1k·15 |
| 13998.941 | -95.6 | 43.0 | imd·8·f1+1·f2 |
| 5999.206 | -95.6 | 40.7 | usb1k·6 |
| 15999.471 | -96.0 | 42.8 | imd·4·f1+2·f2 |
| 9999.471 | -96.1 | 41.6 | imd·4·f1+1·f2 |
| 19998.941 | -96.8 | 41.6 | imd·8·f1+2·f2 |
| 12999.073 | -96.9 | 41.0 | imd·7·f1+1·f2 |
| 7998.941 | -97.0 | 39.7 | usb1k·8 |
| 12999.868 | -97.0 | 40.8 | imd·1·f1+2·f2 |
| 49.984 | -96.7 | 28.6 | mains50·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -76.1 | 61.4 | usb1k·1 |
| 6000.000 | -79.1 | 60.9 | fs8·1 |
| 12000.000 | -82.1 | 58.9 | fs8·2 |
| 18000.000 | -82.3 | 59.2 | fs8·3 |
| 2999.603 | -84.0 | 55.0 | usb1k·3 |
| 1999.735 | -84.7 | 54.3 | usb1k·2 |
| 6999.073 | -88.5 | 51.2 | usb1k·7 |
| 15997.882 | -92.8 | 48.9 | usb1k·16 |
| 9998.676 | -93.0 | 48.0 | usb1k·10 |
| 10998.544 | -95.2 | 46.0 | usb1k·11 |
| 14998.014 | -95.5 | 46.1 | usb1k·15 |
| 13998.941 | -95.8 | 45.6 | imd·8·f1+1·f2 |
| 15999.471 | -96.3 | 45.4 | imd·4·f1+2·f2 |
| 9999.470 | -96.3 | 44.5 | imd·4·f1+1·f2 |
| 5999.206 | -96.8 | 43.2 | usb1k·6 |
| 19998.941 | -97.0 | 44.6 | imd·8·f1+2·f2 |
| 12999.073 | -97.1 | 44.6 | imd·7·f1+1·f2 |
| 7998.941 | -97.1 | 42.9 | usb1k·8 |
| 12999.868 | -97.3 | 44.3 | imd·1·f1+2·f2 |
| 16998.544 | -97.4 | 43.5 | imd·11·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 59.5 | usb1k·1 |
| 6000.000 | -79.1 | 56.8 | fs8·1 |
| 1999.735 | -80.7 | 53.5 | usb1k·2 |
| 18000.000 | -82.1 | 55.2 | fs8·3 |
| 2999.603 | -82.2 | 52.5 | usb1k·3 |
| 12000.000 | -82.3 | 54.8 | fs8·2 |
| 6999.073 | -87.3 | 48.5 | usb1k·7 |
| 15997.882 | -91.1 | 46.3 | usb1k·16 |
| 9998.676 | -92.0 | 44.7 | usb1k·10 |
| 4999.338 | -92.7 | 42.2 | usb1k·5 |
| 5999.206 | -93.2 | 42.7 | usb1k·6 |
| 10998.544 | -94.1 | 43.0 | usb1k·11 |
| 13998.941 | -95.6 | 41.5 | imd·8·f1+1·f2 |
| 14998.014 | -95.7 | 41.9 | usb1k·15 |
| 15999.470 | -96.1 | 41.3 | imd·4·f1+2·f2 |
| 9999.471 | -96.3 | 40.4 | imd·4·f1+1·f2 |
| 11998.411 | -96.9 | 40.1 | usb1k·12 |
| 19998.941 | -97.1 | 40.5 | imd·8·f1+2·f2 |
| 12999.073 | -97.2 | 39.9 | imd·7·f1+1·f2 |
| 12999.868 | -97.2 | 39.8 | imd·1·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | -0.01 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.12 | -0.05 | 0.02 |
| led | Kanal 1 | 11/11 | 8.08 | -5.74 | 1.36 |
| mains50 | Kanal 1 | 11/11 | 616.61 | -367.00 | 1.09 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.08 | 0.01 | 0.01 |
| led | Kanal 2 | 11/11 | 0.64 | 0.28 | 0.64 |
| mains50 | Kanal 2 | 11/11 | 445.80 | -402.26 | 0.82 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.08 | -0.00 | 0.02 |
| led | Kanal 3 | 11/11 | 1.04 | -1.02 | 0.64 |
| mains50 | Kanal 3 | 11/11 | 409.83 | 1091.84 | 0.61 |
| fs8 | Kanal 4 | 11/11 | 0.01 | -0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.06 | 0.05 | 0.02 |
| led | Kanal 4 | 11/11 | 1.41 | 1.59 | 0.83 |
| mains50 | Kanal 4 | 11/11 | 217.70 | 453.54 | 0.85 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.89 | 0.16 s (6.39 Hz) | 22.4 |
| Kanal 1 | 999.9 Hz ± 10 | 0.70 | 1.26 s (0.79 Hz) | 32.0 |
| Kanal 2 | breitbandig | 0.79 | 0.16 s (6.39 Hz) | 25.5 |
| Kanal 2 | 999.9 Hz ± 10 | 0.70 | 1.26 s (0.79 Hz) | 34.0 |
| Kanal 3 | breitbandig | 0.53 | 1.26 s (0.79 Hz) | 26.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.68 | 1.26 s (0.79 Hz) | 37.3 |
| Kanal 4 | breitbandig | 0.66 | 0.16 s (6.39 Hz) | 26.0 |
| Kanal 4 | 999.9 Hz ± 10 | 0.68 | 1.26 s (0.79 Hz) | 34.3 |

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
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.94 | 0.95 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.97 | 0.93 | 1.00 |

## Vergleich mit Referenz B3-fx1d-k-r2

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.6 | -71.8 | +0.2 | 65 % | 62 % |
| Kanal 2 | -72.5 | -72.7 | +0.2 | 71 % | 68 % |
| Kanal 3 | -73.9 | -74.2 | +0.3 | 82 % | 79 % |
| Kanal 4 | -71.7 | -71.8 | +0.1 | 72 % | 70 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx2d-r2_psd.png)

### Kammprofile

![Kammprofile](B3-fx2d-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx2d-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 18:27–18:30, Host-Software vor jedem Lauf neu gestartet.
