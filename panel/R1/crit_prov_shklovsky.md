# R1 - Critic: Provocateur (Shklovsky)

- Anchor used: Shklovsky, "Art as Technique": habit devours things; the device makes the stone stony by roughening form. A device seen once and then dropped decays into recognition.

- Observed: index 1280 light: the first screen is the device: `struct lang` boxes, `parent` dots wired back to C, `lessons[12]` and `rosetta[5]` arrays, BCPL pointing to NULL (hero 137 to 707 px, EVIDENCE). index 375 dark: redrawn, not shrunk, but C's `lessons` pointer is gone (array inlined). c_07-pointers 1280: centred column, code, output bar, prose, prev/next; no diagram. Grep of site/: `<svg` only in index.html (2) and family.html (1); c/07-pointers.html has 0. rosetta 1280: line-count table with a Total row, then 25 near-identical code cards.

- Findings:
  - F1 [claim] The hero defeats automatic perception: a site map I would skim becomes memory layout; lineage becomes an address. Strongest device here.
  - F2 [defect] Buried after the first screen: 2 of 22 pages carry it; every inner page reverts to the habitual docs column.
  - F3 [defect] Worst burial: the Pointers lesson, whose subject *is* the device, explains `&num` and `*ptr` in prose and never draws the box and wire the home page taught me to read.
  - F4 [defect] At 375 the `lessons` pointer is dropped, so C's outward wire, the most estranging gesture, vanishes on phone.
  - F5 [defect] Rosetta's line-count table with Total is a stat-tile habit; identical cards automatise by the third program.
  - F6 [premise] The kicker "lesson 07 of 12" could be `lessons[6]` and is not; the notation stops at the door.

- Verdict: OBJECT

- Requested change:
  - F1: none.
  - F2/F6: carry the notation inward: kicker as `lessons[6]`, prev/next as `lessons[5]`/`lessons[7]` wires, each language page headed by its own struct box.
  - F3: draw num, ptr and &num as boxes with a wire on 07-pointers, redrawn after `*ptr = 42` and after swap.
  - F4: restore the `lessons` field and its wire at 375.
  - F5: render the table as `rosetta[5]` rows or cut the Total; let each program's difference be seen, not tallied.
