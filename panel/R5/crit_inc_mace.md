# Critic: Inclusion (Mace), R5

- Anchor used: Principles of Universal Design (Mace et al.). P4 Perceptible Information; P5 Tolerance for Error.

- Observed (Playwright, real Tab; light, dark, forced light, forced dark; 1280 and 375):
  - Nav, 3 pages: all 9 links change 282–822 px on focus in every mode. `outline-offset:-3px` holds.
  - `.setup` line-height is 23.56px. At 1280 the second link starts 8px below the first; it was 0.
  - Hero `a.node-c` (Tab 14 / 13): the C's ink top sits 0.3px (1280) and 0.1px (375) under the 8px `.frame`'s inner edge.

- Findings:
  - F1 [claim] R4 F2 (nav clipping) resolved in all 8 runs.
  - F2 [claim] R4 F3 (download leading) resolved.
  - F3 [defect] In dark mode the ring (#efe8da) meets the glyph (#f6f1e7) at 1.08:1, so the C fuses into the frame. Light (15.9:1) and forced colours stay distinct.
  - F4 [defect] On the `[aria-current]` link, the inset red ring sits on ink: 2.73:1 in light, 2.09:1 in dark, under 3:1.

- Verdict: OBJECT

- Requested change:
  - F1, F2: none.
  - F3: move the C down at least 4 units (y 112), or draw `.frame` outside the box.
  - F4: `.top li a[aria-current]:focus-visible{outline-color:var(--paper)}`.
