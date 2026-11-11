# R1 evidence: LearnC site, whole artifact (after moves M1 to M4)

The site is served at http://localhost:8765/ (static, from `site/`). Source: `_src/build.py`, `_src/content.py`, `site/css/site.css`, and `examples/`.
Rebuild with `python3 _src/build.py`. That compiles and runs every example, writes `_src/runs.json`, and exits 1 on a dead link or a warning.
Measure with `node _src/measure.cjs http://localhost:8765/ panel/shots`. That writes screenshots and `panel/shots/measure.json`.

## Pages (22)
index; c/index plus 12 lessons (c/01-hello ... c/12-sum); cpp; objc; csharp; holyc; rosetta; family; about; 404.

## Build result (last run)
- 41 programs compiled and run, with 0 warnings and 0 non-zero exits.
- Toolchains: c: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0; cpp: g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0; objc: Ubuntu clang version 18.1.3 (1ubuntu1); csharp: Mono JIT compiler version 6.8.0.105 (Debian 6.8.0.105+dfsg-3.6ubuntu2 Sun Mar 31 02:55:28 UTC 2024)
- HolyC: 7 files, not compiled (no compiler; building one from external code was refused in this session). Each is labelled "not run here" on the page and in the hero.
- Dead local links: 0 (the build checks them).

## Measurements (12 pages × 1280x800 and 375x812 × light and dark)
- Horizontal overflow: none on any page, size or scheme.
- Smallest rendered text: 12 px (SVG text scaled by its viewBox is included).
- Text column (`.wrap`) at 1280: 664 px. That is 80 cells of JetBrains Mono at 13.12 px (0.6 em advance) plus 2rem padding and a 2px border.
- Landing hero (the visible pointer-diagram SVG) bounding box:
  - light 1280x800: top 137, bottom 707, width 1248
  - light 375x812: top 135, bottom 745, width 343
  - dark 1280x800: top 137, bottom 707, width 1248
  - dark 375x812: top 135, bottom 745, width 343
- Hero inventory: 5 language structs (C, C++, Objective-C, C#, HolyC), ancestors BCPL and B linking to Family, a `lessons[12]` array (each cell links to a lesson), and a `rosetta[5]` array (each cell links to a program on the Rosetta page). Every topic page is reachable from the hero.
- Hero figures: "hello N lines" is the count of non-blank lines in `examples/<lang>/rosetta/hello.*`; "ran ✓" means it compiled and exited 0 in this build.

## Screenshots (open them; all are in panel/shots/)
index.html-1280-light.png, index.html-1280-dark.png, index.html-375-light.png, index.html-375-dark.png, c_07-pointers.html-1280-light.png, c_09-file-io.html-375-light.png, rosetta.html-1280-light.png (full page), family.html-1280-light.png, holyc.html-375-light.png, objc.html-1280-light.png, about.html-1280-light.png.

## Claims that state a limit or a refusal (file:line in _src/content.py or build.py)
- HolyC is "not run here": content.py PAGES['holyc']['note']; build.py code_block (the `lang == "holyc"` branch).
- C# examples avoid syntax newer than about C# 7 because of Mono mcs: content.py PAGES['csharp']['note'].
- Objective-C uses a stand-in root class because Foundation is absent: examples/objc/Root.h comment; content.py PAGES['objc'] Root.h note.
- The two read_file.c failure modes: measured in panel/R0/EVIDENCE.md and taught on c/09-file-io.html.
