# Übergabe – Fehlersuche fx3i (USB-Playback) per Varianten (Stand 2026-11-16 spätabends)

Für eine neue Session. Ersetzt `uebergabe-2026-11-16-itcm.md` als aktuelle Übergabe (die bleibt für die Bau-Details gültig). Antworte auf Deutsch.

**Auftrag:** Herausfinden, warum Build 4 `v22.4.r-fx3i` (heißer Pfad im ITCM) das USB-Playback stört, und zwar durch **Varianten, die nur Teile ins ITCM legen** (Halbieren). Bauen, mit `tools/check_itcm.py` prüfen, dann mit dem Nutzer je Variante den **60-s-Loop-Test** fahren. Erst wenn eine Variante sauber ist (0 Slips), wieder Rauschmessung und Füllvariante (fx3ip). **Nicht flashen ohne Freigabe**, jeder Flash einzeln.

## Zuerst lesen

1. `CLAUDE.md`, Abschnitte „Build 3d“, „Build 4“ und „Konventionen“. Aufnahmen laufen mit `tools/acdc_rec.py`, das jetzt auch `--sine` und `--dc` kann.
2. `docs/messlog.md`, **D36–D38**. Das ist der Messstand dieser Sitzung.
3. `docs/05-firmware-plan.md`, „Build 4“: die Abschnitte „Umsetzung“ und „Ergebnis der Sitzung“.
4. `firmware/patches/11-itcm-hotpath.patch` (Linkerskript-Muster, Gruppen A–H, Anker, Startup) und `firmware/builds/acdc1-build4-fx3i/check_itcm.md` (Veneers, Literale, Anker).
5. Bei Bedarf `docs/uebergaben/uebergabe-2026-11-16-itcm.md`, Abschnitt „Fakten für den Build“ (Speicher, Startup, Laufzeit).

## Stand

- **acdc1 läuft mit 3d** `v22.4.r-fx2d` (`d212cf8d…`). Er wurde nach fx3i zurückgeflasht, der Readback ist bytegleich, A1 bestanden. acdc2 wird nie angefasst.
- **Builds** (geprüft, in `firmware/builds/`):
  - `acdc1-build4-fx3i`: `8fedebf7…`, 107 304 B, Patches 01 02 04 05 06 03 07d 08 11.
  - `acdc1-build4p-fx3ip`: `d2b36d84…`, dazu 91, nie geflasht.
- **Messung D37:** fx3i gegenüber dem Mittel zweier 3d-Kontrollen: fs/8 **−5,06 dB**, RMS −0,98, Rest −0,89, Mischprodukte −0,54, Kamm ±0. Das ist der größte Effekt bisher und der Grund, den Fehler zu beheben statt ITCM aufzugeben.
- **Fehler D38:**

  | Loop 60 s (Out n → In n, Sinus 440/530/670/790, −6 dBFS) | 3d | fx3i |
  |---|---|---|
  | Slips (alle Kanäle gleichzeitig) | 0 | 28, alle negativ, 1–22 Samples |
  | Phasenrauschen (MAD) | 0,01 mrad | 0,31–1,04 mrad |
  | Amplituden-Spanne | 0,00 dB | 0,36–1,0 dB, Kanal 4 −1,1 dB |
  | Meldung | `fb 48.0004 96.2578` (harmlos) | `fb clamp −208 32` |
  | CPU mit Stream | 15 % | 7–8 % |

  - Störstellen bis 54 ms mit vermischten oder veralteten Samples (z. B. …430, 23, 403, 458, 425…). Das deutet auf vertauschte Kanäle oder alte Puffer hin.
  - `fb clamp −195…−208`: Der RX-Füllstand nach dem Paket liegt ≈ 1 OUT-Paket (192 Samples = 1 ms) unter dem Soll 384. Der Regler aus Patch 06 (±40 ppm) kommt nicht hinterher.
  - Auch in den Rauschläufen meldet fx3i `fb clamp` (Playback mit Nullen), der Fehler läuft dort also mit.
- **Code und RAM-Adressen** von fx3i sind bis auf Lage, Veneers, `Reset_Handler` (Kopien + VTOR) und Linkerskript gleich wie in 3d. Alle 176 RAM-Objekte liegen an derselben Adresse. Es muss also ein Timing- oder Platzierungs-Effekt sein.

## Hypothesen (alle ungeprüft)

