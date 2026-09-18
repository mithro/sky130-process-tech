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

Method: `tmp/gather_candidates.py <query>` (OpenAlex `title_and_abstract.search`,
cached under `tmp/fetch-cache/`, 3 s pacing, exponential back-off on
429/503) collects hits not already in `data/papers.yaml` or
`data/papers-excluded.yaml` (by id) into `tmp/candidates.tsv`. Titles were
then filtered (`tmp/check_known_titles.py`) against both files by
casefolded title (catches preprint/published-version dupes id-matching
misses) and manually triaged with `tmp/oa_work.py <openalex id>`
(abstract reconstructed from `abstract_inverted_index`).

| # | Service | Query | Date | Hits | Examined | Added | Excluded/Held | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | OpenAlex | title_and_abstract.search "sky130-based" | 2026-09-19 | 53 | 48 new | 0 | 0 | Duplicates of already-known papers by title/id |
| 2 | OpenAlex | title_and_abstract.search "skywater-130" | 2026-09-19 | 117 | 78 new | 0 | 0 | |
| 3 | OpenAlex | title_and_abstract.search "skywater 130-nm" | 2026-09-19 | 108 | 9 new | 0 | 0 | |
| 4 | OpenAlex | title_and_abstract.search "130-nm skywater" | 2026-09-19 | 108 | 4 new | 0 | 0 | |
| 5 | OpenAlex | title_and_abstract.search "skywater cmos" | 2026-09-19 | 90 | 29 new | 0 | 0 | |
| 6 | OpenAlex | title_and_abstract.search "skywater process" | 2026-09-19 | 158 | 26 new | 0 | 0 | |
| 7 | OpenAlex | title_and_abstract.search "SKY130" | 2026-09-19 | 137 | 52 new | 0 | 0 | Already-run round-1 term, re-run for completeness |
| 8 | OpenAlex | title_and_abstract.search "SkyWater 130" | 2026-09-19 | 117 | 0 new | 0 | 0 | |
| 9 | OpenAlex | title_and_abstract.search "sky130" | 2026-09-19 | 137 | 0 new | 0 | 0 | |
| 10 | OpenAlex | title_and_abstract.search "SkyWater PDK" | 2026-09-19 | 100 | 17 new | 0 | 0 | |
| 11 | OpenAlex | title_and_abstract.search "open-source PDK 130 nm" | 2026-09-19 | 68 | 29 new | 0 | 0 | |
| 12 | OpenAlex | title_and_abstract.search "Open MPW" | 2026-09-19 | 86 | 78 new | 0 | 0 | Screened by title for skywater/sky130/caravel/efabless/openlane/tinytapeout/chipignite; rest are unrelated MPW usages (astronomy, chemistry) |
| 13 | OpenAlex | title_and_abstract.search "Efabless" | 2026-09-19 | 14 | 8 new | 1 | 4 | See below — Dubey ASIC tape-out paper added |
| 14 | OpenAlex | title_and_abstract.search "OpenLane" | 2026-09-19 | 224 | 84 new | 0 | 5 (book chs.) | Most hits are the lane-detection computer-vision dataset "OpenLane"; SKY130-relevant OpenLane-only hits (no SKY130/SkyWater named) are EDA-methodology papers with no fabrication, screened by title and abstract but not individually recorded (see log) |
| 15 | OpenAlex | title_and_abstract.search "silicon-proven" | 2026-09-19 | 5856 | 100 new (sampled) | 0 | 0 | Overwhelmingly unrelated (generic phrase); only useful in combination with skywater/sky130, already covered by #1-11 |
| 16 | OpenAlex | title_and_abstract.search "Caravel" | 2026-09-19 | 401 | 98 new (sampled) | 0 | 0 | Overwhelmingly false positives (the sailing ship, medical catheter brand, unrelated software); SKY130-relevant Caravel hits already covered by #1-11, #13 |
| 17 | OpenAlex | citing works of key PDK/OpenLane/OpenROAD papers | not done | | | | | Deferred — see Held/open items below |
| 18 | arXiv export API | all:sky130 | 2026-09-19 | 14 | 13 new | 0 | 13 | 1 already known (Beall); 13 new all excluded — SKY130 used only as an EDA/agent-benchmark PDK target (synthesis/PnR/SPICE), no fabrication; see log |
| 19 | DBLP | skywater / sky130 | 2026-09-19 | n/a | — | 0 | 0 | `dblp.org` TLS connection reset (same as round 1's "connection refused"); not retried in a loop per pacing rules |
| 20 | Crossref | bibliographic search, further container titles | not done | | | | | Deferred — time budget |
| 21 | Semantic Scholar | keyless public API, sky130/skywater | 2026-09-19 | n/a | — | 0 | 0 | HTTP 429 on first request and again after one 8 s back-off; not retried further per pacing rules (still rate-limited, as in round 1) |
| 22 | Held items (round 1) | full-text re-check | 2026-09-19 | 6 items | 6 | 0 | 6 still held/excluded | See below |

## Held items re-checked (from `data/papers-excluded.yaml`, round 1)

- [x] `doi:10.1145/3400302.3415735` — Building OpenLANE. Re-fetched the ACM DL page via the Wayback
  Machine (gold OA, but ACM itself returns HTTP 403 to a direct fetch): confirms SKY130/SkyWater appear
  only in the reference list ([11] OSU Standard Cells for Sky130, [12] SKY130 PDK), not in the abstract
  body describing StriVe's own fabrication. Still **held**.
- [x] `doi:10.1109/mssc.2024.3381097` — Tiny Tapeout platform article. OpenAlex abstract unchanged
  (one sentence, no process named); IEEE closed access, no free copy. Still **held**.
- [x] `doi:10.36227/techrxiv.172055642.27780676/v1` — Tiny Tapeout preprint. TechRxiv still returns
  HTTP 403 to a scripted fetch. Still **held**.
- [x] `doi:10.1109/mssc.2024.3385734` — Unlocking Circuits for Quantum (4 K). Full OpenAlex abstract
  re-read in full (not truncated this time): motivation/background only, never names the process or
  gives the measured results the title promises. Still **held**.
- [x] `doi:10.1109/hswtech64936.2025.11277421` — HSWTech 2025 amplifier. **Resolved to excluded**: the
  abstract's "measured" gain/noise/power figures are explicitly from "comprehensive post-layout extraction
  and parasitic-aware simulations" of a "fabricated-ready" (i.e. not yet fabricated) layout.
- [x] `doi:10.2139/ssrn.7289627` — SSRN image-sensor preprint. SSRN still returns HTTP 403. Still **held**.

## Log

- 2026-09-19: Worktree created, briefs and design doc read, progress file
  started. Network access confirmed (OpenAlex reachable). Beginning
  OpenAlex hyphenated-variant searches per design §5.
- 2026-09-19: Ran all 16 OpenAlex `title_and_abstract.search` queries in
  the table above (searches #1–16), collecting ~660 raw hits, filtered by
  title keyword match to ~175, then de-duplicated by title against both
  datasets. Two apparent "new" hits (arxiv:2604.21625 Beall 2026 and
  doi:10.1109/jxcdc.2026.3670667 Didin 2026) turned out to already be in
  `data/papers.yaml` under a different id form (arXiv vs. Crossref DOI) —
  id-only dedup missed these; title-casefold dedup (`tmp/check_known_titles.py`)
  catches this class of duplicate going forward.
- 2026-09-19: Added `doi:10.1109/mdat.2026.3670063` (Dubey, Aysu,
  Cammarota, "ASIC Tape-Out of the First Side-Channel-Protected Neural
  Network Design", IEEE Design & Test 2026) — verified via Crossref
  (title/authors/year/volume/issue/pages match OpenAlex); named-process
  basis from the abstract's "We fabricated the ASIC using the SkyWater
  130nm technology node ... integrating ... Efabless' ChipIgnite shuttle
  program." Label `paper-dubey-2026a`.
- 2026-09-19: Screened ~54 SKY130/SkyWater-titled candidates from
  searches #1–11 by abstract (`tmp/oa_work.py`); all but the one addition
  above are simulation/post-layout/EDA-methodology studies with no
  fabrication statement, software/dataset records (Zenodo SBGR, IAIONEX),
  or theses/dissertations (SHAREOK ×2, BRAC, TU/e — not recorded, out of
  scope by type, no DOI to record against). One Zenodo "paper" (Silicluster
  v2 analog blocks) turned out to be an 18-page MOS-AK conference slide
  deck (downloaded and read with `pdftotext`) — excluded as slides, not a
  paper, despite giving two measured values.
- 2026-09-19: The "Efabless" query (#13) surfaced
  `doi:10.1109/mdat.2026.3670063` (added) plus two companion PWM-design
  papers built for the "Efabless AI-Generated Open-Source Chip Design
  Challenge" (arxiv:2405.02329, doi:10.1109/peds63958.2025.11144900):
  fetched the arXiv PDF full text of 2405.02329 (no arXiv HTML version
  exists) and confirmed SKY130/SkyWater is named nowhere in it, so both
  stay excluded per the design's "no shuttle-context inference" rule. A
  Zenodo "SoM-Memristor v3" record was excluded as an unfabricated,
  internally-inconsistent (claims both "Sky130" and "180 nm") self-published
  design-file release.
- 2026-09-19: arXiv export API query `all:sky130` (#18, `http://export.arxiv.org/api/query`,
  redirects to https) returned 14 hits; 13 were new. All 13 use SKY130
  only as a benchmark/target PDK for EDA, LLM-agent or accelerator papers
  evaluated by synthesis, place-and-route or SPICE simulation (confirmed
  by full abstract text for each, with two — LearnAFE and the memristive
  SNN accelerator — additionally checked against their arXiv PDF full
  text via `pdftotext`, confirming "post-layout simulation" and a
  literature-sourced (not SKY130-fabricated) "measured" dataset
  respectively); none report SKY130 fabrication or silicon measurement,
  so all 13 are excluded. Also excluded via the same pass: the arXiv
  preprint of "mflowgen" (evaluated across five nodes, no SKY130-specific
  findings) and its ICCAD 2022 published version is noted in the same
  record.
- 2026-09-19: DBLP (`dblp.org/search/publ/api`) still resets the TLS
  connection for both "sky130" and "skywater" (as in round 1); not
  retried in a loop. Semantic Scholar's public search API returned
  HTTP 429 on first request and again after an 8 s back-off; not retried
  further.
- 2026-09-19: Citing-works search (#17) run for one seed paper (the
  "Building OpenLANE" WOSET/ICCAD invited-talk abstract,
  doi:10.1145/3400302.3415735, OpenAlex W3114230949, 41 citing works):
  found and excluded two more in-scope-looking hits by abstract
  (doi:10.3390/computers13010009 SHA-256 ASIC — SKY130 named but only
  synthesis/PnR results; doi:10.3390/electronics15051048 — a generic
  open-source-EDA survey, not SKY130-specific). Citing-works searches for
  the SkyWater PDK description paper and for OpenROAD's own paper were
  not run (time budget) — the SkyWater PDK description paper
  (paper-edwards-2020a) has no DOI (`web:woset-2020-a03`), so it cannot
  be looked up by DOI in OpenAlex; it would need a title search.
- 2026-09-19: Re-checked all six items held from round 1 (see above);
  five remain held (still unretrievable/unconfirmable), one (HSWTech 2025
  amplifier) resolved to excluded on a closer reading of its existing
  abstract.
- 2026-09-19: Crossref bibliographic search restricted by further
  container titles (task step 2, design's "next round" item) was not
  run — time budget spent on the OpenAlex/arXiv passes above, which
  covered a broader surface. Left for a future round.

## Summary

Before this round: 49 included papers, 36 excluded/held.
After this round: 50 included papers (+1: paper-dubey-2026a), 91
excluded/held (+55: 54 new considered-and-rejected records plus one
round-1 held item resolved to excluded). No topic additions were needed.
No disagreements between sources were found for the one new record
(Crossref and OpenAlex agree on title, authors, year, volume, issue,
pages). Blocked/limited services: DBLP (TLS reset), Semantic Scholar
(HTTP 429), SSRN and TechRxiv (HTTP 403 on scripted fetch, per design's
known open questions) — all as in round 1, so still open questions for a
future round with browser access.
