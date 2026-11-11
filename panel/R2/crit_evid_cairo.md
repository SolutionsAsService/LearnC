# Critic: Evidence (Cairo), R2

**Anchor used:** *How Charts Lie*: a figure is honest only if the reader can get the same one from the stated source and method.

**Observed:** I re-ran all 41 runs.json commands on a copy of examples/. C, C++ and C# give 0 warnings, exit 0 and the same stdout. The Rosetta cells and totals (39/37/68/42/33), the hero hello counts (5/4/5/6/2), Root.h+.m = 24, the c/index lesson counts (7…7) and the 7 HolyC files all match `grep -cv '^\s*$'`. I reproduced the c/09 bug: `a\xffb` gives "a", -funsigned-char loops on \377, and only -Wconversion warns. In Playwright, the hero SVG bottom is 707 at 1280x800 and 768 at 375x812, in both schemes, with no horizontal overflow. The narrow arrows end at C's borders (x=347, y=199) through gutters, and NULL is drawn.

**Findings**
- F1 [claim] R1 F1 is resolved. The home page and About name the flags per language, and they match runs.json.
- F2 [claim] R1 F2 is resolved. The caption says "comments included" and "Root.h and Root.m (24 lines)", and 3 programs use Root, as stated.
- F3 [premise] R1 F3 stays DEFERRED. At 375x812 the key (y 776–869) and the start link (885–928) fall below the fold. At 375x667, C#, HolyC and rosetta[5] are below it too.
- F4/F5/F6 [claim] Resolved on the live page.
- F7 [defect] The printed Objective-C command is not reproducible. Run as shown, all 7 ObjC programs fail with `objc/runtime.h` not found. The build adds `-I/usr/lib/gcc/x86_64-linux-gnu/13/include -L…` (build.py:76–77), but build.py:60 prints the command without them. With those flags, all 7 pass with 0 warnings.
- F8 [claim] The hero's "hello 5 lines" counts comments (ObjC 1 of 5, HolyC 1 of 2), and the hero has no caption saying so. The c/index "N lines" has none either.

**Verdict:** OBJECT (F7 only; everything else passes)

**Requested change:** F7: print the command the build actually ran, or add the -I/-L note to the ObjC command. F8: add "non-blank lines, comments included" to the hero key and to c/index. F3: none for this round.
