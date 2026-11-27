# Report X1-rec: X1-rec – acdc1 x1-rec-open-inputs, 60 s

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Gegenprobe Werkzeug 2/2 (ITCM-Plan Q14): tools/acdc_rec.py, Eingänge offen, rohe ADC-Daten. Gegenstück: X1-vcv (Host-Software mit Mehrkanal-Recorder) |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_x1-rec-open-inputs_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis X1-rec --ref X1-vcv --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.2 | -69.2 | -71.8 | -72.7 | -74.4 | -85.4 | -73.3 | -103.8 | -72.7 | 48 % | -75.5 | 2.8 |
| Kanal 2 | -6.7 | -70.6 | -74.3 | -73.1 | -74.6 | -87.6 | -73.5 | – | -73.1 | 61 % | -77.2 | 4.1 |
| Kanal 3 | -4.9 | -72.7 | -76.4 | -75.0 | -76.9 | -91.3 | -75.5 | -104.0 | -75.1 | 70 % | -80.4 | 5.3 |
| Kanal 4 | -5.8 | -70.6 | -75.1 | -72.5 | -73.8 | -87.9 | -72.9 | – | -72.5 | 60 % | -76.4 | 4.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.2 | 22.3 % |
| 1-kHz-Kamm | Kanal 1 | 999.8666 | 0.0003 | 22/23 | k=1: 999.867 Hz, -78.9 dB | -79.7 | 19.9 % |
| Netz 50 Hz | Kanal 1 | 50.0214 | 0.0001 | 2/19 | k=1: 50.021 Hz, -93.5 dB | -96.4 | 0.4 % |
| Mischprodukte n·999.8666 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8666 | 0.0012 | 142 | k=8·f1+1·f2: 13998.933 Hz, -95.7 dB | -85.5 | 5.2 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 1 | 21000.0000 | 0.0000 | 1/1 | k=1: 21000.000 Hz, -100.8 dB | -103.8 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.2 dB | -79.1 | 24.9 % |
| 1-kHz-Kamm | Kanal 2 | 999.8666 | 0.0012 | 23/23 | k=1: 999.867 Hz, -77.2 dB | -78.3 | 29.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5449 | 0.0017 | 8/10 | k=9: 20884.904 Hz, -115.6 dB | -112.2 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0215 | 0.0001 | 2/19 | k=1: 50.021 Hz, -94.3 dB | -97.2 | 0.4 % |
| Mischprodukte n·999.8666 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8666 | 0.0011 | 153 | k=8·f1+1·f2: 13998.933 Hz, -95.6 dB | -85.4 | 5.8 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.5 dB | -79.3 | 37.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8666 | 0.0006 | 23/23 | k=1: 999.867 Hz, -80.9 dB | -81.3 | 24.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5451 | 0.0023 | 6/10 | k=7: 16243.819 Hz, -123.1 dB | -120.5 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0217 | 0.0001 | 2/19 | k=1: 50.022 Hz, -95.1 dB | -97.9 | 0.5 % |
| Mischprodukte n·999.8666 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8666 | 0.0016 | 162 | k=8·f1+1·f2: 13998.933 Hz, -95.9 dB | -85.7 | 8.7 % |
| stärkste übrige Linie (21000.00 Hz) | Kanal 3 | 21000.0000 | 0.0000 | 1/1 | k=1: 21000.000 Hz, -101.0 dB | -104.0 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -79.5 dB | -79.4 | 20.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8666 | 0.0005 | 23/23 | k=1: 999.867 Hz, -75.9 dB | -77.1 | 34.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5452 | 0.0022 | 4/10 | k=3: 6961.633 Hz, -120.6 dB | -118.9 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0214 | 0.0001 | 2/19 | k=1: 50.021 Hz, -94.9 dB | -97.8 | 0.3 % |
| Mischprodukte n·999.8666 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8666 | 0.0013 | 148 | k=8·f1+1·f2: 13998.933 Hz, -95.7 dB | -85.6 | 4.8 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -78.9 | 53.0 | usb1k·1 |
| 6000.000 | -79.2 | 54.4 | fs8·1 |
| 18000.000 | -82.1 | 53.6 | fs8·3 |
| 12000.000 | -82.3 | 50.7 | fs8·2 |
| 2999.600 | -85.2 | 48.0 | usb1k·3 |
| 1999.733 | -87.8 | 44.8 | usb1k·2 |
| 6999.066 | -89.1 | 45.1 | usb1k·7 |
| 9998.666 | -92.4 | 42.5 | usb1k·10 |
| 50.021 | -93.5 | 29.2 | mains50·1 |
| 15997.866 | -94.7 | 41.0 | usb1k·16 |
| 14997.999 | -95.3 | 40.6 | usb1k·15 |
| 13998.933 | -95.7 | 40.1 | imd·8·f1+1·f2 |
| 10998.533 | -95.7 | 39.1 | usb1k·11 |
| 15999.466 | -96.1 | 39.6 | imd·4·f1+2·f2 |
| 9999.467 | -96.3 | 38.6 | imd·4·f1+1·f2 |
| 7998.933 | -96.3 | 38.8 | usb1k·8 |
| 12999.067 | -96.8 | 38.4 | imd·7·f1+1·f2 |
| 19998.933 | -96.9 | 39.3 | imd·8·f1+2·f2 |
| 16998.533 | -97.2 | 38.4 | imd·11·f1+1·f2 |
| 12999.867 | -97.3 | 37.9 | imd·1·f1+2·f2 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -77.2 | 55.9 | usb1k·1 |
| 6000.000 | -79.2 | 56.2 | fs8·1 |
| 18000.000 | -82.1 | 55.3 | fs8·3 |
| 12000.000 | -82.2 | 53.1 | fs8·2 |
| 2999.600 | -84.4 | 50.4 | usb1k·3 |
| 1999.733 | -85.6 | 48.6 | usb1k·2 |
| 6999.066 | -88.8 | 47.0 | usb1k·7 |
| 9998.666 | -92.3 | 44.5 | usb1k·10 |
| 15997.866 | -93.7 | 43.8 | usb1k·16 |
| 50.021 | -94.3 | 30.6 | mains50·1 |
| 14997.999 | -95.2 | 42.0 | usb1k·15 |
| 10998.533 | -95.2 | 41.2 | usb1k·11 |
| 13998.933 | -95.6 | 41.5 | imd·8·f1+1·f2 |
| 15999.466 | -96.0 | 41.5 | imd·4·f1+2·f2 |
| 9999.467 | -96.2 | 40.6 | imd·4·f1+1·f2 |
| 12999.066 | -96.7 | 40.2 | imd·7·f1+1·f2 |
| 19998.933 | -96.9 | 40.6 | imd·8·f1+2·f2 |
| 16998.533 | -97.0 | 40.1 | imd·11·f1+1·f2 |
| 7998.933 | -97.1 | 39.0 | usb1k·8 |
| 12999.867 | -97.1 | 39.7 | imd·1·f1+2·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -79.5 | 59.3 | fs8·1 |
| 999.867 | -80.9 | 56.9 | usb1k·1 |
| 12000.000 | -82.1 | 56.0 | fs8·2 |
| 18000.000 | -82.3 | 57.4 | fs8·3 |
| 2999.600 | -86.6 | 51.9 | usb1k·3 |
| 1999.733 | -88.9 | 49.1 | usb1k·2 |
| 6999.066 | -90.0 | 49.1 | usb1k·7 |
| 9998.666 | -92.9 | 46.5 | usb1k·10 |
| 15997.866 | -95.3 | 44.5 | usb1k·16 |
| 14997.999 | -95.3 | 44.1 | usb1k·15 |
| 50.022 | -95.1 | 34.4 | mains50·1 |
| 13998.933 | -95.9 | 43.7 | imd·8·f1+1·f2 |
| 7998.933 | -95.9 | 43.5 | usb1k·8 |
| 15999.466 | -96.3 | 43.5 | imd·4·f1+2·f2 |
| 9999.467 | -96.4 | 42.9 | imd·4·f1+1·f2 |
| 10998.533 | -96.5 | 42.7 | usb1k·11 |
| 12999.066 | -96.9 | 42.6 | imd·7·f1+1·f2 |
| 19998.933 | -97.0 | 42.9 | imd·8·f1+2·f2 |
| 16998.533 | -97.1 | 42.0 | imd·11·f1+1·f2 |
| 12999.867 | -97.5 | 42.0 | imd·1·f1+2·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.867 | -75.9 | 56.5 | usb1k·1 |
| 6000.000 | -79.5 | 55.0 | fs8·1 |
| 18000.000 | -82.2 | 53.9 | fs8·3 |
| 12000.000 | -82.5 | 52.2 | fs8·2 |
| 1999.733 | -82.8 | 51.1 | usb1k·2 |
| 2999.600 | -84.0 | 49.7 | usb1k·3 |
| 6999.066 | -88.7 | 46.2 | usb1k·7 |
| 9998.666 | -92.5 | 42.9 | usb1k·10 |
| 15997.866 | -92.7 | 43.5 | usb1k·16 |
| 10998.533 | -95.0 | 40.4 | usb1k·11 |
| 14997.999 | -95.4 | 40.7 | usb1k·15 |
| 50.021 | -94.9 | 30.0 | mains50·1 |
| 5999.200 | -95.6 | 38.9 | usb1k·6 |
| 13998.933 | -95.7 | 40.4 | imd·8·f1+1·f2 |
| 15999.466 | -96.2 | 40.0 | imd·4·f1+2·f2 |
| 9999.467 | -96.5 | 38.9 | imd·4·f1+1·f2 |
| 19998.933 | -97.0 | 39.4 | imd·8·f1+2·f2 |
| 12999.066 | -97.0 | 38.8 | imd·7·f1+1·f2 |
| 18997.466 | -97.2 | 39.3 | usb1k·19 |
| 12999.867 | -97.2 | 38.6 | imd·1·f1+2·f2 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.04 | -0.01 | 0.03 |
| usb1k | Kanal 1 | 11/11 | 0.20 | 0.00 | 0.07 |
| mains50 | Kanal 1 | 11/11 | 427.12 | 78.01 | 0.73 |
| other1 | Kanal 1 | 11/11 | 0.17 | 0.04 | 0.34 |
| fs8 | Kanal 2 | 11/11 | 0.03 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.18 | 0.18 | 0.04 |
| led | Kanal 2 | 11/11 | 0.49 | 0.04 | 0.84 |
| mains50 | Kanal 2 | 11/11 | 187.24 | -80.91 | 0.70 |
| fs8 | Kanal 3 | 11/11 | 0.03 | 0.01 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.13 | 0.11 | 0.04 |
| led | Kanal 3 | 11/11 | 4.32 | -9.08 | 2.02 |
| mains50 | Kanal 3 | 11/11 | 163.94 | -165.91 | 0.40 |
| other1 | Kanal 3 | 11/11 | 0.16 | 0.14 | 0.27 |
| fs8 | Kanal 4 | 11/11 | 0.04 | 0.01 | 0.01 |
| usb1k | Kanal 4 | 11/11 | 0.17 | 0.23 | 0.12 |
| led | Kanal 4 | 10/11 | 8.21 | -1.49 | 1.59 |
| mains50 | Kanal 4 | 11/11 | 223.81 | -57.60 | 0.77 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 2.46 | 0.31 s (3.22 Hz) | 33.6 |
| Kanal 1 | 6000.0 Hz ± 10 | 1.33 | 1.25 s (0.80 Hz) | 43.8 |
| Kanal 2 | breitbandig | 1.93 | 0.31 s (3.22 Hz) | 32.8 |
| Kanal 2 | 999.9 Hz ± 10 | 0.94 | 1.25 s (0.80 Hz) | 32.1 |
| Kanal 3 | breitbandig | 1.74 | 0.31 s (3.22 Hz) | 35.3 |
| Kanal 3 | 6000.0 Hz ± 10 | 1.23 | 1.25 s (0.80 Hz) | 47.1 |
| Kanal 4 | breitbandig | 1.54 | 0.31 s (3.22 Hz) | 31.1 |
| Kanal 4 | 999.9 Hz ± 10 | 0.93 | 1.25 s (0.80 Hz) | 31.6 |

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
| Kanal 1 | 1.00 | 0.95 | 0.94 | 0.89 |
| Kanal 2 | 0.95 | 1.00 | 0.92 | 0.96 |
| Kanal 3 | 0.94 | 0.92 | 1.00 | 0.86 |
| Kanal 4 | 0.89 | 0.96 | 0.86 | 1.00 |

## Vergleich mit Referenz X1-vcv

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -72.7 | -72.9 | +0.2 | 48 % | 48 % |
| Kanal 2 | -73.1 | -73.3 | +0.2 | 61 % | 61 % |
| Kanal 3 | -75.0 | -75.3 | +0.2 | 70 % | 71 % |
| Kanal 4 | -72.5 | -72.7 | +0.2 | 60 % | 60 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](X1-rec_psd.png)

### Kammprofile

![Kammprofile](X1-rec_combs.png)

### Zeitverlauf

![Zeitverlauf](X1-rec_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 16:31:18. Stream-Meldungen: 0. owl_read: reports/owl_read/X1-rec (rc 0).
