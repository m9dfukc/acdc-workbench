# check_itcm: acdc1-build6-fx4a

ELF `firmware/builds/acdc1-build6-fx4a/ACDC.elf`, Binary `firmware/builds/acdc1-build6-fx4a/ACDC.bin`

Gruppen im ITCM: **A B C D E F G H L** (alle)

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x6308
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x6308 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 12392 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 108496 B <= 131072 B (frei 22576 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 12392 B @ 0x32a0–0x6308 (zusammen 13064 B ab 0x3000). Patch-Heap im CCM: 40184 B (39.2 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ca1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x00005679 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x00005825 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x00004321 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 104 von 104 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 11670 B
- Funktionen im ITCM insgesamt: 105; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
- **ok** keine unerwarteten Funktionen im ITCM

## 4 Sprünge aus dem ITCM, Veneers

- **ok** keine direkten Sprünge aus dem ITCM hinaus (nur über Veneers)
- **ok** 27 Veneers ITCM → Flash, alle in COLD (Fehler-/Ereignispfad)

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
| `usbd_audio_error` | `_Z15usbd_rx_convertPlj`, `_Z15usbd_tx_convertPlj` | Fehler: USB-Puffer über-/unterlaufen (Debug-Meldung) |

- Veneers Flash → ITCM: 27 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `setLed`, `xTaskResumeAll.part.0`, `getParameterValue`, `uxListRemove`, `vTaskSwitchContext`, `USBD_LL_FlushEP`, `vPortValidateInterruptPriority`, `xTaskResumeAll` …)
- Indirekte Aufrufe (`blx/bx reg`) in: `ADC_DMAConvCplt`, `HAL_DMA_IRQHandler`, `USBD_LL_DataInStage`, `USBD_LL_DataOutStage`, `USBD_LL_IsoINIncomplete`, `USBD_LL_IsoOUTIncomplete`, `USBD_LL_SOF`, `_ZN12MidiReceiver7receiveEv`, `_ZN3Owl4loopEv`, `onProgramReady`

## 5 Literale im ITCM-Code, die in den Flash zeigen

6 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

- `[.text+0x92c]` ← `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh`
- `[.text+0x934]` ← `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`
- `[.text+0x93c]` ← `usbd_audio_sof_callback`
- `[.text+0x948]` ← `usbd_audio_sof_callback`
- `[.text+0x94c]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x954]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **ok** 50 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08003300–0x08003c5b (2395 B)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x52d5) im ITCM
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x5099) im ITCM
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x55dd) im ITCM
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x4fd9) im ITCM
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x4fd5) im ITCM

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build5c-fx3l

- Funktionen gemeinsam: 728, davon ins ITCM verlegt 105, gleiche Adresse 87, andere Größe 3
- nur in der Referenz: –
- nur im neuen Build: `_Z14acdcBootSelectv`, `_ZL12acdcReadSlotv`, `_ZN3Owl16getOperationModeEv`, `_ZN7Storage11getFreeSizeEm`
- Größe geändert: `_ZL14acdcOnLoopLatev` 448→484, `onSetup` 292→304, `_Z9bootstrapv` 168→176

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
| `OTG_FS_IRQHandler` | `00004320` (12) | `00004320` (12) |  |
| `HAL_PCD_IRQHandler` | `0000432c` (1624) | `0000432c` (1624) |  |
| `USB_ReadInterrupts` | `00004d54` (8) | `00004d54` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `00004d5c` (14) | `00004d5c` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `00004d6c` (14) | `00004d6c` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `00004d7c` (18) | `00004d7c` (18) |  |
| `USB_ReadDevInEPInterrupt` | `00004d90` (32) | `00004d90` (32) |  |
| `USB_GetMode` | `00004db0` (8) | `00004db0` (8) |  |
| `USB_ReadPacket` | `00004d0c` (72) | `00004d0c` (72) |  |
| `USB_WritePacket` | `00004ce0` (42) | `00004ce0` (42) |  |
| `USB_EPStartXfer` | `00004abc` (548) | `00004abc` (548) |  |
| `HAL_PCD_SOFCallback` | `00004de0` (8) | `00004de0` (8) |  |
| `USBD_LL_SOF` | `00004f68` (36) | `00004f68` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `000055dc` (64) | `000055dc` (64) |  |
| `usbd_audio_sof_callback` | `000054b4` (296) | `000054b4` (296) |  |
| `usbd_audio_get_rx_count` | `0000561c` (40) | `0000561c` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `00004db8` (20) | `00004db8` (20) |  |
| `USBD_LL_DataOutStage` | `00004e48` (104) | `00004e48` (104) |  |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `00005098` (572) | `00005098` (572) |  |
| `USBD_LL_GetRxDataSize` | `00004e40` (8) | `00004e40` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `000049d4` (18) | `000049d4` (18) |  |
| `USBD_LL_PrepareReceive` | `00004e28` (22) | `00004e28` (22) |  |
| `HAL_PCD_EP_Receive` | `00004984` (78) | `00004984` (78) |  |
| `HAL_PCD_DataInStageCallback` | `00004dcc` (18) | `00004dcc` (18) |  |
| `USBD_LL_DataInStage` | `00004eb0` (182) | `00004eb0` (182) |  |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `000052d4` (480) | `000052d4` (480) |  |
| `USBD_LL_Transmit` | `00004e10` (22) | `00004e10` (22) |  |
| `HAL_PCD_EP_Transmit` | `000049e8` (78) | `000049e8` (78) |  |
| `_ZN5Codec16getSampleCounterEv` | `00005644` (32) | `00005644` (32) |  |
| `codec_ndtr` | `00005664` (20) | `00005664` (20) |  |
| `HAL_PCD_ISOINIncompleteCallback` | `00004df0` (8) | `00004df0` (8) |  |
| `USBD_LL_IsoINIncomplete` | `00004f8c` (36) | `00004f8c` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `00004fd8` (192) | `00004fd8` (192) |  |
| `USBD_LL_FlushEP` | `00004df8` (22) | `00004df8` (22) |  |
| `HAL_PCD_EP_Flush` | `00004a38` (62) | `00004a38` (62) |  |
| `USB_FlushTxFifo` | `00004a78` (36) | `00004a78` (36) |  |
| `USB_FlushRxFifo` | `00004a9c` (32) | `00004a9c` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `00004de8` (8) | `00004de8` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `00004fb0` (36) | `00004fb0` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `00004fd4` (4) | `00004fd4` (4) |  |
| `SysTick_Handler` | `00005678` (24) | `00005678` (24) |  |
| `HAL_IncTick` | `00005690` (24) | `00005690` (24) |  |
| `HAL_GetTick` | `000056a8` (12) | `000056a8` (12) |  |
| `xTaskGetSchedulerState` | `000057d8` (32) | `000057d8` (32) |  |
| `xPortSysTickHandler` | `000057f8` (44) | `000057f8` (44) |  |
| `xTaskIncrementTick` | `000057b4` (36) | `000057b4` (36) |  |
| `xTaskIncrementTick.part.0` | `000056b4` (256) | `000056b4` (256) |  |
| `DMA1_Stream3_IRQHandler` | `00005824` (12) | `00005824` (12) |  |
| `ADC_DMAConvCplt` | `00005844` (108) | `00005844` (108) |  |
| `ADC_DMAHalfConvCplt` | `00005838` (10) | `00005838` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `00005830` (2) | `00005830` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `00005834` (2) | `00005834` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `000058b0` (372) | `000058b0` (372) |  |
| `_ZL14acdcOnLoopLatev` | `00005a24` (448) | `00005a24` (484) | +36 |
| `setLed` | `00005c84` (204) | `00005ca8` (204) |  |
| `setLed.constprop.0` | `00005be4` (160) | `00005c08` (160) |  |
| `getParameterValue` | `00005d50` (20) | `00005d74` (20) |  |
| `setParameterValue` | `00005d64` (16) | `00005d88` (16) |  |
| `StartDefaultTask` | `00005d74` (12) | `00005d98` (12) |  |
| `loop` | `00005d80` (20) | `00005da4` (20) |  |
| `onLoop` | `00005d94` (4) | `00005db8` (4) |  |
| `_ZN3Owl4loopEv` | `00005f64` (76) | `00005f88` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `00005fb0` (16) | `00005fd4` (16) |  |
| `device_watchdog` | `00005fc0` (16) | `00005fe4` (16) |  |
| `vTaskDelayUntil` | `000060f4` (176) | `00006118` (176) |  |
| `vTaskSuspendAll` | `000061a4` (16) | `000061c8` (16) |  |
| `xTaskResumeAll` | `000061b4` (32) | `000061d8` (32) |  |
| `xTaskResumeAll.part.0` | `00005fd0` (292) | `00005ff4` (292) |  |
| `memset` | `000061dc` (16) | `00006200` (16) |  |
| `memcpy` | `000061ec` (28) | `00006210` (28) |  |
| `abs` | `000061d4` (8) | `000061f8` (8) |  |
| `onLoop` | `00005d94` (4) | `00005db8` (4) |  |
| `main` | `08003f20` (2332) | `08003f40` (2332) |  |
| `SystemInit` | `080052dc` (240) | `080052fc` (240) |  |
| `Reset_Handler` | `080032e0` (128) | `08003300` (128) |  |
| `_ZN11MidiHandler11handleSysExEPht` | `08014518` (1252) | `0801493c` (1252) |  |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 179, gleiche RAM-Adresse 179

**Ergebnis:** BESTANDEN (0 FAIL, 0 WARN)
