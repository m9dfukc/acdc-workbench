# check_itcm: acdc1-build5-diag-flash

ELF `firmware/builds/acdc1-build5-diag-flash/ACDC.elf`, Binary `firmware/builds/acdc1-build5-diag-flash/ACDC.bin`

Gruppen im ITCM: **A B C E F G H L**; im Flash (Variante): D USB

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x5508
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x5508 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 8808 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 108728 B <= 131072 B (frei 22344 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 8808 B @ 0x32a0–0x5508 (zusammen 9480 B ab 0x3000). Patch-Heap im CCM: 43768 B (42.7 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ca1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x00004321 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x000044cd DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x080026a1 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im Flash, Gruppe D nicht gewählt)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 64 von 64 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 6700 B
- **ok** 40 von 40 Funktionen der nicht gewählten Gruppen (D) im Flash, zusammen 4990 B
- Funktionen im ITCM insgesamt: 68; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
- **WARN** keine unerwarteten Funktionen im ITCM: _ZL11acdcDiagPutPcS_PKcm.constprop.0, _ZL11acdcDiagPutPcS_PKcm.constprop.1, _ZL17acdcUsbDiagReportm

## 4 Sprünge aus dem ITCM, Veneers

- **ok** keine direkten Sprünge aus dem ITCM hinaus (nur über Veneers)
- **ok** 6 Veneers ITCM → Flash, alle in COLD (Fehler-/Ereignispfad) oder zu nicht gewählten Gruppen (1, gewollt)

| Ziel im Flash | Aufrufer im ITCM | Grund |
|---|---|---|
| `vPortFree` | `prvIdleTask` | Ereignis: Idle-Task räumt gelöschte Tasks auf (Patch-Wechsel) |
| `setup` | `StartDefaultTask` | Ereignis: einmal beim Start der Hauptschleife (StartDefaultTask) |
| `HAL_ADC_ErrorCallback` | `ADC_DMAConvCplt` | Fehler: ADC-DMA-Fehler |
| `vApplicationStackOverflowHook` | `vTaskSwitchContext` | Fehler: Stack-Überlauf (FreeRTOS) |
| `usbd_audio_error` | `_Z15usbd_rx_convertPlj`, `_Z15usbd_tx_convertPlj` | Fehler: USB-Puffer über-/unterlaufen (Debug-Meldung) |
| `USBD_LL_Transmit` | `usbd_midi_tx` | Variante: Gruppe D USB bleibt im Flash (gewollt) |

- Veneers Flash → ITCM: 24 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `memcpy`, `getParameterValue`, `vTaskSuspendAll`, `setLed`, `device_watchdog`, `xTaskResumeAll`, `vPortValidateInterruptPriority`, `HAL_GetTick` …)
- Indirekte Aufrufe (`blx/bx reg`) in: `ADC_DMAConvCplt`, `HAL_DMA_IRQHandler`, `_ZN12MidiReceiver7receiveEv`, `_ZN3Owl4loopEv`, `onProgramReady`

## 5 Literale im ITCM-Code, die in den Flash zeigen

16 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

