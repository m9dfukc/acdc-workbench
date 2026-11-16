#!/usr/bin/env python3
"""Checks an AC/DC build with the hot path in ITCM (build 4, docs/05 "Build 4" Q11).

Read-only: works on the ELF and the binary with the toolchain tools
(objdump, nm, objcopy) and needs no Python packages beyond the standard library.

Checks (FAIL exits with code 1, WARN is only a note):
  1. Sections and symbols: .itcm_vectors/.itcm_text in CCMRAM after .ccmdata,
     _CCMRAM == _eitcm_text, alignment (vectors 1 KB, code and LMA 8 bytes because of ECC),
     LMA == _litcm_text, size of ACDC.bin <= 131072 bytes, bytes in the binary == ELF.
  2. Vector table: the hot interrupt handlers point into ITCM, the copy fits.
  3. Hot functions (list HOT) are all in ITCM.
  4. Branches out of ITCM: no direct bl/b out, the veneers ITCM -> flash are all
     listed in COLD (error paths or rare event paths) with a reason.
  5. Literals in ITCM code that point into flash (addresses of code or .rodata).
  6. Function pointers of the USB audio class (USBD_AUDIO) for the hot callbacks in ITCM.
  7. Nothing in ITCM is called before the copy (SystemInit).
  8. Optional --ref: nm comparison against a reference build (e.g. 3d).
  9. Optional --same-itcm: ITCM content (code and vector copy) byte-identical to
     another build (padded variant fx3ip against fx3i), plus how much has moved in flash.

Bisection variants (build 4x, docs/05): --groups selects the groups that should be in ITCM
(letters A–H and L, default: all). Functions and vectors of the other groups must then
be in flash; veneers from ITCM to them are intended (separate category).
For variants a failed anchor check is only a warning. --no-vector-copy: Reset_Handler does
not copy the vector table and does not set VTOR (variant novt).

Usage:
  uv run python tools/check_itcm.py firmware/builds/acdc1-build4-fx3i \
      [--ref firmware/builds/acdc1-build3d-fx2] [--same-itcm firmware/builds/…] [--out DIR]
      [--groups ABCEFGHL] [--no-vector-copy]
Takes a build directory (with ACDC.elf and ACDC.bin) or an ELF directly. The report is
written as Markdown and JSON to --out (default: the build directory, files check_itcm.*)
and printed. The report text is German.
"""
from __future__ import annotations

import argparse
import bisect
import json
import os
import re
import struct
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

TOOLROOT = os.environ.get("TOOLROOT", "/Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin/")
FLASH_BASE = 0x08000000
FLASH_MAX = 131072
CCMRAM = (0x00001000, 0x00010000)
VTOR_ALIGN = 1024

# Heißer Pfad (docs/uebergaben/uebergabe-2026-11-16-itcm.md, Gruppen A–H + L, Q7). Symbolnamen wie in nm (gemangelt).
# Gruppen wie im Linkerskript (Patch 11); der erste Buchstabe des Schlüssels ist die Gruppe für --groups.
HOT: dict[str, list[str]] = {
    "A SAI-DMA-ISR": [
        "DMA1_Stream0_IRQHandler", "DMA1_Stream1_IRQHandler", "HAL_DMA_IRQHandler",
        "SAI_DMATxHalfCplt", "SAI_DMATxCplt", "SAI_DMARxHalfCplt", "SAI_DMARxCplt",
        "HAL_SAI_RxHalfCpltCallback", "HAL_SAI_RxCpltCallback",
        "HAL_SAI_TxHalfCpltCallback", "HAL_SAI_TxCpltCallback",
        "audioCallback", "vTaskNotifyGiveFromISR", "vPortValidateInterruptPriority",
    ],
    "B Scheduler": [
        "PendSV_Handler", "vTaskSwitchContext", "ulTaskNotifyTake", "prvAddCurrentTaskToDelayedList",
        "vPortEnterCritical", "vPortExitCritical", "uxListRemove", "vListInsertEnd", "vListInsert",
        "prvIdleTask",
    ],
    "C Audio-Task": [
        "onProgramReady", "_Z15usbd_tx_convertPlj", "_Z15usbd_rx_convertPlj", "updateParameters",
        "_ZN10MidiWriter8transmitEv", "_ZN12MidiReceiver7receiveEv", "usbd_midi_ready", "usbd_midi_tx",
        "getProgramVector",
    ],
    "D USB": [
        "OTG_FS_IRQHandler", "HAL_PCD_IRQHandler", "USB_ReadInterrupts", "USB_ReadDevAllOutEpInterrupt",
        "USB_ReadDevAllInEpInterrupt", "USB_ReadDevOutEPInterrupt", "USB_ReadDevInEPInterrupt",
        "USB_GetMode", "USB_ReadPacket", "USB_WritePacket", "USB_EPStartXfer",
        "HAL_PCD_SOFCallback", "USBD_LL_SOF", "_ZL14USBD_AUDIO_SOFP19_USBD_HandleTypeDef",
        "usbd_audio_sof_callback", "usbd_audio_get_rx_count",
        "HAL_PCD_DataOutStageCallback", "USBD_LL_DataOutStage",
        "_ZL18USBD_AUDIO_DataOutP19_USBD_HandleTypeDefh", "USBD_LL_GetRxDataSize",
        "HAL_PCD_EP_GetRxCount", "USBD_LL_PrepareReceive", "HAL_PCD_EP_Receive",
        "HAL_PCD_DataInStageCallback", "USBD_LL_DataInStage",
        "_ZL17USBD_AUDIO_DataInP19_USBD_HandleTypeDefh", "USBD_LL_Transmit", "HAL_PCD_EP_Transmit",
        "_ZN5Codec16getSampleCounterEv", "codec_ndtr",
        "HAL_PCD_ISOINIncompleteCallback", "USBD_LL_IsoINIncomplete",
        "_ZL26USBD_AUDIO_IsoINIncompleteP19_USBD_HandleTypeDefh",
        "USBD_LL_FlushEP", "HAL_PCD_EP_Flush", "USB_FlushTxFifo", "USB_FlushRxFifo",
        "HAL_PCD_ISOOUTIncompleteCallback", "USBD_LL_IsoOUTIncomplete",
        "_ZL27USBD_AUDIO_IsoOutIncompleteP19_USBD_HandleTypeDefh",
    ],
    "E SysTick": [
        "SysTick_Handler", "HAL_IncTick", "HAL_GetTick", "xTaskGetSchedulerState",
        "xPortSysTickHandler", "xTaskIncrementTick", "xTaskIncrementTick.part.0",
    ],
    "F ADC-DMA": [
        "DMA1_Stream3_IRQHandler", "ADC_DMAConvCplt", "ADC_DMAHalfConvCplt",
        "HAL_ADC_ConvCpltCallback", "HAL_ADC_ConvHalfCpltCallback",
    ],
    "G onLoop (07d)": [
        "_ZL20acdcMeasureRawInputsv", "_ZL14acdcOnLoopLatev", "setLed", "setLed.constprop.0",
        "getParameterValue", "setParameterValue",
    ],
    "H Hauptschleife (2 ms)": [
        "StartDefaultTask", "loop", "onLoop", "_ZN3Owl4loopEv", "_ZN14ProgramManager16isProgramRunningEv",
        "device_watchdog",
        "vTaskDelayUntil", "vTaskSuspendAll", "xTaskResumeAll", "xTaskResumeAll.part.0",
    ],
    "L libc-Helfer": ["memset", "memcpy", "abs"],
}
ALL_GROUPS = "".join(g[0] for g in HOT)