- H-a **Verlorene ISO-OUT-Pakete:** `USB_EPStartXfer` wählt beim Neu-Aufsetzen des OUT-Endpunkts die Frame-Parität (gerade/ungerade) anhand von `DSTS` bit 8. Liegt der Aufruf in einem anderen Frame, verwirft der Kern das nächste Paket. Dagegen spricht, dass schnellerer Code eher früher dran ist.
- H-b **Wettlauf zwischen USB-ISR und Audio-Task** um `rx_buffer` (CircularBuffer) bzw. die Füllstandsmessung `rx_buffer.getReadCapacity() − codec.getSampleCounter()` (Patch 06, in `USBD_AUDIO_DataOut`). Durch das neue Timing tritt er häufiger auf.
- H-c **Kanalversatz** im RX-Puffer: Schreib- oder Lesezeiger nicht auf 4-Kanal-Rahmen (Startposition, `len` nicht durch 4 teilbar, Unterlauf-Pfad in `usbd_rx_convert` mit `memset` + `len = cap`). Das würde das gemischte Signal und Kanal 4 −1,1 dB erklären.
- H-d **Halbe CPU-Last mit Stream:** Entweder nur Flash-Wartezyklen bzw. I-Cache-Fehlgriffe, die wegfallen, oder ein Teil der USB-Arbeit läuft gar nicht. Prüfen, wie `CPU:` gemessen wird (`ProgramManager::getCyclesPerBlock`, zählt ISRs mit?).
- H-e Etwas an der Vektortabelle oder VTOR. Unwahrscheinlich, aber billig zu testen (Variante ohne Vektorkopie).

Vor dem Bauen den Code zu H-b/H-c lesen: `Source/usbd_audio.cpp` (`USBD_AUDIO_DataOut`, `usbd_audio_sof_callback`, `USBD_AUDIO_IsoOutIncomplete`), `Source/ProgramManager.cpp` (`usbd_rx_convert`, `usbd_audio_get_rx_count`, `audioCallback`), `Source/CircularBuffer.h`, HAL `stm32h7xx_hal_pcd.c` (ISO OUT, `INCOMPISOOUT`) und `stm32h7xx_ll_usb.c` (`USB_EPStartXfer`). Arbeitsbaum mit allen Patches: `firmware/_work/acdc1-build4-fx3i/` (Wegwerf, `usbd_audio.cpp` hat CRLF).

## Varianten (Vorschlag, mit dem Nutzer abstimmen)

Alle auf Basis 3d + 08 + einer **eigenen Variante von Patch 11**. Patch 11 bleibt unverändert. Neue Patches z. B. `11a-…`, `11b-…`, jeweils als vollständige Alternative zu 11 (nicht zusätzlich anwenden). `FW_VERSION` nur `[A-Za-z0-9._-]`.

| Variante | ITCM-Inhalt | Zweck |
|---|---|---|
| `fx3i-noD` | Gruppen A B C E F G H, **ohne D** (USB-ISR, USBD, Audio-Klasse, Feedback) | Liegt der Fehler am USB-Code im ITCM? |
| `fx3i-noC` | ohne C (Audio-Task: `onProgramReady`, `usbd_tx/rx_convert` …) | Wettlauf ISR ↔ Audio-Task (H-b) |
| `fx3i-onlyD` | nur D (+ Vektorkopie) | Gegenprobe zu noD |
| `fx3i-novt` | wie fx3i, aber ohne Vektorkopie/VTOR | H-e, billig |

- Reihenfolge nach Aufwand: noD und noC zuerst. Je nach Ergebnis D weiter teilen, z. B. nur OUT-Pfad (`DataOut`, `PrepareReceive`, `EP_Receive`, `EPStartXfer`, `ReadPacket`) oder nur SOF/Feedback.
- Pro Variante: bauen mit `tools/build_acdc.sh` (Namen `acdc1-build4x-<variante>`, bestehende Builds nie überschreiben).
- `tools/check_itcm.py` muss Gruppen ausnehmen können, z. B. eine neue Option `--groups A,B,C…`. Heute ist die Hotlist fest im Skript, ebenso die Liste COLD mit den erlaubten Sprüngen aus dem ITCM.
  - Bei Varianten springt der ITCM-Code in Flash-Funktionen, die in fx3i im ITCM lagen. Diese Sprünge sind dann gewollt, als eigene Kategorie zulassen.
  - Der Anker ist nur für Füllvarianten nötig, bei Halbierungs-Varianten genügt eine Warnung.
