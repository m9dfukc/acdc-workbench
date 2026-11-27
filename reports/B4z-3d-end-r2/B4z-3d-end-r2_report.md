# Report B4z-3d-end-r2: B4z-3d-end-r2 – acdc1 3d-end-open-inputs-4z, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4z-Sitzung: Endkontrolle 3d nach fx3k, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-4z-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4z-3d-end-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.9 | -70.3 | -78.7 | -71.0 | -72.1 | -85.6 | -71.4 | – | -71.0 | 67 % | -75.8 | 4.8 |
| Kanal 2 | -7.2 | -71.1 | -79.5 | -71.8 | -72.9 | -87.7 | -72.2 | – | -71.8 | 72 % | -77.4 | 5.6 |
| Kanal 3 | -5.4 | -72.8 | -85.3 | -73.1 | -74.1 | -92.1 | -73.3 | – | -73.1 | 82 % | -80.5 | 7.4 |
| Kanal 4 | -6.2 | -70.4 | -79.7 | -71.0 | -71.8 | -88.0 | -71.3 | – | -71.0 | 74 % | -76.8 | 5.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -78.3 | 18.7 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -74.6 | 44.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0018 | 10/10 | k=2: 4641.089 Hz, -116.8 dB | -112.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9801 | 0.0010 | 2/19 | k=1: 49.979 Hz, -97.4 dB | -100.1 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0011 | 147 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -78.2 | 23.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.4 | 43.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0016 | 10/10 | k=9: 20884.902 Hz, -115.3 dB | -110.2 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9801 | 0.0010 | 2/19 | k=1: 49.979 Hz, -98.3 dB | -100.9 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0011 | 154 | k=8·f1+1·f2: 13998.941 Hz, -94.5 dB | -84.7 | 5.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.4 dB | -78.4 | 28.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.4 | 46.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0012 | 10/10 | k=1: 2320.545 Hz, -117.1 dB | -112.9 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9796 | 0.0006 | 3/19 | k=1: 49.980 Hz, -99.2 dB | -101.9 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0010 | 161 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.9 | 6.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.3 dB | -78.4 | 18.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.5 dB | -73.8 | 51.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0018 | 10/10 | k=2: 4641.089 Hz, -115.6 dB | -111.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9800 | 0.0007 | 2/19 | k=1: 49.979 Hz, -99.2 dB | -101.7 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0011 | 151 | k=8·f1+1·f2: 13998.941 Hz, -94.6 dB | -84.8 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 56.8 | usb1k·1 |
| 6000.000 | -78.1 | 55.9 | fs8·1 |
| 1999.735 | -81.0 | 50.8 | usb1k·2 |
| 18000.000 | -81.4 | 55.0 | fs8·3 |
| 12000.000 | -81.6 | 54.3 | fs8·2 |
| 2999.603 | -81.5 | 51.9 | usb1k·3 |
| 6999.073 | -86.8 | 47.7 | usb1k·7 |
| 15997.882 | -91.1 | 45.0 | usb1k·16 |
| 9998.676 | -91.2 | 44.2 | usb1k·10 |
| 5999.206 | -93.1 | 41.0 | usb1k·6 |
| 10998.544 | -93.7 | 41.9 | usb1k·11 |
| 4999.338 | -94.1 | 39.7 | usb1k·5 |
| 14998.014 | -95.0 | 40.9 | usb1k·15 |
| 15999.471 | -95.4 | 40.8 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 39.8 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 41.1 | imd·8·f1+1·f2 |
| 12999.868 | -96.6 | 39.6 | imd·1·f1+2·f2 |
| 12999.074 | -96.1 | 40.1 | imd·7·f1+1·f2 |
| 18997.485 | -97.2 | 39.2 | usb1k·19 |
| 20997.220 | -97.0 | 39.2 | usb1k·21 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 57.6 | usb1k·1 |
| 6000.000 | -78.1 | 57.6 | fs8·1 |
| 18000.000 | -81.3 | 56.6 | fs8·3 |
| 12000.000 | -81.3 | 56.0 | fs8·2 |
| 2999.603 | -82.1 | 52.9 | usb1k·3 |
| 1999.735 | -82.2 | 51.1 | usb1k·2 |
| 6999.074 | -87.0 | 49.2 | usb1k·7 |
| 15997.882 | -91.5 | 46.3 | usb1k·16 |
| 9998.676 | -91.4 | 45.8 | usb1k·10 |
| 10998.544 | -93.8 | 43.1 | usb1k·11 |
| 14998.014 | -94.6 | 42.9 | usb1k·15 |
| 5999.206 | -94.0 | 41.6 | usb1k·6 |
| 15999.471 | -95.2 | 42.5 | imd·4·f1+2·f2 |
| 9999.471 | -95.4 | 41.8 | imd·4·f1+1·f2 |
| 13998.941 | -94.5 | 42.6 | imd·8·f1+1·f2 |
| 12999.868 | -96.4 | 40.9 | imd·1·f1+2·f2 |
| 12999.074 | -95.9 | 41.4 | imd·7·f1+1·f2 |
| 19998.941 | -95.7 | 41.8 | imd·8·f1+2·f2 |
| 7998.941 | -95.9 | 40.4 | usb1k·8 |
| 14999.603 | -97.0 | 40.5 | imd·3·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 61.1 | usb1k·1 |
| 6000.000 | -78.4 | 60.6 | fs8·1 |
| 12000.000 | -81.4 | 58.6 | fs8·2 |
| 18000.000 | -81.5 | 58.6 | fs8·3 |
| 2999.603 | -82.9 | 55.8 | usb1k·3 |
| 1999.735 | -83.5 | 54.1 | usb1k·2 |
| 6999.074 | -87.5 | 51.9 | usb1k·7 |
| 15997.882 | -92.0 | 48.2 | usb1k·16 |
| 9998.676 | -91.9 | 48.0 | usb1k·10 |
| 14998.014 | -95.0 | 45.0 | usb1k·15 |
| 10998.544 | -94.3 | 45.3 | usb1k·11 |
| 15999.471 | -95.5 | 44.7 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 44.3 | imd·4·f1+1·f2 |
| 5999.206 | -95.4 | 43.7 | usb1k·6 |
| 13998.941 | -94.7 | 45.2 | imd·8·f1+1·f2 |
| 12999.868 | -96.8 | 43.5 | imd·1·f1+2·f2 |
| 12999.073 | -96.2 | 44.0 | imd·7·f1+1·f2 |
| 19998.941 | -96.1 | 43.8 | imd·8·f1+2·f2 |
| 8999.603 | -97.3 | 42.7 | imd·3·f1+1·f2 |
| 14999.603 | -97.4 | 42.7 | imd·3·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.5 | 58.8 | usb1k·1 |
| 6000.000 | -78.3 | 56.8 | fs8·1 |
| 1999.735 | -79.8 | 53.0 | usb1k·2 |
| 2999.603 | -81.1 | 53.4 | usb1k·3 |
| 12000.000 | -81.5 | 55.0 | fs8·2 |
| 18000.000 | -81.5 | 55.2 | fs8·3 |
| 6999.074 | -86.5 | 48.8 | usb1k·7 |
| 15997.882 | -90.5 | 45.8 | usb1k·16 |
| 9998.676 | -90.8 | 45.4 | usb1k·10 |
| 4999.338 | -91.8 | 43.0 | usb1k·5 |
| 5999.206 | -91.5 | 43.5 | usb1k·6 |
| 10998.544 | -93.3 | 42.4 | usb1k·11 |
| 14998.014 | -94.8 | 41.2 | usb1k·15 |
| 15999.471 | -95.5 | 40.9 | imd·4·f1+2·f2 |
| 9999.471 | -95.5 | 40.7 | imd·4·f1+1·f2 |
| 13998.941 | -94.6 | 41.9 | imd·8·f1+1·f2 |
| 12999.868 | -96.5 | 39.8 | imd·1·f1+2·f2 |
| 20997.220 | -96.4 | 40.2 | usb1k·21 |
| 11998.411 | -96.0 | 40.4 | usb1k·12 |
| 13998.147 | -96.7 | 39.8 | usb1k·14 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.13 | -0.08 | 0.03 |
| led | Kanal 1 | 11/11 | 2.52 | -3.33 | 0.65 |
| mains50 | Kanal 1 | 11/11 | 881.23 | 1224.12 | 0.99 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.14 | -0.04 | 0.03 |
| led | Kanal 2 | 11/11 | 0.61 | -0.53 | 0.54 |
| mains50 | Kanal 2 | 11/11 | 526.39 | -622.28 | 0.98 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.11 | -0.07 | 0.02 |
| led | Kanal 3 | 11/11 | 2.12 | -0.32 | 0.40 |
| mains50 | Kanal 3 | 11/11 | 415.27 | 221.92 | 0.58 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.14 | -0.06 | 0.02 |
| led | Kanal 4 | 11/11 | 2.27 | -2.34 | 0.55 |
| mains50 | Kanal 4 | 11/11 | 971.91 | 451.96 | 0.99 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.76 | 0.16 s (6.40 Hz) | 25.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 1.25 s (0.80 Hz) | 30.3 |
| Kanal 2 | breitbandig | 0.74 | 0.16 s (6.40 Hz) | 27.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 32.4 |
| Kanal 3 | breitbandig | 0.38 | 1.25 s (0.80 Hz) | 26.5 |
| Kanal 3 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 35.9 |
| Kanal 4 | breitbandig | 0.61 | 0.16 s (6.40 Hz) | 27.7 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 31.6 |

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

## Vergleich mit Referenz B4z-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.0 | -71.2 | +0.2 | 67 % | 67 % |
| Kanal 2 | -71.8 | -71.7 | -0.1 | 72 % | 73 % |
| Kanal 3 | -73.1 | -72.9 | -0.2 | 82 % | 83 % |
| Kanal 4 | -71.0 | -71.0 | +0.0 | 74 % | 73 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4z-3d-end-r2_psd.png)

### Kammprofile

![Kammprofile](B4z-3d-end-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4z-3d-end-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 19:18:52. Stream-Meldungen: 0. owl_read: reports/owl_read/B4z-3d-end-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
