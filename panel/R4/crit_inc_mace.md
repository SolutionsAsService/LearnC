# Critic: Inclusion (Mace), R4

- Anchor used: Principles of Universal Design (Mace et al.). P4 Perceptible Information; P5 Tolerance for Error.

- Observed (Playwright, real Tab):
  - `a.node-anc` is Tab 13 at 1280 and Tab 12 at 375. Its 8px `.frame` is ink in light and dark, and Highlight in forced colours. Focused and blurred screenshots differ in all 6 modes.
  - Sweep: 274 and 286 tab stops, 9 pages, 6 modes. One stop is unchanged by focus.
  - 31 `a[download]` links: inline, 15px tall, HTTP 200. No motion.

- Findings:
  - F1 [claim] R3 F1 is resolved at both sizes, in all schemes.
  - F2 [defect] At ≥761px, `.top nav{overflow-x:auto}` clips each ring to a 3px side bar. On c/index, the "Home" bar hides under the current "C" box, so focus changes nothing.
  - F3 [defect] `.cmd{font:…}` resets line-height to normal. At 1280, "How to get one" sits 0px below "Download …" on 9 programs. The 2.5.8 inline exception excuses this; P5 does not.

- Verdict: OBJECT

- Requested change:
  - F1: none.
  - F2: pad the nav 6px, or `.top li a{outline-offset:-3px}`.
  - F3: `.setup{line-height:1.55}`.
