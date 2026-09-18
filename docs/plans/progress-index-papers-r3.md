# Paper index — round 3 progress

Branch `topic/index-papers-r3`. Continues the independent review of
`topic/index-papers-r2`, `tmp/review-index-papers-r2.md` (findings
R2-01…R2-27), after that branch was merged to `main`. Fetches use user
agent `sky130-process-tech docs checker` only, no e-mail/mailto anywhere,
paced with back-off on 429/503. Raw fetches and scripts are under the
shared cache `tmp/papers-review/` (main repo) — the review's own cache,
extended in place per common rule 12 — plus this round's own scripts and
enrichment data under `tmp/papers-review-r3/` (this worktree, gitignored).

Starting point: 50 papers in `data/papers.yaml`, 95 excluded/held in
`data/papers-excluded.yaml`.

## Task 1 — the review's 13-paper table (R2-01…R2-13)

Each verified against two independently fetched sources (Crossref
`works/<doi>` and OpenAlex `works/doi:<doi>`); no disagreement found
between the two for any of the 13 — title, authors, year, venue,
volume/issue/pages all matched (OpenAlex sometimes lacks a `venue`
display name for a proceedings record that Crossref has; not a
disagreement, just missing OpenAlex metadata, same gap round 2 already
tolerated for OpenAlex-only fields).

| # | id | Verdict | Where |
|---|---|---|---|
| R2-01 | doi:10.1109/itc51656.2023.00035 | Included | `paper-dubey-2023a` |
| R2-02 | doi:10.1109/mssc.2024.3380586 | Included | `paper-li-2024a` |
| R2-03 | doi:10.1109/mcsoc64144.2024.00066 | Included | `paper-teo-2024a` |
| R2-04 | doi:10.3390/electronics13091704 | Included | `paper-baungarten-leon-2024a` |
| R2-05 | doi:10.1038/s41928-020-0419-7 | Included (affiliation-inference) | `paper-bishop-2020a` |
| R2-06 | doi:10.1109/led.2022.3144936 | Included (affiliation-inference) | `paper-yu-2022a` |
| R2-07 | doi:10.1109/vlsi-tsa54299.2022.9771013 | Excluded | different node (90 nm), not named |
| R2-08 | doi:10.1109/tim.2025.3635830 | Included (affiliation-inference) | `paper-pepel-2025a` |
| R2-09 | doi:10.1109/tns.2026.3684446 | Excluded | different node (90 nm), not named |
| R2-10 | doi:10.1109/iccad51958.2021.9643513 | Excluded | layout method, not named |
| R2-11 | doi:10.1109/ted.2024.3353702 | Excluded | different SkyWater site (Kissimmee FL), not named |
| R2-12 | doi:10.1145/3649329.3658493 | Excluded | tape-out named, no measurement |
| R2-13 | doi:10.1109/fpl53798.2021.00085 | Excluded | fabrication-ready layout only, no measurement |

R2-07/09/11 turned on the "another SkyWater process/site" exclusion
clause in §1 exactly as the review flagged; R2-10/12/13 turned on the
existing no-measurement and tape-out-only clauses. The round 3 checklist
in the review (its own §"Round 3 checklist") explicitly assigns
R2-07/09/10/11/12/13 to `papers-excluded.yaml`, which this round follows.

The review's "additionally not triaged at all" list (13 named-process,
no-silicon items) and the Authorea dedup note (R2-23) were also
processed — see Task 2.

Wording nits:

* **R2-20** applied: `doi:10.1109/devic63749.2025.11012450`'s reason now
  states explicitly that the abstract's "fabricated using ... the PDK" is
  used of the design/layout, not of silicon.
* **R2-21** applied: `doi:10.5281/zenodo.18008454`'s reason now states
  explicitly that it is excluded under the "not a paper" rule *despite*
  giving measured SKY130 values, and cross-references the open owner
  question added to the design doc §7 (whether a presentation with a
  genuine measurement should be included).

## Task 2 — schema extension and the new page

Per the review's recommendation, `data/papers-excluded.yaml` records
gained `authors`, `venue` and `names_process` (a literal text match for
"sky130"/"skywater" in the title or reason, the same test as `basis:
named-process`). All 95 pre-existing records were backfilled (Crossref
for `doi:`, OpenAlex fallback for DOIs not in Crossef's registry such as
Zenodo/arXiv-DOI records, the arXiv API for `arxiv:` ids; the two
`web:woset-*` ids have no fetchable record, so `authors: []` and
`venue: WOSET`). `tools/check_papers.py`'s `EXCLUDED_KEYS` and
`check_excluded` were updated accordingly.

`tools/gen_papers.py` gained `gen_named_process()`, generating
`docs/references/papers/designed-on-sky130.md` (label
`papers-designed-on-sky130`) from every `names_process: true` record,
grouped by year, each line giving title/authors/venue/year, a DOI or
arXiv link, a **Held** mark for `status: held`, and the reason verbatim.
Linked from `index.md`'s "Other views" list with an explicit note that it
is not part of the index. `docs/plans/paper-index-design.md` §2.2, §4 and
§7 updated to match; no change to `papers.yaml`'s inclusion rules (§1).

