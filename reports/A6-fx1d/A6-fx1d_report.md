# Report A6-fx1d: A6-fx1d – acdc1 Build 2, Rückführung, 4 Sinustöne, 10 min

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 2 v22.4.r-fx1d (Build 1d + TX_PRE_FX) |
| test | Abnahme A6: Rückführung Out n → In n, Host-Sinus 440/530/670/790 Hz, 10 min (wie A6L-b1d, aber 10 statt 30 min) |
| gain | g12 |
| usb | usb-rxtx, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX |
| patch | Slot 1: ACDC (Default-Patch); Ausgänge = USB-Playback (RX POST_FX), Aufnahme = rohe Eingänge (TX PRE_FX) |
| Datei(en) | `20261115_acdc1_fx1d-loop-10min_g12_usb-rxtx.4chan.000.wav` |
| Format | 48000 Hz, 600.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis A6-fx1d --no-spectrogram` |

**Hinweise:**

- Clipping: Samples an der Vollaussteuerung.
- Ein Nutzsignal (übrige Linien) dominiert. Störanteil und Notch-Gewinn sind dann nicht aussagekräftig, Störlinien in absoluten dBFS vergleichen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -2.8 | – | -2.8 | -6.9 | -83.1 | -2.8 | -2.8 | -43.1 | 1 % | -43.1 | 0.0 |
| Kanal 2 | -6.9 | -2.8 | – | -2.8 | -5.6 | -84.4 | -2.8 | -2.8 | -44.8 | 1 % | -44.9 | 0.1 |
| Kanal 3 | -4.8 | -2.8 | – | -2.8 | -4.4 | -85.1 | -2.8 | -2.8 | -47.5 | 2 % | -47.6 | 0.1 |
| Kanal 4 | -6.2 | -2.8 | – | -2.8 | -3.6 | -83.5 | -2.8 | -2.8 | -47.5 | 2 % | -47.6 | 0.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.4 dB | -78.5 | 0.0 % |
| 1-kHz-Kamm | Kanal 1 | 999.8675 | 0.0000 | 23/23 | k=1: 999.867 Hz, -72.9 dB | -74.3 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -64.1 dB | -63.7 | 0.9 % |
| Netz 50 Hz | Kanal 1 | 50.0177 | 0.0020 | 6/19 | k=1: 50.018 Hz, -99.9 dB | -99.7 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8675 | 0.0001 | 178 | k=8·f1+1·f2: 13998.940 Hz, -94.7 dB | -85.0 | 0.0 % |
| stärkste übrige Linie (440.00 Hz) | Kanal 1 | 439.9998 | 0.0000 | 54/54 | k=1: 440.000 Hz, 0.5 dB | -2.8 | 100.0 % |
| stärkste übrige Linie (530.00 Hz) | Kanal 1 | 530.0017 | 0.0000 | 45/45 | k=1: 530.002 Hz, -80.7 dB | -81.2 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.7 dB | -77.8 | 0.0 % |
| 1-kHz-Kamm | Kanal 2 | 999.8675 | 0.0000 | 23/23 | k=1: 999.867 Hz, -73.1 dB | -74.5 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -64.7 dB | -64.5 | 1.1 % |
| Netz 50 Hz | Kanal 2 | 50.0178 | 0.0020 | 6/19 | k=1: 50.018 Hz, -100.0 dB | -99.7 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8675 | 0.0001 | 180 | k=8·f1+1·f2: 13998.940 Hz, -94.1 dB | -84.4 | 0.0 % |
| stärkste übrige Linie (530.00 Hz) | Kanal 2 | 530.0017 | 0.0000 | 45/45 | k=1: 530.002 Hz, 0.3 dB | -2.8 | 100.0 % |
| stärkste übrige Linie (120.00 Hz) | Kanal 2 | 120.0000 | 0.0027 | 72/198 | k=1: 120.001 Hz, -87.1 dB | -88.5 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.0 dB | -78.0 | 0.1 % |
| 1-kHz-Kamm | Kanal 3 | 999.8675 | 0.0000 | 23/23 | k=1: 999.867 Hz, -74.5 dB | -75.9 | 0.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -64.9 dB | -64.6 | 2.0 % |
| Netz 50 Hz | Kanal 3 | 50.0180 | 0.0018 | 6/19 | k=1: 50.018 Hz, -100.6 dB | -100.4 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8675 | 0.0000 | 180 | k=8·f1+1·f2: 13998.940 Hz, -94.2 dB | -84.6 | 0.0 % |
| stärkste übrige Linie (670.00 Hz) | Kanal 3 | 670.0003 | 0.0000 | 35/35 | k=1: 670.000 Hz, 0.2 dB | -2.8 | 100.0 % |
| stärkste übrige Linie (790.00 Hz) | Kanal 3 | 789.9977 | 0.0000 | 30/30 | k=1: 789.998 Hz, -86.0 dB | -88.5 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.9 dB | -78.0 | 0.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8675 | 0.0000 | 23/23 | k=1: 999.867 Hz, -72.0 dB | -73.4 | 0.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0000 | 10/10 | k=1: 2320.545 Hz, -64.5 dB | -64.3 | 2.1 % |
| Netz 50 Hz | Kanal 4 | 50.0177 | 0.0023 | 7/19 | k=1: 50.018 Hz, -100.5 dB | -100.2 | 0.0 % |
| Mischprodukte n·999.8675 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8675 | 0.0001 | 180 | k=8·f1+1·f2: 13998.940 Hz, -94.2 dB | -84.5 | 0.0 % |
| stärkste übrige Linie (790.00 Hz) | Kanal 4 | 789.9977 | 0.0000 | 30/30 | k=1: 789.998 Hz, 0.3 dB | -2.8 | 100.0 % |
| stärkste übrige Linie (530.00 Hz) | Kanal 4 | 530.0017 | 0.0001 | 44/45 | k=1: 530.002 Hz, -82.1 dB | -83.2 | 0.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 440.000 | 0.5 | 140.1 | other1·1 |
| 1319.999 | -28.1 | 118.0 | other1·3 |
| 2199.999 | -41.5 | 103.2 | other1·5 |
| 3079.998 | -50.5 | 96.6 | other1·7 |
| 3959.998 | -57.1 | 89.6 | other1·9 |
| 880.000 | -58.5 | 87.9 | other1·2 |
| 4839.997 | -62.3 | 84.7 | other1·11 |
| 2320.545 | -64.1 | 81.2 | led·1 |
| 4641.090 | -66.0 | 80.7 | led·2 |
| 5719.997 | -66.7 | 80.5 | other1·13 |
| 6961.634 | -69.1 | 78.6 | led·3 |
| 6599.996 | -70.5 | 76.8 | other1·15 |
| 999.867 | -72.9 | 72.9 | usb1k·1 |
| 9282.179 | -72.1 | 75.5 | led·4 |
| 7479.996 | -74.0 | 73.7 | other1·17 |
| 11602.724 | -76.0 | 71.5 | led·5 |
| 8359.995 | -76.9 | 70.6 | other1·19 |
| 6000.000 | -78.4 | 68.5 | fs8·1 |
| 9239.995 | -79.4 | 68.0 | other1·21 |
| 1999.735 | -80.1 | 64.6 | usb1k·2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 530.002 | 0.3 | 140.8 | other1·1 |
| 1590.005 | -28.3 | 119.6 | other1·3 |
| 2650.009 | -41.5 | 107.2 | other1·5 |
| 3710.012 | -50.6 | 97.9 | other1·7 |
| 4770.015 | -56.9 | 91.8 | other1·9 |
| 1060.003 | -60.0 | 87.7 | other1·2 |
| 5830.019 | -62.4 | 86.1 | other1·11 |
| 2320.545 | -64.7 | 82.7 | led·1 |
| 4641.090 | -66.7 | 81.8 | led·2 |
| 6890.022 | -66.5 | 82.7 | other1·13 |
| 6961.634 | -70.1 | 79.2 | led·3 |
| 7950.026 | -70.7 | 78.7 | other1·15 |
| 999.867 | -73.1 | 74.9 | usb1k·1 |
| 9010.029 | -73.9 | 75.4 | other1·17 |
| 9282.179 | -73.3 | 76.1 | led·4 |
| 11602.724 | -76.8 | 72.2 | led·5 |
| 10070.033 | -77.0 | 72.5 | other1·19 |
| 6000.000 | -77.7 | 70.6 | fs8·1 |
| 11130.036 | -79.6 | 70.0 | other1·21 |
| 13923.269 | -80.3 | 69.5 | led·6 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 670.000 | 0.2 | 144.8 | other1·1 |
| 2010.001 | -28.2 | 121.7 | other1·3 |
| 3350.002 | -41.5 | 110.0 | other1·5 |
| 4690.002 | -50.6 | 100.8 | other1·7 |
| 6030.003 | -57.2 | 94.5 | other1·9 |
| 7370.003 | -62.5 | 89.3 | other1·11 |
| 2320.545 | -64.9 | 85.5 | led·1 |
| 1340.001 | -66.4 | 84.5 | other1·2 |
| 4641.090 | -66.7 | 84.6 | led·2 |
| 8710.004 | -66.7 | 85.1 | other1·13 |
| 6961.634 | -69.9 | 82.1 | led·3 |
| 10050.005 | -70.8 | 81.3 | other1·15 |
| 11390.005 | -74.3 | 77.8 | other1·17 |
| 999.867 | -74.5 | 75.7 | usb1k·1 |
| 9282.179 | -73.2 | 78.8 | led·4 |
| 11602.724 | -77.4 | 74.6 | led·5 |
| 12730.006 | -77.3 | 74.6 | other1·19 |
| 6000.000 | -78.0 | 73.5 | fs8·1 |
| 12000.000 | -80.9 | 71.2 | fs8·2 |
| 14070.006 | -79.9 | 72.3 | other1·21 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 789.998 | 0.3 | 144.3 | other1·1 |
| 2369.993 | -28.3 | 118.6 | other1·3 |
| 3949.988 | -41.7 | 106.0 | other1·5 |
| 5529.984 | -50.6 | 97.3 | other1·7 |
| 7109.979 | -57.2 | 91.2 | other1·9 |
| 1579.995 | -61.2 | 85.9 | other1·2 |
| 8689.974 | -62.6 | 85.7 | other1·11 |
| 2320.545 | -64.5 | 82.3 | led·1 |
| 4641.090 | -66.5 | 81.2 | led·2 |
| 10269.970 | -67.0 | 81.2 | other1·13 |
| 6961.634 | -69.8 | 78.4 | led·3 |
| 11849.965 | -71.0 | 77.2 | other1·15 |
| 999.867 | -72.0 | 75.3 | usb1k·1 |
| 9282.179 | -73.2 | 75.3 | led·4 |
| 13429.960 | -74.4 | 74.2 | other1·17 |
| 11602.724 | -77.2 | 70.9 | led·5 |
| 15009.956 | -77.6 | 71.0 | other1·19 |
| 6000.000 | -77.9 | 69.5 | fs8·1 |
| 1999.735 | -78.9 | 67.7 | usb1k·2 |
| 16589.951 | -80.2 | 68.5 | other1·21 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 118/118 | 0.01 | 0.00 | 0.04 |
| usb1k | Kanal 1 | 118/118 | 0.10 | -0.00 | 0.02 |
| led | Kanal 1 | 118/118 | 0.01 | 0.00 | 0.02 |
| mains50 | Kanal 1 | 118/118 | 53.76 | 1.46 | 0.22 |
| other1 | Kanal 1 | 118/118 | 0.00 | -0.00 | 0.00 |
| other2 | Kanal 1 | 118/118 | 0.39 | -0.00 | 0.49 |
| fs8 | Kanal 2 | 118/118 | 0.01 | 0.00 | 0.04 |
| usb1k | Kanal 2 | 118/118 | 0.09 | -0.00 | 0.02 |
| led | Kanal 2 | 118/118 | 0.01 | 0.00 | 0.02 |
| mains50 | Kanal 2 | 118/118 | 35.00 | 1.62 | 0.15 |
| other1 | Kanal 2 | 118/118 | 0.00 | -0.00 | 0.00 |
| other2 | Kanal 2 | 118/118 | 0.74 | -0.01 | 2.42 |
| fs8 | Kanal 3 | 118/118 | 0.01 | 0.00 | 0.03 |
| usb1k | Kanal 3 | 118/118 | 0.08 | -0.00 | 0.03 |
| led | Kanal 3 | 118/118 | 0.00 | 0.00 | 0.01 |
| mains50 | Kanal 3 | 118/118 | 214.49 | 9.30 | 0.13 |
| other1 | Kanal 3 | 118/118 | 0.00 | -0.00 | 0.00 |
| other2 | Kanal 3 | 118/118 | 0.41 | 0.00 | 0.83 |
| fs8 | Kanal 4 | 118/118 | 0.01 | 0.00 | 0.03 |
| usb1k | Kanal 4 | 118/118 | 0.09 | -0.00 | 0.02 |
| led | Kanal 4 | 118/118 | 0.01 | 0.00 | 0.02 |
| mains50 | Kanal 4 | 118/118 | 33.49 | 1.42 | 0.18 |
| other1 | Kanal 4 | 118/118 | 0.00 | 0.00 | 0.00 |
| other2 | Kanal 4 | 118/118 | 0.42 | 0.00 | 0.33 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.06 | 0.05 s (20.00 Hz) | 94.0 |
| Kanal 1 | 440.0 Hz ± 10 | 0.18 | 0.05 s (20.00 Hz) | 103.9 |
| Kanal 2 | breitbandig | 0.08 | 0.05 s (19.99 Hz) | 49.0 |
| Kanal 2 | 530.0 Hz ± 10 | 0.19 | 1.69 s (0.59 Hz) | 39.5 |
| Kanal 3 | breitbandig | 0.06 | 0.05 s (20.00 Hz) | 69.5 |
| Kanal 3 | 670.0 Hz ± 10 | 0.18 | 0.05 s (20.00 Hz) | 66.7 |
| Kanal 4 | breitbandig | 0.03 | 0.05 s (20.00 Hz) | 52.3 |
| Kanal 4 | 790.0 Hz ± 10 | 0.17 | 0.05 s (20.00 Hz) | 62.2 |

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
| Kanal 1 | 1.00 | 0.00 | 0.00 | 0.00 |
| Kanal 2 | 0.00 | 1.00 | 0.00 | 0.00 |
| Kanal 3 | 0.00 | 0.00 | 1.00 | 0.00 |
| Kanal 4 | 0.00 | 0.00 | 0.00 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](A6-fx1d_psd.png)

### Kammprofile

![Kammprofile](A6-fx1d_combs.png)

### Zeitverlauf

![Zeitverlauf](A6-fx1d_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Ende ≈ 16:37. Geräte-Meldung danach (Host-Software lief noch): fb 48.0004 96.2500.
