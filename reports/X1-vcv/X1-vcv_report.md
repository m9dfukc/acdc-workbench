# Report X1-vcv: X1-vcv – acdc1 Build 3d, rohe Eingänge offen, 60 s, Host-Software mit Mehrkanal-Recorder

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Gegenprobe Werkzeug 1/2 (ITCM-Plan Q14): Host-Software mit Mehrkanal-Recorder, Eingänge offen, rohe ADC-Daten. Gegenstück: X1-rec (tools/acdc_rec.py) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_x1-vcv-open-inputs_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.2 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis X1-vcv --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.0 | -68.0 | -69.7 | -72.9 | -74.7 | -85.1 | -73.5 | -99.0 | -72.9 | 48 % | -75.7 | 2.8 |
| Kanal 2 | -6.6 | -70.5 | -73.7 | -73.3 | -74.8 | -87.3 | -73.7 | – | -73.3 | 61 % | -77.4 | 4.1 |
| Kanal 3 | -4.8 | -71.1 | -73.2 | -75.3 | -77.2 | -91.0 | -75.7 | – | -75.3 | 71 % | -80.7 | 5.4 |
| Kanal 4 | -5.7 | -70.7 | -75.2 | -72.7 | -74.0 | -87.8 | -73.1 | – | -72.7 | 60 % | -76.6 | 3.9 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.4 dB | -79.2 | 23.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8658 | 0.0009 | 22/23 | k=1: 999.866 Hz, -79.4 dB | -80.2 | 18.5 % |
| Netz 50 Hz | Kanal 1 | 50.0002 | 0.0020 | 3/19 | k=1: 50.002 Hz, -94.0 dB | -96.1 | 0.5 % |
| Mischprodukte n·999.8658 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8658 | 0.0009 | 143 | k=8·f1+1·f2: 13998.927 Hz, -95.3 dB | -85.5 | 5.5 % |
| stärkste übrige Linie (51.12 Hz) | Kanal 1 | 51.1233 | 0.0001 | 2/467 | k=1: 51.123 Hz, -100.1 dB | -99.0 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.1 | 25.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8658 | 0.0013 | 23/23 | k=1: 999.866 Hz, -77.6 dB | -78.7 | 28.6 % |
| Netz 50 Hz | Kanal 2 | 50.0002 | 0.0020 | 3/19 | k=1: 50.002 Hz, -94.8 dB | -96.9 | 0.4 % |
| Mischprodukte n·999.8658 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8658 | 0.0009 | 152 | k=8·f1+1·f2: 13998.927 Hz, -95.4 dB | -85.4 | 6.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.7 dB | -79.4 | 39.0 % |
| 1-kHz-Kamm | Kanal 3 | 999.8658 | 0.0005 | 23/23 | k=1: 999.866 Hz, -81.5 dB | -81.8 | 22.6 % |
| Netz 50 Hz | Kanal 3 | 50.0001 | 0.0018 | 3/19 | k=1: 50.002 Hz, -95.7 dB | -97.7 | 0.6 % |
| Mischprodukte n·999.8658 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8658 | 0.0008 | 164 | k=8·f1+1·f2: 13998.927 Hz, -95.5 dB | -85.6 | 9.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.4 dB | -79.4 | 21.3 % |
| 1-kHz-Kamm | Kanal 4 | 999.8658 | 0.0004 | 23/23 | k=1: 999.866 Hz, -76.3 dB | -77.5 | 33.0 % |
| Netz 50 Hz | Kanal 4 | 50.0003 | 0.0016 | 3/19 | k=1: 50.002 Hz, -95.7 dB | -97.6 | 0.3 % |
| Mischprodukte n·999.8658 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8658 | 0.0008 | 146 | k=8·f1+1·f2: 13998.927 Hz, -95.7 dB | -85.7 | 5.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -79.4 | 55.0 | fs8·1 |
| 999.866 | -79.4 | 51.6 | usb1k·1 |
| 18000.000 | -82.0 | 54.4 | fs8·3 |
| 12000.000 | -82.2 | 53.6 | fs8·2 |
| 2999.597 | -85.8 | 46.9 | usb1k·3 |
| 1999.731 | -89.0 | 43.1 | usb1k·2 |
| 6999.061 | -88.7 | 45.0 | usb1k·7 |
| 9998.659 | -92.3 | 42.8 | usb1k·10 |
| 50.002 | -94.0 | 26.3 | mains50·1 |
| 15997.853 | -94.7 | 40.8 | usb1k·16 |
| 14997.987 | -95.2 | 40.2 | usb1k·15 |
| 10998.524 | -95.5 | 40.0 | usb1k·11 |
| 13998.927 | -95.3 | 40.1 | imd·8·f1+1·f2 |
| 15999.463 | -96.0 | 39.5 | imd·4·f1+2·f2 |
| 9999.463 | -96.3 | 38.8 | imd·4·f1+1·f2 |
| 7998.927 | -95.9 | 37.4 | usb1k·8 |
| 16998.524 | -97.1 | 38.9 | imd·11·f1+1·f2 |
| 12999.865 | -97.3 | 39.0 | imd·1·f1+2·f2 |
| 19998.927 | -96.7 | 39.4 | imd·8·f1+2·f2 |
| 11998.390 | -97.9 | 37.9 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -77.6 | 54.8 | usb1k·1 |
| 6000.000 | -79.2 | 56.7 | fs8·1 |
| 18000.000 | -82.0 | 56.2 | fs8·3 |
| 12000.000 | -82.1 | 55.2 | fs8·2 |
| 2999.597 | -84.9 | 49.3 | usb1k·3 |
| 1999.731 | -86.4 | 47.3 | usb1k·2 |
| 6999.061 | -88.5 | 46.9 | usb1k·7 |
| 9998.658 | -92.2 | 44.4 | usb1k·10 |
| 15997.853 | -93.8 | 43.6 | usb1k·16 |
| 50.002 | -94.8 | 28.3 | mains50·1 |
| 14997.987 | -95.0 | 42.0 | usb1k·15 |
| 10998.524 | -95.1 | 42.4 | usb1k·11 |
| 13998.927 | -95.4 | 42.2 | imd·8·f1+1·f2 |
| 15999.463 | -96.1 | 41.4 | imd·4·f1+2·f2 |
| 9999.463 | -96.2 | 40.3 | imd·4·f1+1·f2 |
| 12999.866 | -97.1 | 40.7 | imd·1·f1+2·f2 |
| 16998.524 | -96.9 | 41.1 | imd·11·f1+1·f2 |
| 14999.597 | -97.5 | 39.6 | imd·3·f1+2·f2 |
| 19998.927 | -96.6 | 40.9 | imd·8·f1+2·f2 |
| 7998.927 | -96.8 | 38.1 | usb1k·8 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -79.7 | 59.5 | fs8·1 |
| 999.866 | -81.5 | 55.5 | usb1k·1 |
| 18000.000 | -82.0 | 58.5 | fs8·3 |
| 12000.000 | -82.1 | 57.9 | fs8·2 |
| 2999.597 | -87.3 | 50.9 | usb1k·3 |
| 1999.731 | -89.6 | 48.2 | usb1k·2 |
| 6999.061 | -89.6 | 49.5 | usb1k·7 |
| 9998.658 | -92.9 | 47.1 | usb1k·10 |
| 14997.987 | -95.2 | 45.0 | usb1k·15 |
| 15997.853 | -95.2 | 45.3 | usb1k·16 |
| 50.002 | -95.7 | 31.2 | mains50·1 |
| 10998.524 | -96.2 | 43.8 | usb1k·11 |
| 15999.463 | -96.0 | 44.4 | imd·4·f1+2·f2 |
| 13998.927 | -95.5 | 44.8 | imd·8·f1+1·f2 |
| 7998.927 | -95.7 | 42.6 | usb1k·8 |
| 9999.463 | -96.5 | 43.4 | imd·4·f1+1·f2 |
| 16998.524 | -97.2 | 43.1 | imd·11·f1+1·f2 |
| 12999.865 | -97.4 | 43.3 | imd·1·f1+2·f2 |
| 19998.927 | -96.9 | 43.0 | imd·8·f1+2·f2 |
| 11998.390 | -98.1 | 42.1 | usb1k·12 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.866 | -76.3 | 54.9 | usb1k·1 |
| 6000.000 | -79.4 | 55.0 | fs8·1 |
| 18000.000 | -82.3 | 54.3 | fs8·3 |
| 12000.000 | -82.4 | 54.2 | fs8·2 |
| 1999.731 | -83.5 | 49.7 | usb1k·2 |
| 2999.597 | -84.6 | 49.2 | usb1k·3 |
| 6999.061 | -88.8 | 45.9 | usb1k·7 |
| 9998.658 | -92.3 | 43.0 | usb1k·10 |
| 15997.853 | -93.1 | 43.1 | usb1k·16 |
| 14997.987 | -94.9 | 40.9 | usb1k·15 |
| 10998.524 | -95.2 | 40.9 | usb1k·11 |
| 50.002 | -95.7 | 28.3 | mains50·1 |
| 5999.195 | -94.9 | 39.4 | usb1k·6 |
| 9999.463 | -96.2 | 39.0 | imd·4·f1+1·f2 |
| 13998.927 | -95.7 | 40.3 | imd·8·f1+1·f2 |
| 15999.463 | -96.4 | 39.9 | imd·4·f1+2·f2 |
| 12999.866 | -97.1 | 39.2 | imd·1·f1+2·f2 |
| 16998.524 | -96.9 | 39.3 | imd·11·f1+1·f2 |
| 14999.597 | -97.5 | 38.3 | imd·3·f1+2·f2 |
| 4999.329 | -96.9 | 37.7 | usb1k·5 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.03 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.12 | 0.37 | 0.05 |
| mains50 | Kanal 1 | 11/11 | 39.16 | 49.72 | 0.51 |
| other1 | Kanal 1 | 11/11 | 2.39 | -5.69 | 3.19 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.02 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.22 | 0.56 | 0.05 |
| mains50 | Kanal 2 | 11/11 | 38.11 | 54.81 | 0.41 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.02 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.18 | 0.49 | 0.02 |
| mains50 | Kanal 3 | 11/11 | 27.95 | 61.20 | 0.40 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.00 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.24 | 0.61 | 0.08 |
| mains50 | Kanal 4 | 11/11 | 36.67 | 75.61 | 0.45 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 3.00 | 0.31 s (3.17 Hz) | 18.4 |
| Kanal 1 | 6000.0 Hz ± 10 | 1.33 | 1.25 s (0.80 Hz) | 42.9 |
| Kanal 2 | breitbandig | 2.04 | 0.31 s (3.22 Hz) | 18.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 1.25 s (0.80 Hz) | 30.2 |
| Kanal 3 | breitbandig | 2.66 | 0.31 s (3.17 Hz) | 20.1 |
| Kanal 3 | 6000.0 Hz ± 10 | 1.23 | 1.25 s (0.80 Hz) | 46.8 |
| Kanal 4 | breitbandig | 1.57 | 1.25 s (0.80 Hz) | 18.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 29.8 |

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
| Kanal 1 | 1.00 | 0.96 | 0.97 | 0.89 |
| Kanal 2 | 0.96 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.97 | 0.96 | 1.00 | 0.90 |
| Kanal 4 | 0.89 | 0.97 | 0.90 | 1.00 |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](X1-vcv_psd.png)

### Kammprofile

![Kammprofile](X1-vcv_combs.png)

### Zeitverlauf

![Zeitverlauf](X1-vcv_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 16:28–16:29.
