# Patent discovery log — PPUBS sweep, 2026-09-19

This file records the Part 2 discovery sweep run against USPTO Patent
Public Search (PPUBS) while Google Patents remained blocked from this
environment (`tmp/patent-cache/.blocked`, confirmed again this round:
`https://patents.google.com/` itself returns the site-wide "unusual
traffic" bot-check). See `docs/plans/patent-index-design.md`'s "PPUBS
fallback" section for the schema/provenance rules this sweep's
additions follow, and `docs/plans/progress-index-patents.md` for the
round's overall summary. This file lives in `docs/plans/`, excluded
from the Sphinx build.

## Method

`tmp/ppubs_search.py` (not tracked; PEP 723 script, `requests` only)
opened a PPUBS session (`POST
https://ppubs.uspto.gov/api/users/me/session`, body `-1`, giving an
`x-access-token` header and a case id) and ran one combined query per
assignee against `POST
https://ppubs.uspto.gov/api/searches/searchWithBeFamily`, paced 16
seconds between requests (no burst; stops immediately on HTTP 429/403),
caching every raw response under `tmp/patent-cache/ppubs/*.json` (not
tracked). Each query combined an assignee restriction (`.as.`) with a
title-field (`.ti.`) OR-list of the process-module keywords the fixer
brief named — STI, wells, gate oxide/nitridation, poly, LDD/spacers,
salicide, local interconnect, W/contact plugs, aluminium
metallisation/barrier/capping layers, MiM, fuses, passivation/pads,
HV/drain-extended, SONOS/charge-trap, ReRAM — and, for the three older
assignees (Cypress, Spansion, Ramtron), a filing-date restriction
(`@ad<"20160101"`) matching the brief's "be inclusive for Cypress
process patents filed 1995-2015" instruction (SkyWater, Longitude,
Infineon Technologies LLC and Weebit Nano postdate that window, so were
left unrestricted).

**A CPC-classification restriction in the query itself proved
unreliable**: `("cypress semiconductor").as. AND H01L21$.cpc.` returned
0 hits although both halves work alone, and even an *exact* CPC symbol
already present on a returned record (`H01L21/823481.cpc.`) returned
only 1 hit against a corpus where that symbol appears on many thousands
of documents — the `.cpc.` field in this PPUBS deployment does not
behave as a working prefix or exact classification search. Restricted
to CPC classes as the brief asked for, instead, by filtering each
query's own results **client-side** against the CPC codes PPUBS returns
with every record (`cpcInventiveFlattened`, `cpcAdditionalFlattened`):
`H01L21`, `H01L27`, `H01L29`, `H01L23`, `H10B`, `H10N70` (the brief's
own list) plus three classes discovered to matter once real titles were
inspected — `H10D` (device structures; CPC's 2022+ reclassification
moved most of old `H01L27`/`H01L29` into `H10D`), `H10W`
(interconnect/wiring, reclassified out of `H01L23`) and `H10P`
(processes/apparatus for semiconductor manufacture, reclassified out of
`H01L21` — several genuine etch/deposition/metrology process patents,
e.g. "Method of uniformly etching refractory metals..." and "Inline
method to monitor ONO stack quality", carry only `H10P` codes and would
have been wrongly excluded without it) — and `G11C13` (resistive-memory
circuits, kept in scope for the ReRAM sweep specifically, per the
brief's inclusion of ReRAM).

## Sweep totals

| Query | Assignee restriction | Hits (`numFound`, capped at 100/query) |
|---|---|---|
| cypress | `"cypress semiconductor".as.` + date + module keywords | 151 |
| skywater | `"skywater technology".as.` + module keywords | 0 |
| longitude | `"longitude flash".as.` + module keywords | 14 |
| infineon-llc | `"infineon technologies llc".as.` + module keywords | 6 |
| spansion | `spansion.as.` + date + module keywords | 172 |
| ramtron | `ramtron.as.` + date + module keywords | 6 |
| weebit | `"weebit nano".as.` + module keywords | 28 |
| **Total hits** | | **377** |

377 hits collapse to **211 distinct DOCDB families** (`familyIdentifierCur`,
grouping every hit that shares one, since a large continuation estate's
several members each independently match the title keywords).
`skywater` returned 0: SkyWater's own family (`GP94259596`, already in
the dataset — the "carbon film" application, M2 above) does not use any
of the module-keyword vocabulary in its title, and no other
SkyWater-assigned family surfaced under either "SkyWater Technology" or
the broader "SkyWater" spelling.

Of the 211 families:

* **39 already present** in `data/patents.yaml` before this round
  (matched by member publication number or DOCDB family id) — this
  sweep independently re-finds most of the families the earlier rounds
  already added by other discovery methods, which is itself a useful
  cross-check that those additions were not missing an obvious
  continuation.
* **24 added** this round (see below).
* **136 in scope by CPC and title, left for later** — almost all a
  single large Spansion estate (about 120 families) and most of the
  Weebit Nano hits not already covered by the four existing Weebit
  families.
* **12 out of scope** — circuit, protection or EDA-tooling patents whose
  title happened to match a module keyword incidentally (e.g. "Cascode
  active shunt gate oxide protect during electrostatic discharge
  event", "Method... of automated generation of masks for spacer
  formation from a desired final wafer pattern" — mask-design software,
  not a fabrication step) but whose CPC class (`H02H`, `H03K`, `H03L`,
  `G03F1`, `G11C16` used for a memory-operation/sensing scheme rather
  than the cell structure) is circuit or tooling, not semiconductor
  process or device fabrication, per the brief's own exclusion.

## Why the 24 were chosen and the rest left for later

The 24 added (full records: `data/patents.yaml`; rendered:
`docs/references/patents/families.md`) were picked for module and
assignee diversity — two Cypress isolation families, two spacer
families, five SONOS/charge-trap families (including one each from
Infineon Technologies LLC and Longitude Flash Memory Solutions), one
gate-oxide, one poly/silicide, one salicide, one local-interconnect
(Ramtron), one contact, one aluminium-metallisation, one barrier-layer
(Ramtron), two MiM (one Cypress, one Spansion), two passivation, two
HV/drain-extended and one ReRAM (Spansion) family — while staying a
size this round could review individually with real care (each needed
its own relevance sentence, module target, and relation judgement; see
`docs/plans/patent-index-design.md`'s "PPUBS fallback" for the
schema this used).

**Left for later, with reasons, rather than added on a lower standard:**

