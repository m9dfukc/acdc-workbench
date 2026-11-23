# TODO – AC/DC: Werkbank, Störlinien, Standalone-FX

Oben steht, was offen ist, nach Themen geordnet. Darunter folgen offene Fragen, dann Entfallenes mit Grund, dann die Chronik des Erledigten. Details jeweils in `docs/`, Belege im Messlog (`docs/messlog.md`, IDs wie D49).

Stand der Neuordnung: 2026-11-16, zuletzt ergänzt 2026-11-18 (Build 7, Patch Schliere).

## Offen

Jeder Flash nur nach ausdrücklicher Freigabe. acdc2 nicht anfassen. Settings nur lesen (E4).

### 1. fx3l/fx4b: Alltagstest
- [x] Entschieden 2026-11-17: fx4b (= fx3l + Boot-Menü) ist die Alltags-Firmware und löst 3d ab (D59). fx3l lief seit 2026-11-16 nachts auf acdc1 (D49). Weiter im Alltag beobachten:
  - Aufnahme und Wiedergabe am Rechner: Aussetzer, Knackser
  - Meldung `fb clamp` per `tools/owl_read.py`
  - Durchleitung ohne Rechner, Eingangs-LEDs
  - Patch-Wechsel (Patch-Heap im CCM nur noch 39,3 KB)
- [ ] Hörprobe: Aufnahme mit Kompressor auf der Spur, fx3l gegen 3d. Das war der Anlass des Projekts und ist seit fx3l nicht geprüft
- [ ] Zweite Rauschsitzung 3d → fx3l → 3d. D48 hatte keine 3d-Startkontrolle, und der Kamm liegt mit +0,2…+0,4 dB an der Schwelle
- [ ] Linien bei 2000,0002 und 3000,0003 Hz (k·fs/48), die fx3j, noD und fx3k zeigen (D42, D44): bei fx3l prüfen. Die Aufnahmen `B5c-fx3l-r1/r2` liegen vor. Stand D60: fx4b zeigt sie auch (−104…−108 dB). [Hypothese] Vielfache des 1-kHz-Systemtakts, der in Codec-Zeit bei 1000,0001 Hz liegt. Welcher Takt es ist, im Code nachsehen
- [ ] Klären, ob der RX-Fix (12b) auch in 3d bzw. einen Standalone-Stand gehört. In 3d wurde der Wettlauf nie gemessen. `acdc1-build3e-fx2e` liegt gebaut bereit
- [ ] Ursache der Kamm-Änderung +2,9 dB zwischen D35 und D37 klären. Aufbau laut Nutzer unverändert, aber mehr CPU-Last am Mac → A/B Mac im Leerlauf gegen Mac unter Last (z. B. `yes > /dev/null` je Kern), 2 × 60 s offene Eingänge [Hypothese: Host-Last → Masse/SOF]
- [ ] Optional: HAL löscht `GINTSTS.SOF` vor dem Callback (überzählige Interrupt-Einsprünge weg), A/B gegen fx3l