Topic decision: no new controlled topic was added for the
SkyWater-Bloomington device-R&D strand (CNFETs, monolithic-3D RRAM,
radiation/RTN reliability) — the existing topics (`beol-integration`,
`rram`, `device-characterisation`, `reliability`, `radiation`) already
fit every record found, as the pre-existing entries for the same strand
already show (see Task 3).

## Task 3 — re-run discovery

### OpenAlex `fulltext.search`

The round 2 review's own cache (`tmp/papers-review/cands.json`, 1186
works after dedup) already covered `fulltext.search:sky130` in full (348
of 348) but `fulltext.search:skywater` only to 600 of 696 (its `pages: 3`
cap); this round fetched the missing page 4 (96 more works, 61 new
candidates after dedup) and re-ran the abstract/full-text triage
(`tmp/papers-review-r3/rebuild_excluded.py` and its inline triage notes)
over the combined 1247-work pool. Besides the review's own 13-item table,
this surfaced ~30 more named-process, no-silicon records now recorded in
`data/papers-excluded.yaml` (self-published Zenodo items — several with
extraordinary, unverifiable claims — education papers, and simulation-only
circuit papers) and confirmed several borderline items as **held**
(`doi:10.24908/pceea.2026.21530`, `doi:10.1109/mspec.2025.11120331`,
`doi:10.1109/mwscas67364.2026.11680747`: no public abstract or no named
process for the fabrication claim).

### OpenAlex `raw_affiliation_strings.search:SkyWater`

35 works (one page, in full). Most of the SkyWater-Bloomington
CNFET/RRAM/monolithic-3D strand this turned up was already in
`data/papers.yaml` (from earlier rounds' title/abstract searches, which
catch it whenever the paper itself says "commercial silicon foundry" or
similar) or `data/papers-excluded.yaml`. Net new: `paper-bishop-2020a`,
`paper-yu-2022a` (Task 1, R2-05/06), `paper-pepel-2025a` (R2-08), plus
five excluded records (R2-07, R2-09, R2-11, and two more: the GF 12LP
FinFET sibling of an already-excluded S90LN paper, and confirming no
further gaps). Several hits were meteorology/limnology papers with an
unrelated "Sky Water"-named research buoy or station in the affiliation
string — false positives, not recorded.

### Citing-works pass

`filter=cites:<id>` for the 33 `named-process` papers in
`data/papers.yaml` that carry a `fabrication` quote and a DOI (every
paper in the index that reports fabricated SKY130 silicon), up to 200
citing works per seed. See the table below for per-seed counts.

| Seed (included paper) | Citing works | New (not already in either file) |
|---|---|---|
| doi:10.1109/lssc.2022.3188925 (OpenFASoC temperature sensor) | 25 | 17 |
| doi:10.1109/icm56065.2022.10005367 | 4 | 4 |
| doi:10.1109/access.2023.3336408 | 0 | 0 |
| doi:10.1109/itc51656.2023.00035 (paper-dubey-2023a) | 5 | 5 |
| doi:10.1109/iscas46773.2023.10182052 | 1 | 0 |
| doi:10.1109/bcicts54660.2023.10310944 (cryogenic model) | 4 | 1 |
| doi:10.1109/fpl60245.2023.00070 | 4 | 2 |
| doi:10.23919/vlsitechnologyandcir57934.2023.10185414 | 19 | 18 |
| doi:10.1109/iscas46773.2023.10181702 | 1 | 0 |
| doi:10.1109/iolts59296.2023.10224899 (space-shuttle paper) | 0 | 0 |
| doi:10.1109/iscas46773.2023.10181379 (SKY130 OpenRAM) | 5 | 2 |
| doi:10.1109/isqed57927.2023.10129298 | 2 | 1 |
| doi:10.1109/tcsi.2024.3355070 | 12 | 10 |
| doi:10.1109/cicc60959.2024.10529028 | 3 | 0 |
| doi:10.1109/mdat.2024.3444728 | 2 | 2 |
| doi:10.1109/lad62341.2024.10691811 | 17 | 17 |
| doi:10.1109/mcsoc64144.2024.00066 (paper-teo-2024a) | 16 | 14 |
| doi:10.1109/mdat.2024.3405892 | 12 | 9 |
| doi:10.1049/ell2.70036 (floating-gate cell) | 1 | 1 |
| doi:10.1109/mssc.2024.3380586 (paper-li-2024a) | 1 | 1 |
| doi:10.3390/electronics13091704 (paper-baungarten-leon-2024a) | 6 | 3 |
| doi:10.1109/ispacs68724.2025.11383342 | 0 | 0 |
| doi:10.1109/austrochip67945.2025.11183685 | 0 | 0 |
| doi:10.1109/iedm50572.2025.11353729 | 0 | 0 |
| doi:10.1109/isqed65160.2025.11014456 | 2 | 1 |
| doi:10.1109/vlsi-soc64688.2025.11421773 | 0 | 0 |
| doi:10.1109/iceee67194.2025.11261982 | 0 | 0 |
| doi:10.1109/sbcci66862.2025.11218693 | 0 | 0 |
| doi:10.1109/sensors59705.2025.11330220 | 0 | 0 |
| doi:10.1109/mdat.2026.3670063 (paper-dubey-2026a) | 0 | 0 |
| doi:10.1109/jxcdc.2026.3670667 (paper-didin-2026a) | 0 | 0 |
| doi:10.1109/lascas67804.2026.11457090 | 0 | 0 |
| doi:10.1109/cae69023.2026.11450324 | 0 | 0 |

