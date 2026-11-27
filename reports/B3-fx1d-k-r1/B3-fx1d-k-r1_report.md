# Report B3-fx1d-k-r1: B3-fx1d-k-r1 – acdc1 Build 2 (Kontrolle), rohe Eingänge offen, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 2 v22.4.r-fx1d (zurückgeflasht nach Build 3b, Kontrolle) |
| test | Kontrolle 1/2 zu D30: Eingänge offen, rohe ADC-Daten, gleiche Sitzung wie B3-fx2b-r1/r2 (Firmware- oder Sitzungseffekt?) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx1d-kontrolle-open-inputs-r1_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx1d-k-r1 --ref B3-fx1d-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.4 | -70.2 | -75.4 | -71.8 | -73.0 | -85.3 | -72.2 | – | -71.8 | 62 % | -76.0 | 4.2 |
| Kanal 2 | -6.8 | -71.5 | -77.6 | -72.7 | -73.9 | -87.2 | -73.1 | – | -72.7 | 68 % | -77.6 | 4.9 |
| Kanal 3 | -5.0 | -72.8 | -78.2 | -74.3 | -75.6 | -91.1 | -74.6 | – | -74.3 | 79 % | -81.0 | 6.7 |
| Kanal 4 | -5.9 | -71.2 | -79.6 | -71.9 | -72.9 | -87.6 | -72.2 | – | -71.9 | 69 % | -77.0 | 5.1 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -78.9 dB | -79.0 | 18.9 % |
| 1-kHz-Kamm | Kanal 1 | 999.8672 | 0.0003 | 23/23 | k=1: 999.867 Hz, -74.4 dB | -76.0 | 38.0 % |
| Netz 50 Hz | Kanal 1 | 49.9811 | 0.0003 | 2/19 | k=1: 49.981 Hz, -92.9 dB | -95.7 | 0.4 % |
| Mischprodukte n·999.8672 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8672 | 0.0012 | 150 | k=8·f1+1·f2: 13998.937 Hz, -95.5 dB | -85.5 | 4.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.9 dB | -79.0 | 23.6 % |
| 1-kHz-Kamm | Kanal 2 | 999.8672 | 0.0003 | 23/23 | k=1: 999.867 Hz, -75.4 dB | -76.9 | 38.3 % |
| Netz 50 Hz | Kanal 2 | 49.9812 | 0.0003 | 2/19 | k=1: 49.981 Hz, -93.4 dB | -96.1 | 0.5 % |
| Mischprodukte n·999.8672 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8672 | 0.0010 | 156 | k=8·f1+1·f2: 13998.937 Hz, -95.3 dB | -85.4 | 5.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.2 | 32.5 % |
| 1-kHz-Kamm | Kanal 3 | 999.8672 | 0.0004 | 23/23 | k=1: 999.867 Hz, -77.1 dB | -78.5 | 38.3 % |
| Netz 50 Hz | Kanal 3 | 49.9818 | 0.0007 | 4/19 | k=1: 49.982 Hz, -94.2 dB | -96.9 | 0.6 % |
| Mischprodukte n·999.8672 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8672 | 0.0009 | 162 | k=8·f1+1·f2: 13998.937 Hz, -95.6 dB | -85.6 | 7.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -79.1 dB | -79.2 | 18.6 % |
| 1-kHz-Kamm | Kanal 4 | 999.8672 | 0.0003 | 23/23 | k=1: 999.867 Hz, -73.7 dB | -75.3 | 46.0 % |
| Netz 50 Hz | Kanal 4 | 49.9812 | 0.0003 | 2/19 | k=1: 49.981 Hz, -94.5 dB | -97.2 | 0.3 % |
| Mischprodukte n·999.8672 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8672 | 0.0014 | 150 | k=8·f1+1·f2: 13998.937 Hz, -95.7 dB | -85.6 | 4.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -74.4 | 55.5 | usb1k·1 |
| 6000.000 | -78.9 | 55.3 | fs8·1 |
| 18000.000 | -82.2 | 54.8 | fs8·3 |
| 12000.000 | -82.3 | 53.6 | fs8·2 |
| 2999.601 | -83.1 | 49.6 | usb1k·3 |
| 1999.734 | -82.9 | 48.1 | usb1k·2 |
| 6999.071 | -87.7 | 47.0 | usb1k·7 |
| 15997.875 | -91.9 | 45.0 | usb1k·16 |
| 9998.672 | -92.3 | 43.1 | usb1k·10 |
| 49.981 | -92.9 | 26.6 | mains50·1 |
| 5999.203 | -95.3 | 38.8 | usb1k·6 |
| 10998.539 | -94.0 | 41.8 | usb1k·11 |
| 14998.008 | -95.4 | 41.4 | usb1k·15 |
| 15999.469 | -95.9 | 41.1 | imd·4·f1+2·f2 |
| 9999.469 | -96.3 | 39.1 | imd·4·f1+1·f2 |
| 13998.937 | -95.5 | 40.9 | imd·8·f1+1·f2 |
| 4999.336 | -96.2 | 37.9 | usb1k·5 |
| 12999.867 | -96.9 | 39.7 | imd·1·f1+2·f2 |
| 12999.071 | -97.2 | 39.4 | imd·7·f1+1·f2 |
| 11998.406 | -97.6 | 38.3 | usb1k·12 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.4 | 56.4 | usb1k·1 |
| 6000.000 | -78.9 | 56.9 | fs8·1 |
| 12000.000 | -82.0 | 55.3 | fs8·2 |
| 18000.000 | -82.1 | 56.5 | fs8·3 |
| 2999.601 | -83.7 | 50.9 | usb1k·3 |
| 1999.734 | -83.8 | 49.4 | usb1k·2 |
| 6999.071 | -87.9 | 48.7 | usb1k·7 |
| 15997.875 | -92.2 | 46.2 | usb1k·16 |
| 9998.672 | -92.6 | 44.4 | usb1k·10 |
| 49.981 | -93.4 | 28.4 | mains50·1 |
| 14998.008 | -95.3 | 42.8 | usb1k·15 |
| 10998.539 | -94.1 | 42.9 | usb1k·11 |
| 5999.203 | -96.2 | 39.7 | usb1k·6 |
| 15999.469 | -95.8 | 42.7 | imd·4·f1+2·f2 |
| 13998.937 | -95.3 | 42.7 | imd·8·f1+1·f2 |
| 9999.469 | -96.2 | 40.9 | imd·4·f1+1·f2 |
| 12999.071 | -97.0 | 40.9 | imd·7·f1+1·f2 |
| 11998.406 | -97.3 | 39.9 | usb1k·12 |
| 12999.867 | -96.9 | 41.0 | imd·1·f1+2·f2 |
| 14999.601 | -97.7 | 40.4 | imd·3·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -77.1 | 59.1 | usb1k·1 |
| 6000.000 | -79.2 | 60.0 | fs8·1 |
| 12000.000 | -82.1 | 58.5 | fs8·2 |
| 18000.000 | -82.3 | 58.8 | fs8·3 |
| 2999.602 | -85.1 | 53.5 | usb1k·3 |
| 1999.734 | -86.0 | 51.3 | usb1k·2 |
| 6999.071 | -88.8 | 51.0 | usb1k·7 |
| 9998.672 | -93.0 | 46.9 | usb1k·10 |
| 15997.875 | -93.3 | 47.8 | usb1k·16 |
| 49.982 | -94.2 | 32.0 | mains50·1 |
| 14998.008 | -95.3 | 45.8 | usb1k·15 |
| 10998.539 | -94.9 | 45.5 | usb1k·11 |
| 15999.469 | -96.1 | 45.0 | imd·4·f1+2·f2 |
| 9999.469 | -96.4 | 43.6 | imd·4·f1+1·f2 |
| 13998.937 | -95.6 | 45.5 | imd·8·f1+1·f2 |
| 12999.071 | -97.3 | 43.3 | imd·7·f1+1·f2 |
| 12999.867 | -97.1 | 43.6 | imd·1·f1+2·f2 |
| 19998.938 | -96.7 | 44.4 | imd·8·f1+2·f2 |
| 5999.203 | -98.0 | 41.3 | usb1k·6 |
| 11998.406 | -97.9 | 42.7 | usb1k·12 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -73.7 | 57.6 | usb1k·1 |
| 6000.000 | -79.1 | 55.9 | fs8·1 |
| 12000.000 | -82.1 | 54.2 | fs8·2 |
| 1999.734 | -81.2 | 51.4 | usb1k·2 |
| 18000.000 | -82.5 | 54.8 | fs8·3 |
| 2999.601 | -82.7 | 51.5 | usb1k·3 |
| 6999.071 | -87.6 | 47.8 | usb1k·7 |
| 15997.875 | -91.3 | 46.2 | usb1k·16 |
| 9998.672 | -92.1 | 43.9 | usb1k·10 |
| 5999.203 | -93.3 | 41.8 | usb1k·6 |
| 4999.335 | -93.2 | 41.8 | usb1k·5 |
| 49.981 | -94.5 | 27.5 | mains50·1 |
| 10998.539 | -93.9 | 42.1 | usb1k·11 |
| 14998.008 | -95.3 | 41.6 | usb1k·15 |
| 15999.469 | -96.1 | 41.6 | imd·4·f1+2·f2 |
| 9999.469 | -96.2 | 39.9 | imd·4·f1+1·f2 |
| 11998.406 | -96.8 | 39.4 | usb1k·12 |
| 13998.937 | -95.7 | 41.0 | imd·8·f1+1·f2 |
| 12999.071 | -97.0 | 39.5 | imd·7·f1+1·f2 |
| 14999.601 | -97.4 | 39.7 | imd·3·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | -0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.14 | 0.30 | 0.09 |
| mains50 | Kanal 1 | 11/11 | 163.44 | -117.05 | 0.37 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.13 | 0.18 | 0.06 |
| mains50 | Kanal 2 | 11/11 | 116.27 | -51.62 | 0.38 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.09 | 0.21 | 0.10 |
| mains50 | Kanal 3 | 11/11 | 342.25 | -641.96 | 0.24 |
| fs8 | Kanal 4 | 11/11 | 0.02 | -0.00 | 0.05 |
| usb1k | Kanal 4 | 11/11 | 0.11 | 0.12 | 0.17 |
| mains50 | Kanal 4 | 11/11 | 127.94 | -46.44 | 0.58 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.30 | 0.31 s (3.22 Hz) | 23.3 |
| Kanal 1 | 999.9 Hz ± 10 | 0.88 | 1.26 s (0.80 Hz) | 27.8 |
| Kanal 2 | breitbandig | 1.10 | 0.31 s (3.22 Hz) | 24.6 |
| Kanal 2 | 999.9 Hz ± 10 | 0.87 | 1.26 s (0.80 Hz) | 30.1 |
| Kanal 3 | breitbandig | 1.12 | 0.31 s (3.18 Hz) | 24.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.86 | 1.26 s (0.80 Hz) | 33.9 |
| Kanal 4 | breitbandig | 0.75 | 0.31 s (3.22 Hz) | 24.3 |
| Kanal 4 | 999.9 Hz ± 10 | 0.87 | 1.26 s (0.80 Hz) | 30.0 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.93 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.96 |
| Kanal 3 | 0.95 | 0.96 | 1.00 | 0.90 |
| Kanal 4 | 0.93 | 0.96 | 0.90 | 1.00 |

## Vergleich mit Referenz B3-fx1d-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.8 | -71.9 | +0.1 | 62 % | 63 % |
| Kanal 2 | -72.7 | -72.7 | -0.1 | 68 % | 70 % |
| Kanal 3 | -74.3 | -74.3 | -0.0 | 79 % | 80 % |
| Kanal 4 | -71.9 | -71.8 | -0.1 | 69 % | 70 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx1d-k-r1_psd.png)

### Kammprofile

![Kammprofile](B3-fx1d-k-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx1d-k-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 17:49–17:52, Host-Software vor jedem Lauf neu gestartet.
