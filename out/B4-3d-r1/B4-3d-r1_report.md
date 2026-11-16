# Report B4-3d-r1: B4-3d-r1 – acdc1 3d-ctrl-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4-Sitzung, Kontrolle 3d vor fx3i (Q3): Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-ctrl-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4-3d-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref X1-rec --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -70.8 | -78.6 | -71.7 | -72.7 | -87.0 | -72.0 | -101.0 | -71.7 | 64 % | -76.1 | 4.4 |
| Kanal 2 | -7.0 | -71.8 | -80.0 | -72.6 | -73.7 | -88.7 | -72.9 | – | -72.6 | 69 % | -77.7 | 5.1 |
| Kanal 3 | -5.2 | -73.3 | -83.6 | -73.8 | -74.9 | -93.1 | -74.1 | – | -73.8 | 80 % | -80.8 | 7.1 |
| Kanal 4 | -6.0 | -71.1 | -80.1 | -71.6 | -72.6 | -88.9 | -72.0 | – | -71.6 | 71 % | -77.0 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -79.0 | 18.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.5 | 41.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5449 | 0.0015 | 10/10 | k=2: 4641.091 Hz, -117.0 dB | -113.4 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9888 | 0.0014 | 2/19 | k=1: 49.990 Hz, -96.4 dB | -99.0 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0009 | 144 | k=8·f1+1·f2: 13998.941 Hz, -95.5 dB | -85.5 | 4.1 % |
| stärkste übrige Linie (51.15 Hz) | Kanal 1 | 51.1522 | 0.0002 | 2/466 | k=1: 51.152 Hz, -99.2 dB | -101.0 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -78.9 | 23.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.1 dB | -76.5 | 40.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0015 | 10/10 | k=9: 20884.904 Hz, -114.7 dB | -110.3 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9886 | 0.0013 | 2/19 | k=1: 49.990 Hz, -96.8 dB | -99.5 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0014 | 160 | k=8·f1+1·f2: 13998.941 Hz, -95.3 dB | -85.4 | 5.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.1 | 29.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -76.0 dB | -77.3 | 44.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0009 | 10/10 | k=2: 4641.091 Hz, -117.7 dB | -113.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9886 | 0.0007 | 2/19 | k=1: 49.989 Hz, -97.6 dB | -100.2 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0008 | 161 | k=8·f1+1·f2: 13998.941 Hz, -95.6 dB | -85.6 | 6.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.1 | 17.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.8 | 48.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0015 | 10/10 | k=1: 2320.542 Hz, -116.6 dB | -112.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9863 | 0.0027 | 3/19 | k=1: 49.989 Hz, -97.3 dB | -99.9 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0013 | 150 | k=8·f1+1·f2: 13998.941 Hz, -95.3 dB | -85.5 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 57.7 | usb1k·1 |
| 6000.000 | -78.7 | 56.1 | fs8·1 |
| 1999.735 | -81.8 | 51.2 | usb1k·2 |
| 18000.000 | -82.3 | 53.9 | fs8·3 |
| 12000.000 | -82.4 | 53.8 | fs8·2 |
| 2999.603 | -82.5 | 51.5 | usb1k·3 |
| 6999.074 | -87.7 | 47.7 | usb1k·7 |
| 15997.882 | -92.0 | 44.2 | usb1k·16 |
| 9998.676 | -92.0 | 41.6 | usb1k·10 |
| 5999.206 | -93.9 | 40.9 | usb1k·6 |
| 14998.015 | -95.1 | 40.9 | usb1k·15 |
| 10998.544 | -94.6 | 41.2 | usb1k·11 |
| 4999.339 | -95.2 | 39.4 | usb1k·5 |
| 15999.471 | -96.2 | 40.1 | imd·4·f1+2·f2 |
| 9999.471 | -96.2 | 37.3 | imd·4·f1+1·f2 |
| 13998.941 | -95.5 | 40.7 | imd·8·f1+1·f2 |
| 12999.868 | -97.1 | 38.7 | imd·1·f1+2·f2 |
| 49.990 | -96.4 | 27.7 | mains50·1 |
| 18999.868 | -97.8 | 38.2 | imd·1·f1+3·f2 |
| 16998.544 | -97.2 | 38.9 | imd·11·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.1 | 58.4 | usb1k·1 |
| 6000.000 | -78.7 | 57.8 | fs8·1 |
| 18000.000 | -82.1 | 55.7 | fs8·3 |
| 12000.000 | -82.1 | 55.1 | fs8·2 |
| 1999.735 | -83.1 | 51.5 | usb1k·2 |
| 2999.603 | -83.1 | 52.6 | usb1k·3 |
| 6999.074 | -87.8 | 49.1 | usb1k·7 |
| 15997.882 | -92.4 | 45.4 | usb1k·16 |
| 9998.676 | -92.3 | 41.7 | usb1k·10 |
| 14998.015 | -95.0 | 42.6 | usb1k·15 |
| 10998.544 | -94.6 | 42.8 | usb1k·11 |
| 5999.206 | -95.2 | 41.3 | usb1k·6 |
| 15999.471 | -96.0 | 41.9 | imd·4·f1+2·f2 |
| 9999.471 | -96.2 | 37.8 | imd·4·f1+1·f2 |
| 13998.941 | -95.3 | 42.1 | imd·8·f1+1·f2 |
| 12999.868 | -97.1 | 40.5 | imd·1·f1+2·f2 |
| 49.990 | -96.8 | 29.0 | mains50·1 |
| 18999.868 | -97.9 | 39.5 | imd·1·f1+3·f2 |
| 16998.544 | -97.1 | 40.4 | imd·11·f1+1·f2 |
| 19998.941 | -96.4 | 40.1 | imd·8·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -76.0 | 62.0 | usb1k·1 |
| 6000.000 | -79.0 | 61.0 | fs8·1 |
| 12000.000 | -82.2 | 58.1 | fs8·2 |
| 18000.000 | -82.4 | 58.0 | fs8·3 |
| 2999.603 | -83.9 | 55.5 | usb1k·3 |
| 1999.735 | -84.0 | 54.8 | usb1k·2 |
| 6999.074 | -88.4 | 52.2 | usb1k·7 |
| 15997.882 | -93.0 | 47.1 | usb1k·16 |
| 9998.676 | -92.7 | 46.6 | usb1k·10 |
| 14998.015 | -95.2 | 44.8 | usb1k·15 |
| 10998.544 | -95.2 | 45.4 | usb1k·11 |
| 15999.471 | -96.3 | 43.9 | imd·4·f1+2·f2 |
| 9999.471 | -96.3 | 43.0 | imd·4·f1+1·f2 |
| 5999.206 | -96.0 | 44.1 | usb1k·6 |
| 13998.941 | -95.6 | 45.1 | imd·8·f1+1·f2 |
| 12999.868 | -97.4 | 42.6 | imd·1·f1+2·f2 |
| 16998.544 | -97.2 | 42.6 | imd·11·f1+1·f2 |
| 12999.074 | -97.1 | 42.9 | imd·7·f1+1·f2 |
| 19998.941 | -96.7 | 43.1 | imd·8·f1+2·f2 |
| 49.989 | -97.6 | 33.0 | mains50·1 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 59.8 | usb1k·1 |
| 6000.000 | -79.0 | 57.1 | fs8·1 |
| 1999.735 | -80.2 | 53.7 | usb1k·2 |
| 18000.000 | -82.2 | 54.5 | fs8·3 |
| 12000.000 | -82.2 | 54.1 | fs8·2 |
| 2999.603 | -82.0 | 52.8 | usb1k·3 |
| 6999.074 | -87.1 | 48.7 | usb1k·7 |
| 15997.882 | -91.1 | 45.7 | usb1k·16 |
| 9998.676 | -91.8 | 41.1 | usb1k·10 |
| 4999.339 | -92.5 | 42.9 | usb1k·5 |
| 5999.206 | -92.3 | 43.8 | usb1k·6 |
| 10998.544 | -94.0 | 42.0 | usb1k·11 |
| 14998.015 | -95.3 | 41.3 | usb1k·15 |
| 15999.471 | -96.0 | 40.8 | imd·4·f1+2·f2 |
| 9999.471 | -96.3 | 36.6 | imd·4·f1+1·f2 |
| 13998.941 | -95.3 | 41.0 | imd·8·f1+1·f2 |
| 13998.147 | -96.8 | 39.4 | usb1k·14 |
| 20997.221 | -96.8 | 39.5 | usb1k·21 |
| 12999.868 | -97.3 | 38.8 | imd·1·f1+2·f2 |
| 11998.412 | -96.9 | 39.6 | usb1k·12 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.14 | -0.10 | 0.05 |
| led | Kanal 1 | 11/11 | 4.98 | -3.63 | 0.85 |
| mains50 | Kanal 1 | 11/11 | 341.99 | 50.57 | 0.50 |
| other1 | Kanal 1 | 11/11 | 0.69 | 0.62 | 1.97 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.12 | -0.08 | 0.05 |
| led | Kanal 2 | 11/11 | 0.39 | 0.25 | 0.39 |
| mains50 | Kanal 2 | 11/11 | 258.18 | -430.08 | 0.47 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.09 | -0.06 | 0.02 |
| led | Kanal 3 | 11/11 | 1.64 | 1.01 | 0.47 |
| mains50 | Kanal 3 | 11/11 | 157.57 | -438.36 | 0.24 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.12 | -0.14 | 0.04 |
| led | Kanal 4 | 11/11 | 1.48 | -0.72 | 0.43 |
| mains50 | Kanal 4 | 11/11 | 412.62 | 41.60 | 0.50 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.92 | 0.31 s (3.18 Hz) | 27.2 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 31.8 |
| Kanal 2 | breitbandig | 0.82 | 0.31 s (3.18 Hz) | 26.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.92 | 1.25 s (0.80 Hz) | 33.2 |
| Kanal 3 | breitbandig | 0.56 | 0.31 s (3.18 Hz) | 29.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 36.9 |
| Kanal 4 | breitbandig | 0.71 | 0.31 s (3.18 Hz) | 27.0 |
| Kanal 4 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 33.5 |

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
| Kanal 1 | 1.00 | 0.96 | 0.93 | 0.94 |
| Kanal 2 | 0.96 | 1.00 | 0.94 | 0.96 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz X1-rec

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.7 | -72.7 | +1.0 | 64 % | 48 % |
| Kanal 2 | -72.6 | -73.1 | +0.5 | 69 % | 61 % |
| Kanal 3 | -73.8 | -75.0 | +1.3 | 80 % | 70 % |
| Kanal 4 | -71.6 | -72.5 | +0.8 | 71 % | 60 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4-3d-r1_psd.png)

### Kammprofile

![Kammprofile](B4-3d-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4-3d-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:09:22. Stream-Meldungen: 0. owl_read: out/owl_read/B4-3d-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
