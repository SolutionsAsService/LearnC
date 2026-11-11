# Critic: Evidence (Cairo), R4

**Anchor used:** *How Charts Lie*: a figure is honest only if a reader following the stated method gets the same one.

**Observed:** Scratch rebuild: 41 programs, 22 pages, `site/` byte-identical, stdout identical; 0 warnings, 0 non-zero exits. All 6 QUOTED_OUTPUTS are whole lines of stdout. measure.cjs: 60 shots, min font 12 px, no overflow, hero bottom 707/768 in both schemes. Live About shows `sudo apt install gcc g++ clang mono-mcs`; apt-cache: clang-18 Depends libobjc-13-dev, which holds objc/runtime.h. 41 Download links (12+20+4+3+2). Downloaded 08_structs.c, pasted the command: exit 0, "Age: 31", "56 bytes".

**Findings**
1. [claim] R3 F3, F4, F5 resolved (build.py:764, 766; evidence).
2. [defect] rosetta.html sum.m, pasted verbatim beside the download: `no such file: '../Root.m'`. "../Root.m, from the same folder" (build.py:246) gives no link, and the needed `Root.h` is never named; with both placed in the parent it runs (55).
3. [defect] objc.html 01_messages.m with Root.m, as instructed: `'Root.h' file not found`.
4. [premise] "15 pages" measured of 22; lessons 02–06, 10, 12 unmeasured.

**Verdict:** OBJECT (F2, F3)

**Requested change:** F2/F3: link Root.m and Root.h, and say where to save them (parent folder for Rosetta). F4: measure all 22 or say 15 of 22.
