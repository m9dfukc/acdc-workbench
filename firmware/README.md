# firmware/

Alles zur eigenen AC/DC-Firmware. Plan, Begründungen und Ergebnis jedes Builds: `docs/05-firmware-plan.md`, Messungen: `docs/messlog.md`.

**Stand 2026-11-23, abends:** Build 11 `builds/acdc1-build11-fx9a/` (`v22.4.r-fx9a`, `fd77ec3a…`) = fx8a + Patch 20 (D-Cache an) ist gebaut und am Rechner geprüft (`check_itcm --same-itcm fx8a`, Disassembly, Offline-Prüfung) und **läuft seit 2026-11-23 auf acdc1** (D88, D89): Abnahme vollständig, Plateau 29 % statt 35 %, fs/8 −0,7 dB gegen fx8a. **Alltags-Firmware** (Entscheidung des Nutzers, 2026-11-23), Rückweg fx8a. **Stand 2026-11-23:** Auf acdc1 läuft `builds/acdc1-build10-fx8a/` (`v22.4.r-fx8a`, `e1b1097b…`) = fx7a + Patch 19 (I-Cache an), Abnahme vollständig (D84, D85), **Alltags-Firmware** (Entscheidung des Nutzers, 2026-11-23), Rückweg fx7a. **Stand 2026-11-19:** Alltags-Firmware auf acdc1 ist `builds/acdc1-build9-fx7a/` (`v22.4.r-fx7a`, SHA-256 `cac6fee0…`, D78, D79) = fx6a + Patch 18 (LED-PWM 48 kHz), Release `acdc-v22.4.r-fx7a`. Rückweg ist `builds/acdc1-build8-fx6a/` (`v22.4.r-fx6a`, `6a3fc427…`) = fx5a + Patch 17 (LED-Modus), Abnahme vollständig (D75–D77), ohne eigenes Release. **Davor am 2026-11-18:** Auf acdc1 läuft `builds/acdc1-build7-fx5a/` (`v22.4.r-fx5a`, SHA-256 `b69c25b3…`, D63) = fx4b + Patch 16 (MIDI-Sendeweg). Abnahme D62–D64, Alltags-Firmware seit 2026-11-18 (D65), Rückweg ist fx4b. **Stand 2026-11-17:** Auf acdc1 läuft `builds/acdc1-build6b-fx4b/` (`v22.4.r-fx4b`, SHA-256 `a21f35c9…`, D55) als Alltags-Firmware (D59). Loop-Test (D57) und Rausch-A/B gegen fx3l (D58) sind bestanden. Der Vorgänger `builds/acdc1-build6-fx4a/` (`e7ee9b90…`) hat das Boot-Menü am Gerät bestanden (D52/D53). Rückweg ist `builds/acdc1-build5c-fx3l/` (`v22.4.r-fx3l`, `b55b94d8…`, D49), danach `builds/acdc1-build3d-fx2/` (`d212cf8d…`).

| Ordner | Inhalt | Regeln |
|---|---|---|
| `OpenWare/` | **Submodul** des Hauptrepos (`https://github.com/m9dfukc/OpenWare.git`, Branch `acdc/fx1d`). Lokale Remotes: `fork` (`m9dfukc/OpenWare`) und `upstream` (RebelTechnology, alle Branches als `upstream/*`, alle Tags). Ausgecheckt: `acdc/fx1d` = Build 2 → 3d → fx3l → **fx4b** + README, Spitze `27d3630b` (gepusht 2026-11-17, Release `acdc-v22.4.r-fx4b`). Daneben `acdc/thru-usb-feedback` = Build 1d + README, Spitze `edb32852`. Die Spitze von `acdc/thru-usb-feedback` ist ein README-Commit vom 2026-11-16 und gepusht. Quelle für `tools/build_acdc.sh` (`git archive <commit>`, unabhängig vom ausgecheckten Branch) | Der ausgecheckte Commit ist der Stand, den das Hauptrepo festhält. Commit/Fetch nur mit Freigabe, Push immer nachfragen |
| `patches/` | Quelltext-Patches für `build_acdc.sh`, siehe Liste unten | Nicht umbenennen, `BUILD_INFO.txt` nennt sie mit SHA |
| `builds/` | Fertige Builds, je Ordner `ACDC.bin`, `ACDC.elf` (beide nur lokal, nicht im Repo), `build.log`, `BUILD_INFO.txt`, bei ITCM-Builds dazu `check_itcm.md`/`.json`. Siehe Liste unten | Geflashte Builds nie überschreiben |
| `builds/archive/` | Überholte Builds: Reproduktions-Builds `repro-*` (E5), Build 1 (`v22.4.s-thru1`, geflasht, kein Audio, D10), Build 2 alt (`v22.4.s-fx1`, nie geflasht) | Nur zum Nachschlagen |
| `flashlog/` | Je Flash ein Ordner: Geräte-Report vorher/nachher, dfu-util-Logs, Readback (nur lokal, nicht im Repo), SHA-Summen. Ab 2026-11-18 von `tools/flash_acdc.py` angelegt, dann mit `flash_report.json` | Unverändert lassen |
| `downloads/` | Externe Abhängigkeiten mit festem Stand: `OpenWareLibraries-9e8f64e.tar.gz` (Quelle und Aufruf in `docs/05-firmware-plan.md`, E5). Nicht im Repo, `tools/setup_repo.sh` lädt die Datei und prüft die SHA-256 | |
| `releases/` | Offizielle Release-Binaries zum Vergleich (`v22.5.0/ACDC.bin`). Kein sicherer Rückweg für acdc1 (USB-Bruch). Nicht im Repo, `tools/setup_repo.sh` lädt die Datei | |
| `itcm-prep/` | Hilfsskripte und Rohliste aus der Vorbereitung von Build 4 (Übergabe vom 2026-11-16, nicht im Repo). Abgelöst durch `tools/check_itcm.py` | Nur zum Nachschlagen |
| `sim/` | Host-Test der Boot-Menü-Logik (`boot_menu_sim.cpp`), Aufruf `tools/sim_boot_menu.sh` | |
| `_work/` | Wegwerf-Quellbäume von `build_acdc.sh`. Der Ordner entsteht beim Bauen, ≈ 130 MB je Build | Darf jederzeit gelöscht werden |

