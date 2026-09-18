# Progress — topic/metal-cap (cross-cutting metal cap / barrier sweep)

Branch `topic/metal-cap`. Handles the cap-and-barrier question deferred by
the Phase 4 fixer branches for steps 135–148, 149–163 and 164–171:
whether every aluminium level of SKY130 carries the Ti / Al–0.5%Cu / TiW
stack of the 2013 Cypress report, or the Ti / TiN / Al–0.5%Cu / Ti / TiN
stack qualified in 2013–2014, and which pages depend on the answer.

Deferred rows this branch closes:

* `progress-topic-p4-135-148.md` — X1, 138-M1, 138-M2, 139-M1, 140-M1,
  145-M2, 146-M1.
* `progress-topic-p4-149-163.md` — X1, X2, X3, X4, 153-L1, 161-L1, 161-L3.
* `progress-topic-p4-164-171.md` — 169-L4 (`168-pdm.md:230`) and the
  unhedged `170-ally.md:57-58`.

(metal-cap-evidence)=
## 1. Evidence table

Every row is a public source read in full for this branch. Quotations are
verbatim from the retrieved copy.

| # | Source (key) | Date | Exact quotation | Scope | What it supports |
|---|---|---|---|---|---|
| E1 | Cypress QTP 113005 (`CYP-QTP-113005`) | January 2013 (product qual completed Nov 2012) | "TECHNOLOGY/FAB PROCESS DESCRIPTION–S8TNV-5R … Metal 1: 100A Ti / 3200A Al -0.5%Cu / 300A TiW / Metal 2: 100A Ti / 3200A Al -0.5%Cu / 300A TiW / Metal 3: 150A Ti / 7200A Al -0.5%Cu / 300A TiW"; "Die Fab Line ID/Wafer Process ID: Fab4 / S8TNV-5"; "Generic Process Technology/Design Rule (drawn): S8TNV-5R/0.13m"; "Name/Location of Die Fab (prime) Facility: Cypress Semiconductor -- Bloomington, MN" | **S8TNV-5R**, a three-metal 0.13 µm technology at Fab 4. Not S8P, not SKY130. Describes the stack *before* the 2013–2014 change | Ti/Al–Cu/TiW at all three levels of a 0.13 µm S8 sibling at the SKY130 fab, as of 2012–2013 |
| E2 | Cypress QTP 123907 / 132302 / 132301 (`CYP-QTP-123907`) | March 2014 | Qualification history: "123907 — Qualification of S8DI Technology Metal Stack Change from Ti/AlCu/TiW to Ti/TiN/AlCu/Ti/TiN in CMI Fab 4 — June 2013"; "132302 — Qualification of S8TNV Technology Metal Stack Change from Ti/AlCu/TiW to Ti/TiN/AlCu/Ti/TiN in CMI Fab 4 — July 2013"; "132301 — Qualification of S8P Metal Stack Change from Ti/AlCu/TiW to Ti/TiN/ALCu/Ti/TiN, excluding top metal layers — Feb 2014" | Three qualifications at Fab 4 CMI. Its **only** process-description page is S8DI's ("Die Fab Line ID/Wafer Process ID: S8DIN-5R", "1P3M, 0.15 um"); the document history page titles the report "QTP 123907: METAL STACK CHANGE, S8DIN TECHNOLOGY, FAB 4 CMI" | The only public statement about **S8P**'s own metal stack: it changed away from TiW in Feb 2014, six years before the first SKY130 MPW wafers, with an exclusion whose scope the record does not define |
| E3 | Same report, S8DI process description | March 2014 | "Metal 1: 150A Ti/250A TiN/3200A Al 0.5% Cu/90A Ti/500A TiN / Metal 2: 150A Ti/250A TiN/3200A Al 0.5% Cu/90A Ti/500A TiN / Metal 3: 500A TiW/21,250A Al 0.5% Cu/300A TiW" | S8DI (0.15 µm, 1P3M) after its change | What "excluding top metal layers" looked like in the one worked example in the same document: the thin levels take the five-film TiN stack; the 2.125 µm top level keeps TiW **both** under and over the aluminium — and the S8DI qualification line carries no exclusion clause at all, so keeping TiW on a thick top level was the practice even where the wording does not say so. Also: the aluminium is 3 200 Å here and in E1's S8TNV-5R metal 1, while the film totals differ (3 600 Å against 4 190 Å) — a comparison across two technologies, since this report does not print S8DI's pre-change stack |
| E4 | Cypress PIN145273 (`CYP-PIN145273`) | 2014-03-13 | "Subject: Improvement of Cypress Minnesota Back-End-of-Line Integration for 130nm SONOS Product Families"; "This change aligns our internal Cypress Minnesota process, Titanium Tungsten (TiW) based metal stack, with the industry-wide Best Known Method Titanium Nitride (TiN) based metal stack."; "Effective with the date of this notification, the affected part numbers in the attached file will transition to the new BEOL integration process."; "The integration process is tuned to ensure that there are no electrical changes" | The customer notification that carries E2. Covers "130nm SONOS Product Families" — 1 005 affected part numbers | TiW was the Minnesota fab's stack **before** March 2014 and TiN the one it moved to for its 130 nm SONOS families. The inventory's present gloss ("describes the TiW-based stack as Cypress's Minnesota process") states only half of this and is corrected on this branch |
| E5 | Cypress QTP 014807 (`CYP-QTP-014807`) | June 2005 | "TECHNOLOGY/FAB PROCESS DESCRIPTION – R7FT-3R … Metal 1: 150Å Ti / 4,200Å Al / 300Å TiW / Metal 2: 150Å Ti /4,200 Å Al / 300Å TiW / Metal 3: 150Å Ti / 8,000Å Al / 300Å TiW" | R7FT-3R, a 0.18 µm "Hot Al" derivative at Fab 4, nine years before the change | Its metal 3 sums to **8 450 Å = exactly the PDK's 0.845 µm** for `met3` and `met4` (our arithmetic) |
| E6 | Cypress QTP 030204 (`CYP-QTP-030204`) | June 2013 | "TiW, AlCu, TiW / 500A, 6000A, 300A" | RAM42HA (0.42 µm) at Fab 4 | The TiW/Al/TiW sandwich as the fab's older house stack; not a 0.13 µm datum |
| E7 | SKY130 PDK process stack diagram (`PDK-04`) | PDK, 2020– | `metal1` 0.36, `metal2` 0.36, `metal3` 0.845, `metal4` 0.845, `metal5` 1.26 (µm) | The published SKY130 stack | 0.36 µm = 3 600 Å = E1's metal-1/2 recipe **exactly**; the TiN stack of E3 sums to 4 190 Å. 0.845 µm = 8 450 Å = E5's metal-3 recipe **exactly** |
| E8 | PDK *Criteria & Assumptions* (`PDK-03`) | PDK | `Met1Thick` 0.35 (S8D\*), `Met2Thick` 0.35 (S8D\*), `Met3thick_p` 0.8 (S8P\*/SP8P\*), `Met4Thick_p` 0.8 (S8P\*/SP8P\*), `Met5Thickp_12` 1.2, `Met5Thick_p` 2, `Met3_Qthick` 0.85 (S8T\* other than S8TM\*) | "thickness for antenna ratio calculation" | met3 and met4: 0.845 − 0.8 = **450 Å**, exactly E1/E5's Ti + TiW cladding (150 + 300); the TiN stack's cladding is 150 + 250 + 90 + 500 = 990 Å. Counter-checks: the table writes 0.85 elsewhere, so 0.8 is not 0.845 rounded; but `Met1Thick` 0.35 against a 0.36 µm metal 1 leaves only 100 Å, so "antenna thickness = aluminium only" is not uniform. Metal 5's 600 Å matches no published cladding. **Strongest counter-check:** 0.85 exceeds the whole 7 650 Å of E1's S8TNV-5R metal 3 by about a tenth, so the antenna entries are not uniformly film-derived |
| E9 | PDK resistance table (`PDK-08`) | PDK | Metal1 125, Metal2 125, Metal3 47, Metal4 47, Metal5 29 mΩ/sq | Published sheet resistances | **Does not discriminate.** The aluminium is 3 200 Å in both E1 and E3, and 750–990 Å of Ti/TiN in parallel with 0.125 Ω/sq changes it by well under a per cent (our arithmetic) — consistent with E4's "no electrical changes" |
| E10 | PDK documentation, full cached text (`PDK-02`, `PDK-03`, `PDK-05`, `PDK-06`, `PDK-07`, `PDK-08`, `PDK-11`, `PDK-HV`, `PDK-PERIPH`, `PDK-04`) | PDK | — | Every published SKY130 rule, layer, device and antenna table | **Silence.** No occurrence of Ti, TiN, TiW, aluminium, "barrier", "ARC" or "anti-reflective" in any metal-stack context; `metal_stack.svg` carries thicknesses and permittivities only |
| E11 | SkyWater *Facilities & Capabilities* (`SKW-01`) | accessed 2026 | PVD: "Aluminum both pure and Cu doped", "TiW", "ESC TiN", "Imp TiN", "Collimated Ti"; metal etch: "Lam 9600, Al, TiW, TiN, Pt", "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt" | The fab's published capability list | **Does not discriminate.** Both stacks are depositable and etchable in the fab as publicly described |
| E12 | Edwards, *SKY130 …* talk (`ANN-16`) | 2021 | slide 46 "5 layers of aluminum metal"; slide 47 "Titanium Nitride (TiN) / aka 'Local interconnect'"; slide 50 repeats 0.36/0.36/0.845/0.845/1.26 µm | The one public SKY130 talk naming TiN | It names TiN as `li1`, not as a metal cap; it does not address the cap |
| E13 | PDK *Background* / periphery rules (`PDK-02`, `PDK-PERIPH`) | PDK | "5 levels of metal (p - penta)"; via3 rule heading "Via3 connects met3 to met4 in the SKY130Q\*/SKY130P\*/SP8Q/SP8P\* flow" | Flow identification | SKY130 is read as a five-metal S8P-family flow, so metals 3 and 4 have a further metal level above them |

