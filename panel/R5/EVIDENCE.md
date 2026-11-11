# R5 evidence: LearnC after the R4 fixes (M12) and the S4 push (M13)

The site is served at http://localhost:8765/. Source: /home/user/learnc. Read your own latest report (panel/R4/, or panel/R3/ for Shklovsky) and the R4 resolution table in DESIGN-LOG.md. Then judge the site as it is now.

## Measured after the last edit
- Build: 41 programs, 0 warnings, 0 failures. Whole-line output checks pass.
- All 22 pages × 1280x800 and 375x812 × light and dark: 0 horizontal overflow, smallest text 12 px.
- Hero: bottom at 707 px (1280x800) and 768 px (375x812). Root C glyph: 129 px tall (was 98).
- Objective-C: Root.h and Root.m now sit beside every .m file (examples/objc and examples/objc/rosetta). Fetched over HTTP into an empty folder, the printed command run verbatim prints 55 for rosetta/sum.m and the recorded output for 01_messages.m.
