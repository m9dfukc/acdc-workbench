# Daisy (libDaisy) and Teensy 4 vs. our ITCM plan: code placement, caches, ECC, veneers, noise (2026-11-16)

Follow-up to `layout_noise_2026-11-16.md` (D33/D34). That note already covers the Daisy callback tone (t/432 #10 shensley, t/6028 #7 passtheducky), the PJRC 344 Hz thread, ST DS12556/AN2834 and Mytkowicz 2009. Those are not repeated here.

Our plan under review (agreed): put everything that runs periodically in a custom section `.itcm_text` (`>CCMRAM AT>FLASH`, VMA from 0x3000 in ITCM, copy loop in `Reset_Handler`), ≈ 10 KB. That covers the SAI DMA ISR + `HAL_DMA_IRQHandler`, the FreeRTOS scheduler (incl. idle/PendSV), the audio task, the USB OTG ISR/`HAL_PCD_IRQHandler`/USB audio class, SysTick and the ADC DMA. Also move the vector table (VTOR) into ITCM.

Sources read:
- **libDaisy** `daisyaudio/libDaisy` (the repo was renamed from `electro-smith/libDaisy`), shallow clone of `master` @ `1289a000bc29dae1bc0ed4129cfa2df40ef71574` (2026-11-03).
- **DaisySP** @ `2c72eaf9eac5fc0dca1919d65d606da907832618`.
- **DaisyExamples** @ `728e93d2fa213df4e2b74160fa02f0f146fede87`.
- **Teensy cores** `PaulStoffregen/cores` `master` @ `27adf000f85619481a47233bb977b64ac41f71d8` (2026-11-03).
- **Forum** community.daisy.audio (formerly forum.electro-smith.com), via its Discourse JSON API.
- **ST AN5342 Rev 2**: the copy that was read was the mirror at kolegite.com, because st.com blocks automated downloads.

## Short answer

1. **libDaisy does not use ITCM at all.** `ITCMRAM` (64 KB at 0x0) is declared in all three linker scripts, but no section is placed there. The startup copies only `.data` and zeroes `.bss`. There are no ITCM, ramfunc or `long_call` attributes or macros in libDaisy, DaisySP or DaisyExamples. The vector table stays where the image is (internal flash, AXI SRAM or QSPI). [belegt]
2. **Electrosmith's official remedy for the block-rate tone** is a smaller block size (tone above 20 kHz) plus **extra CPU work outside the callback** ("calculate trig functions … anything the compiler won't optimize away"), i.e. flattening the current draw, plus hardware layout. Code placement, ITCM, cache and boot mode are not mentioned. [belegt]
3. **No evidence that ITCM, code placement or boot mode changes block-rate tones or noise**, on Daisy, Teensy 4 or any STM32H7 audio project found. The strongest related evidence:
   - A Daisy user with **48 kHz / block 8 has the exact 6 kHz line we have**. It is present even in passthrough and grows with DSP/ADC work.
   - Community DWT benchmarks show that moving code into ITCM **changes the timing of *other*, untouched code**, by up to −70 % and +126 %, because it changes I-cache pressure.

   Both point to *timing/current profile* as the lever. That ITCM reduces the lines remains our [Hypothese], to be measured.
4. **Teensy 4 is the counter-model:** *all* code runs from ITCM by default (`.text*` → ITCM AT> FLASH), the vector table is in DTCM RAM, ITCM is made read-only by the MPU after the copy, and the first 32 B of ITCM are a NULL trap. [belegt]
5. **Corrections or additions to our plan** (details in §5):
   - (a) In OpenWare, **0x3000 is the start of the patch heap** (`_CCMRAM`), and it is zero-filled at every patch start. `.itcm_text` must therefore come before `PROVIDE(_CCMRAM)`. [Code]
   - (b) ITCM has **64-bit ECC**. Align the copy start and end to 8 B. [belegt]
   - (c) Calls between ITCM and flash need linker **veneers**. GNU ld generates them automatically, so `-mlong-calls` is not needed. Every call *out of* ITCM costs a veneer plus a flash fetch, so audit them. [belegt]/[Hypothese]
   - (d) The vector table needs 1 KB alignment. [Hypothese, ARM rule, see §5]
   - (e) Nothing in ITCM may run before the copy, e.g. `SystemInit`. [belegt]

---

## 1. What libDaisy does (Q1)

### 1a. Linker scripts [belegt]

`core/STM32H750IB_flash.lds` (APP_TYPE `BOOT_NONE`, the default):
- MEMORY (L8–19):
  - `FLASH 0x08000000 128K`
  - `DTCMRAM 0x20000000 128K`
  - `SRAM 0x24000000 512K`
  - `RAM_D2 0x30000000 288K`
  - `RAM_D3`, `BACKUP_SRAM`
  - **`ITCMRAM 0x00000000 64K`**
  - `SDRAM 0xC0000000 64M`
  - `QSPIFLASH 0x90000000 8M`
- `_estack = 0x20020000` (L21): **main stack at the top of DTCM**.
- `.isr_vector` → FLASH (L25–30). `.text`/`.rodata` → FLASH (L32–48).
- `.data` → `SRAM AT>FLASH` (L92–104). `.bss` → SRAM (L108–121).
- `.dtcmram_bss` → DTCMRAM (L125–137). `.sram1_bss` → RAM_D2 (L139–151).
- `.sdram_text` (AT>FLASH) exists only **commented out** (L153–168).
- `.sdram_bss`, `.backup_sram`, `.qspiflash_*`, heap → SRAM.
- **No section goes into ITCMRAM.**

`core/STM32H750IB_sram.lds` (`BOOT_SRAM`), diff against the flash script:
- `.isr_vector`, `.text`, `.rodata`, `.init/.fini_array` → **SRAM** (AXI SRAM 0x24000000, 480 KB usable).
- `.data` → `DTCMRAM AT> SRAM`, `.bss` → DTCMRAM, stack reserve → DTCMRAM, heap → RAM_D2.
- `RAM_D2_DMA` = first 32 KB of D2 for `.sram1_bss`.

`core/STM32H750IB_qspi.lds` (`BOOT_QSPI`):
- `.isr_vector`/`.text` → **QSPIFLASH at 0x90040000** (execute in place).
- `.data` → `SRAM AT> QSPIFLASH`, `.bss` → SRAM.

Repo-wide grep (`itcm|ramfunc|fastrun|long-calls|long_call`, without `Drivers/`):
- The only hits are the three `ITCMRAM` MEMORY lines.
- `src/sys/system.cpp:47/596` uses `ITCMRAM_SIZE` only to classify `SCB->VTOR` in `GetMemoryRegion()`.
- The bootloader doc lists "ITCMRAM: 0 GB 64 KB 0.00%" in its example memory reports (`doc/md/_a7_Getting-Started-Daisy-Bootloader.md` L32/L49).

### 1b. Section macros [belegt]

- `src/daisy_core.h:25` `DMA_BUFFER_MEM_SECTION` → `.sram1_bss` (D2 at 0x30000000).
- `src/daisy_core.h:31` `DTCM_MEM_SECTION` → `.dtcmram_bss`.
- `src/dev/sdram.h:74/81` `DSY_SDRAM_DATA`/`DSY_SDRAM_BSS`.
- `src/per/qspi.h:11–17` QSPI sections.
- There is **no macro for code**: no `DSY_ITCM` and no RAMFUNC.
- The audio DMA buffers are `DMA_BUFFER_MEM_SECTION` (`src/hid/audio.cpp:20/22`).
- The audio callback runs **inside the DMA ISR**: `DMA1_Stream0/1_IRQHandler` (`src/per/sai.cpp:507/512`) → `SaiHandle::Impl::InternalCallback` → `AudioHandle::Impl::InternalCallback` (`src/hid/audio.cpp:275`). libDaisy uses no RTOS.

### 1c. Startup and vector table [belegt]

- `core/Makefile:53` uses `startup_stm32h750xx.c` (the `.s` is commented out, L60).
- `Reset_Handler` (`core/startup_stm32h750xx.c` ≈ L1535–1557):
  1. copies `.data`, zeroes `.bss`
  2. calls `SystemInit()` only `#ifndef BOOT_APP`
  3. calls `__libc_init_array()`, then `main()`

  No other copy loop.
- `SystemInit` (`src/sys/system_stm32h7xx.c:238–245`) sets `SCB->VTOR = FLASH_BANK1_BASE | VECT_TAB_OFFSET`. So for `BOOT_NONE` the vector table stays **in flash at 0x08000000**.
- For bootloader apps, `SystemInit` is skipped. The vector table is then at the start of the image in SRAM or QSPI. VTOR is set by the jump: `__JUMPTOQSPI()` writes VTOR = 0x90000000, SP, PC (`src/sys/system.cpp:70–78`).
- Community confirmation: tessera PR #673 says "libDaisy's startup only copies `.data` and zeroes `.bss`", so they fill ITCM/DTCM themselves in `main.cpp`. https://github.com/Rastapopolix/tessera/pull/673

### 1d. Cache, MPU, clock, flash latency [belegt]

- `System::Config::Defaults()` (`src/sys/system.h:35–40`): **400 MHz**, `use_dcache = use_icache = true`. `Boost()` (L47–50): 480 MHz.
- `System::Init` (`src/sys/system.cpp:216–246`): `HAL_Init` → `ConfigureClocks` → `ConfigureMpu` → DMA/I2C/SPI/UART init → `SCB_EnableDCache()` → `SCB_EnableICache()` → TIM2 → RNG.
- `ConfigureClocks` (≈ L400–412):

  | Clock | Voltage scale | PLLN | Flash latency |
  |---|---|---|---|
  | 480 MHz | VOS0 | 240 | `FLASH_LATENCY_4` |
  | 400 MHz (default) | VOS1 | 200 | `FLASH_LATENCY_2` |

  PLLM 4, PLLP 2, PLLQ 5.
- `ConfigureMpu` (L521–558), three regions; everything else uses the default memory map:

  | Region | Base | Size | Attributes |
  |---|---|---|---|
  | 0 | 0x30000000 | 32 KB | not cacheable, not bufferable, shareable, TEX1 (DMA buffers) |
  | 1 | 0xC0000000 | 64 MB | SDRAM, cacheable + bufferable |
  | 2 | 0x38800000 | 4 KB | backup SRAM, not cacheable |

- So the Daisy pattern is "**DMA buffers in a non-cacheable D2 window, everything else cached**". This is the same idea as OpenWare `Source/mpu.c` (region `_DMA_DATA`, 64 KB D2, `NOT_CACHEABLE`, `BUFFERABLE`). [Code]
- Discussion of non-cacheable vs. cache maintenance: libDaisy issue #335, https://github.com/daisyaudio/libDaisy/issues/335. Latest commit `1289a000` "align a few data members to avoid bugs due to cache maintenance" (#727).
- Compiler: `OPT ?= -O2` (`core/Makefile:29`), `-ffunction-sections -fdata-sections`, `--gc-sections` (L185, L269). No `-mlong-calls`.

**Comparison with OpenWare/ACDC [Code]:** 480 MHz, VOS0, `FLASH_LATENCY_4`, I+D cache, `-O3` (`Hardware/xibeca.mk:6`), `-ffunction-sections` (L26), `--gc-sections` (L22), no LTO. The main stack is in ITCM 0x0–0x1000 (`_estack = 0x1000`). Daisy at its default 400 MHz runs flash with **2** wait states instead of 4. With the I-cache on, that matters only on misses.

## 2. Boot modes BOOT_SRAM / BOOT_QSPI (Q2)

- **BOOT_SRAM: the whole program (vectors, `.text`, `.rodata`) runs from AXI SRAM** 0x24000000. The Daisy bootloader in internal flash loads it there; images are stored in QSPI at 0x90040000. **BOOT_QSPI runs the whole program XIP from QSPI.** [belegt: linker scripts above; `doc/md/_a7_Getting-Started-Daisy-Bootloader.md` L8, L22, L74–84]
- Electrosmith's stated speed claims: "Execution from SRAM has comparable speed to the internal flash, while the QSPI flash is naturally a fair bit slower" (L8). [belegt]
- **No report found that noise or tones change with boot mode or code location**:
  - Forum search via `community.daisy.audio/search.json`: `BOOT_SRAM noise`, `QSPI noise`, `ITCM`, `itcm_text`, `ramfunc`, `DTCM performance`, `noise code`, `noise cpu`, `callback noise`, `blocksize noise`.
  - GitHub issue search `repo:daisyaudio/libDaisy`: `noise`, `cache`, `linker`, `ITCM` → 0 ITCM hits.
  - The QSPI threads concern data corruption (t/4323) or bootloader loading (t/8231, t/5799), not audio noise. [belegt, negative result]

## 3. Reports: ITCM / cache / code layout ↔ noise or timing (Q3)

### 3a. Daisy: block-rate tone, newer evidence not yet in `layout_noise`

- **Official Daisy docs, "Avoiding Callback Noise"**: https://docs.daisy.audio/tutorials/eliminating-callback-noise/
  - Callback noise is "a spurious tone that occurs at the block rate (sample rate divided by block size)". It "occurs when your application spends a long time in the audio callback. This can lead to a current transient when your code exits the callback which can affect GND on your PCB."
  - Remedies, from least to most effort:
    1. block size 2 → 24 kHz
    2. "**add additional CPU usage outside of your audio callback** … calculate trig functions (Sin()), or anything the compiler won't optimize away" (called "more complex, and less predictable")
    3. recommended circuits
    4. PCB layout
  - **No mention of ITCM, cache, code placement or boot mode.** [belegt]
  - → Vendor confirmation of the "flatten the current" lever, i.e. our idle-load test in `layout_noise` §4.2. [belegt]
- **t/9084 "Daisy Seed 6kHz oscillation noise in multi-effects pedal (Flick)"** (joulupukki, 2026-03-29…31): https://community.daisy.audio/t/9084
  - 48 kHz, **block 8 → line at 6 kHz**, i.e. **identical to our fs/8**.
  - #3/#4: it moves with block size (block 4 → 12 kHz).
  - #5: "the 6kHz spike is there [in passthrough], it's just not as much as when I start processing controls and using the ADC". The notch in code does not catch it ("getting added after the DAC").
  - #6/#8: fixed with 96 kHz / block 4 or 6 (16–24 kHz).
  - #9: "optimize for speed" and less work in the callback made 96 kHz / block 4 viable.
  - → The amplitude depends on the amount and time profile of the work per block. No ITCM test. [belegt]
- **t/1854 "Daisy performance"** #2/#7 (TheSlowGrowth, 2021): https://community.daisy.audio/t/1854. The whine is "short bursts of processing for each block … current spikes and noise on the power rails". Remedies: "make the power consumption more continuous" (smaller blocks) and better power delivery. [belegt]
- **t/3370 "Daisy boot loader and ITCMRAM"**: https://community.daisy.audio/t/3370
  - The only Electrosmith-forum thread on ITCM code.
  - Motivation is performance and determinism (#3, #11 gregsbrain: "it is also not cached so there are no cache misses, which means access times are deterministic").
  - antisvin (#4, OpenWare/OWLsy developer): "It won't always be substantially faster, because any CPU intensive code will normally run from the MCU cache."
  - Corvus_Prudens (#9, Electrosmith): "We don't have it set up to make that easy."
  - **No noise measurement.** [belegt]
- t/6028 #4/#5 (ITCM proposed for callbacks, rejected because "I-cache large enough", not measured) is already in `layout_noise` §2b.

### 3b. ITCM changes the timing of other code (community DWT measurements, not peer-reviewed)

- **zbuc/ambient_viz PR #1** (Daisy, Rust, 2026-06-09): https://github.com/zbuc/ambient_viz/pull/1
  - "ITCM scaffolding: `itcm.x` section + `pre_init` copy …"
  - "Measured double-benefit (tape −6.4%, untouched voice −12% / limiter −70% from cache relief; sd +126% → **placement is non-monotonic**)".
  - QSPI XIP costs +26 % ("I-cache contention").
  - → Moving one part into ITCM changes the I-cache occupancy and thus the timing of *other* code, in both directions. That is exactly the D33 mechanism (layout → timing → current profile). [belegt, single source]
- **VZtec/daisyConvol PR #1** (2026-11-08): https://github.com/VZtec/daisyConvol/pull/1
  - cabsim CPU ~11 % → ~9 % with `ITCM=1`.
  - Makefile comment (`examples/cabsim/Makefile` L19–23): "the engine and the CMSIS FFT run from the ITCM (64 KB, zero wait states) instead of from QSPI through the 16 KB I-cache …; **code layout then does not change their cost**." [belegt]
- **Brainscape PR #4** (Daisy Seed Rev7, 2026-10-07): https://github.com/zchdvs/Brainscape/pull/4. Engine code copied into ITCM (40–44 KB), with checks in CI (see §5). [belegt]

### 3c. Teensy 4 (i.MX RT1062, Cortex-M7)

- **All code in ITCM by default** [belegt]:
  - `teensy4/imxrt1062.ld` L41–46: `.text.itcm : { . = . + 32; /* MPU to trap NULL pointer deref */ *(.fastrun) *(.text*) } > ITCM AT> FLASH`.
  - Only `.flashmem` (`FLASHMEM`) and `.progmem` stay in flash (L22–39).
  - `.rodata` and `.data` → **DTCM** AT> FLASH (L54–59). `.bss` → DTCM. DMA buffers → OCRAM (`.dmabuffers`, L68–72).
  - PJRC: "By default, functions without any memory type defined are treated as FASTRUN … accessed by the Cortex-M7 ITCM bus, for the fastest possible performance". FLASHMEM: "a delay results while the Flash memory is read into the M7's cache … should be used on startup code and other functions where speed is not important." https://www.pjrc.com/store/teensy41.html (Memory section)
- **Startup** (`teensy4/startup.c`) [belegt]:
  - `ResetHandler2` is `section(".startup")`, i.e. in flash.
  - L108: `startup_early_hook(); // must be in FLASHMEM, as ITCM is not yet initialized!`
  - L127–129: `memory_copy(&_stext, &_stextload, &_etext)` (ITCM), then `.data`, then `.bss`.
  - Vector table: `_VectorsRam[]` with `aligned(1024), section(".vectorsram")` in DTCM (L54–55). It is filled at runtime, then `SCB_VTOR = (uint32_t)_VectorsRam` (L135–137).
  - **MPU** (`configure_cache`, L287ff):
    - region 0 = 4 GB NOACCESS background. The comment links ARM's note on speculative AXIM reads outside defined regions.
    - region 1 = ITCM `MEM_NOCACHE | READONLY` (code becomes read-only after the copy).
    - region 2 = first 32 B NOACCESS (NULL trap).
    - DTCM `NOEXEC`.
- **Noise**: the PJRC 344 Hz thread from `layout_noise` is from the **Teensy 3.x era** (2016, Cortex-M4, no ITCM). It says nothing about ITCM. For Teensy 4, **no thread found** linking FASTRUN, ITCM or FLASHMEM to tones or noise. WebSearch on forum.pjrc.com: `FASTRUN|ITCM|FLASHMEM` + noise/spur/block rate. [negative result]
- Implication [Hypothese]: Teensy 4 shows that "everything in ITCM" is a stable, long-used configuration. It does **not** show that it makes block-rate tones disappear. There is no comparative measurement.

### 3d. Verdict Q3

**Evidence that ITCM, cache or code location changes noise lines: none found.** Evidence for the mechanism chain:
- Code location changes timing and cache behaviour (§3b, AN4891, Mytkowicz).
- The work/current profile per block sets the block-rate tone (official Daisy docs, t/9084, t/1854, t/432).
- Evening out the current helps (official Daisy docs: extra load outside the callback; t/6028 #7 jitter).

D33 itself remains the only direct "layout → line level" measurement. [belegt as negative result; mechanism = Hypothese]

## 4. Hardware facts relevant to the plan (Q4, bus/wait states)

- RM0433 §2.1.2/§2.1.5/§2.4, via the mirror https://docs.dirba.io/rm0433-stm32h742-743-753-750/02-memory-and-bus-architecture/ [belegt]:
  - "The ITCM is accessed by Cortex-M7 at CPU clock speed, with zero wait states." 64-bit ITCM bus, 64 KB at 0x0.
  - "The MDMA controller can access the DTCM and ITCM through AHBS."
  - DTCM: "2x32-bit DTCM bus … It can also fetch instructions." 128 KB at 0x20000000.
  - Everything else (flash, AXI SRAM, D2/D3 SRAM, peripherals on AHB3/4, APB3/4) goes through the "64-bit AXIM bus … to the AXI bus matrix in the D1 domain".
  - **ECC:** "8 ECC bits are added per 64-bit word for AXI-SRAM and ITCM-RAM", 7 bits per 32-bit word elsewhere, SECDED. "When an incomplete word is written to an internal SRAM and a reset occurs, the last incomplete word is not really written."
  - Boot: an invalid boot address falls back to "Boot address 1: ITCM-RAM at 0x0000 0000".
- **AN5342 Rev 2** (January 2020), "Error correction code (ECC) management for internal memories protection on STM32H7 Series". Mirror: https://kolegite.com/EE_library/application_notes/MCU/STM32/STM32H7_ECC.pdf [belegt]:
  - §2.2: "The data width is 64-bit for AXI-SRAM and for ITCM-RAM." "the RAM ECC cannot be turned off."
  - "If a data smaller than word is written … the modification is done on read-modify-write basis. On an incomplete access, the ECC does not write the value immediately … it waits for the next write access."
  - §3.1.1: "all memories that are to be accessed by the code must be initialized. A read access or an unaligned write to uninitialized memories is likely to trigger the ECC error." Then clear the flags, then enable the interrupts.
  - The L1 cache has its own ECC. "The CPU cache is only involved in AXIM bus accesses", i.e. ITCM/DTCM are not cached.
- ST community: an H7A3 user saw a RAMECC error on an **ITCM** address that disappeared after the startup initialised all ITCM and DTCM. The root cause was never found. https://community.st.com/t5/stm32-mcus-products/stm32h7-sram-ecc-triggered-unexpectedly/td-p/803247 [belegt, single case]
- OpenWare ACDC: `HAL_RAMECC_MODULE_ENABLED` is commented out (`ACDC/Core/Inc/stm32h7xx_hal_conf.h:68`), and there is no RAMECC code in `ACDC/` or `Source/`. ECC events are therefore only flagged, not acted on. [Code]
- **GNU ld (ARM)** inserts far-call stubs automatically: "generate and insert small sequences of code into a linked ARM ELF executable whenever an attempt is made to perform a function call to a symbol that is too far away". `--stub-group-size` controls placement, default heuristic `N=+1`. https://sourceware.org/binutils/docs/ld/ARM.html [belegt]
  - ITCM (0x3000) ↔ flash (0x08000000) is ≈ 128 MB apart, beyond the ±16 MB of a Thumb-2 `BL`. [Hypothese: ARMv7-M encoding limit, not re-read]
  - Brainscape `firmware/cmake/ItcmCheck.cmake` (header comment): "A call from code in ITCM to code outside it (QSPI) goes through a linker veneer placed in ITCM beside the caller, so the image's ITCM veneers are exactly its calls out of ITCM." https://github.com/zchdvs/Brainscape/blob/main/firmware/cmake/ItcmCheck.cmake [belegt]

## 5. Patterns to adopt and pitfalls (Q4/Q5), mapped onto our plan

### 5a. OpenWare-specific constraints found while checking the plan [Code]

- **0x3000 is not free.** In Build 3d (`firmware/builds/acdc1-build3d-fx2/ACDC.elf`, `nm`):

  | Address | Symbol | Content |
  |---|---|---|
  | 0x0000–0x1000 | `_estack` = 0x1000 | ITCMRAM 4 KB, main stack |
  | 0x1000–0x3000 | `PROGRAMSTACK` | patch task stack, `.ccmdata` |
  | from 0x3000 | `_CCMRAM` = 0x3000, `_CCMRAM_SIZE` = 0xD000 | patch heap |

  - With `USE_CCM_RAM` (active, `Source/device.h:209`), `ProgramManager.cpp:413–416` hands `[_CCMRAM, _CCMRAM+_CCMRAM_SIZE)` to the patch as heap segment 0. L429–431 does `memset(…, 0, size)` **at every patch start**.
  - → `.itcm_text` must be placed in `Hardware/xibeca.ld` **before** `PROVIDE(_CCMRAM = .)` (L153), e.g. as its own output section between `.ccmdata` and the `PROVIDE`, or inside `.ccmdata`. Otherwise patch start overwrites the code.
  - The patch heap in CCM shrinks from 52 KB by the size of `.itcm_text` (≈ 10 KB → ≈ 42 KB). Check whether patches rely on it (the library patches allocate from several segments).
- **Vector table:**
  - `_ISR_VECTOR_SIZE` = 0x298 = 166 entries. The VTOR base must be aligned to the table size rounded up to a power of two: 256 × 4 = **1 KB**. [Hypothese: ARMv7-M rule, ARM page not readable here; Teensy uses `aligned(1024)` for exactly this]
  - 0x3000 meets this. If `.itcm_text` and vectors share a section, put the vectors first, at an `ALIGN(1024)` address.
  - Copy option: the table stays in flash as the reset image (`.isr_vector` at 0x08000000 is required for boot), and the startup copies it, like Teensy (L135–137). VTOR is set after the copy.
- **Startup order:**
  - The ACDC startup (`ACDC/Core/Src/startup_stm32h743xx.s`) calls `bl SystemInit` (L65) *before* the `.data` copy (L69ff) and calls `main` at L98.
  - The ITCM copy goes right after the `.data`/`.bss` loop and before `main`/`__libc_init_array`.
  - `SystemInit`, `Reset_Handler` itself and **everything called from global constructors** must stay in flash. gregsbrain t/3370 #15: "check you haven't put any code into ITCRAM that will get executed before main is called. In particular look out for functions called from the constructor of a global object." Teensy comment L108. [belegt]
  - SysTick is only started in `HAL_Init` (in `main`), so it is uncritical.

### 5b. Linker-script pattern (sketch, [Hypothese] until built)

```ld
/* in xibeca.ld, after .ccmdata, before PROVIDE(_CCMRAM) */
.itcm_text :
{
  . = ALIGN(1024);
  _sitcm_vect = .;  KEEP(*(.itcm_vectors))          /* optional, if VTOR→ITCM */
  . = ALIGN(8);
  _sitcm_text = .;
  *(.itcm_text .itcm_text*)                          /* attribute-tagged own code */
  *stm32h7xx_hal_dma.o(.text.HAL_DMA_IRQHandler)     /* foreign objects by file+section */
  *stm32h7xx_hal_pcd.o(.text.HAL_PCD_IRQHandler)
  *port.o(.text.xPortPendSVHandler .text.vPortSVCHandler .text.xPortSysTickHandler)
  *tasks.o(.text.vTaskSwitchContext .text.xTaskIncrementTick)
  . = ALIGN(8);                                      /* ECC: full 64-bit words */
  _eitcm_text = .;
} >CCMRAM AT>FLASH
_litcm_text = LOADADDR(.itcm_text);
PROVIDE(_CCMRAM = .);  /* must come AFTER .itcm_text */
```

- **The patterns must come earlier in the script than the general `.text` (`*(.text*)`).** GNU ld assigns an input section to the first matching rule. daisyConvol inserts its `.itcmram_text` with awk *before* `.text` for exactly this reason (`examples/cabsim/Makefile` L31–44, pattern `*<obj>.o(.text .text*)`). [belegt]
- File and section patterns work without changing HAL/FreeRTOS sources because OpenWare compiles with `-ffunction-sections` (`.text.<funktion>`). [Code]
- C++ symbols need mangled names or wildcards (`*(.text._ZN*Codec*)`). Check with `nm`/`readelf -S`.
- Daisy-community variants:
  - attribute only (`__attribute__((section(".itcmram_text")))`, t/3370 #14/#15)
  - per object (daisyConvol)
  - build-time selection from a priority list with a size budget (tessera `itcm_pick.py`, PR #673)

### 5c. Copy loop and ECC [belegt: AN5342; implementation = Hypothese]

- Copy at 8-byte granularity: start and end of `.itcm_text` and the LMA must be `ALIGN(8)`. Use `ldrd/strd` or two consecutive 32-bit stores per 64-bit word.
  - AN5342: "an unaligned write to uninitialized memories is likely to trigger the ECC error". A partial word is held "until the next write access".
  - A half-written last word would remain as an "incomplete word".
- Optionally zero-fill the unused CCM gap up to `_CCMRAM` too (with 64-bit writes). The patch heap is zero-filled anyway (`memset` at patch start).
- After the copy, `DSB` + `ISB` before the first jump into ITCM. This is standard practice for freshly written code. Teensy has a `dsb` at the start of `ResetHandler2`. [Hypothese]
- Optional, as in Teensy: an MPU region over `.itcm_text` read-only + execute after the copy. It protects against patch or stack overruns into code. Watch the region count in `Source/mpu.c`. [Hypothese]

### 5d. Veneers, function pointers, `-mlong-calls`

- **`-mlong-calls` is not needed.** ld automatically inserts stubs for out-of-range `BL` calls (§4). Neither libDaisy, daisyConvol, Brainscape nor Teensy use `-mlong-calls`. [belegt]
- **Calls out of ITCM → flash cost a veneer (in ITCM) plus a fetch from flash via the I-cache.**
  - Brainscape fails its build on any unlisted veneer out of ITCM: "The audio path makes none per sample".
  - For our goal (a current profile independent of the flash layout), every call from the ISR, scheduler or audio task into flash code, e.g. `memcpy`, libgcc/`__aeabi_*` helpers, HAL helpers, `osSemaphore*` wrappers, FreeRTOS `queue.c`, partially undoes the effect.
  - → After the build, list the ITCM veneers (`nm`/map: `__*_veneer`) and pull them into `.itcm_text` or accept them consciously. [Hypothese, based on Brainscape]
- Calls **from flash into ITCM** get veneers in flash (cheap, then in the I-cache). [Hypothese]
- **Function pointers** need no veneers: the vector table, HAL callbacks in `hdma->XferCpltCallback`, FreeRTOS task entries and `BLX reg` all hold full 32-bit addresses. Pitfall: **address 0x0**. A function at 0x0 looks like `NULL`. This is not relevant for us (start 0x3000). [belegt]
  - antisvin t/3370 #4/#13: "a pointer to that value is indistinguishable from a null pointer"
  - Teensy `. = . + 32`
  - daisyConvol `. = . + 8`
- **COMDAT/inline/templates:** with C++, a template or inline function is a COMDAT section, and ld keeps the *first* copy read. Per-object patterns can then leave it in flash. Brainscape checks this explicitly (`ItcmCheck.cmake` header). Relevant for OpenWare C++ (`Codec`, `UsbAudio`, `ProgramManager`). [belegt]
- **Orphan trap:** a section with VMA in RAM and LMA in flash that no loop copies. tessera checks it with `memcheck.py` after the link (PR #673). [belegt]

### 5e. Data alongside the code [Hypothese]

- `.rodata` of the hot path (tables, `switch` jump tables if not inline, constant strings) stays in flash. Read via D-cache/AXI, it still produces layout-dependent flash accesses.
- Teensy moves all `.rodata` into DTCM. Tessera and Brainscape put the hot tables into DTCM.
- For us, check which `.rodata` the hot path reads (map file) and copy small parts into DTCM if needed (`DTCMRAM` 48 KB, `.data` copy is already there).

### 5f. Scope [Hypothese]

- 10 KB of ITCM is small. Teensy runs everything from ITCM. Daisy community projects use 40–58 KB, and in OpenWare 52 KB of CCM are free. The real limit is the patch heap in CCM, not ITCM size.
- Tradeoff:
  - The more of the periodic path (incl. veneer targets) sits in ITCM, the less the line spectrum depends on the flash layout (daisyConvol: "code layout then does not change their cost").
  - The I-cache contents of the rest change too (zbuc: "non-monotonic"), so the patch's timing in flash changes as well. A/B against a control in the same session is mandatory (D33/D34 rule).
- **The patch itself** runs from the patch area (PATCHRAM/PLUSRAM, not flash) and is not affected by this. Its timing per block stays the dominant current pulse. The ITCM move only makes the *firmware* part layout-independent.

## 6. Implications for our plan [Hypothese throughout]

1. **The Daisy comparison does not refute the plan, but gives no precedent for it.** Electrosmith fights the block-rate tone only by moving the frequency (block size), flattening the current (extra load outside the callback) and hardware. ITCM is a performance topic there, without a noise measurement. Our ITCM build would be the first measurement of ITCM ↔ line level on this MCU family.
2. **Keep:** `.itcm_text >CCMRAM AT>FLASH`, copy in `Reset_Handler`, `-ffunction-sections` patterns for HAL/FreeRTOS, VTOR into ITCM.
3. **Change or add:**
   - (a) `_CCMRAM` behind `.itcm_text` (heap collision).
   - (b) Vector table `ALIGN(1024)`.
   - (c) Section and LMA `ALIGN(8)`, 64-bit copy, `DSB/ISB`.
   - (d) Veneer audit after the link (calls out of ITCM ≈ 0 in the ISR/audio path; pull in libgcc/`memcpy`/`__aeabi_*` if needed).
   - (e) Nothing that runs before `main` (incl. global constructors) in ITCM.
   - (f) Optional MPU read-only over ITCM code.
   - (g) Check hot `.rodata` (→ DTCM).
4. **Test the Daisy tutorial lever independently of ITCM:** constant load outside the callback, e.g. an idle task with a dummy MAC loop from DTCM. That matches `layout_noise` §4.2(a) and is now vendor-endorsed. The block-rate alternative from t/9084 (higher callback rate) remains a side path for us because of USB and Patch 06.

## 7. Searched without useful hits (do not repeat)

- libDaisy, DaisySP, DaisyExamples (clones above), grep `itcm|ramfunc|fastrun|long-calls|long_call|section(`:
  - libDaisy: only `ITCMRAM` in MEMORY and `system.cpp` region detection.
  - DaisySP: only `DSY_SDRAM_BSS` in tests.
  - DaisyExamples: only `DSY_SDRAM_BSS` and a copied `.lds` (`pod/Midi`).
- GitHub issues `repo:daisyaudio/libDaisy`: `ITCM` (0), `org:daisyaudio ITCM` (0). `noise` (28, only #656 relevant = t/6028, timing/ripple, not layout), `cache`, `linker`, `sram speed`, `qspi slow`.
  - Note: `repo:electro-smith/...` gives "Validation Failed" because the org was renamed to `daisyaudio`.
- community.daisy.audio search: `ITCM`, `itcm_text`, `BOOT_SRAM noise`, `QSPI noise`, `callback noise`, `blocksize noise`, `noise cpu`, `ramfunc`, `DTCM performance`, `noise code`.
  - Threads read in full: 3370, 9084, 1854.
- PJRC: WebSearch `FASTRUN|ITCM|FLASHMEM` + noise/spur/344 Hz → no Teensy 4 thread on noise vs placement.
- Not reachable: ST AN4891 directly from st.com (connection reset / empty reply), so the numbers in AN4891 were not re-read. The ARM VTOR page (support.arm.com) gave no content.
