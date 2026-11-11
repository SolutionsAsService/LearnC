# R0 — Critic: Provocateur (Debord)

**Anchor used:** *The Society of the Spectacle*, Thesis 1 (what was lived "has moved away into a representation"). README is the image; the files are the lived thing.

**Observed:** README.md (17 lines, at f830dbe); CONTRIBUTING.md; 9 `.c` files; EVIDENCE.md table and read_file.c bug.

**Findings:**
- F1 [claim] README L3 "Each folder contains a set of examples": arrays/, pointers/, structs/, file_io/ hold one file each.
- F2 [claim] README L8 lists `functions/`; no such folder (evidence says L9; it is L8). file_io/ is real but unlisted.
- F3 [defect] README L13 promises "How to Compile and Run"; the file stops at `cd basic_concepts` with an unclosed fence. No compile command exists.
- F4 [defect] read_file.c L11-12 `char ch` with `fgetc`: infinite loop on unsigned-char targets, early stop on 0xFF (evidence); `example.txt` absent, so it only ever prints "Could not open the file."
- F5 [defect] pointers_example.c L10-11 pass `int *` to `%p`; `-Wpedantic` warns (I measured); evidence's "0 warnings" holds only for `-Wall -Wextra`.
- F6 [claim] CONTRIBUTING invites "data corrections", "new features", "Screenshots", "existing tests still pass": no data, no features, no tests.
- F7 [premise] The brief's "C and its family (C++, Objective-C, C#, HolyC)": nothing here backs any of the four. "LearnC" already announces more than nine toy programs teach.

**Verdict:** OBJECT

**Requested change:**
- F1: say "one example per folder" or add examples.
- F2: list the folders `ls` shows.
- F3: finish the section with the exact gcc line and printed output.
- F4: `int ch`; ship example.txt.
- F5: cast to `(void *)`; compile with `-Wpedantic`.
- F6: cut every clause the repo cannot honour.
- F7: no page may name a language until a compiled, run example for it exists.
