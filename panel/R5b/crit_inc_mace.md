# Critic: Inclusion (Mace), R5b

- Anchor used: Principles of Universal Design (Mace et al.). P4 Perceptible Information.

- Observed (Playwright, real Tab, 6 pages; light, dark, forced light, forced dark; 1280 and 375):
  - `.frame` ring is 4.16px (1280) to 2.77px (375) wide, drawn outside the box. A 2–4px paper gap and the band lie between it and the C. Dark 1280 pixel column: ring #efe8da, then paper, then band, then the C 9px further in.
  - Zero clip in all 8 runs, including the `y=-2` narrow frame.

- Findings:
  - F1 [claim] R5 F3 resolved. Ring against paper: 15.56:1 light, 15.34:1 dark. Forced: Highlight against Canvas, about 10:1 or more. The ring no longer touches the glyph.
  - F2 [claim] R5 F4 resolved. The `[aria-current]` ring against the ink fill is 15.56:1 light, 15.34:1 dark, and 13.76:1 or more forced.
  - F3 [claim] No frame is clipped at the viewBox edge.

- Verdict: PASS

- Requested change: none.
