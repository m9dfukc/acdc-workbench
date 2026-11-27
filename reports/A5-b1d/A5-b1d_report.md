# Report A5-b1d: A5-b1d – acdc1 Build 1d, Eingänge offen, Gain 12 Uhr, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d (Build 1c + Pufferstand-Regelung im Feedback, Patch 06) |
| test | Abnahme A5: Eingänge offen (nichts gesteckt), Vergleich mit A5-b1b (Build 1b) und S2-4 (alte Firmware) |
| gain | g12 |
| usb | usb-stream, Thunderbolt-Hub, Host-Software 48 kHz, Audio-Modul ohne Playback (Stille an die Ausgänge) |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_b1d-open-inputs_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 121.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis A5-b1d --ref A5-b1b` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -5.1 | -60.2 | -60.4 | -72.5 | -73.9 | -83.9 | -73.1 | -92.6 | -72.5 | 57 % | -76.2 | 3.7 |
| Kanal 2 | -5.7 | -63.1 | -63.6 | -73.0 | -74.3 | -85.2 | -73.5 | -92.4 | -73.0 | 66 % | -77.7 | 4.6 |
| Kanal 3 | -4.0 | -63.9 | -64.3 | -75.0 | -76.7 | -88.6 | -75.6 | -95.6 | -75.0 | 74 % | -80.9 | 5.9 |
| Kanal 4 | -4.8 | -63.8 | -64.5 | -72.6 | -73.8 | -85.9 | -73.1 | -96.2 | -72.7 | 64 % | -77.1 | 4.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.9 dB | -79.8 | 18.5 % |
| 1-kHz-Kamm | Kanal 1 | 999.8680 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.9 dB | -77.3 | 33.4 % |
| Netz 50 Hz | Kanal 1 | 49.9751 | 0.0043 | 3/19 | k=1: 49.973 Hz, -91.0 dB | -93.1 | 0.9 % |
| Mischprodukte n·999.8680 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8680 | 0.0006 | 157 | k=8·f1+1·f2: 13998.944 Hz, -96.6 dB | -86.3 | 4.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 1 | 75.7229 | 0.0013 | 2/315 | k=1: 75.721 Hz, -90.2 dB | -93.6 | 0.8 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 1 | 44.7584 | 0.0050 | 6/533 | k=1: 44.758 Hz, -97.7 dB | -99.8 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.9 dB | -79.8 | 21.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8680 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.7 dB | -77.1 | 38.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2316.4510 | 0.0000 | 1/10 | k=3: 6949.353 Hz, -124.6 dB | -127.6 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9758 | 0.0078 | 4/19 | k=1: 49.973 Hz, -91.8 dB | -93.9 | 0.8 % |
| Mischprodukte n·999.8680 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8680 | 0.0004 | 163 | k=8·f1+1·f2: 13998.944 Hz, -96.6 dB | -86.3 | 4.7 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 2 | 75.7220 | 0.0007 | 2/315 | k=1: 75.721 Hz, -89.7 dB | -92.8 | 1.0 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 2 | 89.5146 | 0.0005 | 2/266 | k=1: 89.515 Hz, -99.1 dB | -102.1 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -80.3 dB | -80.0 | 31.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8680 | 0.0002 | 23/23 | k=1: 999.868 Hz, -78.6 dB | -79.7 | 34.1 % |
| Netz 50 Hz | Kanal 3 | 49.9759 | 0.0067 | 6/19 | k=1: 49.973 Hz, -93.0 dB | -95.1 | 1.0 % |
| Mischprodukte n·999.8680 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8680 | 0.0005 | 170 | k=8·f1+1·f2: 13998.944 Hz, -96.8 dB | -86.5 | 7.1 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 3 | 75.7213 | 0.0002 | 2/315 | k=1: 75.721 Hz, -93.6 dB | -96.8 | 0.7 % |
| stärkste übrige Linie (44.76 Hz) | Kanal 3 | 44.7576 | 0.0011 | 8/533 | k=1: 44.758 Hz, -99.5 dB | -101.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -80.4 dB | -80.3 | 17.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8680 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.4 | 42.6 % |
| Netz 50 Hz | Kanal 4 | 49.9759 | 0.0079 | 4/19 | k=1: 49.973 Hz, -92.9 dB | -94.9 | 0.6 % |
| Mischprodukte n·999.8680 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8680 | 0.0006 | 160 | k=8·f1+1·f2: 13998.944 Hz, -97.2 dB | -86.8 | 3.8 % |
| stärkste übrige Linie (75.72 Hz) | Kanal 4 | 75.7189 | 0.0015 | 2/315 | k=1: 75.721 Hz, -94.7 dB | -97.8 | 0.3 % |
| stärkste übrige Linie (89.52 Hz) | Kanal 4 | 89.5156 | 0.0002 | 2/266 | k=1: 89.515 Hz, -98.2 dB | -101.2 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.9 | 58.1 | usb1k·1 |
| 6000.000 | -79.9 | 58.2 | fs8·1 |
| 18000.000 | -82.4 | 57.5 | fs8·3 |
| 12000.000 | -82.7 | 56.4 | fs8·2 |
| 2999.604 | -84.1 | 51.7 | usb1k·3 |
| 1999.736 | -83.9 | 51.4 | usb1k·2 |
| 6999.076 | -89.0 | 49.2 | usb1k·7 |
| 49.973 | -91.0 | 32.6 | mains50·1 |
| 75.721 | -90.2 | 36.2 | other1·1 |
| 9998.680 | -92.1 | 47.0 | usb1k·10 |
| 15997.888 | -93.3 | 46.5 | usb1k·16 |
| 10998.548 | -95.3 | 43.9 | usb1k·11 |
| 5999.208 | -95.3 | 42.8 | usb1k·6 |
| 14998.020 | -96.0 | 43.8 | usb1k·15 |
| 4999.340 | -96.9 | 40.9 | usb1k·5 |
| 15999.472 | -96.9 | 42.9 | imd·4·f1+2·f2 |
| 13998.152 | -96.7 | 43.0 | usb1k·14 |
| 44.758 | -97.7 | 25.3 | other2·1 |
| 19998.944 | -97.7 | 42.9 | imd·8·f1+2·f2 |
| 13998.944 | -96.6 | 43.1 | imd·8·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.7 | 59.9 | usb1k·1 |
| 6000.000 | -79.9 | 59.9 | fs8·1 |
| 18000.000 | -82.4 | 59.4 | fs8·3 |
| 12000.000 | -82.5 | 58.4 | fs8·2 |
| 2999.604 | -84.1 | 53.5 | usb1k·3 |
| 1999.736 | -83.5 | 53.5 | usb1k·2 |
| 6999.076 | -89.1 | 50.9 | usb1k·7 |
| 75.721 | -89.7 | 38.8 | other1·1 |
| 49.973 | -91.8 | 33.9 | mains50·1 |
| 9998.680 | -92.1 | 48.5 | usb1k·10 |
| 15997.888 | -93.2 | 48.5 | usb1k·16 |
| 10998.548 | -95.2 | 45.9 | usb1k·11 |
| 5999.208 | -95.0 | 44.7 | usb1k·6 |
| 4999.340 | -96.2 | 43.2 | usb1k·5 |
| 14998.020 | -95.7 | 45.8 | usb1k·15 |
| 15999.472 | -96.9 | 44.7 | imd·4·f1+2·f2 |
| 13998.152 | -96.8 | 44.6 | usb1k·14 |
| 19998.944 | -97.6 | 44.4 | imd·8·f1+2·f2 |
| 13998.944 | -96.6 | 44.9 | imd·8·f1+1·f2 |
| 16998.548 | -97.4 | 44.1 | imd·11·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -78.6 | 61.5 | usb1k·1 |
| 6000.000 | -80.3 | 62.8 | fs8·1 |
| 18000.000 | -82.5 | 61.0 | fs8·3 |
| 12000.000 | -82.5 | 61.2 | fs8·2 |
| 2999.604 | -86.2 | 55.5 | usb1k·3 |
| 1999.736 | -86.0 | 55.1 | usb1k·2 |
| 6999.076 | -90.2 | 52.9 | usb1k·7 |
| 49.973 | -93.0 | 36.6 | mains50·1 |
| 9998.680 | -93.1 | 50.8 | usb1k·10 |
| 15997.888 | -94.6 | 49.7 | usb1k·16 |
| 75.721 | -93.6 | 38.9 | other1·1 |
| 14998.020 | -95.8 | 48.3 | usb1k·15 |
| 10998.548 | -96.2 | 47.6 | usb1k·11 |
| 15999.472 | -97.0 | 47.0 | imd·4·f1+2·f2 |
| 19998.944 | -97.8 | 46.5 | imd·8·f1+2·f2 |
| 13998.944 | -96.8 | 47.4 | imd·8·f1+1·f2 |
| 16998.548 | -97.7 | 46.5 | imd·11·f1+1·f2 |
| 12999.076 | -97.9 | 46.3 | imd·7·f1+1·f2 |
| 5999.208 | -97.5 | 45.5 | usb1k·6 |
| 18997.492 | -97.9 | 46.0 | usb1k·19 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 60.2 | usb1k·1 |
| 6000.000 | -80.4 | 58.5 | fs8·1 |
| 1999.736 | -81.4 | 55.3 | usb1k·2 |
| 18000.000 | -83.0 | 57.4 | fs8·3 |
| 12000.000 | -83.1 | 56.9 | fs8·2 |
| 2999.604 | -84.2 | 52.9 | usb1k·3 |
| 6999.076 | -89.8 | 49.5 | usb1k·7 |
| 49.973 | -92.9 | 32.8 | mains50·1 |
| 4999.340 | -92.7 | 46.0 | usb1k·5 |
| 15997.888 | -93.1 | 47.4 | usb1k·16 |
| 9998.680 | -92.3 | 47.6 | usb1k·10 |
| 5999.208 | -93.1 | 45.7 | usb1k·6 |
| 75.721 | -94.7 | 33.6 | other1·1 |
| 10998.548 | -95.9 | 44.5 | usb1k·11 |
| 14998.020 | -96.0 | 44.5 | usb1k·15 |
| 18997.492 | -96.8 | 43.7 | usb1k·19 |
| 15999.472 | -97.6 | 42.9 | imd·4·f1+2·f2 |
| 89.515 | -98.2 | 30.1 | other2·1 |
| 19998.944 | -98.1 | 42.5 | imd·8·f1+2·f2 |
| 16998.548 | -97.8 | 42.5 | imd·11·f1+1·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 23/23 | 0.02 | -0.01 | 0.05 |
| usb1k | Kanal 1 | 23/23 | 0.34 | 0.52 | 0.24 |
| mains50 | Kanal 1 | 23/23 | 272.82 | -1.27 | 0.55 |
| other1 | Kanal 1 | 23/23 | 31.02 | -7.55 | 0.44 |
| other2 | Kanal 1 | 23/23 | 31.53 | 16.96 | 0.79 |
| fs8 | Kanal 2 | 23/23 | 0.01 | -0.00 | 0.04 |
| usb1k | Kanal 2 | 23/23 | 0.29 | 0.48 | 0.25 |
| led | Kanal 2 | 14/23 | 19.57 | 9.41 | 1.55 |
| mains50 | Kanal 2 | 23/23 | 460.54 | 141.02 | 0.51 |
| other1 | Kanal 2 | 23/23 | 33.55 | 10.43 | 0.35 |
| other2 | Kanal 2 | 23/23 | 61.53 | -24.46 | 0.83 |
| fs8 | Kanal 3 | 23/23 | 0.01 | -0.00 | 0.04 |
| usb1k | Kanal 3 | 23/23 | 0.31 | 0.47 | 0.24 |
| mains50 | Kanal 3 | 23/23 | 290.98 | 111.33 | 0.31 |
| other1 | Kanal 3 | 23/23 | 28.28 | -11.45 | 0.30 |
| other2 | Kanal 3 | 23/23 | 10.91 | 7.34 | 0.40 |
| fs8 | Kanal 4 | 23/23 | 0.02 | -0.01 | 0.06 |
| usb1k | Kanal 4 | 23/23 | 0.32 | 0.52 | 0.29 |
| mains50 | Kanal 4 | 23/23 | 485.16 | 73.74 | 0.52 |
| other1 | Kanal 4 | 23/23 | 67.39 | -5.12 | 0.57 |
| other2 | Kanal 4 | 23/23 | 65.77 | -15.33 | 0.82 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 5.08 | 30.24 s (0.03 Hz) | 29.9 |
| Kanal 1 | 999.9 Hz ± 10 | 0.72 | 1.26 s (0.79 Hz) | 30.8 |
| Kanal 2 | breitbandig | 4.42 | 0.31 s (3.21 Hz) | 31.3 |
| Kanal 2 | 999.9 Hz ± 10 | 0.67 | 1.26 s (0.79 Hz) | 33.0 |
| Kanal 3 | breitbandig | 4.71 | 30.24 s (0.03 Hz) | 30.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.69 | 1.26 s (0.79 Hz) | 36.6 |
| Kanal 4 | breitbandig | 4.11 | 0.31 s (3.19 Hz) | 31.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.71 | 1.26 s (0.79 Hz) | 32.5 |

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
| Kanal 1 | 1.00 | 0.99 | 0.99 | 0.98 |
| Kanal 2 | 0.99 | 1.00 | 0.99 | 0.99 |
| Kanal 3 | 0.99 | 0.99 | 1.00 | 0.98 |
| Kanal 4 | 0.98 | 0.99 | 0.98 | 1.00 |

## Vergleich mit Referenz A5-b1b

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.5 | -71.4 | -1.1 | 57 % | 68 % |
| Kanal 2 | -73.0 | -72.2 | -0.8 | 66 % | 73 % |
| Kanal 3 | -75.0 | -73.7 | -1.2 | 74 % | 82 % |
| Kanal 4 | -72.6 | -71.4 | -1.3 | 64 % | 74 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](A5-b1d_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](A5-b1d_psd.png)

### Kammprofile

![Kammprofile](A5-b1d_combs.png)

### Zeitverlauf

![Zeitverlauf](A5-b1d_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float nativ, Mehrkanal-Recorder. Datei-Werte enthalten den Host-Faktor 2 (messlog D7/D8), wie A5-b1b und S2-4. Ausgang 125 statt 114 (Patch 04), Eingang unverändert 88.
