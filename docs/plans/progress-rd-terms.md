# Progress: rd-terms (final first-use glossary-link pass)

Branch `topic/rd-terms`, worktree `.worktrees/rd-terms`, from `main` at `a03f0de9` ("machines
batch B merged"). Task: readability guide R-TERM rule 2 / readability plan W3–W4, the single
final run of `tools/link_terms.py` on the content pages.

## Page set

`docs/steps/*.md`, `docs/machines/*.md`, `docs/materials/*.md`, `docs/masks/*.md`,
`docs/categories/*.md`, `docs/overview/*.md`, `docs/history/*.md`; excluded: every `index.md`
and `docs/history/sources.md` (a source list). 268 pages.

## Steps

1. [x] `--selftest` passes at the start.
2. [x] `--report` over the page set (saved as `tmp/link-terms-report.txt` in the worktree,
   git-ignored): 1 124 candidates, 141 terms. Read as a reviewer: every candidate of every term
   was read in context (not only the three-per-term minimum), grouped by term.
3. [x] Rejections put into the tool (commit `f903ca2f`, self-test 31a), see below.
4. [x] Idempotence bug found and fixed in the tool (commit `3d16eb28`, self-test 34b), see below.
5. [x] Applied, one commit per directory (`ALLOW_MEGACOMMIT=1`, regenerated output).
6. [x] Verification (below).
7. [x] Rendered check (below).

## Rejections (all in `tools/link_terms.py`, none by hand)

| Term | Where | Why | Mechanism |
|---|---|---|---|
| `spacer` | 5 of 29 first uses: steps 136, 138, 141, 153 (MiM-stack sidewall spacers), overview/sky130b-reram (ReRAM stack) | wrong sense: the glossary entry is the gate-edge spacer; no narrow context separates the uses | `SKIP_TERMS` |
| `TCP` | machines/plasma-etcher-metal "the TCP 9600SE" | model name; the model-number guard missed a letter-suffixed number | `CONTEXT_SKIP` (after-regex allows `[A-Z]{1,3}` suffix) |
| `CMP` | "Applied Materials Mirra CMP" on 7 step pages (106, 122, 127, 133, 142, 148, 157) | tool model name | `CONTEXT_SKIP` before `Mirra` |
| `PVD` | "AMAT PVD Metal" on 7 step pages (120, 123, 131, 134, 146, 149, 161) | SkyWater's platform entry name | `CONTEXT_SKIP` after ` Metal` |
| `PECVD`, `TEOS` | step 080 '"C2" / Producer PECVD TEOS' | SkyWater's tool entry name | `CONTEXT_SKIP` before `Producer` |
| `NA` | masks/pwdem "0.5 λ/NA" | symbol inside a written formula | `CONTEXT_SKIP` before `/` |
| `ICP` | machines/film-thickness-metrology "wet chemistry, ICP or SIMS" | ICP spectrometry (chemical analysis), not the plasma source | `CONTEXT_SKIP` after ` or SIMS` |
| `shadowing`, `LATID` | masks/hvntm, masks/ldntm, masks/ntm "ion-beam shadowing in submicrometre LATID MOSFETs (title)" | wording of a cited title | new `GLOBAL_CONTEXT_SKIP`: any span followed by `(title)` within the clause (after-window widened from 20 to 80 characters) |

A context-guarded occurrence is deferred, not dropped: the term links at its next acceptable use
on the page (e.g. `CMP` on step 122 now links at "tungsten CMP as the oxidation of the metal").
Every replacement candidate that the guards produced was read too.

Accepted after reading (not rejected): `stepper`/`DUV` in "ASML DUV stepper or scanner" (descriptive,
correct sense); `CVD` in "Lam/Novellus tungsten CVD with PNL"; `ARC` for TiN/TiW anti-reflective
layers (the glossary sense covers them); slash compounds such as "TCP/ICP", "PSG/CMP module",
"tip/halo" (correct sense, readable); `hillock` used as a verb once (step 126; same phenomenon).

## Tool fix: idempotence

After the first application a `--check` re-run proposed 7 more links: links deferred by the
3-per-paragraph cap came back on a second run, because the cap counted only the links added in the
current run. Existing `{term}` roles in a paragraph now count toward its cap (self-test 34b).
Effect on this pass: 1 090 → 1 048 links (paragraphs, often long lists, that already carried three
hand-written links get no more). A re-run now proposes 0.

## Counts (links added)

| Directory | Pages changed | Links |
|---|---:|---:|
| docs/steps | 120 of 171 | 447 |
| docs/machines | 29 of 30 | 202 |
| docs/masks | 36 of 36 | 283 |
| docs/materials | 12 of 12 | 81 |
| docs/categories | 7 of 10 | 16 |
| docs/overview | 1 of 1 | 5 |
| docs/history | 6 of 8 | 14 |
| **Total** | **211** | **1 048** |

## Verification

* `tmp/verify_insert_only.py a03f0de9` (worktree, git-ignored): line counts unchanged on every
  file; 1 009 changed lines, 1 048 roles added, 0 failing lines — every changed line equals its base
  once the added roles are unwrapped, and every base role is still present.
* `check_preserved.py --base a03f0de9 --allow-regrouped` on 20 sampled pages (6 steps, 4 machines,
  4 masks, 2 materials, 2 categories, overview, history): only `ADDED refs` (plus the informational
  WORDS lines for the words now inside roles, and one `WORDS ADDED: 's'` where "test tile's"
  became a role plus "'s"); with `--allow-added refs` 0 undeclared differences.
* `--check` re-run: 0 further links (idempotent).
* Source-context script (`tmp/src_context.py`, worktree): of the 1 009 changed lines, 939 are prose,
  64 inside an admonition (the "At a glance" boxes) and 6 inside a `seealso`; none is a heading,
  table row, blockquote, footnote definition, `## References` line, dropdown or figure body.
* Built-HTML script (`tmp/html_ancestors.py`): the 211 glossary links found inside a table,
  References section or `<details>` on the changed pages are all hand links that were already in
  the base (spot-checked in source; the source-context script shows no added role in those places).
* Checkers: check_steps, check_refs, check_machines, check_materials, check_masks, check_papers,
  check_patents, check_filings, check_inforce, check_history — all exit 0, 0 problems.
  Generators `--check`: gen_papers, gen_patents, gen_filings, gen_index_links — 0 differences.
  `sphinx-build -W` — clean.
* Rendered: steps 080 and 122, machine coat-develop-track, material process-gases, mask fom,
  category deposition, desktop and `--width 400` (109 tiles, of which about 25 content tiles
  were opened; the rest are reference lists and footers, which the scripts above cover). Links
  read as links on first use; none sits in a heading, table, quotation, dropdown, figure or
  reading list.

## Odd, not fixed

* Where a new term link sits directly after a `{ref}` or another term (step 122 "NCAPOX3 cap
  oxide", step 080 "LPCVD TEOS"), the two links render side by side and read like one link. The
  same pattern already existed in hand-written text ("cap oxide POC" on step 080). Presentation
  only; a tool guard against adjacency could be added if the owner minds.
* Some paragraphs are long bulleted lists without blank lines, so the paragraph cap treats the
  whole list as one paragraph; with hand links counted, such lists get few new links.
