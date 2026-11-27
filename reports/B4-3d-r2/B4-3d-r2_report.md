# Report B4-3d-r2: B4-3d-r2 – acdc1 3d-ctrl-open-inputs, 60 s (Wiederholung 2)

| Feld | Wert |
|---|---|
| date | 2026-11-16 |
| device | acdc1, Firmware Build 3d v22.4.r-fx2d |
| test | Build-4-Sitzung, Kontrolle 3d vor fx3i (Q3): Eingänge offen, rohe ADC-Daten |
| gain | g12 |
| usb | usb-stream, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), tools/acdc_rec.py duplex, Ausgang Nullen |
| patch | Slot 1: ACDC (Default-Patch), wirkt nicht auf die USB-Aufnahme |
| Datei(en) | `20261116_acdc1_3d-ctrl-open-inputs-r2_g12_usb-stream.wav` |
| Format | 48000 Hz, 60.0 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis B4-3d-r2 --manifest /Users/m9dfukc/Desktop/acdc/recordings/manifest.toml --ref X1-rec --no-spectrogram` |

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | -6.7 | -71.0 | -79.1 | -71.7 | -72.8 | -87.0 | -72.1 | – | -71.7 | 64 % | -76.1 | 4.4 |
| Kanal 2 | -7.0 | -71.8 | -79.8 | -72.6 | -73.7 | -88.7 | -72.9 | – | -72.6 | 69 % | -77.7 | 5.1 |
| Kanal 3 | -5.2 | -73.5 | -85.7 | -73.8 | -74.9 | -93.1 | -74.1 | – | -73.8 | 80 % | -80.9 | 7.1 |
| Kanal 4 | -6.0 | -71.0 | -79.8 | -71.6 | -72.5 | -88.8 | -71.9 | – | -71.6 | 71 % | -77.0 | 5.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -79.0 | 18.6 % |
| 1-kHz-Kamm | Kanal 1 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -74.2 dB | -75.5 | 41.1 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.5447 | 0.0016 | 10/10 | k=1: 2320.545 Hz, -116.7 dB | -113.2 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0001 | 0.0019 | 3/19 | k=1: 49.998 Hz, -97.6 dB | -99.3 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 999.8677 | 0.0011 | 146 | k=8·f1+1·f2: 13998.941 Hz, -95.6 dB | -85.5 | 4.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -78.7 dB | -78.9 | 23.2 % |
| 1-kHz-Kamm | Kanal 2 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -75.2 dB | -76.5 | 40.4 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.5448 | 0.0008 | 10/10 | k=9: 20884.903 Hz, -115.2 dB | -110.3 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0000 | 0.0011 | 3/19 | k=1: 49.998 Hz, -98.1 dB | -99.7 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 999.8677 | 0.0010 | 156 | k=8·f1+1·f2: 13998.941 Hz, -95.3 dB | -85.4 | 5.2 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.1 | 29.3 % |
| 1-kHz-Kamm | Kanal 3 | 999.8677 | 0.0002 | 23/23 | k=1: 999.868 Hz, -76.1 dB | -77.3 | 44.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.5447 | 0.0012 | 10/10 | k=2: 4641.091 Hz, -117.1 dB | -113.3 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0001 | 0.0012 | 3/19 | k=1: 49.999 Hz, -98.7 dB | -100.4 | 0.2 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 999.8677 | 0.0011 | 163 | k=8·f1+1·f2: 13998.941 Hz, -95.6 dB | -85.6 | 6.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -79.0 dB | -79.1 | 17.9 % |
| 1-kHz-Kamm | Kanal 4 | 999.8677 | 0.0003 | 23/23 | k=1: 999.868 Hz, -73.5 dB | -74.7 | 48.7 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.5446 | 0.0017 | 10/10 | k=1: 2320.544 Hz, -116.1 dB | -112.0 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0000 | 0.0012 | 3/19 | k=1: 49.998 Hz, -98.6 dB | -100.2 | 0.1 % |
| Mischprodukte n·999.8677 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 999.8677 | 0.0012 | 149 | k=8·f1+1·f2: 13998.941 Hz, -95.4 dB | -85.5 | 4.1 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -74.2 | 57.3 | usb1k·1 |
| 6000.000 | -78.7 | 56.3 | fs8·1 |
| 1999.736 | -81.8 | 51.2 | usb1k·2 |
| 18000.000 | -82.2 | 54.1 | fs8·3 |
| 12000.000 | -82.5 | 53.5 | fs8·2 |
| 2999.603 | -82.5 | 51.4 | usb1k·3 |
| 6999.074 | -87.7 | 47.5 | usb1k·7 |
| 15997.882 | -92.0 | 44.8 | usb1k·16 |
| 9998.676 | -91.9 | 43.8 | usb1k·10 |
| 5999.206 | -93.7 | 41.3 | usb1k·6 |
| 10998.544 | -94.5 | 42.0 | usb1k·11 |
| 14998.015 | -95.2 | 40.6 | usb1k·15 |
| 4999.339 | -94.9 | 39.0 | usb1k·5 |
| 15999.471 | -96.1 | 40.6 | imd·4·f1+2·f2 |
| 9999.471 | -96.5 | 39.3 | imd·4·f1+1·f2 |
| 12999.868 | -97.0 | 39.6 | imd·1·f1+2·f2 |
| 13998.941 | -95.6 | 40.7 | imd·8·f1+1·f2 |
| 49.998 | -97.6 | 26.5 | mains50·1 |
| 18999.868 | -97.9 | 38.4 | imd·1·f1+3·f2 |
| 18997.486 | -97.9 | 38.2 | usb1k·19 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -75.2 | 58.2 | usb1k·1 |
| 6000.000 | -78.7 | 58.0 | fs8·1 |
| 18000.000 | -82.0 | 55.5 | fs8·3 |
| 12000.000 | -82.2 | 55.4 | fs8·2 |
| 1999.736 | -83.1 | 51.4 | usb1k·2 |
| 2999.603 | -83.1 | 52.2 | usb1k·3 |
| 6999.074 | -87.8 | 48.7 | usb1k·7 |
| 15997.882 | -92.4 | 45.5 | usb1k·16 |
| 9998.676 | -92.2 | 45.0 | usb1k·10 |
| 14998.015 | -95.0 | 42.5 | usb1k·15 |
| 10998.544 | -94.5 | 42.7 | usb1k·11 |
| 5999.206 | -95.0 | 41.8 | usb1k·6 |
| 15999.471 | -95.9 | 42.0 | imd·4·f1+2·f2 |
| 9999.471 | -96.4 | 40.9 | imd·4·f1+1·f2 |
| 13998.941 | -95.3 | 42.3 | imd·8·f1+1·f2 |
| 12999.868 | -97.1 | 41.1 | imd·1·f1+2·f2 |
| 16998.544 | -97.2 | 39.5 | imd·11·f1+1·f2 |
| 19998.941 | -96.5 | 41.4 | imd·8·f1+2·f2 |
| 12999.074 | -96.8 | 41.2 | imd·7·f1+1·f2 |
| 18999.868 | -98.1 | 39.9 | imd·1·f1+3·f2 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -76.1 | 61.8 | usb1k·1 |
| 6000.000 | -79.0 | 60.7 | fs8·1 |
| 12000.000 | -82.3 | 57.7 | fs8·2 |
| 18000.000 | -82.3 | 58.1 | fs8·3 |
| 1999.736 | -84.0 | 55.0 | usb1k·2 |
| 2999.603 | -83.9 | 55.4 | usb1k·3 |
| 6999.074 | -88.4 | 51.7 | usb1k·7 |
| 15997.882 | -93.0 | 47.1 | usb1k·16 |
| 9998.676 | -92.7 | 47.6 | usb1k·10 |
| 14998.015 | -95.3 | 44.6 | usb1k·15 |
| 10998.544 | -95.0 | 45.6 | usb1k·11 |
| 15999.471 | -96.3 | 43.8 | imd·4·f1+2·f2 |
| 5999.206 | -95.8 | 43.9 | usb1k·6 |
| 9999.471 | -96.4 | 43.8 | imd·4·f1+1·f2 |
| 13998.941 | -95.6 | 44.8 | imd·8·f1+1·f2 |
| 12999.868 | -97.3 | 43.2 | imd·1·f1+2·f2 |
| 16998.544 | -97.4 | 41.7 | imd·11·f1+1·f2 |
| 19998.941 | -96.7 | 43.6 | imd·8·f1+2·f2 |
| 12999.074 | -97.1 | 43.5 | imd·7·f1+1·f2 |
| 18999.868 | -98.3 | 41.8 | imd·1·f1+3·f2 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 999.868 | -73.5 | 59.3 | usb1k·1 |
| 6000.000 | -79.0 | 56.7 | fs8·1 |
| 1999.736 | -80.3 | 53.6 | usb1k·2 |
| 18000.000 | -82.2 | 54.0 | fs8·3 |
| 2999.603 | -82.0 | 52.4 | usb1k·3 |
| 12000.000 | -82.3 | 54.3 | fs8·2 |
| 6999.074 | -87.2 | 48.4 | usb1k·7 |
| 15997.882 | -91.0 | 45.7 | usb1k·16 |
| 9998.676 | -91.6 | 44.8 | usb1k·10 |
| 4999.338 | -92.2 | 42.8 | usb1k·5 |
| 5999.206 | -92.0 | 43.8 | usb1k·6 |
| 10998.544 | -94.0 | 42.5 | usb1k·11 |
| 14998.015 | -95.3 | 41.1 | usb1k·15 |
| 15999.471 | -96.0 | 40.7 | imd·4·f1+2·f2 |
| 13998.941 | -95.4 | 41.0 | imd·8·f1+1·f2 |
| 9999.471 | -96.6 | 39.9 | imd·4·f1+1·f2 |
| 13998.147 | -97.0 | 39.4 | usb1k·14 |
| 20997.221 | -96.8 | 39.9 | usb1k·21 |
| 12999.868 | -97.2 | 39.3 | imd·1·f1+2·f2 |
| 11998.412 | -96.9 | 39.6 | usb1k·12 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.01 | 0.02 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.10 | -0.02 | 0.02 |
| led | Kanal 1 | 11/11 | 1.31 | 1.18 | 0.87 |
| mains50 | Kanal 1 | 11/11 | 189.60 | -324.72 | 0.77 |
| fs8 | Kanal 2 | 11/11 | 0.01 | 0.01 | 0.01 |
| usb1k | Kanal 2 | 11/11 | 0.07 | -0.00 | 0.02 |
| led | Kanal 2 | 11/11 | 0.61 | 0.14 | 0.73 |
| mains50 | Kanal 2 | 11/11 | 184.77 | -332.88 | 0.78 |
| fs8 | Kanal 3 | 11/11 | 0.01 | 0.00 | 0.01 |
| usb1k | Kanal 3 | 11/11 | 0.08 | 0.04 | 0.02 |
| led | Kanal 3 | 11/11 | 1.59 | 0.55 | 0.35 |
| mains50 | Kanal 3 | 11/11 | 28.78 | 32.85 | 0.38 |
| fs8 | Kanal 4 | 11/11 | 0.01 | 0.01 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.06 | 0.00 | 0.03 |
| led | Kanal 4 | 11/11 | 1.25 | -0.52 | 0.82 |
| mains50 | Kanal 4 | 11/11 | 183.59 | -365.22 | 0.79 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.76 | 0.16 s (6.40 Hz) | 25.0 |
| Kanal 1 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 30.4 |
| Kanal 2 | breitbandig | 0.76 | 0.16 s (6.40 Hz) | 26.4 |
| Kanal 2 | 999.9 Hz ± 10 | 0.90 | 1.25 s (0.80 Hz) | 31.9 |
| Kanal 3 | breitbandig | 0.42 | 1.25 s (0.80 Hz) | 26.9 |
| Kanal 3 | 999.9 Hz ± 10 | 0.88 | 1.25 s (0.80 Hz) | 36.1 |
| Kanal 4 | breitbandig | 0.64 | 0.16 s (6.40 Hz) | 26.2 |
| Kanal 4 | 999.9 Hz ± 10 | 0.88 | 1.25 s (0.80 Hz) | 31.6 |

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
| Kanal 1 | 1.00 | 0.97 | 0.92 | 0.94 |
| Kanal 2 | 0.97 | 1.00 | 0.93 | 0.96 |
| Kanal 3 | 0.92 | 0.93 | 1.00 | 0.91 |
| Kanal 4 | 0.94 | 0.96 | 0.91 | 1.00 |

## Vergleich mit Referenz X1-rec

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -71.7 | -72.7 | +1.0 | 64 % | 48 % |
| Kanal 2 | -72.6 | -73.1 | +0.5 | 69 % | 61 % |
| Kanal 3 | -73.8 | -75.0 | +1.2 | 80 % | 70 % |
| Kanal 4 | -71.6 | -72.5 | +0.8 | 71 % | 60 % |

## Abbildungen

### Langzeit-Spektrum

![Langzeit-Spektrum](B4-3d-r2_psd.png)

### Kammprofile

![Kammprofile](B4-3d-r2_combs.png)

### Zeitverlauf

![Zeitverlauf](B4-3d-r2_timeline.png)

## Notiz aus dem Manifest

> 48 kHz / pcm16, tools/acdc_rec.py (Gerät OWL-ACDC-FX, duplex, Ausgang Nullen, Block 256, 3 s verworfen). scale = 2 → Datei-dBFS wie die Aufnahmen aus der Host-Software. Start 17:10:36. Stream-Meldungen: 0. owl_read: reports/owl_read/B4-3d-r2 (rc 0). Stream zwischen den Wiederholungen geschlossen und neu geöffnet.
