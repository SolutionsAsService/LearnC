# Critic: Inclusion (Mace), R1

- Anchor used: Principles of Universal Design (Mace et al.): P7 "Size and Space for Approach and Use"; P4 "Perceptible Information" (redundant modes that respect the user's settings).

- Observed (Playwright, real Tab presses; /tmp/claude-0/mace/):
  - HTML controls get `:focus-visible` 3px --ptr: skip link (tab 1), nav, `summary` and pager on c/07.
  - Hero SVG links use `outline:none`; the `.box` stroke goes from 2px ink to 4px --ptr, visible at 1280 light and 375 dark (home1280-tab14, home375dark-tab14).
  - At 375, lessons[12] cells are 25.7x21 px, edge to edge, inside the `.node-c` box. Nav links are 35.7 px tall.
  - Language colours meet 4.5:1 in both schemes (4.94 to 10.11). No motion.

- Findings:
  - F1 [defect] At 375, the hero `.cell` targets are 21 px tall. A 24 px circle overlaps the `.node-c` target, so they fail WCAG 2.5.8.
  - F2 [defect] Forced colours: `svg .band{fill:CanvasText}` (site.css:201) loses to `.node-c .band` (line 90). The bands stay author red, blue and so on (fc-home-focus14).
  - F3 [defect] Forced colours: nav `aria-current` is shown only by a background, which is dropped, so "Home" looks like the other links.
  - F4 [defect] At 375, the nav ends cleanly at "Objective-C" and `scrollbar-width:none` hides the scrollbar. Five links have no visible cue.
  - F5 [claim] The SVG focus ring differs from ink by 2.73:1, relying on width. In forced colours it is author red, not Highlight.
  - F6 [claim] Nothing is carried by colour alone. Bands and timeline dots have text labels, and "ran ✓" and "not run" are words. C and Objective-C differ by only 1.04:1 in luminance.
  - F7 [premise] The kicker link "C" on lessons is 8x17 px and passes only by the spacing exception.

- Verdict: OBJECT

- Requested change:
  - F1: make the narrow cell height 26 or more, or move the array out of the C box.
  - F2: raise specificity inside the forced-colors block.
  - F3: give `[aria-current]` an underline or border.
  - F4: wrap the nav or add a "more" cue.
  - F5: `stroke:Highlight` in forced colours.
  - F6: none.
  - F7: pad to 24 px.