- Optional für H-b/H-c: ein Diagnose-Build mit Zählern (Unterläufe, Überläufe, `INCOMPISOOUT`-Ereignisse, Paketlängen ≠ 192) in `.late_bss`, auslesbar per `PROGRAM_MESSAGE`. Nur mit Absprache, denn das verändert Code.

## Prüfablauf je Variante (mit dem Nutzer am Gerät)

1. Flash (Freigabe) nach dem Ablauf in `CLAUDE.md`: `owl_read` vorher, `--reset-to-dfu --yes`, `dfu-util … -D`, Readback-Vergleich, Neustart durch den Nutzer (Case aus, USB ab, an), A1.
   - Flashlog nach `firmware/flashlog/YYYYMMDD_<build>/`.
   - Alle Geräte-Werkzeuge laufen außerhalb der Sandbox (`dangerouslyDisableSandbox`).
2. **Loop-Test 60 s** (Kabel Out n → In n):
   ```
   UV_CACHE_DIR=.uv-cache uv run python tools/acdc_rec.py --device OWL-ACDC-FX --duration 60 --sine-fade 1 --sine 440 530 670 790 --id B4x-<v>-loop --test <v>-loop-sine --gain g12 --device-desc "acdc1, Firmware …" --test-desc "…" --owl-read
   UV_CACHE_DIR=.uv-cache uv run python tools/phase_slips.py recordings/<datei>.wav --freqs 440 530 670 790
   ```
   - Bestanden: 0 Slips, MAD ≈ 0,01 mrad wie 3d (`B4-3d-loop`), keine `fb clamp`-Meldung.
3. Erst bei sauberem Loop: Kabel ziehen, Rauschen 2 × 60 s (`--reps 2 --owl-read --analyze --ref B4-3d-r1`), Vergleich mit `tools/family_table.py … --ref <3d-Kontrolle derselben Sitzung>`. Immer eine 3d-Kontrolle in derselben Sitzung (Drift ≈ 0,5 dB über 70 min, D37).
4. Am Ende der Sitzung 3d zurück (Freigabe), außer der Nutzer entscheidet anders.

## Werkzeuge (neu oder geändert in dieser Sitzung)

- `tools/check_itcm.py <build> [--ref <build>] [--same-itcm <build>]`: Prüfliste Q11, Bericht `check_itcm.md`/`.json` im Build-Ordner.
- `tools/family_table.py ID… [--ref ID…] [--group NAME=ID,ID] [--out datei.md]`: Familienpegel als Tabelle (reproduziert D35 exakt).
- `tools/acdc_rec.py`: neu `--dc V1…V4` (Vollausschlag −1…1, 1 ≈ 10 V) und `--dc-ramp SEK`. Sinus bis 0 dBFS. Eingangsoffset je Kanal −0,2…−0,4 V (D36).
- `firmware/patches/11-itcm-hotpath.patch`, `91-layout-pad-behind-itcm-anchor.patch`.

## Fallstricke

- Eine Input-Section landet in der **ersten** passenden Linker-Regel. ITCM-Muster stehen vor `.text`, Anker-Muster am Anfang von `.text`.
- `.text.onLoop` enthält in 07d die Füllfunktion `acdc_onloop_pad` (0x1D0 B zusammen).
- `_CCMRAM` (Patch-Heap) muss hinter dem ITCM-Code liegen, sonst nullt der Patch-Start den Code.
- ITCM-ECC: Anfang, Ende und LMA auf 8 B ausrichten, in 64-Bit-Wörtern kopieren (ist in 11 so).
- Heredocs mit `$VAR` und Backticks: Die Shell ersetzt Backticks in Python-f-Strings. Lieber `<<'EOF'` oder das Edit-Werkzeug nehmen.
- Der Aufbau ist gleich geblieben, aber laut Nutzer kam am Mac zwischen D35 und D37 CPU-Last hinzu. Der Kamm lag dabei +2,9 dB höher (D37) [Hypothese: Host-Last → Masse/SOF]. Bei Rauschmessungen die Host-Last konstant halten und im Messlog notieren.
- Git-Schreibzugriffe und Push nur mit Freigabe. Commits auf den Fork nur über einen temporären `git worktree`.
