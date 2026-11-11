# Critic: Usability (Krug), R1 (whole site)

**Anchor used:** Don't Make Me Think (Krug): the five-second test ("what is this, what do I do here") and the trunk test on an inner page.

**Observed:**
- Home, 1280x800 (index.html-1280-light.png): I name the site, LearnC, and three topics from the first screen: a 12-lesson C course, C++/Objective-C/C#/HolyC, and Rosetta. Legibility probe passes: C++'s `parent` dot runs into the bottom of the C box, and C points to B and `lessons[12]`.
- Home, 375x812 (index.html-375-light.png; live check): the nav is 547 px of links in a 229 px strip. HolyC, Rosetta, Family and About are off-screen, with no cue that they are there. The children's arrows end on the `lessons[12]` cells (2, 5, 8, 11), not on the C box.
- Lesson c/07-pointers: trunk test passes. It has the site ID, the "C" nav item highlighted, a "C · lesson 07 of 12" breadcrumb, the page name, prev/next links, and a matching title. There is no search, which is fine at 22 pages.

**Findings:**
- F1 [defect] On a phone, four of nine sections are hidden in an unsignalled sideways scroll.
- F2 [defect] On a phone, the parent arrows of C++, Objective-C, C# and HolyC land on lesson cells, so C++ seems to point at lesson 2.
- F3 [claim] There is no visible first action: "start the course" is cell 01, drawn the same as cell 12.
- F4 [claim] "struct lang" and the `lessons[12]` syntax make you decode before you act. That is tolerable for this audience (my blind spot).
- F5 [premise] At 1280, the five-second test and the probe both pass.

**Verdict:** OBJECT (F1, F2)

**Requested change:**
- F1: At 375, wrap the nav onto two lines, or show a fade or chevron at the edge.
- F2: At 375, route the arrows into the C box's border, or move `lessons[12]` out of the box.
- F3: Mark cell 01 "start", or add a "Start lesson 1" link under the h1.
- F4: None.
- F5: None.
