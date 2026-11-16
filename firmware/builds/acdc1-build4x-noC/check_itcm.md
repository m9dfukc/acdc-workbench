# check_itcm: acdc1-build4x-noC

ELF `firmware/builds/acdc1-build4x-noC/ACDC.elf`, Binary `firmware/builds/acdc1-build4x-noC/ACDC.bin`

Gruppen im ITCM: **A B D E F G H L**; im Flash (Variante): C Audio-Task

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x5f48
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x5f48 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 11432 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 107300 B <= 131072 B (frei 23772 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 11432 B @ 0x32a0–0x5f48 (zusammen 12104 B ab 0x3000). Patch-Heap im CCM: 41144 B (40.2 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ca1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x000052d5 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x00005481 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x00003f99 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 95 von 95 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 10704 B
- **ok** 9 von 9 Funktionen der nicht gewählten Gruppen (C) im Flash, zusammen 902 B
- Funktionen im ITCM insgesamt: 96; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
- **ok** keine unerwarteten Funktionen im ITCM

## 4 Sprünge aus dem ITCM, Veneers

- **ok** keine direkten Sprünge aus dem ITCM hinaus (nur über Veneers)
- **ok** 28 Veneers ITCM → Flash, alle in COLD (Fehler-/Ereignispfad) oder zu nicht gewählten Gruppen (2, gewollt)

| Ziel im Flash | Aufrufer im ITCM | Grund |
|---|---|---|
| `HAL_PCD_SetupStageCallback` | `HAL_PCD_IRQHandler` | Ereignis: Control-Transfer (EP0 Setup) |
| `USBD_CtlContinueRx` | `USBD_LL_DataOutStage` | Ereignis: Control-Transfer (EP0) |
| `USBD_CtlContinueSendData` | `USBD_LL_DataInStage` | Ereignis: Control-Transfer (EP0) |
| `USBD_CtlReceiveStatus` | `USBD_LL_DataInStage` | Ereignis: Control-Transfer (EP0) |
| `USBD_CtlSendStatus` | `USBD_LL_DataOutStage` | Ereignis: Control-Transfer (EP0) |
| `USB_EP0StartXfer` | `HAL_PCD_EP_Receive`, `HAL_PCD_EP_Transmit` | Ereignis: Control-Transfer (EP0) |
| `USB_EP0_OutStart` | `HAL_PCD_IRQHandler` | Ereignis: Control-Transfer/Enumeration (EP0) |
| `USB_ActivateSetup` | `HAL_PCD_IRQHandler` | Ereignis: Enumeration |
| `USB_GetDevSpeed` | `HAL_PCD_IRQHandler` | Ereignis: Enumeration |
| `USB_SetTurnaroundTime` | `HAL_PCD_IRQHandler` | Ereignis: Enumeration |
| `HAL_RCC_GetHCLKFreq` | `HAL_PCD_IRQHandler` | Ereignis: Enumeration (Turnaround-Zeit) |
| `vPortFree` | `prvIdleTask` | Ereignis: Idle-Task räumt gelöschte Tasks auf (Patch-Wechsel) |
| `usbd_midi_rx` | `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | Ereignis: MIDI-Eingang vom Rechner |
| `usbd_audio_rx_start_callback` | `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | Ereignis: Playback-Stream startet |
| `HAL_PCD_ResetCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Bus-Reset |
| `HAL_PCD_ConnectCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Connect |
| `HAL_PCD_DisconnectCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Disconnect |
| `HAL_PCDEx_LPM_Callback` | `HAL_PCD_IRQHandler` | Ereignis: USB-LPM |
| `HAL_PCD_ResumeCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Resume |
| `HAL_PCD_SuspendCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Suspend |
| `setup` | `StartDefaultTask` | Ereignis: einmal beim Start der Hauptschleife (StartDefaultTask) |
| `USBD_LL_StallEP` | `USBD_LL_DataInStage` | Fehler/Control: Endpoint stallen |
| `HAL_ADC_ErrorCallback` | `ADC_DMAConvCplt` | Fehler: ADC-DMA-Fehler |
| `_Z12debugMessagePKcff` | `usbd_audio_sof_callback` | Fehler: Debug-Meldung |
| `_Z12debugMessagePKcfff` | `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`, `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | Fehler: Debug-Meldung |
| `vApplicationStackOverflowHook` | `vTaskSwitchContext` | Fehler: Stack-Überlauf (FreeRTOS) |
| `_ZN10MidiWriter8transmitEv` | `_ZN3Owl4loopEv` | Variante: Gruppe C Audio-Task bleibt im Flash (gewollt) |
| `_ZN12MidiReceiver7receiveEv` | `_ZN3Owl4loopEv` | Variante: Gruppe C Audio-Task bleibt im Flash (gewollt) |

- Veneers Flash → ITCM: 25 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `setLed.constprop.0`, `USBD_LL_Transmit`, `memcpy`, `setLed`, `xTaskResumeAll.part.0`, `getParameterValue`, `vPortExitCritical`, `vPortEnterCritical` …)
- Indirekte Aufrufe (`blx/bx reg`) in: `ADC_DMAConvCplt`, `HAL_DMA_IRQHandler`, `USBD_LL_DataInStage`, `USBD_LL_DataOutStage`, `USBD_LL_IsoINIncomplete`, `USBD_LL_IsoOUTIncomplete`, `USBD_LL_SOF`, `_ZN3Owl4loopEv`

## 5 Literale im ITCM-Code, die in den Flash zeigen

4 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

- `[.text+0x92c]` ← `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh`
- `[.text+0x934]` ← `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`
- `[.text+0x93c]` ← `usbd_audio_sof_callback`
- `[.text+0x948]` ← `usbd_audio_sof_callback`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **WARN** 49 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08002f40–0x0800389b (2395 B); außerhalb: _ZN10MidiWriter8transmitEv, _ZN12MidiReceiver7receiveEv (Variante: Anker nur für Füllvarianten nötig, deshalb nur Warnung)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x4f4d) im ITCM
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x4d11) im ITCM
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x5255) im ITCM
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x4c51) im ITCM
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x4c4d) im ITCM

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build3d-fx2

