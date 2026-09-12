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
- [r] Steps 048–063: poly gate, resistor implants, gate etch (branch `steps/048-063`, written 2026-09-12, under review)
- [~] Steps 064–075: tips, halos, tip RTA (branch `steps/064-075`)
- [ ] Steps 076–088: spacers, source/drain, S/D RTA
- [ ] Steps 089–106: PSG, contact silicide, local interconnect
- [ ] Steps 107–117: contact, metal 1
- [ ] Steps 118–134: via 1–2, metal 2–3 (part)
- [ ] Steps 135–163: MiM caps, metal 3–5, vias 3–4
- [ ] Steps 164–171: passivation, pad, alloy, test

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
- [ ] Mask pages + mask ↔ step ↔ GDS index
- [ ] Glossary
- [ ] References / bibliography

## Phase 4 — Review

- [ ] Technical accuracy review of every step page (independent agent)
- [ ] Conflict review across pages (consistent thicknesses, names, order)
- [ ] Provenance review — repeat after each batch
- [ ] Full Sphinx build with `-W` (warnings as errors)

## Provenance-review log

| Date | Scope | Result |
|------|-------|--------|
| 2026-08-30 | `main` @ dd8ef12, all files + full history | 0 high, 9 medium (wording in `docs/plans/`, "step list" phrasing), 6 low — all fixed on `main` |
| 2026-09-12 | `main` @ e9e42a4, all files + history since dd8ef12 | 0 high, 35 medium, 105 low — all wording/hedging/citation hygiene; all fixed on `main` (merged 2026-09-12) |

## Notes

- 2026-08-30: Worktrees in `.worktrees/` (project-local); max two
  sub-agents concurrently; Sphinx + MyST chosen (see design doc).
- 2026-08-30: `main` is pushed to `origin` after every merge.
- 2026-09-12: Work resumed after a pause; worktrees recreated for the
  surviving branches.
