# R0 — Critic: Usability (Krug)

- **Anchor used:** *Don't Make Me Think* (Krug): the five-second test (what is this, what do I do next?), the trunk test (where am I, what can I click?), and "omit needless words".

- **Observed:** README.md ends mid-step at `cd basic_concepts`, inside an unclosed ```bash fence. It has no compile or run command (seen with `cat -A`; EVIDENCE.md doesn't mention this). README lists `functions/`, which doesn't exist, and leaves out `file_io/`, which does. No output is shown. `read_file.c` fails because `example.txt` is missing. Only C exists and there is no website (EVIDENCE).

- **Findings:**
  - F1 [defect] Five-second test fails. The only how-to is cut off before the compile step.
  - F2 [defect] The first listed folder a newcomer tries (`functions/`) is a dead end, and `file_io/` is hidden.
  - F3 [defect] You have to compile to learn what each program prints.
  - F4 [defect] The last lesson fails on first run, and the newcomer thinks "I broke it".
  - F5 [claim] Trunk test can't be run. There are no pages, no "you are here" and no order.
  - F6 [premise] "C and its family" is promised but only C is delivered.

- **Verdict:** OBJECT

- **Requested change:**
  - F1: one complete copy-paste command on the first screen: `gcc hello_world.c -o hello && ./hello`.
  - F2: a numbered lesson list that matches the files.
  - F3: show the output beside the code.
  - F4: ship `example.txt`.
  - F5: every page shows the site ID, a language tab, a lesson number and prev/next links.
  - F6: mark the missing languages "coming". Never link to an empty page.
