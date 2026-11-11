# R2 — Critic: Craft (Bringhurst)

**Anchor used:** *The Elements of Typographic Style*: 2.1.2 (45–75 characters, 66 ideal), 2.2.2 (a modular scale), 5.1.4 (true apostrophes in text).

**Observed** (Playwright line boxes, whitespace collapsed, last lines excluded):
- Lesson prose at 1280: 19px Newsreader, 551px. c/07 lines run to 71 (median 69), c/01 to 71, about to 73, holyc to 74.
- At 375: 17px prose, 41–49 characters.
- family `.small`: 16px, 67–68 characters.
- Headings: body 19px, h3 20px (1.05×), h2 25.6px (1.35×). Both are mono 800.
- No `p code` breaks on lesson pages. Only the about/cpp command lines wrap, which is intended. Chip padding is 2.39px (.15em).
- Straight `&#x27;` remains in prose: the ledes of csharp ("Hejlsberg's", "C's"), objc ("Smalltalk's") and holyc ("system's"), and rosetta "library's". The other prose is curly.
- `.ros > p` gets max-width var(--cols) = 664px (site.css:198 overrides :66). Each note now fits on one line of ≤73 characters.

**Findings:**
- F1 [premise] The R1 measure is resolved: prose now sits within 45–75 at both sizes, and code keeps its 80 columns.
- F2 [premise] The family caption is resolved.
- F3 [premise] Inline-code breaking and chip padding are resolved.
- F4 [defect] Apostrophes are only partly typeset. The language-page ledes keep the typewriter mark.
- F5 [claim] h3 is only 1.05× the body. Weight and face carry the step, but it is not modular. My R1 rem target missed the 1.1875rem body.
- F6 [claim] The Rosetta notes skip the 29em cap. A longer note would run to about 80 characters.

**Verdict:** OBJECT

**Requested change:**
- F4: Run the curly-apostrophe pass over the ledes and the Rosetta notes as well.
- F5: Optional. h3 at about 1.4rem, so that h3 is 1.18× the body and h2 1.35×.
- F6: Drop `.ros > p` from the line-198 rule, or re-cap it at 29em.
- F1–F3: none.
