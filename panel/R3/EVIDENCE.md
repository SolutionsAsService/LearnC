# R3 evidence: LearnC site after the R2 fixes (moves M9, M10)

The site is served at http://localhost:8765/. Source: `_src/build.py`, `_src/content.py`, `site/css/site.css`. Rebuild with `python3 _src/build.py --no-run`.
Read your own R2 report in `panel/R2/` and the R2 resolution table in `DESIGN-LOG.md` (section "Panel, WHOLE, round R2"). Then judge the site as it stands now.

## Build (re-run with compilers after the flag change)
- 41 programs, 0 warnings, 0 non-zero exits. The flags are now: C `-std=c17 -Wall -Wextra -Wpedantic -Wstrict-prototypes -Wconversion`; C++ `-std=c++20 -Wall -Wextra -Wpedantic -Wconversion`; Objective-C `-Wall -Wextra -Wpedantic -Wconversion`; C# `mcs -warn:4`.
- `_src/runs.json` records a `built` date per language. Footer and About print it.

## Measured (panel/R2/measure-hero.json, panel/shots/measure.json; 12 pages × 2 sizes × 2 schemes)
- Horizontal overflow: none. Smallest rendered text: 12 px.
- Hero bottom: 707 px at 1280x800; 768 px at 375x812 (1280: start link at y 83–127, in the head; 375: start link under the hero at y 885).
- At 375x667 the hero bottom is 768, below the 667 fold (recorded as DEFERRED in the log).
- Smallest hero cell: 43.2×47.8 px at 1280; 37.2×28.6 px at 375 (lesson cells are now outside the C box).
- Nav items off-screen at 375: 0 (the nav wraps to two rows).
- Hero link names (examples): "C lesson 1: Hello, World", "C: year 1972, Bell Labs, by Dennis Ritchie. Overview and lessons".
- Lesson prose width at 1280: 551 px at 19 px Newsreader (cap 29em).

## Screenshots (panel/shots/, refreshed after the last edit)
index.html-1280-light.png, index.html-1280-dark.png, index.html-375-light.png, index.html-375-dark.png, c_07-pointers.html-1280-light.png, holyc.html-375-light.png, rosetta.html-1280-light.png, family.html-1280-light.png, about.html-1280-light.png, c_01-hello.html-375-light.png.

## Changes since R2 (measured after the last edit)
- Objective-C command printed and run: `-I"$(gcc -print-file-name=include)" … -L"$(gcc -print-file-name=)"`; run verbatim in a copy of examples/objc: 01_messages and rosetta/point printed the recorded output.
- The build now fails if Rosetta "Prints X." prose or `QUOTED_OUTPUTS` (content.py) disagree with the real output. It passes.
- New drawings: c/index (C's struct → B), c/08-structs, c/11-malloc. Drawings sit above the code on 07, 08, 11.
- Rosetta: lines identical to the C version are dimmed (class `same`).
- Language pages: kicker removed; struct box + one-line key.
- About › Getting a compiler (#setup), linked under every command.
- Focus: `.frame` rect drawn last in every node; 8px ink stroke on focus.
- Overflow: none on 13 pages × 2 sizes × 2 schemes; smallest text 12 px; hero bottom 707 (1280x800) and 768 (375x812).
