# Progress: qualification-report evidence, round 1 (done)

Round 1 built `data/history/qtp.yaml` from 24 public Cypress qualification reports, fetched from
Infineon's public document store (`infineon.com/assets/row/public/documents/...`). Every quote is
checked against the cached text by `uv run tools/check_history_quotes.py`.

Routes that worked: Infineon's public asset URLs, found by searching for technology codes. Routes that
did not: Infineon `/dgdl/` links that redirect to a myInfineon login (not public, not used), and
Wayback CDX queries across all of cypress.com (time-outs).

The summary of processes, fabs, stackups and the inconsistencies between reports now lives on the
generated pages `docs/history/stackups.md` and `docs/history/products.md` and in each record's `notes`.
Round 2 continued in `progress-cyhist-qtp2.md`.
