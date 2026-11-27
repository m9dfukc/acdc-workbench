# Report B3-fx1p-r2: B3-fx1p-r2 – acdc1 Layout-Test, rohe Eingänge offen, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Layout-Test v22.4.r-fx1p (Build 2 + Füllbytes, Adressen wie Build 3c, sonst funktionsgleich) |
| test | Layout-Test 2/2 (D33): Eingänge offen, rohe ADC-Daten. Verschiebt allein die Lage im Flash/RAM die Störlinien? |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx1p-open-inputs-r2_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.5 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx1p-r2 --ref B3-fx1d-k-r2 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.6 | -69.8 | -75.8 | -71.1 | -72.2 | -85.5 | -71.4 | -101.0 | -71.1 | 71 % | -76.4 | 5.3 |
| Kanal 2 | -6.9 | -70.7 | -77.3 | -71.8 | -72.9 | -87.4 | -72.1 | -101.2 | -71.8 | 76 % | -77.9 | 6.1 |
| Kanal 3 | -5.1 | -72.5 | -81.5 | -73.1 | -74.2 | -91.6 | -73.4 | -105.2 | -73.1 | 86 % | -81.7 | 8.6 |
| Kanal 4 | -6.0 | -70.2 | -77.9 | -71.0 | -71.9 | -87.7 | -71.2 | -101.1 | -71.0 | 76 % | -77.2 | 6.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.1 dB | -77.2 | 24.4 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0004 | 23/23 | k=1: 999.868 Hz, -73.0 dB | -74.6 | 44.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0019 | 10/10 | k=1: 2320.544 Hz, -118.7 dB | -114.4 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 49.9896 | 0.0007 | 2/19 | k=1: 49.990 Hz, -94.5 dB | -97.2 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0012 | 127 | k=15·f1+1·f2: 20998.014 Hz, -100.6 dB | -90.0 | 1.3 % |
| stärkste übrige Linie (51.10 Hz) | Kanal 1 | 51.1066 | 0.0192 | 5/467 | k=1: 51.103 Hz, -100.5 dB | -103.2 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 1 | 23000.9267 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -101.9 dB | -104.9 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.0 dB | -77.1 | 29.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.3 | 44.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5447 | 0.0015 | 10/10 | k=1: 2320.544 Hz, -119.0 dB | -113.9 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 49.9898 | 0.0006 | 2/19 | k=1: 49.990 Hz, -95.3 dB | -97.9 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0014 | 144 | k=15·f1+1·f2: 20998.014 Hz, -100.6 dB | -89.8 | 1.6 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 2 | 23000.9267 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -101.9 dB | -104.9 | 0.0 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 2 | 1215.1899 | 0.0012 | 9/19 | k=1: 1215.189 Hz, -102.3 dB | -103.6 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.4 dB | -77.4 | 37.6 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0009 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.4 | 46.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0013 | 10/10 | k=1: 2320.544 Hz, -118.7 dB | -114.4 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 49.9916 | 0.0081 | 5/19 | k=1: 49.990 Hz, -96.0 dB | -98.7 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0011 | 156 | k=15·f1+1·f2: 20998.014 Hz, -100.8 dB | -90.1 | 2.0 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9267 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -102.2 dB | -105.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.3 | 23.1 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.2 dB | -73.8 | 51.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5447 | 0.0016 | 10/10 | k=1: 2320.544 Hz, -117.3 dB | -112.0 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 49.9898 | 0.0004 | 2/19 | k=1: 49.990 Hz, -95.8 dB | -98.4 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0015 | 134 | k=15·f1+1·f2: 20998.014 Hz, -100.7 dB | -90.0 | 1.3 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 4 | 23000.9268 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -101.9 dB | -104.9 | 0.0 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1899 | 0.0010 | 8/19 | k=1: 1215.189 Hz, -102.1 dB | -103.4 | 0.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.0 | 58.1 | usb1k·1 |
| 6000.000 | -77.1 | 57.2 | fs8·1 |
| 12000.000 | -79.9 | 56.3 | fs8·2 |
| 18000.000 | -80.8 | 55.6 | fs8·3 |
| 1999.735 | -83.2 | 49.2 | usb1k·2 |
| 3999.471 | -84.3 | 48.5 | usb1k·4 |
| 4999.338 | -86.1 | 48.7 | usb1k·5 |
| 7998.941 | -88.2 | 47.0 | usb1k·8 |
| 2999.603 | -88.6 | 45.2 | usb1k·3 |
| 15997.882 | -90.9 | 45.6 | usb1k·16 |
| 11998.411 | -91.4 | 44.8 | usb1k·12 |
| 8998.809 | -92.6 | 43.9 | usb1k·9 |
| 18997.485 | -92.8 | 43.7 | usb1k·19 |
| 16997.750 | -94.9 | 42.0 | usb1k·17 |
| 10998.544 | -95.4 | 41.2 | usb1k·11 |
| 49.990 | -94.5 | 27.5 | mains50·1 |
| 22996.955 | -95.7 | 43.2 | usb1k·23 |
| 9998.676 | -96.1 | 40.1 | usb1k·10 |
| 12998.279 | -98.7 | 37.8 | usb1k·13 |
| 5999.207 | -98.8 | 35.4 | usb1k·6 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 59.3 | usb1k·1 |
| 6000.000 | -77.0 | 59.1 | fs8·1 |
| 12000.000 | -79.7 | 58.5 | fs8·2 |
| 18000.000 | -80.7 | 57.5 | fs8·3 |
| 1999.735 | -83.9 | 50.2 | usb1k·2 |
| 3999.470 | -84.5 | 50.1 | usb1k·4 |
| 4999.338 | -86.6 | 50.0 | usb1k·5 |
| 7998.941 | -88.5 | 48.7 | usb1k·8 |
| 2999.603 | -89.8 | 45.7 | usb1k·3 |
| 15997.882 | -90.9 | 47.4 | usb1k·16 |
| 11998.411 | -91.5 | 46.7 | usb1k·12 |
| 8998.809 | -92.5 | 45.4 | usb1k·9 |
| 18997.485 | -92.7 | 45.8 | usb1k·19 |
| 10998.544 | -94.8 | 43.2 | usb1k·11 |
| 16997.750 | -95.4 | 43.0 | usb1k·17 |
| 22996.955 | -95.7 | 44.9 | usb1k·23 |
| 49.990 | -95.3 | 28.9 | mains50·1 |
| 9998.676 | -96.5 | 41.8 | usb1k·10 |
| 12998.279 | -98.8 | 39.5 | usb1k·13 |
| 19997.353 | -99.1 | 39.5 | usb1k·20 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 62.4 | usb1k·1 |
| 6000.000 | -77.4 | 62.6 | fs8·1 |
| 12000.000 | -79.8 | 61.5 | fs8·2 |
| 18000.000 | -80.9 | 60.4 | fs8·3 |
| 3999.471 | -85.2 | 53.7 | usb1k·4 |
| 1999.735 | -85.5 | 52.9 | usb1k·2 |
| 4999.338 | -87.6 | 52.8 | usb1k·5 |
| 7998.941 | -89.2 | 51.3 | usb1k·8 |
| 15997.882 | -91.4 | 49.6 | usb1k·16 |
| 2999.603 | -91.4 | 47.6 | usb1k·3 |
| 11998.411 | -92.0 | 49.3 | usb1k·12 |
| 18997.485 | -92.9 | 48.2 | usb1k·19 |
| 8998.809 | -93.1 | 48.5 | usb1k·9 |
| 10998.544 | -94.5 | 46.4 | usb1k·11 |
| 16997.750 | -96.1 | 45.7 | usb1k·17 |
| 22996.955 | -96.1 | 46.9 | usb1k·23 |
| 49.990 | -96.0 | 32.5 | mains50·1 |
| 9998.676 | -97.1 | 44.0 | usb1k·10 |
| 19997.353 | -99.4 | 41.8 | usb1k·20 |
| 12998.279 | -99.4 | 41.6 | usb1k·13 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.2 | 60.4 | usb1k·1 |
| 6000.000 | -77.3 | 58.3 | fs8·1 |
| 12000.000 | -79.8 | 57.0 | fs8·2 |
| 18000.000 | -80.9 | 55.7 | fs8·3 |
| 1999.735 | -81.2 | 52.0 | usb1k·2 |
| 3999.470 | -84.2 | 50.1 | usb1k·4 |
| 4999.338 | -85.0 | 50.4 | usb1k·5 |
| 7998.941 | -87.7 | 48.1 | usb1k·8 |
| 2999.603 | -87.8 | 47.1 | usb1k·3 |
| 15997.882 | -90.3 | 47.0 | usb1k·16 |
| 11998.411 | -90.8 | 46.1 | usb1k·12 |
| 8998.808 | -91.4 | 45.5 | usb1k·9 |
| 18997.485 | -92.7 | 44.6 | usb1k·19 |
| 16997.750 | -94.9 | 42.1 | usb1k·17 |
| 22996.955 | -95.3 | 43.8 | usb1k·23 |
| 10998.544 | -95.7 | 40.9 | usb1k·11 |
| 9998.676 | -95.8 | 40.9 | usb1k·10 |
| 5999.206 | -96.4 | 39.3 | usb1k·6 |
| 49.990 | -95.8 | 28.8 | mains50·1 |
| 12998.279 | -96.9 | 39.8 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.15 | -0.03 | 0.41 |
| led | Kanal 1 | 11/11 | 2.98 | -7.06 | 1.33 |
| mains50 | Kanal 1 | 11/11 | 210.92 | -101.30 | 0.93 |
| other1 | Kanal 1 | 11/11 | 0.93 | -0.08 | 2.87 |
| other2 | Kanal 1 | 11/11 | 0.08 | 0.13 | 0.19 |
| fs8 | Kanal 2 | 11/11 | 0.01 | -0.00 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.11 | -0.04 | 0.20 |
| led | Kanal 2 | 11/11 | 2.72 | -6.00 | 0.69 |
| mains50 | Kanal 2 | 11/11 | 182.06 | -71.52 | 0.64 |
| other1 | Kanal 2 | 11/11 | 0.06 | 0.07 | 0.18 |
| other2 | Kanal 2 | 11/11 | 0.31 | -0.09 | 0.31 |
| fs8 | Kanal 3 | 11/11 | 0.01 | -0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.12 | -0.03 | 0.36 |
| led | Kanal 3 | 11/11 | 3.05 | -6.80 | 0.55 |
| mains50 | Kanal 3 | 11/11 | 205.66 | 251.18 | 0.50 |
| other1 | Kanal 3 | 11/11 | 0.06 | 0.06 | 0.12 |
| fs8 | Kanal 4 | 11/11 | 0.01 | -0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.10 | -0.02 | 0.14 |
| led | Kanal 4 | 11/11 | 1.09 | 0.06 | 0.59 |
| mains50 | Kanal 4 | 11/11 | 188.02 | -50.59 | 0.53 |
| other1 | Kanal 4 | 11/11 | 0.06 | 0.00 | 0.24 |
| other2 | Kanal 4 | 11/11 | 0.28 | -0.45 | 0.33 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.18 | 0.31 s (3.21 Hz) | 26.0 |
| Kanal 1 | 999.9 Hz ± 10 | 1.00 | 7.56 s (0.13 Hz) | 31.8 |
| Kanal 2 | breitbandig | 1.00 | 0.16 s (6.40 Hz) | 25.9 |
| Kanal 2 | 999.9 Hz ± 10 | 0.91 | 7.56 s (0.13 Hz) | 31.6 |
| Kanal 3 | breitbandig | 0.65 | 0.31 s (3.21 Hz) | 27.3 |
| Kanal 3 | 999.9 Hz ± 10 | 0.97 | 7.56 s (0.13 Hz) | 36.5 |
| Kanal 4 | breitbandig | 0.79 | 0.16 s (6.40 Hz) | 25.8 |
| Kanal 4 | 999.9 Hz ± 10 | 0.89 | 7.56 s (0.13 Hz) | 30.0 |

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
| Kanal 1 | 1.00 | 0.98 | 0.95 | 0.94 |
| Kanal 2 | 0.98 | 1.00 | 0.95 | 0.97 |
| Kanal 3 | 0.95 | 0.95 | 1.00 | 0.92 |
| Kanal 4 | 0.94 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz B3-fx1d-k-r2

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.8 | +0.7 | 71 % | 62 % |
| Kanal 2 | -71.8 | -72.7 | +0.9 | 76 % | 68 % |
| Kanal 3 | -73.1 | -74.2 | +1.1 | 86 % | 79 % |
| Kanal 4 | -71.0 | -71.8 | +0.8 | 76 % | 70 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx1p-r2_psd.png)

### Kammprofile

![Kammprofile](B3-fx1p-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx1p-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 18:15–18:17, Host-Software vor jedem Lauf neu gestartet.
