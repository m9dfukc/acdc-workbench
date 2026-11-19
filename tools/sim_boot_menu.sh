#!/usr/bin/env bash
# Host test of the boot menu logic (patches 15 and 17): compiles the menu code of a build tree
# unchanged together with stubs for knobs, LEDs, storage and scheduler, and runs it
# against scripted knob movements (firmware/sim/boot_menu_sim.cpp). A tree with the LED mode
# (patch 17, knob 2) also runs the LED mode cases and a second program for what the main loop
# writes to the LEDs in each mode (firmware/sim/led_loop_sim.cpp).
#
# Usage:
#   tools/sim_boot_menu.sh [source tree]
# Default tree: firmware/_work/acdc1-build8-fx6a (left behind by tools/build_acdc.sh).
# Exit code 0 = all cases ok.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TREE="${1:-$ROOT/firmware/_work/acdc1-build8-fx6a}"
SRC="$TREE/ACDC/Core/Src/ACDC.cpp"
[ -f "$SRC" ] || { echo "Not found: $SRC" >&2; exit 2; }
WORK="$(mktemp -d "${TMPDIR:-/tmp}/bootmenu.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT
# Menü-Block: vom Kommentarkopf bis vor den nächsten Abschnitt
awk '/^\/\* --- Boot menu: choose the patch slot at power-on/{p=1} /^#ifdef USE_FAST_POW_RESOURCES/{p=0} p' "$SRC" > "$WORK/menu.inc"
[ -s "$WORK/menu.inc" ] || { echo "No boot menu block in $SRC" >&2; exit 2; }
cp "$ROOT/firmware/sim/boot_menu_sim.cpp" "$WORK/sim.cpp"
DEFS=""
grep -q ACDC_LED_RESOURCE "$WORK/menu.inc" && DEFS="-DACDC_SIM_LED_MODE"
c++ -std=c++17 -O1 -Wall -Wno-unused-function $DEFS -o "$WORK/sim" "$WORK/sim.cpp" 2> "$WORK/cc.log" \
  || { grep -v xcrun_db "$WORK/cc.log" >&2; echo "Compile failed" >&2; exit 1; }
STATUS=0
"$WORK/sim" || STATUS=1
# LED-Schleife (Patch 17): nur wenn der Baum den LED-Modus hat
if [ -n "$DEFS" ]; then
  awk '/^\/\* Input LEDs while the host records/{p=1} p && /^#else/{exit} p' "$SRC" > "$WORK/loop.inc"
  [ -s "$WORK/loop.inc" ] || { echo "No LED loop block in $SRC" >&2; exit 2; }
  cp "$ROOT/firmware/sim/led_loop_sim.cpp" "$WORK/loop.cpp"
  c++ -std=c++17 -O1 -Wall -Wno-unused-function -o "$WORK/loop" "$WORK/loop.cpp" 2> "$WORK/cc.log" \
    || { grep -v xcrun_db "$WORK/cc.log" >&2; echo "Compile failed (LED loop)" >&2; exit 1; }
  echo "== LED loop"
  "$WORK/loop" || STATUS=1
fi
exit $STATUS
