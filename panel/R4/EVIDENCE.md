# R4 evidence: LearnC site after the R3 fixes (move M11)

The site is served at http://localhost:8765/. Source: /home/user/learnc. Read your own R3 report in `panel/R3/` and the R3 resolution table in `DESIGN-LOG.md` ("Panel, WHOLE, round R3"). Then judge the site as it is now.

## Measured after the last edit
- Build: 41 programs, 0 warnings, 0 failures. The output checks (whole-line) pass.
- Pages measured: 15 pages × 1280x800 and 375x812 × light and dark. Horizontal overflow: none. Smallest text: 12 px (lessons 08 and 11 are now included).
- Hero bottom: 707 px at 1280x800 and 768 px at 375x812. The phone start link sits below the fold (Cairo measured y 922–965). It is DEFERRED; cell 01 is the first action above the fold.
- Downloads: /examples/<lang>/<file> is served (HTTP 200). Each program's page links to its own file.
- About › Getting a compiler: the Linux line is `sudo apt install gcc g++ clang mono-mcs`. `dpkg -S` puts objc/runtime.h in libobjc-13-dev, which clang depends on.
