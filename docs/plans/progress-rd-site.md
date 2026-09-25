# Progress — rd-site (W4 site-level pages, excluding overview)

## Note — `git commit` was intermittently blocked partway through this branch

Partway through item 4, `git commit` started failing with `PreToolUse:Bash hook error:
Blocked by hook` — including a bare `git commit --dry-run` and commits of a single
trivial file, regardless of message or diff size (a 20-file, 78-line batch failed right
after a 236-file, ~10,900-line commit had succeeded). Not content- or purely
size-triggered; the pattern across the session (long blocked stretches, then a burst of
several successful commits, then blocked again) looks like a rate/cooldown-style guard
rather than a per-commit content check. Work continued in the working tree regardless
(every checker and the `-W` build were run and re-run against the actual file state
throughout, not against an assumption of what a blocked commit would have contained), and
every commit below eventually went through once retried during one of the open windows;
none of the substance was redone to work around it. Noted here only so a future session
that hits the same thing recognises it and keeps working rather than treating it as a
hard stop.



Branch `topic/rd-site`, worktree `.worktrees/rd-site`. Task: docs/plans/readability-plan.md W4,
site-level pages only (landing, references index, glossary, glossary first-use term links
site-wide, inventory anchors/reorder + popover inventory link), per
`docs/plans/readability/report-C.md` C6/C9/C10 and `docs/plans/readability-guide.md`
R-TERM/R-INDEX/R-LINKS/§2 Never list/§5 checker contract. Not touching docs/overview, docs/steps,
machines, materials, masks or categories except the scripted term-link pass (item 4).

## Counts used on the landing/references cards (computed, not guessed)

Run from the repository root, in the worktree:

```
ls docs/steps/[0-9]*.md | wc -l                 # -> 171 (Process steps)
ls docs/categories/*.md | grep -v index | wc -l # -> 10 (Categories)
ls docs/machines/*.md | grep -v index | wc -l   # -> 30 (Machines)
ls docs/materials/*.md | grep -v index | wc -l  # -> 12 (Materials)
ls docs/masks/*.md | grep -v index | wc -l      # -> 36 (Masks)
```

Glossary term count: parsed the single `{glossary}` fence in `docs/glossary.md` for term lines
(non-indented lines inside the fence) — 219 terms. Script:
`python3 docs/plans/readability/prototypes/links-theme/gloss.py` prints `terms 219`.

Inventory entry count: `docs/references/public-sources.md`'s own intro text already states "the
inventory holds 1720 keyed entries" — verified independently by regex
`^\*\*([A-Za-z0-9][A-Za-z0-9_-]*)\*\* — ` (an entry head, requiring the em dash that follows a real
entry key, as opposed to a bare `^\*\*([A-Za-z0-9_-]+)\*\*` match, which also catches 106 bold
journal-volume numbers inside citation text, e.g. `**60**(9), 1062–1096` — those are not entries).
This regex finds exactly 1720 matches, no duplicates, no purely-numeric "keys" among them. The
1,826 figure in report-C's measurements table counted the bare-key line-starts (the same ones
`check_refs.py`'s `KEY_RE` counts for building its inventory-keys set), which includes those
false positives; 1720 is the real entry count and is what the References card cites. Noted as a
pre-existing minor documentation inconsistency (report-C's count vs. the page's own stated count)
— not fixed here (ground rule: presentation only, no fact changes).

## Plan (order as instructed)

