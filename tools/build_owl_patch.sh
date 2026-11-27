#!/usr/bin/env bash
# Build one C++ OWL patch with OwlProgram for the AC/DC and write the upload SysEx.
#
# Steps:
#   1. Build the OwlProgram libraries once per platform (Libraries/libowlprg.a, libdaisysp.a)
#   2. make patch (PATCHIN/PATCHOUT = 4) into a build folder of its own
#   3. Check the binary with tools/owl_write.py --info and write <name>.syx
#   4. Copy patch.bin, <name>.syx and BUILD_INFO.txt to <out>/<name>/
#
# Uploads nothing. Upload: tools/owl_write.py <out>/<name>/<name>.syx --run | --store N --yes
#
# Usage:
#   tools/build_owl_patch.sh <name> <class> <file.hpp> [header ...]
# Example:
#   tools/build_owl_patch.sh TapeDelay TapeDelayPatch TapeDelayPatch.hpp
#   tools/build_owl_patch.sh Grainz GrainzPatch GrainzPatch.hpp SmoothValue.h
#   LIMIT=1 tools/build_owl_patch.sh Grainz GrainzPatch GrainzPatch.hpp SmoothValue.h
#   SRC=owl/patches/tanh3 tools/build_owl_patch.sh Tanh3 Tanh3Patch Tanh3Patch.hpp
# Extra headers are included before the patch file. That repairs a source with a
# missing include without touching it.
#
# Environment:
#   SDK       OwlProgram tree (default: owl/vendor/OwlProgram). Its compile.mk should use the
#             flags of OwlProgram develop (no -fno-builtin/-ffreestanding/-mtune, D92), the
#             script warns otherwise and writes the compile.mk checksum to BUILD_INFO.txt
#   SRC       folder with the patch sources (default: owl/patches-private)
#   OUT       output base folder (default: owl/vendor/builds)
#   PLATFORM  OWL3 (default: Cortex-M7 code, FPU fpv5-d16) or OWL2 (Cortex-M4 code that
#             runs on every OWL device, like the patch library)
#   LINK      patchram (default: links to 0x2000c000 like the patch library, at most
#             80 KB on the AC/DC) or plusram (0x24000000, up to 512 KB, needs PLATFORM=OWL3)
#   LIMIT     1 = wrap the patch in AcdcLimited<> (owl/include/AcdcOutput.h): limiter on the
#             audio outputs 1/2. The patch source stays untouched.
#   TOOLROOT  toolchain bin directory with a trailing slash
#             (default: /Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin/)
#   JOBS      parallel make jobs for the libraries (default: 8)
#   WORK      folder for the throwaway build trees (default: owl/vendor/_work). A separate
#             one keeps test builds (other SDK or flags) from replacing the regular trees
set -euo pipefail

if [ $# -lt 3 ]; then
  sed -n '2,38p' "$0" >&2
  exit 2
fi

NAME="$1"; CLASS="$2"; FILE="$3"; shift 3
PRELUDE=("$@")

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SDK="$(cd "${SDK:-$ROOT/owl/vendor/OwlProgram}" && pwd)"
SRC="$(cd "${SRC:-$ROOT/owl/patches-private}" && pwd)"
OUT="${OUT:-$ROOT/owl/vendor/builds}"
PLATFORM="${PLATFORM:-OWL3}"
LINK="${LINK:-patchram}"
LIMIT="${LIMIT:-0}"
case "$LINK" in
  patchram) LDSCRIPT="$SDK/Source/owl2.ld";;
  plusram)  LDSCRIPT="$SDK/Source/owl3.ld"; [ "$PLATFORM" = OWL3 ] || { echo "LINK=plusram needs PLATFORM=OWL3" >&2; exit 2; };;
  *) echo "LINK must be patchram or plusram" >&2; exit 2;;
esac
export TOOLROOT="${TOOLROOT:-/Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin/}"
JOBS="${JOBS:-8}"

