(overview-sky130b-reram)=
# The sky130B ReRAM tier

The open-source SKY130 process design kit is distributed in two
variants. `sky130A` is the base process that the step pages of this
reference describe; `sky130B` adds an optional resistive memory
({term}`ReRAM`, also written RRAM) between the first and second metal
levels. The open_pdks build scripts say so in as many words:
"sky130B = 5-metal backend stack with dual MiM and ReRAM", and "ReRAM
support is what distinguishes variant B from variant A".[^opdks-makefile]
The variant has existed since open_pdks version 1.0.269.[^opdks-readme]
SkyWater's own description of the device is a separate documentation
set and library, `sky130_fd_pr_reram`, marked "SkyWater Provided" and
"Initial documentation only release", which states that "a HfO2-based
RRAM layer is fabricated within the BEOL process" and that "This
technology is still under development".[^reram-background]

A ReRAM cell is a {term}`metal–insulator–metal <MiM capacitor>`
sandwich: SkyWater's documentation describes the typical device as a
metal-oxide switching layer "sandwiched by top and bottom metal
electrodes, forming a two-terminal metal-insulator-metal (MIM)
structure".[^reram-background] What the cell stores is not charge but a
resistance, set and reset by voltage pulses. Structurally it is a
relative of the MiM capacitor that SKY130 builds over metal 3
({ref}`CAPILD <step-135>` to {ref}`CAPME <step-138>`): a thin dielectric
between two conductors, inserted into the {term}`BEOL` with an extra
mask. What differs is that the ReRAM stack sits on a via rather than on
a metal plate, and needs a second via level above it.

This module is not part of the 171-step list used in this reference
({ref}`steps-index`), which contains no steps for it.[^steps-sheet] This page
therefore describes the tier as a module: where it sits in the stack,
what the public PDK files say about its layers and masks, how a tier of
this kind is typically built, and what it changes for the rest of the
flow. Two related public statements should be kept apart from it.
SkyWater and Weebit Nano announced Weebit's ReRAM IP "in SkyWater's
130nm CMOS (S130) process", with a photograph captioned "Weebit ReRAM
bitcell is shown integrated into the S130 technology between Metal1 and
Metal2";[^skw-04] and IEEE Spectrum reported in 2018 that SkyWater would
develop a production process flow for a DARPA-funded project based on
technology that allows "carbon nanotube transistors and resistive RAM
memory to be built on top of ordinary CMOS logic chips".[^press-05]
Whether either uses the same process module as `sky130_fd_pr_reram` is
not stated publicly.

## Where the tier sits

SkyWater's user-guide slides are titled "RRAM between met1/met2". They
divide the stack into a front end "same as SKY130 PDK (met1 and
everything below)", an "RRAM tier In between met1 & met2", and a back
end "same as SKY130 PDK (met2 and everything above)".[^reram-ug] In the
drawing, a via from metal 1 lands on the RRAM bottom electrode, the
RRAM oxide and the top electrode follow, and a second via connects the
top electrode to metal 2; beside it, an "RRAM bypass (2 stacked normal
vias: 2x via thickness, same via width & spacing)" connects metal 1 to
metal 2 where there is no cell.[^reram-ug]

The place-and-route tech-file slide gives the vertical stack as
thicknesses and levels above the substrate (µm).[^reram-ug] The last
column compares the `sky130A` levels of the PDK's process stack
diagram.[^pdk-04]

| Layer (tech-file name) | sky130B bottom → top | Thickness | sky130A bottom → top |
|------------------------|----------------------|-----------|----------------------|
| `met1` | 1.3761 → 1.7361 | 0.360 | 1.3761 → 1.7361 |
| `via_bot` (lower part of `via`) | 1.7361 → 2.0061 | 0.270 | `via1` 1.7361 → 2.0061 (0.27) |
| `rr1_bot_electrode` | 2.0061 → 2.0161 | 0.010 | — |
| `rr1_oxide` ("not in .ict"; dielectric constant 10) | 2.0161 → 2.0211 | 0.005 | — |
| `rr1_top_electrode` | 2.0211 → 2.0311 | 0.010 | — |
| `via_top` (upper part of `via`) | 2.0311 → 2.3011 | 0.270 | — |
| `met2` | 2.3011 → 2.6611 | 0.360 | 2.0061 → 2.3661 |

The same slide gives `via` as a whole as 0.565,[^reram-ug] which equals
`via_bot` 0.270 plus `via_top` 0.270 plus the 0.025 of the three RRAM
layers (our arithmetic). The open_pdks Magic technology file uses the same
numbers for its `sky130B` extraction: via 1 at 1.7361 µm with thickness
0.565 µm and metal 2 at 2.3011 µm, against 0.27 µm and 2.0061 µm without
ReRAM.[^opdks-magic-tech] The oxide thickness agrees with the default
`Tox` of 5.0e-9 m in SkyWater's Verilog-A cell model.[^reram-cell]
Whether the tech-file thicknesses are physical film thicknesses or
values chosen for extraction and routing is not stated; the dielectric
constant of 10 given for the oxide is lower than the "4–6 times" that of
SiO₂ quoted for hafnium oxide,[^wiki-hfo2] and the slide marks the
oxide as "not in .ict", the file whose layers its table
lists.[^reram-ug]

Two readings follow from the table, and they fix where the module would
sit in this reference's sequence. First, the lower via ends at
2.0061 µm, the level at which metal 2 begins in the base stack, and has
the base via-1 height of 0.27 µm:[^pdk-04] the lower half of the sky130B
via is, on our reading, the ordinary via-1 level, built as in
{ref}`VIM <step-118>` to {ref}`WCMP3 <step-122>`. Second, the RRAM
electrodes are deposited on top of that level, so the lower vias must
already be etched, filled and polished flat before a 25 nm film stack
can be laid on them (inference from the geometry). The tier therefore
belongs after the via-1 plug polish ({ref}`WCMP3 <step-122>`) and before
the metal-2 stack deposition ({ref}`TIAL12 <step-123>`): the RRAM stack,
its patterning and encapsulation, a second inter-level dielectric of
about 0.295 µm (0.27 µm above the top electrode; our arithmetic), and
the upper vias would all be inserted there, and metal
2 and everything above it would then be built 0.295 µm higher
(2.3011 − 2.0061 µm; our arithmetic from the two stacks).

