#!/usr/bin/env python3
"""Build the LearnC site.

1. Compile and run every program under examples/ with the real toolchains and
   record the result in _src/runs.json. If a toolchain is missing, the cached
   result is reused and the page says which compiler produced it.
2. Write the static site into site/.
3. Fail if any local link is dead or any C/C++/Objective-C/C# example warns.

Standard-library Python only.  Usage:  python _src/build.py [--no-run]
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
EX = ROOT / "examples"
OUT = ROOT / "site"
sys.path.insert(0, str(SRC))
import content as K  # noqa: E402

BUILT = ""
SITE_URL = "https://learnc.shadw.app"
FLAGS = {
    "c": "gcc -std=c17 -Wall -Wextra -Wpedantic -Wstrict-prototypes -Wconversion",
    "cpp": "g++ -std=c++20 -Wall -Wextra -Wpedantic -Wconversion",
    "objc": "clang -x objective-c -fobjc-runtime=gcc -Wall -Wextra -Wpedantic -Wconversion",
    "csharp": "mcs -warn:4",
}
VERSION_CMD = {
    "c": ["gcc", "--version"], "cpp": ["g++", "--version"],
    "objc": ["clang", "--version"], "csharp": ["mono", "--version"],
}


# --------------------------------------------------------------------------- run
def sh(cmd, cwd, timeout=20):
    p = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def shown_command(lang, rel):
    """The command a reader types, run from the file's own folder."""
    name = Path(rel).name
    stem = Path(rel).stem.split("_", 1)[-1] if lang != "csharp" else Path(rel).stem
    if lang == "c":
        return f"{FLAGS['c']} {name} -o {stem} -lm && ./{stem}"
    if lang == "cpp":
        return f"{FLAGS['cpp']} {name} -o {stem} && ./{stem}"
    if lang == "objc":
        root = "Root.m"
        return (f'{FLAGS["objc"]} -I"$(gcc -print-file-name=include)" {name} {root} '
                f'-L"$(gcc -print-file-name=)" -o {stem} -lobjc -lm && ./{stem}')
    if lang == "csharp":
        return f"{FLAGS['csharp']} {name} -out:{stem}.exe && mono {stem}.exe"
    return None


def run_one(lang, path, tmp):
    rel = str(path.relative_to(EX))
    if lang == "holyc" or path.name in ("Root.h", "Root.m"):
        return None
    exe = Path(tmp) / (rel.replace("/", "_") + ".bin")
    if lang == "c":
        cc = f"{FLAGS['c']} {path} -o {exe} -lm"
    elif lang == "cpp":
        cc = f"{FLAGS['cpp']} {path} -o {exe}"
    elif lang == "objc":
        cc = (f'{FLAGS["objc"]} -I"$(gcc -print-file-name=include)" {path} {path.parent / "Root.m"} '
              f'-L"$(gcc -print-file-name=)" -o {exe} -lobjc -lm')
    else:
        cc = f"{FLAGS['csharp']} {path} -out:{exe}"
    code, so, se = sh(cc, tmp)
    warnings = [ln for ln in (so + se).splitlines() if "warning" in ln]
    if code != 0:
        return {"command": shown_command(lang, rel), "compiled": False, "stdout": "",
                "exit": code, "warnings": warnings, "error": se[-2000:]}
    rdir = tempfile.mkdtemp(dir=tmp)
    runner = f"mono {exe}" if lang == "csharp" else str(exe)
    code, so, se = sh(runner, rdir)
    return {"command": shown_command(lang, rel), "compiled": True, "stdout": so + se,
            "exit": code, "warnings": warnings}


def toolchain_ok(lang):
    return shutil.which(VERSION_CMD[lang][0]) is not None and (
        lang != "csharp" or shutil.which("mcs") is not None)


def run_all(do_run):
    cache_path = SRC / "runs.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {"runs": {}, "versions": {}}
    if not do_run:
        return cache
    tmp = tempfile.mkdtemp()
    for lang in ("c", "cpp", "objc", "csharp"):
        if not toolchain_ok(lang):
            print(f"  {lang}: toolchain missing, using cached results")
            continue
        _, so, se = sh(" ".join(VERSION_CMD[lang]), tmp)
        cache["versions"][lang] = (so or se).splitlines()[0].strip()
        cache["runs"] = {k: v for k, v in cache["runs"].items() if not k.startswith(lang + "/")}
        cache.setdefault("built", {})[lang] = time.strftime("%Y-%m-%d", time.gmtime())
        for p in sorted((EX / lang).rglob("*")):
            if p.is_file() and p.suffix in (".c", ".cpp", ".m", ".cs"):
                r = run_one(lang, p, tmp)
                if r:
                    cache["runs"][str(p.relative_to(EX))] = r
    shutil.rmtree(tmp, ignore_errors=True)
    cache_path.write_text(json.dumps(cache, indent=1, ensure_ascii=False) + "\n")
    return cache


# ------------------------------------------------------------------ highlighting
KW = {
    "c": "auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while size_t FILE NULL bool",
    "cpp": "auto bool break case char class const constexpr continue default delete do double else enum explicit for if int long namespace new nullptr operator override private protected public return sizeof static struct template this typename using virtual void while std",
    "objc": "auto break case char const double else for id if int return self sizeof static struct void while nil BOOL Class SEL @interface @implementation @end @selector",
    "csharp": "using class struct static void public private get set new var return if else try catch throw string int decimal double char bool this ref out foreach in",
    "holyc": "U0 U8 U16 U32 I64 I8 I16 I32 F64 Bool class union return if else for while switch case break default public extern",
}
TOKEN = re.compile(
    r'(?P<com>//[^\n]*|/\*.*?\*/)|(?P<str>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')'
    r'|(?P<pre>^[ \t]*#[a-z]+[^\n]*)|(?P<num>\b\d+(?:\.\d+)?m?\b)|(?P<word>@?[A-Za-z_]\w*)',
    re.S | re.M)


def highlight(src, lang):
    kws = set(KW[lang].split())
    out, pos = [], 0
    for m in TOKEN.finditer(src):
        out.append(html.escape(src[pos:m.start()]))
        t = m.group(0)
        e = html.escape(t)
        k = m.lastgroup
        if k == "com":
            out.append(f'<span class="tc">{e}</span>')
        elif k == "str":
            out.append(f'<span class="ts">{e}</span>')
        elif k == "pre":
            out.append(f'<span class="tp">{e}</span>')
        elif k == "num":
            out.append(f'<span class="tn">{e}</span>')
        elif t in kws:
            out.append(f'<span class="tk">{e}</span>')
        else:
            out.append(e)
        pos = m.end()
    out.append(html.escape(src[pos:]))
    return "".join(out)


# ------------------------------------------------------------------------ layout
NAV = [("index.html", "Home"), ("c/index.html", "C"), ("cpp.html", "C++"),
       ("objc.html", "Objective-C"), ("csharp.html", "C#"), ("holyc.html", "HolyC"),
       ("rosetta.html", "Rosetta"), ("family.html", "Family"), ("about.html", "About")]


