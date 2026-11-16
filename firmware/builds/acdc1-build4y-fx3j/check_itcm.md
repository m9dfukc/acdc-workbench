# check_itcm: acdc1-build4y-fx3j

ELF `firmware/builds/acdc1-build4y-fx3j/ACDC.elf`, Binary `firmware/builds/acdc1-build4y-fx3j/ACDC.bin`

Gruppen im ITCM: **A B C E F G H L**; im Flash (Variante): D USB

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x4f20
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x4f20 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 7296 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 107176 B <= 131072 B (frei 23896 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 7296 B @ 0x32a0–0x4f20 (zusammen 7968 B ab 0x3000). Patch-Heap im CCM: 45280 B (44.2 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ce1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x00004361 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x0000450d DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x080020c1 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im Flash, Gruppe D nicht gewählt)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 64 von 64 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 6772 B
- **ok** 40 von 40 Funktionen der nicht gewählten Gruppen (D) im Flash, zusammen 4898 B
- Funktionen im ITCM insgesamt: 65; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
- **ok** keine unerwarteten Funktionen im ITCM

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

- Veneers Flash → ITCM: 24 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `setLed.constprop.0`, `getProgramVector`, `memcpy`, `setLed`, `abs`, `xTaskResumeAll.part.0`, `getParameterValue`, `vPortExitCritical` …)
- Indirekte Aufrufe (`blx/bx reg`) in: `ADC_DMAConvCplt`, `HAL_DMA_IRQHandler`, `_ZN12MidiReceiver7receiveEv`, `_ZN3Owl4loopEv`, `onProgramReady`

## 5 Literale im ITCM-Code, die in den Flash zeigen

2 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

