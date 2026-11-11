# Contributing to LearnC

Fixes and new examples are welcome.

## Add or fix an example

1. Put the program under `examples/<language>/` (for a C lesson, also add an entry to `LESSONS` in `_src/content.py`).
2. Run `python3 _src/build.py`. It compiles and runs everything; the build fails if your program prints a warning or exits non-zero.
3. Commit the program, the rebuilt `site/` and `_src/runs.json` together.

## Report a wrong fact

Open an issue quoting the sentence and a primary source (a standard, the language's official documentation, or the author's own account). All prose lives in `_src/content.py`.

## Pull requests

Keep each one to a single change, say how you checked it, and use an imperative commit message (`Fix off-by-one in reverse.c`).
