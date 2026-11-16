# TODO – AC/DC: Werkbank, Störlinien, Standalone-FX

Oben steht, was offen ist, nach Themen geordnet. Darunter folgen offene Fragen, dann Entfallenes mit Grund, dann die Chronik des Erledigten. Details jeweils in `docs/`, Belege im Messlog (`docs/messlog.md`, IDs wie D49).

Stand der Neuordnung: 2026-11-16.

## Offen

Jeder Flash nur nach ausdrücklicher Freigabe. acdc2 nicht anfassen. Settings nur lesen (E4).

### 1. fx3l: Alltagstest und Entscheidung
- [ ] **Entscheiden, ob fx3l 3d auf acdc1 ablöst.** fx3l läuft seit 2026-11-16 nachts auf acdc1 (D49). Im Alltag beobachten:
  - Aufnahme und Wiedergabe am Rechner: Aussetzer, Knackser
  - Meldung `fb clamp` per `tools/owl_read.py`
  - Durchleitung ohne Rechner, Eingangs-LEDs
  - Patch-Wechsel (Patch-Heap im CCM nur noch 39,3 KB)
- [ ] Hörprobe: Aufnahme mit Kompressor auf der Spur, fx3l gegen 3d. Das war der Anlass des Projekts und ist seit fx3l nicht geprüft
- [ ] Zweite Rauschsitzung 3d → fx3l → 3d. D48 hatte keine 3d-Startkontrolle, und der Kamm liegt mit +0,2…+0,4 dB an der Schwelle
- [ ] Linien bei 2000,0002 und 3000,0003 Hz (k·fs/48), die fx3j, noD und fx3k zeigen (D42, D44): bei fx3l prüfen. Die Aufnahmen `B5c-fx3l-r1/r2` liegen vor
- [ ] Klären, ob der RX-Fix (12b) auch in 3d bzw. einen Standalone-Stand gehört. In 3d wurde der Wettlauf nie gemessen. `acdc1-build3e-fx2e` liegt gebaut bereit
- [ ] Ursache der Kamm-Änderung +2,9 dB zwischen D35 und D37 klären. Aufbau laut Nutzer unverändert, aber mehr CPU-Last am Mac → A/B Mac im Leerlauf gegen Mac unter Last (z. B. `yes > /dev/null` je Kern), 2 × 60 s offene Eingänge [Hypothese: Host-Last → Masse/SOF]
- [ ] Optional: HAL löscht `GINTSTS.SOF` vor dem Callback (überzählige Interrupt-Einsprünge weg), A/B gegen fx3l

### 2. Werkzeuge
- [ ] **Flash-Skript nach `tools/`**: Gerät prüfen (UUID), DFU-Neustart, schreiben, Readback, Vergleich, Flash-Log. Heute ist das ein Ablauf in `CLAUDE.md` und ein Schnipsel in `docs/uebergaben/uebergabe-2026-11-16-patch12b.md`
- [ ] Flash-Ablauf: Prüfen, ob `dfu-util … :leave` den Neustart (Case aus, USB ab) ersetzen kann, A1 + Loop gegen Kaltstart (Nutzer-Frage 2026-11-16)
- [ ] Abhängigkeiten von `tools/owl_read.py` festhalten: Python 3.12, `mido`, `python-rtmidi`. `pyproject.toml` verlangt Python ≥ 3.14 und nennt beide Pakete nicht
- [ ] Werkzeuge in einem Doc beschreiben. Heute stehen sie nur in `CLAUDE.md` und in `--help`, `docs/03` beschreibt nur `analysis/`
- [ ] Englische Hilfe- und Konsolentexte für `tools/` und `analysis/` (zusammen mit dem öffentlichen Repo)
- [ ] Analyse-Tool: Clipping-Hinweis bei Float-Dateien nur bei flachen Kuppen melden (Fehlalarm in D15)
- [ ] **acdc2 nur lesend sichern**, mit eigener Freigabe: `tools/owl_read.py` (Slots, Settings, Report) und DFU-Readback des internen Flash. Der Readback schreibt nichts, braucht aber einen Neustart von acdc2 in den DFU-Modus. Bisher gibt es von v22.4.q kein Abbild
- [ ] Optional: Build aus dem Fork-Branch `acdc/thru-usb-feedback`, SHA mit Build 1d vergleichen (Freigabe). Für `acdc/fx1d` ist das erledigt (`verify-fx1d-5cb2c17c`)

