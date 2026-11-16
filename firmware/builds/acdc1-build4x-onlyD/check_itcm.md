# check_itcm: acdc1-build4x-onlyD

ELF `firmware/builds/acdc1-build4x-onlyD/ACDC.elf`, Binary `firmware/builds/acdc1-build4x-onlyD/ACDC.bin`

Gruppen im ITCM: **D L**; im Flash (Variante): A SAI-DMA-ISR, B Scheduler, C Audio-Task, E SysTick, F ADC-DMA, G onLoop (07d), H Hauptschleife (2 ms)

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x46b8
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x46b8 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x3298, Größe 5152 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 107136 B <= 131072 B (frei 23936 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 5152 B @ 0x3298–0x46b8 (zusammen 5816 B ab 0x3000). Patch-Heap im CCM: 47432 B (46.3 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x080058f1 PendSV_Handler (erwartet PendSV_Handler im Flash, Gruppe B nicht gewählt)
- **ok** Vektor 15 → 0x080036f5 SysTick_Handler (erwartet SysTick_Handler im Flash, Gruppe E nicht gewählt)
- **ok** Vektor 27 → 0x08001815 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im Flash, Gruppe A nicht gewählt)
- **ok** Vektor 28 → 0x08001821 DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im Flash, Gruppe A nicht gewählt)
- **ok** Vektor 30 → 0x08001839 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im Flash, Gruppe F nicht gewählt)
- **ok** Vektor 117 → 0x00003299 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 43 von 43 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 4950 B
- **ok** 61 von 61 Funktionen der nicht gewählten Gruppen (A, B, C, E, F, G, H) im Flash, zusammen 6656 B
- Funktionen im ITCM insgesamt: 43
- **ok** keine unerwarteten Funktionen im ITCM

## 4 Sprünge aus dem ITCM, Veneers