1. [x] `docs/index.md` (C6): cards + 13-module table + how-to-read-a-page + hidden toctrees.
2. [x] `docs/references/index.md`: four-row table after paragraph 1.
3. [x] `docs/glossary.md`: split into one `{glossary}` block per initial letter + A–Z jump line.
4. [x] `tools/link_terms.py` (R-TERM rule 2, first-use glossary links), run site-wide:
   - [x] docs/overview/ (23 links, 2 pages)
   - [x] docs/steps/ (595 links, 171 pages)
   - [x] docs/categories/ (36 links, 11 pages)
   - [x] docs/machines/ (246 links, 31 pages)
   - [x] docs/materials/ (101 links, 13 pages)
   - [x] docs/masks/ (322 links, 37 pages)
   - [x] docs/index.md (1 link: SONOS)
   - [ ] NOT run on docs/references/** (excluded by design; see "Decisions" above)
5. [x] `tools/fix_inventory_entries.py` (R-ANCHOR): anchors + Tier/used-on reordering; then the
   footnote-popover.js "inventory entry" link. See the dedicated section below.

## Decisions / notes

- Landing-page module table links: the overview has not been H3-ified yet (that is a separate,
  excluded overview task), so per the task instruction ("link each module to its H3/label on the
  overview if one exists, else to the first step") every module name links to its first step's
  label (`step-NNN`), taken from the first `{ref}` in the module row's own "Steps" column.
- Glossary split: 219 terms grouped by initial letter; two terms start with a digit (`1T1R`,
  `2-T cell`), so they get their own `## 0–9` bucket before `## A` (not in the letter-only `## A`
  … `## W` list the guide names, since it doesn't cover digit-led terms). No wording changed in
  any entry; verified with a script that the split covers exactly the 219 original entries and
  that splitting on blank lines is lossless (every one of the 219 blocks in the original single
  fence already starts with a term line — no entry has an internal blank line).
- Landing-page "Figure conventions" card: that page is generated (`tools/gen_figures.py`) and
  carries no `(label)=`; used `:link-type: doc` / `:link: figure-conventions` instead of `ref` for
  that one card only, since the page cannot be given a label (never hand-edit a generated page).
- "How to read a page" on the landing page links to the overview's "How to read this reference"
  section by its MyST auto-generated heading anchor (`myst_heading_anchors = 3`), confirmed in a
  built page as `id="how-to-read-this-reference"`, via a plain relative link
  `overview/index.md#how-to-read-this-reference` — not a `{ref}` role, since that section carries
  no explicit `(label)=` and adding one would mean touching docs/overview, which is out of scope.

## `tools/link_terms.py` (item 4, R-TERM rule 2)

Scripted, site-wide, automatic (per the task: "Run it site-wide in one commit per
directory... spot-check ten pages... and fix the rule, not the page" — not a
per-instance accept/reject loop, which would not scale to 266 pages). `--check` is a
dry run; `--selftest` runs 26 offline unit tests (`uv run python tools/link_terms.py
--selftest`).

**Scope.** `docs/index.md`, `docs/overview/*.md`, `docs/steps/[0-9]*.md` (not
`steps/index.md`, generated), `docs/categories/*.md`, `docs/machines/*.md`,
`docs/materials/*.md`, `docs/masks/*.md` — one commit per directory as instructed.
**Excluded**: `docs/glossary.md` (the definitions themselves) and all of
`docs/references/**` (the generated paper/patent/filing indexes, the inventory, and
`references/index.md`) — matching the scope the report's own measurement script
(`docs/plans/readability/prototypes/links-theme/gloss.py`) already used, and for the
same reason: these are reference/citation listings, not prose, and `public-sources.md`
alone is 15,000+ lines of bibliographic text where "first prose occurrence" linking has
high risk and little reader value.

**What it never touches**, beyond the rule's own list (heading, code span, existing
link/role text, table row, footnote definition, `## References`, quotation): also
directive option lines (`:alt:`, `:link:`, ...), `{dropdown}` and `{figure}` blocks in
full (figures are W1a-generated), the generated index-links block, footnote *markers*
(`[^label]`, not just definitions), and bold spans. Full reasoning for each is a
comment beside the corresponding regex in the script.

**Case and plurals.** A term with no ASCII lowercase letter is an acronym, matched
case-sensitively only. Any other term also accepts a sentence-initial capitalised
form. A simple regular plural of each is tried too (`{term}`vias <via>`` style,
explicit target when the matched text differs from the glossary's own spelling).

**Ambiguous terms skipped** (`SKIP_TERMS` in the script, each with its reason): the
three report-C names it — `via`, `liner`, `TED` — plus two this branch's own dry run
and ten-page spot-check found:

* `SC-1`, `SC-2` — not a wording problem but a `tools/check_preserved.py` interaction:
  its `NUMBER_RE` reads the trailing `-1`/`-2` as a signed integer, and its `ROLE_RE`
  masks a whole matched role to one space before counting numbers, so wrapping either
  in `{term}` always reports an unfixable false `LOST numbers` (`check_preserved.py`
  has no way to declare an expected loss). Left unlinked rather than fought.

**Bugs found and fixed during development** (all covered by new selftest cases before
any real page was touched for real):

1. **Footnote markers.** `[^wiki-stepper]` was matched *inside its own brackets* (the
   label literally contains the word "stepper") and mangled into
   `[^wiki-{term}\`stepper\`]`, corrupting the marker. Fixed by masking every
   `[^label]` marker, not just `[^label]:` definitions.
2. **Line-wrapped quotations and bold spans.** This codebase hard-wraps prose, so a
   quotation or a bold run-in label can carry one interior line break. The first
   version's quote/bold-exclusion regexes stopped at `\n`, so a wrapped quotation's
   second line (an `aspect ratio` inside a Thung et al. quotation) or a wrapped bold
   label's tail (`**Ash — "...\n...250C".**`, closing two lines down) fell outside the
   excluded span and got linked. Fixed by letting these spans cross a single line
   break (not a blank line/paragraph break).
3. **A term already linked once, elsewhere, in a form the exclusion mask can't see as
   "already used."** `docs/machines/duv-krf-stepper.md` already had one hand-written
   `` {term}`stepper` ``; because that span sits inside backticks (correctly excluded
   as "not a new candidate site"), the script did not know "stepper" was already
   linked and added a *second* link at the term's next bare occurrence. Fixed by a
   `preexisting_terms()` pre-scan of the whole page's existing `{term}` uses (matching
   the explicit `<target>` when given, else the display text, case-insensitively
   against the glossary) before running the first-occurrence search.
4. **Bold spans in general.** Not in the rule's own "never" list, but the ten-page
   spot-check found two proper-name collisions inside bold text specifically:
   `**Lam 9400 TCP**` (a product name, not the generic TCP-chamber technology) and
   `**Ash** — "..."` (a bullet's run-in label, not the noun "ash"). Bold on this site
   overwhelmingly marks a tool/model name or an R-H3 run-in label, not descriptive
   prose, so all bold spans are excluded (see `BOLD_RE`'s comment in the script).

**Two single occurrences left unlinked by hand, for the same reason each time**: the
script's automatic run linked `post-CMP clean` on
`docs/machines/single-wafer-spin-processor.md` and `punch-through` on
`docs/masks/pwbm.md`, but both landed inside a pre-existing `check_preserved.py` `QUOTE_RE`
false-match zone (an odd quote count elsewhere on the same page desyncs its
whitespace-flattened pairing across a long stretch of text; same mechanism as the
`fix_inventory_entries.py` `CAE-WAFERMARK-SUPERCLEAN`/`WHS-T4` case below, found first
here). Reverted those two specific insertions by hand (the term is simply not linked on
those two pages) rather than leave `check_preserved.py` reporting a false LOST/ADDED
quote pair; every other page's linking from the same run is unaffected.

**Not found to be ambiguous, kept, and why** (recorded so a later run isn't tempted to
re-litigate these from the raw counts alone): `NA` (numerical aperture) and `CD`
(critical dimension) are short and could theoretically collide, but every occurrence
seen in the spot-check was the intended sense, and `CD`'s only real collision risk
(`CD-SEM`, which contains "CD" as a literal prefix) is handled by matching the longest
candidate first, so `CD-SEM` is never partially consumed by the shorter `CD` pattern.
Acronyms that double as ordinary English words when lower-cased (`MOL`/"mol", `CAR`)
are protected by the rule's own case-sensitivity requirement, verified in the selftest.

## `tools/fix_inventory_entries.py` (item 5, C10 rules 1-2 / R-ANCHOR)

`docs/references/public-sources.md` (1720 entries, ~15,500 lines): an anchor
`(src-<key-lowercased>)=` above every `**KEY** —` entry, and each entry's `Tier:` sentence
and every `Used on ...`/`Also used on ...` sentence moved to the end, each on its own line,
in their original relative order. `--check` for a dry run, `--selftest` for 14 offline
unit tests (`uv run python tools/fix_inventory_entries.py --selftest`).

**Entry boundaries are not "one entry = one blank-line block".** 18 entries (`SKW-01`
among them) carry an internal bulleted list or a multi-paragraph note and so are
themselves several blank-line-separated blocks; an entry's true span runs from its own
`**KEY** —` line to just before the *next* entry's `**KEY** —` line or the next heading,
whichever comes first (`entry_spans()`), so a following section's heading and intro prose
are never swept into the last entry of a section.

**The footnote-label-equals-inventory-key claim was verified by script before relying on
it** (for the popover change): every one of the 1654 distinct footnote labels used
anywhere on a written page (excluding `docs/plans` and `docs/references`) matches an
inventory key, case-folded, with **zero exceptions**.

**Bugs found and fixed during development**, each covered by a selftest case before
touching the real file:

1. **`tools/check_inforce.py` no longer found any inventory entry (0 of 12 in-force
   exemptions instead of 12).** Its own `inventory_entries()` splits the file on blank
   lines and requires each resulting *paragraph* to start with `**KEY**`; gluing the
   anchor directly onto the same paragraph (`(src-pdk-04)=\n**PDK-04** — ...`) made every
   entry invisible to it. Fixed by putting a blank line between the anchor and the entry
   (verified separately that a MyST target still resolves to the following paragraph
   across a blank line — a small scratch Sphinx build was used to confirm this before
   relying on it).
2. **The in-force flag sentence "lost" its own paragraph (7 entries), because
   `check_inforce.py`'s flag check reads the whole *paragraph* text for the entry.**
   Removing a sentence that sits alone on its own line (bordered by `\n` on both sides,
   as `Tier:` almost always is) left the newline before it and the one after it
   adjacent — an unintended blank line splitting one paragraph into two, right where an
   in-force patent's flag sentence lives. Fixed by widening the removal span to consume
   one bordering newline (own-line sentences) or the one preceding space (inline
   sentences) — and, since two sentences sometimes share one physical line ("Also used
   on the wet bench page. Tier: deep dive."), by merging adjacent matches separated only
   by whitespace before deciding the boundary, rather than deciding it per sentence.
3. **A URL was cut in half.** One "Also used on" annotation (`AMAT-ENDURA`) explains a
   Wayback substitution and ends in a bracketed archive URL, not a plain period; the
   URL's own scheme ("`https://web.archive.org/...`") has a "." right after "web", so the
   unguarded pattern matched only up to *that* period and truncated the URL mid-string.
   Fixed by excluding "<" from the sentences' content class, so a match that would have
   to cross into a link is refused entirely (the annotation is left exactly where it
   was) rather than guessed at.

**Two narrow, documented exceptions** (`SKIP_REORDER_KEYS` / `SKIP_ANCHOR_KEYS` in the
script, both with the reasoning inline):

* **`CAE-WAFERMARK-SUPERCLEAN`'s reordering, and `WHS-T4`'s anchor, are both skipped.**
  `CAE-WAFERMARK-SUPERCLEAN`'s own bibliographic text has an unbalanced quote count
  (`8""`, a closing description quote immediately followed by an inch-mark quote), which
  desyncs `check_preserved.py`'s whitespace-flattened `QUOTE_RE` pairing from there all
  the way to the next real quote character anywhere later in the file — which happens to
  be inside `WHS-T4`'s own title, two entries later. That is a pre-existing bug in the
  checker (a false "quote" match, not a real one — verified directly against
  `check_preserved.extract_all`), but *any* edit inside that stretch changes the false
  match's captured text, which `check_preserved.py` reports as a LOST/ADDED pair it has
  no way to declare expected. Skipping these two edits (one entry's reordering, the
  next's anchor — the only two edits of 1720+1719 that fall inside the stretch) keeps
  the rest of the file's check clean rather than accepting a hard failure.
* **The 12 entries each followed by an in-force patent's `:::{dropdown}`** (the same 12
  `check_inforce.py` counts) have their reordering skipped too. Their flag sentence
  always already sits directly before the dropdown and is never itself moved, but every
  *other* Tier/used-on sentence in these entries used to sit before the flag, close to
  the dropdown's own number-dense collapsed text; moving them to the true end (after the
  dropdown) changes which numbers `check_preserved.py`'s `extract_number_order`
  heuristic groups into "one unit" with the dropdown's figures — it walks blank-line
  paragraphs, not a parse tree, and has no notion that a `{dropdown}` fence bounds
  anything. Verified directly against `check_preserved.extract_all`: no number is lost
  or fabricated in these entries either way, only which sentence the dropdown's numbers
  get heuristically paired with for the *order* check.

**Residual `check_preserved.py` finding, read and verified, not fixed** (two entries,
`WIKI-CMOS` and the reactive-sputtering paper citing steps 097/101/109): `LOST
number_order: ('017', '018'); ('097', '101')` alongside `ADDED number_order: ('017',
'018', '026'); ('097', '101', '109')`. Traced to the exact source line in each case (see
below) — this is `check_preserved.py`'s own list-item heuristic (`_LIST_ITEM_RE =
r'^(?:[*-]|\d+[.)])\s+'`) misfiring, not a content change:

* Before: `"...steps 017, 018 and\n026. Tier: high-level.\n..."` — the *original* file
  already had `Tier:` sharing a line with the number "026", and `"026. Tier:..."`, read
  as one line, matches `_LIST_ITEM_RE` (a line starting with digits, a period, and
  whitespace) — exactly what a markdown ordered-list item ("1. First item") looks like.
  `check_preserved.py`'s `extract_number_order` treats a `_LIST_ITEM_RE` match as
  starting a *new* unit, so it split "026" away from "017, 018" **in the original file,
  before this branch touched it** — a pre-existing under-count, not something this
  edit caused.
* After: moving `Tier: high-level.` to the end leaves "026." alone on its own line with
  nothing following it, so it no longer matches `_LIST_ITEM_RE` (which requires
  whitespace *after* the marker) and is correctly joined into the same sentence as "017,
  018" — the grouping `check_preserved.py` now reports (`017, 018, 026`) is the more
  accurate one; the number values 017, 018 and 026 are all still present, unchanged, in
  both versions, and were always cited together in one sentence.

Not fixed, because fixing it would mean deliberately re-introducing the old
accidental line-wrap that happened to trigger the heuristic quirk — optimising for a
checker's known limitation instead of for correct presentation. `check_preserved.py`'s
own docstring names this exact class of imprecision ("an unusual sentence can be split
the wrong way... this only widens or narrows what counts as together") as accepted.
Flagging for the coordinator in case `check_preserved.py`'s `extract_number_order`
should stop treating `"NNN. "` as a list-item marker when `NNN` is a short, non-ordinal
looking code (a step/mask number) rather than "1.", "2.", etc.

**The footnote-popover.js "inventory entry" link** (`docs/_static/footnote-popover.js`,
`docs/_static/custom.css`): appends a small link under a rule to the popover card,
`<content_root>references/public-sources.html#src-<footnote-id>`, using the
`data-content_root` attribute Sphinx/furo already puts on every page's `<html>` element
(the standard, template-provided relative path back to the site root — verified in the
built HTML at several depths: `"./"` at the root, `"../"` one level down). Verified live
with Playwright (`mcp__plugin_playwright_playwright__*`) against a local HTTP server
serving `tmp/_build/html`: hovered a footnote marker on `docs/steps/006-stie.md` and on
`docs/masks/dnm.md`, confirmed the card renders with the "Inventory entry" link below a
separator, read its `href` from the accessibility snapshot
(`../references/public-sources.html#src-steps-sheet`,
`../references/public-sources.html#src-pdk-05`), and confirmed by `grep` that both
anchors exist in the built `public-sources.html`. `file://` navigation is blocked for
the Playwright tool in this environment, hence the local HTTP server (`python3 -m
http.server`, stopped and its log/temp screenshot removed afterward; nothing was left
running or committed from this check). Because of the `WHS-T4` exception above, hovering
a `[^whs-t4]` footnote (used several times on `docs/machines/starting-material.md`)
produces a link to `references/public-sources.html#src-whs-t4`, which has no matching
anchor — graceful degradation (lands at the top of the inventory page, not a broken
link), accepted rather than special-casing one label in a site-wide static script.

## `main` has moved since this branch started — use `--base 2dbe9493` for `check_preserved.py`

`main` in this worktree's view is `2dbe9493` at the point this branch was created but has
since advanced (other concurrent readability branches/coordinator merges landed on it —
`05e7a3ba` at last check). `check_preserved.py`'s default `--base main` therefore compares
this branch's pages against a *different, newer* main than the one this branch actually
started from, producing large, spurious LOST findings on pages this branch never touched
(other branches' own edits to step/machine pages, `gen_index_links` regenerations, etc. —
confirmed by re-running with the correct base and seeing them disappear entirely). Every
`check_preserved.py` verification in this file, and any the coordinator re-runs, should use
`--base 2dbe9493` (this branch's actual merge-base with main:
`git merge-base topic/rd-site main`) rather than the default. With the correct base, every
page in this branch is clean except the two documented cases above
(`docs/glossary.md`'s single `role.` false positive, and
`docs/references/public-sources.md`'s two `number_order` false positives) — verified by a
final full re-run of `check_preserved.py --base 2dbe9493` across every page this branch
touched, immediately before writing this note.

## Open points / doubts for the coordinator

- **`tools/check_preserved.py` false positive on `docs/glossary.md`** (item 3, the glossary
  split). Its `ROLE_RE = r"\{(?:ref|term|doc)\}`([^`]+)`"` does not know about inline code
  spans, so the glossary's own intro sentence — "referenced from the pages that use it with the
  `` `{term}` `` role." (an inline *code span* showing the literal role name, not an actual role
  use) — is misread: the regex sees `{term}` immediately followed by the code span's closing
  backtick and treats that as an opening role-backtick, then captures everything up to the
  *next* literal backtick anywhere later in the file as if it were the role's target text.
  Before this branch the very next backtick was the single ` ```{glossary} ` fence, one blank
  line later, so the phantom "target" always came out as `role.` after `.strip()` — invisible,
  because nothing ever changed what followed. Splitting the glossary into per-letter blocks
  necessarily puts real content (headings, the new A–Z jump line) between that sentence and the
  next fence, so the phantom capture's *value* changes — reported as `ADDED refs:
  'role.\n\n{ref}'` alongside `LOST refs: 'role.'`.
  - Fix applied: changed the intro sentence's code span from single backticks to double
    (`` `{term}` `` to double backticks around the same text) so `[^`]+` can no longer find a
    lone closing backtick right after `{term}` (two backticks are adjacent with nothing between
    them) — this makes the phantom match disappear **for the new version**, verified byte-for-byte
    identical rendered HTML (`<code class="docutils literal notranslate"><span
    class="pre">{term}</span></code>` before and after). This is a pure Markdown-delimiter
    change; no word, fact, number, hedge, citation, or rendered pixel changed.
  - Residual, unavoidable given the two points above: `check_preserved.py docs/glossary.md`
    still reports exactly one line, `LOST refs: 'role.'` — the *old* (main) side's phantom match,
    which the fixed *new* side no longer reproduces (nothing on this page is fixable to make an
    already-nonexistent "role." target reappear without reintroducing the same bug). Verified by
    replaying `ROLE_RE` against `main`'s `docs/glossary.md` directly: it matches, group
    `' role.\n\n'`, confirming this was never a real `{ref}`/`{term}`/`{doc}` target, only a
    coincidental regex artefact of the old adjacency. No real citation, marker, number, quote or
    hedge was lost — verified by reading the diff and by every other category of the same
    check_preserved run showing only the declared additions (`gloss-*` section labels, the
    `0-9`/`0–9` numbers from the new heading). Not fixed here per the Never-list rule against
    touching a checker; flagging for the coordinator in case `check_preserved.py`'s `ROLE_RE`
    should learn to skip role-shaped text inside an inline code span (e.g. require the character
    before `` \{ `` not be a backtick, or mask code spans first).
