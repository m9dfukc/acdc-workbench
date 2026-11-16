# Report B4-fx3i-r1: B4-fx3i-r1 – acdc1 fx3i-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4 v22.4.r-fx3i (ITCM) |
| test | Build-4-Sitzung (Q3): fx3i nach Kontrolle B4-3d, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3i-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4-fx3i-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.9 | -69.3 | -72.2 | -72.3 | -73.1 | -85.5 | -72.7 | -94.8 | -72.4 | 63 % | -76.7 | 4.3 |
| Kanal 2 | -7.2 | -70.3 | -73.4 | -73.2 | -73.9 | -87.5 | -73.5 | -95.2 | -73.2 | 68 % | -78.2 | 5.0 |
| Kanal 3 | -5.4 | -72.3 | -75.7 | -74.9 | -75.5 | -91.7 | -75.1 | -96.1 | -74.9 | 79 % | -81.6 | 6.7 |
| Kanal 4 | -6.3 | -70.1 | -74.4 | -72.2 | -73.4 | -87.8 | -72.6 | -98.3 | -72.2 | 72 % | -77.7 | 5.5 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.7 | 7.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.9 | 55.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0007 | 10/10 | k=2: 4641.090 Hz, -112.7 dB | -108.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0307 | 0.0019 | 2/19 | k=1: 50.032 Hz, -96.1 dB | -98.7 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0047 | 6 | k=29·f1-1·f2: 22996.159 Hz, -121.7 dB | -116.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.0 dB | -96.7 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.6 dB | -99.3 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.6 dB | -83.8 | 8.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.1 dB | -75.5 | 59.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5447 | 0.0006 | 10/10 | k=9: 20884.902 Hz, -112.9 dB | -107.6 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0312 | 0.0014 | 2/19 | k=1: 50.032 Hz, -97.0 dB | -99.6 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0038 | 6 | k=8·f1+2·f2: 19998.938 Hz, -121.6 dB | -117.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -97.0 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.7 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -85.3 dB | -84.4 | 11.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.4 dB | -76.6 | 67.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0004 | 10/10 | k=2: 4641.090 Hz, -113.7 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0317 | 0.0004 | 2/19 | k=1: 50.032 Hz, -97.8 dB | -100.3 | 0.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0046 | 22 | k=25·f1-4·f2: 996.682 Hz, -121.2 dB | -112.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -100.3 dB | -98.0 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.4 dB | -100.7 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.8 dB | -84.1 | 6.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.3 dB | -75.5 | 46.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0009 | 10/10 | k=1: 2320.543 Hz, -113.4 dB | -109.3 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0311 | 0.0015 | 2/19 | k=1: 50.032 Hz, -97.7 dB | -100.2 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0012 | 164 | k=-1·f1+4·f2: 23000.132 Hz, -86.2 dB | -79.7 | 18.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -99.4 dB | -100.0 | 0.2 % |
| stärkste übrige Linie (20000.00 Hz) | Kanal 4 | 20000.0008 | 0.0000 | 1/1 | k=1: 20000.001 Hz, -100.2 dB | -103.2 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 55.7 | usb1k·1 |
| 1999.736 | -81.7 | 47.8 | usb1k·2 |
| 2999.603 | -83.3 | 49.8 | usb1k·3 |
| 12000.000 | -84.4 | 53.1 | fs8·2 |
| 6000.000 | -85.1 | 50.4 | fs8·1 |
| 3999.471 | -86.8 | 45.8 | usb1k·4 |
| 18000.000 | -87.4 | 50.7 | fs8·3 |
| 4999.338 | -89.7 | 45.2 | usb1k·5 |
| 9998.676 | -89.2 | 48.2 | usb1k·10 |
| 15997.882 | -90.7 | 46.3 | usb1k·16 |
| 18997.486 | -92.2 | 45.7 | usb1k·19 |
| 8998.809 | -91.6 | 45.0 | usb1k·9 |
| 6999.074 | -92.5 | 43.2 | usb1k·7 |
| 16997.750 | -93.7 | 44.1 | usb1k·17 |
| 11998.411 | -95.1 | 42.4 | usb1k·12 |
| 50.032 | -96.1 | 22.5 | mains50·1 |
| 5999.206 | -95.4 | 40.2 | usb1k·6 |
| 7998.941 | -94.7 | 40.4 | usb1k·8 |
| 12998.280 | -96.8 | 41.1 | usb1k·13 |
| 20997.221 | -97.3 | 40.6 | usb1k·21 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.1 | 56.8 | usb1k·1 |
| 1999.735 | -82.6 | 48.7 | usb1k·2 |
| 2999.603 | -83.8 | 50.7 | usb1k·3 |
| 12000.000 | -84.6 | 54.2 | fs8·2 |
| 6000.000 | -85.1 | 51.5 | fs8·1 |
| 3999.471 | -87.1 | 47.1 | usb1k·4 |
| 18000.000 | -87.6 | 51.4 | fs8·3 |
| 9998.676 | -89.2 | 49.9 | usb1k·10 |
| 4999.338 | -90.2 | 46.0 | usb1k·5 |
| 15997.882 | -91.0 | 47.3 | usb1k·16 |
| 18997.486 | -92.2 | 47.0 | usb1k·19 |
| 8998.809 | -92.0 | 45.8 | usb1k·9 |
| 16997.750 | -94.0 | 45.3 | usb1k·17 |
| 6999.074 | -93.1 | 44.4 | usb1k·7 |
| 11998.411 | -95.4 | 43.3 | usb1k·12 |
| 7998.941 | -95.3 | 41.4 | usb1k·8 |
| 12998.279 | -96.7 | 42.4 | usb1k·13 |
| 5999.206 | -96.2 | 40.4 | usb1k·6 |
| 50.032 | -97.0 | 24.2 | mains50·1 |
| 20997.221 | -97.7 | 41.1 | usb1k·21 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.4 | 60.5 | usb1k·1 |
| 1999.735 | -84.0 | 51.8 | usb1k·2 |
| 2999.603 | -84.8 | 53.9 | usb1k·3 |
| 12000.000 | -85.3 | 55.6 | fs8·2 |
| 6000.000 | -85.7 | 54.7 | fs8·1 |
| 18000.000 | -87.9 | 53.8 | fs8·3 |
| 3999.471 | -87.8 | 50.6 | usb1k·4 |
| 9998.676 | -89.6 | 52.2 | usb1k·10 |
| 15997.882 | -91.6 | 49.8 | usb1k·16 |
| 4999.338 | -91.3 | 48.9 | usb1k·5 |
| 18997.486 | -92.5 | 49.2 | usb1k·19 |
| 8998.809 | -93.1 | 47.7 | usb1k·9 |
| 16997.750 | -94.5 | 47.7 | usb1k·17 |
| 6999.074 | -94.0 | 46.9 | usb1k·7 |
| 11998.412 | -96.0 | 44.9 | usb1k·12 |
| 12998.280 | -97.0 | 45.3 | usb1k·13 |
| 7998.941 | -96.1 | 44.3 | usb1k·8 |
| 50.032 | -97.8 | 27.7 | mains50·1 |
| 5999.206 | -98.0 | 42.4 | usb1k·6 |
| 20997.221 | -98.5 | 42.2 | usb1k·21 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.3 | 57.6 | usb1k·1 |
| 1999.735 | -82.0 | 50.5 | usb1k·2 |
| 2999.603 | -83.0 | 50.8 | usb1k·3 |
| 12000.000 | -84.8 | 52.7 | fs8·2 |
| 6000.000 | -85.4 | 50.4 | fs8·1 |
| 23000.132 | -86.2 | 51.1 | imd·-1·f1+4·f2 |
| 11000.132 | -86.3 | 50.5 | imd·-1·f1+2·f2 |
| 5000.132 | -86.3 | 48.9 | imd·-1·f1+1·f2 |
| 17000.132 | -86.3 | 50.9 | imd·-1·f1+3·f2 |
| 6999.868 | -86.3 | 49.7 | imd·1·f1+1·f2 |
| 18999.868 | -86.3 | 50.7 | imd·1·f1+3·f2 |
| 12999.868 | -86.4 | 50.5 | imd·1·f1+2·f2 |
| 18000.000 | -87.8 | 50.2 | fs8·3 |
| 3999.471 | -87.9 | 46.2 | usb1k·4 |
| 4999.338 | -90.4 | 44.8 | usb1k·5 |
| 8998.809 | -90.3 | 46.5 | usb1k·9 |
| 15997.882 | -91.9 | 44.7 | usb1k·16 |
| 9998.676 | -90.9 | 45.6 | usb1k·10 |
| 7999.736 | -94.1 | 41.1 | imd·2·f1+1·f2 |
| 16000.264 | -94.2 | 42.5 | imd·-2·f1+3·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.19 | 0.21 | 0.05 |
| led | Kanal 1 | 11/11 | 1.32 | -0.01 | 0.61 |
| mains50 | Kanal 1 | 11/11 | 557.63 | 486.67 | 0.74 |
| other1 | Kanal 1 | 11/11 | 1.44 | 2.80 | 0.05 |
| other2 | Kanal 1 | 11/11 | 0.27 | -0.23 | 0.24 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.22 | 0.27 | 0.04 |
| led | Kanal 2 | 11/11 | 0.35 | -0.24 | 0.25 |
| mains50 | Kanal 2 | 11/11 | 543.73 | 632.18 | 0.71 |
| other1 | Kanal 2 | 11/11 | 0.23 | 0.27 | 0.05 |
| other2 | Kanal 2 | 11/11 | 0.22 | -0.07 | 0.18 |
| fs8 | Kanal 3 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.18 | 0.27 | 0.04 |
| led | Kanal 3 | 11/11 | 0.92 | -0.03 | 0.34 |
| mains50 | Kanal 3 | 11/11 | 210.48 | 125.54 | 0.47 |
| other1 | Kanal 3 | 11/11 | 1.70 | 2.51 | 0.05 |
| other2 | Kanal 3 | 11/11 | 0.17 | -0.11 | 0.10 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.01 | 0.03 |
| usb1k | Kanal 4 | 11/11 | 0.18 | 0.27 | 0.05 |
| led | Kanal 4 | 11/11 | 1.11 | 2.17 | 0.43 |
| mains50 | Kanal 4 | 11/11 | 353.52 | 203.80 | 0.78 |
| other1 | Kanal 4 | 11/11 | 0.24 | -0.09 | 0.20 |
| other2 | Kanal 4 | 11/11 | 0.04 | -0.01 | 0.17 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.32 | 0.31 s (3.18 Hz) | 32.7 |
| Kanal 1 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 34.3 |
| Kanal 2 | breitbandig | 2.21 | 0.31 s (3.18 Hz) | 34.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 36.4 |
| Kanal 3 | breitbandig | 2.02 | 0.31 s (3.18 Hz) | 34.8 |
| Kanal 3 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 41.0 |
| Kanal 4 | breitbandig | 1.68 | 0.31 s (3.18 Hz) | 33.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.99 | 1.25 s (0.80 Hz) | 39.3 |

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
| Kanal 1 | 1.00 | 0.98 | 0.94 | 0.87 |
| Kanal 2 | 0.98 | 1.00 | 0.94 | 0.89 |
| Kanal 3 | 0.94 | 0.94 | 1.00 | 0.83 |
| Kanal 4 | 0.87 | 0.89 | 0.83 | 1.00 |

## Vergleich mit Referenz B4-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.3 | -71.7 | -0.7 | 63 % | 64 % |
| Kanal 2 | -73.2 | -72.6 | -0.6 | 68 % | 69 % |
| Kanal 3 | -74.9 | -73.8 | -1.1 | 79 % | 80 % |
| Kanal 4 | -72.2 | -71.6 | -0.6 | 72 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4-fx3i-r1_psd.png)

### Kammprofile

![Kammprofile](B4-fx3i-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4-fx3i-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:17:48. Stream-Meldungen: 0. owl_read: out/owl_read/B4-fx3i-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
