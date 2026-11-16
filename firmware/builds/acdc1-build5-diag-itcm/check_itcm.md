# check_itcm: acdc1-build5-diag-itcm

ELF `firmware/builds/acdc1-build5-diag-itcm/ACDC.elf`, Binary `firmware/builds/acdc1-build5-diag-itcm/ACDC.bin`

Gruppen im ITCM: **A B C D E F G H L** (alle)

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x6938
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x6938 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 13976 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 108904 B <= 131072 B (frei 22168 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 13976 B @ 0x32a0–0x6938 (zusammen 14648 B ab 0x3000). Patch-Heap im CCM: 38600 B (37.7 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ca1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x000056b9 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x00005865 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x00004321 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 104 von 104 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 11690 B
- Funktionen im ITCM insgesamt: 108; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
- **WARN** keine unerwarteten Funktionen im ITCM: _ZL11acdcDiagPutPcS_PKcm.constprop.0, _ZL11acdcDiagPutPcS_PKcm.constprop.1, _ZL17acdcUsbDiagReportm

## 4 Sprünge aus dem ITCM, Veneers

- **ok** keine direkten Sprünge aus dem ITCM hinaus (nur über Veneers)
- **ok** 25 Veneers ITCM → Flash, alle in COLD (Fehler-/Ereignispfad)

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
| `vApplicationStackOverflowHook` | `vTaskSwitchContext` | Fehler: Stack-Überlauf (FreeRTOS) |
| `usbd_audio_error` | `_Z15usbd_rx_convertPlj`, `_Z15usbd_tx_convertPlj`, `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`, `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | Fehler: USB-Puffer über-/unterlaufen (Debug-Meldung) |

- Veneers Flash → ITCM: 27 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `memcpy`, `getParameterValue`, `vTaskSuspendAll`, `setLed`, `device_watchdog`, `xTaskResumeAll`, `vPortValidateInterruptPriority`, `HAL_GetTick` …)
- Indirekte Aufrufe (`blx/bx reg`) in: `ADC_DMAConvCplt`, `HAL_DMA_IRQHandler`, `USBD_LL_DataInStage`, `USBD_LL_DataOutStage`, `USBD_LL_IsoINIncomplete`, `USBD_LL_IsoOUTIncomplete`, `USBD_LL_SOF`, `_ZN12MidiReceiver7receiveEv`, `_ZN3Owl4loopEv`, `onProgramReady`

## 5 Literale im ITCM-Code, die in den Flash zeigen

18 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

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
- `[.text+0x8d4]` ← `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`
- `[.text+0x8dc]` ← `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh`
- `[.text+0x8e4]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x8ec]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **FAIL** 60 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08003930–0x08004223 (2291 B); außerhalb: [.rodata+0x9f4], [.rodata+0x9f8], [.rodata+0x9fc], [.rodata+0xa00], [.rodata+0xa04], [.rodata+0xa08], [.rodata+0xa0c], [.rodata+0xa10], [.rodata+0xa14], [.rodata+0xa18], [.rodata+0xa1c], [.rodata+0xa20], [.rodata+0xa24], [.rodata+0xa28]

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x50b9) im ITCM
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x5225) im ITCM
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x55c1) im ITCM
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x4fe5) im ITCM
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x4fd5) im ITCM

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build4z-fx3k

