# Paper index — round 2 progress

Branch `topic/index-papers-r2`. Continues `docs/plans/paper-index-design.md`
§5 "Not available on 2026-09-14" and the held items in
`data/papers-excluded.yaml`. Fetches use user agent
`sky130-process-tech docs checker` only, no e-mail/mailto anywhere, paced
one request every few seconds with exponential back-off on 429/503, no
looping on a host that bot-checks. Raw fetches cached under `tmp/`
(gitignored).

Starting point: 49 papers in `data/papers.yaml`, 36 in
`data/papers-excluded.yaml`.

## Searches

| # | Service | Query | Date | Hits | Examined | Added | Excluded/Held | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | OpenAlex | title_and_abstract.search "sky130-based" | | | | | | |
| 2 | OpenAlex | title_and_abstract.search "skywater-130" | | | | | | |
| 3 | OpenAlex | title_and_abstract.search "skywater 130-nm" | | | | | | |
| 4 | OpenAlex | title_and_abstract.search "130-nm skywater" | | | | | | |
| 5 | OpenAlex | title_and_abstract.search "skywater cmos" | | | | | | |
| 6 | OpenAlex | title_and_abstract.search "skywater process" | | | | | | |
| 7 | OpenAlex | title_and_abstract.search "SkyWater PDK" | | | | | | |
| 8 | OpenAlex | title_and_abstract.search "open-source PDK 130 nm" | | | | | | |
| 9 | OpenAlex | title_and_abstract.search "Open MPW" | | | | | | |
| 10 | OpenAlex | title_and_abstract.search "Efabless" | | | | | | |
| 11 | OpenAlex | title_and_abstract.search "OpenLane" + silicon-proven | | | | | | |
| 12 | OpenAlex | title_and_abstract.search "Caravel" harness | | | | | | |
| 13 | OpenAlex | citing works of key PDK/OpenLane/OpenROAD papers | | | | | | |
| 14 | arXiv API (export) | sky130 / skywater | | | | | | |
| 15 | DBLP | skywater / sky130 | | | | | | |
| 16 | Crossref | bibliographic search, further container titles | | | | | | |
| 17 | Semantic Scholar | keyless public API, sky130/skywater | | | | | | |
| 18 | Held items | full-text re-check | | | | | | |

## Held items to resolve (from `data/papers-excluded.yaml`)

- [ ] `doi:10.1145/3400302.3415735` — Building OpenLANE
- [ ] `doi:10.1109/mssc.2024.3381097` — Tiny Tapeout platform article
- [ ] `doi:10.36227/techrxiv.172055642.27780676/v1` — Tiny Tapeout preprint
- [ ] `doi:10.1109/mssc.2024.3385734` — Unlocking Circuits for Quantum (4 K)
- [ ] `doi:10.1109/hswtech64936.2025.11277421` — HSWTech 2025 amplifier
- [ ] `doi:10.2139/ssrn.7289627` — SSRN image-sensor preprint

## Log

- 2026-09-19: Worktree created, briefs and design doc read, progress file
  started. Network access confirmed (OpenAlex reachable). Beginning
  OpenAlex hyphenated-variant searches per design §5.
