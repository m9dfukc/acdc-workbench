# check_itcm: acdc1-build4p-fx3ip

ELF `firmware/builds/acdc1-build4p-fx3ip/ACDC.elf`, Binary `firmware/builds/acdc1-build4p-fx3ip/ACDC.bin`

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x62c8
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x62c8 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 12328 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 107640 B <= 131072 B (frei 23432 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 12328 B @ 0x32a0–0x62c8 (zusammen 13000 B ab 0x3000). Patch-Heap im CCM: 40248 B (39.3 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ca1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x0000565d SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x00005809 DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x00004321 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im ITCM)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 104 von 104 heißen Funktionen im ITCM, zusammen 11606 B
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

- Veneers Flash → ITCM: 27 (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. `setLed.constprop.0`, `USBD_LL_Transmit`, `getProgramVector`, `memcpy`, `setLed`, `xTaskResumeAll.part.0`, `getParameterValue`, `vPortExitCritical` …)
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

- **ok** 50 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x080032c0–0x08003c1b (2395 B)

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

**Ergebnis:** BESTANDEN (0 FAIL, 0 WARN)