case "$NAME" in (*/*|""|.|..) echo "Invalid name: $NAME" >&2; exit 2;; esac
[ -x "${TOOLROOT}arm-none-eabi-gcc" ] || { echo "Toolchain not found: ${TOOLROOT}arm-none-eabi-gcc" >&2; exit 2; }
[ -f "$SDK/compile.mk" ] || { echo "OwlProgram not found: $SDK" >&2; exit 2; }
[ -f "$SDK/Libraries/DaisySP/Source/daisysp.h" ] || { echo "DaisySP sources are missing in $SDK/Libraries/DaisySP" >&2; exit 2; }
[ -f "$SRC/$FILE" ] || { echo "Patch file not found: $SRC/$FILE" >&2; exit 2; }
[ "$LIMIT" != 1 ] || [ -f "$ROOT/owl/include/AcdcOutput.h" ] || { echo "owl/include/AcdcOutput.h missing: git submodule update --init owl" >&2; exit 2; }

WORK="${WORK:-$ROOT/owl/vendor/_work}"
BUILD="$WORK/$NAME-$PLATFORM-$LINK"
LIBBUILD="$WORK/_libs-$PLATFORM"
STAMP="$SDK/Libraries/.platform"
# Flags des SDK: compile.mk ist lokal geändert (Flags aus OwlProgram-develop, D92). Die Prüfsumme
# kommt in den Stempel der Bibliotheken (andere Flags = neu bauen) und in BUILD_INFO.txt
MKSHA="$(shasum -a 256 "$SDK/compile.mk" | cut -d' ' -f1)"
if grep -Eq '^[^#]*(-fno-builtin|-ffreestanding)' "$SDK/compile.mk"; then
  BUILTINS="off (-fno-builtin/-ffreestanding in compile.mk)"
  echo "Warning: $SDK/compile.mk still sets -fno-builtin/-ffreestanding: fabsf, sqrtf etc. become newlib calls (D92)" >&2
else
  BUILTINS="on"
fi

cd "$SDK"

# 1. Bibliotheken: liegen im SDK-Baum, deshalb je Plattform und je compile.mk neu bauen
if [ ! -f Libraries/libowlprg.a ] || [ ! -f Libraries/libdaisysp.a ] || [ "$(cat "$STAMP" 2>/dev/null)" != "$PLATFORM $MKSHA" ]; then
  echo "Building the OwlProgram libraries for $PLATFORM"
  rm -rf "$LIBBUILD" Libraries/libowlprg.a Libraries/libdaisysp.a
  mkdir -p "$LIBBUILD"
  make -s -j"$JOBS" -f compile.mk libs PLATFORM="$PLATFORM" CONFIG=Release BUILD="$LIBBUILD" \
       BUILDROOT=. PATCHNAME=libs PATCHSOURCE=./PatchSource 2>&1 | grep -v xcrun_db || true
  [ -f Libraries/libowlprg.a ] && [ -f Libraries/libdaisysp.a ] || { echo "Library build failed" >&2; exit 1; }
  echo "$PLATFORM $MKSHA" > "$STAMP"
fi

# 2. Patch. Mit Zusatz-Headern bindet eine Hülle im Build-Ordner erst diese, dann die Patch-Datei ein
rm -rf "$BUILD"
mkdir -p "$BUILD/Source"
PATCHFILE="$FILE"
PATCHCLASS="$CLASS"
if [ ${#PRELUDE[@]} -gt 0 ] || [ "$LIMIT" = 1 ]; then
  PATCHFILE="${NAME}Wrap.hpp"
  {
    for h in "${PRELUDE[@]+"${PRELUDE[@]}"}"; do echo "#include \"$h\""; done
    echo "#include \"$FILE\""
    if [ "$LIMIT" = 1 ]; then
      PATCHCLASS="${NAME}AcdcPatch"
      echo "#include \"$ROOT/owl/include/AcdcOutput.h\""
      echo "class $PATCHCLASS : public AcdcLimited<$CLASS> {};"
    fi
  } > "$BUILD/Source/$PATCHFILE"
  [ "$LIMIT" = 1 ] && PATCHCLASS="${NAME}AcdcPatch"
fi
make PATCHNAME="$NAME" PATCHCLASS="$PATCHCLASS" PATCHFILE="$PATCHFILE" PATCHSOURCE="$SRC" \
     PATCHIN=4 PATCHOUT=4 PLATFORM="$PLATFORM" LDSCRIPT="$LDSCRIPT" CONFIG=Release BUILD="$BUILD" patch \
     > "$BUILD/build.log" 2>&1 || { grep -v xcrun_db "$BUILD/build.log" | tail -30 >&2; echo "Patch build failed" >&2; exit 1; }
[ -f "$BUILD/patch.bin" ] || { echo "No patch.bin" >&2; exit 1; }

# 3. Prüfen und SysEx schreiben
cd "$ROOT"
DEST="$OUT/$NAME"
mkdir -p "$DEST"
python3 tools/owl_write.py "$BUILD/patch.bin" --info
python3 tools/owl_write.py "$BUILD/patch.bin" --syx-out "$DEST/$NAME.syx" > /dev/null
cp "$BUILD/patch.bin" "$DEST/patch.bin"
grep -v xcrun_db "$BUILD/build.log" > "$DEST/build.log" || true

# 4. BUILD_INFO
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
{
  echo "# Patch $NAME"
  echo "datum:      $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "class:      $CLASS"
  echo "file:       $FILE sha256 $(sha "$SRC/$FILE")"
  [ ${#PRELUDE[@]} -gt 0 ] && echo "prelude:    ${PRELUDE[*]}"
  echo "source:     $SRC"
  echo "sdk:        $SDK"
  echo "sdk_flags:  compile.mk sha256 $MKSHA, builtins $BUILTINS"
  echo "platform:   $PLATFORM, link $LINK ($(basename "$LDSCRIPT"))"
  [ "$LIMIT" = 1 ] && echo "limiter:    owl/include/AcdcOutput.h sha256 $(sha "$ROOT/owl/include/AcdcOutput.h")"
  echo "toolchain:  $("${TOOLROOT}arm-none-eabi-gcc" --version | head -1)"
  echo "size:       $("${TOOLROOT}arm-none-eabi-size" "$BUILD/patch.elf" | tail -1 | awk '{print "text " $1 " data " $2 " bss " $3}')"
  echo "bin_size:   $(wc -c < "$DEST/patch.bin" | tr -d ' ')"
  echo "bin_sha256: $(sha "$DEST/patch.bin")"
  echo "syx_sha256: $(sha "$DEST/$NAME.syx")"
} > "$DEST/BUILD_INFO.txt"
echo "Built $DEST/$NAME.syx"
