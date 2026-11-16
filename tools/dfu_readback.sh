#!/usr/bin/env bash
# Nur-lesender Firmware-Readback des AC/DC über den STM32-ROM-DFU.
#
# Verwendet ausschließlich `dfu-util -l` (auflisten) und `dfu-util -U` (Gerät -> Datei).
# Niemals -D (Download/Flash), niemals ":leave", keine Option-Bytes schreiben.
#
# Voraussetzung: acdc1 ist im DFU-Modus, z. B. per
#   tools/owl_read.py --reset-to-dfu --yes
# Zurück in die normale Firmware: Case aus UND USB-Kabel ab, dann Case an, dann USB
# wieder dran (USB allein hält das Board sonst im DFU).
#
# Aufruf: tools/dfu_readback.sh [ausgabe-verzeichnis]
set -euo pipefail

OUT="${1:-backup/acdc1/$(date +%Y%m%d)/flash}"
REL="firmware/releases/v22.5.0/ACDC.bin"
FLASH_ADDR=0x08000000
FLASH_LEN=131072   # STM32H750: 128 KB internes Flash

command -v dfu-util >/dev/null || { echo "dfu-util not found, please install it" >&2; exit 2; }
mkdir -p "$OUT"

echo "== DFU devices"
dfu-util -l 2>&1 | tee "$OUT/dfu-util_list.txt"
# STM32-ROM-DFU: VID:PID 0483:df11
if ! grep -q "0483:df11" "$OUT/dfu-util_list.txt"; then
  echo "No STM32 DFU device (0483:df11) found. Try the other USB socket (never both at the same time)." >&2
  exit 3
fi

ALT=$(grep "0483:df11" "$OUT/dfu-util_list.txt" | grep -i "Internal Flash" | sed -n 's/.*alt=\([0-9]*\).*/\1/p' | head -1)
[ -n "$ALT" ] || { echo "Alt setting for 'Internal Flash' not found, see $OUT/dfu-util_list.txt" >&2; exit 4; }

IMG="$OUT/acdc1_internal_flash.bin"
[ -e "$IMG" ] && { echo "$IMG already exists, not overwriting." >&2; exit 5; }

echo "== Reading: alt=$ALT, $FLASH_ADDR, $FLASH_LEN bytes -> $IMG"
dfu-util -d 0483:df11 -a "$ALT" -s "$FLASH_ADDR:$FLASH_LEN" -U "$IMG" 2>&1 | tee "$OUT/dfu-util_upload.txt"

ls -l "$IMG"
shasum -a 256 "$IMG" | tee "$OUT/sha256.txt"
[ -f "$REL" ] && shasum -a 256 "$REL" | tee -a "$OUT/sha256.txt"
echo "Done. Evaluate with: python3 tools/compare_firmware.py $IMG $REL"
