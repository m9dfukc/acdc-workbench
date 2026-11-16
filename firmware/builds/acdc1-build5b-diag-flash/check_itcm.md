# check_itcm: acdc1-build5b-diag-flash

ELF `firmware/builds/acdc1-build5b-diag-flash/ACDC.elf`, Binary `firmware/builds/acdc1-build5b-diag-flash/ACDC.bin`

Gruppen im ITCM: **A B C E F G H L**; im Flash (Variante): D USB

## 1 Sections, Symbole, Größe

- **ok** Linker-Symbole vorhanden 
- **ok** Sections .itcm_vectors und .itcm_text vorhanden
- **ok** ITCM-Block liegt im CCMRAM 0x1000–0xFFFF
- **ok** .ccmdata (PROGRAMSTACK 0x1000–0x3000) liegt vor dem ITCM-Block
- **ok** _CCMRAM (Patch-Heap) = _eitcm_text = 0x5550
- **ok** Vektorkopie 0x3000 auf 1 KB ausgerichtet
- **ok** Platz für die Vektortabelle (664 B)
- **ok** _sitcm_text = 0x32a0 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_text = 0x5550 8-Byte-ausgerichtet (ECC)
- **ok** _litcm_text = 0x8000298 8-Byte-ausgerichtet (ECC)
- **ok** _sitcm_vect = 0x3000 8-Byte-ausgerichtet (ECC)
- **ok** _eitcm_vect = 0x3298 8-Byte-ausgerichtet (ECC)
- **ok** .itcm_text VMA 0x32a0, Größe 8880 B = _eitcm_text − _sitcm_text (Veneers inklusive)
- **ok** .itcm_text LMA 0x8000298 = _litcm_text
- **ok** LMA liegt im Flash
- **ok** ACDC.bin 108928 B <= 131072 B (frei 22144 B)
- **ok** Kopierquelle im Binary = Inhalt von .itcm_text im ELF

ITCM-Belegung: Vektorkopie 664 B @ 0x3000, Code 8880 B @ 0x32a0–0x5550 (zusammen 9552 B ab 0x3000). Patch-Heap im CCM: 43696 B (42.7 KB, vorher 53248 B).

## 2 Vektortabelle

- **ok** Vektor 14 → 0x00003ca1 PendSV_Handler (erwartet PendSV_Handler im ITCM)
- **ok** Vektor 15 → 0x00004321 SysTick_Handler (erwartet SysTick_Handler im ITCM)
- **ok** Vektor 27 → 0x000032a1 DMA1_Stream0_IRQHandler (erwartet DMA1_Stream0_IRQHandler im ITCM)
- **ok** Vektor 28 → 0x000032ad DMA1_Stream1_IRQHandler (erwartet DMA1_Stream1_IRQHandler im ITCM)
- **ok** Vektor 30 → 0x000044cd DMA1_Stream3_IRQHandler (erwartet DMA1_Stream3_IRQHandler im ITCM)
- **ok** Vektor 117 → 0x080026f1 OTG_FS_IRQHandler (erwartet OTG_FS_IRQHandler im Flash, Gruppe D nicht gewählt)
- **ok** Vektor 0 (MSP) = 0x1000 = _estack (FreeRTOS liest ihn über VTOR)

## 3 Heiße Funktionen im ITCM

- **ok** 64 von 64 heißen Funktionen der gewählten Gruppen im ITCM, zusammen 6700 B
- **ok** 40 von 40 Funktionen der nicht gewählten Gruppen (D) im Flash, zusammen 5134 B
- Funktionen im ITCM insgesamt: 69; `acdc_onloop_pad`: Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)
- **WARN** keine unerwarteten Funktionen im ITCM: _ZL11acdcDiagPutPcS_PKcm.constprop.0, _ZL11acdcDiagPutPcS_PKcm.constprop.1, _ZL12acdcDiagPutSPcS_PKcl.constprop.0, _ZL17acdcUsbDiagReportm

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

12 Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):

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
- `[.text+0x90c]` ← `_Z15usbd_rx_convertPlj`
- `[.text+0x914]` ← `_Z15usbd_tx_convertPlj`

## 5b Anker im Flash (Voraussetzung für die Füllvariante)

- **WARN** 36 Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker 0x08002550–0x08002e6b (2331 B); außerhalb: [.rodata+0x9f4], [.rodata+0x9f8], [.rodata+0x9fc], [.rodata+0xa00], [.rodata+0xa04], [.rodata+0xa08], [.rodata+0xa0c], [.rodata+0xa10], [.rodata+0xa14], [.rodata+0xe88] (Variante: Anker nur für Füllvarianten nötig, deshalb nur Warnung)

## 6 Funktionszeiger USBD_AUDIO

- USBD_AUDIO.Init → _ZL15USBD_AUDIO_InitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.DeInit → _ZL17USBD_AUDIO_DeInitP19_USBD_HandleTypeDefh (Flash, kalt)
- USBD_AUDIO.Setup → _ZL16USBD_AUDIO_SetupP19_USBD_HandleTypeDefP13usb_setup_req (Flash, kalt)
- USBD_AUDIO.EP0_TxReady → _ZL22USBD_AUDIO_EP0_TxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- USBD_AUDIO.EP0_RxReady → _ZL22USBD_AUDIO_EP0_RxReadyP19_USBD_HandleTypeDef (Flash, kalt)
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x800b0dd) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x800b249) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x800b651) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x800b009) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x800ab51) im Flash (Gruppe D nicht gewählt)

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

**Ergebnis:** BESTANDEN (0 FAIL, 2 WARN)