# Interrupt-Vektoren, die ins ITCM zeigen müssen (Index in der Vektortabelle, Gruppe).
HOT_VECTORS = {"PendSV_Handler": (14, "B"), "SysTick_Handler": (15, "E"),
               "DMA1_Stream0_IRQHandler": (16 + 11, "A"), "DMA1_Stream1_IRQHandler": (16 + 12, "A"),
               "DMA1_Stream3_IRQHandler": (16 + 14, "F"), "OTG_FS_IRQHandler": (16 + 101, "D")}

# Erlaubte Sprünge aus dem ITCM in den Flash (über Veneers): Ziel -> Grund.
# "Fehler" = Fehlerpfad, "Ereignis" = selten und nicht periodisch (Enumeration, Reset,
# Suspend, Stream-Start, Control-Transfer, MIDI-Eingang, Task-Löschen).
COLD: dict[str, str] = {
    "usbd_audio_error": "Fehler: USB-Puffer über-/unterlaufen (Debug-Meldung)",
    "_Z12debugMessagePKcff": "Fehler: Debug-Meldung",
    "_Z12debugMessagePKcfff": "Fehler: Debug-Meldung",
    "_Z12debugMessagePKci": "Fehler: Debug-Meldung",
    "vApplicationStackOverflowHook": "Fehler: Stack-Überlauf (FreeRTOS)",
    "HAL_ADC_ErrorCallback": "Fehler: ADC-DMA-Fehler",
    "HAL_DMA_Abort_IT": "Fehler: DMA-Fehler",
    "Error_Handler": "Fehler",
    "error": "Fehler",
    "USBD_LL_StallEP": "Fehler/Control: Endpoint stallen",
    "vPortFree": "Ereignis: Idle-Task räumt gelöschte Tasks auf (Patch-Wechsel)",
    "usbd_audio_rx_start_callback": "Ereignis: Playback-Stream startet",
    "usbd_midi_rx": "Ereignis: MIDI-Eingang vom Rechner",
    "HAL_PCD_SetupStageCallback": "Ereignis: Control-Transfer (EP0 Setup)",
    "USBD_CtlContinueSendData": "Ereignis: Control-Transfer (EP0)",
    "USBD_CtlContinueRx": "Ereignis: Control-Transfer (EP0)",
    "USBD_CtlReceiveStatus": "Ereignis: Control-Transfer (EP0)",
    "USBD_CtlSendStatus": "Ereignis: Control-Transfer (EP0)",
    "USB_EP0StartXfer": "Ereignis: Control-Transfer (EP0)",
    "USB_EP0_OutStart": "Ereignis: Control-Transfer/Enumeration (EP0)",
    "USB_ActivateSetup": "Ereignis: Enumeration",
    "USB_GetDevSpeed": "Ereignis: Enumeration",
    "USB_SetTurnaroundTime": "Ereignis: Enumeration",
    "HAL_RCC_GetHCLKFreq": "Ereignis: Enumeration (Turnaround-Zeit)",
    "HAL_PCD_ResetCallback": "Ereignis: USB-Bus-Reset",
    "HAL_PCD_SuspendCallback": "Ereignis: USB-Suspend",
    "HAL_PCD_ResumeCallback": "Ereignis: USB-Resume",
    "HAL_PCD_ConnectCallback": "Ereignis: USB-Connect",
    "HAL_PCD_DisconnectCallback": "Ereignis: USB-Disconnect",
    "HAL_PCDEx_LPM_Callback": "Ereignis: USB-LPM",
    "setup": "Ereignis: einmal beim Start der Hauptschleife (StartDefaultTask)",
}

# Im ITCM, aber nie ausgeführt (kein Fehler, nur zur Erklärung im Bericht).
NOT_RUN = {"acdc_onloop_pad": "Füllfunktion aus Patch 07d (liegt mit onLoop in .text.onLoop)"}


def tool(name: str) -> str:
    return f"{TOOLROOT}arm-none-eabi-{name}"