### 3. Störlinien
- [ ] **Optional: Störbänder im Rechner entfernen, Fingerabdruck + Plugin** (Nutzer 2026-11-16). Ob sich das lohnt, hängt davon ab, wie viel Störgeräusch am Ende bleibt. Entscheiden nach Alltagstest, Hörprobe und zweiter Rauschsitzung von fx3l. Hintergrund: Mit `TX_PRE_FX` nimmt der Rechner die rohen Eingänge auf, ein Filter-Patch im Gerät erreicht die Aufnahme nicht mehr. Falls ja:
  - [ ] Das Analyse-Tool schreibt je Modul und USB-Anschluss einen „Fingerabdruck“: die genauen Störbänder (Kamm-f0 und Harmonische, fs/8, LED-PWM, stärkste übrige Linien, je mit Breite)
  - [ ] `analysis/notch.py`: Notch-Bank (SOS) aus dem Fingerabdruck, Vorher/Nachher-PSD, RMS-Reduktion
  - [ ] Parameter an echten Aufnahmen tunen, Hörtest auf Färbung
  - [ ] Kleines Plugin (VST/AU, z. B. aus FAUST), das sich mit dem Fingerabdruck des aktuellen Moduls bestücken lässt
  - Entwurf offen: Dateiformat, Plugin-Technik, Nachführen von f0 (f0 hängt am SOF des USB-Anschlusses, S2-6). Vor dem Bauen eine Grill-Runde
  - Stand heute: Der SOF-Kamm ist mit fx3l die stärkste Familie, eine ideale Notch-Bank brächte ≈ 5,8 dB (`docs/02`, D48)
- [ ] LED-aus-Patch (Messplan Schritt 7) → H3 ja/nein
- [ ] Rausch-Experimente je Build + A/B (E3): Blockgröße 16, LED-PWM-Prescaler → 0, Codec-HPF
- [ ] ITCM-Folgeideen (Q4 der Grill-Runde 2026-11-16): Jitter 0–2 µs (Daisy), WFI im Idle, gleichmäßige Last im Idle. Je eigener Build mit A/B
- [ ] Nebenbefund D6: Mischprodukte f1±f2 nur innerhalb der Ausgangspaare 1/2 und 3/4 (lauter als die Grundtöne). Test: Sinus nur auf Out 1, nur auf Out 2, dann beide, Pegel notieren (`tools/crosstalk_lines.py`)

### 4. Standalone-FX
- Vorlage: `burstMembrane/acdc-patches` (Reverb, Delay, Grain für AC/DC, PRE_FX-Firmware). Siehe `docs/research/notes/forks_update_2026-11-14.md`
- Rahmen: Der FX liegt nur ohne Rechner-Stream an den Buchsen (D20, `docs/01`). Mit fx3l bleiben 39,3 KB Patch-Heap im CCM
- [ ] Erste FX-Patches: Mixer/Attenuator, danach Write/Read-Buffer (Reaktor-artig). Steuerung über 4 Knobs + Audio-Rate-Trigger an den Eingängen
- [ ] OwlProgram + antisvins FAUST-Branch aufsetzen (Werkzeug für eigene Patches)
- [ ] Optional: Auto-Switching zur Laufzeit statt per Compile-Flag
- [ ] Idee (Nutzer, Q7): Regler bei aktivem Stream als MIDI-CC an den Host senden, nur wenn es weder Last noch Störlinien bringt. Die Firmware sendet sie heute nur auf Anfrage [Code]
- [ ] Idee (Nutzer): CV-taugliche Eingangsanzeige, z. B. Grün linear zum Betrag des Gleichanteils. Rot ist reines GPIO ohne PWM, taugt also nicht als Polaritätsanzeige mit Stärke

