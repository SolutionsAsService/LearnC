# R2: Inclusion (Holmes)

**Anchor used:** Holmes, *Mismatch*. Fixing a mismatch for one person (a newcomer, a screen-reader user, a phone user) extends to many.

**Observed (aria snapshots, 375×812):**
- All six R1 fixes landed:
  - the hero is `group "The C family as a pointer diagram"`;
  - node and cell names are clean;
  - the key glosses struct, pointer, [12] and NULL;
  - the nav wraps, and scrollWidth is 375.
- Language pages: the kicker "struct lang C++ · 1985 · … parent: C" comes before `group "C++: 1985 …; its parent is C"`, so a screen reader announces the struct twice. Neither glosses "struct".
- Lesson 03 uses `for`, `samples[]`, `i++`, `static` and a function return. Those are taught in lessons 04–06.
- No page explains a compiler or a terminal, or how to get gcc ("install" and "terminal" are absent from content.py). Every lesson still says "Compile and run it yourself".

**Findings:**
- F1 [defect] Lesson 03 depends on unglossed later topics.
- F2 [premise] A never-programmed reader is invited to run code with no setup path.
- F3 [defect] Language pages announce the struct twice.
- F4 [claim] "struct lang" is unexplained on language pages for readers who skip the home page.
- F5 [defect] Lesson 02 leaves %d, %c, %zu and "bits" unglossed.

**Verdict:** OBJECT. The objection is narrow: the hero and the phone layout now pass.

**Requested change:**
- F1: use three plain `if` calls, or gloss the loop and array in one line that points forward.
- F2: add a short "getting a compiler" note, linked from "Compile and run it yourself".
- F3: hide the kicker from screen readers (`aria-hidden`).
- F4: put a one-line key under the struct box.
- F5: gloss each format code in one line.
