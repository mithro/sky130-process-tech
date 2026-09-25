# Link check report C (the `--include-generated` second check)

This is the follow-up `docs/plans/link-check-2026-09b.md` section
"(c) `--include-generated`" asked for: the four generated-page tokens dead
on their *first* check (2026-09-20) needed a second check ≥ 24 h later
before R-WAYBACK's two-check rule (`docs/plans/readability-guide.md`)
applies. Generated 2026-09-25, five days after the first check.

## Method

Ran `uv run tools/check_links.py --include-generated` to completion,
chunked in the foreground with `--time-budget` and resumed from its own
cache each time, over the full 2540-token corpus (hand-written pages +
`docs/references/{patents,papers,filings}/`). The cache was seeded from an
orphaned worktree's hand-written-page-only cache (a leftover directory not
in `git worktree list`, read-only, never written to) to avoid re-fetching
tokens report B had already checked; `--reclassify` was then run once
(310 entries changed — the seed cache predated the IOP/`perfdrive.com`
cross-domain-challenge fix). The soft-404 check, skipped on generated pages
in report B ("future work"), was run to completion this round.

## Counts

* Tokens: 2540 (1459 URLs, 1081 DOIs).
  * ok: 2058
  * blocked-to-scripts: 443
  * redirected-permanently: 20
  * soft-dead?: 8
  * dead: 11

Raw counts aren't directly comparable to report B's (the `--reclassify` and
five days of host-side churn both move numbers around); the important
figures are the per-token ones below.

## 1. The four first-check-dead tokens, second check (task item 1)

### `doi:10.5281/zenodo.20032068` and `doi:10.5281/zenodo.20950316` — rule 11 applied