### 1a. fx4a/fx4b/fx5a: Boot-Menü und MIDI-Fix (Abnahme D52–D58 und D62–D65, fx5a war Alltags-Firmware bis 2026-11-19)
- Stand: `firmware/builds/acdc1-build6-fx4a/` = fx3l + Patch 15. `check_itcm` und Host-Test bestanden (D50). Plan und Abnahme: `docs/05`, „Build 6“
- [x] Endwerte der vier Regler gemessen: links 2, rechts 127 von 127, Schwellen passen (D51)
- [x] fx4a geflasht, Readback bytegleich (D51)
- [x] A1 und Menü am Gerät: fx4a läuft, Slots unverändert, die Wahl (Slot 3) wurde einmal gemerkt (D52)
- [x] Abbruch mit Regler 3, Start aus dem Speicher und Timeout am Gerät geprüft (Nutzer, fx4a, D53)
- [x] Loop-Test fx4b bestanden, auch mit Tanh3 bei 53 % CPU (D57)
- [x] Rausch-A/B fx4b gegen fx3l bestanden: alle Familien innerhalb ±0,4 dB, im Mittel ±0,2 dB (D58). Abnahme von Build 6/6b vollständig
- [x] fx4b ist die Alltags-Firmware (Nutzer, 2026-11-17, D59). Fork-Branch `acdc/fx1d` lokal nachgezogen (`7ef6284a`, `2c963e3a`, `27d3630b`), ein Build daraus ist bytegleich mit fx4b. `docs/en/05` aufgefrischt
- [x] Fork-Branch `acdc/fx1d` und Workbench gepusht, Release `acdc-v22.4.r-fx4b` am Fork angelegt (2026-11-17, Freigabe des Nutzers)
- [x] **Linien bei 2200,95 / 4401,90 / 6602,85 Hz: welcher Regler, welcher Anschlag?** Serie K1 (D60): jeder Regler, beide Anschläge, links ≈ 2,5 dB stärker als rechts. Ein Regler am Anschlag hebt die Linien um 13…17 dB, auf 12 Uhr bleiben sie 6…16 dB über dem Grundrauschen. Dazu eine Linie bei 8549,33 Hz
- [x] **Reglerlinien, Serie K2** (D61): Der Anschlag selbst ist es nicht. LLLL und RRRR liegen wie 12 Uhr, LRLR bringt −94 dB (21 dB über der Kontrolle), der Pegel wächst stetig mit dem Abstand eines Reglers von den anderen. Es zählt der Unterschied zwischen den Reglern
- [ ] Reglerlinien: Quelle der Frequenzen 2200,95 und 8549,33 Hz finden. 2200,95 Hz steht für einen Durchlauf durch die vier Regler (D61), der ADC-Scan läuft aber mit 105 633,8 Hz und faltet auf 9633,80 Hz (D60). Dazwischen liegen 103 432,86 bzw. 107 834,76 Hz, ein passender Takt ist nicht gefunden. Wege:
  - an acdc2 nur aufnehmen, Regler in Stellung LRLR. Die Verschiebung der Linie gegen acdc1 ergibt die Quellfrequenz (wie beim ADC-Alias, D60). Braucht eine eigene Freigabe, weil acdc2 Referenz ist, geschrieben wird dabei nichts
  - Test-Build mit anderer ADC-Abtastzeit: Wandert die Linie mit der Scanrate?
  - Schaltplan: Zuordnung der ADC-Kanäle 10, 11, 14, 3 zu den Reglern, Beschaltung der Schleifer (Kondensator?), Referenz