PROTECT = re.compile(r"(<pre.*?</pre>|<code.*?</code>|<svg.*?</svg>|<samp.*?</samp>|<[^>]+>)", re.S)


def typeset(markup):
    """Typographer's apostrophes in prose; code, samples and tags are left alone."""
    # a long inline code span may wrap; a short one never breaks inside its token
    markup = re.sub(r"<code>([^<]{25,}?)</code>", r'<code class="w">\1</code>', markup)
    parts = PROTECT.split(markup)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"(?<=\w)(?:'|&#x27;)(?=\w)", "\u2019", parts[i])
        if i and parts[i - 1].startswith("<code") or i and parts[i - 1] == "</code>":
            parts[i] = re.sub(r"^(?:'|&#x27;)(?=\w)", "\u2019", parts[i])
    return "".join(parts)


def page(path, title, body, desc, active=None, wide=False):
    depth = path.count("/")
    up = "../" * depth
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links.append(f'<li><a href="{up}{href}"{cur}>{html.escape(label)}</a></li>')
    full_title = "LearnC" if title is None else f"{title} · LearnC"
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE_URL}/og.png">
<meta name="theme-color" content="#f4efe3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#14120f" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{up}fonts/jetbrains-mono.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{up}css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <a class="mark" href="{up}index.html" aria-label="LearnC home"><span class="mark-box">C</span><span>LearnC</span></a>
  <nav aria-label="Site"><ul>{''.join(links)}</ul></nav>
</header>
<main id="main" class="{'wide' if wide else ''}">
{typeset(body)}
</main>
<footer class="foot">
  <p><span class="mono">return 0;</span> Every C, C++, Objective-C and C# program on this site was compiled and run by the build on {BUILT}; HolyC is shown as source. <a href="{up}about.html">How</a> · <a href="https://github.com/SolutionsAsService/LearnC">Source on GitHub</a> · MIT licence</p>