108 not-already-known citing works in total, after de-duplication across
seeds by id and title. Filtered by the same named+measured/fabricated
regex used for the fulltext sweep: **zero** named a SKY130 process
*and* reported a fabrication or measurement result — the highest count
(7) named the process without any fabrication wording (all
simulation/synthesis/education papers), now recorded in
`data/papers-excluded.yaml` (`doi:10.1109/peds63958.2025.11144891`,
`doi:10.1109/sbcci66862.2025.11218642`,
`doi:10.1109/icetran66854.2025.11114230`,
`doi:10.1109/lascas64004.2025.10966270`,
`doi:10.1109/access.2024.3478832`, `doi:10.3390/math12142267` with its
preprint noted in the reason). No new paper meeting the inclusion rules
(§1) was found by the citing-works pass; it mainly re-confirms the
sweep above rather than adding to it.

## Disagreements between sources

None found. Every Crossref/OpenAlex pair checked (Task 1's 13 papers,
plus every DOI enriched for the excluded-file backfill) agreed on title,
authors, year and venue; OpenAlex occasionally has no `primary_location`
for an obscure proceedings record that Crossref has, which is treated as
missing data, not a disagreement, consistent with round 2's practice.

## Checks

```
tools/check_filings.py       86 filings checked, 0 problems
tools/check_machines.py      30 machine pages checked, 0 problems
tools/check_masks.py         36 mask pages checked, 0 problems
tools/check_materials.py     12 material pages checked, 0 problems
tools/check_papers.py        57 papers checked, 0 problems (142 excluded or held papers checked)
tools/check_patents.py       211 patent families checked, 0 problems
tools/check_refs.py          264 written pages checked, 0 with problems
tools/check_steps.py         171 pages, 171 written, 0 stubs, 0 with missing headings
tools/gen_filings.py --check   6 pages checked, 0 problems
tools/gen_patents.py --check   6 pages checked, 0 problems
tools/gen_papers.py --check    9 pages checked, 0 problems
uv run sphinx-build -W -q -b html docs tmp/build-papers-r3   clean (exit 0)
```

`tools/check_papers.py --online` — 0 problems (every DOI, arXiv id and
`web:` record's title, authors, year, container, volume, issue and pages
still match Crossref/OpenAlex/arXiv; the one title mismatch caught mid-round
— `paper-li-2024a`'s Crossref title carries a subtitle
("...Paving the Way for Low-Cost and Robust Flexible Wearable Sensing")
that this round's first draft omitted — was fixed before this run).
`--links` reports one transient result, inherited from round 2 and
unrelated to this round's changes: `arxiv:2604.21625`'s OSTI mirror
(`https://www.osti.gov/servlets/purl/3363571`) returns HTTP 0 again (round
2 saw the same host-unreachable result on 2026-09-19); the arXiv copy
still resolves, so the record is left as is per common rule 11.

## Summary

Before this round: 50 included papers, 95 excluded/held.
After this round: 57 included papers (+7: paper-dubey-2023a,
paper-li-2024a, paper-teo-2024a, paper-baungarten-leon-2024a,
paper-bishop-2020a, paper-yu-2022a, paper-pepel-2025a), 142 excluded/held
(+47 new considered-and-rejected records: 6 from the review's R2 table
(R2-07/09/10/11/12/13), the rest from its "not triaged at all" list and
from re-running the OpenAlex `fulltext.search` and
`raw_affiliation_strings.search` surfaces to completion, plus 6 from the
citing-works pass). `data/papers-excluded.yaml` records gained `authors`,
`venue` and
`names_process` (125 of 142 name the process); the new page
`docs/references/papers/designed-on-sky130.md` lists all 125, generated
by `tools/gen_papers.py`. No topic addition was needed (owner decision,
§7 of the design). Two wording nits (R2-20, R2-21) applied. No
disagreements were found between Crossref and OpenAlex/arXiv for any
record checked this round. Blocked/limited services: none newly hit this
round (DBLP and Semantic Scholar were not retried, consistent with round
2's pacing decision); the one HTTP anomaly (`--links` on
`arxiv:2604.21625`'s OSTI mirror) is transient and pre-existing.

Left for round 4: DBLP retry, full texts of the held papers (leading with
the 4 K cryogenic SPICE model), a second raw-affiliation pass for
"Cypress" to extend the Bloomington lineage strand earlier, and a
citing-works pass for the SkyWater PDK description paper
(`paper-edwards-2020a`, no DOI — needs an OpenAlex title search rather
than `cites:<doi>`).
