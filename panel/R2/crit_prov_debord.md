# R2 · Critic: Provocateur (Debord)

**Anchor used:** *The Society of the Spectacle*, Thesis 1 (the lived "moves away into a representation"). Test: does each sentence trace back to the build, or only look as if it does?

**Observed:** runs.json holds 41 entries, 0 warnings and 0 failures, and it has no stale keys. There are 7 .HC files. The home page's "{n_ran}/{n_warn}/{n_fail}/{n_hc}", c/index's "{c_warn}", About's flags table and the footer's `{BUILT}` (the earliest per-language date) are all interpolated. I reproduced lesson 09 with gcc 13: `-Wall -Wextra` gives no warning, `-Wconversion` warns "conversion from 'int' to 'char' may change value", the input `a\xffb` prints only "a", and `-funsigned-char` prints \377 in a loop. Every hero box and cell is inside an `<a>`.

**Findings:**
- F1–F6 (R1) resolved: "No output here is typed by hand", the computed warning count, the named flags, the narrowed meta descriptions, a dated footer with the cache explained on About, the .NET line cut, and "simulated here with -funsigned-char".
- F7 (R1) is moot: R2 evidence does not repeat it.
- F8 [claim] Prose that quotes outputs is typed by hand and the build never checks it: "Prints 55.", "Prints 5.0.", "Prints retniop." (content.py:146–149) and '"C++" beats "C"' (content.py:166). Today these match runs.json. But they sit under the heading "No output here is typed by hand", and nothing stops them drifting from the real output.
- F9 [claim] (minor) Stale entries are pruned only for a language that is re-run. Under `--no-run`, a deleted example would still be counted in "41". About states this rule, so this is disclosed and not hidden.

**Verdict:** PASS

**Requested change:**
- F8: have build.py check each "Prints X" against runs.json, or interpolate it from runs.json.
- F9: none.
