# check_itcm: cand-fx9a-gcc15

ELF `firmware/builds/cand-fx9a-gcc15/ACDC.elf`, Binary `firmware/builds/cand-fx9a-gcc15/ACDC.bin`

Gruppen im ITCM: **A B C D E F G H L** (alle)

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x64f0
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x64f0 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 12880 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 112568 B <= 131072 B (frei 18504 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 12880 B @ 0x32a0–0x64f0 (zusammen 13552 B ab 0x3000). Patch-Heap im CCM: 39696 B (38.8 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003cd1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x00005821 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x000059c9 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x00004365 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 105 von 105 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 12474 B
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

- `[.text+0x8f4]` ← `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh`
- `[.text+0x8fc]` ← `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`
- `[.text+0x904]` ← `usbd_audio_sof_callback`
- `[.text+0x910]` ← `usbd_audio_sof_callback`
- `[.text+0x914]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x91c]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **ok** 50 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x080034f0–0x08003e13 (2339 B)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x53a9) im ITCM
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x515d) im ITCM
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x56d1) im ITCM
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x5099) im ITCM
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x5095) im ITCM

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 8 nm-Vergleich gegen acdc1-build11-fx9a

- Funktionen gemeinsam: 734, davon ins ITCM verlegt 106, gleiche Adresse 6, andere Größe 259
- nur in der Referenz: `_strtol_l.constprop.0`
- nur im neuen Build: `_strtol_l.isra.0`
- Größe geändert: `HAL_DMA_IRQHandler` 1704→1726, `SAI_DMATxCplt` 92→96, `SAI_DMARxCplt` 92→96, `audioCallback` 148→152, `vTaskNotifyGiveFromISR` 212→224, `vTaskSwitchContext` 164→184, `ulTaskNotifyTake` 104→112, `vListInsertEnd` 28→26, `vListInsert` 48→54, `uxListRemove` 40→36, `_Z15usbd_rx_convertPlj` 188→160, `_Z15usbd_tx_convertPlj` 128→116, `onProgramReady` 248→208, `_ZN10MidiWriter8transmitEv` 124→132, `_ZN12MidiReceiver7receiveEv` 104→112, `usbd_midi_tx` 56→60, `HAL_PCD_IRQHandler` 1624→1720, `HAL_PCD_EP_Receive` 78→88, `HAL_PCD_EP_Transmit` 78→80, `HAL_PCD_EP_Flush` 62→72, `USB_EPStartXfer` 548→532, `USB_WritePacket` 42→40, `USB_ReadPacket` 72→78, `USB_ReadDevOutEPInterrupt` 18→16, `HAL_PCD_DataOutStageCallback` 20→22, `HAL_PCD_DataInStageCallback` 18→20, `USBD_LL_DataOutStage` 104→110, `USBD_LL_DataInStage` 182→198, `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` 192→196, `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` 572→588, `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` 480→500, `usbd_audio_sof_callback` 296→308, `codec_ndtr` 20→200, `xTaskIncrementTick.part.0` 256→252, `_ZL20acdcMeasureRawInputsv` 372→392, `_ZL14acdcOnLoopLatev` 484→552, `setLed` 204→216, `_ZL14acdcOnLoopDarkh` 292→264, `xTaskResumeAll.part.0` 292→288, `vTaskDelayUntil` 176→180, `USBD_CtlContinueSendData` 18→16, `USBD_CtlContinueRx` 18→16, `USBD_CtlSendStatus` 22→24, `USBD_CtlReceiveStatus` 22→24, `USB_GetDevSpeed` 22→24, `USB_EP0StartXfer` 304→254, `USB_ActivateSetup` 44→32, `USB_EP0_OutStart` 88→84, `HAL_RCC_GetHCLKFreq` 128→140, `vPortFree` 204→228, `usbd_midi_rx` 92→84, `usbd_audio_rx_start_callback` 32→28, `usbd_audio_error` 124→128, `_Z12debugMessagePKcff` 100→96, `_Z12debugMessagePKcfff` 132→124, `SystemClock_Config` 212→220, `HAL_MspInit` 52→48, `HAL_ADC_MspInit` 292→308, `HAL_SPI_MspInit` 340→348, `HAL_TIM_MspPostInit` 300→324, `HAL_UART_MspInit` 352→360, `HAL_PCD_MspInit` 200→212, `HAL_SAI_MspInit` 420→424, `codec_highpass` 76→72, `codec_init` 748→744, `qspi_write_enable` 132→140, `flash_write` 364→348, `flash_erase` 284→268, `flash_init` 124→132, `crc32` 48→44, `eeprom_erase_sector` 32→34, `data_to_sysex` 106→114, `sysex_to_data` 68→66, `onChangeMode` 32→28, `HAL_SAI_Init` 1928→1952, `HAL_SAI_Transmit_DMA` 272→268, `HAL_SAI_IRQHandler` 344→388, `SAI_DMAAbort` 112→120, `HAL_SDRAM_SendCommand` 62→66, `HAL_SDRAM_ProgramRefreshRate` 48→60, `FMC_SDRAM_Init` 388→352, `FMC_SDRAM_SendCommand` 164→168, `FMC_SDRAM_ProgramRefreshRate` 68→88, `osThreadCreate` 98→102, `pxPortInitialiseStack` 48→44, `xPortStartScheduler` 320→324, `prvAddNewTaskToReadyList` 248→236, `xTaskCreateStatic` 324→336, `xTaskCreate` 286→294, `vTaskStartScheduler` 252→264, `xTaskNotifyWait` 140→144, `xTaskGenericNotify` 208→228, `xTaskGenericNotifyFromISR` 284→304, `pvPortMalloc` 392→412, `UART_SetConfig` 1172→1196, `UART_CheckIdleState` 188→192, `HAL_UART_Init` 380→276, `HAL_UARTEx_DisableFifoMode` 188→208, `HAL_UARTEx_SetTxFifoThreshold` 288→308, `HAL_UARTEx_SetRxFifoThreshold` 288→308, `QSPI_Config` 332→486, `HAL_QSPI_Init` 388→424, `HAL_QSPI_Command` 460→508, `HAL_QSPI_Transmit` 264→266, `HAL_QSPI_Receive` 280→286, `HAL_QSPI_AutoPolling` 552→624, `HAL_QSPI_IRQHandler` 528→584, `HAL_QSPI_Abort` 182→206, `HAL_PCD_Init` 340→352, `HAL_PCD_Start` 66→68, `HAL_PCD_SetAddress` 42→52, `HAL_PCD_EP_Open` 124→122, `HAL_PCD_EP_SetStall` 136→150, `HAL_PCD_EP_ClrStall` 118→120, `HAL_PCDEx_SetTxFiFo` 262→266, `HAL_PCDEx_ActivateLPM` 48→40, `USB_CoreInit` 268→276, `USB_DevInit` 496→624, `USB_ActivateEndpoint` 144→148, `USBD_RegisterClass` 44→46, `USBD_LL_SetupStage` 96→108, `USBD_LL_Suspend` 22→20, `USBD_LL_Resume` 22→20, `USBD_CtlPrepareRx` 30→26, `USBD_StdDevReq` 820→840, `USBD_StdItfReq` 102→114, `USBD_StdEPReq` 312→382, `USBD_GetString` 82→96, `USBD_FSHS_ManufacturerStrDescriptor` 28→24, `USBD_FSHS_ProductStrDescriptor` 28→24, `USBD_FSHS_ConfigStrDescriptor` 28→24, `USBD_FSHS_InterfaceStrDescriptor` 28→24, `USBD_FSHS_SerialStrDescriptor` 320→312, `_ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef` 76→102, `_ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req` 860→888, `HAL_InitTick` 76→84, `HAL_RCC_GetSysClockFreq.part.0` 264→232, `HAL_RCC_DeInit` 416→420, `HAL_RCC_OscConfig` 1940→1860, `HAL_RCC_GetSysClockFreq` 320→288, `HAL_RCC_ClockConfig` 1044→1060, `HAL_RCC_GetPCLK1Freq` 144→152, `HAL_RCC_GetPCLK2Freq` 144→152, `DMA_SetConfig` 360→448, `DMA_CalcBaseAndBitshift` 256→252, `DMA_CalcDMAMUXChannelBaseAndMask` 208→224, `HAL_DMA_Init` 2168→2144, `HAL_DMA_Start_IT` 1140→856, `HAL_DMA_Abort` 880→876, `HAL_DMA_Abort_IT` 336→360, `HAL_ADC_IRQHandler` 728→724, `HAL_ADC_ConfigChannel` 2500→2472, `ADC_Enable` 176→168, `HAL_ADC_Start_DMA` 328→360, `HAL_ADC_Stop_DMA` 200→208, `ADC_ConfigureBoostMode` 376→348, `HAL_ADC_Init` 1296→1352, `HAL_GPIO_Init` 1008→1404, `HAL_GPIO_WritePin` 52→76, `HAL_ADCEx_MultiModeConfigChannel` 332→364, `RCCEx_PLL2_Config` 484→480, `RCCEx_PLL3_Config` 484→480, `HAL_RCCEx_PeriphCLKConfig` 3292→3308, `HAL_RCCEx_GetPLL2ClockFreq` 344→312, `HAL_RCCEx_GetPLL3ClockFreq` 344→312, `HAL_RCCEx_GetPLL1ClockFreq` 344→312, `HAL_RCCEx_GetPeriphCLKFreq` 764→692, `FLASH_WaitForLastOperation` 144→132, `HAL_FLASHEx_Erase` 400→396, `HAL_FLASHEx_OBProgram` 940→1160, `HAL_FLASHEx_OBGetConfig` 176→164, `HAL_TIMEx_MasterConfigSynchronization` 512→520, `HAL_TIMEx_ConfigBreakDeadTime` 536→544, `TIM_OC1_SetConfig` 284→300, `TIM_OC3_SetConfig` 200→220, `TIM_OC4_SetConfig` 140→144, `HAL_TIM_Base_Start` 336→360, `HAL_TIM_PWM_Init` 644→668, `TIM_OC2_SetConfig` 204→224, `HAL_TIM_PWM_ConfigChannel` 1196→1176, `TIM_CCxChannelCmd` 188→200, `HAL_TIM_PWM_Start` 660→576, `HAL_NVIC_SetPriorityGrouping` 60→68, `HAL_NVIC_SetPriority` 148→152, `SPI_CloseTransfer` 184→192, `HAL_SPI_Transmit` 688→680, `HAL_SPI_TransmitReceive` 1032→912, `HAL_SPI_IRQHandler` 568→688, `_ZL12acdcReadSlotv` 92→96, `_Z7initLedv` 240→248, `onSetup` 308→752, `_Z14acdcBootSelectv` 1476→1644, `onResourceUpdate` 420→380, `_GLOBAL__sub_I_led_in1` 196→204, `_ZN19ApplicationSettings4initEv` 172→176, `_ZN19ApplicationSettings5resetEv` 68→64, `_ZN11MidiHandler11handleSysExEPht` 1252→1256, `_ZN5Codec5clearEv` 44→40, `_ZN5Codec3setEl` 40→36, `_ZN16SystemMidiReader13readMidiFrameEPh` 620→628, `midiSetOutputChannel` 24→20, `_ZN3Owl17setBackgroundTaskEP14BackgroundTask` 56→88, `_GLOBAL__sub_I_owl` 40→36, `_ZN13PatchRegistry4initEv` 456→388, `_ZN13PatchRegistry11loadProgramEh` 348→320, `_Z16sendResourceTaskPv` 60→76, `_Z19onSetPatchParameterhs` 22→26, `setButtonValue` 88→120, `updateProgramVector` 372→324, `_Z12runAudioTaskPv` 316→324, `_Z9bootstrapv` 176→192, `_Z14runManagerTaskPv` 464→460, `_ZN14ProgramManager18loadDynamicProgramEP14ResourceHeader` 240→236, `_ZN14ProgramManager14eraseFromFlashEh` 68→72, `_ZN14ProgramManager11saveToFlashEhPvm` 84→96, `serviceCall` 576→552, `_Z8msg_itoaiii` 316→368, `msg_itoa` 316→300, `msg_ftoa` 396→392, `debugMessage` 40→48, `_Z12debugMessagePKci` 416→428, `_ZN17BootloaderStorage5storeEPvj` 40→44, `_ZN17BootloaderStorage6unlockEv` 28→36, `_ZN17BootloaderStorage4lockEv` 28→36, `_ZN19UsbdMidiTransmitter8transmitEv` 118→126, `_ZN19UsbdMidiTransmitter5writeE11MidiMessage` 276→268, `_ZN10MidiWriter6sendPcEh` 316→300, `_ZN10MidiWriter6sendCcEhh` 316→300, `_ZN10MidiWriter9sendSysExEPht` 1072→1040, `_ZN10MidiWriter4sendE11MidiMessage` 284→268, `_ZN16SendResourceTask4loopEv` 288→284, `_ZN14MidiController24sendPatchParameterValuesEv` 108→98, `_ZN16SendSettingsTask4loopEv` 704→716, `_ZN14MidiController12sendResourceEP8Resource` 72→80, `_ZN14MidiController8sendNameEhhPKcjm` 134→144, `_ZN14MidiController13sendPatchNameEh` 184→188, `_ZN18SendPatchNamesTask4loopEv` 240→248, `_ZN14MidiController22sendPatchParameterNameE16PatchParameterIdPKc` 66→70, `_ZN14MidiController15sendDeviceStatsEv` 392→368, `_ZN14MidiController16sendProgramStatsEv` 180→168, `_ZN14MidiController14sendDeviceInfoEv` 152→156, `_ZN14MidiController18sendProgramMessageEv` 58→60, `_ZN14MidiController19sendFirmwareVersionEv` 46→44, `_ZN14MidiController21sendBootloaderVersionEv` 46→44, `_ZN14MidiController12sendDeviceIdEv` 116→112, `_GLOBAL__sub_I__ZN12MidiReceiver4initEv` 64→60, `_ZN7Storage5indexEv` 636→620, `_ZN7Storage11getChecksumEP14ResourceHeader` 20→16, `_ZN7Storage12readResourceEP14ResourceHeaderPvjj` 124→144, `_ZN7Storage17getResourceByNameEPKc` 208→192, `_ZN7Storage5eraseEm` 224→232, `_ZN7Storage6defragEPvjm` 1036→916, `_ZN7Storage10verifyDataEP8ResourcePvj` 120→116, `_ZN7Storage13writeResourceEP14ResourceHeader` 764→740, `_ZN7Storage11getFreeSizeEm` 76→68, `_GLOBAL__sub_I_storage` 40→36, `memmove` 52→50, `ceilf` 140→144, `__udivmoddi4` 700→800

| Symbol | Referenz | neu | Δ Größe |
|---|---|---|---|
| `DMA1_Stream0_IRQHandler` | `000032a0` (12) | `000032a0` (12) |  |
| `DMA1_Stream1_IRQHandler` | `000032ac` (12) | `000032ac` (12) |  |
| `HAL_DMA_IRQHandler` | `000032b8` (1704) | `000032b8` (1726) | +22 |
| `SAI_DMATxHalfCplt` | `000039bc` (10) | `000039d8` (10) |  |
| `SAI_DMATxCplt` | `00003960` (92) | `00003978` (96) | +4 |
| `SAI_DMARxHalfCplt` | `00003a24` (10) | `00003a44` (10) |  |
| `SAI_DMARxCplt` | `000039c8` (92) | `000039e4` (96) | +4 |
| `HAL_SAI_RxHalfCpltCallback` | `00003a30` (24) | `00003a50` (24) |  |
| `HAL_SAI_RxCpltCallback` | `00003a48` (32) | `00003a68` (32) |  |
| `HAL_SAI_TxHalfCpltCallback` | `00003a68` (2) | `00003a88` (2) |  |
| `HAL_SAI_TxCpltCallback` | `00003a6c` (2) | `00003a8c` (2) |  |
| `audioCallback` | `00003a70` (148) | `00003a90` (152) | +4 |
| `vTaskNotifyGiveFromISR` | `00003b04` (212) | `00003b28` (224) | +12 |
| `vPortValidateInterruptPriority` | `00003bd8` (92) | `00003c08` (92) |  |
| `PendSV_Handler` | `00003ca0` (100) | `00003cd0` (100) |  |
| `vTaskSwitchContext` | `00003e18` (164) | `00003e48` (184) | +20 |
| `ulTaskNotifyTake` | `00003ebc` (104) | `00003f00` (112) | +8 |
| `prvAddCurrentTaskToDelayedList` | `00003d04` (140) | `00003d34` (140) |  |
| `vPortEnterCritical` | `00003c34` (68) | `00003c64` (68) |  |
| `vPortExitCritical` | `00003c78` (40) | `00003ca8` (40) |  |
| `uxListRemove` | `00003f70` (40) | `00003fc4` (36) | -4 |
| `vListInsertEnd` | `00003f24` (28) | `00003f70` (26) | -2 |
| `vListInsert` | `00003f40` (48) | `00003f8c` (54) | +6 |
| `prvIdleTask` | `00003d90` (136) | `00003dc0` (136) |  |
| `onProgramReady` | `000040d4` (248) | `000040fc` (208) | -40 |
| `_Z15usbd_tx_convertPlj` | `00004054` (128) | `00004088` (116) | -12 |
| `_Z15usbd_rx_convertPlj` | `00003f98` (188) | `00003fe8` (160) | -28 |
| `updateParameters` | `000041d8` (54) | `000041d8` (54) |  |
| `_ZN10MidiWriter8transmitEv` | `00004210` (124) | `00004210` (132) | +8 |
| `_ZN12MidiReceiver7receiveEv` | `0000428c` (104) | `00004294` (112) | +8 |
| `usbd_midi_ready` | `0000432c` (36) | `00004340` (36) |  |
| `usbd_midi_tx` | `000042f4` (56) | `00004304` (60) | +4 |
| `getProgramVector` | `000041cc` (12) | `000041cc` (12) |  |
| `OTG_FS_IRQHandler` | `00004350` (12) | `00004364` (12) |  |
| `HAL_PCD_IRQHandler` | `0000435c` (1624) | `00004370` (1720) | +96 |
| `USB_ReadInterrupts` | `00004d84` (8) | `00004dfc` (8) |  |
| `USB_ReadDevAllOutEpInterrupt` | `00004d8c` (14) | `00004e04` (14) |  |
| `USB_ReadDevAllInEpInterrupt` | `00004d9c` (14) | `00004e14` (14) |  |
| `USB_ReadDevOutEPInterrupt` | `00004dac` (18) | `00004e24` (16) | -2 |
| `USB_ReadDevInEPInterrupt` | `00004dc0` (32) | `00004e34` (32) |  |
| `USB_GetMode` | `00004de0` (8) | `00004e54` (8) |  |
| `USB_ReadPacket` | `00004d3c` (72) | `00004dac` (78) | +6 |
| `USB_WritePacket` | `00004d10` (42) | `00004d84` (40) | -2 |
| `USB_EPStartXfer` | `00004aec` (548) | `00004b70` (532) | -16 |
| `HAL_PCD_SOFCallback` | `00004e10` (8) | `00004e88` (8) |  |
| `USBD_LL_SOF` | `00004f98` (36) | `00005028` (36) |  |
| `_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef` | `0000560c` (64) | `000056d0` (64) |  |
| `usbd_audio_sof_callback` | `000054e4` (296) | `0000559c` (308) | +12 |
| `usbd_audio_get_rx_count` | `0000564c` (40) | `00005710` (40) |  |
| `HAL_PCD_DataOutStageCallback` | `00004de8` (20) | `00004e5c` (22) | +2 |
| `USBD_LL_DataOutStage` | `00004e78` (104) | `00004ef0` (110) | +6 |
| `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh` | `000050c8` (572) | `0000515c` (588) | +16 |
| `USBD_LL_GetRxDataSize` | `00004e70` (8) | `00004ee8` (8) |  |
| `HAL_PCD_EP_GetRxCount` | `00004a04` (18) | `00004a80` (18) |  |
| `USBD_LL_PrepareReceive` | `00004e58` (22) | `00004ed0` (22) |  |
| `HAL_PCD_EP_Receive` | `000049b4` (78) | `00004a28` (88) | +10 |
| `HAL_PCD_DataInStageCallback` | `00004dfc` (18) | `00004e74` (20) | +2 |
| `USBD_LL_DataInStage` | `00004ee0` (182) | `00004f60` (198) | +16 |
| `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh` | `00005304` (480) | `000053a8` (500) | +20 |
| `USBD_LL_Transmit` | `00004e40` (22) | `00004eb8` (22) |  |
| `HAL_PCD_EP_Transmit` | `00004a18` (78) | `00004a94` (80) | +2 |
| `_ZN5Codec16getSampleCounterEv` | `00005674` (32) | `00005738` (32) |  |
| `codec_ndtr` | `00005694` (20) | `00005758` (200) | +180 |
| `HAL_PCD_ISOINIncompleteCallback` | `00004e20` (8) | `00004e98` (8) |  |
| `USBD_LL_IsoINIncomplete` | `00004fbc` (36) | `0000504c` (36) |  |
| `_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh` | `00005008` (192) | `00005098` (196) | +4 |
| `USBD_LL_FlushEP` | `00004e28` (22) | `00004ea0` (22) |  |
| `HAL_PCD_EP_Flush` | `00004a68` (62) | `00004ae4` (72) | +10 |
| `USB_FlushTxFifo` | `00004aa8` (36) | `00004b2c` (36) |  |
| `USB_FlushRxFifo` | `00004acc` (32) | `00004b50` (32) |  |
| `HAL_PCD_ISOOUTIncompleteCallback` | `00004e18` (8) | `00004e90` (8) |  |
| `USBD_LL_IsoOUTIncomplete` | `00004fe0` (36) | `00005070` (36) |  |
| `_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh` | `00005004` (4) | `00005094` (4) |  |
| `SysTick_Handler` | `000056a8` (24) | `00005820` (24) |  |
| `HAL_IncTick` | `000056c0` (24) | `00005838` (24) |  |
| `HAL_GetTick` | `000056d8` (12) | `00005850` (12) |  |
| `xTaskGetSchedulerState` | `00005808` (32) | `0000597c` (32) |  |
| `xPortSysTickHandler` | `00005828` (44) | `0000599c` (44) |  |
| `xTaskIncrementTick` | `000057e4` (36) | `00005958` (36) |  |
| `xTaskIncrementTick.part.0` | `000056e4` (256) | `0000585c` (252) | -4 |
| `DMA1_Stream3_IRQHandler` | `00005854` (12) | `000059c8` (12) |  |
| `ADC_DMAConvCplt` | `00005874` (108) | `000059e8` (108) |  |
| `ADC_DMAHalfConvCplt` | `00005868` (10) | `000059dc` (10) |  |
| `HAL_ADC_ConvCpltCallback` | `00005860` (2) | `000059d4` (2) |  |
| `HAL_ADC_ConvHalfCpltCallback` | `00005864` (2) | `000059d8` (2) |  |
| `_ZL20acdcMeasureRawInputsv` | `000058e0` (372) | `00005a54` (392) | +20 |
| `_ZL14acdcOnLoopLatev` | `00005a54` (484) | `00005bdc` (552) | +68 |
| `_ZL14acdcOnLoopDarkh` | `00005de8` (292) | `00005fc0` (264) | -28 |
| `setLed` | `00005cd8` (204) | `00005ea4` (216) | +12 |
| `setLed.constprop.0` | `00005c38` (160) | `00005e04` (160) |  |
| `getParameterValue` | `00005da4` (20) | `00005f7c` (20) |  |
| `setParameterValue` | `00005db8` (16) | `00005f90` (16) |  |
| `StartDefaultTask` | `00005dc8` (12) | `00005fa0` (12) |  |
| `loop` | `00005dd4` (20) | `00005fac` (20) |  |
| `onLoop` | `00005f0c` (24) | `000060c8` (24) |  |
| `_ZN3Owl4loopEv` | `00005fb8` (76) | `00006174` (76) |  |
| `_ZN14ProgramManager16isProgramRunningEv` | `00006004` (16) | `000061c0` (16) |  |
| `device_watchdog` | `00006014` (16) | `000061d0` (16) |  |
| `vTaskDelayUntil` | `00006148` (176) | `00006300` (180) | +4 |
| `vTaskSuspendAll` | `000061f8` (16) | `000063b4` (16) |  |
| `xTaskResumeAll` | `00006208` (32) | `000063c4` (32) |  |
| `xTaskResumeAll.part.0` | `00006024` (292) | `000061e0` (288) | -4 |
| `memset` | `00006230` (16) | `000063ec` (16) |  |
| `memcpy` | `00006240` (28) | `000063fc` (28) |  |
| `abs` | `00006228` (8) | `000063e4` (8) |  |
| `onLoop` | `00005f0c` (24) | `000060c8` (24) |  |
| `main` | `08003f70` (2556) | `08004100` (2556) |  |
| `SystemInit` | `0800540c` (240) | `080055e4` (240) |  |
| `Reset_Handler` | `08003330` (128) | `080034f0` (128) |  |
| `_ZN11MidiHandler11handleSysExEPht` | `08014d60` (1252) | `080155ec` (1256) | +4 |

- Datenobjekte im RAM (.data/.bss/…) gemeinsam 181, gleiche RAM-Adresse 181

**Ergebnis:** BESTANDEN (0 FAIL, 0 WARN)
