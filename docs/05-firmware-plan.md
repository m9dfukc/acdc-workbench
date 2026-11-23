# 05 – Firmware: Stand, Forks, Build-Plan

> **Stand 2026-11-23:** Auf acdc1 läuft **Build 10 `v22.4.r-fx8a`** (`e1b1097b…`, Abschnitt „Build 10“, messlog D83–D85, I-Cache an) als Alltags-Firmware (Entscheidung des Nutzers). Rückweg ist Build 9 `v22.4.r-fx7a` (`cac6fee0…`), dann Build 8 `v22.4.r-fx6a` (`6a3fc427…`), dann Build 7 `v22.4.r-fx5a` (`b69c25b3…`), Build 6b `v22.4.r-fx4b` (`a21f35c9…`), Build 5c `v22.4.r-fx3l` (`b55b94d8…`), danach Build 3d (`d212cf8d…`).
>
> Dieses Dokument ist chronologisch gewachsen. „Läuft auf acdc1“, „nicht abgestimmt“ und „nächste Schritte“ in den Abschnitten zu Build 1 bis 4z beschreiben den Stand des jeweiligen Abschnitts. Was heute offen ist, steht in `TODO.md`.

## Upstream-Stand [belegt]

- `RebelTechnology/OpenWare`: `develop` = `62a0187` „v22.5.0“, **2023-03-05**, das ist der letzte Firmware-Stand. Letzter Commit unter `ACDC/`: `dd7f7fe` (2022-06-19).
- **Nachtrag 2026-11-16:** `master` steht seit 2026-11-15 auf `36eaf1c4` (PR #89, Build-Flags für GCC 13+, CI auf GCC 14.3). Die 4 neuen Commits ändern nur die Build-Kette, keinen Firmware-Code. Übernommen ist `d5b6409a` als Patch 08. Details: `docs/research/notes/upstream_master_2026-11-16.md`.
- Spätere Branches: `feature/oneiroi` (bis 2025-06, Befaco Oneiroi), `feature/witch3` (2023-10). Keiner davon betrifft das AC/DC.
- Issue-Tracker: 88 Einträge, **kein** AC/DC-Issue von Nutzern, 0 Treffer für „noise“. Offener PR #81 (antisvin): Settings-Speichern aus der USB-ISR kann hängen bleiben.
- Das offizielle `ACDC.bin` v22.5.0 hat laut antisvin **USB kaputtgemacht**. Ein Selbstbau mit passendem `Libraries`-Submodul ging (Thread #2083).
- Juni 2026: Auf manchen Xibeca-Boards fällt USB-Audio nach einer Weile aus (Thread #3725).
- Faktisch ist das Modul verwaist. Firmware-Updates für das AC/DC sind von Rebel nicht zu erwarten.

## Was in Forks und Branches relevant ist

| Quelle | Inhalt | Nutzen |
|---|---|---|
| **shmuga/OpenWare `lich3-usb-fixes`** (2026-10-18) | `d8fdfa3`: Auf H7 legt ein unvollständiger isochroner IN-Transfer den TX-Endpoint **dauerhaft still**, der Host hört nur noch Stille (die H7-HAL verhält sich anders als die F4-HAL). `c5aff8c`: Die TX-Ratenregelung schätzt den Füllstand falsch, was **Klick-Bursts alle paar Sekunden** erzeugt. `d39aa53`: Crash durch `__builtin_clz(0)` mit GCC 12. `9104f1a`: 3 → 5 Puffer-Pakete (Lich3) | Backport-Kandidat für **Option A** (v22.5.0-Linie, E1). Das AC/DC nutzt in v22.5.0 dasselbe `Source/usbd_audio.cpp` mit TX auf H7 und hat ebenfalls 3 Pakete. Der Hack-Branch hat einen eigenen USB-Pfad. Auf dem AC/DC ungetestet |
| **burstMembrane/OpenWare `20d322d`** (2026-03-31) | Einziger Fork mit ACDC-Änderung: beide `*_PRE_FX`-Defines, Produktstring „LIAM-ACDC“, `Libraries`-Submodul auf `5a3f964` („fix usb device enumeration“) | Präzedenzfall. `5a3f964` = altes H7-HAL vor dem Upgrade (siehe „Libraries-Stände“), Vorlage für Option A |
| Upstream `hack/acdc-output-levels` (`7f3cc41`, 2022) | Martin Klangs ungemergte Experimente: exakte 48 kHz (MCLK 12,288 MHz), Codec Auto-Rate, **SAI-OutputDrive aus** (`65fc0db`), **nur 4 TDM-Slots** (`cf8eaf9`), Input-Gain 88, Blocksize 8, 4 Puffer-Pakete, Pegel-LEDs | **Basis aller eigenen Builds** (E1, seit D10 der Stand `db9d3dd` = v22.4.r statt der Spitze), nur ohne `237c63d`: Der mutet den DAC ohne USB-Stream, das Gegenteil von Standalone. Ein Build aus diesem Branch lief ab Werk (etikettiert „v22.5.0“) auf acdc1, v22.4.q läuft auf acdc2 |
| Upstream `feature/acdc-lowspeed` (`237f746`) | CPU auf 240 MHz, SAI retuned. FRACN-Werte inkonsistent (`.ioc` 280 vs. `main.c` 6144) | nicht ungeprüft bauen |
| hirnlego, XponentOneAudio, antisvin/OpenWare_Owlsy | Oneiroi-Storage-Fixes, Lich-Patches, Daisy-Port | nichts für das AC/DC (Stand 2026-11-14 geprüft) |
| **burstMembrane/acdc-patches** (`78ffa22`, 2026-04-02) | Fertige AC/DC-FX-Patches (Dattorro-Reverb, Tape-Delay, Grain, Rings-Reverb) + Helfer `ACDC.h` (Audio L/R = Kanal 1/2, CV = 3/4, LED-Metering), passend zur PRE_FX-Firmware `20d322d` | Vorlage für Phase 4 (Standalone-FX) [belegt: Repo] |
| **shmuga/lich-patcher** (2026-10-18, https://lich.markorel.ninja/) | Browser-Tool, allgemeines OWL-SysEx: Slots/Ressourcen **vom Gerät herunterladen**, **Settings auslesen**, Geräte-Info | Backup von acdc1/acdc2 vor jedem Eingriff, Settings prüfen (nur Lesen, kein Erase/Store) |

Keine Quelle adressiert das analoge Rauschen, den PCM3168A-Treiber oder die LED-PWM.

## Befund 2026-11-14: Durchleitung ohne Rechner fehlt auf beiden Geräten

- acdc2 (v22.4.q) enthält `237c63d` (Nullen an den DAC ohne USB-Playback) [Code].
- acdc1 („v22.5.0“) leitet im Kaltstart ebenfalls nicht durch [gemessen]. Ursache laut D3: Auf acdc1 läuft ein Build aus `hack/acdc-output-levels` mit dem Etikett „v22.5.0“, nicht die Release-`ACDC.bin` [gemessen: Readback + String-Fingerabdruck, `messlog.md` D1–D3]. Der Hack-Branch enthält `237c63d`.
- Folge: Standalone-FX gibt es nur mit eigener Firmware.
- Der Quellcode liegt dauerhaft unter `firmware/OpenWare` (ein Klon mit Remotes `upstream` und `fork`, alle Branches als `upstream/*`). Im Sandbox sind Git-Schreibzugriffe dort gesperrt (`.git/config`), Klonen und Fetchen brauchen eine Freigabe. Das Submodul `Libraries` ist dort **nicht** ausgecheckt.

## Fakten für den eigenen Build (2026-11-14)

### `Libraries`-Stände (pingdynasty/OpenWareLibraries) [belegt: Repo + GitHub-Compare-API]

| Stand | Datum | Inhalt | Wer nutzt ihn |
|---|---|---|---|
| `5a3f964` | 2022-03-24 | OpenWare-Commit `ad6422f2` „revert libs to prevent USB issues“ (vorher schon `2185efd2` „latest libs“) | burstMembrane `20d322d` |
| `9e8f64e` | 2022-03-25 | = `5a3f964` + 1 Commit „apply NAK fix to H7 drivers“, nur `stm32h7xx_hal_hcd.c` (+8). Betrifft nur USB-**Host**, für das AC/DC als USB-Gerät praktisch gleich [Code] | OpenWare `05dc03e0` „patched library“. Ab da alle v22.4.x, alle v22.5.rc* und `hack/acdc-output-levels` |
| `8a07845` | 2023-01-29 | Upgrade auf **STM32H7-HAL v1.11.0**, CMSIS 5.1.0, Middlewares, USB-Host-Fixes (300 Dateien) | OpenWare `8c569c0e` „Updated H7 libs“, 2023-03-05, Release-Tag |
| `e102c6f` | 2023-03-05 | = `8a07845` + CMSIS F4-Header | v22.5.0 `62a0187` |

- Der USB-Bruch der Release-`ACDC.bin` (antisvin, Thread 2083 #4) fällt zeitlich genau mit dem HAL-Upgrade `8a07845`/`e102c6f` zusammen [Hypothese, stark]. Passend dazu `3237e7ca` (2023-01-29): Build-Flags in `Hardware/owl3.mk` an das neue HAL angepasst. Ein v22.5.0-Build mit altem HAL braucht womöglich den Rückbau dieses Commits [Hypothese]. **Nachtrag 2026-11-16:** Für das AC/DC nicht nötig, es baut mit `xibeca.mk` statt `owl3.mk` [Code]. `master` + altes HAL `9e8f64e` baut und linkt ohne Rückbau (`cand-master-oldhal-fx`) [gemessen: Build].
- Die Firmware auf acdc1 (Hack-Branch) läuft also mit dem **alten HAL** `9e8f64e`, und ihr USB funktioniert [gemessen: Betrieb seit Monaten, Serie 2].

### Hack-Branch vs. v22.5.0 [Code]

- Basis: `hack/acdc-output-levels` zweigt bei `dd7f7fe` ab und hat bis 2022-06-19 mehrfach `develop` gemergt. Spitze `7f3cc41` „v22.4.s: MCLK=256fs no master div“ (2022-07-15). `Source/device.h`: `FIRMWARE_VERSION "v22.4.s"`.
- Nur im Hack-Branch: umgebauter USB-Audio-Pfad (SOF-Sync, Feedback-Berechnung, `CircularBuffer`, Puffer-Init auf Frame-Grenze, einheitliches `usbd_audio_error()`), Blockgröße 8, Input-Gain 88, MCLK 256fs/exakte 48 kHz (`bc7391cd`, `e219182a`, `7f3cc41`), SAI-OutputDrive aus (`65fc0db`), 4 TDM-Slots (`cf8eaf9`), Pegel-LEDs, `codec_highpass()`, **`237c63d`**.
- Nur in v22.5.0 (56 Commits): Lich3/Magus3/Witch3, USB-Host, Watchdog, Settings im nicht gemappten Flash, „Ensure valid DAC value range“, HAL-Upgrade. Für das AC/DC fast alles ohne Belang.
- `237c63d` ist in `usbd_rx_convert()` ein `else`-Zweig mit `memset(dst, 0, …)` unter `#ifdef OWL_ACDC`: ohne aktiven RX-Stream Nullen auf den Puffer. Der Revert ist trivial.
- `USE_USBD_AUDIO_TX_PRE_FX` / `_RX_PRE_FX` sind in beiden Ständen gleich implementiert (`Source/ProgramManager.cpp`): POST_FX konvertiert `pv->audio_output`, PRE_FX `pv->audio_input`.
- Welcher Stand auf acdc1 läuft: **kein veröffentlichter Commit** (Reproduktions-Build, `messlog.md` D3a). `ProgramManager.cpp` mit `237c63d` stammt aus dem Hack-Branch [gemessen: Disassembly], `usbd_audio.cpp` passt zu keinem Hack-Commit. Wahrscheinlich ein selbst zusammengesetzter Stand, gebaut mit GCC < 12 [Hypothese, stark]. Welche MCLK-Konfiguration er nutzt, bleibt offen. Dass acdc1 nahezu exakt 48 kHz hat, spricht für ≥ v22.4.r [Hypothese].

### Settings [Code]

- `ApplicationSettings` ist in beiden Ständen gleich aufgebaut. Die Prüfsumme ist `sizeof(*this) ^ 0xf0f0f0f0`. Ein vorhandenes `__SETTINGS__` würde also von jedem neuen Build **übernommen**.
- Auf acdc1 gibt es wahrscheinlich kein `__SETTINGS__` [Hypothese]: Die gemeldete Belegung von 31 232 B ist genau Slot 1 (10 164 B) + Slot 2 (20 724 B), jeweils mit 32-B-Header und auf 256 B aufgerundet. Allerdings zählt `getUsedSize()` nur Ressourcen mit `FLASH_DEFAULT_FLAGS`, also kein Beweis. Blockgröße 8 ist ohnehin die Vorgabe im Hack-Branch.

### Toolchain und Größe

- Upstream-CI (`.github/workflows/c-cpp.yml`, v22.5.0): `carlosperate/arm-none-eabi-gcc-action`, Arm GNU **12.2.Rel1** [belegt: Repo]. Installiert seit 2026-11-14 unter `/Applications/ArmGNUToolchain/12.2.rel1/`.
- Größen: acdc1-Readback 106 608 B, Release 109 080 B, Grenze 131 072 B (128 KB internes Flash laut Build-Config).

## Abgestimmter Plan (Grill-Runde 2026-11-14)

Entschieden mit dem Nutzer in zwei Fragerunden. **Kein Build und kein Flash ohne ausdrückliche Freigabe im Chat, jeder Flash einzeln. acdc2 bleibt unangetastet.**

### E1 – Basis: Hack-Spitze statt v22.5.0

- **Build 1 = `7f3cc41` (v22.4.s, Spitze `hack/acdc-output-levels`) + Libraries `9e8f64e`, nur `237c63d` zurückgenommen.**
- Begründung: Das liegt am nächsten an dem Stand, der auf acdc1 heute mit funktionierendem USB läuft (altes HAL, Hack-USB-Pfad). Damit ist das USB-Risiko am kleinsten, und die Durchleitung lässt sich isoliert testen.
- Bewusst die **Spitze** und nicht der Commit, der dem Readback am nächsten kommt (Nutzerentscheidung). Der Reproduktions-Build hat ohnehin gezeigt, dass es keinen solchen Commit gibt (D3a). Build 1 unterscheidet sich von acdc1 also in mehr als dem Revert: USB-Fehlerpfade in `usbd_audio.cpp`, Compiler, eventuell MCLK. Abweichungen in A5/A6 dann zuerst diesen Unterschieden zuordnen.
- v22.5.0 mit Release-Libraries `e102c6f` scheidet aus (USB-Bruch).
- **Nachtrag (D10, 2026-11-14):** Build 1 auf der Spitze `7f3cc41` gibt auf acdc1 kein Audio (Takt und Codec-Einstellung von v22.4.s). Alle späteren Builds stehen deshalb auf **`db9d3dd` (v22.4.r)**. Das ist auch die Takt-Einstellung der Werks-Firmware von acdc1 [gemessen: Disassembly].
- **Option A (bleibt für später auf dem Plan, Nutzer 2026-11-16: Merge mit v22.5.0 bzw. dem aktuellen Upstream-`master` samt Fixes):** v22.5.0 + Libraries `9e8f64e`/`5a3f964` (wie burstMembrane), **plus die shmuga-USB-Fixes** (`d8fdfa3`, `c5aff8c`, `d39aa53`, 5 Puffer-Pakete aus `9104f1a`), mit `TX_PRE_FX`. Die shmuga-Fixes gehören zu dieser Linie, weil sie gegen den v22.5.0/Lich3-USB-Code geschrieben sind. Der Hack-Branch hat einen eigenen umgebauten USB-Pfad, dort wären sie eine Portierung, kein Cherry-Pick.
  - Der früher genannte Rückbau von `3237e7ca` entfällt: Der Commit ändert `owl3.mk`, das AC/DC baut mit `xibeca.mk` [Code].
  - Laut Upstream-Analyse (`docs/research/notes/upstream_master_2026-11-16.md`) ist der Wechsel eine Portierung: Takt von v22.4.r, Patches 04/05/06/07d und die ITCM-Patches müssten auf den USB-Pfad von v22.5.0 übertragen und neu abgenommen werden. Vorarbeit: Patches 09 und 10, Kandidaten `cand-r-merge2250-fx2d` und `cand-master-oldhal-fx` (gebaut, nicht geflasht).

### E2 – Routing in zwei Stufen

| Build | Änderung gegenüber der Hack-Spitze | Ohne Rechner | Mit Rechner: Aufnahme | Mit Rechner: Playback |
|---|---|---|---|---|
| **1** `v22.4.s-thru1` | nur Revert `237c63d` | Patch → Buchsen | Patch-Ausgang (wie bisher, digitaler Gain drin, vergleichbar mit M/S2) | überschreibt die Ausgänge, solange der RX-Stream läuft |
| **2** `v22.4.s-fx1` | + `USE_USBD_AUDIO_TX_PRE_FX`, Produktstring „OWL-ACDC-FX“ | Patch → Buchsen | **rohe ADC-Daten**, ohne Patch und ohne digitalen Gain | wie Build 1 |

- Beide PRE_FX (burstMembrane) verworfen: Mit `RX_PRE_FX` überschreibt das Playback den Patch-**Eingang**, die Eingangsbuchsen wären bei laufendem Playback weg [Code].
- Offen [Hypothese]: Hält macOS den Ausgangsstream offen, solange das AC/DC als Ausgabegerät gewählt ist, sind die Ausgänge in dieser Zeit stumm (Host-Stille überschreibt den Patch). RX stoppt laut Code erst bei SetInterface Alt 0 oder USB-DeInit. Wird in A4 beobachtet.
- Auto-Switching zur Laufzeit (Routing an `usbd_rx != NULL` bzw. am Pegel festmachen) erst nach Option A.

### E3 – Was vom Hack-Branch bleibt

In Build 1 und 2 bleibt alles so, wie es auf acdc1 heute läuft: Blockgröße 8, Input-Gain 88, Output-Gain 114, MCLK/exakte 48 kHz, OutputDrive aus, 4 TDM-Slots, 3 Puffer-Pakete, Pegel-LEDs, Codec-HPF aus. So bleibt jeder Schritt eine einzige Variable.

Spätere Rausch-Experimente, jeweils als eigener Build mit A/B-Messung gegen die Build-2-Basislinie:
1. Blockgröße 16 → Die 6-kHz-Linie (fs/8) sollte nach 3 kHz (fs/16) wandern, und die Mischprodukte sollten sich ändern.
2. LED-PWM aus dem Audioband (Prescaler 100 → 0, ≈ 234 kHz) → H3.
3. Codec-HPF an (`CODEC_HP_FILTER`).

Die Reihenfolge legen wir nach Build 2 fest.

### E4 – Settings

Nie schreiben, nie zurücksetzen (kein SysEx `0x15`, kein Store). Vor und nach jedem Flash mit `tools/owl_read.py` auslesen: Version, `SR/BS/CH`, Slot-Namen und -CRC, Storage. Bei Abweichungen erst Rückfrage.

### E5 – Toolchain und Build-Baum

- Arm GNU Toolchain **12.2.Rel1**, wie Upstream-CI. Die Installation (Arm-Tarball oder Paketmanager) macht der Nutzer. Die Version kommt in jedes Build-Log.
- Kein Build im Klon `firmware/OpenWare`, weil Git-Schreibzugriffe gesperrt sind und der Klon sauber bleiben soll. Stattdessen:
  - `git archive <commit>` nach `firmware/_work/<name>/`
  - Libraries als GitHub-Tarball des festen Commits (`codeload.github.com/pingdynasty/OpenWareLibraries/tar.gz/9e8f64e…`) nach `firmware/_work/<name>/Libraries/`
  - eigene Änderungen nur als `firmware/patches/NN-<name>.patch` (`01-gcc12-extern-uint8`, Revert `237c63d`, später `TX_PRE_FX` + Produktstring). Den Versionsstring setzt `FW_VERSION=…` im Skript.
  - `.git*`-Dateien werden beim Entpacken ausgelassen, weil der Sandbox `.gitmodules` sperrt und der Build sie nicht braucht.
- `tools/build_acdc.sh <commit> <libraries> <patch…>`: Baum aufbauen, Patches anwenden, `make` für ACDC, `arm-none-eabi-size` gegen 131 072 B prüfen. Dann `.bin`/`.elf` mit SHA-256, Toolchain-Version und Patchliste nach `firmware/builds/<name>/` schreiben.
- **Vorab der Reproduktions-Build:** Hack-Spitze unverändert, nur der Versionsstring auf „v22.5.0“ gesetzt, Vergleich mit dem Readback. Erledigt 2026-11-14, Ergebnis siehe unten. Wird nicht geflasht.
- Der `__builtin_clz(0)`-Fall (shmuga `d39aa53`) betrifft Code aus v22.5.0/Lich3. Für die Hack-Basis wird er nur nachgezogen, wenn er dort auftritt.

#### Ergebnis Reproduktions-Build (2026-11-14)

- Toolchain und Skript funktionieren. Die Hack-Quellen brauchen für GCC 12 den Patch `01-gcc12-extern-uint8.patch`: Upstream `5108fc56` + `fe6eff4f`, ändert nur die Typen von Linker-Symbolen (`extern char` → `uint8_t`). Ohne ihn bricht GCC 12 mit „conflicting declaration '_PATCHRAM'“ ab. `develop` ab v22.5.rc2 enthält den Fix schon.
- **Builds sind deterministisch [gemessen]:** zwei Läufe für `7f3cc41` (einmal mit Versions-Patch, einmal mit `FW_VERSION`) ergeben denselben SHA-256.
- Ablage `firmware/builds/archive/repro-*/` (`ACDC.bin`/`.elf`/`.map`, `BUILD_INFO.txt`, `build.log`), alle mit `FW_VERSION=v22.5.0`, **nicht zum Flashen**:

| Build | Commit | Größe B | SHA-256 (Anfang) |
|---|---|---|---|
| `repro-7f3cc41` | Hack v22.4.s | 105 664 | `910f71e3…` |
| `repro-db9d3dd` | Hack v22.4.r | 105 664 | `1fce4352…` |
| `repro-e81cfc3` | Hack v22.4.q (= acdc2-Quelle) | 105 632 | `cb1c2d0e…` |
| `repro-961b49f` | Hack-Merge 2022-06-19 (v22.4.m) | 104 296 | `924bc72b…` |
| `repro-c79cf7a` | `develop` v22.5.rc5, ohne GCC-Patch | 104 288 | `f1d3026c…` |
| Readback acdc1 | ? | 106 608 | `433b3fd3…` (128-KB-Abbild) |

- Kein Kandidat passt zum Readback. Die Firmware auf acdc1 ist kein veröffentlichter Commit, `237c63d` ist darin per Disassembly belegt (`messlog.md` D3a). Der Plan E1 (Hack-Spitze + Revert) bleibt.

#### Build 1 und Build 2 gebaut (2026-11-14, nicht geflasht)

Gebaut mit `tools/build_acdc.sh`, Basis `7f3cc41` + Libraries `9e8f64e`, Arm GNU 12.2.Rel1. Ablage heute: `firmware/builds/archive/acdc1-build{1-thru1,2-fx1}/`. Die Quellbäume sind gelöscht, ein Neubau ist bitgleich reproduzierbar.

| Build | `FW_VERSION` | Patches | Größe B | SHA-256 `ACDC.bin` |
|---|---|---|---|---|
| `acdc1-build1-thru1` | `v22.4.s-thru1` | 01, 02 | 105 656 | `97a876b45512e23cbc019e721601bb70de38fb9e056b72b0928f1a0c12c4f332` |
| `acdc1-build2-fx1` | `v22.4.s-fx1` | 01, 02, 03 | 105 656 | `3a6e5df63751f32ee821b3cbda8705519f6e11667ffde708fb27b24ceda18289` |

Patches in `firmware/patches/`:
- `01-gcc12-extern-uint8.patch`: GCC-12-Kompatibilität, nur Typen
- `02-revert-237c63d-thru-mute.patch`: entfernt den `else`-Zweig mit `memset` in `usbd_rx_convert()`
- `03-tx-pre-fx-owl-acdc-fx.patch`: `USE_USBD_AUDIO_TX_PRE_FX`, Produktstring „OWL-ACDC-FX“

Geprüft im Binary [Code: Disassembly der ELFs]:
- **Build 1:** `usbd_rx_convert()` enthält nur noch einen `memset` (Unterlauf-Auffüllung), der Tail-Call `memset(dst,0,…)` für `usbd_rx == NULL` ist weg. In der Repro-Spitze sind es 2. `onProgramReady` ruft `tx_convert` und `rx_convert` am Anfang auf `audio_output` auf, also POST_FX wie bisher. Strings: „OWL-ACDC“, „AC/DC v22.4.s-thru1“.
- **Build 2:** wie Build 1, aber `tx_convert` wird erst am Ende von `onProgramReady` als Tail-Call aufgerufen, auf `audio_input` vor dem nächsten Patch-Block (PRE_FX). `rx_convert` bleibt POST_FX. Strings: „OWL-ACDC-FX“, „AC/DC v22.4.s-fx1“.
- Vektortabelle wie beim Readback (SP `0x00001000`), Größe deutlich unter 131 072 B.

Nächste Schritte vor dem ersten Flash (E7): Boot-Pad-Probe, 10-min-Referenzaufnahme, Generalprobe. Alles nur mit Freigabe. **Stand 2026-11-14: alle drei erledigt** (Messlog D4, D5, D6/D7).

### E6 – Kennung

- Versionsstring: Build 1 `v22.4.s-thru1`, Build 2 `v22.4.s-fx1`. Nie wieder „v22.5.0“ auf einem eigenen Build.
- USB-Produktstring: Build 1 bleibt „OWL-ACDC“, damit `owl_read.py`, Audio-Software und macOS unverändert weiterlaufen. Build 2 heißt „OWL-ACDC-FX“, der Gerätename im System zeigt dann das Routing.
- **Nachtrag 2026-11-15:**
  - Build 2 heißt jetzt `v22.4.r-fx1d` (Basis 1d, siehe „Build 2 neu“).
  - `owl_read.py` findet „OWL-ACDC-FX“ schon heute, weil `--port` per Teilstring sucht.
  - Audio-Software am Rechner muss das Gerät neu auswählen.

### E7 – Flash-Weg, Vorbedingungen, Rückweg

- Weg: ROM-DFU über die **vordere USB-B-Buchse**. Einstieg mit `tools/owl_read.py --reset-to-dfu --yes`, dann `dfu-util -a 0 -s 0x08000000:leave -D <bin>`. Den genauen Befehl prüfen wir vor dem ersten Schreiben. **Nachtrag:** Geflasht wird seit D5 **ohne** `:leave`, mit Readback und Vergleich danach (Ablauf in `CLAUDE.md`). Seit 2026-11-19 (D79) startet ein zweites, nur lesendes Readback mit `:leave` die Firmware, Standard in `tools/flash_acdc.py`. Kaltstart von Hand (Case aus **und** USB ab, dann Case an, dann USB an, D3) nur noch mit `--cold`.
- **Vorbedingungen vor dem ersten Schreibvorgang**, in dieser Reihenfolge:
  1. **Boot-Pad-Probe:** DFU-Einstieg über die Boot-Pads auf dem Xibeca-Board, nur `dfu-util -l`, nichts schreiben. Das ist der Notweg, falls USB in einem neuen Build tot ist. **Ohne erfolgreiche Probe wird nicht geflasht.**
  2. **Referenzaufnahme:** 10 min mit der heutigen Firmware, Aufbau wie A6, als Vergleich für Klicks und Ausfälle. Aufnahme in der Host-Software, Engine 48 kHz (kein Hochrechnen), schlanker Patch, AC/DC-Eingang nicht auf den Ausgang gepatcht. Derselbe Patch später für A6. (2026-11-14 von 30 auf 10 min gekürzt: Grobe USB-Fehler wie ein kaputter Feedback-Endpoint zeigen sich bei ≈ 190 ppm Taktabstand in Sekunden. Bei 0 Klicks in 10 min liegt die Rate mit 95 % unter ≈ 1 je 3 min. Ist Build 1 auffällig, gezielt länger aufnehmen.)
  3. **Generalprobe Rückweg:** das Readback-Abbild `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` (identischer Inhalt) flashen, zurücklesen, SHA-256 vergleichen (`433b3fd3…`), Kaltstart, `owl_read.py`. Das testet `-D`, Adresse, Länge und Neustart, ohne den Zustand zu ändern. Ein abgebrochener Schreibvorgang kann den ROM-DFU nicht beschädigen.
- **Programmer:** entfällt (Nutzer 2026-11-16). DFU per SysEx und die Boot-Pads reichen als Wege (D4, D5). Flashen und Debuggen über SWD mit einem ST-Link bleibt möglich, siehe „Flashen – allgemeine Hinweise“.
- **Rückfall auf das Readback-Abbild**, sobald einer dieser Fälle eintritt:
  - USB enumeriert nicht stabil
  - Audio-Ausfälle, oder mehr Klicks als in der Referenzaufnahme
  - Rauschen mehr als 1 dB schlechter als S2 bzw. die Referenz (Ausnahme nach E1: zuerst den MCLK-Unterschied prüfen)
  - Settings oder Storage verändert
- Zwischen Build 1 und Build 2 wird nicht zurückgeflasht, Build 2 geht direkt über Build 1.
- Jeder geflashte Build bleibt mit SHA-256 in `firmware/builds/` liegen.

### Abnahmetests

Jeder Schritt kommt als eigener Abschnitt in `docs/messlog.md` (D4 ff.), Aufnahmen werden in `recordings/manifest.toml` eingetragen.

**Build 1 (`v22.4.s-thru1`)**, in dieser Reihenfolge:
- **A1:** `owl_read.py` meldet `AC/DC v22.4.s-thru1`, `SR/BS/CH 48000 8 4`, Slot 1 „ACDC“ (CRC `0xbeb3bb2e`), Slot 2 `[Lich]`, Storage 31 232 B.
- **A2:** Kaltstart ohne USB, DPO → In 1…4 nacheinander → Out 1…4 hörbar (Default-Patch-VCA, Knob 12 Uhr ≈ ×1).
- **A3:** USB gesteckt, keine Audio-App: weiter hörbar.
- **A4:** Host-Playback → Ausgänge. Danach Playback stoppen bzw. Gerät abwählen: Die Durchleitung kommt zurück. Bleibt macOS im Stream und sind die Ausgänge stumm, als Verhalten notieren, nicht als Fehler.
- **A5:** USB-Aufnahme offene Eingänge wie S2 (acdc1, Hub, Gain 12 Uhr, 120 s). Kamm f0, 6-kHz-Linie, LED-Linie und Rauschen ≥ 20 Hz innerhalb ±1 dB von S2.
- **A6:** Langzeittest 10 min wie D7: Kabel Out n → In n, Sinus 440 / 530 / 670 / 790 Hz aus der Host-Software (gespeicherter Patch, gleiche Pegel), Aufnahme aller 4 Eingänge. `tools/phase_slips.py` und Klick-Detektor: 0 Phasensprünge, 0 Klicks, Kanalzuordnung wie D7 (Referenz `E7-ref-loop`). Ergänzend offene Eingänge wie D6 (`E7-ref`) für den Rauschvergleich.
- **A7:** Danach **S3** messen (Kamm an den Ausgängen mit USB ab, gesteckt und streamend, Aufbau `docs/03`).

**Build 2 (`v22.4.s-fx1`)**: A1–A6 sinngemäß, dazu:
- **B1:** macOS zeigt „OWL-ACDC-FX“, `owl_read.py` findet den Port.
- **B2:** Der Gain-Knob ändert die USB-Aufnahme nicht mehr, nur den Ausgang. Gain 0 → Ausgang stumm, die USB-Aufnahme hat weiter Signal (Umkehrung von Serie 2).
- **B3:** Rauschmessung an den rohen Eingängen = neue Basislinie für alle Rausch-Experimente (E3).

### Build 1d – Feedback mit Pufferstand-Regelung (Entwurf 2026-11-14, nicht gebaut)

**Anlass:** Build 1b und 1c verlieren über USB alle ≈ 2–3 min einen Block à 8 Frames (messlog D12, D16). Der Grund ist eine Netto-Drift von 1,15–1,7 ppm, also etwa 1 LSB des Feedback-Werts. Das Feedback misst bisher nur den Verbrauch und regelt nicht nach dem Pufferstand (offene Schleife). Der atomare Zähler (Patch 05) hilft nicht (D16).

**Basis:** Build 1c = `db9d3dd` + 01, 02, 04, 05. Neu ist `firmware/patches/06-fb-level-control.patch`, der nur `Source/usbd_audio.cpp` ändert. Patch 05 bleibt drin, er ist harmlos und schließt die Race in jedem Fall. Die Patches 01–06 sind auf `db9d3dd` per `patch` getestet, kompiliert ist noch nichts.

**Regelung [Code, nicht auf Hardware geprüft]:**
- **Messgröße:** RX-Füllstand direkt nach jedem USB-Paket in `USBD_AUDIO_DataOut`, also `getReadCapacity() − codec.getSampleCounter()` in Samples über alle Kanäle. Beide Werte werden mit gesperrten Interrupts gelesen. Der Abzug des Codec-Zählers glättet die Blocksprünge des DMA. Gemessen wird immer an derselben Stelle der Paketkurve (Spitze), unabhängig von der Phase zwischen SOF und Codec.
- **Sollwert:** `(Puffer + Paket)/2` = (576 + 192)/2 = **384 Samples** (96 Frames). Vor dem nächsten Paket sind dann ≈ 192 Samples da (Reserve 40 Frames bis zum Unterlauf), nach dem Paket 192 frei (Reserve ≈ 47 Frames bis zum Überlauf).
- **Start:** Der Schreibkopf wird beim ersten Paket so gesetzt, dass der Füllstand gleich auf dem Sollwert liegt (bisher 288 nach dem Paket, also nur ≈ 24 Frames Reserve). Das bringt ≈ 0,5 ms mehr Latenz. Der Regler wird dabei zurückgesetzt.
- **Regler:** Alle 32 ms (`usbd_audio_sof_callback`) wird der Mittelwert der ≈ 32 Messungen geglättet (EMA über ≈ 8 Perioden = 0,26 s). Die Korrektur ist `−FB_GAIN × Abweichung in Frames` in LSB (10.14), mit `FB_GAIN = 2`, begrenzt auf ±32 LSB (≈ ±40 ppm). Zu voll heißt kleineres Feedback, der Rechner schickt dann weniger.
- **Verhalten:** P-Regler erster Ordnung, Zeitkonstante ≈ 1/(2 × 0,061/s) ≈ 8 s. Bei 1,3 LSB Grund-Drift bleibt eine Abweichung von ≈ 0,65 Frames, verglichen mit 40 Frames Reserve vernachlässigbar.
- **Plausibilitätsprüfung:** Die Prüfung „max. 1 Sample Unterschied“ (bzw. Faktor 2) vergleicht weiter den *unkorrigierten* Wert.
- **Diagnose:** Erreicht die Korrektur die Grenze, steht in der PROGRAM_MESSAGE `fb clamp <Abweichung> <Korrektur>`. Im Normalbetrieb kommt keine neue Meldung.

**Risiken [Hypothese]:**
- Wie macOS auf ein schwankendes Feedback reagiert, ist nicht bekannt. Die Korrektur bleibt aber im Bereich weniger ppm und ändert sich langsam.
- Folgt der Host dem Feedback nur verzögert (Sekunden), ist der Regler mit τ ≈ 8 s trotzdem stabil. Schwingt er doch, `FB_GAIN` auf 1 senken.
- Bei Paketverlust oder Ruhe des Hosts ändert sich nichts, ohne Messungen bleibt die Korrektur stehen.

**Abnahme:** A1, kurz A2 (Durchleitung ohne USB), dann A6 als **Langlauf 30 min** im Loop wie D16. Kriterien: 0 Phasensprünge, 0 Klicks, keine neue `rx unf`/`fb clamp`-Meldung bei laufendem Stream. Danach A5 (offene Eingänge) gegen A5-b1b, weil sich die USB-Zeitlage ändert.

**Ergebnis (D17/D18):**
- Geflasht und A1 bestanden.
- Langlauf ohne Block-Slips [gemessen]. Es gab ein Einzelereignis (≈ 20 ms, kein Netto-Versatz, vermutlich am USB-Bus).
- Vom Nutzer als Stand für acdc1 angenommen.
- **A5 [gemessen, D19]:** bestanden. Offene Eingänge im Mittel 1,1 dB leiser als Build 1b, Breitbandrauschen gleich, Mischprodukte +4,7 dB. **D24:** reproduzierbar (Streuung ≤ 0,1 dB), also Firmware (05 und/oder 06), nicht Sitzung.
- **A7 = S3 [gemessen, D20]:** SOF-Kamm am Ausgang ohne USB weg, Standalone-Ausgang sauber. Nimmt eine App vom AC/DC auf, startet macOS auch den Playback, dann ist die Durchleitung aus.
- Masseschleife und Alltags-Aufbau: D21–D23 (kein Firmware-Thema).

### Build 2 neu – `v22.4.r-fx1d` (Grill-Runde 2026-11-15, geflasht und abgenommen 2026-11-15)

**Entscheidungen (Grill-Runde 2026-11-15):**
- **Zweck:** zuerst Mess-Basislinie B3 (rohe Eingänge ohne digitalen Gain), dann Alltags-Test. Ob Build 2 die Alltags-Firmware wird, entscheidet der Nutzer nach ein paar Tagen Betrieb.
- **Routing hingenommen [Code]:** RX bleibt POST_FX. Sobald eine App vom AC/DC aufnimmt, startet macOS auch den Playback-Stream (D20). Die Host-Stille überschreibt dann die Patch-Ausgabe. **Ohne Rechner-Stream ist der FX am Ausgang, während einer Aufnahme ist er weg.** Umschalten zur Laufzeit kommt als eigener Build.
- **Basis:** Build 1d + 03 obendrauf: `db9d3dd` + Libraries `9e8f64e` + 01, 02, 04, 05, 06, **03** (in dieser Reihenfolge).
- **Kennung:** `FW_VERSION=v22.4.r-fx1d`, Produktstring „OWL-ACDC-FX“, Ordner `firmware/builds/acdc1-build2-fx1d/`.
- **Mischprodukte-Frage (D19) wird mitgeklärt:**
  - vor dem Flash, noch mit 1d: A5 zweimal in einer Sitzung
  - nach dem Flash: dasselbe mit Build 2 (= B3)
  - Aufbau wie D19 (Alltags-Kette, Gain 12, offene Eingänge, 120 s, Host-Software mit Mehrkanal-Recorder), jede Datei vorher auf Nullen prüfen
- **Rückweg:** zuerst Build 1d (`f522560e…`), dann das Readback (`433b3fd3…`). Rückfall-Kriterien wie E7.
- **Abnahme:**
  - A1–A4
  - A5/B3 wie oben
  - A6 als 10-min-Loop (bei einem Slip verlängern)
  - B1: Portname in macOS und `owl_read.py`
  - B2: Gain 0 → Ausgang stumm, die USB-Aufnahme hat weiter Signal
- **Host-Software:** Gespeicherte Patches merken sich den Gerätenamen „OWL-ACDC“. Nach dem Flash wird eine Kopie mit „OWL-ACDC-FX“ angelegt, das Original bleibt.
- **`owl_read.py`** braucht keine Änderung: `--port` sucht per Teilstring (Standard „OWL-ACDC“) und findet so auch „OWL-ACDC-FX“.
- **Fork:** Erst nach bestandener Abnahme kommt der lokale Branch `acdc/fx1d` (= `acdc/thru-usb-feedback` + ein Commit mit 03). Push nur mit Freigabe.

**Dry-Run:** In einem frischen Baum (`git archive db9d3dd`) liefen 01, 02, 04, 05 und 06 durch, danach ging 03 per `patch --dry-run` sauber durch (rc 0, ohne Fuzz oder Offset).

**Build (2026-11-15T14:47:57Z):**

| Build | `FW_VERSION` | Patches | Größe B | SHA-256 `ACDC.bin` |
|---|---|---|---|---|
| `acdc1-build1d-thru1` (lief bis zu diesem Flash) | `v22.4.r-thru1d` | 01, 02, 04, 05, 06 | 105 972 | `f522560eb3d3c329c37753a1ebfdb326e45bae02192f81e866693b363f044c28` |
| `acdc1-build2-fx1d` | `v22.4.r-fx1d` | 01, 02, 04, 05, 06, 03 | 105 968 | `7f9f9a34b5b19a0245f0ab15426d891adc4f00505c86236cadec167e0402925b` |

**Geprüft:**
- **Quellbaum:** Ein Diff gegen einen neu erzeugten 1d-Baum zeigt nur drei Zeilen Unterschied:
  - `hardware.h`: der Produktstring und die neue Zeile `USE_USBD_AUDIO_TX_PRE_FX`
  - `device.h`: die Version
- **Binary** [Code: Disassembly der ELFs]:
  - In 1d ruft `onProgramReady` `usbd_tx_convert` und `usbd_rx_convert` am Anfang auf, also POST_FX.
  - In Build 2 steht am Anfang nur noch `usbd_rx_convert`. `usbd_tx_convert` kommt als Tail-Call (`b.w`) am Ende, nach MIDI, Parametern und Buttons, auf `audio_input` des nächsten Blocks (PRE_FX).
  - Alle anderen Funktionen haben dieselbe Größe wie in 1d.
  - Strings „OWL-ACDC-FX“ und „AC/DC v22.4.r-fx1d“.
  - Die Vektortabelle ist dieselbe wie bei 1d (SP `0x00001000`, Reset `0x08018479`).
  - Größe deutlich unter 131 072 B.

**Ergebnis (messlog D24–D27, 2026-11-15):**
- **D24:** vor dem Flash 2 × A5 mit 1d, auf ≤ 0,1 dB gleich. Die +4,7 dB der Mischprodukte (D19) kommen also von der Firmware.
- **D25:**
  - Geflasht, Readback = `ACDC.bin`.
  - A1 bestanden.
  - B1: USB/Audio „OWL-ACDC-FX“. Der MIDI-Port bleibt in CoreMIDI „OWL-ACDC“ (kosmetisch).
  - A2–A4 bestanden.
  - B2 bestanden: Die USB-Aufnahme bleibt beim Gain-Sweep auf 0,05 dB konstant.
- **D26:**
  - A5/B3: Nach Abzug des Patch-Faktors gleich wie 1d auf ±0,2 dB, Mischprodukte +0,2 dB.
  - B3 ist die neue Rausch-Basislinie.
  - Der DC-Offset dient als Gain-Sonde.
- **D27:** A6 (10 min Loop): 0 Slips, 0 Klicks.
- **Build 2 lief danach auf acdc1** (bis Build 3d, D34).
- **Fork-Branch `acdc/fx1d`** (2026-11-15, gepusht):
  - Basis `acdc/thru-usb-feedback` (`06430d10`), darauf:
    1. `f7a255cc` ACDC: TX pre-FX + Produktstring „OWL-ACDC-FX“
    2. `11199347` Version `v22.4.r-fx1d`
    3. `741bac39` README (englisch): Ziele, Basis und warum nicht v22.5.0, jede Änderung mit Grund, Routing-Tabelle inkl. macOS-Verhalten bei reiner Aufnahme, Build, DFU-Backup/Flash, Messwerte (B3 in Geräte-dBFS, SOF-Kamm, USB-Stabilität, Grenzen)
  - Angelegt über einen temporären `git worktree` in `$TMPDIR`. Der Klon bleibt auf `acdc/thru-usb-feedback`.
  - Commit-Texte und Code-Kommentar englisch.
  - **Prüfung:** `git archive acdc/fx1d` gegen den Build-2-Quellbaum: Nur die Kommentare in `hardware.h` und `usbd_audio.cpp` weichen ab (wie bei 1d), der Code ohne Kommentare ist identisch.
  - **Gepusht 2026-11-15** (Freigabe im Chat): https://github.com/m9dfukc/OpenWare/tree/acdc/fx1d

### Build 3 – Eingangs-LEDs zeigen beim Aufnehmen die rohen Eingänge (Grill-Runden 2026-11-15; 3/3b/3c verworfen, **3d `v22.4.r-fx2d` angenommen**, heute Rückweg)

**Ausgangslage [Code]:** Mit TX_PRE_FX und laufendem Stream wirken die Regler weder auf die Aufnahme noch auf den Ausgang. Die Eingangs-LEDs zeigten trotzdem `PARAMETER_AA` des Patches, also den Pegel nach dem Regler-Gain. Das führte in die Irre.

**Entscheidungen (Grill-Runde Q1–Q9):**
- **Q1 Bedingung:** TX-Stream aktiv (`usbd_tx != NULL`). RX allein (reines Playback) zählt nicht.
- **Q2 Ort:** in `usbd_tx_convert` (Audio-Task, nicht ISR), über alle 8 Frames × 4 Kanäle. Läuft nur bei aktivem TX, ohne Stream bleibt die Rechenlast gleich.
- **Q3 Skala:** Quadratmittel × 4096 wie Patch und `tx_levels`, ohne −60-dB-Schwelle. Bei Knob 12 Uhr (Gain ×1) sehen beide Modi gleich aus.
- **Q4 Glättung:** pro Block exponentiell, τ = 4 ms (Faktor 0,9592 bei 6 kHz Blockrate).
- **Q5 Clip:** Rot, sobald ein Sample |s| ≥ −0,1 dBFS (8 293 000 von 8 388 607) erreicht, 300 ms Haltezeit (`HAL_GetTick` in `onLoop`).
- **Q6 Übergänge:** TX-Start und -Stopp setzen Pegel und Clip-Bits zurück. Ohne Stream gilt sofort die alte Logik. Die Ausgangs-LEDs bleiben unverändert, die Eigenheit von `tx_levels` (nur die ersten 8 von 32 Samples je Block) wird nicht angefasst.
- **Q7 Regler als MIDI-CC:** nicht in Build 3. Die Firmware sendet sie nur auf Anfrage (`sendPatchParameterValues` beim Settings-Request) [Code]. Soll später kommen, wenn es weder Last noch Störlinien bringt (`TODO.md`).
- **Q8 Namen:** Patch `07-input-leds-raw-when-recording.patch`, Version `v22.4.r-fx2(b)`, Produktstring bleibt „OWL-ACDC-FX“.
- **Q9 Abbruch:** Ist eine Familie im A/B gegen B3 um mehr als 0,5 dB schlechter und bestätigt das eine Wiederholung, geht es zurück auf Build 2.

**Umsetzung (Patch 07):**
- `Source/ProgramManager.cpp`: `raw_in_levels[4]`, `raw_in_clip` (Bitmaske, `__atomic_fetch_or`), `usbd_audio_tx_active()`, `raw_in_levels_update()` am Anfang von `usbd_tx_convert`, nur unter `USE_USBD_AUDIO_TX_PRE_FX`.
- `ACDC/Core/Src/ACDC.cpp`, `onLoop`: Mit TX liest es `raw_in_clip` per `__atomic_exchange_n` und hält Rot 300 ms, sonst `raw_in_levels × 4096` (auf 4095 begrenzt). Ohne TX gilt der alte Code.
- Namen bewusst `raw_in_*` statt `rx_levels`, weil „rx“ im USB-Teil das Playback heißt.
- **Fallstrick (D28):** SAI1 liefert 24 Bit rechtsbündig **ohne Vorzeichen** (`SAI_DATASIZE_24`). v1 hat das übersehen, dadurch Dauer-Rot. v2 erweitert vor der Messung das Vorzeichen.

**Builds:**

| Build | `FW_VERSION` | Patches | Größe B | SHA-256 `ACDC.bin` | Stand |
|---|---|---|---|---|---|
| `acdc1-build3-fx2` | `v22.4.r-fx2` | 01, 02, 04, 05, 06, 03, 07 v1 | 106 316 | `f01c8e6bab917d9e6b8f9a38b8200a3ff00b8c2d8c13a8331f23ebcfb58d1bb9` | geflasht, LED-Test nicht bestanden (D28) |
| `acdc1-build3b-fx2` | `v22.4.r-fx2b` | 01, 02, 04, 05, 06, 03, 07 v2 | 106 332 | `cfa479f30c3bd71bd9ff5515f0208f59fcd0cf28dad0114d8dba2200a9f9cabb` | LEDs ok (D29), A/B nicht bestanden (D30/D31), danach Build 2 zur Kontrolle |
| `acdc1-build3c-fx2` | `v22.4.r-fx2c` | 01, 02, 04, 05, 06, 03, 07c | 106 304 | `f354239dd305f2417b9ca3d5c9f403aff2890c0c66c8bf117c57643663df7364` | LEDs ok, A/B nicht bestanden (D32) |
| `acdc1-build2p-layout` | `v22.4.r-fx1p` | 01, 02, 04, 05, 06, 03, 90 (Füllbytes) | 106 304 | `cbf45166672a02337d45b9514096dd63ab28a7ba7b23baa1d287d91bb08521f9` | Layout-Test, = 3c auf ≤ 0,12 dB (D33) |
| `acdc1-build3d-fx2` | `v22.4.r-fx2d` | 01, 02, 04, 05, 06, 03, 07d | 106 788 | `d212cf8def6f239db997cd45a73304db9bcaf981375e55fdfc2ca2862718832a` | angenommen (D34), lief bis 2026-11-16, heute Rückweg |

**Abnahme (D29–D31):**
- A1 und A2/A3 bestanden, LED-Test mit Stream bestanden
- Clip-Rot damals nicht geprüft (es fehlte ein Signal über ≈ 9,5 V). Nachgeholt und bestanden mit 3d (D36)
- A6 entfällt (Nutzer)
- **A/B gegen B3 nicht bestanden (D30)** [gemessen]: fs/8 +1,4 dB, Kamm +1,5 dB, Mischprodukte −4,0 dB, Rest −0,4 dB, RMS +0,8 dB. r1/r2 auf ≤ 0,04 dB gleich.
- **Kontrolle (D31):** Build 2 zurückgeflasht, 2 × 60 s in derselben Sitzung = B3 auf ≤ 0,2 dB. Die Verschiebung kommt also von Patch 07, nicht von der Sitzung.
- **Q9 → Build 2 bleibt auf acdc1** (`7f9f9a34…`, seit 2026-11-15 ≈ 17:47).
- **Lehre (H7):** Schon 32 Multiply-Adds pro Block im Audio-Task verschieben die blocksynchronen Störer messbar, und zwar nicht monoton: fs/8 und Kamm steigen, die Mischprodukte fallen. Das ist ein Hebel für E3.
- **Offen:** `fb clamp -50.0000 32.0000` als letzte Meldung von 3b (D31), Zeitpunkt unbekannt, keine Klicks.

**Build 3c (Grill-Runde 3c, D32):**
- Q1 Messung in `onLoop` (alle 2 ms) auf `codec_rxbuf` (64 Samples), nichts im Audio-Pfad
- Q2 lückenhafte Abdeckung (≈ 1/6) hingenommen
- Q3 τ 40 ms gegen Alias-Flackern
- Q4 Skala, Schwelle und Haltezeit wie 07
- Q5 Patch `07c-input-leds-raw-onloop.patch` als Alternative zu 07, Version `v22.4.r-fx2c`
- Q6 Abnahme A1, LEDs, A/B gegen die Kontrolle D31
- Q7 Push später zusammen
- **Ergebnis:** LEDs ok, aber fs/8 +2,0, Kamm +1,5, Mischprodukte −4,4 dB. Ändert nur `ACDC.cpp`, verschiebt aber alle folgenden Funktionen um 0x150 B.

**Füllbyte-Test `v22.4.r-fx1p` (D33):**
- Build 2 + nie aufgerufene Füllfunktion (0x150 B, Section `.text.onLoop`) und 0x28 B RAM (Section `.bss.fast_log_table_size`), Patch `90-layout-pad-like-3c.patch`
- 955 von 957 Adressen wie in 3c
- **Reproduziert 3c auf ≤ 0,12 dB** → Die Lage von Code und Daten im Speicher verschiebt die Linien, nicht die Funktion [gemessen].

**Build 3d `v22.4.r-fx2d` (D34), lief bis 2026-11-16 auf acdc1, heute Rückweg:**
- **Funktion:** wie 3c.
- **Code:** liegt in `.late_text`, einer neuen Output-Section hinter dem `.data`-Ladeabbild am Ende des Flash.
- **Zustand:** liegt in `.late_bss` (NOLOAD) in den obersten 64 B von RAM_D2. `_HEAP_D2_END` rückt um 64 B nach unten, der Heap-Anfang bleibt. Weil der Bereich beim Booten nicht genullt wird, setzt eine Magic-Prüfung ihn beim ersten Aufruf zurück.
- **`onLoop`:** `b.w` + `naked`-Füllfunktion in `.text.onLoop`, zusammen genau 0x1d0 B.
- **Patch:** `07d-input-leds-raw-late-section.patch`, betrifft `ACDC.cpp` und `Hardware/xibeca.ld`.
- **Binary:**
  - 106 788 B, SHA `d212cf8d…`
  - In den ersten 105 968 B bytegleich mit Build 2, außer `onLoop`, dem Literal `_HEAP_D2_SIZE` und einem Zeichen der Version.
- **A/B gegen die Kontrolle:**
  - fs/8 +0,05, Mischprodukte +0,03, Rest −0,18, RMS +0,19 dB
  - Kamm +0,55 (gegen B3 +0,42, r2 − r1 +0,26)
- **Nutzer:** 3d bleibt, ohne weitere Kontrolle.

**Lehre für alle weiteren Builds:**
- Jede Änderung, die Code oder Daten vor den Audio-Funktionen verschiebt, verändert fs/8, Kamm und Mischprodukte um bis zu ±2 bzw. ±4,5 dB.
- A/B zwischen Builds misst deshalb Code **und** Lage.
- Neue Funktionen kommen daher nach `.late_text`/`.late_bss`, oder die Lage wird per `nm` gegen den Referenz-Build geprüft.
- Die Lage ist zugleich ein Hebel für E3: Füllbytes durchprobieren.

**Fork:**
- `acdc/fx1d` + `f206fdd4` (Code 07), `6eee596c` (Version fx2b), `b3bd3752` (README), gepusht 2026-11-15.
- Dazu lokal `8da4eb7b` (README A/B), `6d3b8bd5` (Code 07d), `cc2e08f8` (Version fx2d), `abc3a72a` (README fx2d + „Memory layout matters“). **Gepusht 2026-11-15.**
- Der Branch-Name bleibt historisch.

**Rückweg (ab 3d):** Build 2 (`7f9f9a34…`), dann 1d (`f522560e…`), dann das Readback (`433b3fd3…`).

### Build 4 – Heißer Pfad im ITCM, `v22.4.r-fx3i` / `fx3ip` (Grill-Runde 2026-11-16; gebaut 2026-11-16; **fx3i gemessen: fs/8 −5 dB, aber USB-Playback gestört (D37/D38), danach zurück auf 3d**)

**Ziel:** Die Lage des übrigen Codes im Flash soll die Störlinien nicht mehr verschieben (D33). Grundlage: `docs/research/notes/layout_noise_2026-11-16.md` und `daisy_itcm_2026-11-16.md`. Belege, dass ITCM Störlinien senkt, gibt es nirgends, das bleibt [Hypothese]. Teensy 4 legt allen Code ins ITCM, das Muster ist also erprobt. Daisy nutzt kein ITCM.

**Entscheidungen (Nutzer 2026-11-16, Q1–Q15):**
- **Q1 Basis:** `db9d3dd` + Libraries `9e8f64e` + 01 02 04 05 06 03 07d **+ 08** (Upstream-Build-Flags `d5b6409a`, auf 3d bytegleich). Kein Wechsel auf master `36eaf1c4` (wäre eine Portierung, siehe `docs/research/notes/upstream_master_2026-11-16.md`), kein Patch 09.
- **Q2 Erfolg:** Pflicht sind (a) und (b).
  - (a) `fx3i` ist bei fs/8, Kamm und Mischprodukten nicht schlechter als 3d, Schwelle ≈ 0,5 dB. Leiser ist ein Bonus.
  - (b) `fx3ip` (= `fx3i` + Füllbytes wie `fx1p`/Patch 90) unterscheidet sich von `fx3i` um ≤ 0,5 dB, die Lage zählt also nicht mehr.
- **Q3 Messung:** eine Sitzung, Reihenfolge 3d → fx3i → fx3ip → 3d. Je 2 × 60 s, offene Eingänge, Gain 12 Uhr, Stream zwischen den Läufen neu geöffnet. Jeder Flash nur nach Freigabe.
- **Q4:** Jitter (Daisy), WFI im Idle und gleichmäßige Last im Idle (Electrosmith-Empfehlung, Daisy-Doku „Avoiding Callback Noise“) erst danach, je als eigener Build mit A/B.
- **Q5:** Clip-Test von 3d am Anfang derselben Sitzung (Signal über ≈ 9,5 V).
- **Q6:** kein eigener Diagnose-Build zum Mechanismus (z. B. I-Cache aus).
- **Q7 Umfang:** alles, was periodisch läuft, ≈ 10 KB:
  - SAI-DMA-ISR samt `HAL_DMA_IRQHandler`
  - FreeRTOS-Scheduler mit Idle und PendSV
  - Audio-Task mit `onProgramReady`, `usbd_tx/rx_convert`, `updateParameters`, MIDI-Senden/Empfangen
  - USB-OTG-ISR samt `HAL_PCD_IRQHandler`, USBD-Kern und Audio-Klasse, Feedback
  - SysTick, ADC-DMA
  - Helfer `memset`/`memcpy`/`abs` und die Listenfunktionen
  - die 07d-Funktionen aus `.late_text`

  Die Funktionsliste mit Größen stand in der Übergabe vom 2026-11-16 (nicht im Repo). Heute liefert sie `tools/check_itcm.py --ref <Build>` als Tabelle im Report, z. B. in `firmware/builds/acdc1-build6-fx4a/check_itcm.md`.
- **Q8:** Die Vektortabelle kommt mit ins ITCM, auf 1 KB ausgerichtet. VTOR wird nach dem Kopieren umgesetzt, das Original bleibt im Flash für den Boot.
- **Q9 Ort:** CCMRAM ab 0x3000, hinter `PROGRAMSTACK`. Der Code muss im Linkerskript **vor** `PROVIDE(_CCMRAM)` stehen, sonst nullt der Patch-Start ihn (`ProgramManager.cpp`, `USE_CCM_RAM`). Heap-Segment 0 schrumpft von 52 auf ≈ 41 KB.
- **Q10:** Das Rest-Layout wird nicht festgehalten, (b) prüft die Lagenabhängigkeit direkt.
- **Q11 Prüfung vor dem Flash:** neues `tools/check_itcm.py` prüft am ELF:
  - Alle Hotpath-Funktionen und die Vektortabelle liegen im ITCM-Block.
  - Aus dem heißen Pfad gehen `bl`/`b.w` nur im Fehlerpfad in den Flash.
  - Veneers sind aufgelistet.
  - Die Größe liegt unter 131072 B, LMA/VMA der Kopie stimmen.
  - Dazu die `nm`-Tabelle gegen 3d.

  Nach dem Flash erst A1 (`owl_read.py`), Durchleitung, USB-Aufnahme und LEDs, dann die Rauschmessung. Rückfall: 3d.
- **Q12–Q15 Aufnahme:** mit `tools/acdc_rec.py`, Gegenprobe gegen die Host-Software bestanden (D35).

**Technik (aus den Recherchen, ohne Rückfrage so umzusetzen):**
- **Linkerskript:** `.itcm_text` mit `>CCMRAM AT>FLASH` vor `.text` (die erste passende Output-Section gewinnt). Muster nach Datei und Section, z. B. `*stm32h7xx_hal_dma.o(.text.HAL_DMA_IRQHandler)`. Möglich ist das, weil `-ffunction-sections` gesetzt ist und kein LTO läuft. C++-Namen sind gemangelt. Weak/Strong-Duplikate (SAI-Callbacks, `updateParameters`) nach Objektdatei filtern. COMDAT-Kopien prüfen.
- **ECC:** Das ITCM hat 64-Bit-ECC (AN5342/RM0433). Anfang, Ende und LMA der Section auf `ALIGN(8)` legen, in 64-Bit-Wörtern kopieren, danach DSB/ISB. RAMECC ist in OpenWare aus, Fehler würden also still markiert.
- **Startup:** zweite Kopierschleife in `startup_owl3.s` nach der `.data`-Schleife, vor `__libc_init_array`/`main`. Nichts, was vor `main` läuft (`SystemInit`, Konstruktoren), darf ins ITCM.
- **Veneers:** GNU ld legt sie selbst an, `-mlong-calls` ist nicht nötig. Jeder Aufruf aus dem ITCM in den Flash kostet aber Veneer plus Flash-Fetch. Deshalb nach dem Link alle auflisten und Helfer nachziehen (`__aeabi_*`, `memcpy` usw.).
- **Optional, nicht im ersten Wurf:** heiße `.rodata` ins DTCM, MPU-Schreibschutz über `.itcm_text`.
- **Bauen:** neuer Patch `11-itcm-hotpath.patch` (Nummer frei wählen, bestehende nicht ändern), `FW_VERSION=v22.4.r-fx3i tools/build_acdc.sh acdc1-build4-fx3i db9d3dd firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz 01 02 04 05 06 03 07d 08 11`. `fx3ip` = dazu Patch 90 bzw. ein Füllpatch, der den Flash-Rest verschiebt (Ziel: andere Adressen außerhalb des ITCM, ITCM-Inhalt gleich).

**Umsetzung (2026-11-16) [Code, am ELF geprüft, nicht auf Hardware]:**
- **Patch `11-itcm-hotpath.patch`** (nur `Hardware/xibeca.ld` und `Source/startup_owl3.s`, bestehende Patches unverändert):
  - `.ccmdata` (NOLOAD, PROGRAMSTACK 0x1000–0x3000) im Skript vor `.text` verschoben, Adresse unverändert.
  - `.itcm_vectors` (NOLOAD) bei 0x3000, 1 KB ausgerichtet, für die Vektorkopie (664 B).
  - `.itcm_text >CCMRAM AT>FLASH` vor `.text`, Linker-Muster nach Objektdatei + Section. VMA 0x32A0–0x62C8 (12 328 B inkl. 27 Veneers), LMA 0x08000298. Anfang, Ende und LMA 8-Byte-ausgerichtet (ECC).
  - `_CCMRAM = _eitcm_text`: Patch-Heap im CCM 40 248 B (39,3 KB) statt 53 248 B.
  - `Reset_Handler`: nach `.data`/`.bss` zwei `ldrd/strd`-Schleifen (Vektoren, Code), DSB/ISB, VTOR = 0x3000, DSB/ISB, dann `__libc_init_array` und `main`. `SystemInit` läuft vorher und ruft nichts im ITCM.
  - **Anker** am Anfang von `.text` (0x080032C0, 2 395 B): alle Flash-Ziele, deren Adresse im ITCM steht (Vektor-Handler im Flash, 27 Veneer-Ziele, 6 Debug-Texte). Nur so bleibt der ITCM-Inhalt bei der Füllvariante bytegleich.
- **Umfang gegenüber der Übergabeliste nachgezogen** (Veneer-Prüfung, Q7 „alles, was periodisch läuft“):
  - Gruppe H Hauptschleife alle 2 ms: `StartDefaultTask`, `loop`, `onLoop` (mit 07d-Füllfunktion, 0x1D0 B), `Owl::loop`, `ProgramManager::isProgramRunning`, `device_watchdog`, `vTaskDelayUntil`, `vTaskSuspendAll`, `xTaskResumeAll` (+ `.part.0`).
  - onLoop-Helfer: `setLed` (+ `.constprop.0`), `getParameterValue`, `setParameterValue`, `HAL_GetTick`.
  - USB: `usbd_midi_tx`, Flush-Kette (`USBD_LL_FlushEP`, `HAL_PCD_EP_Flush`, `USB_FlushTx/RxFifo`), ISO-OUT-Incomplete-Kette.
  - Zusammen 104 Funktionen, 11 606 B.
- **Veneers ITCM → Flash (27), alle kalt:** Fehler (`usbd_audio_error`, `debugMessage` ×2, `vApplicationStackOverflowHook`, `HAL_ADC_ErrorCallback`, `USBD_LL_StallEP`) und seltene Ereignisse (Enumeration/Reset/Suspend/Resume/Connect/LPM, EP0-Control-Transfer, Stream-Start `usbd_audio_rx_start_callback`, MIDI-Eingang `usbd_midi_rx`, `vPortFree` im Idle nach Task-Löschen, `setup` einmal beim Start). Literale in den Flash: nur 6 Debug-Texte. Liste mit Aufrufern in `check_itcm.md`.
- **Patch `91-layout-pad-behind-itcm-anchor.patch`** (fx3ip): `. = . + 0x150` hinter `_eitcm_anchor`. 479 Flash-Funktionen +0x150, Anker (171 Symbole inkl. Default-Handler-Aliase) fest, ITCM-Code und Vektortabelle bytegleich mit fx3i, alle RAM-Adressen gleich. Anders als fx1p (D33) bleibt das RAM unverschoben.
- **`tools/check_itcm.py`** prüft Q11 am ELF und Binary (Sections, Ausrichtung, LMA, Binary = ELF, Vektoren, Hotlist, Veneers gegen eine Liste kalter Ziele mit Grund, Literale, Anker, USBD_AUDIO-Zeiger, nichts im ITCM vor der Kopie, nm gegen Referenz, `--same-itcm`). Bericht `check_itcm.md`/`.json` im Build-Ordner.
- **nm gegen 3d:** 728 gemeinsame Funktionen, 105 ins ITCM, keine an alter Adresse (alles verschoben), nur `Reset_Handler` größer (66 → 128 B). RAM: alle 176 Datenobjekte an derselben Adresse wie in 3d.
- [Hypothese] Patches legen nichts fest ins CCM (Heap kommt über `heapSegments`), sonst würden sie den Code überschreiben. Funktionsprobe nach dem Flash klärt das.

| Build | `FW_VERSION` | Patches | Größe B | SHA-256 `ACDC.bin` | Stand |
|---|---|---|---|---|---|
| `acdc1-build4-fx3i` | `v22.4.r-fx3i` | 01 02 04 05 06 03 07d 08 11 | 107 304 | `8fedebf7e909457f69d8b2a06003cd550496c7f65b330d3f5d5206597037fdf2` | geflasht 2026-11-16 (D37): fs/8 −5,1 dB, Rest −0,9 dB, Kamm ±0; **Playback gestört** (28 Slips/60 s, `fb clamp`, D38) → zurück auf 3d |
| `acdc1-build4p-fx3ip` | `v22.4.r-fx3ip` | dazu 91 | 107 640 | `d2b36d8453e856f63c5e2ebbae983b93eaebec41161987078379f4b0cf9b541d` | geprüft, ITCM bytegleich mit fx3i, **nicht geflasht** (hat denselben Fehler) |

**Ergebnis der Sitzung (D36–D38):**
- Clip-Rot von 3d bestanden (D36).
- Q2 (a) erfüllt: fx3i gegenüber dem Mittel zweier 3d-Kontrollen fs/8 −5,06 dB, RMS −0,98, Rest −0,89, Mischprodukte −0,54, Kamm +0,01 dB (D37).
- Q2 (b) offen: fx3ip nicht gemessen.
- **Funktionsfehler:** Im USB-Loop hat fx3i 28 Slips in 60 s und erhöhtes Phasenrauschen, 3d im selben Aufbau 0 (D38). Der RX-Puffer läuft ≈ 1 Paket zu leer (`fb clamp −195…−208`). Ursache offen [Hypothese: verlorene ISO-OUT-Pakete oder Wettlauf ISR/Audio-Task durch das geänderte Timing].
- **Nächster Schritt:** Halbieren mit fx3i-Varianten (ohne Gruppe D bzw. C im ITCM), Prüfung je Variante mit dem 60-s-Loop-Test (`acdc_rec.py --sine 440 530 670 790` + `phase_slips.py`), erst danach wieder Rauschmessung und fx3ip. Jede neue Variante vor dem Flash mit `check_itcm.py`. **Erledigt:** „Build 4x“ unten (D39/D40).

### Build 4x – Halbierung des fx3i-Fehlers (2026-11-16 abends, messlog D39/D40)

**Ziel:** Herausfinden, welche Gruppe im ITCM den Playback-Fehler von fx3i (D38) auslöst. Abgestimmt mit dem Nutzer: alle vier Varianten bauen, am Gerät noD → noC → onlyD, novt nur bei Bedarf, Diagnose-Build mit Zählern erst nach den Varianten.

**Umsetzung [Code, am ELF geprüft]:**
- Je Variante ein eigener, **vollständiger Ersatz für Patch 11** (11 und alle anderen Patches unverändert). Erzeugt aus dem Stand nach Patch 11: Nicht gewählte Gruppen sind im `.itcm_text`-Block durch einen Kommentar ersetzt. Anker, `.itcm_vectors` und Startup bleiben wie in 11.
  - `11a-itcm-variant-noD.patch`: Gruppen A B C E F G H L
  - `11b-itcm-variant-noC.patch`: A B D E F G H L
  - `11c-itcm-variant-onlyD.patch`: D L
  - `11d-itcm-variant-novt.patch`: alle Gruppen, Linkerskript wie 11 (Platz für die Vektoren bleibt reserviert), aber `Reset_Handler` ohne Vektorkopie und ohne VTOR-Schreiben
- Gruppe **L** = libc-Helfer `memset`/`memcpy`/`abs` (im Linkerskript schon eigener Block). Sie bleibt in allen Varianten im ITCM.
- **`tools/check_itcm.py`** neu mit `--groups` (Buchstaben A–H, L) und `--no-vector-copy`:
  - Funktionen und Vektoren nicht gewählter Gruppen müssen im Flash liegen.
  - Veneers zu ihnen sind eine eigene, gewollte Kategorie.
  - Der Anker wird bei Varianten nur gewarnt.
  - `USBD_AUDIO`-Callbacks werden nur bei Gruppe D im ITCM erwartet.
  - Gruppe L ist neu: `memset` stand vorher unter C, `memcpy`/`abs` unter D.
  - fx3i ergibt mit der neuen Fassung denselben Bericht wie vorher.
- Bau: `FW_VERSION=v22.4.r-fx3i-<v> tools/build_acdc.sh acdc1-build4x-<v> db9d3dd firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz 01 02 04 05 06 03 07d 08 11x`. Unter zsh die Patchliste als Array übergeben, sonst kommt sie als ein Argument an.
- Neu **`tools/stale_samples.py`**: einzelne falsche Samples in Loop-Aufnahmen finden (Lage im Block-Raster, bester Abstand des falschen Werts), ergänzt `phase_slips.py`.

| Build | `FW_VERSION` | ITCM-Code | Patch-Heap CCM | Größe B | SHA-256 `ACDC.bin` | check_itcm | Loop-Test (D39) |
|---|---|---|---|---|---|---|---|
| `acdc1-build4x-noD` | `v22.4.r-fx3i-noD` | 7 232 B | 45 344 B | 107 116 | `2c140449cd44b4f93cc43405bca4553ac12d1c6e0ace30cfcb5c336772cfcd59` | bestanden, 1 WARN (Anker) | **USB sauber**, Kanal 4 veraltet |
| `acdc1-build4x-noC` | `v22.4.r-fx3i-noC` | 11 432 B | 41 144 B | 107 300 | `8b7d2197bfe67bb9d31d2a9a9af241e3374f1b5ed59440c40ab44d610c338a26` | bestanden, 1 WARN (Anker) | 16 Slips, `fb clamp`, Kanal 4 sauber |
| `acdc1-build4x-onlyD` | `v22.4.r-fx3i-onlyD` | 5 152 B | 47 432 B | 107 136 | `f75efaeed79c74330819b1c36063d9c31a90e91b80a3d800a7d2b7d31400f107` | bestanden, 1 WARN (Anker) | 8 Slips, Kanal 4 sauber |
| `acdc1-build4x-novt` | `v22.4.r-fx3i-novt` | 12 328 B | 40 248 B | 107 260 | `da25fc5f374a17679408c72b33d08e2b720b0de076579f6cb31e6f673408aaab` | bestanden | nicht geflasht (überflüssig) |

**Ergebnis [gemessen, D39/D40]:** fx3i hat **zwei getrennte Fehler**.
1. **USB-Playback-Fehler ↔ Gruppe D im ITCM.** D allein löst ihn aus (onlyD), ohne D ist er weg (noD). Vektortabelle/VTOR scheiden aus (H-e). Der Mechanismus innerhalb von D ist offen, [Hypothese] H-a (ISO-OUT-Parität beim Neu-Aufsetzen, leeres `IsoOutIncomplete`).
2. **Veralteter letzter Eingangs-Sample (Kanal 4, 16 Frames alt) ↔ Gruppe C im ITCM.** [Code] `audioCallback` hängt am TX-DMA-Interrupt, gibt aber die RX-Hälfte frei, bevor die RX-DMA das letzte Wort geschrieben hat. Der schnelle Audio-Task liest zu früh. Das ist ein latenter Fehler im Original, er trifft auch den Patch-Eingang (Standalone).

**Was taugt als Nächstes für die Rauschmessung (fx3i′ + fx3ip′)?** Vorschlag, noch nicht abgestimmt:
- **Basis noD** (USB-Code im Flash, alles andere im ITCM). Sie ist im USB-Loop sauber.
- **Dazu ein Fix für den RX-Wettlauf**, sonst ist Kanal 4 verfälscht und Standalone betroffen. Zwei Wege, beide ändern Code:
  - (a) In `audioCallback` warten, bis der RX-DMA-Zähler (NDTR von SAI1-A) die Halbgrenze überschritten hat. Das dauert höchstens ein Wort, ≈ 1–5 µs, und ändert das Timing kaum.
  - (b) Den Block wie im CS4271-Zweig an die RX-Interrupts hängen. Das verschiebt die Lage des Audio-Tasks zum Codec und damit möglicherweise die blocksynchronen Störlinien.
  - Empfehlung (a), weil es minimal ist. Ob der Fix auch in 3d gehört, ist offen: Dort wurde der Wettlauf nie gemessen (0 von 96 000).
- **Offen:** Wie viel der fs/8-Verbesserung (−5 dB, D37) noch bleibt, wenn D im Flash liegt. Und ob noD lagenunabhängig ist, denn der 1-kHz-USB-Code liegt dann wieder im Flash, und der Anker bräuchte `USBD_LL_Transmit`. Beides klärt erst die Messung fx3i′ gegen 3d bzw. fx3ip′.
- **Alternative:** Den USB-Fehler mit Gruppe D im ITCM verstehen und beheben (Diagnose-Build mit Zählern in `.late_bss`: `INCOMPISOOUT`, Frame-Nummern-Lücken zwischen `DataOut`, Paketlängen, `rx unf/ovf`, Meldung per `PROGRAM_MESSAGE`). Danach D aufteilen (OUT-Pfad / SOF+Feedback / IN-Pfad). Das ist aufwendiger, wäre aber nötig, falls der fs/8-Gewinn an D hängt.

### Build 4y – fx3j = noD + RX-Fix (2026-11-16 spätabends, messlog D41/D42)

**Entscheidung (Nutzer):** fx3i′ = noD + Fix des RX-Wettlaufs (D40). Gebaut als fx3j, dazu die Füllvariante fx3jp.

**Umsetzung [Code]:**
- **Patch `11e-itcm-variant-noD-anchor.patch`** (Ersatz für 11/11a): wie 11a, dazu `USBD_LL_Transmit` im Anker. Das war das einzige Flash-Ziel des ITCM-Codes hinter dem Anker (Veneer aus `usbd_midi_tx`). `check_itcm --groups ABCEFGHL`: 0 FAIL, 0 WARN.
- **Patch `12-rx-dma-wait.patch`** (`Source/Codec.cpp`, PCM3168A-Zweig):
  - In `HAL_SAI_TxHalfCpltCallback`/`TxCpltCallback` vor `audioCallback` warten, bis NDTR der RX-DMA (`hdma_sai1_a`, DMA1_Stream0) die freigegebene Hälfte verlassen hat.
  - Erste Hälfte fertig: NDTR ≤ blocksize·Kanäle. Zweite Hälfte fertig: NDTR > blocksize·Kanäle.
  - Höchstens 4096 Lesezugriffe. Die Callbacks liegen im ITCM (Gruppe A).
- fx3jp = fx3j + Patch 91: ITCM bytegleich mit fx3j, 514 Flash-Funktionen +0x150. Hier verschiebt sich auch der USB-Code, weil er im Flash liegt. RAM unverändert.

| Build | `FW_VERSION` | Patches | Größe B | SHA-256 `ACDC.bin` | Stand |
|---|---|---|---|---|---|
| `acdc1-build4y-fx3j` | `v22.4.r-fx3j` | 01 02 04 05 06 03 07d 08 11e 12 | 107 176 | `707d9cd3324baa7ea20f3178df972e60c2822466e3a7c7bc826b7b456c5546ac` | geflasht 2026-11-16: Loop sauber (D41), **Rauschen schlechter als 3d** (D42) → 3d zurück |
| `acdc1-build4yp-fx3jp` | `v22.4.r-fx3jp` | dazu 91 | 107 512 | `6db0f56c06469f13e298cd6a4d6baf1f0ef0037508a98f38cc8ef7efadf55306` | geprüft (`--same-itcm` fx3j), nicht geflasht |

**Ergebnis [gemessen, D42]** (Δ gegen 3d derselben Sitzung):
- **fx3j:** fs/8 +5,2, Kamm +3,1, RMS +2,8, Mischprodukte −10,1 dB. Funktional einwandfrei, für die Rauschmessung aber unbrauchbar.
- **noD (ohne Fix):** fs/8 −5,4, Kamm +2,5, RMS +0,7 dB.
- **Daraus:**
  1. Der fs/8-Gewinn von fx3i hängt **nicht** am USB-Code im ITCM.
  2. **Die Warteschleife (Patch 12) kostet ≈ +10,6 dB fs/8.** Ein paar µs Lesen eines D2-Peripherie-Registers pro Block reichen. [Hypothese] Was die CPU im Blocktakt tut, erscheint direkt bei fs/8. Für die Ursachensuche ist das ein wichtiger Befund.
  3. **Den Kamm** senkt nur der USB-Code im ITCM (fx3i ±0, noD +2,5 dB).

**Nächste Schritte (Vorschlag, nicht abgestimmt):**
1. **RX-Fix ohne Abfrage-Schleife (Patch 12b):** **Erledigt, siehe „Build 4z“ (D43/D44).** Im PCM3168A-Zweig `audioCallback` aus `HAL_SAI_RxHalfCpltCallback`/`RxCpltCallback` aufrufen statt aus den TX-Callbacks, wie im CS4271-Zweig.
   - Die RX-DMA-Interrupts laufen heute schon (DMA1_Stream0, die schwachen HAL-Callbacks sind leer). Es entsteht also kein zusätzlicher Interrupt und kein Busverkehr, der Block startet nur ≈ 1 Wort später.
   - Ausgangsseite [Code]: Der Task schreibt die eben gesendete TX-Hälfte, die TX-DMA ist höchstens FIFO-Tiefe voraus. Fast ein ganzer Block bleibt Zeit.
   - Prüfen: Loop (0 Slips, 0 veraltete Samples), Rauschen gegen 3d und noD.
2. **Kamm:** USB-Code (ganz oder nur SOF/Feedback) ins ITCM, ohne den Playback-Fehler. Dazu Gruppe D aufteilen (D-SOF: SOF-Kette + Feedback, D-OUT: `DataOut`/`PrepareReceive`/`EP_Receive`/`EPStartXfer`/`ReadPacket`, D-IN) oder Diagnose-Build mit Zählern (`INCOMPISOOUT`, Frame-Lücken zwischen `DataOut`, Paketlängen).
3. Danach Lagen-Test (Füllvariante) für den gewählten Stand.
4. Offen: ob Patch 12b auch in 3d bzw. den Standalone-Stand gehört. In 3d ist der Wettlauf nie aufgetreten (0 von 96 000 Samples).

### Build 4z – fx3k = noD + RX-Callback (2026-11-16 spätabends, messlog D43/D44)

**Umsetzung [Code]:**
- **Patch `12b-rx-dma-callback.patch`** (Ersatz für 12, `Source/Codec.cpp`, PCM3168A-Zweig):
  - `audioCallback` wird aus `HAL_SAI_RxHalfCpltCallback`/`RxCpltCallback` aufgerufen (RX-DMA, SAI1-A, DMA1_Stream0), mit denselben Argumenten wie vorher aus den TX-Callbacks. Das ist das Muster des CS4271-Zweigs.
  - Die RX-DMA-Interrupts liefen schon vorher, nur mit leeren schwachen Callbacks. Es gibt also keinen zusätzlichen Interrupt und keine Abfrage.
  - Die TX-Callbacks bleiben als starke, leere Definitionen in `Codec.o`. Damit greift die ITCM-Regel weiter, und es entsteht kein Veneer zur HAL-Fassung.
  - [Code] `codec.getSampleCounter()` liest weiter den TX-NDTR und springt ≈ 1 Wort vor dem Blockstart auf 0. Das Fenster, in dem Patch 06 bzw. `usbd_audio_get_rx_count` den Block schon als verbraucht zählen, wird um ≈ 5 µs länger. Es gab dieses Fenster schon vorher (Aufwachlatenz des Tasks), und es korrigiert sich selbst. Im Loop-Test zeigt sich keine Wirkung (D43).
- **Patch `11f-itcm-variant-noD-anchor-rxcb.patch`** (Ersatz für 11/11a/11e): wie 11e, dazu `*Codec.o(.text.HAL_SAI_RxHalfCpltCallback .text.HAL_SAI_RxCpltCallback)` in Gruppe A. Die Regel für `stm32h7xx_hal_sai.o` greift mit 12b nicht mehr, weil die schwachen Fassungen per `--gc-sections` wegfallen.
- Geprüft: `check_itcm.py --groups ABCEFGHL` mit 0 FAIL und 0 WARN. Die RX-Callbacks aus `Codec.o` liegen im ITCM und springen per `b.w` in `audioCallback`, die TX-Callbacks sind `bx lr`. fx3kp mit `--same-itcm` fx3k: ITCM bytegleich (7232 B), 514 Flash-Funktionen +0x150.
- fx2e = 3d + 12b ohne ITCM. Code hinter `Codec.o` rückt dort um −8/−16 B gegen 3d (301 bzw. 163 Funktionen). Patch 08 allein ändert das Binary nicht (`cand-r-fx2d-gcc13flags` = `d212cf8d…`).

| Build | `FW_VERSION` | Patches | Größe B | SHA-256 `ACDC.bin` | Stand |
|---|---|---|---|---|---|
| `acdc1-build4z-fx3k` | `v22.4.r-fx3k` | 01 02 04 05 06 03 07d 08 11f 12b | 107 112 | `06e868d16ea8c601ac1433bd2f67fc14a31edd7737885bcf4754d0c08de3dea8` | geflasht 2026-11-16: Loop sauber (D43), fs/8 −5,8, Kamm +3,5 dB (D44) → 3d zurück |
| `acdc1-build4zp-fx3kp` | `v22.4.r-fx3kp` | dazu 91 | 107 448 | `c3835524f4d5281cb3469800a6cab436d317554c6cb60e49cb957a051c67a91a` | geprüft, nicht geflasht (Kamm-Kriterium verfehlt) |
| `acdc1-build3e-fx2e` | `v22.4.r-fx2e` | 01 02 04 05 06 03 07d 08 12b | 106 780 | `4a1aa25f3cd96f62ef23d477526c86c0ecc0c19c32f20424eabc7af82edf7055` | gebaut, nicht geflasht |

**Ergebnis [gemessen, D43/D44]** (Δ gegen 3d derselben Sitzung):
- **Loop:** 0 Slips, 0 veraltete Samples (30 s), kein `fb clamp`.
- **Rauschen:** fs/8 −5,8, Kamm +3,5, Mischprodukte −19,4, RMS +1,0 dB.
- **12b kostet bei fs/8 nichts** (noD −5,4, fx3i −5,1). Der Anstieg in fx3j kam von der Abfrage-Schleife.
- Q2 (a) verfehlt fx3k nur beim Kamm (USB im Flash), deshalb kein fx3kp.

**Nächste Schritte (Vorschlag, nicht abgestimmt):**
1. **Kamm:** **Erledigt, siehe „Build 5“ (D45–D48): fx3l.** Auf fx3k-Basis USB-Code ins ITCM, ohne den Playback-Fehler aus D39. Entweder Gruppe D aufteilen (D-SOF: SOF-Kette + Feedback; D-OUT: `DataOut`/`PrepareReceive`/`EP_Receive`/`EPStartXfer`/`ReadPacket`; D-IN) oder ein Diagnose-Build mit Zählern (`INCOMPISOOUT`, Frame-Lücken, Paketlängen). Ziel: fx3i-Kamm (±0) mit fx3k-fs/8 und fx3k-Mischprodukten.
2. Danach Lagen-Test (Füllvariante) für den gewählten Stand.
3. Offen: ob 12b auch in 3d/Standalone gehört (fx2e liegt bereit). In 3d ist der Wettlauf nie aufgetreten. Der Fix ist aber richtig, und 12b ist billig.

### Build 5 – USB im ITCM: Diagnose, SOF-Fix, fx3l (2026-11-16 nachts, messlog D45–D48)

**Vorgehen (Nutzer-Entscheidung):** Erst einen Diagnose-Build mit Zählern bauen, dann gezielt beheben. D nicht aufteilen.

**Diagnose [gemessen]:**
- Patch `13-usb-diag-counters`: Zähler im USB-Pfad, Meldung alle 500 ms aus onLoop. Mit USB im ITCM (dg5i) gehen **keine** ISO-OUT-Pakete verloren (H-a widerlegt), der Feedback-Regler klemmt aber ständig. Mit USB im Flash (dg5f) läuft alles sauber (D45).
- Patch `13b-usb-diag-sof-fb`: `USBD_AUDIO_SOF` läuft mit USB im ITCM in ≈ 97 % der Frames **zweimal** (gleiche Frame-Nummer). Die Feedback-Periode umfasst dann ≈ 16 statt 32 Frames, gesendet wird 47,5…48,5, der Puffer läuft an die Grenze (D46).
- [Hypothese] HAL löscht `GINTSTS.SOF` erst nach dem Callback. Der ITCM-Handler springt erneut ein, bevor das Löschen im USB-Taktbereich wirkt.

**Fix:** Patch `14-usbd-sof-once-per-frame` (`Source/usbd_audio.cpp`): `USBD_AUDIO_SOF` merkt sich `DSTS.FNSOF` und kehrt bei einem zweiten Aufruf im selben Frame sofort zurück. Mit USB im Flash ist der Patch wirkungslos.
- Offen und nicht nötig: das Löschen in HAL vor den Callback ziehen. Damit fielen auch die überzähligen Interrupt-Einsprünge weg (≈ 1 kHz, nur wenige Zyklen). Deren Wirkung auf das Rauschen ist unbekannt.

**Linker:** Patch `11g-itcm-hotpath-rxcb` = Patch 11 (alle Gruppen A–H + L) + RX-Callbacks aus `Codec.o` (für 12b).

| Build | `FW_VERSION` | Patches | Größe B | SHA-256 `ACDC.bin` | Stand |
|---|---|---|---|---|---|
| `acdc1-build5-diag-itcm` | `v22.4.r-dg5i` | Basis + 11g 12b 13 | 108 904 | `27390dcadfd911e2697e0cf6caf1d83e4008c2b4918f5736f25796cb2d8faf48` | geflasht, D45 |
| `acdc1-build5-diag-flash` | `v22.4.r-dg5f` | Basis + 11f 12b 13 | 108 728 | `02052846c647e990abdfecaf55c138b067b4d6b6387f653f3b93a053eb808431` | geflasht, D45 |
| `acdc1-build5b-diag-itcm` | `v22.4.r-dg5i2` | Basis + 11g 12b 13 13b | 109 104 | `9611f646d7fa68a1149fcc063cc72f1cc37b16154a8610007367eaff89e9c2e5` | geflasht, D46 |
| `acdc1-build5b-diag-flash` | `v22.4.r-dg5f2` | Basis + 11f 12b 13 13b | 108 928 | `0a0851f43999391378d33eb5c32e2e24136a3577c9919471d5d4e6aca115838f` | gebaut, nicht geflasht |
| **`acdc1-build5c-fx3l`** | `v22.4.r-fx3l` | Basis + **11g 12b 14** | 107 340 | `b55b94d8734baf1cf763dfefb380a561029bd00d4a645cdcef3b75d99e6f010e` | geflasht: Loop sauber (D47), Rauschen D48 |
| `acdc1-build5cp-fx3lp` | `v22.4.r-fx3lp` | dazu 91 | 107 676 | `a4deba3e6263e1b96b7098a6f03b5117d18abb724cdefac987fb28eba556939f` | geflasht: Rauschen D48 (ITCM bytegleich, 479 Flash-Funktionen +0x150) |

(Basis = 01 02 04 05 06 03 07d 08.) Prüfung fx3l/fx3lp: `check_itcm.py` 0 FAIL, 0 WARN, 104 heiße Funktionen im ITCM (12 352 B Code + 664 B Vektoren), 27 Veneers hinaus, alle kalt, Patch-Heap 39,3 KB.

**Ergebnis [gemessen, D47/D48]** (Δ gegen 3d):
- **fx3l:** Loop sauber (0 Slips, 0 veraltete Samples, kein `fb clamp`). fs/8 −5,1, Mischprodukte −34,8, Rest −1,25, RMS −1,1 dB, Kamm +0,2…+0,4 dB.
- **fx3lp:** ≤ 0,25 dB bei fx3l → lagenunabhängig.
- **Damit sind Q2 (a) und (b) erfüllt.** fx3l ist der erste Kandidat, der 3d ersetzen kann.

**Nächste Schritte (Vorschlag, nicht abgestimmt):**
1. Entscheiden, ob fx3l 3d auf acdc1 ablöst. Vorher wäre ein längerer Alltagstest sinnvoll (Aufnahme + Wiedergabe am Rechner, Standalone-Durchleitung, LEDs, Patch-Wechsel; Patch-Heap im CCM nur 39,3 KB).
2. Zweite Rauschsitzung mit 3d-Startkontrolle (3d → fx3l → 3d), weil der Kamm (+0,2…+0,4) nahe an der Schwelle liegt.
3. Fork-Branch: **erledigt 2026-11-16.** `acdc/fx1d` hat jetzt `151bd8bc` (upstream `d5b6409a`, = 08), `2ae8b836` (12b), `0b7122de` (11g), `fb2c6ed9` (14), `5cb2c17c` (Version) und `b7062ef2` (README). Gepusht, Build der Spitze bytegleich mit fx3l.
4. Optional: HAL löscht `GINTSTS.SOF` vor dem Callback, A/B gegen fx3l.

### Build 6 – Boot-Menü zur Patch-Wahl, `v22.4.r-fx4a` (Absprache und Build 2026-11-17, **Abnahme bestanden mit fx4a/fx4b**, messlog D50–D58)

**Anlass:** Beim Einschalten startet immer Slot 1. Ohne Rechner ließ sich der Patch nicht wechseln.

**Entscheidungen (Nutzer, 2026-11-17):**
- Auswahl nur beim Einschalten, nicht im Betrieb.
- Einstieg: Regler 1, 2, 3 am Linksanschlag, Regler 4 am Rechtsanschlag.
- Regler 1 wählt, Regler 4 weg vom Rechtsanschlag bestätigt, Regler 3 weg vom Linksanschlag bricht ab. Nach 60 s ohne Bestätigung Abbruch.
- Regler 1 zählt erst, wenn er einmal bewegt wurde. Bis dahin bleibt der gemerkte Slot gewählt, ein versehentliches Bestätigen ändert also nichts.
- Höchstens 15 Slots (4 LEDs binär). Der Speicher begrenzt das nicht: 8 MB Patch-Flash, die Firmware kann 40 Slots.
- Der gewählte Slot wird im Flash gemerkt und startet beim nächsten Einschalten.
- Beim Start zeigen die Eingangs-LEDs 1 s lang die Slot-Nummer.

**Umsetzung (Patch `15-boot-menu-slot-select.patch`) [Code]:**
- **Ort:** `acdcBootSelect()` in `ACDC/Core/Src/ACDC.cpp`, aufgerufen aus `bootstrap()` (`Source/ProgramManager.cpp`, unter `OWL_ACDC`). Das Menü läuft im Manager-Task, bevor der erste Patch startet. Im Menü ist der Ausgang deshalb still.
- **Scheduler:** `configUSE_PREEMPTION` ist 0. `onSetup()` (LED-Lauflicht, ≈ 0,9 s) ist fertig, bevor `bootstrap()` läuft. Die Hauptschleife (MIDI, Watchdog) läuft nur, während das Menü in `vTaskDelay()` schläft. `owl_read.py` erreicht das Gerät also auch im Menü.
- **Regler:** direkt aus `adc_values` (12 Bit), im Menü mit 1/8 geglättet. „Am Anschlag“ heißt unter 5 % bzw. über 95 %, „weg vom Anschlag“ weitere 5 %. An acdc1 gemessen: Linksanschlag ≈ 1,6 %, Rechtsanschlag 100 % (D51).
- **Auswahl:** Nur belegte Slots sind wählbar, sie teilen sich den Regelweg gleichmäßig, mit Hysterese an den Grenzen.
- **Anzeige:** Eingangs-LEDs = Slot-Nummer binär (LED 1 = 1, 2 = 2, 3 = 4, 4 = 8). Ausgangs-LEDs leuchten im Menü und blinken, solange ein Bestätigen den Slot ändern würde.
- **Speichern:** 4 Byte als System-Ressource `ACDC.slot` im Patch-Flash (QSPI). Die Settings bleiben unberührt (E4 gilt weiter). Nach meinem Lesen des Codes funktioniert der normale Settings-Store auf dem AC/DC ohnehin nicht, weil er memory-mapped Flash verlangt und das AC/DC kein internes Storage hat [Code, nicht geprüft].
  - Jeder Wechsel hängt 256 B an und markiert den alten Eintrag als gelöscht.
  - Unter 64 KB freiem Speicher wird nicht geschrieben, sonst würde `writeResource()` ein Defrag auslösen, das das ganze Flash löscht. Der Slot startet dann ohne Merken, die Eingangs-LEDs blinken 1 s rot.
  - Fehlt der Eintrag oder zeigt er auf einen leeren Slot, startet Slot 1, ersatzweise der erste belegte.
- **Host:** Schickt ein Rechner während des Menüs einen Program Change oder einen Upload, endet das Menü und `bootstrap()` startet nichts selbst.
- **Periodischer Pfad:** Dazu kommt nur die Abfrage `acdc_boot.led_hold` am Anfang von `acdcOnLoopLate` (5 Befehle). Solange sie gesetzt ist (Menü bzw. 1 s Slot-Anzeige), lässt `onLoop()` die LEDs in Ruhe. Der Zustand (2 Byte) liegt in `.late_bss`.
- Ein Program Change vom Rechner im Betrieb wird nicht gemerkt.

**Build:** `firmware/builds/acdc1-build6-fx4a/`, `v22.4.r-fx4a`, 108 496 B, SHA-256 `e7ee9b90ccd2cb2763e695dbab0bb82e5fa63c94c6e823e2e48dc3177ff2f063`. Patches wie fx3l + 15.

**Prüfung ohne Gerät [gemessen, D50]:**
- `tools/check_itcm.py`: BESTANDEN, 0 FAIL, 0 WARN. ITCM-Code +40 B, alle RAM-Objekte an derselben Adresse wie fx3l.
- `tools/sim_boot_menu.sh`: Der Menü-Code läuft unverändert auf dem Rechner gegen simulierte Regler. 18 Fälle: normaler Start, Auswahl, Abbruch, Timeout, Host, voller Speicher, Zittern an Zonengrenzen, 15 Slots, Lücken in den Slots.

**Abnahme nach dem Flash:**
1. Erledigt (D51): Endwerte der Regler gemessen, links 2 und rechts 127 von 127. Die Schwellen passen, kein Neubau. Flash mit bytegleichem Readback.
2. Erledigt (D52): A1 per `owl_read.py`, Version fx4a, Blockgröße 8, Slots 1–5 unverändert. Das Menü läuft (Nutzer), die Wahl von Slot 3 wurde einmal gemerkt (+256 B).
3. Erledigt (D53, D55): Normaler Start aus dem gemerkten Slot.
4. Erledigt (Nutzer, D52/D53, fx4a): Einstieg, Anzeige, Auswahl, Bestätigen, Abbruch mit Regler 3, Abbruch nach 60 s. Der 30-s-Timeout von fx4b ist am Gerät nicht gestoppt.
5. Erledigt (D52, D55, D58): Nach Aus/Ein startet der gewählte Slot (Slot 3, später 4 und 5).
6. Erledigt (D55): Start mit Reglern in Alltagsstellung (104 / 125 / 85 / 50) öffnet das Menü nicht.
7. Erledigt (D57, fx4b): Loop-Test mit `phase_slips.py` und `stale_samples.py`, 0 Slips, 0 veraltete Samples, auch mit Tanh3 bei 53 % CPU.
8. Erledigt (D58, fx4b): Rausch-A/B gegen fx3l in derselben Sitzung (fx4b → fx3l → fx4b, je 2 × 60 s). Alle Familien innerhalb ±0,4 dB, im Mittel ±0,2 dB. fx4b ist beim Rauschen gleich fx3l.

**Build 6b `v22.4.r-fx4b` (2026-11-17, D53/D55):** Nach der Abnahme des Menüs wünschte der Nutzer 30 s statt 60 s bis zum Abbruch. Patch `15b-boot-menu-slot-select-30s.patch` ersetzt 15 vollständig, einziger Unterschied ist `ACDC_MENU_TIMEOUT_MS`. `firmware/builds/acdc1-build6b-fx4b/`, 108 496 B, SHA-256 `a21f35c990cc33737620597d883c4bd205fc4495bf2291a1b6013af6f2b06307`. `check_itcm --same-itcm` gegen fx4a: ITCM-Code und Vektortabelle bytegleich. Geflasht 2026-11-17 (D55). Die offenen Punkte 7 und 8 der Abnahme (Loop-Test, Rausch-A/B) gelten für fx4b.

**Entscheidung (Nutzer, 2026-11-17, D59): fx4b ist die Alltags-Firmware von acdc1.**

**Fork-Branch `acdc/fx1d` (gepusht 2026-11-17):**
1. `7ef6284a` Boot-Menü (= Patch 15b)
2. `2c963e3a` Version `v22.4.r-fx4b`
3. `27d3630b` README: Abschnitt „Boot menu“, Tabellen und Teststand

Ein Build von `2c963e3a` ohne Patches ist bytegleich mit fx4b (`firmware/builds/verify-fx1d-2c963e3a`, `a21f35c9…`). Dazu das Release `acdc-v22.4.r-fx4b` (Tag auf `27d3630b`) mit `ACDC-v22.4.r-fx4b.bin` und `BUILD_INFO-v22.4.r-fx4b.txt`.

**Rückweg:** fx4a (`e7ee9b90…`), dann fx3l (`b55b94d8…`), danach wie bisher 3d.

### Build 7 – MIDI-Sendeweg unteilbar, `v22.4.r-fx5a` (Grill-Runde, Build und Abnahme 2026-11-18, messlog D62–D64, Alltags-Firmware auf acdc1 vom 2026-11-18 bis 2026-11-19)

**Anlass:** Läuft ein Patch und der Rechner lädt einen Slot herunter, kommen Daten beschädigt an, und das Gerät kann danach bis zum Neustart kein MIDI mehr senden (D53, D54). Auf fx4b reproduziert: 19 von 79 Downloads beschädigt, dann der Hänger (D62).

**Fehler im Original-Code [Code]** (in `upstream/master` gleich):
1. Audio-Task, Hauptschleife und USB-Interrupt schreiben in den Sendepuffer, ohne Schutz. Die Antworten auf SysEx-Anfragen entstehen im Interrupt.
2. `write()` ruft `transmit()` an jedem Pufferumlauf, der Audio-Task in jedem Block. `usbd_midi_tx()` sendet bei gesetzter Sperre nichts, der Lesezeiger rückt trotzdem vor.
3. Zwei Kontexte können zweimal auf demselben Endpoint starten [Hypothese: der Hänger].
4. Der Lesezeiger rückt beim Start der Übertragung vor, USB kopiert erst danach aus dem Ringpuffer.
5. `write()` prüft nie, ob der Puffer voll ist.
6. `SendResourceTask` schreibt alle 2 ms 324 B, ohne auf Platz zu warten.

**Entscheidungen (Nutzer, Grill-Runde 2026-11-18):**
- Prüfen, Starten und Merken der Übertragung unteilbar, per Interruptsperre, aus allen drei Kontexten nutzbar. „Nur ein Aufrufer“ reicht nicht, weil auch der Interrupt schreibt.
- Der Lesezeiger rückt erst nach Abschluss der Übertragung vor.
- Ein voller Puffer verwirft die neue Nachricht, statt Altes zu überschreiben.
- Flusskontrolle nur im `SendResourceTask`.
- Keine Rettung der Sperre per Zeitablauf. Tritt der Hänger wieder auf, bekommt er einen eigenen Patch.
- Verschachtelte Nachrichten (Antwort aus dem Interrupt mitten in einem SysEx der Hauptschleife) bleiben draußen.
- `transmit()` bleibt in Gruppe C des ITCM, das Rausch-A/B entscheidet. Rückfall: neuer Code ans Ende des ITCM-Blocks, Füllstück an die alte Stelle.

**Umsetzung (Patch `16-midi-tx-atomic.patch`) [Code]:**
- `Source/MidiWriter.cpp`, `UsbdMidiTransmitter`: Zugriffe auf den Pufferzustand mit gesperrten Interrupts (PRIMASK, wie Patch 05). `inflight` hält die Länge der laufenden Übertragung, der Lesezeiger rückt beim nächsten Aufruf nach gelöster Sperre vor. Der DataIn-Interrupt bleibt unverändert.
- `transmit()` verlässt den Leerlauf ohne Sperre: leerer Puffer, laufende Übertragung oder kein Rechner. Der Audio-Task sperrt nur in den Blöcken, in denen er etwas startet.
- `write()` ruft `transmit()` nur noch bei vollem Puffer, verwirft sonst und meldet einmal `midi tx ovf` (nur mit Rechner am USB).
- `usbd_midi_tx()` gibt zurück, ob gesendet wurde (`usbd_audio.cpp`, gleichlautend in `usbd_midi.c` für andere Geräte, dort ungeprüft).
- `Source/MidiController.cpp`, `SendResourceTask`: schreibt nur, wenn 324 B frei sind, sonst im nächsten Durchlauf. Nach 5 s ohne Platz gibt der Task auf.

**Build:** `firmware/builds/acdc1-build7-fx5a/`, `v22.4.r-fx5a`, 109 524 B, SHA-256 `b69c25b3f469fc6fb793b16569c53a63a7333c32d83c96de4d97b6fb71bdb8ef`. Patches wie fx4b + 16.

**Prüfung ohne Gerät [gemessen, D62]:** `tools/check_itcm.py --ref fx4b` BESTANDEN, 0 FAIL, 0 WARN. ITCM-Code +48 B (`transmit()` 76 → 124 B), alles dahinter im ITCM 48 B höher, Patch-Heap 48 B kleiner. 164 von 180 RAM-Objekten an derselben Adresse. Flash +1028 B.

**Abnahme:**
1. Erledigt (D63): Flash mit `tools/flash_acdc.py` (erster Einsatz am Gerät), Readback bytegleich, A1 bestanden.
2. Erledigt (D63): Download-Stresstest mit `tools/dump_stress.py`, 240 von 240 Downloads in Ordnung (TapeDelay 32 %, Tanh3 51 %, Tanh3 mit Audio-Stream), kein Hänger. fx4b in derselben Sitzung: 19 von 79 beschädigt, Hänger.
3. Erledigt (D63): Loop-Test mit `phase_slips.py` und `stale_samples.py`, 0 Slips, 0 veraltete Samples, auch mit Tanh3 und während 40 Downloads.
4. Erledigt, mit Einschränkung (D64): Rausch-A/B fx4b → fx5a → fx4b → fx5a, je 2 × 60 s. RMS, Rest, Kamm und fs/8 in jedem Block innerhalb ±0,5 dB. Mischprodukte im Mittel +0,70 dB bei 2,3 dB Streuung zwischen den beiden Kontrollen, also nicht entscheidbar. Kein Hinweis auf eine Wirkung des Patches.

**Entscheidung (Nutzer, 2026-11-18, D65): fx5a ist die Alltags-Firmware von acdc1.**

**Fork-Branch `acdc/fx1d` (gepusht 2026-11-18):**
1. `bd04588e` MIDI-Sendeweg (= Patch 16)
2. `c222fa49` Version `v22.4.r-fx5a`
3. `b4b95e43` README: Abschnitt „MIDI send path“, Tabellen und Teststand

Ein Build von `c222fa49` ohne Patches ist bytegleich mit fx5a (`firmware/builds/verify-fx1d-c222fa49`, `b69c25b3…`). Dazu das Release `acdc-v22.4.r-fx5a` (Tag auf `b4b95e43`, bis zum Release von fx7a „Latest“) mit `ACDC-v22.4.r-fx5a.bin` und `BUILD_INFO-v22.4.r-fx5a.txt`.

**Offen:** Kleine Störung auf Kanal 2 während Downloads (D63).

**Rückweg:** fx4b (`a21f35c9…`), dann fx3l (`b55b94d8…`), danach wie bisher.

### Build 8 – LED-Modus im Boot-Menü, `v22.4.r-fx6a` (Absprache und Build 2026-11-18, messlog D72–D77, **Abnahme vollständig, Rückweg von fx7a**)

**Anlass [gemessen, D73, D74]:** Jede leuchtende Eingangs-LED verschiebt den Nullpunkt aller Eingänge um etwa −2,9e-4 Vollausschlag (≈ −2,9 mV, −71 dBFS). Dauerlicht ist nur ein fester Versatz, jeder Wechsel ein Sprung, und eine gedimmte LED wiederholt den Sprung im Takt der PWM (2320,54 Hz): Das ist die LED-PWM-Linie. Die Pegel-LEDs folgen im Alltag dem Signal, die Störung steht damit in jeder Aufnahme.

**Entscheidungen (Nutzer, 2026-11-18):**
- Ein LED-Modus, im Boot-Menü über Regler 2 wählbar (Vorschlag des Nutzers: Regler 2 war dort noch frei) und gemerkt.
- Drei Modi: normal (wie bisher), nur Clip (alles dunkel, Rot nur, wenn beim Aufnehmen ein Eingang übersteuert), aus.
- Die PWM-Frequenz kommt getrennt danach in einem eigenen Build, damit sie einzeln messbar bleibt.
- Nicht in diesem Build: Rot bereinigen (in D73 war davon nichts messbar), ein Umschalter über MIDI im laufenden Betrieb.

**Umsetzung (Patch `17-led-mode-boot-menu.patch`, nur `ACDC/Core/Src/ACDC.cpp`) [Code]:**
- **Boot-Menü:** Regler 2 wählt den Modus, linkes Drittel normal, mittleres nur Clip, rechtes aus. Er zählt wie Regler 1 erst nach Bewegung (250 von 4096), sonst bleibt der gemerkte Modus. Die Ausgangs-LEDs zeigen den Modus (vier, zwei, keine leuchten) und blinken, wenn das Bestätigen Slot oder Modus ändert. Im Modus aus gibt es nichts, das blinken könnte. Abbruch (Regler 3, 30 s) und ein Rechner, der übernimmt, lassen den gemerkten Modus stehen.
- **Speichern:** eigene Ressource `ACDC.led` im Patch-Flash (4 Byte: Modus, ~Modus, 'L', 'D'), getrennt von `ACDC.slot`. fx5a und fx4b finden ihren Slot nach einem Rückweg weiter. Dieselbe Reserve wie beim Slot (64 KB frei): Sonst gilt der gewählte Modus nur bis zum nächsten Einschalten, die Eingangs-LEDs blinken 1 s rot. Die Settings bleiben unberührt.
- **Hauptschleife (alle 2 ms):** `onLoop()` ruft in den dunklen Modi `acdcOnLoopDark()` statt `acdcOnLoopLate()`. Die Funktion schaltet die acht LEDs einmal aus und schreibt danach kein Pin- und kein Timer-Register mehr, solange sich nichts ändert. Im Modus nur Clip misst sie beim Aufnehmen weiter die rohen Eingänge und schaltet eine Eingangs-LED für 300 ms rot (nur der statische Pin, Grün bleibt aus). Im Modus aus entfällt auch diese Messung. `PARAMETER_BA…BD` (Ausgangspegel) laufen in allen Modi weiter.
- **Menü und Slot-Anzeige** beim Einschalten nutzen die LEDs in jedem Modus.
- **Lage im Speicher:** `acdcOnLoopLate()` bleibt unverändert. `acdcOnLoopDark()` (292 B) und das größere `onLoop()` (24 B) liegen in `.text.onLoop` (im ITCM) und nehmen ihren Platz aus der Füllung, die dort seit 3d liegt (`ACDC_ONLOOP_PAD` 0x1cc → 0x94). `AcdcBootState` wächst von 2 auf 4 Byte (`.late_bss`).
- Der Zweig ohne `USE_USBD_AUDIO_TX_PRE_FX` kennt den Modus nicht. Er wird nicht gebaut.

**Build:** `firmware/builds/acdc1-build8-fx6a/`, `v22.4.r-fx6a`, 110 088 B, SHA-256 `6a3fc427b30ae1043b239f01e5ecf9894db92d9a6ca3dc51b47cc9a6f80260eb`. Patches wie fx5a + 17.

**Prüfung ohne Gerät [gemessen am Rechner]:**
- `tools/sim_boot_menu.sh`: 48 Fälle bestanden. 18 alte Menü-Fälle, 15 neue für Regler 2 (Wahl, Hysterese, Abbruch, Zeitablauf, Rechner übernimmt, voller Speicher, zwei Schreibvorgänge bei Slot und Modus) und 15 für die LED-Schleife (`firmware/sim/led_loop_sim.cpp`: was die Hauptschleife je Modus an die LEDs schreibt).
- `tools/check_itcm.py --ref fx5a`: BESTANDEN, 0 FAIL, 0 WARN. ITCM-Ende unverändert 0x6338, Patch-Heap unverändert 40 136 B, alle 180 RAM-Objekte an derselben Adresse.
- ITCM-Inhalt gegen fx5a: Alle Funktionen außerhalb von `.text.onLoop` (0x5de8–0x5fb7) liegen an derselben Adresse. 398 von 12 440 Bytes unterscheiden sich: 316 im neuen Code, der Rest in den Veneers und in Sprungzielen dorthin, weil sich Code im Flash verschoben hat. Flash +564 B.
- `tools/flash_acdc.py acdc1-build8-fx6a`: Offline-Prüfung bestanden.

**Abnahme (Stand D75, jeder Flash nur nach Freigabe):**
1. Erledigt (D75): Flash mit `tools/flash_acdc.py`, Readback bytegleich, A1 bestanden.
2. Zum Teil erledigt (D75): Der Nutzer hat aus und nur Clip über Regler 2 gewählt, die Ressource `ACDC.led` wurde angelegt (+256 B). Nach Aus und Ein ohne Menü ist ein dunkler Modus aktiv (Nachtrag 2026-11-19). Gemerkt ist nur Clip (Clip-Probe, zweiter Nachtrag). Offen: Anzeige auf den Ausgangs-LEDs laut Nutzer, Slot-Wahl wie bisher.
3. Zum Teil erledigt (D75): LED-Messung mit `owl/test/SchliereLedPathPatch.hpp`. Modus normal wie D74 (2–5 % mehr). Modus aus: Verschiebung auf 1,3–1,7 % mit umgekehrtem Vorzeichen, etwa −37 dB. Gemerkter dunkler Modus ohne Stream (Nachtrag 2026-11-19): Blinken 0,3 % von normal, statisch 0,6–2,2 %, der statische Rest streut. Nur Clip frisch aus dem Menü (dritter Nachtrag): ebenso ruhig, Blinken 0,4–0,5 %.
4. Zum Teil erledigt (D75): Modus nur Clip, negative Gleichspannungsrampe auf In 1. Als In 1 die Schwelle erreicht, springen die offenen Eingänge um −0,08…−0,15 mV, wie bei einer roten LED ohne Grün. Am 2026-11-19 im gemerkten Modus wiederholt: Sprung −0,2 mV, in beiden Aufnahmen innerhalb von 2 ms an der Clip-Schwelle der Firmware und 220 ms vor dem Anschlag des Wandlers. Der Sprung ist also die rote LED, die Gegenprobe im Modus aus entfällt als Pflicht. Bei einer Wiederholung hat der Nutzer die rote LED gesehen. Punkt erledigt bis auf die Höhe des Sprungs (am Vorabend halb so groß).
5. Rausch-A/B gegen fx5a in derselben Sitzung (Modus normal), Kontrolle am Anfang und Ende, je 2 × 60 s. Dazu Loop-Test (`phase_slips.py`, `stale_samples.py`) und `dump_stress.py`. Erledigt am 2026-11-19: `dump_stress.py` ohne Stream, 240 von 240 Downloads in Ordnung (D75, vierter Nachtrag). Loop-Test bestanden, auch mit Tanh3 und während 48 Downloads (D76). Rausch-A/B (D77): kein Hinweis auf einen Unterschied, fx5a liegt zwischen den beiden fx6a-Kontrollen, die Sitzung driftet um 2 dB. Nebenbei gefunden: Ein Program Change bei offenem Stream bricht die USB-Wiedergabe (D76), unter fx5a genauso (D77), also älter als Build 8. **Abnahme vollständig.** Als Alltags-Firmware hat der Nutzer danach fx7a gewählt (2026-11-19), fx6a ist der Rückweg.

**Danach geplant (eigener Build):** PWM der LEDs mit genau 48 000 Hz (Timer-Vorteiler 4, 1000 Stufen statt 2320,54 Hz mit 1024 Stufen). [Hypothese] Die Schaltfrequenz liegt dann über dem Hörbereich und im Takt der Abtastung, die Linie verschwindet. Risiko: zwanzigmal so viele Schaltflanken. Die langsame Verschiebung des Nullpunkts mit der Helligkeit bleibt. → Build 9.

**Rückweg:** fx5a (`b69c25b3…`), dann fx4b (`a21f35c9…`), danach wie bisher. Die Ressource `ACDC.led` stört ältere Builds nicht.

### Build 9 – LED-PWM mit 48 kHz, `v22.4.r-fx7a` (Absprache und Build 2026-11-19, messlog D78, D79, Alltags-Firmware auf acdc1 2026-11-19 bis 23, **Rückweg von fx8a**)

**Anlass [gemessen, D67, D73, D74]:** Eine gedimmte LED schaltet die Verschiebung des Nullpunkts im Takt der PWM, das ist die Linie bei 2320,54 Hz mit Vielfachen in Ein- und Ausgängen (bis −39,8 dBFS am UMC mit gedimmtem Grün, D73). Build 8 lässt die LEDs dunkel schalten, Build 9 legt die PWM selbst aus dem Hörbereich. Getrennt gebaut, damit die Wirkung einzeln messbar bleibt (Entscheidung des Nutzers, 2026-11-18).

**Takt [Code]:**
- Timer: HSE 8 MHz, PLL1 × 120 / 2 = 480 MHz Systemtakt, AHB /2, APB1 und APB2 /2 = 120 MHz, Timer-Takt ×2 = 240 MHz. Passt zu den gemessenen 2320,54 Hz = 240 MHz / (101 × 1024) (D60).
- Audio: SAI1 aus PLL3 (8 MHz / 7 × (172 + 262/8192) / 8 = 24,576 MHz), SAI1 Block A ist Master (`SAI_MODEMASTER_RX`), der Codec Slave, Frame 256 Bit. fs ≈ 47 999,995 Hz (gemessen „exakt 48 kHz“, D10).
- Beide stammen aus demselben Quarz. Mit Vorteiler 4 und Period 999 läuft die PWM mit 240 MHz / 5000 = 48 000,000 Hz, 0,1 ppm (0,0049 Hz) über fs. Eine Drift des Quarzes trifft beide gleich. [Hypothese] Was von der PWM in die ADC-Daten faltet, landet bei ≈ 0 Hz (Schwebung alle 204 s) statt bei 2321 Hz mit Vielfachen. 48 kHz selbst liegt im Sperrbereich des Dezimationsfilters im Codec.

**Wer nutzt die Timer [Code]:** Nur `MX_TIM2/3/4/8_Init()` in `main.c`, `initLed()` (Start der acht Kanäle) und `setLed()` (`CCR`). Kein Code liest `ARR`, `CNT` oder `PSC`. Die `htim8`-Stellen in `Source/Codec.cpp` gehören zu anderen Codecs (`USE_IIS3DWB`, `USE_ADS1294`) und werden für das AC/DC nicht gebaut. Die Simulatoren rechnen nicht mit PWM-Werten.

**Entscheidung (Nutzer, 2026-11-19): Variante A, nur der Timer-Init.** `setLed()` liegt im ITCM (0x5cd8, 204 B) vor `.text.onLoop`, jede Änderung dort verschöbe die Adressen dahinter. Variante B (genaue Umrechnung auf 1000 Stufen in `setLed()`) ist deshalb verworfen.

**Umsetzung (Patch `18-led-pwm-48k.patch`, nur `ACDC/Core/Src/main.c`) [Code]:**
- TIM2, TIM3, TIM4, TIM8: Vorteiler 100 → 4, Period 1023 → 999.
- `setLed()` bleibt: `pwm = 1024 − v` mit v = 0…1023, Modus PWM1, LED leuchtet bei CNT ≥ CCR. CCR ≥ 1000 liegt über ARR, die LED bleibt dauerhaft aus: also NO_COLOUR und alle Werte v ≤ 24 (unter 2,4 %). v = 1023 gibt CCR = 1, also 999/1000 an. Darüber ist die Helligkeit (v − 24)/1000 statt v/1024, höchstens 2,4 % daneben. „Aus“ bleibt aus, nichts läuft über. Rot (statischer Pin) ist unberührt.
- Folge: Ganz schwach glimmende Pegel-LEDs gehen aus. Patches, die LEDs mit unter 2,4 % setzen, zeigen nichts mehr.

**Build:** `firmware/builds/acdc1-build9-fx7a/`, `v22.4.r-fx7a`, 110 088 B (wie fx6a), SHA-256 `cac6fee0f86426aed3d9b5bfaa2ff758b69de59ed7e11971f2a2ba0d0233ff20`. Patches wie fx6a + 18.

**Prüfung ohne Gerät [gemessen am Rechner, 2026-11-19]:**
- `tools/check_itcm.py --ref fx6a --same-itcm fx6a`: BESTANDEN, 0 FAIL, 0 WARN. ITCM-Grenzen 0x32a0–0x6338 gleich, `.itcm_text` (12 440 B) und Vektortabelle bytegleich, alle 656 Flash-Funktionen und 180 RAM-Objekte an derselben Adresse.
- Binary gegen fx6a: 113 Bytes verschieden, alle in `main()` (Timer-Init, gleiche Länge, `movs #4` / `movw #999` statt `#100` / `#1023`) und eines im Versions-String.
- `tools/sim_boot_menu.sh`: alle Fälle bestanden (Boot-Menü und LED-Schleife, unverändert gegen fx6a).
- `tools/flash_acdc.py acdc1-build9-fx7a`: Offline-Prüfung bestanden.

**Risiken [Hypothese]:** zwanzigmal so viele Schaltflanken (ob hochfrequent mehr einstreut, zeigt nur die Messung). Die Verschiebung des Nullpunkts mit der mittleren Helligkeit bleibt (−2,9e-4 je LED, D74). 48 kHz direkt am Ausgang (≈ 0,15 mV je LED, D74) ist unhörbar, am UMC fiele ein Rest wegen dessen eigenen Takts auf wenige Hz. Die Schwebung von 204 s kann den Gleichanteil sehr langsam wandern lassen.

**Abnahme (jeder Flash nur nach Freigabe, nur acdc1):**
1. Erledigt (D78): Flash mit `tools/flash_acdc.py acdc1-build9-fx7a --yes`, Readback bytegleich, Neustart durch den Nutzer, A1 bestanden. In D79 zweimal per `:leave` neu gestartet (fx6a und zurück).
2. Erledigt (D78): LED-Linie am Ausgang mit `owl/test/SchliereLedTestPatch.hpp`, Phase „grün 60 %“: **keine Linie mehr** bei 2321 Hz und Vielfachen (−85,2 dBFS im Rauschen gegen −39,8 dBFS unter fx5a, D73), keine neue Linie, auch nicht unter 20 Hz.
3. Erledigt (D78): LED-Verschiebung an den Eingängen mit `owl/test/SchliereLedPathPatch.hpp`: gleich wie fx6a in D77 (±2 %), wie erwartet.
4. Erledigt (D79): Rauschen gegen fx6a, Kontrolle am Anfang und Ende: fx7a am Ende innerhalb von 0,15 dB bei fx6a, die LED-PWM-Linie fehlt auch in den rohen Eingängen (fx6a: −115 dB). Die Kontrolle am Anfang liegt beim Kamm 1,9 dB tiefer, eine Kaltstart-Probe zeigt: Drift der Sitzung. Loop-Test bestanden (D79): 0 Slips, 0 veraltete Samples. **Abnahme vollständig. fx7a ist die Alltags-Firmware (Entscheidung des Nutzers, 2026-11-19).**
5. Erledigt (D78): Helligkeit der LEDs am Gerät laut Nutzer in Ordnung („led helligkeit passt“).

**Fork-Branch `acdc/fx1d` (gepusht 2026-11-19):**
1. `1cf56d3e` LED-Modus (= Patch 17)
2. `34782dea` Version `v22.4.r-fx6a`
3. `bd5ee463` LED-PWM mit 48 kHz (= Patch 18)
4. `351b2071` Version `v22.4.r-fx7a`
5. `13b58412` README: Abschnitt „LEDs: mode and PWM rate“, Tabellen, Teststand, `:leave` im Flash-Ablauf

Builds von `34782dea` und `351b2071` ohne Patches sind bytegleich mit fx6a (`firmware/builds/verify-fx1d-34782dea`, `6a3fc427…`) und fx7a (`verify-fx1d-351b2071`, `cac6fee0…`). Dazu das Release `acdc-v22.4.r-fx7a` (Tag auf `13b58412`, „Latest“, 2026-11-19) mit `ACDC-v22.4.r-fx7a.bin` und `BUILD_INFO-v22.4.r-fx7a.txt`. fx6a hat kein eigenes Release.

**Rückweg:** fx6a (`6a3fc427…`), dann fx5a (`b69c25b3…`), danach wie bisher.

### Build 10 – Befehls-Cache an, `v22.4.r-fx8a` (Build 2026-11-23, messlog D83–D85, **Alltags-Firmware auf acdc1 seit 2026-11-23**)

**Anlass [Code, gemessen, D83]:** `ACDC/Core/Inc/hardware.h` setzt `USE_ICACHE` und `USE_DCACHE` nur `#ifdef NDEBUG`, `Hardware/owl3.mk` setzt im Release-Build nur `-O3`, nie `-DNDEBUG`. Das gilt auch für v22.5.0 und den Upstream-`master`. Unter fx7a meldet SCB->CCR auf acdc1 0, beide Caches sind aus. Plateau braucht dadurch 5000 Takte pro Sample bei rund 1000 Befehlen, alle Abschnitte gleichmäßig etwa fünfmal zu langsam.

**Umsetzung (Patch `19-icache-on.patch`) [Code]:**
- `hardware.h`: `USE_ICACHE` immer, `USE_DCACHE` bleibt hinter `NDEBUG`, also aus.
- `Source/mpu.c`: Die MPU-Region für die DMA-Puffer nur noch mit `USE_DCACHE` statt mit `USE_ICACHE || USE_DCACHE`. Sie betrifft nur Daten, und das Symbol `_DMA_DATA` fehlt im Linker-Skript des ACDC (sonst Link-Fehler).
- Was `USE_ICACHE` sonst schaltet: `SCB_InvalidateICache()` und `SCB_EnableICache()` in `main()` vor `HAL_Init`, `device_cache_invalidate()` (invalidiert den I-Cache; `PatchDefinition.hpp` ruft es nach dem Kopieren eines Patches und vor seinem Start), `device_reset_to()` vor dem Sprung in den Bootloader.
- Warteschleifen über Befehlszahl gibt es im ACDC-Pfad nicht: Der Codec-Init wartet mit `HAL_Delay` (SysTick), `NopDelay` steckt nur im nicht gebauten CS4272-Treiber.

**Was schneller wird [Hypothese]:** Firmware-Code im internen Flash (Hauptschleife, MIDI, Speicher) und Patches im AXI-SRAM (Link plusram, z. B. Plateau). ITCM und DTCM laufen am Cache vorbei. Der heiße Pfad im ITCM ändert sich also nicht, und Patches mit Link patchram (0x2000c000, im DTCM, Standard der Patch-Library und aller bisherigen eigenen Slots) holen ihre Befehle weiter ohne Cache. Für sie hilft erst der Link plusram.

**Build:** `firmware/builds/acdc1-build10-fx8a/`, `v22.4.r-fx8a`, 110 208 B (+120 B), SHA-256 `e1b1097b21008486acc4cda4b446a0e72fcd2e974ef0f5b97c6a707e6086f39a`. Patches wie fx7a + 19.

**Prüfung ohne Gerät [gemessen am Rechner, 2026-11-23]:**
- `tools/check_itcm.py --same-itcm fx7a`: BESTANDEN, 0 FAIL, 0 WARN. ITCM-Grenzen 0x32a0–0x6338 gleich, `.itcm_text` (12 440 B) und Vektortabelle bytegleich, alle 180 RAM-Objekte an derselben Adresse. Von 656 Flash-Funktionen liegen 178 an derselben Adresse, 430 um 0x78 verschoben, der Rest um 0x48–0x5c.
- Disassembly: `main()` beginnt mit ICIALLU und dem Setzen von CCR.IC (CMSIS `SCB_EnableICache`), `device_cache_invalidate()` invalidiert den I-Cache (unter fx7a leer). `MPU_Config` gleich wie fx7a bis auf Adressen, nur die QSPI-Region.
- `tools/flash_acdc.py acdc1-build10-fx8a`: Offline-Prüfung bestanden.

**Risiken [Hypothese]:** Die Flash-Lage hat seit dem ITCM-Build keinen Einfluss mehr auf die Linien gezeigt (D48), mit dem Cache ändert sich aber der Busverkehr des übrigen Firmware-Codes. Die Linien können sich deshalb in beide Richtungen bewegen, fs/8 eher nach unten (D42). Ein Patch-Wechsel ohne Invalidieren ließe alten Code laufen: Der Aufruf ist da, geprüft wird er am Gerät durch wiederholte Wechsel zwischen Slots und RAM-Patches.

**Abnahme (jeder Flash nur nach Freigabe, nur acdc1):**
1. Erledigt (D84): Flash mit `tools/flash_acdc.py acdc1-build10-fx8a --yes`, Readback bytegleich, `:leave` (erstmals aus dem Skript am Gerät), A1 bestanden.
2. Erledigt (D84): Cache-Bits 2. PlateauProfile 3540 statt 5050 Takte pro Sample, Plateau 35 % statt 51 %. Leseschleife TCM 5–6, AXI 15, SDRAM 46 Takte. Slots (patchram) wie vorher, bei nicht gleichen Reglerstellungen.
3. Erledigt (D84): Program Change durch alle zwölf Slots, `--run` von Plateau und PlateauProfile im Wechsel, alles läuft und meldet sich.
4. Erledigt (D84): Download-Stresstest 240 von 240 in Ordnung.
5. Erledigt (D85): Rauschen gegen fx7a (fx8a am Anfang und Ende, fx7a in der Mitte): **fs/8 +0,6 dB** in allen vier fx8a-Läufen, Mischprodukte +1…+3,4 dB, RMS, Rest und Kamm gleich. Keine neue Linie. Loop-Test bestanden (0 Slips, 0 veraltete Samples). **Abnahme vollständig. fx8a ist die Alltags-Firmware (Entscheidung des Nutzers, 2026-11-23).**

**Fork-Branch `acdc/fx1d` (gepusht 2026-11-23, `13b58412..21442efd`):**
1. `8a401e75` Befehls-Cache an (= Patch 19)
2. `f9f9399a` Version `v22.4.r-fx8a`
3. `21442efd` README: Abschnitt „Instruction cache“, Tabellen, Teststand, Hinweis in „Memory layout matters“

Ein Build von `f9f9399a` ohne Patches ist bytegleich mit fx8a (`firmware/builds/verify-fx1d-f9f9399a`, `e1b1097b…`). Dazu das Release `acdc-v22.4.r-fx8a` (Tag auf `21442efd`, „Latest“, 2026-11-23) mit `ACDC-v22.4.r-fx8a.bin` und `BUILD_INFO-v22.4.r-fx8a.txt` aus dem Prüf-Build.

**Rückweg:** fx7a (`cac6fee0…`), dann fx6a, danach wie bisher.

### Fork `m9dfukc/OpenWare` (gepusht 2026-11-14: https://github.com/m9dfukc/OpenWare/tree/acdc/thru-usb-feedback)

- **Lokaler Klon:** `firmware/OpenWare`. Vorbereitet wurde der Branch in einem separaten Klon `firmware/fork/OpenWare`. Beim Aufräumen (2026-11-14) wurden beide zusammengelegt: `upstream` geholt, geprüft, dass alle 55 Refs, 27 Branches, 27 Tags und alle Commits des alten Spiegels enthalten sind, dann den Spiegel gelöscht und den Fork-Klon nach `firmware/OpenWare` verschoben. Remotes:
  - `fork` = `git@github.com:m9dfukc/OpenWare.git`
  - `upstream` = RebelTechnology (alle Branches als `upstream/*`)
- **Branch `acdc/thru-usb-feedback`** ab `db9d3dd` (v22.4.r, Hack-Branch `hack/acdc-output-levels`, Submodul Libraries `9e8f64e`). Commits in dieser Reihenfolge:
  1. `85dd465c` GCC 12 (Patch 01)
  2. `21837c5d` Revert `237c63d` (02)
  3. `3cfa66dd` atomarer RX-Zähler (05)
  4. `174ef59a` Ausgang 125 (04)
  5. `6753794f` Feedback-Regelung (06)
  6. `06430d10` Version `v22.4.r-thru1d`
  7. `41fb9480` README (englisch, gepusht 2026-11-15). Aufbau wie bei `acdc/fx1d`, aber mit Standard-Routing (Rechner nimmt den Patch-Ausgang auf) und Messwerten von 1d (D24, Geräte-dBFS)

  Commit-Texte und Code-Kommentare sind englisch. Autor ist die globale git-Identität des Nutzers, dazu ein Co-Authored-By-Trailer.
- **Prüfung:** Der Baum der Branch-Spitze ist gleich dem Quellbaum von Build 1d (damals `firmware/build/acdc1-build1d-thru1`, beim Aufräumen 2026-11-14 gelöscht, mit `tools/build_acdc.sh` neu erzeugbar). Er unterscheidet sich nur in Kommentaren (`usbd_audio.cpp`, `hardware.h`), der Code ohne Kommentare ist identisch, die Zeilenzahlen sind gleich. `usbd_audio.cpp` hat CRLF-Zeilenenden, die bleiben erhalten. Ein Build aus dem Branch zur Bestätigung der SHA steht noch aus (Freigabe).
- **Push (Nutzer bzw. nach Freigabe):** `git -C firmware/OpenWare push -u fork acdc/thru-usb-feedback`. Der Push lädt die Hack-Branch-Commits bis `db9d3dd` mit hoch, auch wenn der Fork nur `master` enthält.
- **Für einen PR gegen upstream** müssten 01, 05 und 06 auf `master` (v22.5.0, neues HAL) portiert und dort getestet werden (Option A). 02 und 04 sind acdc-spezifisch und gehören nur in den Fork.

### Reihenfolge

1. Toolchain installieren (Nutzer), `tools/build_acdc.sh` schreiben, Reproduktions-Build + Vergleich mit dem Readback.
2. Build 1 und Build 2 bauen (noch kein Flash).
3. Vorbedingungen E7: Boot-Pad-Probe, Referenzaufnahme, Generalprobe. Generalprobe nur nach Freigabe.
4. Build 1 flashen (Freigabe) → A1–A7.
5. Build 2 flashen (Freigabe) → A1–A6, B1–B3. **Erledigt 2026-11-15:** `v22.4.r-fx1d` (1d-Basis), alle Abnahmen bestanden (D25–D27).
6. Rausch-Experimente (E3). **Stand 2026-11-16:** Statt E3 kamen die Lage im Speicher (Build 3, D33) und der heiße Pfad im ITCM (Build 4 und 5, fx3l). Blockgröße 16, LED-PWM und Codec-HPF sind offen.
7. Option A: v22.5.0 bzw. Upstream-`master` + altes HAL + shmuga-Fixes + `TX_PRE_FX`, Abnahme wie Build 2 und Vergleich mit fx3l. Bleibt für später auf dem Plan.
8. Auto-Switching (offen). Öffentlicher Fork: erledigt, Branches `acdc/thru-usb-feedback` und `acdc/fx1d`.

### Verworfen bzw. überholt

- Das frühere Build-Rezept (v22.5.0 + `5a3f964` + `TX_PRE_FX` als erster Build) ist durch E1/E2 ersetzt und lebt als Option A weiter.
- Der „Null-Aufwand-Vortest“ ist erledigt (negativ, 2026-11-14), weil die Firmware auf acdc1 `237c63d` enthält.
- „Release-`ACDC.bin` als bekannt gutes Binary sichern“: Sie ist kein sicherer Rückweg (USB-Bruch). Der Rückweg ist das DFU-Readback.

## Flashen – allgemeine Hinweise

- Weg 1: OpenOCD über ST-Link (`program ACDC.bin 0x08000000 verify reset exit`, Konfiguration stlink + stm32h7x, Thread #2083 #15/#28). Im Projekt nie benutzt. Mit einem ST-Link lässt sich die Firmware über SWD auch debuggen (Anschluss J1 auf dem Xibeca-Board, 2×5 Pins im 1,27-mm-Raster, beim SWD-Flashen das Geräte-USB abziehen, Thread 2083 #19). Programmer: [STLINK-V3MINIE](https://www.st.com/en/development-tools/stlink-v3minie.html), Software: [OpenOCD](https://openocd.org/).
- Weg 2: ST-ROM-DFU, entweder per SysEx `0x7E` (`owl_read.py --reset-to-dfu`, entspricht „Reset to bootloader“ auf openwarelab.org/Tools/firmware.html) oder über die Boot-Pads beim Einschalten. Das AC/DC (Xibeca) hat **keinen** OWL-MIDI-Bootloader, nur den ROM-DFU.
- Der ROM-DFU ist nicht überschreibbar, echtes Bricking ist damit praktisch ausgeschlossen. Riskant ist ein Build mit kaputtem USB: Dann geht nur noch Boot-Pad/DFU oder SWD.
- Nur acdc1 (Testgerät) flashen. acdc2 (DIY, v22.4.q) bleibt Referenz.

## Langfristig

Ein sauberer, öffentlicher ACDC-Branch mit TX_PRE_FX, USB-Fixes, dokumentiertem Libraries-Stand, LED-PWM außerhalb des Audiobands und Messdaten wäre das, was dem Forum fehlt.

**Stand 2026-11-16:** Der Branch `acdc/fx1d` im Fork hat das bis auf die LED-PWM (README mit Messwerten, Spitze `b7062ef2`). Die Forum-Posts in Thread #2072 und #2244 entfallen (Nutzer 2026-11-16). Eventuell kommen die Ergebnisse stattdessen als GitHub-Issue (`TODO.md`).

## DFU-Readback acdc1 (vorbereitet 2026-11-14)

Ziel: Die Firmware von acdc1 rein lesend sichern. Sie ist vermutlich ein nicht öffentlicher Build mit funktionierendem USB (siehe `messlog.md` D2, `docs/research/notes/firmware_update_threads_2026-11-14.md`). Danach Vergleich mit der Release-`ACDC.bin` (`firmware/releases/v22.5.0/ACDC.bin`, 109 080 B, SHA-256 `5f44a811…892c2b`).

Werkzeuge (alle im Projekt, nur lesend außer dem DFU-Neustart):
- `tools/owl_read.py --reset-to-dfu --yes`: sendet SysEx `0x7E` → `device_dfu()` (Magic-Wort + Reset → ROM-DFU) [Code]. Bricht ab, wenn nicht acdc1 verbunden ist.
- `tools/dfu_readback.sh`: nur `dfu-util -l` und `dfu-util -U` (128 KB ab `0x08000000`), überschreibt nichts. Ablage: `backup/acdc1/<datum>/`.
- `tools/compare_firmware.py <readback> <release>`: SHA-256, Byte-Diff, Vektortabelle, Versions-Strings.

Ablauf:
1. Nutzer: `dfu-util` installieren.
2. OWL-Webseiten zu, Audio-Software zu. Nur acdc1 per USB am Rechner.
3. `owl_read.py --reset-to-dfu --yes` (außerhalb des Sandbox, wegen CoreMIDI). Das AC/DC verschwindet als Audio-/MIDI-Gerät.
4. `dfu_readback.sh` (außerhalb des Sandbox, wegen USB). Erscheint kein `0483:df11`: USB vorne ab, Micro-USB hinten am Xibeca-Board probieren. **Nie beide gleichzeitig.** Notfalls die Boot-Pads.
5. Case aus **und USB-Kabel ab**, ein paar Sekunden warten, Case an, dann USB wieder dran → normale Firmware. Nur Case aus/an reicht nicht, weil das USB-Kabel das Xibeca-Board weiter versorgt und es im DFU bleibt (gemessen 2026-11-14, vgl. Thread 2083 #7). Mit `owl_read.py` prüfen, dass acdc1 wieder „v22.5.0“ meldet und Slot 1 läuft.
6. `compare_firmware.py` ausführen, Ergebnis in den Messlog (D3).

Risiken: Ist RDP Level 1 aktiv, schlägt `-U` fehl. Dann keinen RDP-Wechsel versuchen, denn der löscht das Flash. Weiter nur per SWD. Kein `-D`, kein `:leave`, keine Option-Bytes schreiben. Das QSPI-Flash (Patches, Settings) erreicht der ROM-DFU nicht. Die Patches sind per SysEx gesichert (D1).