SkyWater's background page adds that the RRAM layer is fabricated "at
multiple points as described in the physical design rules", and the
layer-description slide in the library repository calls the cell the
"RRAM tier1 cell";[^reram-background][^reram-layers] the published
sky130B material describes only the tier between metal 1 and metal 2.

## Drawn layers and mask layers

SkyWater's slides distinguish *drawn layers* ("used by the designer")
from *mask layers* ("corresponding to physical photomasks"). A slide in
the library repository that the rendered user guide omits tabulates
them:[^reram-layers]

| PDK layer | Drawn | Mask | SkyWater's function text |
|-----------|-------|------|--------------------------|
| `met1` | ✓ | – | "this is the interconnect layer directly beneath the RRAM" |
| `via` | ✓ | – | "defines both top & bottom contacts to RRAM cell (when via is enclosed by r1c), or connects met1 and met2 (when via is not enclosed by r1c)" |
| `cviam` | – | ✓ | "defines bottom part of contacts to RRAM cell … or defines bottom part of connection between met1 and met2" |
| `r1c` | ✓ | ✓ | "RRAM cell": "defines RRAM cell between met1 and met2." |
| `r1v` | – | ✓ | "RRAM via": "defines top part of contacts to RRAM tier1 cell … or defines top part of connection between met1 and met2" |
| `met2` | ✓ | – | "this is the interconnect layer directly above the RRAM" |

Three statements in the slides settle how the cell is described to the
mask shop. The bottom electrode, oxide and top electrode "are defined by
the same layer (r1c)"; "Both top & bottom parts of RRAM vias are drawn
on a single PDK layer, which is separated during mask generation"; and,
on the tech-file slide, "drawn layer "via" defines both "via_bot" and
"via_top" when "via" is enclosed by "r1c"", while it "connects "met1" to
"met2" when it is not enclosed by "r1c"".[^reram-ug] A designer
therefore draws only `r1c` in addition to the base layers; the two via
masks are generated from the one drawn `via` layer. The tech-file slide
gives `r1c` a minimum width of 0.230 µm and a minimum spacing of
0.140 µm; the DRC example slide shows rules `rr1_cell.1 (0.230)` and
`rr1_cell.2 (0.230)`.[^reram-ug] The DRC test layout in the repository
carries twelve such rule labels (`RR1_CELL.1` to `RR1_CELL.12`; eleven
carry values from 0.055 to 0.230 or 20, `RR1_CELL.9` none) but no
descriptions, and we
do not attempt to interpret them.[^reram-cell]

Neither `r1c` nor `r1v` appears in the base PDK's mask table or GDS
layer table, and the layer table has no entry on GDS layer
201.[^pdk-05][^pdk-06] The library's cell layout,
`sky130_fd_pr_reram__reram_cell`, contains base-PDK layers — a 0.15 µm
square on `via` (68:44), `met1` (68:20) labelled BE and `met2` (69:20)
labelled TE — and one further shape, 0.32 µm square, on GDS layer
201:20.[^reram-cell] The open_pdks Magic technology file writes and
reads a layer named `RERAM` as "calma 201 20".[^opdks-magic-tech] We
read 201:20 as the drawn `r1c` layer (inference: it is the only layer in
the cell that the base PDK does not define, and its 0.32 µm × 0.32 µm
area equals the Verilog-A model's default `area_ox` of 0.1024e-12
m²[^reram-cell]). The *S8 / SKY130 Process Steps* sheet, from which the
step list used in this reference is taken, names the tier's two masks
"RRAM Mask, RRM" (for `r1c`) and "Via 1 top, RRAM tier, VIMC" (for
`r1v`), marks neither as used in SKY130, and marks RRM as existing for
the runs it labels MPW-1, -2, -3, -4, -7 and -8 and VIMC for MPW-1, -2,
-3, -4, -5, -7 and -8.[^steps-sheet]

Magic models the cell in its own way: under `#ifdef RERAM` a `reram`
contact type joins metal 1 to metal 2, is written out as `via` squares
on 68:44 plus the 201:20 shape, and is checked with "width reram 260
"ReRAM width < %d (rr1.1)"", "spacing reram reram 55 … (rr1.2)" and
"no_overlap reram v1".[^opdks-magic-tech] Magic draws a contact as the
metal area around its cut — the via-1 width rule, also 260, is annotated
"(via.1a + 2 * via.4a)",[^opdks-magic-tech] that is 0.150 µm plus two
0.055 µm enclosures[^pdk-periph] — so its ReRAM width is not directly
comparable with the 0.230 µm `r1c` minimum of SkyWater's tech-file
slide.

## How such a tier is typically built

SkyWater has not published the process steps of the module. What its
documentation does state is the order of the layers, their thicknesses
in the tech file, the HfO₂ base of the switching layer, the definition
of all three RRAM layers by one mask (`r1c`), and the division of via 1
into a lower (`cviam`) and an upper (`r1v`) via.[^reram-ug][^reram-layers][^reram-background]
The sequence below is an industry-generic outline of a back-end RRAM
module of this shape, assembled from published integrations; each step
says which parts are typical and which are our inference for SKY130.

1. **Lower via level complete.** The via-1 holes are printed, etched,
   lined, filled with tungsten and polished as in the base flow
   ({ref}`VIM <step-118>` to {ref}`WCMP3 <step-122>`); on SkyWater's
   slides this is the `cviam` mask, and the bypass uses the same lower
   via.[^reram-ug] That the lower via is a tungsten plug like the base
   via 1 is our inference from its identical height and mask name. A
   25 nm stack needs a flat, clean surface: plug recess and oxide
   erosion that the base process tolerates under a 0.36 µm metal film
   are a much larger fraction of an electrode 10 nm thick (inference
   from the tech-file numbers).
