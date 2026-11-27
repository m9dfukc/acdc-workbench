# Licenses

This repository mixes three kinds of material. Each has its own license.

| Path | License | Text |
|---|---|---|
| `tools/`, `analysis/`, `firmware/itcm-prep/` | MIT | [LICENSES/MIT.txt](LICENSES/MIT.txt) |
| `firmware/patches/`, patch files in `firmware/builds/` | GPL-2.0, the license of OpenWare, because the patches are derived from its source | [LICENSES/GPL-2.0.txt](LICENSES/GPL-2.0.txt) |
| `docs/`, `README*.md`, `TODO.md`, `CLAUDE.md`, `recordings/manifest.toml`, `reports/`, logs and reports in `firmware/builds/` and `firmware/flashlog/` | CC BY 4.0 | [LICENSES/CC-BY-4.0.txt](LICENSES/CC-BY-4.0.txt) |

## Third-party material

- `firmware/OpenWare/` is a git submodule (a fork of [RebelTechnology/OpenWare](https://github.com/RebelTechnology/OpenWare)) and keeps its own license, GPL-2.0.
- `owl/` is a git submodule ([m9dfukc/acdc-patches](https://github.com/m9dfukc/acdc-patches), the own OWL patches) under GPL-3.0-or-later, the license of OwlProgram, which the patches are built against.
- `.claude/skills/` comes from [mattpocock/skills](https://github.com/mattpocock/skills) under the MIT license: [LICENSES/MIT-mattpocock-skills.txt](LICENSES/MIT-mattpocock-skills.txt).
- `docs/research/` paraphrases and quotes public forum posts and repositories. Each note links its sources. The quotes remain the work of their authors.
