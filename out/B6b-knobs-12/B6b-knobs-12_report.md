# Report B6b-knobs-12: B6b-knobs-12 – acdc1 fx4b-open-inputs-knobs-12, 30 s

| Feld | Wert |
|---|---|
| date | 2026-11-17 |
| device | acdc1, Firmware Build 6b v22.4.r-fx4b |
| test | Wie B6b-osc-detuned, aber alle vier Regler auf 12 Uhr (Nutzer): Test, ob die Linien 2200,95 / 4401,90 / 6602,85 Hz an der Reglerstellung hängen |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) |
| patch | laufender Patch siehe owl_read |
| Datei(en) | `20261117_acdc1_fx4b-open-inputs-knobs-12_g12_usb-stream.wav` |
| Format | 48000 Hz, 30.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B6b-knobs-12 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref B6b-osc-detuned --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -72.0 | -82.2 | -72.5 | -73.2 | -85.9 | -72.8 | -94.9 | -72.5 | 65 % | -77.0 | 4.5 |
| Kanal 2 | -7.4 | -73.0 | -83.6 | -73.4 | -74.1 | -88.1 | -73.7 | -95.0 | -73.4 | 69 % | -78.5 | 5.1 |
| Kanal 3 | -5.6 | -74.6 | -87.8 | -74.8 | -75.3 | -92.3 | -75.0 | -93.8 | -74.8 | 82 % | -82.2 | 7.4 |
| Kanal 4 | -6.5 | -72.2 | -83.4 | -72.6 | -73.1 | -88.3 | -72.8 | -95.4 | -72.6 | 73 % | -78.3 | 5.7 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -82.9 dB | -82.9 | 9.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.8 dB | -75.1 | 55.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0018 | 10/10 | k=2: 4641.093 Hz, -113.9 dB | -109.0 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0305 | 0.0014 | 2/19 | k=1: 50.032 Hz, -97.5 dB | -100.2 | 0.2 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0015 | 5 | k=1·f1+1·f2: 6999.868 Hz, -115.5 dB | -109.0 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -98.4 dB | -96.9 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0004 | 0.0005 | 4/7 | k=1: 3000.001 Hz, -98.5 dB | -99.1 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.0 dB | -83.0 | 11.1 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.7 dB | -75.8 | 57.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5449 | 0.0014 | 10/10 | k=9: 20884.905 Hz, -113.1 dB | -107.7 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0301 | 0.0019 | 2/19 | k=1: 50.032 Hz, -98.1 dB | -100.8 | 0.2 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0038 | 8 | k=1·f1+1·f2: 6999.867 Hz, -115.6 dB | -108.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -98.8 dB | -97.1 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0007 | 4/7 | k=1: 3000.001 Hz, -99.0 dB | -99.3 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.4 dB | -83.6 | 13.2 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -76.5 | 68.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0015 | 10/10 | k=1: 2320.544 Hz, -114.2 dB | -109.6 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0270 | 0.0026 | 5/19 | k=1: 50.029 Hz, -99.2 dB | -101.8 | 0.2 % |
| Mischprodukte n·999.8675 + m·5999.9999 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0030 | 19 | k=1·f1+1·f2: 6999.870 Hz, -117.1 dB | -111.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0004 | 8/11 | k=1: 2000.000 Hz, -100.1 dB | -97.7 | 0.5 % |
| stärkste übrige Linie (1000.00 Hz) | Kanal 3 | 1000.0001 | 0.0007 | 12/23 | k=1: 1000.000 Hz, -100.4 dB | -96.1 | 0.7 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -83.2 | 8.7 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.3 dB | -74.5 | 63.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5449 | 0.0017 | 10/10 | k=2: 4641.093 Hz, -113.2 dB | -108.7 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0301 | 0.0020 | 2/19 | k=1: 50.032 Hz, -98.6 dB | -101.3 | 0.1 % |
| Mischprodukte n·999.8675 + m·5999.9999 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0054 | 8 | k=1·f1+1·f2: 6999.869 Hz, -113.1 dB | -106.8 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0005 | 8/11 | k=1: 2000.000 Hz, -99.1 dB | -97.3 | 0.3 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0004 | 0.0006 | 4/7 | k=1: 3000.001 Hz, -99.4 dB | -99.7 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.8 | 55.2 | usb1k·1 |
| 1999.735 | -81.6 | 48.4 | usb1k·2 |
| 6000.000 | -82.9 | 50.3 | fs8·1 |
| 2999.603 | -83.2 | 47.6 | usb1k·3 |
| 12000.000 | -85.1 | 49.5 | fs8·2 |
| 18000.000 | -86.9 | 48.9 | fs8·3 |
| 3999.470 | -87.7 | 45.1 | usb1k·4 |
| 9998.676 | -88.6 | 45.8 | usb1k·10 |
| 4999.337 | -90.3 | 42.2 | usb1k·5 |
| 6999.073 | -91.1 | 42.7 | usb1k·7 |
| 15997.880 | -90.5 | 40.2 | usb1k·16 |
| 8998.808 | -91.8 | 42.5 | usb1k·9 |
| 16997.748 | -93.4 | 41.2 | usb1k·17 |
| 18997.483 | -93.6 | 40.8 | usb1k·19 |
| 20997.218 | -94.3 | 39.8 | usb1k·21 |
| 5999.205 | -96.2 | 37.1 | usb1k·6 |
| 7998.941 | -96.2 | 36.8 | usb1k·8 |
| 13998.146 | -96.5 | 38.8 | usb1k·14 |
| 50.032 | -97.5 | 22.1 | mains50·1 |
| 11998.411 | -96.9 | 37.8 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 56.2 | usb1k·1 |
| 1999.735 | -82.5 | 49.0 | usb1k·2 |
| 6000.000 | -83.0 | 52.1 | fs8·1 |
| 2999.603 | -83.8 | 48.7 | usb1k·3 |
| 12000.000 | -85.4 | 50.9 | fs8·2 |
| 18000.000 | -86.9 | 49.8 | fs8·3 |
| 3999.470 | -87.9 | 46.3 | usb1k·4 |
| 9998.676 | -88.7 | 47.6 | usb1k·10 |
| 4999.337 | -90.9 | 43.3 | usb1k·5 |
| 6999.073 | -91.6 | 43.1 | usb1k·7 |
| 15997.880 | -90.7 | 42.4 | usb1k·16 |
| 8998.808 | -92.1 | 43.3 | usb1k·9 |
| 16997.748 | -93.6 | 41.9 | usb1k·17 |
| 18997.483 | -93.5 | 42.2 | usb1k·19 |
| 20997.218 | -94.7 | 41.1 | usb1k·21 |
| 7998.941 | -97.1 | 37.5 | usb1k·8 |
| 5999.205 | -97.4 | 37.6 | usb1k·6 |
| 11998.411 | -97.1 | 39.1 | usb1k·12 |
| 50.032 | -98.1 | 23.4 | mains50·1 |
| 12998.278 | -97.5 | 39.5 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 59.6 | usb1k·1 |
| 6000.000 | -83.4 | 55.0 | fs8·1 |
| 1999.735 | -83.6 | 53.2 | usb1k·2 |
| 2999.603 | -84.4 | 52.9 | usb1k·3 |
| 12000.000 | -86.2 | 52.8 | fs8·2 |
| 18000.000 | -87.4 | 51.5 | fs8·3 |
| 3999.470 | -88.4 | 49.4 | usb1k·4 |
| 9998.676 | -89.1 | 50.2 | usb1k·10 |
| 4999.337 | -91.4 | 46.2 | usb1k·5 |
| 15997.880 | -91.2 | 45.2 | usb1k·16 |
| 6999.073 | -92.4 | 46.9 | usb1k·7 |
| 8998.808 | -92.9 | 46.2 | usb1k·9 |
| 16997.748 | -93.9 | 44.6 | usb1k·17 |
| 18997.483 | -93.9 | 43.9 | usb1k·19 |
| 20997.218 | -95.4 | 42.8 | usb1k·21 |
| 7998.941 | -97.1 | 40.6 | usb1k·8 |
| 11998.411 | -97.2 | 42.0 | usb1k·12 |
| 5999.206 | -98.2 | 40.3 | usb1k·6 |
| 12998.278 | -97.8 | 41.3 | usb1k·13 |
| 50.029 | -99.2 | 27.4 | mains50·1 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.3 | 57.4 | usb1k·1 |
| 1999.735 | -80.4 | 50.9 | usb1k·2 |
| 2999.603 | -83.1 | 49.1 | usb1k·3 |
| 6000.000 | -83.2 | 51.5 | fs8·1 |
| 12000.000 | -85.6 | 49.4 | fs8·2 |
| 18000.000 | -87.0 | 48.7 | fs8·3 |
| 3999.470 | -87.4 | 46.1 | usb1k·4 |
| 9998.676 | -89.0 | 46.8 | usb1k·10 |
| 4999.337 | -89.5 | 43.8 | usb1k·5 |
| 6999.073 | -90.7 | 43.4 | usb1k·7 |
| 15997.880 | -90.1 | 42.6 | usb1k·16 |
| 8998.808 | -91.1 | 43.8 | usb1k·9 |
| 16997.748 | -93.5 | 41.8 | usb1k·17 |
| 5999.205 | -94.9 | 39.8 | usb1k·6 |
| 18997.483 | -93.8 | 41.7 | usb1k·19 |
| 20997.218 | -94.0 | 41.3 | usb1k·21 |
| 7998.941 | -95.3 | 38.9 | usb1k·8 |
| 13998.145 | -95.6 | 40.2 | usb1k·14 |
| 11998.411 | -96.4 | 38.7 | usb1k·12 |
| 12998.278 | -97.4 | 39.0 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 5/5 | 0.02 | -0.08 | 0.02 |
| usb1k | Kanal 1 | 5/5 | 0.21 | 0.95 | 0.03 |
| led | Kanal 1 | 5/5 | 1.61 | -8.83 | 0.38 |
| mains50 | Kanal 1 | 5/5 | 968.59 | 236.51 | 0.99 |
| other1 | Kanal 1 | 5/5 | 0.40 | 0.80 | 0.03 |
| other2 | Kanal 1 | 5/5 | 0.17 | 0.46 | 0.10 |
| fs8 | Kanal 2 | 5/5 | 0.01 | -0.02 | 0.02 |
| usb1k | Kanal 2 | 5/5 | 0.20 | 0.90 | 0.04 |
| led | Kanal 2 | 5/5 | 0.35 | -1.62 | 0.18 |
| mains50 | Kanal 2 | 5/5 | 971.09 | -161.78 | 1.05 |
| other1 | Kanal 2 | 5/5 | 0.38 | 0.62 | 0.03 |
| other2 | Kanal 2 | 5/5 | 0.12 | -0.07 | 0.06 |
| fs8 | Kanal 3 | 5/5 | 0.01 | -0.05 | 0.03 |
| usb1k | Kanal 3 | 5/5 | 0.21 | 0.96 | 0.04 |
| led | Kanal 3 | 5/5 | 1.01 | -1.60 | 0.29 |
| mains50 | Kanal 3 | 5/5 | 117.62 | 64.35 | 0.54 |
| other1 | Kanal 3 | 5/5 | 0.29 | -0.56 | 0.04 |
| other2 | Kanal 3 | 5/5 | 0.81 | -2.09 | 0.05 |
| fs8 | Kanal 4 | 5/5 | 0.03 | -0.13 | 0.02 |
| usb1k | Kanal 4 | 5/5 | 0.16 | 0.61 | 0.03 |
| led | Kanal 4 | 5/5 | 0.58 | -2.03 | 0.47 |
| mains50 | Kanal 4 | 5/5 | 956.29 | 276.16 | 1.20 |
| other1 | Kanal 4 | 5/5 | 0.47 | 1.75 | 0.05 |
| other2 | Kanal 4 | 5/5 | 0.18 | -0.27 | 0.09 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.66 | 7.50 s (0.13 Hz) | 16.2 |
| Kanal 1 | 999.9 Hz ± 10 | 1.25 | 7.50 s (0.13 Hz) | 35.0 |
| Kanal 2 | breitbandig | 0.60 | 7.50 s (0.13 Hz) | 17.3 |
| Kanal 2 | 999.9 Hz ± 10 | 1.26 | 7.50 s (0.13 Hz) | 37.1 |
| Kanal 3 | breitbandig | 0.41 | 7.50 s (0.13 Hz) | 25.5 |
| Kanal 3 | 999.9 Hz ± 10 | 1.25 | 7.50 s (0.13 Hz) | 41.0 |
| Kanal 4 | breitbandig | 0.53 | 7.50 s (0.13 Hz) | 18.0 |
| Kanal 4 | 999.9 Hz ± 10 | 1.24 | 7.50 s (0.13 Hz) | 35.9 |

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
| Kanal 1 | 1.00 | 0.96 | 0.92 | 0.94 |
| Kanal 2 | 0.96 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.92 | 0.93 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.96 | 0.92 | 1.00 |

## Vergleich mit Referenz B6b-osc-detuned

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.5 | -71.9 | -0.5 | 65 % | 65 % |
| Kanal 2 | -73.4 | -73.1 | -0.3 | 69 % | 68 % |
| Kanal 3 | -74.8 | -74.3 | -0.5 | 82 % | 82 % |
| Kanal 4 | -72.6 | -72.2 | -0.4 | 73 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B6b-knobs-12_psd.png)

### Kammprofile

![Kammprofile](B6b-knobs-12_combs.png)

### Zeitverlauf

![Zeitverlauf](B6b-knobs-12_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 23:24:36. Stream-Meldungen: 0. owl_read: out/owl_read/B6b-knobs-12 (rc 0).