</footer>
</body>
</html>
"""
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc)


# ---------------------------------------------------------------- code + output
def code_block(lang, rel, runs, title=None, up="", same=None):
    src = (EX / rel).read_text()
    r = runs["runs"].get(rel)
    name = Path(rel).name
    head = f'<figcaption><span class="fname">{html.escape(name)}</span>'
    if title:
        head += f' <span class="ftitle">{html.escape(title)}</span>'
    head += "</figcaption>"
    if same:
        body = "\n".join(f'<span class="same">{highlight(ln, lang)}</span>' if ln.strip() in same else highlight(ln, lang)
                         for ln in src.rstrip("\n").split("\n"))
    else:
        body = highlight(src, lang)
    code = f'<pre class="code lang-{lang}"><code>{body}</code></pre>'
    if r and r.get("compiled"):
        out = html.escape(r["stdout"].rstrip("\n"))
        status = "exit 0" if r["exit"] == 0 else f"exit {r['exit']}"
        outb = (f'<div class="out"><div class="out-h"><span>output</span><span>{status} · '
                f'{len(r["warnings"])} warnings</span></div><pre><samp>{out}</samp></pre></div>')
        cmd = f'<details class="cmd" open><summary>Compile and run it yourself</summary><pre><code>{html.escape(r["command"])}</code></pre><p class="setup"><a download href="{up}examples/{rel}">Download {html.escape(name)}</a>{(" with <a download href=\"" + up + "examples/" + str(Path(rel).parent) + "/Root.h\">Root.h</a> and <a download href=\"" + up + "examples/" + str(Path(rel).parent) + "/Root.m\">Root.m</a> beside it") if lang == "objc" else ""}, open a terminal in the folder you saved it to, and paste the command. No compiler yet? <a href="{up}about.html#setup">How to get one</a>.</p></details>'
    elif lang == "holyc":
        outb = (f'<div class="out out-none"><div class="out-h"><span>output</span><span>not run here</span></div>'
                f'<p>Paste it into <a href="https://holyc.shadw.app">holyc.shadw.app</a> or a TempleOS shell.</p></div>')
        cmd = ""
    else:
        outb, cmd = "", ""
    return f'<figure class="ex lang-{lang}">{head}<div class="ex-body">{code}{outb}</div>{cmd}</figure>'


def lines_of(rel):
    return sum(1 for ln in (EX / rel).read_text().splitlines() if ln.strip())


def rosetta_rel(lang, prog):
    ext = {"c": "c", "cpp": "cpp", "objc": "m", "csharp": "cs", "holyc": "HC"}[lang]
    return f"{lang}/rosetta/{prog}.{ext}"


def ran(runs, rel):
    r = runs["runs"].get(rel)
    return bool(r and r.get("compiled") and r["exit"] == 0)


# ----------------------------------------------------------------------- hero SVG
def esc(s):
    return html.escape(s, quote=True)


def struct_box(x, y, w, h, lang, rows, href, title_size=30, band=44, kw=True):
    """A struct drawn the way C textbooks draw one: a name band and field rows.
    Returns the svg and the y centre of each row, so pointers can start at a field."""
    rh = (h - band) / len(rows)
    label = f"{LNAME[lang]}: " + ", ".join(f"{k} {re.sub('<[^>]+>', '', v)}" for k, v in rows if v != "●")
    parts = [f'<a href="{href}" class="node node-{lang}" aria-label="{esc(label)}">']
    parts.append(f'<rect class="box" x="{x}" y="{y}" width="{w}" height="{h}"/>')
    parts.append(f'<rect class="band" x="{x}" y="{y}" width="{w}" height="{band}"/>')
    if kw:
        parts.append(f'<text class="kw" x="{x + 12}" y="{y + band - 14}">struct lang</text>')
        parts.append(f'<text class="nm" x="{x + w - 12}" y="{y + band - 10}" text-anchor="end" font-size="{title_size}">{esc(LNAME[lang])}</text>')
    else:
        parts.append(f'<text class="nm" x="{x + 12}" y="{y + band / 2 + title_size * .36}" font-size="{title_size}">{esc(LNAME[lang])}</text>')
    centres = []
    for i, (k, v) in enumerate(rows):
        ry = y + band + i * rh
        if i:
            parts.append(f'<line class="rule" x1="{x}" y1="{ry}" x2="{x + w}" y2="{ry}"/>')
        parts.append(f'<text class="fk" x="{x + 12}" y="{ry + rh / 2 + 5}">{esc(k)}</text>')
        if v == "●":
            parts.append(f'<circle class="pdot" cx="{x + 100}" cy="{ry + rh / 2}" r="5"/>')
        else:
            parts.append(f'<text class="fv" x="{x + 92}" y="{ry + rh / 2 + 5}">{v}</text>')
        centres.append(ry + rh / 2)
    parts.append(f'<rect class="frame" x="{x}" y="{y}" width="{w}" height="{h}"/>')
    parts.append("</a>")
    return "".join(parts), centres, rh


LNAME = {l["id"]: l["name"] for l in K.LANGS}


def arrow(path_d, cls="ptr"):
    return f'<path class="{cls}" d="{path_d}" marker-end="url(#ah)"/>'


def hero_desktop(runs):
    W, H = 1200, 548
    s = [f'<svg class="hero-svg hero-wide" viewBox="0 0 {W} {H}" role="group" aria-labelledby="hero-t" aria-describedby="hero-d">',
         '<title id="hero-t">The C family as a pointer diagram</title>',
         '<desc id="hero-d">C is the root struct. C++, Objective-C, C# and HolyC each point to C through a parent pointer; C points to B, B to BCPL, and BCPL to NULL. C also points to an array of twelve lessons; the Rosetta array holds five programs written in all five languages.</desc>',
         '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>']
    # ancestors, left column; their parent pointers run up the left margin
    s.append('<a href="family.html" class="node node-anc" aria-label="Ancestors: BCPL 1967 and B 1969. The family timeline">')
    for i, a in enumerate(K.ANCESTORS):
        y = 34 + i * 116
        s.append(f'<rect class="box" x="20" y="{y}" width="176" height="80"/>')
        s.append(f'<text class="nm" x="34" y="{y + 33}" font-size="24">{esc(a["name"])}</text>')
        s.append(f'<text class="fv" x="182" y="{y + 32}" text-anchor="end">{a["year"]}</text>')
        s.append(f'<text class="fk" x="34" y="{y + 62}">{esc(a["by"])}</text>')
    s.append('<text class="cap" x="20" y="270">ancestors → Family</text>')
    s.append('<rect class="frame" x="14" y="28" width="188" height="248"/>')
    s.append("</a>")
    s.append('<path class="ptr" d="M108,34 L108,14 L150,14"/><text class="null" x="158" y="19">NULL</text>')
    s.append(arrow("M108,150 L108,118"))
    # C: the root, with an oversized name (Weingart counterpoint)
    cx, cy, cw, ch = 262, 34, 360, 244
    c_rel = rosetta_rel("c", "hello")
    rows = [("year", "1972 · Bell Labs"), ("by", "Dennis Ritchie"),
            ("hello", f"{lines_of(c_rel)} lines · ran ✓" if ran(runs, c_rel) else f"{lines_of(c_rel)} lines"),
            ("parent", "●"), ("lessons", "●")]
    svg, cen, rh = struct_box(cx, cy, cw, ch, "c", rows, "c/index.html", title_size=94, band=84)  # S4 push: the root glyph
    s.append(svg)
    py, ly = cen[3], cen[4]
    # C.parent -> B: leave along the rule under the row, out of the left edge
    s.append(arrow(f"M{cx + 100},{py} L{cx + 100},{py + rh / 2} L{cx - 30},{py + rh / 2} L{cx - 30},{34 + 116 + 40} L{200},{34 + 116 + 40}"))
    # C.lessons -> lessons array
    ax, ay, cell = 682, 64, 41.5
    s.append(arrow(f"M{cx + 100},{ly} L{cx + cw + 30},{ly} L{cx + cw + 30},{ay + 23} L{ax - 3},{ay + 23}"))
    s.append(f'<text class="cap" x="{ax}" y="{ay - 14}">lessons[{len(K.LESSONS)}] → the C course</text>')
    for i, les in enumerate(K.LESSONS):
        x = ax + i * cell
        s.append(f'<a href="c/{les[0][:2]}-{les[1]}.html" class="cell" aria-label="C lesson {i + 1}: {esc(les[2])}"><title>{esc(les[2])}</title>'
                 f'<rect class="box" x="{x}" y="{ay}" width="{cell}" height="46"/>'
                 f'<text class="ci" x="{x + cell / 2}" y="{ay + 29}" text-anchor="middle">{i + 1:02d}</text></a>')
    rx, ry, rw = 682, 180, 99.6
    s.append(f'<text class="cap" x="{rx}" y="{ry - 14}">rosetta[{len(K.ROSETTA)}] → one program, five languages</text>')
    for i, (slug, t, _) in enumerate(K.ROSETTA):
        x = rx + i * rw
        s.append(f'<a href="rosetta.html#{slug}" class="cell" aria-label="Rosetta: {esc(t)} in five languages"><title>{esc(t)}</title>'
                 f'<rect class="box" x="{x}" y="{ry}" width="{rw}" height="46"/>'
                 f'<text class="ci" x="{x + rw / 2}" y="{ry + 29}" text-anchor="middle">{slug}</text></a>')
    # children: four structs; each parent pointer leaves through the gap to its right
    kids = K.LANGS[1:]
    bw, bh, by = 266, 196, 344
    gap = (W - 40 - 4 * bw) / 3
    for i, L in enumerate(kids):
        x = 20 + i * (bw + gap)
        rel = rosetta_rel(L["id"], "hello")
        status = "ran ✓" if ran(runs, rel) else "not run"
        rows = [("year", f'{esc(L["year"])} · {esc(L["where"])}'), ("by", esc(L["by"])),
                ("hello", f"{lines_of(rel)} lines · {status}"), ("parent", "●")]
        svg, cen, rh = struct_box(x, by, bw, bh, L["id"], rows, L["page"], title_size=26, kw=False)
        s.append(svg)
        gx = x + bw + min(gap / 2, 10)
        hy = 318 - i * 9  # the farther right, the higher the elbow: no two pointers cross
        tx = cx + 70 + i * 74
        s.append(arrow(f"M{x + 100},{cen[3]} L{gx},{cen[3]} L{gx},{hy} L{tx},{hy} L{tx},{cy + ch + 3}"))
    s.append("</svg>")
    return "".join(s)


def hero_narrow(runs):
    """The phone drawing: same notation, re-laid so that no wire crosses text or a cell."""
    W, H = 360, 602
    s = [f'<svg class="hero-svg hero-narrow" viewBox="0 0 {W} {H}" role="group" aria-labelledby="hero-tn" aria-describedby="hero-dn">',
         '<title id="hero-tn">The C family as a pointer diagram</title>',
         '<desc id="hero-dn">C is the root struct. C++, Objective-C, C# and HolyC each point to C; C points to B, B to BCPL, and BCPL to NULL. C also points to an array of twelve lessons; the Rosetta array holds five programs.</desc>',
         '<defs><marker id="ahn" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>']
    A = lambda d: f'<path class="ptr" d="{d}" marker-end="url(#ahn)"/>'
    # ancestors: B -> BCPL -> NULL
    s.append('<a href="family.html" class="node node-anc" aria-label="Ancestors: BCPL 1967 and B 1969. The family timeline">')
    s.append('<rect class="box" x="70" y="4" width="92" height="38"/><text class="nm" x="80" y="29" font-size="17">BCPL</text><text class="sm" x="154" y="28" text-anchor="end">1967</text>')
    s.append('<rect class="box" x="196" y="4" width="70" height="38"/><text class="nm" x="206" y="29" font-size="17">B</text><text class="sm" x="258" y="28" text-anchor="end">1969</text>')
    s.append('<rect class="frame" x="70" y="4" width="196" height="38"/></a>')
    s.append('<text class="null" x="16" y="28">NULL</text>')
    s.append(A("M70,23 L54,23"))
    s.append(A("M196,23 L166,23"))
    # C
    c_rel = rosetta_rel("c", "hello")
    s.append('<a href="c/index.html" class="node node-c" aria-label="C: year 1972, Bell Labs, by Dennis Ritchie. Overview and lessons">')
    s.append('<rect class="box" x="16" y="58" width="328" height="138"/><rect class="band" x="16" y="58" width="328" height="40"/>')
    s.append('<text class="kw" x="26" y="84">struct lang</text><text class="nm" x="336" y="92" text-anchor="end" font-size="40">C</text>')
    for i, (k, v) in enumerate([("year", "1972 · Bell Labs"), ("by", "Dennis Ritchie"), ("parent", ""), ("lessons", "")]):
        y = 98 + i * 24.5
        if i:
            s.append(f'<line class="rule" x1="16" y1="{y}" x2="344" y2="{y}"/>')
        s.append(f'<text class="sm" x="26" y="{y + 17}">{k}</text>')
        if v:
            s.append(f'<text class="fv sm-v" x="100" y="{y + 17}">{v}</text>')
        else:
            s.append(f'<circle class="pdot" cx="108" cy="{y + 12.25}" r="4.5"/>')
    s.append('<rect class="frame" x="16" y="58" width="328" height="138"/></a>')
    s.append(A("M108,159.25 L300,159.25 L300,23 L270,23"))        # C.parent -> B, clear of the text
    s.append(A("M108,183.75 L108,220"))                            # C.lessons -> lessons[0]
    s.append(f'<text class="sm" x="118" y="214">lessons[{len(K.LESSONS)}]</text>')
    cw = 39
    for i, les in enumerate(K.LESSONS):
        x, y = 16 + (i % 6) * cw, 222 + (i // 6) * 30
        s.append(f'<a href="c/{les[0][:2]}-{les[1]}.html" class="cell" aria-label="C lesson {i + 1}: {esc(les[2])}"><title>{esc(les[2])}</title>'
                 f'<rect class="box" x="{x}" y="{y}" width="{cw}" height="30"/>'
                 f'<text class="ci ci-s" x="{x + cw / 2}" y="{y + 20}" text-anchor="middle">{i + 1:02d}</text></a>')
    # children, 2 x 2; each parent wire runs in a gutter to C's border
    kids = K.LANGS[1:]
    for i, L in enumerate(kids):
        col, row = i % 2, i // 2
        x, y = 16 + col * 168, 302 + row * 124
        rel = rosetta_rel(L["id"], "hello")
        st = "ran ✓" if ran(runs, rel) else "not run"
        s.append(f'<a href="{L["page"]}" class="node node-{L["id"]}" aria-label="{esc(L["name"])}: year {esc(L["year"])}, by {esc(L["by"])}, hello {st}">')
        s.append(f'<rect class="box" x="{x}" y="{y}" width="160" height="112"/><rect class="band" x="{x}" y="{y}" width="160" height="32"/>')
        s.append(f'<text class="nm" x="{x + 10}" y="{y + 23}" font-size="18">{esc(L["name"])}</text>')
        s.append(f'<text class="fv sm-v" x="{x + 10}" y="{y + 50}">{esc(L["year"])}</text>')
        s.append(f'<text class="sm" x="{x + 10}" y="{y + 70}">{esc(L["by"].split(",")[0])}</text>')
        s.append(f'<text class="sm" x="{x + 10}" y="{y + 90}">hello: {st}</text>')
        s.append(f'<line class="rule" x1="{x}" y1="{y + 94}" x2="{x + 160}" y2="{y + 94}"/>')
        s.append(f'<text class="sm" x="{x + 10}" y="{y + 108}">parent</text><circle class="pdot" cx="{x + 70}" cy="{y + 104}" r="4.5"/>')
        s.append(f'<rect class="frame" x="{x}" y="{y}" width="160" height="112"/></a>')
        dy = y + 104
        if col == 0:   # up the middle gutter, under the array, into C's bottom edge
            gx, hy, tx = (178, 290, 270) if row == 0 else (182, 296, 288)
            s.append(A(f"M{x + 70},{dy} L{gx},{dy} L{gx},{hy} L{tx},{hy} L{tx},{199}"))
        else:          # up the right margin into C's right edge
            gx, ty = (350, 122) if row == 0 else (356, 140)
            s.append(A(f"M{x + 70},{dy} L{gx},{dy} L{gx},{ty} L{347},{ty}"))
    s.append(f'<text class="sm" x="16" y="566">rosetta[{len(K.ROSETTA)}]</text>')
    rw = 328 / 5
    for i, (slug, t, _) in enumerate(K.ROSETTA):
        x = 16 + i * rw
        s.append(f'<a href="rosetta.html#{slug}" class="cell" aria-label="Rosetta: {esc(t)} in five languages"><title>{esc(t)}</title>'
                 f'<rect class="box" x="{x:.1f}" y="572" width="{rw:.1f}" height="30"/>'
                 f'<text class="ci ci-s" x="{x + rw / 2:.1f}" y="592" text-anchor="middle">{slug}</text></a>')
    s.append("</svg>")
    return "".join(s)


FRAME = re.compile(r'<rect class="frame" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"/>')


def outset_frames(svg, d=6):
    """Focus frames sit outside their box, clear of any glyph inside it."""
    return FRAME.sub(lambda m: f'<rect class="frame" x="{float(m[1]) - d:g}" y="{float(m[2]) - d:g}" '
                               f'width="{float(m[3]) + 2 * d:g}" height="{float(m[4]) + 2 * d:g}"/>', svg)


# ------------------------------------------------------------- inner diagrams
def mem_panel(caption, cells, arrows, mid, said=None):
    """cells: (x, y, name, value) boxes; arrows: ((x1,y1),(x2,y2)) pointer wires."""
    s = [f'<figure class="mem"><svg viewBox="0 0 240 150" width="240" role="img" aria-labelledby="{mid}">'
         f'<title id="{mid}">{esc(said or caption)}</title>'
         f'<defs><marker id="{mid}h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>']
    for x, y, name, val in cells:
        s.append(f'<text class="fk" x="{x}" y="{y - 8}">{esc(name)}</text>'
                 f'<rect class="box" x="{x}" y="{y}" width="70" height="40"/>')
        if val == "●":
            s.append(f'<circle class="pdot" cx="{x + 35}" cy="{y + 20}" r="5"/>')
        else:
            s.append(f'<text class="fv" x="{x + 35}" y="{y + 26}" text-anchor="middle">{esc(val)}</text>')
    for (x1, y1), (x2, y2) in arrows:
        s.append(f'<path class="ptr" d="M{x1},{y1} C{x1},{y1 + 40} {x2},{y2 + 40} {x2},{y2}" marker-end="url(#{mid}h)"/>')
    s.append(f'</svg><figcaption><code>{esc(caption)}</code></figcaption></figure>')
    return "".join(s)


POINTER_DIAGRAM = ('<div class="mems" aria-label="Memory, drawn in three steps">'
    + mem_panel("int *ptr = &num;", [(20, 30, "num", "10"), (150, 30, "ptr", "●")], [((185, 50), (55, 72))], "m1", "ptr holds the address of num; num is 10")
    + mem_panel("*ptr = 42;", [(20, 30, "num", "42"), (150, 30, "ptr", "●")], [((185, 50), (55, 72))], "m2", "writing through ptr changes num to 42")
    + mem_panel("swap(&x, &y);", [(20, 30, "x", "2"), (150, 30, "y", "1"), (20, 100, "a", "●"), (150, 100, "b", "●")],
                [], "m3", "inside swap, a points to x and b points to y; after the swap x is 2 and y is 1").replace("</svg>", '<path class="ptr" d="M55,120 L55,74" marker-end="url(#m3h)"/><path class="ptr" d="M185,120 L185,74" marker-end="url(#m3h)"/></svg>')
    + "</div>")


def struct_mem():
    """Lesson 08: the struct as one block of memory, changed through a pointer."""
    return ('<div class="mems mems-1"><figure class="mem"><svg viewBox="0 0 420 150" width="420" role="img" aria-labelledby="ms1">'
            '<title id="ms1">person1 is one struct with two fields, name and age; birthday(&amp;person1) changes age through the pointer p</title>'
            '<defs><marker id="ms1h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>'
            '<text class="fk" x="20" y="22">person1 (struct Person, 56 bytes)</text>'
            '<rect class="box" x="20" y="30" width="240" height="80"/><line class="rule" x1="20" y1="70" x2="260" y2="70"/>'
            '<text class="fk" x="32" y="56">name</text><text class="fv" x="100" y="56">"John"</text>'
            '<text class="fk" x="32" y="96">age</text><text class="fv" x="100" y="96">30 → 31</text>'
            '<text class="fk" x="330" y="22">p</text><rect class="box" x="330" y="30" width="70" height="40"/><circle class="pdot" cx="365" cy="50" r="5"/>'
            '<path class="ptr" d="M365,50 L365,90 L264,90" marker-end="url(#ms1h)"/>'
            '</svg><figcaption><code>birthday(&amp;person1);  /* p-&gt;age++ */</code></figcaption></figure></div>')


def heap_mem():
    """Lesson 11: a pointer to the heap, then NULL after free."""
    cells = "".join(f'<rect class="box" x="{20 + i * 38}" y="96" width="38" height="34"/>'
                    f'<text class="fv" x="{39 + i * 38}" y="119" text-anchor="middle">{i * i}</text>' for i in range(10))
    a = ('<figure class="mem"><svg viewBox="0 0 420 150" width="420" role="img" aria-labelledby="mh1">'
         '<title id="mh1">squares points to ten ints on the heap: 0, 1, 4 … 81</title>'
         '<defs><marker id="mh1h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>'
         '<text class="fk" x="20" y="22">squares</text><rect class="box" x="20" y="30" width="70" height="40"/><circle class="pdot" cx="55" cy="50" r="5"/>'
         '<text class="fk" x="130" y="58">on the heap, from malloc</text>'
         f'{cells}<path class="ptr" d="M55,50 L55,92" marker-end="url(#mh1h)"/>'
         '</svg><figcaption><code>squares = malloc(…);</code></figcaption></figure>')
    b = ('<figure class="mem"><svg viewBox="0 0 420 150" width="420" role="img" aria-labelledby="mh2">'
         '<title id="mh2">after free, the heap block is returned and squares is set to NULL</title>'
         '<defs><marker id="mh2h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>'
         '<text class="fk" x="20" y="22">squares</text><rect class="box" x="20" y="30" width="70" height="40"/><circle class="pdot" cx="55" cy="50" r="5"/>'
         '<path class="ptr" d="M55,50 L130,50" marker-end="url(#mh2h)"/><text class="null" x="138" y="56" style="font-size:16px">NULL</text>'
         '<rect class="box freed" x="20" y="96" width="380" height="34"/><text class="fk" x="210" y="119" text-anchor="middle">returned to the heap</text>'
         '</svg><figcaption><code>free(squares); squares = NULL;</code></figcaption></figure>')
    return f'<div class="mems mems-2">{a}{b}</div>'


def lang_struct(L, runs, target=("C", "c/index.html", "c"), up=""):
    """A language page opens with its own struct box, its parent pointer wired to C."""
    rel = rosetta_rel(L["id"], "hello")
    status = "ran ✓" if ran(runs, rel) else "not run"
    rows = [("year", f'{esc(L["year"])} · {esc(L["where"])}'), ("by", esc(L["by"])),
            ("hello", f"{lines_of(rel)} lines · {status}"), ("parent", "●")]
    box, cen, _ = struct_box(4, 4, 300, 196, L["id"], rows, L["page"], title_size=28, kw=True)
    box = re.sub(r'^<a [^>]*>', f'<g class="node node-{L["id"]}">', box).replace("</a>", "</g>")
    tname, thref, tcls = target
    c = (f'<a href="{thref}" class="node node-{tcls}" aria-label="Parent: {tname}">'
         '<rect class="box" x="392" y="60" width="96" height="84"/>'
         + ('<rect class="band" x="392" y="60" width="96" height="84"/>' if tcls != "anc" else "")
         + f'<text class="nm" x="440" y="118" text-anchor="middle" font-size="52">{tname}</text>'
         '<rect class="frame" x="392" y="60" width="96" height="84"/></a>')
    wire = f'<path class="ptr" d="M104,{cen[3]} L340,{cen[3]} L340,102 L388,102" marker-end="url(#lsh)"/>'
    return (f'<svg class="lang-struct" viewBox="0 0 496 204" role="group" aria-label="{esc(L["name"])}: {esc(L["year"])}, by {esc(L["by"])}; its parent is {tname}">'
            '<defs><marker id="lsh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>'
            f'{box}{c}{wire}</svg>')


# ------------------------------------------------------------------------ pages
DIAGRAMS = {"pointers": POINTER_DIAGRAM, "structs": struct_mem(), "malloc": heap_mem()}


def build_home(runs):
    langs = []
    for L in K.LANGS:
        rel = rosetta_rel(L["id"], "hello")
        src = (EX / rel).read_text()
        langs.append(f"""<li class="lcard lang-{L['id']}">
  <a href="{L['page']}"><span class="lc-name">{esc(L['name'])}</span><span class="lc-year">{esc(L['year'])}</span></a>
  <p>{esc(L['tag'])}</p>
  <pre class="code mini"><code>{highlight(src, L['id'])}</code></pre>
