# Report B3-fx2b-r2: B3-fx2b-r2 – acdc1 Build 3b, rohe Eingänge offen, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 3b v22.4.r-fx2b (Build 2 + Patch 07 v2, Eingangs-LEDs roh bei TX) |
| test | A/B gegen B3 2/2: wie r1, nach Neustart der Host-Software |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx2b-open-inputs-r2_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 59.8 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx2b-r2 --ref B3-fx1d-r2 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -70.6 | -80.3 | -71.1 | -72.2 | -85.5 | -71.4 | -99.5 | -71.1 | 69 % | -76.2 | 5.1 |
| Kanal 2 | -6.9 | -71.4 | -81.2 | -71.9 | -73.0 | -87.6 | -72.2 | -102.0 | -71.9 | 75 % | -78.0 | 6.1 |
| Kanal 3 | -5.1 | -73.0 | -86.2 | -73.2 | -74.3 | -91.3 | -73.4 | -102.4 | -73.2 | 86 % | -81.6 | 8.4 |
| Kanal 4 | -6.0 | -70.8 | -81.5 | -71.2 | -72.1 | -87.9 | -71.4 | -102.2 | -71.2 | 76 % | -77.3 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.8 dB | -77.6 | 22.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -72.7 dB | -74.5 | 45.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.546 Hz, -117.1 dB | -114.0 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9939 | 0.0002 | 2/19 | k=1: 49.994 Hz, -94.0 dB | -96.0 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0009 | 122 | k=8·f1+2·f2: 19998.941 Hz, -99.8 dB | -89.6 | 1.4 % |
| stärkste übrige Linie (51.19 Hz) | Kanal 1 | 51.1849 | 0.0013 | 5/466 | k=1: 51.188 Hz, -100.3 dB | -100.9 | 0.1 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 1 | 21000.0008 | 0.0000 | 1/1 | k=1: 21000.001 Hz, -102.1 dB | -105.1 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.8 dB | -77.6 | 27.3 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -75.3 | 45.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0014 | 10/10 | k=9: 20884.904 Hz, -114.0 dB | -110.6 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9938 | 0.0003 | 2/19 | k=1: 49.994 Hz, -94.6 dB | -96.6 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0012 | 136 | k=8·f1+2·f2: 19998.941 Hz, -99.8 dB | -89.4 | 1.8 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 2 | 21000.0008 | 0.0000 | 1/1 | k=1: 21000.001 Hz, -102.0 dB | -105.0 | 0.0 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 2 | 23000.9277 | 0.0000 | 1/1 | k=1: 23000.928 Hz, -102.1 dB | -105.1 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -77.8 | 34.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0003 | 22/23 | k=1: 999.868 Hz, -74.7 dB | -76.4 | 48.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.546 Hz, -118.1 dB | -114.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9944 | 0.0026 | 3/19 | k=1: 49.993 Hz, -95.6 dB | -97.4 | 0.4 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0011 | 149 | k=8·f1+2·f2: 19998.941 Hz, -99.8 dB | -89.7 | 2.3 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 3 | 21000.0010 | 0.0000 | 1/1 | k=1: 21000.001 Hz, -102.2 dB | -105.1 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9278 | 0.0000 | 1/1 | k=1: 23000.928 Hz, -102.6 dB | -105.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0001 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.1 dB | -77.8 | 22.0 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -74.0 | 52.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0009 | 10/10 | k=1: 2320.546 Hz, -116.5 dB | -112.6 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9936 | 0.0006 | 2/19 | k=1: 49.994 Hz, -95.2 dB | -97.1 | 0.3 % |
| Mischprodukte n·999.8675 + m·6000.0001 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0011 | 130 | k=8·f1+2·f2: 19998.941 Hz, -100.3 dB | -89.6 | 1.5 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 4 | 23000.9276 | 0.0000 | 1/1 | k=1: 23000.928 Hz, -102.1 dB | -105.2 | 0.0 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 4 | 21000.0009 | 0.0000 | 1/1 | k=1: 21000.001 Hz, -102.2 dB | -105.2 | 0.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.7 | 58.7 | usb1k·1 |
| 6000.000 | -77.8 | 57.4 | fs8·1 |
| 12000.000 | -80.3 | 56.1 | fs8·2 |
| 18000.000 | -80.7 | 55.7 | fs8·3 |
| 1999.735 | -83.3 | 49.2 | usb1k·2 |
| 3999.470 | -83.8 | 50.6 | usb1k·4 |
| 4999.338 | -85.8 | 48.3 | usb1k·5 |
| 7998.941 | -87.6 | 47.8 | usb1k·8 |
| 2999.603 | -89.0 | 45.0 | usb1k·3 |
| 11998.410 | -91.0 | 45.3 | usb1k·12 |
| 15997.880 | -90.1 | 46.2 | usb1k·16 |
| 18997.483 | -92.2 | 44.2 | usb1k·19 |
| 8998.807 | -92.0 | 43.3 | usb1k·9 |
| 49.994 | -94.0 | 27.8 | mains50·1 |
| 16997.748 | -95.2 | 41.2 | usb1k·17 |
| 10998.543 | -94.0 | 41.5 | usb1k·11 |
| 22996.953 | -94.0 | 44.4 | usb1k·23 |
| 9998.675 | -96.3 | 39.4 | usb1k·10 |
| 19997.351 | -98.0 | 38.5 | usb1k·20 |
| 14998.013 | -98.5 | 37.8 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 59.6 | usb1k·1 |
| 6000.000 | -77.8 | 59.4 | fs8·1 |
| 12000.000 | -80.1 | 58.1 | fs8·2 |
| 18000.000 | -80.6 | 57.4 | fs8·3 |
| 1999.735 | -84.2 | 50.1 | usb1k·2 |
| 3999.470 | -84.0 | 51.7 | usb1k·4 |
| 4999.338 | -86.3 | 49.0 | usb1k·5 |
| 7998.941 | -88.0 | 49.3 | usb1k·8 |
| 2999.603 | -90.3 | 45.0 | usb1k·3 |
| 15997.880 | -90.2 | 47.8 | usb1k·16 |
| 11998.410 | -91.2 | 46.9 | usb1k·12 |
| 18997.483 | -92.1 | 45.8 | usb1k·19 |
| 8998.807 | -92.0 | 44.8 | usb1k·9 |
| 10998.543 | -93.5 | 43.6 | usb1k·11 |
| 49.994 | -94.6 | 29.5 | mains50·1 |
| 22996.953 | -94.0 | 46.1 | usb1k·23 |
| 16997.748 | -95.7 | 42.0 | usb1k·17 |
| 9998.676 | -96.6 | 40.8 | usb1k·10 |
| 19997.351 | -98.1 | 39.8 | usb1k·20 |
| 14998.014 | -98.7 | 39.5 | usb1k·15 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.7 | 62.6 | usb1k·1 |
| 6000.000 | -78.0 | 62.2 | fs8·1 |
| 12000.000 | -80.3 | 60.9 | fs8·2 |
| 18000.000 | -80.9 | 59.6 | fs8·3 |
| 3999.470 | -84.6 | 55.1 | usb1k·4 |
| 1999.735 | -86.0 | 52.5 | usb1k·2 |
| 4999.338 | -87.4 | 52.2 | usb1k·5 |
| 7998.941 | -88.5 | 51.5 | usb1k·8 |
| 11998.410 | -91.6 | 49.5 | usb1k·12 |
| 15997.880 | -90.7 | 50.4 | usb1k·16 |
| 2999.603 | -91.6 | 47.9 | usb1k·3 |
| 18997.483 | -92.3 | 48.4 | usb1k·19 |
| 8998.808 | -92.8 | 47.4 | usb1k·9 |
| 10998.543 | -93.4 | 47.4 | usb1k·11 |
| 22996.953 | -94.4 | 47.9 | usb1k·23 |
| 49.993 | -95.6 | 32.7 | mains50·1 |
| 16997.748 | -96.1 | 44.6 | usb1k·17 |
| 9998.676 | -96.9 | 43.5 | usb1k·10 |
| 19997.351 | -98.4 | 42.3 | usb1k·20 |
| 14998.013 | -98.8 | 41.8 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 60.6 | usb1k·1 |
| 6000.000 | -78.1 | 58.1 | fs8·1 |
| 12000.000 | -80.2 | 56.5 | fs8·2 |
| 18000.000 | -80.8 | 55.8 | fs8·3 |
| 1999.735 | -81.4 | 52.4 | usb1k·2 |
| 3999.470 | -83.8 | 51.1 | usb1k·4 |
| 4999.338 | -84.8 | 49.6 | usb1k·5 |
| 7998.941 | -87.4 | 49.1 | usb1k·8 |
| 2999.603 | -88.5 | 46.1 | usb1k·3 |
| 15997.880 | -89.6 | 47.0 | usb1k·16 |
| 11998.410 | -90.6 | 46.0 | usb1k·12 |
| 8998.807 | -90.8 | 45.0 | usb1k·9 |
| 18997.483 | -92.1 | 44.7 | usb1k·19 |
| 22996.953 | -93.7 | 45.0 | usb1k·23 |
| 16997.748 | -95.2 | 41.4 | usb1k·17 |
| 10998.543 | -94.2 | 42.5 | usb1k·11 |
| 49.994 | -95.2 | 29.0 | mains50·1 |
| 9998.675 | -96.1 | 40.1 | usb1k·10 |
| 12998.278 | -96.4 | 40.0 | usb1k·13 |
| 19997.351 | -97.3 | 39.5 | usb1k·20 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 10/10 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 10/10 | 0.09 | 0.06 | 0.04 |
| led | Kanal 1 | 10/10 | 3.65 | -0.83 | 1.48 |
| mains50 | Kanal 1 | 10/10 | 356.40 | -401.89 | 1.05 |
| other1 | Kanal 1 | 10/10 | 3.50 | 0.38 | 2.77 |
| other2 | Kanal 1 | 10/10 | 0.16 | 0.08 | 1.91 |
| fs8 | Kanal 2 | 10/10 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 2 | 10/10 | 0.08 | 0.07 | 0.03 |
| led | Kanal 2 | 10/10 | 0.23 | -0.04 | 0.47 |
| mains50 | Kanal 2 | 10/10 | 264.95 | -332.18 | 0.82 |
| other1 | Kanal 2 | 10/10 | 0.12 | 0.05 | 1.90 |
| other2 | Kanal 2 | 10/10 | 0.13 | 0.24 | 0.14 |
| fs8 | Kanal 3 | 10/10 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 10/10 | 0.06 | 0.05 | 0.04 |
| led | Kanal 3 | 10/10 | 0.97 | -0.30 | 0.68 |
| mains50 | Kanal 3 | 10/10 | 214.45 | -364.02 | 0.49 |
| other1 | Kanal 3 | 10/10 | 0.10 | 0.10 | 1.79 |
| other2 | Kanal 3 | 10/10 | 0.14 | 0.18 | 0.19 |
| fs8 | Kanal 4 | 10/10 | 0.02 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 10/10 | 0.08 | -0.00 | 0.04 |
| led | Kanal 4 | 10/10 | 1.13 | 0.10 | 0.85 |
| mains50 | Kanal 4 | 10/10 | 248.03 | -335.84 | 0.92 |
| other1 | Kanal 4 | 10/10 | 0.12 | 0.16 | 0.09 |
| other2 | Kanal 4 | 10/10 | 0.15 | 0.03 | 1.85 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.62 | 0.63 s (1.59 Hz) | 20.4 |
| Kanal 1 | 999.9 Hz ± 10 | 0.85 | 1.27 s (0.79 Hz) | 26.0 |
| Kanal 2 | breitbandig | 0.60 | 0.63 s (1.59 Hz) | 22.1 |
| Kanal 2 | 999.9 Hz ± 10 | 0.84 | 1.27 s (0.79 Hz) | 28.3 |
| Kanal 3 | breitbandig | 0.36 | 0.63 s (1.59 Hz) | 29.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.83 | 1.27 s (0.79 Hz) | 31.3 |
| Kanal 4 | breitbandig | 0.51 | 0.63 s (1.59 Hz) | 22.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.83 | 1.27 s (0.79 Hz) | 28.3 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.96 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.98 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.94 |
| Kanal 4 | 0.96 | 0.98 | 0.94 | 1.00 |

## Vergleich mit Referenz B3-fx1d-r2

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.8 | +0.7 | 69 % | 63 % |
| Kanal 2 | -71.9 | -72.6 | +0.7 | 75 % | 70 % |
| Kanal 3 | -73.2 | -74.2 | +1.0 | 86 % | 80 % |
| Kanal 4 | -71.2 | -71.8 | +0.6 | 76 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx2b-r2_psd.png)

### Kammprofile

![Kammprofile](B3-fx2b-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx2b-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 17:43–17:44, Host-Software vorher neu gestartet.