- Funktionen gemeinsam: 728, davon ins ITCM verlegt 96, gleiche Adresse 0, andere Größe 1
- nur in der Referenz: –
- nur im neuen Build: –
- Größe geändert: `Reset_Handler` 66→128

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
| `HAL_SAI_TxHalfCpltCallback` | `08013fa8` (24) | `00003a38` (24) |  |
| `HAL_SAI_TxCpltCallback` | `08013fc0` (32) | `00003a50` (32) |  |
| `audioCallback` | `08014d94` (148) | `00003a70` (148) |  |
| `vTaskNotifyGiveFromISR` | `08004cb8` (212) | `00003b04` (212) |  |
| `vPortValidateInterruptPriority` | `08003e88` (92) | `00003bd8` (92) |  |
| `PendSV_Handler` | `08003c90` (100) | `00003ca0` (100) |  |
| `vTaskSwitchContext` | `08004914` (164) | `00003e18` (164) |  |
| `ulTaskNotifyTake` | `080049d8` (104) | `00003ebc` (104) |  |
| `prvAddCurrentTaskToDelayedList` | `08003fdc` (140) | `00003d04` (140) |  |
| `vPortEnterCritical` | `08003c24` (68) | `00003c34` (68) |  |
| `vPortExitCritical` | `08003c68` (40) | `00003c78` (40) |  |
| `uxListRemove` | `08004df8` (40) | `00003f70` (40) |  |
| `vListInsertEnd` | `08004dac` (28) | `00003f24` (28) |  |
| `vListInsert` | `08004dc8` (48) | `00003f40` (48) |  |
| `prvIdleTask` | `08004068` (136) | `00003d90` (136) |  |
| `onProgramReady` | `08014c90` (248) | `08015448` (248) |  |
| `_Z15usbd_tx_convertPlj` | `08014c10` (128) | `080153c8` (128) |  |
| `_Z15usbd_rx_convertPlj` | `08014b54` (188) | `0801530c` (188) |  |
| `updateParameters` | `08012bf0` (54) | `08013664` (54) |  |
| `_ZN10MidiWriter8transmitEv` | `08016878` (76) | `08016e14` (76) |  |
| `_ZN12MidiReceiver7receiveEv` | `080175a4` (104) | `08017b40` (104) |  |
| `usbd_midi_ready` | `08009a4c` (36) | `0800adfc` (36) |  |
| `usbd_midi_tx` | `08009a14` (56) | `0800adc4` (56) |  |
| `getProgramVector` | `08014d88` (12) | `08015540` (12) |  |
| `OTG_FS_IRQHandler` | `080019d4` (12) | `00003f98` (12) |  |
| `HAL_PCD_IRQHandler` | `08006ad0` (1624) | `00003fa4` (1624) |  |
| `USB_ReadInterrupts` | `0800804c` (8) | `000049cc` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `08008054` (14) | `000049d4` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `08008064` (14) | `000049e4` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `08008074` (18) | `000049f4` (18) |  |
| `USB_ReadDevInEPInterrupt` | `08008088` (32) | `00004a08` (32) |  |
| `USB_GetMode` | `080080a8` (8) | `00004a28` (8) |  |
| `USB_ReadPacket` | `08007ee0` (72) | `00004984` (72) |  |
| `USB_WritePacket` | `08007eb4` (42) | `00004958` (42) |  |
| `USB_EPStartXfer` | `08007b60` (548) | `00004734` (548) |  |
| `HAL_PCD_SOFCallback` | `08008ad8` (8) | `00004a58` (8) |  |
| `USBD_LL_SOF` | `080083bc` (36) | `00004be0` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `080099b4` (36) | `00005254` (36) |  |
| `usbd_audio_sof_callback` | `0800988c` (296) | `0000512c` (296) |  |
| `usbd_audio_get_rx_count` | `08014adc` (40) | `00005278` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `08008ab0` (20) | `00004a30` (20) |  |
| `USBD_LL_DataOutStage` | `0800820c` (104) | `00004ac0` (104) |  |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `080093f4` (572) | `00004d10` (572) |  |
| `USBD_LL_GetRxDataSize` | `08008ca4` (8) | `00004ab8` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `0800728c` (18) | `0000464c` (18) |  |
| `USBD_LL_PrepareReceive` | `08008c8c` (22) | `00004aa0` (22) |  |
| `HAL_PCD_EP_Receive` | `0800723c` (78) | `000045fc` (78) |  |
| `HAL_PCD_DataInStageCallback` | `08008ac4` (18) | `00004a44` (18) |  |
| `USBD_LL_DataInStage` | `08008274` (182) | `00004b28` (182) |  |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `08009630` (480) | `00004f4c` (480) |  |
| `USBD_LL_Transmit` | `08008c74` (22) | `00004a88` (22) |  |
| `HAL_PCD_EP_Transmit` | `080072a0` (78) | `00004660` (78) |  |
| `_ZN5Codec16getSampleCounterEv` | `08013f88` (32) | `000052a0` (32) |  |
| `codec_ndtr` | `08001ad4` (20) | `000052c0` (20) |  |
| `HAL_PCD_ISOINIncompleteCallback` | `08008b4c` (8) | `00004a68` (8) |  |
| `USBD_LL_IsoINIncomplete` | `080083e0` (36) | `00004c04` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `08009334` (192) | `00004c50` (192) |  |
| `USBD_LL_FlushEP` | `08008bec` (22) | `00004a70` (22) |  |
| `HAL_PCD_EP_Flush` | `080073f0` (62) | `000046b0` (62) |  |
| `USB_FlushTxFifo` | `080079b8` (36) | `000046f0` (36) |  |
| `USB_FlushRxFifo` | `080079dc` (32) | `00004714` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `08008b44` (8) | `00004a60` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `08008404` (36) | `00004c28` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `08008e88` (4) | `00004c4c` (4) |  |
| `SysTick_Handler` | `0800194c` (24) | `000052d4` (24) |  |
| `HAL_IncTick` | `08009bcc` (24) | `000052ec` (24) |  |
| `HAL_GetTick` | `08009be4` (12) | `00005304` (12) |  |
| `xTaskGetSchedulerState` | `080049b8` (32) | `00005434` (32) |  |
| `xPortSysTickHandler` | `08003cf4` (44) | `00005454` (44) |  |
| `xTaskIncrementTick` | `080048f0` (36) | `00005410` (36) |  |
| `xTaskIncrementTick.part.0` | `080040f0` (256) | `00005310` (256) |  |
| `DMA1_Stream3_IRQHandler` | `08001988` (12) | `00005480` (12) |  |
| `ADC_DMAConvCplt` | `0800cbf8` (108) | `000054a0` (108) |  |
| `ADC_DMAHalfConvCplt` | `0800c90c` (10) | `00005494` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `0800c904` (2) | `0000548c` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `0800c908` (2) | `00005490` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `08019df0` (372) | `0000550c` (372) |  |
| `_ZL14acdcOnLoopLatev` | `08019f64` (448) | `00005680` (448) |  |
| `setLed` | `08012b24` (204) | `000058e0` (204) |  |
| `setLed.constprop.0` | `08012a84` (160) | `00005840` (160) |  |
| `getParameterValue` | `08014e28` (20) | `000059ac` (20) |  |
| `setParameterValue` | `08014e3c` (16) | `000059c0` (16) |  |
| `StartDefaultTask` | `08000438` (12) | `000059d0` (12) |  |
| `loop` | `08002664` (20) | `000059dc` (20) |  |
| `onLoop` | `08012e3c` (4) | `000059f0` (4) |  |
| `_ZN3Owl4loopEv` | `080143f4` (76) | `00005bc0` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `080156ec` (16) | `00005c0c` (16) |  |
| `device_watchdog` | `080027b8` (16) | `00005c1c` (16) |  |
| `vTaskDelayUntil` | `080046a8` (176) | `00005d50` (176) |  |
| `vTaskSuspendAll` | `080048b4` (16) | `00005e00` (16) |  |
| `xTaskResumeAll` | `080048c4` (32) | `00005e10` (32) |  |
| `xTaskResumeAll.part.0` | `080041f0` (292) | `00005c2c` (292) |  |
| `memset` | `080186c0` (16) | `00005e38` (16) |  |
| `memcpy` | `0801876c` (28) | `00005e48` (28) |  |
| `abs` | `080184ee` (8) | `00005e30` (8) |  |
| `onLoop` | `08012e3c` (4) | `000059f0` (4) |  |
| `main` | `08000590` (2332) | `08003b80` (2332) |  |
| `SystemInit` | `080019e0` (240) | `08004f3c` (240) |  |
| `Reset_Handler` | `08018478` (66) | `08002f40` (128) | +62 |
| `_ZN11MidiHandler11handleSysExEPht` | `08013968` (1252) | `0801420c` (1252) |  |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 176, gleiche RAM-Adresse 176

**Ergebnis:** BESTANDEN (0 FAIL, 1 WARN)