</li>""")
    n_ran = sum(1 for k, r in runs["runs"].items() if r.get("compiled") and r["exit"] == 0)
    n_hc = len(list((EX / "holyc").rglob("*.HC")))
    n_warn = sum(len(r["warnings"]) for r in runs["runs"].values())
    n_fail = sum(1 for r in runs["runs"].values() if not r.get("compiled") or r["exit"] != 0)
    body = f"""
<section class="hero" aria-labelledby="h1">
  <div class="hero-head">
    <h1 id="h1"><span class="h1-c">C</span> and the languages that grew from it</h1>
    <a class="start" href="c/01-hello.html">Start with lesson 01 →</a>
  </div>
  {outset_frames(hero_desktop(runs))}
  {outset_frames(hero_narrow(runs))}
  <div class="hero-foot">
    <p class="hero-key"><span class="mono">●──▶</span> a pointer: each language points to the one it came from. A box is a <em>struct</em>, one record with named fields; <span class="mono">[12]</span> is an array of 12; NULL means nothing before it. “hello 5 lines” counts the non-blank lines of that language’s Hello, World, comments included. Every box and cell is a link.</p>
    <a class="start start-m" href="c/01-hello.html">Start with lesson 01 →</a>
  </div>
</section>
<section class="wrap">
  <h2>Start here</h2>
  <ol class="paths">
    <li><a href="c/01-hello.html"><strong>New to C?</strong> Twelve lessons, from <code>printf</code> to <code>malloc</code>, each with its real output.</a></li>
    <li><a href="rosetta.html"><strong>Know one of them?</strong> The same five programs in all five languages, side by side.</a></li>
    <li><a href="family.html"><strong>Curious where it came from?</strong> From BCPL in 1967 to C23 in 2024.</a></li>
  </ol>
  <h2>The family</h2>
  <ul class="lcards">{''.join(langs)}</ul>
  <h2>No output here is typed by hand</h2>
  <p>The build compiled {n_ran} programs in C, C++, Objective-C and C# with strict warnings (<code>-Wall -Wextra -Wpedantic -Wconversion</code> for C, C++ and Objective-C; <code>-warn:4</code> for C#), ran each one, and printed what it actually wrote: {n_warn} warnings, {n_fail} failures. The {n_hc} HolyC programs are shown as source and marked <em>not run here</em>, because HolyC compiles inside TempleOS. <a href="about.html">How the site is built</a>.</p>