Sources that do **not** bear on the question, checked and recorded so they
are not re-searched: the PDK layer, mask, device, extraction, antenna,
high-voltage and periphery documents (E10); SkyWater's S130 summary table
(`SKW-02`, thickness only); `data/patents.yaml` (no SkyWater- or
Cypress-assigned patent on aluminium cap or barrier composition).

(metal-cap-reading)=
## 2. The reading adopted

Set out in full in the canonical section, {ref}`overview-metal-cap`.

| Level | Reading | Confidence |
|---|---|---|
| Metal 1, metal 2 | Undecided, leaning TiN. E2/E4 are positive evidence that the fab's 130 nm stack changed away from TiW in 2013–2014 and no public exclusion covers the thin levels; against that, E7's 0.36 µm matches the TiW sum exactly and not the TiN sum | low |
| Metal 3, metal 4 | Undecided. E8's 450 Å is a real argument for a two-film cladding, but it carries its own counter-check and metals 3 and 4 are not top metal on E13's reading, so the Feb 2014 exclusion need not cover them | low |
| Metal 5 | TiW-capped, on the reading that SKY130's metal 5 is a "top metal layer" within E2's exclusion, with E3 as the worked example | moderate |

Nothing public names the films of any SKY130 metal level. Every statement
that depends on the choice is presented for both cases or marked as an
inference.