2. **Bottom electrode.** A thin conductor is deposited over the whole
   wafer. Several published HfO₂ RRAMs use TiN electrodes — Lee et al. (ITRI)
   integrated an HfO₂ cell "with the TiN electrodes" in a 0.18 µm CMOS
   process[^lee-2008-hfo2] — and TSMC's integration patent lists Ta,
   TaN, Ti or TiN deposited by CVD, PVD or PECVD for the bottom
   electrode.[^pat-rram-oxide-tsmc] Beckmann et al. used an inert
   tungsten bottom electrode instead.[^beckmann-2016] SkyWater's
   electrode materials are not public; the tech file gives 0.010 µm.[^reram-ug]
3. **Switching oxide.** HfO₂ or a doped or laminated hafnium oxide, a
   few nanometres thick, is deposited by {term}`ALD` — TSMC's patent
   describes alternating HfCl₄ and H₂O pulses, with a long water pulse
   to dope the film with hydrogen and raise its oxygen-vacancy
   concentration[^pat-rram-oxide-tsmc] — or by
   PVD, both chosen, as Intermolecular's patent puts it, "to remain
   within a Back End of Line (BEOL) thermal budget".[^pat-rram-intermolecular]
   ALD's self-limiting half-reactions give the thickness control a
   5 nm film needs.[^wiki-ald][^george-2010] SkyWater states the layer
   is "HfO2-based"[^reram-background] and the tech file gives
   0.005 µm;[^reram-ug] SkyWater's generic description of RRAM names
   metal oxides "by atomic layer deposition",[^reram-background] but
   which method SkyWater uses is not public.
4. **Cap or buffer layer (optional).** Several published HfO₂ cells add
   a thin reactive metal next to the oxide — the "thin reactive Ti
   buffer layer" of Lee et al., the Ti oxygen-exchange layer under the
   TiN top electrode of Beckmann et al., the capping layer of TSMC's
   patent, the Hf of the Hf/HfOx stack of Govoreanu et al.
   (imec)[^lee-2008-hfo2][^beckmann-2016][^pat-rram-oxide-tsmc][^govoreanu-2011]
   — or a second oxide, such as the AlOx buffer that Chen et al. placed
   under the HfOx.[^chen-2009-hfox] The SkyWater tech-file slide shows
   only three RRAM layers.[^reram-ug]
5. **Top electrode**, again a thin nitride or metal by PVD or
   CVD;[^pat-rram-oxide-tsmc] 0.010 µm in the tech file.[^reram-ug] A
   further layer may be added on top: TSMC's etch-stop patent deposits
   an insulating anti-reflective layer on the top electrode that
   "protects the underlying layers from the future etching
   steps".[^pat-rram-etchstop-tsmc]
6. **`r1c` lithography.** Resist islands are printed where the layout
   draws `r1c`. With a 0.230 µm minimum width and a 0.140 µm minimum
   space[^reram-ug] the layer is about as tight as metal 1 and via 1;
   the ITRS 2001 assigns 248 nm exposure with resolution enhancement to
   the critical layers of the 130 nm generation,[^itrs-03] so we infer
   a DUV exposure like {ref}`VIM <step-118>`. Alignment is to the lower vias, which the cell
   must cover.
7. **Stack etch.** The electrodes and oxide are removed outside the
   islands. Beckmann et al. etched TiN/Ti by {term}`RIE` and
   compared a dilute-HF wet etch with a BCl₃/O₂ plasma for the HfO₂,
   examining the effect on structure, electrical behaviour and
   yield;[^beckmann-2016] TSMC's patent etches the top electrode and cap
   with a fluorine or argon plasma, forms nitride sidewall spacers, and
   then etches the oxide and bottom electrode with the spacers as a
   mask.[^pat-rram-oxide-tsmc][^pat-rram-etchstop-tsmc] Because SkyWater
   defines all three layers by `r1c`,[^reram-ug] we infer that the
   stack is etched to one outline, in one or several steps; whether
   spacers are used is not public. The etch must stop without gouging
   the tungsten plugs and oxide beneath, which the bypass vias also
   rely on (inference).
8. **Encapsulation and inter-level dielectric.** The patterned cells
   are covered — in TSMC's patents with nitride spacers or a
   dielectric protection layer, then an upper ILD[^pat-rram-oxide-tsmc][^pat-rram-etchstop-tsmc]
   — to protect the oxide's edges and to build the roughly 0.3 µm of
   dielectric through which the upper vias will pass (0.27 µm above a
   cell, 0.295 µm where there is none; our arithmetic from the tech-file
   levels[^reram-ug]). In an aluminium
   flow such as SKY130's this would, on our reading, be a PECVD or HDP
   oxide like {ref}`NILD3 <step-115>`, followed by polishing as in
   {ref}`CMPM <step-116>` and a cap as in {ref}`NCAPOX3 <step-117>`
   (inference; none of these films is described for sky130B).
9. **`r1v` lithography and via etch.** The upper vias are printed from
   the same drawn `via` layer[^reram-ug] and etched through the new
   dielectric. Over a cell the etch must land on a top electrode only
   10 nm thick without punching through it into the 5 nm oxide; over a
   bypass it must land on the tungsten plug of the lower via (inference
   from the tech-file thicknesses). The two are not the same depth: over
   a cell the upper via passes through 0.27 µm of dielectric, over a
   bypass through 0.295 µm, so an etch shared by both that clears the
   bypass over-etches the cell by about 0.025 µm, more than the whole
   10 nm top electrode; it would need high selectivity to the electrode
   (inference from the tech-file levels).