Rückweg für acdc1 auf die Original-Firmware: `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` (SHA-256 `433b3fd3…`).

## Patches

| Patch | Inhalt |
|---|---|
| 01 | GCC 12: Typen der Linker-Symbole |
| 02 | Revert `237c63d` (Durchleitung ohne Rechner) |
| 03 | `USE_USBD_AUDIO_TX_PRE_FX`, Produktstring „OWL-ACDC-FX“ |
| 04 | Ausgangs-Gain 125 |
| 05 | Atomarer RX-Zähler |
| 06 | Feedback-Regelung nach dem Pufferstand |
| 07, 07c, 07d | Eingangs-LEDs zeigen beim Aufnehmen die rohen Eingänge. 07 im Audio-Task und 07c in `onLoop` sind verworfen (Lage). 07d legt den Code in `.late_text`/`.late_bss` |
| 08 | Upstream-Build-Flags für GCC 13+ (`d5b6409a`), mit GCC 12.2 bytegleich. Seit Build 4 in jedem Build |
| 09 | Gemeinsamer `Source/`-Code von v22.5.0. Kandidat, verschiebt die Lage, nie geflasht |
| 10 | Patch 03 für die `hardware.h` von `master`. Nur für `cand-master-oldhal-fx` |
| 11 | Heißer Pfad und Vektortabelle ins ITCM, Anker im Flash (Build 4, fx3i) |
| 11a–11d | Varianten von 11 für die Halbierung: noD, noC, onlyD, novt (Build 4x) |
| 11e, 11f | noD mit `USBD_LL_Transmit` im Anker (fx3j), dazu die RX-Callbacks aus `Codec.o` (fx3k) |
| **11g** | = 11 + RX-Callbacks aus `Codec.o`. Linker-Patch von fx3l |
| 12 | RX-Fix mit Abfrage-Schleife. Verworfen: hebt fs/8 um ≈ 10,6 dB (D42) |
| **12b** | RX-Fix: `audioCallback` aus den RX-DMA-Callbacks |
| 13, 13b | Diagnose-Zähler im USB-Pfad (Build 5, nur für die Fehlersuche) |
| **14** | `USBD_AUDIO_SOF` wertet jede Frame-Nummer nur einmal aus |
| **15** | Boot-Menü: Patch-Slot beim Einschalten wählen, der Slot bleibt gemerkt (Build 6, fx4a) |
| 15b | = 15 mit Abbruch nach 30 s statt 60 s. Vollständiger Ersatz für 15 (fx4b) |
| **16** | MIDI-Sendeweg über USB unteilbar, Lesezeiger erst nach Abschluss der Übertragung, Flusskontrolle beim Slot-Download (Build 7, fx5a) |
| **17** | LED-Modus (normal, nur Clip, aus), im Boot-Menü mit Regler 2 wählbar und in der Ressource `ACDC.led` gemerkt (Build 8, fx6a) |
| **18** | LED-PWM mit 48 000 Hz statt 2320,54 Hz (TIM2/3/4/8: Vorteiler 4, Period 999), fest an den Audio-Takt gekoppelt. Nur `main.c`, `setLed()` und ITCM unverändert (Build 9, fx7a) |
| **19** | Befehls-Cache (I-Cache) an: `USE_ICACHE` ohne `NDEBUG`, DMA-Region der MPU nur mit `USE_DCACHE`. Der D-Cache bleibt aus (Build 10, fx8a, D83) |
| **20** | Daten-Cache (D-Cache) an: `USE_DCACHE` fest, DMA-Region der MPU (0x30000000, 64 KB) auf TEX=1 C=0 B=0 S=0, D-Cache erst nach `MPU_Config()`, `device_cache_invalidate()` erst D-Clean, dann I-Invalidate (Build 11, fx9a, D87) |
| 90, 91 | Füllbytes für Lage-Tests: 90 wie 3c (`fx1p`), 91 hinter dem ITCM-Anker (`…p`-Varianten) |

