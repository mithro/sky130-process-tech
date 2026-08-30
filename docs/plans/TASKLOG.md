# Task log

Progress log for the SKY130 process technology documentation project.
One item is updated at a time; newest entries at the bottom of each
section.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` done ·
`[r]` awaiting review · `[!]` blocked

## Phase 0 — Setup

- [x] Read the source step list (171 steps) — 2026-08-30
- [x] Write design document — 2026-08-30
- [x] Repository scaffolding (licence, .gitignore, README) — 2026-08-30
- [x] Sphinx + MyST + Read the Docs configuration, builds clean — 2026-08-30
- [x] Step page template and checker script — 2026-08-30
- [x] Generate 171 stub step pages from the step list — 2026-08-30
- [x] Machine index, material index, mask index, glossary stubs — 2026-08-30

## Phase 1 — Research inventory

- [x] Inventory of public SkyWater / SKY130 sources (PDK docs, talks,
      SEC filings, press, job postings, patents, papers) — 2026-08-30,
      reviewed and merged (`docs/references/public-sources.md`)
- [~] Category pages (oxidation, deposition, litho, etch, implant,
      anneal, CMP, clean/strip, metallisation, test)

## Phase 2 — Step pages (grouped by process module)

- [~] Steps 001–013: starting material, STI, deep N-well (branch `steps/001-013`)
- [ ] Steps 014–034: wells and Vt implants
- [ ] Steps 035–047: SONOS tunnel/ONO, gate oxides
- [ ] Steps 048–063: poly gate, resistor implants, gate etch
- [ ] Steps 064–088: tips, halos, spacers, source/drain
- [ ] Steps 089–106: PSG, contact silicide, local interconnect
- [ ] Steps 107–117: contact, metal 1
- [ ] Steps 118–134: via 1–2, metal 2–3 (part)
- [ ] Steps 135–163: MiM caps, metal 3–5, vias 3–4
- [ ] Steps 164–171: passivation, pad, alloy, test

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

## Notes

- 2026-08-30: Worktrees in `.worktrees/` (project-local); max two
  sub-agents concurrently; Sphinx + MyST chosen (see design doc).
