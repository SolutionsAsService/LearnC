# R0 — Critic: Evidence (Cairo)

- **Anchor used:** *How Charts Lie* (Cairo): a figure is honest only if a reader can trace and reproduce it. Omissions and hidden scales mislead too.
- **Observed:** I re-ran all 9 `.c` files (gcc 13.3.0, `-std=c17 -Wall -Wextra -Wpedantic -Wstrict-prototypes -Wconversion`). The outputs match the EVIDENCE table. I also read README.md (17 lines) and CONTRIBUTING.md.

**Findings**
1. F1 [defect] README.md:15-17 stops at step 1 inside an open ```bash fence and never gives a compile command, so the README alone cannot reproduce anything. EVIDENCE does not mention this.
2. F2 [claim] README.md:8 lists `functions/`, which does not exist (EVIDENCE gives line 9). The README also omits `file_io/`.
3. F3 [claim] EVIDENCE's "0 warnings" holds only at -Wall -Wextra. Under -Wpedantic, pointers_example.c:10-11 passes `int*` to `%p`, which is undefined behaviour. All 9 files trip -Wstrict-prototypes.
4. F4 [claim] The read_file.c:12 bug is real (I reproduced both failures). Its "no warning" holds only without `-Wconversion`, which flags 12:18.
5. F5 [defect] variables.c:6 stores 5.9 in a float, so the stored value is 5.9000001. `%.2f` at line 11 hides that.
6. F6 [premise] The repo has only C, with no expected outputs, tests or build script. It supports no claim about C++, Objective-C, C# or HolyC.
7. F7 [claim] CONTRIBUTING.md:4,27 mentions "data corrections" and "run the tests", but neither data nor tests exist.

- **Verdict:** OBJECT
- **Requested change:** F1: finish the compile steps. F2: make the README match `ls`. F3: use `(void*)` casts and `int main(void)`. F4: use `int ch`, ship `example.txt` and state the flags. F5: use `double`. F6: give each page the verbatim output plus the compiler and flags, and cite a primary spec for each non-C language. F7: trim CONTRIBUTING to match the repo.
