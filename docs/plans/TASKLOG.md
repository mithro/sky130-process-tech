# Task log

Progress log for the SKY130 process technology documentation project.
One item is updated at a time; newest entries at the bottom of each
section.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` done ·
`[r]` awaiting review · `[!]` blocked

## Phase 0 — Setup

- [x] Compile the step list used in this reference (171 steps) — 2026-08-30
- [x] Write design document — 2026-08-30
- [x] Repository scaffolding (licence, .gitignore, README) — 2026-08-30
- [x] Sphinx + MyST + Read the Docs configuration, builds clean — 2026-08-30
- [x] Step page template and checker script — 2026-08-30
- [x] Generate 171 stub step pages from the step list used in this reference — 2026-08-30
- [x] Machine index, material index, mask index, glossary stubs — 2026-08-30

## Phase 1 — Research inventory

- [x] Inventory of public SkyWater / SKY130 sources (PDK docs, talks,
      SEC filings, press, job postings, patents, papers) — 2026-08-30,
      reviewed and merged (`docs/references/public-sources.md`)
- [x] Category pages (oxidation, deposition, litho, etch, implant,
      anneal, CMP, clean/strip, metallisation, test) — 2026-08-30,
      reviewed and merged; glossary seeded with 84 terms

## Phase 2 — Step pages (grouped by process module)

- [x] Steps 001–013: starting material, STI, deep N-well — 2026-08-30, reviewed and merged
- [x] Steps 014–034: wells and Vt implants — reviewed, converted to footnotes and merged 2026-09-12
- [x] Steps 035–047: SONOS tunnel/ONO, gate oxides — reviewed and merged 2026-09-12
- [x] Steps 048–063: poly gate, resistor implants, gate etch — reviewed and merged 2026-09-12 (PMOS gate read as n⁺ poly; 020/024 aligned)
- [x] Steps 064–075: tips, halos, tip RTA — reviewed and merged 2026-09-12
- [x] Steps 076–088: spacers, source/drain, S/D RTA — reviewed and merged 2026-09-12
- [x] Steps 089–106: PSG, contact silicide, local interconnect — reviewed and merged 2026-09-12
- [x] Steps 107–117: contact, metal 1 — reviewed and merged 2026-09-12
- [x] Steps 118–134: via 1, metal 2, via 2 — reviewed and merged 2026-09-12 (48 inventory entries added as §8.13; strip-step open question reworded on 108/113/114)
- [x] Steps 135–148: MiM capacitor 1, metal 3, via 3 — reviewed and merged 2026-09-13 (27 inventory entries added as §8.14; PDK capm level inconsistency disclosed)
- [x] Steps 149–163: metal 4, MiM capacitor 2, via 4, metal 5 — reviewed and merged 2026-09-13 (30 inventory entries added as §8.15; SKY130 read as an S8PIR* flow for metal-5 rules)
- [x] Steps 164–171: passivation, pad, alloy, test — reviewed and merged 2026-09-13 (25 inventory entries added as §8.16; all 171 step pages written)
- [x] Cite the public *S8 / SKY130 Process Steps* sheet (STEPS-SHEET) on the landing page, steps index and every step page — 2026-09-13
- [x] Use the sheet's mask tabs on the mask index and lithography pages — reviewed and merged 2026-09-13; plate IDs and reticle-set IDs added after owner approval (see below); lithography pages: see the via 2–4 follow-up
- [x] (merged 2026-09-13) Mask index: add reticle-set IDs, plate IDs and mask-type codes from the sheet, and fab lot numbers from the renders site (owner approved 2026-09-13), and link the public mask-layer renders (MASK-RENDERS; per run × mask directories, renders of drawn tapeout data); update the STEPS-SHEET entry and the NSM MPW-6 wording; add an inventory entry for the renders — after the via 2–4 lithography merge
- [x] (merged 2026-09-13; 014 and 062 aligned too) Apply the low findings of the sweeps provenance review (CD-metrology grade wording, 019/028 step-order tool evidence, EKS265 citation, TMAH arithmetic inputs, plate-case label caveat) — after the via 2–4 lithography merge
- [x] (reports done and integrated into the mask index 2026-09-13) Mask-render research: one read-only agent per MPW run (MPW-1 to MPW-8) reviewing the MASK-RENDERS site (job/slot metadata, the site's derived-mask expressions, cross-check with the sheet's plate records); reports to be integrated into the mask index
- [x] (reports done 2026-09-13; test-tile, HV/native/ESD and 1.8 V MOSFET and passives integration reviewed and merged 2026-09-13; deferred passives additions for 008, 023/024, 171, test category and overview merged 2026-09-13) Raw-data research: four read-only agents reviewing the raw-data repository (RAW-DATA-README; docs and test tile; 1.8 V MOSFETs; HV, native and ESD devices; passives, BJTs and varactors); reports propose additions to step, category and index pages
- [x] Consistency sweep part 1 — SkyWater quotations verbatim, vendor names in prose, S65 mask count, alloy hydrogen wording, BEOL/MOL glossary, PSG and li-top stack readings, Cypress report variants, PECVD tungsten on WDEP, novolac, 2.38 % TMAH — reviewed and merged 2026-09-13
- [x] Consistency sweep part 2 — evidence grades and tool-class names for analogous steps, chemistries of analogous steps, supplier statements with filing and year, developer strength on all mask pages — reviewed and merged 2026-09-13. Left open (see machines and materials indexes): metal-etch gas differences, HMDS on MM3/MM4, Iridia on DNIS/LVTPIS, "strong" vs "strong for existence" for overlay/CD tools, EKS265 vs EKC265

## Phase 2b — Citation conversion (added 2026-08-30)

Citations are now Markdown footnotes with at least eight annotated
deep-dive entries per step page and twelve per category page
(`docs/plans/citation-style.md`, enforced by `tools/check_refs.py`).
`docs/steps/008-dni.md` is the converted exemplar.

- [x] Citation style guide, checker and exemplar page — 2026-08-30
- [x] Convert step pages 001–007, 009–013 and expand deep-dive lists — reviewed and merged 2026-09-12
- [x] Inventory: every source cited on written pages is keyed in `public-sources.md` (612 entries) — merged 2026-09-12
- [x] Convert the ten category pages and expand deep-dive lists — reviewed and merged 2026-09-12
- [x] Convert steps 014–034 — 2026-09-12

## Phase 3 — Cross-cutting pages

- [x] Machine pages + machine ↔ step index — index page reviewed and merged 2026-09-13; per-class pages: pilot (three implanter classes) reviewed and merged 2026-09-13 with `tools/check_machines.py`; thermal batch (three vertical-furnace classes, rapid thermal processor, plasma nitridation chamber) reviewed, provenance-checked and merged 2026-09-13; etch batch (silicon, dielectric and metal plasma etchers, downstream plasma asher, wet bench and spray processor) reviewed, provenance-checked and merged 2026-09-13; deposition batch (PECVD and SACVD, HDP-CVD, tungsten CVD, PVD cluster tool) reviewed, provenance-checked and merged 2026-09-14; lithography batch (i-line stepper, KrF stepper, coat/develop track, CD-SEM and overlay metrology) reviewed, provenance-checked and merged 2026-09-14; CMP, clean and starting-material batch (starting material, single-wafer spin processor, CMP polisher, post-CMP cleaner) reviewed, provenance-checked and merged 2026-09-14; metrology and test batch (defect inspection, film thickness and stress, sheet resistance and dose, cross-section SEM and profilers, parametric tester and prober) reviewed, provenance-checked and merged 2026-09-14 — all 30 machine-class pages written. Follow-ups from the machine reviews (Mercury wording, LSI anneal, Trikon/Lam, Hitachi S-9200, Mirra Mesa caveat, Bibby wording, CMP row marker, AIT/SP1 readings, liner wording, checker also-lists) fixed, reviewed and merged 2026-09-14.
- [x] Materials pages + material ↔ step index — index page reviewed and merged 2026-09-13; per-class pages: pilot (wet chemicals, lithography materials, sputter targets) with `tools/check_materials.py`, row keys, a row-ownership table and the material-page writer brief reviewed, provenance-checked and merged 2026-09-14; substrates, CMP consumables, anneal ambients, ultrapure water and hardware consumables, and the process gases, dopant sources, precursors and etch gases pages reviewed and merged 2026-09-14 (duplicate EPA sources merged) — all 12 material-class pages written. Follow-ups (Al–0.5%Cu wording, EPA record on the index, BF₃ row name, Coburn/Kang abstracts, NF₃ GWP labels, step 111 reading) fixed, reviewed and merged 2026-09-14.
- [~] Mask pages + mask ↔ step ↔ GDS index — index page reviewed and merged 2026-09-13; per-mask pages: pilot (DNM, P1M, VIM4) with `tools/check_masks.py` and the mask-page writer brief reviewed and merged 2026-09-14; 33 masks to go. Follow-up: STOLMEIJER-1986 wording on steps 008, 018, 027 and its inventory note; LEVINSON-2005 "tool choice for non-critical levels" on the masks index and inventory note. ITRS 2001 "cheaper tools for non-critical layers" claim removed from about 30 pages (ASML-30 cited instead; ITRS listed as exposure options), reviewed and merged 2026-09-14
- [x] sky130B ReRAM module page (`docs/overview/sky130b-reram.md`) — reviewed and merged 2026-09-13 (31 inventory entries in §8.17 and RERAM-INDEX)
- [x] Process overview page (`docs/overview/index.md`) — reviewed and merged 2026-09-13
- [x] References landing page (`docs/references/index.md`) — 2026-09-13
- [x] (2026-09-13) Materials index: cite or label the typical values flagged by the 2026-09-13 review (Si₃N₄/SiO₂ thickness ranges, IMP Ti/TiN thickness, H₃PO₄ 85 %, H₂O₂ 30 %, TMAH 2.38 wt.%, Ti:W 10 wt.%); the sheet's "Masks" tab lists 37 rows (incl. PSDI) vs 36 mask steps
- [x] (merged 2026-09-13) Lithography of vias 2–4 after the sheet's mask-type record (Sheet4: 248 nm attenuated PSM for VIM2/VIM3, 248 nm binary for VIM4, our reading): update VIM4 (159) i-line inference and mercury-lamp bullet, VIM2 (129) and VIM3 (144) reticle-type open questions, and the machines index VIM4 i-line assignment — after sweep part 2 merges
- [x] Glossary: 144 terms, linked on first use across all written pages; inventory keyed for every label (748 entries) — merged 2026-09-12
- [x] Glossary and inventory top-up for steps 076–117 (204 terms; 951 inventory entries) — merged 2026-09-12
- [ ] References / bibliography

## Phase 4 — Review

- [ ] Technical accuracy review of every step page (independent agent)
- [ ] Conflict review across pages (consistent thicknesses, names, order)
- [ ] Provenance review — repeat after each batch
- [ ] Full Sphinx build with `-W` (warnings as errors)

## Provenance-review log

| Date | Scope | Result |
|------|-------|--------|
| 2026-08-30 | `main` @ a335c7f, all files + full history | 0 high, 9 medium (wording in `docs/plans/`, "step list" phrasing), 6 low — all fixed on `main` |
| 2026-09-12 | `main` @ 05150a6, all files + history since a335c7f | 0 high, 35 medium, 105 low — all wording/hedging/citation hygiene; all fixed on `main` (merged 2026-09-12) |
| 2026-09-12 | `main` @ c06e388, all files + history since 05150a6 | 0 high, 11 medium, 22 low — hedging/citation hygiene on steps 048–088; all fixed on `main` (merged 2026-09-12) |
| 2026-09-12 | `main` @ eca31e2, files + history since 8060783 (steps 118–134) | 0 high, 3 medium, 6 low — step-list label wording, one broken edit, typical-value marking; fixed on `main` incl. same pattern on steps 004–117 (merged 2026-09-13) |
| 2026-09-13 | `main` @ 9ea20a2, files + history since 8418f18 (steps 135–148) plus job-listing mentions across `docs/` | 0 high, 7 medium, 4 low — step names/order used as evidence (swept across 001–148, categories, glossary), MiM materials stated as fact, unretrievable listing material removed from §4 and pages; fix branch independently reviewed (16 follow-up fixes) and merged 2026-09-13 |
| 2026-09-13 | `main` @ 2e6578a, files + history since 18b0ec7 (steps 149–163) | 0 high, 7 medium, 3 low — step order/code used as evidence on 149–162; fixed on `main` (merged 2026-09-13) |
| 2026-09-13 | `main` @ b88f6ee, files + history since 0fa02fb (steps 164–171, mask index) | clean; 0 high, 0 medium, 6 low — readings stated as fact in openings, one step-name reading, typical NA and derived values unmarked; fixed on `main` (merged 2026-09-13) |
| 2026-09-13 | `main` @ 12d486b, files + history since b88f6ee (sheet citation, overview, ReRAM, machines, materials, references pages) | 0 high, 2 medium, 6 low — step order/name used as evidence on the overview (fixed on `main`, merged 2026-09-13); materials-index typical values without citations and mask-type codes in STEPS-SHEET pending |
| 2026-09-13 | `main` @ 72f7c08, files + history since 2caaa17 (consistency sweeps 1–2, materials citations, mask-run section) | clean of non-public content; 0 high, 0 medium, 5 low (CD-metrology grade wording, step order as tool evidence on 019/028, EKS/EKC citation, TMAH arithmetic inputs, plate-case labels) + 1 owner-decision note — fixes queued after the via 2–4 lithography merge |
| 2026-09-13 | `main` @ 8d9a6f8, files + history since 72f7c08 (via 2–4 lithography, mask plates/renders, raw-data integrations, grade fixes) | clean of non-public content; 0 high, 0 medium, 5 low (bare URLs and wording in this task log, one overview sentence on the test tile) + note on 026 background concentration — fixed on `main` 2026-09-13 (overview sentence via the deferred-passives branch) |

## Notes

- 2026-08-30: Worktrees in `.worktrees/` (project-local); max two
  sub-agents concurrently; Sphinx + MyST chosen (see design doc).
- 2026-08-30: `main` is pushed to `origin` after every merge.
- 2026-09-12: Work resumed after a pause; worktrees recreated for the
  surviving branches.