- [ ] Reglerlinien: Abhilfe prüfen, wenn die Quelle klar ist (ein ADC-Scan je Audioblock statt freiem Lauf, längere Abtastzeit), je mit A/B. Schlimmster Fall heute: −94 dB bei LRLR, 19 dB unter dem Kamm
- [ ] `K2-03-RRRR` zeigt die Mischprodukte aus fs/8 und Kamm 12…17 dB über den Kontrollen (D61, einzelne Aufnahme). Wiederholen: RRRR gegen MMMM, je 2 × 60 s
- [ ] Linie der ADC-Scanrate bei 9633,80 und 19 267,6 Hz (−116…−129 dB, D60): Abhilfe wäre ein ADC-Start im Blocktakt oder eine Scanrate, die auf ein Vielfaches von 48 kHz fällt. Nur mit A/B, die Linie ist schwach
- [x] MIDI-Ausfall (D53) eingegrenzt: Wettlauf im MIDI-Sendeweg der Original-Firmware bei Slot-Downloads neben einem laufenden Patch (D54). Die Werkzeuge umgehen den Download
- [x] **Firmware-Fix für den MIDI-Sendeweg** (Patch 16, Build 7 `v22.4.r-fx5a`, 2026-11-18): Fehler auf fx4b reproduziert (19 von 79 Downloads beschädigt, dann Hänger, D62). fx5a: 240 von 240 Downloads in Ordnung, kein Hänger, Loop-Test bestanden (D63), Rauschen ohne Hinweis auf eine Änderung (D64). fx5a läuft auf acdc1. Plan und Abnahme: `docs/05`, „Build 7“
- [x] fx5a ist die Alltags-Firmware (Nutzer, 2026-11-18, D65)
- [x] Fork-Branch `acdc/fx1d` lokal nachgezogen (`bd04588e`, `c222fa49`, `b4b95e43`), ein Build daraus ist bytegleich mit fx5a (2026-11-18)
- [x] Fork-Branch `acdc/fx1d` und Workbench gepusht, Release `acdc-v22.4.r-fx5a` am Fork angelegt, `docs/en/05` aufgefrischt (2026-11-18, Freigabe des Nutzers)
- [ ] fx5a: Rausch-A/B bei den Mischprodukten nicht entscheidbar (im Mittel +0,70 dB, die beiden fx4b-Kontrollen lagen 2,3 dB auseinander, D64). Bei Gelegenheit wiederholen, ohne Loop-Tests dazwischen
- [ ] Kleine Störung auf Kanal 2 während Slot-Downloads (±0,002 Samples Phase, nur im Loop-Lauf mit Downloads gesehen, D63). Auf fx4b gegenprüfen geht wegen des Hängers schlecht, eher mit fx5a eingrenzen: Kanal, Slot, mit und ohne laufenden Patch
- [ ] MIDI: Antworten aus dem USB-Interrupt können mitten in ein SysEx der Hauptschleife fallen (verschachtelte Nachrichten, bewusst nicht in Patch 16). Tritt nur auf, wenn der Rechner während eines Downloads anfragt
- [ ] MIDI: Patch 16 ändert `usbd_midi.c` (andere Geräte, Bootloader) gleichlautend mit, gebaut und geprüft ist nur das AC/DC
- [x] Neue Patch-Builds gespeichert (D54): TapeDelay, Grainz, RingsReverb mit Limiter, Tanh3 in Slot 5
- [ ] Neue Builds anhören: Limiter scheint zu funktionieren (Nutzer, D56). Tanh3 Fassung 2 (4× Oversampling gegen Aliasing, D56) beurteilen
- [ ] Tanh3 braucht 48 % CPU (D56). Auswege: Blockgröße 16 oder 32 (zur Laufzeit per SysEx `BS` setzbar, nie getestet, verschiebt die Blockraten-Linie), Oversampling nur bei Signal, kürzerer Abwärtsfilter
- [x] fx4b (Abbruch nach 30 s, `acdc1-build6b-fx4b`) geflasht, Readback bytegleich (D55)
- [x] fx4b: A1 nach dem Neustart bestanden, Slot 4 startet aus dem Speicher (D55)
- [ ] fx4b: Timeout 30 s am Gerät nachmessen
- [ ] Grainz: 78 % CPU bei Density am Linksanschlag (D52). Prüfen, ob es Aussetzer gibt. Möglicher Ausweg: Build mit `PLATFORM=OWL3` (Cortex-M7-Flags)
- [ ] Die vier FX-Patches anhören (Slots 2–5, D50). TapeDelay braucht 31 % CPU bei Blockgröße 8