def run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


@dataclass
class Sym:
    addr: int
    size: int
    kind: str
    name: str


@dataclass
class Elf:
    path: Path
    syms: list[Sym]
    by_name: dict[str, Sym]
    sections: dict[str, dict]
    funcs: list[Sym] = field(default_factory=list)
    starts: list[int] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path) -> "Elf":
        syms: list[Sym] = []
        for line in run(tool("nm"), "-S", "-n", str(path)).splitlines():
            p = line.split()
            if len(p) == 4:
                syms.append(Sym(int(p[0], 16), int(p[1], 16), p[2], p[3]))
            elif len(p) == 3:
                syms.append(Sym(int(p[0], 16), 0, p[1], p[2]))
        by_name: dict[str, Sym] = {}
        for s in syms:
            by_name.setdefault(s.name, s)
        sections = {}
        for line in run(tool("objdump"), "-h", str(path)).splitlines():
            m = re.match(r"\s*\d+\s+(\S+)\s+([0-9a-f]+)\s+([0-9a-f]+)\s+([0-9a-f]+)\s+([0-9a-f]+)\s+2\*\*(\d+)", line)
            if m:
                sections[m.group(1)] = dict(size=int(m.group(2), 16), vma=int(m.group(3), 16),
                                            lma=int(m.group(4), 16), align=1 << int(m.group(6)))
        e = cls(path, syms, by_name, sections)
        e.funcs = sorted((s for s in syms if s.kind in "tTwW" and s.size > 0), key=lambda s: s.addr)
        e.starts = [s.addr for s in e.funcs]
        return e

    def sym(self, name: str) -> int | None:
        s = self.by_name.get(name)
        return s.addr if s else None

    def owner(self, addr: int) -> Sym | None:
        i = bisect.bisect_right(self.starts, addr) - 1
        if i >= 0:
            f = self.funcs[i]
            if f.addr <= addr < f.addr + f.size:
                return f
        return None

    def describe(self, addr: int) -> str:
        """Symbol, in dem eine Adresse liegt (Funktion oder Datenobjekt)."""
        a = addr & ~1
        best = None
        for s in self.syms:  # kleinstes Objekt mit Größe, sonst ein Linker-Symbol genau an der Adresse
            if s.size and s.addr <= a < s.addr + s.size and (best is None or not best.size or s.size < best.size):
                best = s
            elif not s.size and s.addr == a and best is None:
                best = s
        if best:
            off = a - best.addr
            return best.name + (f"+0x{off:x}" if off else "")
        for name, sec in self.sections.items():
            if sec["vma"] <= a < sec["vma"] + sec["size"]:
                return f"[{name}+0x{a - sec['vma']:x}]"
        return "?"

    def section_bytes(self, name: str) -> bytes:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "sec.bin"
            run(tool("objcopy"), "-O", "binary", f"--only-section={name}", str(self.path), str(out))
            return out.read_bytes()


@dataclass
class Report:
    lines: list[str] = field(default_factory=list)
    fails: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)
    data: dict = field(default_factory=dict)

    def h(self, title: str) -> None:
        self.lines += ["", f"## {title}", ""]

    def p(self, text: str = "") -> None:
        self.lines.append(text)

    def ok(self, cond: bool, text: str, warn_only: bool = False) -> bool:
        tag = "ok" if cond else ("WARN" if warn_only else "FAIL")
        self.lines.append(f"- **{tag}** {text}")
        if not cond:
            (self.warns if warn_only else self.fails).append(text)
        return cond


def resolve_build(arg: str) -> tuple[Path, Path | None]:
    p = Path(arg)
    if p.is_dir():
        b = p / "ACDC.bin"
        return p / "ACDC.elf", (b if b.exists() else None)
    b = p.with_suffix(".bin")
    return p, (b if b.exists() else None)


def disassemble(elf: Elf, start: int, stop: int) -> list[tuple[int, str, str]]:
    out = run(tool("objdump"), "-d", "--no-show-raw-insn", f"--start-address=0x{start:x}",
              f"--stop-address=0x{stop:x}", str(elf.path))
    ins = []
    for line in out.splitlines():
        m = re.match(r"^\s*([0-9a-f]+):\s+(\S+)\s*(.*)$", line)
        if m and not m.group(2).startswith("."):
            ins.append((int(m.group(1), 16), m.group(2), m.group(3)))
    return ins


BRANCH = re.compile(r"^(b|bl|blx|cbz|cbnz)(eq|ne|cs|cc|hs|lo|mi|pl|vs|vc|hi|ls|ge|lt|gt|le|al)?(\.n|\.w)?$")


def branches(ins):
    for addr, op, rest in ins:
        if BRANCH.match(op):
            m = re.search(r"\b([0-9a-f]+) <", rest)
            if m:
                yield addr, op, int(m.group(1), 16)


def literal_values(elf: Elf, ins, sec_bytes: bytes, sec_vma: int):
    """Werte von pc-relativen ldr (Literal-Pool) und movw/movt-Paaren."""
    vals = []
    movw: dict[str, tuple[int, int]] = {}
    for addr, op, rest in ins:
        if op.startswith("ldr") and not op.startswith("ldrd") and "[pc" in rest:
            m = re.search(r";\s*\(([0-9a-f]+)", rest) or re.search(r"@\s*\(([0-9a-f]+)", rest)
            if m:
                la = int(m.group(1), 16)
                off = la - sec_vma
                if 0 <= off <= len(sec_bytes) - 4:
                    vals.append((addr, struct.unpack_from("<I", sec_bytes, off)[0]))
        elif op.startswith("movw"):
            m = re.match(r"(r\d+|ip|lr),\s*#(\d+)", rest)
            if m:
                movw[m.group(1)] = (addr, int(m.group(2)))
        elif op.startswith("movt"):
            m = re.match(r"(r\d+|ip|lr),\s*#(\d+)", rest)
            if m and m.group(1) in movw:
                vals.append((addr, (int(m.group(2)) << 16) | movw[m.group(1)][1]))
    return vals


