# Progress: fixing the paired reviews of steps 001–013 on `topic/p4-001-013`

Source reviews: `tmp/p4/review-001-013-B.md` (primary; 1 High, 7 Medium,
38 Low) and `tmp/p4/review-001-013-A.md` (2 Low only — both duplicates of
findings B already lists, so tracked against B's ids). Work order: High,
then Medium, then Low, one finding or closely-related group per commit.
Status values: open / fixed / declined.

## High

| Finding | Page(s) | Status | Note |
|---|---|---|---|
| 006-H1 | 006-stie, 089-psg, overview/index, materials/index, references/public-sources | open | re-derive trench depth from the drawing's own dimension labels myself before writing |

## Medium

| Finding | Page(s) | Status | Note |
|---|---|---|---|
| 001-M1 | 001-smat | open | body-doping extraction attributed to wrong device |
| 003-M1 | 003-isonit | open | nitride thickness lower bound unsupported |
| 004-M1 | 004-fom | open | diff/tap -> cfom stated as fact, not inference |
| 008-M1 | 008-dni | open | straggle claim wrong/uncited |
| 009-M1 | 009-dnis | open | uncited furnace temperature |
| 011-M1 | 011-filox | open | fill-thickness arithmetic self-inconsistent |
| 013-M1 | 013-ns19 | open | VGH-1967 quotation unverifiable/probably not verbatim |

## Low

| Finding | Page(s) | Status | Note |
|---|---|---|---|
| 001-L1 (= review A 001-L1) | 001-smat | open | CYP-07 needs Wayback snapshot |
| 001-L2 | 001-smat | open | JOB-01 unarchived, add note |
| 001-L3 | 001-smat | open | RCA temp range vs "75 or 80 C" |
| 001-L4 | 001-smat | open | optional SC-2/HF material links |
| 002-L1 | 002-box | open | non-verbatim US 7,439,141 quote |
| 002-L2 | 002-box, 006-stie | open | AmberWave strained-Si/SiGe qualifier |
| 002-L3 | 002-box | open | Deal-Grove vs thin-regime contradiction |
| 002-L4 | 002-box | open | pad oxide given nitride's screening job |
| 003-L1 | 003-isonit | open | US 2009/0179253 is oxynitride not nitride |
| 003-L2 | 003-isonit | open | unmarked inference nitride thickness -> FOXSTEP |
| 004-L1 (= review A 004-L1) | 004-fom | open | BARC quote scope qualifier dropped |
| 004-L2 | 004-fom | open | cfom 23:0 mask-level layer omitted |
| 004-L3 | 004-fom | open | ZeptoBars hedge quoted as certain |
| 004-L4 | 004-fom | open | FOMCD/FOMCDSP not mentioned |
| 004-L5 | 004-fom, masks/index | open | "30-odd" vs "36" mask steps |
| 005-L1 | 005-stinite | open | "originally designed for polysilicon" overstated |
| 005-L2 | 005-stinite | open | nitride sidewall claim mis-cited to Thung |
| 005-L3 | 005-stinite | open | optional: add page numbers/move support to papers |
| 006-L1 | 006-stie | open | ITRS paraphrase overstated; cite Thung instead |
| 006-L2 | 006-stie | open | HDP-void quote clipped/one step removed |
| 006-L3 | 006-stie, 009-dnis | open | tool name spelling vs SkyWater's own |
| 007-L1 | 007-dnm | open | resist thickness: use patent number not book |
| 007-L2 | 007-dnm | open | "~0.3 µm topography" inherits 006-H1 |
| 007-L3 | 007-dnm | open | "deliberate trade" overstated |
| 008-L1 | 008-dni | open | Axcelis quote attributed to wrong product line |
| 008-L2 | 008-dni | open | Bourdelle conclusion not in abstract |
| 008-L3 | 008-dni | open | uncited P-vs-As preference |
| 009-L1 | 009-dnis, 006-stie | open | same as 006-L3, one fix |
| 009-L2 | 009-dnis | open | crust claim cite primary sources too |
| 010-L1 | 010-linox | open | Lattice figure is thickened 90nm-node liner |
| 010-L2 | 010-linox | open | Spansion/Cypress lineage caveat placement |
| 011-L1 | 011-filox | open | Nishimura numbers unverifiable, mark or drop |
| 011-L2 | 011-filox | open | Wikipedia [citation needed] sentence needs Nguyen cite |
| 011-L3 | 011-filox | open | Trikon Flowfill is IMD tool not STI-fill |
| 012-L1 | 012-cmpnit | open | slurry selectivity numbers unverifiable, mark |
| 012-L2 | 012-cmpnit | open | REB quote source describes LOCOS not STI |
| 012-L3 | 012-cmpnit | open | uncited topography figure, tie to FILOX |
| 013-L1 | 013-ns19 | open | nitride list omits GATENIT |

## Cross-page conflicts (from B's summary, resolved as part of the above)

X1/X2 -> 006-H1; X3 -> 004-L2; X4 -> 004-M1; X5 -> 004-L5; X6 -> 006-L3/009-L1; X7 -> 003-M1; X8 -> 004-L4.