Both `data/papers-excluded.yaml` records (excluded papers, not part of the
index proper). Both still HTTP 410 Gone at Zenodo, independently confirmed
(this branch's run; a direct re-fetch of `doi.org/10.5281/zenodo.*`).

**Snapshot search (R-WAYBACK step 1–2), both records:**

* Wayback availability API, both `https://zenodo.org/record/<id>` and
  `https://zenodo.org/records/<id>` forms: `archived_snapshots: {}` for
  all four URLs.
* CDX API, both URL forms: empty for `.20032068`; for `.20950316`, two
  rows, both non-200 (`410` and `-`) — the capture history itself only
  ever saw the record already gone.
* `archive.ph/newest/` (R-WAYBACK step 4's "by hand as well"): HTTP 429 on
  the one try for each (rate-limited); per common rule 9 (agent-briefs.md),
  never looped — inconclusive, not a hit, same precedent as report B's
  AMAT-RTP finding.

**No snapshot anywhere** → rule 11 of `docs/plans/agent-briefs.md` applied,
in the YAML, not the generated page: the verbatim quotation was removed
from each record's `reason` field, paraphrased without changing its
substance, and a dated note added ("no longer retrievable as of
2026-09-25 ... evidence for this description is now weak, resting only on
the record as it read before it went offline"). No `archive_url` — none
was found, and R-WAYBACK step 5 forbids an archive form for a DOI in any
case (the DOI citation itself is unchanged, still linked). Regenerated
`docs/references/papers/designed-on-sky130.md`.

### `https://www.osti.gov/servlets/purl/3363571` — rule 11 applied

A `free_full_text` entry of `paper-beall-2026a` (`data/papers.yaml`), an
alternate free copy of a paper whose primary free copy is arXiv (still
live, HTTP 200 both checks). Second check: still times out
(`urlopen error timed out`), confirmed on a direct re-fetch too.

Same snapshot search as above (availability API, CDX, `archive.ph/newest/`
— one 429): no snapshot anywhere. Rule 11 applied: added
`dead_since: '2026-09-25'` to the `free_full_text` entry — no quotation
rests on this specific copy (the paper's fabrication quote is sourced from
the abstract, verified independently of OSTI), so nothing to remove there;
the record is kept as a dated mention rather than deleted, alongside the
still-retrievable arXiv copy. No `archive_url` (none found).

`tools/check_papers.py`'s `free_full_text` schema now accepts a link with
`dead_since` alone (this case) or `archive_url`/`archive_date`/`dead_since`
together (a verified snapshot, R-WAYBACK's archive-first form — archive
URL first, original in backticks, "dead since", "Wayback Machine capture
of YYYY-MM-DD"); `tools/gen_papers.py` renders whichever applies via a new
`free_copy_text()` helper. Added `--selftest` to `check_papers.py` (it had
none before), covering both new shapes and six ways they can be rejected.
Regenerated `docs/references/papers/index.md`; the OSTI line now reads
"OSTI copy, `` `https://www.osti.gov/servlets/purl/3363571` `` —
repository copy (OSTI); no longer retrievable as of 2026-09-25 (no Wayback
or archive.today copy found)".

`check_patents.py`/`gen_patents.py`/`data/patents.yaml` and
`check_filings.py`/`gen_filings.py`/`data/filings.yaml` needed **no**
schema or generator change for this round: no patents-page token was dead
in either check, and `filings.yaml` already carries a native `urls.wayback`
field (a different, pre-existing mechanism, unrelated to this R-WAYBACK
extension) — both generators' `--check` still pass unmodified.

### The Wayback capture of the SEC filing — recovered, no action

`https://web.archive.org/web/20230502184124/.../ny20006439x1_def14a.htm`
(the `skywater-def-14a-2023-04-25` filing's `urls.wayback`): HTTP 200 this
run. Confirms report B's read ("intermittent, not dead" — it 404'd once in
that run and recovered on an immediate re-check). No citation change.

## 2. New findings this round, not yet actionable (first check only)

Two **new** dead tokens turned up in today's full pass — neither is one of
the original four, and neither has had a *second* check yet, so R-WAYBACK's
two-check rule does not apply to either. No action taken; both should be
re-checked after 2026-09-26.

* **`doi:10.37934/sej.3.1.1421b`** (`data/papers-excluded.yaml`, "Integrating
  Design for Testability Technique into OpenLane with Skywater
  130-Nanometer Process Design Kit") — DNS resolution failure
  (`Name or service not known`), confirmed on an independent direct fetch.
  A small journal domain; plausibly transient, but this is its first check
  ever (generated pages were never checked before report B, and this
  specific token wasn't among the four report B found dead that day).
* **`https://web.archive.org/web/20230329202011/.../skyt-20230101.htm`**
  (the `urls.wayback` mirror of `data/filings.yaml`'s SkyWater 10-K for
  fiscal year 2022) — HTTP 404, confirmed on a manual recheck (amid some
  transient connection-refused noise from this environment repeatedly
  hitting `archive.org` in a short window — a second, cleaner recheck
  still returned 404, and a CDX lookup for alternate captures of the
  underlying EDGAR URL returned nothing usable). First check for this
  specific token.

## 3. Soft-dead? suspects and bot-wall hosts (task item 2)

**Soft-dead? suspects.** The soft-404 check ran to completion on the
generated-page corpus for the first time (report B explicitly skipped it
there, "future work"). **Zero new suspects found among the ~750
generated-page tokens.** The 8 suspects in today's report are the same
pre-existing hand-written-page ones report B already reviewed and cleared:
`arxiv.org/abs/1908.06182` (LIU-2020), `fossi-foundation.org/...` (ANN-03),
two `github.com/.../blob/...` raw-data pages (generic GitHub blob-viewer
titles), and three `web.archive.org` Novellus/Strasbaugh captures (generic
1990s page titles). Not re-reviewed again since nothing about them changed
this round.

**Bot-wall hosts report B found via `--include-generated`.** All re-fetched
fresh this run (not carried over from any cache), all still `403` /
`blocked-to-scripts`, same as report B:

* `espacenet.com` — all 34 sampled Espacenet record-page tokens, 403.
* `academic.oup.com`, `dl.acm.org`, `escholarship.org`,
  `ietresearch.onlinelibrary.wiley.com`, `onlinelibrary.wiley.com`,
  `pubs.aip.org`, `authorea.com`, `mdpi.com`, `techrxiv.org` — each of the
  one-per-host sampled tokens, still 403.

No host's behaviour changed; nothing to fix.

## Checker suite

All pass: `check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_materials.py`, `check_masks.py`, `check_papers.py`
(56 papers, 0 problems, 154 excluded/held checked),
`check_papers.py --selftest`, `check_patents.py` (552 families, 0
problems), `check_filings.py` (89 filings, 0 problems), `check_inforce.py`,
`gen_papers.py --check`, `gen_patents.py --check`, `gen_filings.py --check`,
`gen_index_links.py --check`, and `sphinx-build -W -q -b html docs
tmp/_build/html`.

`tools/fix_reading_list_links.py --refresh` and
`tools/link_named_titles.py --refresh`: 0 files changed by either — no
hand-written page cites the OSTI or Zenodo tokens touched this round.

## A tool oddity, documented not fixed

`tools/check_links.py`'s bare-URL extraction does not actually exclude a
URL written between backticks: the "original, dead since ..." URL of an
already-converted R-WAYBACK citation (THUNG-2016, TEL-PROBER, and now the
OSTI free copy above) is still picked up by the fallback `URL_RE` scan and
reported "dead" on every future run, even though R-WAYBACK step 3 says
backticks make "the checker stop reporting it". This is pre-existing
behaviour, not introduced here, and explains why THUNG-2016 and TEL-PROBER
still appear in this report's Dead table above (rows 7 and 11) despite
being fully handled in report B — no action needed on either. Left
unfixed: changing `check_links.py`'s extraction regex was not asked for by
this task and risks behaviour report B already relied on elsewhere.

## Needs a human with a browser

Carried over from report B, still true (re-verified this round where
noted):

* **The IOP Science / Radware finding** (report B). 136 DOI citations
  resolving to `iopscience.iop.org` cannot be verified by any script here;
  a person in an ordinary browser should not hit the challenge.
* **Every `blocked-to-scripts` host**, confirmed live via Wayback, a
  differently-configured request, or a browser-UA `curl` in an earlier
  round or this one — still worth a click-through for first-hand
  confirmation: `sec.gov`, `cdc.gov`, `astm.org`, `startribune.com`,
  `appliedmaterials.com`, `businesswire.com`, `forbes.com`, `linkedin.com`,
  `indeed.com`, `glassdoor.com`, `researchgate.net`, `semimarket.com`,
  `openlibrary.org` (intermittent), `iopscience.iop.org` /
  `validate.perfdrive.com` (via `doi.org`), and — re-confirmed fresh this
  round — `espacenet.com` (34 records, all 403), `academic.oup.com`,
  `dl.acm.org`, `escholarship.org`, the Wiley family, `pubs.aip.org`,
  `authorea.com`, `mdpi.com`, `techrxiv.org`.
* **`spie.org/Publications/Book/924283`** (report B) — flickered to a
  soft-404 once, resolved fine on immediate re-checks; still not
  actionable, still worth the owner's own confirmation if they've
  personally seen the 404.
* **New this round, first check only — do not action yet, recheck after
  2026-09-26:**
  * `doi:10.37934/sej.3.1.1421b` — DNS failure. If a human can resolve
    `doi.org/10.37934/sej.3.1.1421b` in a browser right now, that would
    confirm this is transient rather than a genuinely dead journal domain.
  * `https://www.sec.gov/Archives/edgar/data/1819974/000181997423000011/skyt-20230101.htm`
    — the sec.gov original is script-blocked as always, but its two
    fallback copies disagree: the Wayback mirror 404s (this section) while
    the investor-relations PDF mirror
    (`https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/0a7f9a2c-fc5a-4db4-8cff-85ff40d93adf.pdf`)
    still resolves fine. Worth a human confirming the Wayback capture is
    genuinely gone (not this environment's own archive.org flakiness)
    before it is re-checked in ≥ 24 h.
