# R2 - Critic: Provocateur (Shklovsky)

- Anchor used: Shklovsky, "Art as Technique": habit devours things; the device makes the stone stony by roughening form, and a device repeated without change decays back into recognition.

- Observed: R1 asked for kickers, struct headers, a pointer diagram, the phone wire, and asked for the Total row to go (DESIGN-LOG R1 table). c_07-pointers 1280: kicker `C · lessons[6] · lesson 7 of 12`; three drawn states (num/ptr, `*ptr = 42`, swap a/b), placed after the code and the compile line. index 375 dark: `lessons[12]` is back as its own array, wired from C.lessons. holyc 375: its own green struct box, wired to the C box. rosetta 1280: rows read `rosetta[0..4]`, and the Total row is still there. A grep of site/ finds `<svg>` on 07-pointers (3), cpp/objc/csharp/holyc (1 each), index (2) and family (1). c/index.html, the 11 other lessons and rosetta have none. Prev/next on lesson 07 read "previous Arrays / next Structs".

- Findings:
  - F1 [claim] The notation now goes inside: the Pointers drawing makes `&num` into a wire I can see. It is the best device after the hero.
  - F2 [defect] The C page itself has no struct box. The parent every other page wires to is never drawn on its own page.
  - F3 [defect] Lesson 08 Structs, whose subject is the box, draws nothing. Lesson 11 malloc also draws nothing, though the heap is a natural box-and-wire picture.
  - F4 [defect] On lesson 07 the diagram sits after the code and the compile line, so the strangest device on the page is still buried.
  - F5 [defect] Prev/next are plain words. They are not `lessons[5]` and `lessons[7]`.
  - F6 [premise] `lessons[6]` next to "lesson 7 of 12" glosses the device before I have had to work at it. Repeated on 12 pages, the gloss will become habit.
  - F7 [defect] Rosetta is still a tallied table plus 25 identical cards. Prefixing the rows with `rosetta[i]` decorates the habit; it does not break it. The OVERRULE is noted.

- Verdict: OBJECT

- Requested change:
  - F1: none.
  - F2: open c/index with C's own struct box.
  - F3: draw the struct on lesson 08 and the heap on lesson 11.
  - F4: move the lesson 07 diagram above the code, or beside it.
  - F5: label prev/next `lessons[5]` and `lessons[7]`.
  - F6: keep the gloss on lesson 01 only.
  - F7: on each Rosetta program, mark the lines that differ from C instead of counting them.
