# check_itcm: cand-fx9a-gcc14

ELF `firmware/builds/cand-fx9a-gcc14/ACDC.elf`, Binary `firmware/builds/cand-fx9a-gcc14/ACDC.bin`

Gruppen im ITCM: **A B C D E F G H L** (alle)

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x6110
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x6110 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 11888 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 110168 B <= 131072 B (frei 20904 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 11888 B @ 0x32a0–0x6110 (zusammen 12560 B ab 0x3000). Patch-Heap im CCM: 40688 B (39.7 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003a21 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x00005449 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x000055f5 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x000040d9 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 105 von 105 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 11484 B
- Funktionen im ITCM insgesamt: 106; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
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

- Veneers Flash → ITCM: 27 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `usbd_midi_tx`, `vPortValidateInterruptPriority`, `xTaskResumeAll`, `prvAddCurrentTaskToDelayedList`, `device_watchdog`, `getProgramVector`, `USBD_LL_Transmit`, `vPortExitCritical` …)
- Indirekte Aufrufe (`blx/bx reg`) in: `ADC_DMAConvCplt`, `HAL_DMA_IRQHandler`, `USBD_LL_DataInStage`, `USBD_LL_DataOutStage`, `USBD_LL_IsoINIncomplete`, `USBD_LL_IsoOUTIncomplete`, `USBD_LL_SOF`, `_ZN12MidiReceiver7receiveEv`, `_ZN3Owl4loopEv`, `onProgramReady`

## 5 Literale im ITCM-Code, die in den Flash zeigen

6 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

- `[.text+0x8e4]` ← `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh`
- `[.text+0x8ec]` ← `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`
- `[.text+0x8f4]` ← `usbd_audio_sof_callback`
- `[.text+0x900]` ← `usbd_audio_sof_callback`
- `[.text+0x904]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x90c]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **ok** 50 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08003110–0x08003a23 (2323 B)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x50a1) im ITCM
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x4e59) im ITCM
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x53a9) im ITCM
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x4d99) im ITCM
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x4d95) im ITCM

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build11-fx9a

- Funktionen gemeinsam: 734, davon ins ITCM verlegt 106, gleiche Adresse 4, andere Größe 143
- nur in der Referenz: `_strtol_l.constprop.0`
- nur im neuen Build: `_strtol_l.isra.0`
- Größe geändert: `HAL_DMA_IRQHandler` 1704→1060, `_ZN12MidiReceiver7receiveEv` 104→112, `HAL_PCD_IRQHandler` 1624→1660, `HAL_PCD_EP_Receive` 78→76, `HAL_PCD_EP_Flush` 62→60, `USB_EPStartXfer` 548→528, `USB_ReadPacket` 72→76, `USB_ReadDevOutEPInterrupt` 18→16, `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` 572→584, `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` 480→464, `usbd_audio_sof_callback` 296→312, `codec_ndtr` 20→24, `_ZL14acdcOnLoopLatev` 484→548, `setLed` 204→220, `_ZL14acdcOnLoopDarkh` 292→264, `xTaskResumeAll.part.0` 292→288, `vTaskDelayUntil` 176→180, `xTaskResumeAll` 32→40, `USB_GetDevSpeed` 22→24, `USB_EP0StartXfer` 304→248, `USB_ActivateSetup` 44→32, `USB_EP0_OutStart` 88→80, `vPortFree` 204→220, `usbd_midi_rx` 92→84, `_Z12debugMessagePKcfff` 132→128, `main` 2556→2560, `HAL_SAI_MspInit` 420→408, `SystemInit` 240→236, `codec_init` 748→744, `codec_set_gain_in` 72→68, `codec_set_gain_out` 72→68, `flash_write` 364→372, `flash_erase` 284→268, `onChangeMode` 32→28, `HAL_SAI_Init` 1928→1948, `FMC_SDRAM_Init` 388→352, `FMC_SDRAM_Timing_Init` 336→376, `FMC_SDRAM_SendCommand` 164→160, `FMC_SDRAM_ProgramRefreshRate` 68→64, `osThreadCreate` 98→94, `prvAddNewTaskToReadyList` 248→240, `vTaskDelay` 96→92, `UART_SetConfig` 1172→1168, `UART_CheckIdleState` 188→262, `HAL_UART_Init` 380→276, `QSPI_Config` 332→448, `HAL_QSPI_Init` 388→404, `HAL_QSPI_Command` 460→496, `HAL_QSPI_Transmit` 264→282, `HAL_QSPI_Receive` 280→292, `HAL_QSPI_AutoPolling` 552→612, `HAL_QSPI_Abort` 182→194, `HAL_PCD_EP_Open` 124→112, `HAL_PCD_EP_Close` 106→94, `HAL_PCD_EP_SetStall` 136→130, `HAL_PCD_EP_ClrStall` 118→110, `HAL_PCDEx_SetTxFiFo` 262→250, `USB_CoreInit` 268→276, `USB_DevInit` 496→624, `USB_ActivateEndpoint` 144→140, `USB_EPSetStall` 104→110, `USBD_CtlPrepareRx` 30→26, `USBD_StdDevReq` 820→816, `USBD_StdItfReq` 102→106, `USBD_StdEPReq` 312→310, `USBD_FSHS_ManufacturerStrDescriptor` 28→24, `USBD_FSHS_ProductStrDescriptor` 28→24, `USBD_FSHS_ConfigStrDescriptor` 28→24, `USBD_FSHS_InterfaceStrDescriptor` 28→24, `USBD_FSHS_SerialStrDescriptor` 320→340, `_ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req` 860→872, `HAL_RCC_GetSysClockFreq.part.0` 264→228, `HAL_RCC_OscConfig` 1940→1924, `HAL_RCC_GetSysClockFreq` 320→284, `HAL_RCC_ClockConfig` 1044→1060, `DMA_SetConfig` 360→460, `DMA_CalcDMAMUXChannelBaseAndMask` 208→212, `HAL_DMA_Init` 2168→2228, `HAL_DMA_Start_IT` 1140→1016, `HAL_DMA_Abort` 880→876, `HAL_DMA_Abort_IT` 336→408, `HAL_ADC_IRQHandler` 728→732, `HAL_ADC_ConfigChannel` 2500→2404, `HAL_ADC_Start_DMA` 328→324, `ADC_ConfigureBoostMode` 376→344, `HAL_ADC_Init` 1296→1312, `HAL_GPIO_Init` 1008→1444, `HAL_ADCEx_MultiModeConfigChannel` 332→336, `RCCEx_PLL2_Config` 484→480, `RCCEx_PLL3_Config` 484→480, `HAL_RCCEx_PeriphCLKConfig` 3292→3312, `HAL_RCCEx_GetPLL2ClockFreq` 344→308, `HAL_RCCEx_GetPLL3ClockFreq` 344→308, `HAL_RCCEx_GetPLL1ClockFreq` 344→308, `HAL_RCCEx_GetPeriphCLKFreq` 764→736, `FLASH_WaitForLastOperation` 144→140, `HAL_FLASHEx_OBProgram` 940→1020, `HAL_FLASHEx_OBGetConfig` 176→172, `HAL_TIMEx_MasterConfigSynchronization` 512→504, `TIM_OC1_SetConfig` 284→192, `TIM_OC3_SetConfig` 200→196, `HAL_TIM_PWM_Init` 644→620, `TIM_OC2_SetConfig` 204→200, `HAL_TIM_PWM_ConfigChannel` 1196→1192, `HAL_TIM_PWM_Start` 660→560, `HAL_NVIC_SetPriority` 148→140, `HAL_SPI_Init` 776→756, `HAL_SPI_Transmit` 688→684, `HAL_SPI_TransmitReceive` 1032→940, `_Z7initLedv` 240→232, `onSetup` 308→596, `_Z14acdcBootSelectv` 1476→1604, `onResourceUpdate` 420→392, `_ZN11MidiHandler11handleSysExEPht` 1252→1212, `_ZN5Codec5clearEv` 44→40, `_ZN5Codec3setEl` 40→36, `_ZN13PatchRegistry4initEv` 456→356, `_ZN13PatchRegistry11loadProgramEh` 348→304, `updateProgramVector` 372→324, `_Z14runManagerTaskPv` 464→460, `_ZN14ProgramManager12startProgramEb` 80→76, `_ZN14ProgramManager11exitProgramEb` 80→76, `_ZN14ProgramManager12resetProgramEb` 80→76, `serviceCall` 576→552, `_Z8msg_itoaiii` 316→400, `msg_itoa` 316→364, `_ZN19UsbdMidiTransmitter8transmitEv` 118→116, `_ZN10MidiWriter9sendSysExEPht` 1072→1048, `_ZN16SendResourceTask4loopEv` 288→292, `_ZN16SendSettingsTask4loopEv` 704→708, `_ZN14MidiController8sendNameEhhPKcjm` 134→136, `_ZN14MidiController15sendDeviceStatsEv` 392→344, `_ZN14MidiController16sendProgramStatsEv` 180→172, `_GLOBAL__sub_I__ZN12MidiReceiver4initEv` 64→60, `_ZN7Storage5indexEv` 636→616, `_ZN7Storage12readResourceEP14ResourceHeaderPvjj` 124→120, `_ZN7Storage17getResourceByNameEPKc` 208→188, `_ZN7Storage5eraseEm` 224→232, `_ZN7Storage6defragEPvjm` 1036→912, `_ZN7Storage13writeResourceEP14ResourceHeader` 764→716, `memmove` 52→50, `ceilf` 140→148, `__udivmoddi4` 700→760

| Symbol | Referenz | neu | Δ Größe |
|---|---|---|---|
| `DMA1_Stream0_IRQHandler` | `000032a0` (12) | `000032a0` (12) |  |
| `DMA1_Stream1_IRQHandler` | `000032ac` (12) | `000032ac` (12) |  |
| `HAL_DMA_IRQHandler` | `000032b8` (1704) | `000032b8` (1060) | -644 |
| `SAI_DMATxHalfCplt` | `000039bc` (10) | `00003738` (10) |  |
| `SAI_DMATxCplt` | `00003960` (92) | `000036dc` (92) |  |
| `SAI_DMARxHalfCplt` | `00003a24` (10) | `000037a0` (10) |  |
| `SAI_DMARxCplt` | `000039c8` (92) | `00003744` (92) |  |
| `HAL_SAI_RxHalfCpltCallback` | `00003a30` (24) | `000037ac` (24) |  |
| `HAL_SAI_RxCpltCallback` | `00003a48` (32) | `000037c4` (32) |  |
| `HAL_SAI_TxHalfCpltCallback` | `00003a68` (2) | `000037e4` (2) |  |
| `HAL_SAI_TxCpltCallback` | `00003a6c` (2) | `000037e8` (2) |  |
| `audioCallback` | `00003a70` (148) | `000037ec` (148) |  |
| `vTaskNotifyGiveFromISR` | `00003b04` (212) | `00003880` (212) |  |
| `vPortValidateInterruptPriority` | `00003bd8` (92) | `00003954` (92) |  |
| `PendSV_Handler` | `00003ca0` (100) | `00003a20` (100) |  |
| `vTaskSwitchContext` | `00003e18` (164) | `00003b98` (164) |  |
| `ulTaskNotifyTake` | `00003ebc` (104) | `00003c3c` (104) |  |
| `prvAddCurrentTaskToDelayedList` | `00003d04` (140) | `00003a84` (140) |  |
| `vPortEnterCritical` | `00003c34` (68) | `000039b0` (68) |  |
| `vPortExitCritical` | `00003c78` (40) | `000039f4` (40) |  |
| `uxListRemove` | `00003f70` (40) | `00003cf0` (40) |  |
| `vListInsertEnd` | `00003f24` (28) | `00003ca4` (28) |  |
| `vListInsert` | `00003f40` (48) | `00003cc0` (48) |  |
| `prvIdleTask` | `00003d90` (136) | `00003b10` (136) |  |
| `onProgramReady` | `000040d4` (248) | `00003e54` (248) |  |
| `_Z15usbd_tx_convertPlj` | `00004054` (128) | `00003dd4` (128) |  |
| `_Z15usbd_rx_convertPlj` | `00003f98` (188) | `00003d18` (188) |  |
| `updateParameters` | `000041d8` (54) | `00003f58` (54) |  |
| `_ZN10MidiWriter8transmitEv` | `00004210` (124) | `00003f90` (124) |  |
| `_ZN12MidiReceiver7receiveEv` | `0000428c` (104) | `0000400c` (112) | +8 |
| `usbd_midi_ready` | `0000432c` (36) | `000040b4` (36) |  |
| `usbd_midi_tx` | `000042f4` (56) | `0000407c` (56) |  |
| `getProgramVector` | `000041cc` (12) | `00003f4c` (12) |  |
| `OTG_FS_IRQHandler` | `00004350` (12) | `000040d8` (12) |  |
| `HAL_PCD_IRQHandler` | `0000435c` (1624) | `000040e4` (1660) | +36 |
| `USB_ReadInterrupts` | `00004d84` (8) | `00004b18` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `00004d8c` (14) | `00004b20` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `00004d9c` (14) | `00004b30` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `00004dac` (18) | `00004b40` (16) | -2 |
| `USB_ReadDevInEPInterrupt` | `00004dc0` (32) | `00004b50` (32) |  |
| `USB_GetMode` | `00004de0` (8) | `00004b70` (8) |  |
| `USB_ReadPacket` | `00004d3c` (72) | `00004acc` (76) | +4 |
| `USB_WritePacket` | `00004d10` (42) | `00004aa0` (42) |  |
| `USB_EPStartXfer` | `00004aec` (548) | `00004890` (528) | -20 |
| `HAL_PCD_SOFCallback` | `00004e10` (8) | `00004ba0` (8) |  |
| `USBD_LL_SOF` | `00004f98` (36) | `00004d28` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `0000560c` (64) | `000053a8` (64) |  |
| `usbd_audio_sof_callback` | `000054e4` (296) | `00005270` (312) | +16 |
| `usbd_audio_get_rx_count` | `0000564c` (40) | `000053e8` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `00004de8` (20) | `00004b78` (20) |  |
| `USBD_LL_DataOutStage` | `00004e78` (104) | `00004c08` (104) |  |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `000050c8` (572) | `00004e58` (584) | +12 |
| `USBD_LL_GetRxDataSize` | `00004e70` (8) | `00004c00` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `00004a04` (18) | `000047ac` (18) |  |
| `USBD_LL_PrepareReceive` | `00004e58` (22) | `00004be8` (22) |  |
| `HAL_PCD_EP_Receive` | `000049b4` (78) | `00004760` (76) | -2 |
| `HAL_PCD_DataInStageCallback` | `00004dfc` (18) | `00004b8c` (18) |  |
| `USBD_LL_DataInStage` | `00004ee0` (182) | `00004c70` (182) |  |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `00005304` (480) | `000050a0` (464) | -16 |
| `USBD_LL_Transmit` | `00004e40` (22) | `00004bd0` (22) |  |
| `HAL_PCD_EP_Transmit` | `00004a18` (78) | `000047c0` (78) |  |
| `_ZN5Codec16getSampleCounterEv` | `00005674` (32) | `00005410` (32) |  |
| `codec_ndtr` | `00005694` (20) | `00005430` (24) | +4 |
| `HAL_PCD_ISOINIncompleteCallback` | `00004e20` (8) | `00004bb0` (8) |  |
| `USBD_LL_IsoINIncomplete` | `00004fbc` (36) | `00004d4c` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `00005008` (192) | `00004d98` (192) |  |
| `USBD_LL_FlushEP` | `00004e28` (22) | `00004bb8` (22) |  |
| `HAL_PCD_EP_Flush` | `00004a68` (62) | `00004810` (60) | -2 |
| `USB_FlushTxFifo` | `00004aa8` (36) | `0000484c` (36) |  |
| `USB_FlushRxFifo` | `00004acc` (32) | `00004870` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `00004e18` (8) | `00004ba8` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `00004fe0` (36) | `00004d70` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `00005004` (4) | `00004d94` (4) |  |
| `SysTick_Handler` | `000056a8` (24) | `00005448` (24) |  |
| `HAL_IncTick` | `000056c0` (24) | `00005460` (24) |  |
| `HAL_GetTick` | `000056d8` (12) | `00005478` (12) |  |
| `xTaskGetSchedulerState` | `00005808` (32) | `000055a8` (32) |  |
| `xPortSysTickHandler` | `00005828` (44) | `000055c8` (44) |  |
| `xTaskIncrementTick` | `000057e4` (36) | `00005584` (36) |  |
| `xTaskIncrementTick.part.0` | `000056e4` (256) | `00005484` (256) |  |
| `DMA1_Stream3_IRQHandler` | `00005854` (12) | `000055f4` (12) |  |
| `ADC_DMAConvCplt` | `00005874` (108) | `00005614` (108) |  |
| `ADC_DMAHalfConvCplt` | `00005868` (10) | `00005608` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `00005860` (2) | `00005600` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `00005864` (2) | `00005604` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `000058e0` (372) | `00005680` (372) |  |
| `_ZL14acdcOnLoopLatev` | `00005a54` (484) | `000057f4` (548) | +64 |
| `_ZL14acdcOnLoopDarkh` | `00005de8` (292) | `00005bd8` (264) | -28 |
| `setLed` | `00005cd8` (204) | `00005ab8` (220) | +16 |
| `setLed.constprop.0` | `00005c38` (160) | `00005a18` (160) |  |
| `getParameterValue` | `00005da4` (20) | `00005b94` (20) |  |
| `setParameterValue` | `00005db8` (16) | `00005ba8` (16) |  |
| `StartDefaultTask` | `00005dc8` (12) | `00005bb8` (12) |  |
| `loop` | `00005dd4` (20) | `00005bc4` (20) |  |
| `onLoop` | `00005f0c` (24) | `00005ce0` (24) |  |
| `_ZN3Owl4loopEv` | `00005fb8` (76) | `00005d8c` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `00006004` (16) | `00005dd8` (16) |  |
| `device_watchdog` | `00006014` (16) | `00005de8` (16) |  |
| `vTaskDelayUntil` | `00006148` (176) | `00005f18` (180) | +4 |
| `vTaskSuspendAll` | `000061f8` (16) | `00005fcc` (16) |  |
| `xTaskResumeAll` | `00006208` (32) | `00005fdc` (40) | +8 |
| `xTaskResumeAll.part.0` | `00006024` (292) | `00005df8` (288) | -4 |
| `memset` | `00006230` (16) | `0000600c` (16) |  |
| `memcpy` | `00006240` (28) | `0000601c` (28) |  |
| `abs` | `00006228` (8) | `00006004` (8) |  |
| `onLoop` | `00005f0c` (24) | `00005ce0` (24) |  |
| `main` | `08003f70` (2556) | `08003d08` (2560) | +4 |
| `SystemInit` | `0800540c` (240) | `08005198` (236) | -4 |
| `Reset_Handler` | `08003330` (128) | `08003110` (128) |  |
| `_ZN11MidiHandler11handleSysExEPht` | `08014d60` (1252) | `08014d70` (1212) | -40 |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 181, gleiche RAM-Adresse 181

**Ergebnis:** BESTANDEN (0 FAIL, 0 WARN)
