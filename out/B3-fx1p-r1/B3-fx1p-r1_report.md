# Report B3-fx1p-r1: B3-fx1p-r1 – acdc1 Layout-Test, rohe Eingänge offen, 60 s (Wiederholung 1)

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Layout-Test v22.4.r-fx1p (Build 2 + Füllbytes, Adressen wie Build 3c, sonst funktionsgleich) |
| test | Layout-Test 1/2 (D33): Eingänge offen, rohe ADC-Daten. Verschiebt allein die Lage im Flash/RAM die Störlinien? |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Host-Software 48 kHz, Audio-Modul auf OWL-ACDC-FX ohne Playback |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261115_acdc1_fx1p-open-inputs-r1_g12_usb-stream.4chan.000.wav` |
| Format | 48000 Hz, 60.4 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B3-fx1p-r1 --ref B3-fx1d-k-r1 --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.5 | -69.1 | -73.6 | -71.1 | -72.1 | -85.5 | -71.4 | -100.6 | -71.1 | 69 % | -76.2 | 5.1 |
| Kanal 2 | -6.9 | -70.4 | -76.0 | -71.8 | -72.9 | -87.4 | -72.1 | -101.1 | -71.8 | 75 % | -77.7 | 5.9 |
| Kanal 3 | -5.1 | -71.6 | -76.7 | -73.1 | -74.3 | -91.7 | -73.4 | -105.2 | -73.1 | 85 % | -81.3 | 8.2 |
| Kanal 4 | -6.0 | -70.2 | -77.8 | -71.0 | -72.0 | -87.5 | -71.3 | -101.1 | -71.0 | 75 % | -77.0 | 6.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.0 dB | -77.2 | 24.2 % |
| 1-kHz-Kamm | Kanal 1 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.8 dB | -74.7 | 43.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5445 | 0.0009 | 10/10 | k=2: 4641.089 Hz, -117.9 dB | -114.4 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0087 | 0.0005 | 2/19 | k=1: 50.009 Hz, -94.8 dB | -97.2 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8676 | 0.0012 | 129 | k=8·f1+2·f2: 19998.940 Hz, -100.6 dB | -90.0 | 1.3 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 1 | 1215.1898 | 0.0007 | 9/19 | k=1: 1215.190 Hz, -101.5 dB | -102.5 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 1 | 23000.9269 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -101.9 dB | -105.0 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.1 dB | -77.1 | 29.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8676 | 0.0005 | 23/23 | k=1: 999.868 Hz, -73.7 dB | -75.4 | 43.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5446 | 0.0009 | 10/10 | k=2: 4641.090 Hz, -117.8 dB | -113.8 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0087 | 0.0004 | 2/19 | k=1: 50.009 Hz, -95.3 dB | -97.7 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8676 | 0.0011 | 136 | k=8·f1+2·f2: 19998.940 Hz, -100.6 dB | -89.9 | 1.5 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 2 | 1215.1898 | 0.0009 | 10/19 | k=1: 1215.190 Hz, -102.3 dB | -103.3 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 2 | 23000.9269 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -101.8 dB | -105.0 | 0.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -77.3 dB | -77.4 | 37.8 % |
| 1-kHz-Kamm | Kanal 3 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.0 dB | -76.6 | 44.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0008 | 10/10 | k=2: 4641.090 Hz, -118.6 dB | -114.3 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0094 | 0.0009 | 4/19 | k=1: 50.009 Hz, -96.2 dB | -98.7 | 0.3 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8676 | 0.0009 | 153 | k=8·f1+2·f2: 19998.940 Hz, -100.7 dB | -90.1 | 2.0 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 3 | 23000.9268 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -102.0 dB | -105.2 | 0.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -77.4 dB | -77.4 | 23.2 % |
| 1-kHz-Kamm | Kanal 4 | 999.8676 | 0.0003 | 23/23 | k=1: 999.868 Hz, -72.3 dB | -74.0 | 50.3 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5446 | 0.0010 | 10/10 | k=2: 4641.090 Hz, -116.8 dB | -112.4 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0087 | 0.0004 | 2/19 | k=1: 50.009 Hz, -95.7 dB | -98.0 | 0.2 % |
| Mischprodukte n·999.8676 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8676 | 0.0015 | 134 | k=15·f1+1·f2: 20998.014 Hz, -100.6 dB | -90.0 | 1.3 % |
| stärkste übrige Linie (1215.19 Hz) | Kanal 4 | 1215.1898 | 0.0010 | 10/19 | k=1: 1215.190 Hz, -102.1 dB | -103.2 | 0.1 % |
| stärkste übrige Linie (23000.93 Hz) | Kanal 4 | 23000.9268 | 0.0000 | 1/1 | k=1: 23000.927 Hz, -101.9 dB | -105.1 | 0.0 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.8 | 58.3 | usb1k·1 |
| 6000.000 | -77.0 | 57.5 | fs8·1 |
| 12000.000 | -80.0 | 56.2 | fs8·2 |
| 18000.000 | -80.8 | 56.4 | fs8·3 |
| 1999.735 | -83.2 | 49.3 | usb1k·2 |
| 3999.470 | -84.3 | 49.4 | usb1k·4 |
| 4999.338 | -86.2 | 48.3 | usb1k·5 |
| 2999.603 | -88.5 | 44.5 | usb1k·3 |
| 7998.940 | -88.1 | 47.1 | usb1k·8 |
| 11998.411 | -91.4 | 44.9 | usb1k·12 |
| 15997.881 | -90.6 | 46.2 | usb1k·16 |
| 8998.808 | -92.7 | 43.1 | usb1k·9 |
| 18997.484 | -92.5 | 44.8 | usb1k·19 |
| 50.009 | -94.8 | 25.5 | mains50·1 |
| 16997.748 | -94.9 | 42.0 | usb1k·17 |
| 10998.543 | -95.2 | 40.8 | usb1k·11 |
| 22996.954 | -95.5 | 43.2 | usb1k·23 |
| 9998.676 | -96.0 | 40.6 | usb1k·10 |
| 5999.205 | -99.3 | 35.2 | usb1k·6 |
| 12998.279 | -98.4 | 38.3 | usb1k·13 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.7 | 59.1 | usb1k·1 |
| 6000.000 | -77.1 | 59.4 | fs8·1 |
| 12000.000 | -79.8 | 58.3 | fs8·2 |
| 18000.000 | -80.7 | 58.2 | fs8·3 |
| 1999.735 | -83.9 | 50.1 | usb1k·2 |
| 3999.470 | -84.5 | 50.6 | usb1k·4 |
| 4999.338 | -86.6 | 49.3 | usb1k·5 |
| 7998.940 | -88.6 | 48.4 | usb1k·8 |
| 2999.603 | -89.8 | 45.0 | usb1k·3 |
| 11998.411 | -91.5 | 46.6 | usb1k·12 |
| 15997.881 | -90.7 | 47.9 | usb1k·16 |
| 8998.808 | -92.6 | 44.4 | usb1k·9 |
| 18997.484 | -92.4 | 46.4 | usb1k·19 |
| 10998.543 | -94.6 | 42.7 | usb1k·11 |
| 50.009 | -95.3 | 27.0 | mains50·1 |
| 16997.748 | -95.4 | 42.9 | usb1k·17 |
| 22996.954 | -95.6 | 44.4 | usb1k·23 |
| 9998.676 | -96.5 | 41.7 | usb1k·10 |
| 19997.351 | -99.1 | 39.7 | usb1k·20 |
| 12998.279 | -98.6 | 39.4 | usb1k·13 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.0 | 62.5 | usb1k·1 |
| 6000.000 | -77.3 | 62.7 | fs8·1 |
| 12000.000 | -79.9 | 61.6 | fs8·2 |
| 18000.000 | -81.0 | 60.9 | fs8·3 |
| 3999.470 | -85.2 | 54.0 | usb1k·4 |
| 1999.735 | -85.7 | 53.2 | usb1k·2 |
| 4999.338 | -87.8 | 52.3 | usb1k·5 |
| 7998.940 | -89.1 | 51.5 | usb1k·8 |
| 2999.603 | -91.5 | 47.4 | usb1k·3 |
| 11998.411 | -92.0 | 49.7 | usb1k·12 |
| 15997.881 | -91.2 | 50.2 | usb1k·16 |
| 8998.808 | -93.3 | 48.0 | usb1k·9 |
| 18997.484 | -92.7 | 48.9 | usb1k·19 |
| 10998.543 | -94.3 | 46.7 | usb1k·11 |
| 50.009 | -96.2 | 30.8 | mains50·1 |
| 16997.748 | -96.1 | 45.4 | usb1k·17 |
| 22996.954 | -96.1 | 47.0 | usb1k·23 |
| 9998.676 | -97.0 | 44.5 | usb1k·10 |
| 19997.351 | -99.3 | 42.3 | usb1k·20 |
| 14998.013 | -100.2 | 41.1 | usb1k·15 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -72.3 | 60.3 | usb1k·1 |
| 6000.000 | -77.4 | 58.5 | fs8·1 |
| 12000.000 | -79.9 | 56.6 | fs8·2 |
| 18000.000 | -80.9 | 56.9 | fs8·3 |
| 1999.735 | -81.1 | 52.6 | usb1k·2 |
| 3999.471 | -84.2 | 50.4 | usb1k·4 |
| 4999.337 | -85.0 | 50.0 | usb1k·5 |
| 2999.603 | -87.9 | 46.4 | usb1k·3 |
| 7998.940 | -87.9 | 48.2 | usb1k·8 |
| 11998.411 | -90.8 | 45.7 | usb1k·12 |
| 15997.881 | -90.0 | 47.2 | usb1k·16 |
| 8998.808 | -91.4 | 44.7 | usb1k·9 |
| 18997.484 | -92.5 | 44.9 | usb1k·19 |
| 16997.748 | -95.0 | 42.2 | usb1k·17 |
| 22996.954 | -95.1 | 43.5 | usb1k·23 |
| 50.009 | -95.7 | 26.9 | mains50·1 |
| 10998.543 | -95.4 | 40.9 | usb1k·11 |
| 9998.676 | -95.8 | 41.1 | usb1k·10 |
| 5999.205 | -97.2 | 38.7 | usb1k·6 |
| 12998.279 | -96.9 | 40.1 | usb1k·13 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.02 | 0.01 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.13 | -0.04 | 0.06 |
| led | Kanal 1 | 11/11 | 2.83 | -1.74 | 1.00 |
| mains50 | Kanal 1 | 11/11 | 538.09 | 465.16 | 0.78 |
| other1 | Kanal 1 | 11/11 | 0.60 | -0.53 | 0.41 |
| other2 | Kanal 1 | 11/11 | 0.10 | 0.01 | 0.24 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.10 | 0.08 | 0.02 |
| led | Kanal 2 | 11/11 | 1.16 | -0.59 | 0.58 |
| mains50 | Kanal 2 | 11/11 | 141.56 | -153.43 | 0.68 |
| other1 | Kanal 2 | 11/11 | 0.44 | -0.30 | 0.35 |
| other2 | Kanal 2 | 11/11 | 0.11 | -0.03 | 0.21 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.08 | 0.04 | 0.07 |
| led | Kanal 3 | 11/11 | 1.12 | -0.09 | 0.57 |
| mains50 | Kanal 3 | 11/11 | 589.32 | -88.02 | 0.45 |
| other1 | Kanal 3 | 11/11 | 0.06 | -0.00 | 0.16 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.10 | 0.14 | 0.03 |
| led | Kanal 4 | 11/11 | 0.97 | 0.17 | 0.67 |
| mains50 | Kanal 4 | 11/11 | 140.45 | -161.72 | 0.72 |
| other1 | Kanal 4 | 11/11 | 0.57 | -0.04 | 0.38 |
| other2 | Kanal 4 | 11/11 | 0.13 | 0.02 | 0.27 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 1.57 | 0.31 s (3.18 Hz) | 28.6 |
| Kanal 1 | 999.9 Hz ± 10 | 0.78 | 1.26 s (0.80 Hz) | 27.7 |
| Kanal 2 | breitbandig | 1.25 | 0.31 s (3.18 Hz) | 29.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.75 | 1.26 s (0.80 Hz) | 29.6 |
| Kanal 3 | breitbandig | 1.32 | 0.31 s (3.18 Hz) | 30.1 |
| Kanal 3 | 999.9 Hz ± 10 | 0.75 | 7.55 s (0.13 Hz) | 32.5 |
| Kanal 4 | breitbandig | 0.88 | 0.31 s (3.18 Hz) | 26.9 |
| Kanal 4 | 999.9 Hz ± 10 | 0.74 | 1.26 s (0.80 Hz) | 30.1 |

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
| Kanal 1 | 1.00 | 0.98 | 0.96 | 0.93 |
| Kanal 2 | 0.98 | 1.00 | 0.96 | 0.97 |
| Kanal 3 | 0.96 | 0.96 | 1.00 | 0.92 |
| Kanal 4 | 0.93 | 0.97 | 0.92 | 1.00 |

## Vergleich mit Referenz B3-fx1d-k-r1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.1 | -71.8 | +0.8 | 69 % | 62 % |
| Kanal 2 | -71.8 | -72.7 | +0.9 | 75 % | 68 % |
| Kanal 3 | -73.1 | -74.3 | +1.2 | 85 % | 79 % |
| Kanal 4 | -71.0 | -71.9 | +0.9 | 75 % | 69 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B3-fx1p-r1_psd.png)

### Kammprofile

![Kammprofile](B3-fx1p-r1_combs.png)

### Zeitverlauf

![Zeitverlauf](B3-fx1p-r1_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / 32 Bit float, Mehrkanal-Recorder, Host-Faktor 2. Aufnahme ≈ 18:15–18:17, Host-Software vor jedem Lauf neu gestartet.
