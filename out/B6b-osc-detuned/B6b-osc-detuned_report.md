# Report B6b-osc-detuned: B6b-osc-detuned – acdc1 fx4b-open-inputs-osc-detuned, 30 s

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Wie B6b-fx4b-end, aber Oszillator im Rack deutlich verstimmt (Nutzer): Test, ob die Linien 2200,95 / 4401,90 / 6602,85 Hz mitwandern |
| gain | gvar |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | laufender Patch siehe owl_read |
| Datei(en) | `20261117_acdc1_fx4b-open-inputs-osc-detuned_gvar_usb-stream.wav` |
| Format | 48000 Hz, 30.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-osc-detuned --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B6b-fx4b-end-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.0 | -71.5 | -81.8 | -71.9 | -72.7 | -85.9 | -72.3 | -93.4 | -72.0 | 65 % | -76.6 | 4.6 |
| Kanal 2 | -7.4 | -72.6 | -82.8 | -73.1 | -73.8 | -88.0 | -73.4 | -94.7 | -73.1 | 68 % | -78.0 | 4.9 |
| Kanal 3 | -5.5 | -74.1 | -87.2 | -74.3 | -74.8 | -92.2 | -74.5 | -97.2 | -74.3 | 82 % | -81.7 | 7.4 |
| Kanal 4 | -6.5 | -71.8 | -83.3 | -72.2 | -72.7 | -88.2 | -72.4 | -95.0 | -72.2 | 71 % | -77.6 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -83.0 | 7.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -73.1 dB | -74.4 | 57.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5445 | 0.0032 | 10/10 | k=2: 4641.092 Hz, -113.1 dB | -109.8 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0345 | 0.0019 | 2/19 | k=1: 50.033 Hz, -96.8 dB | -99.5 | 0.2 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 1 | 4401.9003 | 0.0015 | 2/5 | k=1: 4401.900 Hz, -91.9 dB | -94.9 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0010 | 4/7 | k=1: 2999.999 Hz, -97.9 dB | -98.7 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0001 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -83.1 | 9.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.5 | 57.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0018 | 10/10 | k=8: 18564.358 Hz, -113.7 dB | -108.5 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0359 | 0.0015 | 3/19 | k=1: 50.034 Hz, -97.4 dB | -100.0 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0001 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0048 | 3 | k=-1·f1+3·f2: 17000.128 Hz, -117.0 dB | -111.8 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 2 | 4401.9010 | 0.0033 | 2/5 | k=1: 4401.900 Hz, -93.7 dB | -96.7 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0008 | 4/7 | k=1: 2999.999 Hz, -98.4 dB | -99.1 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.5 dB | -83.7 | 11.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -75.9 | 70.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0013 | 10/10 | k=2: 4641.090 Hz, -113.9 dB | -109.4 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0355 | 0.0052 | 4/19 | k=1: 50.035 Hz, -98.4 dB | -101.1 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0041 | 6 | k=1·f1+1·f2: 6999.867 Hz, -118.9 dB | -109.9 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 3 | 4401.8999 | 0.0006 | 2/5 | k=1: 4401.900 Hz, -97.4 dB | -100.4 | 0.2 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -99.8 dB | -100.0 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -84.0 dB | -83.3 | 7.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.7 dB | -74.2 | 63.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5446 | 0.0023 | 10/10 | k=2: 4641.091 Hz, -113.2 dB | -109.5 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0361 | 0.0014 | 3/19 | k=1: 50.034 Hz, -97.6 dB | -100.1 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0056 | 3 | k=-1·f1+3·f2: 17000.126 Hz, -116.0 dB | -111.5 | 0.0 % |
| stärkste übrige Linie (4401.90 Hz) | Kanal 4 | 4401.9006 | 0.0015 | 2/5 | k=1: 4401.900 Hz, -93.9 dB | -96.9 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0011 | 4/7 | k=1: 2999.999 Hz, -98.7 dB | -99.3 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.1 | 55.0 | usb1k·1 |
| 1999.735 | -81.2 | 48.5 | usb1k·2 |
| 2999.603 | -82.5 | 48.5 | usb1k·3 |
| 6000.000 | -83.9 | 49.4 | fs8·1 |
| 12000.000 | -85.1 | 49.1 | fs8·2 |
| 18000.000 | -85.5 | 50.0 | fs8·3 |
| 3999.471 | -87.0 | 44.9 | usb1k·4 |
| 9998.676 | -88.3 | 44.1 | usb1k·10 |
| 4999.338 | -89.6 | 40.7 | usb1k·5 |
| 6999.073 | -90.6 | 43.1 | usb1k·7 |
| 15997.881 | -90.2 | 44.5 | usb1k·16 |
| 8998.809 | -91.1 | 42.9 | usb1k·9 |
| 4401.900 | -91.9 | 40.7 | other1·1 |
| 5999.206 | -93.7 | 39.6 | usb1k·6 |
| 16997.749 | -92.7 | 41.5 | usb1k·17 |
| 18997.483 | -93.4 | 41.7 | usb1k·19 |
| 7998.941 | -94.9 | 38.2 | usb1k·8 |
| 20997.219 | -94.2 | 39.2 | usb1k·21 |
| 11998.411 | -96.1 | 38.3 | usb1k·12 |
| 50.033 | -96.8 | 21.3 | mains50·1 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 55.1 | usb1k·1 |
| 1999.735 | -82.9 | 48.3 | usb1k·2 |
| 2999.603 | -83.3 | 49.0 | usb1k·3 |
| 6000.000 | -84.0 | 50.3 | fs8·1 |
| 12000.000 | -85.4 | 50.0 | fs8·2 |
| 18000.000 | -85.6 | 50.7 | fs8·3 |
| 3999.471 | -87.5 | 45.1 | usb1k·4 |
| 9998.676 | -88.4 | 46.1 | usb1k·10 |
| 4999.338 | -90.6 | 41.5 | usb1k·5 |
| 6999.073 | -91.4 | 43.4 | usb1k·7 |
| 15997.881 | -90.7 | 44.7 | usb1k·16 |
| 8998.809 | -92.0 | 42.8 | usb1k·9 |
| 4401.900 | -93.7 | 40.5 | other1·1 |
| 16997.749 | -93.1 | 42.5 | usb1k·17 |
| 18997.484 | -93.4 | 43.2 | usb1k·19 |
| 5999.206 | -95.1 | 39.1 | usb1k·6 |
| 20997.219 | -94.9 | 40.5 | usb1k·21 |
| 7998.941 | -96.2 | 38.3 | usb1k·8 |
| 11998.411 | -96.6 | 39.0 | usb1k·12 |
| 50.034 | -97.4 | 23.0 | mains50·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 59.5 | usb1k·1 |
| 1999.735 | -82.7 | 53.4 | usb1k·2 |
| 2999.603 | -84.0 | 53.5 | usb1k·3 |
| 6000.000 | -84.5 | 53.8 | fs8·1 |
| 18000.000 | -85.9 | 53.2 | fs8·3 |
| 12000.000 | -86.3 | 52.9 | fs8·2 |
| 3999.471 | -87.8 | 49.7 | usb1k·4 |
| 9998.676 | -88.9 | 48.7 | usb1k·10 |
| 4999.338 | -90.8 | 46.4 | usb1k·5 |
| 15997.881 | -90.8 | 47.8 | usb1k·16 |
| 6999.073 | -91.9 | 46.6 | usb1k·7 |
| 8998.809 | -91.9 | 46.7 | usb1k·9 |
| 16997.749 | -93.5 | 44.8 | usb1k·17 |
| 18997.484 | -93.7 | 45.2 | usb1k·19 |
| 5999.206 | -95.9 | 42.6 | usb1k·6 |
| 20997.219 | -95.1 | 42.8 | usb1k·21 |
| 7998.941 | -96.2 | 42.2 | usb1k·8 |
| 4401.900 | -97.4 | 40.8 | other1·1 |
| 11998.411 | -96.7 | 42.5 | usb1k·12 |
| 12998.278 | -97.4 | 41.5 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.7 | 56.3 | usb1k·1 |
| 1999.735 | -81.3 | 49.1 | usb1k·2 |
| 2999.603 | -82.3 | 49.6 | usb1k·3 |
| 6000.000 | -84.0 | 49.7 | fs8·1 |
| 12000.000 | -85.6 | 49.0 | fs8·2 |
| 18000.000 | -85.8 | 49.9 | fs8·3 |
| 3999.471 | -87.0 | 45.0 | usb1k·4 |
| 9998.676 | -88.3 | 45.3 | usb1k·10 |
| 4999.338 | -89.5 | 42.2 | usb1k·5 |
| 6999.073 | -90.6 | 43.5 | usb1k·7 |
| 15997.881 | -90.3 | 44.9 | usb1k·16 |
| 8998.809 | -91.3 | 42.9 | usb1k·9 |
| 5999.206 | -93.2 | 40.6 | usb1k·6 |
| 4401.900 | -93.9 | 39.7 | other1·1 |
| 16997.749 | -92.7 | 41.8 | usb1k·17 |
| 7998.941 | -94.3 | 39.2 | usb1k·8 |
| 18997.484 | -93.8 | 42.2 | usb1k·19 |
| 20997.219 | -94.3 | 40.2 | usb1k·21 |
| 11998.411 | -96.1 | 38.5 | usb1k·12 |
| 50.034 | -97.6 | 23.3 | mains50·1 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 5/5 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 1 | 5/5 | 0.23 | -0.88 | 0.02 |
| led | Kanal 1 | 5/5 | 0.88 | 4.98 | 0.25 |
| mains50 | Kanal 1 | 5/5 | 1075.42 | 7026.67 | 0.77 |
| other1 | Kanal 1 | 5/5 | 1.44 | 8.57 | 0.11 |
| other2 | Kanal 1 | 5/5 | 0.22 | 0.28 | 0.19 |
| fs8 | Kanal 2 | 5/5 | 0.01 | 0.04 | 0.01 |
| usb1k | Kanal 2 | 5/5 | 0.24 | -0.90 | 0.02 |
| led | Kanal 2 | 5/5 | 0.37 | -0.72 | 0.37 |
| mains50 | Kanal 2 | 5/5 | 214.21 | -22.05 | 0.76 |
| other1 | Kanal 2 | 5/5 | 1.48 | 7.50 | 0.12 |
| other2 | Kanal 2 | 5/5 | 0.31 | -0.91 | 0.16 |
| fs8 | Kanal 3 | 5/5 | 0.02 | 0.02 | 0.01 |
| usb1k | Kanal 3 | 5/5 | 0.23 | -0.91 | 0.02 |
| led | Kanal 3 | 5/5 | 0.47 | 0.11 | 0.11 |
| mains50 | Kanal 3 | 5/5 | 118.04 | 78.20 | 0.27 |
| other1 | Kanal 3 | 5/5 | 0.68 | 4.81 | 0.13 |
| other2 | Kanal 3 | 5/5 | 0.22 | -0.71 | 0.14 |
| fs8 | Kanal 4 | 5/5 | 0.01 | 0.06 | 0.01 |
| usb1k | Kanal 4 | 5/5 | 0.18 | -0.55 | 0.03 |
| led | Kanal 4 | 5/5 | 0.82 | -1.10 | 0.22 |
| mains50 | Kanal 4 | 5/5 | 303.07 | 1324.31 | 0.94 |
| other1 | Kanal 4 | 5/5 | 1.06 | 7.04 | 0.13 |
| other2 | Kanal 4 | 5/5 | 0.15 | -0.37 | 0.20 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.63 | 7.50 s (0.13 Hz) | 15.8 |
| Kanal 1 | 999.9 Hz ± 10 | 1.24 | 7.50 s (0.13 Hz) | 34.2 |
| Kanal 2 | breitbandig | 0.61 | 7.50 s (0.13 Hz) | 16.7 |
| Kanal 2 | 999.9 Hz ± 10 | 1.25 | 7.50 s (0.13 Hz) | 35.1 |
| Kanal 3 | breitbandig | 0.40 | 7.50 s (0.13 Hz) | 23.3 |
| Kanal 3 | 999.9 Hz ± 10 | 1.23 | 7.50 s (0.13 Hz) | 39.3 |
| Kanal 4 | breitbandig | 0.49 | 7.50 s (0.13 Hz) | 16.3 |
| Kanal 4 | 999.9 Hz ± 10 | 1.23 | 7.50 s (0.13 Hz) | 33.6 |

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
| Kanal 1 | 1.00 | 0.96 | 0.93 | 0.95 |
| Kanal 2 | 0.96 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.93 | 0.93 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B6b-fx4b-end-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.9 | -71.9 | -0.0 | 65 % | 66 % |
| Kanal 2 | -73.1 | -73.0 | -0.1 | 68 % | 69 % |
| Kanal 3 | -74.3 | -74.4 | +0.1 | 82 % | 82 % |
| Kanal 4 | -72.2 | -72.0 | -0.2 | 71 % | 73 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-osc-detuned_psd.png)

### Kammprofile

![Kammprofile](B6b-osc-detuned_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-osc-detuned_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:21:31. Stream-Meldungen: 0. owl_read: out/owl_read/B6b-osc-detuned (rc 0).