### 2. Werkzeuge
- [x] **Flash-Skript `tools/flash_acdc.py`** (2026-11-18): Offline-Prüfung des Builds, Gerät prüfen (UUID und DFU-Seriennummer), DFU-Neustart, schreiben, Readback, Vergleich, Flash-Log, A1 nach dem Neustart (`--a1`). Geprüft offline und gegen Attrappen für `uv` und `dfu-util`
- [x] `tools/flash_acdc.py` am Gerät erprobt (2026-11-18, D63/D64): drei Flashes mit Readback und A1, ohne Fehler. `--from-dfu` und der Abbruchweg liefen am Gerät noch nicht
- [x] `tools/dump_stress.py` (2026-11-18): Download-Stresstest für den MIDI-Sendeweg, am Gerät benutzt in D62/D63
- [x] `tools/line_levels.py` (Linienpegel direkt bei der Frequenz) und `tools/knob_series.py` (geführte Reglerserie), 2026-11-18, am Gerät benutzt in D60
- [x] Flash-Ablauf: `dfu-util … :leave` ersetzt den Neustart von Hand (D79): A1 bestanden, Rauschen nach `:leave` wie nach Kaltstart, Loop-Test nach Kaltstart bestanden. Seit 2026-11-19 Standard in `flash_acdc.py`, `--cold` für den Kaltstart
- [ ] `flash_acdc.py` mit `:leave` beim nächsten Flash am Gerät erproben (bisher nur gegen Attrappen)
- [ ] Abhängigkeiten von `tools/owl_read.py` festhalten: Python 3.12, `mido`, `python-rtmidi`. `pyproject.toml` verlangt Python ≥ 3.14 und nennt beide Pakete nicht
- [ ] Werkzeuge in einem Doc beschreiben. Heute stehen sie nur in `CLAUDE.md` und in `--help`, `docs/03` beschreibt nur `analysis/`
- [x] Englische Hilfe- und Konsolentexte für `tools/` und `analysis/` (2026-11-16). Kommentare im Code und Reports bleiben deutsch
- [ ] Sprachschalter `--lang en|de` für die Reports der Analyse, Standard deutsch
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
- [x] OwlProgram für C++-Patches aufgesetzt (2026-11-17): `tools/build_owl_patch.sh`, Upload mit `tools/owl_write.py`. Vier Patches aus `burstMembrane/acdc-patches` liegen auf acdc1 (D50)
- [x] Eigener Patch „Schliere“ (2026-11-18, D66): Kette aus 61 Allpässen 2. Ordnung nach dem Vorbild eines Eurorack-Moduls, mono hinein, stereo heraus, dazu Diff und Tail. Host-Test mit 25 Fällen bestanden, 28 % CPU, liegt auf Slot 6 von acdc1
- [x] Fiepsen in Schliere Fassung 1 ist die LED-PWM (D67): 2321 Hz mit Vielfachen an Out 1, Pegel folgt dem LED-Muster des Tap-Reglers um bis zu 27 dB. H3 damit am Ausgang bewiesen
- [x] Schliere Fassung 2 gegengemessen (D68): LED-Linie 2321 Hz um 31 dB kleiner. Es bleiben die Blockraten-Linien 6/12/18 kHz und der 1-kHz-Kamm, sie stecken schon im Eingangssignal
- [x] Rohe Eingänge im Case gemessen (D69): Schliere hebt fs/8 um 3,8 dB und die Mischprodukte um 13,4 dB gegen den Default-Patch (29 % statt 6 % CPU). Im Case gegen daneben keine Verschlechterung in den ADC-Daten
- [x] Blockraten-Sperre am Rechner geprüft (D70): `owl/AcdcInput.h`, an den C1-Aufnahmen fällt die fs/8-Familie um 42–47 dB, Host-Test bestanden. Schliere Fassung 3 damit gebaut
- [x] Schliere Fassung 3 am Gerät gemessen (D71): Blockraten-Linien an Out 1 um 22–25 dB kleiner, Kontrollen mit Fassung 2 innerhalb 0,7 dB. Rest −97…−101 dBFS am UMC, 12–16 dB über dem Teppich
- [x] Schliere Fassung 3 auf Slot 6 gespeichert und bytegleich zurückgelesen (D71, Nachtrag, 2026-11-18)
- [ ] Schliere Fassung 3: Hörurteil des Nutzers. Mit Signal und bewegten Reglern prüfen (Sperre lernt nur in der Stille)
- [ ] Blockraten-Sperre als Hülle für die anderen FX-Patches (`AcdcInput.h`, Schalter in `build_owl_patch.sh` wie `LIMIT=1`), danach je Patch gegenmessen. Woher kommt der Rest von −97 dBFS am Ausgang (D71)?
- [x] D72: Fassung 3 mit Regler 3 von Anschlag zu Anschlag am UMC aufgenommen. Bei dauerhaft leuchtenden LEDs (Rot plus fast volles Grün, [Code]) keine LED-Linie über dem Rauschen. Dem Regler folgen die Regler-Linien 2200,95 / 4401,90 / 6602,85 Hz, am Linksanschlag so stark wie der Kamm
- [x] D73: LED-Test-Patch (`owl/test/SchliereLedTestPatch.hpp`) am UMC gemessen. Dauerhaft rote LEDs stören nicht messbar. Jeder Wechsel einer LED verschiebt den Ausgang (Knack, 6-fach über dem Rauschen je LED), Blinken mit 40 Hz hebt den Pegel um 17,6 dB, gedimmtes Grün fiepst mit −39,8 dBFS
- [x] D74: Die Verschiebung entsteht am Eingang. Mess-Patch `owl/test/SchliereLedPathPatch.hpp` misst an den rohen Eingängen 1–3 je leuchtender LED −2,9e-4 Vollausschlag (≈ −2,9 mV, −71 dBFS), auf allen Kanälen gleich. Direkt am Ausgang kommt bei digital stummem Ausgang etwa 0,15 mV je LED dazu (24 dB weniger)
- [ ] LED-Strom in den Aufnahmen (D74): Wie stark wandert der Nullpunkt mit den Pegel-LEDs bei Musik? Aufnahme der rohen Eingänge mit einem Burst auf einem Kanal, die anderen offen
- [x] Build 8 `v22.4.r-fx6a` vorbereitet (2026-11-18): Patch 17, LED-Modus (normal, nur Clip, aus) im Boot-Menü über Regler 2, Ressource `ACDC.led`. Host-Tests (48 Fälle) und `check_itcm` bestanden, `6a3fc427…`. Nicht geflasht
- [x] Build 8 auf acdc1 geflasht (2026-11-18, D75): Readback bytegleich, A1 bestanden. Modus aus: Verschiebung der Eingänge auf 1,7 % (−37 dB). Modus normal wie fx5a. Clip-Test im Modus nur Clip: Sprung der offenen Eingänge um −0,08…−0,15 mV, als In 1 die Schwelle erreicht
- [ ] **Fehler: Program Change bei offenem Stream bricht die USB-Wiedergabe (D76, unter fx5a genauso: D77).** Danach rund 10 % Stille an allen Ausgängen bis zum nächsten Stream-Start, `fb clamp`. Unabhängig von Patch und Last. Ursache im Code suchen (Audio-Task steht beim Laden, Empfangspuffer und Zähler), eigener Patch, danach die Läufe `B8-fx6a-pc*-stream` wiederholen. Bis dahin: Patch nur ohne offenen Stream wechseln
- [x] Abnahme Build 8 vollständig (D75–D77). Als Alltags-Firmware abgelöst durch fx7a (2026-11-19), fx6a ist der Rückweg. Stand 2026-11-19, 11:23: fx6a, LED-Modus normal, es läuft Slot 1 per Program Change, gemerkt ist Slot 6, kein Kabel, Oszillator im Case abgesteckt
  - [x] Mess-Patch `SchliereLedPath` nach Aus und Ein ohne Stream: Eingänge ruhig (Blinken 0,3 % von normal), ein dunkler Modus ist gemerkt (D75, Nachtrag 2026-11-19)
  - [x] Clip-Probe im gemerkten Modus: Die offenen Eingänge springen an der Clip-Schwelle der Firmware, 220 ms vor dem Anschlag des Wandlers. Gemerkt ist nur Clip, der Sprung ist die rote LED 1, vom Nutzer bei der Wiederholung gesehen (D75, zweiter Nachtrag). Die Gegenprobe im Modus aus ist damit keine Pflicht mehr
  - [x] Nur Clip frisch aus dem Menü, ohne Stream: ruhig (Blinken 0,4–0,5 % von normal). Die laute Messung vom 2026-11-18, 23:24 lässt sich damit nicht nachstellen, vermutlich war da der Modus normal aktiv (D75, dritter Nachtrag)
  - Warum ist die Stufe einer roten LED am 2026-11-19 doppelt so groß (−2,0e-4) wie am Vorabend (−1,1e-4)? Regler, zweites Interface an Out 1?
  - Drift von 2 dB in der Sitzung D77 und LED-Verschiebung heute 25–35 % größer als am Vorabend: Ursache offen
  - Der statische Rest im dunklen Modus streut (+70…+272e-7), vermutlich Drift. Nur klären, wenn er stört
  - [x] Download-Stresstest ohne Stream: 240 von 240 in Ordnung, mit TapeDelay und mit Tanh3 als laufendem Patch (D75, vierter Nachtrag)
  - [x] Loop-Test bestanden, auch mit Tanh3 und während 48 Downloads (D76)
  - [x] Rausch-A/B gegen fx5a: kein Hinweis auf einen Unterschied, fx5a liegt zwischen den beiden fx6a-Kontrollen. Die Sitzung driftet um 2 dB (D77)
  - Danach Entscheidung des Nutzers über die Alltags-Firmware, dann Fork-Commits, Release und englische Fassung von `docs/05`
