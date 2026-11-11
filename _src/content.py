"""Every word on the site that is not generated from examples/ lives here."""

LANGS = [
    {
        "id": "c", "name": "C", "year": "1972", "by": "Dennis Ritchie",
        "where": "Bell Labs", "ext": "c", "page": "c/index.html",
        "tag": "The root. Memory is yours to manage.",
        "parent": "B",
    },
    {
        "id": "cpp", "name": "C++", "year": "1985", "by": "Bjarne Stroustrup",
        "where": "Bell Labs", "ext": "cpp", "page": "cpp.html",
        "tag": "C with classes, templates and destructors.",
        "parent": "C",
    },
    {
        "id": "objc", "name": "Objective-C", "year": "1984", "by": "Brad Cox, Tom Love",
        "where": "PPI", "ext": "m", "page": "objc.html",
        "tag": "C plus Smalltalk-style messages.",
        "parent": "C",
    },
    {
        "id": "csharp", "name": "C#", "year": "2000", "by": "Anders Hejlsberg",
        "where": "Microsoft", "ext": "cs", "page": "csharp.html",
        "tag": "C syntax on a managed runtime.",
        "parent": "C",
    },
    {
        "id": "holyc", "name": "HolyC", "year": "2003–13", "by": "Terry A. Davis",
        "where": "TempleOS", "ext": "HC", "page": "holyc.html",
        "tag": "C as the shell of a whole operating system.",
        "parent": "C",
    },
]

ANCESTORS = [
    {"name": "BCPL", "year": "1967", "by": "Martin Richards", "where": "Cambridge"},
    {"name": "B", "year": "1969", "by": "Ken Thompson", "where": "Bell Labs"},
]

