# Report M2: M2 – kein Eingangssignal, Eingänge gebrückt 1↔2 / 3↔4, Gain voll

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc2 (DIY), Firmware v22.4.q |
| test | kein Eingangssignal, Eingänge gebrückt 1↔2, 3↔4 |
| gain | g17 (Vollanschlag) |
| usb | usb-stream |
| patch | Slot 1: ACDC (9,32 KB, Default-Patch, Knob = digitaler Gain) – laut Device-Status vom 2026-11-13 |
| Datei(en) | `20261113_acdc2_inputs-bridged_g17_usb-stream_ch1.wav`, `20261113_acdc2_inputs-bridged_g17_usb-stream_ch2.wav`, `20261113_acdc2_inputs-bridged_g17_usb-stream_ch3.wav`, `20261113_acdc2_inputs-bridged_g17_usb-stream_ch4.wav` |
| Format | 96000 Hz, 7.4 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis M2` |

**Hinweise:**

- Nur 7.4 s. Für Zeitverhalten und Klicks sind ≥ 60 s vorgesehen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +15.6 | -64.5 | -84.1 | -64.6 | -66.8 | -81.2 | -65.2 | – | -64.6 | 87 % | -73.6 | 9.0 |
| Kanal 2 | +15.0 | -63.9 | -86.3 | -64.0 | -65.7 | -83.8 | -64.5 | – | -64.0 | 90 % | -73.8 | 9.8 |
| Kanal 3 | +6.2 | -65.4 | -85.2 | -65.4 | -66.8 | -84.1 | -65.8 | – | -65.4 | 85 % | -73.8 | 8.3 |
| Kanal 4 | +12.5 | -64.4 | -86.2 | -64.4 | -65.5 | -84.0 | -64.8 | – | -64.4 | 88 % | -73.8 | 9.4 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9998 | 0.0028 | 3/3 | k=1: 6000.004 Hz, -72.5 dB | -72.3 | 16.9 % |
| 1-kHz-Kamm | Kanal 1 | 1000.0508 | 0.1065 | 22/23 | k=1: 1000.052 Hz, -70.0 dB | -70.4 | 26.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.9764 | 0.0016 | 10/10 | k=9: 20888.788 Hz, -72.1 dB | -68.5 | 40.3 % |
| Netz 50 Hz | Kanal 1 | 50.0122 | 0.0260 | 6/19 | k=1: 50.012 Hz, -80.0 dB | -83.0 | 1.4 % |
| Mischprodukte n·1000.0508 + m·5999.9998 Hz (m = ±1…±4) | Kanal 1 | 1000.0508 | 0.0288 | 43 | k=8·f1+2·f2: 20000.429 Hz, -89.0 dB | -80.8 | 2.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 6000.0000 | 0.0038 | 3/3 | k=1: 6000.006 Hz, -72.9 dB | -72.6 | 13.6 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0517 | 0.0635 | 22/23 | k=1: 1000.053 Hz, -67.4 dB | -68.3 | 36.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.9764 | 0.0016 | 10/10 | k=9: 20888.788 Hz, -71.9 dB | -68.3 | 36.8 % |
| Netz 50 Hz | Kanal 2 | 50.0103 | 0.0172 | 4/19 | k=1: 50.010 Hz, -85.1 dB | -88.1 | 0.4 % |
| Mischprodukte n·1000.0517 + m·6000.0000 Hz (m = ±1…±4) | Kanal 2 | 1000.0517 | 0.0286 | 46 | k=8·f1+2·f2: 20000.429 Hz, -89.0 dB | -81.1 | 2.0 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 5999.9998 | 0.0032 | 3/3 | k=1: 6000.005 Hz, -72.8 dB | -72.7 | 18.6 % |
| 1-kHz-Kamm | Kanal 3 | 1000.0511 | 0.0865 | 22/23 | k=1: 1000.053 Hz, -68.5 dB | -69.3 | 41.2 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.9763 | 0.0016 | 10/10 | k=9: 20888.788 Hz, -75.8 dB | -71.9 | 22.4 % |
| Netz 50 Hz | Kanal 3 | 50.0095 | 0.0081 | 3/19 | k=1: 50.011 Hz, -86.7 dB | -89.8 | 0.4 % |
| Mischprodukte n·1000.0511 + m·5999.9998 Hz (m = ±1…±4) | Kanal 3 | 1000.0511 | 0.0264 | 45 | k=8·f1+2·f2: 20000.429 Hz, -89.7 dB | -81.3 | 2.6 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 6000.0000 | 0.0037 | 3/3 | k=1: 6000.006 Hz, -73.0 dB | -72.6 | 15.1 % |
| 1-kHz-Kamm | Kanal 4 | 1000.0518 | 0.0638 | 22/23 | k=1: 1000.053 Hz, -66.3 dB | -67.4 | 50.8 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.9763 | 0.0016 | 10/10 | k=9: 20888.788 Hz, -75.2 dB | -71.4 | 20.1 % |
| Netz 50 Hz | Kanal 4 | 50.0092 | 0.0117 | 3/19 | k=1: 50.010 Hz, -86.7 dB | -89.9 | 0.3 % |
| Mischprodukte n·1000.0518 + m·6000.0000 Hz (m = ±1…±4) | Kanal 4 | 1000.0518 | 0.0260 | 44 | k=8·f1+2·f2: 20000.429 Hz, -88.7 dB | -81.0 | 2.2 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.052 | -70.0 | 48.9 | usb1k·1 |
| 6000.004 | -72.5 | 46.5 | fs8·1 |
| 20888.788 | -72.1 | 50.0 | led·9 |
| 18567.811 | -72.6 | 51.3 | led·8 |
| 16246.834 | -73.4 | 50.7 | led·7 |
| 13925.856 | -74.3 | 49.1 | led·6 |
| 11999.999 | -75.3 | 44.1 | fs8·2 |
| 17999.998 | -75.5 | 45.5 | fs8·3 |
| 2000.105 | -75.7 | 45.7 | usb1k·2 |
| 11604.880 | -75.4 | 46.0 | led·5 |
| 3000.156 | -76.6 | 44.1 | usb1k·3 |
| 9283.904 | -76.7 | 46.4 | led·4 |
| 6962.930 | -78.2 | 44.2 | led·3 |
| 4641.956 | -79.6 | 44.2 | led·2 |
| 2320.978 | -80.5 | 43.1 | led·1 |
| 50.012 | -80.0 | 36.1 | mains50·1 |
| 7000.369 | -80.8 | 37.9 | usb1k·7 |
| 15000.790 | -85.6 | 36.0 | usb1k·15 |
| 12000.630 | -85.3 | 33.7 | usb1k·12 |
| 16000.842 | -87.0 | 30.4 | usb1k·16 |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -67.4 | 52.1 | usb1k·1 |
| 20888.788 | -71.9 | 51.1 | led·9 |
| 18567.811 | -72.4 | 52.1 | led·8 |
| 6000.006 | -72.9 | 46.4 | fs8·1 |
| 16246.834 | -73.2 | 50.7 | led·7 |
| 2000.105 | -73.2 | 48.2 | usb1k·2 |
| 13925.856 | -74.1 | 49.6 | led·6 |
| 3000.157 | -75.2 | 45.7 | usb1k·3 |
| 11604.879 | -75.1 | 47.4 | led·5 |
| 11999.999 | -75.8 | 44.0 | fs8·2 |
| 17999.998 | -75.9 | 45.4 | fs8·3 |
| 9283.904 | -76.5 | 46.7 | led·4 |
| 6962.930 | -78.0 | 44.7 | led·3 |
| 4641.955 | -79.3 | 44.4 | led·2 |
| 2320.978 | -80.0 | 43.1 | led·1 |
| 7000.369 | -80.2 | 39.2 | usb1k·7 |
| 16000.842 | -85.6 | 32.0 | usb1k·16 |
| 50.010 | -85.1 | 29.9 | mains50·1 |
| 15000.790 | -86.1 | 36.4 | usb1k·15 |
| 12000.630 | -86.0 | 33.5 | usb1k·12 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -68.5 | 50.0 | usb1k·1 |
| 6000.005 | -72.8 | 46.3 | fs8·1 |
| 2000.105 | -74.5 | 47.4 | usb1k·2 |
| 11999.999 | -75.9 | 44.2 | fs8·2 |
| 3000.156 | -75.8 | 44.5 | usb1k·3 |
| 17999.998 | -76.1 | 44.7 | fs8·3 |
| 20888.788 | -75.8 | 47.6 | led·9 |
| 18567.811 | -76.3 | 48.1 | led·8 |
| 16246.834 | -77.1 | 46.8 | led·7 |
| 13925.856 | -78.0 | 45.8 | led·6 |
| 11604.879 | -79.0 | 43.1 | led·5 |
| 2320.978 | -81.2 | 42.2 | led·1 |
| 9283.904 | -80.1 | 43.5 | led·4 |
| 7000.369 | -80.6 | 38.5 | usb1k·7 |
| 4641.955 | -81.2 | 42.3 | led·2 |
| 6962.930 | -81.0 | 41.2 | led·3 |
| 15000.790 | -86.3 | 35.8 | usb1k·15 |
| 16000.842 | -86.6 | 31.1 | usb1k·16 |
| 12000.630 | -86.0 | 33.9 | usb1k·12 |
| 50.011 | -86.7 | 29.0 | mains50·1 |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 1000.053 | -66.3 | 52.6 | usb1k·1 |
| 2000.106 | -72.7 | 48.4 | usb1k·2 |
| 6000.006 | -73.0 | 46.3 | fs8·1 |
| 3000.157 | -74.2 | 45.7 | usb1k·3 |
| 17999.998 | -75.7 | 45.1 | fs8·3 |
| 20888.788 | -75.2 | 47.2 | led·9 |
| 11999.999 | -75.8 | 44.0 | fs8·2 |
| 18567.811 | -75.9 | 48.7 | led·8 |
| 16246.834 | -76.6 | 47.1 | led·7 |
| 13925.856 | -77.5 | 46.7 | led·6 |
| 11604.879 | -78.5 | 44.4 | led·5 |
| 7000.369 | -79.5 | 40.3 | usb1k·7 |
| 2320.978 | -80.3 | 42.5 | led·1 |
| 9283.903 | -79.5 | 43.8 | led·4 |
| 4641.955 | -80.5 | 42.8 | led·2 |
| 6962.930 | -80.3 | 42.5 | led·3 |
| 16000.842 | -84.7 | 33.2 | usb1k·16 |
| 10000.528 | -85.4 | 36.4 | usb1k·10 |
| 15000.790 | -86.4 | 35.1 | usb1k·15 |
| 12000.630 | -86.2 | 33.4 | usb1k·12 |

## Zeitverhalten

Fensterlänge 1.8 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 7/7 | 2.50 | -1.19 | 0.65 |
| usb1k | Kanal 1 | 7/7 | 3.48 | -31.88 | 0.17 |
| led | Kanal 1 | 7/7 | 0.09 | 0.08 | 0.04 |
| mains50 | Kanal 1 | 7/7 | 1710.81 | -34341.96 | 0.35 |
| fs8 | Kanal 2 | 7/7 | 2.40 | 4.80 | 0.78 |
| usb1k | Kanal 2 | 7/7 | 23.34 | 236.91 | 0.12 |
| led | Kanal 2 | 7/7 | 0.08 | -0.13 | 0.04 |
| mains50 | Kanal 2 | 7/7 | 388.52 | -2656.38 | 0.61 |
| fs8 | Kanal 3 | 7/7 | 2.44 | 1.52 | 0.71 |
| usb1k | Kanal 3 | 7/7 | 24.46 | 44.11 | 0.14 |
| led | Kanal 3 | 7/7 | 0.12 | 0.36 | 0.06 |
| mains50 | Kanal 3 | 7/7 | 317.49 | -4595.24 | 0.74 |
| fs8 | Kanal 4 | 7/7 | 2.29 | 6.94 | 0.81 |
| usb1k | Kanal 4 | 7/7 | 4.82 | -52.45 | 0.10 |
| led | Kanal 4 | 7/7 | 0.12 | -0.57 | 0.06 |
| mains50 | Kanal 4 | 7/7 | 541.33 | -2889.11 | 0.84 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, 0,2–20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.26 | 3.69 s (0.27 Hz) | 18.4 |
| Kanal 1 | 20888.8 Hz ± 10 | 2.37 | 0.32 s (3.12 Hz) | 19.8 |
| Kanal 2 | breitbandig | 0.24 | 3.69 s (0.27 Hz) | 20.9 |
| Kanal 2 | 20888.8 Hz ± 10 | 2.37 | 0.32 s (3.12 Hz) | 20.0 |
| Kanal 3 | breitbandig | 0.29 | 3.69 s (0.27 Hz) | 21.3 |
| Kanal 3 | 1000.1 Hz ± 10 | 2.40 | 2.46 s (0.41 Hz) | 22.7 |
| Kanal 4 | breitbandig | 0.27 | 3.69 s (0.27 Hz) | 22.4 |
| Kanal 4 | 1000.1 Hz ± 10 | 2.38 | 2.46 s (0.41 Hz) | 23.4 |

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
| Kanal 1 | 1.00 | 0.98 | 0.97 | 0.93 |
| Kanal 2 | 0.98 | 1.00 | 0.98 | 0.97 |
| Kanal 3 | 0.97 | 0.98 | 1.00 | 0.97 |
| Kanal 4 | 0.93 | 0.97 | 0.97 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](M2_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](M2_psd.png)

### Kammprofile

![Kammprofile](M2_combs.png)

### Zeitverlauf

![Zeitverlauf](M2_timeline.png)

## Notiz aus dem Manifest

> Zu hören: deutliches Rauschen plus hohes Pfeifen/Sirren (1-kHz-Ton mit Obertönen, darüber ein „glasiges“ Zirpen in den Höhen).
> Gain wirkt im Default-Patch digital: Linien, die stärker steigen als der Boden, stecken in den ADC-Daten (kein Beleg für Einkopplung vor einer analogen Gain-Stufe).
> 96 kHz / 16 Bit hochgerechnet, ≈ 7 s. Ursprünglich channel-{1..4}-001.wav.
