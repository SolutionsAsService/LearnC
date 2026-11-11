# Critic: Evidence (Cairo), R5

**Anchor used:** *How Charts Lie*: a number is honest only if a reader following the stated method gets the same one.

**Observed:** Empty folders, files fetched over HTTP, printed command extracted from the live HTML and run verbatim: objc.html 01_messages.m + Root.h + Root.m → "lamp is on / message to nil returns 0", exit 0, no warnings, matches the page; rosetta.html sum.m → 55, exit 0. Scratch rebuild: 41 programs, 0 warnings, 0 non-zero exits, 22 pages, site/ identical. measure.cjs: 88 rows = 22 pages × 2 sizes × 2 schemes, 0 overflow, min 12 px; hero bottom 707/768 both schemes. C glyph at 1280: getBoundingClientRect 129 px, getBBox 124 px; at 375: 50 px.

**Findings**
1. [claim] R4 F2, F3 resolved: Root.h/Root.m linked "beside it" (objc.html, rosetta.html download lines); both runs reproduce.
2. [claim] R4 F4 resolved: measure.cjs enumerates site/ (measure.cjs:7); 22 of 22.
3. [claim] Build, overflow, 12 px floor, 707/768 all reproduce.
4. [premise] "C glyph 129 px tall" is the text layout box at 1280 only, not the ink; label it "text box, 1280".

**Verdict:** PASS

**Requested change:** F4: say "text box at 1280x800" in the log and evidence.