# C lessons: (file stem in examples/c, slug, title, one line, notes html)
LESSONS = [
    ("01_hello", "hello", "Hello, World",
     "The smallest whole program: one include, one function, one call.",
     """<p><code>#include &lt;stdio.h&gt;</code> pastes in the <em>declarations</em> (the names
     and argument types) of the standard input/output library, which is where
     <code>printf</code> lives. Every C program starts running at <code>main</code>. Its
     <code>int</code> return value goes back to the <em>shell</em>, the program you typed the
     command into: 0 means success.</p>
     <p>Under every program on this site, the dark box shows what it printed. Its header
     gives the exit code (<code>exit 0</code> is success) and the number of compiler
     warnings.</p>
     <p>Write <code>main(void)</code>, not <code>main()</code>. Before C23 (the 2024 C
     standard), empty parentheses declared a function whose parameters were
     <em>unspecified</em>, not absent.</p>"""),
    ("02_variables", "variables", "Variables and types",
     "Each variable has a type, and each type has a size in bytes.",
     """<p>A <em>bit</em> is a single 0 or 1; a <em>byte</em> is 8 bits, enough for a number from
     0 to 255. In <code>printf</code>, each <code>%</code> code prints the next argument:
     <code>%d</code> an <code>int</code>, <code>%c</code> a character, <code>%.2f</code> a
     <code>double</code> with two decimals, and <code>%zu</code> a size such as
     <code>sizeof</code> gives.</p>
     <p>A <code>char</code> is one byte holding a character code: <code>'A'</code> is 65.
     <code>sizeof</code> tells you how many bytes a type or variable takes on <em>this</em>
     machine. The C standard sets minimums, not exact sizes.</p>
     <p><code>float</code> and <code>double</code> hold numbers with a fractional part;
     <code>double</code> has twice the precision. An earlier version of this lesson stored 5.9
     in a <code>float</code>, which actually holds 5.900000095&hellip;, and
     <code>%.2f</code> (print with two decimals) hid the difference. Use <code>double</code>
     unless you have a reason not to.</p>"""),
    ("03_conditionals", "conditionals", "Conditionals",
     "if, else if and else, run on three inputs instead of one.",
     """<p>Two things here are taught later: the <code>for</code> loop (lesson 04), which runs
     <code>sign</code> once for each of the three numbers in the array
     <code>samples</code> (lesson 06). Read it as &ldquo;for each number, print its
     sign&rdquo;. <code>static</code> keeps the function private to this file (lesson 05),
     and <code>%s</code> in <code>printf</code> prints a piece of text.</p>
     <p>Conditions in C are integers: 0 is false and anything else is true. The function
     returns a <code>const char *</code>: a piece of text that the program never changes.
     <a href="10-strings.html">Lesson 10</a> explains why text is written with a
     <code>*</code>.</p>"""),
    ("04_loops", "loops", "Loops",
     "A counted for loop, then a while loop that runs until its condition fails.",
     """<p><code>for (init; test; step)</code> is shorthand for a <code>while</code> loop. The
     second loop follows the Collatz rule from 27. Nobody can tell in advance how many steps
     it will take, which is exactly what <code>while</code> is for.</p>"""),
    ("05_functions", "functions", "Functions",
     "Declare, define, call, and recurse.",
     """<p>The declaration (the prototype) lets <code>main</code> call <code>add</code> before
     its body appears. <code>static</code> on a function means it is visible only inside this
     file. <code>factorial</code> calls itself, so each call gets its own copy of
     <code>n</code> on the stack.</p>"""),
    ("06_arrays", "arrays", "Arrays",
     "A row of same-type values in one block of memory, and how to count them.",
     """<p><code>sizeof numbers / sizeof numbers[0]</code> computes the element count at
     compile time, but only where the array is still an array. Once it is passed to a
     function it decays to a pointer and the trick fails.</p>
     <p>C does not check indexes. <code>numbers[5]</code> compiles, then reads whatever
     happens to follow the array.</p>"""),
    ("07_pointers", "pointers", "Pointers",
     "A variable that holds an address, and the swap that needs one.",
     """<p><code>&amp;num</code> is the address of <code>num</code>, and <code>*ptr</code> is
     the value stored there. Writing through <code>*ptr</code> changes <code>num</code>
     itself. C passes every argument by value, so <code>swap</code> can only reach the
     caller's variables when it is given their addresses.</p>
     <p>An earlier version of this lesson printed raw addresses with <code>%p</code>. Those change on
     every run (address space layout randomisation), and passing an <code>int *</code> to
     <code>%p</code> without a <code>(void *)</code> cast is a warning under
     <code>-Wpedantic</code>. This version compares the pointers instead.</p>"""),
    ("08_structs", "structs", "Structs",
     "Group fields into one type, and change it through a pointer.",
     """<p><code>p-&gt;age</code> is shorthand for <code>(*p).age</code>. The struct is 56
     bytes, not 54 (50 + 4), because the compiler pads it so that an array of
     <code>Person</code> keeps every <code>int</code> aligned.</p>"""),
    ("09_file_io", "file-io", "Files",
     "Write a file, read it back, and the bug the original example had.",
     """<p>The original <code>read_file.c</code> declared <code>char ch</code> and compared
     it with <code>EOF</code>. <code>fgetc</code> returns an <code>int</code>, either a byte
     from 0 to 255 or <code>EOF</code> (-1), and a <code>char</code> cannot hold all 257
     values. We reproduced both failures with gcc 13 on x86:</p>
     <ul>
       <li><strong>Where <code>char</code> is unsigned</strong> (the default on ARM: Raspberry
       Pi, Android; simulated here with <code>-funsigned-char</code>), EOF becomes 255, which never equals -1. The loop never ends and prints
       <code>\\377</code> forever.</li>
       <li><strong>Where <code>char</code> is signed</strong> (x86), a file containing the
       byte 0xFF stops early. The input <code>a\\xffb</code> printed only
       <code>a</code>.</li>
     </ul>
     <p><code>gcc -Wall -Wextra</code> does not warn about it; adding
     <code>-Wconversion</code> does (&ldquo;conversion from &lsquo;int&rsquo; to
     &lsquo;char&rsquo; may change value&rdquo;), which is why every C program here is built
     with it. The repo also lacked <code>example.txt</code>, so the old program only ever
     printed &ldquo;Could not open the file.&rdquo; This version writes its own file
     first.</p>"""),
    ("10_strings", "strings", "Strings",
     "A string is a char array with a zero byte at the end.",
     """<p><code>"pointer"</code> is 7 characters but 8 bytes, because of the terminating
     <code>'\\0'</code>. <code>strlen</code> counts up to the zero byte, while
     <code>sizeof</code> measures the whole array.</p>"""),
    ("11_malloc", "malloc", "The heap",
     "Ask for memory at run time, and give it back.",
     """<p><code>malloc</code> returns memory that lives until you <code>free</code> it, or
     <code>NULL</code> if there is none. Writing <code>sizeof *squares</code> rather than
     <code>sizeof(int)</code> keeps the size right if the type ever changes. Setting the
     pointer to <code>NULL</code> after <code>free</code> turns an accidental later use into
     a clean crash instead of silent corruption.</p>"""),
    ("12_sum", "sum", "Putting it together",
     "Add up 1 to 10. The same program is written in every language on the Rosetta page.",
     """<p>This is the second of the five Rosetta programs. See it in C++, Objective-C, C#
     and HolyC on the <a href="../rosetta.html#sum">Rosetta page</a>.</p>"""),
]

