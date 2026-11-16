# check_itcm: acdc1-build4yp-fx3jp

ELF `firmware/builds/acdc1-build4yp-fx3jp/ACDC.elf`, Binary `firmware/builds/acdc1-build4yp-fx3jp/ACDC.bin`

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
- **ok** ACDC.bin 107512 B <= 131072 B (frei 23560 B)
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
- **ok** USBD_AUDIO.DataIn → _ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh (0x800ae81) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.DataOut → _ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh (0x800ac45) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.SOF → _ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef (0x800b189) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoINIncomplete → _ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh (0x800ab85) im Flash (Gruppe D nicht gewählt)
- **ok** USBD_AUDIO.IsoOUTIncomplete → _ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh (0x800a6d9) im Flash (Gruppe D nicht gewählt)

## 7 Nichts im ITCM vor dem Kopieren

- **ok** SystemInit und Aufgerufene (SystemInit) springen nicht ins ITCM
- Reset_Handler ruft der Reihe nach: `SystemInit`, `__libc_init_array`, `main`
- **ok** Reset_Handler: SystemInit → (Kopien, VTOR) → __libc_init_array → main
- **ok** Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)

## 9 ITCM-Inhalt gegen acdc1-build4y-fx3j

- **ok** gleiche ITCM-Grenzen 0x32a0–0x4f20
- **ok** .itcm_text bytegleich (7296 B)
- **ok** Vektortabelle (wird ins ITCM kopiert) bytegleich
- Flash-Funktionen gemeinsam 687, Verschiebung dieser Build − acdc1-build4y-fx3j: +0x150: 514, +0x0: 173
- Datenobjekte im RAM gemeinsam 178, gleiche Adresse 178

**Ergebnis:** BESTANDEN (0 FAIL, 0 WARN)
