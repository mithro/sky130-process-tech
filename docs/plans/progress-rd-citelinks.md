# Progress — rd-citelinks (W0c: reading-list and named-title links)

Task: `docs/plans/readability-plan.md` W0c. Spec: `docs/plans/readability/report-C.md` C1/C4,
`docs/plans/readability-guide.md` R-LINKS and the Never list, `docs/plans/citation-style.md`,
`tools/check_refs.py`, `tools/check_inforce.py`, `tools/check_links.py`. Prototype:
`docs/plans/readability/prototypes/links-theme/titlelink_dryrun.py`.

## Plan (commit order)

1. [x] Policy: reword `citation-style.md` rule 5; R-LINKS already matched the new wording, no change
   needed there; added a clarifying sentence to `agent-briefs.md`.
2. [x] `check_refs.py` invariant + selftest.
3. [x] `tools/fix_reading_list_links.py` (rules 1–3 of C1) + selftest + `--check`.
4. [x] Run site-wide, one commit per directory; checkers + `-W` build after each.
5. [x] Hand-finish leftovers: analysed exhaustively; found none that unambiguously fit rules 2–3
   (see below) — nothing left to hand-edit.
6. [ ] C4 row 2 script: named italic titles in prose linked, first occurrence per H2.
7. [ ] `docs/references/index.md` "How citations work" wording.

## Decisions / notes

* citation-style.md rule 5 now says the bullet head links to the first URL of its own `[^label]:`
  definition; the footnote is unchanged and stays (full citation, hover card, inventory key).
* No change was needed to `readability-guide.md`'s R-LINKS section: it already specifies exactly this
  behaviour (it was written anticipating W0c landing).
* `tools/fix_reading_list_links.py` implements **rule 3** (N markers, N italic titles in the same
  order) in full — the prototype (`titlelink_dryrun.py`) only ever implemented rules 1–2 and dumped
  every multi-marker bullet into one "multi-marker" bucket regardless of whether it actually fit rule
  3. Implementing rule 3 properly (including a title wrapped across a line break, e.g.
  `docs/machines/pecvd.md:470-471`) converted 161 bullets site-wide that the original dry run counted
  as leftovers, which is most of why the final "hand-finish" pass in step 5 found nothing left to do.
