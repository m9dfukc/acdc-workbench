# Report B4y-fx3j-r1: B4y-fx3j-r1 – acdc1 fx3j-open-inputs, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 4y v22.4.r-fx3j (ITCM ohne USB + RX-Warten) |
| test | Build-4y-Sitzung: fx3j gegen 3d-Kontrolle, Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_fx3j-open-inputs-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4y-fx3j-r1 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B4y-3d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.2 | -67.9 | -77.3 | -68.5 | -69.7 | -86.2 | -68.7 | -94.7 | -68.5 | 85 % | -76.6 | 8.1 |
| Kanal 2 | -7.5 | -68.4 | -78.4 | -68.8 | -70.1 | -88.2 | -69.1 | -94.9 | -68.9 | 88 % | -78.0 | 9.1 |
| Kanal 3 | -5.7 | -69.4 | -80.8 | -69.7 | -71.0 | -92.5 | -69.9 | -95.8 | -69.7 | 93 % | -81.2 | 11.5 |
| Kanal 4 | -6.5 | -68.2 | -79.3 | -68.6 | -69.7 | -88.5 | -68.8 | -95.2 | -68.6 | 88 % | -77.6 | 9.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.2 dB | -72.9 | 35.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.9 dB | -71.6 | 48.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0010 | 10/10 | k=1: 2320.545 Hz, -113.7 dB | -108.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0000 | 0.0006 | 3/19 | k=1: 50.001 Hz, -97.2 dB | -98.3 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0014 | 134 | k=15·f1+1·f2: 20998.014 Hz, -105.7 dB | -94.7 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.8 dB | -96.7 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0003 | 4/7 | k=1: 3000.000 Hz, -98.2 dB | -99.0 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.3 dB | -73.0 | 38.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -72.0 | 48.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5447 | 0.0007 | 10/10 | k=9: 20884.903 Hz, -112.9 dB | -107.6 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0000 | 0.0012 | 3/19 | k=1: 50.000 Hz, -98.0 dB | -98.8 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0012 | 140 | k=15·f1+1·f2: 20998.014 Hz, -105.8 dB | -94.7 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -96.9 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0003 | 0.0001 | 4/7 | k=1: 3000.000 Hz, -98.7 dB | -99.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.7 dB | -73.5 | 42.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.7 dB | -72.7 | 50.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0005 | 10/10 | k=1: 2320.545 Hz, -113.9 dB | -109.3 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9936 | 0.0056 | 5/19 | k=1: 50.000 Hz, -98.8 dB | -101.1 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0011 | 152 | k=15·f1+1·f2: 20998.015 Hz, -106.5 dB | -95.2 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.8 dB | -97.7 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -100.0 dB | -100.3 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -73.6 dB | -73.2 | 34.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.2 dB | -71.4 | 52.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0010 | 10/10 | k=1: 2320.545 Hz, -112.8 dB | -108.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0000 | 0.0009 | 3/19 | k=1: 50.000 Hz, -98.6 dB | -99.2 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0020 | 137 | k=15·f1+1·f2: 20998.014 Hz, -105.7 dB | -94.8 | 0.2 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.7 dB | -97.1 | 0.1 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.1 dB | -99.6 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -73.2 | 61.9 | fs8·1 |
| 999.868 | -73.9 | 57.9 | usb1k·1 |
| 12000.000 | -75.0 | 62.4 | fs8·2 |
| 18000.000 | -76.5 | 61.6 | fs8·3 |
| 2999.603 | -77.2 | 57.0 | usb1k·3 |
| 1999.735 | -77.9 | 55.3 | usb1k·2 |
| 6999.074 | -78.4 | 57.7 | usb1k·7 |
| 14998.015 | -81.5 | 56.8 | usb1k·15 |
| 9998.676 | -81.5 | 55.6 | usb1k·10 |
| 4999.339 | -82.1 | 52.9 | usb1k·5 |
| 13998.147 | -84.0 | 53.6 | usb1k·14 |
| 21997.089 | -84.3 | 53.2 | usb1k·22 |
| 11998.412 | -85.2 | 52.0 | usb1k·12 |
| 7998.941 | -84.3 | 52.6 | usb1k·8 |
| 19997.353 | -85.8 | 52.0 | usb1k·20 |
| 20997.221 | -86.7 | 51.1 | usb1k·21 |
| 16997.750 | -87.2 | 50.5 | usb1k·17 |
| 18997.486 | -87.2 | 51.1 | usb1k·19 |
| 5999.206 | -88.9 | 46.1 | usb1k·6 |
| 8998.809 | -88.9 | 46.7 | usb1k·9 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -73.3 | 63.4 | fs8·1 |
| 999.868 | -74.7 | 58.5 | usb1k·1 |
| 12000.000 | -75.1 | 63.6 | fs8·2 |
| 18000.000 | -76.5 | 62.8 | fs8·3 |
| 2999.603 | -77.5 | 58.1 | usb1k·3 |
| 1999.735 | -78.5 | 56.2 | usb1k·2 |
| 6999.074 | -78.5 | 58.9 | usb1k·7 |
| 14998.015 | -81.5 | 57.6 | usb1k·15 |
| 4999.339 | -81.7 | 54.4 | usb1k·5 |
| 9998.676 | -81.5 | 56.9 | usb1k·10 |
| 13998.147 | -84.2 | 54.3 | usb1k·14 |
| 21997.089 | -84.4 | 54.5 | usb1k·22 |
| 11998.412 | -84.9 | 53.6 | usb1k·12 |
| 7998.941 | -84.1 | 54.3 | usb1k·8 |
| 19997.353 | -85.6 | 53.6 | usb1k·20 |
| 16997.750 | -87.3 | 51.9 | usb1k·17 |
| 20997.221 | -86.9 | 52.1 | usb1k·21 |
| 18997.486 | -87.2 | 52.1 | usb1k·19 |
| 5999.206 | -89.6 | 47.1 | usb1k·6 |
| 17997.618 | -90.6 | 48.7 | usb1k·18 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -73.7 | 66.7 | fs8·1 |
| 12000.000 | -75.6 | 66.1 | fs8·2 |
| 999.868 | -75.7 | 62.4 | usb1k·1 |
| 18000.000 | -77.0 | 64.5 | fs8·3 |
| 2999.603 | -78.2 | 61.8 | usb1k·3 |
| 1999.735 | -79.7 | 59.8 | usb1k·2 |
| 6999.074 | -79.1 | 62.0 | usb1k·7 |
| 14998.015 | -81.9 | 59.5 | usb1k·15 |
| 4999.339 | -82.0 | 58.6 | usb1k·5 |
| 9998.676 | -81.8 | 59.9 | usb1k·10 |
| 13998.147 | -84.9 | 56.8 | usb1k·14 |
| 21997.089 | -84.9 | 56.3 | usb1k·22 |
| 11998.412 | -85.3 | 56.3 | usb1k·12 |
| 7998.941 | -84.4 | 57.1 | usb1k·8 |
| 19997.353 | -86.0 | 55.5 | usb1k·20 |
| 16997.750 | -87.6 | 54.0 | usb1k·17 |
| 18997.486 | -87.7 | 53.8 | usb1k·19 |
| 20997.221 | -87.5 | 54.0 | usb1k·21 |
| 17997.618 | -91.2 | 50.4 | usb1k·18 |
| 5999.206 | -90.8 | 49.6 | usb1k·6 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.2 | 59.7 | usb1k·1 |
| 6000.000 | -73.6 | 62.6 | fs8·1 |
| 12000.000 | -75.3 | 62.9 | fs8·2 |
| 18000.000 | -76.7 | 61.4 | fs8·3 |
| 1999.735 | -77.1 | 57.1 | usb1k·2 |
| 2999.603 | -77.2 | 58.1 | usb1k·3 |
| 6999.074 | -78.3 | 58.2 | usb1k·7 |
| 14998.015 | -81.8 | 56.4 | usb1k·15 |
| 9998.676 | -81.7 | 56.0 | usb1k·10 |
| 4999.339 | -83.0 | 52.6 | usb1k·5 |
| 13998.147 | -83.9 | 53.7 | usb1k·14 |
| 21997.089 | -84.5 | 53.5 | usb1k·22 |
| 11998.412 | -85.7 | 52.4 | usb1k·12 |
| 19997.353 | -86.2 | 52.1 | usb1k·20 |
| 7998.941 | -84.9 | 52.8 | usb1k·8 |
| 20997.221 | -86.6 | 51.6 | usb1k·21 |
| 16997.750 | -87.5 | 51.0 | usb1k·17 |
| 18997.486 | -87.5 | 50.8 | usb1k·19 |
| 5999.206 | -87.9 | 48.2 | usb1k·6 |
| 8998.809 | -88.3 | 48.4 | usb1k·9 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 1 | 11/11 | 0.18 | -0.09 | 0.02 |
| led | Kanal 1 | 11/11 | 0.99 | -2.13 | 0.45 |
| mains50 | Kanal 1 | 11/11 | 18.23 | 38.93 | 0.33 |
| other1 | Kanal 1 | 11/11 | 1.33 | -1.57 | 0.05 |
| other2 | Kanal 1 | 11/11 | 0.21 | 0.24 | 0.17 |
| fs8 | Kanal 2 | 11/11 | 0.00 | 0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.20 | -0.06 | 0.02 |
| led | Kanal 2 | 11/11 | 0.42 | -0.64 | 0.30 |
| mains50 | Kanal 2 | 11/11 | 16.29 | 40.77 | 0.45 |
| other1 | Kanal 2 | 11/11 | 0.37 | -0.35 | 0.06 |
| other2 | Kanal 2 | 11/11 | 0.20 | 0.11 | 0.13 |
| fs8 | Kanal 3 | 11/11 | 0.00 | 0.00 | 0.00 |
| usb1k | Kanal 3 | 11/11 | 0.04 | -0.00 | 0.01 |
| led | Kanal 3 | 11/11 | 0.70 | -0.53 | 0.37 |
| mains50 | Kanal 3 | 11/11 | 12.52 | 26.86 | 0.20 |
| other1 | Kanal 3 | 11/11 | 0.26 | 0.04 | 0.04 |
| other2 | Kanal 3 | 11/11 | 0.21 | -0.01 | 0.09 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.15 | -0.04 | 0.03 |
| led | Kanal 4 | 11/11 | 1.45 | -0.76 | 0.45 |
| mains50 | Kanal 4 | 11/11 | 39.65 | 58.12 | 0.52 |
| other1 | Kanal 4 | 11/11 | 1.75 | -2.45 | 0.07 |
| other2 | Kanal 4 | 11/11 | 0.23 | -0.15 | 0.19 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.68 | 0.31 s (3.22 Hz) | 28.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.93 | 7.50 s (0.13 Hz) | 38.1 |
| Kanal 2 | breitbandig | 0.63 | 0.31 s (3.22 Hz) | 30.1 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 39.4 |
| Kanal 3 | breitbandig | 0.51 | 0.63 s (1.58 Hz) | 31.2 |
| Kanal 3 | 999.9 Hz ± 10 | 0.92 | 7.50 s (0.13 Hz) | 43.3 |
| Kanal 4 | breitbandig | 0.53 | 0.31 s (3.22 Hz) | 29.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 38.3 |

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
| Kanal 1 | 1.00 | 0.98 | 0.96 | 0.97 |
| Kanal 2 | 0.98 | 1.00 | 0.97 | 0.98 |
| Kanal 3 | 0.96 | 0.97 | 1.00 | 0.96 |
| Kanal 4 | 0.97 | 0.98 | 0.96 | 1.00 |

## Vergleich mit Referenz B4y-3d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -68.5 | -71.1 | +2.6 | 85 % | 68 % |
| Kanal 2 | -68.8 | -71.9 | +3.0 | 88 % | 73 % |
| Kanal 3 | -69.7 | -73.1 | +3.4 | 93 % | 82 % |
| Kanal 4 | -68.6 | -71.0 | +2.4 | 88 % | 74 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4y-fx3j-r1_psd.png)

### Kammprofile

![Kammprofile](B4y-fx3j-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B4y-fx3j-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 18:17:27. Stream-Meldungen: 0. owl_read: reports/owl_read/B4y-fx3j-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
