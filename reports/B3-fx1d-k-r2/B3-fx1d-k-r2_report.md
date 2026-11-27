# Report B3-fx1d-k-r2: B3-fx1d-k-r2 – acdc1 Build 2 (Kontrolle), rohe Eingänge offen, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 2 v22.4.r-fx1d (zurückgeflasht nach Build 3b, Kontrolle) |
| test | Kontrolle 2/2 zu D30: Eingänge offen, rohe ADC-Daten, gleiche Sitzung wie B3-fx2b-r1/r2 (Firmware- oder Sitzungseffekt?) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx1d-kontrolle-open-inputs-r2_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx1d-k-r2 --ref B3-fx1d-r2 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.4 | -71.0 | -79.0 | -71.8 | -73.0 | -85.0 | -72.2 | – | -71.8 | 62 % | -76.0 | 4.2 |
| Kanal 2 | -6.8 | -72.1 | -81.3 | -72.7 | -73.9 | -87.0 | -73.1 | – | -72.7 | 68 % | -77.6 | 5.0 |
| Kanal 3 | -5.0 | -73.7 | -82.9 | -74.2 | -75.5 | -90.8 | -74.6 | – | -74.2 | 79 % | -81.0 | 6.8 |
| Kanal 4 | -5.9 | -71.4 | -82.9 | -71.8 | -72.7 | -87.5 | -72.1 | – | -71.8 | 70 % | -77.0 | 5.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.1 | 18.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8673 | 0.0003 | 23/23 | k=1: 999.867 Hz, -74.4 dB | -75.9 | 38.4 % |
| Netz 50 Hz | Kanal 1 | 49.9998 | 0.0057 | 3/19 | k=1: 49.996 Hz, -92.9 dB | -95.6 | 0.4 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8673 | 0.0008 | 143 | k=8·f1+1·f2: 13998.939 Hz, -95.5 dB | -85.5 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.9 dB | -79.0 | 23.5 % |
| 1-kHz-Kamm | Kanal 2 | 999.8673 | 0.0003 | 23/23 | k=1: 999.867 Hz, -75.3 dB | -76.8 | 38.9 % |
| Netz 50 Hz | Kanal 2 | 49.9997 | 0.0059 | 3/19 | k=1: 49.996 Hz, -93.6 dB | -96.2 | 0.4 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8673 | 0.0007 | 155 | k=8·f1+1·f2: 13998.939 Hz, -95.4 dB | -85.4 | 5.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.3 dB | -79.2 | 31.9 % |
| 1-kHz-Kamm | Kanal 3 | 999.8673 | 0.0003 | 23/23 | k=1: 999.867 Hz, -76.9 dB | -78.3 | 39.5 % |
| Netz 50 Hz | Kanal 3 | 49.9988 | 0.0131 | 6/19 | k=1: 49.996 Hz, -94.2 dB | -96.8 | 0.6 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8673 | 0.0008 | 164 | k=8·f1+1·f2: 13998.939 Hz, -95.6 dB | -85.6 | 7.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.2 | 18.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8673 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.4 dB | -75.0 | 47.4 % |
| Netz 50 Hz | Kanal 4 | 49.9991 | 0.0115 | 4/19 | k=1: 49.996 Hz, -94.7 dB | -97.3 | 0.3 % |
| Mischprodukte n·999.8673 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8673 | 0.0008 | 145 | k=8·f1+1·f2: 13998.939 Hz, -95.6 dB | -85.6 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.4 | 55.8 | usb1k·1 |
| 6000.000 | -79.0 | 56.0 | fs8·1 |
| 18000.000 | -82.0 | 54.6 | fs8·3 |
| 12000.000 | -82.2 | 53.2 | fs8·2 |
| 2999.602 | -82.9 | 50.7 | usb1k·3 |
| 1999.735 | -82.5 | 48.9 | usb1k·2 |
| 6999.071 | -87.5 | 46.8 | usb1k·7 |
| 15997.877 | -91.5 | 44.4 | usb1k·16 |
| 49.996 | -92.9 | 29.1 | mains50·1 |
| 9998.673 | -92.5 | 42.8 | usb1k·10 |
| 10998.541 | -94.2 | 41.3 | usb1k·11 |
| 5999.204 | -95.5 | 39.6 | usb1k·6 |
| 14998.010 | -95.7 | 40.3 | usb1k·15 |
| 13998.939 | -95.5 | 39.9 | imd·8·f1+1·f2 |
| 15999.469 | -95.8 | 40.1 | imd·4·f1+2·f2 |
| 9999.469 | -96.3 | 39.0 | imd·4·f1+1·f2 |
| 11998.408 | -97.2 | 38.2 | usb1k·12 |
| 4999.337 | -96.7 | 37.1 | usb1k·5 |
| 19998.939 | -96.6 | 39.4 | imd·8·f1+2·f2 |
| 12999.071 | -97.1 | 38.6 | imd·7·f1+1·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.3 | 56.8 | usb1k·1 |
| 6000.000 | -78.9 | 57.4 | fs8·1 |
| 18000.000 | -82.0 | 56.0 | fs8·3 |
| 12000.000 | -82.0 | 55.2 | fs8·2 |
| 2999.602 | -83.5 | 52.0 | usb1k·3 |
| 1999.735 | -83.6 | 49.5 | usb1k·2 |
| 6999.071 | -87.9 | 48.4 | usb1k·7 |
| 15997.877 | -92.0 | 45.5 | usb1k·16 |
| 9998.673 | -92.7 | 44.0 | usb1k·10 |
| 49.996 | -93.6 | 30.5 | mains50·1 |
| 14998.010 | -95.3 | 42.5 | usb1k·15 |
| 10998.541 | -94.4 | 42.6 | usb1k·11 |
| 5999.204 | -96.2 | 40.1 | usb1k·6 |
| 13998.939 | -95.4 | 41.9 | imd·8·f1+1·f2 |
| 15999.469 | -95.8 | 41.6 | imd·4·f1+2·f2 |
| 9999.469 | -96.2 | 40.6 | imd·4·f1+1·f2 |
| 11998.408 | -97.1 | 40.0 | usb1k·12 |
| 19998.939 | -96.5 | 41.4 | imd·8·f1+2·f2 |
| 7998.939 | -96.6 | 39.8 | usb1k·8 |
| 12999.071 | -96.9 | 40.4 | imd·7·f1+1·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -76.9 | 59.7 | usb1k·1 |
| 6000.000 | -79.3 | 60.7 | fs8·1 |
| 12000.000 | -82.0 | 58.0 | fs8·2 |
| 18000.000 | -82.1 | 58.8 | fs8·3 |
| 2999.602 | -84.7 | 54.6 | usb1k·3 |
| 1999.735 | -85.4 | 51.8 | usb1k·2 |
| 6999.071 | -88.6 | 50.8 | usb1k·7 |
| 15997.877 | -92.9 | 47.3 | usb1k·16 |
| 9998.673 | -93.3 | 46.5 | usb1k·10 |
| 49.996 | -94.2 | 34.5 | mains50·1 |
| 14998.010 | -95.5 | 44.9 | usb1k·15 |
| 10998.541 | -95.1 | 45.1 | usb1k·11 |
| 13998.939 | -95.6 | 44.6 | imd·8·f1+1·f2 |
| 15999.469 | -96.0 | 44.0 | imd·4·f1+2·f2 |
| 9999.469 | -96.4 | 43.5 | imd·4·f1+1·f2 |
| 11998.408 | -97.5 | 42.3 | usb1k·12 |
| 7998.939 | -96.7 | 42.9 | usb1k·8 |
| 19998.939 | -96.7 | 43.7 | imd·8·f1+2·f2 |
| 12999.071 | -97.1 | 43.3 | imd·7·f1+1·f2 |
| 14999.602 | -98.0 | 42.3 | imd·3·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.4 | 58.2 | usb1k·1 |
| 6000.000 | -79.0 | 56.5 | fs8·1 |
| 1999.735 | -80.9 | 51.9 | usb1k·2 |
| 18000.000 | -82.3 | 54.2 | fs8·3 |
| 12000.000 | -82.3 | 54.1 | fs8·2 |
| 2999.602 | -82.5 | 52.3 | usb1k·3 |
| 6999.071 | -87.6 | 48.1 | usb1k·7 |
| 15997.877 | -91.2 | 45.3 | usb1k·16 |
| 9998.673 | -92.0 | 43.5 | usb1k·10 |
| 5999.204 | -93.5 | 42.1 | usb1k·6 |
| 4999.337 | -93.3 | 41.3 | usb1k·5 |
| 49.996 | -94.7 | 30.0 | mains50·1 |
| 10998.541 | -94.0 | 42.4 | usb1k·11 |
| 14998.010 | -95.4 | 40.8 | usb1k·15 |
| 13998.939 | -95.6 | 40.7 | imd·8·f1+1·f2 |
| 15999.469 | -96.0 | 40.5 | imd·4·f1+2·f2 |
| 11998.409 | -96.9 | 39.4 | usb1k·12 |
| 9999.469 | -96.3 | 39.3 | imd·4·f1+1·f2 |
| 8998.806 | -97.4 | 38.7 | usb1k·9 |
| 12999.867 | -96.8 | 39.6 | imd·1·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.12 | 0.05 | 0.02 |
| mains50 | Kanal 1 | 11/11 | 53.23 | -25.08 | 0.71 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.02 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.11 | 0.01 | 0.01 |
| mains50 | Kanal 2 | 11/11 | 44.11 | -36.54 | 0.68 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.09 | 0.03 | 0.02 |
| mains50 | Kanal 3 | 11/11 | 36.93 | -21.06 | 0.36 |
| fs8 | Kanal 4 | 11/11 | 0.01 | -0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.09 | 0.07 | 0.02 |
| mains50 | Kanal 4 | 11/11 | 53.67 | -48.15 | 0.71 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.85 | 1.26 s (0.80 Hz) | 16.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.80 | 1.26 s (0.80 Hz) | 28.4 |
| Kanal 2 | breitbandig | 0.70 | 1.26 s (0.80 Hz) | 19.7 |
| Kanal 2 | 999.9 Hz ± 10 | 0.80 | 1.26 s (0.80 Hz) | 30.7 |
| Kanal 3 | breitbandig | 0.61 | 1.26 s (0.80 Hz) | 24.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.79 | 1.26 s (0.80 Hz) | 35.3 |
| Kanal 4 | breitbandig | 0.50 | 1.26 s (0.80 Hz) | 24.0 |
| Kanal 4 | 999.9 Hz ± 10 | 0.78 | 1.26 s (0.80 Hz) | 30.8 |

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
| Kanal 1 | 1.00 | 0.97 | 0.95 | 0.93 |
| Kanal 2 | 0.97 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz B3-fx1d-r2

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.8 | -71.8 | +0.0 | 62 % | 63 % |
| Kanal 2 | -72.7 | -72.6 | -0.0 | 68 % | 70 % |
| Kanal 3 | -74.2 | -74.2 | +0.0 | 79 % | 80 % |
| Kanal 4 | -71.8 | -71.8 | +0.0 | 70 % | 71 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx1d-k-r2_psd.png)

### Kammprofile

![Kammprofile](B3-fx1d-k-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx1d-k-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 17:49–17:52, Host-Software vor jedem Lauf neu gestartet.
