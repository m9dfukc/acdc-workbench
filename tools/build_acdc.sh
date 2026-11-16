#!/usr/bin/env bash
# Reproduzierbarer AC/DC-Firmware-Build (OpenWare), ohne Schreibzugriff auf den Git-Klon.
#
# Ablauf:
#   1. Quellbaum per `git archive <commit>` aus firmware/OpenWare nach firmware/_work/<name>/ (Wegwerf-Baum, jederzeit neu erzeugbar)
#   2. Libraries-Tarball (fester Commit, z. B. firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz)
#      nach firmware/_work/<name>/Libraries/
#   3. Patches (patch -p1) in der angegebenen Reihenfolge anwenden
#   4. make -C ACDC CONFIG=Release mit fester Toolchain (TOOLROOT)
#   5. Größe gegen 131072 B prüfen, Ergebnis mit Log nach firmware/builds/<name>/
#
# Flasht nichts. Plan: docs/05-firmware-plan.md, Abschnitt „Abgestimmter Plan“ (E5).
#
# Aufruf:
#   tools/build_acdc.sh <name> <commit> <libraries.tar.gz> [patch ...]
# Beispiel (Reproduktions-Build):
#   FW_VERSION=v22.5.0 tools/build_acdc.sh repro-7f3cc41 7f3cc41 \
#       firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz firmware/patches/01-gcc12-extern-uint8.patch
#
# Umgebung:
#   FW_VERSION  ersetzt FIRMWARE_VERSION in Source/device.h (z. B. v22.4.s-thru1)
#   TOOLROOT  Toolchain-bin-Verzeichnis mit Schrägstrich am Ende
#             (Standard: /Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin/)
#   FORCE=1   vorhandenes firmware/builds/<name>/ überschreiben (sonst Abbruch)
#   JOBS      parallele make-Jobs (Standard: 8)
set -euo pipefail

if [ $# -lt 3 ]; then
  sed -n '2,25p' "$0" >&2
  exit 2
fi

NAME="$1"; COMMIT="$2"; LIBTAR="$3"; shift 3
PATCHES=("$@")

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$ROOT/firmware/OpenWare"
TREE="$ROOT/firmware/_work/$NAME"
OUT="$ROOT/firmware/builds/$NAME"
TOOLROOT="${TOOLROOT:-/Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin/}"
JOBS="${JOBS:-8}"
FLASH_MAX=131072

case "$NAME" in (*/*|""|.|..) echo "Ungültiger Name: $NAME" >&2; exit 2;; esac
[ -x "${TOOLROOT}arm-none-eabi-gcc" ] || { echo "Toolchain fehlt: ${TOOLROOT}arm-none-eabi-gcc" >&2; exit 2; }
[ -f "$LIBTAR" ] || { echo "Libraries-Tarball fehlt: $LIBTAR" >&2; exit 2; }
for p in "${PATCHES[@]+"${PATCHES[@]}"}"; do [ -f "$p" ] || { echo "Patch fehlt: $p" >&2; exit 2; }; done
if [ -e "$OUT" ] && [ "${FORCE:-0}" != 1 ]; then
  echo "$OUT existiert schon (FORCE=1 zum Überschreiben). Geflashte Builds nie überschreiben." >&2
  exit 2
fi

FULL="$(git -C "$REPO" rev-parse --verify "$COMMIT^{commit}")"
SHORT="${FULL:0:7}"

# 1. Quellbaum (nur unterhalb firmware/_work/ löschen)
rm -rf "$TREE"
mkdir -p "$TREE"
# .git*-Dateien (.gitmodules usw.) braucht der Build nicht, der Sandbox verbietet sie
git -C "$REPO" archive --format=tar "$FULL" | tar -x -C "$TREE" --exclude '.git*' --exclude '*/.git*'

# 2. Libraries
rm -rf "$TREE/Libraries"
mkdir -p "$TREE/Libraries"
tar -xzf "$LIBTAR" -C "$TREE/Libraries" --strip-components=1 --exclude '.git*' --exclude '*/.git*'

# 3. Patches
for p in "${PATCHES[@]+"${PATCHES[@]}"}"; do
  echo "== Patch $(basename "$p")"
  patch -d "$TREE" -p1 --forward --no-backup-if-mismatch < "$p"
done

# 3b. Versionsstring (Source/device.h), falls FW_VERSION gesetzt
if [ -n "${FW_VERSION:-}" ]; then
  case "$FW_VERSION" in (*[!A-Za-z0-9._-]*) echo "FW_VERSION nur [A-Za-z0-9._-]" >&2; exit 2;; esac
  grep -q '^#define FIRMWARE_VERSION "' "$TREE/Source/device.h" || { echo "FIRMWARE_VERSION nicht gefunden" >&2; exit 1; }
  sed -i '' "s/^#define FIRMWARE_VERSION \".*\"/#define FIRMWARE_VERSION \"$FW_VERSION\"/" "$TREE/Source/device.h"
fi

# 4. Build
LOG="$TREE/build.log"
echo "== make ($SHORT, $(basename "$LIBTAR"))"
make -C "$TREE/ACDC" -j"$JOBS" CONFIG=Release TOOLROOT="$TOOLROOT" \
  GIT_REVISION="$SHORT Release" all > "$LOG" 2>&1 || { tail -40 "$LOG" >&2; echo "Build fehlgeschlagen, Log: $LOG" >&2; exit 1; }

BIN="$TREE/ACDC/Build/ACDC.bin"
ELF="$TREE/ACDC/Build/ACDC.elf"
SIZE_BIN=$(stat -f %z "$BIN")
"${TOOLROOT}arm-none-eabi-size" "$ELF" | tee -a "$LOG"
if [ "$SIZE_BIN" -gt "$FLASH_MAX" ]; then
  echo "ACDC.bin ist $SIZE_BIN B > $FLASH_MAX B" >&2; exit 1
fi

# 5. Ablage
mkdir -p "$OUT"
cp "$BIN" "$ELF" "$LOG" "$OUT/"
[ -f "$TREE/ACDC/Build/ACDC.map" ] && cp "$TREE/ACDC/Build/ACDC.map" "$OUT/"
{
  echo "# Build $NAME"
  echo "datum:      $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "commit:     $FULL"
  echo "libraries:  $(basename "$LIBTAR") sha256 $(shasum -a 256 "$LIBTAR" | cut -d' ' -f1)"
  echo "toolchain:  $("${TOOLROOT}arm-none-eabi-gcc" --version | head -1)"
  echo "make:       CONFIG=Release GIT_REVISION=\"$SHORT Release\""
  echo "fw_version: ${FW_VERSION:-(unverändert)}"
  for p in "${PATCHES[@]+"${PATCHES[@]}"}"; do
    echo "patch:      $(basename "$p") sha256 $(shasum -a 256 "$p" | cut -d' ' -f1)"
  done
  echo "bin_size:   $SIZE_BIN"
  echo "bin_sha256: $(shasum -a 256 "$BIN" | cut -d' ' -f1)"
  echo "version:    $(strings -n 6 "$BIN" 2>/dev/null | grep -m1 '^AC/DC v' || echo '?')"
} > "$OUT/BUILD_INFO.txt"
cat "$OUT/BUILD_INFO.txt"
