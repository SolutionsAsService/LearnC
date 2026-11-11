# Critic: Evidence (Cairo), R3

**Anchor used:** *How Charts Lie*: a figure is honest only if a reader can get the same one from the stated source and method.

**Observed:** In a scratch copy, a full build gives 41 programs and 22 pages, identical to `site/` and `runs.json`. All 41 commands give 0 warnings and recorded stdout. The 7 printed Objective-C commands, run verbatim: exit 0, outputs match. 08: "56 bytes" and 30 → 31 match stdout. 11: 0..81 comes from `i*i` (stdout shows only `squares[9] = 81`). Rosetta 39/37/68/42/33, hello 5/4/5/6/2 and c/index 7…7 match `grep -cv '^\s*$'`. Playwright, both schemes: hero bottom 707 (1280x800) and 768 (375x812), no overflow.

**Findings**
- F1 [claim] R2 F7 resolved: the printed ObjC command is the one that runs (build.py:60 = 76–77).
- F2 [claim] R2 F8 resolved: the hero key and c/index say what "lines" counts.
- F3 [defect] About › Getting a compiler (build.py:762): `apt install gcc g++ mono-mcs` "covers … Objective-C (the GNU runtime ships with gcc)". False here: the command needs `clang`, and libobjc-13-dev comes from clang-18, not gcc-13 (apt-cache depends).
- F4 [premise] macOS line unverified: Apple clang with `-fobjc-runtime=gcc -lobjc` and `gcc -print-file-name` is untested.
- F5 [claim] Evidence says the 375 start link is at y 885; I measure 922–965.
- F6 [premise] At 375x667 the hero bottom is 768: still DEFERRED.

**Verdict:** OBJECT (F3)

**Requested change:** F3: `sudo apt install gcc g++ clang mono-mcs` and drop the parenthesis. F4: say ObjC was verified on Linux only. F5: correct the evidence.
