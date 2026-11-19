#!/usr/bin/env bash
# Host test of the project's own OWL patch code (owl/Tanh3Patch.hpp, owl/AcdcOutput.h,
# owl/AcdcInput.h, owl/schliere/: all Schliere variants): compiles it unchanged against a minimal stand-in for the
# OwlProgram API (owl/test/Patch.h).
#   dsp_test.cpp       Tanh3 and limiter: levels, saturation, antialiasing, mix, CV
#   schliere_test.cpp  Schliere: transfer function against the textbook allpass, group
#                      delay, notches, feedback, DC, CV scaling, stability
#   blockrate_test.cpp Block-rate canceller: learning, DC, slow CV, loud signals, a tone at fs/8
#   ledtest_test.cpp   LED test patch (owl/test/SchliereLedTestPatch.hpp): schedule of the LED states
#   ledpath_test.cpp   LED path test patch (owl/test/SchliereLedPathPatch.hpp): schedule, outputs per
#                      phase, the measurement at the inputs
#
# Usage: tools/test_owl_dsp.sh        Exit code 0 = all cases ok.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/owldsp.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT
STATUS=0
for T in dsp_test schliere_test blockrate_test ledtest_test ledpath_test; do
  c++ -std=c++17 -O1 -Wall -I"$ROOT/owl/test" -I"$ROOT/owl" -I"$ROOT/owl/schliere" -o "$WORK/$T" "$ROOT/owl/test/$T.cpp" 2> "$WORK/cc.log" \
    || { grep -v xcrun_db "$WORK/cc.log" >&2; echo "Compile failed: $T" >&2; exit 1; }
  echo "== $T"
  "$WORK/$T" || STATUS=1
done
exit $STATUS