</section>
"""
    page("index.html", None, body,
         "C and its family: C++, Objective-C, C# and HolyC. Every C, C++, Objective-C and C# example is compiled and run, with its real output.",
         active="index.html", wide=True)


def pager(prev, nxt):
    p = f'<a class="prev" href="{prev[0]}"><span>← {prev[2]}</span>{esc(prev[1])}</a>' if prev else "<span></span>"
    n = f'<a class="next" href="{nxt[0]}"><span>{nxt[2]} →</span>{esc(nxt[1])}</a>' if nxt else "<span></span>"
    return f'<nav class="pager" aria-label="Lessons">{p}{n}</nav>'


def build_c(runs):
    items = []
    for i, (stem, slug, title, line, _) in enumerate(K.LESSONS):
        rel = f"c/{stem}.c"
        items.append(f'<li><a href="{stem[:2]}-{slug}.html"><span class="num">{i + 1:02d}</span>'
                     f'<span class="lt">{esc(title)}</span><span class="ll">{esc(line)}</span>'
                     f'<span class="lo">{lines_of(rel)} lines</span></a></li>')  # non-blank, comments included
    c_warn = sum(len(runs["runs"][f"c/{L[0]}.c"]["warnings"]) for L in K.LESSONS)
    n_les = len(K.LESSONS)
    std = "".join(f"<li><span class='yr'>{y}</span><span>{t}</span></li>" for y, t in [
        ("1972", "C at Bell Labs, to rewrite Unix"), ("1978", "<cite>The C Programming Language</cite> (K&amp;R)"),
        ("1989", "ANSI C, C89 (ISO C90 in 1990)"), ("1999", "C99"), ("2011", "C11"), ("2018", "C17"),
        ("2024", "C23, ISO/IEC 9899:2024")])
    body = f"""