- **ok** keine direkten Sprünge aus dem ITCM hinaus (nur über Veneers)
- **ok** 22 Veneers ITCM → Flash, alle in COLD (Fehler-/Ereignispfad)

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
| `usbd_midi_rx` | `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | Ereignis: MIDI-Eingang vom Rechner |
| `usbd_audio_rx_start_callback` | `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | Ereignis: Playback-Stream startet |
| `HAL_PCD_ResetCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Bus-Reset |
| `HAL_PCD_ConnectCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Connect |
| `HAL_PCD_DisconnectCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Disconnect |
| `HAL_PCDEx_LPM_Callback` | `HAL_PCD_IRQHandler` | Ereignis: USB-LPM |
| `HAL_PCD_ResumeCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Resume |
| `HAL_PCD_SuspendCallback` | `HAL_PCD_IRQHandler` | Ereignis: USB-Suspend |
| `USBD_LL_StallEP` | `USBD_LL_DataInStage` | Fehler/Control: Endpoint stallen |
| `_Z12debugMessagePKcff` | `usbd_audio_sof_callback` | Fehler: Debug-Meldung |
| `_Z12debugMessagePKcfff` | `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`, `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | Fehler: Debug-Meldung |

- Veneers Flash → ITCM: 7 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `USBD_LL_Transmit`, `memcpy`, `USBD_LL_PrepareReceive`, `memset`, `USBD_LL_FlushEP`, `_ZN5Codec16getSampleCounterEv`, `memset`)
- Indirekte Aufrufe (`blx/bx reg`) in: `USBD_LL_DataInStage`, `USBD_LL_DataOutStage`, `USBD_LL_IsoINIncomplete`, `USBD_LL_IsoOUTIncomplete`, `USBD_LL_SOF`

## 5 Literale im ITCM-Code, die in den Flash zeigen

4 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

- `[.text+0x95c]` ← `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh`
- `[.text+0x964]` ← `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`
- `[.text+0x96c]` ← `usbd_audio_sof_callback`
- `[.text+0x978]` ← `usbd_audio_sof_callback`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **WARN** 48 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x080016c0–0x0800204b (2443 B); außerhalb: PendSV_Handler, SysTick_Handler (Variante: Anker nur für Füllvarianten nötig, deshalb nur Warnung)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x424d) im ITCM
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x4011) im ITCM
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x4555) im ITCM
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x3f51) im ITCM
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x3f4d) im ITCM

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build3d-fx2

- Funktionen gemeinsam: 728, davon ins ITCM verlegt 43, gleiche Adresse 0, andere Größe 1
- nur in der Referenz: –
- nur im neuen Build: –
- Größe geändert: `Reset_Handler` 66→128

| Symbol | Referenz | neu | Δ Größe |
|---|---|---|---|
| `DMA1_Stream0_IRQHandler` | `08001964` (12) | `08001814` (12) |  |
| `DMA1_Stream1_IRQHandler` | `08001970` (12) | `08001820` (12) |  |
| `HAL_DMA_IRQHandler` | `0800c258` (1704) | `0800c668` (1704) |  |
| `SAI_DMATxHalfCplt` | `08003390` (10) | `08005010` (10) |  |
| `SAI_DMATxCplt` | `08003334` (92) | `08004fb4` (92) |  |
| `SAI_DMARxHalfCplt` | `08003400` (10) | `08005080` (10) |  |
| `SAI_DMARxCplt` | `080033a0` (92) | `08005020` (92) |  |
| `HAL_SAI_RxHalfCpltCallback` | `080033fc` (2) | `0800507c` (2) |  |
| `HAL_SAI_RxCpltCallback` | `0800339c` (2) | `0800501c` (2) |  |
| `HAL_SAI_TxHalfCpltCallback` | `08013fa8` (24) | `08014394` (24) |  |
| `HAL_SAI_TxCpltCallback` | `08013fc0` (32) | `080143ac` (32) |  |
| `audioCallback` | `08014d94` (148) | `08015138` (148) |  |
| `vTaskNotifyGiveFromISR` | `08004cb8` (212) | `08006918` (212) |  |
| `vPortValidateInterruptPriority` | `08003e88` (92) | `08005ae8` (92) |  |
| `PendSV_Handler` | `08003c90` (100) | `080058f0` (100) |  |
| `vTaskSwitchContext` | `08004914` (164) | `08006574` (164) |  |
| `ulTaskNotifyTake` | `080049d8` (104) | `08006638` (104) |  |
| `prvAddCurrentTaskToDelayedList` | `08003fdc` (140) | `08005c3c` (140) |  |
| `vPortEnterCritical` | `08003c24` (68) | `08005878` (68) |  |
| `vPortExitCritical` | `08003c68` (40) | `080058bc` (40) |  |
| `uxListRemove` | `08004df8` (40) | `08006a58` (40) |  |
| `vListInsertEnd` | `08004dac` (28) | `08006a0c` (28) |  |
| `vListInsert` | `08004dc8` (48) | `08006a28` (48) |  |
| `prvIdleTask` | `08004068` (136) | `08005cc8` (136) |  |
| `onProgramReady` | `08014c90` (248) | `08015034` (248) |  |
| `_Z15usbd_tx_convertPlj` | `08014c10` (128) | `08014fb4` (128) |  |
| `_Z15usbd_rx_convertPlj` | `08014b54` (188) | `08014ef8` (188) |  |
| `updateParameters` | `08012bf0` (54) | `08012ffc` (54) |  |
| `_ZN10MidiWriter8transmitEv` | `08016878` (76) | `08016ac8` (76) |  |
| `_ZN12MidiReceiver7receiveEv` | `080175a4` (104) | `080177f4` (104) |  |
| `usbd_midi_ready` | `08009a4c` (36) | `08009edc` (36) |  |
| `usbd_midi_tx` | `08009a14` (56) | `08009ea4` (56) |  |
| `getProgramVector` | `08014d88` (12) | `0801512c` (12) |  |
| `OTG_FS_IRQHandler` | `080019d4` (12) | `00003298` (12) |  |
| `HAL_PCD_IRQHandler` | `08006ad0` (1624) | `000032a4` (1624) |  |
| `USB_ReadInterrupts` | `0800804c` (8) | `00003ccc` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `08008054` (14) | `00003cd4` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `08008064` (14) | `00003ce4` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `08008074` (18) | `00003cf4` (18) |  |
| `USB_ReadDevInEPInterrupt` | `08008088` (32) | `00003d08` (32) |  |
| `USB_GetMode` | `080080a8` (8) | `00003d28` (8) |  |
| `USB_ReadPacket` | `08007ee0` (72) | `00003c84` (72) |  |
| `USB_WritePacket` | `08007eb4` (42) | `00003c58` (42) |  |
| `USB_EPStartXfer` | `08007b60` (548) | `00003a34` (548) |  |
| `HAL_PCD_SOFCallback` | `08008ad8` (8) | `00003d58` (8) |  |
| `USBD_LL_SOF` | `080083bc` (36) | `00003ee0` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `080099b4` (36) | `00004554` (36) |  |
| `usbd_audio_sof_callback` | `0800988c` (296) | `0000442c` (296) |  |
| `usbd_audio_get_rx_count` | `08014adc` (40) | `00004578` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `08008ab0` (20) | `00003d30` (20) |  |
| `USBD_LL_DataOutStage` | `0800820c` (104) | `00003dc0` (104) |  |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `080093f4` (572) | `00004010` (572) |  |
| `USBD_LL_GetRxDataSize` | `08008ca4` (8) | `00003db8` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `0800728c` (18) | `0000394c` (18) |  |
| `USBD_LL_PrepareReceive` | `08008c8c` (22) | `00003da0` (22) |  |
| `HAL_PCD_EP_Receive` | `0800723c` (78) | `000038fc` (78) |  |
| `HAL_PCD_DataInStageCallback` | `08008ac4` (18) | `00003d44` (18) |  |
| `USBD_LL_DataInStage` | `08008274` (182) | `00003e28` (182) |  |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `08009630` (480) | `0000424c` (480) |  |
| `USBD_LL_Transmit` | `08008c74` (22) | `00003d88` (22) |  |
| `HAL_PCD_EP_Transmit` | `080072a0` (78) | `00003960` (78) |  |
| `_ZN5Codec16getSampleCounterEv` | `08013f88` (32) | `000045a0` (32) |  |
| `codec_ndtr` | `08001ad4` (20) | `000045c0` (20) |  |
| `HAL_PCD_ISOINIncompleteCallback` | `08008b4c` (8) | `00003d68` (8) |  |
| `USBD_LL_IsoINIncomplete` | `080083e0` (36) | `00003f04` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `08009334` (192) | `00003f50` (192) |  |
| `USBD_LL_FlushEP` | `08008bec` (22) | `00003d70` (22) |  |
| `HAL_PCD_EP_Flush` | `080073f0` (62) | `000039b0` (62) |  |
| `USB_FlushTxFifo` | `080079b8` (36) | `000039f0` (36) |  |
| `USB_FlushRxFifo` | `080079dc` (32) | `00003a14` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `08008b44` (8) | `00003d60` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `08008404` (36) | `00003f28` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `08008e88` (4) | `00003f4c` (4) |  |
| `SysTick_Handler` | `0800194c` (24) | `080036f4` (24) |  |
| `HAL_IncTick` | `08009bcc` (24) | `0800a05c` (24) |  |
| `HAL_GetTick` | `08009be4` (12) | `0800a074` (12) |  |
| `xTaskGetSchedulerState` | `080049b8` (32) | `08006618` (32) |  |
| `xPortSysTickHandler` | `08003cf4` (44) | `08005954` (44) |  |
| `xTaskIncrementTick` | `080048f0` (36) | `08006550` (36) |  |
| `xTaskIncrementTick.part.0` | `080040f0` (256) | `08005d50` (256) |  |
| `DMA1_Stream3_IRQHandler` | `08001988` (12) | `08001838` (12) |  |
| `ADC_DMAConvCplt` | `0800cbf8` (108) | `0800d004` (108) |  |
| `ADC_DMAHalfConvCplt` | `0800c90c` (10) | `0800cd1c` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `0800c904` (2) | `0800cd14` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `0800c908` (2) | `0800cd18` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `08019df0` (372) | `08019f40` (372) |  |
| `_ZL14acdcOnLoopLatev` | `08019f64` (448) | `0801a0b4` (448) |  |
| `setLed` | `08012b24` (204) | `08012f30` (204) |  |
| `setLed.constprop.0` | `08012a84` (160) | `08012e90` (160) |  |
| `getParameterValue` | `08014e28` (20) | `080151cc` (20) |  |
| `setParameterValue` | `08014e3c` (16) | `080151e0` (16) |  |
| `StartDefaultTask` | `08000438` (12) | `080021e4` (12) |  |
| `loop` | `08002664` (20) | `080042fc` (20) |  |
| `onLoop` | `08012e3c` (4) | `08013248` (4) |  |
| `_ZN3Owl4loopEv` | `080143f4` (76) | `080147e0` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `080156ec` (16) | `08015a90` (16) |  |
| `device_watchdog` | `080027b8` (16) | `08004438` (16) |  |
| `vTaskDelayUntil` | `080046a8` (176) | `08006308` (176) |  |
| `vTaskSuspendAll` | `080048b4` (16) | `08006514` (16) |  |
| `xTaskResumeAll` | `080048c4` (32) | `08006524` (32) |  |
| `xTaskResumeAll.part.0` | `080041f0` (292) | `08005e50` (292) |  |
| `memset` | `080186c0` (16) | `000045dc` (16) |  |
| `memcpy` | `0801876c` (28) | `000045ec` (28) |  |
| `abs` | `080184ee` (8) | `000045d4` (8) |  |
| `onLoop` | `08012e3c` (4) | `08013248` (4) |  |
| `main` | `08000590` (2332) | `08002338` (2332) |  |
| `SystemInit` | `080019e0` (240) | `0800370c` (240) |  |
| `Reset_Handler` | `08018478` (66) | `080016c0` (128) | +62 |
| `_ZN11MidiHandler11handleSysExEPht` | `08013968` (1252) | `08013d74` (1252) |  |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 176, gleiche RAM-Adresse 176

**Ergebnis:** BESTANDEN (0 FAIL, 1 WARN)
