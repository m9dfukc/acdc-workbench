# Report B10-fx8a-a-r1: B10-fx8a-a-r1 – acdc1 fx8a-open-inputs-10a, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-23 |
| device | acdc1 |
| test | Build-10-Sitzung: fx8a am Anfang, LED-Modus wie gemerkt, Eingänge offen, Regler 12 Uhr, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261123_acdc1_fx8a-open-inputs-10a-r1_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B10-fx8a-a-r1` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -7.1 | -69.6 | -73.0 | -72.2 | -72.9 | -86.0 | -72.5 | -93.6 | -72.2 | 66 % | -76.9 | 4.7 |
| Kanal 2 | -7.4 | -70.5 | -74.0 | -73.0 | -73.7 | -88.0 | -73.3 | -93.9 | -73.0 | 70 % | -78.3 | 5.2 |
| Kanal 3 | -5.7 | -71.8 | -75.2 | -74.5 | -75.1 | -92.3 | -74.7 | -94.7 | -74.5 | 80 % | -81.5 | 7.0 |
| Kanal 4 | -6.5 | -70.3 | -74.8 | -72.2 | -72.7 | -88.1 | -72.4 | -94.1 | -72.2 | 72 % | -77.8 | 5.6 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0002 | 3/3 | k=2: 12000.000 Hz, -83.0 dB | -82.1 | 10.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8678 | 0.0002 | 23/23 | k=1: 999.868 Hz, -73.4 dB | -74.7 | 56.3 % |
| Netz 50 Hz | Kanal 1 | 49.9933 | 0.0047 | 2/19 | k=2: 99.980 Hz, -109.3 dB | -107.9 | 0.0 % |
| Mischprodukte n·999.8678 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8678 | 0.0028 | 10 | k=-15·f1+4·f2: 9001.979 Hz, -121.0 dB | -115.3 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 1 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -96.8 dB | -95.4 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 1 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -97.9 dB | -98.5 | 0.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.1 dB | -82.2 | 12.0 % |
| 1-kHz-Kamm | Kanal 2 | 999.8678 | 0.0002 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.4 | 57.9 % |
| Mischprodukte n·999.8678 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8678 | 0.0023 | 13 | k=-3·f1+4·f2: 21000.396 Hz, -121.9 dB | -114.6 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 2 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -97.4 dB | -95.6 | 0.5 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 2 | 3000.0004 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -98.2 dB | -98.7 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -83.8 dB | -82.7 | 15.0 % |
| 1-kHz-Kamm | Kanal 3 | 999.8678 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.3 dB | -76.4 | 64.9 % |
| Netz 50 Hz | Kanal 3 | 49.9929 | 0.0137 | 5/19 | k=2: 99.980 Hz, -113.9 dB | -109.3 | 0.0 % |
| Mischprodukte n·999.8678 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8678 | 0.0020 | 24 | k=-3·f1+4·f2: 21000.397 Hz, -121.8 dB | -113.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 3 | 2000.0002 | 0.0002 | 8/11 | k=1: 2000.000 Hz, -98.9 dB | -96.5 | 0.6 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 3 | 3000.0003 | 0.0002 | 4/7 | k=1: 3000.000 Hz, -99.2 dB | -99.5 | 0.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=2: 12000.000 Hz, -83.3 dB | -82.4 | 9.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8678 | 0.0002 | 23/23 | k=1: 999.868 Hz, -72.9 dB | -74.2 | 62.9 % |
| Netz 50 Hz | Kanal 4 | 49.9930 | 0.0142 | 4/19 | k=2: 99.979 Hz, -110.2 dB | -108.0 | 0.0 % |
| Mischprodukte n·999.8678 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8678 | 0.0026 | 11 | k=-8·f1+4·f2: 16001.057 Hz, -121.3 dB | -114.7 | 0.0 % |
| stärkste übrige Linie (2000.00 Hz) | Kanal 4 | 2000.0002 | 0.0003 | 8/11 | k=1: 2000.000 Hz, -97.6 dB | -95.8 | 0.4 % |
| stärkste übrige Linie (3000.00 Hz) | Kanal 4 | 3000.0003 | 0.0004 | 4/7 | k=1: 3000.000 Hz, -98.6 dB | -99.1 | 0.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.4 | 57.0 | usb1k·1 |
| 1999.736 | -81.1 | 51.1 | usb1k·2 |
| 2999.604 | -82.6 | 50.8 | usb1k·3 |
| 12000.000 | -83.0 | 55.2 | fs8·2 |
| 6000.000 | -83.4 | 52.3 | fs8·1 |
| 18000.000 | -86.0 | 52.7 | fs8·3 |
| 3999.472 | -87.1 | 47.8 | usb1k·4 |
| 9998.678 | -88.3 | 49.0 | usb1k·10 |
| 15997.885 | -89.9 | 48.6 | usb1k·16 |
| 4999.339 | -89.2 | 45.4 | usb1k·5 |
| 6999.075 | -90.0 | 46.1 | usb1k·7 |
| 8998.810 | -92.0 | 44.6 | usb1k·9 |
| 16997.752 | -93.0 | 45.6 | usb1k·17 |
| 18997.488 | -93.2 | 45.1 | usb1k·19 |
| 20997.224 | -93.7 | 45.4 | usb1k·21 |
| 13998.149 | -95.5 | 42.8 | usb1k·14 |
| 14998.017 | -96.2 | 41.5 | usb1k·15 |
| 11998.413 | -96.1 | 42.1 | usb1k·12 |
| 2000.000 | -96.8 | 35.4 | other1·1 |
| 17997.620 | -97.1 | 41.6 | usb1k·18 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 57.9 | usb1k·1 |
| 1999.736 | -82.1 | 52.1 | usb1k·2 |
| 12000.000 | -83.1 | 56.4 | fs8·2 |
| 6000.000 | -83.3 | 53.6 | fs8·1 |
| 2999.604 | -83.1 | 51.8 | usb1k·3 |
| 18000.000 | -86.0 | 53.5 | fs8·3 |
| 3999.472 | -87.5 | 48.9 | usb1k·4 |
| 9998.678 | -88.3 | 50.0 | usb1k·10 |
| 15997.885 | -90.2 | 49.0 | usb1k·16 |
| 4999.339 | -89.8 | 46.1 | usb1k·5 |
| 6999.074 | -90.6 | 47.3 | usb1k·7 |
| 16997.752 | -93.2 | 46.2 | usb1k·17 |
| 8998.810 | -92.5 | 45.4 | usb1k·9 |
| 18997.488 | -93.2 | 46.2 | usb1k·19 |
| 20997.224 | -94.1 | 45.9 | usb1k·21 |
| 14998.017 | -96.2 | 43.0 | usb1k·15 |
| 13998.149 | -96.4 | 42.9 | usb1k·14 |
| 11998.413 | -96.4 | 43.2 | usb1k·12 |
| 17997.620 | -97.0 | 42.5 | usb1k·18 |
| 2000.000 | -97.4 | 36.8 | other1·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.3 | 60.6 | usb1k·1 |
| 1999.736 | -83.3 | 55.1 | usb1k·2 |
| 6000.000 | -83.8 | 56.6 | fs8·1 |
| 12000.000 | -83.8 | 58.8 | fs8·2 |
| 2999.604 | -84.1 | 54.8 | usb1k·3 |
| 18000.000 | -86.4 | 56.0 | fs8·3 |
| 3999.472 | -88.1 | 52.0 | usb1k·4 |
| 9998.678 | -88.6 | 53.3 | usb1k·10 |
| 15997.885 | -90.8 | 51.2 | usb1k·16 |
| 4999.339 | -90.3 | 49.1 | usb1k·5 |
| 6999.075 | -91.5 | 50.3 | usb1k·7 |
| 16997.752 | -93.7 | 48.6 | usb1k·17 |
| 18997.488 | -93.5 | 48.7 | usb1k·19 |
| 8998.810 | -93.1 | 48.2 | usb1k·9 |
| 20997.224 | -94.9 | 47.3 | usb1k·21 |
| 14998.017 | -96.7 | 45.3 | usb1k·15 |
| 11998.413 | -96.8 | 45.7 | usb1k·12 |
| 12998.281 | -97.4 | 45.0 | usb1k·13 |
| 17997.620 | -97.3 | 45.1 | usb1k·18 |
| 13998.149 | -97.9 | 44.3 | usb1k·14 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.9 | 58.6 | usb1k·1 |
| 1999.736 | -80.4 | 53.3 | usb1k·2 |
| 2999.603 | -82.4 | 52.3 | usb1k·3 |
| 12000.000 | -83.3 | 55.2 | fs8·2 |
| 6000.000 | -83.5 | 53.0 | fs8·1 |
| 18000.000 | -86.2 | 52.7 | fs8·3 |
| 3999.472 | -86.9 | 49.0 | usb1k·4 |
| 9998.678 | -88.4 | 49.5 | usb1k·10 |
| 4999.339 | -88.8 | 46.1 | usb1k·5 |
| 15997.885 | -89.7 | 48.7 | usb1k·16 |
| 6999.075 | -89.8 | 47.4 | usb1k·7 |
| 8998.810 | -91.7 | 45.4 | usb1k·9 |
| 16997.752 | -93.0 | 45.9 | usb1k·17 |
| 18997.488 | -93.3 | 45.6 | usb1k·19 |
| 20997.224 | -93.5 | 45.9 | usb1k·21 |
| 13998.149 | -94.7 | 43.7 | usb1k·14 |
| 11998.413 | -95.9 | 42.5 | usb1k·12 |
| 14998.017 | -96.3 | 41.9 | usb1k·15 |
| 5999.207 | -96.3 | 40.1 | usb1k·6 |
| 7998.942 | -95.9 | 41.0 | usb1k·8 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.03 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.28 | -0.27 | 0.21 |
| mains50 | Kanal 1 | 11/11 | 18.00 | -18.69 | 0.78 |
| other1 | Kanal 1 | 11/11 | 1.72 | 0.28 | 0.29 |
| other2 | Kanal 1 | 11/11 | 0.26 | 0.39 | 0.19 |
| fs8 | Kanal 2 | 11/11 | 0.02 | 0.00 | 0.03 |
| usb1k | Kanal 2 | 11/11 | 0.28 | -0.24 | 0.21 |
| other1 | Kanal 2 | 11/11 | 2.03 | -1.98 | 0.30 |
| other2 | Kanal 2 | 11/11 | 0.23 | 0.25 | 0.16 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.03 |
| usb1k | Kanal 3 | 11/11 | 0.26 | -0.19 | 0.18 |
| mains50 | Kanal 3 | 11/11 | 131.37 | 260.33 | 0.49 |
| other1 | Kanal 3 | 11/11 | 0.22 | -0.03 | 0.26 |
| other2 | Kanal 3 | 11/11 | 0.18 | 0.29 | 0.14 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.04 | 0.04 |
| usb1k | Kanal 4 | 11/11 | 0.26 | -0.31 | 0.26 |
| mains50 | Kanal 4 | 11/11 | 172.58 | 41.44 | 0.65 |
| other1 | Kanal 4 | 11/11 | 2.17 | 3.49 | 0.32 |
| other2 | Kanal 4 | 11/11 | 0.26 | 0.24 | 0.21 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.00 | 0.31 s (3.22 Hz) | 25.4 |
| Kanal 1 | 999.9 Hz ± 10 | 0.99 | 7.50 s (0.13 Hz) | 37.3 |
| Kanal 2 | breitbandig | 1.92 | 0.31 s (3.22 Hz) | 27.2 |
| Kanal 2 | 999.9 Hz ± 10 | 0.99 | 7.50 s (0.13 Hz) | 38.8 |
| Kanal 3 | breitbandig | 1.99 | 0.31 s (3.22 Hz) | 24.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.97 | 7.50 s (0.13 Hz) | 42.5 |
| Kanal 4 | breitbandig | 1.57 | 0.31 s (3.22 Hz) | 27.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.99 | 7.50 s (0.13 Hz) | 37.1 |

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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.95 |
| Kanal 2 | 0.97 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.93 |
| Kanal 4 | 0.95 | 0.97 | 0.93 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](B10-fx8a-a-r1_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](B10-fx8a-a-r1_psd.png)

### Kammprofile

![Kammprofile](B10-fx8a-a-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B10-fx8a-a-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 14:52:59. Stream-Meldungen: 0. owl_read: out/owl_read/B10-fx8a-a-r1 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet. Firmware Build 10 v22.4.r-fx8a (I-Cache an), acdc1 im Case. Vor der Aufnahme lief wieder der gemerkte Slot 12, acdc1 wurde vermutlich beim Umstecken neu gestartet. Regler 69/55/72/56 von 127. Oszillator im Case abgesteckt (Nutzer). messlog D85.
