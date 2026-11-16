# Report G4-in-no-out: G4-in-no-out – acdc1 Eingänge offen, Alltags-Aufbau, Ausgänge frei, 120 s

| Feld | Wert |
|---|---|
| date | 2026-11-15 |
| device | acdc1, Firmware Build 1d v22.4.r-thru1d |
| test | G4-in-no-out: wie G4-in, aber Ausgänge frei (Alltag: kein AC/DC-Out → UMC-In). UMC-Ausgänge an Boxen/Kopfhörer |
| gain | g12 |
| usb | usb-duplex, passiver Hub → Monitor-Hub → TB-Hub |
| patch | Slot 1: ACDC (Default-Patch) |
| Datei(en) | `20261115_acdc1_g4-in-daily-no-out_g12_usb-duplex.4chan.000.wav` |
| Format | 48000 Hz, 122.3 s, 4 Kanäle |
| Erzeugt mit | `uv run python -m analysis G4-in-no-out --ref A5-b1d` |

**Hinweise:**

- Datei ist digital stumm (< −150 dB). Beim Default-Patch heißt das: Gain auf 0, nach dem Patch kommt nichts mehr hinzu.

Pegel: Linien als Sinus-Amplitude (Vollaussteuerungs-Sinus = 0 dBFS). Rausch-Kennzahlen im Hörband (Hochpass 20 Hz), Drift < 20 Hz separat. RMS als 20·log10(RMS) (Vollaussteuerungs-Sinus = −3 dB). Störanteil = Leistung der bekannten Störfamilien (fs/8, 1-kHz-Kamm, LED, Netz, Mischprodukte) / Rauschleistung. Rauschleistung = AC-Leistung minus „übrige Linien“ (other*, z. B. Testsignal). Gewinn Notch-Bank = Rauschen vorher/nachher, wenn alle Störfamilien entfernt wären.

## Kennzahlen pro Kanal

| Kanal | DC [% FS] | AC-RMS gesamt [dB] | Drift < 20 Hz [dB] | RMS ≥ 20 Hz [dB] | RMS A-bew. [dB] | 20–200 Hz | 200 Hz–20 kHz | übrige Linien [dB] | Rauschen [dB] | Störanteil | Rest ohne Störlinien [dB] | Gewinn Notch-Bank [dB] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanal 1 | +0.0 | -300.0 | – | -300.0 | -300.0 | -300.0 | -300.0 | – | -300.0 | 0 % | -300.0 | 0.0 |
| Kanal 2 | +0.0 | -300.0 | – | -300.0 | -300.0 | -300.0 | -300.0 | – | -300.0 | 0 % | -300.0 | 0.0 |
| Kanal 3 | +0.0 | -300.0 | – | -300.0 | -300.0 | -300.0 | -300.0 | – | -300.0 | 0 % | -300.0 | 0.0 |
| Kanal 4 | +0.0 | -300.0 | – | -300.0 | -300.0 | -300.0 | -300.0 | – | -300.0 | 0 % | -300.0 | 0.0 |

## Linienfamilien (Kämme)

f0 aus Least-Squares-Fit über alle gefundenen Harmonischen. Residuum = RMS-Abweichung der Linien vom Raster k·f0.

| Familie | Kanal | f0 [Hz] | Residuum [Hz] | Linien | stärkste Linie | Summenpegel [dB RMS] | Anteil |
|---|---|---|---|---|---|---|---|

## Stärkste Linien (Kanal für Kanal)

### Kanal 1

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

### Kanal 2

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

### Kanal 3

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

### Kanal 4

| Frequenz [Hz] | Pegel [dBFS] | über Boden [dB] | Familie·k |
|---|---|---|---|

## Zeitverhalten

Fensterlänge 10.0 s, 50 % Überlappung.

| Familie | Kanal | Fenster gültig | f0-Streuung [ppm] | f0-Drift [ppm/min] | Pegelstreuung [dB] |
|---|---|---|---|---|---|

**Periodische Pegelschwankung** (Spektrum der 10-ms-Hüllkurve, ab 4 Perioden pro Aufnahme bis 20 Hz):

| Kanal | Band | Streuung [dB] | stärkste Periode | Prominenz [dB] |
|---|---|---|---|---|
| Kanal 1 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |
| Kanal 1 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |
| Kanal 2 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |
| Kanal 2 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |
| Kanal 3 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |
| Kanal 3 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |
| Kanal 4 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |
| Kanal 4 | breitbandig | 0.00 | 30.58 s (0.03 Hz) | 53.4 |

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
| Kanal 1 | 0.00 | 0.00 | 0.00 | 0.00 |
| Kanal 2 | 0.00 | 0.00 | 0.00 | 0.00 |
| Kanal 3 | 0.00 | 0.00 | 0.00 | 0.00 |
| Kanal 4 | 0.00 | 0.00 | 0.00 | 0.00 |

## Vergleich mit Referenz A5-b1d

| Kanal | AC-RMS [dB] | Referenz [dB] | Δ [dB] | Linienanteil | Referenz |
|---|---|---|---|---|---|
| Kanal 1 | -300.0 | -72.5 | -227.5 | 0 % | 57 % |
| Kanal 2 | -300.0 | -73.0 | -227.0 | 0 % | 66 % |
| Kanal 3 | -300.0 | -75.0 | -225.0 | 0 % | 74 % |
| Kanal 4 | -300.0 | -72.6 | -227.4 | 0 % | 64 % |

## Abbildungen

### Spektrogramm

![Spektrogramm](G4-in-no-out_spectrogram.png)

### Langzeit-Spektrum

![Langzeit-Spektrum](G4-in-no-out_psd.png)

### Zeitverlauf

![Zeitverlauf](G4-in-no-out_timeline.png)

## Notiz aus dem Manifest

> Datei-Werte mit Host-Faktor 2. Vergleich mit A5-b1d (TB-Hub direkt, Host-Software Duplex mit Stille).
