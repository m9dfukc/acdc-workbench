# Übergabe – ITCM-Build (Stand 2026-11-16 abends)

Für eine neue Session. Ersetzt `uebergabe-2026-11-16.md`. Deren Fallstricke gelten weiter, die wichtigsten stehen unten.

**Stand 2026-11-16 (später):** Schritte 1–4 erledigt. `acdc1-build4-fx3i` und `acdc1-build4p-fx3ip` liegen geprüft in `firmware/builds/` (Patches 11 und 91, `tools/check_itcm.py`, Details in docs/05 „Build 4“ → „Umsetzung“). Messsitzung am Abend: Clip-Test 3d bestanden, fx3i gemessen (fs/8 −5 dB), aber USB-Playback gestört, deshalb zurück auf 3d und fx3ip nicht gemessen (messlog D36–D38). Weiter mit Fehlersuche, siehe docs/05 „Build 4“ → „Ergebnis der Sitzung“.

**Auftrag:** Build 4 **`v22.4.r-fx3i`** bauen (der heiße Pfad läuft aus dem ITCM), dazu die Füllbyte-Variante **`fx3ip`**. Beide prüfen (`tools/check_itcm.py`, `nm` gegen 3d) und für die Messsitzung vorbereiten. **Nicht flashen ohne Freigabe.** Der Plan ist mit dem Nutzer abgestimmt (Grill-Runde Q1–Q15) und steht in `docs/05-firmware-plan.md` im Abschnitt **„Build 4“**. Das ist die maßgebliche Quelle.

**Zuerst lesen:**
1. `CLAUDE.md`, vor allem „Build 3d“ und „Konventionen“ (Aufnahmen jetzt mit `tools/acdc_rec.py`).
2. `docs/05-firmware-plan.md`, Abschnitt „Build 4“, dazu „Build 3“ für das 07d-/`.late_text`-Muster.
3. `docs/research/notes/daisy_itcm_2026-11-16.md`: Technik (ECC, Veneers, Linker-Muster), Teensy-4-Vorbild.
4. `docs/research/notes/layout_noise_2026-11-16.md`, Abschnitt 1c (Code-Fakten).
5. `docs/messlog.md` D33–D35.

## Stand