- `[.rodata+0x9f4]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0x9f8]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0x9fc]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa00]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa04]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa08]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa0c]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa10]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa14]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa18]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa1c]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa20]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa24]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa28]` ← `_ZL17acdcUsbDiagReportm`
- `[.text+0x90c]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x914]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **WARN** 40 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08002500–0x08002e1b (2331 B); außerhalb: [.rodata+0x9f4], [.rodata+0x9f8], [.rodata+0x9fc], [.rodata+0xa00], [.rodata+0xa04], [.rodata+0xa08], [.rodata+0xa0c], [.rodata+0xa10], [.rodata+0xa14], [.rodata+0xa18], [.rodata+0xa1c], [.rodata+0xa20], [.rodata+0xa24], [.rodata+0xa28] (Variante: Anker nur für Füllvarianten nötig, deshalb nur Warnung)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x800b08d) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x800b1f9) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x800b595) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x800afb9) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x800ab01) im Flash (Gruppe D nicht gewählt)

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build4z-fx3k

- Funktionen gemeinsam: 726, davon ins ITCM verlegt 65, gleiche Adresse 46, andere Größe 8
- nur in der Referenz: `_GLOBAL__sub_I_rx_buffer`, `_Z12debugMessagePKcff`
- nur im neuen Build: `_GLOBAL__sub_I_acdc_usb_diag`, `_ZL11acdcDiagPutPcS_PKcm.constprop.0`, `_ZL11acdcDiagPutPcS_PKcm.constprop.1`, `_ZL17acdcUsbDiagReportm`
- Größe geändert: `_ZL14acdcOnLoopLatev` 448→440, `usbd_audio_error` 124→136, `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` 4→16, `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` 192→212, `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` 572→696, `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` 480→364, `usbd_audio_sof_callback` 296→228, `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` 36→156

| Symbol | Referenz | neu | Δ Größe |
|---|---|---|---|
| `DMA1_Stream0_IRQHandler` | `000032a0` (12) | `000032a0` (12) |  |
| `DMA1_Stream1_IRQHandler` | `000032ac` (12) | `000032ac` (12) |  |
| `HAL_DMA_IRQHandler` | `000032b8` (1704) | `000032b8` (1704) |  |
| `SAI_DMATxHalfCplt` | `000039bc` (10) | `000039bc` (10) |  |
| `SAI_DMATxCplt` | `00003960` (92) | `00003960` (92) |  |
| `SAI_DMARxHalfCplt` | `00003a24` (10) | `00003a24` (10) |  |
| `SAI_DMARxCplt` | `000039c8` (92) | `000039c8` (92) |  |
| `HAL_SAI_RxHalfCpltCallback` | `00003a30` (24) | `00003a30` (24) |  |
| `HAL_SAI_RxCpltCallback` | `00003a48` (32) | `00003a48` (32) |  |
| `HAL_SAI_TxHalfCpltCallback` | `00003a68` (2) | `00003a68` (2) |  |
| `HAL_SAI_TxCpltCallback` | `00003a6c` (2) | `00003a6c` (2) |  |
| `audioCallback` | `00003a70` (148) | `00003a70` (148) |  |
| `vTaskNotifyGiveFromISR` | `00003b04` (212) | `00003b04` (212) |  |
| `vPortValidateInterruptPriority` | `00003bd8` (92) | `00003bd8` (92) |  |
| `PendSV_Handler` | `00003ca0` (100) | `00003ca0` (100) |  |
| `vTaskSwitchContext` | `00003e18` (164) | `00003e18` (164) |  |
| `ulTaskNotifyTake` | `00003ebc` (104) | `00003ebc` (104) |  |
| `prvAddCurrentTaskToDelayedList` | `00003d04` (140) | `00003d04` (140) |  |
| `vPortEnterCritical` | `00003c34` (68) | `00003c34` (68) |  |
| `vPortExitCritical` | `00003c78` (40) | `00003c78` (40) |  |
| `uxListRemove` | `00003f70` (40) | `00003f70` (40) |  |
| `vListInsertEnd` | `00003f24` (28) | `00003f24` (28) |  |
| `vListInsert` | `00003f40` (48) | `00003f40` (48) |  |
| `prvIdleTask` | `00003d90` (136) | `00003d90` (136) |  |
| `onProgramReady` | `000040d4` (248) | `000040d4` (248) |  |
| `_Z15usbd_tx_convertPlj` | `00004054` (128) | `00004054` (128) |  |
| `_Z15usbd_rx_convertPlj` | `00003f98` (188) | `00003f98` (188) |  |
| `updateParameters` | `000041d8` (54) | `000041d8` (54) |  |
| `_ZN10MidiWriter8transmitEv` | `00004210` (76) | `00004210` (76) |  |
| `_ZN12MidiReceiver7receiveEv` | `0000425c` (104) | `0000425c` (104) |  |
| `usbd_midi_ready` | `000042fc` (36) | `000042fc` (36) |  |
| `usbd_midi_tx` | `000042c4` (56) | `000042c4` (56) |  |
| `getProgramVector` | `000041cc` (12) | `000041cc` (12) |  |
| `OTG_FS_IRQHandler` | `08002080` (12) | `080026a0` (12) |  |
| `HAL_PCD_IRQHandler` | `0800855c` (1624) | `08008b14` (1624) |  |
| `USB_ReadInterrupts` | `08009898` (8) | `08009e50` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `080098a0` (14) | `08009e58` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `080098b0` (14) | `08009e68` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `080098c0` (18) | `08009e78` (18) |  |
| `USB_ReadDevInEPInterrupt` | `080098d4` (32) | `08009e8c` (32) |  |
| `USB_GetMode` | `080098f4` (8) | `08009eac` (8) |  |
| `USB_ReadPacket` | `0800972c` (72) | `08009ce4` (72) |  |
| `USB_WritePacket` | `08009700` (42) | `08009cb8` (42) |  |
| `USB_EPStartXfer` | `080094dc` (548) | `08009a94` (548) |  |
| `HAL_PCD_SOFCallback` | `0800a23c` (8) | `0800a7f4` (8) |  |
| `USBD_LL_SOF` | `08009b84` (36) | `0800a13c` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `0800aff8` (36) | `0800b594` (156) | +120 |
| `usbd_audio_sof_callback` | `0800aed0` (296) | `0800b4b0` (228) | -68 |
| `usbd_audio_get_rx_count` | `080154fc` (40) | `08015b10` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `0800a214` (20) | `0800a7cc` (20) |  |
| `USBD_LL_DataOutStage` | `080099d4` (104) | `08009f8c` (104) |  |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `0800aab4` (572) | `0800b1f8` (696) | +124 |
| `USBD_LL_GetRxDataSize` | `0800a364` (8) | `0800a91c` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `08008d18` (18) | `080092d0` (18) |  |
| `USBD_LL_PrepareReceive` | `0800a34c` (22) | `0800a904` (22) |  |
| `HAL_PCD_EP_Receive` | `08008cc8` (78) | `08009280` (78) |  |
| `HAL_PCD_DataInStageCallback` | `0800a228` (18) | `0800a7e0` (18) |  |
| `USBD_LL_DataInStage` | `08009a3c` (182) | `08009ff4` (182) |  |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `0800acf0` (480) | `0800b08c` (364) | -116 |
| `USBD_LL_Transmit` | `0800214c` (22) | `0800276c` (22) |  |
| `HAL_PCD_EP_Transmit` | `08008d2c` (78) | `080092e4` (78) |  |
| `_ZN5Codec16getSampleCounterEv` | `08014a2c` (32) | `08015040` (32) |  |
| `codec_ndtr` | `08003ff8` (20) | `080045b0` (20) |  |
| `HAL_PCD_ISOINIncompleteCallback` | `0800a24c` (8) | `0800a804` (8) |  |
| `USBD_LL_IsoINIncomplete` | `08009ba8` (36) | `0800a160` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `0800a9f4` (192) | `0800afb8` (212) | +20 |
| `USBD_LL_FlushEP` | `0800a2dc` (22) | `0800a894` (22) |  |
| `HAL_PCD_EP_Flush` | `08008e7c` (62) | `08009434` (62) |  |
| `USB_FlushTxFifo` | `0800934c` (36) | `08009904` (36) |  |
| `USB_FlushRxFifo` | `08009370` (32) | `08009928` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `0800a244` (8) | `0800a7fc` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `08009bcc` (36) | `0800a184` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `0800a548` (4) | `0800ab00` (16) | +12 |
| `SysTick_Handler` | `00004320` (24) | `00004320` (24) |  |
| `HAL_IncTick` | `00004338` (24) | `00004338` (24) |  |
| `HAL_GetTick` | `00004350` (12) | `00004350` (12) |  |
| `xTaskGetSchedulerState` | `00004480` (32) | `00004480` (32) |  |
| `xPortSysTickHandler` | `000044a0` (44) | `000044a0` (44) |  |
| `xTaskIncrementTick` | `0000445c` (36) | `0000445c` (36) |  |
| `xTaskIncrementTick.part.0` | `0000435c` (256) | `0000435c` (256) |  |
| `DMA1_Stream3_IRQHandler` | `000044cc` (12) | `000044cc` (12) |  |
| `ADC_DMAConvCplt` | `000044ec` (108) | `000044ec` (108) |  |
| `ADC_DMAHalfConvCplt` | `000044e0` (10) | `000044e0` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `000044d8` (2) | `000044d8` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `000044dc` (2) | `000044dc` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `00004558` (372) | `00004558` (372) |  |
| `_ZL14acdcOnLoopLatev` | `000046cc` (448) | `00004cf8` (440) | -8 |
| `setLed` | `0000492c` (204) | `00004f50` (204) |  |
| `setLed.constprop.0` | `0000488c` (160) | `00004eb0` (160) |  |
| `getParameterValue` | `000049f8` (20) | `0000501c` (20) |  |
| `setParameterValue` | `00004a0c` (16) | `00005030` (16) |  |
| `StartDefaultTask` | `00004a1c` (12) | `00005040` (12) |  |
| `loop` | `00004a28` (20) | `0000504c` (20) |  |
| `onLoop` | `00004a3c` (4) | `00005060` (4) |  |
| `_ZN3Owl4loopEv` | `00004c0c` (76) | `00005230` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `00004c58` (16) | `0000527c` (16) |  |
| `device_watchdog` | `00004c68` (16) | `0000528c` (16) |  |
| `vTaskDelayUntil` | `00004d9c` (176) | `000053c0` (176) |  |
| `vTaskSuspendAll` | `00004e4c` (16) | `00005470` (16) |  |
| `xTaskResumeAll` | `00004e5c` (32) | `00005480` (32) |  |
| `xTaskResumeAll.part.0` | `00004c78` (292) | `0000529c` (292) |  |
| `memset` | `00004e84` (16) | `000054a8` (16) |  |
| `memcpy` | `00004e94` (28) | `000054b8` (28) |  |
| `abs` | `00004e7c` (8) | `000054a0` (8) |  |
| `onLoop` | `00004a3c` (4) | `00005060` (4) |  |
| `main` | `08002b48` (2332) | `08003100` (2332) |  |
| `SystemInit` | `08003f04` (240) | `080044bc` (240) |  |
| `Reset_Handler` | `08001ee0` (128) | `08002500` (128) |  |
| `_ZN11MidiHandler11handleSysExEPht` | `0801440c` (1252) | `08014a20` (1252) |  |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 178, gleiche RAM-Adresse 116

**Ergebnis:** BESTANDEN (0 FAIL, 2 WARN)
