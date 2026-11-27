# Report B6b-fx4b-end-r2: B6b-fx4b-end-r2 – acdc1 fx4b-open-inputs-6-end, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Build-6-Sitzung: fx4b am Ende (nach der fx3l-Kontrolle), Eingänge offen, rohe ADC-Daten |
| gain | gvar |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | Slot 1: ACDC (Default-Patch, per Program Change), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261117_acdc1_fx4b-open-inputs-6-end-r2_gvar_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-fx4b-end-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B6b-fx3l-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.9 | -69.8 | -73.7 | -72.0 | -72.7 | -85.2 | -72.3 | -93.0 | -72.0 | 65 % | -76.6 | 4.6 |
| Kanal 2 | -7.3 | -70.8 | -74.6 | -73.1 | -73.9 | -87.1 | -73.4 | -93.7 | -73.2 | 67 % | -78.0 | 4.8 |
| Kanal 3 | -5.5 | -73.2 | -79.4 | -74.4 | -75.0 | -91.6 | -74.6 | -95.6 | -74.4 | 82 % | -81.8 | 7.4 |
| Kanal 4 | -6.4 | -70.3 | -74.7 | -72.3 | -72.9 | -87.2 | -72.6 | -95.6 | -72.3 | 70 % | -77.5 | 5.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.9 dB | -83.0 | 7.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.5 | 57.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0013 | 10/10 | k=1: 2320.544 Hz, -112.5 dB | -109.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0000 | 0.0027 | 3/19 | k=1: 49.999 Hz, -98.1 dB | -98.8 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0015 | 5 | k=-4·f1+4·f2: 20000.532 Hz, -121.1 dB | -118.1 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 1 | 4401.9001 | 0.0005 | 2/5 | k=1: 4401.900 Hz, -91.9 dB | -94.9 | 0.5 % |
| stärkste übrige Linie (2200.95 Hz) | Kanal 1 | 2200.9501 | 0.0002 | 2/10 | k=1: 2200.950 Hz, -96.6 dB | -97.4 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -84.2 dB | -83.2 | 9.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.6 | 56.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0006 | 10/10 | k=1: 2320.544 Hz, -113.6 dB | -108.6 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0000 | 0.0017 | 3/19 | k=1: 49.999 Hz, -98.7 dB | -99.2 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0024 | 12 | k=-1·f1+2·f2: 11000.134 Hz, -120.9 dB | -114.9 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 2 | 4401.9001 | 0.0005 | 2/5 | k=1: 4401.900 Hz, -93.8 dB | -96.8 | 0.4 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.1 dB | -96.6 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -85.0 dB | -83.8 | 11.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.8 dB | -76.0 | 69.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0008 | 10/10 | k=1: 2320.544 Hz, -113.2 dB | -109.4 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9997 | 0.0156 | 5/19 | k=1: 49.999 Hz, -99.0 dB | -99.6 | 0.3 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0028 | 29 | k=-7·f1+4·f2: 17000.926 Hz, -121.5 dB | -112.9 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 3 | 4401.9001 | 0.0003 | 2/5 | k=1: 4401.900 Hz, -97.3 dB | -100.3 | 0.3 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0001 | 8/11 | k=1: 2000.000 Hz, -99.7 dB | -97.5 | 0.5 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -84.4 dB | -83.4 | 7.8 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.4 | 61.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0011 | 10/10 | k=1: 2320.545 Hz, -112.9 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0000 | 0.0019 | 3/19 | k=1: 49.999 Hz, -98.9 dB | -99.6 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0053 | 17 | k=-1·f1+2·f2: 11000.131 Hz, -115.3 dB | -110.0 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 4 | 4401.9001 | 0.0004 | 2/5 | k=1: 4401.900 Hz, -94.0 dB | -96.9 | 0.3 % |
| stärkste übrige Linie (6602.85 Hz) | Kanal 4 | 6602.8502 | 0.0000 | 1/3 | k=1: 6602.850 Hz, -98.5 dB | -101.5 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 56.2 | usb1k·1 |
| 1999.735 | -81.1 | 51.2 | usb1k·2 |
| 2999.603 | -82.5 | 51.7 | usb1k·3 |
| 12000.000 | -83.9 | 53.5 | fs8·2 |
| 6000.000 | -84.4 | 51.5 | fs8·1 |
| 18000.000 | -86.5 | 51.6 | fs8·3 |
| 3999.471 | -87.5 | 45.7 | usb1k·4 |
| 9998.676 | -88.4 | 48.6 | usb1k·10 |
| 15997.882 | -90.3 | 48.0 | usb1k·16 |
| 4999.339 | -90.2 | 45.5 | usb1k·5 |
| 4401.900 | -91.9 | 41.2 | other1·1 |
| 6999.074 | -90.8 | 45.3 | usb1k·7 |
| 8998.809 | -90.9 | 45.0 | usb1k·9 |
| 16997.750 | -93.0 | 45.0 | usb1k·17 |
| 18997.486 | -93.5 | 44.4 | usb1k·19 |
| 20997.221 | -95.2 | 43.1 | usb1k·21 |
| 5999.206 | -94.8 | 41.1 | usb1k·6 |
| 7998.941 | -94.5 | 41.5 | usb1k·8 |
| 11998.411 | -95.6 | 41.8 | usb1k·12 |
| 12998.279 | -95.9 | 41.5 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 56.2 | usb1k·1 |
| 1999.735 | -82.5 | 51.3 | usb1k·2 |
| 2999.603 | -83.3 | 52.0 | usb1k·3 |
| 12000.000 | -84.2 | 54.4 | fs8·2 |
| 6000.000 | -84.5 | 52.7 | fs8·1 |
| 18000.000 | -86.5 | 52.7 | fs8·3 |
| 3999.471 | -88.0 | 46.9 | usb1k·4 |
| 9998.676 | -88.5 | 50.0 | usb1k·10 |
| 15997.882 | -90.8 | 48.1 | usb1k·16 |
| 4999.339 | -91.4 | 45.2 | usb1k·5 |
| 6999.074 | -91.5 | 45.7 | usb1k·7 |
| 8998.809 | -91.8 | 45.5 | usb1k·9 |
| 16997.750 | -93.5 | 45.4 | usb1k·17 |
| 18997.486 | -93.5 | 45.1 | usb1k·19 |
| 4401.900 | -93.8 | 41.1 | other1·1 |
| 20997.221 | -95.7 | 43.7 | usb1k·21 |
| 12998.279 | -96.3 | 42.3 | usb1k·13 |
| 11998.412 | -96.2 | 42.4 | usb1k·12 |
| 7998.941 | -96.0 | 41.6 | usb1k·8 |
| 5999.206 | -97.0 | 40.3 | usb1k·6 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.8 | 61.0 | usb1k·1 |
| 1999.735 | -82.8 | 55.6 | usb1k·2 |
| 2999.603 | -83.9 | 56.3 | usb1k·3 |
| 12000.000 | -85.0 | 57.6 | fs8·2 |
| 6000.000 | -85.1 | 56.1 | fs8·1 |
| 18000.000 | -86.9 | 55.2 | fs8·3 |
| 3999.471 | -88.4 | 50.7 | usb1k·4 |
| 9998.676 | -89.0 | 52.6 | usb1k·10 |
| 15997.882 | -91.0 | 51.3 | usb1k·16 |
| 4999.339 | -91.3 | 49.6 | usb1k·5 |
| 8998.809 | -91.8 | 49.4 | usb1k·9 |
| 6999.074 | -92.3 | 49.0 | usb1k·7 |
| 18997.486 | -93.7 | 48.1 | usb1k·19 |
| 16997.750 | -93.9 | 48.1 | usb1k·17 |
| 20997.221 | -96.3 | 45.9 | usb1k·21 |
| 11998.412 | -96.2 | 46.4 | usb1k·12 |
| 12998.279 | -96.5 | 45.2 | usb1k·13 |
| 4401.900 | -97.3 | 41.9 | other1·1 |
| 7998.941 | -95.8 | 45.6 | usb1k·8 |
| 5999.206 | -96.9 | 44.4 | usb1k·6 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 57.0 | usb1k·1 |
| 1999.735 | -80.9 | 52.5 | usb1k·2 |
| 2999.603 | -82.6 | 52.3 | usb1k·3 |
| 12000.000 | -84.4 | 53.4 | fs8·2 |
| 6000.000 | -84.6 | 51.8 | fs8·1 |
| 18000.000 | -86.7 | 51.5 | fs8·3 |
| 3999.471 | -87.5 | 46.8 | usb1k·4 |
| 9998.676 | -88.6 | 48.9 | usb1k·10 |
| 15997.882 | -90.4 | 47.8 | usb1k·16 |
| 4999.339 | -90.4 | 45.4 | usb1k·5 |
| 6999.074 | -90.7 | 46.1 | usb1k·7 |
| 8998.809 | -91.1 | 45.6 | usb1k·9 |
| 16997.750 | -93.2 | 44.8 | usb1k·17 |
| 18997.486 | -93.7 | 44.2 | usb1k·19 |
| 4401.900 | -94.0 | 40.8 | other1·1 |
| 20997.221 | -95.2 | 43.7 | usb1k·21 |
| 7998.941 | -94.2 | 42.7 | usb1k·8 |
| 5999.206 | -95.2 | 41.3 | usb1k·6 |
| 11998.412 | -95.6 | 42.2 | usb1k·12 |
| 12998.279 | -96.4 | 41.7 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.18 | -0.05 | 0.03 |
| led | Kanal 1 | 11/11 | 1.67 | -0.92 | 0.45 |
| mains50 | Kanal 1 | 11/11 | 39.38 | 69.05 | 0.89 |
| other1 | Kanal 1 | 11/11 | 1.21 | 0.90 | 0.13 |
| other2 | Kanal 1 | 11/11 | 0.22 | -0.03 | 0.14 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.23 | -0.07 | 0.07 |
| led | Kanal 2 | 11/11 | 0.40 | -0.07 | 0.23 |
| mains50 | Kanal 2 | 11/11 | 48.96 | 77.18 | 0.82 |
| other1 | Kanal 2 | 11/11 | 1.75 | 1.53 | 0.13 |
| other2 | Kanal 2 | 11/11 | 1.97 | -2.88 | 0.14 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.19 | -0.12 | 0.02 |
| led | Kanal 3 | 11/11 | 0.64 | -0.74 | 0.31 |
| mains50 | Kanal 3 | 11/11 | 14.85 | -3.86 | 0.40 |
| other1 | Kanal 3 | 11/11 | 1.20 | 1.37 | 0.12 |
| other2 | Kanal 3 | 11/11 | 0.25 | -0.27 | 0.12 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.03 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.20 | -0.10 | 0.10 |
| led | Kanal 4 | 11/11 | 1.41 | -0.79 | 0.43 |
| mains50 | Kanal 4 | 11/11 | 51.48 | 80.68 | 0.89 |
| other1 | Kanal 4 | 11/11 | 1.63 | 0.50 | 0.13 |
| other2 | Kanal 4 | 11/11 | 0.23 | 0.04 | 0.14 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.73 | 0.16 s (6.40 Hz) | 32.8 |
| Kanal 1 | 999.9 Hz ± 10 | 0.94 | 7.50 s (0.13 Hz) | 34.9 |
| Kanal 2 | breitbandig | 1.72 | 0.16 s (6.40 Hz) | 34.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.96 | 7.50 s (0.13 Hz) | 36.4 |
| Kanal 3 | breitbandig | 1.11 | 0.16 s (6.40 Hz) | 31.2 |
| Kanal 3 | 999.9 Hz ± 10 | 0.91 | 7.50 s (0.13 Hz) | 41.2 |
| Kanal 4 | breitbandig | 1.50 | 0.16 s (6.40 Hz) | 35.5 |
| Kanal 4 | 999.9 Hz ± 10 | 0.96 | 0.31 s (3.20 Hz) | 35.4 |

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
| Kanal 1 | 1.00 | 0.97 | 0.93 | 0.96 |
| Kanal 2 | 0.97 | 1.00 | 0.92 | 0.97 |
| Kanal 3 | 0.93 | 0.92 | 1.00 | 0.92 |
| Kanal 4 | 0.96 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz B6b-fx3l-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.0 | -72.0 | +0.0 | 65 % | 66 % |
| Kanal 2 | -73.1 | -73.1 | -0.1 | 67 % | 68 % |
| Kanal 3 | -74.4 | -74.5 | +0.1 | 82 % | 82 % |
| Kanal 4 | -72.3 | -72.1 | -0.2 | 70 % | 72 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-fx4b-end-r2_psd.png)

### Kammprofile

![Kammprofile](B6b-fx4b-end-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-fx4b-end-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:18:01. Stream-Meldungen: 0. owl_read: reports/owl_read/B6b-fx4b-end-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
