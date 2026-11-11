# R4 · Critic: Provocateur (Debord)

**Anchor used:** *The Society of the Spectacle*, Thesis 1: what was lived "moves away into a representation".

**Observed:** About › Getting a compiler now reads `sudo apt install gcc g++ clang mono-mcs`. clang-18 depends on libobjc-13-dev, which owns `objc/runtime.h`, and mono-mcs depends on mono-runtime (`/usr/bin/mono`). macOS is limited to C and C++, and Windows is "two steps". "One command" is gone. All 41 Download links return 200. On objc.html the sentence reads "(it also needs Root.m, from the same folder)", and no page links to Root.m or Root.h. Root.m `#include`s Root.h. On rosetta.html it reads "needs ../Root.m, from the same folder".

**Findings:**
- F10, F11, F8 resolved.
- F12 [claim] The Objective-C download sentence names a file it does not give: Root.m has no link, and Root.h, which Root.m needs, is not mentioned.
- F13 [defect] On Rosetta, "../Root.m, from the same folder" contradicts itself.
- F14 [claim] On About, "download any program… compare with the dark output box": HolyC has neither.

**Verdict:** OBJECT

**Requested change:**
- F12: link Root.m and Root.h beside each Objective-C download.
- F13: say "Root.m and Root.h, saved one folder up", or flatten the command.
- F14: "any program except HolyC".
