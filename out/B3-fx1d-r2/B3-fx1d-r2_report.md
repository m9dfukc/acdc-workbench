# Report B3-fx1d-r2: B3-fx1d-r2 – acdc1 Build 2, rohe Eingänge offen, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 2 v22.4.r-fx1d (Build 1d + TX_PRE_FX) |
| test | Abnahme A5/B3 2/2: wie r1, nach Neustart der Host-Software |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx1d-open-inputs-r2_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx1d-r2 --ref A5-b1d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -71.4 | -81.4 | -71.8 | -73.0 | -85.1 | -72.3 | – | -71.8 | 63 % | -76.2 | 4.4 |
| Kanal 2 | -6.8 | -72.3 | -83.0 | -72.6 | -73.8 | -87.1 | -73.0 | – | -72.6 | 70 % | -77.8 | 5.2 |
| Kanal 3 | -5.1 | -74.1 | -88.0 | -74.2 | -75.5 | -91.0 | -74.6 | – | -74.2 | 80 % | -81.3 | 7.1 |
| Kanal 4 | -5.9 | -71.5 | -83.1 | -71.8 | -72.8 | -87.6 | -72.1 | – | -71.8 | 71 % | -77.1 | 5.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.9 dB | -79.0 | 19.1 % |
| 1-kHz-Kamm | Kanal 1 | 999.8673 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.9 | 39.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5448 | 0.0018 | 10/10 | k=1: 2320.545 Hz, -115.9 dB | -113.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9898 | 0.0002 | 2/19 | k=1: 49.990 Hz, -92.5 dB | -95.1 | 0.5 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8673 | 0.0010 | 147 | k=8·f1+1·f2: 13998.938 Hz, -95.2 dB | -85.4 | 4.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.8 dB | -78.9 | 23.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8673 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.6 | 40.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0011 | 10/10 | k=9: 20884.904 Hz, -114.5 dB | -110.1 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9898 | 0.0003 | 2/19 | k=1: 49.990 Hz, -93.4 dB | -96.0 | 0.5 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8673 | 0.0008 | 154 | k=8·f1+1·f2: 13998.938 Hz, -95.2 dB | -85.3 | 5.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.2 | 32.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8673 | 0.0003 | 23/23 | k=1: 999.868 Hz, -76.9 dB | -78.2 | 40.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5448 | 0.0012 | 10/10 | k=1: 2320.545 Hz, -117.3 dB | -113.8 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9916 | 0.0040 | 3/19 | k=1: 49.990 Hz, -94.0 dB | -96.6 | 0.6 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8673 | 0.0007 | 163 | k=8·f1+1·f2: 13998.938 Hz, -95.4 dB | -85.6 | 7.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.1 | 18.5 % |
| 1-kHz-Kamm | Kanal 4 | 999.8673 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -75.0 | 47.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5448 | 0.0017 | 10/10 | k=1: 2320.545 Hz, -115.4 dB | -112.1 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9896 | 0.0001 | 2/19 | k=1: 49.990 Hz, -94.2 dB | -96.8 | 0.3 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8673 | 0.0010 | 149 | k=8·f1+1·f2: 13998.938 Hz, -95.3 dB | -85.5 | 4.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 56.6 | usb1k·1 |
| 6000.000 | -78.9 | 55.8 | fs8·1 |
| 18000.000 | -82.1 | 54.6 | fs8·3 |
| 12000.000 | -82.2 | 53.8 | fs8·2 |
| 2999.602 | -82.8 | 50.7 | usb1k·3 |
| 1999.734 | -82.2 | 50.8 | usb1k·2 |
| 6999.072 | -87.5 | 47.3 | usb1k·7 |
| 15997.878 | -91.3 | 45.1 | usb1k·16 |
| 49.990 | -92.5 | 29.3 | mains50·1 |
| 9998.674 | -92.5 | 43.4 | usb1k·10 |
| 5999.204 | -95.1 | 39.7 | usb1k·6 |
| 10998.540 | -94.4 | 41.4 | usb1k·11 |
| 14998.010 | -95.6 | 40.2 | usb1k·15 |
| 13998.938 | -95.2 | 40.8 | imd·8·f1+1·f2 |
| 15999.470 | -95.8 | 40.6 | imd·4·f1+2·f2 |
| 4999.336 | -96.3 | 37.9 | usb1k·5 |
| 9999.470 | -96.3 | 39.7 | imd·4·f1+1·f2 |
| 11998.408 | -97.2 | 38.9 | usb1k·12 |
| 19998.938 | -96.5 | 40.1 | imd·8·f1+2·f2 |
| 12999.071 | -97.0 | 39.2 | imd·7·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 57.4 | usb1k·1 |
| 6000.000 | -78.8 | 57.4 | fs8·1 |
| 12000.000 | -82.0 | 56.1 | fs8·2 |
| 18000.000 | -82.1 | 56.5 | fs8·3 |
| 2999.602 | -83.4 | 51.7 | usb1k·3 |
| 1999.734 | -83.1 | 51.4 | usb1k·2 |
| 6999.072 | -87.8 | 48.4 | usb1k·7 |
| 15997.878 | -91.7 | 46.3 | usb1k·16 |
| 49.990 | -93.4 | 30.3 | mains50·1 |
| 9998.674 | -92.7 | 44.8 | usb1k·10 |
| 14998.010 | -95.3 | 42.2 | usb1k·15 |
| 10998.540 | -94.6 | 42.7 | usb1k·11 |
| 5999.204 | -95.7 | 40.5 | usb1k·6 |
| 13998.938 | -95.2 | 42.6 | imd·8·f1+1·f2 |
| 15999.470 | -95.7 | 42.3 | imd·4·f1+2·f2 |
| 9999.470 | -96.1 | 41.3 | imd·4·f1+1·f2 |
| 19998.938 | -96.3 | 42.0 | imd·8·f1+2·f2 |
| 11998.408 | -97.2 | 40.8 | usb1k·12 |
| 7998.939 | -96.9 | 40.1 | usb1k·8 |
| 12999.071 | -96.8 | 40.9 | imd·7·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -76.9 | 60.5 | usb1k·1 |
| 6000.000 | -79.2 | 60.6 | fs8·1 |
| 12000.000 | -82.0 | 59.0 | fs8·2 |
| 18000.000 | -82.3 | 58.7 | fs8·3 |
| 2999.602 | -84.6 | 54.5 | usb1k·3 |
| 1999.734 | -85.2 | 53.8 | usb1k·2 |
| 6999.072 | -88.5 | 51.4 | usb1k·7 |
| 15997.878 | -92.8 | 47.9 | usb1k·16 |
| 9998.674 | -93.2 | 47.1 | usb1k·10 |
| 49.990 | -94.0 | 34.8 | mains50·1 |
| 14998.010 | -95.5 | 45.6 | usb1k·15 |
| 10998.540 | -95.1 | 45.6 | usb1k·11 |
| 13998.938 | -95.4 | 45.5 | imd·8·f1+1·f2 |
| 15999.470 | -96.0 | 44.7 | imd·4·f1+2·f2 |
| 9999.470 | -96.4 | 44.1 | imd·4·f1+1·f2 |
| 19998.938 | -96.6 | 44.3 | imd·8·f1+2·f2 |
| 11998.408 | -97.6 | 43.5 | usb1k·12 |
| 7998.938 | -96.9 | 43.5 | usb1k·8 |
| 5999.204 | -97.7 | 42.0 | usb1k·6 |
| 12999.072 | -97.0 | 43.7 | imd·7·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 58.7 | usb1k·1 |
| 6000.000 | -79.0 | 56.3 | fs8·1 |
| 1999.734 | -80.6 | 53.7 | usb1k·2 |
| 18000.000 | -82.2 | 54.7 | fs8·3 |
| 12000.000 | -82.2 | 54.8 | fs8·2 |
| 2999.602 | -82.5 | 51.7 | usb1k·3 |
| 6999.072 | -87.5 | 47.9 | usb1k·7 |
| 15997.878 | -90.9 | 45.8 | usb1k·16 |
| 9998.673 | -92.1 | 44.1 | usb1k·10 |
| 5999.204 | -93.2 | 42.1 | usb1k·6 |
| 4999.336 | -93.0 | 41.5 | usb1k·5 |
| 49.990 | -94.2 | 29.7 | mains50·1 |
| 10998.540 | -94.2 | 41.9 | usb1k·11 |
| 14998.010 | -95.4 | 40.5 | usb1k·15 |
| 13998.938 | -95.3 | 41.6 | imd·8·f1+1·f2 |
| 15999.470 | -95.9 | 40.9 | imd·4·f1+2·f2 |
| 11998.408 | -97.0 | 40.1 | usb1k·12 |
| 20997.214 | -97.1 | 40.1 | usb1k·21 |
| 9999.470 | -96.4 | 39.9 | imd·4·f1+1·f2 |
| 19998.938 | -96.5 | 40.9 | imd·8·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.02 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.12 | 0.01 | 0.02 |
| led | Kanal 1 | 11/11 | 1.69 | -0.68 | 0.79 |
| mains50 | Kanal 1 | 11/11 | 181.40 | 80.90 | 0.66 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.10 | 0.02 | 0.02 |
| led | Kanal 2 | 11/11 | 0.41 | 0.37 | 0.52 |
| mains50 | Kanal 2 | 11/11 | 155.75 | 52.09 | 0.61 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.09 | 0.05 | 0.02 |
| led | Kanal 3 | 11/11 | 1.17 | -0.07 | 0.57 |
| mains50 | Kanal 3 | 11/11 | 118.63 | 212.62 | 0.30 |
| fs8 | Kanal 4 | 11/11 | 0.02 | 0.02 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.08 | 0.04 | 0.02 |
| led | Kanal 4 | 11/11 | 1.41 | -0.09 | 0.58 |
| mains50 | Kanal 4 | 11/11 | 183.47 | 47.44 | 0.59 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.67 | 1.26 s (0.80 Hz) | 16.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.78 | 1.26 s (0.80 Hz) | 31.5 |
| Kanal 2 | breitbandig | 0.57 | 1.26 s (0.80 Hz) | 19.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.77 | 1.26 s (0.80 Hz) | 33.5 |
| Kanal 3 | breitbandig | 0.36 | 1.26 s (0.80 Hz) | 25.7 |
| Kanal 3 | 999.9 Hz ± 10 | 0.76 | 1.26 s (0.80 Hz) | 37.0 |
| Kanal 4 | breitbandig | 0.49 | 1.26 s (0.80 Hz) | 21.6 |
| Kanal 4 | 999.9 Hz ± 10 | 0.76 | 1.26 s (0.80 Hz) | 31.5 |

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
| Kanal 1 | 1.00 | 0.98 | 0.94 | 0.95 |
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.94 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz A5-b1d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.8 | -72.1 | +0.3 | 63 % | 63 % |
| Kanal 2 | -72.6 | -73.0 | +0.4 | 70 % | 68 % |
| Kanal 3 | -74.2 | -74.6 | +0.3 | 80 % | 78 % |
| Kanal 4 | -71.8 | -73.4 | +1.6 | 71 % | 69 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx1d-r2_psd.png)

### Kammprofile

![Kammprofile](B3-fx1d-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx1d-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 16:20–16:21, Host-Software vorher neu gestartet.
