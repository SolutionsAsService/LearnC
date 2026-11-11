# R5: Inclusion (Holmes)

**Anchor used:** Holmes, *Mismatch*. A fix reaches many only if it covers the whole path.

**Observed (aria snapshots at 375×812; curl):**
- objc.html: under each program, "Download 01_messages.m with Root.h and Root.m beside it, open a terminal in the folder you saved it to, and paste the command." All three are `download` links. All four I fetched returned 200. R4 F1 is resolved.
- About › Getting a compiler: "WSL (a Linux shell inside Windows)". R4 F2 is resolved.
- "beside it" is the only cue to keep the files together.
- macOS: "The Objective-C commands here … were verified on Linux only"; the page gives no Mac path.
- "PowerShell" and `sudo` are not glossed.

**Findings:**
- F1 [claim] "beside it" is spatial shorthand. A first-time reader saves three downloads and may not know they must land in one folder.
- F2 [premise] Mac newcomers cannot run the Objective-C programs. Disclosed honestly; out of scope.
- F3 [claim] PowerShell and `sudo` are unglossed.

**Verdict:** PASS. Both R4 findings are fixed.

**Requested change:**
- F1: "save all three in the same folder".
- F2: none.
- F3: optional: "PowerShell (Start menu › PowerShell)"; "`sudo` asks for your password".
