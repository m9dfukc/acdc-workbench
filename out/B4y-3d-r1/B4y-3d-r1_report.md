# Report B4y-3d-r1: B4y-3d-r1 – acdc1 3d-open-inputs-4y, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4y-Sitzung: Startkontrolle 3d vor fx3j/fx3jp, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-open-inputs-4y-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-3d-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -69.8 | -75.6 | -71.1 | -72.2 | -86.7 | -71.5 | – | -71.1 | 68 % | -76.0 | 4.9 |
| Kanal 2 | -7.2 | -70.5 | -76.1 | -71.9 | -72.9 | -88.5 | -72.2 | – | -71.9 | 73 % | -77.5 | 5.7 |
| Kanal 3 | -5.4 | -72.3 | -79.7 | -73.1 | -74.2 | -92.7 | -73.4 | – | -73.1 | 82 % | -80.6 | 7.5 |
| Kanal 4 | -6.2 | -69.8 | -76.3 | -71.0 | -71.8 | -89.0 | -71.3 | – | -71.0 | 74 % | -76.9 | 5.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.3 | 19.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.7 | 44.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.543 Hz, -117.0 dB | -112.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9837 | 0.0009 | 2/19 | k=1: 49.983 Hz, -96.6 dB | -99.4 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0014 | 147 | k=8·f1+1·f2: 13998.941 Hz, -94.6 dB | -84.7 | 4.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -78.2 | 23.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.4 | 44.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0010 | 10/10 | k=8: 18564.358 Hz, -114.3 dB | -109.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9836 | 0.0008 | 2/19 | k=1: 49.983 Hz, -97.3 dB | -100.0 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0014 | 152 | k=8·f1+1·f2: 13998.941 Hz, -94.4 dB | -84.6 | 5.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.4 | 29.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.5 | 46.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0007 | 10/10 | k=1: 2320.544 Hz, -116.6 dB | -112.3 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9833 | 0.0004 | 2/19 | k=1: 49.983 Hz, -97.9 dB | -100.5 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0013 | 163 | k=8·f1+1·f2: 13998.941 Hz, -94.6 dB | -84.8 | 6.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.3 dB | -78.4 | 18.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.4 dB | -73.8 | 51.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0017 | 10/10 | k=1: 2320.543 Hz, -116.0 dB | -111.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9838 | 0.0010 | 2/19 | k=1: 49.983 Hz, -98.0 dB | -100.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0013 | 150 | k=8·f1+1·f2: 13998.941 Hz, -94.6 dB | -84.7 | 4.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 55.6 | usb1k·1 |
| 6000.000 | -78.2 | 56.5 | fs8·1 |
| 1999.735 | -81.2 | 51.4 | usb1k·2 |
| 18000.000 | -81.3 | 54.8 | fs8·3 |
| 12000.000 | -81.6 | 54.0 | fs8·2 |
| 2999.603 | -81.5 | 51.7 | usb1k·3 |
| 6999.074 | -86.8 | 48.2 | usb1k·7 |
| 15997.882 | -91.1 | 44.9 | usb1k·16 |
| 9998.676 | -91.2 | 43.9 | usb1k·10 |
| 5999.206 | -93.5 | 41.2 | usb1k·6 |
| 10998.544 | -93.9 | 41.9 | usb1k·11 |
| 14998.014 | -94.9 | 41.5 | usb1k·15 |
| 4999.338 | -94.6 | 38.8 | usb1k·5 |
| 15999.471 | -95.2 | 40.8 | imd·4·f1+2·f2 |
| 9999.471 | -95.7 | 39.5 | imd·4·f1+1·f2 |
| 13998.941 | -94.6 | 41.1 | imd·8·f1+1·f2 |
| 12999.868 | -96.3 | 39.5 | imd·1·f1+2·f2 |
| 49.983 | -96.6 | 25.6 | mains50·1 |
| 19998.941 | -95.5 | 39.5 | imd·8·f1+2·f2 |
| 12999.074 | -96.0 | 39.9 | imd·7·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 56.3 | usb1k·1 |
| 6000.000 | -78.1 | 58.0 | fs8·1 |
| 18000.000 | -81.2 | 56.7 | fs8·3 |
| 12000.000 | -81.4 | 56.0 | fs8·2 |
| 2999.603 | -81.9 | 52.8 | usb1k·3 |
| 1999.735 | -82.2 | 51.9 | usb1k·2 |
| 6999.074 | -87.0 | 49.4 | usb1k·7 |
| 15997.882 | -91.5 | 46.0 | usb1k·16 |
| 9998.676 | -91.5 | 45.1 | usb1k·10 |
| 14998.014 | -94.6 | 42.9 | usb1k·15 |
| 10998.544 | -94.0 | 43.5 | usb1k·11 |
| 5999.206 | -94.5 | 41.6 | usb1k·6 |
| 15999.471 | -95.1 | 42.4 | imd·4·f1+2·f2 |
| 9999.471 | -95.5 | 41.1 | imd·4·f1+1·f2 |
| 13998.941 | -94.4 | 42.9 | imd·8·f1+1·f2 |
| 12999.868 | -96.2 | 41.2 | imd·1·f1+2·f2 |
| 19998.941 | -95.4 | 40.8 | imd·8·f1+2·f2 |
| 12999.074 | -95.9 | 41.5 | imd·7·f1+1·f2 |
| 14999.603 | -96.9 | 40.6 | imd·3·f1+2·f2 |
| 16998.544 | -96.3 | 40.8 | imd·11·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 59.7 | usb1k·1 |
| 6000.000 | -78.5 | 61.1 | fs8·1 |
| 12000.000 | -81.4 | 58.5 | fs8·2 |
| 18000.000 | -81.4 | 58.4 | fs8·3 |
| 2999.603 | -82.8 | 55.9 | usb1k·3 |
| 1999.735 | -83.7 | 54.5 | usb1k·2 |
| 6999.074 | -87.5 | 52.3 | usb1k·7 |
| 15997.882 | -92.1 | 47.6 | usb1k·16 |
| 9998.676 | -91.9 | 47.6 | usb1k·10 |
| 14998.014 | -94.8 | 45.3 | usb1k·15 |
| 10998.544 | -94.5 | 45.2 | usb1k·11 |
| 15999.471 | -95.3 | 44.4 | imd·4·f1+2·f2 |
| 9999.471 | -95.7 | 43.8 | imd·4·f1+1·f2 |
| 13998.941 | -94.6 | 44.9 | imd·8·f1+1·f2 |
| 12999.868 | -96.6 | 43.2 | imd·1·f1+2·f2 |
| 5999.206 | -95.8 | 43.8 | usb1k·6 |
| 19998.941 | -95.7 | 43.4 | imd·8·f1+2·f2 |
| 12999.074 | -96.1 | 43.7 | imd·7·f1+1·f2 |
| 14999.603 | -97.1 | 42.9 | imd·3·f1+2·f2 |
| 16998.544 | -96.5 | 43.2 | imd·11·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.4 | 58.1 | usb1k·1 |
| 6000.000 | -78.3 | 57.2 | fs8·1 |
| 1999.735 | -79.7 | 54.2 | usb1k·2 |
| 2999.603 | -81.1 | 53.1 | usb1k·3 |
| 18000.000 | -81.4 | 55.3 | fs8·3 |
| 12000.000 | -81.5 | 54.7 | fs8·2 |
| 6999.074 | -86.6 | 49.3 | usb1k·7 |
| 15997.882 | -90.5 | 45.8 | usb1k·16 |
| 9998.676 | -90.9 | 44.5 | usb1k·10 |
| 4999.338 | -91.8 | 41.4 | usb1k·5 |
| 5999.206 | -91.9 | 43.6 | usb1k·6 |
| 10998.544 | -93.5 | 42.7 | usb1k·11 |
| 14998.014 | -94.7 | 41.9 | usb1k·15 |
| 15999.471 | -95.3 | 41.1 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 39.9 | imd·4·f1+1·f2 |
| 13998.941 | -94.6 | 42.0 | imd·8·f1+1·f2 |
| 12999.868 | -96.3 | 40.3 | imd·1·f1+2·f2 |
| 20997.220 | -96.1 | 40.1 | usb1k·21 |
| 11998.412 | -96.0 | 40.2 | usb1k·12 |
| 19998.941 | -95.5 | 39.2 | imd·8·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.02 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.09 | 0.13 | 0.02 |
| led | Kanal 1 | 11/11 | 3.76 | -6.05 | 0.79 |
| mains50 | Kanal 1 | 11/11 | 1426.57 | 2103.13 | 0.93 |
| fs8 | Kanal 2 | 11/11 | 0.02 | -0.02 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.07 | 0.06 | 0.02 |
| led | Kanal 2 | 11/11 | 0.51 | -0.02 | 0.59 |
| mains50 | Kanal 2 | 11/11 | 921.78 | 1098.08 | 0.76 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.03 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.07 | 0.11 | 0.01 |
| led | Kanal 3 | 11/11 | 0.91 | -0.54 | 0.61 |
| mains50 | Kanal 3 | 11/11 | 157.59 | 151.94 | 0.40 |
| fs8 | Kanal 4 | 11/11 | 0.03 | -0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.09 | 0.08 | 0.02 |
| led | Kanal 4 | 11/11 | 0.86 | 1.81 | 0.53 |
| mains50 | Kanal 4 | 11/11 | 916.34 | 1066.19 | 0.87 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.13 | 0.16 s (6.40 Hz) | 29.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 1.25 s (0.80 Hz) | 29.3 |
| Kanal 2 | breitbandig | 1.17 | 0.16 s (6.40 Hz) | 31.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 30.9 |
| Kanal 3 | breitbandig | 0.89 | 0.31 s (3.22 Hz) | 34.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 34.9 |
| Kanal 4 | breitbandig | 0.98 | 0.16 s (6.40 Hz) | 31.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 31.0 |

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
| Kanal 2 | 0.97 | 1.00 | 0.93 | 0.97 |
| Kanal 3 | 0.93 | 0.93 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz B4-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.7 | +0.5 | 68 % | 64 % |
| Kanal 2 | -71.9 | -72.6 | +0.7 | 73 % | 69 % |
| Kanal 3 | -73.1 | -73.8 | +0.7 | 82 % | 80 % |
| Kanal 4 | -71.0 | -71.6 | +0.7 | 74 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-3d-r1_psd.png)

### Kammprofile

![Kammprofile](B4y-3d-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-3d-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:11:23. Stream-Meldungen: 0. owl_read: out/owl_read/B4y-3d-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