- **acdc1:** Build 3d `v22.4.r-fx2d` (`firmware/builds/acdc1-build3d-fx2/`, SHA `d212cf8d…`), unverändert seit 2026-11-15. acdc2 wird nie angefasst.
- **Upstream (2026-11-16):** master steht bei `36eaf1c4` (PR #89: GCC-13+-Build-Flags, CI auf GCC 14.3). Firmware-Code ist dabei nicht neu. Die Flags sind übernommen als **Patch 08** (`firmware/patches/08-upstream-gcc13-build-flags.patch`), auf 3d **bytegleich**. Kandidaten-Builds `cand-*` in `firmware/builds/` sind nur zur Ansicht da, nicht flashen. Details: `docs/research/notes/upstream_master_2026-11-16.md`. Einmal `git fetch upstream` ist gelaufen, der Klon steht weiter auf `acdc/thru-usb-feedback`.
- **Aufnahme-Werkzeug:** `tools/acdc_rec.py` ersetzt Host-Software mit Mehrkanal-Recorder. Die Gegenprobe ist bestanden (D35: fs/8 und Mischprodukte ±0,01 dB, Kamm +0,43 dB). Das Skript kann auch Sinus-Testsignale je Ausgang senden (`--sine`). Am Gerät ist das noch ungeprüft, der Pegel ±5 V geht ins Rack, also vorher fragen. Die Analyse liest das Manifest-Feld `scale`.
- **Kamm-Streuung zwischen Läufen** ≈ 0,4 dB (D34, D35). Deshalb immer 2 × 60 s und eine Kontrolle in derselben Sitzung.

## Fakten für den Build [Code / Build 3d, nur gelesen]

- **Speicher** (`Hardware/xibeca.ld`):
  - ITCM 0x0–0xFFF ist ganz MSP-Stack (`_estack` = 0x1000).
  - CCMRAM 0x1000–0x2FFF ist `PROGRAMSTACK` (Audio-Task, NOLOAD).
  - **0x3000–0xFFFF = Patch-Heap-Segment 0**, wird bei jedem Patch-Start per `memset` genullt (`PROVIDE(_CCMRAM)`, `ProgramManager.cpp` `USE_CCM_RAM`). Der ITCM-Code muss also im Linkerskript **vor** `PROVIDE(_CCMRAM)` liegen.
  - Der Patch läuft aus DTCM, PATCHRAM 0x2000C000.
- **Startup** (`startup_owl3.s`): Magic → `sp` → `SystemInit` (VTOR = 0x08000000) → einzige Kopierschleife `.data` → `.bss` → `__libc_init_array` → `main` (Caches an, `MPU_Config`). Die zweite Schleife kommt nach `.data`.
- **Laufzeit:**
  - FreeRTOS mit `configUSE_PREEMPTION 0`, kein WFI. Der Idle-Task dreht dauernd PendSV/`vTaskSwitchContext`, die CPU-Last liegt bei ≈ 8 %.
  - Der Audio-Block läuft **im Audio-Task**, nicht in der ISR: TX-DMA-ISR → `audioCallback` → `vTaskNotifyGiveFromISR`.
  - USB OTG_FS Prio 6, Feedback (Patch 06) bei jedem 32. SOF.
- **Flash-Reserve:** 24 284 B frei. `.late_text` 0x08019DF0–0x0801A124 (820 B, `acdcMeasureRawInputs`, `acdcOnLoopLate`).
- **Heißer Pfad ≈ 9,5 KB** (Build 3d, alle heute in Flash-`.text`, Input-Section `.text.<Symbol>`):

  | Gruppe | Funktionen (Bytes) | Σ B |
  |---|---|---|
  | A SAI-ISR (je 6 kHz) | `DMA1_Stream0/1_IRQHandler` 12+12, `HAL_DMA_IRQHandler` 1704, `SAI_DMATx/RxHalfCplt` 10+10, `SAI_DMATx/RxCplt` 92+92, `HAL_SAI_Rx(Half)CpltCallback` 2+2, `HAL_SAI_TxHalfCpltCallback` 24 / `TxCpltCallback` 32 (Codec.o; weak-Duplikat in hal_sai.o), `audioCallback` 148, `vTaskNotifyGiveFromISR` 212, `vPortValidateInterruptPriority` 92 | 2444 |
  | B Scheduler | `PendSV_Handler` 100, `vTaskSwitchContext` 164, `ulTaskNotifyTake` 104, `prvAddCurrentTaskToDelayedList` 140, `vPortEnter/ExitCritical` 68+40, `uxListRemove` 40, `vListInsertEnd` 28, `vListInsert` 48, `prvIdleTask` 136 | 868 |
  | C Audio-Task | `onProgramReady` 248, `usbd_tx_convert` 128, `usbd_rx_convert` 188, `updateParameters` 54 (ACDC.o; weak in callbacks.o), `MidiWriter::transmit` 76, `MidiReceiver::receive` 104, `usbd_midi_ready` 36, `getProgramVector` 12, `memset` 16 (libc_nano) | 862 |
  | D USB (1 kHz) | `OTG_FS_IRQHandler`, `HAL_PCD_IRQHandler` 1624, `USB_Read*`/`USB_ReadPacket`/`USB_WritePacket`/`USB_EPStartXfer` 548, `HAL_PCD_*Callback`, `USBD_LL_SOF/DataOutStage/DataInStage`, `USBD_AUDIO_SOF/DataOut 572/DataIn 480`, `usbd_audio_sof_callback` 296, `usbd_audio_get_rx_count`, `abs`, `USBD_LL_GetRxDataSize`, `HAL_PCD_EP_GetRxCount/Receive/Transmit`, `USBD_LL_PrepareReceive/Transmit`, `Codec::getSampleCounter`, `codec_ndtr`, `memcpy` 28, ISO-IN-incomplete-Kette | 4734 |
  | E SysTick | `SysTick_Handler`, `HAL_IncTick`, `xTaskGetSchedulerState`, `xPortSysTickHandler`, `xTaskIncrementTick` + `.part.0` | 416 |
  | F ADC-DMA | `DMA1_Stream3_IRQHandler`, `ADC_DMA(Half)ConvCplt`, `HAL_ADC_Conv(Half)CpltCallback` | 134 |
  | dazu (Q7) | 07d: `acdcMeasureRawInputs` 372, `acdcOnLoopLate` 448; Vektortabelle 0x298 (Q8) | ≈ 1500 |

  Die Rohliste steht in `firmware/itcm-prep/hot.txt`. Die Skripte des Fakten-Agenten liegen in `firmware/itcm-prep/` (`cg.py` Call-Graph aus `objdump -d`, `tab.py`, `lit.py` Literal-Scan, `br.py` Sprünge, `nmcmp.py` nm-Vergleich). Sie sind schnell geschrieben, vor Gebrauch lesen.
- **Sprünge:** Im heißen Satz stehen 129 `bl` und 15 `b.w` über Funktionsgrenzen. ITCM ↔ Flash liegen ≈ 128 MB auseinander, GNU ld setzt die Veneers selbst ein. Literal-Pools wandern mit, nur der Fehlerpfad liest `.rodata` (Texte).

## Nächste Schritte

1. Patch `11-itcm-hotpath.patch` schreiben. Er ändert `xibeca.ld` (`.itcm_text` + Vektortabelle, `ALIGN(8)`, vor `PROVIDE(_CCMRAM)`), `startup_owl3.s` (64-Bit-Kopierschleife, DSB/ISB) und das Setzen von VTOR (nach dem Kopieren, z. B. früh in `main`). Die Platzierung per Linker-Muster ist besser als Attribute im HAL-Code. Die bestehenden Patches nicht ändern.
2. `tools/check_itcm.py` schreiben (Prüfliste in docs/05 Q11) und am ELF laufen lassen. Veneers in den Flash nachziehen, bis nur noch der Fehlerpfad hinausspringt.
3. Bauen mit `FW_VERSION=v22.4.r-fx3i tools/build_acdc.sh acdc1-build4-fx3i db9d3dd firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz <01 02 04 05 06 03 07d 08 11 als Pfade>`. `fx3ip`: eigener Füllpatch, der nur Flash-Adressen außerhalb des ITCM verschiebt, z. B. 0x150 B in eine Flash-Funktion, die nicht im ITCM liegt. **Patch 90 passt nicht auf 07d** (`onLoop` ist dort ein Stub). Prüfen: Der ITCM-Inhalt von fx3i und fx3ip muss bytegleich sein, der Rest verschoben.
4. `nm`-Tabelle gegen 3d, Größe, `BUILD_INFO.txt`. Dann den Nutzer fragen, ob er für die Messsitzung bereit ist.
5. **Messsitzung** (nur mit dem Nutzer am Gerät):
   - Clip-Test 3d.
   - 3d-Kontrolle 2 × 60 s.
   - Flash fx3i (Freigabe), A1, Funktionsprobe, 2 × 60 s.
   - Flash fx3ip (Freigabe), dasselbe.
   - Flash 3d (Freigabe), 2 × 60 s.

   Aufnahmen z. B. `uv run python tools/acdc_rec.py --id B4-fx3i --test fx3i-open-inputs --reps 2 --device-desc "…" --test-desc "…" --owl-read --analyze --ref …` (außerhalb der Sandbox, `UV_CACHE_DIR=.uv-cache`). Auswertung wie D34/D35 als Mittel der Familienpegel (fs8, usb1k, imd, rest) aus `out/<ID>/<ID>.json`.
6. Messlog D36ff., docs/05, CLAUDE.md, TODO. Fork-Commits und Push nur nach Freigabe.

## Fallstricke (weiter gültig)

- SAI1 liefert 24 Bit rechtsbündig **ohne Vorzeichen**: `(int32_t)((uint32_t)x << 8) >> 8`.
- `--gc-sections` entfernt ungenutzte Füllfunktionen. Füllbytes in bestehende Input-Sections legen oder `KEEP`.
- `.late_bss` wird nicht genullt (Magic-Wert, siehe 07d).
- Patches brauchen `+++ b/`-Pfade und werden mit `patch -p1` eingespielt. `usbd_audio.cpp` hat CRLF.
- Git-Schreibzugriffe, `owl_read.py`, `dfu-util` und `acdc_rec.py` laufen nur außerhalb der Sandbox. Git-Schreibzugriffe und Flash nur mit Freigabe, Push nur nach Nachfrage. Commits auf `acdc/fx1d` nur über einen temporären `git worktree`.
- Flash-Ablauf und Rückweg (3d → Build 2 → 1d → Readback) stehen in `CLAUDE.md`.
- Während `acdc_rec.py` läuft, darf Host-Software nicht offen sein, sonst hält Host-Software das Gerät.