10. **Upper via fill.** A liner, tungsten fill and polish as at
    {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>` and
    {ref}`WCMP3 <step-122>` — "2 stacked normal vias … same via width
    & spacing"[^reram-ug] suggests, on our reading, the same via
    process repeated.
11. **Metal 2 and above** as in the base flow from
    {ref}`TIAL12 <step-123>`, shifted up by 0.295 µm.

Intel's report on RRAM embedded in its 22FFL logic process describes
the same kind of "bit cell integration into the logic flow" at
22 nm,[^golonzka-2019] and the multi-tier RRAM of Srimani et
al. was built "within the BEOL interconnect stack" of a ~130 nm process
in "a commercial foundry";[^srimani-2020] neither publishes a recipe,
and the foundry in the latter is not named in its abstract.

## The added masks

The base flow prints via 1 with one mask, `VIM`, whose mask-level layer
is `cviam` (40:0, "Via mask") and whose drawn layer is `via` (68:44)
(see the {ref}`masks-index` row for {ref}`VIM <step-118>`).[^pdk-05][^pdk-06]
In sky130B, SkyWater's mask-layer slide keeps `cviam` for the lower
vias and adds two mask layers:[^reram-ug][^reram-layers]

* **`r1c`** — the RRAM cell (bottom electrode, oxide and top electrode),
  printed after the lower vias are complete; listed as "RRAM Mask, RRM"
  in the process-steps sheet's mask table.[^steps-sheet]
* **`r1v`** — the upper vias, over cells and over bypasses, printed
  after the RRAM encapsulation; listed as "Via 1 top, RRAM tier,
  VIMC".[^steps-sheet]

In mask order the tier thus puts two levels between
{ref}`VIM <step-118>` and {ref}`MM2 <step-124>`: `cviam` → `r1c` → `r1v`
→ `cmm2` (order from the cross-section; inference). Neither mask is in
`masks.csv` or `gds_layers.csv`,[^pdk-05][^pdk-06] which is why neither
appears in this reference's {ref}`masks-index`. Both via masks come from
the one drawn `via` layer, separated "during mask generation";[^reram-ug]
whether `r1v` is identical to `cviam` or is sized or selected
differently is not public.

## Electrical operation

SkyWater's background page describes three modes of operation.
**Forming** ({term}`electroforming`) creates "an initial oxygen
filament": a fresh cell starts at "an ultra-high resistance", and a high
field forms a filament by creating oxygen vacancies. **Writing** then
switches the filament: RESET raises the resistance "by applying a
negative electric field", SET lowers it with a positive field, and
"voltages applied during SET/RESET are usually of lower magnitude than
forming". **Reading** uses "a low-applied voltage (e.g., 0.1-0.2V)",
with the high-resistance state usually storing 0 and the low-resistance
state 1.[^reram-background] This is the anion-migration, local-redox
switching of transition-metal oxides that Waser and Aono
classified,[^waser-2007] reviewed for HfO₂ and other binary oxides by
Wong et al. and by Ielmini.[^wong-2012][^ielmini-2016]

Arrays use a {term}`1T1R` cell: a transistor that "is used both to
select the cell within the array but also controls the compliance
current during the FORM, SET, and RESET operations", with the cell
between bit line, word line and source line; SET raises the bit line
with the source line grounded, RESET the reverse.[^reram-background]
Forming therefore has to be built into the product: "built-in forming
must be enabled, otherwise the RRAM will be non-functional".[^reram-background]
SkyWater also describes 1T4R and 1T8R arrays, in which one transistor
serves several cells, and multi-bit storage.[^reram-specs]

SkyWater's technology-specification page publishes forming data "on a
1Mbit RRAM array": fresh conductance "below 0.1 uS (e.g., resistance
above 10MOhms)", forming voltages "from 2.2 to 3.1V … (average 2.5V)",
yields "above 99%" with a maximum forming voltage of 3.1 V, a
low-resistance state after forming of "30-120uS" (about 8–33 kΩ; our
arithmetic), and forming pulses of "1,000ns".[^reram-specs] Its
transcribed tables for a 1T1R test structure give forming with a word
line of 1.4–2.0 V and a bit line of 2.6–3.1 V, RESET with 2.5 V on the
word line and 2.6 V on the source line, and SET with 1.7 V and 2.4 V,
all with 1 000 ns pulses.[^reram-specs] If the whole 2.5 V appeared
across 5 nm of oxide the field would be 5 MV/cm (our arithmetic; part
of the voltage is dropped across the transistor). The page reproduces a
figure from Hsieh et al., whose IEDM 2019 paper reports a 1T4R,
two-bits-per-cell array of "HfO2-based RRAM … built using a logic
foundry technology that is fully compatible with the CMOS back-end
process", with over 10⁶ cycles of endurance and a projected 10-year
retention at 120 °C.[^reram-specs][^hsieh-2019] The documentation's
reference list names two compact models of oxide RRAM, by Guan, Yu and
Wong and by Jiang et al.,[^reram-refs][^guan-2012][^jiang-2014] and the
library's Verilog-A cell describes the device by a filament thickness
between `Tfilament_min` and `Tfilament_max` in an oxide of thickness
`Tox`.[^reram-cell]

## Consequences for the rest of the flow

* **Stack height.** Everything from metal 2 upwards is built 0.295 µm
  higher. In the open_pdks extraction heights, metal 3 moves from
  2.7861 µm to 3.0811 µm and Magic's `mimcap` extraction layer from
  2.4661 µm to 2.7611 µm[^opdks-magic-tech] (an extraction value, not the
  capacitor's physical level, which is over metal 3 —
  {ref}`CAPILD <step-135>` to {ref}`CAPME <step-138>`); the film thicknesses above metal 2 are
  unchanged.[^reram-ug][^opdks-magic-tech] The added height is one more
  dielectric layer and one more via level to build (inference).
* **Via-1 resistance.** Every metal-1-to-metal-2 connection outside a
  cell becomes "2 stacked normal vias".[^reram-ug] The open_pdks
  extraction doubles the via-1 contact resistance for sky130B — 9 000
  against 4 500 in the nominal variant (the unit is mΩ in the base PDK's
  table, which gives the via 4 500 mΩ[^pdk-08]), 30 000 against 15 000
  and 4 000 against 2 000 in the corner variants.[^opdks-magic-tech]
  The doubling applies to every via-1 connection in a sky130B design,
  not only to those near memory, and each bypass adds an interface
  between two plugs (inference from the bypass drawing).
* **Design rules.** `r1c` adds its own width and spacing
  rules;[^reram-ug] Magic also forbids a plain via overlapping a ReRAM
  contact ("no_overlap reram v1").[^opdks-magic-tech]
* **Thermal budget.** Every film and anneal after the RRAM stack — the
  dielectrics and tungsten of the upper vias, the four remaining metal
  levels, the MiM capacitors, passivation and the
  {ref}`ALLY <step-170>` forming-gas anneal — is seen by the 5 nm oxide.
  Intermolecular's patent describes depositing the switching layer
  "to remain within a Back End of Line (BEOL) thermal
  budget";[^pat-rram-intermolecular] what temperatures the SKY130 cell
  tolerates is not public.
* **Test.** Because a fresh cell does not switch until
  formed,[^reram-background] some forming step — on-chip or at wafer
  test ({ref}`HPETEST <step-171>`) — is part of making a working memory;
  which SkyWater uses is not public.

## Machines typically used

* **PVD cluster tool** for the electrodes and any cap metal — TiN and Ti
  by reactive and metal sputtering (Applied Materials Endura
  class[^amat-endura]; {ref}`category-deposition`).
* **ALD chamber** for the hafnium-oxide switching layer — thermal ALD
  from HfCl₄ and water as in TSMC's patent, or plasma-enhanced
  ALD.[^pat-rram-oxide-tsmc][^wiki-ald]
* **DUV stepper or scanner and coat/develop track** for `r1c` and `r1v`
  ({ref}`category-lithography`).
* **Plasma etcher** able to etch the electrodes and HfO₂ — RIE of
  TiN/Ti, fluorine- or argon-based plasmas for the top electrode, and a
  BCl₃/O₂ plasma or a dilute-HF wet etch for the
  oxide[^beckmann-2016][^pat-rram-oxide-tsmc] ({ref}`category-etch`).
* **PECVD or HDP-CVD** for encapsulation and the upper dielectric,
  **oxide CMP**, and the **TiN liner, tungsten CVD and tungsten CMP**
  tools of the base via module ({ref}`category-cmp`).

## Machines likely used at SkyWater

Nothing public ties a SkyWater tool to the ReRAM module. The
capabilities SkyWater lists for its Minnesota fab include every process
the tier needs:[^skw-01]

* **ALD** — "Atomic Layer Deposition", with "Metals: … TiN" and "Oxides:
  SiO2, Al2O3, HfO2, TiO2, ZrO2"; no vendor named. Strength: **strong**
  for an HfO₂ and TiN ALD capability; its use for the RRAM layers is an
  **inference**.
* **PVD** — "AMAT PVD Metal" with "ESC TiN", "Imp TiN" and "Collimated
  Ti". Strength: strong for the capability; electrode use is an
  inference.
* **Metal etch** — "Lam 9600, Al, TiW, TiN, Pt" and "Lam 2300 Versys,
  Al, TiW, TiN, Nb, Pt". Strength: strong for TiN etch; no HfO₂ etch is
  listed.
* **Lithography** — "ASML DUV stepper" and "ASML DUV scanner"; the
  assignment of `r1c`/`r1v` to them is an inference from the 0.14 µm
  space.
* **Dielectrics, tungsten and CMP** — Lam/Novellus/AMAT PECVD and HDP,
  "Lam/Novellus PECVD Tungsten – plug fill", "AMAT Mirra CMP" for oxide
  and tungsten. Strength: strong for existence.
* **Special modules** — the list also includes "Carbon nanotube
  dep/pattern/etch", consistent with the monolithic-3D work reported
  with SkyWater.[^skw-01][^press-05]

## Materials

* **Hafnium-oxide-based switching layer** — stated by
  SkyWater.[^reram-background] A typical ALD route uses HfCl₄ and
  water;[^pat-rram-oxide-tsmc] the precursor at SkyWater is not public.
  Hafnia is the high-κ material of gate stacks and DRAM
  capacitors.[^wilk-2001][^wiki-hfo2]
* **Electrodes** — not stated by SkyWater. The published HfO₂ cells
  cited here use TiN, some with a thin Ti or Hf layer next to the
  oxide; Intermolecular's patent calls TiN an "oxygen reactive"
  electrode material.[^lee-2008-hfo2][^govoreanu-2011][^pat-rram-intermolecular]
* **Etch chemistries** — BCl₃/O₂ plasma, fluorine- or argon-based
  plasmas, and dilute HF as a wet
  alternative.[^beckmann-2016][^pat-rram-oxide-tsmc]
* **Dielectrics** — silicon oxide and silicon nitride for encapsulation
  and the upper ILD (typical[^pat-rram-oxide-tsmc]); **TiN, tungsten
  and WF₆** for the upper vias, as in the base via 1 (inference).
* **Reticles** for `r1c` and `r1v`.

## Related steps and cross-references

* The lower via level: {ref}`NILD3 <step-115>`, {ref}`CMPM <step-116>`,
  {ref}`NCAPOX3 <step-117>`, {ref}`VIM <step-118>`,
  {ref}`VIME <step-119>`, {ref}`TIN3 <step-120>`,
  {ref}`WDEP3 <step-121>`, {ref}`WCMP3 <step-122>`; the metal below:
  {ref}`MM1 <step-113>`, {ref}`MM1E <step-114>`.
* The first step after the tier: {ref}`TIAL12 <step-123>`, then
  {ref}`MM2 <step-124>`, {ref}`MM2E <step-125>` and the via-2 module
  from {ref}`NILD4 <step-126>`.
* The structural analogue: the MiM capacitor, {ref}`CAPILD <step-135>`,
  {ref}`CAPTIW1 <step-136>`, {ref}`CAPM <step-137>`,
  {ref}`CAPME <step-138>`.
* Later steps the cell must survive or that exercise it:
  {ref}`ALLY <step-170>`, {ref}`HPETEST <step-171>`.
* The {ref}`masks-index`; category pages {ref}`category-deposition`,
  {ref}`category-etch`, {ref}`category-lithography`,
  {ref}`category-cmp`.

## References

### Cross-check

* SkyWater, `sky130_fd_pr_reram` *Background* — HfO₂-based RRAM in the
  BEOL; FORM, SET, RESET, read; the 1T1R cell.[^reram-background]
* SkyWater, `sky130_fd_pr_reram` *Technology Specifications* — forming
  voltages and pulses, resistance states, programming
  tables.[^reram-specs]
* SkyWater, `sky130_fd_pr_reram` *User Guide* — "RRAM between met1/met2",
  drawn and mask layers, the bypass, DRC example and tech-file
  stack.[^reram-ug]
* SkyWater, layer-description slide in the library repository — `via`,
  `cviam`, `r1c`, `r1v`.[^reram-layers]
* SkyWater, `reram_cell` layout and Verilog-A model and the DRC test
  layout — GDS 201:20, cell area, `Tox`.[^reram-cell]
* SkyWater, `sky130_fd_pr_reram` *References* — the two compact
  models.[^reram-refs]
* open_pdks `Makefile.in` and `README` — the sky130B variant and its
  definition by ReRAM support.[^opdks-makefile][^opdks-readme]
* open_pdks Magic technology file — the `RERAM` layer on 201:20, its
  DRC, the shifted extraction heights and the doubled via-1
  resistance.[^opdks-magic-tech]
* SkyWater PDK, process stack diagram — the base via-1 and metal-2
  levels.[^pdk-04]
* SkyWater PDK, *Masks*, *Layers Reference*, *Periphery rules* and
  *Parasitic Layout Extraction* — `cviam`, `via`, via
  enclosures and via resistance.[^pdk-05][^pdk-06][^pdk-periph][^pdk-08]
* *S8 / SKY130 Process Steps* sheet — the step list, and in "Run Mask
  IDs" the RRM and VIMC masks and the runs for which they
  exist.[^steps-sheet]
* SkyWater, *Facilities & Capabilities* — ALD HfO₂ and TiN, PVD TiN,
  TiN metal etch.[^skw-01]
* SkyWater, Weebit Nano ReRAM press release — a ReRAM bitcell "between
  Metal1 and Metal2" in S130.[^skw-04]
* IEEE Spectrum, 2018 — SkyWater's role in the DARPA monolithic-3D
  project with RRAM.[^press-05]

### High-level understanding

* Wikipedia, *Resistive random-access memory* — oxygen vacancies,
  forming, set and reset.[^wiki-reram]
* Wikipedia, *Atomic layer deposition* and *Hafnium(IV) oxide* — how
  the switching layer is typically grown, and the
  material.[^wiki-ald][^wiki-hfo2]
* Wikipedia, *Physical vapor deposition*, *Reactive-ion etching* and
  *Chemical-mechanical polishing* — the electrode, etch and polish
  processes of the module.[^wiki-pvd][^wiki-rie][^wiki-cmp]
* ITRS 2001, *Lithography* — the exposure technology of the 130 nm
  generation's critical layers.[^itrs-03]

### Deep dive

* Guan, Yu and Wong, *IEEE EDL* 2012 — the SPICE compact model of
  metal-oxide RRAM the SkyWater documentation cites.[^guan-2012]
* Jiang et al., SISPAD 2014 — the Verilog-A RRAM model the SkyWater
  documentation cites.[^jiang-2014]
* Hsieh et al., IEDM 2019 — a 1T4R multi-bit HfO₂ RRAM array in a
  logic foundry back end, the source of a figure in SkyWater's
  specifications.[^hsieh-2019]
* Le et al., *IEEE TED* 2019 — 3-bits-per-cell programming of HfOx 1T1R
  arrays in a 130 nm back end.[^le-2019]
* Srimani et al., VLSI 2020 — two RRAM tiers and two CNFET tiers in a
  ~130 nm commercial-foundry back end.[^srimani-2020]
* Wong et al., *Proc. IEEE* 2012 — the standard review of metal-oxide
  RRAM.[^wong-2012]
* Waser and Aono, *Nature Materials* 2007 — the classification of
  resistive-switching mechanisms.[^waser-2007]
* Ielmini, *Semicond. Sci. Technol.* 2016 — open-access review of
  switching, reliability and scaling.[^ielmini-2016]
* Lee et al. (ITRI), IEDM 2008 — a TiN/HfO₂ cell with a Ti buffer
  integrated with 0.18 µm CMOS.[^lee-2008-hfo2]
* Chen et al. (ITRI), IEDM 2009 — a 1 kb HfOx 1T1R array with an AlOx
  buffer.[^chen-2009-hfox]
* Govoreanu et al. (imec), IEDM 2011 — a sub-10 nm Hf/HfOx cell and the
  role of the cap layer.[^govoreanu-2011]
* Beckmann et al., *ECS Trans.* 2016 — wet HF versus BCl₃/O₂ RIE
  removal of the HfO₂, compared for structure, electrical behaviour and
  yield.[^beckmann-2016]
* Golonzka et al. (Intel), VLSI 2019 — RRAM integrated into a
  production logic flow.[^golonzka-2019]
* George, *Chem. Rev.* 2010 — atomic layer deposition.[^george-2010]
* Wilk, Wallace and Anthony, *J. Appl. Phys.* 2001 — high-κ dielectrics
  and their process compatibility.[^wilk-2001]
* Dang et al. (TSMC), US 9,431,609 B2 — an RRAM stack with ALD HfOx,
  capping layer, spacers and top-electrode via.[^pat-rram-oxide-tsmc]
* Liu et al. (TSMC), US 10,003,022 B2 — a conductive etch stop and a
  three-etch, spacer-defined stack patterning.[^pat-rram-etchstop-tsmc]
* Lee, Chiang and Pramanik (Intermolecular), US 9,076,523 B2 — embedded
  bipolar ReRAM, BEOL thermal budget and reactive TiN
  electrodes.[^pat-rram-intermolecular]

## Open questions

* The electrode materials, their deposition method, and whether a cap
  or oxygen-exchange layer lies next to the oxide are not public; the
  tech-file slide shows three layers of 0.010, 0.005 and 0.010 µm.
* Whether the HfO₂-based layer is deposited by ALD or PVD, and whether
  the tech-file thicknesses (and the oxide's dielectric constant of 10)
  are physical values or values for extraction and routing, is not
  stated.
* How the stack is etched (one etch or several, with or without
  spacers), how it is encapsulated, and which dielectric forms the
  added 0.295 µm are not public.
* How the upper via lands on a 10 nm top electrode is not described.
  Over a cell the 0.025 µm of the RRAM layers accounts for the
  difference between `via_bot` plus `via_top` (0.540 µm) and the
  0.565 µm between metal 1 and metal 2 (our arithmetic); how the bypass's "2 stacked
  normal vias", where there is no RRAM stack, span the same 0.565 µm is
  not described.
* Whether `r1v` is geometrically identical to `cviam`; whether 201:20 is
  the drawn `r1c` layer (our inference from the library cell and the
  Magic file); what the DRC rules `rr1_cell.1` to `rr1_cell.12` check
  (the DRC example labels `rr1_cell.2` 0.230, while the tech-file
  slide's spacing is 0.140 µm and `rr1_cell.3`/`.4` carry 0.140).
* Whether the lower via of the tier is the unchanged base via-1 module
  and the upper via repeats it, as this page reads the cross-section.
* How the module relates to the Weebit ReRAM offered in S130, to the
  multi-tier RRAM of the DARPA monolithic-3D work, and to the "multiple
  points" in the BEOL that SkyWater's background page mentions.
* What thermal budget the cell tolerates after its deposition, and
  whether forming is done on-chip or at wafer test.

<!-- footnotes -->

[^opdks-makefile]: R. T. Edwards et al., *open_pdks*,
    `sky130/Makefile.in`, lines 4 and 345–346, commit 1689ac3
    (2026-08-27), accessed 2026-09-13.
    <https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/Makefile.in>
[^opdks-readme]: R. T. Edwards et al., *open_pdks*, `sky130/README`,
    commit 1689ac3, accessed 2026-09-13.
    <https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/README>
[^opdks-magic-tech]: R. T. Edwards et al., *open_pdks*,
    `sky130/magic/sky130.tech` (Magic technology file source), lines
    1293–1301, 4194, 4821–4842, 5303–5336 and 5421–5547, commit 1689ac3,
    accessed 2026-09-13.
    <https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/magic/sky130.tech>
[^reram-background]: SkyWater PDK Authors, *Background*,
    `sky130_fd_pr_reram` — SKY130 ReRAM (SkyWater Provided)
    documentation, accessed 2026-09-13.
    <https://sky130-fd-pr-reram.readthedocs.io/en/latest/background.html>
[^reram-specs]: SkyWater PDK Authors, *Technology Specifications*,
    `sky130_fd_pr_reram` documentation, accessed 2026-09-13.
    <https://sky130-fd-pr-reram.readthedocs.io/en/latest/technology_specifications.html>
[^reram-ug]: SkyWater PDK Authors, *User Guide* (slides "RRAM between
    met1/met2", drawn and mask layers, DRC example and "TechFile for
    Place-and-Route"), `sky130_fd_pr_reram` documentation, accessed
    2026-09-13. <https://sky130-fd-pr-reram.readthedocs.io/en/latest/user_guide.html>
[^reram-layers]: SkyWater PDK Authors, `docs/figures/page_5.svg`
    ("sky130_fd_pr_reram Layer Descriptions"),
    google/skywater-pdk-libs-sky130_fd_pr_reram repository, commit
    d6d2a3c (2022-04-20).
    <https://github.com/google/skywater-pdk-libs-sky130_fd_pr_reram/blob/d6d2a3c6960aac0a0b12fc21221c31777bbf284d/docs/figures/page_5.svg>
[^reram-cell]: SkyWater PDK Authors, `cells/reram_cell/`
    (`sky130_fd_pr_reram__reram_cell.gds`, `.va`) and
    `cells/reram_test_drc/`, google/skywater-pdk-libs-sky130_fd_pr_reram
    repository, commit d6d2a3c.
    <https://github.com/google/skywater-pdk-libs-sky130_fd_pr_reram/tree/d6d2a3c6960aac0a0b12fc21221c31777bbf284d/cells>
[^reram-refs]: SkyWater PDK Authors, *References*,
    `sky130_fd_pr_reram` documentation, accessed 2026-09-13.
    <https://sky130-fd-pr-reram.readthedocs.io/en/latest/references.html>
[^skw-04]: SkyWater Technology, *Weebit Nano ReRAM IP now available in
    SkyWater Technology's S130 process*, press release, 2023-03-07,
    accessed 2026-09-13.
    <https://www.skywatertechnology.com/weebit-nano-reram-ip-now-available-in-skywater-technologys-s130-process/>
[^press-05]: S. K. Moore, "The Foundry at the Heart of DARPA's Plan to
    Let Old Fabs Beat New Ones", *IEEE Spectrum*, 2018-08-06.
    <https://spectrum.ieee.org/the-foundry-at-the-heart-of-darpas-plan-to-let-old-fabs-beat-new-ones>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tabs "Sheet1" (step number, code and description) and "Run Mask IDs"
    (rows "RRAM Mask, RRM" and "Via 1 top, RRAM tier, VIMC"), retrieved
    2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^wiki-ald]: Wikipedia, *Atomic layer deposition*.
    <https://en.wikipedia.org/wiki/Atomic_layer_deposition>
[^wiki-hfo2]: Wikipedia, *Hafnium(IV) oxide*.
    <https://en.wikipedia.org/wiki/Hafnium(IV)_oxide>
[^george-2010]: S. M. George, "Atomic Layer Deposition: An Overview",
    *Chemical Reviews* **110**(1), 111–131 (2010).
    <https://doi.org/10.1021/cr900056b>
[^wilk-2001]: G. D. Wilk, R. M. Wallace and J. M. Anthony, "High-κ gate
    dielectrics: Current status and materials properties
    considerations", *Journal of Applied Physics* **89**(10), 5243–5275
    (2001). <https://doi.org/10.1063/1.1361065>
[^lee-2008-hfo2]: H. Y. Lee, P. S. Chen, T. Y. Wu, Y. S. Chen,
    C. C. Wang, P. J. Tzeng, C. H. Lin, F. Chen, C. H. Lien and
    M.-J. Tsai, "Low power and high speed bipolar switching with a thin
    reactive Ti buffer layer in robust HfO2 based RRAM", *2008 IEEE
    International Electron Devices Meeting*, pp. 1–4.
    <https://doi.org/10.1109/IEDM.2008.4796677>
[^chen-2009-hfox]: Y. S. Chen, H. Y. Lee, P. S. Chen, P. Y. Gu et al.,
    "Highly scalable hafnium oxide memory with improvements of resistive
    distribution and read disturb immunity", *2009 IEEE International
    Electron Devices Meeting (IEDM)*, pp. 1–4.
    <https://doi.org/10.1109/IEDM.2009.5424411>
[^govoreanu-2011]: B. Govoreanu, G. S. Kar, Y.-Y. Chen, V. Paraschiv et
    al., "10×10nm² Hf/HfOx crossbar resistive RAM with excellent
    performance, reliability and low-energy operation", *2011
    International Electron Devices Meeting*, pp. 31.6.1–31.6.4.
    <https://doi.org/10.1109/IEDM.2011.6131652>
[^beckmann-2016]: K. Beckmann, J. Holt, W. Olin-Ammentorp, J. Van
    Nostrand and N. Cady, "Impact of Etch Process on Hafnium Dioxide
    Based Nanoscale RRAM Devices", *ECS Transactions* **75**(13), 93–99
    (2016). <https://doi.org/10.1149/07513.0093ecst>
[^golonzka-2019]: O. Golonzka, U. Arslan, P. Bai, M. Bohr, O. Baykan et
    al., "Non-Volatile RRAM Embedded into 22FFL FinFET Technology",
    *2019 Symposium on VLSI Technology*, pp. T230–T231.
    <https://doi.org/10.23919/VLSIT.2019.8776570>
[^srimani-2020]: T. Srimani, G. Hills, M. Bishop, C. Lau, P. Kanhaiya
    et al., "Heterogeneous Integration of BEOL Logic and Memory in a
    Commercial Foundry: Multi-Tier Complementary Carbon Nanotube Logic
    and Resistive RAM at a 130 nm node", *2020 IEEE Symposium on VLSI
    Technology*, pp. 1–2.
    <https://doi.org/10.1109/VLSITechnology18217.2020.9265083>
[^hsieh-2019]: E. R. Hsieh, M. Giordano, B. Hodson, A. Levy, S. K.
    Osekowsky, R. M. Radway, Y. C. Shih, W. Wan, T. F. Wu, X. Zheng,
    M. Nelson, B. Q. Le, H.-S. P. Wong, S. Mitra and S. Wong,
    "High-Density Multiple Bits-per-Cell 1T4R RRAM Array with Gradual
    SET/RESET and its Effectiveness for Deep Learning", *2019 IEEE
    International Electron Devices Meeting (IEDM)*, pp. 35.6.1–35.6.4.
    <https://doi.org/10.1109/IEDM19573.2019.8993514>
[^guan-2012]: X. Guan, S. Yu and H.-S. P. Wong, "A SPICE Compact Model
    of Metal Oxide Resistive Switching Memory With Variations", *IEEE
    Electron Device Letters* **33**(10), 1405–1407 (2012).
    <https://doi.org/10.1109/LED.2012.2210856>
[^jiang-2014]: Z. Jiang, S. Yu, Y. Wu, J. H. Engel, X. Guan and
    H.-S. P. Wong, "Verilog-A compact model for oxide-based resistive
    random access memory (RRAM)", *2014 International Conference on
    Simulation of Semiconductor Processes and Devices (SISPAD)*,
    pp. 41–44. <https://doi.org/10.1109/SISPAD.2014.6931558>
[^waser-2007]: R. Waser and M. Aono, "Nanoionics-based resistive
    switching memories", *Nature Materials* **6**(11), 833–840 (2007).
    <https://doi.org/10.1038/nmat2023>
[^wong-2012]: H.-S. P. Wong, H.-Y. Lee, S. Yu, Y.-S. Chen, Y. Wu,
    P.-S. Chen, B. Lee, F. T. Chen and M.-J. Tsai, "Metal–Oxide RRAM",
    *Proceedings of the IEEE* **100**(6), 1951–1970 (2012).
    <https://doi.org/10.1109/JPROC.2012.2190369>
[^ielmini-2016]: D. Ielmini, "Resistive switching memories based on
    metal oxides: mechanisms, reliability and scaling", *Semiconductor
    Science and Technology* **31**(6), 063002 (2016).
    <https://doi.org/10.1088/0268-1242/31/6/063002>
[^pat-rram-oxide-tsmc]: T. H. Dang, H.-L. Lin, C.-Y. Tsai, C.-S. Tsai
    and R.-L. Lee (Taiwan Semiconductor Manufacturing Co.), *Oxide film
    scheme for RRAM structure*, US 9,431,609 B2, filed 2014-08-14,
    granted 2016-08-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9431609>
[^pat-rram-etchstop-tsmc]: M. C. Liu, Y.-T. Tseng, C.-Y. Hsu, S.-C. Liu
    and C.-S. Tsai (Taiwan Semiconductor Manufacturing Co.), *RRAM cell
    structure with conductive etch-stop layer*, US 10,003,022 B2, filed
    2014-03-04, granted 2018-06-19.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10003022>
[^pat-rram-intermolecular]: M. Lee, T. Chiang and D. Pramanik
    (Intermolecular, Inc.), *Methods of manufacturing embedded bipolar
    switching resistive memory*, US 9,076,523 B2, filed 2012-12-13,
    granted 2015-07-07.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9076523>
[^wiki-reram]: Wikipedia, *Resistive random-access memory*.
    <https://en.wikipedia.org/wiki/Resistive_random-access_memory>
[^wiki-pvd]: Wikipedia, *Physical vapor deposition*.
    <https://en.wikipedia.org/wiki/Physical_vapor_deposition>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-cmp]: Wikipedia, *Chemical-mechanical polishing*.
    <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
[^le-2019]: B. Q. Le, A. Grossi, E. Vianello, T. Wu, G. Lama, E. Beigne,
    H.-S. P. Wong and S. Mitra, "Resistive RAM With Multiple Bits Per
    Cell: Array-Level Demonstration of 3 Bits Per Cell", *IEEE
    Transactions on Electron Devices* **66**(1), 641–646 (2019).
    <https://doi.org/10.1109/TED.2018.2879788>