### 5. Firmware-Basis (später)
- [ ] **Merge mit v22.5.0 bzw. dem aktuellen Upstream-`master` (`36eaf1c4`) samt Fixes** (früher „Option A“, bleibt auf dem Plan, Nutzer 2026-11-16). Laut `docs/research/notes/upstream_master_2026-11-16.md` ist das eine Portierung, kein Merge:
  - Takt und Codec-Einstellung von v22.4.r, Blockgröße 8, 4 TDM-Slots
  - Patches 04, 05, 06, 07d, 11g, 12b, 14 auf den USB-Pfad von v22.5.0
  - shmuga-Fixes (`d8fdfa3`, `c5aff8c`, `d39aa53`, 5 Pakete aus `9104f1a`)
  - altes HAL `9e8f64e`/`5a3f964`, `TX_PRE_FX`
  - volle Abnahme A1–A7 und B1–B3, Vergleich mit fx3l
  - Vorarbeit: Patches 09 und 10, Kandidaten `cand-r-merge2250-fx2d` und `cand-master-oldhal-fx` (gebaut, nicht geflasht)
  - Der früher genannte „Rückbau `3237e7ca`“ entfällt: Der Commit betrifft `owl3.mk`, das AC/DC baut mit `xibeca.mk` [Code]
- [ ] Optional: alte Firmware (Readback) disassemblieren, ob ihr Feedback eine Pufferstand-Korrektur hat (D16)

### 6. Veröffentlichung
- [ ] Öffentliches Repo `acdc-workbench`: erster Commit, `README.md`, englische Fassung der Docs 01–05 und 99
- [ ] Eventuell: Ergebnisse als GitHub-Issue anlegen. Wo (Upstream `RebelTechnology/OpenWare` oder eigenes Repo) ist offen

## Offene Fragen
- Woher kommt die 119,944-Hz-Familie direkt am Mac?
- Einzelereignis D18 (≈ 20 ms gestört, ≈ 32 ms ohne SOF, kein Netto-Versatz): USB-Bus/Hub oder Host? Tritt es wieder auf, auch direkt am Mac?
- Hat die alte acdc1-Firmware dieselbe Feedback-Drift (nur 10 min geprüft, ≈ 72 Frames Reserve reichen ≈ 20 min)?
- Warum steigt der 1-kHz-Kamm stärker als der digitale Gain (+14…26 dB statt ≈ +9 dB)? Gemessen an acdc2 mit dem Default-Patch
- Wie entsteht die fs/8-Linie? Was die CPU im Blocktakt tut, erscheint bei fs/8 (D42) [Hypothese: Busverkehr bzw. Strompuls]
- Warum hängt der Kamm an der Lage des USB-Codes (ITCM ±0, Flash +2,5…+3,5 dB, D42/D44)?
- Warum läuft die SOF-Kette mit USB im ITCM doppelt (D46)? [Hypothese: Der Handler springt ein, bevor das gelöschte `GINTSTS.SOF` wirkt]
- Welcher der Commits `f90e3f4` (Codec Auto Rate) und `e219182` (MCLK 256fs) nimmt acdc1 das Audio (D10)?

## Entfallen oder überholt

