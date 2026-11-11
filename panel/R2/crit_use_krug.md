# Critic: Usability (Krug), R2 (whole site, after M5 to M8)

**Anchor used:** Don't Make Me Think (Krug): the five-second test, the trunk test, and "make the first action obvious".

**Observed (live, Playwright):**
- 1280x800 home: "LearnC", h1 "C and the languages that grew from it", and a red "Start with lesson 01 →" at y 83–127 beside it. Probe: C++'s parent wire enters C's bottom border, and C points to B and `lessons[12]`. Passes.
- 375x812 home: the nav wraps to two rows (Home…HolyC / Rosetta, Family, About). scrollWidth is 375. The children's wires climb through gutters into C's bottom and right borders, and none ends on a cell. The start link is at y 885, below the 812 fold.
- Lesson c/07-pointers at both sizes: site ID, "C" current (underlined), crumb "C · lessons[6] · lesson 7 of 12", h1 "Pointers", prev/next ("Arrays", "Structs"), title "Pointers (C lesson 7) · LearnC". Trunk test passes.

**Findings:**
- F1 [premise] R1 F1 fixed: the nav wraps and all nine items are visible at 375.
- F2 [premise] R1 F2 fixed: the phone wires land on C's borders, not on lesson cells.
- F3 [claim] R1 F3 fixed at 1280. On the phone, the start link is 73 px below the fold. Cell 01 is still tappable above it, so I do not object.
- F4 [claim] The crumb puts "lessons[6]" next to "lesson 7", so a beginner has to work out zero-indexing before reading on.
- F5 [premise] The five-second test and the probe pass at both sizes.

**Verdict:** PASS

**Requested change:**
- F1, F2, F5: none.
- F3: optional. At 375, move the start link above the hero or just under the h1.
- F4: optional. Show "lessons[6]" in a lighter style, or drop it from the crumb.