- Funktionen gemeinsam: 726, davon ins ITCM verlegt 105, gleiche Adresse 33, andere Größe 8
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
| `OTG_FS_IRQHandler` | `08002080` (12) | `00004320` (12) |  |
| `HAL_PCD_IRQHandler` | `0800855c` (1624) | `0000432c` (1624) |  |
| `USB_ReadInterrupts` | `08009898` (8) | `00004d54` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `080098a0` (14) | `00004d5c` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `080098b0` (14) | `00004d6c` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `080098c0` (18) | `00004d7c` (18) |  |
| `USB_ReadDevInEPInterrupt` | `080098d4` (32) | `00004d90` (32) |  |
| `USB_GetMode` | `080098f4` (8) | `00004db0` (8) |  |
| `USB_ReadPacket` | `0800972c` (72) | `00004d0c` (72) |  |
| `USB_WritePacket` | `08009700` (42) | `00004ce0` (42) |  |
| `USB_EPStartXfer` | `080094dc` (548) | `00004abc` (548) |  |
| `HAL_PCD_SOFCallback` | `0800a23c` (8) | `00004de0` (8) |  |
| `USBD_LL_SOF` | `08009b84` (36) | `00004f68` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `0800aff8` (36) | `000055c0` (156) | +120 |
| `usbd_audio_sof_callback` | `0800aed0` (296) | `000054dc` (228) | -68 |
| `usbd_audio_get_rx_count` | `080154fc` (40) | `0000565c` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `0800a214` (20) | `00004db8` (20) |  |
| `USBD_LL_DataOutStage` | `080099d4` (104) | `00004e48` (104) |  |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `0800aab4` (572) | `00005224` (696) | +124 |
| `USBD_LL_GetRxDataSize` | `0800a364` (8) | `00004e40` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `08008d18` (18) | `000049d4` (18) |  |
| `USBD_LL_PrepareReceive` | `0800a34c` (22) | `00004e28` (22) |  |
| `HAL_PCD_EP_Receive` | `08008cc8` (78) | `00004984` (78) |  |
| `HAL_PCD_DataInStageCallback` | `0800a228` (18) | `00004dcc` (18) |  |
| `USBD_LL_DataInStage` | `08009a3c` (182) | `00004eb0` (182) |  |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `0800acf0` (480) | `000050b8` (364) | -116 |
| `USBD_LL_Transmit` | `0800214c` (22) | `00004e10` (22) |  |
| `HAL_PCD_EP_Transmit` | `08008d2c` (78) | `000049e8` (78) |  |
| `_ZN5Codec16getSampleCounterEv` | `08014a2c` (32) | `00005684` (32) |  |
| `codec_ndtr` | `08003ff8` (20) | `000056a4` (20) |  |
| `HAL_PCD_ISOINIncompleteCallback` | `0800a24c` (8) | `00004df0` (8) |  |
| `USBD_LL_IsoINIncomplete` | `08009ba8` (36) | `00004f8c` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `0800a9f4` (192) | `00004fe4` (212) | +20 |
| `USBD_LL_FlushEP` | `0800a2dc` (22) | `00004df8` (22) |  |
| `HAL_PCD_EP_Flush` | `08008e7c` (62) | `00004a38` (62) |  |
| `USB_FlushTxFifo` | `0800934c` (36) | `00004a78` (36) |  |
| `USB_FlushRxFifo` | `08009370` (32) | `00004a9c` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `0800a244` (8) | `00004de8` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `08009bcc` (36) | `00004fb0` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `0800a548` (4) | `00004fd4` (16) | +12 |
| `SysTick_Handler` | `00004320` (24) | `000056b8` (24) |  |
| `HAL_IncTick` | `00004338` (24) | `000056d0` (24) |  |
| `HAL_GetTick` | `00004350` (12) | `000056e8` (12) |  |
| `xTaskGetSchedulerState` | `00004480` (32) | `00005818` (32) |  |
| `xPortSysTickHandler` | `000044a0` (44) | `00005838` (44) |  |
| `xTaskIncrementTick` | `0000445c` (36) | `000057f4` (36) |  |
| `xTaskIncrementTick.part.0` | `0000435c` (256) | `000056f4` (256) |  |
| `DMA1_Stream3_IRQHandler` | `000044cc` (12) | `00005864` (12) |  |
| `ADC_DMAConvCplt` | `000044ec` (108) | `00005884` (108) |  |
| `ADC_DMAHalfConvCplt` | `000044e0` (10) | `00005878` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `000044d8` (2) | `00005870` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `000044dc` (2) | `00005874` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `00004558` (372) | `000058f0` (372) |  |
| `_ZL14acdcOnLoopLatev` | `000046cc` (448) | `00006090` (440) | -8 |
| `setLed` | `0000492c` (204) | `000062e8` (204) |  |
| `setLed.constprop.0` | `0000488c` (160) | `00006248` (160) |  |
| `getParameterValue` | `000049f8` (20) | `000063b4` (20) |  |
| `setParameterValue` | `00004a0c` (16) | `000063c8` (16) |  |
| `StartDefaultTask` | `00004a1c` (12) | `000063d8` (12) |  |
| `loop` | `00004a28` (20) | `000063e4` (20) |  |
| `onLoop` | `00004a3c` (4) | `000063f8` (4) |  |
| `_ZN3Owl4loopEv` | `00004c0c` (76) | `000065c8` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `00004c58` (16) | `00006614` (16) |  |
| `device_watchdog` | `00004c68` (16) | `00006624` (16) |  |
| `vTaskDelayUntil` | `00004d9c` (176) | `00006758` (176) |  |
| `vTaskSuspendAll` | `00004e4c` (16) | `00006808` (16) |  |
| `xTaskResumeAll` | `00004e5c` (32) | `00006818` (32) |  |
| `xTaskResumeAll.part.0` | `00004c78` (292) | `00006634` (292) |  |
| `memset` | `00004e84` (16) | `00006840` (16) |  |
| `memcpy` | `00004e94` (28) | `00006850` (28) |  |
| `abs` | `00004e7c` (8) | `00006838` (8) |  |
| `onLoop` | `00004a3c` (4) | `000063f8` (4) |  |
| `main` | `08002b48` (2332) | `08004508` (2332) |  |
| `SystemInit` | `08003f04` (240) | `080058c4` (240) |  |
| `Reset_Handler` | `08001ee0` (128) | `08003930` (128) |  |
| `_ZN11MidiHandler11handleSysExEPht` | `0801440c` (1252) | `08014b00` (1252) |  |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 178, gleiche RAM-Adresse 116

**Ergebnis:** NICHT BESTANDEN (1 FAIL, 1 WARN)
