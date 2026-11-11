# LearnC: C and the languages that grew from it

A static website about C and its family: **C, C++, Objective-C, C# and HolyC**. It has twelve C lessons, the same five programs in all five languages (Rosetta), and the family tree from BCPL (1967) to C23 (2024).

Every C, C++, Objective-C and C# program on the site was compiled with all warnings switched on and run when the site was built. Each page shows the program's real output and the exact command that produced it. HolyC programs are shown as source and marked *not run here*, because HolyC compiles inside TempleOS (try them at [holyc.shadw.app](https://holyc.shadw.app)).

## Layout

```
examples/
  c/          12 lessons (01_hello.c … 12_sum.c) + rosetta/
  cpp/        C++ examples + rosetta/
  objc/       Objective-C examples + rosetta/, Root.h/Root.m (a root class for the GNU runtime)
  csharp/     C# examples + rosetta/
  holyc/      HolyC examples + rosetta/ (not compiled)
_src/
  content.py  every sentence on the site that is not generated
  build.py    compiles + runs examples, writes site/, checks links
  runs.json   cached compiler output (used when a toolchain is missing)
  measure.cjs screenshots + layout measurements (Playwright)
site/         the deployable static site (committed)
```

## Run one example yourself

```bash
cd examples/c
gcc -std=c17 -Wall -Wextra -Wpedantic -Wstrict-prototypes -Wconversion 01_hello.c -o hello -lm && ./hello
```

The command for every other example is printed under it on the site.

## Rebuild the site

```bash
python3 _src/build.py          # compile, run, write site/
python3 _src/build.py --no-run # reuse _src/runs.json
```

The build needs `gcc`, `g++`, `clang` with GNU `libobjc` (installed with gcc), and Mono (`mcs`, `mono`). If one of them is missing, the build reuses that language's cached results in `_src/runs.json`. It exits with an error if any program warns, fails, or exits non-zero, or if any local link is dead.

## Deploy

A plain static site with no build step on the host. `vercel.json` serves `site/` whether the project root is the repo or `site/`, and the root `index.html` redirects to `site/` for other static hosts.

## Design

The text column is 80 characters of the code font wide, the width of a terminal. The home page draws the whole site as a C pointer diagram. The decisions and the critique rounds are in [DESIGN-LOG.md](DESIGN-LOG.md), and the critics' reports are in `panel/`.

## Licence

MIT, see [LICENSE](LICENSE). Exception: `examples/holyc/02_null_case.HC` is from TempleOS and is in the public domain. Fonts: Newsreader and JetBrains Mono, SIL Open Font Licence.
