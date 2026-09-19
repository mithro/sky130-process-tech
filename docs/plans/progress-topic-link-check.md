# Progress: topic/link-check

Agent brief: write `tools/check_links.py`, run it over the whole site,
fix what it finds. See the task description in the coordinator message
(not reproduced here); this file is the running log.

## Task 1 — the tool

- [x] Read agent-briefs.md common rules, citation-style.md,
      references/index.md, public-sources.md head, check_refs.py,
      check_papers.py (`--links` mode) for house style.
- [x] Wrote `tools/check_links.py`:
      - extracts URLs/DOIs from `docs/references/public-sources.md`
        (`**KEY**` blocks) and from every page's footnote *definitions*
        under `docs/` (the same scope as `check_refs.py`; generated
        index pages under `docs/references/{papers,patents,filings}/`
        use inline links, not footnotes, so are out of scope, matching
        the citation-style.md exception).
      - dedups a `https://doi.org/<doi>` URL against a bare `DOI
        10.xxxx/yyyy` mention of the same identifier.
      - per-host rate limiting (default 3 s, `patents.google.com` 20 s),
        at most `--workers` (default 4) hosts contacted concurrently
        (one worker thread per host group), HEAD then GET fallback,
        redirects followed by a custom handler that paces the new host
        and records the whole chain, retries with backoff on
        429/502/503/504/timeout.
      - JSON cache under `tmp/link-check-cache.json` (`--cache`),
        written after every single check so a killed run resumes;
        `--max-age-days` (default 30) skips fresh entries, `--force`
        ignores that.
      - DOIs checked via `https://doi.org/`; a 403 from the publisher
        after a DOI redirect classifies as `ok` ("resolves,
        access-controlled"), not dead.
      - `BLOCKED_HOSTS` (sec.gov, linkedin.com, indeed.com,
        glassdoor.com, researchgate.net, astm.org — astm.org confirmed
        2026-09-19: this UA gets 403, a browser UA gets 307) classify
        as `blocked-to-scripts` rather than dead.
      - dead tokens get a Wayback availability-API lookup.
      - Markdown report: counts + tables of dead / redirected-permanently
        / blocked-to-scripts, each row naming the inventory key(s) and
        page/footnote-label citers. `--strict` exits non-zero iff any
        token is dead.
      - `--selftest`: offline unit tests of the extraction/classify
        logic, no network, no cache file touched.
      - `--list-hosts`, `--only-host`, `--skip-host`, `--time-budget`
        for chunked/resumable foreground runs.
- [x] Documented in `README.md` under a new "Checkers" section
      alongside the other `tools/check_*.py` / `gen_*.py --check`
      tools.
- [x] Not added to `.readthedocs.yaml` / `docs/conf.py` (nothing there
      references `tools/` anyway).
- [x] Smoke-tested live on a couple of small hosts (arxiv.org,
      astm.org, store-us.semi.org) before the full run.

Inventory as extracted: 1781 tokens (850 URLs, 931 DOIs) across 1720
inventory entries and every page's footnotes.

## Task 2 — full run

Status: **done.** Ran in foreground chunks (`--time-budget`,
`--only-host`/`--skip-host`) because of the per-host pacing (doi.org
~930 tokens at ~3-5 s each; patents.google.com 121 tokens at 20 s
each); cache resumed between chunks. While triaging the first pass,
found and fixed three real bugs in the checker itself (each its own
commit, each with a new `--selftest` case):

1. A DOI's own `doi.org` -> publisher redirect hop was being read as
   "please update this citation" (`redirected-permanently`) — 336
   DOIs affected. The DOI is the permanent citation regardless of the
   resolver's current HTTP code; only the final outcome matters now.
2. The bare-URL fallback regex (and the bare "DOI 10.xxx" regex)
   excluded `)`, truncating every pre-2000 Elsevier DOI
   (`10.1016/0022-0248(82)90456-2` -> `...82`) and Wikipedia title with
   a disambiguator (`Wafer_(electronics)`) at the first `(` — ~55 bogus
   404s. House style always wraps a citation URL in `<...>`; that
   delimiter is now tried first and takes the whole interior verbatim.
3. `HEAD` was trusted alone; media.asml.com's CDN answers `HEAD` with a
   bare 404 for a PDF that `GET` serves fine — now any `HEAD` failure
   (not just a fixed status list) gets a `GET` second opinion.

Also: openlibrary.org's HEAD *and* occasionally GET 303-redirect a
perfectly good book URL to a `/verify_human` challenge page while
still reporting the ordinary final 200 — added challenge-URL detection
that overrides the numeric status. Final report: `docs/plans/
link-check-2026-09.md` (has its own "Investigation and remediation
notes" section — read that before re-doing any of this triage).

## Task 3 — fixes

Status: **done.** See `docs/plans/link-check-2026-09.md`'s notes
section for the full per-source detail. Summary:

* 10 permanent redirects fixed (citation + every repeating footnote
  updated, new URL verified live first): GOV-04, BYU-OXCALC,
  OPDKS-MAKEFILE/README/MAGIC-TECH, JOB-05/SKW-08, ANN-11, SKW-12,
  CYP-23, ANN-02, GCE-KLA8100 (restructured to new-URL-primary with a
  "formerly ..." note, matching a pre-existing model on
  cd-sem-overlay-metrology.md).
* `BLOCKED_HOSTS` extended (glassdoor.com, researchgate.net, astm.org,
  cdc.gov, appliedmaterials.com, forbes.com, businesswire.com,
  startribune.com) after confirming with both this tool's User-Agent
  and a browser one that these hosts block automated fetches
  generically, not just this project — no citations needed changing,
  51 tokens moved from dead/ok to the correctly-labelled
  blocked-to-scripts.
* Rule 11 applied to 2 sources with no retrievable copy anywhere:
  MERCKEL-1977 (evidence marked weak; no verbatim quote to remove) and
  ROSENFIELD-1986 (had a verbatim quote — removed and replaced with a
  weak paraphrase).
* THUNG-2016: not actually dead — the citation's own PDF link works;
  surfaced it identically on all 11 repeating footnotes.
* 2 sources (AMAT-RTP / edn.com, TEL-PROBER / telcertifiedused.com)
  independently confirmed live and NOT edited — the first is
  unreachable only from this checking sandbox (Akamai/IPv6 routing),
  the second is a flaky load-balancer backend. Both still show "dead"
  in the saved report's counts, which is an honest record of what this
  run's network could reach, not an outstanding fix.

Finishing checklist run in the foreground and clean: all
`tools/check_*.py`, `gen_papers/patents/filings.py --check`,
`uv run sphinx-build -W -q -b html docs tmp/build-link-check`.
