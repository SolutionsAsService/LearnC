# R4: Inclusion (Holmes)

**Anchor used:** Holmes, *Mismatch*. A fix reaches many only if it covers the whole path.

**Observed (aria snapshots at 375×812, HTML, a Playwright click):**
- Lesson 07's images are named in words ("ptr holds the address of num; num is 10"). R3 F1 is resolved.
- Lessons 01–03 have a `download` link plus "open a terminal in the folder you saved it to". The click saved 01_hello.c. R3 F2 is resolved for C.
- "How to get one", and Windows is "two steps". R3 F3 is resolved.
- Lesson 03 glosses `static` and `%s`. R3 F4 is resolved.
- objc.html says "(it also needs Root.m, from the same folder)" but has no link. 01_messages.m has `#include "Root.h"`, which the page never mentions. Both files are served.
- About leaves "WSL" unexplained.

**Findings:**
- F1 [defect] A reader of the Objective-C page cannot get Root.m or Root.h from it. "The same folder" is the repository, which they never see.
- F2 [claim] "WSL" is not glossed.

**Verdict:** OBJECT. This is narrow: all four R3 findings are resolved.

**Requested change:**
- F1: link Root.m and Root.h beside each download, and say "save all three in one folder".
- F2: "WSL (a Linux shell inside Windows)".