## 3. Locations that depend on the cap or barrier

Status: `pending` / `done` / `n-a` (true for either stack, or about the
fab's capability, a cited paper, a target, or a tool's material list).

Bulk counts from `grep -rn "TiW\|Ti:W\|titanium–tungsten\|titanium-tungsten"`:
658 hits in `docs/steps`, `docs/categories`, `docs/machines`,
`docs/materials`, `docs/masks`, `docs/overview` and `docs/glossary.md`.
Most are footnote definitions, Deep-dive annotations about TiW
metallisation in the literature, sputter-target and tool-capability lists
— those are `n-a`. The table lists the load-bearing ones.

| File | Lines | What depends | Status |
|---|---|---|---|
| `docs/overview/index.md` | new section; module paragraph; open question | canonical treatment | done |
| `docs/steps/112-tial6.md` | 15–24, 50–62, 78–90, generic recipe, open questions | metal-1 stack; PIN145273 gloss | done |
| `docs/steps/113-mm1.md` | 15, 38, 86–97, 111, 262 | reflectivity/ARC over the cap | done |
| `docs/steps/114-mm1e.md` | cap breakthrough, ARC, over-etch | metal-1 etch | done |
| `docs/steps/118-vim.md`, `119-vime.md` | via-1 floor | landing layer | done |
| `docs/steps/123-tial12.md` | 15–46, 98–114, 146, 196, 277–279 | metal-2 stack | done |
| `docs/steps/124-mm2.md`, `125-mm2e.md` | ARC, breakthrough | metal-2 litho/etch | done |
| `docs/steps/129-vim2.md`, `130-vim2e.md` | 30, 47, 63, 68, 77 | via-2 floor | done |
| `docs/steps/134-wtial3.md` | stack description, "On the bottom layer" | metal-3 stack — module source of truth | done |
| `docs/steps/136-captiw1.md` | 19–21, 32–34 | MiM top-plate inference | done |
| `docs/steps/137-capm.md` | 17, 23, 51, 120, 131, 143 | reflectivity over the plate stack | done |
| `docs/steps/138-capme.md` | 28–29, 33–39, 61–64, 106–109, 300–308 | **the stop-on-dielectric argument**; Liu & Kuo selectivity | done |
| `docs/steps/139-mm3.md` | 19–31, 69–78 | resist over capped Al | done |
| `docs/steps/140-mm3e.md` | 20–22, 71–72, 118–120 | breakthrough | done |
| `docs/steps/144-vim3.md`, `145-vim3e.md` | 18–19, 84–85 | via-3 floor | done |
| `docs/steps/146-tin5.md` | 19–20, 117–119 | pre-clean margin | done |
| `docs/steps/149-wtial4.md` | 16–20, 53–61, 113–124, 140–167, 218, 300–305 | metal-4 stack; **X1 misattribution** | done |
| `docs/steps/150-capild2.md` | 192–195 | MiM bottom-plate surface | done |
| `docs/steps/151-captiw2.md` | top-plate material | second MiM | done |
| `docs/steps/152-cap2m.md` | reflectivity | second MiM litho | done |
| `docs/steps/153-cap2me.md` | 28–35, 55–58, 93–98, 221 | stop-on-dielectric; **153-L1** | done |
| `docs/steps/154-mm4.md` | 73–77, 108–113 | ARC | done |
| `docs/steps/155-mm4e.md` | 20–23, 59–60, 73–79, 123–125 | breakthrough | done |
| `docs/steps/159-vim4.md`, `160-vim4e.md` | 15–22, 46–48, 84–89, 140–155, 192–194, 269 | **the whole via-4 etch-stop argument** | done |
| `docs/steps/161-wtial5.md` | 51–62, 162–164, 197–215 | metal-5 stack; **X2**, **161-L1**, **161-L3** | done |
| `docs/steps/162-mm5.md` | 102–112 | ARC | done |
| `docs/steps/163-mm5e.md` | 17–19, 112–114, 267 | breakthrough | done |
| `docs/steps/168-pdm.md` | 230–231 | **169-L4** Danzl annotation | done |
| `docs/steps/169-pdme.md` | 31–39, 74–79, 111–115, 165–166, 236–247 | already correct — model for tone; link added | done |
| `docs/steps/170-ally.md` | 57–58 | unhedged "aluminium, TiW and tungsten" | done |
| `docs/categories/deposition.md` | multi-layer metal class | class description | done |
| `docs/categories/etch.md` | metal-etch class entry | chemistry per cap | done |
| `docs/materials/sputter-targets.md` | Ti:W row, summary, steps | which targets are needed | done |
| `docs/materials/etch-gases.md` | TiW etch chemistry | gases per cap | done |
| `docs/materials/index.md` | Ti:W row | index row wording | done |
| `docs/machines/pvd-cluster-tool.md` | chamber set | which chambers | done |
| `docs/machines/plasma-etcher-metal.md` | cap breakthrough | chemistry | done |
| `docs/masks/mm1.md`, `mm2.md`, `mm5.md`, `capm.md`, `vim.md`, `vim2.md`, `vim3.md`, `pdm.md` | ARC/tone/landing sentences | mask-page readings | done |
| `docs/glossary.md` | ARC, Ti:W entries | definitions | done |
| `docs/references/public-sources.md` | `CYP-PIN145273`, `CYP-QTP-113005`, `CYP-QTP-123907` glosses | inventory accuracy | done |