<article class="wrap">
  <h1>C</h1>
  {outset_frames(lang_struct(K.LANGS[0], runs, target=("B", "../family.html", "anc"), up="../"))}
  <p class="struct-key">A <em>struct</em> is one record with named fields. The red wire is its <code>parent</code> pointer: C grew from <a href="../family.html">B</a>, which grew from BCPL.</p>
  <p class="lede">Dennis Ritchie gave types to Ken Thompson's B so that Unix could be written in something higher than assembly. Fifty years later C still runs the kernels, the interpreters and the firmware everything else stands on. It hands you memory and trusts you with it.</p>
  <div class="two">
    <div><h2>What C gives you</h2><ul class="ticks"><li>Direct access to memory through pointers</li><li>Predictable cost: what you write is close to what runs</li><li>A tiny language and a compiler on every platform</li></ul></div>
    <div><h2>What C leaves to you</h2><ul class="ticks warn"><li>Freeing every byte you allocate</li><li>Staying inside array bounds</li><li>Strings, error handling, and almost everything else</li></ul></div>
  </div>
  <h2 id="lessons">Twelve lessons</h2>
  <p>Each lesson is one program, compiled with <code>gcc -std=c17 -Wall -Wextra -Wpedantic -Wstrict-prototypes -Wconversion</code> ({c_warn} warnings across all {n_les}) and shown with what it printed.</p>
  <ol class="lessons">{''.join(items)}</ol>
  <p class="small">Line counts are non-blank lines, comments included.</p>
  <h2>The standards</h2>
  <ul class="years">{std}</ul>
  <p class="docs">Reference: <a href="https://en.cppreference.com/w/c">cppreference: C</a> · <a href="https://www.open-std.org/jtc1/sc22/wg14/">ISO WG14, the C committee</a></p>
</article>"""
    page("c/index.html", "C", body, "C: twelve lessons, every program compiled and run, plus the standards from K&R to C23.",
         active="c/index.html")
    for i, (stem, slug, title, line, notes) in enumerate(K.LESSONS):
        prev = (f"{K.LESSONS[i - 1][0][:2]}-{K.LESSONS[i - 1][1]}.html", K.LESSONS[i - 1][2], f"lessons[{i - 1}]") if i else ("index.html", "All lessons", "C")
        nxt = (f"{K.LESSONS[i + 1][0][:2]}-{K.LESSONS[i + 1][1]}.html", K.LESSONS[i + 1][2], f"lessons[{i + 1}]") if i + 1 < len(K.LESSONS) else ("../rosetta.html", "Rosetta", "rosetta[0]")
        body = f"""
<article class="wrap">
  <p class="kicker"><a href="index.html">C</a> · <span class="idx">lessons[{i}]</span> · lesson {i + 1} of {len(K.LESSONS)}</p>
  <h1>{esc(title)}</h1>
  <p class="lede">{esc(line)}</p>
  {DIAGRAMS.get(slug, "")}
  {code_block("c", f"c/{stem}.c", runs, up="../")}
  <div class="notes">{notes}</div>
  {pager(prev, nxt)}
