# R0 evidence: LearnC as inherited (commit f830dbe)

Measured by the conductor on 2026-11-11, gcc 13.3.0 (Ubuntu 24.04, x86_64).

## What exists
- No website. The repo is a README, LICENSE, CONTRIBUTING and 9 `.c` files in 6 folders:
  `basic_concepts/` (hello_world, variables, conditionals, loops, simple_function), `arrays/`, `pointers/`, `structs/`, `file_io/read_file.c`.
- Only C. No C++, Objective-C, C# or HolyC material anywhere.
- README.md lists a `functions/` folder (README line 9). `ls` shows no such folder; the function example is `basic_concepts/simple_function.c`.
- README gives no output for any example; a reader cannot see what a program prints without compiling it.

## Each example compiled with `gcc -std=c17 -Wall -Wextra` and run
| file | warnings | output |
|---|---|---|
| hello_world.c | 0 | `Hello, World!` |
| variables.c | 0 | `Age: 25` / `Height: 5.90` / `Grade: A` |
| conditionals.c | 0 | `The number is positive.` |
| loops.c | 0 | `Iteration number: 0` .. `4` |
| simple_function.c | 0 | `The sum is: 30` |
| arrays_example.c | 0 | `numbers[0] = 1` .. `numbers[4] = 5` |
| pointers_example.c | 0 | two addresses, e.g. `0x7ffd6eac170c`, differ every run (ASLR) |
| structs_example.c | 0 | `Name: John` / `Age: 30` |
| read_file.c | 0 | `Could not open the file.` exit 1: `example.txt` is not in the repo |

## A real bug in read_file.c (line 12: `char ch; while ((ch = fgetc(file)) != EOF)`)
`fgetc` returns `int` so it can return EOF (-1) distinct from every byte. Stored in `char`:
- with `-funsigned-char` (the default on ARM: Raspberry Pi, Android), EOF becomes 255 and never equals -1: the loop never ends and prints `\377` forever (measured: `timeout 2` killed it after printing `hi\n` then a stream of 0xFF bytes).
- with signed char (x86 default), a file containing the byte 0xFF stops early: input `a\xffb\n` printed only `a`.
gcc -Wall -Wextra gives no warning for it.

## Style notes
- Every example uses `int main()` (empty parens). Before C23 that declares a function with unspecified parameters; `int main(void)` is the portable form.
