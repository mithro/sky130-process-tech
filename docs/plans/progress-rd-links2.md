# Progress: rd-links2 (R-WAYBACK second check for `--include-generated`)

Task: docs/plans/link-check-2026-09b.md section "(c) `--include-generated`" —
four tokens dead on their first check (2026-09-20) needed a second check
≥ 24 h later before R-WAYBACK applies.

## Done

* Re-ran `uv run tools/check_links.py --include-generated` to completion
  (chunked with `--time-budget`, foreground; cache seeded from an orphaned
  worktree's hand-written-page cache where available, otherwise fresh),
  covering the full 2540-token corpus (hand-written + generated). Ran
  `--reclassify` once (310 entries changed — the IOP/perfdrive fix etc. had
  never been applied to the seed cache). Ran the soft-404 top-up to
  completion for every non-DOI `ok`/`redirected-permanently` token
  (previously skipped on generated pages in report B).
* All four original first-check-dead tokens re-verified:
  * `doi:10.5281/zenodo.20032068`, `doi:10.5281/zenodo.20950316` — still
    dead (HTTP 410 both). Checked Wayback availability API + CDX for both
    `zenodo.org/record(s)/<id>` forms (empty / non-200 only) and
    `archive.ph/newest/` (HTTP 429, one try, common rule 9). **No snapshot
    anywhere** → rule 11 applied in `data/papers-excluded.yaml`: removed the
    verbatim quotation from each `reason`, paraphrased, added a dated
    "no longer retrievable ... evidence weak" note. No `archive_url` (none
    found, and these are DOI records — R-WAYBACK step 5 forbids an archive
    form for a DOI anyway).
  * `https://www.osti.gov/servlets/purl/3363571` (free copy of
    `paper-beall-2026a` in `data/papers.yaml`) — still dead (timeout).
    Same Wayback/CDX/archive.ph checks, no snapshot. Rule 11 applied: added
    `dead_since: '2026-09-25'` to the `free_full_text` entry (no
    `archive_url`); the paper's own fabrication quote rests on the
    still-live arXiv copy, not OSTI, so nothing to remove there.
  * The `web.archive.org/.../ny20006439x1_def14a.htm` capture — recovered,
    now `ok` (200). Confirms report B's "intermittent" read; no action.
* Extended `tools/check_papers.py`'s `free_full_text` schema: a link may now
  carry `dead_since` alone (rule 11, no snapshot) or
  `archive_url`/`archive_date`/`dead_since` together (verified snapshot).
  Added `--selftest` (check_papers.py had none before) covering both new
  shapes and their rejections (8 cases). `tools/gen_papers.py` renders the
  archive-first form (archive URL first, original in backticks, "dead
  since", "Wayback Machine capture of YYYY-MM-DD") or the plain dead notice,
  via a new `free_copy_text()` helper.
* Regenerated `docs/references/papers/{index,designed-on-sky130}.md`.
  `gen_papers.py --check`, `check_papers.py`, `check_papers.py --selftest`
  all pass.
* `check_patents.py`/`gen_patents.py`/`data/patents.yaml` and
  `check_filings.py`/`gen_filings.py`/`data/filings.yaml` needed **no**
  change: no patents-page token was dead in either check, and filings.yaml
  already has a native `urls.wayback` field (unrelated to this R-WAYBACK
  extension) — confirmed both `--check`s still pass.
* Two **new** first-check-dead tokens turned up in today's full pass
  (neither is one of the original four; neither meets the two-check rule
  yet — needs a recheck after 2026-09-26):
  * `doi:10.37934/sej.3.1.1421b` (`data/papers-excluded.yaml`) — DNS
    resolution failure, confirmed independently.
  * `https://web.archive.org/web/20230329202011/.../skyt-20230101.htm`
    (the `wayback` mirror of `data/filings.yaml`'s
    `skywater-10-k-2023-03-15`-ish 10-K record) — HTTP 404, confirmed on a
    manual recheck too (amid some transient connection-refused noise from
    this environment hitting archive.org repeatedly).
* Bot-wall hosts report B found via `--include-generated` (espacenet.com —
  all 34 sampled tokens, academic.oup.com, dl.acm.org, escholarship.org,
  wiley.com family, pubs.aip.org, authorea.com, mdpi.com, techrxiv.org) —
  all re-fetched fresh this run (not carried over), all still 403
  (`blocked-to-scripts`). No change needed.
* Soft-dead? suspects: ran the check to completion on the generated-page
  corpus for the first time (report B skipped it there). **Zero new
  suspects on generated pages.** The 8 suspects in today's report are the
  same pre-existing hand-written-page ones report B already reviewed as
  "Fine" (LIU-2020, ANN-03/fossi-foundation, 2 GitHub raw-data blob pages,
  3 archived Novellus/Strasbaugh pages) — not re-reviewed again since
  nothing changed for them.
* All checkers, all three generators' `--check`, and the `-W` build pass
  (see the final commit's checker-run output / link-check-2026-09c.md).

## Left / next

All done. `docs/plans/link-check-2026-09c.md` written; full checker suite,
all three generators' `--check`, and the `-W` build all pass (re-run after
the report was written); `fix_reading_list_links.py --refresh` and
`link_named_titles.py --refresh` both ran for real, 0 files changed by
either. Ready to push.

## Notes / oddities

* `tools/check_links.py`'s bare-URL extraction (`URL_RE`) does not actually
  exclude a URL written between backticks — a backtick-wrapped "original,
  dead since ..." citation (THUNG-2016, TEL-PROBER, and now the OSTI free
  copy) is still picked up and reported "dead" on every future run, despite
  R-WAYBACK step 3's comment that backticks make "the checker stop
  reporting it". This is pre-existing tool behaviour (not introduced here);
  documented in link-check-2026-09c.md as expected/no-action rather than
  fixed, since fixing `check_links.py`'s extraction regex was not asked for
  and risks changing behaviour report B already relied on.
* Do not use `python3 -c "..."` (inline scripts) or multi-command `&&`/`;`
  chains with heredocs in one Bash call in this environment — a hookify
  rule blocks them. Write throwaway scripts to `tmp/scripts/*.py` with the
  Write tool (or a single `cat > file << 'EOF'` heredoc call on its own)
  and run them with a plain `python3 <path>` call.
* The link-check cache (`tmp/link-check-cache.json`, gitignored) is seeded
  from `.worktrees/rd-theme/tmp/link-check-cache.json`, an orphaned
  worktree directory left on disk (not in `git worktree list`) holding a
  pre-`--include-generated`, pre-IOP-fix hand-written-page cache. Reading
  it (not writing) to save redundant network fetches; `--reclassify` was
  run afterwards so categories reflect the current `classify()` logic.
