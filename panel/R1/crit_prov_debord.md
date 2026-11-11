# R1 · Critic: Provocateur (Debord)

**Anchor used:** *Society of the Spectacle*, Thesis 1: what was lived "moves away into a representation". Test: is each sentence a trace of the build, or an image of one?

**Observed:** The hero's "hello N lines · ran ✓" and HolyC's "not run" are computed in build.py (`lines_of`, `ran()`), so the hero is a claim, not a brochure. The prose outruns the build at build.py:196, 436, 441, 472 and 625, in the csharp note, and in lesson 09.

**Findings:**
- F1 [claim] "Nothing here is typed by hand" (build.py:436). content.py line 1 says all the prose is hand-written. Only the outputs are untouched.
- F2 [defect] "(0 warnings)" on c/index (build.py:472) is a literal, not read from runs.json. A hand-typed figure sits under that promise.
- F3 [claim] "every warning switched on". The flags are -Wall -Wextra(-Wpedantic). C++ and ObjC have no -Wconversion, and lesson 09 says -Wall -Wextra misses the fgetc bug.
- F4 [defect] The index and about meta descriptions say "every example compiled and run" (build.py:441, 625). The 7 HolyC files were not.
- F5 [claim] Footer "compiled and run when the site was built" (build.py:196). run_all reuses cached runs.json under --no-run or when a toolchain is missing, and never prunes stale entries.
- F6 [claim] "Modern .NET runs them unchanged" is untested: only Mono ran them. "-Wconversion does [warn]" (lesson 09) is not in R0 evidence. The ARM failure was simulated with -funsigned-char on x86.
- F7 [premise] Evidence says the hero reads "not run here". It reads "not run".

**Verdict:** OBJECT

**Requested change:**
- F1: "No output here is typed by hand".
- F2: interpolate the count from runs.
- F3: name the flags.
- F4: "every C, C++, Objective-C and C# example".
- F5: print the build date and cache status, and prune stale entries.
- F6: cut the .NET line or run it, record a -Wconversion run, and say "with -funsigned-char, as on ARM".
- F7: fix the evidence.
