# Critic: Inclusion (Mace), R3

- Anchor used: Principles of Universal Design (Mace et al.). P4 "Perceptible Information" requires legibility in every mode. P5 "Tolerance for Error" requires the user to always know where they are.

- Observed (Playwright, real Tab presses on index, cpp, c/index; 1280 and 375; light, dark and forced colours):
  - The C, C++, Objective-C, C# and HolyC nodes and both "Parent" links draw an 8px `.frame` on top. Its outer half is ink on paper, 15.6:1 in light and 15.3:1 in dark. In forced colours the frame is Highlight.
  - At 375, the lesson cells (37x29) get a 4px `--ptr` ring on all four sides. It measures 5.7:1 against paper and 7.3:1 in dark.
  - Dark `.start:hover` is #14120f on #efe8da, 15.3:1.
  - `.kw` has opacity 1 on all five bands: C 5.81, C++ 6.37, Objective-C 6.04, C# 7.05, HolyC 5.56.

- Findings:
  - F1 [defect] Hero `a.node-anc` ("Ancestors…") contains no `.frame`. On focus, only its fill changes, from paper to paper-2 (1.10:1). In forced colours, the focused and unfocused screenshots are byte-identical.
  - F2 [claim] My R2 F1 to F4 are resolved, as measured above.
  - F3 [claim] Targets are at least 24 px, no information is carried by colour alone, and there is no motion.

- Verdict: OBJECT

- Requested change:
  - F1: add a `.frame` rect, covering both boxes, to the Ancestors node at both sizes.
  - F2 and F3: none.
