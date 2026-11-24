# Messlog

Jede Messung bekommt einen Eintrag. Kurzfassung in der Tabelle, Details darunter.
Pegel sind Linienamplituden in dBFS (Sinus mit Vollaussteuerung = 0 dBFS), sofern nicht anders angegeben.

| # | Datum | Gerät | Dateien | Setup | Befund | Fazit |
|---|---|---|---|---|---|---|
| M1 | 2026-11-13 | acdc2 (DIY) | `recordings/channel-{1..4}.wav` | Kein Signal, Eingänge gebrückt 1↔2 / 3↔4, Gain 12 Uhr, USB-Stream aktiv | 1-kHz-Kamm bei **1000,05 Hz**, −80…−96 dBFS. 6-kHz-Linie exakt 6000,00 Hz. Gesamt −77 dBFS RMS, davon ≈ 55–65 % im Kamm | Kamm vorhanden, aber **≈ 50 dB schwächer als bei atau** |
| M2 | 2026-11-13 | acdc2 (DIY) | `recordings/channel-{1..4}-001.wav` | wie M1, Gain voll | Kamm −66…−70 dBFS, LED-Linie **2320,98 Hz** jetzt −80 dBFS (M1: −110). Gesamt −64 dBFS RMS | Kamm + LED-Linien ≈ 90 % der Leistung. Notch-Bank brächte ≈ 10 dB |
| M3 | 2026-11-13 | acdc2 (DIY) | `recordings/channel-{1..4}-002.wav` | Sinus ≈ 838 Hz (Make Noise DPO) per Stackcable auf alle 4 Eingänge, Gain 11:45 | THD ≈ 3,6 %, fast nur ungerade Obertöne. LED-Linie 2320,98 Hz −75 dBFS, neue Linie 173,8 Hz −84 dBFS | Klirren vermutlich von der DPO. LED-Linie **pegelabhängig** → stützt H3 |
| S2-1 | 2026-11-13 | acdc2 (DIY), v22.4.q | `20261114_acdc2_open-inputs_g12_usb-stream.4chan.000.wav` (122 s) | Eingänge offen, Gain 12 Uhr, USB-Stream | ≥ 20 Hz −69…−72 dBFS. Kamm 1000,0528 Hz (k=1 −71…−76 dB), 6 kHz −76…−79 dB. **Musterperiode 3,13 s** auf allen Kanälen (Prominenz 33 dB) | Störanteil 79–90 %, Notch-Gewinn 6,8–9,9 dB. Mischprodukt-Mechanismus bestätigt |
| S2-2 | 2026-11-13 | acdc2 (DIY), v22.4.q | `20261114_acdc2_open-inputs_g17_usb-stream.4chan.000.wav` (60 s) | wie S2-1, Gain voll | ≥ 20 Hz −59…−62 dBFS (+8…10 dB). DC 11–30 % FS. LED-Linie +35 dB (−70…−72 dB). Periode 3,17 s | Gain wirkt als ≈ +9 dB digital, LED-Linie folgt dem DC-Pegel |
| S2-3 | 2026-11-13 | acdc2 (DIY), v22.4.q | `20261114_acdc2_open-inputs_g7_usb-stream.4chan.000.wav` (60 s) | wie S2-1, Gain 7 Uhr (Linksanschlag) | **digital stumm** (−194 dB) | Default-Patch multipliziert mit 0. Nach dem Patch (USB-TX, Host) kommt **nichts** hinzu |
| S2-4 | 2026-11-13 | acdc1, v22.5.0 | `20261114_acdc1_open-inputs_g12_usb-stream.4chan.000.wav` (120 s) | wie S2-1 | Kamm bei **999,8663 Hz** (k=1 −72…−76 dB), 6 kHz −77…−81 dB. Musterperiode im 1-kHz-Band **1,24 s**. DC-Drift < 1 Hz stark (Kanal 1). Driftender Ton 352→468 Hz, −97 dB | Gleiches Linienbild wie acdc2, nur mit anderem Taktversatz. Hörband-Rauschen ähnlich |
| S2-6 | 2026-11-13 | acdc1, v22.5.0 | `20261114_acdc1_nohub_open-inputs_g12_usb-stream.4chan.000.4chan.000.wav` (119 s) | wie S2-4, aber USB **direkt am Mac** statt am Thunderbolt-Hub | Kamm wandert 999,8663 → **999,9908 Hz** (+124,5 ppm), LED (Gerätetakt) unverändert. Kamm ≈ 3 dB leiser, dafür neue 119,944-Hz-Familie (−81…−85 dB RMS) | **H1 bestätigt: Der Kamm ist an den USB-SOF des Host-Controllers gekoppelt.** Direkt am Mac insgesamt ≈ 2 dB lauter (120-Hz-Brumm) |

Gerät acdc2: Firmware **v22.4.q**, Slot 1 = Patch „ACDC“ (9,32 KB, Default-Patch), CPU 15 %, UUID `00250049:31315102:39333437` (Device-Status openwarelab, 2026-11-13).

Auswertung: `uv run python -m analysis M1` (bzw. M2, M3) → `out/M1/` usw. Messdaten-Metadaten in `recordings/manifest.toml`.
Alte Plots des ersten Skripts: `out/v0/*.png`. Ihre Texte enthalten noch die überholte Gain-Deutung.

Dateien umbenannt (2026-11-13): `channel-N.wav` → `20261113_acdc2_inputs-bridged_g12_usb-stream_chN.wav`, `channel-N-001.wav` → `…_g17_…`, `channel-N-002.wav` → `20261113_acdc2_sine838-dpo_g1145_usb-stream_chN.wav`.

## Einschränkungen dieser ersten Serie (M1–M3)

- Gerät: **acdc2 (DIY-Variante)**, nachgetragen am 2026-11-13. UUID und Firmware siehe oben bzw. Gerätetabelle in `CLAUDE.md`.
- **96 kHz / 16 Bit** im File, das AC/DC liefert aber nur 48 kHz. Die Aufnahme-Software hat also hochgerechnet. Oberhalb ≈ 22 kHz ist das File leer (−153 dB) **[gemessen]**. Künftig nativ mit 48 kHz und 32 Bit float aufnehmen.
- Nur **7–10 s** pro Messung statt 60 s. Für Zeitstabilität und Klick-Detektion zu kurz.
- Dateinamen folgen noch nicht der Konvention `YYYYMMDD_<geraet>_<test>_<gain>_<usb-zustand>.wav`.
- Patch: laut Device-Status Slot 1 = „ACDC“ (Default-Patch, Knob = **digitaler** Gain). Nachträglich festgestellt, vermutlich derselbe Stand wie bei der Aufnahme.
- „Eingänge gebrückt“ heißt: Kabel von Eingang 1 auf Eingang 2 und von 3 auf 4. Kein Kurzschlussstecker.

## Details

### Nachmessung mit Peak-Interpolation (2026-11-13)

Volle FFT über die ganze Datei (Hann-Fenster, Auflösung ≈ 0,1 Hz) und parabolische Interpolation. Das Skript war ein Wegwerf-Skript und ist noch nicht in `analysis/`. Werte für Kanal 2, die anderen Kanäle liegen innerhalb ±0,01 Hz.

| Linie | M1 (g12) | M2 (voll) | M3 (Sinus) | Bemerkung |
|---|---|---|---|---|
| 50 Hz | 50,01 Hz, −95 dB | −85 dB | −89 dB | schwach, Netzbrumm |
| 1 kHz | **1000,05 Hz**, −82 dB | −67 dB | −84 dB | Obertöne bei 2000,11 / 3000,16 → f0 ≈ 1000,053 Hz |
| 6 kHz | **6000,00 Hz**, −83 dB | −73 dB | −84 dB | exakt fs/8 → an den Sample-Takt gekoppelt |
| 2,32 kHz | 2320,98 Hz, −110 dB | **−80 dB** | **−75 dB** | LED-PWM (berechnet 2320,4 Hz [Code]). Nur bei Pegel/DC sichtbar |
| 4,64 kHz | 4641,95 Hz, −109 dB | −79 dB | −78 dB | 2. Harmonische der LED-PWM |
| 173 Hz | – | – | 173,81 Hz, −84 dB | nur mit DPO, Herkunft unklar |

**Kanalunterschiede beim 1-kHz-Kamm (M1):** Kanal 1 −96 dB, Kanal 3 −87 dB, Kanal 2 −82 dB, Kanal 4 −80 dB. Die 6-kHz-Linie ist auf allen Kanälen gleich (−82…−85 dB).

**Korrelation** zwischen den Kanälen: M1 0,71–0,92, M2 0,93–0,98, M3 1,0.

### Woraus besteht die Rauschleistung? (Kanal 2)

| Anteil | M1 (g12) | M2 (voll) |
|---|---|---|
| Gesamt (AC-RMS) | −77,1 dBFS | −63,9 dBFS |
| < 200 Hz | −88 dBFS | −81 dBFS |
| 1-kHz-Kamm (k = 1…23, ±3 Hz, inkl. 6/12/18 kHz) | −79,0 dBFS | −66,7 dBFS |
| LED-Kamm (k·2320,98 Hz) | −96 dBFS | −68,3 dBFS |
| 200 Hz–20 kHz **ohne** Kamm und LED | −83,6 dBFS | −74,9 dBFS |

- Der tieffrequente „orange Teppich“ im Spektrogramm sieht laut aus, trägt aber wenig Leistung bei (wenige Bins).
- Bei Gain 12 macht der 1-kHz-Kamm ≈ 55–65 % der Leistung aus (je nach Kanal). Eine Notch-Bank brächte ≈ 4–5 dB.
- Bei vollem Gain machen Kamm und LED-Linien ≈ 90 % aus. Eine Notch-Bank brächte ≈ 10 dB.

### Deutung

1. **Der 1-kHz-Kamm ist nicht an den Sample-Takt gekoppelt** [gemessen]. Die 6-kHz-Linie liegt exakt auf 6000,00 Hz, ist also sample-synchron. Der Kamm liegt dagegen bei 1000,053 Hz, also 53 ppm daneben. Er kommt aus einer anderen Taktdomäne: USB-SOF des Hosts oder ein geräteinterner Timer (z. B. FreeRTOS-Tick).
   - Bei SOF-Kopplung und der aus dem Code berechneten Samplerate von 47 991 Hz wären 1000,19 Hz zu erwarten [Code]. Gemessen sind 1000,05 Hz. Entweder läuft der Codec real mit ≈ 47 997,5 Hz, oder die Quelle ist nicht der SOF [Hypothese].
   - Entscheidender Test: die echte Samplerate des AC/DC messen (siehe TODO, Phase 2).
2. **Die 2,32-kHz-Linie ist sehr wahrscheinlich die LED-PWM** [gemessen, Frequenz + Pegelabhängigkeit]. Die Frequenz passt zur Rechnung aus dem Code. Die Linie ist ohne Signal bei Gain 12 praktisch weg (−110 dB) und erscheint, sobald die LEDs leuchten: bei vollem Gain (der DC-Offset von 15 % lässt die LEDs leuchten) und mit Sinus. Beweis steht noch aus: LED-aus-Patch.
3. **Der Gain-Knob wirkt digital im Patch** [belegt]. Die Aussage im Plot-Text von M2 („kommen VOR der Gain-Stufe rein, nicht erst im Wandler“) ist so nicht haltbar. Richtig ist: Die Störungen stecken in den ADC-Daten und werden vom Patch mitverstärkt.
   - DC-Offset (+9 dB), 50 Hz (+9…12 dB) und Rauschboden (+8 dB) steigen ähnlich → digitaler Gain ≈ +9 dB (Faktor ≈ 2,8).
   - Der 1-kHz-Kamm steigt um +14…26 dB, die LED-Linie um +30 dB. Das ist **mehr** als der Gain. Für die LED-Linie erklärt das die Pegelabhängigkeit. Warum der 1-kHz-Kamm überproportional steigt, ist offen [Hypothese: ebenfalls an LED-Strom oder Pegel gekoppelt, oder er schwankt über die Zeit].
4. **Gemeinsame Quelle:** Hohe Korrelation auch zwischen nicht verbundenen Kanälen (1↔3: 0,92) spricht für Versorgung, Referenz oder Masse statt Rauschen pro Kanal [Hypothese].
5. **Vergleich mit atau:** Er sah ≈ −30 dB bei Gain 12, hier sind es −80…−96 dBFS. Entweder ist mein Gerät deutlich besser, oder atau's Anzeige war anders skaliert. Offen.

### Neuauswertung mit `analysis/` (2026-11-13)

Das neue Tool fittet f0 gewichtet über alle Harmonischen und trennt Linienfamilien. Ergebnisse M1, alle Kanäle [gemessen]:

| Familie | f0 | Linien | Anteil an der Rauschleistung (Kanal 1/2/3/4) |
|---|---|---|---|
| fs/8 (sample-synchron) | 6000,0000 Hz | 3 | 35 / 27 / 33 / 20 % |
| 1-kHz-Kamm | **1000,0527 Hz** (alle 4 Kanäle gleich, ±0,1 mHz) | 23/23 | 13 / 33 / 21 / 50 % |
| **Mischprodukte** n·1000,0527 + m·6000 Hz | – | ≈ 72 | 4–7 % |
| LED-PWM | 2320,9765 Hz | 10 | ≈ 1 % (M2: 20–40 %) |
| Netz | 50,012 Hz | 4–7 | 0,4–3 % |
| Störanteil gesamt | | | **60–75 %** (M2: 84–89 %) |
| Gewinn einer idealen Notch-Bank | | | **4,0–6,0 dB** (M2: 7,9–9,6 dB) |

**Neuer Befund – Mischprodukte [gemessen]:** Um jedes k·1000 Hz liegt ein Büschel von Linien im Abstand ≈ 0,316 Hz. Alle passen auf **f = n·1000,0527 + m·6000,000 Hz** (m = ±1…±4, n auch negativ). Das heißt:
- 1-kHz-Störer und 6-kHz-Störer überlagern sich nicht nur, sie **wirken nichtlinear zusammen** (z. B. weil es stört, wenn USB-Verarbeitung und Audio-Block-Callback zeitlich zusammenfallen) [Hypothese].
- Die relative Phase der beiden Takte wiederholt sich alle 1/(6·0,0527 Hz) ≈ **3,16 s**. Die Hüllkurve zeigt in M2 auf allen Kanälen eine Periode von ≈ 3,7 s (Prominenz ≈ 20 dB). Bei 7,4 s Aufnahme ist die Auflösung nur 0,135 Hz, das passt also im Rahmen. Bestätigung mit ≥ 60 s steht aus.
- **Parallele zu antisvin:** Er hörte eine Periode von ≈ 0,8 s. Mit der im Code berechneten Samplerate (47 991 Hz) und einem 1-kHz-Takt aus dem Host läge die Schwebung bei 1/(6·0,1875 Hz) ≈ 0,89 s [Hypothese]. Dieselbe Mechanik mit anderem Taktversatz würde beide Beobachtungen erklären.

**Woher die 6 kHz kommen [Code]:** Firmware v22.4.q = Commit `e81cfc3` (2022-06-27) aus Klangs ungemergtem Branch `hack/acdc-output-levels`. Dort gilt `AUDIO_BLOCK_SIZE 8` (seit v22.4.k „bs=8, hpf, leds“), der Audio-Callback läuft also mit 48 000 / 8 = **6 kHz**. Upstream v22.5.0 hat Blockgröße 16 → 3 kHz. Takt-PLL und LED-Timer sind in beiden Ständen gleich, der Input-Gain ist 88 statt 104.

**Woher die 1000,0527 Hz kommen:** offen.
- Ein geräteinterner 1-kHz-Timer (FreeRTOS-Tick aus dem CPU-Takt) läge relativ zum Sample-Takt bei ≈ 1000,19–1000,22 Hz [Code + LED-Linie als Referenz]. Gemessen sind 1000,0527 Hz → eher **kein** interner Timer.
- USB-SOF des Hosts passt, wenn der Mac-Takt relativ zum Quarz des AC/DC um ≈ −165 ppm abweicht. Das ist viel, aber bei zwei unabhängigen Quarzen nicht unmöglich [Hypothese].
- Entscheidender Test: **anderer Rechner als Host**. Verschiebt sich f0 dann, ist es der SOF.

**Zeitverhalten:** In Fenstern unter ≈ 10 s lassen sich die 0,316-Hz-Nachbarlinien nicht trennen. Die f0-„Streuung“ in M1/M2 ist daher Messartefakt, nicht Drift.

### Serie 2 (S2-1 … S2-4, 2026-11-13)

Aufnahmen: 4-Kanal-WAV, Float32, 96 kHz (wieder hochgerechnet, aber sauber 2×: fs/8 liegt exakt auf 6000,0000 Hz), offene Eingänge. Dateinamen tragen 20261114, aufgenommen am 2026-11-13. Auswertung: `out/S2-*/`. Seit dieser Serie rechnet das Tool Rausch-Kennzahlen im Hörband (Hochpass 20 Hz) und weist die Drift < 20 Hz separat aus.

**1. Mischprodukt-Mechanismus bestätigt [gemessen].** Die Musterperiode folgt aus dem Abstand von 6·f1k zur 6-kHz-Blockrate, vorhergesagt vor der Messung:

| Gerät | f1k im File | vorhergesagt 1 / (6·f1k − 6000) | gemessen (Hüllkurve) |
|---|---|---|---|
| acdc2 | 1000,0528 Hz | 3,16 s | **3,13 s** (S2-1), 3,17 s (S2-2) |
| acdc1 | 999,8663 Hz | 1,247 s | **1,24 s** (S2-4, 1-kHz-Band) |

antisvins „≈ 0,8 s“ wäre dieselbe Mechanik bei einem Versatz von ≈ 0,21 Hz.

Gerät acdc1: Firmware **v22.5.0** (offizielles Release), Slot 1 = „ACDC“ (9,93 KB), CPU 8 %, Storage 10 KB, UUID `0039001c:31315101:39333437` (Device-Status, 2026-11-13).

**2. acdc1 und acdc2 haben ein unterschiedliches Verhältnis Sample-Takt / CPU-Takt [gemessen].** Die LED-PWM hängt am CPU-Takt, die Linien im File am Sample-Takt:

| | LED im File | 1-kHz-Kamm im File | 6-kHz-Linie |
|---|---|---|---|
| acdc2 | 2320,9763 Hz | 1000,0528 Hz | 6000,0000 Hz |
| acdc1 | 2320,5448 Hz | 999,8663 Hz | 6000,0000 Hz |
| Verhältnis acdc2/acdc1 | **+186,0 ppm** | **+186,5 ppm** | 0 |

- 186 ppm entspricht zufällig (?) genau dem Verhältnis 48 000 / 47 991,07 Hz (Taktteiler-Rundung laut Code).
- **Korrektur (nach Device-Status acdc1 = v22.5.0):** Meine Vermutung „acdc1 läuft mit v22.4.r/s und exakt 48 kHz“ ist falsch. PLL1/2/3, SAI-Konfiguration und LED-Timer sind in v22.5.0 und v22.4.q **identisch** [Code]. Mit diesen Teilern sind exakt 48 kHz rechnerisch nicht möglich. Unterschiedlich sind nur der HAL-Stand (`Libraries`: v22.5.0 `e102c6f`, v22.4.q `9e8f64e`), `OutputDrive` und die Hardware (acdc2 = DIY). **Ursache der 186 ppm: offen.**
  - **Nachtrag 2026-11-16:** Geklärt durch D3/D3a und D10. acdc1 trug nicht das Release v22.5.0, sondern einen Hack-Branch-Build mit diesem Etikett. Sein Takt ist der von v22.4.r (PLL3 P/Q 8, FRACN 262, exakt 48 kHz), acdc2 hat den von v22.4.q (P/Q 2, FRACN 0, ≈ 47 991 Hz) [gemessen: Disassembly, D10]. Die ursprüngliche Vermutung „v22.4.r/s“ war also richtig. Auch der nächste Punkt erledigt sich damit: Blockgröße 8 ist die Vorgabe des Hack-Branchs.
- **6-kHz-Linie auch auf acdc1 (v22.5.0, Default-Blockgröße 16):** Die Blockgröße kommt aus den gespeicherten Settings (`audio_blocksize`). Der Settings-Code prüft nur `sizeof(Settings) ^ 0xf0f0f0f0` [Code]. Alte Settings mit Blockgröße 8 aus einer früheren Hack-Firmware überleben deshalb ein Update, solange die Struktur gleich groß ist [Hypothese]. Gegenprobe: Beide Module zeigen dasselbe Linienbild (6 kHz dominant, nur schwache ungerade 3-kHz-Vielfache bei −105…−130 dB).

**3. Woher kommt der 1-kHz-Kamm? Eingegrenzt, aber nicht entschieden.** Das Verhältnis Kamm/LED ist in beiden Modulen gleich (0,430880, Abweichung < 1 ppm). Zwei Erklärungen:
- (A) **Externer Takt (USB-SOF des Hosts/Hubs, ≈ 999,83 Hz)**. Dann müssten die Quarze beider Module auf < 1 ppm übereinstimmen. Möglich, aber unwahrscheinlich (typische Streuung ±10–20 ppm).
- (B) **Moduleigener Takt aus dem CPU-Quarz bei ≈ 999,83 Hz** (kein exakter 1-kHz-Timer, der läge bei 1000,22 Hz). Einen passenden Timer im Code habe ich noch nicht gefunden.
- Entscheidung per Test: AC/DC **direkt am Mac statt am Thunderbolt-Hub** (anderer USB-Controller → anderer SOF-Takt). Verschiebt sich f1k, gilt (A). Endgültig: USB abziehen (Test S3).
- Hinweis: Die Rechnung „LED = 240 MHz / (101·1024)“ ergibt relativ zu den nominellen Sample-Raten in beiden Modulen 32 ppm Abweichung. Diese Differenz ist systematisch, kürzt sich bei Verhältnissen aber heraus. Absolute Frequenzaussagen daher nur ± ≈ 30 ppm.

**4. Nach dem Patch kommt nichts hinzu [gemessen].** S2-3 (Gain = 0) ist digital stumm. Der USB-Sendepfad, der Rechner und die DAW fügen keine Störung hinzu. Alles steckt in den ADC-Daten **vor** dem Patch.

**5. Weitere Befunde:**
- Offene Eingänge sind ≈ 6–8 dB lauter als gebrückte (S2-1 vs. M1). Kamm k=1 auf Kanal 2: −70,6 vs. −82,4 dB.
- acdc1 Kanal 1: starke DC-Drift < 1 Hz (−64 dB). Kanal 1 hat einen um ≈ 8 dB höheren Breitband-Boden als die anderen Kanäle. Die Breitband-Hüllkurve schwankt mit 3,2 Hz (Streuung ≈ 3 dB), Ursache offen.
- acdc1: ein langsam steigender Ton 352 → 468 Hz (≈ 1,2 Hz/s, −97 dB), vermutlich von außen (Oszillator im Case?).
- Klicks: in keiner Messung (H5 vorerst ohne Befund).

### S2-6: Hub gegen direkt am Mac (acdc1, 2026-11-13)

| | S2-4 (Thunderbolt-Hub) | S2-6 (direkt am Mac) |
|---|---|---|
| 1-kHz-Kamm f0 | 999,8663 Hz | **999,9908 Hz** |
| LED-PWM (Gerätetakt) | 2320,5448 Hz | 2320,5447 Hz |
| 6-kHz-Linie | 6000,0000 Hz | 6000,0000 Hz |
| Kamm k=1 | −72…−76 dB | −75…−79 dB |
| Störanteil / Notch-Gewinn | 60–81 % / 4–7 dB | 33–41 % / 1,7–2,3 dB |
| neue Familie | – | 119,944 Hz (17–28 Harmonische), −81…−85 dB RMS, dazu 179,92 Hz |
| Rauschen ≥ 20 Hz | −69,7 / −73,1 / −73,7 / −73,2 dB | −67,6 / −70,8 / −70,2 / −71,4 dB |

**Deutung:**
1. **H1 [gemessen]:** Nur der USB-Anschluss wurde geändert, der Gerätetakt (LED, 6 kHz) blieb gleich, und der Kamm wanderte um +124,5 ppm. Der 1-kHz-Kamm folgt also dem **SOF-Takt des USB-Host-Controllers**. Der USB-Controller im Thunderbolt-Hub läuft ≈ 124,5 ppm langsamer als der im Mac. Erklärung (B) „moduleigener Takt“ ist damit vom Tisch.
2. Folge für die Musterperiode: direkt am Mac 1/(6·0,0092 Hz) ≈ 18 s (vorhergesagt). Im 1-kHz-Band von Kanal 1 und 3 zeigt sich ≈ 24 s (Prominenz 18 dB). Bei 119 s Aufnahme sind das nur 5 Perioden, die Auflösung reicht nicht für eine Bestätigung.
3. **Folge für ein Notch-Filter:** f0 hängt vom USB-Controller ab (Hub vs. Mac: 0,12 Hz bei 1 kHz, 2,9 Hz bei 23 kHz). Ein fest eingestelltes Notch-Filter muss pro Setup neu gemessen werden, oder es muss f0 selbst nachführen.
4. **Neu direkt am Mac:** eine Familie bei 119,944 Hz (≈ 120 Hz, kein Vielfaches von 50 Hz). Vielleicht kommt sie vom Mac selbst (z. B. Display mit 120 Hz, Netzteil) über die direkte Masseverbindung [Hypothese]. Am Hub nicht vorhanden. Insgesamt ist „direkt“ deshalb nicht besser.
5. Bei 120 s fand die erweiterte Modulationssuche (ab 4 Perioden pro Aufnahme) in S2-4 zusätzlich ≈ 7,5 s im 1-kHz-Band. Das entspricht 1/(1000 − f1k) = 7,48 s, also einer Schwebung zwischen der Kammlinie und einem Anteil bei exakt 1000 Hz. Noch nicht weiter untersucht.

### Durchleitung Eingang → Ausgang (S3-Planung, 2026-11-14)

Bei der Planung von S3 (Ausgänge über Startup → UMC aufnehmen, USB ab / gesteckt / Stream) hat sich gezeigt, dass die Ausgänge ohne Rechner-Playback stumm sind.

**Beobachtungen [gemessen, Nutzer]:**
- **acdc1 (v22.5.0), Kaltstart ohne USB**, DPO in In 1, Gain 12 Uhr, Out 1 abgehört: **kein Signal**.
- Mit und ohne USB-Kabel ist an den Ausgängen nichts zu hören, solange nicht eine Software (Host-Software) den AC/DC-Eingang auf den AC/DC-Ausgang zurückschickt.
- „_Lich_Nichts“ (Durchleit-Patch aus der Library, per Load im RAM) verhält sich gleich. Getestet wurde ohne Neustart nach Host-Betrieb.

**Was der Code sagt [Code]:**
- Der Default-Patch „ACDC“ (Martin Klang, Library, Quelle gesichert in `owl-patches/library/ACDC_ACDCPatch.hpp`) ist ein **4-Kanal-VCA mit Durchleitung**: Ausgang = (Eingang + Offset) × (Knob·2)². Knob 12 Uhr → ×1, Rechtsanschlag → ×4. Die LEDs zeigen Pegel/Clipping.
- `_Lich_Nichts` = FAUST `process = _,_;` (2 Kanäle).
- v22.5.0 (`62a0187`, `usbd_rx_convert()`): Ohne aktiven USB-Playback-Stream wird der Patch-Ausgang **nicht** überschrieben → er ginge an die Buchsen. RX wird nur bei SetInterface Alt 0 oder USB-DeInit gestoppt.
- **v22.4.q (acdc2) enthält `237c63d` „hack to prevent ACDC audio thru“**: Ohne USB-Playback schreibt die Firmware Nullen an die Ausgänge. Das erklärt das Verhalten für acdc2.
- **v22.5.0 enthält den Hack nicht** (`git merge-base`: kein Vorfahre). Die öffentliche `ACDC.bin` zu v22.5.0 (109 080 Bytes, 2023-03-05) enthält Release-Textkonstanten („Storing bootloader“) und keine aus dem Hack-Branch („Readback failed“, „v22.4.s“) → sehr wahrscheinlich aus dem Release-Quelltext gebaut.

**Widerspruch, offen:** acdc1 meldet v22.5.0 und leitet trotzdem nicht durch. Kandidaten [Hypothese]:
1. Auf acdc1 läuft nicht die GitHub-Binärdatei, sondern ein anderer Build mit Etikett „v22.5.0“ (Werks- oder openwarelab-Build). Dazu würden auch Blockgröße 8 und der 186-ppm-Taktunterschied passen.
2. Eine Ausgangsstummschaltung in der Hardware oder per GPIO, die nur im USB-Betrieb freigegeben wird.
3. Gespeicherte Settings (z. B. `program_index` auf einen leeren Slot → Configure-Modus).
4. Der Slot-1-Patch auf acdc1 (9,93 KB) ist nicht identisch mit dem Library-„ACDC“.

**Folgen:**
- S3 ist mit der aktuellen Firmware **nicht messbar**. Die SOF-Frage ist mit S2-6 trotzdem beantwortet.
- **Standalone-FX geht mit der Firmware auf beiden Modulen derzeit nicht**, auch nicht mit eigenem Patch in Slot 1. Die frühere Aussage „läuft laut Code ohne Rechner“ gilt nur für den Quelltext, nicht für die Geräte.
- Nächster Schritt: Ursache der fehlenden Durchleitung auf acdc1 klären (Handoff 2026-11-14), erst danach Notch-Prototyp.

### D1 – acdc1 per SysEx ausgelesen und gesichert (2026-11-14)

Werkzeug: `tools/owl_read.py` (eigenes Skript, nur lesend: CC67-Abfragen, SysEx `0x18` „Slot zurücksenden“, optional RAM-Programmwechsel). Protokoll aus v22.5.0 abgeleitet. Läuft mit Python 3.12 (`--with mido --with python-rtmidi`) und nur **außerhalb des Claude-Sandbox**, weil der den CoreMIDI-Server sperrt. Rohdaten: `backup/acdc1/20261114/owl/` (`device_report.json`, `slot01_ACDC.{bin,syx}`, `slot02__Lich_.{bin,syx}`).

Achtung: Offene OWL-Webseiten (openwarelab/rebeltech) fragen das Gerät dauernd ab und brechen damit eigene Abfragen und Downloads ab. Vor dem Auslesen schließen.

**Befund [gemessen]:**
- Firmware „AC/DC v22.5.0“, Bootloader „N/A“, Storage 31 232 / 8 388 608 B.
- Laufende Settings: Blockgröße **8**, 48 kHz, Codec-Bypass 0, Swap 0, PC-Button 1. Die Ein- und Ausgangs-Gains schickt `sendSettings()` nicht mit.
- Patch-Meldung beim Start: `SR/BS/CH 48000 8 4`.
- Slot 1 „ACDC“: 10 164 B, CRC32 `0xbeb3bb2e`. Slot 2 „[Lich]“ = `_Lich_Nichts`, 20 724 B, CRC32 `0xeed65a68`, **im Flash gespeichert** (vom Nutzer über die Weboberfläche gestartet). Nach Aus/Ein läuft wieder Slot 1.
- Keine sichtbaren Ressourcen. `__SETTINGS__` ist eine System-Ressource (Flag `0x0100`), die Registry blendet sie aus und SysEx `0x18` kann sie nicht liefern [Code]. Dass Blockgröße 8 statt der v22.5.0-Vorgabe 16 läuft, spricht dafür, dass sie existiert [Hypothese].
- Prüfsummen: Das Gerät meldet Standard-CRC32 (zlib). Beide Downloads stimmen damit überein.
- **Slot 1 ≠ Library-„ACDC“:** Die Library-SysEx (`owl-patches/library/ACDC_library.syx`, Build 2022-07-27) hat 9 236 B und CRC `0x1a580324`. Der Slot-1-Patch ist größer und hat keinen String `ACDC.cfg`, ist also eine andere, vermutlich ältere Quellversion. Quelltext dazu fehlt.

**Beobachtung Nutzer, Kaltstart mit Slot 1 [gemessen]:** DPO in In 1. Die Eingangs-LEDs leuchten, die Ausgangs-LED bleibt dunkel, an Out 1 ist nichts zu hören.
- Deutung: Im Library-Quelltext zeigt LED 1–4 den Pegel des *Patch-Ausgangs* (`PARAMETER_AA`), LED 5–8 (`PARAMETER_BA`) setzt der Patch nie. Die dunkle Ausgangs-LED wäre dort also normal [Code]. Für die Slot-1-Version ist das nicht belegt, weil der Quelltext fehlt.

**Nächster Test (D2):** Kaltstart, USB nur für MIDI, keine Audio-App. Dann per Program Change (nur RAM) Slot 2 `_Lich_Nichts` (`process = _,_;`) starten, DPO in In 1, Out 1 abhören.
- Ton da → die Firmware leitet durch, Ursache ist der Slot-1-Patch.
- Stumm → Firmware oder Hardware nullt den Ausgang. Dann die Firmware lesend per ROM-DFU sichern und mit der Release-`ACDC.bin` vergleichen.

### D2 – Durchleitung mit `_Lich_Nichts`, ohne Store/Flash (2026-11-14)

Ablauf: acdc1 aus- und wieder eingeschaltet (Slot 1 startet), USB nur für MIDI. Das AC/DC ist in macOS nicht Standardgerät, Standard ist der UMC202HD (`system_profiler SPAudioDataType`). Keine Audio-App offen, OWL-Seiten geschlossen. Dann `tools/owl_read.py --program 2`, das Gerät meldet „[Lich]“ als laufend. DPO in In 1, Out 1 über MTM Startup → UMC abgehört.

**Ergebnis [gemessen, Nutzer]:**
- D2a, USB gesteckt, kein Audio-Stream: Out 1 **stumm**.
- D2b, danach das USB-Kabel gezogen, Case bleibt an, Slot 2 läuft weiter: Out 1 **stumm**.

**Deutung:**
- Ein reiner Durchleit-Patch (`process = _,_;`) kommt nicht an der Buchse an, mit und ohne USB. Der Slot-1-Patch ist also **nicht** die Ursache. Auch ein USB-Stream scheidet aus (Kandidat 3 und 4 aus dem Abschnitt „Durchleitung“ sind damit weg).
- Der Analogpfad DAC → Buchse funktioniert, denn bei Host-Playback ist Out 1 hörbar.
- Also wird der Ausgang nach dem Patch genullt, wenn USB-Playback fehlt. Das ist genau das Verhalten von `237c63d` [Hypothese, stark]. Im Repo steckt `237c63d` nur in `hack/acdc-output-levels` („v22.4.s“, 2022-07-15). Kein Stand mit dem Versionsstring „v22.5.0“ enthält ihn [Code].
- Am wahrscheinlichsten läuft auf acdc1 ein Build, der als „v22.5.0“ markiert ist, aber den Hack enthält, also nicht die GitHub-`ACDC.bin`. Dazu passen auch die Blockgröße 8 und der 186-ppm-Unterschied [Hypothese].
- Eine analoge Stummschaltung ist unwahrscheinlich: v22.5.0 hat keinen Mute-Pin, und bei Host-Playback geht der Ausgang ja.

**Nächster Schritt:** Das interne Flash von acdc1 lesend per ROM-DFU (`dfu-util -U`) sichern und mit der Release-`ACDC.bin` vergleichen. Das Ergebnis entscheidet, ob ein Flash der offiziellen `ACDC.bin` die Durchleitung bringt.

**Erinnerung Nutzer (unsicher, Gerät und Firmware unbekannt):** Auch früher getestete OWL-/Lich-Patches gaben am AC/DC keinen Ton aus. Hörbar wurden sie nur über einen Umweg: Patch laden, den Patch-Ausgang als „Eingang“ in der Host-Software empfangen und zurück auf den AC/DC-Ausgang schicken. Das passt zu TX nach dem Patch (gemessen: Gain 0 → USB-Strom stumm, Serie 2), RX überschreibt den DAC, und ohne RX wird der DAC genullt. Welches Modul und welche Firmware das damals war, ist offen. Mit acdc2 (v22.4.q, `237c63d`) wäre es nach Quelltext genau so zu erwarten.

**Erinnerung Nutzer zur Firmware von acdc1 (unsicher):** Die laufende „v22.5.0“ hat er vermutlich selbst aufgespielt, um das kaputte USB-Audio der offiziellen Version zu beheben. Quelle war ein Fork oder eigene Änderungen, das weiß er nicht mehr genau. Das passt zu D2 und zu Thread 2083 #4. Suche nach dem damaligen Build-Baum oder Binary auf dem Rechner (2026-11-14): nichts gefunden. Der alte Downloads-Ordner wurde nicht auf den neuen Rechner übernommen. Die SysEx-Dateien in `~/Downloads/` vom 2026-11-14 11:50 (`ACDC.syx`, `_Lich_.syx`) sind inhaltlich identisch mit den Backups von Slot 1 und 2.

### D3 – Firmware-Readback acdc1 per ROM-DFU (2026-11-14)

Ablauf: `tools/owl_read.py --reset-to-dfu --yes` → acdc1 erscheint als `0483:df11`, und zwar **über die vordere USB-B-Buchse**. Danach `tools/dfu_readback.sh`, zusätzlich dasselbe mit 2 MB. Nur `dfu-util -U`, nichts geschrieben. Dateien in `backup/acdc1/20261114/flash/`: `acdc1_internal_flash.bin` (128 KB, SHA-256 `433b3fd3…e5b1`), `acdc1_internal_flash_2MB.bin` (`4ddd5e53…5afd`), `compare_release.json`, `dfu-util_*.txt`, `sha256.txt`.

**Befund [gemessen]:**
- Kein Ausleseschutz, das Lesen geht.
- Der ROM-DFU meldet `@Internal Flash /0x08000000/16*128Kg`, also 2 MB. Alle 16 Sektoren lassen sich lesen. Nur Sektor 0 ist belegt, die Sektoren 1–15 enthalten nur 0xFF. Mehr als 128 KB passt eher zu einem H743 als zu einem H750 [Hypothese]. Ein H750 könnte aber auch ein H743-Die sein. Die MCU-Frage in CLAUDE.md bleibt offen.
- Die Firmware von acdc1 ist **nicht** die Release-`ACDC.bin` v22.5.0:
  - Nutzdaten 106 608 B statt 109 080 B, 101 835 Bytes unterschiedlich, Reset-Handler `0x08018ca9` statt `0x0801964d`.
  - Versions-String in beiden „AC/DC v22.5.0“.
  - String-Fingerabdruck: „**Readback failed**“ steht nur im Hack-Branch `hack/acdc-output-levels` (`Storage.cpp`). „**Storing bootloader**“ steht nur in v22.5.0 und fehlt auf acdc1. Die Strings „rx unf“ und „tx ovf“ sind auf acdc1 im Klartext. Im Hack-Branch gehen sie immer über `usbd_audio_error()`, in v22.5.0 nur mit `DEBUG_USBD_AUDIO`.
- Deutung: acdc1 läuft mit einem Build aus dem Hack-Branch (oder einem Mix), dessen Versions-String auf „v22.5.0“ gesetzt wurde. Das passt zur Erinnerung des Nutzers („selbst aufgespielt, um USB zu fixen“). Der Hack-Branch enthält `237c63d`, deshalb ist der Ausgang ohne USB-Playback stumm, und auch Blockgröße 8 und Input-Gain 88 kommen von dort. Damit sind D2 und Serie 2 erklärt [Hypothese, stark]. Für den Beweis müsste man `usbd_rx_convert()` disassemblieren.
- **Folge:** Auch acdc1 hat keine originale Release-Firmware. Das Abbild hier ist der einzige Rückweg zum jetzigen Zustand mit funktionierendem USB. Zurückschreiben ginge per `dfu-util -D` auf `0x08000000`, wurde aber nicht getestet und nur nach Rückfrage.
- Rückweg [gemessen]: Nur Case aus/an ließ acdc1 im DFU, weil USB das Board weiter versorgt hat. Mit Case aus, USB ab und Case an startet wieder die normale Firmware: „AC/DC v22.5.0“, Slot 1 „ACDC“, Blockgröße 8, Storage unverändert 31 232 B.

### D3a – Nachtrag: Fingerabdruck korrigiert, `237c63d` per Disassembly belegt (2026-11-14)

Ohne Gerätezugriff, nur Auswertung des D3-Abbilds und eigener Builds (`tools/build_acdc.sh`, Arm GNU 12.2.Rel1, Libraries `9e8f64e`, `docs/05` „Reproduktions-Build“).

**Korrektur zu D3 [Code]:** „Readback failed“ steht **nicht nur** im Hack-Branch. Es steht in allen Quellständen bis v22.5.rc7, auch auf `develop`. Erst v22.5.rc8/rc9 ersetzen es durch „Storing bootloader“. Über alle 214 Commits von 2022-04 bis 2023-06 in allen Branches:

| Muster (rx ovf, rx unf, tx ovf, tx unf, Readback failed, Storing bootloader) | Commits | Wo |
|---|---|---|
| `111110` | 81 | Hack-Branch, v22.4.0, v22.5.rc1 |
| `011010` | 106 | `develop` v22.5.rc2 … rc7 |
| `011001` | 27 | v22.5.rc8 … v22.5.0 |

Gezählt ist hier, was im Quelltext steht, nicht was kompiliert wird. In `develop` stehen „rx unf“ und „tx ovf“ unter `#ifdef DEBUG_USBD_AUDIO`, die Release-`ACDC.bin` enthält keinen der vier Strings.

**Kompilierte Strings [gemessen am Binary]:**

| String | Readback acdc1 | Release v22.5.0 | Build Hack-Spitze `7f3cc41` |
|---|---|---|---|
| rx unf / tx ovf (`ProgramManager.cpp`) | ja | nein | ja |
| rx ovf / tx unf (`usbd_audio.cpp`) | **nein** | nein | ja |
| Readback failed | ja | nein | ja |
| Storing bootloader | nein | ja | nein |

Keiner der gebauten Kandidaten hat genau dieses Muster: Hack v22.4.q `e81cfc3`, v22.4.r `db9d3dd`, v22.4.s `7f3cc41`, Hack-Merge `961b49f`, `develop` v22.5.rc5 `c79cf7a`. Die übrigen Textkonstanten unterscheiden die Stände nicht.

**Disassembly `usbd_rx_convert()` im Readback [gemessen]:**
- Die Funktion liegt bei `0x08015614`, gefunden über den Literal-Pool-Verweis auf „rx unf“ (`0x08019b94`).
- Am Anfang wird der globale RX-Zeiger geladen. Ist er `NULL` (`cbz`/`beq` → `0x0801569a`), folgt ein Tail-Call `memset(dst, 0, len*4)`. `0x08000608` ist `memset`, die Byte-Schleife mit `strb` ist geprüft.
- Das ist genau `237c63d` („hack to prevent ACDC audio thru“).
- Der Unterlauf-Pfad ruft `usbd_audio_error("rx unf", …)` auf (`0x0800a6fc`). Das ist die Fehlerbehandlung des Hack-Branchs ab `c2d25879`, nicht `develop`s `debugMessage()` unter `#ifdef`.

**Deutung:**
- **`237c63d` ist auf acdc1 belegt [gemessen: Disassembly].** Damit sind D2 und das stumme Kaltstart-Verhalten erklärt.
- Die Firmware von acdc1 entspricht **keinem veröffentlichten Commit**. Ihr `ProgramManager.cpp` stammt aus dem Hack-Branch (Thru-Mute, `usbd_audio_error`), in `usbd_audio.cpp` fehlen aber die „rx ovf“/„tx unf“-Meldungen, die jeder Hack-Commit ab `c2d25879` hat. Wahrscheinlich ist sie ein selbst zusammengesetzter oder lokal geänderter Stand, so wie der Nutzer sich erinnert [Hypothese, stark].
- Gebaut wurde sie mit einem älteren GCC als 12. GCC 12 bricht an den Hack-Quellen mit „conflicting declaration“ ab (`_PATCHRAM` u. a.), Upstream hat das erst Ende 2022 korrigiert [Hypothese, stark]. Deshalb ist ein bitgleicher Nachbau nicht möglich: Readback 106 608 B, eigene Builds 104 288–105 664 B.
- Den „nächstliegenden Commit“ gibt es also nicht. Die Plan-Entscheidung E1 für die Hack-Spitze (Q9) bleibt davon unberührt.

### D4 – Boot-Pad-Probe, Versuch 1 (2026-11-14)

Ablauf: Case aus, USB ab, BOOT-Pads auf dem Xibeca-Board gebrückt (Lage: Foto im Forum-Beitrag https://community.rebeltech.org/t/ac-dc-firmware-update/2083/4, Jumper „BOOT“ unter „PDR“), Case an, dann USB-B vorne an. Abgefragt nur mit `dfu-util -l` und `ioreg`, nichts geschrieben.

**Ergebnis [gemessen]:** **Kein DFU.** `dfu-util -l` findet nur den UMC202HD-Runtime-DFU (`1397:0507`), kein `0483:df11`. Das AC/DC meldet sich normal als „OWL-ACDC“ (`1209:dada`) mit USB-Seriennummer `396C34533131`. Das ist acdc1: Die STM32-Ableitung UID0+UID2 / UID1>>16 ergibt aus `0039001c:31315101:39333437` genau `396C3453` + `3131`. Die normale Firmware ist also gestartet, BOOT0 war beim Reset nicht high.

**Mögliche Ursachen [Hypothese]:** zu schwacher oder unterbrochener Kontakt (Oxid auf den Pads, Erinnerung des Nutzers; Forum 2083 #6/#22/#23 mit demselben Fehlbild), Brücke zu früh gelöst, oder das Board war über einen anderen Weg schon versorgt.

**Nächster Versuch:** siehe Chat 2026-11-14. Pads reinigen bzw. dünn verzinnen (nicht verbinden), Brücke fest halten, bis USB steckt.

**Versuch 2 [gemessen]:** Pads gereinigt, Brücke fest gehalten, bis USB vorne steckte. **DFU erreicht.** `dfu-util -l` meldet `0483:df11` „DFU in FS Mode“ mit `@Internal Flash /0x08000000/16*128Kg` und `@Option Bytes /0x5200201C/01*128 e`, Seriennummer `200364500000`, Pfad `1-1`. Das ist dieselbe Seriennummer wie beim SysEx-Einstieg in D3, also acdc1 über die vordere USB-B-Buchse.

**Fazit:** Der Notweg über die Boot-Pads funktioniert, braucht aber guten Kontakt (beim ersten Versuch kein DFU). Damit ist die Vorbedingung 1 aus E7 erfüllt (`docs/05`). Nichts geschrieben. Zurück in die normale Firmware: Case aus, USB ab, Case an (ohne Brücke), USB an.

### D5 – Generalprobe: Readback-Abbild zurückgeflasht (2026-11-14)

Vorbedingung 3 aus E7 (`docs/05`). Freigabe vom Nutzer im Chat („Generalprobe jetzt“). Erster Schreibvorgang auf acdc1. Das Gerät war über die Boot-Pads im ROM-DFU (D4, Versuch 2), USB-B vorne, Seriennummer `200364500000`.

Ablauf und Dateien (`firmware/flashlog/20261114_generalprobe/`):
1. `dfu-util -d 0483:df11 -S 200364500000 -a 0 -s 0x08000000 -D backup/acdc1/20261114/flash/acdc1_internal_flash.bin`: Erase Sektor 0, Download 131 072 B, „File downloaded successfully“, Exit 0. Ohne `:leave`. Die Warnung „Invalid DFU suffix signature“ kommt nur, weil die `.bin` keinen DFU-Suffix hat, und ist harmlos (`dfu-util_download.txt`).
2. `dfu-util … -s 0x08000000:131072 -U readback_after.bin`: SHA-256 `433b3fd3…e5b1`, **bitgleich** mit dem Abbild (`cmp` ohne Unterschied, `sha256.txt`).
3. Case aus, USB ab, Case an (ohne Brücke), USB an → normale Firmware.
4. `tools/owl_read.py` (`owl_read/acdc1/20261114/device_report.json`).

**Ergebnis [gemessen]:** „AC/DC v22.5.0“, `SR/BS/CH 48000 8 4`, Storage 31 232 / 8 388 608 B, Slot 1 „ACDC“ 10 164 B CRC `0xbeb3bb2e`, Slot 2 „[Lich]“ 20 724 B CRC `0xeed65a68`. Alles identisch mit D1. Nur CC 20–23 weichen um wenige Stufen ab, das sind die aktuellen Werte von Parameter A–D (Knob-Stellungen), keine Settings.

**Fazit:** Der Schreibweg (DFU-Download, Adresse `0x08000000`, Länge, Neustart) funktioniert, und der Rückweg zum Ist-Zustand ist erprobt. Vorbedingung 3 ist erfüllt. Offen vor Build 1 bleibt die Referenzaufnahme (Vorbedingung 2, inzwischen 10 min, siehe `docs/05` E7).

### D6 – Referenzaufnahme E7-ref: alte Firmware, 10 min mit Playback (2026-11-14)

**Setup:** acdc1 nach D5 (Readback-Abbild, meldet v22.5.0, enthält `237c63d`), am Thunderbolt-Hub. Host-Software, Engine 48 kHz. Aufnahme der 4 Eingänge, gleichzeitig Playback auf Out 1–4: Sinus 220 / 330 / 470 / 590 Hz (Out 1…4), Pegel nicht notiert. Ausgänge nicht auf die Eingänge geführt, Eingänge offen, Gain 12 Uhr. Datei `recordings/20261114_acdc1_ref-10min_g12_usb-rxtx.4chan.000.wav`, 48 kHz / 32 Bit float nativ, 600,9 s. Manifest-ID `E7-ref`, Auswertung `out/E7-ref/` (`--ref S2-4`).

**Ergebnis [gemessen]:**
- **Klicks: 0** auf allen 4 Kanälen in 10 min. Alle 119 Analysefenster gültig. f0 des 1-kHz-Kamms streut nur 0,1 ppm (999,8676 Hz), fs/8 liegt exakt auf 6000,0000 Hz.
- Störlinien wie in S2-4, aber die **LED-PWM-Familie (2320,54 Hz) ist mit −68…−75 dBFS jetzt die stärkste** (50–66 % der Störleistung). Gesamt 2–5 dB lauter als S2-4. Das passt zu H3: LEDs folgen dem Signalpegel, und hier lief Playback.
- **Übersprechen Ausgänge → Eingänge** (`tools/crosstalk_lines.py --freqs 220 330 470 590`, Mittel über 10 min, Pegel als Sinus-Amplitude in dBFS):

  | Linie | In 1 | In 2 | In 3 | In 4 |
  |---|---|---|---|---|
  | Out 1: 220 Hz | −86 | −93 | −95 | −96 |
  | Out 2: 330 Hz | −85 | −90 | −94 | −94 |
  | Out 3: 470 Hz | −93 | −102 | −104 | −106 |
  | Out 4: 590 Hz | −92 | −101 | −102 | −106 |
  | 330 − 220 = 110 Hz | −86 | −87 | −94 | −88 |
  | 220 + 330 = 550 Hz | −86 | −87 | −94 | −88 |
  | 590 − 470 = 120 Hz | −84 | −88 | −93 | −88 |
  | 470 + 590 = 1060 Hz | −84 | −88 | −93 | −88 |
  | Produkte über Kreuz (z. B. 470 − 220, 220 + 470) | −120…−134, am Boden | | | |

  - Die Grundtöne kommen auf allen Eingängen an, am stärksten auf In 1. Out 3/4 sprechen ≈ 8–10 dB schwächer über als Out 1/2. Playback-Pegel nicht notiert, das absolute Übersprechmaß bleibt offen.
  - **Mischprodukte 2. Ordnung (Summe und Differenz) gibt es nur innerhalb der Paare Out 1/2 und Out 3/4**, nicht über Kreuz. Sie sind gleich laut wie oder lauter als die Grundtöne selbst, bei Out 3/4 bis ≈ 9 dB lauter. Dazu kommen die 2. Harmonischen (440, 660, 940, 1180 Hz) mit −88…−98 dBFS. Die vom Tool gemeldete „110-Hz-Familie“ mit ≈ 150 Linien ist dieses Raster aus Mischprodukten, kein Sägezahn.
  - **[Hypothese]** Summe und Differenz gleich stark heißt: Etwas multipliziert die beiden Signale eines Paars. Kandidaten sind eine gemeinsame Stufe je Ausgangspaar, also der Stereo-Paar-Slot im Codec bzw. TDM, ein gemeinsamer Ausgangstreiber oder dessen Versorgung, oder die Pegel-LEDs. Prüfbar mit je einem Sinus nur auf Out 1 und nur auf Out 2, danach mit beiden.
- Musterperiode der Mischprodukte 1,26 s (wie S2-4: 1,24 s).

**Empfindlichkeit des Detektors** (`tools/click_sensitivity.py`, künstliche Fehler in einem 60-s-Ausschnitt dieser Aufnahme) **[gemessen]**:

| Fehler | offene Eingänge (wie E7-ref) | mit Sinus 440 Hz, −12 dBFS (Rückführung nachgebildet) |
|---|---|---|
| 48 Samples Null (Lücke) | erkannt (27–29 dB) | erkannt (36–41 dB) |
| 8 Samples Null | erkannt (31–34 dB) | erkannt (38–46 dB) |
| 48 Samples fehlen / doppelt (Frame-Slip) | **nicht erkannt** | erkannt (41–49 dB) |
| 1 Sample fehlt / doppelt | **nicht erkannt** | erkannt (10–15 dB) |

Fehlalarme ohne Eingriff: 0.

**Fazit:** Mit der alten Firmware gibt es in 10 min keine Lücken mit Stille. **Sample-Slips** sind bei offenen Eingängen (Pegel ≈ −65 dBFS) aber unsichtbar. Gerade die erwartet man bei Problemen mit dem Feedback-Endpoint oder dem Puffer. Für A6 reicht E7-ref deshalb nur zur Hälfte. Abhilfe: Kabel Out → In am selben Modul, Sinus aus der Host-Software, dann sind auch Slips in beiden Richtungen (RX und TX) sichtbar.

### D7 – Referenz mit Rückführung E7-ref-loop: alte Firmware, Slips (2026-11-14)

**Setup:** acdc1 wie D6 (alte Firmware nach D5), am Thunderbolt-Hub. Patchkabel Out 1→In 1 … Out 4→In 4. Host-Software, Engine 48 kHz, Sinus 440 / 530 / 670 / 790 Hz auf Out 1…4, in der Host-Software kein Eingang auf einen Ausgang. Gain 12 Uhr, Playback-Pegel nicht notiert. Datei `recordings/20261114_acdc1_ref-loop-10min_g12_usb-rxtx.4chan.000.wav`, 48 kHz / 32 Bit float, 600,4 s. Manifest-ID `E7-ref-loop`, Auswertung `out/E7-ref-loop/` (`--ref E7-ref`), Phasen-Ergebnis `out/E7-ref-loop/phase_slips.json`.

**Pegel – keine Übersteuerung (korrigiert):** In der Datei reichen die Spitzen bis −1,023 (In 1), bei In 2–4 bis −0,87…−0,92. Ein Clipping ist das nicht:
- Es gibt keine flachen Kuppen. Die Extremwerte kommen je Kanal nur 1–3-mal vor, die Werte um das Maximum verlaufen glatt wie ein Sinus.
- **Faktor 2 zwischen Gerät und Datei [gemessen]:** Alle Samples liegen exakt auf einem Raster von 1/16 384 statt 1/32 768, sowohl in E7-ref-loop als auch in E7-ref. Bei 16 Bit ist ein Wert über 1,0 nicht möglich. Also hat die Host-Software die USB-Daten mit genau 2 multipliziert (+6,02 dB), in der Float-Datei ohne Begrenzung. Am Gerät liegt die Spitze bei ≈ 0,51, also ≈ −6 dBFS.
- Die Prüfung im Analyse-Tool (|x| ≥ 0,999) hat deshalb fälschlich „Clipping“ gemeldet. Die Meldung trifft diese Datei nicht.
- Auffällig sind ungerade Harmonische auf allen 4 Kanälen, fast gleich: k = 3 bei −29 dBc, k = 5 bei −42 dBc, k = 7 bei −51 dBc, die geraden bei −59…−101 dBc. Sie stammen aus dem Host-Oszillator, nicht aus dem AC/DC (**[gemessen]**, D8). Für die Slip-Suche spielt das keine Rolle.
- Für A6 mit Build 1 denselben Patch mit denselben Pegeln nehmen.

**Ergebnis [gemessen]:**
- **Kanalzuordnung stimmt:** Jeder Eingang trägt genau den Ton seines Ausgangs (439,9998 / 530,0017 / 670,0003 / 789,9977 Hz).
- **Klick-Detektor: 0** auf allen Kanälen. Empfindlichkeit mit diesen Pegeln (`tools/click_sensitivity.py`): Frame-Slips (48 Samples) und Lücken werden erkannt (24–48 dB), 1-Sample-Slips nur knapp (9–18 dB, ein Fall nicht erkannt).
- **Phasenverfolgung: 0 Sprünge** auf allen Kanälen in 10 min (`tools/phase_slips.py --freqs 440 530 670 790`, Fenster 50 ms, Raster 10 ms, Schwelle 10·MAD). Das Phasenrauschen liegt bei 0,01 mrad. Ein einzelner Sample-Slip springt 58–103 mrad, also mehr als 5000× darüber. Probe: ±1 eingebauter Sample wird auf allen 4 Kanälen zur selben Zeit mit −0,99 bzw. +0,99 Samples gefunden.
- **Amplitude stabil:** Spanne 0,02–0,04 dB (0,1–99,9 %-Perzentil), keine Pegeleinbrüche.
- Störlinien (Datei-dBFS, inkl. Faktor 2): Die LED-PWM-Familie steigt mit dem lauten Signal weiter auf −63…−65 dBFS (D6: −67…−74). fs/8 −78 dBFS, 1-kHz-Kamm −74…−76 dBFS, beide wie in D6. Stützt H3 weiter.
- Nebenbefund: Neben jedem Ton steht eine einzelne Linie im Abstand von 75,72 Hz (515,72 / 605,72 / 745,72 / 714,28 Hz), −73…−77 dBFS, also ≈ 72 dB unter dem Ton. Ursache offen.

**Fazit:** Die alte Firmware läuft 10 min ohne einen einzigen Slip oder Aussetzer, in beiden Richtungen (Playback → DAC und ADC → Aufnahme). Damit ist die Referenz für A6 vollständig. Vorbedingung 2 aus E7 ist erfüllt. **Abnahme A6 für Build 1:** derselbe Aufbau, 0 Phasensprünge und 0 Klicks.

**Folge für alle Host-Aufnahmen [Hypothese, gestützt]:** Der Faktor 2 sitzt in der Host-Kette. Laut D8 entsteht er durch die Skalierung: Das Audio-Modul bildet ±1,0 auf ±10 V ab, der Mehrkanal-Recorder ±5 V auf ±1,0. In den 48-kHz-Dateien E7-ref und E7-ref-loop ist er belegt. Die Serie-2-Dateien (96 kHz, hochgerechnet) lassen sich so nicht prüfen. Ihre fs/8- und 1-kHz-Pegel stimmen aber auf ±1 dB mit E7-ref überein (S2-4 gegen E7-ref), dieselbe Kette ist also wahrscheinlich. **Absolute dBFS-Werte aus Host-Aufnahmen (S2, D6, D7) liegen damit ≈ 6 dB über dem Vollausschlag des Geräts.** Verhältnisse wie Störanteil, Notch-Gewinn, Vergleiche zwischen Host-Aufnahmen und Frequenzen sind davon nicht betroffen. M1–M3 kamen aus einer anderen Aufnahme-Software und sind nicht geprüft. Klärung: in der Host-Software Recorder- bzw. Audio-Modul-Gain ansehen, oder eine Aufnahme mit bekanntem Pegel machen.

### D8 – Oszillator direkt gegen Rückführung, gleichzeitig aufgenommen (2026-11-14)

**Setup:** Gleicher Host-Patch und gleiche Pegel wie D7. Zwei Recorder liefen gleichzeitig, je 34,8 s, 48 kHz / 32 Bit float:
- `D8-loop`: In 1–4 des AC/DC, Kabel Out n → In n. Datei `recordings/20261114_acdc1_loop-30s_g12_usb-rxtx.4chan.000.wav`.
- `D8-osc`: die vier Oszillatoren direkt in den Recorder, ohne AC/DC. Datei `recordings/20261114_vcv_osc-direct-30s_440-530-670-790.4chan.000.wav`.

Amplituden mit `tools/phase_slips.py` (Hann 50 ms, ohne Scalloping), Harmonische per Blackman-FFT über die ganze Datei.

**Ergebnis [gemessen]:**

| Kanal | Osc direkt (Datei) | Loop (Datei) | Loop/direkt | am Gerät (Datei/2) | k=2 direkt / Loop | k=3 | k=5 | k=7 |
|---|---|---|---|---|---|---|---|---|
| 1 (440 Hz) | +0,3 dB | −0,2 dB | −0,5 dB | −6,2 dBFS | −131 / −58 dBc | −28 / −28 | −42 / −41 | −50 / −51 |
| 2 (530 Hz) | +0,3 dB | −0,3 dB | −0,6 dB | −6,3 dBFS | −141 / −60 dBc | −29 / −28 | −42 / −41 | −51 / −51 |
| 3 (670 Hz) | +0,3 dB | −0,3 dB | −0,6 dB | −6,3 dBFS | −132 / −67 dBc | −29 / −28 | −43 / −43 | −51 / −51 |
| 4 (790 Hz) | +0,3 dB | −0,5 dB | −0,8 dB | −6,5 dBFS | −125 / −62 dBc | −29 / −29 | −42 / −42 | −51 / −51 |

- **Die ungeraden Harmonischen (k = 3, 5, 7) stecken schon im Oszillator**, auf ±1 dB gleich. Das AC/DC fügt sie nicht hinzu. Die Kurvenform hat eine gerundete Spitze bei exakt 1,0, keine flachen Kuppen. Grundton +0,3 dB über der Spitze, die Kuppen sind also leicht abgeflacht.
- **Eigene Verzerrung des AC/DC (DAC → Kabel → ADC):** vor allem die 2. Harmonische mit −58…−67 dBc, dazu k = 4/6 mit −87…−99 dBc. Direkt liegen diese bei −125…−157 dBc.
- **Pegel:** Am Gerät liegt der Grundton bei ≈ −6,3 dBFS (Datei-Wert / 2, Faktor 2 aus D7). DC-Offset am Eingang −2,4…−3,3 % FS.
- **Schleifenverstärkung** Out → In bei Gain 12 Uhr: −0,5…−0,8 dB, bezogen auf die Host-Spannungen. Die Scopes im Patch bestätigen das (siehe unten).
- **Faktor 2 geklärt:** Der Patch (Screenshot nur lokal, nicht im Repo) besteht aus 4× Software-Oszillator (SIN-Ausgang), Audio-Modul (Core Audio, „OWL-ACDC“, 48 kHz, Block 256), Merge → Mehrkanal-Recorder und 4 Pegelanzeigen.
  - Die Scopes zeigen an den Oszillatoren 10,00 V Spitze-Spitze (±5,00 V). In der Datei ist das 1,0. **Der Mehrkanal-Recorder bildet also ±5 V auf ±1,0 ab.**
  - Die Werte vom Gerät (Audio-Modul „From Device“) zeigen in den Scopes 9,45 / 9,42 / 9,33 / 9,14 V Spitze-Spitze, also −0,49 / −0,52 / −0,60 / −0,78 dB gegen den Oszillator. Der DC-Anteil liegt bei −0,32 / −0,33 / −0,24 / −0,29 V. Beides stimmt mit der Datei überein.
  - **Das Audio-Modul bildet ±1,0 vom Gerät auf ±10 V ab.** Die VCO-Spitze von 5 V ist am DAC also 0,5 = −6 dBFS. Die LOUD-Meter zeigen True Peak −5,9…−6,2 dB, auch das passt.
  - Faktor 2 = 10 V (Audio-Modul) / 5 V (Mehrkanal-Recorder). Das ist eine Skalierungsfrage, keine Verstärkung im Signalweg.
- **Slips:** 0 Phasensprünge, 0 Klicks in 34,8 s.
- Gegenüber E7-ref-loop sind Kanal 2–4 um 0,8–1,0 dB lauter (E7: −1,1 / −0,9 / −1,5 dB, D8: −0,3 / −0,3 / −0,5 dB). Kanal 1 ist gleich. Vermutlich stehen die Gain-Knobs nicht exakt gleich. Für die Slip-Suche ist das unerheblich.

**Woher die ungeraden Obertöne kommen [gemessen + Rechnung]:** Die Werte passen genau zu einem stückweise parabolischen Sinus, also zwei Parabelbögen je Periode statt sin(). Rechnerisch hat diese Form nur ungerade Harmonische mit 1/k³: k = 3 −28,6 dBc, k = 5 −41,9 dBc, k = 7 −50,7 dBc. Bei Spitze 1,0 liegt der Grundton bei +0,27 dB. Gemessen: −28…−29 / −42…−43 / −50…−51 dBc und +0,3 dB. Rack 2 erzeugt den SIN-Ausgang des VCO im Analog-Modus vermutlich so (Parabel-Näherung) **[Hypothese, Quelltext nicht geprüft]**. Im Digital-Modus (Kontextmenü) sollte ein echter Sinus kommen. Im Scope ist das nicht zu sehen, denn 4 % Klirr ändern die Kurve nur um wenige Prozent der Amplitude.
- Die Loop-Datei liegt exakt auf dem 16-Bit-Raster ×2. Nach dem Gerät hat also nichts nichtlinear eingegriffen, auch der Mehrkanal-Recorder nicht.

**Fazit:** Der Analogpfad des AC/DC ist sauber bis auf eine 2. Harmonische von ≈ −60 dBc bei −6 dBFS. Die starken ungeraden Obertöne kommen aus dem Software-Oszillator (Parabel-Sinus). Für Verzerrungsmessungen den VCO auf digital stellen oder einen anderen reinen Sinus nehmen. Für A6 bleibt der Patch unverändert.

### D9 – Build 1 `v22.4.s-thru1` auf acdc1 geflasht, Abnahme A1 (2026-11-14)

Freigabe vom Nutzer im Chat („kann losgehen“, nach der Frage nach dem Flash von Build 1). acdc2 nicht angefasst. Dateien in `firmware/flashlog/20261114_build1-thru1/`.

Ablauf:
1. `tools/owl_read.py` vorher (`owl_read_before/`): „AC/DC v22.5.0“, `SR/BS/CH 48000 8 4`, Storage 31 232 B, Slot 1 „ACDC“ CRC `0xbeb3bb2e`, Slot 2 „[Lich]“ CRC `0xeed65a68`. Das ist wie D1/D5.
2. `owl_read.py --reset-to-dfu --yes` (SysEx `0x7E`, ohne Pads) → `0483:df11`, Seriennummer `200364500000`, vordere USB-B-Buchse.
3. `dfu-util -d 0483:df11 -S 200364500000 -a 0 -s 0x08000000 -D firmware/builds/archive/acdc1-build1-thru1/ACDC.bin`: 105 656 B, „File downloaded successfully“, Exit 0 (`dfu-util_download.txt`).
4. Zurückgelesen wurden 131 072 B (`readback_after.bin`). Bytes 0…105 655 sind **bitgleich** mit dem Abbild (SHA-256 `97a876b4…c4f332`). Dahinter stehen nur 0xFF (`sha256.txt`).
5. Neustart durch den Nutzer: Case aus, USB ab, Case an, USB an.
6. `owl_read.py` nachher (`owl_read_after/`).

**A1 [gemessen]: bestanden.**
- USB meldet „OWL-ACDC“ mit Seriennummer `396C34533131`.
- „AC/DC v22.4.s-thru1“, `SR/BS/CH 48000 8 4`, Storage 31 232 / 8 388 608 B.
- Slot 1 „ACDC“ CRC `0xbeb3bb2e`, Slot 2 „[Lich]“ CRC `0xeed65a68`.
- Alle Konfigurationswerte sind gleich wie vorher. Abweichungen gibt es nur bei CC 22 (62 → 61, Knob-Stellung) und bei der CPU-Anzeige (9 % → 7 %).

Rückweg bei Bedarf: `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` wie in D5. Der SysEx-Einsprung in den DFU ist auch in Build 1 vorhanden (`Source/MidiHandler.cpp` → `device_dfu()`).

### D10 – Build 1 ohne Audio: Ursache Takt v22.4.s (2026-11-14)

**Beobachtung des Nutzers [gemessen, per Gehör und LEDs]:**
- **A2 (ohne USB):** Das Modul bootet mit LED-Lauflicht. Mit einem Oszillator an In 1 bleiben die Eingangs-LEDs dunkel, an Out 1 ist nichts zu hören.
- **Mit USB und Host-Loop-Patch:** Die Ausgangs-LEDs folgen dem Host-Signal, sie gehen an und wieder aus. An den Ausgangsbuchsen liegt trotzdem kein Signal an. Ein Eurorack-Oszillator an In 1 kommt in der Host-Software nicht an.
- Der Codec arbeitet also in keiner Richtung, egal ob mit oder ohne USB. Programm, USB und MIDI laufen (A1: CPU 7 %, `SR/BS/CH 48000 8 4`).

**Vergleich mit der alten Firmware (Readback D3) [gemessen: Disassembly]:**

| Stand | PLL3 P/Q | PLL3 FRACN | SAI-Masterteiler | Codec-Register 64 |
|---|---|---|---|---|
| v22.4.q `e81cfc3` (acdc2) | 2 | 0 | an | `0xC1` Single Rate |
| v22.4.r `db9d3dd` | 8 | 262 | an | `0xC1` Single Rate |
| **Readback acdc1 (alte Firmware, lief)** | **8** | **262** | (nicht geprüft) | **`0xC1` Single Rate** |
| v22.4.s `7f3cc41` = **Build 1 (kein Audio)** | 16 | 262 | **aus** | `0xC0` Auto Rate |

Belegt durch die Konstanten in `PeriphCommonClock_Config` (Readback `0x08001218`: `movs #172` / `#8` / `#8`, `mov.w #262`) und in `codec_init` (`movw #0xc140` gegen `#0xc040` in Build 1).

**Deutung:** Die alte Firmware von acdc1 hat die Takt- und Codec-Einstellung von **v22.4.r**. Die beiden letzten Commits des Hack-Branchs zerstören das Audio auf acdc1 **[gemessen]**: `f90e3f4` (Codec Auto Rate) und `e219182` (MCLK 256fs, SAI-Masterteiler aus). Welcher von beiden allein reicht, ist offen. **[Hypothese]** Ohne Masterteiler gibt der SAI keinen nutzbaren MCLK an den PCM3168A aus.

**Folge:** Der Rückfall nach E7 („Audio-Ausfälle“) ist erreicht. Vorschlag **Build 1b** = `db9d3dd` (v22.4.r) + Patch 01 + 02 (Revert `237c63d`), Version `v22.4.r-thru1`. Das ist dieselbe Takt- und Codec-Einstellung wie bei der alten, funktionierenden Firmware. Der Unterschied zu `7f3cc41` besteht nur aus den drei Commits `f90e3f4`, `e219182`, `7f3cc41` (Takt, Codec-Rate, Version und `DEBUG_AUDIO` in `usbd_audio.cpp`).

### D11 – Build 1b `v22.4.r-thru1` auf acdc1 geflasht, A1 (2026-11-14)

Freigabe vom Nutzer im Chat („Ja, bauen und flashen“). Build `firmware/builds/acdc1-build1b-thru1/` (`db9d3dd` + 01 + 02, 105 656 B, SHA-256 `406709e9…ee35`). Im Binary geprüft: „AC/DC v22.4.r-thru1“, PLL3 P = Q = 8 und FRACN 262 wie im Readback, Codec-Register 64 = `0xC1` (`movw #0xc140`). Die Stummschaltung ist entfernt: `usbd_rx_convert` enthält 1 `memset` statt 2 wie in `repro-db9d3dd`.

Ablauf wie D9, Dateien in `firmware/flashlog/20261114_build1b-thru1/`. DFU per SysEx aus Build 1, Seriennummer `200364500000`. Das Zurücklesen ist **bitgleich**, dahinter nur 0xFF. Danach Neustart durch den Nutzer.

**A1 [gemessen]:** „AC/DC v22.4.r-thru1“, `SR/BS/CH 48000 8 4`, Storage 31 232 B, Slot 1 „ACDC“ `0xbeb3bb2e`, Slot 2 „[Lich]“ `0xeed65a68`. Konfiguration unverändert, mit einer Ausnahme:
- **`bootloader_lock` (BL) meldet 1 statt 0.** Gesendet wird `bool(bootloader.getWriteProtectedSectors())`. Das ruft `eeprom_write_protection()` → `HAL_FLASHEx_OBGetConfig(&OptionBytes)` auf, mit einer Struktur auf dem Stack, die nicht initialisiert ist. Auf dem H7 hängt die WRP-Abfrage aber vom Feld `Banks` ab, das der Aufrufer setzen muss. **[Code/Hypothese]** Der Wert ist deshalb Zufall vom Stack und hängt vom Build ab. Ein echter Schreibschutz ist es nicht. Option-Bytes wurden nie geschrieben: nur `dfu-util -a 0` (Internal Flash), kein SysEx `BL`. Prüfbar, wenn nötig, über den DFU-Readback der Option-Bytes (alt 1, nur lesen). Kein Rückfall-Kriterium, denn Settings und Storage sind unverändert.
- CC 21–23 weichen um ±1 ab, das sind die Knob-Stellungen.

**A2 [gemessen, per Gehör]: bestanden.** Kaltstart ohne USB, Oszillator nacheinander an In 1–4: **Alle vier Kanäle** sind am jeweiligen Ausgang zu hören, Eingangs- und Ausgangs-LEDs leuchten. **Damit läuft das AC/DC zum ersten Mal standalone als Durchleitung.** Durchleit-Patch ist der Default-Patch „ACDC“ in Slot 1. Bei Build 1 (D10) war das wegen des Takts nicht möglich, bei der alten Firmware wegen `237c63d` (D2).

**A3 [gemessen, per Gehör]: bestanden.** USB vorne eingesteckt, keine Audio-App offen: Die Durchleitung bleibt hörbar, beim Einstecken knackt es nicht.

**A4 [gemessen, per Gehör]: bestanden.** Läuft das Host-Playback, liegt es an den Ausgängen an. Wird es gestoppt, kommt die Durchleitung zurück. Der Wechsel geht in beide Richtungen sauber.

**A5 [gemessen]: im Mittel bestanden, pro Kanal ±1,8 dB.** Aufnahme `A5-b1b` (`recordings/20261114_acdc1_b1b-open-inputs_g12_usb-stream.4chan.000.wav`, 120,5 s, 48 kHz nativ, Eingänge offen, Gain 12 Uhr, Hub, Host-Software ohne Playback). Auswertung `out/A5-b1b/` (`--ref S2-4`). Pegel als Datei-dBFS, beide Aufnahmen mit Host-Faktor 2.

| Größe | S2-4 (alte FW), Mittel | A5 (Build 1b), Mittel | Δ Mittel | Δ Kanal 1 / 2 / 3 / 4 |
|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,1 dB | −72,1 dB | ±0,0 | −1,7 / +0,9 / ±0,0 / +1,8 |
| A-bewertet | −73,2 dB | −73,2 dB | ±0,0 | −1,7 / +0,9 / −0,1 / +1,7 |
| Rest ohne Störlinien | −76,9 dB | −77,9 dB | −1,0 | −2,6 / +0,1 / −0,5 / +0,7 |
| fs/8-Linie 6000 Hz | −78,3 dB | −78,2 dB | +0,1 | −1,5 / +1,2 / −0,4 / +1,8 |
| 1-kHz-Kamm (Summe) | −76,1 dB | −75,4 dB | +0,6 | −1,0 / +1,4 / +0,3 / +2,3 |

- Gemittelt über die Kanäle (Leistung) ist das Rauschen **gleich** geblieben. Das breitbandige Rauschen ohne Störlinien ist 1 dB besser.
- Pro Kanal verschiebt sich etwas: Kanal 1 ist besser, Kanal 4 schlechter (bis +2,3 dB beim Kamm). Die fs/8-Linie ist jetzt auf allen Kanälen fast gleich (−78,1…−78,4 statt −76,6…−80,1).
- Das strenge Kriterium „±1 dB je Kanal“ ist auf Kanal 2 und 4 nicht erfüllt. **[Hypothese]** Das ist Streuung zwischen den Sitzungen (offene Eingänge koppeln Felder ein) und keine Verschlechterung durch die Firmware: Mittel unverändert, Abweichungen in beide Richtungen, das Breitbandrauschen ist nirgends mehr als 0,7 dB schlechter. Wie groß die Streuung ist, wurde noch nicht gemessen.
- f0 Kamm 999,8674 Hz (S2-4: 999,8663 Hz), fs/8 exakt 6000,0000 Hz, LED-Linie bei −114…−120 dBFS (praktisch weg), Klicks 0.
- **Entscheidung Nutzer (Chat, 2026-11-14):** A5 gilt als bestanden („Ja, weiter mit A6“). Die Streuung zwischen Sitzungen ist nicht gemessen, das Kriterium „±1 dB je Kanal“ wird künftig auf das Kanalmittel bezogen.

**Ausgangspegel −5,5 dB (Beobachtung Nutzer vor A6, Ursache [gemessen: Disassembly]):** Im Loop-Patch zeigt das Host-Scope „From Device“ mit Build 1b etwa 5 Vpp statt 9,45 Vpp wie in D8, das sind −5,5 dB.
- Der Eingangsweg ist unverändert, denn die Störlinien in A5 liegen im Mittel gleich hoch wie in S2-4.
- `usbd_rx_convert` (16 Bit → `lsl #8`) und `codec_set_gain_out` (Register 71 = Wert − 128) sind in alter Firmware und Build 1b gleich. Beide Codec-Funktionen lesen den Pegel aus `settings` Byte 13 (`audio_output_gain`).
- **Unterschiedlich sind die Vorgabewerte in `ApplicationSettings::reset()`:** In der alten Firmware steht `movw #0x7d58`, also Eingang 88 und **Ausgang 125** (−1 dB). In Build 1b steht `movw #0x7258`, also Eingang 88 und **Ausgang 114** (−6,5 dB). Differenz 11 Schritte à 0,5 dB = **5,5 dB**, das passt genau zur Messung.
- Ausgang 125 gibt es in keinem Commit des Repos (`git log -G`). Das bestätigt noch einmal, dass die alte Firmware ein selbst angepasster Stand war (D3a). Dass die Vorgabewerte überhaupt wirken, heißt: Die Gains kommen nicht aus gespeicherten Settings **[Hypothese]**.
- Vorschlag: Patch 04 `AUDIO_OUTPUT_GAIN 125` → Build 1c. Die Slip-Prüfung A6 hängt vom Pegel nicht ab und gilt auch für Build 1c.

### D12 – A6 mit Build 1b: Block-Slips im USB-Audio (2026-11-14)

**Setup:** wie D7 (`E7-ref-loop`): gleicher Host-Patch, Kabel Out n → In n, Sinus 440 / 530 / 670 / 790 Hz, Gain 12 Uhr, Hub, 10 min. Datei `recordings/20261114_acdc1_b1b-loop-10min_g12_usb-rxtx.4chan.000.wav`, Manifest `A6-b1b`, Auswertung `out/A6-b1b/` (`--ref E7-ref-loop`, `phase_slips.json`). Pegel am Eingang −5,8 dBFS Datei, ≈ −11,8 dBFS am Gerät (Ausgang −5,5 dB, D11).

**Ergebnis [gemessen]: A6 nicht bestanden.**
- **12 Phasensprünge und 12 Klicks pro Kanal.** Auf allen 4 Kanälen liegen sie zur selben Zeit und mit derselben Sample-Zahl, das spricht für den gemeinsamen USB- bzw. Audio-Pfad. Bei der alten Firmware (E7-ref-loop, D7) waren es 0.
- Die Ereignisse kommen in **6 Paaren**: zuerst ein Sprung um 2 oder 3 Samples, ≈ 0,33–0,38 s später weitere 6 bzw. 5 Samples, verteilt über ≈ 20–30 ms. **Jedes Paar ergibt zusammen genau 8 Samples Verzögerung, das ist ein Audioblock (`AUDIO_BLOCK_SIZE 8`).** Die Verzögerung wächst immer in dieselbe Richtung (Signal kommt später zurück).

  | Paar | 1. Sprung | 2. Sprung (≈ 0,35 s später) |
  |---|---|---|
  | 1 | 34,88 s: 2 | 35,21 s: 6 |
  | 2 | 226,06 s: 3 | 226,44 s: 5 |
  | 3 | 360,70 s: 2 | 361,04 s: 6 |
  | 4 | 458,82 s: 2 | 459,14 s: 6 |
  | 5 | 465,12 s: 2 | 465,44 s: 6 |
  | 6 | 501,57 s: 3 | 501,93 s: 5 |

  Feinauflösung am Paar 1 (Fenster 10 ms): vorher Versatz 0,00 ± 0,02 Samples, ab 34,885 s −2,00, ab 35,225 s −8,00. Amplitude unverändert, keine Nullfolgen.
- In 10 min summiert sich das auf 48 Samples, also ≈ 1,7 ppm Drift. Die läuft offenbar in einem Puffer auf, der dann um einen Block nachgestellt wird **[Hypothese]**. Ob das auf der RX- oder TX-Seite passiert, ist mit der Rückführung nicht zu trennen.
- Gleich wie bei der alten Firmware sind PLL3, SAI und Codec (D10) sowie `usbd_rx_convert` (D11). Unterschiedlich sind `usbd_audio.cpp`, denn die alte Firmware passt zu keinem Hack-Commit (D3a), sowie HAL-Stand und Compiler.

**Folge:** Das Rückfall-Kriterium „mehr Klicks als die Referenz“ (E7) ist erfüllt. Standalone-Durchleitung (A2–A4) geht dagegen nur mit Build 1b. Entscheidung offen, siehe Chat.

### D13 – Analyse der Block-Slips aus D12 (2026-11-14, ohne Flash)

**Debug-Meldung des Geräts [gemessen]:** Nach A6 liefert `owl_read.py` als PROGRAM_MESSAGE **`rx unf 0.9513 0.4722 4.0000`** (`firmware/flashlog/20261114_build1b-thru1/owl_read_after_A6/`). Das ist ein **Unterlauf des Empfangspuffers** (Rechner → Gerät) aus `usbd_rx_convert()`: Der RX-Puffer ist zu 95 % leer, der TX-Puffer halb voll. Vom Rechner kommen also auf Dauer zu wenig Samples. Die Slips liegen damit auf der RX-Seite.

**Mechanismus [Code + Hypothese]:**
- Das Feedback (`usbd_audio_sof_callback`, alle 32 ms) meldet dem Rechner, wie viele Samples der Codec verbraucht hat. Diese Zahl liefert `usbd_audio_get_rx_count()`:
  `samples = codec.getSampleCounter(); pos = usbd_audio_rx_count + samples; usbd_audio_rx_count = -samples;`
- `usbd_audio_rx_count += len` (ein Block = 8 Frames) läuft im SAI-DMA-Interrupt mit Priorität 5. `get_rx_count` läuft im USB-Interrupt mit Priorität 6 und kann also unterbrochen werden. Im Binary von Build 1b liegt zwischen `ldr r1, [r3]` (lesen) und `str r2, [r3]` (überschreiben) genau ein Befehl. Kommt der DMA-Interrupt dort dazwischen, **geht ein Block verloren**.
- Folge: Das Feedback meldet 8 Frames zu wenig, der Rechner schickt insgesamt 8 Frames weniger. Der RX-Puffer läuft später um genau diesen Block leer, und das Signal kommt 8 Samples später. Das passt zu den 6 Paaren mit je genau 8 Samples aus D12.
- Ein reiner Taktfehler würde den Puffer gleichmäßig leeren und in kleinen Schritten slippen, nicht in Blöcken.

**Offen:** Die alte Firmware hat dieselbe Funktion (Readback `0x080155b2`: `negs`/`ldr`/`str`, bitgleiches Muster) und dieselbe USB-Priorität 6 (`movs r1, #6` vor `HAL_NVIC_SetPriority(101)`). Trotzdem gab es dort in 10 min 0 Slips (D7). Mögliche Gründe: Ihr `usbd_audio.cpp` ist anders aufgebaut (RX/TX-Start in `SetInterface`, Paketpuffer 392 B) und beginnt vermutlich mit mehr Puffer-Reserve. v22.5.0 setzt den Schreibkopf auf `size/2`, v22.4.r auf `size/2 − len` (≈ 24 statt 72 Frames Reserve). Dann würden 6 verlorene Blöcke in 10 min noch nicht zum Unterlauf führen. **[Hypothese]** Die geschätzte Trefferrate für ein 1-Befehl-Fenster liegt eher bei 1 pro 20 min als bei 1 pro 100 s. Der Mechanismus ist deshalb nicht bewiesen.

**Vorschlag Build 1c** = `db9d3dd` + Patches 01, 02 und:
- `04-output-gain-125.patch`: `AUDIO_OUTPUT_GAIN 125` wie die alte Firmware. Laut Kommentar im Quelltext gibt 114 bei 10 Vpp Eingang nur ≈ 5 Vpp aus, die Durchleitung wäre also halbiert.
- `05-atomic-usbd-rx-count.patch`: `get_rx_count()` mit gesperrten Interrupts (`__disable_irq`, PRIMASK sichern und wiederherstellen).
- Beide Patches sind auf `db9d3dd` mit `--dry-run`/`patch` getestet. Gebaut ist noch nichts.

**Test:** A6 wie D12, 10 min. Bleibt die Rate wie bisher (6 in 10 min), ist die Wahrscheinlichkeit für 0 Ereignisse ≈ 0,25 %. 0 Slips würden den Mechanismus also stark stützen. Danach ein längerer Lauf (≥ 30 min), weil die alte Firmware nur 10 min geprüft ist.

### D14 – Flash Build 1c, A1 (2026-11-14)

**Build:** `firmware/builds/acdc1-build1c-thru1/` = `db9d3dd` + Libraries `9e8f64e` + Patches 01, 02, 04, 05, FW_VERSION `v22.4.r-thru1c`. 105 672 B, SHA-256 `78afacf045c11df8cd37e2d2310ddce873d6b7ad1127981cf829d5268a6e23b5`.

**Prüfung im Binary [Code]:** Gegenüber Build 1b unterscheiden sich nur drei Stellen:
- der Versionsstring,
- `ApplicationSettings::reset` mit `movw r1, #0x7d58` (in 88 / out 125, wie die alte Firmware) statt `#0x7258`,
- `usbd_audio_get_rx_count` (+12 B): `mrs r4, PRIMASK; cpsid i` … `msr PRIMASK, r4` um Lesen und Schreiben des Zählers.

Alle anderen Symbole sind gleich groß, also bleiben Takt, Codec-Setup und Revert `237c63d` wie in Build 1b.

**Flash:** Ablauf wie D11 (SysEx 0x7E → ROM-DFU, `dfu-util -D`, Readback 128 KB). Der Readback ist auf 105 672 B byte-gleich mit `ACDC.bin`, der Rest ist 0xFF. Logs: `firmware/flashlog/20261114_build1c-thru1/`.

**A1 [gemessen]:** `owl_read_after` meldet `AC/DC v22.4.r-thru1c`. Slots 1/2 (ACDC 10 164 B, [Lich] 20 724 B), Kalibrierung und Settings sind unverändert. `bootloader_lock = 1` wie direkt nach dem Flash von Build 1b, der Wert ist unzuverlässig (uninitialisierte Struktur).

**Panne:** Das erste `owl_read.py` vor dem Flash lief ohne `--out`. Dadurch wurde `backup/acdc1/20261114/owl/device_report.json` (12:07) überschrieben. Ersetzt durch die gleichwertige Kopie der Generalprobe (13:51, gleiche alte Firmware), mit Hinweisdatei daneben. Die Slot-Dateien sind unberührt.

**Noch offen:** Ausgangspegel am Scope (Soll ≈ 9,45 Vpp im Loop statt 5 Vpp), Durchleitung ohne USB, A6 (10 min, D12-Setup), Langlauf ≥ 30 min.

### D15 – A6 mit Build 1c (2026-11-14)

**Vorab, Nutzer am Gerät [gemessen]:** Ausgangspegel am Scope wieder wie mit der alten Firmware (Patch 04 wirkt). Durchleitung ohne USB geht weiter.

**Setup:** wie D12 (`A6-b1b`): gleicher Host-Patch, Kabel Out n → In n, Sinus 440 / 530 / 670 / 790 Hz, Gain 12 Uhr, Hub. Datei `recordings/20261114_acdc1_b1c-loop-10min_g12_usb-rxtx.4chan.000.wav` (604,5 s, 32-Bit-Float), Manifest `A6-b1c`. Auswertung in `out/A6-b1c/`: `--ref E7-ref-loop`, dazu `phase_slips.json/.txt`.

**Ergebnis [gemessen]: A6 bestanden.**
- **0 Phasensprünge und 0 Klicks auf allen 4 Kanälen** (D12: je 12). Ein 1-Sample-Slip läge 6 000–16 600× über dem Phasenrauschen, wäre also nicht zu übersehen. Bei gleicher Rate wie in D12 (6 Blöcke in 10 min) wäre die Wahrscheinlichkeit für 0 Ereignisse ≈ 0,25 %. Das stützt den Mechanismus aus D13 (Race in `usbd_audio_get_rx_count`) stark. Bewiesen ist er damit nicht, dafür fehlt der Langlauf.
- Pegel in der Datei −0,3…−0,5 dBFS, das sind ≈ −6,3 dBFS am Gerät (D12: −5,8 dBFS in der Datei). +5,5 dB, passt zu 125 statt 114. Spanne der Amplitude über 10 min 0,03–0,04 dB.
- Der Hinweis „Clipping“ der Analyse ist ein Fehlalarm. Die Float-Datei läuft über ±1,0 hinaus (In 1: −1,008 / +0,883, In 2: −1,009 / +0,878), ohne flache Kuppen. Am Gerät liegt die Spitze bei ≈ 0,5 FS (Host-Faktor 2). Die Asymmetrie heißt, dass In 1/2 einen leichten Gleichanteil führen.

**Debug-Meldung nach der Aufnahme:** `rx unf 1.0000 0.3055 32.0000` (`firmware/flashlog/20261114_build1c-thru1/owl_read_after_A6/`).
- Laut `usbd_audio_error()` ist das ein RX-Puffer **ganz leer**, dem **genau ein Block fehlt** (32 Samples = 8 Frames × 4 Kanäle).
- In D12 war es anders: `0.9513 … 4.0000`, ein Teil-Unterlauf mitten im Lauf.
- Ein Unterlauf während der Aufnahme hätte Nullen und einen Slip erzeugt, und davon gibt es keine. Die Meldung stammt also von außerhalb der 604,5 s, vermutlich vom Ende des Streams: Host-Software hört auf zu senden, das Interface bleibt offen, der Puffer läuft leer **[Hypothese]**. Das Gerät behält nur die letzte Meldung.

**Folge:**
- Für die Standalone-Durchleitung mit USB-Betrieb ist Build 1c der Kandidat.
- Noch offen ist der Langlauf ≥ 30 min. Dabei die Geräte-Meldung **vor** dem Stoppen der Host-Software lesen, damit ein Unterlauf mitten im Lauf vom Stream-Ende zu trennen ist.

### D16 – Langlauf 30 min mit Build 1c (2026-11-14)

**Setup:** wie D15, 1 800 s. Datei `recordings/20261114_acdc1_b1c-loop-30min_g12_usb-rxtx.4chan.000.wav`, Manifest `A6L-b1c`, Auswertung `out/A6L-b1c/phase_slips.json/.txt`. Die Standard-Analyse (Klicks) wurde wegen der Dateigröße noch nicht gerechnet.

**Ergebnis [gemessen]: Langlauf nicht bestanden.**
- **25 Phasensprünge, auf allen 4 Kanälen zur selben Zeit und gleich groß.** Erstes Ereignis bei 54,6 s, letztes bei 1 793 s. Muster wie D12: Paare aus 2–3 und dann ≈ 0,33 s später 5–6 Samples. Summe −99,1 Samples ≈ 12,4 Blöcke à 8, immer in Richtung Verzögerung. Abstände 14–320 s, im Mittel ≈ 145 s.
- Netto-Drift ≈ 99 Frames / 1 800 s = 0,055 Frames/s ≈ **1,15 ppm**. D12: 48 / 600 s = 0,080 Frames/s ≈ 1,7 ppm.
- **Patch 05 (atomarer Zähler) behebt das nicht.** Die Race-Hypothese aus D13 ist damit als Hauptursache **widerlegt**. Die 0 Ereignisse in D15 erklären sich vermutlich durch Puffer-Reserve am Stream-Anfang (siehe unten), nicht durch den Patch.

**Debug-Meldung bei laufendem Stream (direkt nach Aufnahme-Stopp, Host-Software noch an):** `rx unf 0.9513 0.4722 4.0000`, auf vier Stellen gleich wie D12.
- Das ist kein Zufall, sondern der feste Zustand beim Unterlauf: Der RX-Puffer fasst 576 Samples (144 Frames). Ist noch 28 von 32 benötigten Samples da (`len − cap = 4`), ergibt das 548/576 = 0,9514 frei. Die Meldung zeigt also einen **Unterlauf mitten im Lauf**.
- Die Meldung `1.0000 … 32` aus D15 ist dagegen ein ganz leerer Puffer, typisch für Stream-Ende oder Neustart der Host-Software **[Hypothese]**.

**Neue Deutung [Code + Hypothese]:**
- Das Feedback (`usbd_audio_sof_callback`) meldet alle 32 ms die gezählten Samples im Format 10.14, **ohne Rückkopplung über den Pufferstand** (offene Regelschleife). Die Zählung selbst summiert sich exakt auf, ein Fehler im Gerät müsste also systematisch sein.
- Die gemessene Drift von 1,15–1,7 ppm liegt bei **≈ 1 LSB des Feedback-Werts**: 1/16 384 Frame pro 1-ms-Frame = 0,061 Frames/s = 1,27 ppm. Ein Rundungsfehler von etwa einem LSB irgendwo zwischen Gerät und Host (z. B. Host rundet ab) würde den Puffer genau so leerlaufen lassen.
- Mit 24 Frames Start-Reserve (v22.4.r, D13) reicht das für einige Minuten, danach slippt es im Abstand von ≈ 8 / 0,06 ≈ 130 s. Das passt zum mittleren Abstand 145 s.
- Die alte Firmware startet mit ≈ 72 Frames Reserve, das reicht für ≈ 20 min. **Ihre 0 Slips in 10 min (D7) beweisen deshalb nicht, dass sie das Problem nicht hat.**

**Folge:** Ein echter Fix braucht eine **geschlossene Regelschleife**: Das Feedback wird um den Pufferstand korrigiert (Abweichung vom halben Puffer → einige LSB nach oben oder unten). Mehr Start-Reserve allein würde den ersten Slip nur hinausschieben.

### D17 – Flash Build 1d, A1 (2026-11-14)

**Build:** `firmware/builds/acdc1-build1d-thru1/` = Build 1c + `06-fb-level-control.patch` (Pufferstand-Regelung im Feedback, Entwurf `docs/05` „Build 1d“), FW_VERSION `v22.4.r-thru1d`. 105 972 B, SHA-256 `f522560eb3d3c329c37753a1ebfdb326e45bae02192f81e866693b363f044c28`. Kompiliert ohne Warnungen in `usbd_audio.cpp`.

**Prüfung im Binary [Code]:** Gegenüber Build 1c sind nur `usbd_audio_sof_callback` (0x84 → 0x128 B), `USBD_AUDIO_DataOut` (+124 B) und vier neue BSS-Variablen (`fb_*`) dazugekommen.
- `sof_callback`: Sollwert `#384`, EMA mit `asr #3`, Grenzen ±32 (`mvn #31` / `movs #32`) mit `debugMessage("fb clamp")`. Vergleich auf ±0x4000 gegen `val − corr`, Ausgabe `samples + corr` bzw. `2·samples + corr`.
- `DataOut`: Messung zwischen `mrs PRIMASK; cpsid i` und `msr PRIMASK`, Startwert `rsb …, #384` (Schreibkopf = 384 − len).

**Flash:** wie D14. Der Readback ist auf 105 972 B byte-gleich, der Rest 0xFF. Logs in `firmware/flashlog/20261114_build1d-thru1/`. Vor dem Flash meldete Build 1c `rx unf 1.0000 0.2500 32.0000`, also einen ganz leeren Puffer nach dem Schließen der Host-Software. Das stützt die Deutung der `1.0000 … 32`-Meldung aus D15/D16 als Stream-Ende.

**A1 [gemessen]:** `AC/DC v22.4.r-thru1d`, `SR/BS/CH 48000 8 4`. Slots, Kalibrierung und Settings sind unverändert.

**Noch offen:** A2 kurz (Durchleitung ohne USB), Langlauf 30 min im Loop wie D16, Geräte-Meldung bei laufendem Stream, danach A5.

### D18 – Langlauf 30 min mit Build 1d (2026-11-14)

**Setup:** wie D16, 1 804,6 s, ≈ 22:36:37–23:06:42. Datei `recordings/20261114_acdc1_b1d-loop-30min_g12_usb-rxtx.4chan.000.wav`, Manifest `A6L-b1d`, Auswertung `out/A6L-b1d/phase_slips.json/.txt`. Vorher kurz A2 (Durchleitung ohne USB): geht, laut Nutzer.

**Ergebnis [gemessen]:**
- **Keine Block-Slips mehr.** Build 1c hatte unter denselben Bedingungen 25 Sprünge ≈ 12 Blöcke (D16), Build 1d hat **keinen einzigen** Sprung vom Typ „2–3 + 5–6 Samples“. Die Pufferstand-Regelung (Patch 06) behebt die Drift aus D12/D16.
- **Ein einzelnes, anderes Ereignis bei 460,81 s (≈ 22:44:18):**
  - Auf allen 4 Kanälen ist das Signal von 460,8054 bis 460,8250 s gestört (≈ 19,6 ms). Die Störung zerfällt in Stücke von ≈ 45–48 Samples, also USB-Paketgröße (1 ms), mit Sprüngen zwischen den Stücken.
  - Danach läuft das Signal **phasenrichtig** weiter. Über einen 2-s-Fit vor und nach dem Ereignis ist der Netto-Versatz ≈ 0 Samples (beste Lösung 0,06). Es geht also netto kein Block verloren, und die Amplitude ist unverändert.
  - `phase_slips.py` meldet deshalb unplausible, je Kanal verschiedene „Sprünge“ (−15,3 / −5,4 / −0,6 / −2,9 Samples). Das ist ein Messartefakt der Störung.
- **Geräte-Meldung bei laufendem Stream:** `fb 48.0004 96.2578` aus `usbd_audio_sof_callback`. Eine Feedback-Periode hat **doppelt so viele** Samples gezählt (96,26 statt ≈ 48 Frames/ms), der Wert wurde von der Plausibilitätsprüfung verworfen.
  - Das passiert, wenn das Gerät für ≈ 32 ms keine SOFs verarbeitet hat. Danach kam keine weitere Fehlermeldung. Einen `rx unf` während der Störung würde diese spätere Meldung überschreiben, er ist also nicht ausgeschlossen.
  - Es gab keine `fb clamp`-Meldung, die Korrektur blieb also innerhalb ±32 LSB.

**Deutung [Hypothese]:** Eine kurze Unterbrechung auf dem USB-Bus (≈ 20–30 ms ohne SOF bzw. Pakete), etwa am Thunderbolt-Hub oder beim Host. Die Drift-Ursache aus D16 ist es nicht, und der Regler kann SOFs nicht beeinflussen. Das macOS-Log (`log show`) lieferte für 22:44:10–22:44:26 keine Einträge (vermutlich keine Berechtigung). Ob das Ereignis wiederkehrt und ob es auch mit der alten Firmware auftritt, ist offen. Bei der alten Firmware sind nur 10 min geprüft (D7).

**Bewertung:** Das Drift-Problem ist gelöst. Das Abnahmekriterium „0 Ereignisse, keine Meldung“ ist wegen des Einzelereignisses formal **nicht** erfüllt.

**Entscheidung (Nutzer, 2026-11-14):** Build 1d bleibt auf acdc1, ein zweiter Langlauf entfällt. Das Einzelereignis aus D18 bleibt offen und wird beobachtet.

### D19 – A5 mit Build 1d: offene Eingänge (2026-11-15)

**Setup:** wie A5-b1b (D11). acdc1 mit Build 1d `v22.4.r-thru1d`, Eingänge offen (nichts gesteckt), Gain 12 Uhr, Thunderbolt-Hub, Host-Software 48 kHz, Audio-Modul ohne Playback, Mehrkanal-Recorder. Aufnahme am Morgen ≈ 10:17–10:19. Datei `recordings/20261115_acdc1_b1d-open-inputs_g12_usb-stream.4chan.000.wav` (121,0 s, 48 kHz nativ, 32 Bit float). Manifest `A5-b1d`, Auswertung `out/A5-b1d/` (`--ref A5-b1b`). Pegel als Datei-dBFS, alle drei Aufnahmen mit Host-Faktor 2.

**Ergebnis [gemessen]: A5 bestanden.** Gemessen am Kanalmittel (Kriterium aus D11) ist das Rauschen gegenüber Build 1b nicht schlechter, sondern ≈ 1 dB besser.

| Größe | S2-4 (alte FW) | A5-b1b (Build 1b) | A5-b1d (Build 1d) | Δ 1d − 1b, Mittel | Δ Kanal 1 / 2 / 3 / 4 |
|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,1 dB | −72,1 dB | −73,2 dB | −1,1 | −1,1 / −0,8 / −1,2 / −1,3 |
| A-bewertet | −73,2 dB | −73,2 dB | −74,6 dB | −1,3 | −1,4 / −1,0 / −1,6 / −1,5 |
| Rest ohne Störlinien | −76,9 dB | −77,9 dB | −77,6 dB | +0,2 | +0,2 / +0,3 / +0,4 / +0,2 |
| fs/8-Linie 6000 Hz | −78,3 dB | −78,2 dB | −80,0 dB | −1,7 | −1,7 / −1,7 / −1,6 / −2,0 |
| 1-kHz-Kamm (Summe) | −76,1 dB | −75,4 dB | −77,4 dB | −2,0 | −2,3 / −1,5 / −2,4 / −2,1 |
| Mischprodukte (Summe) | −91,5 dB | −91,1 dB | −86,5 dB | **+4,7** | +4,7 / +4,7 / +4,8 / +4,4 |
| Störanteil (Mittel) | 69 % | 74 % | 65 % | | 57 / 66 / 74 / 64 % |
| Gewinn ideale Notch-Bank | 5,2 dB | 6,0 dB | 4,6 dB | | 3,7 / 4,6 / 5,9 / 4,4 |

- **Breitbandrauschen unverändert:** Der Rest ohne Störlinien liegt auf allen Kanälen innerhalb von +0,4 dB von Build 1b.
- **Kamm und fs/8-Linie sind 1,5–2,4 dB leiser,** auf allen Kanälen gleichmäßig. Ob das an der Firmware liegt oder an der Sitzung, ist offen **[Hypothese: Sitzung]**. Die Streuung zwischen Sitzungen ist noch nicht gemessen (D11). Dass die Verschiebung auf allen Kanälen gleich ist, spricht für eine gemeinsame Ursache (Host/Hub, Gerät kalt).
- **Neu: Mischprodukte n·f1k + m·6000 Hz ≈ 5 dB lauter,** auf allen Kanälen gleich. Einzelne Linien mit m = ±1, 2 steigen um 7–11 dB, z. B. Kanal 1:
  - 8·f1 + f2 = 13 998,94 Hz: −103,6 → −96,6 dB
  - 4·f1 + 2·f2 = 15 999,47 Hz: −106,2 → −96,9 dB
  - 4·f1 + f2 = 9 999,47 Hz: −108,5 → −97,6 dB

  S2-4 und A5-b1b liegen dagegen gleich auf (−104,3 / −105,6 / −108,9 dB). Absolut bleibt es klein, der Anteil am Rauschen ist 4–7 %. Musterperiode 1,26 s wie bisher.
  - **[Hypothese]** Zwischen 1b und 1d hat sich die CPU-Last pro USB-Paket geändert: Patch 05 (atomarer RX-Zähler, kurz Interrupts aus), Patch 06 (Pufferstand-Messung in `DataOut` unter `cpsid i` und längerer `sof_callback`). Das könnte die Kopplung zwischen USB-Takt (1 kHz) und Blocktakt (6 kHz) verstärken. Build 1c ist nicht mit offenen Eingängen gemessen, deshalb lassen sich 05 und 06 nicht trennen. Sitzungsstreuung ist auch möglich, wurde bei den Mischprodukten aber bisher nicht beobachtet (S2-4 ≈ A5-b1b).
- f0 Kamm 999,8680 Hz (1b: 999,8674, S2-4: 999,8663), fs/8 exakt 6000,0000 Hz. LED-Linie ≤ −124 dB (weg), Klicks 0, Kanal-Korrelation 0,98–0,99.
- **Langsame DC-Drift:** Der DC-Wert wandert in 120 s auf allen Kanälen gleichsinnig um ≈ 0,3 % FS (Kanal 1: −4,90 → −5,20 %). In A5-b1b war er auf 0,01 % stabil. Die Kennzahl „Drift < 20 Hz“ steigt deshalb von −82 auf −60 dB, das Band unter 20 Hz ohne DC-Verlauf nur um ≈ 2,5 dB. **[Hypothese]** Das Gerät war kurz vorher kalt gestartet (Aufwärmdrift) oder die Kabel waren gerade erst gezogen. Unhörbar, für A5 nicht relevant.

**Bewertung:** Durch die USB-Änderungen (Patches 04–06) ist das Eingangsrauschen nicht schlechter geworden. A5 für Build 1d ist bestanden. Offen bleibt, ob die Mischprodukte wirklich zugenommen haben. Klären lässt sich das mit einer Wiederholung (A5 zweimal in derselben Sitzung = Sitzungsstreuung) oder später im A/B-Vergleich bei Build 2.

### D20 – A7 = S3 mit Build 1d: Kamm an den Ausgängen je USB-Zustand (2026-11-15)

**Setup** (Aufbau aus `docs/03` S3, für Build 1d angepasst):
- acdc1 mit Build 1d direkt an einem USB-Port des Macs, UMC202HD am Thunderbolt-Hub. Eingänge offen, Gain 12 Uhr, Slot 1 „ACDC“ (Durchleitung ×1).
- **Nur ein Kanal**, weil das MTM Startup nicht hart nach links/rechts pannt: acdc1 Out 1 → Startup (Line, fest) → UMC In 1 (LINE, Gain fest). Out 2–4 frei.
- Das zweite Y-Bein steckte in UMC In 2, war in der Host-Software aber nicht verbunden. Kanal 2 der UMC-Dateien ist deshalb digital 0 und wird per `channels = [1]` ausgelassen. Dafür kann das Analyse-Tool jetzt Kanäle auswählen (`analysis/audio_io.py`).
- Aufnahme UMC in Host-Software (Mehrkanal-Recorder, Datei-Werte mit Host-Faktor 2), 120 s je Zustand. Reihenfolge: S3-0 → b → c → d → a → b2.

| ID | Zustand | Datei |
|---|---|---|
| S3-0 | Kette Startup → UMC allein (Kabel Out 1 → Startup gezogen), acdc1-USB gesteckt | `20261115_umc_s3-0-chain-only_g12_usb-plugged.2chan.000.wav` |
| S3-b | USB gesteckt, kein Stream | `20261115_acdc1_s3b-out-via-umc_g12_usb-plugged.2chan.000.wav` |
| S3-c | Eingangs-Stream: Aufnahmeprogramm nimmt vom AC/DC auf (Wiedergabe auf anderem Gerät) | `…_s3c-out-via-umc_g12_usb-stream.2chan.000.wav`, Gegenseite `…_s3c-in-audacity_g12_usb-stream.wav` (`S3-c-in`) |
| S3-d | Duplex: Host-Software öffnet das AC/DC, Nullen an die Ausgänge | `…_s3d-out-via-umc_g12_usb-duplex.2chan.000.wav`, Gegenseite `…_s3d-in-vcv_g12_usb-duplex.4chan.000.wav` (`S3-d-in`) |
| S3-a | USB des AC/DC gezogen, Case an | `…_s3a-out-via-umc_g12_usb-off.2chan.000.wav` |
| S3-b2 | wie b, am Serienende | `…_s3b2-out-via-umc_g12_usb-plugged.2chan.000.wav` |

Auswertung: `out/S3-*/` (`--ref S3-b`). Die Zuordnung der Linien wurde mit einer eigenen Peak-Suche um 1/2/3/6 kHz, 50 und 60 Hz gemacht (Hann über die volle Länge, Bin 8,3 mHz).

**Zwei Zeitbasen.** Die UMC-Dateien laufen im Takt des UMC, die AC/DC-Dateien im Takt von acdc1. Die fs/8-Linie von acdc1 (6000,0000 Hz im eigenen Takt) erscheint im UMC bei 6001,111 Hz. Das ergibt das Verhältnis **UMC/acdc1 = 1,000185 (185 ppm)**. Die 59,98-Hz-Linie bestätigt das (59,9831 / 59,9720), ebenso der Fremdkamm (1000,2198 / 1000,0346). Frequenzen unten mit „UMC“ bzw. „AC/DC“ markiert.

**Linien und Pegel am Ausgang Out 1 [gemessen]** (UMC-Datei-dBFS, Sinus-Amplitude der Grundlinie k = 1, „–“ = keine Linie > 15 dB über Boden):

| Komponente | f (UMC) | f (AC/DC) | S3-0 | S3-b | S3-c | S3-d | S3-a | S3-b2 |
|---|---|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | | | −86,7 | −56,5 | −54,6 | −56,4 | **−75,9** | −57,2 |
| AC/DC-SOF-Kamm (Mac-Port) | 1000,175 | 999,9895 | – | −93,4 | −89,7 | −94,7 | **– (< −124)** | −92,5 |
| Fremdkamm | 1000,220 | 1000,0346 | −121,5 | −73,9 | −70,5 | −71,6 | −120,7 | −75,6 |
| 59,98-Hz-Familie | 59,983 | 59,972 | −108,8 | −68,5 | −66,5 | −71,6 | −108,9 | −69,9 |
| fs/8 von acdc1 | 6001,111 | 6000,000 | −114,1 | −80,9 | **−112,7** | −98,5 | −80,5 | −80,7 |
| fs/48-Kamm (k = 1/2/3) | 1000,185 | 1000,000 | – | (verdeckt) | (verdeckt) | (verdeckt) | −111,5 / −105,3 / −107,2 | (verdeckt) |
| „Klicks“ (Abstand Median 17 ms) | | | 0 | 6 581 | 7 | 6 512 | 0 | 5 772 |

**Ergebnisse:**
1. **H1 am Ausgang bestätigt:** Der SOF-gekoppelte 1-kHz-Kamm von acdc1 (999,9895 Hz AC/DC = USB-Port des Macs, wie S2-6) **verschwindet ohne USB** (S3-a, mindestens 31 dB unter S3-b). Er ist schon in S3-b da, also ohne jeden Stream: **der SOF allein reicht**. Stream (c) und Duplex (d) ändern seinen Pegel um höchstens 4 dB.
2. **In S3-d ist er gleich stark wie in S3-b**, obwohl der DAC nur Nullen bekommt. Er gelangt also nicht (nur) über ADC → Durchleitung an den Ausgang, sondern über den Analog- bzw. Massepfad (siehe 3).
3. **Masseschleife beherrscht den Ausgang, sobald USB steckt [gemessen, Deutung Hypothese]:** Mit gestecktem USB ist Out 1 rund **20 dB lauter** als ohne (−55…−57 gegen −76 dB), unabhängig vom Stream-Zustand. Es dominieren:
   - eine Impulsfolge bei **59,97 Hz** (Familie mit vielen Harmonischen, der Klick-Detektor schlägt alle 17 ms an)
   - ein **zweiter 1-kHz-Kamm bei 1000,0346 Hz (AC/DC)**. Er ist nicht der SOF von acdc1 und auch nicht der Hub-SOF von gestern (999,868), Quelle unbekannt.

   Beide sind in S3-0 (kein Audiokabel AC/DC → UMC) und S3-a (kein USB) um ≈ 40–50 dB schwächer. Sie brauchen also **beide Verbindungen gleichzeitig**: USB acdc1 ↔ Mac und Audiokabel acdc1 → Startup → UMC ↔ Hub ↔ Mac. Das ist eine Masseschleife. Woher 59,97 Hz und der Fremdkamm kommen (Mac, Hub, UMC), ist offen. 60 Hz ist kein Netz in DE, es kommt also eher aus dem Rechner (Display, Netzteil).
4. **Ohne USB (Standalone) ist der Ausgang sauber:** RMS −75,9 dB. Übrig bleiben:
   - die fs/8-Linie (−80,5), die über die Durchleitung vom Eingang kommt
   - ein schwacher Kamm **genau bei fs/48 = 1000,000 Hz im Takt von acdc1** (−105…−111 dB). **[Hypothese]** Das ist firmware-interne 1-ms-Aktivität (SysTick o. ä., CPU-Takt aus demselben Quarz) und nicht USB.
   - Netz 50 Hz (−91,5)
5. **Mit Eingangs-Stream (S3-c) war die Durchleitung aus [gemessen + Code]:** Die fs/8-Linie am Ausgang fällt in c auf −112,7 dB, noch unter d (−98,5). In b, a und b2 liegt sie bei −80,5…−80,9. Laut Code (`USBD_AUDIO_DataOut`) startet RX erst mit dem ersten **ankommenden Playback-Paket**. macOS hat also auch den Ausgangs-Stream des AC/DC gestartet, obwohl das Aufnahmeprogramm nur aufnahm und auf ein anderes Gerät wiedergab **[Hypothese: CoreAudio startet beim USB-Gerät beide Richtungen]**. Folge: **Sobald irgendeine App vom AC/DC aufnimmt, ersetzt der Host-Playback (meist Stille) die Durchleitung.** Ein reiner Zustand „nur Eingang streamt“ lässt sich so nicht herstellen, S3-c entspricht praktisch S3-d.
6. **b und b2 stimmen überein:** RMS −56,5 / −57,2, SOF-Kamm −93,4 / −92,5, Fremdkamm −73,9 / −75,6, fs/8 −80,9 / −80,7. Die Serie war also stabil, die Streuung innerhalb einer Sitzung liegt bei ≈ 1–2 dB. In b2 ist zusätzlich schwach (−98 dB) der Hub-SOF von gestern zu sehen (1000,0541 UMC = 999,869 AC/DC).
7. **Eingänge in diesem Aufbau lauter als in A5:**
   - S3-c-in −71,3 dB Gerät (Aufnahmeprogramm, ohne Host-Faktor), S3-d-in −66,0 dB Datei ≈ −72 dB Gerät. A5-b1d: −73,2 dB Datei ≈ −79 dB Gerät. Das sind **≈ 7–8 dB mehr**.
   - Auf den Eingängen liegen SOF-Kamm (−88), Fremdkamm (−88), 59,97 Hz (−83) und fs/8 (−87).
   - **[Hypothese]** Auch hier wirkt die Masseschleife über das Ausgangskabel zum UMC, dazu kommt der Mac-Port statt des Hubs (vgl. S2-6).

**Bewertung A7/S3:**
- Die Ausgangsfrage ist beantwortet: Der USB-1-kHz-Kamm von acdc1 kommt vom SOF, ist schon ohne Stream da und verschwindet ohne USB.
- Für den Standalone-Betrieb ist das gut, denn ohne USB ist der Ausgang frei von USB-Kämmen.
- Im gemischten Betrieb, mit AC/DC-USB am Rechner und Ausgängen in ein zweites Interface am selben Rechner, ist dagegen die **Masseschleife das größte Problem** (+20 dB), nicht der SOF-Kamm.

**Nächste Schritte (Vorschlag):**
- Schleife auftrennen und S3-b wiederholen: AC/DC am selben Hub wie der UMC (kürzere Schleife) und/oder ein USB-Isolator am AC/DC. Im Unterschied zum Eingangskamm (atau, #2072) sollte der Isolator **hier** wirken.
- Herkunft von 59,97 Hz und 1000,0346 Hz klären (z. B. Display/Netzteil des Macs ab, UMC an anderem Port).

### D21 – Masseschleife: Serie G (2026-11-15)

**Setup:** wie S3-b (D20): acdc1 Build 1d, Eingänge offen, Gain 12 Uhr, Out 1 → MTM Startup → UMC In 1, USB gesteckt ohne Stream, Host-Software nimmt nur den UMC auf (Datei mit Host-Faktor 2), 120 s. Umgebung laut Nutzer: Mac über den Thunderbolt-Hub versorgt, externer Monitor am Hub, kein Isolator und keine DI-Box vorhanden. Case, Hub-Netzteil und Mac-Netzteil hängen an derselben Doppelsteckdose, aber an zwei verschiedenen Leisten. Je Messung wurde genau eine Verbindung gegenüber G0 geändert. Manifest `G0`, `G2`, `G2a`, `G1`, Auswertung `out/G*/` (`--ref G0`).

| ID | Änderung gegenüber G0 | Datei |
|---|---|---|
| G0 | keine (= S3-b neu: AC/DC am Mac-Port, UMC + Monitor am Hub) | `20261115_acdc1_g0-loop-ref_g12_usb-plugged.2chan.000.wav` |
| G2 | Monitor-Kabel am Hub gezogen | `20261115_acdc1_g2-no-monitor_g12_usb-plugged.2chan.000.wav` |
| G2a | Monitor ab **und** AC/DC-USB ab (versehentlich, behalten als Gegenstück zu S3-a) | `20261115_acdc1_g2a-no-monitor_g12_usb-off.2chan.000.wav` |
| G1 | AC/DC-USB **am Hub** (wie der UMC), Monitor dran | `20261115_acdc1_g1-acdc-at-hub_g12_usb-plugged.2chan.000.wav` |
| G3 | ohne Hub, Mac auf Akku, UMC + AC/DC direkt am Mac | **entfällt** (Nutzer: mobiler Betrieb kommt nicht vor) |

**Ergebnis [gemessen]** (Out 1, UMC-Datei-dBFS, Linien als Sinus-Amplitude k = 1, Frequenzen in UMC-Zeitbasis, „–“ = keine Linie > 15 dB über Boden):

| Komponente | S3-b | G0 | G2 (ohne Monitor) | G1 (AC/DC am Hub) | S3-a (USB ab) | G2a (USB + Monitor ab) |
|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −56,5 | −57,4 | −56,0 | **−75,1** | −75,9 | −75,8 |
| Rest ohne Störlinien | −57,1 | −57,8 | −57,5 | **−76,6** | −78,0 | −78,1 |
| 59,98-Hz-Impulse | −68,5 | −70,2 | **–** | – | −108,9 | – |
| 29,20-Hz-Familie | −75,1 | −76,1 | **−63,5** | – | – | – |
| Fremdkamm 1000,220 (k = 1 / 2) | −73,9 / −76,7 | −74,8 / −77,7 | −69,3 / −65,8 | **–** | −120,7 / – | – |
| AC/DC-SOF-Kamm (Mac-Port 1000,175) | −93,4 | −90,6 | −92,4 | (am Hub: 1000,053) – | – | – |
| fs/48-Kamm 1000,185 | verdeckt | verdeckt | verdeckt | −107,0 | −111,5 | −115,0 |
| fs/8 6001,11 (Durchleitung) | −80,9 | −81,2 | −80,9 | −81,1 | −80,5 | −79,7 |
| Klick-Treffer | 6 581 | 6 400 | 0 | 1 | 0 | 0 |

1. **G0 = S3-b:** reproduzierbar innerhalb ≈ 1 dB, über ≈ 1,5 h und mehrfaches Umstecken.
2. **Die Masseschleife entsteht, weil das AC/DC am USB-Port des Macs hängt und der UMC am Hub. Mit beiden am Hub (G1) ist sie weg:**
   - RMS −75,1 dB ist so gut wie ohne USB (S3-a −75,9). 59,98 Hz, 29,2 Hz und der Fremdkamm sind verschwunden.
   - Auch der SOF-Kamm des AC/DC (jetzt Hub-SOF ≈ 1000,053 UMC) liegt am Ausgang unter der Nachweisgrenze (< −116 dB). Übrig bleiben nur fs/8, fs/48 und Netz 50 Hz, also dasselbe Bild wie im Standalone-Betrieb.
   - **[Hypothese]** Der Mac wird über das Thunderbolt-Kabel vom Hub versorgt. Zwischen der Masse am Mac-Port und der Masse am Hub fließt deshalb ein Ausgleichsstrom mit Anteilen von Monitor, Hub-Netzteil und Mac. Die Schleife über USB (Mac-Port) und Audiokabel (UMC am Hub) greift ihn ab. Hängen beide Geräte am Hub, liegen sie auf fast derselben Masse.
3. **Der Monitor erzeugt die 59,98-Hz-Impulse:** Ohne Monitor (G2) sind sie samt Klick-Treffern weg. Die Schleife bleibt aber gleich laut (RMS −56,0). Stattdessen werden eine Familie bei 29,20 Hz und der Fremdkamm 1000,220 lauter (+5…+12 dB). **[Hypothese]** Der Ausgleichsstrom verteilt sich nach dem Ziehen des Monitors anders. Die Quelle bleibt Hub/Mac, der Monitor ist nur eine von mehreren.
4. **G2a ≈ S3-a:** Ohne USB ändert der Monitor nichts (−75,8 / −75,9 dB). Er wirkt also nur über die USB-Schleife.

**Folge für den Betrieb [gemessen]:**
- **AC/DC und UMC (bzw. jedes zweite Interface, in dessen Eingang der AC/DC-Ausgang geht) gehören an denselben Hub.** Dann ist der Ausgang mit gestecktem USB so sauber wie standalone.
- Der Mac-Port war nur für S3 gewählt, damit sich die SOF-Kämme trennen lassen. Er ist für diesen Aufbau die schlechteste Wahl. Das passt zu S2-6 (Hub bleibt die bessere Wahl), dort ohne Audiokabel zum UMC.
- Ein USB-Isolator ist für diesen Fall nicht nötig.

**Offen:**
- G3 entfällt. Stattdessen G4: AC/DC im Alltags-Aufbau (passiver USB-Hub → Monitor-Hub → TB-Hub).
- Ob die Eingänge in der Hub-Konfiguration ebenfalls zum A5-Niveau zurückgehen: Hier wurde nur Out 1 gemessen, nicht die AC/DC-Eingänge.

### D22 – Alltags-Aufbau: G4 (Ausgang) und G4-in (Eingänge) (2026-11-15)

**Alltag laut Nutzer:**
- Die AC/DC-Eingänge dienen für Aufnahmen aus dem Rack. Die Ausgänge führen CV oder Audio zurück ins Rack, der UMC ist nur Ausgabe an Boxen/Kopfhörer. **AC/DC-Out → UMC-In kommt nicht vor.**
- USB-Kette: AC/DC → passiver USB-Hub → USB-Hub im Monitor → TB-Hub. G3 (ohne Hub) entfällt.

**G4** (`20261115_acdc1_g4-daily-hub-chain_g12_usb-plugged.2chan.000.wav`, Manifest `G4`, `out/G4/`, `--ref G1`): Aufbau wie G1 (Out 1 → Startup → UMC In 1, USB gesteckt, kein Stream), aber das AC/DC hängt an der Alltags-USB-Kette.

**Ergebnis G4 [gemessen]: sauber.**
- RMS −76,1 dB, Rest −77,9 dB, so gut wie G1 (−75,1) und S3-a ohne USB (−75,9).
- Keine 59,98-Hz-Impulse, kein Fremdkamm, keine Klick-Treffer.
- Der SOF-Kamm liegt jetzt beim Hub-SOF (1000,0531 Hz UMC = 999,868 Hz AC/DC) und ist mit ≈ −104 dB (k = 1) bzw. −99 dB (Summe) praktisch bedeutungslos.
- Die Kette über passiven Hub und Monitor-Hub bringt also **keine Masseschleife**.

**G4-in, erste Versuche ungültig:** `…_g4-in-daily-hub-chain_…` (mit Kabel Out 1 → UMC) und `…_g4-in-daily-no-out_…` sind **digital 0, in jedem Sample**. Ursache unbekannt, vermutlich Patch oder Gerätewahl in der Host-Software. Im Manifest als UNGÜLTIG markiert.

**G4-in-no-out-2** (`20261115_acdc1_g4-in-daily-no-out-2_g12_usb-duplex.4chan.000.wav`, Manifest `G4-in-no-out-2`, `out/G4-in-no-out-2/`, `--ref A5-b1d`): AC/DC-Eingänge 1–4 offen, Gain 12 Uhr, Ausgänge frei, Alltags-USB-Kette, Host-Software Duplex (AC/DC ausgewählt, Stille an die Ausgänge), UMC-Ausgänge an Boxen/Kopfhörer. 120 s, Datei mit Host-Faktor 2.

| Größe (Kanalmittel, Datei-dBFS) | A5-b1d (TB-Hub direkt, morgens) | S3-d-in (Mac-Port + Schleife) | G4-in-no-out-2 (Alltag) |
|---|---|---|---|
| RMS ≥ 20 Hz | −73,2 | −66,7 | **−67,4** |
| A-bewertet | −74,6 | −69,8 | −71,8 |
| Rest ohne Störlinien | −77,6 | −67,2 | **−68,1** |
| fs/8-Linie | −80,0 | −82,1 | −80,0 |
| 1-kHz-Kamm (Summe) | −77,4 (f0 999,8680) | −81,6 (999,9895) | −77,9 (999,8676) |
| Mischprodukte | −86,5 | −89,1 | −86,6 |
| Störanteil | 65 % | 7 % | 16 % |

**Ergebnis [gemessen]:**
- **Die USB-Linien sind im Alltags-Aufbau genau wie in A5:** Kamm beim Hub-SOF (999,8676 Hz), fs/8, Mischprodukte, alle auf ±0,5 dB gleich. Die USB-Kette fügt keine Linien hinzu. Fremdkamm und 59,98 Hz fehlen.
- **Das breitbandige Rauschen ist aber ≈ 10 dB höher als in A5** (Rest −68,1 gegen −77,6), fast genauso hoch wie in S3-d-in mit Schleife. Es steigt zu tiefen Frequenzen hin an (Median-Rauschdichte Kanal 1 gegen A5-b1d):

  | Band | Δ |
  |---|---|
  | 20–100 Hz | +11,8 dB |
  | 100–300 Hz | +14,2 dB |
  | 300 Hz–1 kHz | +9,7 dB |
  | 1–3 kHz | +5,2 dB |
  | 3–8 kHz | +2,1 dB |
  | über 8 kHz | ≈ 0 |

  Es ist kein Linienspektrum, sondern breitbandig und zu tiefen Frequenzen hin ansteigend.
- **[Hypothese]** Das ist keine USB-Wirkung, denn die Linien sind gleich geblieben. Eher ist es Einstreuung in die offenen, hochohmigen Eingänge durch die Umgebung am Nachmittag: andere Module, Kabel, Startup/UMC/Boxen eingeschaltet, Hände in der Nähe. S3-d-in (gleicher Nachmittag) zeigt dieselbe Form. Getestet ist das nicht. Ein direkter A/B-Test fehlt: A5-Aufbau (AC/DC direkt am TB-Hub) jetzt in derselben Umgebung.

**Folge:** Für Linien und Masse ist der Alltags-Aufbau unbedenklich. Woher die +10 dB breitbandig bei offenen Eingängen kommen, ist offen.

### D23 – A/B Eingänge: TB-Hub direkt gegen Alltags-Kette (G5/G6, 2026-11-15)

**Setup:** wie G4-in-no-out-2 (D22): Eingänge offen, Gain 12 Uhr, Ausgänge frei, UMC-Ausgänge an Boxen/Kopfhörer, Host-Software Duplex. **Je 60 s, direkt nacheinander** (15:27 / 15:30), am Tisch nichts verändert.
- G5: AC/DC-USB direkt am TB-Hub (wie A5), `20261115_acdc1_g5-in-tbhub-direct_g12_usb-duplex.4chan.000.wav`
- G6: wieder Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), `20261115_acdc1_g6-in-daily-chain-again_g12_usb-duplex.4chan.000.wav`

Manifest `G5`, `G6`, Auswertung `out/G5/`, `out/G6/` (`--ref G4-in-no-out-2`). Kanalmittel, Datei-dBFS (Host-Faktor 2):

| Größe | A5-b1d (morgens, 120 s) | G4-in-no-out-2 (15:19) | G5 TB-Hub direkt | G6 Alltags-Kette | Δ G6 − G5 |
|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −73,2 | −67,4 | −73,0 | −73,3 | −0,4 |
| Rest ohne Störlinien | −77,6 | −68,1 | −78,3 | −78,2 | ±0,0 |
| fs/8-Linie | −80,0 | −80,0 | −80,0 | −79,7 | +0,3 |
| 1-kHz-Kamm (Summe) | −77,4 | −77,9 | −76,3 | −77,5 | −1,2 |
| f0 Kamm | 999,8680 | 999,8676 | **999,9970** | 999,8675 | |

Median-Rauschdichte Kanal 1 [dB/Hz], erste 60 s jeder Datei:

| Band | A5-b1d | G4-in | G5 | G6 |
|---|---|---|---|---|
| 20–100 Hz | −107,0 | −92,3 | −107,5 | −106,3 |
| 100–300 Hz | −112,4 | −94,2 | −113,6 | −113,1 |
| 300 Hz–1 kHz | −114,8 | −102,7 | −116,3 | −116,3 |
| 1–3 kHz | −117,8 | −111,3 | −118,7 | −118,6 |
| über 3 kHz | −120,6…−123,3 | −118,2…−122,7 | −120,9…−123,4 | −120,8…−123,2 |

**Ergebnis [gemessen]:**
- **Die Alltags-Kette ist gleichwertig mit dem TB-Hub direkt.** G5 und G6 stimmen beim Breitbandrauschen auf 0,1 dB und bei RMS auf 0,4 dB überein. Beide liegen auf dem Niveau von A5-b1d (Rest −78,3 / −78,2 gegen −77,6).
- **Die +10 dB in G4-in-no-out-2 (D22) waren vorübergehend** und sind 8–11 min später nicht mehr da. Sie stammen also weder von der Hub-Kette noch dauerhaft von der Umgebung. **[Hypothese]** Eine kurzzeitige Einstreuung in die offenen Eingänge: Die Aufnahme folgte direkt auf die Fehlersuche an den leeren G4-in-Dateien (Hantieren an Rack/Kabeln, Oszillator-Gegentest). Bei offenen Eingängen sind solche Ausreißer zu erwarten. Messungen mit offenen Eingängen sollten deshalb in Ruhe und doppelt (b/b2-Prinzip) gemacht werden.
- **Der TB-Hub hat mehr als einen SOF-Takt:** G5 (TB-Hub direkt, heute) zeigt f0 999,9970 Hz, A5-b1d (TB-Hub, heute Morgen) und die Alltags-Kette 999,868 Hz. **[Hypothese]** Der Port in G5 hängt an einem anderen USB-Controller im Hub als der Port von A5 bzw. der Monitor-Hub. Für Notch-Filter heißt das: f0 hängt vom Port ab, siehe auch S2-6.
- Die Mischprodukte sind in G5 (−89,2) niedriger als in G6 (−86,4). Das ist nicht vergleichbar: Bei f0 999,997 Hz liegt die Musterperiode 1/|6·f0 − 6000| bei ≈ 55 s, in 60 s also kaum auflösbar.

**Folge:** Für Aufnahmen über die AC/DC-Eingänge ist der Alltags-Aufbau (passiver Hub → Monitor-Hub → TB-Hub) in Ordnung. Er rauscht wie der direkte TB-Hub-Anschluss und wie A5.

### D24 – A5 zweimal mit Build 1d: Sitzungsstreuung vor Build 2 (2026-11-15)

**Anlass:** Grill-Runde Build 2 (`docs/05`, „Build 2 neu“, Q5). Vor dem Flash von Build 2 soll gemessen werden, wie stark A5 zwischen zwei Aufnahmen streut. Erst damit lässt sich sagen, ob die +4,7 dB bei den Mischprodukten in D19 von der Firmware kommen oder von der Sitzung. Die Streuung ist außerdem der Maßstab für den späteren Vergleich 1d ↔ Build 2 (B3).

**Setup:**
- acdc1 mit Build 1d `v22.4.r-thru1d`, Eingänge offen, Gain 12 Uhr, Slot 1 „ACDC“.
- **Alltags-Kette:** passiver Hub → Monitor-Hub → TB-Hub. A5-b1d (D19) lief am TB-Hub direkt, aber an einem Port mit demselben SOF.
- Host-Software 48 kHz, Audio-Modul ohne Playback, Mehrkanal-Recorder (Host-Faktor 2).
- r1 ≈ 15:53–15:55, dann **Host-Software ganz neu gestartet** (neuer USB-Stream), danach r2 ≈ 15:55–15:57. Rack, USB und Case blieben unberührt.
- Dateien:
  - `recordings/20261115_acdc1_b1d-open-inputs-r1_g12_usb-stream.4chan.000.wav` (120,3 s)
  - `recordings/20261115_acdc1_b1d-open-inputs-r2_g12_usb-stream.4chan.000.wav` (120,1 s)

  Beide 48 kHz / 32 Bit float, keine Null-Samples.
- Manifest `A5-b1d-r1`, `A5-b1d-r2`, Auswertung `out/A5-b1d-r{1,2}/` (`--ref A5-b1d`).

**Ergebnis [gemessen]** (Datei-dBFS, Mittel über die 4 Kanäle):

| Größe | A5-b1b (1b, 14.11.) | A5-b1d (1d, morgens) | r1 (1d) | r2 (1d) | r2 − r1 | r1 − A5-b1d | r1 − A5-b1b |
|---|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,2 | −73,3 | −73,3 | −73,3 | 0,0 | 0,0 | −1,1 |
| A-bewertet | −73,3 | −74,7 | −74,5 | −74,5 | 0,0 | +0,2 | −1,2 |
| Rest ohne Störlinien | −78,2 | −77,9 | −78,6 | −78,6 | 0,0 | −0,6 | −0,4 |
| fs/8-Linie 6000 Hz | −78,2 | −80,0 | −79,7 | −79,7 | 0,0 | +0,2 | −1,5 |
| 1-kHz-Kamm (Summe) | −75,5 | −77,6 | −77,2 | −77,2 | 0,0 | +0,4 | −1,7 |
| **Mischprodukte (Summe)** | −91,1 | −86,5 | −86,4 | −86,4 | −0,1 | +0,1 | **+4,8** |
| Störanteil | 74 % | 65 % | 70 % | 70 % | | | |
| Gewinn ideale Notch-Bank | 6,0 dB | 4,6 dB | 5,3 dB | 5,3 dB | | | |

Einzelne Mischprodukte, Kanal 1 (wie in D19):

| Linie | A5-b1b | A5-b1d | r1 | r2 |
|---|---|---|---|---|
| 8·f1 + f2 | −103,6 | −96,6 | −96,5 | −96,7 |
| 4·f1 + 2·f2 | −106,2 | −96,9 | −96,6 | −96,6 |
| 4·f1 + f2 | −108,5 | −97,6 | −97,0 | −97,2 |

- **r1 und r2 sind gleich.** Alle Größen stimmen auf ≤ 0,1 dB überein, auch nach einem neuen USB-Stream. Klicks 0, f0 Kamm 999,8676 Hz, fs/8 exakt 6000,0000 Hz.
- **Auch zwischen Sitzungen ist die Streuung klein.** Gegenüber A5-b1d vom Morgen (anderer Aufbau, ≈ 5,5 h früher, kurz nach einem Kaltstart) liegen r1/r2 im Mittel auf ±0,6 dB, je Kanal auf ±1,4 dB.
- Unter 20 Hz ist A5-b1d ≈ 10 dB lauter (RMS gesamt −60 gegen −71 dB). Das ist die Aufwärmdrift aus D19, ab 20 Hz spielt sie keine Rolle.

**Bewertung:**
- **Die +4,7 dB bei den Mischprodukten kommen von der Firmware, nicht von der Sitzung [gemessen].** Mit Build 1d sind sie in drei Aufnahmen aus zwei Sitzungen auf 0,1 dB gleich, der Abstand zu Build 1b (+4,8 dB) ist 50-mal größer als die Streuung. Die Hypothese „Sitzung“ aus D19 ist widerlegt.
- Ebenso sind **Kamm (−1,7 dB) und fs/8 (−1,5 dB) bei 1d wirklich leiser als bei 1b**, nicht nur in einer Sitzung.
- **[Hypothese, weiter offen]** Zwischen 1b und 1d kamen Patch 05 (atomarer RX-Zähler) und 06 (Pufferstand-Regelung, mehr Arbeit in `DataOut`/`sof_callback`) dazu. Patch 04 ändert nur den Ausgangspegel. Mehr Arbeit im USB-Interrupt verstärkt die Kopplung USB-Takt × Blocktakt. Trennen ließe sich das mit Build 1c (nur 05), der mit offenen Eingängen nie gemessen wurde.
- Absolut bleibt es klein: Die Mischprodukte machen ≈ 4–7 % des Rauschens aus, der Gesamtpegel ab 20 Hz ist mit 1d sogar 1,1 dB niedriger als mit 1b.
- **Für Build 2:** Die Streuung innerhalb einer Sitzung liegt bei ≤ 0,1 dB, im Kanalmittel und je Kanal. Unterschiede von mehr als ≈ 0,5 dB zwischen 1d und Build 2 können also als echt gelten. Build 2 ändert nur die TX-Quelle (vor dem Patch). Erwartet wird deshalb dasselbe Bild, bis auf den Faktor des Gain-Knobs bei 12 Uhr (≈ ×1, nicht exakt bekannt).

### D25 – Build 2 `v22.4.r-fx1d` geflasht, A1 und B1 (2026-11-15)

**Flash** (Ablauf aus `CLAUDE.md`, Freigabe des Nutzers im Chat, Log `firmware/flashlog/20261115_build2-fx1d/`):
1. `owl_read_before`: `AC/DC v22.4.r-thru1d`, Slot 1 „ACDC“ (CRC `0xbeb3bb2e`), Storage 31 232 B. Die letzte Meldung `tx ovf 0.4444 1.0000 32.0000` stammt vom Schließen der Host-Software (Stream-Ende).
2. `owl_read.py --reset-to-dfu --yes` → ROM-DFU `0483:df11`, Seriennummer `200364500000`.
3. `dfu-util … -s 0x08000000 -D firmware/builds/acdc1-build2-fx1d/ACDC.bin` → rc 0.
4. Readback 128 KB: Die ersten 105 968 B haben die SHA-256 `7f9f9a34…` (= `ACDC.bin`), der Rest ist 0xFF (`sha256.txt`).
5. Der Nutzer hat neu gestartet: Case aus, USB ab, Case an, USB an.

**A1 [gemessen]:** `owl_read_after` meldet:
- `AC/DC v22.4.r-fx1d`, `SR/BS/CH 48000 8 4`
- Slots unverändert (1 „ACDC“ `0xbeb3bb2e`, 2 „[Lich]“ `0xeed65a68`), Storage 31 232 B

`settings_cc` weicht nur zweimal ab:
- `bootloader_lock` 1 → 0: zufälliger Wert vom Stack, siehe D11. Er springt schon seit Build 1b bei jedem Flash zwischen 0 und 1.
- CC 22 61 → 62: Knob-Zittern

**Bestanden.**

**B1 [gemessen]:**
- `ioreg` meldet „USB Product Name“ = **„OWL-ACDC-FX“**, auch `system_profiler SPAudioDataType` zeigt „OWL-ACDC-FX“ (4 Eingänge).
- Der **MIDI-Port heißt aber weiter „OWL-ACDC“** (`mido`, Ein- und Ausgang). **[Hypothese]** CoreMIDI merkt sich das USB-MIDI-Gerät mit seinem ersten Namen (Audio-Einstellungen des Systems, MIDI-Studio) und benennt es beim erneuten Anmelden nicht um.
- `owl_read.py` findet das Gerät so oder so (Teilstring).
- **B1 bestanden** für Audio und `owl_read.py`. Der MIDI-Name ist nur kosmetisch. Ändern ließe er sich im MIDI-Studio, indem man das Gerät dort löscht oder umbenennt. Nicht nötig.

**A2, A3, B2 ohne Stream [gemessen, Nutzer am Rack, nach Gehör]:**
- A2: USB ab, Signal in In 1…4 → an Out 1…4 hörbar, Gain 12 Uhr. **Bestanden.**
- A3: USB gesteckt, keine Audio-App → weiter hörbar. **Bestanden.**
- B2, Teil 1 (ohne Rechner-Stream): Gain 0 → Ausgang stumm. **Bestanden.**

**B2, Teil 2 [gemessen]:** Manifest `B2-fx1d`, Datei `recordings/20261115_acdc1_fx1d-b2-gain-sweep_gvar_usb-duplex.4chan.000.wav` (36,7 s).
- Setup: Oszillator ≈ 124,5 Hz in In 1, In 2–4 offen. Das Gerät wurde in der Host-Software als „OWL-ACDC-FX“ gewählt (`vcv-patches/acdc-fx-umc-in-out.vcv`, neu). Gain während der Aufnahme: 12 Uhr → 0 → Vollanschlag → 12 Uhr.
- **Kanal 1 bleibt in allen 36 Sekundenfenstern bei −2,8 dB (Datei-dBFS) auf 0,05 dB konstant.** Der Gain-Knob wirkt also nicht mehr auf die USB-Aufnahme, sie kommt vor dem Patch (PRE_FX). Mit 1d wäre Kanal 1 bei Gain 0 digital null gewesen (S2). **B2 bestanden.**
- Nebenbefund **Übersprechen [gemessen]:** Bei Gain auf Vollanschlag ((Knob·2)² = ×4) übersteuert Out 1. In den offenen Eingängen 2–4 steigen dann die Harmonischen des Oszillators (117/132, 246–255, 4400, 6604 Hz) um 9–17 dB, auf ≈ −89…−110 dB. Das Band 20–500 Hz steigt um 2,7–5,1 dB, darüber bleibt alles gleich. Beim Umschalten gibt es kurze Spitzen (−65 dB). Bei Gain 0 sind die offenen Kanäle 0,5–0,7 dB leiser als bei 12 Uhr (Ausgang stumm, kein Übersprechen). **[Hypothese]** Der Ausgang koppelt über Masse oder Versorgung in die hochohmigen offenen Eingänge (kein USB-Effekt, die Aufnahme ist roh). Für A5/B3 deshalb Gain fest auf 12 Uhr und nichts an den Ausgängen.

**A4 [gemessen, Nutzer nach Gehör]:** Host-Playback ist an den Ausgängen hörbar. Nach dem Beenden bzw. Abwählen in der Host-Software kommt die Durchleitung zurück. **Bestanden.**

2 × A5/B3 → D26, A6 → D27.

### D26 – A5/B3 mit Build 2: rohe Eingänge offen, Vergleich mit 1d (2026-11-15)

**Setup:** wie D24, mit Build 2 `v22.4.r-fx1d`:
- Eingänge und Ausgänge frei, Gain-Knobs 12 Uhr
- Alltags-Kette, Host-Software auf „OWL-ACDC-FX“, Audio-Modul ohne Playback, Mehrkanal-Recorder
- **60 s** statt 120 s (Musterperiode der Mischprodukte 1,26 s, also ≈ 48 Perioden)
- r1 ≈ 16:18, Host-Software ganz neu gestartet, r2 ≈ 16:20
- Dateien `recordings/20261115_acdc1_fx1d-open-inputs-r{1,2}_g12_usb-stream.4chan.000.wav` (je 60,3 s, keine Null-Samples)
- Manifest `B3-fx1d-r1/-r2`, Auswertung `out/B3-fx1d-r{1,2}/`

Zum fairen Vergleich wurden die 1d-Aufnahmen aus D24 auf dieselbe Länge gekürzt (erste 60,3 s) und ausgewertet: `out/A5-b1d-r{1,2}-60s/`. Die gekürzten WAVs waren nur temporär.

**Patch-Faktor:** Bei 1d lief die USB-Aufnahme durch den VCA des Default-Patches (Gain = (2·Knob)²), bei Build 2 nicht.
- Vorhersage aus den Knob-Werten vor dem Flash (CC 20–23 = 62/61/61/58): 1d leiser um 0,42 / 0,70 / 0,70 / 1,57 dB.
- **Gemessen über das DC-Verhältnis B3/1d:** +0,37 / +0,46 / +0,48 / +1,62 dB [gemessen]. Der DC-Offset der offenen Eingänge eignet sich also als Gain-Sonde. Die Abweichung bei Kanal 2/3 passt zur 7-Bit-Auflösung der CC-Werte und zum Knob-Zittern.
- In der Spalte „korrigiert“ unten ist dieser gemessene Faktor je Kanal abgezogen.

**Ergebnis [gemessen]** (Datei-dBFS, Mittel über die 4 Kanäle):

| Größe | 1d r1 (60 s) | 1d r2 (60 s) | B2 r1 | B2 r2 | B2: r2 − r1 | B2 − 1d roh | **B2 − 1d korrigiert** | korrigiert je Kanal |
|---|---|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −73,28 | −73,28 | −72,64 | −72,62 | +0,02 | +0,65 | **−0,08** | −0,07 / −0,06 / −0,15 / −0,04 |
| A-bewertet | −74,55 | −74,55 | −73,79 | −73,79 | +0,01 | +0,76 | **+0,03** | −0,01 / +0,08 / −0,04 / +0,07 |
| Rest ohne Störlinien | −78,62 | −78,59 | −78,09 | −78,10 | 0,00 | +0,51 | **−0,22** | −0,08 / −0,20 / −0,47 / −0,15 |
| fs/8-Linie 6000 Hz | −79,75 | −79,75 | −79,04 | −79,05 | 0,00 | +0,71 | **−0,02** | |
| 1-kHz-Kamm (Summe) | −77,17 | −77,19 | −76,46 | −76,42 | +0,04 | +0,74 | **+0,01** | |
| Mischprodukte (Summe) | −86,42 | −86,43 | −85,50 | −85,48 | +0,03 | +0,93 | **+0,20** | +0,23 / +0,20 / +0,21 / +0,17 |
| Störanteil | 70,0 % | 69,8 % | 70,8 % | 71,0 % | | +1,0 % | | |
| Gewinn ideale Notch-Bank | 5,31 dB | 5,28 dB | 5,45 dB | 5,48 dB | | +0,17 | | |

- Klicks 0 in allen vier Aufnahmen. f0 Kamm 999,8673 Hz (1d 999,8676, gleicher Port), fs/8 exakt 6000,0000 Hz.
- **r1 und r2 sind auch bei Build 2 gleich** (≤ 0,04 dB). Die 60-s-Kürzung ändert bei 1d nichts gegenüber 120 s (D24).

**Bewertung:**
- **A5 für Build 2 bestanden.** Nach Abzug des Patch-Faktors sind Rauschen, Kamm und fs/8 auf ±0,2 dB gleich wie bei 1d. Rein rechnerisch ist der Rest bei Kanal 3 0,47 dB besser. TX_PRE_FX ändert am Rauschen in den ADC-Daten also nichts. Das war zu erwarten, denn die Störungen stecken vor dem Patch (S2).
- Die Mischprodukte liegen +0,2 dB über 1d. Das ist mehr als die Streuung (0,03 dB), aber weit unter der Schwelle von 0,5 dB und verglichen mit den +4,8 dB von 1b → 1d unbedeutend. **[Hypothese]** Der USB-TX-Teil (`usbd_tx_convert`) läuft jetzt am Ende statt am Anfang von `onProgramReady`. Das verschiebt die CPU-Last im Block leicht.
- **B3 = neue Basislinie für alle Rausch-Experimente (E3)** (Datei-dBFS, Geräte-dBFS = −6,02 dB):
  - RMS ≥ 20 Hz −72,6 dB, A-bewertet −73,8 dB, Rest −78,1 dB
  - fs/8 −79,0 dB, Kamm −76,4 dB, Mischprodukte −85,5 dB
  - Störanteil 71 %, ideale Notch-Bank 5,5 dB

  Die Werte gelten unabhängig von der Knob-Stellung.

### D27 – A6 mit Build 2: Rückführung 10 min (2026-11-15)

**Setup:**
- Wie A6L-b1d (D18), aber 10 min, Build 2 `v22.4.r-fx1d`, Alltags-Kette.
- Kabel Out n → In n, Gain 12 Uhr. Host-Software auf „OWL-ACDC-FX“ spielt Sinus 440/530/670/790 Hz auf Out 1…4 (RX POST_FX überschreibt den Patch). Mehrkanal-Recorder nimmt In 1…4 auf (rohe Eingänge, TX PRE_FX).
- Datei `recordings/20261115_acdc1_fx1d-loop-10min_g12_usb-rxtx.4chan.000.wav` (599,98 s, keine Null-Bereiche), Ende ≈ 16:37.
- Manifest `A6-fx1d`, Auswertung `out/A6-fx1d/` (Standard-Analyse und `phase_slips.json/.txt`).

**Ergebnis [gemessen]:**
- **`phase_slips.py`: 0 Ereignisse auf allen 4 Kanälen.** Ein Slip von 1 Sample läge 5 000–16 000-fach über dem Phasenrauschen. Amplitude 0,2 dBFS (Datei), Spanne 0,1–99,9 % = 0,00 dB.
- **Klick-Detektor: 0 Klicks** auf allen Kanälen.
- Kanalzuordnung stimmt (Kanal n = Ton n). Die LED-Linie 2320,54 Hz ist mit Signal wieder da (1–2 % Anteil, wie bisher, H3).
- **Geräte-Meldung** nach dem Ende der Aufnahme, Host-Software lief noch: `fb 48.0004 96.2500`.
  - Eine Feedback-Messung wurde verworfen, weil das Intervall doppelt so lang war wie erwartet (≈ 2 ms statt 1 ms, also ein SOF ausgefallen oder verspätet).
  - Der Zeitpunkt ist unbekannt (nur die letzte Meldung bleibt).
  - In der Aufnahme gibt es dazu weder einen Slip noch einen Klick. Der Regler hat die Messung wie vorgesehen verworfen.
  - **[Hypothese]** Ein einzelner verspäteter SOF im Hub (Alltags-Kette mit drei Hubs). Ähnlich wie D18, dort aber mit hörbarer Störung.

**Bewertung: A6 für Build 2 bestanden.** Der USB-Pfad ist mit TX_PRE_FX genauso stabil wie mit 1d.

**Abnahme Build 2 komplett (D25–D27):** A1, A2, A3, A4, A5, A6, B1 (Audio; MIDI-Name kosmetisch), B2, B3 bestanden. Rückfall-Kriterien (E7) nicht erfüllt. Build 2 bleibt auf acdc1.

### D28 – Build 3 `v22.4.r-fx2` geflasht: Eingangs-LEDs mit Stream dauerhaft rot (2026-11-15)

**Ziel (Grill-Runde 2026-11-15, `docs/05` „Build 3“):** Mit TX-Stream (Rechner nimmt auf) zeigen die Eingangs-LEDs 1–4 den rohen Eingangspegel statt des Patch-Werts. Rot = Spitze ≥ −0,1 dBFS, 300 ms gehalten. Ohne Stream bleibt alles wie bisher.

**Build:**
- `firmware/builds/acdc1-build3-fx2/` = Build 2 + Patch 07 v1, 106 316 B, SHA `f01c8e6b…`
- Patch 07 v1 als Beleg: `firmware/builds/acdc1-build3-fx2/07-input-leds-raw-when-recording.v1.patch`

**Flash** (Freigabe im Chat, Log `firmware/flashlog/20261115_build3-fx2/`):
- `owl_read_before`: `v22.4.r-fx1d`, Slots unverändert.
- DFU, `dfu-util -D` rc 0. Readback: Die ersten 106 316 B = `ACDC.bin`, der Rest 0xFF.

**A1 [gemessen]:**
- `v22.4.r-fx2`, `SR/BS/CH 48000 8 4`, CPU 9 %, Slots und Storage gleich.
- `settings_cc`: CC 20 66 → 61 und CC 22 61 → 62 (Knob). Bestanden.

**A2, A3 [gemessen, Nutzer]:** Durchleitung ohne USB bzw. mit USB ohne App, Eingangs-LEDs folgen dem Regler. Bestanden.

**LED-Test mit Stream [gemessen, Nutzer]:**
- **Nicht bestanden.** Alle vier roten Eingangs-LEDs leuchten dauernd, unabhängig vom Signal.
- Ausgangs-LEDs normal.
- Wählt man in der Host-Software ein anderes Gerät (Stream aus), kommt das Verhalten ohne Stream zurück. Die Umschaltung selbst geht also.

**Ursache [Code]:**
- SAI1 läuft mit `SAI_DATASIZE_24` (`ACDC/Core/Src/main.c:479`). Die ADC-Wörter im Puffer sind 24 Bit rechtsbündig, **ohne Vorzeichenerweiterung**.
- Ein negatives Sample, z. B. −1, ist als `int32` 0x00FFFFFF = +16 777 215 und liegt damit über der Clip-Schwelle. Rauschen um 0 setzt deshalb in jedem Block das Clip-Bit.
- Die USB-Daten stimmen trotzdem: `AUDIO_INT32_TO_SAMPLE` = `x>>8`, abgeschnitten auf `int16`, Bit 23 wird dabei zum Vorzeichen.
- `tx_levels` misst den DAC-Puffer, den der Patch mit Vorzeichen schreibt.
- Den Patch-Programmen fällt das nicht auf, weil die Library beim Einlesen um 8 Bit nach links schiebt. **[Hypothese]**, in diesem Baum nicht nachgelesen.

**Folge:** Patch 07 v2 erweitert vor der Messung das Vorzeichen, `(int32_t)(x << 8) >> 8`. Daraus wird Build 3b (D29).

### D29 – Build 3b `v22.4.r-fx2b` geflasht, A1–A3, LED-Test mit Stream (2026-11-15)

**Build:**
- `firmware/builds/acdc1-build3b-fx2/` = `db9d3dd` + Libraries `9e8f64e` + 01, 02, 04, 05, 06, 03, 07 (v2)
- 106 332 B, SHA `cfa479f30c3bd71bd9ff5515f0208f59fcd0cf28dad0114d8dba2200a9f9cabb`
- Eine Build-Warnung, wie bei Build 2

**Flash** (Freigabe im Chat, Log `firmware/flashlog/20261115_build3b-fx2/`):
- `owl_read_before`: `v22.4.r-fx2`, letzte Meldung `rx unf 1.0000 0.2777 32.0000` (Stream-Ende beim Gerätewechsel in der Host-Software).
- `dfu-util -D` rc 0. Readback: Die ersten 106 332 B = `ACDC.bin`, der Rest 0xFF.

**A1 [gemessen]:**
- `v22.4.r-fx2b`, `SR/BS/CH 48000 8 4`, CPU 8 %
- Slots 1 „ACDC“ `0xbeb3bb2e`, 2 „[Lich]“ `0xeed65a68`, Storage 31 232 B
- `settings_cc`: CC 21/22/23 ±1 (Knob-Zittern), `bootloader_lock` 0 → 1 (Stack-Zufall, D11)
- **Bestanden.**

**A2/A3 kurz [gemessen, Nutzer]:** Ohne Stream folgen die Eingangs-LEDs dem Regler wie bisher. Bestanden.

**LED-Test mit Stream [gemessen, Nutzer, nach Augenschein]:**
- Die Regler ändern die Eingangs-LEDs nicht mehr, sie folgen dem rohen Eingang. Kein Dauer-Rot mehr. **Bestanden.**
- **Rot (Clip) nicht geprüft:** Es war kein Signal über Vollausschlag zur Hand. Über die Rückführung geht der Test nicht, weil die Schleife ≈ 0,3 dB verliert (A6-b1c: Spitze ≈ −0,3 dBFS bei Vollausschlag am DAC) und die Schwelle bei −0,1 dBFS liegt.

**Eingangsbereich (Frage des Nutzers: Ergibt Rot Sinn, wenn die Eingänge ±12 V vertragen?):**
- Spezifikation ±10 V [belegt].
- Aus dem Loop (D8/D15: ≈ 9,45 Vpp am Ausgang bei ≈ −6 dBFS) folgt ein Vollausschlag des Eingangs bei ≈ ±9,5 V [gemessen, indirekt].
- `AUDIO_INPUT_GAIN 88` setzt Register 88 (ADC-Dämpfung) auf 216. Nach dem PCM3168A-Datenblatt (aus dem Gedächtnis) wären das +0,5 dB digital [Hypothese].
- Signale zwischen ≈ 9,5 V und den Rails werden also abgeschnitten. Rot ist dafür sinnvoll.
- Für CV ist die Quadratmittel-Skala ungünstig: 1 V ≈ 1 %, 5 V ≈ 28 % Helligkeit. Rot ist reines GPIO ohne PWM (PC13/PI11 ohne Timer) [Code], taugt also nicht als Polaritätsanzeige mit Stärke. Beides kommt als Idee in `TODO.md`.

**Fork:** `acdc/fx1d` hat drei neue Commits, angelegt über einen temporären Worktree, **gepusht 2026-11-15** auf Wunsch des Nutzers:
- `f206fdd4` Code = Patch 07 v2. Der Code ist identisch mit dem Build-3b-Baum (`diff` der beiden Dateien leer).
- `6eee596c` Version `v22.4.r-fx2b`
- `b3bd3752` README: Abschnitt „Input LEDs“, Teststand ehrlich vermerkt (Clip und Rauschmessung mit fx2b offen)

**Entscheidung Nutzer (2026-11-15):** kein A6 (Patch 07 berührt weder USB-Timing noch Puffer), nur das A/B gegen B3 (D30).

### D30 – A/B Build 3b gegen B3: offene Eingänge, 2 × 60 s (2026-11-15)

**Setup:** wie D26 (B3), mit Build 3b `v22.4.r-fx2b`:
- Ein- und Ausgänge frei, Gain-Knobs 12 Uhr (ohne Wirkung auf die Aufnahme)
- Alltags-Kette, Host-Software „OWL-ACDC-FX“, Audio-Modul ohne Playback, Mehrkanal-Recorder
- r1 ≈ 17:42 (Host-Software frisch gestartet), r2 ≈ 17:43 (nach Neustart der Host-Software)
- Dateien `recordings/20261115_acdc1_fx2b-open-inputs-r{1,2}_g12_usb-stream.4chan.000.wav` (60,3 s / 59,8 s, keine Null-Samples)
- Manifest `B3-fx2b-r1/-r2`, Auswertung `out/B3-fx2b-r{1,2}/` (`--ref B3-fx1d-r{1,2}`)
- Kein Patch-Faktor nötig, beide Builds nehmen vor dem Patch auf. DC −6,12 gegen −6,06 % FS, also gleiche Verstärkung.

**Ergebnis [gemessen]** (Datei-dBFS, Mittel über die 4 Kanäle):

| Größe | B3 r1 | B3 r2 | 3b r1 | 3b r2 | 3b: r2 − r1 | **3b − B3** | je Kanal |
|---|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,64 | −72,62 | −71,88 | −71,85 | +0,03 | **+0,77** | +0,75 / +0,72 / +1,04 / +0,57 |
| A-bewertet | −73,79 | −73,79 | −72,94 | −72,91 | +0,03 | **+0,87** | |
| Rest ohne Störlinien | −78,09 | −78,10 | −78,32 | −78,30 | +0,03 | **−0,21** | −0,03 / −0,18 / −0,35 / −0,29 |
| fs/8-Linie 6000 Hz | −79,04 | −79,05 | −77,70 | −77,69 | +0,01 | **+1,35** | +1,39 / +1,35 / +1,35 / +1,31 |
| 1-kHz-Kamm (Summe) | −76,46 | −76,42 | −75,10 | −75,06 | +0,04 | **+1,36** | +1,35 / +1,28 / +1,84 / +0,97 |
| Mischprodukte (Summe) | −85,50 | −85,48 | −89,57 | −89,57 | +0,01 | **−4,08** | −4,12 / −4,10 / −4,07 / −4,03 |
| Störanteil | 70,8 % | 71,0 % | 76,5 % | 76,5 % | | +5,6 % | |
| Gewinn ideale Notch-Bank | 5,45 dB | 5,48 dB | 6,44 dB | 6,44 dB | | +0,98 | |

- Klicks 0, f0 Kamm 999,8675 Hz (B3 999,8673, gleicher Port), fs/8 6000,0000 Hz.
- r1 und r2 stimmen auf ≤ 0,04 dB überein.

**Bewertung:**
- Das Breitbandrauschen (Rest) ist gleich bzw. 0,2 dB besser.
- **fs/8 und Kamm liegen +1,35 dB höher**, auf allen Kanälen fast gleich. Die **Mischprodukte liegen −4,1 dB tiefer**, das macht die +4,8 dB von 1b → 1d (D19/D24) fast rückgängig. Insgesamt ist der RMS +0,8 dB.
- **Das Q9-Kriterium (> 0,5 dB schlechter in einer Familie) ist für fs/8 und Kamm erfüllt.**
- **[gemessen, D31]** Die Firmware ist die Ursache, die Kontrolle mit Build 2 trifft B3. Mechanismus [Hypothese]: Patch 07 rechnet im Audio-Task pro Block 32 Samples mehr, das verschiebt Zeitpunkt und Form der CPU-Last im Block. Die blocksynchrone fs/8-Linie und das Zusammenspiel mit dem SOF (Mischprodukte) hängen genau daran (H7, D24). Ein Sitzungseffekt war zunächst nicht ausgeschlossen (B3 ≈ 1,5 h früher, Ausreißer in D23). Deshalb die Kontrolle D31.

### D31 – Kontrolle: Build 2 zurück, 2 × 60 s in derselben Sitzung (2026-11-15)

**Flash** (Q9-Rückweg, Freigabe im Chat, Log `firmware/flashlog/20261115_build2-fx1d-kontrolle/`):
- `owl_read_before` (3b, Host-Software lief noch): `v22.4.r-fx2b`, CPU 15 % (mit Stream normal, Build 2 nach A6 ebenso), letzte Meldung **`fb clamp -50.0000 32.0000`**.
  - Zum ersten Mal überhaupt: Der Feedback-Regler stand an der Grenze, der RX-Puffer lag 50 Frames neben dem Sollwert. Der Zeitpunkt ist unbekannt.
  - **[Hypothese]** Einschwingen beim Stream-Start oder -Stopp (Neustart der Host-Software, Gerätewechsel). In B3-fx2b gab es 0 Klicks.
  - Offen: Patch 07 ändert am USB-Pfad nichts außer der Laufzeit in `usbd_tx_convert`.
- `dfu-util -D firmware/builds/acdc1-build2-fx1d/ACDC.bin` rc 0. Readback: Die ersten 105 968 B = `7f9f9a34…`, der Rest 0xFF.
- **A1 [gemessen]:** `v22.4.r-fx1d`, CPU 7 %, Slots und Storage gleich, `settings_cc` ohne jede Abweichung. Bestanden.

**Aufnahme:**
- Setup wie D30, r1 ≈ 17:49, r2 ≈ 17:51, Host-Software vor jedem Lauf neu gestartet
- Dateien `recordings/20261115_acdc1_fx1d-kontrolle-open-inputs-r{1,2}_g12_usb-stream.4chan.000.wav` (60,3 s, keine Null-Zeilen)
- Manifest `B3-fx1d-k-r1/-r2`, Auswertung `out/B3-fx1d-k-r{1,2}/`
- Meldung danach, Host-Software noch offen: `tx ovf 0.4652 1.0000 32.0000` (Stream-Ende beim Neustart der Host-Software, wie D25)

**Ergebnis [gemessen]** (Datei-dBFS, Mittel über 4 Kanäle und beide Läufe):

| Größe | B3 (Build 2, 16:18) | 3b (17:42) | **Kontrolle Build 2 (17:50)** | Kontrolle − B3 | **3b − Kontrolle** |
|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,63 | −71,86 | −72,64 | −0,01 | **+0,78** |
| A-bewertet | −73,79 | −72,92 | −73,82 | −0,03 | **+0,90** |
| Rest ohne Störlinien | −78,10 | −78,31 | −77,90 | +0,19 | **−0,40** |
| fs/8-Linie 6000 Hz | −79,05 | −77,70 | −79,10 | −0,06 | **+1,40** |
| 1-kHz-Kamm | −76,44 | −75,08 | −76,57 | −0,13 | **+1,49** |
| Mischprodukte | −85,49 | −89,57 | −85,54 | −0,05 | **−4,03** |
| Störanteil | 70,9 % | 76,5 % | 69,5 % | | +6,9 % |
| Gewinn Notch-Bank | 5,47 dB | 6,44 dB | 5,26 dB | | +1,18 |

- Je Kanal 3b − Kontrolle: fs/8 +1,42 / +1,41 / +1,39 / +1,39, Kamm +1,43 / +1,50 / +1,97 / +1,07, Mischprodukte −4,06 / −4,05 / −4,03 / −3,99, Rest −0,28 / −0,36 / −0,61 / −0,37 dB.
- Kontrolle r2 − r1 ≤ 0,16 dB, f0 Kamm 999,8672 Hz, Klicks 0.

**Bewertung:**
- **Die Kontrolle trifft B3 auf ≤ 0,2 dB.** Ein Sitzungseffekt ist damit ausgeschlossen. **Die Verschiebung in D30 kommt von Patch 07 [gemessen].**
- Die 32 zusätzlichen Multiply-Adds und Vergleiche pro Block im Audio-Task heben fs/8 und Kamm um ≈ 1,4 dB, senken die Mischprodukte um 4 dB und das Breitbandrauschen um 0,4 dB.
- **H7 gestützt:** Lage und Form der CPU-Last im Block wirken auf die blocksynchronen Störer, schon bei sehr kleinen Änderungen. Die Wirkung ist nicht monoton. Das ist ein Hebel für die Rausch-Experimente (E3): Die Last im Block ließe sich gezielt verteilen.
- **Q9 erfüllt:** **Build 2 bleibt auf acdc1.** Build 3b ist im Fork-Branch, aber nicht im Alltag.

### D32 – Build 3c `v22.4.r-fx2c` (LED-Messung in `onLoop`): geflasht, A1, A/B gegen die Kontrolle (2026-11-15)

**Build:**
- `firmware/builds/acdc1-build3c-fx2/` = `db9d3dd` + Libraries `9e8f64e` + 01, 02, 04, 05, 06, 03, **07c**
- 106 304 B, SHA `f354239dd305f2417b9ca3d5c9f403aff2890c0c66c8bf117c57643663df7364`
- Patch 07c ändert **nur `ACDC.cpp`**: `onLoop` misst alle 2 ms die 64 Samples des Codec-DMA-Eingangspuffers, τ 40 ms. `ProgramManager.cpp` (Audio-Pfad) ist bitgleich mit Build 2.
- **Lage im Flash [Code: `nm`]:** Die Audio-Funktionen (`audioCallback`, `onProgramReady`, `usbd_tx_convert`, `usbd_rx_convert`, SAI-Callbacks) sind gleich groß wie in Build 2, liegen aber **0x150 B weiter hinten**, weil `onLoop` von 0x1d0 auf 0x320 B gewachsen ist. Bei 3b waren die SAI-Callbacks −0x3C und `audioCallback` +0x16C verschoben.

**Flash** (Freigabe im Chat, Log `firmware/flashlog/20261115_build3c-fx2/`):
- `owl_read_before` (Build 2, Host-Software lief): `fb 48.0003 96.2500` (ein verspäteter SOF wie in D27), kein `fb clamp`.
- `dfu-util -D` rc 0. Readback: Die ersten 106 304 B = `ACDC.bin`, der Rest 0xFF.
- **A1 [gemessen]:** `v22.4.r-fx2c`, CPU 7 %, Slots und Storage gleich, CC 21/22 ±1. Bestanden.

**LEDs [gemessen, Nutzer]:** ohne Stream folgen sie dem Regler, mit Stream dem rohen Eingang, die Regler wirken nicht. Bestanden.

**A/B [gemessen]:**
- Setup wie D30/D31, r1 ≈ 18:05, r2 ≈ 18:07, Host-Software vor jedem Lauf neu gestartet
- Dateien `recordings/20261115_acdc1_fx2c-open-inputs-r{1,2}_g12_usb-stream.4chan.000.wav` (60,3 s, keine Null-Zeilen)
- Manifest `B3-fx2c-r1/-r2`, Auswertung `out/B3-fx2c-r{1,2}/` (`--ref B3-fx1d-k-r{1,2}`)
- Meldung danach: `tx ovf 0.4861 1.0000 32.0000` (Stream-Ende), CPU 12 %

Datei-dBFS, Mittel über 4 Kanäle und beide Läufe:

| Größe | Kontrolle Build 2 (D31) | 3b (D30) | **3c** | 3c: r2 − r1 | **3c − Kontrolle** | 3b − Kontrolle |
|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,64 | −71,86 | −71,66 | +0,08 | **+0,98** | +0,78 |
| A-bewertet | −73,82 | −72,92 | −72,72 | +0,10 | **+1,10** | +0,90 |
| Rest ohne Störlinien | −77,90 | −78,31 | −78,08 | 0,00 | **−0,18** | −0,40 |
| fs/8-Linie 6000 Hz | −79,10 | −77,70 | −77,14 | +0,02 | **+1,96** | +1,40 |
| 1-kHz-Kamm | −76,57 | −75,08 | −75,07 | +0,16 | **+1,51** | +1,49 |
| Mischprodukte | −85,54 | −89,57 | −89,89 | −0,01 | **−4,36** | −4,03 |
| Störanteil | 69,5 % | 76,5 % | 76,5 % | | +6,9 % | +6,9 % |

- Je Kanal 3c − Kontrolle: fs/8 +1,98 / +1,97 / +1,95 / +1,95, Kamm +1,38 / +1,61 / +1,85 / +1,18, Mischprodukte −4,37 / −4,36 / −4,36 / −4,34 dB.
- **Keine neue 500-Hz-Familie** (Tick-Rate von `onLoop`): Bei 250/500/750/1500/2500/3500/4500 Hz liegt 3c innerhalb −1,3…+0,7 dB der Kontrolle (Welch, Kanal 1, r1).

**Bewertung:**
- **Q9 erfüllt, 3c nicht bestanden:** fs/8 +2,0 dB, Kamm +1,5 dB. Das Muster ist dasselbe wie bei 3b, bei fs/8 sogar stärker.
- **Die Hypothese „mehr Arbeit im Audio-Pfad“ (D31) ist damit widerlegt [gemessen]:** 3c hat im Audio-Pfad keinen einzigen zusätzlichen Befehl, und die Messung in `onLoop` ist rund 6-mal kleiner und nicht blocksynchron. Trotzdem verschieben sich die Linien gleich.
- **Neuer Verdacht [Hypothese]:** Die **Lage des Codes im Flash** (Adressen und Ausrichtung der Audio-Funktionen, Flash-Wartezyklen, Cache-Zeilen) bestimmt das Zeitmuster der CPU im Block mit. 3b und 3c haben gemeinsam, dass sich die Audio-Funktionen um 0x150–0x16C B verschoben haben.
- Möglich bleibt auch: Irgendein anderer Unterschied zur Laufzeit, den beide Builds teilen. Die LED-PWM-Werte sind es eher nicht, denn offene Eingänge geben in beiden Fällen ≈ 0. [Hypothese]
- **Test dafür:** Build 2 + reine Füllbytes in `ACDC.cpp` (ungenutzte Funktion mit `used`, Audio-Funktionen um ≈ 0x150 B verschoben), sonst nichts ändern. Verschieben sich die Linien wie bei 3b/3c, ist es die Lage.

### D33 – Füllbyte-Test `v22.4.r-fx1p`: Die Lage im Speicher verschiebt die Störlinien (2026-11-15)

**Frage (aus D32):** Verschiebt allein die andere Lage des Codes und der Variablen die Störlinien, ohne jede Funktionsänderung?

**Build:**
- `firmware/builds/acdc1-build2p-layout/` = Build 2 + `firmware/patches/90-layout-pad-like-3c.patch`
- 106 304 B (wie 3c), SHA `cbf45166672a02337d45b9514096dd63ab28a7ba7b23baa1d287d91bb08521f9`
- Version `v22.4.r-fx1p`, gleich lang wie `fx1d`, damit `.rodata` nicht wandert
- Der Patch hängt an das Ende von `ACDC.cpp`:
  - eine nie aufgerufene `naked`-Funktion mit `.space 0x150`, in der Input-Section `.text.onLoop`
  - ein Feld von 0x28 B in `.bss.fast_log_table_size`
  - So bleibt beides trotz `--gc-sections` erhalten. Der erste Versuch ohne geteilte Section wurde komplett entfernt (Binary = Build 2).
- **Prüfung [Code: `nm`]:** Von 957 Symbolen, die Build 2, 3c und fx1p gemeinsam haben, liegen 955 an genau derselben Adresse wie in 3c. Die zwei Ausnahmen sind `fast_pow/log_table_size`, die zwei selten genutzten Zähler der Tabellen.

**Flash** (Freigabe im Chat: „mache den Füllbyte-Test“, Log `firmware/flashlog/20261115_build2p-layout/`):
- vorher 3c, `rx unf 1.0000 0.2708 32.0000` (Stream-Ende)
- Readback = `ACDC.bin`, der Rest 0xFF
- **A1:** `v22.4.r-fx1p`, CPU 8 %, Slots und Storage gleich, CC 20/23 ±1. Bestanden.

**Aufnahme:**
- Setup wie D30–D32, r1 ≈ 18:15, r2 ≈ 18:17
- Dateien `recordings/20261115_acdc1_fx1p-open-inputs-r{1,2}_g12_usb-stream.4chan.000.wav` (60,4 s / 60,5 s, keine Null-Zeilen)
- Manifest `B3-fx1p-r1/-r2`, Auswertung `out/B3-fx1p-r{1,2}/`
- Meldung danach `tx ovf 1.0000 1.0000 32.0000` (Stream-Ende)

**Ergebnis [gemessen]** (Datei-dBFS, Mittel über 4 Kanäle und beide Läufe):

| Größe | Kontrolle Build 2 | 3c | **fx1p (nur Füllbytes)** | fx1p: r2 − r1 | **fx1p − Kontrolle** | 3c − Kontrolle | **3c − fx1p** |
|---|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,64 | −71,66 | −71,74 | +0,03 | +0,91 | +0,98 | **+0,07** |
| A-bewertet | −73,82 | −72,72 | −72,80 | +0,03 | +1,03 | +1,10 | **+0,07** |
| Rest ohne Störlinien | −77,90 | −78,08 | −78,18 | −0,23 | −0,28 | −0,18 | **+0,10** |
| fs/8-Linie | −79,10 | −77,14 | −77,26 | +0,03 | **+1,84** | +1,96 | **+0,12** |
| 1-kHz-Kamm | −76,57 | −75,07 | −75,11 | +0,15 | **+1,47** | +1,51 | **+0,04** |
| Mischprodukte | −85,54 | −89,89 | −90,00 | +0,06 | **−4,46** | −4,36 | **+0,11** |

- Je Kanal fx1p − Kontrolle: fs/8 +1,85 / +1,85 / +1,83 / +1,83, Kamm +1,35 / +1,49 / +1,83 / +1,20, Mischprodukte −4,47 / −4,46 / −4,48 / −4,43 dB.

**Bewertung:**
- **Die Füllbytes allein reproduzieren 3c auf ≤ 0,12 dB [gemessen].** Die Verschiebung von fs/8, Kamm und Mischprodukten kommt also von der **Lage von Code und Daten im Speicher**, nicht von der LED-Messung.
- Die LED-Funktion von 3c kostet zusätzlich praktisch nichts (≤ 0,12 dB).
- **Folgerung für D31:** Die „Mehrarbeit pro Block“ war nicht die Ursache. Auch 3b hat die Audio-Funktionen verschoben (−0x3C bis +0x16C B).
- **Mechanismus [Hypothese]:** Das Zeitmuster der CPU im Audioblock hängt von der Ausrichtung des Codes ab (Flash-Wartezyklen, Prefetch, I-Cache-Zeilen, Bank-Konflikte im RAM). Über Versorgung und Masse wirkt es auf ADC-Daten und SOF-Verkopplung.
- **Folgen:**
  - Jede Firmware-Änderung kann die Störlinien um ±2 dB (fs/8) bzw. ±4,5 dB (Mischprodukte) verschieben, auch wenn sie nur Code außerhalb des Audio-Pfads betrifft. A/B-Vergleiche zwischen Builds messen also immer den Code **und** die Lage im Speicher. Das betrifft auch die +4,8 dB von 1b → 1d (D24).
  - Ein neuer Hebel für E3: Die Lage gezielt wählen, also Füllbytes durchprobieren, und schauen, ob eine Lage besser ist als die von Build 2.
  - LEDs ohne Linienverschiebung: Den LED-Code so platzieren, dass alle anderen Adressen gleich Build 2 bleiben (Build 3d).

### D34 – Build 3d `v22.4.r-fx2d` (LED-Code am Ende des Speichers): geflasht, A1, A/B (2026-11-15)

**Build:**
- `firmware/builds/acdc1-build3d-fx2/` = Build 2 + `firmware/patches/07d-input-leds-raw-late-section.patch`
- 106 788 B, SHA `d212cf8def6f239db997cd45a73304db9bcaf981375e55fdfc2ca2862718832a`
- **Funktion:** wie 3c, Messung in `onLoop` auf dem DMA-Puffer, τ 40 ms, Rot 300 ms ab −0,1 dBFS.
- **Platzierung:**
  - Die neue Logik liegt in `.late_text` hinter dem `.data`-Ladeabbild am Ende des Flash (0x334 B).
  - Der Zustand liegt in `.late_bss` (0x2c B) in den obersten 64 B von RAM_D2 (`_HEAP_D2_END` −64). Er wird beim Booten nicht genullt, deshalb gibt es eine Magic-Prüfung.
  - `onLoop` = `b.w` + Füllbytes auf die alte Größe 0x1d0.
  - Dazu ein Patch für `Hardware/xibeca.ld`.
- **Prüfung [Code]:** In den ersten 105 968 B ist das Binary **bytegleich mit Build 2**, bis auf drei Stellen:
  - `onLoop` (464 B)
  - Literal `_HEAP_D2_SIZE` (0x26000 → 0x25fc0)
  - ein Zeichen der Version

  Alle 957 gemeinsamen Symbole liegen an derselben Adresse.

**Flash** (Freigabe im Chat, Log `firmware/flashlog/20261115_build3d-fx2/`):
- vorher fx1p, `fb 48.0006 96.2500` (ein verspäteter SOF), CPU 20 % mit Stream
- Readback = `ACDC.bin`, der Rest 0xFF
- **A1:** `v22.4.r-fx2d`, CPU 8 %, Slots und Storage gleich, CC ±1. Bestanden.
- **LEDs [Nutzer]:** „passen soweit“, mit und ohne Stream. Bestanden.

**Aufnahme:**
- r1 ≈ 18:27, r2 ≈ 18:29, Host-Software vor jedem Lauf neu gestartet
- Dateien `recordings/20261115_acdc1_fx2d-open-inputs-r{1,2}_g12_usb-stream.4chan.000.wav` (60,3 s / 63,0 s, keine Null-Zeilen)
- Manifest `B3-fx2d-r1/-r2`, Auswertung `out/B3-fx2d-r{1,2}/`
- Meldung danach: `fb 48.0004 96.2500`

**Ergebnis [gemessen]** (Datei-dBFS, Mittel über 4 Kanäle und beide Läufe):

| Größe | B3 (Build 2, 16:18) | Kontrolle Build 2 (17:50) | fx1p (Füllbytes) | **3d** | 3d: r2 − r1 | **3d − Kontrolle** | 3d − B3 |
|---|---|---|---|---|---|---|---|
| RMS ≥ 20 Hz | −72,63 | −72,64 | −71,74 | −72,46 | +0,09 | **+0,19** | +0,17 |
| A-bewertet | −73,79 | −73,82 | −72,80 | −73,52 | +0,14 | +0,30 | +0,27 |
| Rest ohne Störlinien | −78,10 | −77,90 | −78,18 | −78,08 | −0,09 | −0,18 | +0,02 |
| fs/8-Linie | −79,05 | −79,10 | −77,26 | −79,05 | +0,01 | **+0,05** | −0,01 |
| 1-kHz-Kamm | −76,44 | −76,57 | −75,11 | −76,02 | +0,26 | **+0,55** | +0,42 |
| Mischprodukte | −85,49 | −85,54 | −90,00 | −85,51 | −0,01 | **+0,03** | −0,02 |

- Kamm je Lauf (Mittel 4 Kanäle):
  - Build 2: −76,46 / −76,42 (B3), −76,65 / −76,49 (Kontrolle)
  - 3d: −76,15 / −75,89

  Je Kanal 3d − Kontrolle: +0,55 / +0,42 / +0,85 / +0,38 dB.
- f0 Kamm 999,8676 Hz, fs/8 6000,0000 Hz.

**Bewertung:**
- **Die Lageverschiebung ist beseitigt [gemessen]:** fs/8 und Mischprodukte sind auf ≤ 0,05 dB gleich Build 2. Die ±2/±4,5 dB von 3b/3c/fx1p sind weg. Das bestätigt D33 von der anderen Seite.
- **Kamm +0,4…+0,55 dB, an der Schwelle von Q9 (0,5 dB):**
  - Innerhalb von 3d steigt er von r1 auf r2 um 0,26 dB. Das ist mehr als die Streuung der Build-2-Läufe (Spanne 0,23 dB über vier Läufe und zwei Sitzungen).
  - **[Hypothese]** Entweder Sitzungsdrift des SOF-Kamms (der Kamm hängt am Host und am Hub, D23, S2-6) oder ein kleiner echter Effekt von 07d. Für Letzteres käme der Lesezugriff von `onLoop` auf den DMA-Puffer in D2 in Frage, also Buskonkurrenz mit der SAI-DMA, oder der neue Code am Flash-Ende.
- Klärung: eine Kontrolle mit Build 2 in derselben Sitzung (wie D31).

**Entscheidung Nutzer (2026-11-15): Build 3d bleibt auf acdc1** trotz Kamm +0,4…0,55 dB, ohne weitere Kontrolle. Der Kamm bleibt beim nächsten Rausch-Experiment im Blick, Build 2 ist der Rückweg.

**Fork:** `acdc/fx1d` + `8da4eb7b` (README A/B fx2b), `6d3b8bd5` (07d: LEDs ohne Lageänderung, setzt ProgramManager.cpp auf fx1d zurück), `cc2e08f8` (Version `v22.4.r-fx2d`), `abc3a72a` (README: fx2d, Abschnitt „Memory layout matters“). Die drei Dateien im Branch sind identisch mit dem Build-3d-Baum (`cmp`). Gepusht 2026-11-15 (Freigabe im Chat).

### D35 – Gegenprobe Aufnahme-Werkzeug: `tools/acdc_rec.py` gegen Host-Software mit Mehrkanal-Recorder (2026-11-16)

**Setup:** acdc1 mit Build 3d `v22.4.r-fx2d`, Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub), Eingänge offen, Gain 12 Uhr, Slot 1 ACDC.
- `X1-vcv`: Host-Software, Audio-Modul auf OWL-ACDC-FX (48 kHz, Block 256, ohne Playback-Kabel), Mehrkanal-Recorder, 60 s, ≈ 16:28. Danach Host-Software beendet.
- `X1-rec`: `tools/acdc_rec.py` (duplex, Ausgang Nullen, Block 256, 16 Bit PCM, 3 s verworfen, `scale = 2.0`), 60 s, direkt danach, mit `--owl-read` (Report `out/owl_read/X1-rec/`). 0 Stream-Meldungen.
- Vorher ein 10-s-Probelauf mit dem Skript (nur Scratchpad, ohne Manifest): fs/8 bei 6000,0000 Hz, Kamm bei 999,862 Hz.

**Ergebnis** (Mittel über 4 Kanäle in Leistung, Datei-dBFS wie die Aufnahmen aus der Host-Software; Auswertung `out/X1-vcv/`, `out/X1-rec/`):

| Größe | X1-vcv | X1-rec | Δ |
|---|---|---|---|
| RMS ≥ 20 Hz | −73,41 | −73,21 | +0,20 |
| Rest ohne Störlinien | −77,23 | −77,03 | +0,20 |
| Kamm (SOF) | −79,24 | −78,81 | +0,43 |
| fs/8 | −79,28 | −79,27 | +0,01 |
| Mischprodukte | −85,55 | −85,55 | ±0,00 |

- Kamm-f0: 999,8658 Hz (Host-Software) gegen 999,8666 Hz (Skript), also SOF-Drift zwischen den Läufen.
- Im Skript-Lauf findet die Analyse auf Kanal 2–4 eine winzige LED-Linie bei 2320,545 Hz (Anteil ≈ 0 %).

**Deutung:** [gemessen] Beide Werkzeuge liefern dieselben Daten. fs/8 und Mischprodukte stimmen auf ≤ 0,01 dB, Breitband +0,2 dB. Der Kamm liegt +0,43 dB höher, knapp unter der Schwelle von 0,5 dB. Das passt zur bekannten Kamm-Streuung zwischen Läufen (D34: +0,4…0,55 dB) und zur SOF-Drift. Kriterium Q14 (≤ 0,5 dB) erfüllt. **`tools/acdc_rec.py` ersetzt ab jetzt die Host-Software mit Mehrkanal-Recorder für Aufnahmen.** Weil der Kamm zwischen Läufen ≈ 0,4 dB streut, bleibt für Kamm-Aussagen die Wiederholung (2 × 60 s) Pflicht.

### D36 – Build-4-Sitzung: Clip-Test 3d (Q5) mit Loop Out → In (2026-11-16)

**Setup:** acdc1 mit Build 3d `v22.4.r-fx2d`, Alltags-Kette, Gain 12 Uhr. Aufnahmen mit `tools/acdc_rec.py`, Rohpegel in Geräte-dBFS (16-Bit-Datei = Gerätewerte). Clip-Schwelle in 07d: |s| ≥ 8 293 000 / 8 388 607 = 0,98855 FS (−0,1 dBFS). Der Nutzer beobachtet die LEDs.
- `B4-clip3d` (90 s): Sinus-Oszillator von Hand an In 1…4. Spitze nur −10,6 bis −11,0 dBFS (≈ 2,7 V), kein Rot möglich. Ein Signal über 9,5 V hatte der Nutzer nicht.
- `B4-clip3d-sine` (30 s): Patchkabel Out n → In n, Sinus 440 Hz mit −3 / −1 / −0,3 / 0 dBFS (neu: Testsignale aus dem Skript).
- `B4-clip3d-dc` (40 s): Out n → In n, Gleichanteil +1,0 / −0,94 / −0,97 / −1,0 FS, 20 s Rampe, dann stehend (neu: `--dc`, `--dc-ramp`).

**Ergebnis:**

| Eingang | Sinus: Spitze am Eingang | LED | DC stehend am Eingang | Schwelle ab | LED |
|---|---|---|---|---|---|
| In 1 | −2,67 dBFS | kein Rot | +0,956 | nie | kein Rot |
| In 2 | −0,69 dBFS | kein Rot | −0,972 | nie | kein Rot |
| In 3 | −0,12 dBFS (neg. Spitze −0,9867) | kein Rot | −0,990 | 20,2 s | **Rot** |
| In 4 | 0,00 dBFS (86 745 Samples an −FS) | **Rot** | −1,000 | 19,4 s | **Rot** |

- Kennlinie Out → In (DC-Rampe): Verstärkung 0,991–0,994, Offset je Kanal −0,043 / −0,027 / −0,016 / −0,022 FS (≈ −0,2…−0,4 V). Wegen des negativen Offsets erreicht +1,0 FS am Ausgang den Eingang nur mit +0,956, positive Clips sind über den Loop nicht auslösbar.
- Stehende Gleichspannung: Rauschen ≈ 0,2 mFS, In 4 am Anschlag fast still (0,015 mFS).

**Deutung:** [gemessen] Das Clip-Rot von 07d sitzt genau an der Schwelle −0,1 dBFS: In 3 lag 0,02 dB darunter und blieb dunkel, alles an oder über der Schwelle wurde rot. Damit ist der offene Punkt „Clip-Rot ungeprüft“ von Build 3d erledigt. Nebenbefund: Eingangsoffset ≈ −0,2…−0,4 V je Kanal.

### D37 – Build-4-Sitzung: 3d-Kontrolle, fx3i (ITCM), 3d-Endkontrolle, offene Eingänge (2026-11-16)

**Setup:** acdc1, Alltags-Kette, Eingänge offen, Gain 12 Uhr, Slot 1 ACDC, je 2 × 60 s mit `tools/acdc_rec.py` (Stream zwischen den Läufen neu geöffnet, `--owl-read`). Reihenfolge: `B4-3d` (3d) → Flash fx3i (`firmware/flashlog/20261116_build4-fx3i/`, Readback bytegleich `8fedebf7…`) → A1 → `B4-fx3i` → Loop-Test (D38) → Flash 3d zurück (`firmware/flashlog/20261116_build3d-fx2-zurueck/`, Readback bytegleich `d212cf8d…`) → Loop-Test → `B4-3d-end`. **fx3ip wurde nicht gemessen** (wegen D38). Tabelle: `out/B4-session-table.md` (`tools/family_table.py`).
- A1 fx3i: `AC/DC v22.4.r-fx3i`, `SR/BS/CH 48000 8 4`, Patches und Settings unverändert.

**Ergebnis** (Datei-dBFS, Mittel über 4 Kanäle in Leistung; Δ gegen das Mittel der beiden 3d-Kontrollen):

| Messung | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| B4-3d (Start) | −72,33 (−0,27) | −77,59 (−0,16) | −75,91 (−0,33) | −79,03 (−0,28) | −85,50 (−0,30) |
| **B4-fx3i** | −73,04 (**−0,98**) | −78,31 (**−0,89**) | −75,57 (+0,01) | **−83,82 (−5,06)** | −85,73 (−0,54) |
| B4-3d-end | −71,81 (+0,25) | −77,27 (+0,16) | −75,28 (+0,30) | −78,50 (+0,26) | −84,91 (+0,28) |

- r1/r2 je Build ≤ 0,2 dB (fs/8 von fx3i: −84,00 / −83,65). Kamm-f0 999,8677 Hz in allen Läufen.
- 3d driftet über die Sitzung (≈ 70 min) gleichmäßig um +0,5…0,6 dB in allen Familien.
- Gegenüber der Gegenprobe X1-rec (D35, 16:31) lag schon die Start-Kontrolle beim Kamm +2,9 dB höher, f0 999,8666 → 999,8677 Hz. Laut Nutzer blieb der Hardware-Aufbau gleich, am Mac kam aber zwischenzeitlich CPU-Last hinzu. [Hypothese] Host-Last ändert Masse-/Schirmstrom und Host-Takt (f0 +1,1 ppm). A/B Leerlauf gegen Last steht in der TODO.
- CPU-Anzeige mit Stream: 3d 15–16 %, fx3i 7 % (ohne Stream 3d 8 %, fx3i 6 %).
- Gerätemeldung nach jedem fx3i-Lauf `fb clamp −195 / −127 32`, bei 3d nie (nur `tx ovf …` bzw. `fb 48.0003 96.25`).

**Deutung:**
- [gemessen] **fs/8 ist mit dem heißen Pfad im ITCM ≈ 5 dB leiser**, Breitband und Rest ≈ 0,9–1,0 dB, Mischprodukte −0,5 dB, Kamm unverändert. Kriterium Q2 (a) „nicht schlechter als 3d“ ist erfüllt, der fs/8-Effekt ist der größte aller bisherigen Builds und liegt weit über Drift und Streuung.
- [Hypothese] Die halbe CPU-Last passt zur These, dass Flash-Zugriffe (Cache-Fehlgriffe in den ISRs) Last und Stromprofil im Blocktakt prägen. Belegt ist das nicht, und fx3i hat einen Fehler im Playback-Pfad (D38), der die Last ebenfalls verändern kann.
- Die Lagen-Unabhängigkeit (Q2 b, fx3ip) ist **nicht geprüft**.

### D38 – fx3i: USB-Playback gestört, Loop-Test gegen 3d (2026-11-16)

**Setup:** Patchkabel Out n → In n, `tools/acdc_rec.py --sine 440 530 670 790` (−6 dBFS, 1 s Einblenden), 60 s, danach `tools/phase_slips.py`. `B4-fx3i-loop` mit fx3i, `B4-3d-loop` mit 3d direkt nach dem Zurückflashen, gleicher Aufbau.

**Ergebnis:**

| | 3d (`B4-3d-loop`) | fx3i (`B4-fx3i-loop`) |
|---|---|---|
| Slips (alle 4 Kanäle gleichzeitig) | **0** | **28** in 60 s, alle negativ, 1–22 Samples |
| Phasenrauschen (MAD) | 0,00–0,01 mrad | 0,31–1,04 mrad |
| Amplituden-Spanne 0,1–99,9 % | 0,00 dB | 0,36–1,00 dB, Kanal 4 −1,1 dB zu leise |
| Gerätemeldung | `fb 48.0004 96.2578` | `fb clamp −208 32` |
| CPU mit Stream | 15 % | 8 % |

- An den Störstellen ist das Signal über bis zu 2 600 Samples (≈ 54 ms) zerstört (z. B. …430, 23, 403, 458, 425…), das sieht nach vermischten oder veralteten Samples aus.
- `fb clamp −195…−208`: Der RX-Füllstand nach dem Paket liegt im Mittel ≈ 190 Samples unter dem Sollwert 384, also eine OUT-Paketlänge (192 Samples = 1 ms) zu leer. Der Regler (Patch 06, max. ±32 LSB ≈ 40 ppm) kann das nicht ausgleichen, der Puffer läuft bei jedem Zittern leer.

**Deutung:** [gemessen] Der Fehler liegt in fx3i, nicht im Aufbau: 3d ist im selben Aufbau sauber. Code und RAM-Adressen sind bis auf Lage, Veneers und Startup gleich wie in 3d (`check_itcm.md`), es ist also ein Timing- oder Platzierungs-Effekt. [Hypothese] Verlorene ISO-OUT-Pakete oder ein Wettlauf zwischen USB-ISR (schreibt `rx_buffer`, misst den Füllstand gegen den Codec-DMA-Zähler) und Audio-Task (liest `rx_buffer`). Die Parität gerade/ungerade beim Neu-Aufsetzen des ISO-OUT-Endpunkts (`USB_EPStartXfer`) passt nur, wenn der Code später statt früher dran ist. Nächster Schritt: Halbieren, fx3i-Varianten ohne Gruppe D (USB) bzw. ohne C (Audio-Task) im ITCM, je Loop-Test 60 s. fx3i bleibt nicht auf acdc1, **3d läuft wieder** (A1 bestanden).

**Nachtrag (D39/D40):** Die Halbierung zeigt zwei getrennte Fehler. Die Slips und `fb clamp` kommen von Gruppe D (USB) im ITCM. „Kanal 4 −1,1 dB“ ist ein veralteter letzter Eingangs-Sample pro Block (16 Frames alt), ausgelöst durch Gruppe C (Audio-Task) im ITCM.

### D39 – Build 4x: fx3i-Varianten (Halbierung), Loop-Test je Variante (2026-11-16, abends)

**Setup:** acdc1, Alltags-Kette, Gain 12 Uhr, Patchkabel Out n → In n, je 60 s `tools/acdc_rec.py --sine 440 530 670 790` (−6 dBFS, 1 s Einblenden, `--owl-read`), danach `tools/phase_slips.py` und neu `tools/stale_samples.py` (einzelne falsche Samples, JSON in `out/B4x/`). Varianten: `docs/05` „Build 4x“, Patches 11a–11c, alle mit `check_itcm.py --groups …` geprüft. Jeder Flash einzeln freigegeben, Readback jeweils bytegleich, A1 jeweils bestanden (Version, `SR/BS/CH 48000 8 4`, Slots ACDC/ACDC/[Lich]). Flashlogs `firmware/flashlog/20261116_build4x-{noD,noC,onlyD}/`, `…_build3d-fx2-zurueck-4x/`. Reihenfolge: 3d-Kontrolle → noD → noC → onlyD → 3d zurück → 3d-Endkontrolle. fx3i-novt wurde gebaut, aber nicht geflasht (H-e durch noD erledigt).

**Ergebnis:**

| Messung | ITCM-Gruppen | Slips (alle Kanäle gleichzeitig) | MAD | Kanal 4 Amplitude | veraltete Samples Kanal 4 | Meldung nach dem Lauf | CPU mit Stream |
|---|---|---|---|---|---|---|---|
| `B4x-3d-loop` (3d) | – | 0 | 0,00–0,01 mrad | −6,07 dBFS | 0 | `tx ovf …` | 15 % |
| `B4x-noD-loop` | A B C E F G H L | **0** | 0,00–0,01 mrad (K4 0,04) | **−7,17 dBFS** | **94 % der Blöcke** | `tx ovf …` | 8 % |
| `B4x-noC-loop` | A B D E F G H L | **16**, alle negativ, 5–24 Samples | 12–22 mrad | −6,06 dBFS | 0 | `fb clamp −96 32` | 12 % |
| `B4x-onlyD-loop` | D L | **8**, alle negativ, 1–23 Samples | 5–9 mrad | −6,06 dBFS | 0 | `fb 48.0019 25.5000` | 14 % |
| `B4x-3d-end-loop` (3d) | – | 0 | 0,00–0,02 mrad | −6,06 dBFS | 0 | `tx ovf …` | 15 % |
| zum Vergleich `B4-fx3i-loop` (D38) | alle | 28 | 0,31–1,04 mrad | −7,21 dBFS | 96 % (nachträglich, D40) | `fb clamp −208 32` | 8 % |

- CPU ohne Stream nach dem Flash: noD 6 %, noC 6 %, onlyD 7 %, 3d 7 %.
- In noD erzeugt der veraltete Sample auf Kanal 4 in `phase_slips.py` 130 kleine Phasensprünge von ±0,25 Samples. Das sind keine Slips, nur ein Folgeeffekt.

**Deutung:** [gemessen] **fx3i hat zwei getrennte Fehler.**
1. **USB-Playback (Slips, `fb clamp`):** Er tritt genau dann auf, wenn Gruppe D (USB-OTG-ISR, HAL_PCD/LL_USB, USBD-Kern, Audio-Klasse, Feedback) im ITCM liegt. D allein reicht dafür (onlyD), ohne D ist der Fehler weg (noD). Andere Gruppen und die Vektorkopie sind nicht nötig, H-e ist widerlegt (noD hat die Vektorkopie und läuft sauber). Der Mechanismus innerhalb von D ist offen, [Hypothese] H-a (verlorene ISO-OUT-Pakete beim Neu-Aufsetzen des Endpunkts) bleibt der Hauptverdacht. Die Stärke schwankt (fx3i 28, noC 16, onlyD 8 Slips/60 s).
2. **Veralteter letzter Eingangs-Sample auf Kanal 4:** Er tritt auf, wenn Gruppe C (Audio-Task) im ITCM liegt (fx3i, noD), sonst nicht (noC, onlyD, 3d). Mechanismus siehe D40.
- Der USB-Fehler ist unabhängig vom Kanal-4-Fehler: In noC ist Kanal 4 sauber, aber USB gestört.
- [Hypothese] Die Meldung `fb 48.0019 25.5000` bei onlyD (gezählte Samples pro Feedback-Periode ≈ halb so viele wie erwartet) passt zu einem Fehler im Zusammenspiel von SOF-Takt und Codec-Zähler und sollte im Diagnose-Build mitgezählt werden.

### D40 – Kanal 4: der letzte Sample jedes Blocks ist 16 Frames alt (Auswertung D38/D39, 2026-11-16)

**Methode:** `tools/stale_samples.py` (neu) passt je Kanal einen Sinus samt Gleichanteil robust an (2 s ab 3 s) und markiert Samples mit |Rest| > 8 × Median. Dann zählt es die Lage im 8-Frame-Raster und sucht den Abstand, der die falschen Werte am besten erklärt (Wert ≈ Modell[n + lag]).

**Ergebnis:**
- fx3i (`B4-fx3i-loop`) und noD (`B4x-noD-loop`): Auf Kanal 4 ist in **94–96 % der 8-Frame-Blöcke genau ein Sample** falsch, immer an derselben Rasterstelle. Sein Wert ist der Wert von **n − 16 Frames**: mittlerer Fehler 0,0009–0,0013, Rauschen 0,0009–0,0010, beim richtigen Wert n + 0 dagegen 0,47. Kanäle 1–3 sind sauber.
- Saubere Samples von Kanal 4: −6,07 dBFS wie bei 3d. Der Pegelverlust −1,10 bzw. −1,12 dB entsteht nur durch den falschen Sample, rechnerisch |7/8 + 1/8·e^(−j·2π·790·16/48 000)| = −1,17 dB.
- 3d (drei Läufe), noC und onlyD: 0 falsche Samples.

**Deutung:**
- [gemessen] 16 Frames = ein Umlauf des Doppelpuffers (2 × 8 Frames). Gelesen wird also der Platz des letzten Worts eines Blocks, bevor die DMA ihn neu beschrieben hat. Der Wert stammt aus dem vorigen Umlauf.
- [Code] `audioCallback` wird vom **TX**-DMA-Interrupt ausgelöst (`HAL_SAI_TxHalfCpltCallback`/`TxCpltCallback` in `Codec.cpp`, Zweig „PCM3168A: TX is slave“; TX = SAI1-B, Speicher → Peripherie). Freigegeben wird aber auch die **RX**-Hälfte (SAI1-A, Peripherie → Speicher). Die TX-DMA füllt das SAI-FIFO voraus, die RX-DMA hängt hinterher. Beim Interrupt ist das letzte RX-Wort der Hälfte deshalb noch nicht geschrieben.
- [Hypothese] Der Audio-Task liest die Eingänge (`usbd_tx_convert(pv->audio_input)` bei `TX_PRE_FX`, ebenso der Patch) erst nach dem Aufwachen. Mit dem Code im Flash (3d) ist er langsam genug. Mit dem Audio-Task im ITCM (Gruppe C) liest er fast immer zu früh. Das ist ein latenter Fehler im Original-Code, ITCM macht ihn nur sichtbar. Betroffen wäre auch der Standalone-Patch (liest `audio_input` ebenso früh).
- [Hypothese] Dass es nur das letzte Wort (Kanal 4 von Frame 8) trifft, heißt: Die RX-DMA liegt beim Lesen höchstens ein Wort zurück.
- Folge für die Rauschmessung D37: In `B4-fx3i` war Kanal 4 ebenfalls betroffen. Ein fs/8-periodischer Störanteil bleibt beim Ersetzen durch den Wert von n − 16 unverändert (Periode 8). Rauschen und Kamm auf Kanal 4 sind aber leicht verfälscht. [Hypothese] Den Vergleich in D37 ändert das kaum, er mittelt über 4 Kanäle.

### D41 – Build 4y fx3j (= noD + RX-Warten, Patch 11e + 12): geflasht, A1, Loop-Test (2026-11-16, spätabends)

**Setup:** wie D39. Flash `firmware/flashlog/20261116_build4y-fx3j/` (Readback bytegleich `707d9cd3…`), A1: `AC/DC v22.4.r-fx3j`, `SR/BS/CH 48000 8 4`, Slots unverändert, CPU 5 % ohne Stream. Loop `B4y-fx3j-loop`.

**Ergebnis:** 0 Slips, MAD 0,00–0,02 mrad, Spanne ≤ 0,01 dB auf allen Kanälen. Veraltete Samples (`stale_samples.py`): 0 in 2 s und 0 in 30 s (1,44 Mio. Samples je Kanal), Kanal 4 −6,06 dBFS. Meldung `tx ovf 1.0000 1.0000 32` (Stream-Start), kein `fb clamp`. CPU mit Stream 9 %.

**Deutung:** [gemessen] Patch 12 behebt den veralteten Eingangs-Sample (D40). Mit USB im Flash bleibt das Playback stabil. Funktional ist fx3j in Ordnung.

### D42 – Build-4y-Sitzung: Rauschen 3d → fx3j → noD → 3d, offene Eingänge (2026-11-16, spätabends)

**Setup:** acdc1, Alltags-Kette, Eingänge offen, Gain 12 Uhr, je 2 × 60 s `tools/acdc_rec.py --reps 2 --owl-read` (Stream dazwischen neu geöffnet). Reihenfolge: `B4y-3d` → Flash fx3j → Loop (D41) → `B4y-fx3j` → Flash noD (`firmware/flashlog/20261116_build4x-noD-rauschen/`, A1) → `B4y-noD` → Flash 3d (`…_build3d-fx2-zurueck-4y/`, Readback bytegleich, A1) → `B4y-3d-end`. fx3jp gebaut, aber nicht gemessen. Tabelle `out/B4y-session-table.md` (`tools/family_table.py`).

**Ergebnis** (Datei-dBFS, Mittel über 4 Kanäle; Δ gegen das Mittel der vier 3d-Läufe):

| Messung | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| B4y-3d (Start, r1/r2) | −71,69 / −71,66 (≈ 0) | −77,46 / −77,52 | −74,99 / −74,92 | −78,34 / −78,30 | −84,71 / −84,68 |
| **B4y-fx3j** (r1/r2) | −68,88 / −68,85 (**+2,8**) | −78,06 (−0,7) | −71,89 / −71,84 (**+3,1**) | −73,15 / −73,13 (**+5,2**) | −94,86 / −94,89 (**−10,1**) |
| **B4y-noD** (r1/r2) | −70,92 / −70,91 (+0,7) | −78,0 (−0,6) | −72,45 / −72,44 (**+2,5**) | −83,77 / −83,76 (**−5,4**) | −84,44 / −84,40 (+0,3) |
| B4y-3d-end (r1/r2) | −71,66 / −71,58 (≈ 0) | −77,30 / −77,31 | −75,00 / −74,83 | −78,38 / −78,37 | −84,82 / −84,83 |
| zum Vergleich fx3i (D37, gegen eigene Kontrollen) | −0,98 | −0,89 | +0,01 | −5,06 | −0,54 |

- 3d Start gegen Ende ≤ 0,1 dB in allen Familien (keine Drift in dieser Sitzung). r1/r2 je Build ≤ 0,05 dB. Kamm-f0 999,8676–999,8677 Hz.
- fx3j und noD zeigen zusätzlich schwache Linien bei 2000,0002 und 3000,0003 Hz (k·fs/48 im Gerätetakt), 3d nicht.
- Meldungen: fx3j `fb 48.0079 46.5000` / `tx ovf`, noD `fb 48.0003 46.5156` / `fb 48.2656 46.5078` (Feedback-Messung verworfen, kein `fb clamp`), CPU mit Stream fx3j/noD 6–7 %.

**Deutung:**
- [gemessen] **Der fs/8-Gewinn braucht den USB-Code nicht im ITCM:** noD −5,4 dB, fx3i −5,1 dB (D37). Er hängt also an den Gruppen A/B/C/E–H (Audio-DMA-ISR, Scheduler, Audio-Task, Hauptschleife …).
- [gemessen] **Die Warteschleife aus Patch 12 hebt fs/8 um ≈ +10,6 dB** (fx3j gegen noD) und senkt die Mischprodukte um ≈ 10 dB. Pro Block liest die CPU ein paar µs lang das NDTR-Register von DMA1 (D2-Domäne, wo auch SAI1 sitzt). [Hypothese] Busverkehr bzw. Strompuls im Blocktakt koppelt direkt in die ADC-Daten ein. Das ist der bisher stärkste Hinweis auf den Mechanismus der fs/8-Linie: Was die CPU im Blocktakt tut, erscheint bei fs/8. Patch 12 ist deshalb als Fix ungeeignet.
- [gemessen] **Der Kamm hängt an der Lage des USB-Codes:** USB-ISR im ITCM (fx3i) ±0 dB, im Flash bei noD-Layout +2,5 dB gegen 3d. [Hypothese] Der 1-kHz-SOF-Interrupt aus dem Flash (Cache-Fehlgriffe, Flash-Zugriffe im SOF-Takt) prägt den Kamm, und seine Lage im Flash verschiebt ihn (vgl. D33).
- Die Mischprodukte folgen nicht einfach fs/8 und Kamm (fx3j: beide lauter, Mischprodukte −10 dB). [Hypothese] Hier zählt die Phasenlage beider Störer, nicht nur ihr Pegel.
- Q2 (a) „nicht schlechter als 3d“: fx3j fällt durch (Kamm +3,1, fs/8 +5,2). noD verfehlt es beim Kamm (+2,5) und hat zudem den Kanal-4-Fehler.

### D43 – Build 4z fx3k (= noD + RX-Callback, Patch 11f + 12b): gebaut, geprüft, geflasht, A1, Loop-Test (2026-11-16, spätabends)

**Build:** `acdc1-build4z-fx3k` (`v22.4.r-fx3k`, Patches 01 02 04 05 06 03 07d 08 **11f 12b**, 107 112 B, SHA `06e868d1…`), docs/05 „Build 4z“.
- Patch 12b: `audioCallback` aus `HAL_SAI_RxHalfCpltCallback`/`RxCpltCallback` statt aus den TX-Callbacks. Die TX-Callbacks bleiben leer in `Codec.o`.
- Patch 11f: wie 11e, dazu die RX-Callbacks aus `Codec.o` in Gruppe A.
- `check_itcm.py --groups ABCEFGHL`: 0 FAIL, 0 WARN, 6 Veneers hinaus, alle auf Fehler- bzw. Ereignispfaden oder `USBD_LL_Transmit` (gewollt).
- Disassembly: Die RX-Callbacks im ITCM springen direkt (`b.w`) in `audioCallback`, mit denselben Argumenten wie vorher die TX-Callbacks in 3d. Die TX-Callbacks bestehen nur aus `bx lr`. Es gibt keine Schleife und keine zweite (schwache) Fassung.
- Flash-Lage: 505 Flash-Funktionen auf derselben Adresse wie noD (11a), 7 wie fx3j.

**Setup:** wie D39. Flash `firmware/flashlog/20261116_build4z-fx3k/` (Readback bytegleich, Rest 0xFF). A1: `AC/DC v22.4.r-fx3k`, `SR/BS/CH 48000 8 4`, Slots ACDC/ACDC/[Lich], CPU 5 % ohne Stream. Loop `B4z-fx3k-loop` (60 s, `--sine 440 530 670 790`, −6 dBFS, `--owl-read`).

**Ergebnis:**
- `phase_slips.py`: 0 Ereignisse auf allen Kanälen, MAD 0,00–0,01 mrad, Spanne 0,00 dB.
- `stale_samples.py`: 0 falsche Samples in 2 s und in 30 s (1,44 Mio. je Kanal). Kanal 4 bei −6,06 dBFS wie 3d. JSON in `out/B4z/`.
- Meldung `fb 48.0003 46.5156` (verworfene Feedback-Messung wie bei noD in D42), **kein `fb clamp`**. CPU mit Stream 7 %.

**Deutung:** [gemessen] Patch 12b behebt den veralteten Eingangs-Sample (D40) ohne Abfrage-Schleife. Das USB-Playback bleibt mit dem um ≈ 1 Wort späteren Blockstart stabil. Funktional ist fx3k in Ordnung.

### D44 – Build-4z-Sitzung: Rauschen 3d → fx3k → 3d, offene Eingänge (2026-11-16, spätabends)

**Setup:** wie D42 (acdc1, Alltags-Kette, Eingänge offen, Gain 12 Uhr, je 2 × 60 s `acdc_rec.py --reps 2 --owl-read --analyze`). Reihenfolge: `B4z-3d` (19:03) → Flash fx3k → Loop (D43) → `B4z-fx3k` (19:13) → Flash 3d (`firmware/flashlog/20261116_build3d-fx2-zurueck-4z/`, Readback bytegleich mit `d212cf8d…`, A1: `v22.4.r-fx2d`, `48000 8 4`, Slots unverändert) → `B4z-3d-end` (19:17). fx3kp wurde nicht gemessen: Abbruchkriterium Kamm, siehe unten. fx2e (3d + 12b) wurde gebaut, aber nicht gemessen (Nutzer: nur, falls fx3k bei fs/8 auffällt). Tabelle `out/B4z-session-table.md`.

**Ergebnis** (Datei-dBFS, Mittel über 4 Kanäle; Δ gegen das Mittel der vier 3d-Läufe):

| Messung | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| B4z-3d (Start, r1/r2) | −71,64 / −71,60 | −77,39 / −77,36 | −75,38 / −75,29 | −77,63 / −77,64 | −83,94 / −83,98 |
| **B4z-fx3k** (r1/r2) | −70,59 / −70,57 (**+1,0**) | −78,19 / −78,29 (−0,9) | −71,71 / −71,66 (**+3,5**) | −83,73 / −83,79 (**−5,8**) | −103,87 / −103,56 (**−19,4**) |
| B4z-3d-end (r1/r2) | −71,63 / −71,64 | −77,33 / −77,31 | −74,94 / −74,96 | −78,30 / −78,32 | −84,78 / −84,80 |

- r1/r2 sind je Build auf ≤ 0,1 dB gleich (Mischprodukte fx3k 0,3 dB).
- **3d driftet in dieser Sitzung:** Ende gegen Start fs/8 −0,7, Mischprodukte −0,8, Kamm +0,4 dB. Das 3d-Ende entspricht D42 (fs/8 −78,3, Kamm −74,9). Gegen den 3d-Start allein liegt fx3k bei fs/8 −6,1, Kamm +3,7 und Mischprodukten −19,8 dB. Die Aussagen ändern sich dadurch nicht.
- fx3k zeigt wie fx3j und noD die schwachen Linien bei 2000,0002 und 3000,0003 Hz (k·fs/48), 3d nicht. Kamm-f0 durchgehend 999,8676 Hz.
- Meldungen: 3d `fb …`/`tx ovf …` (Stream-Start), fx3k `fb 48.0162 46.5078` / `fb 47.9991 46.5078`, kein `fb clamp`. CPU mit Stream: 3d 14–15 %, fx3k 6 %.

**Deutung:**
- [gemessen] **Patch 12b kostet bei fs/8 nichts:** fx3k −5,8 dB, noD −5,4 dB (D42), fx3i −5,1 dB (D37), jeweils gegen 3d. Der Blockstart aus dem RX- statt aus dem TX-Interrupt (≈ 1 Wort später) ändert fs/8 nicht messbar. Der Anstieg in fx3j (D42) kam also von der Abfrage-Schleife, nicht vom Warten auf die RX-DMA an sich.
- [gemessen] **Die Mischprodukte fallen um ≈ 19 dB** (noD +0,3, fx3j −10,1). [Hypothese] Die Phasenlage zwischen Blocktakt und SOF entscheidet, nicht nur der Pegel der beiden Störer (vgl. D42). Mit 12b liegt der Blockstart anders zum SOF-Interrupt.
- [gemessen] **Kamm +3,5 dB** (noD +2,5, fx3j +3,1): Mit USB im Flash bleibt der Kamm über 3d. Q2 (a) „nicht schlechter als 3d (≤ +0,5 dB)“ verfehlt fx3k nur beim Kamm. Deshalb wurde fx3kp nicht gemessen.
- RMS +1,0 dB: Der Kamm trägt mehr bei, als fs/8 und die Mischprodukte zusammen einsparen. Bei vollem Gain und mit Kompressor (Alltag) zählt aber gerade die fs/8-Linie [Hypothese, nicht getrennt geprüft].
- **Folge:** fx3k ist funktional sauber und der neue Basisstand für den nächsten Schritt, USB (ganz oder nur die SOF-Kette) ins ITCM ohne den Playback-Fehler (D39). acdc1 läuft wieder mit 3d.

### D45 – Build 5: Diagnose-Zähler im USB-Pfad, USB im ITCM gegen USB im Flash, Loop (2026-11-16, nachts)

**Builds** (docs/05 „Build 5“), Basis fx3k (01 02 04 05 06 03 07d 08 + 12b) + Diagnose-Patch `13-usb-diag-counters`:
- `acdc1-build5-diag-itcm` (`v22.4.r-dg5i`, Patch 11g = alle Gruppen inklusive D im ITCM, 108 904 B, `27390dca…`)
- `acdc1-build5-diag-flash` (`v22.4.r-dg5f`, Patch 11f = D im Flash, 108 728 B, `02052846…`)

`check_itcm.py`: Hot-Liste, Veneers und Vektoren ok. Bei dg5i meldet es einen FAIL beim Anker, bei dg5f eine WARN. Grund sind die Texte der Diagnose-Meldung in `.rodata`, für Diagnose-Builds ohne Belang.

**Setup:** Loop wie D39 (60 s, `--sine 440 530 670 790`, `--owl-read`). Flashlogs `firmware/flashlog/20261116_build5-diag-{itcm,flash}/`, Readback jeweils bytegleich, A1 bestanden. Meldung (Zählerstände, ab dem ersten OUT-Paket des Streams, Bedeutung im Patch-Kopf):

| Build | Meldung | Slips | MAD |
|---|---|---|---|
| dg5i (USB im ITCM) | `l0 g0 k0 L0 b0 i0 t0 f61508 c2370 d98 e43 s0 p51-…` | 4 je Kanal | 2,2–6,8 mrad |
| dg5f (USB im Flash) | `l0 g0 k0 L0 b0 i0 t0 f61507 c0 d0 e0 s0 p57-…` | 0 | ≤ 0,02 mrad |

**Deutung:**
- [gemessen] **Mit USB im ITCM geht kein ISO-OUT-Paket verloren.** Es gibt keine Frame-Lücken, kein zu spätes Neu-Aufsetzen und kein INCOMPISOOUT. H-a (ISO-OUT-Parität) ist widerlegt.
- `f` (Feedback-Endpunkt incomplete in ≈ 31 von 32 Frames) ist in beiden Builds gleich. Der Host holt das Feedback nur alle 32 Frames ab, das ist normal.
- Der Fehler steckt in der Feedback-Regelung: 2370 Klemmen, 98 verworfene Messungen, 43 Puffer-Fehler. Der Regler läuft nur alle 32 SOF, das wären in ≈ 64 s etwa 2000 Perioden. 2370 Klemmen heißen also, dass es mehr Perioden gab als Frames/32. [Hypothese] Es gibt zusätzliche SOF-Aufrufe (D46 bestätigt das).
- `p` max ist ein Artefakt (erstes Paket ohne gültigen SOF-Zeitstempel).

### D46 – Diagnose 13b: Die SOF-Kette läuft mit USB im ITCM fast in jedem Frame zweimal (2026-11-16, nachts)

**Build:** `acdc1-build5b-diag-itcm` (`v22.4.r-dg5i2` = dg5i + Patch `13b-usb-diag-sof-fb`, 109 104 B, `9611f646…`), Flash `…_build5b-diag-itcm/` bytegleich, A1 bestanden. Kontrolle dg5f2 gebaut (`0a0851f4…`), nicht geflasht. Loop wie D45.

**Meldung:** `n125276 S61784 P3915 d308 c1919 R-24243/-3000 V-487/517 E-209/…` (auf 63 Zeichen gekürzt)
- 125 276 SOF-Aufrufe in ≈ 64 s, davon **61 784 mit derselben Frame-Nummer wie der vorige** → in ≈ 97 % der Frames läuft `USBD_AUDIO_SOF` zweimal.
- 3915 Feedback-Perioden statt ≈ 2000, also je ≈ 16 Frames statt 32.
- Gemessen 23,8 … 45,0 Samples pro Frame (statt 48), gesendet 47,513 … 48,517.
- Füllstandsfehler bis −209 Samples. Loop: 4 Slips je Kanal, MAD 0,25–1,4 mrad.

**Deutung:**
- [gemessen] **Ursache des USB-Fehlers mit Gruppe D im ITCM (D38/D39):** Die SOF-Kette läuft doppelt. Der Regler misst und sendet deshalb falsches Feedback, der Host liefert falsch viel, und der RX-Puffer läuft an die Grenze (`fb clamp`, Slips). Auch `fb 48.0019 25.5000` bei onlyD (D39) passt dazu: eine Periode von ≈ 17 Frames.
- [Code] HAL löscht `GINTSTS.SOF` erst nach dem Callback (`GINTSTS &= SOF`). [Hypothese] Im ITCM ist der Handler so kurz, dass er erneut einspringt, bevor das Löschen im USB-Taktbereich wirkt. Dann sieht er das Flag noch gesetzt. Im Flash ist er langsam genug (dg5f: keine Klemmen). Beim Incomplete-Interrupt tritt das nicht auf (f gleich), dessen Callback ist lang (Flush).
- Fix: Patch 14 (`USBD_AUDIO_SOF` wertet jede Frame-Nummer nur einmal aus).

### D47 – Build 5c fx3l (alle Gruppen im ITCM + 12b + 14): geflasht, A1, Loop-Test (2026-11-16, nachts)

**Build:** `acdc1-build5c-fx3l` (`v22.4.r-fx3l`, Patches 01 02 04 05 06 03 07d 08 **11g 12b 14**, 107 340 B, `b55b94d8…`). `check_itcm.py`: 0 FAIL, 0 WARN, 104 heiße Funktionen im ITCM (12 352 B Code), 27 Veneers hinaus, alle kalt. Disassembly: `USBD_AUDIO_SOF` vergleicht `DSTS.FNSOF` mit dem letzten Wert und kehrt bei Gleichheit sofort zurück.

**Setup:** wie D39, Flash `…_build5c-fx3l/` bytegleich, A1: `v22.4.r-fx3l`, `48000 8 4`, Slots unverändert, CPU 5 %. Loop `B5c-fx3l-loop`.

**Ergebnis:**
- 0 Slips, MAD ≤ 0,02 mrad, Spanne 0,00 dB.
- 0 veraltete Samples in 30 s, Kanal 4 −6,06 dBFS (`out/B5/`).
- Meldung `tx ovf 1.0000 1.0000 32` (Stream-Start), **kein `fb clamp`**, CPU mit Stream 8 %.

**Deutung:** [gemessen] Mit Patch 14 läuft der USB-Code im ITCM fehlerfrei, der Fehler aus D38/D39 ist behoben.

### D48 – Build-5-Sitzung: Rauschen fx3l, fx3lp, 3d-Endkontrolle, offene Eingänge (2026-11-16, nachts)

**Setup:** wie D44. Reihenfolge: (Diagnose D45/D46) → fx3l Loop (D47) → `B5c-fx3l` → Flash fx3lp (`…_build5cp-fx3lp/`, bytegleich, A1) → `B5c-fx3lp` → Flash 3d (`…_build3d-fx2-zurueck-5/`, Readback bytegleich mit `d212cf8d…`, A1 bestanden) → `B5-3d-end`. In dieser Sitzung gab es keine 3d-Startkontrolle. Als Referenz dienen die 3d-Endkontrollen von B4z (≈ 2,5 h vorher) und B5. Die beiden stimmen auf ≤ 0,1 dB überein (fs/8 −78,30/−78,29, Kamm −74,95/−74,88). Tabelle `out/B5-session-table.md`.

**Ergebnis** (Datei-dBFS; Δ gegen das Mittel von B4z-3d-end und B5-3d-end, je r1/r2):

| Messung | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| **B5c-fx3l** (r1/r2) | −72,75 / −72,65 (**−1,1**) | −78,5 (**−1,25**) | −74,68 / −74,54 (+0,23 / +0,38) | −83,40 / −83,34 (**−5,1**) | −119,1 / −120,1 (**−34,8**) |
| **B5c-fx3lp** (r1/r2) | −72,77 / −72,70 (−1,1) | −78,3 / −78,4 (−1,1) | −74,81 / −74,62 (+0,11 / +0,29) | −83,51 / −83,60 (−5,3) | −118,5 / −115,8 (−32,4) |
| B5-3d-end (r1/r2) | −71,55 / −71,56 | −77,19 | −74,86 / −74,90 | −78,30 / −78,28 | −84,78 / −84,76 |
| zum Vergleich fx3k (D44) | +1,0 | −0,9 | +3,5 | −5,8 | −19,4 |

- Meldungen fx3l/fx3lp: nur `tx ovf …` (Stream-Start), CPU mit Stream 6–7 %. Kamm-f0 999,8675–999,8676 Hz.
- fx3lp gegen fx3l: RMS, Rest, Kamm und fs/8 ≤ 0,25 dB. Die Mischprodukte streuen bei −116…−120 dB, das liegt am Grundrauschen.

**Deutung:**
- [gemessen] **fx3l ist der erste Build, der Q2 (a) erfüllt** (nicht schlechter als 3d, ≤ +0,5 dB): fs/8 −5,1, Mischprodukte ≈ −35 dB (praktisch verschwunden), Rest −1,25, RMS −1,1 dB. Der Kamm liegt bei +0,2…+0,4 dB, also an der Schwelle.
- [gemessen] **Q2 (b), lagenunabhängig:** fx3lp (Flash-Code +0x150) liegt ≤ 0,25 dB bei fx3l. Das Rauschen hängt nicht mehr an der Flash-Lage (anders als D33).
- Gegenüber fx3k (USB im Flash) senkt der USB-Code im ITCM den Kamm um ≈ 3 dB und die Mischprodukte um weitere ≈ 15 dB.
- Einschränkung: Es gab keine 3d-Startkontrolle direkt vor fx3l. Die beiden 3d-Endkontrollen im Abstand von 2,5 h sind aber gleich, die Drift aus D44 ist hier nicht aufgetreten.

### D49 – fx3l für den Alltagstest auf acdc1 (2026-11-16, nachts)

**Entscheidung (Nutzer):** fx3l (`acdc1-build5c-fx3l`, `b55b94d8…`) bleibt für einen Alltagstest auf acdc1.

**Flash:** `firmware/flashlog/20261116_build5c-fx3l-alltag/`, Readback bytegleich, Rest 0xFF. Neustart (Case aus, USB ab, Case an, USB an). A1: `AC/DC v22.4.r-fx3l`, `SR/BS/CH 48000 8 4`, Slots ACDC/ACDC/[Lich], CPU 5 % ohne Stream.

**Zu beobachten im Alltag:**
- Aufnahme + Wiedergabe in DAW/Host-Software: Aussetzer, Knackser, Meldung `fb clamp` per `owl_read.py`.
- Durchleitung ohne Rechner (Standalone).
- Eingangs-LEDs.
- Patch-Wechsel: Der Patch-Heap im CCM ist auf 39,3 KB verkleinert, große Patches könnten nicht mehr passen.

**Rückweg:** Build 3d (`firmware/builds/acdc1-build3d-fx2/ACDC.bin`, `d212cf8d…`), Flash-Ablauf wie in CLAUDE.md.

### D50 – Patch-Upload per `owl_write.py`, vier FX-Patches auf acdc1, Build 6 fx4a gebaut (2026-11-17)

**Anlass (Nutzer):** Patches ohne Weboberfläche aufspielen, die Patches aus `burstMembrane/acdc-patches` auf acdc1 ablegen, Patch-Wahl beim Einschalten (Boot-Menü, `docs/05` „Build 6“).

**Werkzeug `tools/owl_write.py` [gemessen]:**
- Offline-Gegenprobe: Aus den Daten der Library-Datei `owl-patches/library/ACDC_library.syx` erzeugt das Werkzeug dieselben 46 Upload-Pakete, die Datei ist **bytegleich**.
- RAM-Test: `Dummy.syx --run` → 29 Pakete in 0,7 s, das Gerät meldet „Dummy“ als laufend. Nichts gespeichert.
- Store: Jeder Slot wurde danach heruntergeladen und ist bytegleich mit der Datei (Name, Größe, CRC stimmen).

**Patches** (gebaut mit `tools/build_owl_patch.sh`, OwlProgram `60f44ab`, DaisySP `4263388`, Quellen `78ffa22`, `PLATFORM=OWL2`, Link-Adresse 0x2000c000 wie die Library-Patches):

| Slot | Patch | Größe B | CRC32 | CPU | Speicher B | Quelle |
|---|---|---|---|---|---|---|
| 1 | ACDC (unverändert) | 10 164 | `0xbeb3bb2e` | 5 % | 368 | wie D1 |
| 2 | TapeDelay | 35 524 | `0xbd9ce988` | 31 % | 769 272 | `TapeDelayPatch.hpp` |
| 3 | Grainz | 32 572 | `0x8c11a850` | 11 % | 4 197 904 | `GrainzPatch.hpp` |
| 4 | RingsReverb | 21 292 | `0x91cd2742` | 14 % | 337 440 | `RingsStereoReverbPatch.hpp` |
| 5 | Dummy | 5 636 | `0x01a7a0cd` | nicht gelesen | | `Dummypatch.hpp` (leere Durchleitung) |

- CPU und Speicher laut `PROGRAM_STATS`, je direkt nach dem Store gelesen (der gespeicherte Slot läuft dann), Blockgröße 8, Regler um 12 Uhr, Firmware fx3l. Ob dabei ein USB-Stream lief, wurde nicht festgehalten.
- `GrainzPatch.hpp` baut im Original nicht: `SmoothFloat` ist nicht deklariert. Das Build-Skript bindet `SmoothValue.h` davor ein, die Quelle bleibt unverändert.
- Nicht gebaut: `TapeDelay.dsp` und `FaustTapeDelay.dsp`. Dafür fehlt der FAUST-Compiler.
- Gehört wurde noch keiner der Patches.

**Gerät:** Sicherung vorher `backup/acdc1/20261117/owl/` (nur Slot 1 belegt, Storage 10 240 B). Danach Slots 1–5 belegt, Storage 105 984 / 8 388 608 B, per Program Change zurück auf Slot 1 („ACDC“ läuft). Logs: `out/owl_write/acdc1/20261117/`.

**Nebenbefund:** Nach jedem Store bzw. Patch-Wechsel steht als letzte Meldung `fb 0.0859 48.0156` bzw. `fb 0.0625 48.0078` (verworfene Feedback-Messung, vgl. D18). [Hypothese] Der Flash-Schreibvorgang und der Patch-Start halten die SOF-Auswertung kurz auf. Kein `fb clamp`.

**Build 6 `acdc1-build6-fx4a` (`v22.4.r-fx4a`, `e7ee9b90…`, 108 496 B) = fx3l + Patch 15, gebaut, nicht geflasht:**
- `tools/check_itcm.py … --ref acdc1-build5c-fx3l`: BESTANDEN (0 FAIL, 0 WARN). ITCM-Code 12 392 B (fx3l 12 352), Patch-Heap im CCM 40 184 B. Alle 179 RAM-Objekte an derselben Adresse wie fx3l.
- Im periodischen Pfad kommen 5 Befehle am Anfang von `acdcOnLoopLate` dazu (Abfrage `led_hold`).
- Host-Test `tools/sim_boot_menu.sh`: 18 Fälle mit simulierten Reglern, alle wie erwartet.

**Offen vor dem Flash:** Endwerte der vier Regler messen (Schwellen 5 % / 95 % sind vorläufig). Die Regler lassen sich per `owl_read.py` lesen (CC 20–23 nach dem Settings-Request, 7 Bit): heute um 12 Uhr 61 / 48 / 58 / 66.

### D51 – Build 6 fx4a geflasht (2026-11-17)

**Regler-Endwerte [gemessen]:** Muster eingestellt (Regler 1, 2, 3 links, Regler 4 rechts), drei Lesungen per `owl_read.py`, CC 20–23: **2 / 2 / 2 / 127** (7 Bit), alle drei gleich. Der Linksanschlag liegt also bei ≈ 64–95 von 4095, nicht bei 0. Die Schwellen aus Patch 15 (unter 205, über 3890 ≙ 6 bzw. 121 in 7 Bit) passen, kein Neubau. Belegt ist damit auch CC 23 = Regler 4. Die Zuordnung der Regler 1–3 zu CC 20–22 zeigt erst die Menü-Abnahme.

**Flash (Freigabe Nutzer):** `firmware/flashlog/20261117_build6-fx4a/`. Vorher `owl_read_before` (fx3l, Slots 1–5). `ACDC.bin` `e7ee9b90…`, Readback bytegleich, Rest 0xFF.

**Offen:** Neustart durch den Nutzer, A1 und die Abnahme 3–8 aus `docs/05`, „Build 6“. Rückweg: fx3l (`b55b94d8…`).

### D52 – fx4a: Boot-Menü am Gerät, A1 (2026-11-17)

**Ablauf (Nutzer):** Neustart mit den Reglern auf dem Muster (Case aus, USB ab, Case an). Rückmeldung: Das Menü läuft. Welche Einzelschritte geprüft wurden (Abbruch mit Regler 3, Timeout, zweiter Start ohne Muster), ist nicht festgehalten.

**A1 per `owl_read.py` [gemessen]:** `firmware/flashlog/20261117_build6-fx4a/owl_read_after/`
- Version `AC/DC v22.4.r-fx4a`, Blockgröße 8, 48 kHz.
- Slots 1–5 unverändert (Namen, Größen, CRC wie vor dem Flash).
- Es läuft **Slot 3 „Grainz“** (Program 3). Storage 106 240 B, vorher 105 984 B: genau **ein Eintrag von 256 B** dazu, also wurde die Wahl einmal gemerkt. Der Eintrag `ACDC.slot` erscheint nicht in der Ressourcen-Liste (System-Ressource).
- Regler beim Auslesen: 127 / 13 / 41 / 4 (CC 20–23).

**Nebenbefund [gemessen]:** Grainz meldet in dieser Reglerstellung **CPU 78 %** (Speicher 4 197 904 B). Direkt nach dem Store waren es mit Reglern um 12 Uhr 11 % (D50). Die Last hängt also stark von den Reglern ab. Regler 4 ist „Density“, am Linksanschlag überlappen die meisten Grains [Code]. Ab 100 % sind Aussetzer zu erwarten, gemessen ist das nicht.

**Offen aus der Abnahme (`docs/05`, „Build 6“):** Abbruch und Timeout gezielt prüfen, Start in Alltagsstellung (Fehlauslösung), Loop-Test, Rausch-A/B gegen fx3l.

### D53 – Menü-Abnahme (Nutzer), neue Patch-Builds, acdc1 antwortet nach einem Slot-Download nicht mehr auf MIDI (2026-11-17, abends)

**Abnahme Boot-Menü (Nutzer) [gemessen]:** Abbruch mit Regler 3 geht, Start aus dem gemerkten Slot geht, Abbruch nach 60 s geht. Wunsch: 30 s statt 60 s.

**Wünsche (Nutzer):** Ausgänge mancher Patches übersteuern (z. B. Grainz) → Pegel senken oder Limiter. Alle Patches mit Cortex-M7-Flags bauen. Slot 5: statt Dummy ein Patch nach dem Vorbild des Instruō tanh[3], Kanal 4 = Mix der Kanäle 1–3, Regler 4 = Pegel, In 4 = CV auf den Pegel.

**Gebaut (nichts davon ist auf dem Gerät gespeichert):**
- `owl/AcdcOutput.h`: gekoppelter Spitzenwert-Limiter auf Out 1/2 (Schwelle 0,5 ≙ 5 V, Anstieg 1 ms, Abfall 150 ms, tanh-Knie bis höchstens 0,75), als Hülle `AcdcLimited<…>` um den Patch. Die fremde Quelle bleibt unverändert.
- `owl/Tanh3Patch.hpp`: Out n = 5 V · tanh(Level n · In n / 5 V), Level 0,5…16-fach, Antialiasing erster Ordnung. Out 4 = tanh-begrenzter Mix × Pegel (Regler 4 + CV an In 4, 5 V ≙ voller Weg). Das Handbuch des Vorbilds nennt je Kanal einen Level-Regler vor dem tanh und keine Pegel, die 5 V sind meine Wahl.
- `tools/test_owl_dsp.sh`: 17 Fälle am Rechner (Pegel, Sättigung, Antialiasing, Mix, CV, Limiter), alle wie erwartet.
- Builds mit `PLATFORM=OWL3`, gelinkt nach 0x2000c000: TapeDelay 30 036 B (`0xe104abf8`), Grainz 26 700 B (`0xcc5b8e81`), RingsReverb 21 556 B (`0x14db59ec`), je mit Limiter, Tanh3 11 564 B (`0xbac2e7dc`). Die Builds aus D50 liegen in `owl-patches/builds-owl2/`.
- Firmware `acdc1-build6b-fx4b` (`v22.4.r-fx4b`, `a21f35c9…`, 108 496 B) = fx3l + Patch 15b (Abbruch nach 30 s). `check_itcm` bestanden, ITCM-Inhalt bytegleich mit fx4a. Nicht geflasht.

**Last der alten Builds (D50, `PLATFORM=OWL2`) [gemessen]:** TapeDelay 31 %, Grainz 12 %, RingsReverb 14 %, bei Reglern 104 / 110–125 / 86–127 / 38–50 (der Nutzer drehte währenddessen).

**Vorfall [gemessen]:**
1. `owl_write.py TapeDelay.syx --run` (neuer M7-Build mit Limiter, nur RAM): läuft, 3 s später CPU 31 %, Speicher 769 288 B.
2. `owl_write.py TapeDelay.syx --store 2 --yes`: Geräte-ID, Version und Slot-Liste kommen noch. Die Sicherung des belegten Slots 2 (Download per SysEx `0x18`) kommt unvollständig an („CRC mismatch“). Das Werkzeug bricht ab, **geschrieben wird nichts**.
3. Danach antwortet acdc1 auf keine MIDI-Anfrage mehr (6 s gelauscht, 0 Nachrichten). Am USB ist es weiter angemeldet (`OWL-ACDC-FX`, Audiogerät vorhanden). Die folgenden Aufrufe für Slot 3–5 brachen deshalb vor jedem Schreiben ab.

**Deutung [Code]:** Läuft ein Patch, bedient nur der Audio-Task MIDI (`Owl::loop` tut es nur ohne laufenden Patch). Ein Gerät, das am USB hängt, aber kein MIDI mehr spricht, passt also zu einem stehenden Audio-Task bei weiterlaufender Hauptschleife (sonst hätte der Watchdog nach 8 s neu gestartet). **Ursache offen.** Kandidaten [Hypothese]: der neue Patch-Build selbst (M7-Flags, Limiter-Hülle) oder der Slot-Download, während ein aus dem RAM gestarteter Patch läuft. In D50 liefen Downloads neben laufenden, gespeicherten Patches viermal fehlerfrei, damals mit fx3l und den M4-Builds.

**Stand:** Slots 1–5 unverändert wie D52 (laut letzter Slot-Liste vor dem Abbruch), gemerkter Slot vermutlich 4. acdc1 braucht einen Neustart.

**Nächste Schritte:** Neustart, Zustand lesen. Dann getrennt prüfen: (a) alter Build per `--run` und Download, (b) neuer Build per `--run` ohne Download über mehrere Minuten, (c) neuer Build ohne Limiter.

### D54 – Ursache des MIDI-Ausfalls eingegrenzt, neue Patch-Builds gespeichert (2026-11-17, abends)

**Nutzer:** Vor dem Ausschalten lief noch Ton, er klang aber eigenartig. Danach Neustart.

**Nach dem Neustart [gemessen]:** fx4a, Slot 4 „RingsReverb“ (alter Build) läuft, 15 % CPU, Slots unverändert. `owl_read.py --out backup --dump` (`backup/acdc1/20261117/owl_223558/`, siehe `HINWEIS.txt` dort):

| Slot | Ergebnis |
|---|---|
| 1 ACDC | vollständig, CRC stimmt |
| 2 TapeDelay | **unvollständig**: 177 Pakete, 35 509 von 35 524 B (15 B fehlen), keine Prüfsumme |
| 3 Grainz | vollständig, CRC stimmt |
| 4 RingsReverb (lief gerade) | **Paket 34 trägt Index 31**, Reihenfolge gestört |
| 5 Dummy | vollständig, CRC stimmt |

Das Gerät antwortete danach weiter. Der Fehler tritt also auch mit einem alten, gespeicherten Patch auf. Der neue M7-Build und die Limiter-Hülle scheiden damit als Auslöser des Download-Fehlers aus.

**Ursache [Code], Auslösung [Hypothese]:** Wettlauf im MIDI-Sendeweg der Original-Firmware.
- Läuft ein Patch, ruft der Audio-Task in jedem Block `midi_tx.transmit()` auf (`onProgramReady`).
- Der Slot-Download (`SendResourceTask`) läuft in der Hauptschleife und schreibt je Durchlauf ≈ 320 B in den 1024-B-Sendepuffer. Ist der fast voll, ruft `UsbdMidiTransmitter::write()` selbst `transmit()` auf.
- `transmit()` prüft `usbd_midi_ready()`, startet die Übertragung und rückt danach den Lesezeiger vor. Der Audio-Task kann die Hauptschleife dazwischen unterbrechen (der Wechsel kommt aus dem Codec-Interrupt). Dann sendet einer, und der andere rückt den Lesezeiger trotzdem vor: Daten gehen verloren oder kommen doppelt.
- Das erklärt die fehlenden 15 B und die gestörte Reihenfolge. [Hypothese] Derselbe Wettlauf kann `midi_tx_lock` gesetzt lassen, dann sendet das Gerät bis zum Neustart kein MIDI mehr (D53). Ton läuft dabei weiter.
- Kurze Antworten (Geräte-ID, Slot-Liste, Statistik) füllen den Puffer nicht und sind nicht betroffen, Uploads ebenfalls nicht.
- In D50 liefen fünf Downloads fehlerfrei, heute scheiterten drei von sechs. Was den Unterschied macht (Last, USB-Verkehr), ist offen. Der Code ist in fx3l und fx4a derselbe.

**Folge für die Werkzeuge:** `owl_write.py` nimmt mit `--backup-file` eine lokale Kopie als Sicherung, wenn Größe und CRC zum Slot passen, und lädt nach dem Store nur noch auf Wunsch zurück (`--download-check`). `owl_read.py --dump` kann bei laufendem Patch beschädigte Dateien liefern, das Feld `ok` im Report beachten.

**Store [gemessen]:** Sicherung je Slot aus `owl-patches/builds-owl2/` (Größe und CRC wie auf dem Gerät), danach Name, Größe und CRC vom Gerät zurückgelesen. Kein Download. Logs `out/owl_write/acdc1/20261117/`, Sicherungen `backup/acdc1/20261117/owl_write_2238*/` und `…_223904/`.

| Slot | Patch | Größe B | CRC32 | CPU neu | CPU alt (D53) |
|---|---|---|---|---|---|
| 2 | TapeDelay, M7, Limiter | 30 036 | `0xe104abf8` | 33 % | 31 % |
| 3 | Grainz, M7, Limiter | 26 700 | `0xcc5b8e81` | 14 % | 12 % |
| 4 | RingsReverb, M7, Limiter | 21 556 | `0x14db59ec` | 16 % | 14 % |
| 5 | Tanh3, M7 | 11 564 | `0xbac2e7dc` | 20 % | (Dummy) |

- Regler bei allen Lesungen 104 / 125 / 86 / 50, je 3 s nach dem Store.
- **Die M7-Flags sparen keine Last.** Die Builds sind 1–2 Prozentpunkte teurer als die alten, das ist der Limiter. Die Binaries sind kleiner (TapeDelay −15 %, Grainz −18 %).
- Nach dem letzten Store läuft Tanh3 (Slot 5). Gemerkter Slot bleibt 4.
- Gehört und beurteilt hat die neuen Builds noch niemand. „Klang eigenartig“ (Nutzer, neuer TapeDelay aus dem RAM) ist nicht geklärt, in Frage kommt der Limiter bei 5 V.

### D55 – Build 6b fx4b geflasht (2026-11-17, abends)

**Flash (Freigabe Nutzer):** `firmware/flashlog/20261117_build6b-fx4b/`. Vorher `owl_read_before` (fx4a). `ACDC.bin` `a21f35c9…` (`v22.4.r-fx4b` = fx3l + Patch 15b, Abbruch des Boot-Menüs nach 30 s statt 60 s), Readback bytegleich, Rest 0xFF.

**Offen:** Neustart durch den Nutzer, A1, Timeout nachmessen. Dazu weiter Loop-Test und Rausch-A/B gegen fx3l (`docs/05`, „Build 6“). Rückweg: fx4a (`e7ee9b90…`), dann fx3l (`b55b94d8…`).

**A1 nach dem Neustart [gemessen]:** `firmware/flashlog/20261117_build6b-fx4b/owl_read_after/`. Version `AC/DC v22.4.r-fx4b`, Blockgröße 8. Es läuft der gemerkte Slot 4 „RingsReverb“ (neuer Build, 16 % CPU). Slots 1–5 wie nach D54 (Namen, Größen, CRC). Storage 101 120 B. Der Timeout von 30 s ist am Gerät noch nicht nachgemessen.

### D56 – Tanh3: Störgeräusche = Aliasing, neue Fassung mit vierfachem Oversampling (2026-11-17, abends)

**Nutzer:** Der Limiter scheint zu funktionieren. Im Tanh3-Patch treten manchmal Störgeräusche auf, „sehr digital, fast wie eine modulierte Pulswelle“. Boot-Menü unter fx4a: Abbruch mit Regler 3, Start aus dem Speicher und Abbruch nach 60 s gehen.

**Untersuchung am Rechner [gemessen, Simulation]:** Der Patch-Code (Kanal 1) mit Sinus 5 V Spitze, 1 s kohärent, Summe aller Linien unter 15 kHz, die keine Harmonischen sind, relativ zum Grundton:

| f | Level | tanh ohne Antialiasing | Fassung 1 (ADAA 1. Ordnung) | Fassung 2 (4× Oversampling, 48 Taps) |
|---|---|---|---|---|
| 1 kHz | 6,7 | −70,9 dB | −80,1 dB | −108,4 dB |
| 2 kHz | 6,7 | −38,7 dB | −49,4 dB | −104,2 dB |
| 3 kHz | 2,8 (12 Uhr) | −49,8 dB | −59,4 dB | −122,4 dB |
| 3 kHz | 6,7 | −26,7 dB | −36,9 dB | −98,2 dB |
| 3 kHz | 16 | −18,4 dB | −29,9 dB | −60,3 dB |
| 5 kHz | 2,8 (12 Uhr) | −31,4 dB | −43,4 dB | −115,0 dB |
| 5 kHz | 6,7 | −18,6 dB | −30,7 dB | −79,4 dB |
| 5 kHz | 16 | −14,4 dB | −27,2 dB | −42,4 dB |
| 8 kHz | 16 | −11,7 dB | −28,0 dB | −31,4 dB |

- Fassung 1 brachte nur ≈ 10 dB gegen den nackten tanh. Bei hellem Material und Level über 12 Uhr lagen unharmonische Linien bei −30…−50 dB. **Das passt zur Beschreibung des Nutzers** [Hypothese: Es ist das, was er hörte. Beim Auslesen stand Regler 2 auf Rechtsanschlag, Level 16].
- Die stärksten Aliaslinien liegen oft über 20 kHz, deshalb zählt die Tabelle nur bis 15 kHz.
- 64 statt 48 Taps bringt höchstens 5 dB, 8× Oversampling wäre bei 5 kHz / Level 16 weitere 30 dB besser, kostet aber etwa die doppelte Rechenzeit.

**Fassung 2 (`owl/Tanh3Patch.hpp`):** je Kanal FIR-Polyphase hoch auf 192 kHz (48 Taps, Kaiser β = 9, Grenze 22 kHz, jede Phase auf Summe 1 normiert), tanh als Kettenbruch (Fehler unter 1e-4, stetig), FIR herunter. Laufzeit 11,75 Samples (0,25 ms). Bandbegrenzte Ausgänge schwingen bei harter Aussteuerung bis ≈ 10–28 % über 5 V hinaus (gemessen bis 0,64 bei 12 kHz, Level 16). `tools/test_owl_dsp.sh`: 18 Fälle, darunter die Aliasprüfung (3 kHz, Level 6,7: −99,6 dB).

**Gerät [gemessen]:** Build `Tanh3` 18 580 B, CRC `0xaed73395`, `PLATFORM=OWL3`. Erst `--run`, dann Store in Slot 5 (Sicherung der Fassung 1 aus `owl-patches/builds-owl2/Tanh3-v1/`). **CPU 48–49 %** (Fassung 1: 16–20 %), Speicher 2 608 B, dreimal gelesen über 30 s, Regler 2 / 127 / 2 / 2. Firmware fx4b.

**Offen:** Hörurteil des Nutzers. Die Last ist hoch, Auswege: größere Blockgröße (siehe unten), Oversampling nur für Kanäle mit Signal, kürzerer Abwärtsfilter.

**Blockgröße (Frage des Nutzers) [Code]:** `settings.audio_blocksize` ist zur Laufzeit per SysEx-Konfiguration `BS` setzbar (4…256, nur im RAM), `Codec` übernimmt sie. Auf den eigenen Builds nie ausprobiert. Alle Messungen und die USB-Abstimmung (Feedback, RX-Fix) liefen mit 8. Die Störlinie fs/8 = 6 kHz ist die Blockrate, sie würde mit 16 auf 3 kHz wandern [Hypothese].

### D57 – fx4b: Loop-Test, auch mit Tanh3 unter Last (2026-11-17, abends)

**Setup:** acdc1 mit fx4b, Alltags-Kette, Patchkabel Out n → In n (Nutzer), `tools/acdc_rec.py --sine 440 530 670 790` (−6 dBFS, 1 s Einblenden, `--owl-read`), je 60 s. Regler nicht auf 12 Uhr gestellt (zuletzt gelesen 2 / 127 / 2 / 2), sie wirken mit `TX_PRE_FX` weder auf die Aufnahme noch auf den Ausgang mit Stream.

| ID | Laufender Patch | Slips (`phase_slips.py`) | MAD | Spanne | veraltete Samples (`stale_samples.py`) | Geräte-Meldung | CPU |
|---|---|---|---|---|---|---|---|
| `B6b-fx4b-loop` | Slot 1 ACDC | 0 auf allen 4 Kanälen | ≤ 0,01 mrad | 0,00 dB | 0 von 96 000 je Kanal | `tx ovf 1.0000 1.0000 32` (Stream-Start) | 6 % |
| `B6b-fx4b-loop-tanh3` | Slot 5 Tanh3 (Fassung 2) | 0 auf allen 4 Kanälen | ≤ 0,01 mrad | 0,00 dB | 0 von 96 000 je Kanal | `tx ovf 1.0000 1.0000 32` (Stream-Start) | 53 % |

- Stream-Meldungen von PortAudio: 0 in beiden Läufen. Kein `fb clamp`, kein `rx unf`.
- Pegel −6,05…−6,10 dBFS wie bei fx3l (D47).
- **Loop-Test für fx4b bestanden**, auch mit 53 % Patch-Last neben dem Stream.

**Offen:** Rausch-A/B gegen fx3l in derselben Sitzung.

### D58 – Build-6-Sitzung: Rauschen fx4b gegen fx3l, offene Eingänge (2026-11-17, 23:07–23:19)

**Setup:** acdc1, Alltags-Kette, Loop-Kabel entfernt (Nutzer), Eingänge offen, `tools/acdc_rec.py` duplex mit Nullen am Ausgang, je 2 × 60 s. In allen Läufen lief Slot 1 „ACDC“ (bei fx4b per Program Change, weil dort der gemerkte Slot 5 startet). Regler unverändert 2 / 127 / 2 / 2 (nicht 12 Uhr, wirken mit `TX_PRE_FX` nicht auf die Aufnahme), Dateiname deshalb mit `gvar`. Rack und Verkabelung während der Sitzung nicht verändert (Nutzer gebeten).

**Reihenfolge:** `B6b-fx4b-r1/r2` (23:07) → Flash fx3l (`firmware/flashlog/20261117_build5c-fx3l-kontrolle/`, Readback bytegleich, A1: `v22.4.r-fx3l`, `SR/BS/CH 48000 8 4`, Slots 1–5) → `B6b-fx3l-r1/r2` (23:12) → Flash fx4b (`…_build6b-fx4b-zurueck/`, Readback bytegleich, A1: `v22.4.r-fx4b`) → `B6b-fx4b-end-r1/r2` (23:16). Die Kontrolle liegt also in der Mitte, der Prüfling am Anfang und am Ende. Tabelle `out/B6b-session-table.md`.

**Ergebnis** (Datei-dBFS, Mittel über 4 Kanäle; Δ gegen das Mittel der fx3l-Kontrolle):

| Messung | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| fx4b Start (r1/r2) | −73,08 / −73,01 (−0,17) | −78,42 / −78,52 (−0,35) | −75,17 / −75,07 (−0,05) | −83,93 / −83,59 (−0,38) | −116,5 / −117,0 |
| **fx3l Kontrolle** (r1/r2) | −72,79 / −72,96 | −78,15 / −78,09 | −74,91 / −75,23 | −83,42 / −83,34 | −111,8 / −111,4 |
| fx4b Ende (r1/r2) | −72,71 / −72,85 (+0,10) | −78,17 / −78,07 (0,00) | −74,78 / −75,06 (+0,15) | −83,40 / −83,35 (+0,01) | −113,1 / −113,1 |
| **fx4b alle vier** | (−0,03) | (−0,17) | (+0,05) | (−0,18) | am Grundrauschen |

- Kamm-f0 999,8676–999,8677 Hz in allen Läufen. Meldungen: nur `tx ovf …` (Stream-Start), CPU 6–7 %.
- Gegen fx3l vom Vortag (D48): fx3l heute RMS −0,2, Rest +0,4, Kamm −0,5, fs/8 0,0 dB.

**Deutung:**
- [gemessen] **fx4b ist beim Rauschen gleich fx3l.** Alle vier Familien liegen im Mittel innerhalb ±0,2 dB, die Einzelpaare innerhalb ±0,4 dB. Das ist die Streuung zwischen Läufen (D35) bzw. die Drift in der Sitzung (Rest: Start −0,35, Ende 0,00).
- Das Kriterium aus Build 3 (keine Familie mehr als 0,5 dB schlechter) ist erfüllt. Der Boot-Menü-Code und die zusätzliche Abfrage in `onLoop` kosten nichts Messbares.
- Die Mischprodukte liegen bei −111…−117 dB am Grundrauschen, die Unterschiede dort sagen nichts.
- **Damit ist die Abnahme von Build 6/6b vollständig** (Menü D52/D53, Loop D57, Rauschen D58). Den 30-s-Timeout hat am Gerät noch niemand gestoppt.

**Nebenbefund: Linien bei 2200,95 / 4401,90 / 6602,85 Hz** in allen sechs Aufnahmen, beide Builds, stärkste auf Kanal 1 (4401,90 Hz: −91,8 dB, 2200,95 Hz: −96,6 dB), Kanal 3 am schwächsten (−97,3 dB).
- Frequenz über 11 min und zwei Flashes auf ≤ 0,001 Hz gleich. [Hypothese] Das spricht gegen einen analogen Oszillator und für eine quarzgenaue Quelle. Der Nutzer prüft es durch Verstimmen seines Oszillators (folgt).
- In D25 standen „4400, 6604 Hz“ als Harmonische des Oszillators. Ob das dieselben Linien waren, ist offen.
- Daneben wieder k·fs/48 (2000,0002 und 3000,0003 Hz, ≈ −98…−100 dB), bei fx3l und fx4b gleich (offener Punkt aus D42/D44).

**Nachtrag D58 – Oszillator verstimmt (`B6b-osc-detuned`, 30 s, 23:2x) [gemessen]:** Der Nutzer hat seinen Oszillator deutlich verstimmt, sonst nichts geändert. Pegel auf Kanal 1, direkt bei der Linienfrequenz gemessen (Hann, ganze Aufnahme, Dateiwerte ohne die Linien-Skalierung der Analyse):

| Aufnahme | 2200,95 Hz | 4401,90 Hz | 6602,85 Hz |
|---|---|---|---|
| `B6b-fx4b-end-r1` (vorher) | −102,7 dB | −97,9 dB | −104,1 dB |
| `B6b-osc-detuned` (nachher) | −102,6 dB | −97,9 dB | −104,1 dB |
| `B5c-fx3l-r1` (Vortag, Regler 12 Uhr) | −118,6 dB | −118,9 dB | −120,9 dB |

- **Die Linien wandern nicht mit: Der Oszillator ist es nicht.**
- **Am Vortag fehlten sie** (Werte am Grundrauschen). Sie sind also heute dazugekommen und in fx3l und fx4b gleich.
- Was heute anders ist: die Reglerstellung (2 / 127 / 2 / 2 statt 12 Uhr), dazu möglicherweise das Rack. [Hypothese] Die Reglerstellung: In D25 tauchten „4400, 6604 Hz“ ebenfalls bei Gain auf Vollanschlag auf und wurden damals dem Oszillator zugeschrieben. Die Quelle ist an den Gerätetakt gekoppelt (Frequenz in Geräte-Zeit auf 0,001 Hz stabil). Die Abtastrate des Regler-ADC passt nach einer groben Rechnung aus dem Code nicht dazu (≈ 100 kHz), der Mechanismus ist offen.
- Nächster Test: alle Regler auf 12 Uhr, 30 s aufnehmen. Verschwinden die Linien, hängen sie an der Reglerstellung.

**Nachtrag 2 zu D58 – Regler auf 12 Uhr (`B6b-knobs-12`, 30 s) [gemessen]:** Der Nutzer hat alle vier Regler auf 12 Uhr gestellt (gelesen 70 / 62 / 67 / 59), sonst nichts geändert. fx4b, Slot 1, Eingänge offen. Pegel direkt bei der Linienfrequenz (wie oben):

| Aufnahme | Kanal | 2200,95 Hz | 4401,90 Hz | 6602,85 Hz | fs/8 |
|---|---|---|---|---|---|
| `B6b-osc-detuned` (Regler 2 / 127 / 2 / 2) | 1 | −102,6 | −97,9 | −104,1 | −89,9 |
| | 2 | −104,1 | −99,7 | −106,6 | −90,0 |
| | 3 | −109,1 | −103,4 | −108,9 | −90,5 |
| | 4 | −105,1 | −99,9 | −104,4 | −90,1 |
| `B6b-knobs-12` (Regler 12 Uhr) | 1 | −123,6 | −118,6 | −123,0 | −88,9 |
| | 2 | −124,5 | −120,9 | −125,3 | −89,0 |
| | 3 | −128,9 | −123,6 | −127,4 | −89,5 |
| | 4 | −128,1 | −119,4 | −124,3 | −89,2 |

- **Die Linien hängen an der Reglerstellung.** Mit den Reglern auf 12 Uhr liegen sie auf allen vier Kanälen am Grundrauschen, ≈ 20 dB tiefer.
- Welcher Regler und welcher Anschlag (links oder rechts) sie auslöst, ist offen. D25 spricht für den Rechtsanschlag.
- fs/8 liegt mit 12 Uhr auf allen Kanälen ≈ 1 dB höher. Das ist eine einzelne 30-s-Aufnahme, also noch kein Befund.
- Mechanismus [Hypothese]: Der Regler-ADC läuft frei im Scan. Steht ein Schleifer am Anschlag, liegt der ADC-Eingang direkt an Masse bzw. an der Referenz, und der Ladestrom des Abtastkondensators fließt ungedämpft über die Versorgung. Die Linie wäre dann ein Mischprodukt der Scanrate mit dem Audiotakt. Dazu passt, dass sie an den Gerätetakt gekoppelt ist. Die Scanrate selbst ist nicht nachgerechnet.
- Größenordnung: −92…−97 dB in der Skala der Analyse, der Kamm liegt bei −75 dB. Die Linien sind also klein, aber im Standalone-Betrieb stehen Regler oft am Anschlag.
- **Folge für alle Rauschmessungen:** Regler auf 12 Uhr, wie im Protokoll vorgesehen. Die Sitzung D58 lief durchgehend mit 2 / 127 / 2 / 2, der Vergleich fx4b gegen fx3l bleibt deshalb gültig.

### D59 – fx4b wird Alltags-Firmware, Fork-Branch nachgezogen (2026-11-17, nachts)

**Entscheidung (Nutzer):** fx4b (`acdc1-build6b-fx4b`, `a21f35c9…`) ist die Alltags-Firmware von acdc1. Grundlage: Boot-Menü am Gerät geprüft (D52/D53), Loop-Test (D57), Rauschen gleich fx3l (D58).

**Fork `m9dfukc/OpenWare`, Branch `acdc/fx1d` (lokal committet, nicht gepusht):** `7ef6284a` Boot-Menü (Patch 15b), `2c963e3a` Version `v22.4.r-fx4b`, `27d3630b` README.

**Prüfung [gemessen]:** `tools/build_acdc.sh verify-fx1d-2c963e3a 2c963e3a …` ohne Patches und ohne `FW_VERSION` ergibt 108 496 B, SHA-256 `a21f35c990cc33737620597d883c4bd205fc4495bf2291a1b6013af6f2b06307`, **bytegleich mit dem geflashten fx4b**.

**Offen:** Push des Fork-Branches und Release `acdc-v22.4.r-fx4b` (je mit Freigabe). Hörurteil zu Tanh3 Fassung 2. Die Punkte aus D54 (MIDI-Wettlauf), D56 (Last von Tanh3) und D58 (Regler-Linien).

**Nachtrag D59 (2026-11-17, Freigabe des Nutzers):** Fork-Branch `acdc/fx1d` (Spitze `27d3630b`) und die Workbench sind gepusht. Release am Fork: `acdc-v22.4.r-fx4b`, Tag auf `27d3630b`, Dateien `ACDC-v22.4.r-fx4b.bin` (108 496 B, `a21f35c9…`) und `BUILD_INFO-v22.4.r-fx4b.txt`.


### D60 – Reglerserie K1: Welche Regler und welcher Anschlag heben die Linien bei 2200,95 Hz? (2026-11-18, 13:27–13:42)

**Setup:** acdc1, fx4b, Alltags-Kette, Eingänge offen, Slot 1 „ACDC“ (per Program Change, vorher lief Tanh3). Geführte Serie mit `tools/knob_series.py --series K1`: Das Werkzeug liest die Regler als CC 20–23, wartet auf die Stellung und nimmt dann mit `tools/acdc_rec.py` 30 s auf (duplex, Nullen am Ausgang, `--owl-read`). Zehn Aufnahmen `K1-01-MMMM` … `K1-10-MMMM`: alle auf 12 Uhr, dann jeder Regler einzeln am Links- und am Rechtsanschlag (die anderen auf 12 Uhr), am Ende wieder alle auf 12 Uhr. Gelesene Werte: Anschläge 2 und 127, „12 Uhr“ 54…73. Zwischen `K1-02` und `K1-03` lagen etwa 6 min Pause. Tabelle mit allen Kanälen: `out/K1-session-table.md`, Werte: `out/K1-lines.json`, Geräte-Reports: `out/owl_read/K1-*`.

**Auswertung:** `tools/line_levels.py` (neu): Pegel direkt bei der Linienfrequenz, Hann über die ganze Aufnahme, Datei-dBFS. Es trifft die Handwerte aus D58 auf 0,1 dB. Der Abstand zum Grundrauschen ist dieselbe Messung an 42 Stellen neben der Linie (Median), Rauschen allein ergibt ≈ 0 dB.

**Ergebnis** (Leistungsmittel über 4 Kanäle, Δ gegen das Mittel der beiden 12-Uhr-Kontrollen):

| Aufnahme | Regler 1–4 | 2200,95 Hz | 4401,90 Hz | 6602,85 Hz | 8549,33 Hz | Summe der ersten drei |
|---|---|---|---|---|---|---|
| `K1-01-MMMM` (Kontrolle) | 12 Uhr | −125,5 | −120,3 | −125,0 | −136,3 | −118,1 |
| `K1-02-LMMM` | 1 links | −112,5 (+11,9) | −102,0 (+16,6) | −109,1 (+14,8) | −115,5 (+16,6) | −100,9 |
| `K1-03-RMMM` | 1 rechts | −110,4 (+14,0) | −105,3 (+13,3) | −110,1 (+13,8) | −116,0 (+16,1) | −103,2 |
| `K1-04-MLMM` | 2 links | −110,4 (+14,0) | −102,2 (+16,5) | −111,1 (+12,7) | −116,7 (+15,4) | −101,1 |
| `K1-05-MRMM` | 2 rechts | −111,2 (+13,2) | −105,9 (+12,8) | −111,1 (+12,7) | −116,0 (+16,1) | −103,8 |
| `K1-06-MMLM` | 3 links | −108,1 (+16,3) | −102,8 (+15,8) | −110,1 (+13,7) | −118,8 (+13,3) | −101,1 |
| `K1-07-MMRM` | 3 rechts | −113,0 (+11,5) | −104,3 (+14,4) | −117,8 (+6,0) | −115,3 (+16,8) | −103,6 |
| `K1-08-MMML` | 4 links | −108,4 (+16,0) | −100,7 (+17,9) | −115,0 (+8,8) | −115,1 (+17,0) | −99,9 |
| `K1-09-MMMR` | 4 rechts | −107,1 (+17,4) | −105,8 (+12,9) | −121,5 (+2,4) | −117,8 (+14,3) | −103,3 |
| `K1-10-MMMM` (Kontrolle) | 12 Uhr | −123,6 | −117,5 | −123,0 | −130,0 | −115,6 |

- Die Linienfrequenzen sind in allen zehn Aufnahmen gleich: 2200,950 / 4401,900 / 6602,850 Hz (Raster 0,008 Hz).
- fs/8 (6000 Hz): −90,6 dB in `K1-01` und `K1-02`, danach −88,4…−88,9 dB in allen acht Aufnahmen. Der Sprung liegt in der Pause, nicht an einem Regler.

**Deutung:**
- [gemessen] **Jeder der vier Regler hebt die Linien an, und zwar an beiden Anschlägen.** Die Frage „welcher Regler, welcher Anschlag“ aus D58 ist damit beantwortet: alle, beide. Ein einzelner Regler am Anschlag hebt die drei Linien zusammen um 13…17 dB über das Mittel der 12-Uhr-Kontrollen.
- [gemessen] **Der Linksanschlag wirkt stärker als der Rechtsanschlag, welcher Regler es ist, zählt kaum.** Summe der drei Linien: links −99,9…−101,1 dB, rechts −103,2…−103,8 dB. Der Unterschied steckt vor allem in 4401,90 Hz (links ≈ 3,5 dB mehr).
- [gemessen] **Auf 12 Uhr sind die Linien nicht weg.** Sie liegen in beiden Kontrollen 6…16 dB über dem Grundrauschen. Das gilt auch für `B6b-knobs-12` (7…17 dB) und für `B5c-fx3l-r1` vom 2026-11-16 (15…18 dB bei 60 s). D58 schrieb „am Grundrauschen“, das war zu grob: Die Regler am Anschlag verstärken eine Linie, die es immer gibt.
- [gemessen] Die Endkontrolle liegt 2…3 dB über der Startkontrolle (Summe −115,6 gegen −118,1 dB). Die Regler standen am Ende etwas anders (Regler 1/2/4: 70/62/58 → 72/67/54). Ob das die Ursache ist oder Drift, ist offen.
- [gemessen] Eine vierte Linie bei **8549,33 Hz** kommt mit jedem Anschlag (+13…+17 dB, −115…−119 dB), dazu 10750,3 Hz (= 8549,33 + 2200,95) und die vierte Harmonische 8803,80 Hz. 8549,33 Hz ist kein Vielfaches von 2200,95 Hz.
- D58 mit 2 / 127 / 2 / 2 (drei Regler links, einer rechts) lag auf Kanal 1 bei −102,6 / −97,9 / −104,1 dB, also 2…8 dB über Regler 1 allein am Linksanschlag (`K1-02`). Mehr Regler am Anschlag heben die Linien weiter an (anderer Tag, deshalb nur als Hinweis).

**Nebenbefund: Die Scanrate des Regler-ADC steht im Spektrum [Code, gemessen].**
- [Code] ADC1 läuft frei im Scan über 4 Kanäle: 12 Bit, Abtastzeit 64,5 Takte, ADC-Takt = HCLK/4 (`ACDC/Core/Src/main.c`). Mit HCLK = 240 MHz, dem festen Teiler 2 des H7 und 6,5 Takten Wandlung je Kanal (Werte für Teiler und Wandlung aus dem Gedächtnis, nicht nachgeschlagen) sind das 30 MHz / 284 = **105 633,80 Hz**. Gefaltet an 2 × 48 kHz ergibt das 9633,80 Hz, die zweite Harmonische 19 267,61 Hz.
- [gemessen] Beide Linien stehen in allen K1-Aufnahmen: 9633,80 Hz bei −116…−120 dB (14…20 dB über dem Grundrauschen), 19 267,6 Hz bei −118…−129 dB. Auch `B5c-fx3l-r1` und `B6b-fx3l-r1` zeigen 9633,82 Hz. Eine Gegenrechnung mit 288 Takten (8166,67 Hz) liegt am Grundrauschen.
- [gemessen] **Gegenprobe an acdc2** (`S2-1`, `S2-2`, v22.4.q, Abtastrate 47 991,07 Hz): Dort liegt die Linie bei 9653,46 Hz und 19 306,91 Hz. Erwartet für eine Quelle bei 105 633,8 Hz, die am Quarz hängt: (105 633,8 − 2 × 47 991,07) × 48 000 / 47 991,07 = 9653,46 Hz. Aus der Verschiebung zwischen den Modulen (19,65 Hz) folgt die Quellfrequenz auch ohne den Code: ≈ 105,61 kHz ± 0,04.
- Diese Linien hängen kaum an der Reglerstellung (9633,80 Hz: −1,3…+2,2 dB gegen die Kontrollen).
- **Die Reglerlinien selbst passen nicht zur Scanrate.** Die Harmonischen von 105 633,8 Hz falten auf 9633,8 / 19 267,6 / 19 098,6 / 9464,8 / 169,0 Hz usw., 2200,95 Hz und 8549,33 Hz sind nicht darunter. Geprüft und verworfen sind auch: LED-PWM (siehe unten), ganzzahlige Teiler von 30, 60 und 240 MHz bis auf 13 ppm (zu ungenau, die Linie steht auf ≈ 4 ppm fest). Die Quelle der Reglerlinien ist offen.

**Zwei weitere Linien lassen sich aus dem Takt ableiten:**
- [Code, gemessen] **LED-PWM auf acdc1 = 2320,54 Hz**, nicht 2320,98 Hz: Timer-Takt 240 MHz / (101 × 1024) = 2320,5446 Hz. In den K1-Aufnahmen stehen 2320,54 / 4641,09 / 6961,63 Hz bei −119…−124 dB (8…15 dB über dem Grundrauschen), unabhängig von den Reglern. Die 2320,98 Hz aus M2/S2 gelten für acdc2: 2320,5446 × 48 000 / 47 991,07 = 2320,98 Hz.
- [Hypothese] **Die Linien bei 2000,0002 und 3000,0003 Hz (D42, D44, D58) sind Vielfache des 1-kHz-Systemtakts.** Laut PLL3-Einstellung läuft der Codec mit 47 999,9951 Hz in Quarz-Zeit [Code], ein Quarz-genauer 1-kHz-Takt erscheint dann bei 1000,0001 Hz. Das passt auf die Nachkommastellen. Welcher Takt es ist (FreeRTOS-Tick, SysTick), ist nicht geprüft.

**Mechanismus der Reglerlinien [Hypothese]:** Am Anschlag liegt der Schleifer an Masse oder an der Referenz, auf 12 Uhr liegen alle vier Eingänge nahe derselben Spannung. Im Scan muss der Abtastkondensator bei einem Regler am Anschlag zweimal je Durchlauf um ≈ 1,65 V umgeladen werden, bei vier Reglern auf 12 Uhr fast gar nicht. Das erklärt „jeder Regler, beide Anschläge“ und den Hinweis aus D58, dass mehr Regler am Anschlag mehr bringen. Es erklärt nicht die Frequenz. Vorhersage für den nächsten Test: Stehen alle vier Regler am selben Anschlag (LLLL oder RRRR), sind die Linien so schwach wie auf 12 Uhr, bei LRLR am stärksten. Kommen sie bei LLLL trotzdem, liegt es am Anschlag selbst (z. B. ADC-Wert am Bereichsende) und nicht am Spannungsunterschied zwischen den Kanälen.

**Einschränkungen:** Je Stellung eine Aufnahme von 30 s, keine Wiederholung. Die Kontrollen unterscheiden sich um 2…3 dB, kleinere Unterschiede zwischen Reglern sagen deshalb nichts. Im Band 100…1300 Hz liegen schwache, wandernde Töne aus dem Rack (z. B. 740, 962, 1025 Hz), die nichts mit den Reglern zu tun haben. Größenordnung: Ein Regler am Anschlag bringt zusammen ≈ −100 dB, der Kamm liegt bei −75 dB, fs/8 bei −89 dB.

**Fazit:** Für Aufnahmen spielt die Reglerstellung fast keine Rolle (25 dB unter dem Kamm). Die Regel „Rauschmessungen mit Reglern auf 12 Uhr“ bleibt. Nächster Schritt: Serie K2 mit LLLL, RRRR, LRLR und einem Regler in Zwischenstellungen.

### D61 – Reglerserie K2: Nicht der Anschlag zählt, sondern der Unterschied zwischen den Reglern (2026-11-18, 13:52–14:02)

**Setup:** wie D60, gleiche Sitzung, Rack unverändert. `tools/knob_series.py --series K2 --steps MMMM LLLL RRRR LRLR LLRR 8,M,M,M 24,M,M,M 44,M,M,M MMMM`, neun Aufnahmen von 30 s. Buchstaben und Zahlen stehen für Regler 1–4 in dieser Reihenfolge (L = Linksanschlag, R = Rechtsanschlag, M = 12 Uhr, Zahl = CC-Wert). Gelesene Werte und alle Kanäle: `out/K2-session-table.md`, `out/K2-lines.json`.

**Ergebnis** (Leistungsmittel über 4 Kanäle, Datei-dBFS, `tools/line_levels.py`):

| Aufnahme | Regler gelesen | 2200,95 Hz | 4401,90 Hz | 6602,85 Hz | 8549,33 Hz | Summe der ersten drei |
|---|---|---|---|---|---|---|
| `K2-01-MMMM` (Kontrolle) | 72 / 67 / 69 / 54 | −123,2 | −118,0 | −123,7 | −129,6 | −116,0 |
| `K2-02-LLLL` | 2 / 2 / 2 / 2 | −127,9 | −120,3 | −129,3 | −134,6 | **−119,2** |
| `K2-03-RRRR` | 127 / 127 / 127 / 127 | −118,8 | −116,0 | −125,6 | −131,0 | **−113,9** |
| `K2-04-LRLR` | 2 / 127 / 2 / 127 | −109,9 | −94,6 | −108,2 | −103,1 | **−94,3** |
| `K2-05-LLRR` | 2 / 2 / 127 / 127 | −102,1 | −110,6 | −104,2 | −118,0 | **−99,6** |
| `K2-06-8MMM` | 8 / 62 / 63 / 62 | −112,4 | −102,1 | −109,9 | −116,2 | −101,1 |
| `K2-07-24-M-M-M` | 24 / 62 / 63 / 62 | −116,8 | −104,5 | −112,8 | −119,2 | −103,7 |
| `K2-08-44-M-M-M` | 42 / 62 / 63 / 62 | −121,2 | −107,9 | −117,7 | −123,5 | −107,3 |
| `K2-09-MMMM` (Kontrolle) | 60 / 63 / 63 / 62 | −125,0 | −114,7 | −133,2 | −134,5 | −114,2 |

- Linienfrequenzen wie in D60: 2200,950 / 4401,900 / 6602,850 Hz, die vierte bei 8549,33…8549,35 Hz.
- Die Linien der ADC-Scanrate bleiben in allen neun Aufnahmen gleich: 9633,80 Hz −117,1…−118,4 dB, 19 267,6 Hz −121…−129 dB. LED-PWM 2320,54 Hz −117,5…−122,1 dB, fs/8 −88,8…−90,8 dB.

**Deutung:**
- [gemessen] **Die Vorhersage aus D60 trifft zu: Der Anschlag selbst ist es nicht.** Mit allen vier Reglern am Linksanschlag (−119,2 dB) oder am Rechtsanschlag (−113,9 dB) liegen die Linien im Bereich der 12-Uhr-Kontrollen (−116,0 und −114,2 dB). LLLL ist die leiseste Aufnahme der Serie.
- [gemessen] **Es zählt der Unterschied zwischen den Reglern.** LRLR bringt −94,3 dB, das sind 21 dB über den Kontrollen und 6…7 dB über einem einzelnen Regler am Linksanschlag (D60: −99,9…−101,1 dB). LLRR liegt bei −99,6 dB.
- [gemessen] **Der Pegel wächst stetig mit dem Abstand eines Reglers von den anderen.** Regler 1 gegen die anderen drei auf ≈ 62: Abstand 20 → −107,3 dB, Abstand 38 → −103,7 dB, Abstand 54 → −101,1 dB, Anschlag (D60, `K1-02`) → −100,9 dB. Eine Schwelle am Anschlag gibt es nicht.
- [gemessen] **Das Muster der Regler bestimmt, welche Linie führt.** LLRR (ein Wechsel hin und einer zurück je Durchlauf durch die vier Regler) hebt 2200,95 und 6602,85 Hz, also Grundton und dritte Harmonische. LRLR (zwei solche Wechsel je Durchlauf) hebt 4401,90 Hz, also die zweite, dazu 8549,33 und 8803,80 Hz. [Hypothese] 2200,95 Hz steht für einen Durchlauf durch die vier Regler in der Reihenfolge 1-2-3-4, wie ihn der ADC-Scan macht.
- Ein Rest bleibt auch bei fast gleichen Reglern: `K2-09` mit 60 / 63 / 63 / 62 liegt bei −114,2 dB, 4401,90 Hz allein bei −114,7 dB.
- Das stützt den Mechanismus aus D60 [Hypothese]: Der Abtastkondensator des ADC wird von Kanal zu Kanal umgeladen, und die Ladung wächst mit dem Spannungsunterschied zwischen aufeinanderfolgenden Kanälen. Gemessen ist nur die Abhängigkeit, nicht der Strom.
- **Offen bleibt die Frequenz.** Der Scan läuft mit 105 633,8 Hz (D60), und seine eigenen Linien bei 9633,80 und 19 267,6 Hz reagieren nicht auf das Reglermuster, auch nicht bei LRLR. Das Reglermuster erscheint dagegen bei 2200,95 Hz und Vielfachen. Zwischen beiden liegen 103 432,86 bzw. 107 834,76 Hz. Ein Takt mit dieser Frequenz oder einem Teiler davon ist im Code bisher nicht gefunden (geprüft: 48 kHz und Vielfache, 6 kHz, 1 kHz, LED-PWM, USB-SOF).

**Nebenbefund [gemessen, einzelne Aufnahme]:** In `K2-03-RRRR` liegen die Mischprodukte aus fs/8 und Kamm (z. B. 3000,40 = 6000 − 3 × 999,868 Hz, 4000,27, 7999,73, 10 000,27 Hz) bei −117…−121 dB und damit 12…17 dB über beiden Kontrollen. In den anderen Aufnahmen fällt das nicht auf. Ob es an den vier Reglern am Rechtsanschlag liegt (voller Gain im laufenden Default-Patch), ist ohne Wiederholung offen.

**Einschränkungen:** Je Stellung eine Aufnahme von 30 s. Die Zuordnung der ADC-Kanäle (Rang 1–4 = Kanal 10, 11, 14, 3) zu den Reglern 1–4 ist nicht am Schaltplan geprüft. Wandernde Töne aus dem Rack bei 1500…1650 Hz wie in D60.

**Fazit:** Wer die Linien klein halten will, stellt die vier Regler ähnlich, wohin auch immer. Für Rauschmessungen reicht „alle auf 12 Uhr“ weiter aus. Eine Abhilfe in der Firmware (ADC nicht frei laufen lassen, z. B. ein Scan je Audioblock, oder längere Abtastzeit) ist erst sinnvoll, wenn klar ist, woher 2200,95 Hz kommt. Größenordnung im schlimmsten Fall (LRLR): −94 dB, 19 dB unter dem Kamm.

### D62 – MIDI-Sendeweg: Fehler auf fx4b reproduziert, Patch 16 und Build 7 `fx5a` (2026-11-18, nachmittags)

**Anlass:** D53/D54. Ziel war ein Test, der den Fehler verlässlich auslöst, und ein Fix.

**Werkzeug:** `tools/dump_stress.py` lädt bei laufendem Patch alle belegten Slots in Runden herunter und prüft jeden Download gegen Größe und CRC aus der Slot-Liste. Es schreibt `out/<name>-session-table.md` und `out/dump_stress/<name>.json`. Nur lesend, bis auf einen Program Change (RAM). Antwortet das Gerät nach einem beschädigten Download nicht mehr, bricht es ab.

**Basislinie fx4b [gemessen]:** `D62-fx4b-slot2`, 15:42, Slot 2 TapeDelay läuft (32 % CPU), Alltags-Kette.

| Slot | Patch | Größe B | in Ordnung | beschädigt |
|---|---|---|---|---|
| 1 | ACDC | 10 164 | 13 | 3 |
| 2 | TapeDelay | 30 036 | 13 | 3 |
| 3 | Grainz | 26 700 | 9 | 7 |
| 4 | RingsReverb | 21 556 | 12 | 4 |
| 5 | Tanh3 | 18 580 | 13 | 2 |
| Summe | | | 60 | 19 |

- **19 von 79 Downloads beschädigt (24 %).** Bei 18 davon kamen alle Pakete mit richtigem Index an, in den Nachrichten fehlten aber 49…183 B.
- **Der Hänger aus D53 trat auf:** Runde 16, Slot 4, nach 18 Paketen kam nichts mehr, auch keine Geräte-ID. Der Ton lief weiter. Der Nutzer hat acdc1 neu gestartet.
- Damit ist der Hänger eine Folge des Downloads bei laufendem Patch [gemessen]. Die Stelle im Code ist weiter [Hypothese].

**Ursachen im Original-Code [Code]** (ergänzt D54, `Source/MidiWriter.cpp`, `usbd_audio.cpp`, `MidiController.cpp`, Stand `27d3630b`, in `upstream/master` gleich):
1. Drei Kontexte schreiben in den Sendepuffer: Audio-Task, Hauptschleife und der USB-Interrupt. SysEx-Anfragen werden im Interrupt verarbeitet (`usbd_midi_rx` → `readMidiFrame`), die Antworten entstehen dort. `SerialBuffer::push` und `incrementReadHead` sind nicht unteilbar.
2. `write()` ruft `transmit()` an jedem Pufferumlauf (`getContiguousWriteCapacity() <= 4`), beim Download etwa alle drei Nachrichten. Dort trifft die Hauptschleife auf den Audio-Task, der `transmit()` in jedem Block ruft. `usbd_midi_tx()` sendet bei gesetzter Sperre nichts, der Lesezeiger rückt trotzdem vor.
3. Bestehen beide die Prüfung der Sperre, starten sie zweimal auf demselben Endpoint. `HAL_PCD_EP_Transmit` überschreibt dabei `xfer_buff`, `xfer_len`, `xfer_count` und `DIEPTSIZ` der laufenden Übertragung. [Hypothese] Das ist der Hänger.
4. Der Lesezeiger rückt beim Start der Übertragung vor. USB kopiert die Daten erst danach paketweise (64 B, im Interrupt) aus dem Ringpuffer. Ein Schreiber kann sie überschreiben.
5. `write()` prüft nie, ob der Puffer voll ist. Holt der Schreibzeiger den Lesezeiger ein, gilt der Puffer als leer.
6. `SendResourceTask` schreibt alle 2 ms 324 B, ohne auf Platz zu warten.

**Absprache (Grill-Runde mit dem Nutzer, 2026-11-18):** Prüfen, Starten und Merken unteilbar. Lesezeiger erst nach Abschluss der Übertragung. Voller Puffer verwirft die neue Nachricht. Flusskontrolle im `SendResourceTask`. Keine Rettung der Sperre per Zeitablauf. Verschachtelte Nachrichten bleiben draußen. `transmit()` bleibt in Gruppe C des ITCM, das Rausch-A/B entscheidet (Grenze ±0,5 dB je Familie). Name `v22.4.r-fx5a`.

**Patch `16-midi-tx-atomic.patch` [Code]:**
- `UsbdMidiTransmitter`: Jeder Zugriff auf den Pufferzustand läuft mit gesperrten Interrupts (PRIMASK wie in Patch 05, statt BASEPRI aus der Absprache: auf dem AC/DC liegt kein Interrupt über Priorität 5, und die Datei baut so auch ohne FreeRTOS). Die laufende Länge steht in `inflight`, der Lesezeiger rückt beim nächsten Aufruf nach gelöster Sperre vor. Der DataIn-Interrupt bleibt unverändert.
- `transmit()` verlässt den Leerlauf ohne Sperre (leerer Puffer, laufende Übertragung, kein Rechner).
- `write()` verwirft bei vollem Puffer und meldet einmal `midi tx ovf`, nur mit Rechner am USB.
- `usbd_midi_tx()` gibt zurück, ob gesendet wurde.
- `SendResourceTask` schreibt nur, wenn 324 B frei sind, und gibt nach 5 s ohne Platz auf (Zusatz zur Absprache).

**Build 7 [gemessen]:** `firmware/builds/acdc1-build7-fx5a/`, `v22.4.r-fx5a`, 109 524 B, SHA-256 `b69c25b3f469fc6fb793b16569c53a63a7333c32d83c96de4d97b6fb71bdb8ef`. Patches wie fx4b + 16.
- `check_itcm.py --ref fx4b`: BESTANDEN, 0 FAIL, 0 WARN. `MidiWriter::transmit` 76 → 124 B, alles dahinter im ITCM liegt 48 B höher, ITCM-Ende 0x6308 → 0x6338, Patch-Heap 48 B kleiner. 164 von 180 RAM-Objekten an derselben Adresse (der Sendepuffer ist 8 B größer).
- Flash +1028 B, weil `write()` in `sendSysEx`, `sendCc` und `sendPc` eingesetzt wird. Frei 21 548 B.
- Leerlauf-Pfad von `transmit()` im Maschinencode: zwei Ladebefehle und ein Vergleich, ohne Sperre.

### D63 – fx5a geflasht, Download-Stresstest und Loop-Test (2026-11-18, 15:48–16:02)

**Flash (Freigabe Nutzer):** `firmware/flashlog/20261118_build7-fx5a/`, mit `tools/flash_acdc.py`. **Das Skript lief dabei zum ersten Mal am Gerät**, alle Schritte ohne Fehler: Auslesen, DFU-Neustart, Schreiben, Readback bytegleich, Rest 0xFF. Nach dem Neustart `--a1`: `v22.4.r-fx5a`, 48 000 Hz, Blockgröße 8, Slots 1–5 unverändert.

**Download-Stresstest fx5a [gemessen]:**

| Serie | Laufender Patch | CPU | Downloads | beschädigt | Hänger |
|---|---|---|---|---|---|
| `D62-fx4b-slot2` (Basislinie, D62) | TapeDelay | 32 % | 79 | 19 | ja |
| `D62-fx5a-slot2` | TapeDelay | 32…33 % | 100 | 0 | nein |
| `D62-fx5a-slot5` | Tanh3 | 51 % | 100 | 0 | nein |
| `D62-fx5a-slot5-stream` | Tanh3, dazu Audio-Stream mit Loop-Sinus | 50 % | 40 | 0 | nein |

- Geräte-Meldung nach den Serien: `Sending 100` (Fortschrittsanzeige des Downloads), kein `midi tx ovf`.
- **Reproduktionstest bestanden:** 240 von 240 Downloads in Ordnung.

**Loop-Test fx5a [gemessen]:** Patchkabel Out n → In n (Nutzer), `acdc_rec.py --sine 440 530 670 790` (−6 dBFS, 1 s Einblenden), je 60 s, Regler 60 / 63 / 63 / 62.

| ID | Laufender Patch | Slips (`phase_slips.py`) | veraltete Samples (`stale_samples.py`) | Geräte-Meldung | CPU |
|---|---|---|---|---|---|
| `B7-fx5a-loop` | Slot 1 ACDC | 0 auf allen 4 Kanälen | 0 von 96 000 je Kanal | `tx ovf 1.0000 1.0000 32` (Stream-Start) | 8 % |
| `B7-fx5a-loop-tanh3` | Slot 5 Tanh3 | 0 | 0 | `tx ovf 1.0000 1.0000 32` | 52 % |
| `B7-fx5a-loop-tanh3-dl` | Tanh3, währenddessen 40 Slot-Downloads | 0 ganze Samples | 0 | nicht gelesen (MIDI war belegt) | 50 % |

- Stream-Meldungen von PortAudio: 0 in allen drei Läufen. Pegel −6,05…−6,10 dBFS wie bei fx4b (D57).
- **Loop-Test bestanden**, auch während das Gerät MIDI sendet und dabei kurz die Interrupts sperrt.
- **Nebenbefund [gemessen, eine Aufnahme]:** Im Lauf mit Downloads meldet `phase_slips.py` auf Kanal 2 (530 Hz), und nur dort, 48 Ereignisse von ±0,0017…0,0020 Samples (≈ 0,13 mrad) zwischen 8 und 45 s, also solange die Downloads liefen. Ein Slip ist das nicht (er träfe alle Kanäle mit ganzen Samples). Es ist eine kleine Störung auf Kanal 2 während der Downloads. Ob fx4b sie auch zeigt, ist nicht gemessen. Kandidaten [Hypothese]: Lesen aus dem QSPI-Flash, Fortschrittsanzeige.

### D64 – Build-7-Sitzung: Rauschen fx5a gegen fx4b, offene Eingänge (2026-11-18, 15:45–16:25)

**Setup:** acdc1, Alltags-Kette, Eingänge offen, Slot 1, Regler 60 / 62…63 / 63 / 62…63, `acdc_rec.py`, je Block 2 × 60 s. Reihenfolge fx4b → fx5a → fx4b → fx5a, dazwischen je ein Flash mit Neustart (`firmware/flashlog/20261118_build7-fx5a/`, `…_build6b-fx4b-zurueck/`, `…_build7-fx5a-2/`, alle Readbacks bytegleich, A1 je bestanden). Zwischen dem ersten fx5a-Block und der zweiten Kontrolle lagen die Loop-Tests (D63), vor dem zweiten fx5a-Block etwa 14 min Pause.

Familienpegel, Mittel je Block, Δ gegen das Mittel der vier fx4b-Aufnahmen, Datei-dBFS (`out/B7-session-table.md`):

| Block | Start | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. | Kamm-f0 Hz |
|---|---|---|---|---|---|---|---|
| `B7-fx4b-a` | 15:45 | −73,23 (+0,03) | −78,58 (−0,01) | −75,47 (+0,02) | −83,19 (+0,24) | −113,53 (+1,00) | 999,8676 |
| `B7-fx5a` | 15:53 | −73,11 (+0,15) | −78,57 (0,00) | −75,31 (+0,17) | −82,96 (+0,47) | −113,45 (+1,08) | 999,8676 |
| `B7-fx4b-b` | 16:07 | −73,29 (−0,03) | −78,55 (+0,01) | −75,50 (−0,02) | −83,69 (−0,26) | −115,83 (−1,30) | 999,8676 |
| `B7-fx5a-b` | 16:22 | −72,99 (+0,27) | −78,27 (+0,29) | −75,15 (+0,33) | −83,60 (−0,17) | −114,25 (+0,28) | 999,8665…999,8671 |
| fx5a, alle vier | | −73,05 (+0,21) | −78,42 (+0,15) | −75,23 (+0,25) | −83,27 (+0,16) | −113,83 (+0,70) | |

**Deutung:**
- [gemessen] **fs/8 und Mischprodukte folgen der Sitzung, nicht dem Build.** Beide lagen in der ersten Hälfte höher (fx4b-a und fx5a) und in der zweiten tiefer (fx4b-b und fx5a-b). Die beiden fx4b-Kontrollen liegen bei fs/8 0,5 dB und bei den Mischprodukten 2,3 dB auseinander. Im Mittel aller Aufnahmen: fs/8 +0,16 dB, Mischprodukte +0,70 dB.
- [gemessen] **RMS, Rest und Kamm:** erster fx5a-Block innerhalb +0,17 dB. Im zweiten Block liegen Rest (+0,29 dB) und Kamm (+0,33 dB) höher, zugleich ist die Kammfrequenz um 0,5…1 mHz gewandert. Der Rest enthält keine Störlinien, sein Anstieg spricht für eine Änderung der Umgebung nach der Pause, nicht für den Build [Hypothese].
- **Gegen die vereinbarte Grenze von ±0,5 dB:** RMS, Rest, Kamm und fs/8 liegen in jedem Block darin. Die Mischprodukte liegen im ersten Block (+1,08 dB) und im Mittel (+0,70 dB) darüber, bei einer Streuung der Kontrolle von 2,3 dB. Die Familie liegt bei −113…−116 dB, 38 dB unter dem Kamm.
- **Fazit:** Kein Hinweis, dass Patch 16 das Rauschen ändert. Für die Mischprodukte ist die Sitzung zu unruhig für ein Urteil auf 0,5 dB. Die 48 B Verschiebung im ITCM (auch des USB-Codes) zeigen keine Wirkung, die über die Streuung hinausgeht.

**Stand nach der Sitzung:** Auf acdc1 läuft fx5a (`b69c25b3…`), Slot 1 per Program Change, gemerkter Slot weiter 5. Slots unverändert. Ob fx5a Alltags-Firmware wird, entscheidet der Nutzer. Rückweg fx4b (`a21f35c9…`).

**Offen:** Entscheidung über fx5a. Störung auf Kanal 2 während Downloads (D63). Verschachtelte MIDI-Nachrichten. Fork-Commit, Push und Release je mit Freigabe.

### D65 – fx5a ist die Alltags-Firmware (2026-11-18, nachmittags)

**Entscheidung (Nutzer):** fx5a (`acdc1-build7-fx5a`, `b69c25b3…`) ist die Alltags-Firmware von acdc1 und löst fx4b ab. Grundlage: Download-Stresstest und Loop-Test (D63), Rauschen ohne Hinweis auf eine Änderung (D64). fx4b (`a21f35c9…`) ist der erste Rückweg.

**Offen:** Fork-Commit auf `acdc/fx1d`, Push und Release `acdc-v22.4.r-fx5a` (je mit Freigabe), `docs/en/05` auffrischen. Die Punkte aus D63 (Störung auf Kanal 2 während Downloads) und D64 (Mischprodukte nicht entscheidbar).

**Nachtrag D65 – Fork:** Der Branch `acdc/fx1d` ist lokal nachgezogen: `bd04588e` (Patch 16), `c222fa49` (Version), `b4b95e43` (README). Ein Build von `c222fa49` ohne Patches ist bytegleich mit fx5a (`firmware/builds/verify-fx1d-c222fa49`, `b69c25b3…`). Gepusht ist nichts.

**Nachtrag 2 zu D65:** Fork-Branch `acdc/fx1d` (`b4b95e43`) und Workbench gepusht, Release `acdc-v22.4.r-fx5a` am Fork angelegt (Tag auf `b4b95e43`, reguläres Release, „Latest“), je mit Freigabe des Nutzers.

### D66 – Patch „Schliere“: lange Allpass-Kette, Host-Test, Slot 6 (2026-11-18, 17:33–17:41)

**Anlass (Nutzer):** Ein weiterer eigener Patch für Slot 6, nach dem Vorbild eines digitalen Eurorack-Moduls mit zwei Allpass-Sektionen zu je 98 Polen. Nachgebaut ist eine Sektion: mono hinein, stereo heraus, dazu zwei abgeleitete Signale. Grundlage waren das Handbuch des Vorbilds (v1.2.1) und der Forum-Thread des Herstellers (vom Nutzer als Datei geliefert).

**Aufbau [Code]:** `owl/schliere/SchlierePatch.hpp`, 61 gleiche Allpässe 2. Ordnung in Reihe (1 Stufe = 2 Pole).
- Regler 1–4: Frequency (20 Hz…20 kHz), Resonance (Q 0,01…16), Tap (sieben Rastpunkte mit Haltezonen, dazwischen Überblendung), Feedback (0…97 %).
- In 1 Audio oder CV (Vorwärtsweg DC-gekoppelt), In 2 Frequency-CV 1 V/Okt ohne Totzone, In 3 Tap-CV, In 4 Feedback-CV (unter null negatives Feedback), In 3/4 mit Totzone ±0,5 V.
- Out 1 (L): Abgriffe 2, 18 … 98 Pole. Out 2 (R): 2, 22 … 122 Pole. Out 3: (L − R)/2. Out 4: Ende der Kette (122 Pole).
- Feedback von Out 1 über Hochpass 10 Hz und weiche Begrenzung (ab 5 V) auf den Eingang, Eingang mit √(1 − fb²) abgesenkt. Ausgänge linear bis 7,5 V, höchstens 9,8 V.
- LEDs 1–3: Rastpunkt binär, LED 4: Feedback, Rot = Begrenzung in der Schleife.

**Filterform, Vergleich am Rechner [gemessen, Host]:** 61 Stufen in float, 1-kHz-Sinus, Rest neben dem Sinus nach 8 s.

| Mittenfrequenz, Q | Direktform (2 Multiplikationen) | Zustandsvariablenfilter |
|---|---|---|
| 100 Hz, Q 16 | −70,5 dB | −114,7 dB |
| 100 Hz, Q 0,5 | −81,1 dB | −124,3 dB |
| 1 kHz, Q 16 | −83,9 dB | −102,7 dB |
| 1 kHz, Q 0,01 | −69,9 dB | −120,1 dB |
| 10 kHz, Q 16 | −124,4 dB | −134,5 dB |

Gewählt ist das Zustandsvariablenfilter (trapezförmige Integration, Allpass = Eingang − 2k · Bandpass). Bei 20 Hz stecken in den Zahlen noch Einschwingreste (Laufzeit der Kette bis ≈ 30 s), sie sind deshalb nicht aufgeführt.

**Host-Test [gemessen, Host]:** `tools/test_owl_dsp.sh`, neu `owl/test/schliere_test.cpp`, 25 Fälle, alle bestanden (auch mit `-O3 -ffast-math` wie im Patch-Build). Übertragungsfunktion aus der Impulsantwort.
- Eine Stufe gegen die Lehrbuchformel, Q 0,01 … 16: Fehler höchstens 2 · 10⁻⁵.
- Gruppenlaufzeit bei 98 Polen, Q 16: 0,5005 s bei 1 kHz, 1,2483 s bei 400 Hz. Das Handbuch nennt 0,50 und 1,25 s.
- Zwischen den Rastpunkten 4 und 5: 8 Kerben an L (Handbuch: 8), 10 an R.
- Auf einem Rastpunkt ohne Feedback: Pegel höchstens 0,0007 dB neben flach.
- Feedback 90 %, kleines Signal: Spitzen +12,7 dB, Täler −12,8 dB (Rechnung ±12,8 dB), mit negativem Feedback vertauscht.
- Gleichspannung: läuft mit Faktor 1 durch, bei Feedback 90 % mit √(1 − fb²), wird also nicht verstärkt.
- 9 V Rechteck plus Rauschen bei vollem Feedback und Q 16: Ausgänge höchstens 0,968 (9,7 V), endlich. Die Schleife klingt aus (−139 dB nach 12 s), keine Selbstschwingung.
- Modulation aller CV-Eingänge mit Audio-Rate und Frequenzsprünge über 4 Oktaven bei Q 16: endlich, keine Pegelspitze.

**Build:** `SRC=owl tools/build_owl_patch.sh Schliere SchlierePatch SchlierePatch.hpp`, OWL3, patchram. `owl-patches/builds/Schliere/`: 17 196 B, CRC `0x99171e91`, `patch.bin` `bf9c0c5d…`, Quelle `e1407810…`.

**Am Gerät (acdc1, fx5a) [gemessen]:**
1. Vorher (`out/owl_read/acdc1/20261118_173350/`): Slot 1 „ACDC“ läuft, CPU 5 %, Slots 1–5 belegt, Storage 108 032 B.
2. `owl_write.py Schliere.syx --run` (17:34): 84 Pakete in 1,4 s, läuft aus dem RAM.
3. **CPU 28 %**, drei Lesungen, Regler 61–63 von 127 (alle um 12 Uhr), Speicher 1040 B.
4. Das Gerät war danach kurz nicht am USB. Ein erster Store-Versuch brach deshalb ab, bevor etwas gesendet wurde („MIDI port not found“).
5. Wieder am USB (17:39): Schliere lief weiter aus dem RAM, CPU 28 %, Slot 6 frei.
6. `owl_write.py Schliere.syx --store 6 --yes` (Freigabe des Nutzers): Slot 6 „Schliere“, 17 196 B, CRC `0x99171e91` zurückgelesen (`out/owl_write/acdc1/20261118/owl_write_173957.json`).
7. `owl_read.py --slots 6` (`out/owl_read/acdc1/20261118_174016/`): Download `ok`, bytegleich mit `patch.bin`. Slots 1–5 unverändert, Storage 125 440 B, Programm 6 läuft, CPU 29 % bei Reglern 25 / 69 / 35 / 51.

**Fazit:** Schliere liegt auf Slot 6 von acdc1 und braucht 28–29 % CPU [gemessen]. Die Last hängt kaum von den Reglern ab [Code: die Kette rechnet immer alle 61 Stufen].

**Einschränkungen und offen:**
- Der Nutzer hat nach dem Probelauf im RAM das Speichern freigegeben. Ein ausführliches Hörurteil steht aus.
- Übertragungsfunktion, CV-Skalierung und LEDs sind nur am Rechner geprüft, nicht am Gerät. Eine Loop-Messung (Out n → In 1, Impuls oder Sinus-Serie mit `acdc_rec.py`) fehlt.
- Die Breite der Haltezonen am Tap-Regler (je 15 % um einen Rastpunkt) ist geschätzt, das Handbuch nennt keine Zahl.
- In 2 ist nicht kalibriert. Der Offset des offenen Eingangs (−0,2…−0,4 V, D36) verstimmt um 0,2 bis 0,4 Oktaven, die Regler-Endwerte 20 Hz und 20 kHz bleiben durch eine halbe Oktave Reserve erreichbar [Code].
- Loop-Test und Rauschen unter dieser Patch-Last sind nicht gemessen. Mit Tanh3 bei 53 % war der Loop-Test bestanden (D57).
- Ob der gemerkte Slot (`ACDC.slot`) unverändert ist, wurde nicht geprüft.

**Nachtrag D66 – Fiepsen (Nutzer, 2026-11-18 abends):** Im Patch ist ein eindeutiges Fiepsen zu hören. Gemessen ist es am Gerät noch nicht, eingegrenzt wurde am Rechner.

- **Der Patch erzeugt es nicht aus seinen Eingangsdaten [gemessen, Host]:** Eine echte Aufnahme der offenen Eingänge (`20261118_acdc1_fx5a-open-inputs-7-r1…`, 40 s, alle vier Kanäle auf In 1–4) lief durch den Patch. Ohne Signal liegt Out 1 bei −81…−88 dBFS wie der Eingang (−83 dBFS), die Linien bei 1, 2, 3, 6, 12 und 18 kHz bleiben innerhalb von ±6 dB. Neue Linien entstehen nicht.
- **Der offene Frequency-Eingang ist es auch nicht [gemessen, Host]:** Mit einem Sinus (220 oder 640 Hz, 2,5 V) an In 1 erzeugen die Störlinien auf In 2 Seitenbänder bei ±1 kHz von −74…−88 dBc, mit In 2 = 0 V sind es −103…−118 dBc. Das liegt unter dem Rauschen neben dem Ton. Die Abschätzung „Phase = Laufzeit × Verstimmung“ lag 26 dB zu hoch: Eine Modulation, die schneller ist als die Laufzeit der Kette, mittelt sich über die Stufen weg. Ein versuchsweise eingebauter Tiefpass auf In 2 ist deshalb wieder entfernt.
- **Verdacht LED-PWM [Code, Hypothese]:** Fassung 1 lässt LED 1–3 auf einem Rastpunkt dauerhaft mit Wert 0,6 leuchten und LED 4 mit 0,9 × Feedback. Die Firmware dimmt Grün per PWM (`setLed()` in `ACDC.cpp`: Tastgrad = Wert, TIM2/TIM3, 2320,54 Hz). Die LED-PWM ist als Störquelle bekannt (H3 in `docs/02`: 2320 und 4641 Hz mit −75…−80 dBFS, sobald die LEDs leuchten). In den Aufnahmen und mit den anderen Patches leuchten die LEDs nur mit Signal. Schliere gibt die Eingänge mit Faktor 1 auf die Ausgänge.
- **Fassung 2 (`owl-patches/builds/Schliere/`, 17 268 B, CRC `0xcd590595`, `e2fb0332…`, Quelle `321e0cc5…`):** LEDs nur noch aus oder rot. Rot ist ein statischer Pin, Grün steht dabei auf Tastgrad 1023/1024 [Code], die Grundwelle der PWM ist damit rechnerisch 50 dB kleiner als bei 60 %. LED 4 zeigt nur noch die Begrenzung. Host-Test 26 Fälle bestanden. Fassung 1 liegt in `owl-patches/builds/Schliere-v1/` (`bf9c0c5d…`) und auf Slot 6.
- **Probe ohne neuen Build:** Tap zwischen zwei Rastpunkte und Feedback auf null stellen, dann sind in Fassung 1 alle vier LEDs aus. Verschwindet das Fiepsen, ist es die LED-PWM. Das wäre zugleich der fehlende Beweis für H3.
- **Nicht ausgeschlossen:** höhere Blockraten-Linie (6 kHz) durch die Rechenlast (D42), der Kamm am Ausgang bei gestecktem USB (D20).
- **Fassung 2 im RAM [gemessen], 17:49:** `owl_write.py Schliere.syx --run`, 85 Pakete in 1,4 s. Danach läuft Programm 0 „Schliere“ mit 17 268 B, CPU 28 %, Regler 42 / 83 / 115 / 68. Slots 1–6 unverändert, auf Slot 6 liegt weiter Fassung 1 (`out/owl_read/acdc1/20261118_174928/`). Das Hörurteil des Nutzers zum Vergleich steht aus.
- **Hörurteil zu Fassung 2 (Nutzer, ≈ 17:55):** Das Fiepsen ist unverändert da. Die gedimmten LEDs sind damit nicht die Ursache, jedenfalls nicht allein. H3 bleibt ohne Beweis.
- **Neuer Umstand (Nutzer):** acdc1 ist heute zum ersten Mal ins Case geschraubt. Bei allen bisherigen Messungen und beim Hören lag das Modul neben dem Case. Der Nutzer vermutet Einstreuungen aus dem Case und will Schritt für Schritt selbst eingrenzen [Hypothese, ungeprüft]. Ob das Fiepsen an Schliere hängt oder mit jedem Patch auftritt, ist damit offen.
- **Zurückschalten:** Der Programmwechsel auf Slot 6 scheiterte, weil acdc1 nicht am USB war („MIDI port not found“). Gesendet wurde nichts. Fassung 2 läuft bis zum nächsten Neustart aus dem RAM, danach startet der gemerkte Slot. Auf Slot 6 liegt Fassung 1, die Quelle `owl/schliere/SchlierePatch.hpp` und der Build in `owl-patches/builds/Schliere/` sind Fassung 2.
- **Zurückgeschaltet [gemessen], 18:07:** `owl_read.py --program 6` (Auftrag des Nutzers). Es läuft wieder Fassung 1 aus Slot 6 (17 196 B), CPU 28 %, Slots 1–6 unverändert (`out/owl_read/acdc1/20261118_180730/`). Der Programmwechsel wird nicht gemerkt.

### D67 – Das Fiepsen in Schliere ist die LED-PWM: Out 1 über das zweite Interface aufgenommen (2026-11-18, 18:16)

**Frage:** Woher kommt das Fiepsen, das der Nutzer mit Schliere hört (D66, Nachtrag)?

**Setup:** acdc1 fx5a, ins Case geschraubt, USB gesteckt, kein Stream am AC/DC. Slot 6 „Schliere“ Fassung 1 nach einem Neustart. Kein Eingang gepatcht, alle Regler auf 12 Uhr. acdc1 Out 1 → UMC202HD In 1 (Kette des Nutzers, Pegel nicht kalibriert). Der Nutzer dreht Regler 3 (Tap) langsam zum Rechtsanschlag, zurück zum Linksanschlag und wieder auf 12 Uhr.

**Aufnahme:** `D67-schliere-out1-umc`, `20261118_acdc1_schliere-out1-via-umc-tap_g12_usb-plugged.wav`, 30 s, 48 kHz, 24 Bit, `acdc_rec.py --device UMC202HD --input-only --channels 2 --progress 1 --prompt` im Terminal des Nutzers (Zeitanzeige im Sekundentakt). Plot `out/D67-schliere-out1-umc/spectrogram.png`. Alle Pegel in dBFS des UMC.

**Ergebnis [gemessen]:**

| Linie | Pegel | über dem Rauschteppich |
|---|---|---|
| **2321,0 Hz** | −51,4 dBFS im Mittel, **−44 … −71 dBFS je nach Stellung von Regler 3** | +45 dB |
| Vielfache: 4642, 6963, 9284, 11 605, 13 926, 16 247, 18 568, 20 889 Hz | −67 … −77 dBFS | +23 … +34 dB |
| 6001,5 / 12 002 / 18 004 Hz (Blockrate) | −65,5 / −66,2 / −69,6 dBFS | +29 … +34 dB |
| k · 1000 Hz (1 bis 5, 8, 9, 16, 17, 20 kHz) | −78 … −86 dBFS | +13 … +20 dB |

- Die Linie bei 2321,0 Hz und ihre Vielfachen sind die **LED-PWM** (240 MHz / (101 × 1024) = 2320,54 Hz im Takt von acdc1, hier im Takt des UMC gemessen, Auflösung 0,7 Hz).
- **Ihr Pegel folgt dem Tap-Regler:** zu Beginn auf 12 Uhr −62 dBFS, am Rechtsanschlag (6–8 s) −46,6 dBFS, zwischen zwei Rastpunkten (15 s, 23 s) −66 und −71 dBFS, am Linksanschlag (18–19 s) −48 dBFS. Fassung 1 zeigt den Rastpunkt binär auf LED 1–3 mit Wert 0,6, zwischen zwei Rastpunkten sind sie aus [Code]. LED 4 leuchtet bei Feedback auf 12 Uhr dauernd mit ≈ 0,44 [Code], das erklärt den Rest von −66 … −71 dBFS [Hypothese].
- Am Rechtsanschlag ist die Linie so stark wie der ganze übrige Ausgang zusammen (RMS gesamt −47,6 dBFS, Linie −46,6 dBFS).
- Das Rauschen selbst ändert mit dem Tap-Regler seine Färbung (Kerben beim Überblenden). Das ist die erwartete Wirkung des Patches auf das Eingangsrauschen.

**Fazit:** Das Fiepsen von Fassung 1 ist die LED-PWM. **H3 ist damit am Ausgang bewiesen [gemessen]:** Bei sonst gleichem Zustand ändert allein das LED-Muster die Linie um bis zu 27 dB. Der Verdacht aus dem Nachtrag zu D66 war richtig.

**Einschränkungen und offen:**
- Der Nutzer hörte das Fiepsen auch mit Fassung 2 (LEDs nur aus oder rot). Eine Aufnahme mit Fassung 2 fehlt. Mögliche Reste [Hypothese]: die Blockraten-Linien bei 6, 12 und 18 kHz, Grün auf Tastgrad 1023/1024 neben Rot, die Ausgangs-LEDs (PWM nach Ausgangspegel, Schliere reicht den Eingangsoffset an die Ausgänge durch).
- Ob die Blockraten-Linien mit Schliere (28 % CPU) höher sind als mit dem Default-Patch, zeigt diese Aufnahme nicht.
- Der Weg der Einkopplung ist offen: über die Eingänge (H3 in den ADC-Daten) oder direkt auf den Ausgang. Ob der Einbau ins Case mitspielt, ebenfalls.
- Nur Out 1. Kanal 2 der Datei ist UMC In 2, die Belegung ist nicht notiert.
- Die Auswertung lief mit einem Einmal-Skript (Welch 65 536 Punkte, Spektren je Sekunde), nicht mit `analysis`.

### D68 – Schliere Fassung 2: LED-Linie um 31 dB kleiner, es bleiben die Blockraten-Linien (2026-11-18, 18:21)

**Frage:** Beseitigt Fassung 2 (LEDs nur aus oder rot) die LED-PWM-Linie aus D67, und was fiept dann noch?

**Setup:** wie D67, dieselbe Kette und dieselbe Reglerbewegung (alle Regler 12 Uhr, Regler 3 rechts, links, 12 Uhr). Fassung 2 per `owl_write.py --run` im RAM (17 268 B, `e2fb0332…`, CPU 28 %, `out/owl_write/acdc1/20261118/owl_write_182100.json`). Aufnahme `D68-schliere-v2-out1-umc`, `20261118_acdc1_schliere-v2-out1-via-umc-tap_g12_usb-plugged.wav`, 30 s. Plot beider Fassungen: `out/D68-schliere-v2-out1-umc/spectrogram_f1_f2.png`. Pegel in dBFS des UMC, je Linie aus Sekundenspektren (Band ±6 Hz).

**Ergebnis [gemessen]:** Mittel über 30 s, in Klammern Maximum und Minimum der Sekundenwerte.

| Linie | Fassung 1 (D67) | Fassung 2 (D68) | Δ Mittel |
|---|---|---|---|
| 2321 Hz (LED-PWM) | −51,1 (−44,2 … −72,7) | −82,1 (−75,1 … −91,2) | **−31,0 dB** |
| 4642 Hz | −67,3 (−61,6 … −81,7) | −81,7 (−75,8 … −90,0) | −14,4 dB |
| 6963 Hz | −65,8 (−60,4 … −81,6) | −85,3 (−78,0 … −94,7) | −19,5 dB |
| 9284 Hz | −70,7 | −85,4 | −14,7 dB |
| 6001,5 Hz (Blockrate) | −64,0 (−57,6 … −77,2) | −58,3 (−53,6 … −66,9) | +5,7 dB |
| 12 002 Hz | −65,9 | −61,4 | +4,5 dB |
| 18 004 Hz | −68,3 | −63,1 | +5,2 dB |
| 1000 Hz (USB-Kamm) | −78,9 | −73,6 | +5,3 dB |
| RMS gesamt | −51,0 | −48,4 | +2,6 dB |

- **Die LED-Linie ist mit Fassung 2 um 31 dB kleiner** und liegt jetzt 24 dB unter der 6-kHz-Linie. Sie folgt dem Tap-Regler nicht mehr erkennbar.
- **Es bleiben die Blockraten-Linien bei 6, 12 und 18 kHz**, +30 … +35 dB über dem Rauschteppich, dazu der 1-kHz-Kamm (+16 … +19 dB). Das sind die bekannten Störfamilien aus den ADC-Daten (`docs/02`).
- **Die 6-kHz-Linie schwankt mit dem Tap-Regler um 13 dB.** Sie läuft also durch das Filter des Patches und steckt schon im Eingangssignal. Eine Störung, die erst am Ausgang dazukäme, bliebe vom Regler unberührt.
- Ihr Abstand zum Gesamtpegel (≈ −10 dB) liegt nahe am Abstand in den rohen Eingangsdaten von heute Nachmittag (6 kHz −96,0 gegen RMS −83,0 dBFS in der Datei, also −13 dB, `fx5a-open-inputs-7-r1`, D64).

**Fazit:** Fassung 2 behebt das Fiepsen der LED-PWM. Was der Nutzer mit Fassung 2 weiter hört, sind sehr wahrscheinlich die Blockraten-Linien und der Kamm der offenen Eingänge, die Schliere wie jedes Signal mit Faktor 1 an die Ausgänge gibt [gemessen: Linien und ihr Verhalten, Hypothese: dass genau sie das Gehörte sind].

**Einschränkungen und offen:**
- Die Blockraten-Linien, der Kamm und der Gesamtpegel sind in D68 um 3 bis 6 dB höher als in D67. **Der Nutzer hat zwischen den Aufnahmen den Eingangspegel am UMC verstellt** (Angabe des Nutzers), die absoluten Pegel beider Aufnahmen sind deshalb nicht vergleichbar. Bezogen auf die 6-kHz-Linie fällt die LED-Linie um ≈ 37 dB (D67: 12,9 dB darüber, D68: 23,8 dB darunter), die −31 dB der Tabelle sind die vorsichtige Zahl.
- **Hörurteil (Nutzer):** Mit Fassung 2 ist das Fiepsen weniger geworden, mehr im Hintergrund, eventuell bei einer anderen Frequenz. Das passt zum Befund: 2321 Hz fällt weg, 6 kHz bleibt.
- Ob die Rechenlast von Schliere (28 %) die Blockraten-Linie hebt (D42) und ob der Einbau ins Case mitspielt, zeigt erst eine Aufnahme der rohen Eingänge im Case gegen D64.
- Ohne Eingangssignal ist am Ausgang nur das Eingangsrauschen (≈ −83 dBFS am Gerät). Das Fiepsen fällt bei stark aufgedrehter Abhöre auf. Wie weit es unter einem echten Signal stört, ist nicht gemessen.
- Auf Slot 6 liegt weiter Fassung 1.

### D69 – Case-Sitzung: rohe Eingänge im Case, Schliere gegen Default-Patch (2026-11-18, 18:28–18:33)

**Fragen:** Hebt der Einbau ins Case die Störlinien in den ADC-Daten? Hebt die Rechenlast von Schliere die Blockraten-Linie (D42)?

**Setup:** acdc1 fx5a, ins Case geschraubt, Alltags-Kette, Eingänge offen, Out 1 steckt am zweiten Interface. `acdc_rec.py`, je Block 2 × 60 s, rohe ADC-Daten. Regler 68…69 / 57…58 / 58…59 / 73 von 127 (nach Augenmaß auf 12 Uhr, nicht nachgestellt).
1. `C1-schliere-r1/-r2` (18:28): Schliere Fassung 2 läuft aus dem RAM, CPU 29 %.
2. `C1-acdc-r1/-r2` (18:30): nach `owl_read.py --program 1` läuft der Default-Patch, CPU 6 %. Kontrolle derselben Sitzung.
3. Danach Fassung 2 wieder per `--run` geladen (`owl_write_183254.json`).

Vergleich mit den vier fx5a-Aufnahmen von heute Nachmittag neben dem Case (D64, Slot 1, Regler 60…63).

**Familienpegel [gemessen]**, Mittel je Block, Datei-dBFS, Δ gegen `C1-acdc` (`out/C1-session-table.md`):

| Block | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| B7-fx5a, neben dem Case, Slot 1 (D64) | −73,05 (−0,36) | −78,42 (+0,09) | −75,23 (−0,65) | −83,27 (+0,19) | −113,83 (+3,65) |
| C1-acdc, im Case, Slot 1 | −72,69 | −78,50 | −74,58 | −83,47 | −117,48 |
| **C1-schliere, im Case, Schliere läuft** | −72,32 (+0,37) | −78,40 (+0,10) | −74,79 (−0,22) | **−79,69 (+3,77)** | **−104,11 (+13,37)** |

Die beiden Wiederholungen je Block liegen bei RMS, Rest, Kamm und fs/8 höchstens 0,16 dB auseinander, bei den Mischprodukten 0,5 (Schliere) und 1,2 dB (Kontrolle).

**Deutung:**
- **Die Rechenlast von Schliere hebt die Blockraten-Linie um 3,8 dB und die Mischprodukte um 13,4 dB [gemessen].** Rest und Kamm bleiben innerhalb ±0,25 dB. Das passt zu D42: Was die CPU im Blocktakt tut, erscheint bei fs/8. Hier sind es 29 % statt 6 % Last.
- **Der Einbau ins Case zeigt in den ADC-Daten keine Verschlechterung [gemessen]:** im Case gegen daneben, je Slot 1, Rest −0,09 dB, fs/8 −0,19 dB, Mischprodukte −3,65 dB, Kamm +0,65 dB, RMS +0,36 dB. Der Kamm liegt leicht über der Streuung zwischen Läufen (≈ 0,4 dB, D35). Zwischen beiden Sitzungen lagen aber zwei Stunden, andere Reglerstellungen und das Kabel an Out 1, eine Kontrolle in derselben Sitzung gibt es für diese Frage nicht.
- **Die Mischprodukte bleiben mit −104 dB 29 dB unter dem Kamm.** Hörbar wird vor allem fs/8 (6, 12, 18 kHz): mit Schliere nur noch 4,9 dB unter dem Kamm.

**Fazit:** Das restliche Fiepsen von Fassung 2 (D68) sind die Blockraten-Linien. Sie stecken in den ADC-Daten, Schliere hebt sie durch seine Rechenlast um 3,8 dB und reicht sie mit Faktor 1 an die Ausgänge. Der Verdacht „Einstreuung aus dem Case“ ist für die Eingänge nicht bestätigt.

**Einschränkungen und offen:**
- Gemessen sind die Eingänge. Ob das Case direkt auf die Ausgänge einstreut, zeigt das nicht.
- Regler nicht genau auf 12 Uhr (Abstand bis 16 von 127). Das betrifft die Regler-Linien (D61), die in keiner der fünf Familien stecken.
- Meldung in beiden Blöcken `tx ovf 1.0000 1.0000 32` (Stream-Start).
- **Mögliche Abhilfe im Patch [Hypothese]:** Die Blockraten-Störung ist sample-synchron und hat genau die Periode eines Blocks (8 Samples). Ein Patch kann je Position im Block einen langsamen Mittelwert des Eingangs führen und dessen Abweichung vom Gesamtmittel abziehen. Das nimmt 6, 12, 18 und 24 kHz heraus, ohne Gleichspannung oder Audio zu berühren. Nicht gebaut, nicht gemessen.

### D70 – Sperre für die Blockraten-Linien: am Rechner geprüft, Schliere Fassung 3 gebaut (2026-11-18, abends)

**Frage:** Lässt sich die Blockraten-Störung (fs/8 mit Vielfachen, D68/D69) im Patch aus dem Eingang herausrechnen?

**Verfahren [Code]:** `owl/AcdcInput.h`, `AcdcBlockRateCanceller`. Je Position im Takt von 8 Samples ein langsamer Mittelwert des Eingangs (0,5 s). Abgezogen wird dessen Abweichung vom Mittel der letzten 8 Mittelwerte, also genau der Anteil mit Periode 8. Gelernt wird nur, wenn der Unterschied zum Sample 8 Takte vorher unter 20 mV bleibt (Hüllkurve, 50 ms Nachlauf). Die Korrektur ist auf 10 mV begrenzt.

**An den Aufnahmen aus D69 [gemessen, Host]:** rohe Eingänge durch den C++-Baustein, Datei-dBFS, Mittel über vier Kanäle, Bänder ±0,3 Hz, ohne die ersten 5 s.

| Aufnahme | fs/8 (6 + 12 + 18 kHz) vor | nach | Δ | 5999,2 Hz (6. Kamm-Harmonische) | 1 kHz | RMS vor / nach |
|---|---|---|---|---|---|---|
| `C1-schliere-r1` | −82,62 | −130,12 | −47,5 dB | −100,5 → −101,1 | unverändert | −77,78 / −78,56 |
| `C1-schliere-r2` | −82,79 | −124,87 | −42,1 dB | −100,4 → −101,0 | unverändert | −77,47 / −78,16 |
| `C1-acdc-r1` | −86,45 | −131,61 | −45,2 dB | −100,3 → −101,0 | unverändert | −77,71 / −78,01 |
| `C1-acdc-r2` | −86,51 | −131,93 | −45,4 dB | −100,2 → −100,9 | unverändert | −78,27 / −78,61 |
| `B7-fx5a-loop` (Sinus −9 dBFS) | −83,75 | −83,75 | 0,0 dB | unverändert | unverändert | −9,08 / −9,08 |

- **Die Blockraten-Familie fällt um 42 bis 47 dB auf den Rauschteppich.** Der Gesamtpegel sinkt mit Schliere-Last um 0,7 bis 0,8 dB, mit dem Default-Patch um 0,3 dB.
- Kamm und Mischprodukte bleiben, wie erwartet. Neben 6000,0 Hz steht die 6. Kamm-Harmonische bei 5999,2 Hz (−100 dB), sie ist jetzt die stärkste Linie dort.
- Mit einem lauten Dauersignal (Loop-Aufnahme) lernt die Sperre nicht und ändert nichts. Die Linie liegt dann 77 dB unter dem Signal.

**Host-Test [gemessen, Host]:** `owl/test/blockrate_test.cpp` (10 Fälle) und zwei neue Fälle in `schliere_test.cpp`. `tools/test_owl_dsp.sh` hat damit 56 Fälle, alle bestanden. Die beiden neuen Testdateien laufen auch mit `-O3 -ffast-math` durch.
- Störung 9 · 10⁻⁵ mit Offset und Rauschen: nach 2 s unter 2 · 10⁻⁶, nach 4 s bei 4 · 10⁻⁷. Der Offset läuft unverändert durch.
- 1-Hz-CV mit 5 V: Abweichung höchstens 7 · 10⁻⁵, kein Anteil im Blocktakt.
- 2 s Rauschen mit 3 V nach dem Lernen: die Schätzung bleibt stehen, danach ist die Störung sofort wieder weg.
- Ein Ton genau auf fs/8 mit 2,5 V verliert 13 mV.
- Schliere mit Störung am Eingang: an L, R und Tail unter 3 · 10⁻⁶.

**Fassung 3 von Schliere:** In 1 läuft durch die Sperre, sonst wie Fassung 2. `owl-patches/builds/Schliere/`: 17 860 B, CRC `0x936d0028`, `db33b525…`, Quelle `18a11124…`, `AcdcInput.h` `39c3f2ab…`. Fassung 2 liegt in `owl-patches/builds/Schliere-v2/` (`e2fb0332…`), Fassung 1 in `Schliere-v1/` und auf Slot 6.

**Einschränkungen und offen:**
- Nichts davon ist am Gerät gemessen. Offen ist vor allem, ob am Ausgang noch ein Anteil der Blockrate entsteht, der nicht über den Eingang kommt.
- Die Aufnahmen sind 16 Bit über USB, der Patch sieht die ADC-Daten in voller Auflösung.
- Rechenlast und Lage der Störung im Takt sind am Gerät dieselben wie in der Aufnahme [Hypothese]: Der Patch rechnet in Blöcken zu 8, die Sperre zählt die Position selbst.
- Bei wechselnder Rechenlast (Grainz) hinkt die Schätzung nach, solange es laut ist.

### D71 – Schliere Fassung 3 am Gerät: Blockraten-Linien am Ausgang um 22 bis 25 dB kleiner (2026-11-18, 18:47–18:51)

**Frage:** Wirkt die Blockraten-Sperre (D70) am Gerät, gemessen am Ausgang?

**Setup:** acdc1 fx5a im Case, USB gesteckt, kein Stream, kein Eingang gepatcht. Out 1 → UMC202HD In 1, Kette und Pegel in der Sitzung unverändert. Regler fest auf 68 / 57…58 / 58 / 72 von 127 (vor jedem Block gelesen). Je 30 s, `acdc_rec.py --device UMC202HD --input-only`, 24 Bit. Reihenfolge mit `owl_write.py --run`: Fassung 2 (`D71-schliere-f2-a`) → Fassung 3 (`D71-schliere-f3-r1/-r2`) → Fassung 2 (`D71-schliere-f2-b`). Nach jedem Laden 6 s Wartezeit. CPU: Fassung 2 29…30 %, Fassung 3 30 %, Speicher 1040 und 1128 B.

**Auswertung:** Linienpegel aus dem Spektrum über 30 s, Bänder ±0,25 Hz, Kanal 1, dBFS des UMC. Der Takt des UMC liegt 183 ppm über dem von acdc1 (6000 Hz erscheinen bei 6001,10 Hz), die Linien sind entsprechend umgerechnet. Plot `out/D71-schliere-f3-out1-umc/psd_f2_f3.png`.

| Linie (im Takt von acdc1) | F2 a | F3 r1 | F3 r2 | F2 b | F3 − F2 |
|---|---|---|---|---|---|
| **6000 Hz (Blockrate)** | −72,7 | −97,6 | −97,2 | −72,6 | **−24,7 dB** |
| **12 000 Hz** | −76,0 | −100,8 | −100,9 | −75,6 | **−25,1 dB** |
| **18 000 Hz** | −79,0 | −101,3 | −101,1 | −79,7 | **−21,9 dB** |
| 5999,2 Hz (6. Kamm-Harmonische) | −88,7 | −89,1 | −89,3 | −89,0 | −0,3 dB |
| 1 / 2 / 3 kHz (Kamm) | −93,2 / −92,8 / −93,8 | −93,8 / −92,4 / −93,0 | −94,0 / −92,7 / −93,0 | −93,5 / −92,7 / −92,6 | −0,6 / +0,2 / +0,2 dB |
| 2320,5 Hz (LED-PWM) | −112,3 | −114,0 | −111,0 | −110,8 | im Teppich |
| Umgebung bei 6 kHz (gleiches Band) | −113,2 | −113,6 | −113,8 | −113,4 | −0,4 dB |
| RMS gesamt | −64,9 | −65,7 | −65,7 | −65,0 | −0,8 dB |

**Deutung [gemessen]:**
- **Die Sperre wirkt am Gerät:** Die drei Blockraten-Linien fallen am Ausgang um 22 bis 25 dB. Die beiden Kontrollen mit Fassung 2 liegen höchstens 0,7 dB auseinander.
- **Es bleibt ein Rest von −97 … −101 dBFS, 12 bis 16 dB über dem Teppich.** Am Rechner fiel die Familie bis auf den Teppich (D70). Der Rest kommt also nicht über den Eingang, den die Sperre sieht [Hypothese: Anteil, der erst am Ausgang entsteht, oder Übersprechen in der Messkette].
- **Stärkste Linien sind jetzt die des Kamms:** die 6. Harmonische bei 5999,2 Hz mit −89 dBFS und 1 bis 3 kHz mit −93 dBFS. Sie sind unverändert.
- Die LED-Linie liegt mit beiden Fassungen im Teppich. Beide Fassungen zeigen die LEDs nur aus oder rot, und die Regler standen so, dass die Linie nicht messbar ist.
- Der Gesamtpegel sinkt um 0,8 dB, wie am Rechner.

**Fazit:** Fassung 3 senkt das restliche Fiepsen von Fassung 2 messbar. Von den drei Ursachen sind zwei behoben (LED-PWM: D68, Blockrate: D71), der USB-Kamm bleibt.

**Einschränkungen und offen:**
- Ohne Eingangssignal und mit festen Reglern gemessen. Mit Signal, bei bewegten Reglern und über längere Zeit ist die Sperre am Gerät nicht geprüft.
- Das Hörurteil des Nutzers steht aus.
- Nur Out 1. Der Pegel am UMC war ein anderer als in D67/D68, die Zahlen sind nur innerhalb dieser Sitzung vergleichbar.
- Am Ende läuft Fassung 3 aus dem RAM (`owl_write_…`, 17 860 B). Auf Slot 6 liegt weiter Fassung 1.

**Nachtrag D71 – Fassung 3 auf Slot 6 (19:17, Freigabe des Nutzers):** `owl_write.py Schliere.syx --store 6 --yes --backup-file owl-patches/builds/Schliere-v1/patch.bin`. Die Sicherung von Fassung 1 passte in Größe und CRC zum Slot (`backup/acdc1/20261118/owl_write_191742/`). Slot 6 danach „Schliere“, 17 860 B, CRC `0x936d0028`. `owl_read.py --slots 6`: Download `ok`, bytegleich mit dem Build von Fassung 3 (`db33b525…`). Slots 1–5 unverändert, Storage 125 952 B, Programm 6 läuft mit 30 % CPU (`out/owl_read/acdc1/20261118_191753/`).

---

## D72 – Schliere Fassung 3: Störgeräusch bei leuchtenden LEDs? (2026-11-18, 22:14)

**Anlass:** Hörurteil des Nutzers zu Fassung 3: viel besser. Sobald die LEDs aufleuchten, hört er aber wieder ein leises Störgeräusch, und bei „Rot“ leuchten Rot und Grün zusammen. Seine These: Die LEDs sind generell für die Störgeräusche verantwortlich, auch bei Aufnahmen.

**Code-Befund [Code]:** `setLed()` und die Hauptschleife (`ACDC/Core/Src/ACDC.cpp`, `acdcOnLoopLate()`) behandeln einen Wert ab 4090 so, alle 2 ms neu:
- Zuerst `setLed(i+1, value)`: Der rote Pin geht auf high (aus), die grüne PWM bekommt den Vergleichswert 1024 − 1023 = 1. Grün leuchtet also mit Tastgrad 1023/1024 weiter, mit einer Lücke von 0,42 µs je Periode (2320,54 Hz). Der Vergleichswert 0 (dauerhaft an) ist über `setLed()` nicht erreichbar.
- Danach `setLed(i+1, RED_COLOUR)`: Der rote Pin geht auf low (an). Die grüne PWM bleibt, die Zeile zum Abschalten ist auskommentiert.
- Folge: „Rot“ ist Rot plus fast volles Grün. Der rote Pin bekommt 500-mal pro Sekunde einen kurzen Puls, die grüne PWM schaltet weiter. Die Aussage aus D68 („Rot ist ein statischer Pin“) stimmt für den Pin, aber nicht für die LED als Ganzes. Ein Patch kann eine LED nur ganz aus ohne Schaltflanken betreiben.

**Setup:** acdc1 fx5a im Case, USB gesteckt, kein Stream, kein Eingang gepatcht, Slot 6 (Schliere Fassung 3). Out 1 → UMC202HD In 1, UMC-Gain vom Nutzer deutlich erhöht (nach den Kamm-Linien etwa +23 dB gegen D71). Regler 1, 2, 4 auf 12 Uhr. Regler 3 (Tap) erst am Linksanschlag, dann zum Rechtsanschlag, dort bis zum Ende. Nach dem Spektrogramm lief die Drehung etwa von 7,5 bis 22,5 s, schneller als geplant.

**Aufnahme:** `D72-schliere-f3-tap-leds-umc`, `20261118_acdc1_schliere-f3-out1-via-umc-tap-sweep_g12_usb-plugged.wav`, 45 s, 48 kHz, 24 Bit, `acdc_rec.py --device UMC202HD --input-only --channels 2 --prompt --progress 1`. Plot `out/D72-schliere-f3-tap-leds-umc/spectrogram.png`. Alle Pegel in dBFS des UMC, Kanal 1. Takt des UMC 188 ppm über dem von acdc1, f0 des Kamms 999,868 Hz.

**Auswertung:** Zwei ruhende Abschnitte, in denen die LEDs dauerhaft leuchten: A = Linksanschlag (0,5–7 s, Rastpunkt 1, LED 1) und B = Rechtsanschlag (25–44,8 s, Rastpunkt 7, LED 1–3). Spektrum mit 0,37 Hz (A) und 0,18 Hz (B) Auflösung. „über Umgebung“ = stärkster Bin in ±0,4 Hz gegen den Median der Nachbarschaft, bei reinem Rauschen ergibt dieses Maß bis etwa +8 dB.

| Linie (im Takt von acdc1) | A: Linksanschlag, LED 1 | B: Rechtsanschlag, LED 1–3 |
|---|---|---|
| Kamm 1 kHz / 5 kHz | −72,1 / −64,4 | −75,0 / −73,7 |
| **Regler-Linie 2200,95 Hz** | **−72,7** (+21,9 dB) | −77,8 (+17,5 dB) |
| **Regler-Linie 4401,90 Hz** | **−66,5** (+21,9 dB) | −80,5 (+19,6 dB) |
| **Regler-Linie 6602,85 Hz** | **−67,7** (+20,0 dB) | −80,3 (+16,4 dB) |
| Regler-Linie 8549,33 Hz | −77,4 (+13,9 dB) | −86,8 (+14,0 dB) |
| Blockrate 6000 / 18 000 Hz | vom Kamm verdeckt / −81,1 | −81,8 / −81,4 |
| LED-PWM 2320,54 Hz, k = 1…10 | −84,6 … −100,6, höchstens +4,3 dB | −84,9 … −96,4, höchstens +7,9 dB (einmal +9,8 bei k = 8) |
| 500 Hz, ungerade Vielfache bis 6,5 kHz | höchstens +6,4 dB | höchstens +8,5 dB |

Verlauf der Regler-Linien in Fenstern von 1 s: am Linksanschlag 16–21 dB über der Umgebung, während der Drehung fallend, um die Mitte des Regelwegs (etwa 15–19 s) nicht vom Rauschen zu unterscheiden, am Rechtsanschlag wieder 8–16 dB darüber.

**Deutung:**
- **Keine LED-Linie [gemessen]:** Mit einer und mit drei dauerhaft leuchtenden LEDs (Rot plus fast volles Grün) gibt es an Out 1 weder bei der PWM-Frequenz und ihren Vielfachen noch bei Vielfachen von 500 Hz eine Linie über dem Rauschen. Was die LEDs in diesem Zustand beitragen, liegt mindestens 20 dB unter den Kamm-Linien. Die beiden Verdachtsstellen aus dem Code sind damit am Ausgang nicht nachweisbar.
- **Dem dritten Regler folgen die Regler-Linien [gemessen]:** 2200,95 / 4401,90 / 6602,85 Hz (D58, D60, D61) stehen am Linksanschlag mit −66 … −73 dBFS am Ausgang, so stark wie die stärksten Kamm-Linien. In der Mitte des Regelwegs verschwinden sie, am Rechtsanschlag sind sie 5 bis 14 dB schwächer als links. Bisher waren sie nur in den rohen ADC-Daten gemessen. Ein FX-Patch reicht sie wie Kamm und Blockrate an den Ausgang durch.
- **[Hypothese]** Was der Nutzer beim Drehen von Regler 3 hört, sind diese Linien (fester Ton, Pegel folgt der Reglerstellung) und die Klangfarbe des Patches selbst: Bei 12 Uhr steht Feedback auf etwa der Hälfte, das Eingangsrauschen bekommt Resonanzen, die auf einem Rastpunkt stehen und beim Überblenden wandern. Beides fällt mit den LEDs zusammen, weil alles an Regler 3 hängt.
- **Die These des Nutzers stimmt zum Teil:** Die LED-PWM ist eine von vier Störfamilien und nur bei gedimmten LEDs messbar (D67: bis −44 dBFS). Kamm und Blockrate sind auch bei dunklen LEDs da (D20, D33, D42, D69).

**Einschränkungen und offen:**
- Die Aufnahme trennt „LED leuchtet“ nicht von „Abgriff steht auf einem Rastpunkt“. Die Haltezonen dauerten bei dieser Drehung unter 1 s, zu kurz für Linienpegel je Zone. Ob das Schalten der LEDs an den Zonengrenzen stört (Regler-Rauschen lässt sie dort flackern), ist nicht geprüft.
- Entscheidend wäre ein Test-Build, der die LEDs nach der Uhr schaltet (aus, eine rot, drei rot, gedimmt grün), bei unbewegten Reglern auf 12 Uhr.
- Neu gegen D71 und nicht zugeordnet: schmale Linien, die im Lauf der Aufnahme wandern, mit Vielfachen nur in Oktaven. A: 684,8 Hz mit ×2, ×4, ×8, ×16 (bis −67 dBFS), 942,5 Hz mit ×2, ×4, 281,6 Hz mit ×4. B: 686,2 Hz mit ×2, ×4, ×16, 490,1 Hz mit ×2, 299,6 Hz mit ×4. Sie hängen nicht am Takt von acdc1. Ob sie der Reglerstellung folgen oder von außen kommen (andere Module im Case, Messkette), ist offen.
- Nur Out 1, Pegel des UMC anders als in D67, D68 und D71.

---

## D73 – LED-Test-Patch: Stören die LEDs selbst? (2026-11-18, 22:29)

**Frage (aus D72):** Trägt eine leuchtende LED etwas zum Ausgang bei, wenn sich sonst nichts ändert? D72 konnte „LED leuchtet“ nicht von „Abgriff steht auf einem Rastpunkt“ trennen.

**Mess-Patch:** `owl/test/SchliereLedTestPatch.hpp`, eine von `SchlierePatch` abgeleitete Klasse. Der Klang ist unverändert (`SchlierePatch::processAudio()` läuft wie auf Slot 6, dieselbe Funktion mit 0xab0 Bytes im ELF), nur die vier LED-Werte werden danach überschrieben. Ablauf je 5 s, ab dem Laden, wiederholt: aus, LED 1 rot, LED 1–3 rot, LED 1–4 rot, aus, LED 1–3 blinken rot mit 40 Hz (12,5 ms an, 12,5 ms aus), aus, LED 1–3 grün mit 60 %. Host-Test `owl/test/ledtest_test.cpp` (10 Fälle, Zeitplan). Build `owl-patches/builds/SchliereLedTest/` (15 412 B, CRC `0x1ce0c9a6`, `fbfca250…`). Geladen mit `owl_write.py --run` um 22:26 (nur RAM, `out/owl_write/acdc1/20261118/owl_write_222628.json`), Stand davor `out/owl_read/acdc1/20261118_222618/`: Programm 6, Regler 62 / 51 / 58 / 58.

**Setup:** acdc1 fx5a im Case, USB gesteckt, kein Stream, kein Eingang gepatcht. Out 1 → UMC202HD In 1, UMC-Gain wie D72. Regler vom Nutzer vor der Aufnahme gestellt und dann nicht bewegt: 78 / 45 / 77 / 1 von 127 (nach der Aufnahme gelesen, `out/owl_read/acdc1/20261118_223105/`), Feedback also am Linksanschlag. CPU 29 %.

**Aufnahme:** `D73-schliere-ledtest-umc`, `20261118_acdc1_schliere-ledtest-out1-via-umc_g12_usb-plugged.wav`, 90 s, 48 kHz, 24 Bit, `acdc_rec.py --device UMC202HD --input-only --channels 2 --prompt --progress 1`. Plot `out/D73-schliere-ledtest-umc/led_phases.png`. Alle Pegel in dBFS des UMC, Kanal 1.

**Auswertung:** Die Lage der Phasen folgt aus der grünen Phase (2321-Hz-Linie an bei 29,813 und 69,806 s, aus bei 34,810 und 74,804 s). Je Zustand alle Phasen gemittelt, je 0,6 s nach und 0,4 s vor einem Wechsel ausgelassen. Linien: stärkster Bin in ±0,8 Hz, Raster 0,73 Hz.

| | aus | LED 1 rot | LED 1–3 rot | LED 1–4 rot | blinken 40 Hz | grün 60 % |
|---|---|---|---|---|---|---|
| RMS gesamt | −47,4 | −47,3 | −47,6 | −47,5 | **−29,8** | **−40,6** |
| Rauschen 200–2000 Hz (Median) | −58,3 | −58,5 | −58,4 | −58,5 | −54,7 | −58,6 |
| Rauschen 2–8 kHz (Median) | −56,5 | −56,6 | −56,7 | −56,6 | −56,2 | −56,5 |
| LED-PWM 2320,54 Hz | −90,9 | −91,4 | −88,8 | −88,7 | −85,2 | **−39,8** |
| LED-PWM ×2 / ×3 | −89,0 / −83,1 | −91,3 / −83,7 | −86,3 / −81,6 | −84,4 / −78,9 | −86,5 / −83,3 | **−48,5 / −49,4** |
| Kamm 1 kHz / 5 kHz | −71,8 / −65,5 | −71,8 / −64,6 | −71,9 / −64,7 | −72,4 / −64,6 | −71,2 / −65,1 | −71,5 / −65,1 |
| Blockrate 6 / 12 / 18 kHz | −77,7 / −82,0 / −79,5 | −77,7 / −82,4 / −78,4 | −78,3 / −81,1 / −78,9 | −78,4 / −81,5 / −79,1 | −77,9 / −82,5 / −78,3 | −78,5 / −83,2 / −78,1 |
| Regler-Linien 2200,95 / 6602,85 Hz | −79,6 / −76,0 | −80,3 / −75,1 | −79,5 / −74,4 | −79,3 / −74,2 | −73,9 / −75,5 | −80,8 / −75,4 |

Schaltvorgänge (Signal mit 300 Hz tiefpassgefiltert, Rauschen dort 0,0020 Vollausschlag effektiv):

| Wechsel | Spitze (Vollausschlag UMC) | gegen das Rauschen |
|---|---|---|
| aus → LED 1 rot | +0,013 / +0,015 | 6…7-fach |
| LED 1 rot → LED 1–3 rot | +0,026 / +0,024 / +0,026 | 12…13-fach |
| LED 1–3 rot → LED 1–4 rot | +0,015 / +0,013 | 6…7-fach |
| LED 1–4 rot → aus | −0,049 / −0,051 | 24…25-fach |
| aus → grün 60 % / zurück | +0,013 / −0,017 … −0,013 | 6…8-fach |

Blinken mit 40 Hz: Grundton −28,3 dBFS, 120 Hz −40,1, 200 Hz −41,3, je 35–37 dB über dem Zustand „aus“ an derselben Stelle. Die ungeraden Vielfachen stehen bei 2 kHz noch 18 dB und bei 4 kHz 11 dB darüber, ab etwa 8 kHz gehen sie im Rauschen auf.

**Deutung [gemessen]:**
- **Dauerhaft leuchtende LEDs stören nicht messbar.** Mit einer, drei und vier roten LEDs (Rot plus Grün mit Tastgrad 1023/1024) sind Gesamtpegel, Rauschen, Kamm, Blockrate und Regler-Linien gleich wie bei dunklen LEDs (±1 dB). Bei den Vielfachen der PWM-Frequenz gibt es mit vier LEDs höchstens +2…5 dB an Linien um −79…−89 dBFS, mindestens 14 dB unter der stärksten Kamm-Linie und nicht gesichert. Das bestätigt D72.
- **Jeder Wechsel einer LED verschiebt den Ausgang.** Der Sprung ist additiv, etwa +0,0125 Vollausschlag des UMC je LED, die eingeschaltet wird, und zeigt beim Ausschalten in die andere Richtung. Schon eine LED ergibt einen Knack mit dem 6-fachen des Rauschens im Bass, etwa 26 dB über der Amplitude der stärksten Kamm-Linie. Der UMC ist wechselspannungsgekoppelt, die wahre Stufe ist deshalb eher größer als die Spitze.
- **Schnelles Schalten wird zum Brummen und Knattern:** Drei LEDs mit 40 Hz heben den Gesamtpegel um 17,6 dB, mit Oberwellen bis in den kHz-Bereich.
- **Gedimmtes Grün fiepst wie in D67:** 2320,54 Hz mit −39,8 dBFS, 25 dB über der stärksten Kamm-Linie, Gesamtpegel +6,8 dB. Die Gegenprobe zeigt, dass die Messung LED-Einflüsse erfasst.
- **Folgerung für Schliere Fassung 2 und 3 [Hypothese]:** Die LEDs schalten hart, sobald der Abgriff in eine Haltezone kommt. Das knackt bei jedem Rastpunkt, und an der Grenze einer Zone lässt das Rauschen des Reglers die LEDs flackern. Das passt zum Hörurteil des Nutzers („sobald die LEDs aufleuchten“).
- **Folgerung für den Alltag [Hypothese]:** Die Pegel-LEDs der Firmware folgen dem Signal. Ihr Strom verschiebt den Ausgang dann im Takt der Hüllkurve, zusätzlich zur PWM-Linie.

**Einschränkungen und offen:**
- Wo die Verschiebung entsteht, ist offen: am Ausgang (DAC, Ausgangsstufe) oder am Eingang (ADC), von wo der gleichspannungsgekoppelte Patch sie an Out 1 durchreicht. Nur im zweiten Fall träfe sie auch die Aufnahmen. Test: derselbe Ablauf mit digital stummen Ausgängen.
- Die Größe in Volt ist nicht bekannt (UMC nicht kalibriert). Die Form der Stufe ist durch die Wechselspannungskopplung des UMC verfälscht, die Spitze liegt 75–105 ms nach dem Wechsel.
- Nur Out 1, nur die Eingangs-LEDs. Die Ausgangs-LEDs steuert die Firmware nach dem Ausgangspegel, sie waren dunkel.
- Nach der Aufnahme per Program Change zurück auf Slot 6 (Schliere Fassung 3), nichts gespeichert.

---

## D74 – LED-Strom: Eingang oder Ausgang? (2026-11-18, 22:39–22:47)

**Frage (aus D73):** Entsteht die Verschiebung durch den LED-Strom am Eingang (ADC), von wo der Patch sie durchreicht, oder am Ausgang? Nur im ersten Fall trifft sie auch die Aufnahmen.

**Mess-Patch:** `owl/test/SchliereLedPathPatch.hpp`, von `SchlierePatch` abgeleitet. Zehn Phasen zu je 5 s, wiederholt: (0) Schliere, LEDs aus, (1) Schliere, LED 1–3 blinken mit 40 Hz, (2) Ausgänge digital null, aus, (3) null, blinken, (4) null, aus, (5) null, LED 1–4 rot, (6) null, aus, (7) null, Eichton 300 Hz mit Amplitude 0,001 an Out 1, (8) alle Ausgänge = 4 × In 1, aus, (9) 4 × In 1, blinken. Der Patch misst dazu selbst an den rohen Eingängen 1–3 und meldet per `debugMessage` in 1e-7 Vollausschlag: „LEDblink“ = Mittel bei LED an minus LED aus in Phase 3 (ohne die ersten 4 ms nach jedem Wechsel, über alle Durchläufe), „LEDstat“ = Mittel in Phase 5 minus Mittel der Phasen 4 und 6 (je ohne die erste Sekunde). In den Phasen 2–7 liegt am Ausgang kein Signal, das auf die Eingänge übersprechen könnte. Host-Test `owl/test/ledpath_test.cpp` (11 Fälle: Zeitplan, Ausgänge je Phase, die Messung findet eine eingebaute Verschiebung auf 0,1 % wieder). Build `owl-patches/builds/SchliereLedPath/` (20 108 B, CRC `0xb0fa2194`, `98fdd642…`), geladen mit `owl_write.py --run` um 22:39 (nur RAM, `out/owl_write/acdc1/20261118/owl_write_223933.json`).

**Setup:** acdc1 fx5a im Case, USB gesteckt, kein Stream, kein Eingang gepatcht, Regler 61 / 68 / 62 / 58 von 127, nicht bewegt. CPU 28–31 %.

### Messung am Eingang (vom Patch selbst, über `owl_read.py`)

| gelesen | Meldung | In 1 | In 2 | In 3 |
|---|---|---|---|---|
| 22:40:05 | LEDblink (3 LEDs, 40 Hz) | −8008 | −7956 | −8333 |
| 22:40:19 | LEDstat (4 LEDs, dauerhaft) | −11774 | −11521 | −11557 |
| 22:46:53 | LEDblink | −7974 | −7928 | −8310 |
| 22:46:58 | LEDstat | −11796 | −11469 | −11656 |
| 22:47:36 | LEDblink | −7973 | −7927 | −8309 |

Einheit 1e-7 Vollausschlag, bei ±10 V also 1 ≙ 1 µV. Reports in `out/owl_read/acdc1/20261118_2240*/` und `…_2246*/`, `…_2247*/`.

### Aufnahme am Ausgang

`D74-schliere-ledpath-umc`, `20261118_acdc1_schliere-ledpath-out1-via-umc_g12_usb-plugged.wav`, 110 s, 48 kHz, 24 Bit, Out 1 → UMC202HD In 1, UMC-Gain wie D72/D73, `acdc_rec.py --device UMC202HD --input-only --channels 2 --prompt --progress 1`. Lage der Phasen aus dem Eichton (an bei 27,234 und 77,224 s). Eichton: −22,14 dBFS am UMC für 0,001 Vollausschlag am Ausgang, also 1 Vollausschlag UMC ≙ 0,01279 Vollausschlag von acdc1 ≈ 128 mV (bei 10 V).

| Phase | 40 Hz am UMC (dBFS) | am Ausgang von acdc1 (Spitze) |
|---|---|---|
| Schliere, blinken | −24,5 | 7,58 mV |
| Ausgänge null, blinken | −52,8 | 0,29 mV |
| 4 × In 1, blinken | −16,4 | 19,4 mV |
| Ausgänge null, LEDs aus | −97 … −108 | unter 0,002 mV |

Schalten von vier LEDs bei stummem Ausgang (Tiefpass 300 Hz): +0,51 / +0,56 mV beim Einschalten, −0,72 / −0,71 mV beim Ausschalten, Rauschen davor 0,03–0,06 mV.

**Deutung [gemessen]:**
- **Die Verschiebung entsteht am Eingang.** Jede leuchtende Eingangs-LED verschiebt die rohen ADC-Daten um −2,9e-4 Vollausschlag (statisch: −2,95 / −2,87 / −2,91e-4 an In 1 / 2 / 3), das sind etwa −2,9 mV oder −70,8 dBFS. Beim Blinken mit 40 Hz sind es −2,7e-4 je LED. Die Werte sind über sieben Minuten auf 0,5 % gleich.
- **Alle drei gemessenen Eingänge verschieben sich gleich** (±2 %). [Hypothese] Der LED-Strom verschiebt einen gemeinsamen Bezugspunkt des Wandlers (Masse oder Referenz).
- **Die Rechnung geht auf:** Ein Rechteck mit 8,0e-4 Spitze-Spitze hat einen Grundton von 5,1e-4. Mit 4 × In 1 stehen am Ausgang 19,4e-4, auf den Eingang bezogen 4,8e-4 (95 %). Mit Schliere sind es 7,6e-4, mehr als 5,1e-4, weil Feedback bei 12 Uhr auf etwa 44 % steht.
- **Am Ausgang selbst kommt ein kleiner Anteil dazu:** Bei digital stummem Ausgang bleiben 0,29 mV Grundton, das entspricht etwa 0,15 mV je LED, 24 dB weniger als über den Eingang bei Verstärkung 1. Die Sprünge beim Schalten von vier LEDs (0,5–0,7 mV) passen dazu.
- **Die LED-PWM-Linie ist derselbe Effekt.** Eine gedimmte LED schaltet die Verschiebung 2321-mal pro Sekunde. Ein Rechteck mit 2,9e-4 und Tastgrad 60 % hätte einen Grundton von 1,8e-4 = −75 dBFS je LED. In den frühen Aufnahmen lag die Linie mit Signal bei −75 … −80 dBFS (H3 in `docs/02`). Am Ausgang waren es in D73 mit drei LEDs 1,3e-4 (−39,8 dBFS am UMC), 12 dB weniger als diese Rechnung: Der Effekt ist bei 2,3 kHz also schwächer als statisch, oder der Patch dämpfte dort.
- **Die These des Nutzers stimmt im Kern:** Was die LEDs tun, steht in den ADC-Daten und damit in jeder Aufnahme. Dauerlicht ist nur ein fester Versatz. Jeder Wechsel ist ein Sprung von −71 dBFS je LED, rund 30 dB über den Kamm-Linien der rohen Eingänge.

**Folgerungen:**
- [Hypothese] Im Alltag folgen die Pegel-LEDs dem Signal (gedimmtes Grün, Zeitkonstante 40 ms, Rot beim Übersteuern). Der Nullpunkt aller Eingänge wandert dann mit der Hüllkurve des lautesten Kanals, um bis zu etwa 1,2e-3 Vollausschlag bei vier hellen LEDs, und die PWM-Linie kommt dazu. Wie hörbar das unter Musik ist, ist nicht gemessen.
- Für Patches: LEDs gar nicht oder selten schalten, nie flackern lassen, nie dimmen.
- Für die Firmware: Ein Schalter „LEDs aus“ beseitigt beides. Eine PWM-Frequenz über dem Hörbereich nähme die Linie, ließe die langsame Verschiebung aber stehen. Pegel-LEDs in Stufen mit Hysterese statt gedimmt würden sie seltener machen.

**Einschränkungen und offen:**
- In 4 ist nicht gemessen (die Meldung fasst drei Werte). Die Ausgangs-LEDs und die Eingangs-LEDs einzeln sind nicht gemessen, nur LED 1–3 zusammen und LED 1–4 zusammen.
- Volt-Angaben mit ±10 V Vollausschlag gerechnet (gemessen ≈ ±9,5 V am Eingang, D29). Frequenzgang des UMC zwischen 40 und 300 Hz nicht bekannt.
- Der UMC übersteuert kurz bei den Wechseln der Ausgangsart, weil der Eingangsoffset am Ausgang erscheint oder verschwindet. Die Bezugsphasen direkt danach (0, 2, 8) tragen noch den Ausschwinger, ihre Pegel sind deshalb obere Grenzen.
- Nach der Aufnahme per Program Change zurück auf Slot 6 (Schliere Fassung 3), nichts gespeichert.

---

## D75 – Build 8 `v22.4.r-fx6a` auf acdc1: Flash, LED-Modi am Gerät (2026-11-18, 23:10–23:45)

**Anlass:** Abnahme von Build 8 (Patch 17, LED-Modus im Boot-Menü über Regler 2, `docs/05`, „Build 8“). Freigabe des Nutzers für den Flash.

**Flash:** `tools/flash_acdc.py acdc1-build8-fx6a --yes`, Log `firmware/flashlog/20261118_build8-fx6a/`. Vorher fx5a mit sechs Slots, DFU-Neustart, 110 088 B geschrieben, Readback bytegleich, Rest 0xFF. Nach dem Neustart durch den Nutzer `--a1`: bestanden (acdc1, `AC/DC v22.4.r-fx6a`, 48 000 Hz, Blockgröße 8, Slots unverändert, Storage 125 952 B, Slot 6 startet mit 30 % CPU).

**Messung der LED-Verschiebung je Modus:** Mess-Patch aus D74 (`SchliereLedPath`, nur RAM), Meldungen über `owl_read.py`, Einheit 1e-7 Vollausschlag (≙ µV bei ±10 V), In 1 / In 2 / In 3. Kein Kabel gesteckt, kein Stream.

| Modus | gelesen | LEDblink (3 LEDs, 40 Hz) | LEDstat (4 LEDs dauerhaft) |
|---|---|---|---|
| normal (nach dem Flash) | 23:15 | −8421 / −8085 / −8507 | −12344 / −11742 / −11875 |
| aus (im Boot-Menü gewählt) | 23:27 | +108 / +107 / +96 | +190 / +231 / +192 |

Eine Messung um 23:24 zeigte noch die volle Verschiebung (−9329 / −7226 / −7966, statisch −34606 / −10650 / −11066). Laut Nutzer war dabei der falsche Modus eingestellt, die Regler standen während der Messung nicht still (47 / 17 / 58 / 95). Welcher Modus das war, ist offen (siehe unten).

**Boot-Menü am Gerät (Nutzer):** Modus aus und danach nur Clip über Regler 2 gewählt und mit Regler 4 bestätigt. Storage nach der ersten Wahl 126 208 B (+256 B, neue Ressource `ACDC.led`), bei den späteren Wechseln unverändert: `getUsedSize()` zählt nur gültige Ressourcen, die alte Fassung wird als gelöscht markiert [Code].

**Clip-Anzeige im Modus nur Clip:** Kabel Out 2 → In 1, In 2–4 offen, Slot 1 (per Program Change, damit Schliere mit dem Kabel keine Schleife bildet), Aufnahme der rohen Eingänge mit `acdc_rec.py --dc 0 ∓1 --dc-ramp 20`, 30 s, 16 Bit (Datei = Gerätewerte).
- `D75-fx6a-clip-ramp` (+1,0): In 1 erreicht nur +0,9635, unter der Schwelle 0,9886 (negativer Eingangsoffset, wie D36). Kein Clip. In 2–4 ändern sich über die ganze Rampe um weniger als 6e-5.
- `D75-fx6a-clip-ramp-neg` (−1,0): In 1 erreicht die Schwelle bei 18,437 s und steht danach am Anschlag (−0,99992). In diesem Moment springen die offenen Eingänge: In 2 −101e-6, In 3 −146e-6, In 4 −82e-6 Vollausschlag (Mittel 0,05–1,2 s danach gegen den Trend der 4 s davor).

**Deutung:**
- **[gemessen] Der Modus aus wirkt am Gerät:** Die Verschiebung der Eingänge fällt von −1,2e-3 auf +2e-5 Vollausschlag (vier LEDs), also auf 1,7 %, rund 37 dB weniger. Beim Blinken sind es 1,3 %.
- Der Rest hat das umgekehrte Vorzeichen und ist an allen drei Eingängen gleich. Die LEDs fasst die Firmware in diesem Modus nicht an. [Hypothese] Etwas anderes folgt den LED-Parametern des Patches, zum Beispiel deren Weitergabe in der Firmware.
- **[gemessen] Im Modus normal ist die Verschiebung unter fx6a dieselbe wie unter fx5a** (D74: −11774 / −11521 / −11557), hier 2 bis 5 % größer.
- **Clip-Anzeige:** Der Sprung der offenen Eingänge fällt mit dem Erreichen der Schwelle zusammen und passt in der Größe zu einer einzelnen roten LED ohne Grün (ein Drittel bis die Hälfte der −2,9e-4 für Rot plus Grün). [Hypothese] Das ist LED 1. Ob stattdessen das Übersteuern von In 1 selbst die anderen Kanäle verschiebt, trennt die Messung nicht. Gegenprobe: dieselbe Rampe im Modus aus.

**Offen:**
- Bestätigung des Nutzers, dass bei der negativen Rampe nur LED 1 rot wurde.
- Modus nur Clip ohne Stream mit dem Mess-Patch (Eingänge müssen ruhig bleiben), gemerkter Modus nach Aus und Ein.
- Welcher Modus bei der Messung um 23:24 eingestellt war. Wäre es nur Clip gewesen, hätte der Modus ohne Stream einen Fehler.
- Rausch-A/B gegen fx5a, Loop-Test, Download-Stresstest (`docs/05`, „Build 8“, Abnahme 5).

### Nachtrag 2026-11-19, 10:10–10:14: Modus nur Clip ohne Stream, nach Aus und Ein

**Setup:** Der Nutzer hat das Kabel Out 2 → In 1 gezogen und das Case aus- und eingeschaltet, ohne das Menü zu öffnen. acdc1 im Case, alle Eingänge offen, kein Stream. Zuletzt gewählt war am Vorabend nur Clip.

- **Zustand nach dem Neustart** (`out/owl_read/20261119_fx6a_after-restart/`): `v22.4.r-fx6a`, es läuft Slot 6 (Schliere, 29 % CPU), Storage 126 208 B, Regler 66 / 61 / 64 / 61.
- **Kabelprobe vor dem Mess-Patch:** Der Mess-Patch gibt in zwei Phasen 4 × In 1 auf alle Ausgänge, mit einem Kabel Out 2 → In 1 wäre das eine Schleife. Deshalb zuerst 3 s Sinus 220 Hz mit −40 dBFS an Out 2 bei offenem Stream (`acdc_rec.py --no-manifest`, Datei nur im Scratch-Ordner): an In 1–4 liegt 220 Hz bei −92…−99 dBFS (Datei), mit Kabel wären es etwa −34 dBFS. Kein Kabel.
- **Mess-Patch** `SchliereLedPath` um 10:11:28 mit `owl_write.py --run` geladen (nur RAM, `out/owl_write/acdc1/20261119/owl_write_101128.json`), 14-mal ausgelesen (`out/owl_read/20261119_fx6a_clip-nostream/01…14`). Einheit 1e-7 Vollausschlag, In 1 / In 2 / In 3:

| gelesen | Meldung | Wert |
|---|---|---|
| 10:11:58 | LEDblink (3 LEDs, 40 Hz) | +22 / +21 / +31 |
| 10:12:14 | LEDstat (4 LEDs dauerhaft) | +70 / +121 / +78 |
| 10:12:45 | LEDblink (laufendes Mittel über beide Durchläufe) | +26 / +27 / +33 |
| 10:13:01 | LEDstat | +272 / +257 / +156 |

- Danach per Program Change auf Slot 1 (`out/owl_read/20261119_fx6a_slot1/`: ACDC, 5 % CPU, `SR/BS/CH 48000 8 4`).

**Deutung:**
- **[gemessen] Nach Aus und Ein ohne Menü ist ein dunkler Modus aktiv, die Eingänge bleiben ohne Stream ruhig:** beim Blinken 0,3 % der Verschiebung im Modus normal (etwa −50 dB), statisch 0,6–2,2 %. Im Modus normal stünden hier −8000 und −12000. Damit ist der Modus gemerkt und nur Clip ohne Stream stört nicht.
- Ob nur Clip oder aus gemerkt ist, trennt diese Messung nicht: Ohne Stream tun beide Modi dasselbe [Code]. Die Ressourcen `ACDC.slot` und `ACDC.led` lassen sich mit `owl_read.py --slots 40…43` nicht lesen (keine Antwort). Den Unterschied zeigt erst die Clip-Probe mit Stream.
- Der statische Rest streut von Durchlauf zu Durchlauf um den Faktor 2 bis 4 (+70…+272). [Hypothese] Das ist langsame Drift der offenen Eingänge im 5-s-Fenster und keine feste Wirkung der LED-Parameter. Der Blink-Wert ist gegen Drift unempfindlich und liegt heute bei +2e-6…+3e-6, am Vorabend im Modus aus bei +1e-5. Der „Rest von +2e-5“ aus der ersten Messung ist damit keine feste Größe.

### Zweiter Nachtrag 2026-11-19, 10:21: Clip-Probe im gemerkten Modus

**Setup:** Wie oben, dazu Kabel Out 2 → In 1 (vom Nutzer gesteckt, vorher Slot 1 geprüft: ACDC, 5 % CPU). In 2–4 offen, Regler 66 / 61 / 64 / 62. `acdc_rec.py --dc 0 -1 0 0 --dc-ramp 20 --duration 30 --owl-read`, Manifest `D75-fx6a-clip-ramp-neg-b`, 16 Bit (Datei = Gerätewerte). Zum Vergleich die Aufnahme vom Vorabend (`D75-fx6a-clip-ramp-neg`) mit derselben Auswertung.

| | Vorabend (nur Clip im Menü gewählt) | heute (gemerkter Modus) |
|---|---|---|
| In 1 erreicht die Clip-Schwelle 0,9886 | 18,4373 s | 18,4149 s |
| In 1 erreicht den Anschlag (−0,99992) | 18,6633 s | 18,6387 s |
| Stufe im Mittel von In 2–4 (beste einzelne Stufe) | bei 18,4369 s | bei 18,4166 s |
| Abstand der Stufe zur Schwelle / zum Anschlag | −0,3 ms / −226 ms | +1,7 ms / −222 ms |
| Höhe der Stufe, In 2 / In 3 / In 4 (Mittel 1,2 s danach gegen den Trend davor) | −101 / −146 / −82e-6 | −195 / −210 / −196e-6 |
| Mittel In 2–4, 0,3–1,3 s danach gegen 16–18,2 s | −108e-6 | −202e-6 |

Die Stufe bleibt bis zum Ende der Aufnahme stehen (heute −215…−258e-6 gegen das Mittel 14–18 s). Streuung derselben Statistik an Stellen ohne Ereignis: 10…26e-6.

**Deutung:**
- **[gemessen] Die offenen Eingänge springen in dem Moment, in dem In 1 die Clip-Schwelle der Firmware erreicht, nicht erst am Anschlag des Wandlers** (in beiden Aufnahmen innerhalb von 2 ms an der Schwelle, 220 ms vor dem Anschlag). Die Schwelle 0,9886 kennt nur die Firmware. Der Sprung ist also die rote LED 1 und nicht das Übersteuern von In 1. Damit entfällt die Gegenprobe im Modus aus als Pflicht.
- **[gemessen] Gemerkt ist nur Clip:** Im Modus aus reagiert die Firmware an der Schwelle nicht [Code]. Der Modus hat Aus und Ein überstanden.
- **Eine rote LED ohne Grün kostet −1,1e-4…−2,0e-4 Vollausschlag** (etwa −1…−2 mV), gegen −2,9e-4 für Rot mit Grün im Modus normal (D74). Der Wert von heute ist fast doppelt so groß wie der vom Vorabend. Unterschiede zwischen beiden Aufnahmen: Reglerstellung (127 / 52 / 2 / 74 gegen 12 Uhr), am Vorabend hing Out 1 am zweiten Interface, heute nicht geprüft. Die Ursache ist offen.
- **Folge für den Modus nur Clip:** Ein Clip kostet einen Knack von der Größe einer LED. Das ist gewollt (der Clip selbst ist die größere Störung), der Modus ist aber nur bis zum ersten Clip störungsfrei.

**Wiederholung um 10:32** (`D75-fx6a-clip-ramp-neg-c`, damit der Nutzer die LED beobachten kann, sonst unverändert): Schwelle bei 18,3794 s, Anschlag bei 18,6006 s, Stufe bei 18,3796 s (+0,2 ms zur Schwelle, −221 ms zum Anschlag), In 2 / In 3 / In 4 −211 / −219 / −217e-6, Mittel danach −242e-6. Die Höhe von heute ist damit wiederholt, der kleinere Wert vom Vorabend bleibt ungeklärt. **Beobachtung des Nutzers:** Die LED hat rot geleuchtet. Damit ist die Clip-Anzeige im Modus nur Clip auch am Gerät gesehen.

**Zur Messung um 23:24 (Nutzer, 2026-11-19):** Er meint, es sei nur Clip eingestellt gewesen, ist aber nicht sicher. Welche LED bei der Rampe am Vorabend leuchtete, weiß er nicht mehr. Heute ist nur Clip ohne Stream ruhig, allerdings aus der Ressource gelesen und nicht frisch im Menü gewählt. Im Code ist der Weg derselbe (`acdc_boot.led_mode`). Probe: nur Clip im Menü wählen und sofort ohne Stream messen.

### Dritter Nachtrag 2026-11-19, 10:36–10:39: nur Clip frisch aus dem Menü, ohne Stream

**Setup:** Der Nutzer hat das Kabel gezogen, das Boot-Menü geöffnet, mit Regler 2 nur Clip gewählt und mit Regler 4 bestätigt, danach kein Aus und Ein. Zustand (`out/owl_read/20261119_fx6a_after-menu-clip/`): Slot 6 (Schliere, 30 % CPU), Storage 126 208 B, Regler 68 / 59 / 63 / 61. Kabelprobe wie im ersten Nachtrag (220 Hz, −40 dBFS an Out 2, 4 s Stream): In 1–4 bei −93…−100 dBFS, kein Kabel. Mess-Patch um 10:36:18 geladen (`out/owl_write/acdc1/20261119/owl_write_103618.json`), 20-mal ausgelesen (`out/owl_read/20261119_fx6a_clip-menu-nostream/01…20`), danach Program Change auf Slot 1.

| gelesen | Meldung | Wert (1e-7 Vollausschlag, In 1 / In 2 / In 3) |
|---|---|---|
| 10:36:46 | LEDblink | +34 / +35 / +34 |
| 10:36:59 | LEDstat | +5 / +15 / +44 |
| 10:37:33 | LEDblink (laufendes Mittel) | +41 / +39 / +38 |
| 10:37:47 | LEDstat | +75 / +37 / +84 |
| 10:38:27 | LEDblink (laufendes Mittel) | +46 / +43 / +39 |

**Deutung:**
- **[gemessen] Nur Clip ist auch frisch aus dem Menü ohne Stream ruhig:** Blinken 0,4–0,5 % der Verschiebung im Modus normal, statisch unter 1 %. Die laute Messung vom 2026-11-18, 23:24 lässt sich mit nur Clip nicht nachstellen.
- [Hypothese] Um 23:24 war der Modus normal aktiv, zum Beispiel weil Regler 2 im linken Drittel stand oder das Menü ohne Bestätigung endete. Dazu passen die Werte von damals (volle Verschiebung wie im Modus normal).
- Einschränkung: Zwischen Menü und Messung lief für die Kabelprobe 4 s lang ein Stream. Ein Fehler, der nur ohne jeden Stream seit dem Einschalten auftritt, wäre damit nicht ausgeschlossen. Im Code gibt es dafür keinen Anhalt [Code].
- Der statische Wert streut wieder (+5…+84), der Blink-Wert liegt stabil bei +3e-6…+5e-6.

### Vierter Nachtrag 2026-11-19, 10:39–10:43: Download-Stresstest

`tools/dump_stress.py`, LED-Modus nur Clip, kein Kabel, kein Stream, je 20 Runden über alle sechs Slots.

| Serie | laufender Patch | CPU | Downloads | beschädigt | Hänger |
|---|---|---|---|---|---|
| `D75-fx6a-slot2` | TapeDelay | 31–32 % | 120 | 0 | nein |
| `D75-fx6a-slot5` | Tanh3 | 50–51 % | 120 | 0 | nein |

Tabellen in `out/D75-fx6a-slot2-session-table.md` und `out/D75-fx6a-slot5-session-table.md`, danach Program Change auf Slot 1. **[gemessen] 240 von 240 Downloads in Ordnung, wie fx5a (D63).** Der Lauf mit Audio-Stream fehlt noch, er gehört zum Loop-Test.

**Offen (ersetzt die Liste oben):**
- Warum die Stufe einer roten LED heute doppelt so groß ist wie am Vorabend.
- Rausch-A/B gegen fx5a (weitere Flashes). Loop-Test und Stresstest mit Stream: D76.

## D76 – fx6a: Loop-Test bestanden, Program Change bei offenem Stream bricht die Wiedergabe (2026-11-19, 10:44–10:55)

**Anlass:** Abnahme Build 8, Punkt 5 (Loop-Test wie D57/D63). Dabei ein neuer Fehler, der mit Build 8 vermutlich nichts zu tun hat.

**Setup:** acdc1 im Case, fx6a, LED-Modus nur Clip, Alltags-Kette, vier Patchkabel Out n → In n (Nutzer), Regler 68 / 60 / 63 / 60. `acdc_rec.py --sine 440 530 670 790` (−6 dBFS, 1 s Einblenden), danach `phase_slips.py` und `stale_samples.py` (JSON in `out/B8/`).

### Loop-Test

| ID | laufender Patch | Slips | veraltete Samples | Geräte-Meldung | CPU |
|---|---|---|---|---|---|
| `B8-fx6a-loop` | Slot 1 ACDC | 0 auf allen 4 Kanälen | 0 von 96 000 je Kanal | `tx ovf 0.3819 0.9513 4` | 8 % |
| `B8-fx6a-loop-tanh3-b` | Slot 5 Tanh3, schon vor dem Stream gewählt | 0 | 0 | `tx ovf 1.0000 1.0000 32` (Stream-Start) | 52 % |
| `B8-fx6a-loop-tanh3-dl` | Tanh3, währenddessen 48 Slot-Downloads (`D75-fx6a-slot5-stream`, 48 von 48 in Ordnung) | 0 ganze Samples | 0 | nicht gelesen | – |

- Stream-Meldungen von PortAudio: 0 in allen Läufen. Pegel −6,04…−6,10 dBFS wie D57 und D63.
- Im Lauf mit Downloads meldet `phase_slips.py` wieder nur auf Kanal 2 (530 Hz) 30 Ereignisse unter 0,005 Samples zwischen 10 und 33 s, solange die Downloads liefen. Derselbe Nebenbefund wie unter fx5a (D63).
- Die Meldung `tx ovf 0.3819 0.9513 4` im ersten Lauf ist neu: Der Sendepuffer war zu 95 % voll, vier Samples (ein Frame) wurden verworfen [Code: `usbd_tx_convert`]. In den 60 s der Aufnahme gibt es keinen Slip, das Ereignis lag also in den 3 s davor (Stream-Start). Sonst steht dort `… 1.0000 32`.
- **[gemessen] Loop-Test bestanden**, auch unter 52 % Patch-Last und während der Downloads. Damit zusammen mit D75: 288 von 288 Downloads in Ordnung.

### Program Change bei offenem Stream

Im ersten Tanh3-Lauf (`B8-fx6a-loop-tanh3`) hatte ich die Reihenfolge geändert: erst den Stream geöffnet, dann per Program Change auf Slot 5 geschaltet (damit Tanh3 mit den Kabeln nie ohne Stream läuft). Ergebnis: Die Wiedergabe setzt periodisch aus. Zwei kurze Läufe (25 s, Program Change etwa 5 s nach dem Start) grenzen das ein:

| ID | Program Change bei offenem Stream | stiller Anteil danach | Abstand / Länge der Aussetzer (Median) | Geräte-Meldung | CPU |
|---|---|---|---|---|---|
| `B8-fx6a-loop-tanh3` | Slot 1 → 5 (Tanh3), vor Beginn der Aufnahme | 10,3 %, über 60 s gleichbleibend | 4223 / 415 Frames | `fb 48.0088 46.3203` | 52 % |
| `B8-fx6a-pc2-stream` | Slot 1 → 2 (TapeDelay) | 10,0…10,7 % | 4223 / 397 Frames | `fb clamp -72 32` | 36 % |
| `B8-fx6a-pc1-stream` | Slot 1 → 1 (derselbe Patch) | 9,8…11,3 % | 4224 / 435 Frames | `fb clamp -57 32` | 6 % |

- In den stillen Abschnitten lesen alle vier Eingänge gleichzeitig nur ihren Ruhewert (−0,035 / −0,037 / −0,026 / −0,033, Streuung 1e-4): Die Ausgänge geben wirklich nichts aus, die Aufnahme selbst läuft weiter.
- Die Phase der Töne ist nach jedem Aussetzer dieselbe wie davor (auf 0,03 Samples). Die Samples, die der Rechner in dieser Zeit schickt, gehen also verloren und werden nicht verspätet gespielt.
- Vor dem Program Change ist die Aufnahme sauber, der erste Aussetzer kommt 7,2 s nach Beginn der Datei, also mit dem Wechsel. Nach dem Schließen und neuen Öffnen des Streams ist alles wieder in Ordnung (`B8-fx6a-loop-tanh3-b` lief direkt danach).
- `fb clamp -72 32`: Der Füllstand des Empfangspuffers liegt 57…72 Samples unter dem Soll, die Regelung aus Patch 06 steht am Anschlag (+32 LSB ≈ 40 ppm) und kann 10 % Verlust nicht ausgleichen [Code].

**Deutung:**
- **[gemessen] Ein Program Change bei offenem Stream bricht die USB-Wiedergabe bis zum nächsten Stream-Start:** rund 10 % der Zeit Stille an allen Ausgängen, etwa alle 88 ms für 8–9 ms. Unabhängig vom Ziel-Patch und von der Rechenlast.
- [Hypothese] Der Fehler ist älter als Build 8. Patch 17 fasst weder den Program Change noch den USB-Audio-Weg an, und diese Reihenfolge wurde bisher nie gemessen (D57 und D63 wählten den Patch vor dem Stream). Kandidaten [Code, ungeprüft]: Der Audio-Task steht während des Ladens, Empfangspuffer und Zähler passen danach nicht mehr zusammen, oder Schreib- und Lesezeiger des Ringpuffers stehen so, dass je Umlauf ein Stück verworfen wird (4223 Frames Abstand).
- Folge im Alltag: Wer vom Rechner aus den Patch wechselt, während ein Aufnahmeprogramm das AC/DC offen hält, bekommt gestörte Wiedergabe über die AC/DC-Ausgänge. Die Aufnahme der rohen Eingänge ist nach dieser Messung nicht betroffen (nicht eigens geprüft).

**Einschränkungen und offen:**
- Gegenprobe unter fx5a (gleiche 25 s) beim Zurückflashen für das Rausch-A/B: zeigt, ob der Fehler älter ist.
- Ursache im Code finden und beheben (eigener Patch), danach dieselben Läufe.
- Ob auch die Aufnahme (TX) in diesem Zustand Samples verliert, ist nicht gemessen: dafür braucht es eine Quelle, die nicht über die Wiedergabe läuft.
- Der Loop-Test lief im LED-Modus nur Clip. Im Modus normal ist der Code der LED-Schleife derselbe wie unter fx5a.

## D77 – Build-8-Sitzung: Rauschen fx6a gegen fx5a, Gegenprobe zum Program Change unter fx5a (2026-11-19, 10:58–11:23)

**Anlass:** Letzter Punkt der Abnahme von Build 8 (`docs/05`, „Build 8“, Abnahme 5) und Gegenprobe zu D76. Freigabe des Nutzers für beide Flashes.

**Setup:** acdc1 im Case, Alltags-Kette, Eingänge offen, Regler 12 Uhr (62…66 / 58…59 / 66 / 62…63), Slot 1 ACDC (vor dem Stream gewählt), je 2 × 60 s `acdc_rec.py --reps 2 --owl-read`. fx6a im LED-Modus normal (vom Nutzer im Menü gewählt, mit dem Mess-Patch geprüft). Reihenfolge: `B8-fx6a-a` → Flash fx5a (`firmware/flashlog/20261119_build7-fx5a-ab/`, Readback bytegleich, A1 bestanden) → `B8-fx5a` → Kabel Out 1 → In 1, `B8-fx5a-pc1-stream` → Flash fx6a (`firmware/flashlog/20261119_build8-fx6a-zurueck/`, Readback bytegleich, A1 bestanden) → `B8-fx6a-b`. Vor jeder Messung ohne Kabel eine Kabelprobe mit leisen Testtönen (alle Eingänge unter −97 dBFS).

**Störgröße (Nutzer):** Bei `B8-fx6a-a` und bei allen Messungen des Vormittags davor (D75-Nachträge, D76) hing ein Oszillator im Case am Strom, am Vorabend nicht. Ab `B8-fx5a` ist er abgesteckt.

### Rauschen

Tabelle `out/B8-session-table.md` (`family_table.py`, Datei-dBFS, Mittel über 4 Kanäle und 2 Läufe, Δ gegen fx5a):

| Messung | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| `B8-fx6a-a` (Anfang, mit Oszillator) | −72,88 (−1,04) | −77,30 (−0,74) | −75,58 (−1,44) | −83,08 (+0,34) | −119,88 (−3,40) |
| `B8-fx5a` | −71,84 | −76,56 | −74,14 | −83,42 | −116,48 |
| `B8-fx6a-b` (Ende) | −70,84 (+1,00) | −75,26 (+1,30) | −73,22 (+0,92) | −83,26 (+0,16) | −118,87 (−2,39, ein Lauf) |

- Die Sitzung driftet stetig nach oben: RMS, Rest und Kamm steigen von der ersten zur letzten Messung um 2,0…2,4 dB. fx5a liegt dazwischen, beim RMS auf 0,02 dB in der Mitte der beiden fx6a-Kontrollen, beim Kamm 0,26 dB darüber, beim Rest 0,28 dB darunter.
- fs/8 bleibt in allen sechs Läufen innerhalb von ±0,3 dB. Die Mischprodukte findet die Analyse nicht in jedem Lauf (in `B8-fx6a-b-r2` gar nicht), sie sind wie in D64 nicht entscheidbar.
- Wiederholungen innerhalb eines Blocks liegen ≤ 0,45 dB auseinander.
- `family_table.py` brach ab, wenn eine Familie in einer Aufnahme fehlt. Es schreibt jetzt „–“ und mittelt über die Läufe, die sie haben.

**Deutung:**
- **[gemessen] Kein Hinweis auf einen Unterschied zwischen fx6a (Modus normal) und fx5a:** fx5a liegt zwischen den beiden fx6a-Kontrollen. Das passt zum Code, im Modus normal ist der periodische Pfad derselbe.
- Die Drift von 2 dB in 20 Minuten (Start der Blöcke 11:00, 11:09, 11:19) ist größer als in früheren Sitzungen (0,4…0,8 dB, D44). Sie trifft auch den breitbandigen Rest. Ursache offen: Aufwärmen nach den Neustarts, der Oszillator (abgesteckt wurde es lauter, nicht leiser), etwas anderes im Case. Eine Aussage auf wenige Zehntel dB erlaubt die Sitzung deshalb nicht.
- Der Vergleich der dunklen Modi gegen normal (Linie der LED-PWM mit Signal) steht aus. Mit offenen Eingängen leuchten die LEDs auch im Modus normal nicht.

### Program Change bei offenem Stream unter fx5a

`B8-fx5a-pc1-stream`: Loop Out 1 → In 1, 440 Hz, Program Change Slot 1 → 1 etwa 5 s nach dem Start. Danach 9,4…10,8 % Stille, 214 Aussetzer, Abstand 4223 Frames, Länge 387 Frames (Median), Meldung am Ende `tx ovf 0.4375 1.0000 32`.

**[gemessen] Der Fehler aus D76 tritt unter fx5a genauso auf.** Er ist älter als Build 8 und kein Mangel von Patch 17. Ab welchem Build es ihn gibt, ist offen (Kandidaten: die Feedback-Regelung aus Patch 06 oder schon die Original-Firmware).

### LED-Verschiebung im Modus normal an diesem Tag

Mess-Patch `SchliereLedPath`, Einheit 1e-7 Vollausschlag, In 1 / In 2 / In 3:

| gelesen | Oszillator | LEDblink | LEDstat |
|---|---|---|---|
| 2026-11-18, 23:15 (D75) | ab | −8421 / −8085 / −8507 | −12344 / −11742 / −11875 |
| 10:59 | am Strom | −11376 / −10797 / −11132 | −16399 / −15470 / −15502 |
| 11:19 | ab | −10530 / −10563 / −10933 | −15226 / −15007 / −15051 |

Die Verschiebung ist heute 25…35 % größer als am Vorabend, mit und ohne Oszillator. Dazu passt, dass die Stufe einer roten LED heute doppelt so groß war (D75, zweiter Nachtrag). [Hypothese] Die Kopplung hängt von etwas ab, das sich über Nacht geändert hat (Temperatur, Versorgung im Case, Reglerstellung: am Vorabend standen die Regler zeitweise nicht auf 12 Uhr). Die Werte aus D74 gelten deshalb nur als Größenordnung.

**Fazit:** Die Abnahme von Build 8 ist vollständig: Flash, A1, drei LED-Modi, gemerkter Modus, Clip-Anzeige, Stresstest (288 von 288), Loop-Test, Rauschen ohne Hinweis auf eine Änderung. Über die Alltags-Firmware entscheidet der Nutzer.

**Einschränkungen und offen:**
- Drift der Sitzung (2 dB) und die größere LED-Verschiebung von heute sind nicht erklärt.
- Der Fehler beim Program Change ist nicht behoben.


---

## D78 – Build 9 `v22.4.r-fx7a` auf acdc1: Flash und A1 (2026-11-19, 11:46–11:47)

**Anlass:** Abnahme von Build 9 (Patch 18, LED-PWM mit 48 000 Hz statt 2320,54 Hz, `docs/05`, „Build 9“). Freigabe des Nutzers für den Flash.

**Flash:** `tools/flash_acdc.py acdc1-build9-fx7a --yes`, Log `firmware/flashlog/20261119_build9-fx7a/`. Vorher fx6a mit sechs Slots, DFU-Neustart, 110 088 B geschrieben, Readback bytegleich, Rest 0xFF. Neustart durch den Nutzer (Case aus, USB ab, Case an, USB an), danach `--a1`: bestanden (acdc1, `AC/DC v22.4.r-fx7a`, 48 000 Hz, Blockgröße 8, Slots 1–6 unverändert, Storage 126 208 B).

**Zustand danach:** Slot 6 (Schliere) läuft als gemerkter Slot, CPU 29 %, Regler 62 / 58 / 65 / 63 von 127. LED-Modus normal (gemerkt aus D77, nicht neu gewählt). Kein Kabel gesteckt, kein Stream. Oszillator im Case weiter abgesteckt (Nutzer), wie am Ende von D77.

### LED-Linie am Ausgang (11:53)

**Setup:** wie D73: Mess-Patch `SchliereLedTest` (nur RAM, `owl_write.py --run` um 11:50, `out/owl_write/acdc1/20261119/owl_write_115008.json`), Out 1 → UMC202HD In 1, UMC-Gain unverändert seit D73 (Nutzer), kein Stream an acdc1. Vorher Kabelprobe (−60 dBFS Sinus an alle Ausgänge, an keinem Eingang über −95 dB, also kein Kabel an den Eingängen). Regler 62 / 58 / 66 / 63 von 127 (nach der Aufnahme gelesen), nicht bewegt. CPU 31 %.

**Aufnahme:** `D78-fx7a-ledtest-umc`, `20261119_acdc1_fx7a-schliere-ledtest-out1-via-umc_g12_usb-plugged.wav`, 90 s, 48 kHz, 24 Bit, `scale = 1`, `acdc_rec.py --device UMC202HD --input-only --channels 2 --format pcm24 --scale 1 --prompt --progress 1`. Lage der Phasen aus dem 40-Hz-Blinken (an bei 28,5 und 68,45 s), weil die grüne Phase keine Linie mehr hat. D73 mit demselben Skript neu ausgewertet (Blinken an bei 19,9 und 59,9 s). Je Phase 0,6 s nach dem Wechsel bis 1,0 s vor dem nächsten, Welch 65 536 Punkte, Linie = stärkster Bin in ±0,8 Hz. Skripte in `out/D78-fx7a-ledtest-umc/` (`phases.py`, `ctrl.py`). Alle Pegel in dBFS des UMC, Kanal 1.

| | D73 fx5a aus | D73 grün 60 % | D78 fx7a aus | D78 grün 60 % |
|---|---|---|---|---|
| RMS gesamt | −47,4 | **−40,6** | −41,5 | **−41,5** |
| Rauschen 200–2000 Hz (Median) | −88,0 | −87,9 | −82,1 | −82,2 |
| LED-PWM 2320,54 Hz | −90,0 | **−39,8** | −82,9 | **−85,2** |
| ×2 / ×3 | −92,2 / −80,3 | −52,2 / −51,9 | −85,7 / −85,3 | −83,7 / −85,5 |
| Kamm 1 kHz / 5 kHz | −70,8 / −65,2 | −71,6 / −65,0 | −72,2 / −70,2 | −71,5 / −70,1 |
| Blockrate 6 / 12 / 18 kHz | −77,4 / −77,8 / −74,4 | −77,7 / −77,8 / −74,7 | −73,2 / −75,8 / −71,2 | −74,9 / −76,6 / −70,6 |

(Rauschen hier als Median je Bin, deshalb andere Zahlen als die Tabelle in D73. Die Werte aus D73 stimmen sonst auf ±1 dB mit der ersten Auswertung überein.)

Suche nach neuen Linien, grün gegen das Mittel der drei Aus-Phasen, 50 Hz–20 kHz: unter fx7a höchstens +15,1 dB an einzelnen Bins, 99,9-%-Quantil +7,9 dB. Dieselbe Rechnung für LED 1 rot (+14,6 / +7,8 dB) und LED 1–4 rot (+18,2 / +8,0 dB) gibt dasselbe, also Streuung. Unter fx5a (D73) waren es +51,4 dB bei 2321 Hz und +17,0 dB im Quantil. 0,5–20 Hz: grün −53,7, aus −53,5 dB (D73: −54,8 / −54,8).

**Deutung [gemessen]:**
- **Die LED-PWM-Linie ist mit fx7a weg.** Gedimmtes Grün bringt bei 2321 Hz und den Vielfachen nichts mehr über das Rauschen (−85,2 dBFS gegen −39,8 dBFS unter fx5a, also mindestens 45 dB weniger, begrenzt durch das Rauschen). Der Gesamtpegel in der grünen Phase ist gleich wie bei dunklen LEDs (unter fx5a +6,8 dB).
- **Es taucht keine neue Linie auf**, weder im Hörbereich noch unter 20 Hz. Der Unterschied grün gegen aus ist so groß wie zwischen zwei Phasen ohne PWM.
- Das Blinken mit 40 Hz stört weiter (RMS −30,6 dBFS, +10,9 dB über aus): Das ist der Effekt des Schaltens, nicht der PWM, und war so erwartet.

**Einschränkungen:**
- Das Grundrauschen liegt heute 6 dB höher als in D73 (RMS −41,5 gegen −47,4 dBFS). Ursache sind sehr wahrscheinlich die Regler: In D73 stand Feedback (Regler 4) am Linksanschlag (1 von 127), heute auf 12 Uhr (63) [Hypothese]. Die Nachweisgrenze für eine Linie liegt damit bei etwa −85 dBFS statt −90 dBFS.
- Ob die Faltung der 48 kHz in den ADC-Daten wirklich bei ≈ 0 Hz landet, zeigt diese Aufnahme nicht (UMC wechselspannungsgekoppelt, Ausgang nach dem Patch). Das prüft die Messung an den Eingängen.
- Nur Out 1, nur die Eingangs-LEDs gedimmt.

### LED-Verschiebung an den Eingängen (11:59–12:01)

**Setup:** Mess-Patch `SchliereLedPath` aus D74 (nur RAM, `owl_write.py --run` um 11:59, `out/owl_write/acdc1/20261119/owl_write_115907.json`). Kein Kabel gesteckt (Out 1 → UMC vorher gezogen), kein Stream, Regler wie oben, LED-Modus normal, Oszillator abgesteckt. Zwölf Mal `owl_read.py` im Abstand von etwa 13 s, Reports in `out/owl_read/acdc1/20261119_1159*/` bis `…_1201*/`. Einheit 1e-7 Vollausschlag (≙ µV bei ±10 V), In 1 / In 2 / In 3.

| Build | gelesen | LEDblink (3 LEDs, 40 Hz) | LEDstat (4 LEDs dauerhaft) |
|---|---|---|---|
| fx6a (D77) | 11:19 | −10530 / −10563 / −10933 | −15226 / −15007 / −15051 |
| fx7a | 11:59:39 | −10605 / −10530 / −11156 | −15440 / −15019 / −15391 |
| fx7a | 12:00:31 | −10620 / −10546 / −11167 | −15278 / −14883 / −15280 |
| fx7a | 12:01:22 | −10635 / −10558 / −11175 | −15612 / −15172 / −15475 |

**Deutung [gemessen]:** Die Verschiebung der Eingänge durch den LED-Strom ist unter fx7a gleich wie unter fx6a vor 40 Minuten (Blinken +0,2…+2 %, statisch −1…+2 %). Das war erwartet: Die Messung schaltet LEDs ganz ein und aus, die PWM-Frequenz spielt dafür keine Rolle. Gegen die langsame Verschiebung helfen weiter nur die Modi „nur Clip“ und „aus“ (Build 8).

**Einschränkung:** Diese Messung prüft nicht, wohin eine gedimmte LED mit 48 kHz in den ADC-Daten faltet. Dafür bräuchte es gedimmte LEDs bei laufender Aufnahme der rohen Eingänge. Mit Stream zeigen die Eingangs-LEDs im Modus normal aber den rohen Pegel und überschreiben, was der Patch setzt (D36).

Danach läuft weiter `SchliereLedPath` im RAM.

### Helligkeit am Gerät

Laut Nutzer passt die Helligkeit der LEDs unter fx7a („led helligkeit passt“, 12:05).

**Offen:** Rauschen gegen fx6a und Loop-Test (`docs/05`, „Build 9“, Punkt 4), siehe D79.

---

## D79 – Build-9-Sitzung: Rauschen fx7a gegen fx6a (2026-11-19, ab 12:05)

**Setup:** acdc1 im Case, Alltags-Kette, Eingänge offen (Kabelprobe in D78), Regler 12 Uhr, Slot 1 ACDC (vor dem Stream per Program Change gewählt), LED-Modus normal, Oszillator im Case abgesteckt, je 2 × 60 s `acdc_rec.py --reps 2 --owl-read`. Reihenfolge: `B9-fx7a-a` → Flash fx6a (`firmware/flashlog/20261119_build8-fx6a-ab9/`, Readback bytegleich) → `B9-fx6a` → Flash fx7a → `B9-fx7a-b`.

### Neustart über `dfu-util :leave` statt von Hand (12:20)

**Anlass:** Der Nutzer fragte, ob der Neustart mit Case aus, USB ab, Case an, USB an nötig ist. Nur Case aus und an reicht nicht, weil das USB-Kabel das Board versorgt und es im DFU bleibt (D3).

**Test:** Nach dem Flash von fx6a (Readback bytegleich) hing acdc1 noch im DFU-Modus. Der Nutzer hatte USB kurz abgezogen (Case blieb an) und wieder gesteckt, acdc1 war weiter im DFU (`0483:df11`, Seriennummer `200364500000`). Dann nur lesend: `dfu-util -d 0483:df11 -S 200364500000 -a 0 -s 0x08000000:131072:leave -U readback_leave.bin` (Log `dfu-util_upload_leave.txt` im Flash-Log-Ordner). Readback 131 072 B bytegleich mit fx6a, Rest 0xFF. Danach „Submitting leave request...“ und „Error during download get_status“, Exit 74: Das Gerät verlässt den DFU-Modus, bevor es den Status melden kann. 4 s später kein DFU-Gerät mehr.

**Ergebnis [gemessen]:** acdc1 startete ohne Zutun des Nutzers die Firmware. `flash_acdc.py --a1` bestanden (acdc1, `AC/DC v22.4.r-fx6a`, 48 000 Hz, Blockgröße 8, Slots unverändert, Slot 6 mit 29 % CPU). Ob das Audio nach diesem Start gleich läuft wie nach einem Kaltstart, zeigt `B9-fx6a` und der Vergleich `B9-fx7a-a` (Kaltstart) gegen `B9-fx7a-b` (über `:leave`).

**Unterschied zum Kaltstart [Hypothese]:** Der Codec und alles andere außerhalb der MCU bleiben unter Strom. Ob der ROM-Bootloader beim Verlassen einen Reset auslöst oder springt, ist nicht geprüft. Die Firmware lief nach dem Start jedenfalls mit richtiger Version, Abtastrate und Slots.

### Beobachtung: Das Modul fiept hörbar (Nutzer, etwa 12:10)

Mit acdc1 im DFU-Modus (nach dem Flash von fx6a, vor dem Neustart, also ohne Firmware, Audio und LED-PWM) hört der Nutzer ein leises Fiepen aus dem Modul, ohne dass etwas angeschlossen ist. Fast konstant, vielleicht leicht wandernd, geschätzt 800–1000 Hz, zu leise für eine genaue Angabe. Heute schon vorher gehört, gestern vielleicht auch (da mit Kopfhörern).

**Nachtrag (Nutzer):** Zieht man im DFU-Modus das USB-Kabel ab (Case weiter an), wird das Fiepen deutlich leiser und höher.

**Deutung [Hypothese]:** Da es im DFU-Modus auftritt, hängt es nicht an Build 8 oder 9. Dass es sich mit dem USB-Kabel ändert, spricht für eine Abhängigkeit von Laststrom oder Versorgung über USB (USB-Schnittstelle aktiv, Strom über VBUS oder die Kabelmasse). Ein leiser Ton, der mit der Last wandert, passt zu einem Schaltregler im Pulsbetrieb bei geringer Last, dessen Spule oder ein Keramikkondensator hörbar mitschwingt. Ob die Quelle auf dem Modul oder im Netzteil des Cases sitzt, ist offen. Ob es mit den elektrischen Störlinien zusammenhängt, ebenfalls.

### Rauschen (12:05–12:35)

Tabelle `out/B9-session-table.md` (`family_table.py`, Datei-dBFS, Mittel über 4 Kanäle, Δ gegen fx6a). Alle sechs Läufe ohne Stream-Fehler (am Ende nur `tx ovf … 32` vom Stream-Start), CPU 6–7 %, Regler 12 Uhr.

| | Start | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|---|
| `B9-fx7a-a` (Anfang) | Kaltstart (11:46) | −72,09 (−1,02) | −75,71 (−0,08) | −75,26 (−1,86) | −83,25 (±0,00) | −119,05 (+1,03) |
| `B9-fx6a` (Mitte) | `:leave` | −71,08 | −75,63 | −73,40 | −83,26 | −120,08 |
| `B9-fx7a-b` (Ende) | `:leave` | −71,00 (+0,08) | −75,59 (+0,05) | −73,29 (+0,11) | −83,30 (−0,04) | −119,39 (+0,69) |

LED-PWM-Linie (2320,54 Hz und Vielfache) in den rohen ADC-Daten laut Analyse-Report:

| | gefunden |
|---|---|
| `B9-fx6a-r1` / `-r2` | ja, 2320,544 Hz auf 3 von 4 Kanälen, −115…−117 dB, dazu k = 9 (20 884,9 Hz) auf Kanal 2, −114 dB |
| `B9-fx7a-a`, `B9-fx7a-b` (je 2 Läufe) | nein, auf keinem Kanal |

**Deutung:**
- **[gemessen] fx7a rauscht wie fx6a.** `B9-fx7a-b` liegt in allen Familien innerhalb von 0,15 dB bei fx6a (Mischprodukte +0,7 dB, die streuen von Lauf zu Lauf um mehrere dB). fs/8 und Rest sind in allen sechs Läufen gleich (±0,1 dB).
- **[gemessen] Die LED-PWM-Linie ist auch in den rohen ADC-Daten weg.** Unter fx6a steht sie mit offenen Eingängen bei −115 dB (die Eingangs-LEDs zeigen beim Aufnehmen den rohen Pegel, mit offenem Eingang schwach), unter fx7a ist sie in keinem Lauf zu finden. Eine neue Linie meldet die Analyse nicht. [Hypothese] Ein Teil davon kann auch daher kommen, dass unter fx7a Werte unter 2,4 % dunkel bleiben und die LEDs mit offenem Eingang gar nicht leuchten.
- **Kontrolle A weicht ab:** Kamm −1,9 dB und RMS −1,0 dB gegen die beiden späteren Läufe, Rest und fs/8 gleich. Zwei Erklärungen sind möglich: die Drift der Sitzung (D77: +1…2 dB in 20 Minuten, alle Starts kalt, gleiche Richtung) oder die Art des Starts (A nach Kaltstart, fx6a und B nach `:leave`). Diese Sitzung trennt das nicht.

**Kaltstart-Probe (12:30):** Direkt nach `B9-fx7a-b` hat der Nutzer acdc1 kalt neu gestartet (Case aus, USB ab, Case an, USB an), dann Slot 1 und `B9-fx7a-c` (2 × 60 s, ohne Stream-Fehler):

| | Start | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|---|
| `B9-fx7a-c` (12:31) | Kaltstart | −70,64 (+0,44) | −75,19 (+0,45) | −72,91 (+0,49) | −83,38 (−0,13) | −123,03 (−2,96) |

Auch hier keine LED-PWM-Linie in den rohen Eingängen.

- **[gemessen] Die Abweichung von Kontrolle A ist Drift, nicht die Art des Starts.** Nach dem Kaltstart liegt der Kamm bei −72,9 dBFS, also nicht wieder bei −75,3 wie um 12:05, sondern weiter oben als nach `:leave`. Über die Sitzung steigt der Kamm stetig: −75,3 (12:05) → −73,4 (12:22) → −73,3 (12:28) → −72,9 (12:31), dazu RMS und Rest ab etwa 12:30 um 0,4 dB. fs/8 bleibt in allen acht Läufen innerhalb von 0,15 dB.
- Ein Start über `:leave` ändert das Rauschen also nicht messbar gegen einen Kaltstart (innerhalb der Drift von etwa 0,5 dB zwischen zwei benachbarten Läufen).

**Fazit:** Build 9 bringt beim Rauschen keinen Nachteil gegen fx6a und nimmt die LED-PWM-Linie aus Ausgängen (D78) und rohen Eingängen. Der Start über `dfu-util :leave` taugt als Ersatz für den Neustart von Hand. Die Drift des Kamms (+2,4 dB in 26 Minuten) ist wie in D77 nicht erklärt.

### Loop-Test (12:36)

Kabel Out 1–4 → In 1–4 (Nutzer), Gain 12 Uhr, Slot 1, `acdc_rec.py --sine 440 530 670 790 --duration 60 --owl-read`, Aufnahme `B9-fx7a-loop` (`20261119_acdc1_fx7a-loop_g12_usb-stream.wav`). Stream-Meldungen 0, Geräte-Meldung am Ende `tx ovf 1.0000 1.0000 32` (Stream-Start).

- `phase_slips.py`: Pegel −6,0…−6,1 dBFS, Streuung 0,00 dB, 0 Ereignisse auf allen vier Kanälen (1-Sample-Sprung 5800- bis 14 000-fach über dem Phasenrauschen).
- `stale_samples.py`: 0 von 96 000 Samples falsch auf allen vier Kanälen.
- Ergebnisse in `out/B9-fx7a-loop/` (`phase_slips.json`, `stale_samples.json`).

**[gemessen] Loop-Test bestanden.** Die Abnahme von Build 9 ist damit vollständig (D78, D79). Über die Alltags-Firmware entscheidet der Nutzer.

Danach: Kabel stecken noch, Slot 1 läuft.

### Folge für den Flash-Ablauf (Entscheidung des Nutzers, 2026-11-19)

`:leave` ist ab jetzt der Standard: `tools/flash_acdc.py` liest nach dem Readback ein zweites Mal nur lesend mit `:leave` zurück, wartet, bis das DFU-Gerät verschwindet, und macht A1 selbst. Kaltstart von Hand nur noch mit `--cold`: wenn `:leave` scheitert, wenn ein Build am Einschalten etwas ändert (Takt, Codec-Init), wenn der Test das Einschalten betrifft und auf dem Rückweg nach einem Problem. Im Skript bisher nur gegen Attrappen getestet.

**Entscheidung (Nutzer, 2026-11-19):** fx7a ist die Alltags-Firmware auf acdc1. Rückweg fx6a, dann fx5a.

## D80 – Schliere: Tap- und Feedback-Modulation, Fassung 4 und Schliere M (2026-11-19, nachmittags, am Rechner)

**Anlass (Nutzer, 2026-11-19):** Moduliert man in Schliere den Tap, klingt es hart, bei Audio-Rate vermutlich mit Aliasing. Steckt man Out 2, 3 oder 4 auf In 4 (Feedback-CV), klingt es nach hartem digitalem Clipping in den Höhen. Frage: Wie macht das Vorbild das, und gibt es eine elegantere Art?

**Vorbild [belegt]:** Handbuch v1.2.1 des Vorbilds (PDF von der Hersteller-Seite, Fassung 2026-11-07) und Forum-Thread 296092. Das Vorbild überblendet genauso linear zwischen festen Abgriffen, mit Haltezonen (Diagramm „Level of each tap“). Audio-Rate am Tap beschreibt das Handbuch selbst als metallisch, „like FM or ring modulation“. Den CV glättet es (Thread #36), mit Firmware 1.1.1 wurde die Glättung gelockert („more responsive“). Ein anderes Verfahren für den Tap ist nicht dokumentiert.

**Mechanismus [Code]:** Zwischen zwei Abgriffen ist der Ausgang (1 − t)·A + t·B. Moduliert man t, werden die Kerben nicht verschoben, sondern ein- und ausgeblendet: eine Amplitudenmodulation, die Seitenbänder tragen fast die ganze Energie. Gefaltet wird, was die Abbildung CV → t an Oberwellen erzeugt. In Fassung 3 gab es drei Knicke: harte Totzone im Nulldurchgang (±0,5 V), Ränder der Haltezonen, Klemmung am Ende. Dazu wirkte der CV ungeglättet pro Sample. Beim Feedback-CV ist es dasselbe: Die Feedback-Menge multipliziert das Schleifensignal pro Sample, und die Grenze bei ±1 schnitt den CV hart ab.

**Messung [gemessen, Host]:** echter Patch-Code gegen `owl/test/Patch.h`, Fassung 3 aus `git show HEAD`. Eingang Sinus 5 kHz mit 3 V, Frequency 632 Hz, Resonance 12 Uhr, Tap zwischen Rastpunkt 3 und 4. Modulator Sinus 441 Hz. „Gefaltet“ = Linien, die nicht auf dem Raster 5000 + k · 441 Hz liegen, gegen alle Linien des Rasters, Blackman-Harris über 2 s. Beim Selbst-Patch Out 2 → In 4 (ein Block Verzögerung) zählen die Vielfachen von 1 kHz, die keine von 5 kHz sind, gegen die Oberwellen von 5 kHz.

| Fall | Fassung 3 | Fassung 4 | Schliere M |
|---|---|---|---|
| Tap-CV ±1 V | −51,0 dB | −116,2 dB | −69,9 dB |
| Tap-CV ±3 V | −34,1 dB | −81,9 dB | −64,5 dB |
| Feedback-CV ±3 V, Feedback 50 % | −69,0 dB | −124,6 dB | −122,7 dB |
| Out 2 → In 4, Feedback 30 %, 2 V | −47,0 dB | −86,8 dB | −63,8 dB |
| Out 2 → In 4, Feedback 30 %, 6 V | −19,0 dB | −69,8 dB | −48,8 dB |
| Out 2 → In 4, Feedback 70 %, 2 V | −38,0 dB | −70,2 dB | −69,3 dB |
| Out 2 → In 4, Feedback 70 %, 6 V | −20,7 dB | −59,8 dB | −41,3 dB |

Bei Tap-CV ±1 V liegt der Ton selbst bei −7 dB, die Seitenbänder bei −0,9 dB, in allen drei Fassungen. Bei Schliere M mit ±3 V liegt der Ton bei −27 dB (Phasenmodulation mit großem Index).

**Was Fassung 4 ändert [Code]:**
- Totzone an In 3 und In 4 mit weicher Kante: bis 0,45 V null, bis 0,65 V Übergang y³ − y⁴/2, danach linear mit 0,55 V Versatz.
- Rand der Haltezonen mit S-Kurve statt Knick.
- Die Gewichte der sieben Abgriffe laufen einzeln durch zwei Tiefpässe 1. Ordnung (je 3 kHz, trapezförmig mit Nullstelle bei fs/2). Geglättet wird nach der Abbildung, nicht der CV. Mit einfachen Tiefpässen (y += (x − y)·a, nur −14 dB je Pol bei fs/2) lag Tap-CV ±3 V erst bei −62,6 dB.
- Feedback-Menge: weiches Knie ab 90 % statt harter Grenze, danach zwei Tiefpässe mit je 1,5 kHz. Regler 4 erreicht damit 95 % statt 97 %, 97 % nur noch mit CV. Mit 3 kHz lag der Selbst-Patch bei 70 % und 6 V bei −50,6 dB, mit 800 Hz bei −70,0 dB.
- Die Rastpunkt-LEDs folgen nur noch Regler 3, nicht dem CV, mit Hysterese (an ±12 %, aus ±18 % des Abstands). Vorher schalteten sie bei Tap-Modulation im Blocktakt, und jeder Wechsel gibt einen Knack am Ausgang (D73). Das erledigt auch den offenen Punkt zum Flackern an den Haltezonen.

**Schliere M [Code]:** zweiter Patch in derselben Datei (`SchliereMPatch`). Tap ändert die Länge der Kette stufenlos: 1 + 8u Stufen links, 1 + 10u rechts (u = 0 … 6). Die angebrochene Stufe setzt von 0 Hz her ein, ihre Eckfrequenz ist so gewählt, dass sich die Phase bei Frequency linear mit dem Bruchteil ändert. Die Kette ist in jeder Stellung ein Allpass (Host-Test: 0,0004 dB Abweichung bei 27,4 Stufen). Ein langsamer Lauf über alle Stufen ändert den Pegel bei 1 kHz um weniger als 0,1 dB. Out 4 ist hier die Summe (L + R)/2 statt Tail. L und R brauchen getrennte Ketten, bis zu 49 + 61 Stufen.

**Host-Test:** `schliere_test.cpp` hat jetzt 45 Fälle (vorher 28), alle bestanden. Neu sind drei Fälle zur Faltung, zwei zu den LEDs bei Modulation und Zittern und zwölf für Schliere M.

**Builds:** `owl-patches/builds/Schliere/` (Fassung 4, 20 948 B, CRC `0xedf1ef5f`, `fe0beeba…`) und `owl-patches/builds/SchliereM/` (24 100 B, CRC `0x7261d05f`, `d5966d72…`). Fassung 3 (Slot 6) liegt als Kopie in `owl-patches/builds/Schliere-v3/`.

**Einschränkungen und offen:**
- Nichts davon ist am Gerät gemessen oder gehört. Rechenlast offen, bei Schliere M geschätzt 50–55 % statt 30 % [Hypothese].
- Der Selbst-Patch ist mit einem Block Verzögerung modelliert. Am Gerät kommen Wandler und Codec-Filter dazu, die Schleife verhält sich dort anders.
- Bei Schliere M faltet Tap-Modulation mit −64…−70 dB mehr als Fassung 4. Die Tiefpässe glätten die Tap-Stellung, aber die Abbildung Stellung → Koeffizient der Teilstufe liegt dahinter [Hypothese: Knicke der Gruppenlaufzeit an den ganzen Stufen abseits von Frequency]. Auch der Selbst-Patch faltet bei Schliere M mehr, Ursache nicht geklärt.
- Weil die Teilstufe von unten einsetzt, hebt ein steigender Tap die Tonhöhe kurz an, ein fallender senkt sie [Code].
- Ein Teil der Härte ist das Prinzip, nicht ein Fehler: Rückkopplung, die ihre eigene Stärke moduliert, ist Feedback-Amplitudenmodulation. Sie erzeugt schon ohne Faltung sägezahnartige, bei viel Verstärkung chaotische Spektren [Hypothese, nach der Literatur zu FBAM].

**Nachtrag (2026-11-19, 14:45–14:46): auf acdc1 geladen.** Freigabe des Nutzers. Vorher Sicherung mit `owl_read.py --out backup --dump` nach `backup/acdc1/20261119/owl/`: sechs Slots, alle `ok`, Slot 6 = Fassung 3 (17 860 B, `0x936d0028`), Fassung 3 lief mit 31 % CPU.
- Slot 6: `owl_write.py … --store 6 --yes --backup-file owl-patches/builds/Schliere-v3/Schliere.syx`. Gespeichert und zurückgemeldet als 'Schliere', 20 948 B, `0xedf1ef5f`. **33 % CPU** (`PROGRAM_STATS`, Regler 1–4: 91/33/100/1 von 127).
- Slot 7 (leer): `--store 7 --yes`, zurückgemeldet als 'SchliereM', 24 100 B, `0x7261d05f`. **49 % CPU** bei Tap 82 von 127 (etwa 32 + 40 Stufen). Mit Tap am Rechtsanschlag (127 von 127, 49 + 61 Stufen, Regler 1/2/4: 127/50/15) **54 % CPU** [gemessen], weniger als geschätzt (60–65 %).
- Danach läuft Slot 7 (Program Change nur im RAM). Der gemerkte Slot (`ACDC.slot`) ist unverändert.

**Zweiter Nachtrag (2026-11-19, 14:54): Fassung 3 zusätzlich auf Slot 8.** Der Nutzer findet Fassung 4 zu zahm und mochte die Glitches von Fassung 3. `owl_write.py owl-patches/builds/Schliere-v3/Schliere.syx --store 8 --yes` (Slot 8 war leer), zurückgemeldet als 'Schliere', 17 860 B, `0x936d0028`, 30 % CPU. Zwei Slots heißen damit 'Schliere': 6 = Fassung 4, 8 = Fassung 3.

**Was Fassung 4 zahm macht [gemessen, Host]:** Selbst-Patch Out 2 → In 4 wie oben, Eingang 5 kHz. „Obertöne“ = 10 + 15 + 20 kHz gegen 5 kHz, „gefaltet“ = Vielfache von 1 kHz, die keine von 5 kHz sind, gegen alle Linien von 5 kHz. Fassung 4 mit anderer Grenzfrequenz der Feedback-Glättung (je Pol), sonst unverändert (weiches Knie, LEDs):

| Fassung | 30 %, 2 V Obert. / gef. | 30 %, 6 V | 70 %, 2 V | 70 %, 6 V |
|---|---|---|---|---|
| 3 | −31,7 / −47,0 | −6,3 / −19,0 | −18,3 / −38,0 | −10,3 / −20,7 |
| 4 (1,5 kHz) | −58,1 / −86,8 | −44,4 / −69,8 | −46,3 / −70,2 | −38,0 / −59,8 |
| 4 mit 6 kHz | −39,5 / −71,8 | −19,9 / −41,2 | −27,7 / −57,1 | −16,7 / −34,8 |
| 4 mit 12 kHz | −34,3 / −56,2 | −10,8 / −32,2 | −21,9 / −49,5 | −11,4 / −29,7 |
| 4 ohne Glättung (23 kHz) | −31,2 / −44,2 | −14,3 / +1,7 | −18,4 / −40,4 | −10,6 / −20,1 |

- Die Glättung mit 1,5 kHz nimmt nicht nur die Faltung, sondern auch die neuen Obertöne: 28–38 dB weniger als Fassung 3. Das ist das „Zahme“.
- Mit 12 kHz kommen die Obertöne fast wieder auf Fassung 3 (innerhalb 1–5 dB), gefaltet wird 9–13 dB weniger. Ohne Glättung faltet es wie Fassung 3, mit 30 % und 6 V sogar mehr als Nutzsignal (der Lauf wird chaotisch).
- Die Obertöne aus der Feedback-Modulation sind also gewollt und lassen sich von der Faltung nur zum Teil trennen. Ganz trennen ließe sich das nur mit Oversampling des Produkts in der Schleife [Hypothese].

**Dritter Nachtrag (2026-11-19, 15:00): Zwischenstufe SchliereW auf Slot 9.** Wunsch des Nutzers nach dem Vorschlag oben. `SchliereWPatch` = SchlierePatch (Fassung 4) mit Feedback-Glättung 12 kHz je Pol statt 1,5 kHz, sonst gleich (weiches Knie, Tap-Glättung 3 kHz, LEDs nach Regler 3). Die Klasse steht in `owl/schliere/SchlierePatch.hpp` hinter `SCHLIERE_WILD_PATCH` und wird über `owl/schliere/SchliereWPatch.hpp` gebaut: Schon eine abgeleitete Klasse änderte das Binary von SchlierePatch (20 844 statt 20 948 B), so bleibt der Build von Slot 6 bytegleich mit der Quelle (`fe0beeba…` erneut gebaut). Host-Test: vier neue Fälle, ohne CV gleich SchlierePatch, Selbst-Patch 70 % / 6 V gefaltet −29,7 dB, beschränkt, klingt aus. Build `owl-patches/builds/SchliereW/`: 21 028 B, CRC `0x3d5a81ad`, `fee4cf81…`. Gespeichert auf Slot 9 (war leer), zurückgemeldet mit Größe und CRC. CPU 32–36 % (zwei `PROGRAM_STATS` im selben Report). Danach läuft Slot 9. Am Gerät nicht gehört.

**Vierter Nachtrag (2026-11-19, 15:07): SchliereO mit doppelter Abtastrate in der Schleife, Slot 10.** Wunsch des Nutzers: alle Fassungen nacheinander vergleichen. `owl/schliere/SchliereOPatch.hpp`: Überblendung wie Fassung 4, aber der Eingang der Kette läuft mit 96 kHz. Eingang (nach der Sperre), In 4 und Schleifensignal werden hochgerechnet, dort laufen Totzone, weiches Knie und beide Produkte, danach geht es zurück auf 48 kHz. Die Feedback-Menge wird nicht geglättet (wie Fassung 3, aber ohne harte Grenze).

- **Filter [gemessen, Host]:** Polyphasen-IIR-Halbband aus sechs Allpässen 1. Ordnung (elliptischer Entwurf nach Valenzuela/Constantinides, Übergang 0,045, Koeffizienten im Kopf der Datei). Entwurf numerisch geprüft: Durchlass bis 20 kHz ohne Welligkeit, Sperre ab 28 kHz −77 dB. Am C++-Code: Spiegelbilder ≤ −78 dB, Faltung beim Heruntertakten ≤ −82 dB. Verzögerung je Richtung ≈ 1,4 Samples bei 48 kHz (1 kHz), die Schleife wird um 2,8 Samples länger (Host-Test). Wegen der IIR-Form steigt die Verzögerung zu 20 kHz hin auf ≈ 4,5 Samples je Richtung.
- **Selbst-Patch Out 2 → In 4 [gemessen, Host]**, Obertöne / gefaltet wie im zweiten Nachtrag:

| Fassung | 30 %, 2 V | 30 %, 6 V | 70 %, 2 V | 70 %, 6 V |
|---|---|---|---|---|
| 3 (Slot 8) | −31,7 / −47,0 | −6,3 / −19,0 | −18,3 / −38,0 | −10,3 / −20,7 |
| 4 (Slot 6) | −58,1 / −86,8 | −44,4 / −69,8 | −46,3 / −70,2 | −38,0 / −59,8 |
| W (Slot 9) | −34,3 / −56,2 | −10,8 / −32,2 | −21,9 / −49,5 | −11,4 / −29,7 |
| O (Slot 10) | −21,0 / −56,8 | +4,3 / −33,4 | −13,8 / −53,0 | +1,4 / −35,1 |

  SchliereO erzeugt mehr neue Obertöne als Fassung 3 (bei 6 V lauter als der Grundton), gefaltet wird 10–15 dB weniger. Was noch als gefaltet zählt, ist bei 6 V zum Teil vermutlich kein Aliasing, sondern nicht periodischer Anteil der rückgekoppelten Schleife [Hypothese]. Das Maß trennt beides nicht.
- **Host-Test:** neun neue Fälle (Halbband, flacher Pegel und Verzögerung ohne Feedback, Selbst-Patch −34,4 dB, beschränkt, LEDs, klingt aus, Gleichspannung). `schliere_test.cpp` hat damit 58 Fälle (mit den vier für SchliereW), alle bestanden. Die Builds von Slot 6, 7 und 9 bauen weiter bytegleich (`fe0beeba…`, `d5966d72…`, `fee4cf81…`).
- **Build und Slot:** `owl-patches/builds/SchliereO/`: 21 868 B, CRC `0x9d98ea19`, `76c2da97…`. Auf Slot 10 gespeichert (war leer), zurückgemeldet mit Größe und CRC. **43 % CPU** (Fassung 4: 33 %). Danach läuft Slot 10. Am Gerät nicht gehört.

**Fünfter Nachtrag (2026-11-19, 15:12–15:13): Namen.** Zwei Slots hießen 'Schliere'. Auf Wunsch des Nutzers tragen alle Schliere-Slots jetzt einen Buchstaben: Slot 8 = **SchliereA** (Fassung 3, „alt“), Slot 6 = **SchliereZ** (Fassung 4, „zahm“), dazu SchliereM, SchliereW, SchliereO. Der Name steckt im Binary. SchliereA ist aus der Quelle von Fassung 3 gebaut (`git show HEAD:owl/SchlierePatch.hpp`, `AcdcInput.h` unverändert, lokal in `owl-patches/src-schliere-v3/`), SchliereZ aus der aktuellen Quelle. Gegen `Schliere-v3/` bzw. den Build von Fassung 4 unterscheiden sich beide nur in zwei Bytes, dem Buchstaben im Namen. Zwischendurch lag Fassung 4 kurz als 'Schliere4' auf Slot 6 (`owl-patches/builds/Schliere4/`), ersetzt nach dem Wunsch „Buchstaben statt Zahl“.
- Slot 6: 'SchliereZ', 20 948 B, CRC `0x36b5b8e0`, `owl-patches/builds/SchliereZ/`. Vorher gesichert: `backup/acdc1/20261119/owl_write_151205/`, `owl_write_151255/`.
- Slot 8: 'SchliereA', 17 860 B, CRC `0x80731b57`, `owl-patches/builds/SchliereA/`. Vorher gesichert: `backup/acdc1/20261119/owl_write_151305/`. 29 % CPU.
- Danach läuft Slot 8. `owl-patches/builds/Schliere/` (Fassung 4 unter altem Namen) und `Schliere4/` sind überholt.

**Sechster Nachtrag (2026-11-19, 15:14–15:40): Slots getauscht, Quellen in `owl/schliere/`.** Auf Wunsch des Nutzers, damit die Reihenfolge klar ist:
- **Slots 6 und 8 getauscht:** Slot 6 = SchliereA (Fassung 3), Slot 8 = SchliereZ (Fassung 4), je mit lokaler Kopie als Sicherung (`backup/acdc1/20261119/owl_write_151430/`, `owl_write_151439/`), zurückgemeldet mit Größe und CRC. Belegung jetzt: 6 A, 7 M, 8 Z, 9 W, 10 O. Ein im Boot-Menü gemerkter Slot 6 oder 8 startet jetzt die andere Fassung.
- **Quellen:** `owl/schliere/` mit `SchlierePatch.hpp` (Z), `SchliereAPatch.hpp` (Fassung 3, nur die Klasse umbenannt), `SchliereMPatch.hpp` (aus `SchlierePatch.hpp` herausgelöst), `SchliereWPatch.hpp`, `SchliereOPatch.hpp` und `README.md` (Varianten, Belegung, Messwerte, Bauen, deutsch und englisch in einer Datei). `AcdcInput.h` bleibt in `owl/`, die Mess-Patches `owl/test/SchliereLed*.hpp` auch (sie binden jetzt `../schliere/SchlierePatch.hpp` ein). `owl-patches/src-schliere-v3/` aus dem fünften Nachtrag ist gelöscht, die Quelle von A ist jetzt `SchliereAPatch.hpp`.
- **Bytegleich:** Alle fünf Varianten aus `owl/schliere/` gebaut und mit den Slot-Builds verglichen: A `16ee54fe…`, Z `3e20acb3…`, M `d5966d72…`, W `fee4cf81…`, O `76c2da97…`, alle gleich. Host-Test mit zwei Fällen für A (Rastpunkt 7 wie das Lehrbuch; Tap-CV ±3 V faltet mit −34,1 dB wie oben), insgesamt 60 Fälle bestanden.
- **SchliereM** sollte erst vom Modul, dann wollte der Nutzer doch alle Varianten behalten. Dafür hat `owl_write.py` jetzt `--erase SLOT --yes` (Wunsch des Nutzers, es zu behalten): nur ein Slot ab 2, nur mit einer lokalen Kopie, die in Größe und CRC zum Slot passt (wird zur Sicherung), Slotnummer immer mit 5 Bytes, danach müssen alle anderen Slots unverändert zurückkommen. Offline geprüft (Slot 1 und fehlendes `--yes` abgelehnt), am Gerät noch nie gesendet. Gefunden dabei [Code]: `MidiHandler::handleFlashEraseCommand` löscht ohne Slotnummer den ganzen Patch-Speicher, mit Slotnummer nur diesen Patch, die anderen Slots behalten ihre Nummern (`PatchRegistry` legt Patches nach ihrer Nummer ab).

**Siebter Nachtrag (2026-11-19, 15:45–16:05): SchliereS auf Slot 11.** Der Nutzer mag O fast am liebsten, wünscht bei Feedback-Modulation aber „ein ganz klein wenig weniger Glitch“. `owl/schliere/SchliereSPatch.hpp`: von `SchliereOPatch` abgeleitet, glättet den CV an In 4 mit zwei Tiefpässen 1. Ordnung (trapezförmig, je 12 kHz bei 48 kHz, zusammen ≈ 7,7 kHz), bevor O ihn verarbeitet.
- **Zuerst** sollte die Glättung nach der Kennlinie bei 96 kHz in O selbst sitzen (wie bei Z). Als Template gebaut, änderte das Binary von O (CRC `0x7756d25a` statt `0x9d98ea19`, gleiche Größe), deshalb verworfen. Eine Ableitung in eigener Datei lässt O bytegleich (erneut geprüft: `76c2da97…`).
- **Wahl der Grenzfrequenz [gemessen, Host]**, Selbst-Patch wie oben, Obertöne / gefaltet:

| Variante | 30 %, 2 V | 30 %, 6 V | 70 %, 2 V | 70 %, 6 V |
|---|---|---|---|---|
| O | −21,0 / −56,8 | +4,3 / −33,4 | −13,8 / −53,0 | +1,4 / −35,1 |
| In 4 mit 18 kHz je Pol | −21,4 / −57,0 | −2,6 / −36,8 | −15,2 / −53,4 | +3,8 / −31,5 |
| **In 4 mit 12 kHz je Pol (S)** | −22,0 / −58,4 | −5,3 / −42,9 | −17,0 / −57,3 | +2,6 / −35,5 |
| In 4 mit 8 kHz je Pol | −24,2 / −63,8 | −9,0 / −49,3 | −21,1 / −72,4 | −3,2 / −41,1 |
| Glättung der Feedback-Menge bei 96 kHz, 16 kHz je Pol (verworfen) | −22,1 / −61,3 | −4,8 / −42,9 | −18,0 / −57,4 | +0,5 / −34,9 |

  Bei 70 % und 6 V läuft die Schleife chaotisch, die Werte streuen um einige dB. 12 kHz nimmt 1–9 dB Faltung und wenig Obertöne weg, wie „ganz klein wenig“ gewünscht.
- **Host-Test:** vier neue Fälle (ohne CV an In 4 gleich O, Feedback-Modulation bei 3 kHz −0,5 dB gegen O, bei 15 kHz gedämpft, Selbst-Patch −35,7 dB, beschränkt). 65 Fälle in `schliere_test.cpp`, alle bestanden.
- **Build und Slot:** `owl-patches/builds/SchliereS/`: 18 156 B, CRC `0xd9b2a0f9`, `9be06b12…`. Auf Slot 11 gespeichert (war leer), zurückgemeldet mit Größe und CRC, **39 % CPU**. Danach läuft Slot 11. Im Boot-Menü ist 11 = LED 1, 2 und 4.
- Begriff: Im Deutschen heißt es „Oversampling“ (Nutzer), README und Messlog sind angepasst.

## D81 – SchliereL: Kette aus 160 Stufen (2026-11-21, am Rechner)

**Anlass (Nutzer, 2026-11-21):** Schliere soll mindestens so viele Stufen haben wie das Vorbild. Die alten Varianten bleiben, wie sie sind.

**Vorbild [belegt]:** Laut Handbuch des Vorbilds (v1.2.1, 2026-11-07) hat eine Sektion 2 bis 98 Pole, mit der Config-Datei bis 160 Pole (Abgriffe 0 bis 80 Stufen, 1 Stufe = 2 Pole). Im Normalbetrieb laufen beide Sektionen in Reihe, im Split-Modus jede Sektion zweimal. Höchstens sind es damit 196 Pole je Kanal, mit Config-Datei 320. Die Config-Datei gibt es ab Firmware v1.2.1. Schliere hatte bisher 61 Stufen (L bis 98, R und Tail bis 122 Pole).

**Umsetzung:** `owl/schliere/SchliereLPatch.hpp`, Klasse `SchliereLPatch`, auf Grundlage von S, der jüngsten Wunschfassung des Nutzers (D80, siebter Nachtrag): Eingang der Kette mit 96 kHz, Feedback-CV mit 2 × 12 kHz geglättet. Die Kette hat 160 Stufen (320 Pole). Abgriffe L: Stufen 1, 22, 43, 64, 85, 106, 127 (2 … 254 Pole, je 21), R: 1, 28, 54, 81, 107, 134, 160 (2 … 320 Pole, abwechselnd 27 und 26), L : R wie bisher etwa 4 : 5. Die Klasse ist eigenständig, mit eigener Konstante für die Länge. So bleiben O und S bytegleich, und alle Varianten laufen in einem Host-Test.

**Host-Test [gemessen, Host]:** neun neue Fälle in `owl/test/schliere_test.cpp`, insgesamt 78, alle bestanden:
- Rastpunkt 7 ohne Feedback flach (0,002 dB). Die Laufzeit entspricht 127 bzw. 160 Lehrbuch-Stufen plus 2,85 Samples (Halbbänder wie bei O).
- 1 kHz, Q 16: Laufzeit an L 1,297 s, an R und Tail 1,634 s (Rechnung 0,501 s × 127/49 bzw. × 160/49).
- Zwischen Rastpunkt 4 und 5: 21 Kerben an L, 26 an R (bisher 8 und 10).
- Rastpunkt 1: L = R. Mit 50 % Feedback ist L und R gleich S bis auf Rundung (< 1e-6).
- Out 2 → In 4, 70 % Feedback, 6 V: gefaltete Linien −35,3 dB (S: −35,5 dB in D80).
- Audio-Rate an allen CV-Eingängen, Q und Feedback am Anschlag: endlich, unter 9,8 V, LEDs nur 0 oder 1. Feedback am Anschlag klingt aus (−98,5 dB nach 12 s). DC läuft mit Faktor 1 durch.

**Build:** `owl-patches/builds/SchliereL/`: 22 948 B, CRC `0xb2496457`, `1213fdfe…`. Gegenprobe: SchliereS neu gebaut, bytegleich mit Slot 11 (`9be06b12…`).

**Einschränkungen:** Nicht gehört. Rechenlast vor dem Laden geschätzt aus D80 (≈ 0,43 % je Stufe, S 39 %): ≈ 82 %, gemessen 70 % (Nachtrag). Mehr Rechenlast hebt fs/8 und die Mischprodukte (D69). Das Rauschen der float-Kette bei 160 Stufen ist nicht gemessen.

**Nachtrag (2026-11-21, 12:11): auf Slot 12 geladen.** Freigabe des Nutzers. Vorher Sicherung mit `owl_read.py --out backup --dump` nach `backup/acdc1/20261121/owl/`: elf Slots, alle `ok`, Größen und CRC wie in D80, Slot 12 leer. `owl_write.py owl-patches/builds/SchliereL/SchliereL.syx --store 12 --yes`, zurückgemeldet als 'SchliereL', 22 948 B, `0xb2496457` (`out/owl_write/acdc1/20261121/owl_write_121126.json`). Danach läuft Slot 12 (Program Change, nicht gemerkt).
- **Rechenlast [gemessen]:** dreimal ausgelesen (`out/owl_read/20261121_schliereL_1…3/`), jedes Mal `CPU: 70% Memory: 2640`. Alle Regler am Linksanschlag (2, bei Regler 1 einmal 1 von 127). Die Kette wird immer ganz gerechnet, die Last hängt kaum von den Reglern ab [Hypothese]. Geschätzt waren ≈ 82 %. Je zusätzliche Stufe sind es damit ≈ 0,31 % (S 39 %, 99 Stufen mehr).
- Alle zwölf Slots melden Name, Größe und CRC wie vorher.
- Nicht gehört, die Ausgänge sind nicht gemessen. Bei 70 % Last sind höhere Blockraten-Linien und Mischprodukte zu erwarten als bei S (D69) [Hypothese].

## D82 – Plateau: erster Lauf am Gerät aus dem RAM (2026-11-23, 13:51)

**Anlass:** Plateau-Port (`owl/plateau/`, Valleys Plateau aus ValleyRackFree 2.4.5 in float) zum ersten Mal am Gerät, Freigabe des Nutzers. Nur RAM, kein Slot.

**Setup:** acdc1 mit fx7a, Einbau im Case. Vorher lief Slot 12 (SchliereL, per Program Change), alle Regler am Linksanschlag (CC 20–23: 2, 1, 2, 1). Ob Kabel stecken und ob ein Stream offen war, ist nicht notiert. Vorher `owl_read.py` (`out/owl_read/acdc1/20261123/`), dann `owl_write.py owl-patches/builds/Plateau/Plateau.syx --run` (33 828 B, CRC `0x9594a7be`, PLUSRAM, 164 Pakete in 2,4 s, `out/owl_write/acdc1/20261123/owl_write_135129.json`), 3 s später `owl_read.py` (`out/owl_read/acdc1/20261123_135150/`).

**Ergebnis [gemessen]:**
- Program Message `Plateau KiB 30 66 461 28`: ITCM 30, DTCM 66, AXI 461, SDRAM 28 KiB. Das ist genau die Belegung aus dem Host-Test und dem Plan im README. Nur der Pre-Delay liegt im SDRAM.
- `PROGRAM_STATS`: **CPU 51 %**, Memory 600 528 B (586 KiB, Puffer 584,7 KiB plus Verwaltung).
- Alle zwölf Slots unverändert (Liste vor dem Upload), Firmware `v22.4.r-fx7a`.

**Deutung:** Die Recherche schätzte 5–15 %. 51 % sind bei 480 MHz und 48 kHz etwa 5000 Takte pro Sample. Laut Disassembly rechnet der Patch pro Sample in der Größenordnung von 1000 Befehlen (`PlateauReverb::tank` 2,5 KB Code, `processAudio` 8 KB für einen Block, Funktionsaufrufe wie `expf`, `log10f`, `sqrtf` nur im Blocktakt). Das erklärt höchstens ein Drittel der Last [Hypothese]. Kandidaten:
- Das SDRAM bei 0xC0000000 liegt im Standard-Speicherplan des Cortex-M7 als Device-Speicher, ohne Cache und ohne Schreibpuffer. Die MPU-Region dafür ist in OpenWare auskommentiert (`Source/mpu.c`, `#if 0`) [Code]. Der Pre-Delay greift dreimal pro Sample darauf zu.
- Cache-Fehlgriffe im AXI-SRAM: 461 KiB Delay-Lines gegen 16 KiB D-Cache, etwa 40 Lese- und Schreibzeiger [Hypothese].
- `__aeabi_d2ulz` (64-Bit-Umwandlung der LFO-Frequenz in Software) viermal pro Block [Code], fällt kaum ins Gewicht [Hypothese].

**Einschränkungen:** Einmal gelesen, alle Regler am Linksanschlag (Mix trocken, Space klein, Decay kurz). Die Rechenlast des Kerns hängt kaum von den Reglern ab [Hypothese], gemessen ist das nicht. Nicht gehört, Ausgänge nicht gemessen. Nächster Schritt: Taktzähler (DWT) je Abschnitt im Patch messen und als Program Message melden, dann den Pre-Delay testweise ins AXI legen.

## D83 – Plateau mit Taktzählern: Die Caches der MCU sind aus (2026-11-23, 14:06–14:12)

**Anlass:** D82, 51 % CPU für Plateau, etwa fünfmal mehr als die Befehlszahl erwarten lässt. Freigabe des Nutzers für einen Mess-Build mit Taktzähler.

**Mess-Patch:** `owl/test/PlateauProfilePatch.hpp`, Klasse `PlateauProfilePatch`. Das ist Plateau unverändert, dazu Messpunkte `PLATEAU_PROBE(n)` in `PlateauPatch.hpp` und `PlateauCore.h`. Im normalen Build sind sie leer: Plateau neu gebaut ist bytegleich mit dem Stand aus D82 (`11c0e9d6…`). Die Messpunkte lesen den DWT-Zykluszähler, den die Firmware zu Beginn jedes Blocks auf 0 setzt [Code, `ProgramManager.cpp`]. Beim Start misst der Patch einmal Lesezugriffe mit 32 Byte Abstand (neue Cache-Zeile je Zugriff, zweiter Durchgang zählt) über den größten Plateau-Puffer je Speicherbereich und Schreibzugriffe ins SDRAM. Er meldet abwechselnd `PA` (Takte pro Sample je Abschnitt) und `PB` (Summe, langsamster Block, Kosten eines Messpunkts, Zugriffszeiten, Cache-Bits aus SCB->CCR). Host-Test `owl/test/plateau_profile_test.cpp`. Build `owl-patches/builds/PlateauProfile/` (29 644 B, CRC `0xc893c62b`, PLUSRAM). Im Mess-Build ist `tank` in `processAudio` eingebettet, in Plateau nicht.

**Ablauf:** zweimal `owl_write.py … --run` (14:06 ohne, 14:11 mit Cache-Bits), dazwischen und danach `owl_read.py` (`out/owl_read/20261123_plateauprofile_*`). Der Nutzer hatte die Regler inzwischen bewegt (CC 20–23 etwa 36, 120, 44, 8, später Regler 2 auf 2 und Regler 3 gedreht).

**Ergebnis [gemessen]:**

| Abschnitt | Takte pro Sample |
|---|---|
| c: Kontrollrate am Blockanfang (je Sample) | 856–885 |
| i: Eingänge (zwei Blockraten-Sperren, Normalisierung In 2, Clear-Hülle) | 594–596 |
| n: Kern-Eingang (DC-Sperren, Eingangsfilter, Pre-Delay, vier Allpässe) | 722–724 |
| t: Tank-Schleife | 1216–1232 |
| o: 14 Abgriffe des Tanks | 485–489 |
| s: Mix, Sättigung, Energie-Folger | 652–660 |
| p: Blockende (Clear, NaN-Prüfung, LEDs, je Sample) | 436–460 |
| **Summe** | **4990–5149** (langsamster Block 5422–10 754) |

- Firmware-Anzeige im Mess-Build 53–56 % (Plateau selbst 51 %, D82). 5000 Takte entsprechen 52 % von 10 000 Takten pro Sample.
- Ein Messpunkt kostet 5–6 Takte, etwa 30 pro Sample, unter 1 %.
- Leseschleife mit 32 Byte Abstand: ITCM 24–25, DTCM 24, AXI 26, SDRAM 46–47 Takte pro Zugriff. SDRAM schreiben 5 Takte (Schreibpuffer).
- **SCB->CCR meldet 0: I-Cache und D-Cache sind aus.**

**Deutung:**
- `ACDC/Core/Inc/hardware.h` setzt `USE_ICACHE` und `USE_DCACHE` nur `#ifdef NDEBUG`. `Hardware/owl3.mk` setzt im Release-Build nur `-O3`, nie `-DNDEBUG` [Code]. Das gilt für unseren Stand, für v22.5.0 und für den Upstream-`master`. Im fx7a-Binary fehlt der Code zum Einschalten der Caches, `MPU_Config` richtet nur die QSPI-Region ein [Code, Disassembly]. Am Gerät bestätigt (CCR = 0) [gemessen].
- Ohne I-Cache holt der Kern jeden Befehl über den Bus aus dem AXI-SRAM (Patch-Code mit plusram) bzw. dem DTCM (patchram). Die Leseschleife braucht deshalb in allen internen Speichern gleich viel, etwa 24 Takte statt einer Handvoll: Es bremst der Befehlsabruf, nicht der Datenzugriff [Hypothese, gestützt durch ITCM ≈ AXI]. Alle Abschnitte von Plateau sind gleichmäßig etwa fünfmal zu langsam. Das SDRAM kostet pro Lesezugriff etwa 22 Takte mehr, beim Pre-Delay also rund 50 Takte pro Sample, 1 % der Last.
- Das betrifft alle Patches auf beiden Modulen, nicht nur Plateau. Es passt zu den bisherigen Befunden: Die Lage des Codes im Flash verschob die Störlinien (D33), und erst der heiße Pfad im ITCM machte die Firmware davon unabhängig (D48). Mit Cache wäre der Busverkehr kleiner, was nach D42 auch fs/8 senken könnte [Hypothese].
- Ein Firmware-Build mit eingeschaltetem I-Cache ist der naheliegende nächste Schritt. Der D-Cache braucht dagegen mehr: die MPU-Region für die DMA-Puffer (`_DMA_DATA` fehlt im Linker-Skript des ACDC) und Kohärenz für SAI und USB. **Korrigiert in D87:** `_DMA_DATA` ist in `xibeca.ld` per `PROVIDE` definiert, USB nutzt keine DMA.

**Einschränkungen:** Wenige Lesungen, Regler nicht auf festen Stellungen, keine Aufnahme. Der langsamste Block schwankt stark (einmal 10 754 Takte pro Sample, Ursache offen, etwa MIDI-Verkehr durch `owl_read.py`). Ob die Abschnitte mit Cache gleichmäßig schneller werden, ist nicht gemessen. Danach lief `PlateauProfile` aus dem RAM weiter.

## D84 – Build 10 `v22.4.r-fx8a` (I-Cache an) auf acdc1: Flash, A1, Rechenlast, Patch-Wechsel (2026-11-23, 14:32–)

**Anlass:** D83, beide Caches aus. Build 10 = fx7a + Patch 19 (I-Cache an, D-Cache weiter aus, `docs/05`, „Build 10“). Freigabe des Nutzers zum Flashen.

**Vorher:** Sicherung mit `owl_read.py --out backup --dump` nach `backup/acdc1/20261123/owl/`: zwölf Slots, alle `ok`, Größen und CRC wie in D81.

**Flash [gemessen]:** `tools/flash_acdc.py acdc1-build10-fx8a --yes`, Log `firmware/flashlog/20261123_build10-fx8a/`. Vorher lief PlateauProfile aus dem RAM unter fx7a. 110 208 B geschrieben, Readback bytegleich, Rest 0xFF. Start per `:leave` (erstmals im Skript am Gerät), A1 bestanden: `v22.4.r-fx8a`, 48000 Hz, Blockgröße 8, Slots unverändert. Danach lief der gemerkte Slot 12 (SchliereL).

**Rechenlast Plateau [gemessen]:** `PlateauProfile` mit `--run`, Regler 40, 119, 22–23, 8 (wie in den letzten Lesungen von D83):

| | fx7a (D83) | fx8a |
|---|---|---|
| Cache-Bits (SCB->CCR) | 0 | **2 (I-Cache an)** |
| c Kontrollrate | 856–885 | 500 |
| i Eingänge | 594–596 | 385 |
| n Kern-Eingang | 722–724 | 506 |
| t Tank-Schleife | 1216–1232 | 926 |
| o 14 Abgriffe | 485–489 | 400 |
| s Mix, Sättigung, Energie | 652–660 | 511 |
| p Blockende | 436–460 | 301 |
| **Summe (Takte pro Sample)** | **4990–5149** | **3528–3555** |
| Firmware-Anzeige | 53–56 % | 38–39 % |
| Leseschleife ITCM / DTCM / AXI / SDRAM | 24 / 24 / 26 / 46 | **5 / 5–6 / 15 / 46** |

- Plateau selbst (ohne Messpunkte): **35 %** statt 51 % (D82). Speichermeldung unverändert `Plateau KiB 30 66 461 28`.
- Deutung: Ohne I-Cache bremste der Befehlsabruf alles gleich (die Leseschleife brauchte überall 24 Takte). Jetzt zeigt die Schleife die Datenzugriffe selbst: TCM 5–6 Takte, AXI ohne D-Cache 15, SDRAM 46 [gemessen]. Plateau liegt mit 461 KiB im AXI, der Rest von 3500 Takten hängt vermutlich an diesen Datenzugriffen und an Zustand und Stack im AXI [Hypothese]. Den Abschnitt s (wenige Dutzend Befehle, 511 Takte) erklärt das Rechnen allein nicht.

**Patch-Wechsel [gemessen]:** Program Change durch alle zwölf Slots, dann `--run` Plateau, Program Change 6, `--run` PlateauProfile, nach jedem Schritt `owl_read.py` (`out/owl_read/20261123_fx8a_switch_*`). Jeder Patch läuft und meldet sich, Plateau mit der Speichermeldung, PlateauProfile mit Cache-Bits 2 und denselben Takten wie vorher. Kein Hänger, kein Fehler. Der I-Cache wird beim Wechsel also invalidiert, wie im Code (`device_cache_invalidate`).

**Rechenlast der Slots unter fx8a [gemessen]**, alle mit Link patchram (DTCM), Regler 40, 119, 22–23, 8, in Klammern der letzte Wert unter fx7a oder älter, mit anderen Reglerstellungen:

| Slot | fx8a | vorher |
|---|---|---|
| 1 ACDC | 5 % | 5 % (D75) |
| 2 TapeDelay | 31 % | 32 % (D62, fx4b) |
| 3 Grainz | 76 % | – |
| 4 RingsReverb | 16 % | 16 % (D55) |
| 5 Tanh3 | 50 % | 48–49 % (D56) |
| 6 SchliereA | 29 % | 29 % (D69) |
| 7 SchliereM | 25 % | 49–54 % je nach Tap (D80) |
| 8 SchliereZ | 36 % | 33 % (D80) |
| 9 SchliereW | 35 % | 32–36 % (D80) |
| 10 SchliereO | 44 % | 43 % (D80) |
| 11 SchliereS | 45 % | 39 % (D80) |
| 12 SchliereL | 76–78 % | 70 % (D81, Regler links) |

- Wie erwartet: Patches im DTCM holen ihre Befehle am Cache vorbei, ihre Last ändert sich nicht messbar [Hypothese, Reglerstellungen nicht gleich]. Die Unterschiede bei M, S und L passen zur Abhängigkeit von den Reglern (M: Tap), eine Messung bei gleichen Stellungen fehlt. Schneller würden diese Patches erst mit Link plusram.

**Download-Stresstest [gemessen]:** `tools/dump_stress.py`, je 10 Runden über alle zwölf Slots, einmal bei laufendem Slot 5 (Tanh3, 50 %), einmal bei Slot 2 (TapeDelay), danach Program Change auf 12. **240 von 240 Downloads in Ordnung**, kein Hänger (`out/D84-fx8a-slot5-session-table.md`, `out/D84-fx8a-slot2-session-table.md`). Kein Kabel bekannt, ob ein Stream offen war, ist nicht notiert.

**Einschränkungen und offen:** Rauschen gegen fx7a (Kontrolle am Anfang und Ende) und Loop-Test fehlen noch, beide brauchen den Nutzer am Gerät (Kabel, Reglerstellung 12 Uhr). Erst danach ist die Abnahme vollständig und über die Alltags-Firmware zu entscheiden. Danach läuft Slot 12 per Program Change. **Rückweg ist fx7a.**

## D85 – Build-10-Sitzung: Rauschen fx8a gegen fx7a, Loop-Test (2026-11-23, ab etwa 14:45)

**Setup:** acdc1 im Case, Alltags-Kette, Eingänge offen, keine Kabel, Oszillator im Case abgesteckt (Nutzer), Regler etwa 12 Uhr (CC 69/55–56/72/56 von 127), Slot 1 ACDC (vor dem Stream per Program Change gewählt), LED-Modus wie gemerkt, je 2 × 60 s `acdc_rec.py --reps 2 --owl-read`. Vor der ersten Aufnahme lief wieder der gemerkte Slot 12, acdc1 war also neu gestartet worden, vermutlich beim Umstecken (Kaltstart). Reihenfolge: `B10-fx8a-a` → Flash fx7a (`firmware/flashlog/20261123_build9-fx7a-ab10/`, Readback bytegleich, `:leave`, A1) → `B10-fx7a` → Flash fx8a (`firmware/flashlog/20261123_build10-fx8a-b/`, ebenso) → `B10-fx8a-b`. Diesmal ist der Testkandidat an beiden Enden, die Kontrolle fx7a in der Mitte.

**Nebenbei [gemessen]:** Slot 12 (SchliereL, patchram) direkt nach den Flashes bei gleichen Reglern: fx7a 70 %, fx8a 71 %. Patches im DTCM werden durch den I-Cache nicht schneller, wie erwartet (D84).

### Rauschen

Tabelle `out/B10-session-table.md` (`family_table.py`, Datei-dBFS, Mittel über 4 Kanäle, Δ gegen fx7a). Alle sechs Läufe ohne Stream-Fehler (am Ende nur `tx ovf … 32` vom Stream-Start), CPU 6–8 %.

| | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| `B10-fx8a-a-r1` | −72,85 (−0,21) | −78,32 (+0,44) | −75,10 (−0,62) | −82,37 (**+0,58**) | −114,54 (+1,44) |
| `B10-fx8a-a-r2` | −72,89 (−0,24) | −78,60 (+0,16) | −75,02 (−0,54) | −82,40 (**+0,55**) | −112,55 (+3,42) |
| `B10-fx7a-r1` | −72,74 (−0,10) | −78,74 (+0,02) | −74,64 (−0,16) | −82,97 (−0,02) | −115,70 (+0,27) |
| `B10-fx7a-r2` | −72,55 (+0,10) | −78,78 (−0,02) | −74,33 (+0,15) | −82,93 (+0,02) | −116,26 (−0,29) |
| `B10-fx8a-b-r1` | −72,62 (+0,03) | −78,83 (−0,07) | −74,51 (−0,03) | −82,32 (**+0,63**) | −114,97 (+1,00) |
| `B10-fx8a-b-r2` | −72,51 (+0,13) | −78,75 (+0,01) | −74,37 (+0,11) | −82,35 (**+0,59**) | −112,72 (+3,26) |

Weitere Linien: Die Analyse findet keine neue Linie. Der bekannte Kamm bei k · 500 Hz um −100 dB (auch in B9, gleicher Pegel) liegt unter fx8a 0,3–0,5 dB höher als unter fx7a, ebenso die Vielfachen bis 7,5 kHz.

**Deutung:**
- **[gemessen] fx8a hebt fs/8 um 0,6 dB.** Alle vier fx8a-Läufe liegen +0,55 bis +0,63 dB über fx7a, die beiden fx7a-Läufe stimmen auf 0,04 dB überein. Weil fx8a vor und nach der Kontrolle gleich liegt, ist das keine Drift.
- **Mischprodukte +1,0 bis +3,4 dB** in allen vier fx8a-Läufen. Sie streuen von Lauf zu Lauf um mehrere dB (D79), die Richtung ist aber in allen Läufen gleich. [Hypothese] Eine kleine Zunahme, passend zu fs/8.
- **RMS, Rest und Kamm unverändert** innerhalb der Streuung (Kamm am Anfang −0,6 dB, am Ende ±0,1 dB: Drift wie in D79).
- Die Hypothese aus D83 (mit Cache weniger Busverkehr, also weniger fs/8) trifft nicht zu. [Hypothese] Mit I-Cache erledigt die CPU die Arbeit jedes Blocks in kürzerer Zeit, der Strompuls im Blocktakt wird kürzer und höher. Das wäre derselbe Mechanismus wie in D42 und D69 (mehr Arbeit oder Busverkehr im Blocktakt hebt fs/8), nur über die Form statt die Menge.
- Größenordnung: +0,6 dB bei fs/8 ist kleiner als das, was ein FX-Patch mit 29 % Last bringt (+3,8 dB, D69). Plateau spart unter fx8a 16 Prozentpunkte Last.
- Der Rest liegt in dieser Sitzung rund 3 dB tiefer als in D79 (−78,8 gegen −75,6 dBFS), bei derselben Firmware fx7a. Ursache offen (Umgebung, anderer Tag).

### Loop-Test

Kabel Out 1–4 → In 1–4 (Nutzer), Regler etwa 12 Uhr, Slot 1, `acdc_rec.py --sine 440 530 670 790 --duration 60 --owl-read`, Aufnahme `B10-fx8a-loop` (`20261123_acdc1_fx8a-loop_g12_usb-stream.wav`). Stream-Meldungen 0, Geräte-Meldung am Ende `tx ovf 1.0000 1.0000 32` (Stream-Start), CPU 7 %.

- `phase_slips.py`: Pegel −6,0…−6,1 dBFS, Streuung 0,00 dB, 0 Ereignisse auf allen vier Kanälen.
- `stale_samples.py`: 0 von 96 000 Samples falsch auf allen vier Kanälen.
- Ergebnisse in `out/B10-fx8a-loop/`.

**[gemessen] Loop-Test bestanden.** Die Abnahme von Build 10 ist damit vollständig (D84, D85): Flash, A1, Cache-Bits 2, Patch-Wechsel, Downloads 240/240, Loop-Test. Beim Rauschen fs/8 +0,6 dB, sonst gleich. Über die Alltags-Firmware entscheidet der Nutzer.

Danach: Kabel stecken noch, fx8a, Slot 1 läuft.

**Entscheidung (Nutzer, 2026-11-23):** fx8a ist die Alltags-Firmware auf acdc1. Rückweg fx7a, dann fx6a.

## D86 – Original-Sitzung: Werks-Firmware gegen fx8a, offene Eingänge (2026-11-23, abends)

**Anlass:** Für die Rauschtabelle der READMEs fehlte ein Vergleich mit der Original-Firmware in derselben Sitzung. Bisher gab es nur S2-4 (2026-11-13, früherer Aufnahmeweg, TB-Hub direkt, neben dem Case). Freigabe der beiden Flashes durch den Nutzer im Chat.

**Setup:** acdc1 im Case, Alltags-Kette, Eingänge offen, keine Kabel, Regler 69/56/72/56 von 127 in allen sechs Geräte-Reports (nicht bewegt), Slot 1 ACDC vor jedem Stream per Program Change, je 2 × 60 s `acdc_rec.py --reps 2 --owl-read --analyze`. Reihenfolge:
1. `ORG-fx8a-a` (fx8a, Stand nach D85)
2. Flash Werks-Firmware: Readback `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` (`433b3fd3…`, D3, D5) mit `flash_acdc.py`, Log `firmware/flashlog/20261123_original-orga/`. Readback bytegleich, `:leave`, A1 bestanden („AC/DC v22.5.0“, 48000 / 8, alle zwölf Slots unverändert). Die Werks-Firmware liest die Slots und Ressourcen der eigenen Builds ohne Probleme. Erstmals mit `:leave` gestartet statt Kaltstart.
3. `ORG-orig` (Werks-Firmware, Audiogerät „OWL-ACDC“, CPU 13 % statt 6 % bei Slot 1)
4. Flash fx8a zurück, Log `firmware/flashlog/20261123_build10-fx8a-nach-original/`. Readback bytegleich, `:leave`, A1 bestanden. Gestartet ist der gemerkte Slot 12, danach Program Change auf Slot 1.
5. `ORG-fx8a-b`

Alle sechs Aufnahmen ohne Stream-Meldungen und ohne Klicks.

**Gain-Korrektur:** Die Werks-Firmware nimmt nach dem VCA des Default-Patches auf, fx8a roh (`TX_PRE_FX`). Den Gain je Kanal misst das DC-Verhältnis der offenen Eingänge gegen das Mittel der vier fx8a-Läufe (Verfahren aus D26, dafür neu `family_table.py --dc-ref/--dc-correct`, gegen D26 nachgerechnet auf ≤ 0,05 dB gleich): **+0,85 / −2,73 / +1,63 / −2,64 dB** (Kanal 1–4), in r1 und r2 auf 0,01 dB gleich. Aus den CC-Werten vorhergesagt wären (2·CC/127)² = +1,44 / −2,18 / +2,18 / −2,18 dB, also je Kanal 0,5–0,6 dB mehr. [Hypothese] Die 7-Bit-CC-Werte bilden die Regler-Parameter nicht genau ab (wie die kleineren Abweichungen in D26). Der DC von fx8a driftet zwischen Anfang und Ende um 0,1 dB.

### Rauschen

Tabelle `out/ORG-session-table.md` (Datei-dBFS, Mittel über 4 Kanäle, Δ gegen das Mittel der vier fx8a-Läufe, Original gain-korrigiert):

| | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| `ORG-fx8a-a-r1` | −72,75 (+0,02) | −79,14 (−0,30) | −74,63 (+0,13) | −82,27 (+0,02) | −112,82 (+0,27) |
| `ORG-fx8a-a-r2` | −72,72 (+0,05) | −78,99 (−0,15) | −74,64 (+0,12) | −82,17 (+0,12) | −114,23 (−1,15) |
| `ORG-orig-r1` | −70,99 (**+1,78**) | −75,64 (**+3,20**) | −75,00 (−0,24) | −77,12 (**+5,17**) | −90,45 (**+22,64**) |
| `ORG-orig-r2` | −70,97 (**+1,80**) | −75,60 (**+3,24**) | −74,98 (−0,22) | −77,11 (**+5,18**) | −90,44 (**+22,65**) |
| `ORG-fx8a-b-r1` | −72,71 (+0,06) | −78,63 (+0,21) | −74,73 (+0,03) | −82,34 (−0,05) | −113,21 (−0,12) |
| `ORG-fx8a-b-r2` | −72,91 (−0,14) | −78,62 (+0,22) | −75,04 (−0,29) | −82,38 (−0,09) | −112,31 (+0,77) |

Ohne Gain-Korrektur liegt das Original bei RMS +1,28, Rest +2,58, Kamm −0,79, fs/8 +4,89, Mischprodukte +22,37 dB.

In Geräte-dBFS (−6,02 dB), wie in den READMEs: Original gegen fx8a RMS −77,0 / −78,8, Rest −81,6 / −84,9, Kamm −81,0 / −80,8, fs/8 −83,1 / −88,3, Mischprodukte −96,5 / −119,1.

**Weitere Linien:**
- **LED-PWM nur beim Original:** 2320,545 Hz mit 10 Harmonischen auf allen Kanälen, −110…−115 dB (Datei-dBFS, unkorrigiert). Unter fx8a nicht gefunden (die LED-PWM läuft seit fx7a mit 48 kHz, D78).
- **Neu beim Original:** eine Familie bei 75,72 Hz (k = 1 bei −91…−98 dB, Summe −94…−101 dB) auf allen Kanälen, unter fx8a nicht vorhanden. Quelle offen.
- Der Rest steigt beim Original gleichmäßig über das ganze Band (Median-PSD je Band, gain-korrigiert): 100 Hz–20 kHz +2,8…+3,5 dB auf Kanal 1, 2, 4, auf Kanal 3 von +3,3 dB (unter 1 kHz) auf +2,1 dB (über 15 kHz) fallend, 20–100 Hz +4…+5 dB.

**Deutung:**
- **[gemessen] fx8a ist gegen die Original-Firmware leiser:** RMS −1,8 dB, Breitbandrauschen ohne Linien −3,2 dB, fs/8 −5,2 dB, Mischprodukte −22,6 dB. Die LED-PWM-Linie und die 75,72-Hz-Familie fehlen. Der SOF-Kamm ist gleich (+0,2 dB). Beide Enden der Kontrolle liegen auf ≤ 0,3 dB zusammen (Rest, Kamm), also keine Drift von Bedeutung.
- Die Richtung passt zur Kette der Vergleiche in einzelnen Sitzungen: Original ≈ 1b (D19), 1b → 1d Kamm −1,7, fs/8 −1,5, Mischprodukte +4,8 dB (D24), Build 2 ≈ 1d (D26), 3d ≈ Build 2 (D34), 3d → fx3l fs/8 −5,1, Mischprodukte −35, Rest −1,25 dB (D48), danach bis fx8a gleich bis auf fs/8 +0,6 dB (D85).
- Der Rest ist um 3,2 dB besser, mehr als die Kette erwarten lässt (etwa 2,5 dB). [Hypothese] Ein breitbandiger Anteil der Werks-Firmware, etwa aus der CPU-Last ohne ITCM (13 % statt 6 % bei Slot 1) oder aus den Pegel-LEDs, die beim Original dem Signal nach dem Patch folgen (D73, D74). Nicht weiter untersucht.
- Einschränkung: Das Original ist über den DC-Offset korrigiert. Ein Fehler darin verschiebt alle Größen des Originals um denselben Betrag. Der Kamm (gleich bei beiden) spricht dafür, dass die Korrektur stimmt.

**Danach:** fx8a, Slot 1 per Program Change, gemerkt bleibt Slot 12, keine Kabel.

## D87 – D-Cache vorbereiten: DMA-Puffer, MPU-Region, Korrektur zu `_DMA_DATA` (2026-11-23, am Rechner)

**Anlass:** Planung von Build 11 (D-Cache an). Nur lesend, Quellbaum von fx8a (`firmware/_work/acdc1-build10-fx8a/`) und ELF von Build 10.

**Befunde [Code]:**
- **Korrektur zu D83, Build 10 und Patch 19:** `_DMA_DATA` fehlt nicht. Das ACDC linkt mit `Hardware/xibeca.ld` (`ACDC/Makefile` bindet `Hardware/xibeca.mk` ein), dort steht `.dmadata (NOLOAD) : { PROVIDE (_DMA_DATA = .); *(.dmadata) } >DMA_D2` mit `DMA_D2` bei 0x30000000, 64 KB. Im ELF von fx7a fehlte das Symbol nur, weil `PROVIDE` es erst anlegt, wenn es benutzt wird. Ob `USE_ICACHE` allein einen Link-Fehler gegeben hätte, ist damit hinfällig: eher nicht. Am Inhalt von Build 10 ändert das nichts, die Bindung der Region an `USE_DCACHE` ist trotzdem richtig.
- **Nur drei Puffer werden per DMA beschrieben oder gelesen** (alle DMA1): `codec_txbuf` 0x30000000 (SAI1 B), `codec_rxbuf` 0x30002000 (SAI1 A), je 0x2000 B, und `adc_values` 0x30004000 (ADC1, 8 B). Alle liegen über das Makro `DMA_RAM` (`hardware.h`) in `.dmadata`, also im Fenster der Region. Dazu in `.dmadata`, aber nur von der CPU benutzt: `midi_rx_buffer`. MDMA und BDMA laufen nicht, SPI3 hat einen DMA-Kanal, wird aber nie per DMA gestartet.
- **Ohne DMA:** USB (OTG FS, `dma_enable = DISABLE`, alle Puffer im DTCM), QSPI (indirekt, CPU-Polling, auch beim Laden und Speichern von Patches), SPI zum Codec, UART.
- **Patches arbeiten direkt in den SAI-Puffern:** `pv->audio_input` und `pv->audio_output` zeigen in `codec_rxbuf`/`codec_txbuf`, das SDK wandelt int↔float in eigene Puffer. Die Firmware liest und schreibt dieselben Puffer (USB-Umwandlung, Pegel, LEDs).
- **Fehler im Code hinter `USE_DCACHE`, bisher nie gebaut:**
  - Die DMA-Region in `Source/mpu.c` setzt TEX=1, C=0, **B=1**. Diese Kodierung ist in ARMv7-M reserviert. Normal ohne Cache ist TEX=1, C=0, B=0, wie der Kommentar dort sagt.
  - `main()` schaltet den D-Cache vor `MPU_Config()` ein.
  - `device_cache_invalidate()` invalidiert erst den I-Cache, dann schreibt es den D-Cache zurück. Für Patch-Code im AXI ist die umgekehrte Reihenfolge richtig.
  - Die auskommentierte SDRAM-Region ist 8 MB statt 32 MB groß und shareable (auf dem M7 praktisch ohne Cache).
- Firmware-Daten liegen fast alle im DTCM (nie gecacht). Cachebar würden mit D-Cache: AXI (Patch-Code und -Heap bei plusram), D2 außerhalb von `.dmadata` (Tabellen, SysEx-Puffer), D3. Das SDRAM bleibt ohne eigene Region Device.

**Folge:** Planung von Build 11 in einer Fragerunde mit dem Nutzer (siehe `docs/05`, „Build 11“, sobald abgestimmt). Die falsche Aussage ist in `docs/05` (de/en), D83, `CLAUDE.md`, `TODO.md` und im Fork-README korrigiert, Patch 19 bleibt unverändert (Prüfsumme in `BUILD_INFO.txt`).


## D88 – Build 11 `v22.4.r-fx9a` (D-Cache an) auf acdc1: Flash, A1, Kaltstart, kurzer Loop-Test (2026-11-23, ab etwa 16:25)

**Anlass:** Build 11 nach Plan (`docs/05`, „Build 11“, Punkt 10), Flash mit Freigabe des Nutzers (2026-11-23). Vorher lief fx8a mit Slot 12 (SchliereL), keine Kabel. acdc1 im Case, Alltags-Kette.

**Flash [gemessen]:** `tools/flash_acdc.py acdc1-build11-fx9a --yes`, Log `firmware/flashlog/20261123_build11-fx9a/`. 110 520 B geschrieben, Readback bytegleich, Rest 0xFF. Start per `:leave`, A1 bestanden: `v22.4.r-fx9a`, 48000 Hz, Blockgröße 8, Slots unverändert. Danach lief der gemerkte Slot 12 (SchliereL, CPU 71 %, wie unter fx8a: Link patchram, im DTCM ohne Cache).

**Kaltstart von Hand (Nutzer: Case aus, USB ab, Case an, USB an) [gemessen]:** `flash_acdc.py --a1` bestanden (Report `owl_read_after/acdc1/20261123_163202/`), wieder Slot 12 mit 72 % CPU. Die Firmware startet also auch aus dem Kaltstart mit D-Cache. Danach `owl_read.py --program 1` (Slot 1 ACDC), erst dann die Kabel.

**Kurzer Loop-Test [gemessen]:** Kabel Out 1–4 → In 1–4 (Nutzer), Gain und Regler 12 Uhr, Slot 1, `acdc_rec.py --sine 440 530 670 790 --duration 60 --owl-read`, Aufnahme `B11-fx9a-loop-cold` (`20261123_acdc1_fx9a-loop-cold_g12_usb-stream.wav`). Stream-Meldungen 0, Geräte-Meldung am Ende `tx ovf 1.0000 1.0000 32.0000` (Stream-Start), CPU 7 %.
- `phase_slips.py`: Pegel −6,0…−6,1 dBFS, Streuung 0,00 dB, 0 Ereignisse auf allen vier Kanälen.
- `stale_samples.py`: 0 von 96 000 Samples falsch auf allen vier Kanälen.

**Fazit:** Punkt 10 des Plans bestanden. Die DMA-Puffer bleiben mit D-Cache kohärent, soweit 60 s Loop das zeigen. Offen ist die Abnahme nach Punkt 11 (Loop-Test 10 min, Patch-Wechsel, Downloads 240/240, Plateau-Store auf Slot 13, PlateauProfile, Rausch-Sandwich gegen fx8a). Cache-Bits und Takte sind noch nicht gemessen. Rückweg fx8a.

## D89 – Build 11 `v22.4.r-fx9a`: Abnahme (Loop 10 min, Rechenlast, Patch-Wechsel, Downloads, Rauschen) und neue Slot-Belegung (2026-11-23, ab etwa 16:40)

**Setup:** acdc1 im Case, Alltags-Kette, fx9a seit D88. Regler auf 12 Uhr (CC 68–69/55–56/72/56 von 127), bei den fx8a-Werten aus D84 standen sie auf 40/119/22/8. Abnahme nach `docs/05`, „Build 11“, Punkt 11, Freigabe des Nutzers.

**Loop-Test 10 min [gemessen]:** Kabel Out 1–4 → In 1–4, Slot 1, `acdc_rec.py --sine 440 530 670 790 --duration 600 --owl-read`, Aufnahme `B11-fx9a-loop10` (`20261123_acdc1_fx9a-loop10_g12_usb-stream.wav`). Stream-Meldungen 0, CPU 7 %.
- `phase_slips.py`: −6,0…−6,1 dBFS, Streuung 0,00 dB, 0 Ereignisse auf allen vier Kanälen.
- `stale_samples.py`: 0 von 28 656 000 Samples falsch auf allen vier Kanälen.
- Geräte-Meldung am Ende `tx ovf 0.3888 1.0000 32.0000`. Dieselbe Form kommt beim Öffnen oder Schließen eines Streams vor (D25, D75). In den 600 s gibt es weder Slip noch veraltetes Sample, das Ereignis lag also in den 3 s Einschwingzeit.

**Rechenlast [gemessen]:** Kabel ab, `owl_write.py … --run`, danach je `owl_read.py` (`out/owl_read/20261123_fx9a_plateauprofile_*`, `…_plateau_*`).

| | fx8a (D84) | fx9a |
|---|---|---|
| Cache-Bits (SCB->CCR) | 2 | **3 (I- und D-Cache an)** |
| c Kontrollrate | 500 | 403 |
| i Eingänge | 385 | 369 |
| n Kern-Eingang | 506 | 468 |
| t Tank-Schleife | 926 | 665 |
| o 14 Abgriffe | 400 | 236 |
| s Mix, Sättigung, Energie | 511 | 295 |
| p Blockende | 301 | 207 |
| **Summe (Takte pro Sample)** | **3528–3555** | **2635–2651** |
| Firmware-Anzeige PlateauProfile | 38–39 % | 29–30 % |
| Leseschleife ITCM / DTCM / AXI / SDRAM | 5 / 5–6 / 15 / 46 | 5–6 / 5 / 14–15 / 46–47 |
| **Plateau selbst** | **35 %** | **29 %** |

- Plateau braucht 25 % weniger Takte. Am meisten gewinnen die Abschnitte mit vielen Zugriffen auf Zustand und kurze Puffer: Abgriffe −41 %, Mix −42 %, Tank −28 %. Die Speichermeldung ist unverändert (`Plateau KiB 30 66 461 28`).
- **Die Leseschleife bleibt bei 15 Takten für das AXI, das ist kein Gegenbeweis [Code].** Sie liest mit einer neuen Cache-Zeile je Zugriff über den größten Plateau-Puffer im Bereich (`latencyTest()` in `owl/test/PlateauProfilePatch.hpp`), der weit größer ist als die 16 KB D-Cache. Beide Durchgänge treffen deshalb nie den Cache, sie messen die Zeit eines Fehlzugriffs. Das Ziel „Leseschleife AXI gegen 5 Takte“ aus dem Plan war eine falsche Erwartung. Maßgeblich ist die Zeit von Plateau.
- Einschränkung: Reglerstellungen anders als in D84. Unter fx7a lagen Messungen mit verschiedenen Reglern innerhalb von 3 % (D83).

**Patch-Wechsel [gemessen]:** zwei Runden mit Program Change durch alle zwölf Slots, dann `--run` Plateau, Program Change 6, `--run` PlateauProfile, nach jedem Schritt `owl_read.py` (`out/owl_read/20261123_fx9a_switch_r*`). Jeder Patch läuft und meldet sich, PlateauProfile beide Male mit Cache-Bits 3 und 2650–2651 Takten. Kein Hänger, kein Fehler. Last der Slots bei Reglern 12 Uhr (patchram, DTCM): ACDC 5 %, TapeDelay 31 %, Grainz 13 %, RingsReverb 15 %, Tanh3 50 %, SchliereA 29–30 %, M 37 %, Z 32 %, W 32 %, O 37–39 %, S 39 %, L 70–71 %. TapeDelay, RingsReverb, Tanh3, SchliereA, S und L liegen wie unter fx8a (D84). Grainz (D84: 76 %) und SchliereM (25 %) hängen stark von den Reglern ab [Hypothese].

**Download-Stresstest [gemessen]:** `tools/dump_stress.py`, je 10 Runden über alle zwölf Slots bei laufendem Slot 5 (Tanh3) und Slot 2 (TapeDelay), danach Slot 1. **240 von 240 in Ordnung**, kein Hänger (`out/D89-fx9a-slot5-session-table.md`, `out/D89-fx9a-slot2-session-table.md`).

**Neue Slot-Belegung (Wunsch des Nutzers, 2026-11-23) [gemessen]:** Schliere A, M, Z, W und O entfernt, Plateau hinter RingsReverb, der Rest rückt nach. Statt des Store-Tests auf Slot 13 aus dem Plan.
- Vorher Sicherung aller Slots mit `owl_read.py --out backup --dump` nach `backup/acdc1/20261123/owl_171118/`, alle zwölf `ok`.
- `owl_write.py --store N --yes --backup-file <Kopie des alten Slots> --download-check`: Slot 5 Plateau (33 828 B, CRC `0x9594a7be`, aus `owl-patches/builds/Plateau/`), 6 Tanh3, 7 SchliereS, 8 SchliereL (jeweils die Bytes aus der Sicherung). Alle vier beim Rückladen bytegleich.
- `owl_write.py --erase N --yes` für die Slots 9–12, **erstmals am Gerät** (D80). Jedes Mal ist der Slot danach weg und die anderen Slots unverändert, keine Fehlermeldung. Danach Program Change auf 1.
- Neue Belegung: **1 ACDC, 2 TapeDelay, 3 Grainz, 4 RingsReverb, 5 Plateau, 6 Tanh3, 7 SchliereS, 8 SchliereL**, Slots 9–12 leer. Kontrolle mit `owl_read.py --out backup --dump` (`backup/acdc1/20261123/owl_171330/`), alle acht `ok`, CRC wie oben. Program Change 5–8: Plateau 29 %, Tanh3 51 %, SchliereS 39 %, SchliereL 70 %.
- Die Kopien der alten Slots stehen in `backup/acdc1/20261123/owl_write_*/` und `owl_171118/`, die Builds in `owl-patches/builds/`.
- **Gemerkt ist weiter Slot 12, der jetzt leer ist.** Beim Einschalten startet dann Slot 1 [Code, Patch 15b: `acdcBootSelect()` fällt auf `DEFAULT_PROGRAM` zurück]. Einen anderen Slot merkt das Boot-Menü. Wird später wieder etwas auf Slot 12 gespeichert, startet das beim Einschalten.

**Rauschen fx9a gegen fx8a [gemessen]:** acdc1 im Case, Eingänge offen, keine Kabel, Regler 69/56/72/56 von 127, Slot 1 vor jedem Stream per Program Change, je 2 × 60 s `acdc_rec.py --reps 2 --owl-read`. Zustand des Oszillators im Case nicht erfragt, in der Sitzung niemand am Case. Reihenfolge: `B11-fx9a-a` (17:15) → Flash fx8a (`firmware/flashlog/20261123_build10-fx8a-sandwich11/`, Readback bytegleich, `:leave`, A1) → `B11-fx8a` → Flash fx9a (`firmware/flashlog/20261123_build11-fx9a-sandwich/`, ebenso) → `B11-fx9a-b` (bis 17:23). Alle sechs Läufe ohne Stream-Fehler. Tabelle `out/B11-session-table.md` (`family_table.py`, Datei-dBFS, Mittel über 4 Kanäle, Δ gegen fx8a):

| | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| `B11-fx9a-a-r1` | −73,14 (−0,33) | −79,27 (−0,61) | −75,02 (−0,15) | −82,97 (**−0,65**) | −110,01 (+1,89) |
| `B11-fx9a-a-r2` | −73,18 (−0,38) | −79,22 (−0,56) | −75,09 (−0,21) | −83,18 (**−0,85**) | −114,00 (−2,11) |
| `B11-fx8a-r1` | −72,88 (−0,07) | −78,62 (+0,03) | −75,01 (−0,14) | −82,29 (+0,03) | −112,69 (−0,80) |
| `B11-fx8a-r2` | −72,73 (+0,07) | −78,69 (−0,03) | −74,74 (+0,14) | −82,35 (−0,03) | −111,22 (+0,68) |
| `B11-fx9a-b-r1` | −73,02 (−0,21) | −78,78 (−0,12) | −75,02 (−0,14) | −83,03 (**−0,70**) | −116,25 (−4,36) |
| `B11-fx9a-b-r2` | −72,99 (−0,18) | −78,87 (−0,21) | −74,93 (−0,06) | −83,06 (**−0,74**) | −113,90 (−2,01) |

Einzelne Linien (`line_levels.py`, `out/B11-lines-table.md`): 2000 und 3000 Hz unter fx8a −103…−105 dBFS, unter fx9a-a −110…−115, unter fx9a-b −105…−108. 1215,19 Hz (≈ 96 000/79) und 7384,62 Hz (= 96 000/13) liegen in allen sechs Läufen auf 0,3 dB gleich, sie stehen in fx9a-a nur deshalb unter den „stärksten übrigen Linien“, weil 2000/3000 Hz dort tiefer liegen. Beide gab es schon in B3 (fx1p, fx2b, fx2c).

**Deutung:**
- **[gemessen] fx9a senkt fs/8 um 0,7 dB gegen fx8a.** Alle vier fx9a-Läufe liegen −0,65 bis −0,85 dB unter fx8a, vor und nach der Kontrolle gleich. fx8a liegt mit −82,32 dBFS wie in D85 (−82,32…−82,40). fx9a landet damit etwa beim Stand von fx7a (−82,95 in D85), der Anstieg durch den I-Cache ist ausgeglichen.
- **RMS −0,2…−0,4 dB, Rest −0,1…−0,6 dB, Kamm −0,1…−0,2 dB:** klein, aber in allen vier Läufen in derselben Richtung. Mischprodukte streuen wie immer um mehrere dB (D79), keine Richtung.
- **Keine neue Linie.** Die Linien bei 2000 und 3000 Hz (Vielfache des 1-kHz-Systemtakts, [Hypothese] D60) sinken mit fx9a, unterschiedlich stark zwischen Anfang und Ende.
- [Hypothese] Mit D-Cache gehen weniger Zugriffe über die Busmatrix zu AXI und D2, der Strom im Blocktakt sinkt. Das passt zu D42 (Busverkehr im Blocktakt hebt fs/8), D85 (I-Cache machte den Puls kürzer und höher) bleibt als Erklärung für fx8a offen.

**Fazit:** Alle Kriterien aus `docs/05`, „Build 11“, Punkt 1 sind erfüllt: Plateau 29 % statt 35 % (unter 30 %), fs/8 −0,7 dB (Grenze +1 dB), keine neue Linie, Loop 10 min, zwei Wechselrunden, 240/240 Downloads, vier Stores mit Rückladen, vier Löschungen. Die Leseschleife war als Kriterium falsch gewählt (siehe oben). Statt des Store-Tests auf Slot 13 lief die neue Belegung (Stores mit `--download-check`). **Die Abnahme ist vollständig. fx9a ist die Alltags-Firmware (Entscheidung des Nutzers, 2026-11-23), Rückweg fx8a.** Zustand danach: fx9a, Slot 1 läuft, gemerkt Slot 12 (leer), keine Kabel.

## D90 – Masse-Brücke auf dem Xibeca-Modul: Draht Pin 15 (GND) ↔ Pin 33 (AGND) (2026-11-23 und 2026-11-24)

**Anlass:** Antwort im Forum (modwiggler) auf den eigenen Beitrag: Die Ferritperle zwischen AGND und GND auf dem Prozessor-Modul überbrücken, die Spannung über ihr koppele in die Messung. Der Beitrag stützte sich auf den Plan von Noctua2. Schaltplan-Befund dazu in `docs/06-hardware-mod-masse.md` und `docs/01`, „Masse“: Im AC/DC steckt das Modul Xibeca (gleiche Pinbelegung, gleiche drei Ferrite L1–L3 wie Noctua2). L1 (0603) verbindet AGND und GND auf dem Modul. Die Trägerplatine von Befaco verbindet alle AGND-Pins des Moduls direkt mit GND [Code: Schaltplan]. L1 liegt also schon parallel zu einem Weg über die Steckerleiste. Erwartet war deshalb ein kleiner Effekt [Hypothese], das hat sich nicht bestätigt.

**Eingriff (2026-11-24, etwa 10:50–11:05, Nutzer):** acdc1 ausgebaut, isolierter Draht von Pin 15 zu Pin 33 auf der Rückseite des Moduls (Lötseite der Stiftleiste, Nummern laut Aufdruck), mit Kapton fixiert. Vorher Durchgang beider Pins zur Hülse einer Klinkenbuchse geprüft. Widerstand stromlos, schwarz (COM) auf Pin 15: Pin 1 (+3V3) 2,293 → 2,281 kΩ, Pin 95 (+5V) 9,04 → 8,9 kΩ, also kein Kurzschluss. Werte vom 2026-11-23 (2,26 und 8,5 kΩ) ohne Beachtung der Polung, nicht verwendet.

**Setup:** acdc1 im Case, fx9a, Slot 1, Regler 63/64/71/50 von 127 (vor und nach dem Umbau gleich), keine Kabel, Alltags-Kette, Eingänge offen, je 2 × 60 s `acdc_rec.py --reps 2 --owl-read`. Vorher-Kontrolle am Vortag `D90-vor-r1/r2` (2026-11-23, 22:41, Regler 66/56/73/56). Am Messtag `D90b-vor-r1/r2` (10:34), Umbau, `D90b-nach-r1/r2` (11:09). Alle Läufe ohne Stream-Meldungen. Kamm-f0 999,864 Hz in allen Läufen (gleicher Anschluss).

**Familien (`family_table.py`, `out/D90-session-table.md`, Datei-dBFS, Mittel über 4 Kanäle, Δ gegen D90b-vor):**

| Messung | RMS ≥ 20 Hz | Rest | Kamm | fs/8 | Mischprod. |
|---|---|---|---|---|---|
| `D90-vor-r1` (Vortag) | −72,54 | −78,23 | −74,55 | −82,70 | −115,30 |
| `D90-vor-r2` (Vortag) | −72,52 | −78,36 | −74,48 | −82,60 | −113,14 |
| `D90b-vor-r1` | −72,83 (−0,14) | −78,09 (±0) | −75,06 (−0,23) | −82,87 (−0,02) | −116,67 |
| `D90b-vor-r2` | −72,56 (+0,13) | −78,09 (±0) | −74,62 (+0,21) | −82,83 (+0,02) | −116,17 |
| `D90b-nach-r1` | −78,37 (**−5,68**) | −80,79 (**−2,70**) | −82,15 (**−7,32**) | −101,01 (**−18,16**) | nicht erkannt |
| `D90b-nach-r2` | −78,42 (**−5,73**) | −81,12 (**−3,03**) | −81,85 (**−7,02**) | −101,23 (**−18,38**) | nicht erkannt |

Breitbandiger Boden (Median der PSD-Differenz, ohne Linien): 20–200 Hz −4,0 dB, 200–2000 Hz −3,3 dB, 2–8 kHz −2,4 dB, 8–20 kHz −1,9 dB. Plot `docs/img/psd_gnd_mod.png`.

**Einzelne Linien (`line_levels.py`, Tabelle `out/D90b-lines-table.md`, Datei-dBFS, Leistungsmittel über vier Kanäle und zwei Läufe):**

| Linie | vorher | nachher | Δ |
|---|---|---|---|
| Kamm k = 1 (999,864 Hz) | −79,8 | −86,9 | −7,1 dB |
| Kamm k = 2 / k = 5 | −87,0 / −94,9 | −91,9 / −100,3 | −4,9 / −5,3 dB |
| fs/8 6000 / 12 000 / 18 000 Hz | −90,2 / −89,8 / −92,4 | −108,8 / −107,8 / −110,7 | −18,6 / −18,0 / −18,3 dB |
| 2000,0002 / 3000,0003 Hz | −106,1 / −107,0 | −118,1 / −120,4 | −12,0 / −13,4 dB |
| 50 Hz | −113,8 | −122,8 | −9,0 dB |
| 7384,62 Hz (96 000/13) / 1215,19 Hz (≈ 96 000/79) | −111,9 / −110,1 | −111,3 / −111,6 | +0,6 / −1,5 dB |
| 4401,90 Hz (Regler) | −120,4 | −119,8 | +0,6 dB |
| 9633,80 Hz (Scan des Regler-ADC) | −124,1 | −120,3 | **+3,7 dB** (Kanal 1 und 3 +9…+11 dB) |
| 19 267,6 Hz (zweite Faltung des Scans) | −117,5 | −123,4 | −5,8 dB |

**DC der offenen Eingänge (Datei, Kanal 1–4):** vorher −0,057/−0,065/−0,047/−0,057, nachher −0,043/−0,047/−0,032/−0,038. In Geräte-Vollausschlag rückt der Offset um +0,007…+0,009 näher an null, bei ≈ 9,5 V Vollausschlag (D29) etwa 65–90 mV. Im Loop-Test ebenso (−0,036/−0,038/−0,028/−0,034 → −0,023/−0,024/−0,015/−0,020).

**LED-Verschiebung (`SchliereLedPath` per `--run`, In 1–3, 1e-7 Vollausschlag):**

| | LEDstat (4 LEDs dauerhaft) | LEDblink (3 LEDs, 40 Hz) |
|---|---|---|
| 2026-11-23, 22:45–22:48 (Vortag) | −16 330 / −15 380 / −15 350 (4 Werte) | −11 360 / −10 700 / −10 950 |
| D90b-vor, 10:44–10:47 | −16 585 / −15 681 / −15 769 (4 Werte, Streuung ≈ 1 %) | −11 630 / −11 069 / −11 366 |
| D90b-nach, 11:14–11:16 | **−4 225 / −3 139 / −3 989** (3 Werte, Streuung ≈ 2 %) | −2 759 / −2 048 / −2 840 |
| Verhältnis nach/vor | **0,25 / 0,20 / 0,25** (−12…−14 dB) | 0,24 / 0,19 / 0,25 |

Je LED heißt das ≈ −1,0e-4 statt ≈ −4,0e-4 Vollausschlag (D74 maß −2,9e-4 vor dem Einbau ins Case). Der Lauf nachher wurde vom Nutzer nach drei LEDstat-Werten abgebrochen, der Mess-Patch lief danach noch etwa 2 min weiter (mit gesteckten Loop-Kabeln, D75), um 11:17:56 von Hand auf Slot 1.

**Verstärkung und Loop (`D90b-nach-loop`, 60 s, Sinus 440/530/670/790 Hz, −6 dBFS):** Pegel je Kanal −9,084/−9,034/−9,050/−9,056 dB gegen −9,106/−9,057/−9,069/−9,078 in `B11-fx9a-loop-cold` (2026-11-23), also +0,02 dB: Die Verstärkung der Kette Ausgang → Eingang ist unverändert, der Rückgang im Rauschen ist kein Pegelfehler. `phase_slips.py` 0 Ereignisse, `stale_samples.py` 0 von 96 000, 0 Stream-Meldungen.

**Deutung:**
- **[gemessen] Der Draht Pin 15 ↔ Pin 33 senkt das Rauschen der rohen Eingänge deutlich:** RMS −5,7 dB, Rest −2,9 dB, Kamm −7,2 dB, fs/8 −18,3 dB, Mischprodukte unter der Erkennung, LED-Verschiebung auf ein Viertel. Die zwei Läufe je Seite liegen auf 0,3 dB beieinander, vorher stimmt mit dem Vortag auf 0,5 dB überein. Das ist weit mehr als die Drift zwischen Sitzungen.
- **Der Kamm ist damit noch stärker die führende Familie:** Er trägt 30–50 % der Rauschleistung, fs/8 nur noch 0,5–1,3 %. Die ideale Notch-Bank brächte nur noch 1,6–3,0 dB (vorher 6–8 dB).
- [Hypothese] Ein Teil des Rückstroms des Moduls (MCU, SDRAM, LEDs, USB) floss über L1, die AGND-Fläche und die AGND-Pins zum Träger. Die Spannung über L1 und den AGND-Weg stand zwischen dem Bezug des Codecs (AGND) und dem der Eingangsstufe (Träger-GND) und landete in jeder Aufnahme. Der Draht schließt diesen Weg direkt an der Steckerleiste kurz. Dazu passt, dass alle Familien sinken, die aus Strompulsen des Moduls stammen (fs/8, Kamm, 2000/3000 Hz, LED-Strom), und der DC-Offset sich um 65–90 mV verschiebt. Ein DC-Abfall von dieser Größe braucht allerdings mehr Strom oder Widerstand, als L1 und die Steckerleiste allein erklären. Woher der DC-Anteil kommt, ist offen.
- **Nicht gesunken:** 7384,62 und 1215,19 Hz (+0,6 und −1,5 dB), 4401,90 Hz (Regler). **Gestiegen:** 9633,80 Hz (Scan des Regler-ADC) um 3,7 dB im Mittel, liegt aber bei −121 dBFS und damit 35 dB unter dem Kamm. [Hypothese] Diese Linien koppeln über einen anderen Weg (Regler-ADC und seine Referenz am Modul), den der Draht nicht oder umgekehrt berührt.
- **Nicht geprüft:** Ausgänge (am UMC), Ein- und Ausbau als Ursache (A-B-A: Draht ab, erneut messen), Hörprobe. Wegen der Größe des Effekts und der Linien, die sich nicht bewegen, ist ein Effekt des Wiedereinbaus unwahrscheinlich [Hypothese].
- **`owl/AcdcInput.h` (Sperre für fs/8 am Eingang) muss nicht angepasst werden:** Der Canceller lernt die Linien in der Stille selbst, die Schwellen (Lernen unter 20 mV Änderung, Korrektur höchstens 10 mV) hängen nicht vom Pegel der Linien ab. fs/8 liegt jetzt bei ≈ 20 µV, weit unter der Grenze der Korrektur. Der Nutzen sinkt mit dem Mod, schaden kann die Sperre nicht.

**Fazit:** Die Masse-Brücke ist die bisher wirksamste Einzelmaßnahme gegen das Rauschen der Eingänge, stärker als alle Firmware-Schritte zusammen (fx2d → fx9a: fs/8 ≈ −5 dB). acdc1 behält den Draht. acdc2 bleibt unverändert (Referenz). Anleitung: `docs/06-hardware-mod-masse.md`. Offen: A-B-A, Ausgänge, Hörprobe, Rückmeldung ins Forum.
