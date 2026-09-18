> **Warning: AI in use — use at own risk.**

# SKY130 Process Technology — a step-by-step manufacturing reference

This project documents, step by step, how the SKY130 130 nm CMOS process
technology is manufactured. SKY130 is the open-source process design kit
(PDK) released by SkyWater Technology and Google in 2020; it is derived
from the Cypress Semiconductor "S8" 130 nm process and is fabricated on
200 mm wafers at SkyWater's Bloomington, Minnesota fab (see the
[SkyWater PDK documentation](https://skywater-pdk.readthedocs.io/) and
[SkyWater Technology](https://www.skywatertechnology.com/)).

The aim is to be the most comprehensive public reference on how a
mass-produced 130 nm process is set up — using SKY130 as the worked
example — covering, for every process step:

* what the step is and which general class of step it belongs to
  (oxidation, deposition, lithography, etch, implant, anneal, CMP, …);
* why the step exists in the integration flow;
* which kinds of manufacturing tools perform it, and which tools
  SkyWater is likely to use (based on public evidence);
* which consumables it needs (gases, wet chemicals, sputter targets,
  slurries, photoresists, …);
* public references for cross-checking, for a high-level understanding,
  and for a deep dive.

The documentation is written in Markdown, built with Sphinx + MyST, and
intended for publication on Read the Docs.

## Building

```sh
uv sync
uv run sphinx-build -W -b html docs docs/_build/html
```

## Checks

Before merging any branch, run:

```sh
uv run tools/check_steps.py
uv run tools/check_machines.py
uv run tools/check_materials.py
uv run tools/check_masks.py
uv run tools/check_refs.py
uv run tools/check_papers.py
uv run tools/check_patents.py
uv run tools/check_filings.py
uv run tools/gen_papers.py --check
uv run tools/gen_patents.py --check
uv run tools/gen_filings.py --check
uv run tools/gen_index_links.py --check
uv run sphinx-build -W -b html docs docs/_build/html
```

`tools/gen_index_links.py` rewrites the generated "Related patents /
papers / filings" block on every process page from the three datasets;
`--check` fails if a page's block is missing, stale or was hand-edited.
See `docs/plans/agent-briefs.md` for the full pre-merge checklist per
kind of page.

## Sources

Only publicly available sources are cited. See
`docs/references/` for the bibliography and the source policy in
`docs/plans/`.

## Checkers

`tools/` holds offline (and a few `--online`) checkers that enforce the
documentation's own house style; run each with `uv run`:

* `check_steps.py`, `check_machines.py`, `check_materials.py`,
  `check_masks.py` — page-template and cross-reference checks for the
  step, machine, material and mask pages respectively.
* `check_refs.py` — every page's footnote citations resolve to an
  inventory entry, are all defined and all used, and the Deep dive
  reading list meets its minimum length (`docs/plans/citation-style.md`).
* `check_papers.py`, `check_patents.py`, `check_filings.py` — validate
  the `data/papers*.yaml`, `data/patents.yaml` and `data/filings.yaml`
  datasets behind the generated indexes; `check_papers.py
  --online`/`--links` and `check_filings.py --online` re-fetch sources
  over the network to cross-check metadata and free-text links.
* `check_links.py` — re-fetches every URL and DOI cited anywhere in the
  documentation (the public-sources inventory and every page's footnote
  definitions) and reports which are OK, permanently redirected, blocked
  to scripted clients, or dead (with a Wayback Machine snapshot for
  each dead one). Polite by default: a per-host rate limit, HEAD before
  GET, retries with backoff, and a resumable on-disk cache under
  `tmp/`. Run with `uv run tools/check_links.py`; useful flags include
  `--only-host`/`--skip-host` and `--time-budget` for chunked runs,
  `--max-age-days`/`--force` for cache freshness, `--list-hosts` to plan
  a chunked run, `--report FILE` to save the Markdown report, `--strict`
  to fail on any dead link, and `--selftest` for the offline extraction
  unit tests. It is not part of the Read the Docs build.
* `gen_papers.py --check`, `gen_patents.py --check`, `gen_filings.py
  --check` — confirm the generated index pages under `docs/references/`
  are up to date with their datasets.

## Licence

Apache License 2.0 — see `LICENSE`.
