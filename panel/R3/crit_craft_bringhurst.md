# R3 — Critic: Craft (Bringhurst)

**Anchor used:** *The Elements of Typographic Style*: 5.1.4 (true apostrophes and quotation marks), 2.1.2 (measure), 3.2 (a modular scale), 1.2.1 (size held to reading distance).

**Observed** (Playwright, 22 pages, 1280 and 375, code excluded):
- Straight `'` outside code: one, in about.html: "`fgetc`'s result", where the mark follows a `<code>`. Straight `"` in prose: rosetta ("Reverse "pointer""), and cpp ("C++" beats "C"; "C#" … "C++").
- h3 is 22.4px, 1.18× the 19px body. h2 is 25.6px, 1.35×.
- Rosetta notes are 551px wide, with at most 73 characters on one line.
- Drawing labels, rendered size (font-size × width/viewBox): 07 is 13.2–14px at 1280 and 21.4–22.9 at 375. 08 is 23.7–25.3 at 1280 and 12.3–13.1 at 375. 11 is 10.8–12.3 at 1280 ("NULL" 10.8).
- The evidence says the smallest text is 12px. The 11 drawing contradicts that.

**Findings:**
- F1 [premise] The h3 scale and the Rosetta measure are resolved.
- F2 [defect] One apostrophe was missed, the one after inline code. The typesetter skips text that follows an element.
- F3 [claim] The straight double quotes in rosetta and cpp mark string values but sit in roman prose.
- F4 [defect] The drawings scale their type with their width. At one viewport, labels run from 10.8px (11) to 25.3px (08), which is above h2.

**Verdict:** OBJECT

**Requested change:**
- F2: Typeset apostrophes across element boundaries.
- F3: Set them as `<code>"pointer"</code>`, or use “ ”.
- F4: Fix the label size at about 15px rendered, never below 12px.
- F1: none.
