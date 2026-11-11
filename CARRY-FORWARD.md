# Carry-Forward Ledger (facts about the medium, measured in the LearnC run)

- A grid list item with a year span plus loose text and inline `<code>` breaks into anonymous grid cells. Wrapping the body in one `<span>` fixed the Family list (measured visually; same fact as PersonalPortfolio's ledger).
- `code, pre { font-size: .84em }` plus `pre.code { font-size: .82rem }` shrinks code inside pre twice (to 10.2 px). `pre code { font-size: 1em }` fixed it. The "80 columns" measure was wrong until it did.
- In SVG, a CSS class `font-size` beats a `font-size` presentation attribute. `font-size="16"` on a `.null` text was inert (11.4 px measured); an inline `style` moved it to 12 px.
- An SVG focus stroke on a `rect.box` is invisible where a same-colour `rect.band` is painted over it (1.00:1). Draw a separate `.frame` rect last, and outset it from the box, so it never meets the content.
- `overflow-x: auto` on a nav clips each link's outer focus outline to a side bar. `outline-offset: -3px` keeps it inside.
- JetBrains Mono contextual ligatures render `==` as one glyph. Teaching code needs `font-variant-ligatures: none`.
- A measuring script given a typed list of pages will miss pages. Enumerate `site/` instead.
- GNU Objective-C on Ubuntu: the headers are in `libobjc-13-dev`, pulled in by clang (not gcc). `-I"$(gcc -print-file-name=include)" -L"$(gcc -print-file-name=)"` finds them portably.
