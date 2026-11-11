# Critic: Evidence (Cairo), R1

**Anchor used:** *How Charts Lie*: a chart lies through bad data, bad scale or omission, and every figure must be reproducible.

**Observed:** `build.py --no-run` exit 0, 22 pages. runs.json has 41 runs, all exit 0 with 0 warnings (17 C, 9 C++, 7 ObjC, 8 C#), plus 7 HolyC files. Recounting the Rosetta table with `grep -cv '^\s*$'`, every cell and total matches (39/37/68/42/33). The hero hello counts (5/4/5/6/2) match. The lesson figures match: Collatz 111, 56 bytes, 7 chars in 8 bytes. In Playwright, the hero section bottom is 734 at 1280x800 and 788 at 375x812 in both schemes (the SVG bottoms are 707 and 745). The smallest SVG text is 12.4 px. I checked about 40 dates in content.py and found none wrong.

**Findings**
- F1 [claim] "every warning switched on" (index) is false. C++ and ObjC do not get `-Wconversion`, the flag c/09 credits with catching the bug (runs.json commands).
- F2 [defect] The Rosetta ObjC total of 68 omits Root.h and Root.m (26 lines), which 4 of the 5 programs use. The counts include comments, so HolyC's "2 lines" is half comment.
- F3 [premise] The 375x812 pass has 24 px to spare, and 812 is the device height. Safari shows about 660 px, so on a real phone the rosetta[5] row and the key fall below the fold.
- F4 [defect] On the 375 hero, the child arrows end on lesson cells 3, 5, 8 and 11, which reads as "C++ points to lesson 3". The alt text says "BCPL to NULL", but no NULL is drawn.
- F5 [claim] content.py:18 puts ObjC "1984 · Stepstone", but :176 says the company was still PPI in 1984.
- F6 [claim] c/09 says "We measured" the ARM failure, but R0 measured it with `-funsigned-char` on x86.

**Verdict:** OBJECT (F1 and F2 mislead; F3 to F6 are minor)

**Requested change:** F1: list the flags per language. F2: add a "+26 lines Root.h/.m" note and caption the table "comments included". F3: also measure at 375x667. F4: end the arrows on the C header, and draw or drop NULL. F5: "PPI (later Stepstone)". F6: "simulated with -funsigned-char".
