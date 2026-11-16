# Report M3: M3 – Sinus ≈ 838 Hz (Make Noise DPO) auf alle 4 Eingänge, Gain 11:45

| Feld | Wert |
|---|---|
| date | 2026-11-13 |
| device | acdc2 (DIY), Firmware v22.4.q |
| test | Sinus ≈ 838 Hz (Make Noise DPO) per Stackcable auf alle 4 Eingänge |
| gain | g1145 |
| usb | usb-stream |
| patch | Slot 1: ACDC (9,32 KB, Default-Patch, Knob = digitaler Gain) – laut Device-Status vom 2026-11-13 |
| Datei(en) | `20261113_acdc2_sine838-dpo_g1145_usb-stream_ch1.wav`, `20261113_acdc2_sine838-dpo_g1145_usb-stream_ch2.wav`, `20261113_acdc2_sine838-dpo_g1145_usb-stream_ch3.wav`, `20261113_acdc2_sine838-dpo_g1145_usb-stream_ch4.wav` |
| Format | 96000 Hz, 9.2 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis M3` |

**Hinweise:**

- Nur 9.2 s. Für Zeitverhalten und Klicks sind ≥ 60 s vorgesehen.
- Ein Nutzsignal (übrige Linien) dominiert. Störanteil und Notch-Gewinn sind dann nicht aussagekräftig, Störlinien in absoluten dBFS vergleichen.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +3.6 | -8.6 | – | -8.6 | -9.3 | -83.2 | -8.6 | -8.6 | -38.3 | 0 % | -38.3 | 0.0 |
| Kanal 2 | +3.4 | -8.7 | – | -8.7 | -9.3 | -82.9 | -8.7 | -8.7 | -38.4 | 0 % | -38.4 | 0.0 |
| Kanal 3 | +1.2 | -9.0 | – | -9.0 | -9.6 | -83.7 | -9.0 | -9.0 | -38.8 | 0 % | -38.8 | 0.0 |
| Kanal 4 | +2.6 | -9.4 | – | -9.4 | -10.0 | -83.3 | -9.4 | -9.4 | -39.2 | 0 % | -39.2 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|
| fs/8 (6000 Hz, sample-synchron) | Kanal 1 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.2 dB | -83.3 | 0.0 % |
| 1-kHz-Kamm | Kanal 1 | 1000.0516 | 0.0629 | 23/23 | k=1: 1000.050 Hz, -90.3 dB | -86.9 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 1 | 2320.9763 | 0.0012 | 10/10 | k=1: 2320.975 Hz, -75.1 dB | -75.6 | 0.0 % |
| Netz 50 Hz | Kanal 1 | 50.0284 | 0.0000 | 1/19 | k=1: 50.028 Hz, -88.2 dB | -91.5 | 0.0 % |
| Mischprodukte n·1000.0516 + m·5999.9999 Hz (m = ±1…±4) | Kanal 1 | 1000.0516 | 0.0214 | 64 | k=8·f1+1·f2: 14000.423 Hz, -99.7 dB | -90.5 | 0.0 % |
| stärkste übrige Linie (837.04 Hz) | Kanal 1 | 837.0409 | 0.0997 | 26/28 | k=1: 837.042 Hz, -5.7 dB | -8.7 | 99.5 % |
| stärkste übrige Linie (837.33 Hz) | Kanal 1 | 837.3456 | 0.1046 | 5/28 | k=1: 837.326 Hz, -28.6 dB | -32.4 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 2 | 5999.9999 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -83.7 dB | -83.8 | 0.0 % |
| 1-kHz-Kamm | Kanal 2 | 1000.0529 | 0.0050 | 23/23 | k=1: 1000.049 Hz, -84.4 dB | -84.1 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 2 | 2320.9763 | 0.0012 | 10/10 | k=1: 2320.975 Hz, -74.7 dB | -75.2 | 0.0 % |
| Netz 50 Hz | Kanal 2 | 50.0234 | 0.0042 | 2/19 | k=1: 50.029 Hz, -88.8 dB | -90.7 | 0.0 % |
| Mischprodukte n·1000.0529 + m·5999.9999 Hz (m = ±1…±4) | Kanal 2 | 1000.0529 | 0.0133 | 64 | k=8·f1+1·f2: 14000.421 Hz, -100.3 dB | -90.9 | 0.0 % |
| stärkste übrige Linie (837.04 Hz) | Kanal 2 | 837.0420 | 0.0854 | 26/28 | k=1: 837.042 Hz, -5.8 dB | -8.7 | 99.5 % |
| stärkste übrige Linie (837.33 Hz) | Kanal 2 | 837.3460 | 0.1025 | 5/28 | k=1: 837.326 Hz, -28.7 dB | -32.4 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 3 | 5999.9999 | 0.0001 | 3/3 | k=1: 6000.000 Hz, -83.9 dB | -84.1 | 0.0 % |
| 1-kHz-Kamm | Kanal 3 | 1000.0517 | 0.0629 | 23/23 | k=1: 1000.048 Hz, -87.3 dB | -86.1 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 3 | 2320.9763 | 0.0011 | 10/10 | k=1: 2320.975 Hz, -75.6 dB | -76.1 | 0.0 % |
| Netz 50 Hz | Kanal 3 | 50.0288 | 0.0000 | 1/19 | k=1: 50.029 Hz, -88.9 dB | -92.2 | 0.0 % |
| Mischprodukte n·1000.0517 + m·5999.9999 Hz (m = ±1…±4) | Kanal 3 | 1000.0517 | 0.0207 | 64 | k=8·f1+1·f2: 14000.423 Hz, -100.7 dB | -91.4 | 0.0 % |
| stärkste übrige Linie (837.04 Hz) | Kanal 3 | 837.0408 | 0.1006 | 26/28 | k=1: 837.042 Hz, -6.1 dB | -9.0 | 99.5 % |
| stärkste übrige Linie (837.33 Hz) | Kanal 3 | 837.3448 | 0.1035 | 5/28 | k=1: 837.326 Hz, -29.0 dB | -32.7 | 0.4 % |
| fs/8 (6000 Hz, sample-synchron) | Kanal 4 | 5999.9999 | 0.0002 | 3/3 | k=1: 6000.000 Hz, -84.4 dB | -84.4 | 0.0 % |
| 1-kHz-Kamm | Kanal 4 | 1000.0529 | 0.0099 | 23/23 | k=1: 1000.051 Hz, -81.6 dB | -82.1 | 0.0 % |
| LED-PWM (≈ 2,32 kHz) | Kanal 4 | 2320.9763 | 0.0012 | 10/10 | k=1: 2320.975 Hz, -75.2 dB | -75.7 | 0.0 % |
| Netz 50 Hz | Kanal 4 | 50.0225 | 0.0059 | 2/19 | k=1: 50.031 Hz, -89.1 dB | -89.7 | 0.0 % |
| Mischprodukte n·1000.0529 + m·5999.9999 Hz (m = ±1…±4) | Kanal 4 | 1000.0529 | 0.0137 | 67 | k=8·f1+1·f2: 14000.421 Hz, -100.8 dB | -91.3 | 0.0 % |
| stärkste übrige Linie (837.04 Hz) | Kanal 4 | 837.0409 | 0.1002 | 26/28 | k=1: 837.042 Hz, -6.4 dB | -9.4 | 99.5 % |
| stärkste übrige Linie (837.33 Hz) | Kanal 4 | 837.3460 | 0.1029 | 5/28 | k=1: 837.326 Hz, -29.3 dB | -33.1 | 0.4 % |

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 837.042 | -5.7 | 73.7 | other1·1 |
| 837.326 | -28.6 | 50.9 | other2·1 |
| 2511.128 | -35.2 | 61.9 | other1·3 |
| 837.700 | -43.6 | 35.9 | – |
| 836.334 | -45.4 | 33.9 | – |
| 2511.416 | -47.5 | 49.8 | – |
| 4185.211 | -47.4 | 54.2 | other1·5 |
| 838.099 | -52.7 | 26.9 | – |
| 1674.085 | -58.2 | 63.8 | other1·2 |
| 2511.725 | -61.4 | 36.1 | – |
| 838.707 | -61.0 | 18.7 | – |
| 835.372 | -63.3 | 15.8 | – |
| 5859.287 | -64.5 | 47.0 | other1·7 |
| 2510.317 | -66.7 | 29.8 | – |
| 4185.777 | -68.2 | 34.1 | – |
| 5859.046 | -70.4 | 40.7 | – |
| 3348.174 | -70.1 | 53.8 | other1·4 |
| 2512.197 | -71.7 | 26.1 | other2·3 |
| 7533.365 | -74.5 | 41.2 | other1·9 |
| 1674.363 | -74.5 | 47.5 | – |

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 837.042 | -5.8 | 74.0 | other1·1 |
| 837.326 | -28.7 | 51.2 | other2·1 |
| 2511.128 | -35.3 | 61.9 | other1·3 |
| 837.699 | -43.7 | 36.2 | – |
| 836.333 | -45.5 | 34.2 | – |
| 2511.416 | -47.6 | 49.8 | – |
| 4185.211 | -47.4 | 54.1 | other1·5 |
| 838.102 | -52.6 | 27.3 | – |
| 1674.085 | -58.7 | 63.4 | other1·2 |
| 2511.725 | -61.5 | 36.2 | – |
| 838.706 | -61.0 | 19.0 | – |
| 835.370 | -63.4 | 16.1 | – |
| 5859.287 | -64.6 | 47.0 | other1·7 |
| 2510.317 | -66.8 | 29.9 | – |
| 4185.777 | -68.3 | 34.0 | – |
| 5859.046 | -70.4 | 40.7 | – |
| 3348.174 | -70.5 | 53.6 | other1·4 |
| 2512.198 | -71.8 | 26.2 | other2·3 |
| 7533.365 | -74.6 | 41.6 | other1·9 |
| 2320.975 | -74.7 | 51.3 | led·1 |

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 837.042 | -6.1 | 74.0 | other1·1 |
| 837.326 | -29.0 | 51.2 | other2·1 |
| 2511.128 | -35.5 | 61.7 | other1·3 |
| 837.699 | -44.0 | 36.2 | – |
| 836.333 | -45.8 | 34.3 | – |
| 2511.416 | -47.8 | 49.6 | – |
| 4185.211 | -47.7 | 54.1 | other1·5 |
| 838.102 | -53.1 | 27.1 | – |
| 1674.085 | -58.8 | 63.5 | other1·2 |
| 2511.725 | -61.7 | 35.9 | – |
| 838.706 | -61.3 | 18.9 | – |
| 835.371 | -63.8 | 16.1 | – |
| 5859.287 | -64.8 | 47.0 | other1·7 |
| 2510.317 | -67.0 | 29.6 | – |
| 4185.777 | -68.5 | 34.0 | – |
| 5859.046 | -70.7 | 40.7 | – |
| 3348.174 | -70.4 | 54.2 | other1·4 |
| 2512.198 | -72.1 | 25.9 | other2·3 |
| 7533.365 | -74.9 | 41.4 | other1·9 |
| 1674.363 | -75.1 | 47.2 | – |

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|
| 837.042 | -6.4 | 73.7 | other1·1 |
| 837.326 | -29.3 | 50.8 | other2·1 |
| 2511.128 | -35.9 | 61.8 | other1·3 |
| 837.700 | -44.3 | 35.8 | – |
| 836.334 | -46.2 | 34.0 | – |
| 2511.416 | -48.2 | 49.8 | – |
| 4185.211 | -48.0 | 54.2 | other1·5 |
| 838.101 | -53.3 | 26.9 | – |
| 1674.084 | -59.6 | 63.2 | other1·2 |
| 2511.726 | -62.1 | 36.1 | – |
| 838.707 | -61.6 | 18.7 | – |
| 835.372 | -64.0 | 16.1 | – |
| 5859.287 | -65.1 | 47.2 | other1·7 |
| 2510.317 | -67.4 | 29.8 | – |
| 4185.777 | -68.9 | 34.0 | – |
| 5859.046 | -71.0 | 40.9 | – |
| 3348.174 | -71.1 | 53.6 | other1·4 |
| 2512.197 | -72.4 | 26.1 | other2·3 |
| 7533.365 | -75.1 | 41.6 | other1·9 |
| 2320.975 | -75.2 | 50.9 | led·1 |

## Zeitverhalten

Fensterlänge 2.3 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|
| fs8 | Kanal 1 | 7/7 | 2.06 | 21.69 | 0.33 |
| usb1k | Kanal 1 | 7/7 | 2.06 | 21.69 | 0.15 |
| led | Kanal 1 | 7/7 | 0.21 | 0.55 | 0.02 |
| mains50 | Kanal 1 | 7/7 | 348.27 | 657.90 | 0.41 |
| other1 | Kanal 1 | 7/7 | 28.62 | 338.19 | 0.03 |
| other2 | Kanal 1 | 7/7 | 28.62 | 338.19 | 0.03 |
| fs8 | Kanal 2 | 7/7 | 1.94 | 21.56 | 0.43 |
| usb1k | Kanal 2 | 7/7 | 3.13 | 33.60 | 0.26 |
| led | Kanal 2 | 7/7 | 0.23 | 1.47 | 0.02 |
| mains50 | Kanal 2 | 7/7 | 435.08 | 3130.56 | 0.67 |
| other1 | Kanal 2 | 7/7 | 28.62 | 338.17 | 0.03 |
| other2 | Kanal 2 | 7/7 | 28.62 | 338.17 | 0.03 |
| fs8 | Kanal 3 | 7/7 | 1.99 | 21.77 | 0.36 |
| usb1k | Kanal 3 | 7/7 | 3.29 | 33.74 | 0.20 |
| led | Kanal 3 | 7/7 | 0.25 | 1.77 | 0.02 |
| mains50 | Kanal 3 | 7/7 | 248.79 | 2446.22 | 0.43 |
| other1 | Kanal 3 | 7/7 | 28.62 | 338.18 | 0.03 |
| other2 | Kanal 3 | 7/7 | 28.62 | 338.18 | 0.03 |
| fs8 | Kanal 4 | 7/7 | 1.89 | 21.80 | 0.56 |
| usb1k | Kanal 4 | 7/7 | 4.84 | 13.73 | 0.27 |
| led | Kanal 4 | 7/7 | 0.23 | 0.09 | 0.02 |
| mains50 | Kanal 4 | 7/7 | 457.15 | 7619.89 | 0.71 |
| other1 | Kanal 4 | 7/7 | 28.62 | 338.15 | 0.03 |
| other2 | Kanal 4 | 7/7 | 28.62 | 338.15 | 0.03 |

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, 0,2–20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.05 | 0.08 s (12.69 Hz) | 8.5 |
| Kanal 1 | 837.0 Hz ± 10 | 1.51 | 4.61 s (0.22 Hz) | 47.6 |
| Kanal 2 | breitbandig | 0.05 | 0.26 s (3.90 Hz) | 18.0 |
| Kanal 2 | 837.0 Hz ± 10 | 1.51 | 4.61 s (0.22 Hz) | 48.7 |
| Kanal 3 | breitbandig | 0.05 | 0.49 s (2.06 Hz) | 12.4 |
| Kanal 3 | 837.0 Hz ± 10 | 1.51 | 4.61 s (0.22 Hz) | 46.4 |
| Kanal 4 | breitbandig | 0.05 | 0.26 s (3.90 Hz) | 14.2 |
| Kanal 4 | 837.0 Hz ± 10 | 1.51 | 4.61 s (0.22 Hz) | 44.5 |

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
| Kanal 1 | 1.00 | 1.00 | 1.00 | 1.00 |
| Kanal 2 | 1.00 | 1.00 | 1.00 | 1.00 |
| Kanal 3 | 1.00 | 1.00 | 1.00 | 1.00 |
| Kanal 4 | 1.00 | 1.00 | 1.00 | 1.00 |

## Abbildungen

### Spektrogramm

![Spektrogramm](M3_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](M3_psd.png)

### Kammprofile

![Kammprofile](M3_combs.png)

### Zeitverlauf

![Zeitverlauf](M3_timeline.png)

## Notiz aus dem Manifest

> Zu hören: Sinuston ≈ 838 Hz (≈ −6 dBFS Spitze, kein Clipping), etwas „hohl/obertonreich“.
> Fast nur ungerade Obertöne → typisch für einen aus dem Dreieck geformten VCO-Sinus, vermutlich die DPO selbst.
> 96 kHz / 16 Bit hochgerechnet, ≈ 9 s. Ursprünglich channel-{1..4}-002.wav.