* Bullets inside a `{dropdown}` (an in-force patent note) are left untouched by the script, not
  converted in place as R-LINKS step 7 allows: `tools/check_preserved.py` treats *any* change inside a
  dropdown's body as content requiring `--allow-dropdown-edits`, which is a page-by-page judgement call
  this script cannot make safely at 6,000-bullet scale. Left as hand-finish work for whoever reviews the
  in-force notes; not attempted here (rule 2.5's "if in doubt, leave it" applied). 77 bullets, on 15
  pages (see `git grep -n "^:::{dropdown}" -A2 docs/steps docs/machines docs/materials docs/masks
  docs/categories docs/overview` to find them — the note titles name the family).
* Two **pre-existing bugs in `tools/check_preserved.py`** were exposed by this branch (both fixed,
  each with its own commit and selftest case) because it had never before been asked to compare a page
  with an external URL inline in its body (report C: "External links inline in the body of any
  hand-written page: 0" before this branch):
  1. Its bare-URL mask for the "numbers" pass stopped at the first `)`, so a paren-containing DOI
     written in the page's own `<...>` house style (`.../0040-6090(89)90102-8`) was only
     half-masked and the remainder read as a new number. Fixed by trying the angle-bracket form whole
     first, exactly as `check_links.py` already does for the identical reason.
  2. Its number-chaining regex treated an em-dash as a valid range separator alongside hyphen and
     en-dash, so a number at the end of a bullet's head (a patent number) immediately before the
     bullet's own " — " separator got silently *chained* with the next number in the annotation into
     one combined token; linking the head un-chains them (new characters now sit between the number and
     the dash) and reads as a LOST/ADDED pair though no value changed. Fixed by narrowing the chaining
     dash class to hyphen/en-dash only, matching this site's own convention (unspaced en-dash/hyphen for
     ranges, always-spaced em-dash for prose).
* Also fixed: my own first draft of the citation-style.md rule-5 reword used `https://…` as a
  placeholder and a real-looking patent URL in a worked example. `check_links.py`'s footnote-definition
  regex is greedy to the *next* `[^label]:` line or end of file; `citation-style.md` has only two real
  definitions near its top, so `[^pdk-04]`'s "body" already swallows the rest of the file (a pre-existing,
  unrelated quirk — the file is a worked example, not checked content). The placeholder text landed in
  that swallowed region and registered as bogus citer tokens, one a non-resolving URL. Reworded to use a
  bare `<URL>` placeholder (the file's own existing style); verified `check_links.py`'s registry token
  set is now identical between `main` and this branch (1,794 tokens either way) — confirms it neither
  double-counts nor chokes on the new inline links generally, since it never reads body text at all
  (only `[^label]:` definitions), so the 6,000+ new inline links are invisible to it by construction.

## Site-wide run (commit history, one commit per directory)

Site totals after the full run (`tools/fix_reading_list_links.py --check`, idempotent — a second pass
converts 0 more): of 7,074 reading-list bullets, **6,288 converted** (rule 1: 5,986; rule 2: 141; rule 3:
161) and **786 left alone**. All checkers, `check_preserved.py --allow-added urls` (site-wide, 264
pages, 0 undeclared differences) and the `-W` build pass at every commit and at the end.

| Directory | Files | Converted | Left | Notes |
|---|---:|---:|---:|---|
| steps | 171 | 3,645 | 566 | in-dropdown 58 |
| machines | 31 | 887 | 43 | in-dropdown 5 |
| materials | 13 | 342 | 49 | in-dropdown 3 |
| masks | 37 | 1,028 | 16 | in-dropdown 7 |
| categories | 11 | 318 | 96 | no-dash-heavy (R-COMPARE-shaped bullets) |
| overview | 2 | 68 | 16 | in-dropdown 4 |
| others (index.md, glossary.md, figure-conventions.md) | 3 | 0 | — | no `## References` section; nothing to do |

## Step 5: why nothing was hand-finished, by pattern

I looked for cases where a leftover bullet unambiguously fits rule 2 or rule 3 but the script's
mechanical check was too conservative, by recomputing marker/italic counts directly for every leftover
bullet (script: ad hoc, not committed — the analysis is reproducible from `tools/fix_reading_list_links.py`'s
own `page_urls`/`HEAD_TAIL_RE`/`MARK_RE`/`ITALIC_RE`). Found **zero** such near-misses. The leftover
buckets (709 outside dropdowns, 77 inside) break down as:

* **no-dash, 284** (mostly `docs/categories/*`, plus scattered "read term by term" style entries
  elsewhere). The bullet has no ` — ` at all — e.g. `docs/categories/anneal.md:208`: `* Osburn,
  "Silicides", in Fair (ed.), *Rapid Thermal Processing*.[^osburn-1993]`. Rule 1 is defined in terms of
  "the text before the first ' — ' (the head)"; with no dash there is no head/annotation boundary to
  apply it to. Category pages' comparison-style bullets (R-COMPARE territory, a different workstream)
  account for most of these. Not a rule-1/2/3 case; left, per "anything else: leave alone".
* **multi-marker, 403.** Recomputed per bullet: **285** have zero italic titles in the head at all (a
  plain-text name cited under several markers at once, e.g. `docs/machines/pvd-cluster-tool.md:405`:
  "SkyWater Technology, Form S-1 (2021) and Form 10-K for 2023 …[^sec-01][^sec-02]" — two documents, one
  un-italicised head, two markers: nothing to select a title from). **105** have exactly one italic title
  but two or more markers (e.g. `docs/machines/cross-section-sem-profilers.md:343`: "Tencor, *Surface
  Profiling* page (1997) and HRP-200 press release (1996) — …[^tencor-profiling-1997][^tencor-hrp200-1996]"
  — one italicised source plus one plain-named source in the same bullet). **13** have two or more
  italics but still not equal to the marker count (an extra plain-named source alongside two or three
  italicised ones). Rule 3 requires *exactly* N markers matched to N italics in order; every one of these
  403 fails that match by construction, not by a script bug — linking only the matching subset (e.g. the
  Tencor case's one italic) would be a new, unwritten rule, not rule 3, so none were hand-edited.
* **role-in-head, 16.** Every one has a role/backtick in the head and *zero* italic titles (e.g.
  `docs/machines/hdp-cvd.md:410`: `` * SkyWater PDK Authors, `metal_stack.svg` — the FOX, PSG and NILD
  dielectrics.[^pdk-04] `` — a code-formatted filename, no italic to select). Rule 2 needs exactly one
  italic title to link; with none, there is nothing rule 2 can point at. Verified there is no case with
  the needed single italic that the script missed.
* **no-url, 6.** The marker's own definition carries no URL — always because none exists (e.g.
  `[^preston-1927]: Preston, *J. Soc. Glass Technol.* 1927 …` with no online copy known, cited
  identically on `docs/categories/cmp.md`, `docs/machines/cmp-polisher.md` and elsewhere; `[^kern-1970]`
  the same, on four pages). §2.11 forbids inventing a URL; correctly left.
* **in-dropdown, 77** (15 pages, 15 distinct in-force families). See the decision above — genuine
  hand-finish work, intentionally not attempted by this branch.

Conclusion: implementing rule 3 in the script (rather than leaving it as a manual step, as the original
plan assumed before rule 3 existed as code) already did the hand-finish work rules 2–3 called for. What
remains is either a different bullet shape entirely (no-dash), a pattern rule 3 explicitly excludes by
its own "exactly N" wording (multi-marker with a count mismatch), a rule-2 case with nothing to link
(role-in-head, zero italics), a source with no citable URL (no-url), or dropdown content deferred by
policy (in-dropdown).

## Open points for the coordinator

* The 77 in-dropdown bullets (15 pages) are unconverted by design; converting them needs a human
  decision per page plus `check_preserved.py --allow-dropdown-edits` on that page, which this branch's
  script-based approach cannot safely automate at scale.
* Two `check_preserved.py` bugs were fixed on this branch (see above) — worth a look from whoever
  reviews W0b, since they are general fixes, not W0c-specific, and could in principle affect other
  branches' `--allow-added` runs on pages with parenthesised DOIs or a number immediately before an
  em-dash.