</article>"""
        page(f"c/{stem[:2]}-{slug}.html", f"{title} (C lesson {i + 1})", body, f"C lesson {i + 1}: {line}",
             active="c/index.html")


def build_lang(lang, runs):
    P = K.PAGES[lang]
    L = next(x for x in K.LANGS if x["id"] == lang)
    adds = "".join(f"<li><strong>{t}</strong> {d}</li>" for t, d in P["adds"])
    exs = []
    for f, t, note in P["examples"]:
        exs.append(f'<section class="exs"><h3>{esc(t)}</h3><p>{note}</p>{code_block(lang, f"{lang}/{f}", runs)}</section>')
    hist = "".join(f"<li><span class='yr'>{y}</span><span>{t}</span></li>" for y, t in P["history"])
    docs = " · ".join(f'<a href="{u}">{esc(n)}</a>' for n, u in P["docs"])
    note = f'<aside class="callout">{P["note"]}</aside>' if P.get("note") else ""
    ver = runs["versions"].get(lang)
    tool = f'<p class="small">Compiled with <code>{esc(ver)}</code>.</p>' if ver else ""
    body = f"""
<article class="wrap lang-{lang}">
  <h1>{esc(P['title'])}</h1>
  {outset_frames(lang_struct(L, runs))}
  <p class="struct-key">A <em>struct</em> is one record with named fields. The red wire is its <code>parent</code> pointer: {esc(P['title'])} grew from <a href="c/index.html">C</a>.</p>
  <p class="lede">{esc(P['lede'])}</p>
  {note}
  <h2>What it adds to C</h2>
  <ul class="adds">{adds}</ul>
  <h2>Programs</h2>
  {tool}
  {''.join(exs)}
  <p>See the same five programs in every language on the <a href="rosetta.html">Rosetta page</a>.</p>
  <h2>Timeline</h2>
  <ul class="years">{hist}</ul>
  <p class="docs">Further: {docs}</p>
</article>"""
    page(L["page"], P["title"], body, f"{P['title']}: {L['tag']}", active=L["page"])


def build_rosetta(runs):
    # the table of line counts is the figure of this page
    head = "".join(f"<th scope='col'>{esc(L['name'])}</th>" for L in K.LANGS)
    rows = []
    for i, (slug, t, _) in enumerate(K.ROSETTA):
        cells = "".join(f"<td>{lines_of(rosetta_rel(L['id'], slug))}</td>" for L in K.LANGS)
        rows.append(f"<tr><th scope='row'><span class='idx'>rosetta[{i}]</span> <a href='#{slug}'>{esc(t)}</a></th>{cells}</tr>")
    root_lines = lines_of("objc/Root.h") + lines_of("objc/Root.m")
    tot = "".join(f"<td>{sum(lines_of(rosetta_rel(L['id'], s)) for s, _, _ in K.ROSETTA)}</td>" for L in K.LANGS)
    secs = []
    for slug, t, d in K.ROSETTA:
        c_lines = {ln.strip() for ln in (EX / rosetta_rel("c", slug)).read_text().splitlines() if len(ln.strip()) > 1}
        blocks = "".join(code_block(L["id"], rosetta_rel(L["id"], slug), runs, title=L["name"],
                                    same=c_lines if L["id"] != "c" else None) for L in K.LANGS)
        secs.append(f'<section id="{slug}" class="ros"><div class="wrap"><h2>{esc(t)}</h2><p>{esc(d)}</p></div><div class="ros-grid">{blocks}</div></section>')
    body = f"""
<article class="wrap">
  <p class="kicker">rosetta[{len(K.ROSETTA)}]</p>
  <h1>One program, five languages</h1>
  <p class="lede">Five small programs, each written in C, C++, Objective-C, C# and HolyC. In every version after C, lines identical to the C version are dimmed, so what is left in full ink is what that language changes.</p>
  <table class="lines">
    <caption>Non-blank lines of source per program, comments included. The Objective-C programs that define a class also use <code>Root.h</code> and <code>Root.m</code> ({root_lines} lines, not counted).</caption>
    <thead><tr><th scope="col">Program</th>{head}</tr></thead>
    <tbody>{''.join(rows)}</tbody>
    <tfoot><tr><th scope="row">Total</th>{tot}</tr></tfoot>
  </table>
</article>
<div class="wide-wrap">{''.join(secs)}</div>"""
    page("rosetta.html", "Rosetta", body, "Hello, sum, point, swap and reverse in C, C++, Objective-C, C# and HolyC, side by side.",
         active="rosetta.html", wide=True)


def family_svg():
    y0, y1 = 1965, 2026
    W, H = 1100, 300
    lanes = {"anc": 50, "c": 120, "child": 190, "cousin": 260}
    names = {"anc": "ancestors", "c": "C itself", "child": "children", "cousin": "borrowed the syntax"}

    def X(y):
        return 150 + (y - y0) / (y1 - y0) * (W - 180)
    s = [f'<svg class="tl" viewBox="0 0 {W} {H}" role="img" aria-label="Timeline of the C family, 1967 to 2024, in four lanes"><g>']
    for d in range(1970, 2030, 10):
        s.append(f'<line class="grid" x1="{X(d):.1f}" y1="20" x2="{X(d):.1f}" y2="{H - 10}"/><text class="fk" x="{X(d):.1f}" y="14" text-anchor="middle">{d}</text>')
    for k, y in lanes.items():
        s.append(f'<text class="fk" x="0" y="{y + 5}">{names[k]}</text>')
    lastx = {}
    for year, name, _, lane in K.FAMILY:
        x = X(year)
        y = lanes[lane]
        # stagger labels that would collide
        dy = -12 if lastx.get(lane, -99) < x - 60 else 22
        lastx[lane] = x if dy == -12 else lastx[lane]
        kid = {"Objective-C": "objc", "C++": "cpp", "C#": "csharp", "HolyC": "holyc"}.get(name)
        s.append(f'<circle class="dot dot-{lane}{" dot-" + kid if kid else ""}" cx="{x:.1f}" cy="{y}" r="7"/>'
                 f'<text class="tlab" x="{x:.1f}" y="{y + dy}" text-anchor="middle">{esc(name)}</text>')
    s.append("</g></svg>")
    return "".join(s)


def build_family():
    rows = "".join(f"<li class='fam-{lane}'><span class='yr'>{y}</span><span><strong>{esc(n)}</strong> {t}</span></li>"
                   for y, n, t, lane in K.FAMILY)
    body = f"""
<article class="wrap">
  <p class="kicker">BCPL → B → C → …</p>
  <h1>The family</h1>
  <p class="lede">C did not start with C. It grew out of BCPL and B, and its braces, semicolons and <code>for (;;)</code> were copied by languages that share none of its machinery.</p>
</article>
<div class="wide-wrap tl-wrap">{family_svg()}</div>
<article class="wrap">
  <ul class="years fam">{rows}</ul>
  <p class="small">The four lanes: the ancestors, the C standard itself, the languages built directly on C (the ones this site teaches), and languages that borrowed C's syntax without being built on it.</p>
</article>"""
    page("family.html", "Family", body, "The C family from BCPL (1967) to C23 (2024): ancestors, standards, children and cousins.",
         active="family.html")


def build_about(runs):
    vers = "".join(f"<tr><th scope='row'>{esc(LNAME[k])}</th><td><code>{esc(v)}</code></td><td><code>{esc(FLAGS[k])}</code></td></tr>"
                   for k, v in runs["versions"].items())
    n = len(runs["runs"])
    nw = sum(len(r["warnings"]) for r in runs["runs"].values())
    body = f"""