* **The Spansion estate (~120 families).** Round-1 finding M4 (this
  branch's own earlier fix, see `docs/plans/progress-index-patents.md`)
  established that a Spansion-original family needs individual,
  narrowly-worded lineage reasoning — Spansion is the AMD/Fujitsu
  NOR-flash joint venture, not the Cypress/SkyWater Bloomington fab
  lineage, so each family needs its own `technique-class` relation and
  a reason that does not overstate a lineage tie. Applying that care to
  ~120 families individually is a substantial undertaking on its own;
  doing it hastily would either repeat the M4 mistake at scale or
  produce 120 templated, low-value entries. Left as a clearly-scoped
  follow-up.
* **Most of the Weebit Nano hits (~17 not already covered).** The four
  existing Weebit families already establish the `technique-class`
  relation for the OxRAM cell/manufacturing technique itself. Most of
  the remaining hits are circuit-level programming, read/write or
  binning schemes ("Write method for differential resistive memories",
  "Circuitry for parallel set and reset...", "Method for resetting an
  array...") that the brief's own exclusion list ("circuit/design...
  patents") argues against including; a smaller number look like
  genuine device/process patents ("Method for determining a
  manufacturing parameter of a resistive random access memory cell",
  "Resistive memory with selector, equipped with a write capacitor")
  and are worth a future, title-by-title pass rather than a blanket
  decision either way.
* **The 12 out-of-scope hits** are recorded in the table below with
  their CPC-based reason rather than silently dropped, so a future
  sweep does not re-examine them from scratch.

## Full family-level triage

One row per distinct DOCDB family found by this sweep (all 211); `Query`
names which assignee-restricted query (or queries) found it. Where a
family already existed in the dataset, its own entry in
`data/patents.yaml`/`docs/references/patents/families.md` is the record
of what it is; this table exists for audit of the *sweep*, not as a
second description of an already-documented family.

| Decision | Query | Family (DOCDB id) | Representative | Year | Title | CPC | Reason |
|---|---|---|---|---|---|---|---|
| added | cypress | 22827270 | US4986878A | 1991 | Process for improved planarization of the passivation layers for semiconductor devices | `H10P14/6681;H10P50/283;H10P95/064;H10W20/092;H10W74/43;Y10S4...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 27012173 | US5443998A | 1995 | Method of forming a chlorinated silicon nitride barrier layer | `H10P95/00` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 22147006 | US6255180B1 | 2001 | Semiconductor device with outwardly tapered sidewall spacers and method for forming same | `H10D30/0227;H10D30/0229;H10P30/22;H10W20/069` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 23689290 | US6172907B1 | 2001 | Silicon-oxide-nitride-oxide-semiconductor (SONOS) type memory cell and method for retaining data in the same | `G11C11/4125;G11C16/0441;H10B69/00;H10D30/69` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 23670081 | US6344281B1 | 2002 | Aluminum metallization method and product | `B32B15/04;H10P14/412;H10W20/065;Y10S428/938;Y10T428/12576;Y1...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 32823649 | US6774452B1 | 2004 | Semiconductor structure having alignment marks with shallow trench isolation | `H10W10/0143;H10W10/17;H10W46/00;H10W46/301;H10W46/501` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 24694701 | US6707112B2 | 2004 | MOS transistor with ramped gate oxide thickness | `H10D30/0221;H10D30/60;H10D64/01336;H10D64/516;H10D64/693;H10...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 36710501 | US7084066B1 | 2006 | Method of uniformly etching refractory metals, refractory metal alloys and refractory metal silicides | `H10P50/267;H10P50/283` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 37526559 | US7151048B1 | 2006 | Poly/silicide stack and method of forming the same | `H10D64/0131;H10D64/01354` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 39743211 | US7425489B1 | 2008 | Self-aligned shallow trench isolation | `H10D84/0151;H10D84/038;H10W10/014;H10W10/17` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 38973874 | US7323377B1 | 2008 | Increasing self-aligned contact areas in integrated circuits using a disposable spacer | `H10D64/021;H10W20/069;H10W20/0698;H10D30/0223;H10D30/60` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 41076959 | US7592661B1 | 2009 | CMOS embedded high voltage transistor | `H10D30/0221;H10D30/603;H10D62/151;H10D62/307;H10D84/0191;H10...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 42358802 | US7768068B1 | 2010 | Drain extended MOS transistor with increased breakdown voltage | `H10D30/0221;H10D30/603;H10D62/116;H10D62/126;H10D62/151` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 43981552 | US7944020B1 | 2011 | Reverse MIM capacitor | `H10D1/692;H10F39/803;H10F39/811;Y10T29/43;Y10T29/435;Y10T29/...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 40071591 | US7880219B2 | 2011 | Nonvolatile charge trap memory device having &amp;lt;100&amp;gt; crystal plane channel orientation | `H10B41/30;H10B69/00;H10D30/6891;H10D30/69;H10D62/405;H10D64/...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 51031728 | US8772057B1 | 2014 | Inline method to monitor ONO stack quality | `H10P74/207` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress | 57705840 | US9543262B1 | 2017 | Self aligned bump passivation | `H10W72/012;H10W72/20;H10W72/90;H10W70/05;H10W70/60;H10W70/66...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress,infineon-llc,spansion | 52808978 | US9466496B2 | 2016 | Spacer formation with straight sidewall | `H10D30/0413;H10D30/69;H10D30/694;H10D30/696;H10D64/037` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress,spansion | 39526963 | US7989328B2 | 2011 | Resistive memory array using P-I-N diode select device and methods of fabrication thereof | `G11C13/0023;G11C13/004;G11C13/0069;G11C13/0097;H10B63/00;H10...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | cypress,spansion | 39047941 | US8232175B2 | 2012 | Damascene metal-insulator-metal (MIM) device with improved scaleability | `H10N70/20;H10N70/066;H10N70/028;H10N70/8833;H10N70/826;H10N7...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | infineon-llc | 73016725 | US11610820B2 | 2023 | Embedded SONOS and high voltage select gate with a high-K metal gate and manufacturing methods of the same | `H10D84/038;H10D84/856;H10B41/49;H10B43/00;H10B43/30;H10B43/4...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | longitude | 65897319 | US11641745B2 | 2023 | Embedded sonos with a high-K metal gate and manufacturing methods of the same | `H10B43/30;H10B43/35;H10B43/40;H10D30/694;H10D64/037;H10P14/6...` | added to data/patents.yaml this round via the PPUBS fallback |
| added | ramtron | 24479530 | US5838605A | 1998 | Iridium oxide local interconnect | `H10B53/00;H10D1/692;H10W20/0698;H10D1/682` | added to data/patents.yaml this round via the PPUBS fallback |
| added | ramtron | 23084824 | US6242299B1 | 2001 | Barrier layer to protect a ferroelectric capacitor after contact has been made to the capacitor electrode | `H10B53/00;H10B53/30;H10D1/682;H10W20/0698` | added to data/patents.yaml this round via the PPUBS fallback |
| in scope, left for later | cypress | 24743931 | US5911887A | 1999 | Method of etching a bond pad | `H10P50/283;H10W72/012;H10W72/251` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 24428538 | US5907784A | 1999 | Method of making multi-layer gate structure with different stoichiometry silicide layers | `C07K7/62;H10D64/0132;H10D64/668` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 25047874 | US6461904B1 | 2002 | Structure and method for making a notched transistor with spacers | `H10D30/0225;H10D64/01324;H10D64/018;H10D84/854;H10D64/01326` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 23341388 | US20020090817A1 | 2002 | Method for selectively etching silicon and/or metal silicides | `H10P50/268` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 33096598 | US6803321B1 | 2004 | Nitride spacer formation | `H10P14/6336;H10P14/6687;H10P50/283;H10W20/069;H10D64/01354;H...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 32823653 | US6773975B1 | 2004 | Formation of a shallow trench isolation structure in integrated circuits | `H10D84/0151;H10D84/038;H10W10/0143;H10W10/17` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 31188927 | US6693042B1 | 2004 | Method for etching a dielectric layer formed upon a barrier layer | `H10P50/283;H10W20/081` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 37863803 | US7192867B1 | 2007 | Protection of low-k dielectric in a passivation level | `H10W20/076;H10W20/081` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 34381269 | US7371637B2 | 2008 | Oxide-nitride stack gate dielectric | `H10D30/60;H10D64/01308;H10D64/664;H10P14/6529;H10P14/69433;H...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 43087275 | US7838937B1 | 2010 | Circuits providing ESD protection to high voltage laterally diffused metal oxide semiconductor (LDMOS) transistors | `H10D8/80;H10D89/713;H10D89/811` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 42669670 | US7791851B1 | 2010 | Cascode combination of low and high voltage transistors for electrostatic discharge circuit | `H10D89/811` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 44261896 | US7981800B1 | 2011 | Shallow trench isolation structures and methods for forming the same | `H10P50/283;H10P50/287;H10P50/692;H10W10/0143;H10W10/17` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 40264143 | US8536640B2 | 2013 | Deuterated film encapsulation of nonvolatile charge trap memory device | `H10D30/0413;H10D30/69;H10D30/694;H10D64/037;H10D64/681` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 48744178 | US8871595B2 | 2014 | Integration of non-volatile charge trap memory devices and logic CMOS devices | `B82Y10/00;H10B43/27;H10B43/30;H10B43/40;H10D30/0227;H10D30/0...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 40752056 | US8860122B1 | 2014 | Nonvolatile charge trap memory device having a high dielectric constant blocking region | `H10D30/0411;H10D30/0413;H10D30/681;H10D30/69;H10D64/035;H10D...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 51296891 | US9018693B2 | 2015 | Deuterated film encapsulation of nonvolatile charge trap memory device | `H10D30/0413;H10D30/6891;H10D30/69;H10D30/693;H10D64/037;H10W...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 49580585 | US9716153B2 | 2017 | Nonvolatile charge trap memory device having a deuterated layer in a multi-layer charge-trapping region | `H10D64/118;H10D64/685;H10D30/0413;H10D30/501;H10D30/62;H10D3...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress | 49777200 | US9564331B2 | 2017 | Apparatus and method for rounded ONO formation in a flash memory device | `H10B43/30;H10D30/0413;H10D30/69;H10D64/037;H10W10/014;H10W10...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,infineon-llc,spansion | 50929933 | US9590079B2 | 2017 | Use disposable gate cap to form transistors, and split gate charge trapping memory cells | `H10B43/30;H10B43/35;H10B43/40;H10D30/0413;H10D30/69;H10D30/6...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,longitude | 48744177 | US9102522B2 | 2015 | Method of ONO integration into logic CMOS flow | `B82Y10/00;H10B43/27;H10B43/30;H10B43/40;H10D30/0413;H10D30/6...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,longitude | 48743336 | US9431549B2 | 2016 | Nonvolatile charge trap memory device having a high dielectric constant blocking region | `H10D30/69;H10D30/691;B82Y10/00;H10B43/20;H10D30/025;H10D30/0...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 39541572 | US7687360B2 | 2010 | Method of forming spaced-apart charge trapping stacks | `H10B43/00;H10B69/00;H10B43/30` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 52825443 | US9508736B2 | 2016 | Three-dimensional charge trapping NAND cell with discrete charge trapping film | `H10B43/27;H10B43/30;H10B43/35;H10D30/0413;H10D30/693;H10P50/...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 52776290 | US9437470B2 | 2016 | Self-aligned trench isolation in integrated circuits | `H10D30/0217;H10D30/023;H10D30/0411;H10D30/0413;H10D30/681;H1...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 54069643 | US9252026B2 | 2016 | Buried trench isolation in integrated circuits | `H10D62/115;H10D62/124;H10D62/832;H10P95/906;H10W10/014;H10W1...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 41726088 | US9236448B2 | 2016 | Method for achieving very small feature size in semiconductor device by undertaking silicide sidewall growth and etching | `H10D30/0221;H10D64/0133;H10D84/0135;H10D84/038;H10D64/015;H1...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 52808963 | US9735289B2 | 2017 | Ion implantation-assisted etch-back process for improving spacer shape and spacer width control | `H10D30/0413;H10D30/69;H10D30/696;H10D64/037;H10P50/268;H10P5...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 51728382 | US9614105B2 | 2017 | Charge-trap NOR with silicon-rich nitride as a charge trap layer | `H10B43/30;H10D30/0413;H10D30/69;H10D64/037;H10D64/693;H10W10...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 50931409 | US9966477B2 | 2018 | Charge trapping split gate device and method of fabricating same | `H10B43/40;H10D30/0413;H10D30/69;H10D30/696` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 50929932 | US9922833B2 | 2018 | Charge trapping split gate embedded flash memory and associated methods | `H10B43/30;H10B43/40;H10D30/0413;H10D30/69;H10D30/696;H10D64/...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | cypress,spansion | 55853538 | US10644016B2 | 2020 | Charge-trapping memory device | `H10B41/30;H10B43/30;H10D30/6891;H10D30/69;H10D30/694;H10D64/...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | infineon-llc | 85479282 | US12622033B2 | 2026 | Method of integrating SONOS into HKMG flow | `H10D64/037;H10B43/35;H10B43/40;H10D30/69;G11C11/5671;G11C16/...` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | ramtron | 22791262 | US5438023A | 1995 | Passivation method and structure for a ferroelectric integrated circuit using hard ceramic materials or the like | `H10W74/147;H10W74/43;Y10S438/958` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | ramtron | 23131786 | US5498569A | 1996 | Layered local interconnect compatible with integrated circuit ferroelectric capacitors | `H10W20/0698` | in scope by CPC and title; not reviewed individually this round (time budget) |
| in scope, left for later | spansion | 36462611 | US7053445B1 | 2006 | Memory device with barrier layer | `H10D30/681;H10D30/6891;H10D30/69;H10D64/037;H10D64/685` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37526574 | US7151293B1 | 2006 | SONOS memory with inversion bit-lines | `H10B43/30;H10B69/00;H10D30/0413;H10D30/69;G11C16/0475` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 36406523 | US7154769B2 | 2006 | Memory device including barrier layer for improved switching speed and data retention | `G11C13/0009;H10N70/245;H10N70/8833;G11C13/0016;H10N70/826;G1...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37526557 | US7151028B1 | 2006 | Memory cell with plasma-grown oxide spacer for reduced DIBL and Vss resistance and increased reliability | `H10D30/0221;H10D30/0411;H10D30/681;H10D62/021;H10D62/292` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 36658629 | US20060256608A1 | 2006 | Resistive memory device with improved data retention and reduced power | `G11C13/0009;G11C13/0069;G11C2213/34;G11C2213/15;G11C2213/12;...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37072391 | US7118967B1 | 2006 | Protection of charge trapping dielectric flash memory devices from UV-induced charging in BEOL processing | `H10D30/0413;H10D30/691;Y10S438/954` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37037238 | US7115469B1 | 2006 | Integrated ONO processing for semiconductor devices using in-situ steam generation (ISSG) process | `H10D64/035;H10D64/037;H10P14/6522;H10P14/6682;H10P14/6309;H1...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 36974476 | US7109555B1 | 2006 | Method for providing short channel effect control using a silicide VSS line | `H10B41/30;H10B69/00` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 36021799 | US7035141B1 | 2006 | Diode array architecture for addressing nanoscale resistive memory arrays | `G11C13/0002;G11C13/0007;G11C13/003;H10B63/20;G11C2213/56;G11...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 36922217 | US7303964B2 | 2007 | Self-aligned STI SONOS | `H10B43/30;H10B43/40;H10B69/00;H10W10/0143;H10W10/17` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 38456873 | US7265014B1 | 2007 | Avoiding field oxide gouging in shallow trench isolation (STI) regions | `H10W10/014;H10W10/17` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 38623372 | US7289351B1 | 2007 | Method of programming a resistive memory device | `G11C11/5685;G11C13/0069;G11C11/16;G11C13/0007;G11C13/0064;G1...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 38607057 | US7286388B1 | 2007 | Resistive memory device with improved data retention | `G11C13/02;G11C13/0069;G11C2013/009;G11C2213/79;G11C2213/56;G...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37068259 | US7259983B2 | 2007 | Page buffer architecture for programming, erasing and reading nanoscale resistive memory devices | `G11C13/0097;G11C13/0064;G11C7/1051;G11C13/0069;G11C7/106;G11...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 34968152 | US7242102B2 | 2007 | Bond pad structure for copper metallization having increased reliability and method for fabricating same | `H10W72/019;H10W70/60;H10W72/923;H10W72/932;H10W72/952;H10W72...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 38157065 | US7232724B1 | 2007 | Radical oxidation for bitline oxide of SONOS | `H10B41/30;H10B69/00` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37886039 | US7196008B1 | 2007 | Aluminum oxide as liner or cover layer to spacers in memory device | `H10B43/30;H10B43/40;H10W20/074` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37526986 | US20070054463A1 | 2007 | Method for forming spacers between bitlines in virtual ground memory array and related structure | `H10B41/30;H10B69/00` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37648745 | US7163860B1 | 2007 | Method of formation of gate stack spacer and charge storage materials having reduced hydrogen content in charge trapping dielectric flash memory device | `H10D30/691;H10D64/037;Y10S438/954` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39734335 | US7423312B1 | 2008 | Apparatus and method for a memory array with shallow trench isolation regions between bit lines for increased process margins | `H10B41/30;H10B69/00;H10D30/683;H10D30/6891;H10D64/685` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39474662 | US7468525B2 | 2008 | Test structures for development of metal-insulator-metal (MIM) devices | `H10P74/273` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40027933 | US20080286921A1 | 2008 | METHODS OF FORMING SILICIDES OF DIFFERENT THICKNESSES ON DIFFERENT STRUCTURES | `H10D30/0213;H10D30/60;H10D64/0131;H10P95/90` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37441108 | US7446369B2 | 2008 | SONOS memory cell having high-K dielectric | `H10D30/69;H10D64/037;H10D64/511;H10D64/685` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39596675 | US7400013B1 | 2008 | High-voltage transistor having a U-shaped gate and method for forming same | `H10D30/605;H10D30/608;H10D64/027;H10D64/513;H10D30/0212` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39474107 | US7384800B1 | 2008 | Method of fabricating metal-insulator-metal (MIM) device with stable data retention | `H10N70/841;H10N70/028;H10N70/8833;H10N70/063;H10N70/20;H10N7...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39310140 | US7361587B1 | 2008 | Semiconductor contact and nitride spacer formation system and method | `H10W20/074;H10W20/076;H10W20/082;H10W20/089;Y10S438/97` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39263523 | US7355886B1 | 2008 | Method of programming, erasing and reading memory cells in a resistive memory array | `G11C13/0007;G11C13/0069;G11C2213/72;G11C2013/009;G11C2213/32...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40364644 | US7495951B1 | 2009 | Resistive memory cell array with common plate | `G11C13/0007;G11C13/0069;H10B63/00;G11C2213/82;G11C2213/79;G1...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40131447 | US7566628B2 | 2009 | Process for making a resistive memory cell with separately patterned electrodes | `H10N70/821;H10N70/021;H10N70/883;H10N70/011;H10N70/023;H10N7...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40635948 | US7534732B1 | 2009 | Semiconductor devices with copper interconnects and composite silicon nitride capping layers | `C23C16/345;H10B41/30;H10B43/30;H10P14/662;H10W20/075;H10W20/...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40244010 | US7691751B2 | 2010 | Selective silicide formation using resist etchback | `H10B43/30;H10B69/00;H10D30/0212;H10P50/73;H10B41/43;H10D64/0...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 42646624 | US7786003B1 | 2010 | Buried silicide local interconnect with sidewall spacers and method for making the same | `H10D64/0112;H10W20/021;H10W20/0698` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 42237573 | US7737019B1 | 2010 | Method for containing a silicided gate within a sidewall spacer in integrated circuit technology | `H10D64/0131;H10D64/017;H10W20/40` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40346939 | US7776688B2 | 2010 | Use of a polymer spacer and Si trench in a bitline junction of a flash memory cell to improve TPD characteristics | `H10B43/30;H10D30/0413;H10D30/691;H10D30/694` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 36614602 | US7675107B2 | 2010 | Non-volatile SONOS-type memory device | `H10B43/30;H10B69/00;H10D30/0413;H10D30/69;H10D64/037` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40966514 | US7838406B2 | 2010 | SONOS-NAND device having a storage region separated between cells | `H10B43/10;H10B43/30;H10D30/0413;H10D64/037` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40562595 | US7829936B2 | 2010 | Split charge storage node inner spacer process | `H10B43/30;H10B69/00;H10D30/691;H10D30/696;H10D64/037` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40501100 | US7825448B2 | 2010 | U-shaped SONOS memory having an elevated source and drain | `H10B43/30;H10D30/0413;H10D30/69` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39541585 | US7713875B2 | 2010 | Variable salicide block for resistance equalization in an array | `H10B43/30;H10B69/00;H10D30/691;H10D64/037;H10W20/098` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 37395764 | US7704878B2 | 2010 | Contact spacer formation using atomic layer deposition | `H10W20/076;H10W20/081` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40582592 | US7706168B2 | 2010 | Erase, programming and leakage characteristics of a resistive memory device | `H10N70/028;H10N70/20;H10N70/8833;G11C13/0007;H10N70/826;G11C...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 41819493 | US7679129B1 | 2010 | System and method for improving oxide-nitride-oxide (ONO) coupling in a semiconductor device | `H10B41/30;H10D30/0411;H10D64/035` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39203201 | US7646624B2 | 2010 | Method of selecting operating characteristics of a resistive memory device | `H10N70/028;G11C13/0007;H10N70/826;H10N70/25;H10N70/8833;H10B...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40997420 | US8035099B2 | 2011 | Diode and resistive memory device structures | `H10B63/20;H10B63/84;H10N70/20;H10N70/826;H10N70/841` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39582589 | US7879718B2 | 2011 | Local interconnect having increased misalignment tolerance | `H10B41/30;H10B41/35;H10B43/30;H10B69/00;H10W20/069;H10W20/06...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40501101 | US8076206B2 | 2011 | Method for manufacturing SONOS flash memory | `H10B43/30;H10D30/0413;H10D30/69` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40581713 | US7883963B2 | 2011 | Split charge storage node outer spacer process | `H10B43/30;H10B69/00;H10D30/691;H10P50/71;H10P76/4085;H10P76/...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39323899 | US7948052B2 | 2011 | Dual-bit memory device having trench isolation material disposed near bit line contact areas | `H10B43/30;H10B69/00;H10D89/10` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 42264741 | US7943983B2 | 2011 | HTO offset spacers and dip off process to define junction | `H10B43/30;H10D30/0413;H10D84/0133;H10D84/038` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39475534 | US7916523B2 | 2011 | Method of erasing a resistive memory device | `G11C13/0097;G11C13/0069;G11C13/0007;G11C2213/79;G11C2013/007...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40611363 | US7910980B2 | 2011 | Sonos device with insulating storage layer and P-N junction isolation | `H10B43/30;H10B43/10` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40382576 | US7902056B2 | 2011 | Plasma treated metal silicide layer formation | `H10B41/30;H10B69/00;H10D30/0212;H10D64/0112;H10W20/081` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39475529 | US7894243B2 | 2011 | Methods of programming and erasing resistive memory devices | `G11C13/0007;G11C13/0069;G11C2213/32;G11C2013/009` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39543437 | US7888218B2 | 2011 | Using thick spacer for bitline implant then remove | `H10B69/00;H10B43/30` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39541570 | US7863175B2 | 2011 | Zero interface polysilicon to polysilicon gate for flash memory | `H10B41/40;H10B41/42;H10D64/035;H10P70/27` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 45419095 | US8093680B1 | 2012 | Metal-insulator-metal-insulator-metal (MIMIM) memory device | `H10N70/25;G11C13/0007;H10N70/8833` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 44655377 | US8202779B2 | 2012 | Methods for forming a memory cell having a top oxide spacer | `H10D64/037;H10D30/69;H10B43/30` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 46234933 | US8263458B2 | 2012 | Process margin engineering in charge trapping field effect transistors | `H10W10/0145;H10W10/17;H10B43/35;H10D30/69;H10D64/037` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39274367 | US8143661B2 | 2012 | Memory cell system with charge trap | `H10B43/30;H10B69/00;H10D30/69;H10D64/035` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 45556444 | US8114756B1 | 2012 | Method and manufacture for high voltage gate oxide formation after shallow trench isolation formation | `H10B43/40;H10D84/0144;H10D84/038;H10W10/014;H10W10/17;H10B41...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39475426 | US8093698B2 | 2012 | Gettering/stop layer for prevention of reduction of insulating oxide in metal-insulator-metal device | `H01G4/224;H10B63/22;H10D1/68;H10W76/48` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39476348 | US8089113B2 | 2012 | Damascene metal-insulator-metal (MIM) device | `H10N70/20;H10N70/8833;H10N70/826;H10N70/821;H10N70/061;H10B6...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 46234943 | US8461053B2 | 2013 | Self-aligned NAND flash select-gate wordlines for spacer double patterning | `H10B41/10;H10B41/35;H10B43/10;H10B43/35;H10P50/00;H10P50/71;...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 40582507 | US8445913B2 | 2013 | Metal-insulator-metal (MIM) device and method of formation thereof | `H01G13/00;H01G4/10;H10D1/68;H10D1/688;H10B20/00;Y10T29/435` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 42130337 | US8404549B2 | 2013 | Fabricating method of mirror bit memory device having split ONO film with top oxide film formed by oxidation process | `H10B43/30;H10D30/69;H10D30/691;H10D30/697;H10D64/037` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 38608845 | US8587049B2 | 2013 | Memory cell system with charge trap | `H10B43/00;H10B43/30;H10B69/00;H10D30/69;H10D64/037;H10D64/68...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 42225015 | US8551858B2 | 2013 | Self-aligned SI rich nitride charge trap layer isolation for charge trap flash memory | `H10B43/30;H10D30/69;H10D64/037;H10W10/014;H10W10/17` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 47556056 | US8598005B2 | 2013 | Method and manufacture for embedded flash to achieve high quality spacers for core and high voltage devices and low temperature spacers for high performance logic devices | `H10B43/40;H10D64/021;H10D64/037;H10D84/013;H10D84/0147;H10D8...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 46379999 | US8441063B2 | 2013 | Memory with extended charge trapping layer | `H10D30/69;H10D30/694;H10D64/037;H10B43/30` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 46162631 | US8349685B2 | 2013 | Dual spacer formation in flash memory | `H10B43/40;H10B43/35` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 51901766 | US8896048B1 | 2014 | Apparatus and method for source side implantation after spacer formation to reduce short channel effects in metal oxide semiconductor field effect transistors | `H10D30/0221;H10D30/0411;H10D30/681` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 50432072 | US8836012B2 | 2014 | Spacer design to prevent trapped electrons | `H10B41/35;H10D30/0411` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 50728316 | US8835277B2 | 2014 | Method to improve charge trap flash memory core cell performance and reliability | `H10B43/30;H10D30/0413;H10D30/69;H10D30/694;H10D64/037;H10D64...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 50929927 | US8816438B2 | 2014 | Process charging protection for split gate charge trapping flash | `H10B43/35;H10B43/40;H10D30/69;H10D30/696;H10D89/921;H10B43/0...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 51222001 | US20140210012A1 | 2014 | Manufacturing of FET Devices Having Lightly Doped Drain and Source Regions | `H10B43/30;H10B43/40;H10D30/0227;H10D64/037;H10D84/017;H10D84...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 44354058 | US8790530B2 | 2014 | Planar cell ONO cut using in-situ polymer deposition and etch | `H10B43/10;H10B43/30` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 50929928 | US20140167136A1 | 2014 | Charge Trapping Device with Improved Select Gate to Memory Gate Isoloation | `H10D30/0413;H10D30/69;H10D30/696` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 43029745 | US8742496B2 | 2014 | Sonos memory cells having non-uniform tunnel oxide and methods for fabricating same | `H10B43/30;H10D30/69;H10D30/699` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 50773659 | US20140148009A1 | 2014 | Forming a Substantially Uniform Wing Height Among Elements in a Charge Trap Semiconductor Device | `H10B43/30;H10D64/037;H10P95/08` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 54539205 | US20150333188A1 | 2015 | TILTED IMPLANT FOR POLY RESISTORS | `H10D1/43;H10D1/47;H10P30/204;H10P30/21;H10P30/221;H10P30/222` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 54018154 | US20150255480A1 | 2015 | Method to Improve Charge Trap Flash Memory Top Oxide Quality | `H10B43/10;H10B43/30;H10D30/0413;H10D30/69;H10D30/694;H10D62/...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 53495834 | US20150194537A1 | 2015 | MULTI-LAYER INTER-GATE DIELECTRIC STRUCTURE | `H10D30/0413;H10D30/69;H10D30/696;H10D64/037` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 50773660 | US8975185B2 | 2015 | Forming charge trap separation in a flash memory semiconductor device | `H10D30/694;H10D64/037;H10P72/0462;H10P72/0468;H10B43/30` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 52776279 | US20150097224A1 | 2015 | BURIED TRENCH ISOLATION IN INTEGRATED CIRCUITS | `H10D84/0151;H10D84/038;H10W10/014;H10W10/17;H10D84/83` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | spansion | 39761810 | US8994093B2 | 2015 | Semiconductor device with ONO film | `H10B43/30;H10B69/00;H10D30/691;H10D30/699;H10D64/037;H10D64/...` | Spansion-original; needs the same per-family lineage care as M4 before adding (time budget) |
| in scope, left for later | weebit | 79292686 | US11538524B2 | 2022 | Silicon over insulator two-transistor two-resistor in-series resistive memory cell | `G11C13/0026;G11C13/0028;G11C13/0069;G11C13/004;G11C2213/74;G...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 79292795 | US11659720B2 | 2023 | Silicon over insulator two-transistor one-resistor in-series resistive memory cell | `G11C13/004;G11C13/0069;H10B63/30;H10D86/201;G11C2213/74;G11C...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 82495765 | US12040017B2 | 2024 | Current and voltage limit circuitry for resistive random access memory programming | `G11C13/0069;H10B63/00;G11C2013/0071;G11C2013/0078` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 69061233 | US12165706B2 | 2024 | Method for resetting an array of resistive memory cells | `G11C13/0033;G11C13/0069;G11C13/0097` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 85706587 | US12131777B2 | 2024 | Resistive random-access memory (ReRAM) cell optimized for reset and set currents | `G11C13/0028;G11C13/0064;G11C13/0097;G11C13/0069;G11C13/0026;...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 80933811 | US12119059B2 | 2024 | Write method for differential resistive memories | `G11C29/52;G11C13/0069;G11C13/004;G11C2213/74;G11C2213/79` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 76283589 | US12087360B2 | 2024 | Method for programming an array of resistive memory cells | `G11C13/0069;G11C13/0035;G11C13/0064;G11C2013/0071;G11C2013/0...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 83116320 | US12068028B2 | 2024 | Circuitry for parallel set and reset of resistive random-access memory (ReRAM) cells | `G11C13/004;G11C13/0038;G11C13/0069;G11C13/0097;G11C13/0064;G...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 75438899 | US12052876B2 | 2024 | Memory comprising a matrix of resistive memory cells, and associated method of interfacing | `G11C13/0004;G11C13/003;G11C13/004;G11C13/0061;H10B63/84;H10N...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 69061234 | US12033698B2 | 2024 | Method for resetting an array of resistive memory cells | `G11C13/0097;G11C13/004;G11C13/0033` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 97838881 | US20250372165A1 | 2025 | SYSTEM AND METHODS FOR SMART BINNING AND HEALING PROGRAMMING OF RESISTIVE RANDOM-ACCESS MEMORIES (RERAMS) | `G11C13/0069;G11C2013/0076` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 92456560 | US20250322872A1 | 2025 | Resistive Random-Access Memory With Reduced Disturb Current in a Shared Source Line Bit Cell Architecture | `G11C13/003;G11C13/0033;G11C11/1655;G11C11/1659;G11C11/1673;G...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 80595187 | US12406724B2 | 2025 | Resistive memory with selector, equipped with a write capacitor, and associated writing method | `G11C13/0061;G11C11/1697;G11C11/1659;G11C13/0038;G11C11/1675;...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 68138409 | US12224007B2 | 2025 | Method for determining a manufacturing parameter of a resistive random access memory cell | `H10N70/826;H10N70/026;H10N70/20;G11C13/0069;H10N70/883;H10N7...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 91896531 | US20260221185A1 | 2026 | RESISTIVE RANDOM-ACCESS MEMORY (RERAM) CONFIGURED FOR OVERCOMING THE AFFECTS OF READ DISTURB | `G11C13/0033;G11C13/004;G11C13/0061;G11C13/0064;G11C13/0069;G...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 94172955 | US20260088086A1 | 2026 | Programming of the High Resistive State of a Resistive Memory Element | `G11C13/0069;G11C13/0007;G11C13/0028;G11C13/004;G11C13/0064;G...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| in scope, left for later | weebit | 98472343 | US20260031143A1 | 2026 | SYSTEM AND METHOD FOR REDUCTION OF TIME-DEPENDENT DIELECTRIC BREAKDOWN (TDDB) OF UNSELECTED TRANSISTORS OF A RESISTIVE RANDOM-ACCESS MEMORY (RERAM) DEVICE | `G11C13/0026;G11C13/0069;G11C13/0028;G11C13/003;G11C13/004;G1...` | Weebit ReRAM; mostly circuit programming/read-write scheme, needs per-title review (time budget) |
| out of scope | cypress | 24566551 | US5821770A | 1998 | Option decoding with on-chip electrical fuses | `H03K19/1733` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 24698376 | US6249177B1 | 2001 | Method, circuit and/or architecture for reducing gate oxide stress in low-voltage regulated devices | `H03L7/06` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 26868539 | US6417696B1 | 2002 | Interface circuit for mixed voltage I/O buffer to provide gate oxide protection | `H03K19/00315` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 25399480 | US6532169B1 | 2003 | SONOS latch and application | `G11C16/24;G11C16/28;G11C14/00` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 39484406 | US7385793B1 | 2008 | Cascode active shunt gate oxide project during electrostatic discharge event | `H02H9/046` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 40072247 | US20080291732A1 | 2008 | Three cycle SONOS programming | `G11C16/3477;G11C16/3468;G11C16/16;G11C16/0466` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 39583704 | US7710776B2 | 2010 | Method for on chip sensing of SONOS V.sub.T window in non-volatile static random access memory | `G11C16/26` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 44350795 | US7995397B1 | 2011 | Power supply tracking single ended sensing scheme for SONOS memories | `G11C16/28;G11C16/08;G11C11/5642` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 49181495 | US8542514B1 | 2013 | Memory structure having SRAM cells and SONOS devices | `G11C14/0063;G11C14/0054;G11C5/06` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 56136458 | US9378821B1 | 2016 | Endurance of silicon-oxide-nitride-oxide-silicon (SONOS) memory cells | `G11C16/10;G11C16/0466;G11C16/14;G11C16/12;G11C14/0063` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | cypress | 44353987 | US9274410B2 | 2016 | Method and system for automated generation of masks for spacer formation from a desired final wafer pattern | `G03F1/62;G03F1/70` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| out of scope | spansion | 36498862 | US7130210B2 | 2006 | Multi-level ONO flash program algorithm for threshold width control | `G11C11/5671;G11C16/16` | CPC class is circuit/protection/EDA, not semiconductor process or device fabrication |
| already present | cypress | 24244177 | US5965924A | 1999 | Metal plug local interconnect | `H10W20/40;Y10S257/903` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 25130177 | US6593208B1 | 2003 | Method of uniform polish in shallow trench isolation process | `H10W10/0145;H10W10/17;H10P95/062;H10P95/066` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 29778448 | US6677213B1 | 2004 | SONOS structure including a deuterated oxide-silicon interface and method for making the same | `H10D30/69;H10D64/01338;H10D64/01342;H10D64/01344;H10D64/037;...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 33476239 | US6828201B1 | 2004 | Method of manufacturing a top insulating layer for a sonos-type device | `H10B43/30;H10B69/00` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 33449343 | US6825544B1 | 2004 | Method for shallow trench isolation and shallow trench isolation structure | `H10W10/0147;H10W10/17` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 31979047 | US6818558B1 | 2004 | Method of manufacturing a dielectric layer for a silicon-oxide-nitride-oxide-silicon (SONOS) type devices | `H10B43/30;H10B69/00;H10D30/682;H10D30/6893` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 24310003 | US6784552B2 | 2004 | Structure having reduced lateral spacer erosion | `H10D84/0133;H10D84/0149;H10D84/038;H10W20/031;H10W20/069;H10...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 32823623 | US6774033B1 | 2004 | Metal stack for local interconnect layer | `H10P14/412;H10W20/0698` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 35465546 | US6977217B1 | 2005 | Aluminum-filled via structure with barrier layer | `H10W20/033` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 41115772 | US7799670B2 | 2010 | Plasma oxidation of a memory layer to form a blocking layer in non-volatile charge trap memory devices | `H10D30/69;H10D30/694;H10D64/037` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 40072821 | US7670963B2 | 2010 | Single-wafer process for fabricating a nonvolatile charge trap memory device | `H10D30/694;H10D64/037;H10P14/6328;H10D30/0413;H10P14/662;Y10...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 45034384 | US8071453B1 | 2011 | Method of ONO integration into MOS flow | `H10B43/30;H10B43/40;H10D30/69;H10D64/037;H10W20/01` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 44994327 | US8067284B1 | 2011 | Oxynitride bilayer formed using a precursor inducing a high charge trap density in a top layer of the bilayer | `H10D30/69;H10D64/037;H10D64/685;H10P14/6334;H10P14/662;H10P1...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 39541580 | US8222111B1 | 2012 | Simultaneous formation of a top oxide layer in a silicon-oxide-nitride-oxide-silicon (SONOS) transistor and a gate oxide in a metal oxide semiconductor (MOS) | `H10B43/30;H10D64/693;H10D30/69;H10B43/40;H10D64/685;H10D64/6...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 41681547 | US8163660B2 | 2012 | SONOS type stacks for nonvolatile change trap memory devices and methods to form the same | `H10D30/69;H10D64/685;H10D64/037;H10D30/694;H10D30/0413` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 40072822 | US8283261B2 | 2012 | Radical oxidation process for fabricating a nonvolatile charge trap memory device | `H10D64/037;H10D30/694;H10P14/6328;H10P14/662;H10D30/0413;H10...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 40072804 | US8093128B2 | 2012 | Integration of non-volatile charge trap memory devices and logic CMOS devices | `H10B43/30;H10B43/40;H10D30/0227;H10D30/601;H10D30/605;H10D30...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 41115802 | US8088683B2 | 2012 | Sequential deposition and anneal of a dielectic layer in a charge trapping memory device | `H10D64/037;H10P14/6529;H10P14/662;H10P14/69215;H10P14/6927` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 40071593 | US8614124B2 | 2013 | SONOS ONO stack scaling | `H10D30/69;H10D30/694;H10D64/037;H10D64/661;H10D64/683;H10D64...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 48952138 | US8513753B1 | 2013 | Photodiode having a buried well region | `H10F30/221;H10F39/812;H10F77/14;H10F39/8027` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 40071592 | US8680601B2 | 2014 | Nonvolatile charge trap memory device having a deuterated layer in a multi-layer charge-trapping region | `H10D30/0413;H10D30/69;H10D64/037;H10D64/685` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 52101816 | US8916432B1 | 2014 | Methods to integrate SONOS into CMOS flow | `H10B43/00;H10B43/40;H10D30/0223;H10D30/0413;H10D30/69;H10D30...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 51229009 | US8796098B1 | 2014 | Embedded SONOS based memory cells | `H10B43/30;H10B43/35;H10B43/40;H10D30/0413;H10D30/69;H10D30/6...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 48743334 | US8772059B2 | 2014 | Inline method to monitor ONO stack quality | `H10D30/0413;H10D30/69;H10P74/207` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 48743335 | US8710578B2 | 2014 | SONOS stack with split nitride memory layer | `B82Y10/00;H10D30/62;H10D30/69;H10D30/693;H10D64/037;H10D64/6...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 53939072 | US9123642B1 | 2015 | Method of forming drain extended MOS transistors for high voltage circuits | `H10D30/0221;H10D30/0281;H10D30/603;H10D84/017;H10D84/038;H10...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress | 52707807 | US8993457B1 | 2015 | Method of fabricating a charge-trapping gate stack using a CMOS process flow | `H10B43/30;H10B43/40;H10D30/0413;H10D30/69;H10D30/694;H10D64/...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress,longitude | 46465479 | US8222688B1 | 2012 | SONOS stack with split nitride memory layer | `H10D64/037;G11C16/04;H10B43/00;H10D30/69;H10D30/694;H10D64/6...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress,longitude | 48945910 | US8685813B2 | 2014 | Method of integrating a charge-trapping gate stack into a CMOS flow | `H10B43/10;H10B43/30;H10B43/40;H10D30/69;H10D64/037;H10D64/66...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress,longitude | 49581632 | US8940645B2 | 2015 | Radical oxidation process for fabricating a nonvolatile charge trap memory device | `B82Y10/00;H10D30/0413;H10D30/43;H10D30/693;H10D30/694;H10D62...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress,longitude | 54848024 | US9218978B1 | 2015 | Method of ONO stack formation | `H10B43/00;H10B43/30;H10B43/40;H10D30/0413;H10D30/69;H10D30/6...` | matches an existing family (by member number or DOCDB family id) |
| already present | cypress,longitude | 49580623 | US9299568B2 | 2016 | SONOS ONO stack scaling | `H10D30/0413;H10D30/69;H10D62/40;H10D62/83;H10D64/037;H10D64/...` | matches an existing family (by member number or DOCDB family id) |
| already present | infineon-llc | 65016688 | US12029041B2 | 2024 | Method of forming high-voltage transistor with thin gate poly | `H10B41/30;H10B41/49;H10B43/30;H10B43/35;H10B43/40;H10D30/022...` | matches an existing family (by member number or DOCDB family id) |
| already present | longitude | 63208150 | US10784356B2 | 2020 | Embedded sonos with triple gate oxide and manufacturing method of the same | `H10B43/30;H10B43/40;H10D30/0413;H10D30/69;H10D64/037;H10P14/...` | matches an existing family (by member number or DOCDB family id) |
| already present | spansion | 26708682 | US7439141B2 | 2008 | Shallow trench isolation approach for improved STI corner rounding | `H10W10/0147;H10W10/17` | matches an existing family (by member number or DOCDB family id) |
| already present | weebit | 74192490 | US20220122660A1 | 2022 | CONFIGURATION AND METHOD OF OPERATION OF A ONE-TRANSISTOR TWO-RESISTORS (1T2R) RESISTIVE MEMORY (RERAM) CELL AND AN ARRAY THEREOF | `G11C13/0007;G11C13/0069;G11C13/0097;G11C13/004;G11C13/003;G1...` | matches an existing family (by member number or DOCDB family id) |
| already present | weebit | 90721530 | US12414485B2 | 2025 | Method for manufacturing an OxRAM-type resistive memory cell and associated OxRAM-type memory cell | `H10N70/826;H10N70/841;H10B63/00;H10N70/011;H10N70/043;H10N70...` | matches an existing family (by member number or DOCDB family id) |
| already present | weebit | 68072713 | US12349605B2 | 2025 | Method for manufacturing an OxRAM type resistive memory cell | `G11C13/0002;G11C13/0007;G11C13/0011;H10B63/80;H10N70/026;H10...` | matches an existing family (by member number or DOCDB family id) |
| already present | weebit | 69743400 | US12349609B2 | 2025 | Low forming voltage OxRAM memory cell, and associated method of manufacture | `H10N70/063;H10N70/24;H10N70/826;H10N70/841;H10N70/8833;H10N7...` | matches an existing family (by member number or DOCDB family id) |