- [x] Build 9 `v22.4.r-fx7a` gebaut (2026-11-19): Patch 18, LED-PWM mit 48 000 Hz (TIM2/3/4/8 Vorteiler 4, Period 999), fest an den Audio-Takt gekoppelt (gleicher Quarz, 0,1 ppm). Variante A: nur Timer-Init, `setLed()` unverändert, Werte unter 2,4 % dunkel. `check_itcm --same-itcm fx6a` (ITCM bytegleich), Host-Tests, Offline-Prüfung bestanden, `cac6fee0…`. Nicht geflasht
- [x] Build 9 auf acdc1 geflasht (2026-11-19, D78): Readback bytegleich, A1 bestanden
- [x] Build 9, LED-Linie am Ausgang (D78): gedimmtes Grün bringt keine Linie mehr (2321 Hz −85,2 dBFS im Rauschen statt −39,8), keine neue Linie
- [x] Build 9, LED-Verschiebung an den Eingängen (D78): gleich wie fx6a (±2 %), wie erwartet
- [x] Build 9: Rauschen gleich fx6a, LED-PWM-Linie auch in den rohen Eingängen weg, Loop-Test bestanden, Helligkeit in Ordnung (D78, D79)
- [x] fx7a ist die Alltags-Firmware (Entscheidung des Nutzers, 2026-11-19), Rückweg fx6a
- [x] Fork-Commits für fx6a und fx7a auf `acdc/fx1d` (`1cf56d3e` … `13b58412`), Prüf-Builds bytegleich (2026-11-19)
- [x] Fork `acdc/fx1d` gepusht (2026-11-19, `b4b95e43..13b58412`)
- [x] Release `acdc-v22.4.r-fx7a` (2026-11-19, Tag auf `13b58412`, „Latest“)
- [x] Englische Fassung von `docs/05` für Build 8 und 9 aufgefrischt (2026-11-19)
- [ ] Hörbares Fiepen des Moduls (D79, auch im DFU-Modus, ≈ 800–1000 Hz, leise): Quelle eingrenzen (Modul oder Netzteil, Ohr oder Mikrofon), hören, ob es mit Last, Slot oder Reglern wandert. USB abziehen macht es leiser und höher (Nutzer). [Hypothese] Schaltregler im Pulsbetrieb
- [ ] Idee (D74): Die Verschiebung ist auf allen Eingängen gleich. Ein offener Eingang als Bezug, den ein Patch abzieht? Kostet Rauschen, träfe aber auch Kamm und Blockrate, soweit sie auf allen Kanälen gleich sind
- [x] Schliere Fassung 4 (D80, am Rechner): Tap- und Feedback-CV bandbegrenzt, weiche Totzone und weiches Knie, gefaltete Linien bei Audio-Rate um 30–50 dB kleiner. Rastpunkt-LEDs nur noch nach Regler 3, mit Hysterese (D73). Dazu Schliere M (Tap ändert die Länge der Kette stufenlos)
- [x] Schliere Fassung 4 auf Slot 6 und Schliere M auf Slot 7 geladen (D80, Nachtrag, 2026-11-19, 14:45): Rückmeldung von Größe und CRC stimmt, 33 % und 49 % CPU
- [x] Schliere M: Rechenlast mit Tap am Rechtsanschlag 54 % (110 Stufen, D80 Nachtrag)
- [x] Fassung 4 ist dem Nutzer zu zahm, er mochte die Glitches von Fassung 3. Fassung 3 liegt deshalb zusätzlich auf Slot 8 (D80, zweiter Nachtrag)
- [x] Zwischenstufe SchliereW (Feedback-Glättung 12 kHz, weiches Knie bleibt) gebaut und auf Slot 9 geladen (D80, dritter Nachtrag)
- [x] SchliereO: Eingang der Kette mit 96 kHz, Feedback ungeglättet, auf Slot 10 (D80, vierter Nachtrag)
- [x] Schliere-Varianten in `owl/schliere/` mit README (de/en), Slots 6 A, 7 M, 8 Z, 9 W, 10 O (D80, sechster Nachtrag). SchliereM ist dem Nutzer zu zahm, bleibt aber vorerst auf Slot 7
- [x] SchliereS (O mit ganz leicht geglättetem Feedback-CV) auf Slot 11 (D80, siebter Nachtrag)
- [ ] Schliere-Varianten hören und entscheiden, welche bleiben: 6 SchliereA (Fassung 3), 8 SchliereZ (Fassung 4), 9 SchliereW, 10 SchliereO, 11 SchliereS, 12 SchliereL
- [x] SchliereL: S mit 160 Stufen (320 Pole) wie das Vorbild mit Config-Datei, am Rechner geprüft, gebaut (D81)
- [x] SchliereL auf Slot 12 geladen, 70 % CPU (D81, Nachtrag 2026-11-21)
- [ ] SchliereL anhören, dazu die Linien am Ausgang bei 70 % Last (fs/8 und Mischprodukte steigen mit der Last, D69)
- [ ] Schliere M anhören: Tap- und Feedback-Modulation, Out 2 → In 4
- [ ] Schliere M: Faltung bei Tap-Modulation (−64…−70 dB) und im Selbst-Patch höher als Fassung 4 (D80), Ursache klären
- [ ] Regler-Linien am Ausgang eines FX-Patches (D72): Quelle klären (D61) und prüfen, ob die Firmware sie senken kann (Abtastzeit oder Scanrate des Regler-ADC)
- [ ] Wandernde Linien in D72 (684,8 Hz mit Oktaven, 942,5 Hz, 281,6 Hz) zuordnen: Reglerstellung, andere Module im Case oder Messkette?
- [ ] Stärkste Linien am Ausgang sind jetzt die des USB-Kamms (D71). Der ist nicht sample-synchron, eine Sperre müsste f0 nachführen
- [ ] Ausgänge im Case gegen daneben messen (zweites Interface, gleiche Kette, gleicher Pegel): Streut das Case direkt auf die Ausgänge ein? (D69 hat nur die Eingänge)
- [ ] LED-PWM als Störquelle (D67): betrifft jeden Patch, der LEDs dimmt, und die Ausgangs-LEDs der Firmware. Möglicher Firmware-Weg: PWM-Frequenz über den Hörbereich legen oder LEDs nur schalten
- [ ] Schliere anhören und beurteilen (D66): Breite der Haltezonen am Tap-Regler (geschätzt 15 %), Regelweg des Feedbacks, Pegel der Ausgänge 3/4
- [ ] Schliere am Gerät nachmessen (D66): Gruppenlaufzeit und Kerben per Loop Out n → In 1, CV-Skalierung an In 2–4, LEDs
- [ ] Schliere, Ideen: Abgriffe als Ressource einstellbar, Regler für die Streuung der Koeffizienten (Richtung Diffusion), Hüllkurven-CV statt Tail an Out 4
- [ ] FAUST-Patches bauen (`TapeDelay.dsp`, `FaustTapeDelay.dsp`): braucht den FAUST-Compiler und laut antisvin seinen OwlProgram-Branch
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
- [x] Repo `acdc-workbench` lokal angelegt (2026-11-16): `.gitignore`, Lizenzen, `README.md`/`README.de.md`, `firmware/OpenWare` als Submodul, englische Fassung der Docs 01–05 und 99 in `docs/en/`
- [x] Fork-README ohne Programmnamen gepusht 2026-11-16 (`acdc/fx1d` `3e3a74fd`, `acdc/thru-usb-feedback` `edb32852`)
- [x] `acdc-workbench` auf GitHub angelegt, gepusht und öffentlich geschaltet (2026-11-16): https://github.com/m9dfukc/acdc-workbench
- [x] Releases am Fork angelegt 2026-11-16: `acdc-v22.4.r-fx2d` (3d, Tag auf `abc3a72a`) und `acdc-v22.4.r-fx3l` (Vorabversion, Tag auf `3e3a74fd`), je `ACDC-<version>.bin` und `BUILD_INFO`. Anhänge heruntergeladen und gegen die SHA-256 geprüft
- [ ] fx3l-Release von „Vorabversion“ auf Release stellen, wenn Alltagstest und zweite Rauschsitzung bestanden sind
- [x] Eigene OWL-Patches als eigenes Repo `m9dfukc/acdc-patches` (öffentlich, GPL-3.0-or-later, Geschichte von `owl/` übernommen), hier als Submodul `owl/` eingebunden (2026-11-23).. `BUILD_INFO.txt` der eigenen Builds kurz mit im Repo, am selben Tag wieder entfernt (volle lokale Pfade, Nutzer 2026-11-23), bleiben lokal in `owl-patches/builds/`
- [ ] Gebaute `.syx` der eigenen Patches (Tanh3, Schliere A–L) als Release-Assets an `acdc-patches` hängen (Nutzer 2026-11-23: nicht ins Repo). SHA-256 aus `owl-patches/builds/<name>/BUILD_INFO.txt` in die Release-Notiz, nicht die ganze Datei (lokale Pfade)
- [ ] Eventuell: Ergebnisse als GitHub-Issue anlegen. Wo (Upstream `RebelTechnology/OpenWare` oder eigenes Repo) ist offen

