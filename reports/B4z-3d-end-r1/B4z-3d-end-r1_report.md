# Report B4z-3d-end-r1: B4z-3d-end-r1 – acdc1 3d-end-open-inputs-4z, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4z-Sitzung: Endkontrolle 3d nach fx3k, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-4z-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4z-3d-end-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4z-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.9 | -69.8 | -75.8 | -71.0 | -72.0 | -85.6 | -71.4 | – | -71.0 | 67 % | -75.9 | 4.8 |
| Kanal 2 | -7.2 | -70.7 | -77.2 | -71.8 | -72.9 | -87.7 | -72.2 | – | -71.8 | 73 % | -77.4 | 5.6 |
| Kanal 3 | -5.4 | -72.3 | -80.2 | -73.1 | -74.1 | -92.0 | -73.4 | – | -73.1 | 82 % | -80.5 | 7.5 |
| Kanal 4 | -6.2 | -70.2 | -78.5 | -70.9 | -71.8 | -88.0 | -71.2 | – | -70.9 | 74 % | -76.8 | 5.8 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.3 | 18.8 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.6 | 44.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0016 | 10/10 | k=1: 2320.543 Hz, -117.5 dB | -112.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9811 | 0.0000 | 1/19 | k=1: 49.981 Hz, -98.6 dB | -101.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0011 | 146 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.2 | 23.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.0 dB | -75.4 | 44.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0014 | 10/10 | k=9: 20884.905 Hz, -114.2 dB | -110.2 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9815 | 0.0000 | 1/19 | k=1: 49.982 Hz, -99.0 dB | -102.0 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0009 | 155 | k=8·f1+1·f2: 13998.941 Hz, -94.5 dB | -84.6 | 5.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.4 dB | -78.4 | 29.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.1 dB | -76.4 | 46.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.543 Hz, -116.8 dB | -112.7 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9813 | 0.0004 | 2/19 | k=1: 49.982 Hz, -99.8 dB | -102.5 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0010 | 162 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.9 | 6.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.4 | 18.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.8 | 51.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0015 | 10/10 | k=1: 2320.542 Hz, -115.7 dB | -111.8 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9814 | 0.0000 | 1/19 | k=1: 49.981 Hz, -99.6 dB | -102.5 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0011 | 153 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 56.6 | usb1k·1 |
| 6000.000 | -78.0 | 56.5 | fs8·1 |
| 1999.735 | -81.1 | 50.8 | usb1k·2 |
| 18000.000 | -81.5 | 54.7 | fs8·3 |
| 12000.000 | -81.6 | 54.2 | fs8·2 |
| 2999.603 | -81.5 | 51.4 | usb1k·3 |
| 6999.074 | -86.7 | 47.8 | usb1k·7 |
| 15997.882 | -91.1 | 45.1 | usb1k·16 |
| 9998.676 | -91.3 | 43.9 | usb1k·10 |
| 5999.206 | -93.1 | 41.4 | usb1k·6 |
| 10998.543 | -93.7 | 42.4 | usb1k·11 |
| 4999.338 | -94.4 | 39.8 | usb1k·5 |
| 14998.014 | -95.0 | 40.7 | usb1k·15 |
| 15999.471 | -95.4 | 40.8 | imd·4·f1+2·f2 |
| 9999.471 | -95.7 | 39.5 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 41.2 | imd·8·f1+1·f2 |
| 12999.868 | -96.5 | 39.2 | imd·1·f1+2·f2 |
| 20997.220 | -97.0 | 39.8 | usb1k·21 |
| 12999.074 | -96.2 | 39.5 | imd·7·f1+1·f2 |
| 19998.941 | -95.8 | 40.4 | imd·8·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.0 | 57.4 | usb1k·1 |
| 6000.000 | -78.0 | 58.1 | fs8·1 |
| 12000.000 | -81.3 | 56.1 | fs8·2 |
| 18000.000 | -81.4 | 56.6 | fs8·3 |
| 1999.735 | -82.1 | 51.5 | usb1k·2 |
| 2999.603 | -82.0 | 52.6 | usb1k·3 |
| 6999.074 | -86.9 | 49.3 | usb1k·7 |
| 15997.882 | -91.5 | 45.8 | usb1k·16 |
| 9998.676 | -91.6 | 45.1 | usb1k·10 |
| 10998.543 | -93.7 | 43.9 | usb1k·11 |
| 14998.014 | -94.6 | 42.9 | usb1k·15 |
| 5999.206 | -94.1 | 42.0 | usb1k·6 |
| 15999.471 | -95.3 | 42.2 | imd·4·f1+2·f2 |
| 9999.471 | -95.5 | 41.2 | imd·4·f1+1·f2 |
| 13998.941 | -94.5 | 43.2 | imd·8·f1+1·f2 |
| 12999.868 | -96.4 | 40.9 | imd·1·f1+2·f2 |
| 12999.074 | -96.0 | 41.3 | imd·7·f1+1·f2 |
| 19998.941 | -95.7 | 42.3 | imd·8·f1+2·f2 |
| 14999.603 | -97.0 | 40.6 | imd·3·f1+2·f2 |
| 8999.603 | -97.1 | 39.9 | imd·3·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.1 | 60.9 | usb1k·1 |
| 6000.000 | -78.4 | 61.0 | fs8·1 |
| 12000.000 | -81.4 | 58.4 | fs8·2 |
| 18000.000 | -81.6 | 58.2 | fs8·3 |
| 2999.603 | -82.9 | 55.8 | usb1k·3 |
| 1999.735 | -83.6 | 53.8 | usb1k·2 |
| 6999.074 | -87.5 | 51.8 | usb1k·7 |
| 15997.882 | -92.1 | 48.1 | usb1k·16 |
| 9998.676 | -92.0 | 47.6 | usb1k·10 |
| 14998.014 | -94.9 | 45.0 | usb1k·15 |
| 10998.543 | -94.3 | 46.0 | usb1k·11 |
| 15999.471 | -95.5 | 44.7 | imd·4·f1+2·f2 |
| 9999.471 | -95.7 | 43.8 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 45.3 | imd·8·f1+1·f2 |
| 5999.206 | -95.4 | 44.0 | usb1k·6 |
| 12999.868 | -96.8 | 43.4 | imd·1·f1+2·f2 |
| 12999.074 | -96.2 | 44.0 | imd·7·f1+1·f2 |
| 19998.941 | -96.0 | 44.0 | imd·8·f1+2·f2 |
| 8999.603 | -97.3 | 42.2 | imd·3·f1+1·f2 |
| 14999.603 | -97.3 | 42.8 | imd·3·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 59.0 | usb1k·1 |
| 6000.000 | -78.2 | 57.3 | fs8·1 |
| 1999.735 | -79.7 | 53.7 | usb1k·2 |
| 2999.603 | -81.1 | 53.1 | usb1k·3 |
| 12000.000 | -81.5 | 54.6 | fs8·2 |
| 18000.000 | -81.6 | 55.2 | fs8·3 |
| 6999.074 | -86.4 | 49.0 | usb1k·7 |
| 15997.882 | -90.5 | 46.0 | usb1k·16 |
| 9998.676 | -91.0 | 44.9 | usb1k·10 |
| 4999.338 | -91.9 | 43.0 | usb1k·5 |
| 5999.206 | -91.7 | 43.8 | usb1k·6 |
| 10998.544 | -93.3 | 43.1 | usb1k·11 |
| 14998.014 | -94.9 | 41.4 | usb1k·15 |
| 15999.471 | -95.4 | 41.2 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 40.3 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 42.1 | imd·8·f1+1·f2 |
| 12999.868 | -96.4 | 39.6 | imd·1·f1+2·f2 |
| 20997.220 | -96.3 | 40.6 | usb1k·21 |
| 13998.147 | -96.7 | 40.2 | usb1k·14 |
| 11998.411 | -96.2 | 39.7 | usb1k·12 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.14 | -0.03 | 0.03 |
| led | Kanal 1 | 11/11 | 2.14 | -1.24 | 0.85 |
| mains50 | Kanal 1 | 11/11 | 286.78 | -278.36 | 1.01 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.11 | -0.09 | 0.05 |
| led | Kanal 2 | 11/11 | 0.34 | 0.84 | 0.59 |
| mains50 | Kanal 2 | 11/11 | 232.33 | -236.32 | 0.82 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.09 | -0.02 | 0.01 |
| led | Kanal 3 | 11/11 | 1.11 | -1.42 | 0.49 |
| mains50 | Kanal 3 | 11/11 | 770.97 | -27.33 | 0.52 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.10 | -0.09 | 0.05 |
| led | Kanal 4 | 11/11 | 1.48 | 1.50 | 0.90 |
| mains50 | Kanal 4 | 11/11 | 235.64 | -165.54 | 0.79 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.22 | 0.31 s (3.18 Hz) | 26.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 28.2 |
| Kanal 2 | breitbandig | 1.07 | 0.31 s (3.18 Hz) | 26.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 30.0 |
| Kanal 3 | breitbandig | 0.84 | 0.31 s (3.18 Hz) | 28.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 33.3 |
| Kanal 4 | breitbandig | 0.76 | 0.16 s (6.40 Hz) | 25.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 30.2 |

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
| Kanal 1 | 1.00 | 0.97 | 0.94 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.96 |
| Kanal 3 | 0.94 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4z-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.0 | -71.2 | +0.2 | 67 % | 67 % |
| Kanal 2 | -71.8 | -71.7 | -0.1 | 73 % | 73 % |
| Kanal 3 | -73.1 | -72.9 | -0.2 | 82 % | 83 % |
| Kanal 4 | -70.9 | -71.0 | +0.1 | 74 % | 73 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4z-3d-end-r1_psd.png)

### Kammprofile

![Kammprofile](B4z-3d-end-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4z-3d-end-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 19:17:39. Stream-Meldungen: 0. owl_read: reports/owl_read/B4z-3d-end-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
