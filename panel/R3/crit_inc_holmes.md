# R3: Inclusion (Holmes)

**Anchor used:** Holmes, *Mismatch*. Fixing a mismatch for one person extends to many.

**Observed (aria snapshots at 375×812, plus HTML):**
- All five R2 fixes landed:
  - lesson 03 has a forward gloss;
  - lesson 02 glosses the % codes;
  - About #setup is linked under every command;
  - language pages have no kicker and carry a struct key.
- The drawings on lessons 08 and 11 have plain-words names.
- Lesson 07's three drawings are named by their code captions (`aria-labelledby="m1…m3"`). A screen reader hears "int *ptr = &num;" three times, never "ptr points to num". M10 promised plain-words titles.
- The link "Getting one takes one command" is wrong for Windows, which needs two.
- About says "run it in the folder that holds the file". No page offers the .c file or says to save it and `cd` there.
- Lesson 03 leaves `static` and `%s` unglossed.

**Findings:**
- F1 [defect] Lesson 07's drawings have code names, not plain words.
- F2 [defect] A newcomer has no path from the page to a file on disk.
- F3 [claim] "One command" is false on Windows.
- F4 [claim] Lesson 03 leaves `static` and `%s` unglossed.

**Verdict:** OBJECT. The objection is narrow: R2 is resolved.

**Requested change:**
- F1: plain-words img names, e.g. "ptr holds num's address; num is 10".
- F2: a download link for each program, and "save as NAME.c, then cd to its folder".
- F3: "a command or two".
- F4: one more clause in the gloss.
