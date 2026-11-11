# R3 · Critic: Provocateur (Debord)

**Anchor used:** *The Society of the Spectacle*, Thesis 1: the lived "moves away into a representation".

**Observed:** build.py:812–823 checks the Rosetta "Prints X." lines and QUOTED_OUTPUTS against runs.json. The drawings' text matches the programs: 10→42 and x=2 y=1 (07), "John" 30→31 and 56 bytes (08), 0…81 then NULL (11). About › Getting a compiler: "`sudo apt install gcc g++ mono-mcs` covers … Objective-C (the GNU runtime ships with gcc)". On this Ubuntu 24.04, `gcc` does not depend on `libobjc-13-dev`, which owns `objc/runtime.h` and `libobjc.so`. The printed Objective-C command calls `clang`, and that line does not install clang. "Getting one takes one command" appears 41 times.

**Findings:**
- F8 (R2) resolved. The check is a substring match ("5.0" would also pass "15.0"), and 0x23/0x2B on cpp.html and "30 → 31" are still unchecked. Minor.
- F10 [claim] The Linux setup line does not install what the printed Objective-C command needs: clang, and libobjc headers and library.
- F11 [claim] The macOS line implies that every printed command will run. But the Objective-C commands use `-fobjc-runtime=gcc -lobjc` (the GNU runtime), and `mcs`/`mono` are not installed. "One command" oversells: Windows takes two.
- F9 (R2) stands, and it is disclosed.

**Verdict:** OBJECT

**Requested change:**
- F10: `sudo apt install gcc g++ clang mono-mcs`. On Ubuntu, clang pulls in libobjc-dev. Drop "ships with gcc".
- F11: say macOS covers C and C++ only. Change the link to "How to get a compiler".
- F8: optional, tighten the match to a whole line or word.
