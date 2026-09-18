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
- [ ] Fetching the remaining only-listed members of 53 pre-1999-05-29
      families (435 members) for completeness, even though the design's
      verification-level rule does not require it once a family is
      already bounded expired. In progress this round; batch status
      below.
- [ ] Second-source cross-check (Patentscope/Espacenet/USPTO) for a
      sample of members, recording disagreements in `notes` rather than
      silently choosing one source — not started.

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

- [ ] Cross-check every patent already cited anywhere under `docs/`
      (grep for `US `, `EP `, `WO ` + digits and Google Patents URLs)
      against the dataset; add any missing family. Not yet re-verified
      after the paper/filings rebase pulled in new pages — redo the grep
      on the post-rebase tree.
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
- [ ] Weebit Nano ReRAM patents (coordinator: in scope, unexpired ones
      collapsed) — not yet searched.
- [ ] Supplier equipment/material patents where a docs page already
      cites them or a public source ties them to this process lineage —
      not yet searched (distinct from a general supplier-patent trawl,
      which is out of scope).

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

- [x] `uv run tools/check_patents.py` — 207 families, 0 problems
      (rerun after every dataset change).
- [x] `uv run tools/gen_patents.py --check` — 6 pages checked, 0
      problems.
- [x] All other `tools/check_*.py` (`check_steps`, `check_refs`,
      `check_machines`, `check_materials`, `check_masks`,
      `check_papers`) — 0 problems each.
- [x] `uv run sphinx-build -W -b html docs <scratch dir>` — clean,
      0 warnings, exit 0 (run twice: once found the H1-to-H3 issue
      above, once confirmed clean after the fix).

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
