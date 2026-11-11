# R1 — Critic: Craft (Bringhurst)

**Anchor used:** *The Elements of Typographic Style*, 2.1.2: lines of 45 to 75 characters, with 66 as the ideal. Also 2.1.1 (hierarchy) and 5.1 (punctuation).

**Observed** (measured line boxes in Playwright):
- c/07-pointers at 1280: 19px Newsreader in a 664px column, leading 1.55. Full lines run 79, 81, 77, 80 and 82 characters.
- c/07 at 375: lines run 37 to 47 characters.
- about.html at 1280: 81 to 84 characters.
- family.html caption: 14.4px with a 107-character line.
- Headings: h2 is 21.6px and h3 is 16.8px, both mono. Body is 19px.
- On c/07 at 1280, `(void *)` breaks after "(void".
- Prose apostrophes are straight ("caller's", "C's"). The en dash in "1969–2018" is correct.

**Findings:**
- F1 [defect] Lesson prose runs about 80 characters. The measure follows the code box, not the reader, and passes the ceiling of 75.
- F2 [defect] The family caption runs 107 characters at 14.4px.
- F3 [defect] h3 is smaller than the body it heads (holyc, "Default arguments"). h2 is only 1.14× the body, so its rule does the ranking.
- F4 [defect] Inline code breaks inside a token: "(void" / "*)".
- F5 [defect] Typewriter apostrophes appear in serif prose.
- F6 [claim] Code-chip padding opens a gap before the punctuation that follows: "`num` ," and "`Greet(, 3)` .".
- F7 [premise] The 375 setting is well judged: 1.55 leading, 37–47 characters, 17px. The mono/serif pairing suits the subject.

**Verdict:** OBJECT

**Requested change:**
- F1: Cap the prose at about 34em (roughly 66 characters) and leave code at 80 columns.
- F2: Apply the same cap, or set the caption at body size.
- F3: Set h3 at 1.2rem or more and h2 at about 1.6rem.
- F4: Add `white-space: nowrap` to `p code` and `li code`.
- F5: Use ’ in prose strings (content.py) and keep straight quotes in code.
- F6: Cut the chip's side padding to .15em.