ROSETTA = [
    ("hello", "Hello, World", "Print one line."),
    ("sum", "Sum 1 to 10", "A loop, or the library's way of avoiding one. Prints 55."),
    ("point", "A point", "A record type with x and y, and its distance from the origin. Prints 5.0."),
    ("swap", "Swap", "Exchange two variables through a function: pointers, references or ref."),
    ("reverse", "Reverse a string", "Reverse “pointer” in place. Prints retniop."),
]

# Per-language page copy. examples: (path under examples/<id>/, title, html note)
PAGES = {
    "cpp": {
        "title": "C++",
        "lede": "Bjarne Stroustrup began “C with Classes” at Bell Labs in 1979. It was renamed C++ in 1983 and released commercially in 1985. It keeps almost all of C and adds what C leaves to you: types that clean up after themselves, generic code, and a large standard library.",
        "adds": [
            ("Destructors and RAII", "A resource is released when the object that owns it goes out of scope. There is no <code>free</code> to forget."),
            ("References", "<code>int &amp;a</code> is another name for an existing variable. It is never null and never reseated."),
            ("Templates", "One definition, compiled separately for every type it is used with."),
            ("Classes and virtual functions", "Inheritance, and calls dispatched at run time through a table of pointers."),
            ("The standard library", "<code>vector</code>, <code>string</code>, <code>map</code> and the algorithms that work on them."),
        ],
        "examples": [
            ("01_raii.cpp", "RAII: release in reverse order", "Read the output from the bottom up: <code>b</code> is released when its block closes, and <code>a</code> when <code>main</code> returns. Nothing calls a release function."),
            ("02_templates.cpp", "Templates", "<code>largest</code> is compiled three times: for <code>int</code>, <code>double</code> and <code>std::string</code>. With strings, <code>&gt;</code> compares alphabetically, so <code>\"C++\"</code> beats <code>\"C\"</code>."),
            ("03_containers.cpp", "Containers and algorithms", "<code>std::sort</code> orders by character code, so <code>\"C#\"</code> (0x23) sorts before <code>\"C++\"</code> (0x2B)."),
            ("04_classes.cpp", "Classes and dynamic dispatch", "Each <code>s-&gt;area()</code> call is resolved at run time through the object's virtual table."),
        ],
        "history": [("1979", "C with Classes begins at Bell Labs"), ("1983", "renamed C++"), ("1985", "first commercial release and the first edition of <cite>The C++ Programming Language</cite>"), ("1998", "first ISO standard, C++98"), ("2011", "C++11: move semantics, lambdas, <code>auto</code>"), ("2024", "C++23 published as ISO/IEC 14882:2024")],
        "docs": [("isocpp.org", "https://isocpp.org/"), ("cppreference: C++", "https://en.cppreference.com/w/cpp")],
    },
    "objc": {
        "title": "Objective-C",
        "lede": "Brad Cox and Tom Love added Smalltalk's message passing to C in the early 1980s. NeXT licensed it in 1988, and through NeXTSTEP it became the language of Mac OS X and iOS until Swift arrived in 2014. Every C program is a valid Objective-C program.",
        "adds": [
            ("Messages", "<code>[object message:arg]</code> is looked up at run time, not bound at compile time."),
            ("nil is safe to message", "Sending a message to <code>nil</code> returns zero instead of crashing."),
            ("Categories", "Add methods to a class you did not write, without subclassing it."),
            ("Introspection", "Ask an object at run time whether it responds to a selector."),
        ],
        "examples": [
            ("01_messages.m", "Messages and nil", "Each <code>toggle</code> returns <code>self</code>, so messages can be chained. The last line sends <code>isOn</code> to <code>nil</code> and gets 0 back."),
            ("02_categories.m", "Categories and introspection", "<code>shout</code> is added by a category in a separate <code>@interface</code>/<code>@implementation</code> pair. <code>@selector(fly)</code> names a method that does not exist, and the runtime says so."),
            ("Root.h", "The root class", "On Apple platforms, classes inherit from <code>NSObject</code> in Foundation. Foundation is not part of this toolchain (clang with the GNU runtime, <code>libobjc</code>), so this small root class stands in. It allocates with <code>class_createInstance</code> and answers <code>respondsTo:</code>."),
        ],
        "history": [("1984", "first appears at Productivity Products International (PPI), later renamed Stepstone"), ("1986", "Cox's book <cite>Object-Oriented Programming: An Evolutionary Approach</cite>"), ("1988", "licensed by NeXT"), ("2007", "Objective-C 2.0 with Mac OS X Leopard"), ("2014", "Apple introduces Swift as its successor")],
        "docs": [("Apple: Programming with Objective-C (archive)", "https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html"), ("GCC: GNU Objective-C runtime", "https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html")],
    },
    "csharp": {
        "title": "C#",
        "lede": "Anders Hejlsberg's team at Microsoft announced C# in 2000, and version 1.0 shipped with .NET in 2002. It has C's braces and operators but runs on a managed runtime: a garbage collector frees memory, and indexes are checked.",
        "adds": [
            ("Garbage collection", "Objects are freed when nothing refers to them. There is no <code>free</code> and no <code>delete</code>."),
            ("Value and reference types", "<code>struct</code> copies like C; <code>class</code> copies the reference."),
            ("Properties and exceptions", "Fields guarded by code, and errors that cannot be silently ignored."),
            ("LINQ", "Queries over any collection: <code>Where</code>, <code>OrderBy</code>, <code>Select</code>."),
        ],
        "examples": [
            ("01_classes.cs", "Classes, properties, exceptions", "<code>Balance</code> can be read anywhere but only set inside <code>Account</code>. The negative deposit throws, and the catch reports it."),
            ("02_linq.cs", "LINQ", "Filter, sort and project in one expression over an array of anonymous objects."),
            ("03_value_vs_reference.cs", "Value or reference", "The same code does two different things: the struct copy leaves <code>s1</code> alone, but the class copy shares one object."),
        ],
        "history": [("2000", "announced by Microsoft"), ("2002", "C# 1.0 with .NET Framework 1.0"), ("2007", "C# 3.0 adds LINQ and lambdas"), ("2016", ".NET Core: C# runs on Linux and macOS"), ("2025", "C# 14 with .NET 10")],
        "docs": [("Microsoft Learn: C#", "https://learn.microsoft.com/en-us/dotnet/csharp/"), ("ECMA-334, the C# standard", "https://ecma-international.org/publications-and-standards/standards/ecma-334/")],
        "note": "These examples were compiled with Mono's <code>mcs</code>, which implements C# up to about version 7, so they avoid newer syntax such as records and top-level statements. They were not tested on Microsoft's .NET.",
    },
    "holyc": {
        "title": "HolyC",
        "lede": "Terry A. Davis (1969–2018) wrote HolyC for his own operating system, which he developed alone from 2003 and named TempleOS in 2013. HolyC is both the system's programming language and its shell: you type HolyC at the prompt and it is compiled just in time and run.",
        "adds": [
            ("No main", "Statements at the top level of a file run when the file is included."),
            ("A string is a print", "A string literal on its own is printed. Follow it with arguments and it is formatted."),
            ("Default arguments", "Any parameter can have a default, and you can skip it in the middle: <code>Greet(, 3)</code>."),
            ("Calls without parentheses", "A call with no arguments can drop the <code>()</code>."),
            ("Explicit types", "<code>I64</code>, <code>U8</code>, <code>F64</code> and <code>U0</code> (void) say their size in their name."),
        ],
        "examples": [
            ("01_default_args.HC", "Default arguments", "Three calls to one function: with no arguments, with both, and with the first one skipped."),
            ("02_null_case.HC", "A switch with null cases", "From the TempleOS source. A <code>case:</code> with no number takes the previous case's number plus one."),
        ],
        "history": [("2003", "Davis begins the operating system"), ("2013", "it is named TempleOS; HolyC is its only language"), ("2017", "the last TempleOS release, V5.03")],
        "docs": [("Run HolyC in your browser: holyc.shadw.app", "https://holyc.shadw.app"), ("TempleOS", "https://templeos.org/")],
        "note": "<strong>Not run here.</strong> HolyC is compiled by TempleOS itself, and no HolyC compiler was available in the build environment, so the HolyC programs on this site are shown as source only, with no output. You can run HolyC in your browser at holyc.shadw.app, or inside TempleOS in a virtual machine.",
    },
}

