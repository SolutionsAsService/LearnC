# R1: Inclusion (Holmes)

**Anchor used:** Holmes, *Mismatch*. Exclusion is a mismatch between a design and a person. Fix it for one person and the fix extends to many.

**Observed:**
- Home page at 375 px: the hero uses `struct lang`, `parent ●`, `lessons[12]`, `rosetta[5]` and `NULL`. The legend glosses only "pointer".
- The lesson cells are 26×21 px and sit flush against each other.
- The nav (site.css:49–50) scrolls with a hidden scrollbar and cuts off after "Objective-C".
- The hero SVG is `role="img"` and contains 23 focusable links. The cells get clean names from `<title>` ("Pointers"). The node links do not; they read as run-on text, for example "struct lang C year 1972 · Bell Labs by Dennis Ritchie hello 5 lines · ran ✓ parent lessons".
- Lessons 01–03 use these terms without explaining them:
  - "declarations", "shell", "C23" and the "exit 0 · 0 warnings" badge;
  - "byte", "float", `%.2f` and "the original example";
  - "`const char *`, a pointer…", although pointers are taught in lesson 07.

**Findings:**
- F1 [defect] On the phone the lesson cells are 26×21 px and touch each other, which fails WCAG 2.2 2.5.8 (24 px target size).
- F2 [defect] At 375 px, five nav destinations are hidden with no cue that the nav scrolls.
- F3 [defect] The node links have run-on accessible names that read like a data dump.
- F4 [claim] The links sit inside `role="img"`, whose children are presentational. Some screen readers may flatten them; I did not verify this in NVDA or VoiceOver.
- F5 [premise] The hero states its premise in C syntax, so the never-programmed reader the page invites ("New to C?") is the one it excludes.
- F6 [defect] Lessons 01–03 depend on terms taught later or never.

**Verdict:** OBJECT

**Requested change:**
- F1: make the cells at least 24 px (two rows of six).
- F2: wrap the nav or show a visible "more" cue.
- F3: give each node a `<title>` ("C: the C course").
- F4: use `role="group"` with `aria-labelledby`.
- F5: add a plain-language caption for struct, `[n]` and `NULL`.
- F6: gloss each term on first use, and drop "original example".