| Punkt | Grund |
|---|---|
| Messplan Schritt 2b: echte Samplerate über einen Testton | H1 ist über S2-6 belegt. Das Taktverhältnis UMC/acdc1 = 1,000185 steht in D20 |
| Messplan Schritt 3: Bypass-Patch | Gain 0 → USB-Strom digital stumm (Serie 2). Mit Build 2 nimmt der Rechner die rohen Eingänge auf (B2/B3, D25/D26). Die Störung steckt in den ADC-Daten |
| Messplan Schritt 4: Laptop im Akkubetrieb. Dazu G3 (ohne Hub, Mac auf Akku) | Nutzer 2026-11-15: mobiler Betrieb kommt nicht vor. Masseschleife geklärt (D21) |
| Messplan Schritt 5: Ground-Lift auf der Audioseite | D21: Die Masseschleife entsteht nur mit AC/DC am Mac-Port und UMC am Hub. Im Alltag gibt es AC/DC-Out → UMC nicht |
| Isolator kaufen und testen (ADuM3160, Olimex USB-ISO-HS) | Kein Isolator nötig (D21–D23). Damit auch: VBUS-Erkennung (PA9) hinter einem Isolator, und die Frage, was Paupers „ground isolator“ war |
| FAUST-Patch `NotchBank` in Slot 1 (`load`, dann `store`, USB-Aufnahme erneut messen) | Seit Build 2 (`TX_PRE_FX`) geht der Patch-Ausgang nicht mehr in die USB-Aufnahme (D25, B2). Möglicher Ersatz, optional: Fingerabdruck + Plugin, siehe „Störlinien“ |
| Build 1: A2–A7 | A2 nicht bestanden, kein Audio (Takt v22.4.s, D10) |
| Optional: Kontrolle Build 2 gegen 3d in derselben Sitzung | fx3l löst die Frage ab (D48) |
| E3-Hebel Lage: Füllbytes vor den Audio-Funktionen durchprobieren | Mit dem heißen Pfad im ITCM zählt die Flash-Lage nicht mehr: fx3lp ≤ 0,25 dB bei fx3l (D48) |
| Neu bewerten: +4,8 dB Mischprodukte von 1b → 1d durch die Lage statt durch 05/06? | Mit fx3l liegen die Mischprodukte bei −119 dB (−35 dB gegen 3d, D48). Die Antwort ändert nichts mehr |
| `fb clamp -50.0000 32.0000` als letzte Meldung von 3b (D31) | 3b ist verworfen. `fb clamp` wird im Alltagstest von fx3l beobachtet (D49) |
| Forum-Posts in Thread #2072 und #2244 | Nutzer 2026-11-16: entfällt. Eventuell stattdessen ein GitHub-Issue, siehe „Veröffentlichung“ |
| ST-Link bestellen | Nutzer 2026-11-16: entfällt. DFU und Boot-Pads reichen (D4, D5). Debuggen per ST-Link bleibt möglich, Hinweis in `docs/05` „Flashen“ |

## Erledigt (Chronik)

### Phase 0 – Projekt-Setup
- [x] `docs/messlog.md` angelegt (M1–M3 eingetragen)
- [x] `analysis/` + `out/` angelegt, alte Aufnahmen umbenannt, `recordings/manifest.toml` angelegt
- [x] Firmware acdc2 geprüft: v22.4.q (Branch `hack/acdc-output-levels`, Blockgröße 8)
- [x] `uv add numpy scipy soundfile matplotlib`
- [x] Kennung beider AC/DCs notiert (Device-UUID statt Seriennummer, siehe Gerätetabelle in `CLAUDE.md`)
- [x] Firmware-Stand beider Geräte geprüft (openwarelab Device-Status, 2026-11-13): acdc1 meldet „v22.5.0“, acdc2 v22.4.q. Später: acdc1 war ein Hack-Build mit diesem Etikett (D3/D3a)
- [x] Testgerät = **acdc1**, Referenz = **acdc2** (v22.4.q bleibt unangetastet)
- [x] Vor dem ersten Eingriff in acdc1: gespeicherte Settings (Blockgröße, Gains) ausgelesen und gesichert (D1, `backup/acdc1/20261114/owl/`)

### Phase 1 – Analyse-Tool (Python) → `docs/03-messplan-python.md`
- [x] Spektrogramm aus Aufnahmen (erstes Skript, später entfernt. Plots M1–M3 in `out/v0/`)
- [x] Analyse-Tool neu geschrieben (`analysis/`, CLI + Manifest, Selbsttest). Altes Skript entfernt
- [x] Welch-PSD mit langem Fenster, log-x, dBFS, optional `--ref` zum Überlagern
- [x] Peak-Liste mit parabolischer Interpolation (Selbsttest: < 1 mHz bei 60 s) → JSON + Markdown
- [x] Familien fs/8, 1 kHz, LED, Netz + stärkste übrige Linien, Energieanteile (60-Hz-Kandidat ersetzt durch `--mains`)
- [x] f0-Least-Squares-Fit über alle Harmonischen (gewichtet)
- [x] Mischprodukte n·f1 + m·f2
- [x] Zeitstabilität (Fenster 10 s), Hüllkurven-Modulation
- [x] Klick-Detektor (HP 5 kHz, Hüllkurve, Abstände)
- [x] Report-Generator `out/<name>/<name>_report.md`
- [x] Aufnahme-Skript `tools/acdc_rec.py` (Ersatz für die frühere Aufnahmekette aus Host-Software und Mehrkanal-Recorder), ohne Gerät getestet (2026-11-16)
- [x] `acdc_rec.py`: Probelauf am Gerät + Gegenprobe gegen die frühere Aufnahmekette mit 3d bestanden (D35: fs/8 und Mischprodukte ±0,01, Kamm +0,43 dB)
- [x] `acdc_rec.py --sine`/`--dc`: Testsignale je Ausgang (statt Software-Oszillatoren), am Gerät benutzt ab D36 (Clip-Test) und D38 (Loop-Test)
- [x] `tools/check_itcm.py`, `tools/stale_samples.py`, `tools/family_table.py` (2026-11-16, D37–D40)