FAMILY = [
    # (year, name, note, lane) lane: anc, c, child, cousin
    (1967, "BCPL", "Martin Richards, Cambridge. Typeless: everything is a machine word.", "anc"),
    (1969, "B", "Ken Thompson, Bell Labs. BCPL cut down to fit a PDP-7.", "anc"),
    (1972, "C", "Dennis Ritchie adds types to B. In 1973 Unix is rewritten in it.", "c"),
    (1978, "K&R C", "<cite>The C Programming Language</cite> by Kernighan and Ritchie becomes the de facto standard.", "c"),
    (1984, "Objective-C", "Cox and Love add Smalltalk messages to C.", "child"),
    (1985, "C++", "Stroustrup's C with Classes ships commercially.", "child"),
    (1989, "C89", "ANSI X3.159-1989; adopted by ISO as C90 in 1990.", "c"),
    (1995, "Java", "Sun. Borrows C's syntax for a virtual machine.", "cousin"),
    (1999, "C99", "<code>//</code> comments, <code>&lt;stdint.h&gt;</code>, declarations anywhere.", "c"),
    (2000, "C#", "Microsoft. C syntax on the .NET runtime.", "child"),
    (2001, "D", "Walter Bright. A redesign of C++.", "cousin"),
    (2003, "HolyC", "Terry A. Davis starts the OS that becomes TempleOS.", "child"),
    (2009, "Go", "Google; Ken Thompson is one of its three designers.", "cousin"),
    (2011, "C11", "Threads, atomics and <code>_Generic</code>.", "c"),
    (2016, "Zig", "Andrew Kelley. Aims to replace C, and can compile C.", "cousin"),
    (2018, "C17", "A bug-fix revision of C11.", "c"),
    (2024, "C23", "ISO/IEC 9899:2024: <code>bool</code>, <code>nullptr</code> and <code>constexpr</code> keywords, and <code>()</code> now means <code>(void)</code>.", "c"),
]

# Sentences in the prose above that quote a program's output; the build checks each one.
QUOTED_OUTPUTS = [
    ("cpp/02_templates.cpp", "C++"),
    ("c/04_loops.c", "27 reaches 1 in 111 Collatz steps"),
    ("c/08_structs.c", "sizeof(struct Person) = 56 bytes"),
    ("c/08_structs.c", "Age: 31"),
    ("c/10_strings.c", "retniop (7 chars, 8 bytes)"),
    ("cpp/03_containers.cpp", "C# 2000"),
]