### 7. Serielles MIDI oder I2C über den Header hinten (irgendwann, keine Eile)
- Nutzer 2026-11-18: im Moment nicht wichtig, könnte später interessant werden. Ziel: MIDI-Controller steuern im Standalone-Betrieb Patch-Parameter (E–H und erweiterte, A–D gehören den Reglern)
- Stand: nur recherchiert. Header = roher 3,3-V-UART (Pin 1 RX, 2 GND, 3 TX) ohne Versorgung, das vorhandene 2-HP-Breakout ist passiv. Schaltung der Zwischenplatine und Belege: `docs/01`, „MIDI-Header auf der Rückseite“, und `docs/research/notes/midi_header_2026-11-18.md`
- USB-Host an der vorderen Buchse ist verworfen (Port nur Gerät, keine 5 V, Flash knapp)
- [ ] Am Gerät messen, mit fx4b: Header-Pin 3 gegen Pin 2 ≈ 3,3 V? Bestätigt TX und die Orientierung
- [ ] Firmware-Patch für UART-MIDI: 31250 Baud, `USE_UART_MIDI_RX` (TX optional), `UART_MIDI_HANDLE`, DMA-Kanal und Interrupts. Vorlage `XibecaDevKit`. Mit `check_itcm`, Loop-Test und Rausch-A/B gegen fx4b
- [ ] Klären, welcher MCU-Pin an Header-Pin 1 liegt (PB5 = UART5 oder PB7 = USART1): Test-Build und Drahtbrücke Pin 3 → Pin 1
- [ ] Zwischenplatine in Lochraster bauen: erst MIDI In (H11L1, 78L33), MIDI Out (74HC14) nur bei Bedarf
- [ ] Typ A oder B an den MIDI-Buchsen der Controller prüfen. Controller nur mit USB bleiben außen vor
- **Alternative I2C statt MIDI** (Nutzer-Frage 2026-11-18): Der Header taugt elektrisch auch für I2C (Netze `SDA_RX`/`SCL_TX`), z. B. als Follower am ii-Bus eines monome crow. MIDI und I2C teilen sich die Pins, es geht nur eines von beiden. Für die Steuerung der kürzere Weg: kein Optokoppler, keine Versorgung. Einzelheiten in der Notiz, Abschnitt 6
  - [ ] Vor dem Anschließen: Pinfolge kreuzen (ii = GND, SCL, SDA, AC/DC = SDA, GND, SCL) und Busspannung klären. Die ii-Pull-ups gehen laut monome nach 5 V, also 5-V-Festigkeit von PB6/PB7 im Datenblatt prüfen oder Pegelwandler bauen
  - [ ] Firmware-Patch: I2C1 als Follower mit eigener Adresse, Befehle auf Patch-Parameter legen (Format wie TELEXo, `0x11 Port High Low`). Mit `check_itcm`, Loop-Test und Rausch-A/B
  - Ein- und Ausgänge erweitern: nur Steuerspannungen und Regler (AC/DC führt den Bus, z. B. TELEXi), mit Rausch-A/B wegen der regelmäßigen Abfragen (D42). Audio geht über I2C nicht

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