### Phase 2 – Messen → Hypothesen klären (`docs/02`, `docs/03`)
- [x] Schritt 1: offene Eingänge, Gain-Serie, beide Geräte. **Habe ich den 1-kHz-Kamm? → Ja, aber leise (M1/M2).** Sauber wiederholt in Serie 2: nativ 48 kHz, 60–120 s, Gain 7/12/17 Uhr an acdc2, Gain 12 an acdc1
- [x] Schritt 2: f0 exakt bestimmt: 1000,053 Hz (M1/M2), 1000,0528 Hz an 120 s (S2-1)
- [x] **Serie 2 aufgenommen** (S2-1 … S2-4) und ausgewertet: Mischprodukt-Periode bestätigt, acdc1 ≈ exakt 48 kHz
- [x] S2-6: acdc1 direkt am Mac statt am Hub → Kamm wandert um +124,5 ppm → **H1 (SOF-Kopplung) bestätigt**
- [x] Device-Status acdc1: „v22.5.0“, Slot 1 „ACDC“
- [x] Settings acdc1 per `tools/owl_read.py` ausgelesen (D1)
- [x] Warum unterscheidet sich das Verhältnis Sample-/CPU-Takt um 186 ppm? → Die Firmwares haben verschiedene Takteinstellungen: Readback acdc1 wie v22.4.r (PLL3 P/Q 8, FRACN 262, exakt 48 kHz), acdc2 v22.4.q (P/Q 2, FRACN 0, ≈ 47 991 Hz) [gemessen: Disassembly, D10]
- [x] Schritt 6 / S3: **Standalone-Gegenprobe** gemessen mit Build 1d (D20): Kamm ohne USB weg, SOF allein reicht
- [x] Entscheidungsbaum (`docs/03`): Kamm ja, H1 bestätigt → Isolator sinnlos, weiter mit Firmware und Filter im Rechner. Ergebnis steht in `docs/02-noise-befunde.md` als [gemessen] (S2-6, D20, D21)

### Phase 2b – Durchleitung klären (Handoff 2026-11-14)
- [x] Backup acdc1 mit eigenem Lese-Tool `tools/owl_read.py` (statt lich-patcher): Slot 1 „ACDC“ + Slot 2 `_Lich_Nichts` in `backup/acdc1/20261114/owl/`. Settings: Blockgröße 8, Bypass 0. `__SETTINGS__` ist per SysEx nicht lesbar (System-Ressource). Messlog D1
- [x] Ohne Flash/Store geprüft (D2): Auch `_Lich_Nichts` kommt mit und ohne USB nicht an der Buchse an. Patch, Settings-Bypass und USB-Stream scheiden aus. Verdacht: Build mit `237c63d` unter dem Etikett „v22.5.0“
- [x] Internes Flash von acdc1 per ROM-DFU gelesen (D3): Die Firmware ist ein Hack-Branch-Build mit dem Etikett „v22.5.0“, nicht die Release-Datei. Abbild in `backup/acdc1/20261114/flash/`
- [x] `usbd_rx_convert()` im Abbild disassembliert: `237c63d` belegt. Die acdc1-Firmware ist kein veröffentlichter Commit (Messlog D3a)
- [x] Eigenen Build geplant (`/grill-me`, 2026-11-14): Basis Hack-Spitze `7f3cc41` + Libraries `9e8f64e`, nur `237c63d` zurück. Plan E1–E7 + Abnahme A1–A7/B1–B3 in `docs/05-firmware-plan.md`. Die Basis wurde später `db9d3dd` (v22.4.r), siehe D10
- [x] Durchleitung ohne Flash nicht möglich (Firmware-Ursache, D3) → eigene Firmware vorgezogen
- [x] S3 gemessen (D20, 2026-11-15)

