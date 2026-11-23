#!/usr/bin/env bash
# Host test of the project's own OWL patch code. The code and the test runner live in the
# submodule owl/ (m9dfukc/acdc-patches): tanh3/Tanh3Patch.hpp, AcdcOutput.h, AcdcInput.h, schliere/
# (all Schliere variants) and the two LED measurement patches in owl/test/. This script only
# calls owl/test/run.sh, see there for the test cases.
#
# Usage: tools/test_owl_dsp.sh        Exit code 0 = all cases ok.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RUN="$ROOT/owl/test/run.sh"
[ -x "$RUN" ] || { echo "Submodule owl/ is missing: git submodule update --init owl" >&2; exit 2; }
exec "$RUN" "$@"
