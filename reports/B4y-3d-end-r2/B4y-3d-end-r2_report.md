# Report B4y-3d-end-r2: B4y-3d-end-r2 – acdc1 3d-end-open-inputs-4y, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d (zurückgeflasht) |
| test | Build-4y-Sitzung: 3d-Endkontrolle nach fx3j/noD, Eingänge offen |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-end-open-inputs-4y-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-3d-end-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.8 | -70.2 | -77.7 | -71.0 | -72.0 | -85.6 | -71.4 | – | -71.0 | 67 % | -75.9 | 4.9 |
| Kanal 2 | -7.1 | -71.0 | -79.1 | -71.7 | -72.8 | -87.5 | -72.1 | – | -71.7 | 73 % | -77.4 | 5.6 |
| Kanal 3 | -5.4 | -72.7 | -82.8 | -73.1 | -74.2 | -91.7 | -73.4 | – | -73.1 | 82 % | -80.6 | 7.4 |
| Kanal 4 | -6.2 | -70.3 | -79.7 | -70.8 | -71.7 | -87.8 | -71.1 | – | -70.8 | 74 % | -76.7 | 5.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.4 | 18.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.5 | 44.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0013 | 10/10 | k=1: 2320.543 Hz, -117.9 dB | -112.7 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9888 | 0.0011 | 2/19 | k=1: 49.990 Hz, -96.6 dB | -99.3 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0012 | 147 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -84.8 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -78.2 | 22.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.2 | 44.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0011 | 10/10 | k=9: 20884.904 Hz, -114.6 dB | -109.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9889 | 0.0006 | 2/19 | k=1: 49.989 Hz, -97.1 dB | -99.7 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0011 | 154 | k=8·f1+1·f2: 13998.941 Hz, -94.6 dB | -84.7 | 5.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.5 dB | -78.5 | 29.0 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.1 dB | -76.5 | 46.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0010 | 10/10 | k=1: 2320.544 Hz, -117.8 dB | -113.0 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9927 | 0.0055 | 3/19 | k=1: 49.989 Hz, -97.8 dB | -100.4 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0010 | 162 | k=8·f1+1·f2: 13998.941 Hz, -94.7 dB | -85.0 | 6.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.2 dB | -78.4 | 17.4 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.1 dB | -73.6 | 52.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0012 | 10/10 | k=3: 6961.633 Hz, -116.8 dB | -111.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9890 | 0.0003 | 2/19 | k=1: 49.989 Hz, -97.9 dB | -100.6 | 0.1 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0012 | 144 | k=8·f1+1·f2: 13998.941 Hz, -94.8 dB | -84.9 | 3.9 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 58.0 | usb1k·1 |
| 6000.000 | -78.2 | 55.6 | fs8·1 |
| 1999.735 | -81.2 | 51.3 | usb1k·2 |
| 18000.000 | -81.5 | 54.7 | fs8·3 |
| 12000.000 | -81.6 | 54.2 | fs8·2 |
| 2999.603 | -81.7 | 51.3 | usb1k·3 |
| 6999.073 | -86.5 | 48.4 | usb1k·7 |
| 15997.881 | -91.0 | 45.1 | usb1k·16 |
| 9998.676 | -91.3 | 43.8 | usb1k·10 |
| 5999.206 | -93.2 | 40.6 | usb1k·6 |
| 4999.339 | -93.8 | 39.9 | usb1k·5 |
| 10998.543 | -94.0 | 41.4 | usb1k·11 |
| 14998.014 | -94.9 | 41.2 | usb1k·15 |
| 9999.471 | -95.4 | 39.6 | imd·4·f1+1·f2 |
| 15999.470 | -95.5 | 40.7 | imd·4·f1+2·f2 |
| 13998.941 | -94.7 | 41.4 | imd·8·f1+1·f2 |
| 12999.868 | -96.7 | 39.3 | imd·1·f1+2·f2 |
| 7998.941 | -95.5 | 39.9 | usb1k·8 |
| 11998.411 | -96.2 | 39.5 | usb1k·12 |
| 12999.073 | -96.2 | 39.8 | imd·7·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 58.7 | usb1k·1 |
| 6000.000 | -78.1 | 57.6 | fs8·1 |
| 12000.000 | -81.4 | 55.8 | fs8·2 |
| 18000.000 | -81.4 | 56.3 | fs8·3 |
| 1999.735 | -82.2 | 52.0 | usb1k·2 |
| 2999.603 | -82.2 | 52.3 | usb1k·3 |
| 6999.073 | -86.8 | 49.5 | usb1k·7 |
| 15997.881 | -91.4 | 46.5 | usb1k·16 |
| 9998.676 | -91.4 | 45.3 | usb1k·10 |
| 14998.014 | -94.6 | 42.9 | usb1k·15 |
| 5999.206 | -94.0 | 41.7 | usb1k·6 |
| 10998.543 | -94.1 | 43.0 | usb1k·11 |
| 9999.471 | -95.2 | 41.4 | imd·4·f1+1·f2 |
| 15999.470 | -95.3 | 42.5 | imd·4·f1+2·f2 |
| 13998.941 | -94.6 | 42.6 | imd·8·f1+1·f2 |
| 12999.868 | -96.5 | 41.0 | imd·1·f1+2·f2 |
| 4999.339 | -96.0 | 39.1 | usb1k·5 |
| 7998.941 | -95.5 | 41.3 | usb1k·8 |
| 12999.073 | -96.0 | 41.5 | imd·7·f1+1·f2 |
| 11998.411 | -96.3 | 40.9 | usb1k·12 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.1 | 61.8 | usb1k·1 |
| 6000.000 | -78.5 | 60.7 | fs8·1 |
| 12000.000 | -81.4 | 58.6 | fs8·2 |
| 18000.000 | -81.6 | 58.5 | fs8·3 |
| 2999.603 | -83.1 | 55.6 | usb1k·3 |
| 1999.735 | -83.8 | 54.4 | usb1k·2 |
| 6999.073 | -87.3 | 52.2 | usb1k·7 |
| 15997.881 | -92.0 | 47.9 | usb1k·16 |
| 9998.676 | -92.0 | 47.7 | usb1k·10 |
| 14998.014 | -94.9 | 44.8 | usb1k·15 |
| 10998.543 | -94.5 | 45.0 | usb1k·11 |
| 15999.471 | -95.5 | 44.4 | imd·4·f1+2·f2 |
| 9999.471 | -95.6 | 44.1 | imd·4·f1+1·f2 |
| 13998.941 | -94.7 | 45.2 | imd·8·f1+1·f2 |
| 5999.206 | -95.5 | 43.7 | usb1k·6 |
| 12999.868 | -96.8 | 43.6 | imd·1·f1+2·f2 |
| 11998.411 | -96.5 | 43.4 | usb1k·12 |
| 7998.941 | -96.0 | 44.2 | usb1k·8 |
| 12999.073 | -96.3 | 44.1 | imd·7·f1+1·f2 |
| 14999.603 | -97.2 | 42.6 | imd·3·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.1 | 59.9 | usb1k·1 |
| 6000.000 | -78.2 | 56.8 | fs8·1 |
| 1999.735 | -79.8 | 53.9 | usb1k·2 |
| 2999.603 | -81.2 | 52.7 | usb1k·3 |
| 12000.000 | -81.5 | 54.9 | fs8·2 |
| 18000.000 | -81.6 | 54.9 | fs8·3 |
| 6999.073 | -86.3 | 48.8 | usb1k·7 |
| 15997.881 | -90.4 | 46.2 | usb1k·16 |
| 4999.338 | -91.1 | 43.5 | usb1k·5 |
| 9998.676 | -90.8 | 44.7 | usb1k·10 |
| 5999.206 | -91.5 | 43.5 | usb1k·6 |
| 10998.543 | -93.6 | 42.2 | usb1k·11 |
| 14998.014 | -94.8 | 41.6 | usb1k·15 |
| 9999.471 | -95.3 | 40.1 | imd·4·f1+1·f2 |
| 15999.471 | -95.5 | 41.1 | imd·4·f1+2·f2 |
| 13998.941 | -94.8 | 41.8 | imd·8·f1+1·f2 |
| 7998.941 | -95.1 | 40.9 | usb1k·8 |
| 12999.868 | -96.4 | 40.1 | imd·1·f1+2·f2 |
| 11998.411 | -95.8 | 40.5 | usb1k·12 |
| 20997.220 | -96.4 | 39.5 | usb1k·21 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.13 | 0.16 | 0.03 |
| led | Kanal 1 | 11/11 | 1.52 | -1.18 | 0.57 |
| mains50 | Kanal 1 | 11/11 | 493.66 | -1042.30 | 0.92 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.11 | 0.13 | 0.03 |
| led | Kanal 2 | 11/11 | 0.29 | -0.09 | 0.29 |
| mains50 | Kanal 2 | 11/11 | 337.75 | -11.02 | 0.78 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.02 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.07 | 0.11 | 0.03 |
| led | Kanal 3 | 11/11 | 1.16 | -0.98 | 0.28 |
| mains50 | Kanal 3 | 11/11 | 24.53 | 35.38 | 0.56 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.11 | 0.11 | 0.03 |
| led | Kanal 4 | 11/11 | 0.86 | 0.03 | 0.43 |
| mains50 | Kanal 4 | 11/11 | 337.66 | -69.17 | 0.78 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.91 | 0.31 s (3.22 Hz) | 22.8 |
| Kanal 1 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 30.0 |
| Kanal 2 | breitbandig | 0.79 | 0.16 s (6.38 Hz) | 24.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.89 | 1.25 s (0.80 Hz) | 31.1 |
| Kanal 3 | breitbandig | 0.54 | 0.31 s (3.18 Hz) | 26.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.88 | 1.25 s (0.80 Hz) | 35.3 |
| Kanal 4 | breitbandig | 0.62 | 0.16 s (6.40 Hz) | 24.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.88 | 1.25 s (0.80 Hz) | 30.7 |

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
| Kanal 2 | 0.97 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.94 | 0.94 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.0 | -71.1 | +0.1 | 67 % | 68 % |
| Kanal 2 | -71.7 | -71.9 | +0.1 | 73 % | 73 % |
| Kanal 3 | -73.1 | -73.1 | -0.0 | 82 % | 82 % |
| Kanal 4 | -70.8 | -71.0 | +0.2 | 74 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-3d-end-r2_psd.png)

### Kammprofile

![Kammprofile](B4y-3d-end-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-3d-end-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:29:11. Stream-Meldungen: 0. owl_read: reports/owl_read/B4y-3d-end-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
