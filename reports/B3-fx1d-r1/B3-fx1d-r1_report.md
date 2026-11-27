# Report B3-fx1d-r1: B3-fx1d-r1 – acdc1 Build 2, rohe Eingänge offen, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 2 v22.4.r-fx1d (Build 1d + TX_PRE_FX) |
| test | Abnahme A5/B3 1/2: Eingänge offen, rohe ADC-Daten (vor dem Patch), Vergleich mit A5-b1d-r1/r2 (D24) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx1d-open-inputs-r1_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx1d-r1 --ref A5-b1d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -70.6 | -76.6 | -71.9 | -73.0 | -85.5 | -72.3 | – | -71.9 | 63 % | -76.2 | 4.4 |
| Kanal 2 | -6.8 | -71.4 | -77.5 | -72.7 | -73.8 | -87.5 | -73.0 | – | -72.7 | 70 % | -77.8 | 5.2 |
| Kanal 3 | -5.0 | -73.7 | -83.0 | -74.3 | -75.6 | -91.3 | -74.6 | – | -74.3 | 80 % | -81.3 | 7.0 |
| Kanal 4 | -5.9 | -70.8 | -77.6 | -71.8 | -72.8 | -88.0 | -72.1 | – | -71.8 | 70 % | -77.1 | 5.3 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.0 | 19.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8673 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.4 dB | -75.9 | 39.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0023 | 9/10 | k=1: 2320.541 Hz, -116.1 dB | -112.9 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9860 | 0.0010 | 2/19 | k=1: 49.987 Hz, -93.3 dB | -95.8 | 0.4 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8673 | 0.0009 | 144 | k=8·f1+1·f2: 13998.938 Hz, -95.4 dB | -85.5 | 4.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.9 dB | -78.9 | 23.7 % |
| 1-kHz-Kamm | Kanal 2 | 999.8673 | 0.0002 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.6 | 40.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0014 | 10/10 | k=9: 20884.903 Hz, -115.4 dB | -110.2 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9853 | 0.0047 | 4/19 | k=1: 49.987 Hz, -94.2 dB | -96.5 | 0.4 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8673 | 0.0010 | 154 | k=8·f1+1·f2: 13998.938 Hz, -95.4 dB | -85.4 | 5.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.1 | 32.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8673 | 0.0002 | 23/23 | k=1: 999.868 Hz, -77.0 dB | -78.3 | 39.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0009 | 10/10 | k=1: 2320.543 Hz, -117.5 dB | -113.6 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9843 | 0.0055 | 6/19 | k=1: 49.987 Hz, -94.6 dB | -96.9 | 0.5 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8673 | 0.0007 | 163 | k=8·f1+1·f2: 13998.938 Hz, -95.5 dB | -85.6 | 7.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.1 | 18.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8673 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.6 dB | -75.0 | 47.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5446 | 0.0016 | 10/10 | k=1: 2320.544 Hz, -115.7 dB | -111.9 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9848 | 0.0020 | 3/19 | k=1: 49.986 Hz, -95.0 dB | -97.4 | 0.3 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8673 | 0.0009 | 144 | k=8·f1+1·f2: 13998.938 Hz, -95.5 dB | -85.6 | 4.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.4 | 57.6 | usb1k·1 |
| 6000.000 | -79.0 | 56.0 | fs8·1 |
| 18000.000 | -82.0 | 54.8 | fs8·3 |
| 12000.000 | -82.2 | 53.8 | fs8·2 |
| 2999.602 | -82.9 | 50.5 | usb1k·3 |
| 1999.734 | -82.2 | 50.6 | usb1k·2 |
| 6999.071 | -87.5 | 47.3 | usb1k·7 |
| 15997.876 | -91.5 | 45.0 | usb1k·16 |
| 9998.673 | -92.5 | 43.0 | usb1k·10 |
| 49.987 | -93.3 | 28.6 | mains50·1 |
| 10998.540 | -94.4 | 41.6 | usb1k·11 |
| 5999.204 | -95.4 | 39.6 | usb1k·6 |
| 14998.009 | -95.7 | 40.9 | usb1k·15 |
| 13998.938 | -95.4 | 41.1 | imd·8·f1+1·f2 |
| 15999.469 | -95.8 | 40.6 | imd·4·f1+2·f2 |
| 19998.938 | -96.3 | 39.9 | imd·8·f1+2·f2 |
| 4999.336 | -96.4 | 36.8 | usb1k·5 |
| 9999.469 | -96.4 | 39.1 | imd·4·f1+1·f2 |
| 11998.407 | -97.4 | 38.5 | usb1k·12 |
| 14999.602 | -97.8 | 38.8 | imd·3·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 58.3 | usb1k·1 |
| 6000.000 | -78.9 | 57.5 | fs8·1 |
| 18000.000 | -81.9 | 56.6 | fs8·3 |
| 12000.000 | -81.9 | 55.4 | fs8·2 |
| 2999.602 | -83.4 | 51.5 | usb1k·3 |
| 1999.734 | -83.1 | 51.4 | usb1k·2 |
| 6999.071 | -87.8 | 48.7 | usb1k·7 |
| 15997.877 | -91.9 | 46.2 | usb1k·16 |
| 9998.673 | -92.7 | 44.1 | usb1k·10 |
| 49.987 | -94.2 | 30.2 | mains50·1 |
| 14998.009 | -95.3 | 43.0 | usb1k·15 |
| 10998.540 | -94.6 | 42.8 | usb1k·11 |
| 5999.203 | -96.0 | 40.4 | usb1k·6 |
| 13998.938 | -95.4 | 42.8 | imd·8·f1+1·f2 |
| 15999.469 | -95.8 | 42.3 | imd·4·f1+2·f2 |
| 19998.938 | -96.2 | 41.8 | imd·8·f1+2·f2 |
| 9999.469 | -96.3 | 40.5 | imd·4·f1+1·f2 |
| 11998.407 | -97.2 | 40.1 | usb1k·12 |
| 14999.602 | -97.6 | 40.6 | imd·3·f1+2·f2 |
| 12999.071 | -96.9 | 40.7 | imd·7·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -77.0 | 61.3 | usb1k·1 |
| 6000.000 | -79.3 | 60.8 | fs8·1 |
| 12000.000 | -82.0 | 58.7 | fs8·2 |
| 18000.000 | -82.1 | 58.9 | fs8·3 |
| 2999.602 | -84.7 | 54.6 | usb1k·3 |
| 1999.734 | -85.2 | 53.3 | usb1k·2 |
| 6999.071 | -88.6 | 51.3 | usb1k·7 |
| 15997.876 | -92.9 | 48.0 | usb1k·16 |
| 9998.673 | -93.2 | 47.0 | usb1k·10 |
| 49.987 | -94.6 | 33.9 | mains50·1 |
| 14998.009 | -95.5 | 45.6 | usb1k·15 |
| 10998.540 | -95.2 | 45.5 | usb1k·11 |
| 13998.938 | -95.5 | 45.3 | imd·8·f1+1·f2 |
| 15999.469 | -96.0 | 44.8 | imd·4·f1+2·f2 |
| 19998.938 | -96.4 | 44.5 | imd·8·f1+2·f2 |
| 9999.469 | -96.5 | 43.8 | imd·4·f1+1·f2 |
| 11998.407 | -97.7 | 43.1 | usb1k·12 |
| 7998.938 | -97.0 | 42.5 | usb1k·8 |
| 14999.602 | -98.0 | 43.0 | imd·3·f1+2·f2 |
| 12999.071 | -97.2 | 43.5 | imd·7·f1+1·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.6 | 59.3 | usb1k·1 |
| 6000.000 | -79.0 | 56.5 | fs8·1 |
| 1999.734 | -80.6 | 53.3 | usb1k·2 |
| 12000.000 | -82.2 | 54.2 | fs8·2 |
| 18000.000 | -82.2 | 54.8 | fs8·3 |
| 2999.602 | -82.6 | 51.6 | usb1k·3 |
| 6999.071 | -87.6 | 48.2 | usb1k·7 |
| 15997.877 | -91.1 | 45.8 | usb1k·16 |
| 9998.673 | -92.1 | 43.5 | usb1k·10 |
| 5999.204 | -93.3 | 42.2 | usb1k·6 |
| 4999.336 | -93.2 | 40.8 | usb1k·5 |
| 10998.540 | -94.2 | 42.0 | usb1k·11 |
| 49.986 | -95.0 | 29.8 | mains50·1 |
| 14998.009 | -95.4 | 42.1 | usb1k·15 |
| 13998.938 | -95.5 | 40.7 | imd·8·f1+1·f2 |
| 15999.470 | -96.0 | 40.9 | imd·4·f1+2·f2 |
| 11998.407 | -97.0 | 39.4 | usb1k·12 |
| 19998.938 | -96.4 | 40.6 | imd·8·f1+2·f2 |
| 9999.469 | -96.5 | 39.2 | imd·4·f1+1·f2 |
| 20997.213 | -97.3 | 40.1 | usb1k·21 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.18 | 0.02 | 0.02 |
| led | Kanal 1 | 11/11 | 3.56 | 6.95 | 0.78 |
| mains50 | Kanal 1 | 11/11 | 245.16 | 200.04 | 0.61 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.15 | 0.07 | 0.02 |
| led | Kanal 2 | 11/11 | 0.44 | 0.27 | 0.56 |
| mains50 | Kanal 2 | 11/11 | 468.27 | 1055.38 | 0.53 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.11 | 0.03 | 0.01 |
| led | Kanal 3 | 11/11 | 1.84 | 0.25 | 0.51 |
| mains50 | Kanal 3 | 11/11 | 237.54 | -52.39 | 0.32 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.00 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.12 | 0.08 | 0.02 |
| led | Kanal 4 | 11/11 | 1.01 | 2.28 | 0.61 |
| mains50 | Kanal 4 | 11/11 | 217.99 | -214.06 | 0.59 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.09 | 0.16 s (6.40 Hz) | 28.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.63 | 1.26 s (0.80 Hz) | 31.4 |
| Kanal 2 | breitbandig | 1.00 | 0.16 s (6.40 Hz) | 30.0 |
| Kanal 2 | 999.9 Hz ± 10 | 0.63 | 1.26 s (0.80 Hz) | 33.3 |
| Kanal 3 | breitbandig | 0.58 | 0.16 s (6.40 Hz) | 27.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.62 | 1.26 s (0.80 Hz) | 37.3 |
| Kanal 4 | breitbandig | 0.84 | 0.16 s (6.40 Hz) | 30.4 |
| Kanal 4 | 999.9 Hz ± 10 | 0.61 | 1.26 s (0.80 Hz) | 32.0 |

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
| Kanal 1 | 1.00 | 0.98 | 0.93 | 0.95 |
| Kanal 2 | 0.98 | 1.00 | 0.94 | 0.97 |
| Kanal 3 | 0.93 | 0.94 | 1.00 | 0.92 |
| Kanal 4 | 0.95 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz A5-b1d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.9 | -72.1 | +0.3 | 63 % | 63 % |
| Kanal 2 | -72.7 | -73.0 | +0.4 | 70 % | 68 % |
| Kanal 3 | -74.3 | -74.6 | +0.3 | 80 % | 78 % |
| Kanal 4 | -71.8 | -73.4 | +1.6 | 70 % | 69 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx1d-r1_psd.png)

### Kammprofile

![Kammprofile](B3-fx1d-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx1d-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 16:18–16:19.
