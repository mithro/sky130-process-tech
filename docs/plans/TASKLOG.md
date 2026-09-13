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
- [~] Steps 164–171: passivation, pad, alloy, test (branch `steps/164-171`)

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

- [ ] Machine pages + machine ↔ step index
- [ ] Materials pages + material ↔ step index
- [~] Mask pages + mask ↔ step ↔ GDS index (index page on branch `topic/masks-index`)
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

## Notes

- 2026-08-30: Worktrees in `.worktrees/` (project-local); max two
  sub-agents concurrently; Sphinx + MyST chosen (see design doc).
- 2026-08-30: `main` is pushed to `origin` after every merge.
- 2026-09-12: Work resumed after a pause; worktrees recreated for the
  surviving branches.
