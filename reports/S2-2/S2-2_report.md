# Report S2-2: S2-2 – acdc2, Eingänge offen, Gain voll, 60 s

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc2 (DIY), Firmware v22.4.q |
| test | Eingänge offen (nichts gesteckt) |
| gain | g17 (Vollanschlag) |
| usb | usb-stream |
| patch | Slot 1: ACDC (Default-Patch, Knob = digitaler Gain) |
| Datei(en) | `20261114_acdc2_open-inputs_g17_usb-stream.4chan.000.wav` |
| Format | 96000 Hz, 60.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis S2-2 --ref S2-1` |

**Hinweise:**

- Datei hat 96000 Hz, oberhalb 24000 Hz ist nichts drin (-156 dB) → von 48000 Hz hochgerechnet.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +30.0 | -61.0 | -69.5 | -61.6 | -63.4 | -73.5 | -62.1 | – | -61.6 | 77 % | -68.0 | 6.3 |
| Kanal 2 | +28.9 | -59.8 | -71.2 | -60.2 | -61.1 | -73.8 | -60.5 | – | -60.2 | 85 % | -68.4 | 8.2 |
| Kanal 3 | +11.4 | -60.8 | -71.1 | -61.2 | -62.5 | -73.6 | -61.6 | – | -61.2 | 80 % | -68.2 | 7.1 |
| Kanal 4 | +23.9 | -58.8 | -71.0 | -59.1 | -59.7 | -73.6 | -59.4 | – | -59.1 | 88 % | -68.3 | 9.2 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -66.7 dB | -66.6 | 31.7 % |
| 1-kHz-Kamm | Kanal 1 | 1000.0528 | 0.0002 | 23/23 | k=1: 1000.053 Hz, -70.1 dB | -68.2 | 21.9 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.9763 | 0.0002 | 10/10 | k=1: 2320.976 Hz, -75.0 dB | -71.0 | 11.5 % |
| Netz 50 Hz | Kanal 1 | 50.0357 | 0.0010 | 6/19 | k=1: 50.035 Hz, -71.3 dB | -74.3 | 5.4 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 1 | 1000.0528 | 0.0011 | 160 | k=8·f1+1·f2: 14000.423 Hz, -83.2 dB | -73.6 | 6.3 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -67.1 dB | -67.0 | 20.7 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0528 | 0.0002 | 23/23 | k=1: 1000.053 Hz, -63.0 dB | -63.4 | 47.5 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.9763 | 0.0002 | 10/10 | k=1: 2320.976 Hz, -74.7 dB | -70.7 | 8.9 % |
| Netz 50 Hz | Kanal 2 | 50.0356 | 0.0005 | 5/19 | k=1: 50.035 Hz, -71.6 dB | -74.6 | 3.6 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 1000.0528 | 0.0011 | 159 | k=8·f1+1·f2: 14000.423 Hz, -83.6 dB | -74.0 | 4.1 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -67.1 dB | -67.1 | 25.6 % |
| 1-kHz-Kamm | Kanal 3 | 1000.0528 | 0.0002 | 23/23 | k=1: 1000.053 Hz, -65.8 dB | -65.7 | 35.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.9763 | 0.0002 | 10/10 | k=1: 2320.976 Hz, -75.3 dB | -71.6 | 9.1 % |
| Netz 50 Hz | Kanal 3 | 50.0356 | 0.0004 | 5/19 | k=1: 50.035 Hz, -71.4 dB | -74.5 | 4.7 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 3 | 1000.0528 | 0.0011 | 159 | k=8·f1+1·f2: 14000.423 Hz, -83.8 dB | -74.2 | 5.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0000 | 3/3 | k=1: 6000.000 Hz, -67.1 dB | -66.9 | 16.3 % |
| 1-kHz-Kamm | Kanal 4 | 1000.0528 | 0.0002 | 23/23 | k=1: 1000.053 Hz, -60.8 dB | -61.5 | 57.6 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.9763 | 0.0002 | 10/10 | k=1: 2320.976 Hz, -74.2 dB | -70.0 | 8.0 % |
| Netz 50 Hz | Kanal 4 | 50.0357 | 0.0004 | 5/19 | k=1: 50.035 Hz, -71.4 dB | -74.4 | 2.9 % |
| Mischprodukte n·1000.0528 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 1000.0528 | 0.0010 | 159 | k=8·f1+1·f2: 14000.423 Hz, -83.5 dB | -73.9 | 3.3 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -66.7 | 59.3 | fs8·1 |
| 12000.000 | -69.4 | 56.5 | fs8·2 |
| 18000.000 | -69.6 | 55.9 | fs8·3 |
| 2000.106 | -71.4 | 53.9 | usb1k·2 |
| 1000.053 | -70.1 | 54.9 | usb1k·1 |
| 50.035 | -71.3 | 46.7 | mains50·1 |
| 4641.953 | -75.9 | 48.8 | led·2 |
| 3000.158 | -74.6 | 50.9 | usb1k·3 |
| 2320.976 | -75.0 | 50.3 | led·1 |
| 6962.929 | -76.7 | 49.6 | led·3 |
| 7000.369 | -77.0 | 48.5 | usb1k·7 |
| 9283.905 | -77.9 | 48.1 | led·4 |
| 8000.423 | -78.5 | 47.1 | usb1k·8 |
| 13925.858 | -78.6 | 48.8 | led·6 |
| 12000.634 | -78.5 | 47.3 | usb1k·12 |
| 11604.881 | -78.3 | 49.1 | led·5 |
| 16246.834 | -78.8 | 48.7 | led·7 |
| 18567.811 | -78.9 | 47.9 | led·8 |
| 20888.786 | -79.1 | 48.2 | led·9 |
| 15000.792 | -79.7 | 46.0 | usb1k·15 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -63.0 | 61.6 | usb1k·1 |
| 2000.106 | -66.2 | 59.5 | usb1k·2 |
| 6000.000 | -67.1 | 59.1 | fs8·1 |
| 12000.000 | -69.9 | 56.4 | fs8·2 |
| 18000.000 | -69.9 | 56.4 | fs8·3 |
| 3000.158 | -70.7 | 55.0 | usb1k·3 |
| 50.035 | -71.6 | 46.3 | mains50·1 |
| 4641.953 | -75.6 | 48.1 | led·2 |
| 2320.976 | -74.7 | 49.9 | led·1 |
| 7000.370 | -75.5 | 50.2 | usb1k·7 |
| 6000.317 | -76.8 | 49.3 | usb1k·6 |
| 9283.905 | -77.5 | 48.7 | led·4 |
| 6962.929 | -76.5 | 50.2 | led·3 |
| 13925.858 | -78.1 | 50.0 | led·6 |
| 11604.881 | -77.9 | 50.1 | led·5 |
| 16246.834 | -78.3 | 49.7 | led·7 |
| 18567.811 | -78.3 | 47.7 | led·8 |
| 20888.786 | -78.6 | 49.4 | led·9 |
| 12000.634 | -79.3 | 46.9 | usb1k·12 |
| 21001.109 | -80.6 | 45.2 | usb1k·21 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 6000.000 | -67.1 | 59.2 | fs8·1 |
| 1000.053 | -65.8 | 59.2 | usb1k·1 |
| 2000.106 | -68.5 | 57.1 | usb1k·2 |
| 12000.000 | -70.1 | 56.2 | fs8·2 |
| 18000.000 | -70.2 | 55.9 | fs8·3 |
| 50.035 | -71.4 | 46.6 | mains50·1 |
| 3000.158 | -72.4 | 53.5 | usb1k·3 |
| 4641.953 | -76.2 | 48.1 | led·2 |
| 2320.976 | -75.3 | 50.1 | led·1 |
| 7000.370 | -76.4 | 49.2 | usb1k·7 |
| 6962.929 | -77.3 | 49.3 | led·3 |
| 9283.905 | -78.5 | 47.9 | led·4 |
| 6000.317 | -79.1 | 47.1 | usb1k·6 |
| 13925.858 | -79.3 | 48.4 | led·6 |
| 12000.634 | -79.3 | 46.9 | usb1k·12 |
| 11604.881 | -79.0 | 48.7 | led·5 |
| 16246.834 | -79.5 | 48.5 | led·7 |
| 18567.811 | -79.6 | 47.0 | led·8 |
| 20888.786 | -79.8 | 47.9 | led·9 |
| 8000.423 | -80.0 | 45.9 | usb1k·8 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -60.8 | 63.6 | usb1k·1 |
| 2000.106 | -64.3 | 61.2 | usb1k·2 |
| 6000.000 | -67.1 | 58.9 | fs8·1 |
| 18000.000 | -69.7 | 56.7 | fs8·3 |
| 12000.000 | -70.0 | 56.5 | fs8·2 |
| 3000.158 | -69.1 | 56.1 | usb1k·3 |
| 50.035 | -71.4 | 45.7 | mains50·1 |
| 6000.317 | -74.8 | 51.1 | usb1k·6 |
| 4641.953 | -75.1 | 49.0 | led·2 |
| 7000.370 | -74.7 | 51.2 | usb1k·7 |
| 2320.976 | -74.2 | 50.3 | led·1 |
| 9283.905 | -76.9 | 49.6 | led·4 |
| 6962.929 | -76.0 | 50.9 | led·3 |
| 13925.858 | -77.5 | 50.8 | led·6 |
| 18567.811 | -77.5 | 48.8 | led·8 |
| 20888.786 | -77.7 | 50.2 | led·9 |
| 11604.881 | -77.2 | 50.8 | led·5 |
| 16246.834 | -77.5 | 50.7 | led·7 |
| 21001.109 | -79.2 | 46.6 | usb1k·21 |
| 12000.634 | -79.6 | 46.8 | usb1k·12 |

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 11/11 | 0.03 | 0.02 | 0.02 |
| usb1k | Kanal 1 | 11/11 | 0.08 | -0.04 | 0.06 |
| led | Kanal 1 | 11/11 | 0.05 | 0.02 | 0.03 |
| mains50 | Kanal 1 | 11/11 | 162.84 | 492.23 | 0.09 |
| fs8 | Kanal 2 | 11/11 | 0.03 | 0.02 | 0.02 |
| usb1k | Kanal 2 | 11/11 | 0.05 | -0.01 | 0.05 |
| led | Kanal 2 | 11/11 | 0.06 | 0.02 | 0.02 |
| mains50 | Kanal 2 | 11/11 | 152.20 | 474.10 | 0.10 |
| fs8 | Kanal 3 | 11/11 | 0.03 | 0.02 | 0.02 |
| usb1k | Kanal 3 | 11/11 | 0.06 | -0.01 | 0.05 |
| led | Kanal 3 | 11/11 | 0.05 | 0.03 | 0.03 |
| mains50 | Kanal 3 | 11/11 | 160.92 | 476.38 | 0.11 |
| fs8 | Kanal 4 | 11/11 | 0.03 | 0.02 | 0.02 |
| usb1k | Kanal 4 | 11/11 | 0.05 | 0.01 | 0.04 |
| led | Kanal 4 | 11/11 | 0.05 | 0.03 | 0.02 |
| mains50 | Kanal 4 | 11/11 | 150.77 | 478.81 | 0.11 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, 0,2–20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.81 | 3.17 s (0.32 Hz) | 32.1 |
| Kanal 1 | 6000.0 Hz ± 10 | 1.34 | 3.17 s (0.32 Hz) | 51.9 |
| Kanal 2 | breitbandig | 0.53 | 3.17 s (0.32 Hz) | 36.2 |
| Kanal 2 | 1000.1 Hz ± 10 | 0.58 | 3.17 s (0.32 Hz) | 36.6 |
| Kanal 3 | breitbandig | 0.67 | 3.17 s (0.32 Hz) | 34.5 |
| Kanal 3 | 1000.1 Hz ± 10 | 0.64 | 3.17 s (0.32 Hz) | 36.7 |
| Kanal 4 | breitbandig | 0.49 | 3.17 s (0.32 Hz) | 35.5 |
| Kanal 4 | 1000.1 Hz ± 10 | 0.56 | 3.17 s (0.32 Hz) | 35.7 |

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
| Kanal 1 | 1.00 | 0.92 | 0.97 | 0.85 |
| Kanal 2 | 0.92 | 1.00 | 0.97 | 0.98 |
| Kanal 3 | 0.97 | 0.97 | 1.00 | 0.94 |
| Kanal 4 | 0.85 | 0.98 | 0.94 | 1.00 |

## Vergleich mit Referenz S2-1

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -61.6 | -72.0 | +10.4 | 77 % | 79 % |
| Kanal 2 | -60.2 | -69.2 | +9.0 | 85 % | 87 % |
| Kanal 3 | -61.2 | -69.3 | +8.1 | 80 % | 84 % |
| Kanal 4 | -59.1 | -69.9 | +10.8 | 88 % | 90 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](S2-2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](S2-2_psd.png)

### Kammprofile

![Kammprofile](S2-2_combs.png)

### Zeitverlauf

![Zeitverlauf](S2-2_timeline.png)
