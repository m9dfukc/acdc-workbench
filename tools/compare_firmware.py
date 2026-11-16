"""Compares a firmware image (DFU readback) with a reference .bin.

Output: size, end of the payload (before the 0xFF padding), SHA-256, match,
vector table, version and marker strings. Read-only, standard library only.

Usage: python3 tools/compare_firmware.py <readback.bin> <reference.bin> [--json out.json]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
from pathlib import Path

# Strings, die Builds unterscheiden (aus Repo-Analyse, docs/messlog.md „Durchleitung“)
MARKERS = [
    "v22.5.0", "v22.4", "v22.5.rc", "Storing bootloader", "Readback failed",
    "OWL-ACDC", "LIAM-ACDC", "AC/DC", "Rebel Technology", "rx unf",
]


def payload_end(b: bytes) -> int:
    end = len(b)
    while end > 0 and b[end - 1] == 0xFF:
        end -= 1
    return end


def strings(b: bytes, n: int = 5) -> list[str]:
    return [m.group().decode() for m in re.finditer(rb"[\x20-\x7e]{%d,}" % n, b)]


def info(path: Path) -> dict:
    b = path.read_bytes()
    end = payload_end(b)
    sp, reset = struct.unpack("<II", b[:8])
    s = strings(b[:end])
    return {
        "path": str(path), "size": len(b), "payload_end": end,
        "sha256_full": hashlib.sha256(b).hexdigest(),
        "sha256_payload": hashlib.sha256(b[:end]).hexdigest(),
        "initial_sp": f"0x{sp:08x}", "reset_handler": f"0x{reset:08x}",
        "markers": {m: [x for x in s if m in x][:5] for m in MARKERS if any(m in x for x in s)},
        "version_like": sorted({x for x in s if re.search(r"v2\d\.\d", x)})[:20],
        "_bytes": b,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("readback", type=Path)
    ap.add_argument("reference", type=Path)
    ap.add_argument("--json", type=Path)
    a = ap.parse_args(argv)

    r, ref = info(a.readback), info(a.reference)
    rb, fb = r.pop("_bytes"), ref.pop("_bytes")
    n = min(len(rb), len(fb))
    diffs = [i for i in range(n) if rb[i] != fb[i]]
    res = {
        "readback": r, "reference": ref,
        "identical_prefix": rb[:len(fb)] == fb,
        "readback_tail_all_ff": all(x == 0xFF for x in rb[len(fb):]),
        "differing_bytes_in_overlap": len(diffs),
        "first_diffs": [f"0x{i:06x}" for i in diffs[:20]],
    }
    print(json.dumps(res, indent=2, ensure_ascii=False))
    if a.json:
        a.json.write_text(json.dumps(res, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