- `[.text+0x974]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x97c]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **ok** 26 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08001f20–0x080028a3 (2435 B)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x800ad31) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x800aaf5) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x800b039) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x800aa35) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x800a589) im Flash (Gruppe D nicht gewählt)

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build3d-fx2

- Funktionen gemeinsam: 728, davon ins ITCM verlegt 65, gleiche Adresse 0, andere Größe 3
- nur in der Referenz: –
- nur im neuen Build: –
- Größe geändert: `HAL_SAI_TxHalfCpltCallback` 24→56, `HAL_SAI_TxCpltCallback` 32→64, `Reset_Handler` 66→128

| Symbol | Referenz | neu | Δ Größe |
|---|---|---|---|
| `DMA1_Stream0_IRQHandler` | `08001964` (12) | `000032a0` (12) |  |
| `DMA1_Stream1_IRQHandler` | `08001970` (12) | `000032ac` (12) |  |
| `HAL_DMA_IRQHandler` | `0800c258` (1704) | `000032b8` (1704) |  |
| `SAI_DMATxHalfCplt` | `08003390` (10) | `000039bc` (10) |  |
| `SAI_DMATxCplt` | `08003334` (92) | `00003960` (92) |  |
| `SAI_DMARxHalfCplt` | `08003400` (10) | `00003a24` (10) |  |
| `SAI_DMARxCplt` | `080033a0` (92) | `000039c8` (92) |  |
| `HAL_SAI_RxHalfCpltCallback` | `080033fc` (2) | `00003a34` (2) |  |
| `HAL_SAI_RxCpltCallback` | `0800339c` (2) | `00003a30` (2) |  |
| `HAL_SAI_TxHalfCpltCallback` | `08013fa8` (24) | `00003a38` (56) | +32 |
| `HAL_SAI_TxCpltCallback` | `08013fc0` (32) | `00003a70` (64) | +32 |
| `audioCallback` | `08014d94` (148) | `00003ab0` (148) |  |
| `vTaskNotifyGiveFromISR` | `08004cb8` (212) | `00003b44` (212) |  |
| `vPortValidateInterruptPriority` | `08003e88` (92) | `00003c18` (92) |  |
| `PendSV_Handler` | `08003c90` (100) | `00003ce0` (100) |  |
| `vTaskSwitchContext` | `08004914` (164) | `00003e58` (164) |  |
| `ulTaskNotifyTake` | `080049d8` (104) | `00003efc` (104) |  |
| `prvAddCurrentTaskToDelayedList` | `08003fdc` (140) | `00003d44` (140) |  |
| `vPortEnterCritical` | `08003c24` (68) | `00003c74` (68) |  |
| `vPortExitCritical` | `08003c68` (40) | `00003cb8` (40) |  |
| `uxListRemove` | `08004df8` (40) | `00003fb0` (40) |  |
| `vListInsertEnd` | `08004dac` (28) | `00003f64` (28) |  |
| `vListInsert` | `08004dc8` (48) | `00003f80` (48) |  |
| `prvIdleTask` | `08004068` (136) | `00003dd0` (136) |  |
| `onProgramReady` | `08014c90` (248) | `00004114` (248) |  |
| `_Z15usbd_tx_convertPlj` | `08014c10` (128) | `00004094` (128) |  |
| `_Z15usbd_rx_convertPlj` | `08014b54` (188) | `00003fd8` (188) |  |
| `updateParameters` | `08012bf0` (54) | `00004218` (54) |  |
| `_ZN10MidiWriter8transmitEv` | `08016878` (76) | `00004250` (76) |  |
| `_ZN12MidiReceiver7receiveEv` | `080175a4` (104) | `0000429c` (104) |  |
| `usbd_midi_ready` | `08009a4c` (36) | `0000433c` (36) |  |
| `usbd_midi_tx` | `08009a14` (56) | `00004304` (56) |  |
| `getProgramVector` | `08014d88` (12) | `0000420c` (12) |  |
| `OTG_FS_IRQHandler` | `080019d4` (12) | `080020c0` (12) |  |
| `HAL_PCD_IRQHandler` | `08006ad0` (1624) | `0800859c` (1624) |  |
| `USB_ReadInterrupts` | `0800804c` (8) | `080098d8` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `08008054` (14) | `080098e0` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `08008064` (14) | `080098f0` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `08008074` (18) | `08009900` (18) |  |
| `USB_ReadDevInEPInterrupt` | `08008088` (32) | `08009914` (32) |  |
| `USB_GetMode` | `080080a8` (8) | `08009934` (8) |  |
| `USB_ReadPacket` | `08007ee0` (72) | `0800976c` (72) |  |
| `USB_WritePacket` | `08007eb4` (42) | `08009740` (42) |  |
| `USB_EPStartXfer` | `08007b60` (548) | `0800951c` (548) |  |
| `HAL_PCD_SOFCallback` | `08008ad8` (8) | `0800a27c` (8) |  |
| `USBD_LL_SOF` | `080083bc` (36) | `08009bc4` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `080099b4` (36) | `0800b038` (36) |  |
| `usbd_audio_sof_callback` | `0800988c` (296) | `0800af10` (296) |  |
| `usbd_audio_get_rx_count` | `08014adc` (40) | `0801553c` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `08008ab0` (20) | `0800a254` (20) |  |
| `USBD_LL_DataOutStage` | `0800820c` (104) | `08009a14` (104) |  |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `080093f4` (572) | `0800aaf4` (572) |  |
| `USBD_LL_GetRxDataSize` | `08008ca4` (8) | `0800a3a4` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `0800728c` (18) | `08008d58` (18) |  |
| `USBD_LL_PrepareReceive` | `08008c8c` (22) | `0800a38c` (22) |  |
| `HAL_PCD_EP_Receive` | `0800723c` (78) | `08008d08` (78) |  |
| `HAL_PCD_DataInStageCallback` | `08008ac4` (18) | `0800a268` (18) |  |
| `USBD_LL_DataInStage` | `08008274` (182) | `08009a7c` (182) |  |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `08009630` (480) | `0800ad30` (480) |  |
| `USBD_LL_Transmit` | `08008c74` (22) | `0800218c` (22) |  |
| `HAL_PCD_EP_Transmit` | `080072a0` (78) | `08008d6c` (78) |  |
| `_ZN5Codec16getSampleCounterEv` | `08013f88` (32) | `08014a6c` (32) |  |
| `codec_ndtr` | `08001ad4` (20) | `08004038` (20) |  |
| `HAL_PCD_ISOINIncompleteCallback` | `08008b4c` (8) | `0800a28c` (8) |  |
| `USBD_LL_IsoINIncomplete` | `080083e0` (36) | `08009be8` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `08009334` (192) | `0800aa34` (192) |  |
| `USBD_LL_FlushEP` | `08008bec` (22) | `0800a31c` (22) |  |
| `HAL_PCD_EP_Flush` | `080073f0` (62) | `08008ebc` (62) |  |
| `USB_FlushTxFifo` | `080079b8` (36) | `0800938c` (36) |  |
| `USB_FlushRxFifo` | `080079dc` (32) | `080093b0` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `08008b44` (8) | `0800a284` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `08008404` (36) | `08009c0c` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `08008e88` (4) | `0800a588` (4) |  |
| `SysTick_Handler` | `0800194c` (24) | `00004360` (24) |  |
| `HAL_IncTick` | `08009bcc` (24) | `00004378` (24) |  |
| `HAL_GetTick` | `08009be4` (12) | `00004390` (12) |  |
| `xTaskGetSchedulerState` | `080049b8` (32) | `000044c0` (32) |  |
| `xPortSysTickHandler` | `08003cf4` (44) | `000044e0` (44) |  |
| `xTaskIncrementTick` | `080048f0` (36) | `0000449c` (36) |  |
| `xTaskIncrementTick.part.0` | `080040f0` (256) | `0000439c` (256) |  |
| `DMA1_Stream3_IRQHandler` | `08001988` (12) | `0000450c` (12) |  |
| `ADC_DMAConvCplt` | `0800cbf8` (108) | `0000452c` (108) |  |
| `ADC_DMAHalfConvCplt` | `0800c90c` (10) | `00004520` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `0800c904` (2) | `00004518` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `0800c908` (2) | `0000451c` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `08019df0` (372) | `00004598` (372) |  |
| `_ZL14acdcOnLoopLatev` | `08019f64` (448) | `0000470c` (448) |  |
| `setLed` | `08012b24` (204) | `0000496c` (204) |  |
| `setLed.constprop.0` | `08012a84` (160) | `000048cc` (160) |  |
| `getParameterValue` | `08014e28` (20) | `00004a38` (20) |  |
| `setParameterValue` | `08014e3c` (16) | `00004a4c` (16) |  |
| `StartDefaultTask` | `08000438` (12) | `00004a5c` (12) |  |
| `loop` | `08002664` (20) | `00004a68` (20) |  |
| `onLoop` | `08012e3c` (4) | `00004a7c` (4) |  |
| `_ZN3Owl4loopEv` | `080143f4` (76) | `00004c4c` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `080156ec` (16) | `00004c98` (16) |  |
| `device_watchdog` | `080027b8` (16) | `00004ca8` (16) |  |
| `vTaskDelayUntil` | `080046a8` (176) | `00004ddc` (176) |  |
| `vTaskSuspendAll` | `080048b4` (16) | `00004e8c` (16) |  |
| `xTaskResumeAll` | `080048c4` (32) | `00004e9c` (32) |  |
| `xTaskResumeAll.part.0` | `080041f0` (292) | `00004cb8` (292) |  |
| `memset` | `080186c0` (16) | `00004ec4` (16) |  |
| `memcpy` | `0801876c` (28) | `00004ed4` (28) |  |
| `abs` | `080184ee` (8) | `00004ebc` (8) |  |
| `onLoop` | `08012e3c` (4) | `00004a7c` (4) |  |
| `main` | `08000590` (2332) | `08002b88` (2332) |  |
| `SystemInit` | `080019e0` (240) | `08003f44` (240) |  |
| `Reset_Handler` | `08018478` (66) | `08001f20` (128) | +62 |
| `_ZN11MidiHandler11handleSysExEPht` | `08013968` (1252) | `0801444c` (1252) |  |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 176, gleiche RAM-Adresse 176

**Ergebnis:** BESTANDEN (0 FAIL, 0 WARN)
