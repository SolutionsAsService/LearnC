# Critic: Inclusion (Mace), R2

- Anchor used: Principles of Universal Design (Mace et al.). P4 "Perceptible Information" asks for legibility in every mode. P7 "Size and Space" asks for room to operate.

- Observed (Playwright, real Tab presses, 1280 and 375, light, dark and forced colours):
  - HTML controls get a 3px --ptr outline. Hero boxes and the 375 cells get a 4px stroke, which is Highlight in forced colours.
  - My R1 fixes hold. Cells measure 37.2x28.6 px, the nav wraps, and the kicker "C" measures 19.9x24.3 px. Bands are CanvasText, and `aria-current` has a border.
  - At 375, the only targets under 24 px are the nav "C" and the Rosetta links. Both pass on spacing.
  - On cpp.html, the struct link "Parent: C" draws `.band` over `.box` at the same size.

- Findings:
  - F1 [defect] Light scheme: the focused struct "C" link has a #b3261e stroke on a #b3261e band (1.00:1). The ring cannot be seen, and in forced colours it is navy on black.
  - F2 [defect] `.start:hover` in the dark scheme is #f6f1e7 on #efe8da (1.08:1).
  - F3 [defect] `svg .kw` at opacity .8 on the bands: C 4.20:1 and HolyC 4.17:1, both under 4.5.
  - F4 [claim] In forced colours, the focus fill var(--paper-2) beats `fill:Canvas`, so beige shows through.
  - F5 [claim] No information is carried by colour alone, and there is no motion.

- Verdict: OBJECT

- Requested change:
  - F1: draw the focus stroke above the band, or use a double ring.
  - F2: use a var(--paper) hover text.
  - F3: set opacity to 1.
  - F4: add a Canvas fill to the forced-colours focus rule.
  - F5: none.