<article class="wrap">
  <p class="kicker">#include &lt;about.h&gt;</p>
  <h1>How this site is built</h1>
  <p class="lede">One Python script, <code>_src/build.py</code>, compiles every program under <code>examples/</code>, runs it, and writes the pages from the results. Change an example, rebuild, and its page changes.</p>
  <h2>Toolchains</h2>
  <table class="lines tools"><thead><tr><th scope="col">Language</th><th scope="col">Compiler</th><th scope="col">Flags</th></tr></thead><tbody>{vers}
  <tr><th scope="row">HolyC</th><td colspan="2">Not run. HolyC is compiled by TempleOS; try <a href="https://holyc.shadw.app">holyc.shadw.app</a>.</td></tr></tbody></table>
  <p>Last compiled on {BUILT}: {n} programs, {nw} warnings. With <code>--no-run</code>, or when a compiler is missing, the build reuses the results stored in <code>_src/runs.json</code>; the date above is when they were produced.</p>
  <h2 id="setup">Getting a compiler</h2>
  <p>A <em>compiler</em> turns the program text into something your computer can run. You type its command into a <em>terminal</em> (Terminal on macOS, a Linux shell, or Windows Terminal).</p>
  <ul>
    <li><strong>Debian or Ubuntu Linux:</strong> <code>sudo apt install gcc g++ clang mono-mcs</code> installs everything the commands on this site use: <code>clang</code> brings the GNU Objective-C runtime (<code>libobjc</code>) the Objective-C commands link against, and <code>mono-mcs</code> brings C#.</li>
    <li><strong>Windows:</strong> two steps: <code>wsl --install</code> in PowerShell, which installs WSL (a Linux shell inside Windows), restart, then the Linux line inside WSL.</li>
    <li><strong>macOS:</strong> <code>xcode-select --install</code> gives you <code>clang</code>, which also answers to <code>gcc</code>, so the C and C++ commands run as printed. The Objective-C commands here use the GNU runtime and were verified on Linux only (on a Mac you would use Apple's runtime and <code>NSObject</code> instead), and C# needs Mono or .NET installed separately.</li>
  </ul>
  <p>Then download any C, C++, Objective-C or C# program from its page (the link is under the program), open a terminal in that folder (<code>cd</code> into it), paste the command printed under the program, and compare what it prints with the dark output box.</p>
  <h2>What changed from the old repo</h2>
  <ul>
    <li>The nine original C examples became twelve lessons. Each was compiled with <code>-Wpedantic -Wstrict-prototypes -Wconversion</code> and fixed until it built without warnings.</li>
    <li><code>read_file.c</code> stored <code>fgetc</code>'s result in a <code>char</code>. That loops forever where <code>char</code> is unsigned and stops early on byte 0xFF where it is signed. <a href="c/09-file-io.html">Lesson 09</a> explains the bug.</li>
    <li>C++, Objective-C, C# and HolyC were added, along with the Rosetta and Family pages.</li>
  </ul>
  <h2>Design</h2>
  <p>The text sits on an 80-column grid, the width of a terminal. The home page draws the site as a C pointer diagram: struct boxes, parent pointers and arrays. The design decisions and the critique rounds are in <code>DESIGN-LOG.md</code> in the repository.</p>
  <p>Type: Newsreader and JetBrains Mono (SIL Open Font Licence), self-hosted. Code on this site is MIT licensed, except <code>examples/holyc/02_null_case.HC</code>, which is from TempleOS (public domain).</p>
</article>"""
    page("about.html", "About", body, "How LearnC is built: every C, C++, Objective-C and C# example is compiled and run by one script.", active="about.html")


def build_404():
    body = """<article class="wrap"><p class="kicker">Segmentation fault (core dumped)</p><h1>404</h1>
<p class="lede">That address points nowhere. <a href="index.html">Dereference the home page instead.</a></p></article>"""
    page("404.html", "Not found", body, "Page not found.")


# ------------------------------------------------------------------ link check
def check_links():
    bad = []
    for f in OUT.rglob("*.html"):
        for href in re.findall(r'href="([^"#]+)(?:#[^"]*)?"', f.read_text()):
            if href.startswith(("http", "mailto:")):
                continue
            if not (f.parent / href).resolve().exists():
                bad.append(f"{f.relative_to(OUT)} -> {href}")
    return bad


def check_deploy():
    """Shadw and Vercel both serve site/: the three config files must exist and agree."""
    bad = []
    try:
        root = json.loads((ROOT / "vercel.json").read_text())
        inner = json.loads((OUT / "vercel.json").read_text())
        fluid = json.loads((ROOT / "fluid.json").read_text())
    except (OSError, ValueError) as e:
        return [f"deploy config: {e}"]
    if root.get("outputDirectory") != "site" or inner.get("outputDirectory") != ".":
        bad.append("deploy config: vercel.json must serve site/ (root) and . (site/vercel.json)")
    if fluid.get("static_dir") != "site" or not root.get("fluid"):
        bad.append("deploy config: fluid.json static_dir must be site and vercel.json must set fluid: true")
    if not SITE_URL.endswith(".shadw.app"):
        bad.append("deploy config: SITE_URL must be the project's shadw.app address")
    return bad


def main():
    global BUILT
    do_run = "--no-run" not in sys.argv
    runs = run_all(do_run)
    BUILT = min(runs.get("built", {"x": "an unknown date"}).values())
    for f in OUT.rglob("*.html"):
        f.unlink()
    shutil.rmtree(OUT / "examples", ignore_errors=True)
    shutil.copytree(EX, OUT / "examples")
    build_home(runs)
    build_c(runs)
    for lang in ("cpp", "objc", "csharp", "holyc"):
        build_lang(lang, runs)
    build_rosetta(runs)
    build_family()
    build_about(runs)
    build_404()
    problems = check_links() + check_deploy()
    for slug, _, d in K.ROSETTA:
        m = re.search(r"Prints (\S+)\.$", d)
        if m:
            for L in K.LANGS[:4]:
                out = runs["runs"][rosetta_rel(L["id"], slug)]["stdout"]
                if m.group(1) not in out.splitlines():
                    problems.append(f"rosetta {slug}: prose says {m.group(1)}, {L['id']} printed {out!r}")
    for rel, expect in K.QUOTED_OUTPUTS:
        if expect not in runs["runs"][rel]["stdout"].splitlines():
            problems.append(f"{rel}: prose quotes {expect!r}, not in its output")
    warned = [k for k, r in runs["runs"].items() if r["warnings"] or not r.get("compiled") or r["exit"] != 0]
    pages = len(list(OUT.rglob("*.html")))
    print(f"built {pages} pages from {len(runs['runs'])} compiled programs")
    if problems or warned:
        print("problems:", problems)
        print("failed or warned:", warned)
        sys.exit(1)


if __name__ == "__main__":
    main()
