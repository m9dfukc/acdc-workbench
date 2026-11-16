# check_itcm: acdc1-build5b-diag-itcm

ELF `firmware/builds/acdc1-build5b-diag-itcm/ACDC.elf`, Binary `firmware/builds/acdc1-build5b-diag-itcm/ACDC.bin`

Gruppen im ITCM: **A B C D E F G H L** (alle)

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x6a10
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x6a10 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 14192 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 109104 B <= 131072 B (frei 21968 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 14192 B @ 0x32a0–0x6a10 (zusammen 14864 B ab 0x3000). Patch-Heap im CCM: 38384 B (37.5 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ca1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x00005749 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x000058f5 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x00004321 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 104 von 104 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 11834 B
- Funktionen im ITCM insgesamt: 109; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
- **WARN** keine unerwarteten Funktionen im ITCM: _ZL11acdcDiagPutPcS_PKcm.constprop.0, _ZL11acdcDiagPutPcS_PKcm.constprop.1, _ZL12acdcDiagPutSPcS_PKcl.constprop.0, _ZL17acdcUsbDiagReportm

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

14 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

- `[.rodata+0x9f4]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0x9f8]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0x9fc]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa00]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa04]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa08]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa0c]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa10]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xa14]` ← `_ZL17acdcUsbDiagReportm`
- `[.rodata+0xe88]` ← `_ZL12acdcDiagPutSPcS_PKcl.constprop.0`
- `[.text+0x8d4]` ← `_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh`
- `[.text+0x8dc]` ← `_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh`
- `[.text+0x8e4]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x8ec]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **FAIL** 56 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08003a10–0x08004303 (2291 B); außerhalb: [.rodata+0x9f4], [.rodata+0x9f8], [.rodata+0x9fc], [.rodata+0xa00], [.rodata+0xa04], [.rodata+0xa08], [.rodata+0xa0c], [.rodata+0xa10], [.rodata+0xa14], [.rodata+0xe88]

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x50b9) im ITCM
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x5225) im ITCM
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x562d) im ITCM
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x4fe5) im ITCM
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x4fd5) im ITCM

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

**Ergebnis:** NICHT BESTANDEN (1 FAIL, 1 WARN)