Also changed, outside the table above because the cap is mentioned only
in passing: `docs/steps/116-cmpm.md`, `127-cmpm2.md` (the polish must not
break through to the cap), `121-wdep3.md`, `132-wdep4.md` (the plug floor
is the liner over the cap), `142-cmpm3.md` and `docs/masks/vim.md`,
`vim2.md`, `vim3.md`, `mm1.md`, `mm2.md`, `capm.md`,
`docs/machines/film-thickness-metrology.md`, `docs/machines/index.md`.

## 4. Sources added or re-glossed

No new source was fetched that the inventory did not already hold. Three
inventory glosses were wrong or incomplete and are corrected on this
branch:

* `CYP-PIN145273` said the notification "describes the TiW-based stack
  as Cypress's Minnesota process". It announces the move **away** from
  it. Gloss rewritten with the quotation and its date.
* `CYP-QTP-123907` recorded only the S8DI/S8TNV change line. Gloss now
  gives all three qualifications with dates and scope, and both printed
  stacks.
* `CYP-QTP-113005` did not say that the stack it describes is
  S8TNV-5R's and predates the change. It does now.

`LIU-2007-TIW`, `PAT-MIM-TI-ETCH` and `MIN-2008` gained the selectivity
and chemistry figures the rebuilt `CAPME` argument uses.

## 5. Work log

* Worktree created; briefs, citation style and the three Phase 4 reviews
  read in full; both Cypress PDFs and PIN145273 read page by page;
  PDK caches re-grepped for any metal-stack material name (none).
* Evidence table above written from the retrieved copies only.
* Canonical section written at {ref}`overview-metal-cap`; every
  dependent page brought into line; the three Phase 4 progress files'
  deferred rows marked closed.
