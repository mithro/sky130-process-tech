# Progress — rd-site (W4 site-level pages, excluding overview)

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
4. [ ] `tools/link_terms.py` (R-TERM rule 2, first-use glossary links), run site-wide.
5. [ ] `tools/fix_inventory_entries.py` (R-ANCHOR): anchors + Tier/used-on reordering; then the
   footnote-popover.js "inventory entry" link.

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
