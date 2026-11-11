# R5 · Critic: Provocateur (Debord)

**Anchor used:** *The Society of the Spectacle*, Thesis 1: what was lived "moves away into a representation". A claim must be a thing you can do, not an image of one.

**Observed:** All 22 pages read. 41 programs counted under site/examples (17 C, 9 C++, 8 C#, 7 ObjC; 7 HolyC). runs.json dates all four languages 2026-11-11. Rosetta table, the "24 lines" of Root.h+Root.m, the twelve lesson counts and "56 bytes" match the files and output. Fetched point.m and 02_categories.m with Root.h/Root.m over HTTP into empty folders, ran the printed commands verbatim: 5.0 and the recorded four lines.

**Findings:**
- F12, F13, F14 resolved: Root.h and Root.m linked beside every ObjC download (2 on objc.html, 5 on Rosetta); no "../"; About now says "any C, C++, Objective-C or C# program".
- F15 [claim] csharp.html: exceptions are "errors that cannot be silently ignored"; an empty catch ignores them.
- F16 [defect] objc.html "The root class" says it "allocates with class_createInstance", but shows only Root.h; that call lives in Root.m.

**Verdict:** PASS

**Requested change:**
- F15 (optional): "errors that cannot pass unnoticed unless you catch them".
- F16 (optional): show Root.m too, or say "Root.m allocates…".
