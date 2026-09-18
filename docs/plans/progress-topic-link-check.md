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

Status: not started / in progress / done (update as it proceeds).
Run in foreground chunks (`--time-budget`, `--only-host`/`--skip-host`)
because of the per-host pacing (doi.org alone is ~930 tokens at ~3-5 s
each; patents.google.com 121 tokens at 20 s each). Cache resumes
between chunks. Final report saved to
`docs/plans/link-check-2026-09.md`.

## Task 3 — fixes

(filled in as sources are repaired)