### Phase 4 – Standalone ohne Flash
- [x] Null-Aufwand-Vortest → **nein**: acdc1 im Kaltstart ohne USB stumm, obwohl der Default-Patch durchleitet (2026-11-14)
- [x] Mit Build 1d läuft der Default-Patch standalone durch (D11/D17). FX-Patches laufen auf 1d. Für „Interface nimmt rohe Eingänge auf, Ausgang mit FX“ braucht es `TX_PRE_FX` (ab Build 2)

### Phase 5 – Firmware (`docs/05-firmware-plan.md`)
- [x] Arm GNU Toolchain 12.2.Rel1 installiert (`/Applications/ArmGNUToolchain/12.2.rel1/`)
- [x] `tools/build_acdc.sh` + `firmware/patches/01-gcc12-extern-uint8.patch` + `firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz` (E5). Builds deterministisch
- [x] Reproduktions-Builds (q, r, s, Merge 961b49f, rc5) und Vergleich mit dem Readback: kein Treffer, acdc1 = selbst zusammengesetzter Stand (Messlog D3a)
- [x] Build 1 `v22.4.s-thru1` (`97a876b4…`) und Build 2 alt `v22.4.s-fx1` (`3a6e5df6…`) gebaut und im Binary geprüft, heute in `firmware/builds/archive/` (docs/05)
- [x] Boot-Pad-Probe (D4): DFU über die Pads erreicht, beim 2. Versuch nach Reinigen und festem Halten
- [x] Generalprobe (D5): Readback-Abbild per DFU geflasht, zurückgelesen bitgleich, Gerät unverändert
- [x] 10-min-Referenzaufnahme alte Firmware (D6, `E7-ref`): 0 Klicks. Detektor sieht bei offenen Eingängen aber nur Lücken, keine Sample-Slips
- [x] Referenz mit Rückführung (D7, `E7-ref-loop`): 0 Phasensprünge, 0 Klicks, Kanalzuordnung stimmt. Prüfwerkzeug `tools/phase_slips.py`
- [x] Build 1 geflasht (D9), A1 bestanden. A2 nicht bestanden: kein Audio (Takt v22.4.s, D10)
- [x] Build 1b `v22.4.r-thru1` gebaut und geflasht (D11): A1 und A2 bestanden, **Durchleitung ohne Rechner geht**
- [x] Build 1b: A3 (USB ohne App) und A4 (Host-Playback ↔ Durchleitung) bestanden (D11)
- [x] Build 1b: A5 im Mittel bestanden (D11)
- [x] Build 1b: **A6 nicht bestanden** – 6 Block-Slips (je 8 Samples) in 10 min (D12). Entscheidung: behalten und USB analysieren → Ursache Feedback-Drift, gelöst in Build 1d
- [x] Build 1c: `db9d3dd` + 01 + 02 + 04 (Ausgang 125) + 05 (atomarer RX-Zähler) gebaut, geflasht, A1 bestanden (D14)
- [x] Build 1c: Pegel am Scope, Durchleitung ohne USB, A6 (10 min): **0 Slips, 0 Klicks** (D15)
- [x] Build 1c: Langlauf 30 min: **nicht bestanden**, 25 Sprünge ≈ 12 Blöcke, Drift ≈ 1,15 ppm ≈ 1 Feedback-LSB; atomarer Zähler hilft nicht (D16)
- [x] Build 1d entworfen: `06-fb-level-control.patch` (Pufferstand-Regelung im Feedback), auf `db9d3dd` mit 01–05 getestet, Entwurf in `docs/05` „Build 1d“
- [x] Build 1d gebaut, geflasht, A1 bestanden (D17)
- [x] Build 1d: A2 kurz ok, Langlauf 30 min: **0 Block-Slips** (1c: 25), aber 1 Einzelereignis ≈ 20 ms ohne Netto-Versatz + `fb`-Meldung (≈ 32 ms ohne SOF) (D18)
- [x] Build 1d als Stand für acdc1 angenommen (Nutzer, 2026-11-14): kein zweiter Langlauf. Einzelereignis aus D18 beobachten, falls es im Alltag hörbar wird
- [x] Build 1d: A5 bestanden (D19): Mittel −1,1 dB gegen `A5-b1b`, Breitbandrauschen gleich, Kamm/fs8 −2 dB
- [x] Mischprodukte in A5-b1d +4,7 dB (D19): Firmware oder Sitzung? → **Firmware** (D24: 2 × A5 mit 1d auf ≤ 0,1 dB gleich)
- [x] Build 1d: **A7 = S3** gemessen (D20): SOF-Kamm am Ausgang ohne USB weg, schon ohne Stream da. Mit USB +20 dB durch Masseschleife (59,97 Hz + Fremdkamm 1000,03 Hz). Eingangs-Stream schaltet die Durchleitung ab
- [x] Masseschleife geklärt (D21): entsteht nur mit AC/DC am Mac-Port + UMC am Hub. **Beide am Hub → Ausgang so sauber wie ohne USB** (−75 dB). 59,98-Hz-Impulse = Monitor am Hub
- [x] G4: Alltags-USB-Kette (passiver Hub → Monitor-Hub → TB-Hub): Ausgang sauber, Eingangs-Linien wie A5 (D22)
- [x] G4-in +10 dB breitbandig war vorübergehend: A/B G5 (TB-Hub direkt) = G6 (Alltags-Kette) = A5-Niveau (D23). Alltags-Kette für Aufnahmen in Ordnung
- [x] **Build 2 neu auf 1d-Basis**: `v22.4.r-fx1d` = `db9d3dd` + 01, 02, 04, 05, 06 + `03-tx-pre-fx`, geflasht 2026-11-15, A1–A6 + B1–B3 bestanden (D24–D27). `owl_read.py` brauchte keine Änderung. B3 = Rausch-Basislinie der rohen Eingänge
- [x] **Build 3 (Eingangs-LEDs roh beim Aufnehmen)**: Grill-Runde, Patch 07, Build 3 `v22.4.r-fx2` (Dauer-Rot, fehlende Vorzeichenerweiterung), Build 3b `v22.4.r-fx2b` (LEDs ok), A/B gegen B3 **nicht bestanden** (fs/8 +1,4, Kamm +1,5, Mischprodukte −4,0 dB), Kontrolle mit Build 2 = B3 (D28–D31, 2026-11-15)
- [x] Build 3c (`onLoop`, DMA-Puffer): LEDs ok, A/B wie 3b nicht bestanden (D32)
- [x] Füllbyte-Test `fx1p`: **Die Lage im Speicher verschiebt die Störlinien** (D33)
- [x] **Build 3d `v22.4.r-fx2d`**: LED-Code in `.late_text`/`.late_bss`, Binary bis auf 3 Stellen = Build 2. fs/8 und Mischprodukte = Build 2, Kamm +0,4…0,55 dB. Lief auf acdc1 vom 2026-11-15 bis 2026-11-16 (D34), seitdem Rückweg
- [x] Clip-Rot von 3d geprüft und bestanden (D36), per Loop Out → In mit `acdc_rec.py --sine/--dc` statt Mixer
- [x] Recherche Lage ↔ Rauschen (2026-11-16, `docs/research/notes/layout_noise_2026-11-16.md`): Nirgends berichtet, verwandt ist der Daisy-Callback-Ton
- [x] **Heißer Pfad ins ITCM** (Idee aus der Recherche, Plan: Grill-Runde 2026-11-16, Q1–Q15):
  - [x] Patch 11 + 91, `tools/check_itcm.py`, `fx3i` und `fx3ip` gebaut und geprüft (docs/05 „Build 4“ → „Umsetzung“)
  - [x] Messsitzung 2026-11-16: 3d → fx3i → 3d (D37: fs/8 −5 dB), fx3i-Playback gestört (D38)
  - [x] fx3i-Fehler durch Halbieren gefunden (D39/D40, docs/05 „Build 4x“): USB-Slips ↔ Gruppe D im ITCM; veralteter letzter Eingangs-Sample (Kanal 4) ↔ Gruppe C im ITCM (RX-DMA-Wettlauf in `audioCallback`)
  - [x] **fx3j** = noD + RX-Warten (Patches 11e + 12), Loop sauber (D41), Rauschen 3d → fx3j → noD → 3d (D42): fx3j fs/8 +5,2 / Kamm +3,1 dB (Warteschleife kostet ≈ 10,6 dB fs/8), noD fs/8 −5,4 / Kamm +2,5 dB
  - [x] RX-Fix ohne Abfrage-Schleife: **fx3k** (Patches 11f + 12b, `audioCallback` aus den RX-DMA-Callbacks), Loop sauber (D43), Rauschen 3d → fx3k → 3d (D44): fs/8 −5,8, Kamm +3,5, Mischprodukte −19,4 dB. fx3kp nicht gemessen (Kamm-Kriterium), fx2e (3d + 12b) gebaut, nicht gemessen
  - [x] Kamm: USB-Code ins ITCM ohne Playback-Fehler. Diagnose (Patches 13/13b, D45/D46): kein Paketverlust, aber die SOF-Kette läuft mit USB im ITCM doppelt → falsches Feedback. Fix Patch 14. **fx3l** (11g + 12b + 14): Loop sauber (D47), fs/8 −5,1, Mischprodukte −35, RMS −1,1, Kamm +0,2…+0,4 dB gegen 3d (D48)
  - [x] Füllvariante gemessen (Q2 b): fx3lp ≤ 0,25 dB bei fx3l, lagenunabhängig (D48)
  - [x] fx3l für den Alltagstest auf acdc1 geflasht (D49)