fx9a = fx8a + **20**. fx8a = fx7a + **19**. fx7a = fx6a + **18**. fx6a = fx5a + **17**. fx5a = fx4b + **16**. fx4b = fx3l + **15b**. fx3l = `db9d3dd` + Libraries `9e8f64e` + 01 02 04 05 06 03 07d 08 **11g 12b 14**. 01, 02, 04, 05, 06 stecken als Commits in `acdc/thru-usb-feedback`, der ganze fx5a-Stand in `acdc/fx1d`. Upstream-Analyse: `docs/research/notes/upstream_master_2026-11-16.md`.

## Builds

| Ordner in `builds/` | Version | Geflasht | Ergebnis |
|---|---|---|---|
| `acdc1-build1b-thru1` | `v22.4.r-thru1` | ja | Durchleitung geht, 6 Block-Slips in 10 min (D11, D12) |
| `acdc1-build1c-thru1` | `v22.4.r-thru1c` | ja | 25 Slips in 30 min (D14–D16) |
| `acdc1-build1d-thru1` | `v22.4.r-thru1d` | ja | 30 min ohne Slips (D17–D20). Rückfall |
| `acdc1-build2-fx1d` | `v22.4.r-fx1d` | ja | Abnahme bestanden, Basislinie B3 (D24–D27). Rückfall |
| `acdc1-build2p-layout` | `v22.4.r-fx1p` | ja | Füllbyte-Test: Die Lage verschiebt die Linien (D33) |
| `acdc1-build3-fx2`, `3b-fx2`, `3c-fx2` | `v22.4.r-fx2`, `fx2b`, `fx2c` | ja | LEDs, verworfen (D28–D32). In `build3-fx2` liegt die erste Fassung von Patch 07 |
| `acdc1-build3d-fx2` | `v22.4.r-fx2d` | ja | **Rückweg** (D34, D36) |
| `acdc1-build3e-fx2e` | `v22.4.r-fx2e` | nein | 3d + 12b ohne ITCM, liegt bereit |
| `acdc1-build4-fx3i` | `v22.4.r-fx3i` | ja | fs/8 −5 dB, Playback gestört (D37, D38) |
| `acdc1-build4p-fx3ip` | `v22.4.r-fx3ip` | nein | Füllvariante von fx3i |
| `acdc1-build4x-noD`, `-noC`, `-onlyD` | `v22.4.r-fx3i-<v>` | ja | Halbierung: zwei getrennte Fehler (D39, D40, D42) |
| `acdc1-build4x-novt` | `v22.4.r-fx3i-novt` | nein | überflüssig |
| `acdc1-build4y-fx3j` | `v22.4.r-fx3j` | ja | Loop sauber, Rauschen schlechter (D41, D42) |
| `acdc1-build4yp-fx3jp` | `v22.4.r-fx3jp` | nein | Füllvariante von fx3j |
| `acdc1-build4z-fx3k` | `v22.4.r-fx3k` | ja | fs/8 −5,8, Kamm +3,5 dB (D43, D44) |
| `acdc1-build4zp-fx3kp` | `v22.4.r-fx3kp` | nein | Füllvariante von fx3k |
| `acdc1-build5-diag-itcm`, `-diag-flash` | `v22.4.r-dg5i`, `dg5f` | ja | Diagnose-Zähler (D45) |
| `acdc1-build5b-diag-itcm` | `v22.4.r-dg5i2` | ja | SOF-Kette läuft doppelt (D46) |
| `acdc1-build5b-diag-flash` | `v22.4.r-dg5f2` | nein | Kontrolle zu dg5i2 |
| **`acdc1-build5c-fx3l`** | **`v22.4.r-fx3l`** | ja | **läuft auf acdc1** (D47–D49) |
| `acdc1-build5cp-fx3lp` | `v22.4.r-fx3lp` | ja | Füllvariante: lagenunabhängig (D48) |
| `acdc1-build6-fx4a` | `v22.4.r-fx4a` | ja | fx3l + 15 (Boot-Menü). `check_itcm` und Host-Test bestanden (D50), geflasht (D51), Menü läuft (D52). Loop-Test und Rausch-A/B offen |
| **`acdc1-build6b-fx4b`** | **`v22.4.r-fx4b`** | ja | fx3l + 15b (Abbruch nach 30 s). ITCM-Inhalt bytegleich mit fx4a (D53). Alltags-Firmware 2026-11-17 bis 18 (D55, D59). Loop-Test bestanden (D57), Rauschen = fx3l (D58) |
| **`acdc1-build7-fx5a`** | **`v22.4.r-fx5a`** | ja | fx4b + 16 (MIDI-Sendeweg). `check_itcm` bestanden (D62). Alltags-Firmware 2026-11-18 bis 19 (D63, D65). Download-Stresstest 240/240, Loop-Test bestanden (D63), Rauschen ohne Hinweis auf eine Änderung (D64) |
| **`acdc1-build8-fx6a`** | **`v22.4.r-fx6a`** | ja | fx5a + 17 (LED-Modus). Host-Tests und `check_itcm` bestanden, ITCM-Ende und alle Funktionen außerhalb von `.text.onLoop` wie fx5a. Abnahme vollständig (D75–D77), Rückweg von fx7a |
| **`acdc1-build9-fx7a`** | **`v22.4.r-fx7a`** | ja | fx6a + 18 (LED-PWM 48 kHz). `check_itcm --same-itcm fx6a` bestanden: ITCM bytegleich, alle Adressen gleich, 113 Bytes Unterschied nur im Timer-Init und im Versions-String. Host-Tests und Offline-Prüfung bestanden. Alltags-Firmware 2026-11-19 bis 23, Rückweg von fx8a. Abnahme vollständig (D78, D79): LED-Linie weg, Rauschen = fx6a, Loop-Test bestanden |
| `acdc1-build10-fx8a` | `v22.4.r-fx8a` | nein | fx7a + 19 (I-Cache an, D83). `check_itcm --same-itcm fx7a` bestanden: ITCM bytegleich, Flash-Funktionen teils um 0x78 verschoben. Offline-Prüfung bestanden. **Seit 2026-11-23 auf acdc1** (D84): Cache-Bits 2, Plateau 35 % statt 51 %, Patch-Wechsel, Downloads 240/240 und Loop-Test bestanden, fs/8 +0,6 dB gegen fx7a (D85). Abnahme vollständig. Alltags-Firmware am 2026-11-23, **Rückweg von fx9a** |
| `acdc1-build11-fx9a` | `v22.4.r-fx9a` | ja | fx8a + 20 (D-Cache an, D87). 110 520 B (+312 B). `check_itcm --same-itcm fx8a` bestanden: ITCM bytegleich, alle 180 RAM-Objekte an derselben Adresse, Flash-Funktionen teils um 0x138 verschoben. Disassembly von `MPU_Config`, `main()` und `device_cache_invalidate` wie geplant, Offline-Prüfung bestanden. **Seit 2026-11-23 auf acdc1** (D88, D89): Abnahme vollständig, Plateau 29 % statt 35 %, fs/8 −0,7 dB gegen fx8a. **Alltags-Firmware auf acdc1** (2026-11-23) |
| `cand-r-fx2d-gcc13flags` | `v22.4.r-fx2d` | nein | 3d + 08, bytegleich mit 3d |
| `cand-r-merge2250-fx2d` | `v22.4.r-fx2d-m` | nein | 3d-Stand mit Patch 09 |
| `cand-master-oldhal-fx` | `v22.5.0-oldhal-fx` | nein | `master` `36eaf1c4` + altes HAL + 10. Zeigt nur, dass es baut |
| `verify-fx1d-5cb2c17c` | `v22.4.r-fx3l` | nein | Build aus dem Fork-Branch, bytegleich mit fx3l |
| `verify-fx1d-2c963e3a` | `v22.4.r-fx4b` | nein | Build aus dem Fork-Branch, bytegleich mit fx4b (D59) |
| `verify-fx1d-c222fa49` | `v22.4.r-fx5a` | nein | Build aus dem Fork-Branch, bytegleich mit fx5a (D65) |
| `verify-fx1d-34782dea` | `v22.4.r-fx6a` | nein | Build aus dem Fork-Branch, bytegleich mit fx6a (2026-11-19) |
| `verify-fx1d-351b2071` | `v22.4.r-fx7a` | nein | Build aus dem Fork-Branch, bytegleich mit fx7a (2026-11-19) |
| `verify-fx1d-f9f9399a` | `v22.4.r-fx8a` | nein | Build aus dem Fork-Branch, bytegleich mit fx8a (2026-11-23) |