def check(build: str, ref: str | None, same: str | None, out_dir: str | None,
          groups: str = ALL_GROUPS, vector_copy: bool = True) -> int:
    elf_path, bin_path = resolve_build(build)
    elf = Elf.load(elf_path)
    r = Report()
    name = elf_path.parent.name
    variant = set(groups) != set(ALL_GROUPS)
    flash_groups = {g: names for g, names in HOT.items() if g[0] not in groups}
    flash_names = {n: g for g, names in flash_groups.items() for n in names}
    r.p(f"# check_itcm: {name}")
    r.p("")
    r.p(f"ELF `{elf_path}`" + (f", Binary `{bin_path}`" if bin_path else ""))
    r.p("")
    r.p(f"Gruppen im ITCM: **{' '.join(sorted(groups))}**"
        + (f"; im Flash (Variante): {', '.join(flash_groups)}" if variant else " (alle)")
        + ("" if vector_copy else "; **ohne Vektorkopie/VTOR** (--no-vector-copy)"))
    r.data["groups"] = "".join(sorted(groups))
    r.data["vector_copy"] = vector_copy

    # 1. Sections und Symbole
    r.h("1 Sections, Symbole, Größe")
    S = {k: elf.sym(k) for k in ("_sitcm_vect", "_eitcm_vect", "_sitcm_text", "_eitcm_text",
                                 "_litcm_text", "_CCMRAM", "_CCMRAM_END", "_CCMRAM_SIZE",
                                 "_ISR_VECTOR", "_ISR_VECTOR_SIZE")}
    missing = [k for k, v in S.items() if v is None]
    if not r.ok(not missing, f"Linker-Symbole vorhanden {'' if not missing else missing}"):
        return finish(r, elf_path, out_dir)
    it = elf.sections.get(".itcm_text")
    iv = elf.sections.get(".itcm_vectors")
    cd = elf.sections.get(".ccmdata")
    r.ok(it is not None and iv is not None, "Sections .itcm_vectors und .itcm_text vorhanden")
    r.ok(CCMRAM[0] <= S["_sitcm_vect"] < S["_eitcm_text"] <= CCMRAM[1], "ITCM-Block liegt im CCMRAM 0x1000–0xFFFF")
    if cd:
        r.ok(cd["vma"] + cd["size"] <= S["_sitcm_vect"],
             f".ccmdata (PROGRAMSTACK 0x{cd['vma']:x}–0x{cd['vma'] + cd['size']:x}) liegt vor dem ITCM-Block")
    r.ok(S["_CCMRAM"] == S["_eitcm_text"], f"_CCMRAM (Patch-Heap) = _eitcm_text = 0x{S['_eitcm_text']:x}")
    r.ok(S["_sitcm_vect"] % VTOR_ALIGN == 0, f"Vektorkopie 0x{S['_sitcm_vect']:x} auf 1 KB ausgerichtet")
    r.ok(S["_eitcm_vect"] - S["_sitcm_vect"] >= S["_ISR_VECTOR_SIZE"],
         f"Platz für die Vektortabelle ({S['_ISR_VECTOR_SIZE']} B)")
    for k in ("_sitcm_text", "_eitcm_text", "_litcm_text", "_sitcm_vect", "_eitcm_vect"):
        r.ok(S[k] % 8 == 0, f"{k} = 0x{S[k]:x} 8-Byte-ausgerichtet (ECC)")
    if it:
        r.ok(it["vma"] == S["_sitcm_text"] and it["size"] == S["_eitcm_text"] - S["_sitcm_text"],
             f".itcm_text VMA 0x{it['vma']:x}, Größe {it['size']} B = _eitcm_text − _sitcm_text (Veneers inklusive)")
        r.ok(it["lma"] == S["_litcm_text"], f".itcm_text LMA 0x{it['lma']:x} = _litcm_text")
        r.ok(FLASH_BASE <= it["lma"] and it["lma"] + it["size"] <= FLASH_BASE + FLASH_MAX, "LMA liegt im Flash")
    itcm_text = elf.section_bytes(".itcm_text")
    bin_bytes = bin_path.read_bytes() if bin_path else None
    if bin_bytes is not None:
        r.ok(len(bin_bytes) <= FLASH_MAX, f"ACDC.bin {len(bin_bytes)} B <= {FLASH_MAX} B (frei {FLASH_MAX - len(bin_bytes)} B)")
        off = S["_litcm_text"] - FLASH_BASE
        r.ok(bin_bytes[off:off + len(itcm_text)] == itcm_text, "Kopierquelle im Binary = Inhalt von .itcm_text im ELF")
        voff = S["_ISR_VECTOR"] - FLASH_BASE
        vec = bin_bytes[voff:voff + S["_ISR_VECTOR_SIZE"]]
    else:
        r.ok(False, "ACDC.bin fehlt, Binary-Prüfungen übersprungen", warn_only=True)
        vec = elf.section_bytes(".isr_vector")
    heap = S["_CCMRAM_SIZE"]
    sizes = dict(itcm_vectors=S["_eitcm_vect"] - S["_sitcm_vect"], itcm_text=len(itcm_text),
                 itcm_total=S["_eitcm_text"] - S["_sitcm_vect"], patch_heap_ccm=heap,
                 bin=len(bin_bytes) if bin_bytes else None)
    r.data["sizes"] = sizes
    r.data["symbols"] = {k: f"0x{v:x}" for k, v in S.items()}
    r.p("")
    r.p(f"ITCM-Belegung: Vektorkopie {sizes['itcm_vectors']} B @ 0x{S['_sitcm_vect']:x}, "
        f"Code {sizes['itcm_text']} B @ 0x{S['_sitcm_text']:x}–0x{S['_eitcm_text']:x} "
        f"(zusammen {sizes['itcm_total']} B ab 0x{S['_sitcm_vect']:x}). "
        f"Patch-Heap im CCM: {heap} B ({heap / 1024:.1f} KB, vorher 53248 B).")

    lo, hi = S["_sitcm_text"], S["_eitcm_text"]
    in_itcm = lambda a: lo <= (a & ~1) < hi  # noqa: E731

    # 2. Vektortabelle
    r.h("2 Vektortabelle")
    if not vector_copy:
        r.p("- Ohne Vektorkopie: die Tabelle im Flash (VTOR = 0x08000000) zeigt direkt auf die Handler.")
    for hname, (idx, g) in HOT_VECTORS.items():
        v = struct.unpack_from("<I", vec, idx * 4)[0]
        if g in groups:
            r.ok(in_itcm(v) and elf.describe(v) == hname, f"Vektor {idx} → 0x{v:08x} {elf.describe(v)} (erwartet {hname} im ITCM)")
        else:
            r.ok(not in_itcm(v) and elf.describe(v) == hname,
                 f"Vektor {idx} → 0x{v:08x} {elf.describe(v)} (erwartet {hname} im Flash, Gruppe {g} nicht gewählt)")
    v0 = struct.unpack_from("<I", vec, 0)[0]
    r.ok(v0 == elf.sym("_estack"), f"Vektor 0 (MSP) = 0x{v0:x} = _estack (FreeRTOS liest ihn über VTOR)")

    # 3. Heiße Funktionen
    r.h("3 Heiße Funktionen im ITCM")
    hot_rows = []
    cold_rows = []
    for group, names in HOT.items():
        for n in names:
            s = elf.by_name.get(n)
            if s is None:
                r.ok(False, f"{group}: `{n}` nicht im ELF (inline oder umbenannt?)", warn_only=True)
                continue
            if group in flash_groups:
                cold_rows.append((group, n, s.addr, s.size, in_itcm(s.addr)))
                if in_itcm(s.addr):
                    r.ok(False, f"{group}: `{n}` liegt im ITCM (0x{s.addr:08x}), sollte in dieser Variante im Flash sein")
                continue
            hot_rows.append((group, n, s.addr, s.size, in_itcm(s.addr)))
            if not in_itcm(s.addr):
                r.ok(False, f"{group}: `{n}` liegt bei 0x{s.addr:08x}, nicht im ITCM")
    n_in = sum(1 for x in hot_rows if x[4])
    r.ok(n_in == len(hot_rows), f"{n_in} von {len(hot_rows)} heißen Funktionen der gewählten Gruppen im ITCM, "
         f"zusammen {sum(x[3] for x in hot_rows)} B")
    if flash_groups:
        n_fl = sum(1 for x in cold_rows if not x[4])
        r.ok(n_fl == len(cold_rows), f"{n_fl} von {len(cold_rows)} Funktionen der nicht gewählten Gruppen "
             f"({', '.join(g[0] for g in flash_groups)}) im Flash, zusammen {sum(x[3] for x in cold_rows)} B")
    itcm_funcs = [f for f in elf.funcs if in_itcm(f.addr) and not f.name.endswith("_veneer")]
    hot_names = {x[1] for x in hot_rows}
    extra = [f.name for f in itcm_funcs if f.name not in hot_names and f.name not in NOT_RUN]
    r.p(f"- Funktionen im ITCM insgesamt: {len(itcm_funcs)}"
        + "".join(f"; `{n}`: {why}" for n, why in NOT_RUN.items() if elf.by_name.get(n) and in_itcm(elf.by_name[n].addr)))
    r.ok(not extra, "keine unerwarteten Funktionen im ITCM" + (f": {', '.join(extra)}" if extra else ""), warn_only=True)
    r.data["hot"] = [dict(group=g, name=n, addr=f"0x{a:x}", size=sz, itcm=i) for g, n, a, sz, i in hot_rows]
    r.data["hot_in_flash"] = [dict(group=g, name=n, addr=f"0x{a:x}", size=sz, itcm=i) for g, n, a, sz, i in cold_rows]

    # 4. Sprünge und Veneers
    r.h("4 Sprünge aus dem ITCM, Veneers")
    ins = disassemble(elf, lo, hi)
    veneers = {s.addr: s for s in elf.syms if s.name.endswith("_veneer") and in_itcm(s.addr)}
    callers: dict[int, set[str]] = {}
    direct_out = []
    for addr, op, tgt in branches(ins):
        src = elf.owner(addr)
        if src and src.name.endswith("_veneer"):
            continue
        if tgt in veneers:
            callers.setdefault(tgt, set()).add(src.name if src else f"0x{addr:x}")
        elif not in_itcm(tgt):
            direct_out.append((addr, op, tgt))
    r.ok(not direct_out, "keine direkten Sprünge aus dem ITCM hinaus (nur über Veneers)"
         + ("" if not direct_out else ": " + ", ".join(f"0x{a:x} {o} 0x{t:x}" for a, o, t in direct_out)))
    vrows = []
    unknown = []
    for va, vs in sorted(veneers.items()):
        off = va + 4 - S["_sitcm_text"]
        tgt = struct.unpack_from("<I", itcm_text, off)[0]
        tname = elf.describe(tgt)
        reason = COLD.get(tname)
        if reason is None and tname in flash_names:
            reason = f"Variante: Gruppe {flash_names[tname]} bleibt im Flash (gewollt)"
        if in_itcm(tgt):
            reason = "Ziel im ITCM?"
        vrows.append(dict(veneer=vs.name, addr=f"0x{va:x}", target=tname, target_addr=f"0x{tgt:08x}",
                          callers=sorted(callers.get(va, [])), reason=reason))
        if reason is None:
            unknown.append(tname)
    n_var = sum(1 for v in vrows if (v["reason"] or "").startswith("Variante"))
    r.ok(not unknown, f"{len(vrows)} Veneers ITCM → Flash, alle in COLD (Fehler-/Ereignispfad)"
         + (f" oder zu nicht gewählten Gruppen ({n_var}, gewollt)" if n_var else "")
         + ("" if not unknown else f"; unerwartet: {', '.join(unknown)}"))
    r.p("")
    r.p("| Ziel im Flash | Aufrufer im ITCM | Grund |")
    r.p("|---|---|---|")
    for v in sorted(vrows, key=lambda v: (v["reason"] or "", v["target"])):
        r.p(f"| `{v['target']}` | {', '.join(f'`{c}`' for c in v['callers'])} | {v['reason'] or '**unerwartet**'} |")
    r.data["veneers_out"] = vrows
    fl_veneers = [s for s in elf.syms if s.name.endswith("_veneer") and s.addr >= FLASH_BASE]
    r.p("")
    r.p(f"- Veneers Flash → ITCM: {len(fl_veneers)} (Aufrufe aus dem Flash-Code in den heißen Pfad, z. B. "
        + ", ".join(f"`{s.name[2:-7]}`" for s in fl_veneers[:8]) + (" …" if len(fl_veneers) > 8 else "") + ")")
    r.data["veneers_in"] = [s.name for s in fl_veneers]
    indirect = sorted({elf.owner(a).name for a, op, rest in ins
                       if op in ("blx", "bx") and not rest.startswith("lr") and elf.owner(a)})
    r.p(f"- Indirekte Aufrufe (`blx/bx reg`) in: {', '.join(f'`{n}`' for n in indirect)}")

    # 5. Literale
    r.h("5 Literale im ITCM-Code, die in den Flash zeigen")
    lits = literal_values(elf, ins, itcm_text, S["_sitcm_text"])
    flash_refs: dict[str, set[str]] = {}
    for a, v in lits:
        if FLASH_BASE <= v < FLASH_BASE + FLASH_MAX:
            src = elf.owner(a)
            flash_refs.setdefault(elf.describe(v), set()).add(src.name if src else f"0x{a:x}")
    r.p(f"{len(flash_refs)} Ziele (Daten oder Code im Flash, deren Adresse der ITCM-Code lädt):")
    r.p("")
    for t, srcs in sorted(flash_refs.items()):
        r.p(f"- `{t}` ← {', '.join(f'`{s}`' for s in sorted(srcs))}")
    r.data["flash_literals"] = {t: sorted(s) for t, s in flash_refs.items()}

    # 5b. Anker: alles, worauf das ITCM in den Flash zeigt, liegt vor _eitcm_anchor
    r.h("5b Anker im Flash (Voraussetzung für die Füllvariante)")
    anchor = elf.sym("_eitcm_anchor")
    refs = []  # (Adresse, Art, Name)
    for v in vrows:
        refs.append((int(v["target_addr"], 16), "Veneer-Ziel", v["target"]))
    for a, val in lits:
        if FLASH_BASE <= val < FLASH_BASE + FLASH_MAX:
            refs.append((val, "Literal", elf.describe(val)))
    for i in range(1, len(vec) // 4):
        val = struct.unpack_from("<I", vec, i * 4)[0]
        if FLASH_BASE <= val < FLASH_BASE + FLASH_MAX:
            refs.append((val, f"Vektor {i}", elf.describe(val)))
    uniq = {}
    for a, kind, n in refs:
        uniq.setdefault((a & ~1, n), []).append(kind)
    if anchor is None:
        r.ok(False, "_eitcm_anchor fehlt, Lage der Flash-Ziele nicht geprüft", warn_only=True)
    else:
        sa = elf.sym("_sitcm_anchor")
        behind = sorted({n for (a, n) in uniq if not (sa <= a < anchor)})
        r.ok(not behind, f"{len(uniq)} Flash-Ziele des ITCM (Vektoren, Veneer-Ziele, Literale) liegen im Anker "
             f"0x{sa:08x}–0x{anchor:08x} ({anchor - sa} B)" + ("" if not behind else f"; außerhalb: {', '.join(behind)}")
             + (" (Variante: Anker nur für Füllvarianten nötig, deshalb nur Warnung)" if variant and behind else ""),
             warn_only=variant)
    r.data["anchor"] = dict(start=f"0x{elf.sym('_sitcm_anchor') or 0:x}", end=f"0x{anchor or 0:x}",
                            refs=sorted({n for (a, n) in uniq}))

    # 6. USB-Klasse
    r.h("6 Funktionszeiger USBD_AUDIO")
    ua = elf.by_name.get("USBD_AUDIO")
    data = elf.sections.get(".data")
    if ua and data and data["vma"] <= ua.addr < data["vma"] + data["size"]:
        db = elf.section_bytes(".data")
        fields = ["Init", "DeInit", "Setup", "EP0_TxReady", "EP0_RxReady", "DataIn", "DataOut", "SOF",
                  "IsoINIncomplete", "IsoOUTIncomplete"]
        for i, f in enumerate(fields):
            v = struct.unpack_from("<I", db, ua.addr - data["vma"] + 4 * i)[0]
            hot = f in ("DataIn", "DataOut", "SOF", "IsoINIncomplete", "IsoOUTIncomplete")
            if hot and "D" in groups:
                r.ok(in_itcm(v), f"USBD_AUDIO.{f} → {elf.describe(v)} (0x{v:x}) im ITCM")
            elif hot:
                r.ok(not in_itcm(v), f"USBD_AUDIO.{f} → {elf.describe(v)} (0x{v:x}) im Flash (Gruppe D nicht gewählt)")
            else:
                r.p(f"- USBD_AUDIO.{f} → {elf.describe(v)} (Flash, kalt)")
    else:
        r.ok(False, "USBD_AUDIO nicht in .data gefunden", warn_only=True)

    # 7. Vor dem Kopieren
    r.h("7 Nichts im ITCM vor dem Kopieren")
    si = elf.by_name.get("SystemInit")
    seen, stack, bad = set(), [si] if si else [], []
    while stack:
        f = stack.pop()
        if f.name in seen:
            continue
        seen.add(f.name)
        for a, op, t in branches(disassemble(elf, f.addr, f.addr + f.size)):
            if in_itcm(t) or (elf.owner(t) and elf.owner(t).name.endswith("_veneer")):
                bad.append(f"{f.name} → 0x{t:x}")
            else:
                g = elf.owner(t)
                if g and g.addr != f.addr:
                    stack.append(g)
    r.ok(si is not None and not bad, f"SystemInit und Aufgerufene ({', '.join(sorted(seen))}) springen nicht ins ITCM"
         + ("" if not bad else f": {bad}"))
    rh = elf.by_name.get("Reset_Handler")
    if rh:
        rins = disassemble(elf, rh.addr, rh.addr + rh.size)
        order = [(a, t) for a, op, t in branches(rins) if op.startswith("bl")]
        names = [elf.describe(t) for a, t in order]
        r.p(f"- Reset_Handler ruft der Reihe nach: {', '.join(f'`{n}`' for n in names)}")
        r.ok(names[:1] == ["SystemInit"] and "__libc_init_array" in names and "main" in names,
             "Reset_Handler: SystemInit → (Kopien" + (", VTOR" if vector_copy else "") + ") → __libc_init_array → main")
        tsec = elf.sections[".text"]
        rvals = {v for a, v in literal_values(elf, rins, elf.section_bytes(".text"), tsec["vma"])}
        if vector_copy:
            r.ok(0xE000ED08 in rvals and S["_sitcm_vect"] in rvals and S["_litcm_text"] in rvals,
                 "Reset_Handler lädt _litcm_text, _sitcm_vect und SCB->VTOR (0xE000ED08)")
        else:
            r.ok(0xE000ED08 not in rvals and S["_sitcm_vect"] not in rvals and S["_litcm_text"] in rvals,
                 "Reset_Handler lädt _litcm_text, aber weder _sitcm_vect noch SCB->VTOR (ohne Vektorkopie)")

    # 8. nm gegen Referenz
    if ref:
        nm_compare(r, elf, ref)
    # 9. gleicher ITCM-Inhalt
    if same:
        same_itcm(r, elf, itcm_text, vec, S, same)
    return finish(r, elf_path, out_dir)


def nm_compare(r: Report, elf: Elf, ref: str) -> None:
    ref_elf = Elf.load(resolve_build(ref)[0])
    r.h(f"8 nm-Vergleich gegen {Path(ref).name}")
    ref_t = {s.name: s for s in ref_elf.funcs}
    new_t = {s.name: s for s in elf.funcs}
    common = [n for n in ref_t if n in new_t and not n.endswith("_veneer")]
    lo, hi = elf.sym("_sitcm_text"), elf.sym("_eitcm_text")
    moved_itcm = [n for n in common if lo <= new_t[n].addr < hi]
    same_addr = [n for n in common if new_t[n].addr == ref_t[n].addr]
    size_diff = [n for n in common if new_t[n].size != ref_t[n].size]
    only_ref = sorted(n for n in ref_t if n not in new_t and not n.endswith("_veneer"))
    only_new = sorted(n for n in new_t if n not in ref_t and not n.endswith("_veneer"))
    r.p(f"- Funktionen gemeinsam: {len(common)}, davon ins ITCM verlegt {len(moved_itcm)}, "
        f"gleiche Adresse {len(same_addr)}, andere Größe {len(size_diff)}")
    r.p(f"- nur in der Referenz: {', '.join(f'`{n}`' for n in only_ref) or '–'}")
    r.p(f"- nur im neuen Build: {', '.join(f'`{n}`' for n in only_new) or '–'}")
    if size_diff:
        r.p("- Größe geändert: " + ", ".join(f"`{n}` {ref_t[n].size}→{new_t[n].size}" for n in size_diff))
    r.p("")
    r.p("| Symbol | Referenz | neu | Δ Größe |")
    r.p("|---|---|---|---|")
    want = [n for g in HOT.values() for n in g] + ["onLoop", "main", "SystemInit", "Reset_Handler",
                                                    "_ZN11MidiHandler11handleSysExEPht"]
    rows = []
    for n in want:
        a, b = ref_elf.by_name.get(n), elf.by_name.get(n)
        fa = f"`{a.addr:08x}` ({a.size})" if a else "–"
        fb = f"`{b.addr:08x}` ({b.size})" if b else "–"
        ds = (b.size - a.size) if a and b else None
        r.p(f"| `{n}` | {fa} | {fb} | {'' if ds in (None, 0) else f'{ds:+d}'} |")
        rows.append(dict(name=n, ref=f"0x{a.addr:x}" if a else None, new=f"0x{b.addr:x}" if b else None,
                         ref_size=a.size if a else None, new_size=b.size if b else None))
    # Daten: RAM-Adressen der Variablen (Lage im RAM)
    ref_d = {s.name: s for s in ref_elf.syms if s.kind in "bBdD" and not FLASH_BASE <= s.addr < FLASH_BASE + FLASH_MAX}
    new_d = {s.name: s for s in elf.syms if s.kind in "bBdD" and not FLASH_BASE <= s.addr < FLASH_BASE + FLASH_MAX}
    dcommon = [n for n in ref_d if n in new_d]
    dsame = sum(1 for n in dcommon if ref_d[n].addr == new_d[n].addr)
    r.p("")
    r.p(f"- Datenobjekte im RAM (.data/.bss/…) gemeinsam {len(dcommon)}, gleiche RAM-Adresse {dsame}")
    r.data["nm_compare"] = dict(ref=str(ref), common=len(common), moved_itcm=len(moved_itcm),
                                same_addr=len(same_addr), size_diff=size_diff, only_ref=only_ref,
                                only_new=only_new, data_common=len(dcommon), data_same=dsame, rows=rows)


def same_itcm(r: Report, elf: Elf, itcm_text: bytes, vec: bytes, S: dict, other: str) -> None:
    o_elf_path, o_bin = resolve_build(other)
    o = Elf.load(o_elf_path)
    r.h(f"9 ITCM-Inhalt gegen {Path(other).name}")
    o_text = o.section_bytes(".itcm_text")
    r.ok(o.sym("_sitcm_text") == S["_sitcm_text"] and o.sym("_eitcm_text") == S["_eitcm_text"],
         f"gleiche ITCM-Grenzen 0x{S['_sitcm_text']:x}–0x{S['_eitcm_text']:x}")
    diffs = [i for i in range(min(len(o_text), len(itcm_text))) if o_text[i] != itcm_text[i]]
    r.ok(o_text == itcm_text, f".itcm_text bytegleich ({len(itcm_text)} B)"
         + ("" if not diffs else f"; {len(diffs)} Bytes verschieden, erste bei 0x{S['_sitcm_text'] + diffs[0]:x} "
            f"({elf.describe(S['_sitcm_text'] + diffs[0])})"))
    if o_bin:
        ob = o_bin.read_bytes()
        ovec = ob[o.sym("_ISR_VECTOR") - FLASH_BASE:][:len(vec)]
    else:
        ovec = o.section_bytes(".isr_vector")
    vd = [i // 4 for i in range(0, len(vec), 4) if vec[i:i + 4] != ovec[i:i + 4]]
    r.ok(vec == ovec, "Vektortabelle (wird ins ITCM kopiert) bytegleich"
         + ("" if not vd else f"; verschiedene Einträge: {vd[:12]}"))
    # Verschiebung im Flash außerhalb des ITCM
    a = {s.name: s.addr for s in elf.funcs if s.addr >= FLASH_BASE}
    b = {s.name: s.addr for s in o.funcs if s.addr >= FLASH_BASE}
    common = [n for n in a if n in b]
    shifts: dict[int, int] = {}
    for n in common:
        d = a[n] - b[n]
        shifts[d] = shifts.get(d, 0) + 1
    r.p(f"- Flash-Funktionen gemeinsam {len(common)}, Verschiebung dieser Build − {Path(other).name}: "
        + ", ".join(f"{d:+#x}: {c}" for d, c in sorted(shifts.items(), key=lambda x: -x[1])))
    ad = {s.name: s.addr for s in elf.syms if s.kind in "bBdD" and not FLASH_BASE <= s.addr < FLASH_BASE + FLASH_MAX}
    bd = {s.name: s.addr for s in o.syms if s.kind in "bBdD" and not FLASH_BASE <= s.addr < FLASH_BASE + FLASH_MAX}
    dc = [n for n in ad if n in bd]
    r.p(f"- Datenobjekte im RAM gemeinsam {len(dc)}, gleiche Adresse {sum(1 for n in dc if ad[n] == bd[n])}")
    r.data["same_itcm"] = dict(other=str(other), text_equal=o_text == itcm_text, vectors_equal=vec == ovec,
                               flash_shift_histogram={f"{d:+#x}": c for d, c in shifts.items()})


def finish(r: Report, elf_path: Path, out_dir: str | None) -> int:
    r.p("")
    r.p(f"**Ergebnis:** {'BESTANDEN' if not r.fails else 'NICHT BESTANDEN'} "
        f"({len(r.fails)} FAIL, {len(r.warns)} WARN)")
    text = "\n".join(r.lines) + "\n"
    out = Path(out_dir) if out_dir else elf_path.parent
    out.mkdir(parents=True, exist_ok=True)
    (out / "check_itcm.md").write_text(text)
    r.data.update(fails=r.fails, warns=r.warns, passed=not r.fails)
    (out / "check_itcm.json").write_text(json.dumps(r.data, indent=1, ensure_ascii=False) + "\n")
    print(text)
    print(f"→ {out / 'check_itcm.md'}", file=sys.stderr)
    return 0 if not r.fails else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("build", help="build directory (ACDC.elf, ACDC.bin) or ELF")
    ap.add_argument("--ref", help="reference build for the nm comparison (e.g. firmware/builds/acdc1-build3d-fx2)")
    ap.add_argument("--same-itcm", help="other build whose ITCM content must be byte-identical")
    ap.add_argument("--out", help="output directory for check_itcm.md/.json (default: build directory)")
    ap.add_argument("--groups", default=ALL_GROUPS,
                    help=f"groups in ITCM as letters (default: {ALL_GROUPS}; e.g. ABCEFGHL for noD)")
    ap.add_argument("--no-vector-copy", action="store_true",
                    help="variant without vector copy/VTOR (novt)")
    a = ap.parse_args()
    groups = a.groups.replace(",", "").replace(" ", "").upper()
    bad = set(groups) - set(ALL_GROUPS)
    if bad or not groups:
        ap.error(f"unknown groups {sorted(bad)}; allowed: {ALL_GROUPS}")
    return check(a.build, a.ref, a.same_itcm, a.out, groups, not a.no_vector_copy)


if __name__ == "__main__":
    sys.exit(main())