### Phase 6 – Fork und Veröffentlichung
- [x] Fork-Branch `acdc/thru-usb-feedback` (= Build 1d: Durchleitung + USB-Feedback-Fix) vorbereitet und gepusht 2026-11-14: https://github.com/m9dfukc/OpenWare/tree/acdc/thru-usb-feedback
- [x] README im Fork-Branch `acdc/thru-usb-feedback` (`41fb9480`, englisch, gepusht 2026-11-15)
- [x] Fork-Branch `acdc/fx1d` (Build 2) mit README gepusht 2026-11-15: https://github.com/m9dfukc/OpenWare/tree/acdc/fx1d
- [x] `acdc/fx1d`: Commits für Build 3/3b (`f206fdd4`/`6eee596c`/`b3bd3752`), A/B von fx2b im README (`8da4eb7b`), ersetzt durch fx2d (`abc3a72a`), gepusht 2026-11-15
- [x] fx3l-Patches als Commits auf `acdc/fx1d` (08 als Cherry-Pick, 12b, 11g, 14, Version, README), gepusht 2026-11-16, Spitze `b7062ef2`, Build bytegleich mit fx3l

### Beantwortete Fragen
- Woher kommt die sample-synchrone 6-kHz-Linie (fs/8)? → Audio-Blockrate bei `AUDIO_BLOCK_SIZE 8` [Code]
- Kommt der 1-kHz-Takt vom Host-SOF? → Ja (S2-6). Verschwindet er ohne USB ganz, und reicht SOF ohne Stream? → Ja und ja, am Ausgang gemessen (S3, D20)
- Hat acdc1 dieselbe Firmware wie acdc2? → Nein: Hack-Build mit Etikett „v22.5.0“ (D3/D3a). Heute läuft fx3l (D49)
- Welcher `Libraries`-Stand liefert stabiles USB auf dem AC/DC? → altes H7-HAL `9e8f64e`/`5a3f964`. Der Bruch kam mit dem HAL-v1.11.0-Upgrade `8a07845`/`e102c6f` (docs/05) [Hypothese, stark]
