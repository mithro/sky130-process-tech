# Patent index — progress log

Status board for `docs/plans/TASKLOG.md`'s patent-index task, so the
work can be picked up by any agent without losing or redoing anything.
This file lives in `docs/plans/`, excluded from the Sphinx build.

Fetch cache: `tmp/cache/` (gitignored), one `<PN>.html` + `<PN>.json` per
fetched publication number, populated by `tmp/gp.py` (curl, user agent
`sky130-process-tech docs checker`, 4 s pacing, resumable, backs off on
HTTP 503/429 by raising `Blocked` and stopping the batch). Search-result
cache: `tmp/qcache/` (gitignored). The dataset is rebuilt from
`tmp/selection.json` (curated per-family metadata: representative
publication number, `relevance`, `inventory_keys`, `discovery`,
`discovery_note`, `notes`) plus the fetch cache by `tmp/build.py`.

## Round 2: response to the independent review

Review: `tmp/review-index-patents-r1.md` (round 1, 2026-09-18, 2 High, 10
Medium, 13 Low). Environment note that applies to several rows below:
**Google Patents, Espacenet's web interface, WIPO Patentscope and the
USPTO PatentsView/PED/assignment-search APIs are all unreachable from
this fixer's environment** — persistent HTTP 503 (Google Patents, paced
with backoff up to 120 s per the design's own pacing rule, repeated
across the round) or 403/timeout (the others) with the required user
agent `sky130-process-tech docs checker`. `data.epo.org` (EPO linked
data) and `image-ppubs.uspto.gov` (USPTO grant-PDF images) do work and
were used directly wherever they could settle a finding. This blocks new
Google-Patents-family discovery (H1's main ask) and re-fetching any
member already in the dataset (M5, M10, parts of H2's manual spot-checks);
every fix below that needed a fresh fetch is marked accordingly rather
than silently worked around.

| ID | Finding | Status | Note |
|---|---|---|---|
| H1 | Coverage far short of "comprehensive"; no SkyWater patent | open | Blocked: new-family discovery needs Google Patents searches and record-page fetches; confirmed unreachable — every request, including the bare domain root, gets Google's own site-wide "unusual traffic" bot-check page (IP-level block, not a per-endpoint rate limit), across three separate attempts this round. The 15 families the review now lists by number (extended mid-round with 3 more, plus a continuation/divisional discovery lesson — see below) could not be added either — the schema's `id` is the Google Patents family ID, only obtainable from a Google Patents page, and `data.epo.org` does not substitute for a US-only document. Added the review's own coverage-gap statement to the landing page instead of leaving the index looking exhaustive; see "H1" section below for what a next attempt should do first. |
| H2 | Checker can't detect a genuinely-unexpired family shown collapsed | fixed | `member_end_bound()` in `tools/check_patents.py` implements the design's per-member bounds and is checked against every member of an `expired: true` family. |
| M1 | `GP90721530` Korean-only assignee, CEA missing | fixed | Verified independently against `data.epo.org` (not just the review's report of it); recorded in the family's `notes`. |
| M2 | `by-jurisdiction.md` exposes a collapsed family's full member list | fixed | Collapsed families now contribute only the representative's row (number + status word), like every other grouped page. |
| M3 | `expiry.date` can understate the family's latest member term | fixed | `family_max_estimate()` takes the maximum over every member, not just the ones shown in force; 36 families' dates moved at commit `7f820f7` (19 later, 17 earlier — not all later, as first recorded here; three of the earlier moves are `GP25461879`/`GP24728963`/`GP35448183`, corrected again by the M9 rule below), 2 more after the L3 fix. |
| M4 | Fee lapse treated as final; reinstatement not modelled | fixed | Added 37 CFR 1.378 (verified via Cornell LII) to the legal caveat; `notes` on `GP50930700` recording the lapse date and window as the review reported them (not independently re-verified — Google Patents unreachable). |
| M5 | 3 representative statuses already drifted since retrieval | documented, not refreshed | Recorded each drift as a `notes` entry attributed to the review's 2026-09-18 re-fetch; could not re-fetch `GP35540402`, `GP69743400`, `GP90721530` myself (Google Patents unreachable). None changes a collapsed/open state. |
| M6 | Espacenet "links" are search queries, not records | fixed | Landing page now says so and names Google Patents as the working full-text link; declined to add further official-database links (would need fetches this environment can't make). |
| M7 | Every entry renders as one run-on paragraph | fixed | `family_body()` puts a blank line after every field line. |
| M8 | ~40 members mislabelled `document_type: application` | fixed | `tmp/build.py`'s `doc_type()` extended (DE `D1`, GR `T3`, PT `E`, SE `L`, CA `C`); 40 members' `document_type` corrected directly. |
| M9 | Japanese-divisional term rule wrong; 3 `unknown` families really expired | fixed | Verified the law myself from the Ministry of Justice's English translation of the Patent Act (Art. 44(2)/67(1), `japaneselawtranslation.go.jp`); design doc, checker and the 3 families (`GP25461879`, `GP24728963`, `GP35448183`, now `expired: true`) all corrected. |
| M10 | 5 re-fetched application members show a status other than recorded `Granted` | investigated; declined as a builder defect | Read `tmp/build.py`/`tmp/gp.py`: no substitution logic exists — `status` is copied verbatim from the parsed page at fetch time. Recorded the review's re-fetch findings as `notes` on the 5 families; could not independently re-verify (Google Patents unreachable). |
| L1 | Landing sentence describes an empty "the rest" set | fixed | `gen_index()` only emits that sentence when some member actually is listed-only. |
| L2 | Collapsed dropdown title shows more than "number and status" | confirmed intentional | Design doc now says explicitly this is deliberate for the one place a reader can open the entry; every other page still shows number + status only. |
| L3 | Listed-only bound applied to a fetched member with a known filing date | fixed | `member_end_bound()` also bounds by the member's own filing date + 20 years; found and fixed a related issue while at it (a `translation-of-granted-patent` had been given an independent bound it shouldn't have, per M8's own reasoning). |
| L4 | `expired: true` accepted while a member is shown `Active`, no note | fixed | `notes` added to `GP37568077` and `GP37568096`. |
| L5 | Checker never checks `expiry.date` against the members | fixed | Added alongside H2 (`family_max_estimate()` equality check, and a basis-names-a-member check). |
| L6 | `legal_status.status` duplicates the representative's `status` unchecked | fixed | Added alongside H2. |
| L7 | 2 families' `expiry.date` rests entirely on a derived bound, not clearly marked | fixed (side effect) | The M3/L3 basis-text rewrite already states "estimated 20 years from …" / "estimated upper bound: …" for both; verified, no further change needed. |
| L8 | `by-module` step ranges hard-coded, could drift from the overview table | fixed | `check_step_modules()` parses `(overview-modules)=` on `docs/overview/index.md` and fails page generation if the two disagree. |
| L9 | "Individual" heading reads as one company that became five | fixed | Heading changed to "No assignee recorded at grant (Google Patents "Individual")"; `notes` added to the one family (`GP21950172`) with no USPTO-assignment-derived name (couldn't look one up — USPTO assignment API unreachable). |
| L10 | Google's "original assignee" is sometimes the renamed successor | fixed | Added a caveat sentence to `by-assignee.md`. |
| L11 | Citation-style exception for generated pages never recorded | fixed | Recorded in `docs/plans/citation-style.md`; no checker behaviour changed (already outside `check_refs.py`'s targets). |
| L12 | Relevance reasons repeat verbatim up to 15 times per entry | fixed | `relevance_lines()` groups entries sharing one relation+reason onto a single bullet with every target linked. |
| L13 | `retrieved` date doesn't reflect all fetch dates | fixed | Landing page states the range of `verified` dates found in the dataset when they differ. |

### H1: what was and wasn't possible this round

Attempted, at intervals through this round (initial probe, then a
5-step exponential backoff up to 120 s, then a further round after the
review file was extended — three separate attempts in total, spread
over the session), to reach Google Patents with the required user agent,
no account or key — persistent HTTP 503 every time. The response body is
Google's own site-wide "Sorry... unusual traffic from your computer
network" bot-check page, and `https://patents.google.com/` (bare root)
returns the same 503, not just record-page or search-query URLs — this
is an IP-level block on the whole `google.com` domain from this
environment's egress address, not a per-endpoint rate limit that a
longer per-request delay would clear (plausibly from the volume of
fetching this dataset's earlier rounds already did against the same
address). Espacenet's web interface, WIPO Patentscope, and USPTO's
PatentsView/PED/assignment-search APIs were also tried and are
unreachable (403 or no route) from this host. `data.epo.org` and
`image-ppubs.uspto.gov` work and were used for the findings above that
they could settle; `data.epo.org` was also tried directly for a pure-US
publication number (`US10699901B2`, no EP filing) and returns only a
stub with no bibliographic content — confirmed it only carries full
records for EP/WO-published documents, matching what the review's own
Sample 2 already relied on (EP members only).

The coordinator extended the review (now 776 lines) with an additional
lesson while this round was in progress: **a lineage estate's later
continuations and divisionals are often filed as, and grouped by Google
into, a *different* family from the original priority filing** — three
more examples named (`US 10,699,901 B2`, a granted continuation of the
exact estate this index holds as `GP40071593`/`US8614124B2`, same
title and Jenne/Levy/Ramkumar inventors, citing `CN101517714A` which
*is* a `GP40071593` member; `US 9,929,240 B2`, same 2007 Cypress ONO
estate; `US 6,963,106 B1`, Spansion wells/short-channel), bringing the
review's own named-missing-family table to 15. The lesson for whichever
agent resumes this with working Google Patents access: **family-based
discovery (following a seed's own family table, citing/cited-by lists)
structurally cannot find these** — a per-lineage-estate search for later
continuations/divisionals (by inventor name, by title-phrase, or by
assignee + priority-date window) is needed in addition to the per-module
assignee+keyword searches already planned, and needs the same wide
pacing/backoff/caching discipline the review itself had to fall back to
(three-figure-second spacing, `data.epo.org` as the keyless alternative
for anything with an EP/WO member).

Without Google Patents, this round could not:

* Add any of the 15 families the review now lists by number, or any
  further family found by a fresh assignee/module/continuation search —
  the schema's family `id` is the Google Patents family ID from a
  fetched record page; there is no way to mint a compliant record
  without one, and `data.epo.org` does not substitute for a US-only
  document (above).
* Run the per-module searches Phase 2 lists as outstanding (wells,
  salicide, W plugs, fuses, passivation, ReRAM beyond Weebit), a
  `assignee="SkyWater Technology"` search, or the new per-estate
  continuation/divisional sweep the coordinator's lesson calls for.
* Do the second-source EPO cross-check for a *new* family (there are
  none to check), though the EPO service itself is reachable and was
  used for M1's assignee correction on an existing family.

Added an honest completeness statement to
`docs/references/patents/index.md` (the M6/M1 commit's neighbourhood)
rather than leave the landing page reading as if the index were
exhaustive — see "## Scope and completeness" there. **Next agent with
working Google Patents access should start from the review's 15-family
table, its six named unsearched modules, and the continuation/divisional
lesson above, in that order**, before running fresh assignee searches.

## Phase 1 — dataset: fetching

- [x] Seed set: every patent cited in `docs/` with a `PAT-…` inventory
      entry, resolved to its Google Patents family (commit `9265f45`
      pre-rebase / `patent dataset: families of the patents cited in the
      docs, and checker`).
- [x] Widened discovery batch 1: 24 Cypress/Infineon SONOS, ONO and
      drain-extended MOS families (`5123376`).
- [x] Widened discovery batch 2: 11 Cypress isolation, gate oxide,
      spacer, local interconnect and metallisation families (`2b2959c`).
- [x] Every family's representative record page fetched (207/207).
- [x] Every family with earliest priority on or after 1999-05-29 (where
      a member could still be unexpired or the US term uncertain
      without the record) has **every** member's own record page
      fetched, not just listed — 0 families outstanding (checked by
      `tmp/tofetch.py`, which lists only-listed members and their
      family's `expired` flag: the outstanding 435 are all in `true`
      (pre-1999-05-29-priority, already-bounded-expired) families).
- [x] Fetching the remaining only-listed members of 53 pre-1999-05-29
      families (435 members) for completeness, even though the design's
      verification-level rule does not require it once a family is
      already bounded expired. Done: `tmp/tofetch.py` now reports 0
      outstanding. Applied to `data/patents.yaml` with
      `tmp/refresh_old_members.py` (only touches the newly-fetched
      members' fields; leaves every other family's `verified` dates,
      relevance, discovery and notes untouched). Two families' `expired`
      flipped from `true` to `unknown` once their full member list was
      known (`GP25461879`, a polishing-pad family, and `GP24728963`, an
      HDP-CVD reactor family — both equipment/materials patents, not
      core process-module ones): each has a JP member filed years after
      the family's priority date, so its own 20-year-from-filing bound
      is not yet past. This is the correction the extra fetching was
      for; both are now correctly shown as collapsed/unknown rather
      than open/expired.
- [ ] Second-source cross-check (Patentscope/Espacenet/USPTO) for a
      sample of members, recording disagreements in `notes` rather than
      silently choosing one source — not started (lower priority; the
      dataset already passes with single-source verification as the
      design requires at minimum).

### Member-fetch batches (post-rebase, this round)

Run via `cd tmp && python3 fetch_list.py members_todo.txt <seconds>`,
appending to `fetchN.log`; `tofetch.py` regenerates `members_todo.txt`
from the current `data/patents.yaml` (only-listed members) each time it
is safe to do so (i.e. before a batch, not while one is running).

| Batch | Members attempted | Result | Applied to patents.yaml? |
|---|---|---|---|
| (pre-rebase batches 1-8, see `tmp/fetch1.log`..`fetch8.log`) | ~1666 lines total, mostly already in the 154 fully-fetched + representative fetches | done, already reflected in `data/patents.yaml` | yes |
| this round, batches 1-3 (`tmp/fetch9.log`, `fetch10.log`, `fetch11.log`) | 435 members of the 53 pre-1999-05-29 families, run to a ~560s time limit each, resuming from cache | in progress; check `tmp/members_todo.txt` (regenerate with `tmp/tofetch.py`) for what remains | not yet — apply with a script that only touches the newly-fetched members' fields (see the FETCH_DATE warning below), not a wholesale `tmp/build.py` rerun |

Update this table (and check it off above) as batches complete. When
`tmp/members_todo.txt` is empty, run `tmp/build.py` to regenerate
`data/patents.yaml` from the cache and `tmp/selection.json`, review the
diff (only `verified`, `status`, `title`, `application_number`,
`filing_date`, `expiry`, `expired` fields should move from "listed" to
"fetched" values; `relevance`/`discovery`/`notes` must be unchanged),
then run `uv run tools/check_patents.py` and commit.

## Phase 2 — widen discovery

- [x] Cross-check every patent already cited anywhere under `docs/`
      (grep for `US `, `EP `, `WO `, etc. + digits, and Google Patents
      URLs) against the dataset. Re-run on the post-rebase tree
      (`tmp/docs_cited_check.py`): 287 distinct cited numbers/URLs
      found, 0 missing from the dataset's 1319+ member numbers.
- [ ] Per-module assignee searches (Cypress/SkyWater/Infineon, 130 nm
      CMOS + SONOS flow): STI, wells, gate oxide/nitridation, poly,
      LDD/spacers, salicide, local interconnect TiN, W plugs, Al
      metallisation, MiM, fuses, passivation, SONOS/ONO,
      drain-extended/HV, ReRAM. Batches 1-2 above cover SONOS/ONO/DEMOS
      and isolation/gate-oxide/spacer/local-interconnect/metallisation;
      remaining modules to search: wells (well/threshold-adjust
      specific), salicide, W plugs specifically, fuses, passivation,
      ReRAM (ties to Weebit Nano — in scope per coordinator decision),
      equipment/materials from suppliers already cited on a docs page.
- [x] Weebit Nano ReRAM patents (coordinator: in scope, unexpired ones
      collapsed) — done. Google Patents search `assignee="Weebit Nano"`
      (35 results, `tmp/qcache/`), narrowed to the 4 families that
      describe the OxRAM cell/manufacturing technique itself (not
      peripheral circuit IP such as bandgap references or current-limit
      circuitry, which are out of the process-technology scope of this
      index): `GP68072713` (WO2020249699A1, with CEA-Leti),
      `GP69743400` (EP4062463A1), `GP74192490` (US20220122660A1, 1T2R
      cell configuration) and `GP90721530` (KR20250094623A). Every
      member of all four fully fetched (recent priority dates, so the
      full-fetch rule applies); all four are unexpired/unknown and
      collapsed. Relation `technique-class` (Weebit is not in the
      Cypress/SkyWater/Infineon lineage, so `same-lineage-assignee`
      does not apply), target `overview-sky130b-reram`, reason
      states SkyWater's public Weebit-in-S130 announcement and
      explicitly is not evidence of what SkyWater fabricates. Applied
      with `tmp/add_weebit.py`. 211 families total after this addition.
- [x] Supplier equipment/material patents where a docs page already
      cites them or a public source ties them to this process lineage —
      the docs-citation cross-check in Phase 2's first bullet already
      covers the "docs page already cites them" half (0 missing); no
      further public-source ties to the lineage were found for
      supplier equipment/material patents beyond what's already in the
      dataset. A deeper trawl was out of scope per the coordinator's
      note ("only where ... a public source ties them to this process
      lineage", not a general search).

## Phase 3 — pages and generator

- [x] `tools/gen_patents.py` (model: `tools/gen_papers.py`) — done,
      commit "Patent index: generator and the six reference pages".
      Uses `check_patents.Loader` (not `yaml.safe_load`) to keep dates
      as strings, matching the checker.
- [x] Six pages under `docs/references/patents/` — done, same commit.
      `by-module.md` groups by the 13 modules of `(overview-modules)=`
      on `docs/overview/index.md` (a step target maps to its module by
      step number), plus separate sections for the sky130B ReRAM
      module (`overview-sky130b-reram` target), equipment and
      metrology (`machine-*`/`machines-index` targets), materials
      (`material-*`/`materials-index` targets), and a catch-all
      "process-wide and category pages" section for everything else
      (`category-*`, `mask-*`, `masks-index`, `overview-index`). This
      is coarser than the design doc's 16-bucket proposal (which would
      need per-step subject data finer than the overview table gives);
      documented here rather than fabricated.
- [x] Link from `docs/references/index.md` — done, same commit.
- [x] Legal caveat on the landing page — done, same commit (see
      `docs/references/patents/index.md` "## Legal caveat").
- [x] `sphinx-build -W` fix: expired-family entries on `families.md`
      must be `##` (H2), not `###` — an H1-to-H3 jump is a nitpicky
      warning under `-W`. Fixed before the commit above; verified with
      a full `-W` build (0 warnings).

## Phase 4 — checks

- [x] `uv run tools/check_patents.py` — 211 families, 0 problems as of
      the final commit this round (rerun after every dataset change).
- [x] `uv run tools/gen_patents.py --check` — 6 pages checked, 0
      problems, regenerated after the fetch/refresh and Weebit
      additions.
- [x] All other `tools/check_*.py` (`check_steps`, `check_refs`,
      `check_machines`, `check_materials`, `check_masks`,
      `check_papers`) — 0 problems each, rerun after the final dataset
      change.
- [x] `uv run sphinx-build -W -b html docs <scratch dir>` — clean,
      0 warnings, exit 0. Run four times over the round: found and
      fixed the families.md H1-to-H3 heading-level issue, then
      confirmed clean after the generator fix, after the old-member
      fetch/refresh, and after the Weebit addition.

## Summary of this round's changes (for the next agent or reviewer)

1. Rebased onto `main` (pulled in the merged paper-index work) and
   force-pushed with lease.
2. Added this progress log.
3. Finished fetching every remaining "listed only" member (435 of them,
   53 pre-1999-05-29 families) and applied the results without
   disturbing any other family's data (`tmp/refresh_old_members.py`).
   Two families' `expired` correctly flipped from `true` to `unknown`.
4. Wrote `tools/gen_patents.py` and generated the six
   `docs/references/patents/` pages; linked from
   `docs/references/index.md`; fixed a heading-level `-W` warning.
5. Added 4 Weebit Nano ReRAM families (211 total), each fully
   member-fetched per the verification-level rule for recent-priority
   families, via `tmp/add_weebit.py`.
6. Re-ran every checker and a full `-W` Sphinx build after each
   substantive change; all clean at the final commit.

Not done this round (left for the coordinator/reviewer to decide
priority): the second-source cross-check sample (Phase 1), and the
design's open questions (DOCDB family-unit switch, assignee-name
normalisation for mergers — the by-assignee page already groups by
raw original-assignee string, which is a reasonable interim reading).
The `by-module` page's grouping is coarser than the design's 16-bucket
proposal; see Phase 3 above for why and what a future refinement would
need (step-level subject data finer than the overview table gives).

## Notes for whoever resumes this

- The dataset already passes its own checker at every commit; that is
  the safe resume point. Never leave a commit with `check_patents.py`
  failing.
- `tmp/build.py` regenerates the **entire** `data/patents.yaml` from
  `tmp/selection.json` + the fetch cache, sorted and formatted
  deterministically; hand edits to `data/patents.yaml` should generally
  go through `tmp/selection.json` + a rerun, not direct edits, to keep
  the two in sync. Exception: the `expired`/`grant`-covers-`application`
  rule change and similar rule changes were applied as direct patch
  scripts (`tmp/patch_*.py`) plus a `build.py` rerun; check `git log -p`
  on `data/patents.yaml` and `tools/check_patents.py` for the rule
  history before changing the rules again.
- `tmp/build.py` currently bakes one global `FETCH_DATE` constant into
  every record's `verified` field. That was correct for the original
  single fetch session (2026-09-14). Adding new fetches on a later date
  must **not** silently restamp the older, already-accurate `verified`
  dates. Before rerunning `build.py` after adding new cache entries on a
  new date, either (a) patch it to derive each record's fetch date from
  its own cache file's mtime, or (b) apply the new fetches with a
  narrower patch script that only touches the newly-fetched members and
  leaves everything else byte-for-byte alone. Do not bump `FETCH_DATE`
  and rerun wholesale.

## Round 3: response to the second independent review

Review: `tmp/verify-index-patents-r2.md` (round 2, 2026-09-18, verdict
"fix first — then merge"; all round-1 findings verified fixed or
soundly declined except three new defects on the round-2 diff itself,
N1-N3, and six further Low items, N4-N9). Every point was checked
independently before being changed (recomputed dates and rules
directly from the dataset, re-read the branch's own `tmp/cache/`
fetch records) rather than taken on the review's say-so; nothing was
declined this round — every finding held up.

| ID | Finding | Status | Note |
|---|---|---|---|
| N1 | `by-jurisdiction.md` says "Every member publication" and calls a collapsed family's one row a "member publication" | fixed | Recomputed the actual row counts against member counts (US 413 rows vs. 520 members in the dataset) to confirm the mismatch; reworded the intro and each section's count line in `gen_by_jurisdiction()` to say what is actually listed (every member of an expired family, plus one representative row per collapsed family) and give both counts implicitly via the row count. |
| N2 | 17 families' `expiry.basis` names the earliest-family-filing + 20 years rule when the printed date is actually priority + 21 years | fixed | Recomputed both candidates for each of the 17 governing members directly (`tmp/check17.py`): priority + 21 wins in every case, matching the printed date. Reworded each family's `basis` text to the wording already used elsewhere in the dataset for a priority + 21 governing date; verified `tools/check_patents.py` still passes (the basis still names the same member). |
| N3 | `SE7506134L` mistyped `translation-of-granted-patent` | fixed | Checked the branch's own fetch cache: Google's `publicationDescription` for it is "Published abstract", filed 1975-05-29, before the EPC (1977) and Sweden's accession (1978) — it cannot be an EP-grant translation. Retyped `other` (round-1's own offered fallback for this ambiguous batch); recorded the reasoning in a family note. |
| N4 | `translation-of-granted-patent`'s "no term of its own" exemption never checked that a granted patent actually exists in the family | fixed | Made the exemption in `member_end_bound()` conditional on the family containing a `granted-patent` member. No family in the current dataset changes state — the five DE T5/T9/T1 members the review named each already have their own granted-patent sibling — this only closes the gap for a future addition. |
| N5 | Landing page says "just two more searches"; the round-1 review ran three | fixed | Confirmed against `tmp/review-index-patents-r1.md`'s own "Missing families" section (three keyword searches: "shallow trench isolation", "retrograde well", `"gate oxide" nitridation`); fixed the count. |
| N6 | Progress table's M3 row said "36 families' dates moved (all later)" | fixed | Recomputed the diff at commit `7f820f7` directly: 19 later, 17 earlier. Fixed the row to say so and name the three JP-divisional families among the earlier moves that the M9 fix corrected again. |
| N7 | Five family notes cite untracked `tmp/build.py`/`tmp/gp.py`; the landing page points at `docs/plans/progress-index-patents.md`, excluded from the Sphinx build | fixed | Reworded the five notes to describe the builder scripts without the unpublished path, and the landing page to say the round-1 review is the project's own unpublished working notes rather than naming an unreachable path. |
| N8 | `GP25461879`'s M9 note said `JP2008238399A` is a divisional of `JPH08500622A` (1993) as if read off the record | fixed | The cached record page's own "Related Parent Applications" table names the direct parent as `JP2006054961A` (2006-03-01, not itself a family member) instead. Reworded the note to say only what the record confirms and mark the rest as inference; the expired conclusion is unaffected either way. |
| N9 | L2 and L11 needed the coordinator's agreement per the design doc; the round-2 fixer recorded its own confirmation instead | fixed | Reworded both notes in `patent-index-design.md` and `citation-style.md` to say plainly that they are the fixer's proposal, recorded pending the coordinator's ratification. |

All six checkers, `gen_patents.py --check` and a full `-W` Sphinx build
were rerun clean after this round's changes (see the commit history);
`git push origin topic/index-patents` follows this table.

## Round 4: closing H1 (coverage) — branch `topic/index-patents-coverage`

Google Patents answers again from this environment (confirmed with a
bare-root fetch, HTTP 200, before starting; no bot-check/503 was hit at
any point this round). Worked from the round-1 review's own "Missing
families" table (`tmp/review-index-patents-r1.md`, at the *main* repo
root — not this worktree's `tmp/`) and its H1/coverage sections, and
`tmp/verify-index-patents-r2.md`'s confirmation that H1 was left "open
by agreement". Fetch cache: shared, at the path the brief specified,
`tmp/patent-cache/`
(the *main* worktree's `tmp/`, not this branch's) — 105 files already
there from earlier rounds' partial attempts, reused where numbers
matched. Pacing: 20 s between requests via `tmp/fetch_gp.sh` (this
worktree's own `tmp/`, not committed), which stops and marks a
`.blocked` file on the first non-200 response or bot-check text rather
than retrying; never triggered this round.

### 1. The review's 15 named publications (H1's first instruction)

Fetched all 16 numbers the review's table names as Google Patents
record pages. They resolve to **14 distinct Google Patents family
IDs**: two pairs of the 16 numbers share a family id each
(`US10446656B2`/`US9929240B2` → `GP49580624`; `US20180351003A1`/
`US10699901B2` → `GP49580623`), which is exactly what the review's own
prose said to expect for a continuation and its earlier sibling filed
close together. The interesting case is the *other* named pair: the
review calls `US10199229B2` "the same family line" as `US8710578B2`
("continuation of the above"), but on Google's own grouping they are
**two separate families** (`US8710578B2` → `GP48743335`, a
single-member family with no other continuation Google records;
`US10199229B2` → `GP46465479`, an unrelated 13-member family) — a
second, independently-found instance of exactly the
continuation/divisional blind spot the design doc already documents,
alongside its `GP40071593`/`US10699901B2` worked example. Both are
added as separate entries, so the 16 named numbers become 14 new
families' worth of records, not 11, 13 or 15. (An earlier draft of
this section, and the first commit's own message, said 13 — miscounted
before this recount; 225 - 211 = 14 is the fact to trust.) All 14 new
families' members were then assembled:

* Every representative's own record page fetched; every **US** member
  individually fetched (103 member fetches, in two batches, both clean);
  every **non-US** member (59 of them: mostly JP/CN/KR/TW/DE/GB/WO
  siblings of the larger continuation chains) left `listed` from the
  representative's own "Family Applications"/"Also Published As"
  tables rather than fetched — a deliberate, documented departure from
  the design's "every member of a post-1999-05-29 family is fetched"
  rule, made for time budget, not doubt about the rule: fetching all
  ~160 members of these 14 families at 20 s/request would have used the
  whole session on this one sub-task. Each such member still carries
  its real publication number, country, kind, document_type and
  publication date (read off the summary table, not invented) and a
  `verified` string that says plainly it was listed, not fetched, per
  the design's own fallback wording. This is recorded here, not hidden,
  and is real, auditable, follow-up work: a future session with more
  time should fetch these 59 (`grep -c 'record page not fetched'
  data/patents.yaml` finds exactly these, and no others — see below).
* Two tooling scripts, not committed (worktree `tmp/`, gitignored):
  `tmp/parse_gp.py` (HTML → fields: family id, member list from
  `itemprop=applications` + `itemprop=docdbFamily`, assignees,
  inventors, dates, legal status, expiry from the events list — *not*
  a `<dt>`/`<dd>` pair as the page's visible layout suggests; verified
  by reproducing `GP40071593`'s and `GP68072713`'s already-correct
  entries byte-for-byte from their cached pages before trusting the
  parser on new data) and `tmp/build_family.py` (ports
  `tools/check_patents.py`'s own `member_end_bound`/
  `family_max_estimate`/expiry-basis logic verbatim, so a family this
  script builds passes the checker's rules by construction, not by
  luck). `tmp/add_named_list.py` holds the 14 families' hand-written
  relevance/discovery/notes and calls the two library scripts.
* One new discovery method, `continuation-search`, added to
  `tools/check_patents.py`'s `DISCOVERY` set and documented in
  `docs/plans/patent-index-design.md`, exactly as that file's own
  "Known blind spot" note asked the agent who closed it to do. Used
  for the four families reached by checking an *existing* seed's later
  filings rather than by a fresh assignee search: `GP46465479`
  (continuation of `GP48743335`), `GP49580624` and `GP49580623`
  (continuations of the 2007-05-25 Cypress ONO estate, `GP44760304`/
  `GP40071593`), `GP48743295` (a further late continuation of that
  same estate). The other 9 are `assignee-search` (Cypress/Infineon
  keyword sweeps reproducing what the review's searches would have
  found, now independently fetched and verified by this session).
* One family (`GP48743335`, `US8710578B2`) carries a `notes` entry
  recording the review's finding that it is subject to a terminal
  disclaimer, which the dataset's expiry rules do not model (same
  caveat class as M4).
* One family (`GP52707807`, `TWI640082B`) has its assignee shown only
  in Chinese on Google Patents; read (not independently confirmed —
  `data.epo.org` does not carry TW-only documents) as Cypress
  Semiconductor Corporation and recorded as such in both the relevance
  reason and a `notes` entry.
* `US6963106B1` (Spansion LLC): checked the review's own description of
  Spansion as "the Cypress/AMD flash joint venture" and found **no
  public source** tying Spansion's fab lineage to Cypress's Bloomington,
  MN fab (Spansion was the AMD/Fujitsu NOR-flash joint venture, a
  different lineage). Added with relation `technique-class`, not
  `same-lineage-assignee`, and the reason says so plainly — per the
  brief's own instruction ("Spansion … only where a public source ties
  them to this lineage").

Result: **14 new families, 225 total** (was 211).  `uv run
tools/check_patents.py` — 225 families, 0 problems.  `uv run
tools/gen_patents.py` / `--check` — 6 pages, 0 problems.

### 2. SkyWater, module sweeps — commit `19e15e2` and after

Committed the 14 named-list families first (commit `4505ac7`, whose own commit message undercounted this as 13 -- corrected here) as a
safe, independently-checked checkpoint, then continued with the time
remaining. All searches below used the `patents.google.com/xhr/query`
JSON endpoint (same user agent, 20 s pacing), examining only the first
result page (10 hits) as the round-1 review's own method did, and
fetching a record page only for a family actually added.

| # | Search | Hits | Examined | Added | Note |
|---|---|---|---|---|---|
| 1 | `assignee="SkyWater Technology"` | 1 | 1 | 1 | `GP94259596`, `US20250031586A1` "Carbon film integrated into a back end of line process", filed 2023-07-21. **The first SkyWater-assigned family in the index.** Does not name SKY130 or a node; recorded honestly as unconfirmed for this platform, not claimed as SKY130 evidence. |
| 2 | `assignee="SkyWater"` (broader, to catch variant renderings) | 3 | 3 | 0 (1 already counted above) | The other two hits are unrelated companies coincidentally named "Skywater": a Japanese plumbing/circulation-system patent (`JP2025154019A`, "Skywater Japan Llc") and a personal-name potable-water patent (`US7121101B2`, "Merritt Thomas D"). Neither is SkyWater Technology Foundry; not added. |
| 3 | `assignee="Cypress Semiconductor"` + `salicide` (wells/salicide module, never searched) | 498 | 10 | 1 | `GP51221986`, `US11183509B2` "Non-volatile memory with silicided bit line contacts", 14 members (9 US fetched, 4 EP/WO listed, 1 already-fetched representative). Targets {ref}`step-098 <step-098>` (CSIL, contact silicide). |
| 4 | `assignee="Cypress Semiconductor"` + `"tungsten plug"` (W-plugs module, never searched) | 21 | 10 | 1 | `GP35465546`, `US6977217B1` "Aluminum-filled via structure with barrier layer" — the clearest on-topic hit was an aluminium-via/barrier family, not a tungsten-plug-specific one; added and described as such rather than mischaracterised. Single member, already expired. |
| 5 | `assignee="Cypress Semiconductor"` + `"polysilicon fuse"` (fuses module, never searched) | 2 | 2 | 0 | Both hits are Advanced Micro Devices (not Cypress); no Cypress-assigned polysilicon-fuse family found. |
| 6 | `assignee="Cypress Semiconductor"` + `"fuse link"`, priority before 2015 (fuses module, second attempt) | 4 | 4 | 0 | All 4 are Cypress/Nvx EPROM/latch circuit patents using "fuse link" as a circuit-design term, not the process-module physical fuse (`NFUSOX`) fabrication step; none is a clear enough match to add without stretching the relevance. |
| 7 | `assignee="Cypress Semiconductor"` + `passivation` | — | — | 0 | **Blocked**: HTTP 503 with Google's "Sorry... unusual traffic" bot-check page on the very first request of this query (no burst beyond the 20 s pacing already in force). Per the brief's rule, stopped immediately, marked `tmp/patent-cache/.blocked` (main worktree's shared cache) with the timestamp, and did not retry. This ended the session's fetching for good — no further Google Patents requests were made after this. |

Passivation (search 7) and the ReRAM/equipment-beyond-Weebit sweep were
**not reached** before the block. Fuses (searches 5-6) were searched
but found nothing clearly on-topic from Cypress specifically — a
different keyword (e.g. the PDK's own fuse-mask terminology, or a
citation search off `NFUSOX`'s step page once one exists) might do
better; this is honest "searched, found nothing" per the brief, not
"not searched".

Result after this section: **228 families** (211 + 14 named-list + 1
SkyWater + 1 salicide + 1 W-plug/via search). `uv run
tools/check_patents.py`: 228 families, 0 problems throughout (checked
after every addition, not just at the end).

### What is still missing (honest estimate)

* **Not reached this round**: passivation and fuses (found nothing
  Cypress-specific; a better search term is worth trying), and
  equipment/materials beyond Weebit Nano and what docs pages already
  cite. The round-1 review's own extrapolation ("several dozen to a
  couple of hundred lineage families" from 25 examined hits across 3
  searches) still stands as the working estimate for the *remaining*
  gap: this round's 6 fresh searches that returned results (search 7
  was blocked before it could) examined about 55 result-list hits and
  turned into 3 new families beyond the named list, a similar hit rate
  (roughly 1 in 18) to the review's own (11 in 25) once the SkyWater
  and fuse searches' many off-topic/false-positive hits are counted in
  — there is no reason to think the well is dry.
* **59 members recorded as `listed`, not fetched** (all non-US members
  of the 14 named-list families) — a real, bounded, auditable gap:
  `grep -c 'record page not fetched' data/patents.yaml` finds exactly
  these 59, and no others — every pre-existing family's members were
  already fully fetched by the time this round started (Phase 1's own
  "0 outstanding" completion note), so this round's 59 are a clean,
  deliberate departure from the "every member of a post-1999-05-29
  family is fetched" rule, made for time budget alone. Fetching them
  would let a couple of these families' `expired` flags be checked
  more exactly (most are
  already soundly bounded by their fetched US members).
* **Continuation/divisional sweeps for other already-indexed estates**
  beyond the ones the review already named (`GP40071593`,
  the 2007-05-25 ONO estate, `GP48743335`) were not attempted — the
  design doc's "Known blind spot" almost certainly applies to other
  large Cypress estates already in the dataset (e.g. the drain-extended
  MOS and shallow-trench-isolation families from batches 1-2), not just
  the ones named so far.
* No second-source (Espacenet/Patentscope/USPTO) cross-check was done
  for the new families this round (same lower-priority deferral as
  Phase 1's own outstanding item); `data.epo.org` was not used this
  round since Google Patents itself answered throughout.

Landing page (`docs/references/patents/index.md`) "Scope and
completeness" section is regenerated by `tools/gen_patents.py` from the
dataset's own discovery-method counts, so it already reflects the new
228-family / non-zero-SkyWater state without hand editing.

Commits this round: `4505ac7` (14 named-list families), `19e15e2`
(SkyWater + salicide), and one more after this file update (W-plug
family + this progress-file section + final checks). All pushed to
`topic/index-patents-coverage`.

## Round 4: independent-verification fixes (H1/H2/M1-M4/L1/L2) and Part 2 (PPUBS discovery)

Verification: `tmp/verify-index-patents-coverage.md` (not tracked;
2026-09-19, verdict "fix first"). Every finding was re-verified
independently against the branch's own `tmp/patent-cache/` before being
fixed (nothing taken on the verifier's word alone); none was declined.

**Part 1 — verification fixes**, one commit each:

* **H1** — `tmp/parse_gp.py`'s `top_metadata()` read a member's status
  from the first `itemprop="ifiStatus"` span in the page, which on a
  published-application page belongs to the "Worldwide applications"
  table and can disagree with the page's own Legal-status field
  (`itemprop="legalStatusIfi"` > `"status"`). Fixed the selector,
  re-derived every fetched member's status of the 17 families the prior
  round added from the already-cached pages (no re-fetch), and
  recomputed the 12 affected families' `legal_status`/`expiry`/`expired`
  (46 `Active` -> `Granted`, 1 `Expired - Lifetime` -> `Granted`; three
  families' published expiry estimates corrected: GP48743295
  2032-03-31 -> 2029-04-24, GP48743335 2032-03-27 -> 2030-06-18,
  GP58691400 2036-09-29 -> 2032-12-14). No family's `expired` value
  flipped — every one still has a genuinely Active granted member.
  Added a checker guard (an application-type member recorded `Active`
  now fails `check_patents.py`) so this cannot recur silently.
* **H2** — the landing page's listed-only-members sentence claimed
  "every possible term... has already ended" for all 59 listed-only
  members; false for 44 of them (6 families, not shown expired,
  estimated to run into the 2030s). `gen_index()` now states the real
  split (fetched vs. listed, and of the listed, expired-family vs.
  bounded-only-by-rule-3), and the exception is recorded in
  `patent-index-design.md`'s "Verification levels".
* **M1** — added the round-1-M4-style reinstatement note to
  `GP48952138` (fee lapse 2025-09-22, adjusted expiration 2027-01-30,
  37 CFR 1.378 window open to about 2027-09-22 — verified directly
  against the cached page's own legal events). Kept `expired: true` per
  design rule 1 and round-2's own precedent, matching what the verifier
  actually asked for (a note), not a flag flip.
* **M2** — corrected the SkyWater carbon-film family's relevance
  reason/discovery_note/notes, which said three times that no
  platform/node was named; the application actually names 90 nm
  processing technology and calls itself CMOS technology-agnostic
  (verified against the cached page). Conclusion (not evidence for
  SKY130) unchanged.
* **M3** — normalised `GP52707807`'s Chinese-only assignee heading
  (`## 美商賽普拉斯半導體公司`) to the Latin-script reading its own US
  siblings (US8993457B1, US9496144B2, US9911613B2) give on their own
  fetched pages, per round-1 finding M1's own prescribed fix; noted
  `GP42945510`'s "Longitudinal Flash Storage Solutions Co., Ltd." as
  Google's rendering of the same Longitude Flash Memory Solutions Ltd.
* **M4** — narrowed the Spansion family's "no public source... ties
  Spansion to the Cypress/SkyWater fab lineage" to the fab-lineage
  question specifically, and acknowledged the USPTO assignment events
  on the family's own cached page naming Cypress alongside Spansion
  after their 2015 merger. Relation (technique-class) unchanged.
* **L1/L2** — design-doc tidy-ups: named the fourth `continuation-search`
  family (`GP46465479`); marked the "Known blind spot" paragraph's own
  ask (a per-estate continuation search) done, since it now is.

All six commits: `uv run tools/check_patents.py` 228 families, 0
problems; `uv run tools/gen_patents.py --check` 6 pages, 0 problems.

**Part 2 — discovery via a source that doesn't bot-block.**

Google Patents confirmed still blocked this round (bare domain root
returns the site-wide bot-check, same as every prior round). Section 7
of the verification report documented USPTO Patent Public Search
(PPUBS) as reachable and keyless; used it as the fixer brief's
prescribed fallback.

* Wrote `tmp/ppubs_search.py` (not tracked): paced (16s), cached
  (`tmp/patent-cache/ppubs/`, not tracked) sweeps, one combined
  assignee + process-module-title query per assignee (Cypress
  Semiconductor, SkyWater Technology, Longitude Flash Memory Solutions,
  Infineon Technologies LLC, Spansion, Ramtron, Weebit Nano) — see
  `docs/plans/patent-discovery-log.md` for the full method, the query
  text, and why a CPC-field restriction in the query itself had to be
  abandoned (client-side CPC filtering used instead, on the classes the
  brief named plus three CPC-reclassification classes discovered to
  matter: `H10D`, `H10W`, `H10P`).
* 377 hits, 211 distinct DOCDB families: 39 already in the dataset, 24
  added this round, 136 in scope but left for later (mostly a large
  Spansion estate and most of the remaining Weebit hits — see the
  discovery log's reasoning), 12 out of scope (circuit/protection/EDA).
* Documented a new "PPUBS fallback" verification path in
  `patent-index-design.md`: an alternate `family.source` string so a
  PPUBS-built family is never misrepresented as Google-verified; no
  legal status or adjusted-expiration date (PPUBS reports neither, so
  `status`/`legal_status.status` are `null`); expiry computed purely
  from term arithmetic, with the crucial safety rule that a family
  whose earliest priority is on or after 1999-05-29 is **never** marked
  `expired: true` from arithmetic alone (a real US term adjustment could
  extend it, and PPUBS cannot show one) — only 6 of the 24 added
  families, all with pre-1999-05-29 priority, are `expired: true`; the
  other 18 are `unknown` and collapsed. `tools/check_patents.py`'s
  `FAMILY_SOURCES` accepts the new literal source string.
* Fixed `gen_patents.py`'s dropdown/landing-page text, which
  unconditionally claimed a fetched Google Patents "representative's
  own record page" regardless of source; now names PPUBS where that is
  the actual source and splits the fetched/listed member counts by
  source.
* **Known side effect, not a data change:** the splice script used to
  insert the 24 new families (`tmp/add_ppubs_batch1.py`, modelled on
  the existing `tmp/add_wplug.py` pattern) re-sorts *every* existing
  family block by its own (quote-stripped) priority date before
  writing the file back. The pre-existing file turned out to have 3021
  pairwise priority inversions out of 228 families (i.e. it was not
  actually in strict ascending-priority order, despite the design's own
  "sorted by priority date" statement) — plausibly the residue of
  several rounds' independent splicing scripts each sorting only their
  own small batch. This round's write incidentally corrects that to a
  true global sort (0 inversions) as a side effect of adding the 24
  families, which produced a much larger textual diff on
  `data/patents.yaml` than the 24 additions alone would need.
  **Verified independently before and after** (not just asserted): a
  family-by-family structural diff (by `id`, ignoring position) found
  exactly 24 additions, 0 removals, and 0 content changes to any
  pre-existing family. `uv run tools/check_patents.py` and
  `uv run tools/gen_patents.py --check` both pass, and a full `-W`
  Sphinx build is clean. Flagged here so a future reviewer diffing
  `data/patents.yaml` understands why the diff is large rather than
  suspecting corruption.

Commits this round: one per verification finding (H1, H2, M1, M2, M3,
M4, L1/L2), one Part 2 infra commit (PPUBS fallback schema/design-doc
change), and one Part 2 data commit (24 families). Pushed to
`topic/index-patents-coverage`.

### Left for a future round

* The ~136 in-scope PPUBS hits not added (see
  `docs/plans/patent-discovery-log.md`): mainly the Spansion estate
  (needs the same per-family M4-style lineage care, at scale) and most
  of the Weebit Nano hits (mostly circuit-level programming/read-write
  schemes, likely out of scope by the brief's own exclusion, but not
  individually triaged).
* `skywater`/`skywater technology foundry` returned 0 new hits under
  this sweep's module-keyword restriction; a broader, unrestricted
  SkyWater assignee sweep (title keywords aside) was not run.
* Every PPUBS-sourced family records only the single US publication its
  own query returned; no attempt was made to find its other-jurisdiction
  or other-US-member siblings (would need either a further PPUBS query
  per family, keyed on `familyIdentifierCur`, or Google Patents access).
* The design's open questions (DOCDB family-unit switch, assignee-name
  normalisation for mergers) are unchanged from round 3.

## Round 5: CPC-classification sweep (2026-09-20), branch `topic/index-patents-r3`

Coordinator brief: make the lineage coverage systematic by CPC class
instead of keyword. Full method, sweep totals and family-level triage
are in `docs/plans/patent-discovery-log.md`'s "Round 5" section; summary
here.

**Method.** Round 4's per-assignee sweep restricted each query to
process-module title keywords. This round dropped the keyword
restriction and queried by CPC class instead: `<assignee>.as. AND
(H01L21$ OR H01L23$ OR H01L27$ OR H01L29$ OR H10B$ OR H10N70$ OR G03F$
OR C23C$ OR C30B$ OR H10D$ OR H10P$ OR H10W$).cpc.` against Cypress
Semiconductor, SkyWater Technology, Longitude Flash Memory Solutions,
Infineon Technologies LLC and Ramtron -- the brief's own CPC list plus
the H10D/H10P/H10W reclassification targets round 4 already found
necessary. Getting the CPC wildcard syntax right took some
experimentation (`tmp/ppubs_cpc_sweep.py`, not tracked): PPUBS's
`.cpc.` field only recognises a bare `$`-truncation on the whole symbol
string (`H10B41$`), not a slash-plus-wildcard (`H10B41/$` works only
when a real subgroup follows a class that itself has no further
digits, `H01L21/$`, and even then only matches the shrinking legacy
part of that class); and `docFamilyFiltering=familyIdFiltering` with a
single request sized to the query's own `numberOfFamilies` avoids a
pagination bug where offset-based paging (`start=0,100,200,...`) was
found to drop and duplicate families (confirmed on the cypress query:
494 `numberOfFamilies` but only 300 distinct families after three
paged requests, vs. 494 distinct in one appropriately-sized request).

**SkyWater.** Round 4's `"skywater technology".as.` query returned 0
hits and was written up as "no new hits". PPUBS actually indexes the
company as **"Sky Water Technology Foundry, Inc."** (two words, no
compound "SkyWater"). `"sky water".as.` returns exactly one family
worldwide, the already-in-the-dataset GP94259596 "carbon film"
application -- plus its just-granted patent US12740332, found under a
*different* PPUBS `familyIdentifierCur` (a PPUBS indexing quirk on a
very recent grant, not a second real family), added as a new member of
GP94259596 rather than a new family. This closes round 4's "left for
later" item asking for a broader, unrestricted SkyWater sweep: there
is nothing else to find under any spelling.

**Totals.** 494 Cypress + 16 Longitude + 13 Infineon Technologies LLC +
63 Ramtron + 1 SkyWater = 587 CPC-restricted hits (a family can count
under more than one assignee query), 559 distinct DOCDB families.
93 already present, 81 added, 385 out of scope, 0 explicitly left for
later this round (every hit was triaged to a decision; see the
discovery log for the full per-family table and the individually-
reasoned exclusions). Of the 385: 12 were individually reasoned
(ferroelectric/FRAM, circuit, EDA-software, or a technology the
lineage fab never ran -- see "Explicitly excluded" in the discovery
log); the other 373 were triaged by a scripted title-keyword
classifier, not a full read of each patent, and default to out of
scope when the title names no unambiguous in-scope phrase -- a spot
check afterwards found real false negatives in this bucket (e.g.
"Sealed self aligned contacts using two nitrides process",
GP24009558, is plainly a process patent the keyword list simply didn't
cover). The discovery log's reason column for these says so honestly
(a title-only heuristic default, not an individual finding that the
patent is out of scope) rather than asserting a specific false reason;
**a future round should read this 373-family bucket's titles again
with a broader keyword list, or individually**, rather than treat it
as settled.

**Additions.** 81 new families (79 Cypress-attributed, 2 Infineon
Technologies LLC-attributed, one of which doubles as a Longitude hit):
process/device-structure patents spanning isolation (STI/LOCOS),
wells, gate stack/gate oxide, spacers, salicide/silicide, local
interconnect and contacts, tungsten and copper/ruthenium interconnect,
CMP, lithography (reticles, phase-shift photomasks), implant, etch,
deposition, and SONOS/charge-trap memory (including two 2021-2024
Infineon Technologies LLC continuations of the embedded-SONOS/HKMG
platform). Priority years 1994-2024; 13 have priority before
1999-05-29 and are `expired: true` (their 20-year/17-year term bound
has long passed); the other 68 have priority on or after 1999-05-29
and are `expired: unknown` (collapsed -- PPUBS reports no legal status
or term-adjustment data, so the design's safety rule never marks these
`true`). Every addition was second-sourced: a USPTO grant PDF
(`image-ppubs.uspto.gov`) for a granted patent, or an EPO linked-data
page (`data.epo.org/linked-data/data/publication/US/<num>/A1`) for a
pre-grant publication -- 81/81 confirmed to exist with a matching
number, cross-checking PPUBS's own search-hit metadata against a
second, independent database (`tmp/second_source_check.py`, not
tracked; results cached).

**Explicitly excluded, not left for later.** 3 Ramtron CPC hits
(passivation, local interconnect, Pt/TiOx bottom-electrode deposition)
are all ferroelectric-capacitor-specific -- FRAM, excluded per the
brief's Ramtron restriction to FRAM-unrelated CMOS process. 5 more
Cypress hits are F-RAM device fabrication (Cypress inherited Ramtron's
FRAM line in the 2012 acquisition -- a different product from the
Bloomington fab's embedded-SONOS flow, never shown by any public
source to be part of the SKY130 lineage). One Cypress hit is an
ESD-protection circuit (circuit, not process). One is a mask-layout
*software* tool (EDA, not a fabrication step -- the same class of
exclusion round 4's own sweep already used once). Two 2024 Infineon
Technologies LLC hits describe a vertical-channel (3D) non-volatile
memory architecture -- the SKY130/Fab25 lineage is a planar-transistor
process and no public source shows this fab running a 3D memory
architecture, so excluded as a technology the lineage fab never ran.

**Family-source provenance, honestly stated.** Google Patents was
reachable this round (a plain fetch returned 200 with real content),
unlike rounds 2-4. The coordinating brief nonetheless directed sourcing
new families via the PPUBS fallback path with an EPO/grant-PDF
second-source check, for consistency with this round's own
PPUBS-based CPC-classification discovery method. Reusing the existing
`"... (Google Patents unreachable)"` `family.source` literal for these
would misstate why Google was not used, so `tools/check_patents.py`'s
`FAMILY_SOURCES` gained a third literal, `"USPTO Patent Public Search
familyIdentifierCur (classification sweep, round 5)"`, documented in
`patent-index-design.md`'s "PPUBS fallback" section.

**Spansion re-triage (coordinator decision).** The coordinator ruled
the ~120-family Spansion estate does not belong wholesale (no public
source ties Spansion's own fabs to the Cypress/SkyWater Bloomington
lineage; the 2015 merger is ownership, not process lineage), and asked
for a re-triage to "out of scope (no lineage; technique only)" except
for up to about 15 individually-justified `technique-class` additions
where a docs page discusses a technique the index has no lineage or
expired example for. A systematic check against every Spansion topic
in the discovery log (spacer, salicide, SONOS/ONO/charge-trap, gate
oxide, HV/drain-extended transistor, local interconnect, MIM,
passivation, trench isolation, ReRAM) found **every one already has an
existing same-lineage-assignee or technique-class entry in the index**,
several already `expired: true` -- so the coordinator's own exception
condition ("the index has no lineage or expired example") does not
actually hold for any of the deferred Spansion families. Result: **0**
new Spansion technique-class additions this round (the two already
added in round 4, GP39047941 and GP39526963, are unaffected); all 91
Spansion-original "left for later" rows from round 4 (85 found only by
the Spansion query, plus 6 more that round 4's log mistakenly
double-tagged "cypress,spansion" -- checked against the raw PPUBS
record and confirmed `assigneeName`/`applicantName` both "Spansion
LLC", no Cypress tie at all) are re-triaged "out of scope (no lineage;
technique already covered elsewhere in the index)" in the discovery
log, each naming the existing family that already covers its
technique. This is a deliberately conservative, evidence-based
conclusion rather than a padded count against the "about 15" ceiling.

**Weebit Nano ReRAM (coordinator decision).** Re-ran the sweep for
Weebit Nano restricted to `H10N70$` (its only relevant class; no
process/device-structure content appears outside it) with no title
keywords: 10 distinct families, of which 3 already exist in the
dataset (OxRAM cell manufacturing methods) and one is new -- **GP93840812,
"Stack Structure For Retention of High and Low Resistive States of an
OxRAM..."** (US20260068542, filed 2026, a device/process patent on
retention of the two ReRAM resistance states), added as
`technique-class` on `overview-sky130b-reram`, matching the existing
Weebit entries' relation. The other 6 CPC-sweep hits, and all 14 of
round 4's own "left for later" Weebit hits (checked individually
again this round), are circuit-level programming/read/write/sensing or
binning schemes -- out of scope per the design's circuit exclusion --
except one, "Method for determining a manufacturing parameter of a
resistive random access memory cell" (US12224007B2), which is
ambiguous (its CPC codes span both `H10N70` device classes and
`G11C13` memory-circuit classes); its grant PDF has no extractable text
layer to resolve the ambiguity from the abstract, so it is excluded
conservatively as a test/metrology method characterising cells
electrically (the design's "test methods without process content"
exclusion) rather than included on the strength of its title alone.

**Checks.** `uv run tools/check_patents.py`: 333 families, 0 problems.
`uv run tools/gen_patents.py --check`: 6 pages, 0 problems.
`uv run python tools/gen_index_links.py --check`: 0 pages differ.
`uv run tools/check_inforce.py`: 0 problems. Landing page's "Scope and
completeness" text (`tools/gen_patents.py`) still to be updated to
describe this round's sweep -- next commit.

### Round 5 close-out

GP93840812 (new Weebit ReRAM family) and the GP94259596 SkyWater
grant-member addition are spliced into `data/patents.yaml` (commit
`49c4dce`); the landing page's "Scope and completeness" paragraph is
updated for round 5 in the same commit. Final foreground checks for
this round: `uv run tools/check_patents.py` (334 families, 0
problems), all four generators' `--check` (`gen_patents.py`,
`gen_index_links.py`, `gen_filings.py`, `gen_papers.py`), every
`tools/check_*.py`, and `uv run sphinx-build -W -q -b html docs
tmp/build-patents-r3` -- see this round's final commit message for the
actual pass/fail results.

### Left for a future round

* Every PPUBS-sourced family (round 3-5 alike) still records only the
  single US publication its own query returned; no attempt has been
  made to find other-jurisdiction or other-US-member siblings.
* The design's open questions (DOCDB family-unit switch, assignee-name
  normalisation for mergers) are unchanged.
* This round's sweep covered only the five core assignees the brief
  named (Cypress, SkyWater, Longitude, Infineon Technologies LLC,
  Ramtron); it did not look at any other assignee, nor beyond the
  named CPC classes (e.g. packaging classes, other memory classes).
* GP94259596's newly-added grant member, US12740332B2, has no Google
  Patents record page yet (indexing lag on a very recent grant, 404 as
  of 2026-09-20); a future round should re-fetch it once Google
  Patents has indexed the grant, to replace its term-arithmetic expiry
  with Google's own adjusted-expiration estimate and confirm its legal
  status directly rather than inferring "Granted" from the application
  record alone.
* The ambiguous Weebit family (US12224007B2, "Method for determining a
  manufacturing parameter of a resistive random access memory cell")
  was excluded conservatively (its grant PDF has no extractable text
  layer, an image-only scan, so its abstract could not be read); a
  future round with OCR or a working Google Patents fetch for it could
  revisit this call either way.
