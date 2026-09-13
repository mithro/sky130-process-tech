(step-161)=
# Step 161 — WTIAL5: AlCu 2/TiW deposition

| | |
|---|---|
| **Step number** | 161 of 171[^steps-sheet] |
| **Step code** | `WTIAL5` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`VIM4E <step-160>` |
| **Next step** | {ref}`MM5 <step-162>` |

## What this step is

`WTIAL5` deposits the metal-5 film stack — the top metal of SKY130,
which carries power, wide buses, inductors and the {term}`bond pads <bond pad>`. Onto the
cap oxide of {ref}`NCAPOX6 <step-158>`, and into the open via-4 holes
just etched at {ref}`VIM4E <step-160>`, a sputtering {term}`cluster tool` lays
down, in one vacuum sequence on our reading, a refractory underlayer, a
thick aluminium–copper alloy and a titanium–tungsten cap; the
{ref}`MM5 <step-162>` mask and {ref}`MM5E <step-163>` etch then pattern
it into the `met5` layer (GDS 72:20, "Metal 5").[^pdk-06] The PDK's
background page describes the technology as having "5 levels of
metal (p - penta)",[^pdk-02] and its layer table defines the later opening
over metal-5 pads, `pad` (76:20), "Passivation cut (opening over
pads)".[^pdk-06]

The PDK's numbers for metal 5 are larger than for any level below. The
process stack diagram labels `metal5` 1.26 µm, with its bottom at
5.3711 µm,[^pdk-04] and Edwards's slides repeat the 1.26 µm;[^ann-16]
the antenna-rule table gives "Metal5 thickness for antenna ratio
calculation" as 1.2 µm for "S8P*/SP8P* with 1.2um thick metal" and 2 µm
for "S8P*/SP8P* with 2um thick metal";[^pdk-03] the antenna chapter's
Table Ig, for "S8P12-10R*/S8PIR-10R/S8PF-10R*", gives 1.200 µm in its
`met5.1` row, while Table Ie, for "S8P-5R/SP8P-5R/S8P-10R*", has no
`met5` row and gives 2.000 µm in a row labelled
`waffle_chip`;[^pdk-11] and the device page gives `RSM5` 28.5 mΩ/sq
(limits 21.2–35.8), which the extraction table rounds to
29 mΩ/sq.[^pdk-07][^pdk-08] On the S8PIR* reading set out at
{ref}`MM5 <step-162>` the 1.2 µm table applies (inference). About
1.2 µm of Al–Cu at 28.5 mΩ/sq implies a resistivity of about
3.4 µΩ·cm, within the range expected for sputtered Al–0.5%Cu (typical
industry value;[^txt-02] our arithmetic), whereas a 2 µm film at the
same sheet resistance would imply 5.7 µΩ·cm, too high for the alloy; the
arithmetic agrees with that reading (inference). The metal-5 design
rules are coarse: 1.600 µm width and space (m5.1, m5.2), a 4.000 µm²
minimum area (m5.4, whose probe-pad exemption excludes
"SKY130PIR*/SKY130PF*" flows) and 0.310 µm enclosure of via 4
(m5.3).[^pdk-periph]

No public source gives the metal-5 films. The Cypress qualification
reports that describe stacks at the same fab are for three-metal
processes;[^cyp-qtp-113005] the nearest analogue is the thick top metal of the S8DI
technology in the 2014 metal-stack-change report, "Metal 3: 500A
TiW/21,250A Al 0.5% Cu/300A TiW",[^cyp-qtp-123907] a 2.2 µm stack of
the thickness class of the PDK's 2 µm antenna entry rather than of the
1.2 µm film read here. This reference describes
metal 5 as a Ti or TiW underlayer, some 1.2 µm of Al–Cu and a TiW cap
(inference: SkyWater's PVD film list includes "Aluminum both pure and
Cu doped", "TiW" and "Collimated Ti",[^skw-01] the Cypress stacks at
the same fab are built this way,[^cyp-qtp-113005][^cyp-qtp-123907] and
the PDK's thickness and sheet resistance fit such a stack).

**How is via 4 filled?** No public source states how via 4 is filled.
This reference describes no TiN liner, tungsten fill or plug polish for
via 4, unlike vias 1–3 ({ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`,
{ref}`WCMP5 <step-148>`); this deposition comes next. We read the via-4
holes as filled by the metal-5 stack itself, on the following evidence
and reasoning (all inference):

* *The geometry suits it.* Via 4 is allowed only as a 0.800 µm square
  (via4.1, via4.3) and is 0.505 µm deep,[^pdk-periph][^pdk-04] an
  {term}`aspect ratio` of about 0.63:1, while the metal-5 stack is more
  than twice as thick as the via is deep (our arithmetic). Skelly and
  Gruenke showed that straight-walled vias 1.3 µm wide and 1 µm deep —
  a steeper hole — could be planarised by bias-sputtered aluminium,
  where unbiased sputtering gave 20 % coverage,[^skelly-1986] and Taylor,
  Jain and Cale found that the step coverage of sputtered Al–Cu improves
  with temperature and lower deposition rate.[^taylor-1998] A single
  fixed via size lets one deposition recipe serve every via.
* *The rules are written for it.* Metal 5 must enclose via 4 by
  0.310 µm (m5.3) where metal 4 needs 0.190 µm (via4.4),[^pdk-periph] and
  the minimum metal-5 line is twice the via width; a via that the top
  metal fills needs the metal to overlap its rim generously (inference).
* *Established techniques exist.* {term}`Aluminium via fill <aluminium via fill>` was a production
  alternative to {term}`tungsten plugs <W plug>` in the 1990s, compared with them by Gn,
  Liu and Guo:[^gn-1994] hot or {term}`reflow` sputtering — reviewed by Kikuta,
  who notes that it avoids Al/W interfaces and the higher resistivity of
  tungsten[^kikuta-1995] — and studied by Ono, Ushiku and Yoda (Al–Si
  contact fill at 500–550 °C) and Nishimura, Yamada and Ogawa
  (high-temperature Al–Si–Cu via fill), with Hariu et al. measuring the
  {term}`electromigration` lifetime of Al–Cu/Ti films sputtered at 500 °C with
  bias;[^ono-1990][^nishimura-1991][^hariu-1989]
  the Applied Materials multistep process, which sputters a thin
  aluminium layer at modest power, then continues at high power with
  wafer bias until, in the patent's words, "the wafer temperature
  reaches about 500° C., preferably about
  400° C.";[^pat-al-multistep-amat] two-step fills, whose
  deposition-time ratio Deshmukh related to via fill;[^deshmukh-2003]
  and Electrotech's "Forcefill", which closes the via with sputtered
  metal and then applies "temperatures in the range 350° C. to 650° C.
  and pressures in excess of 3,000 p.s.i.",[^pat-forcefill-electrotech]
  whose mechanism Dirks et al. and Janssen et al.
  studied.[^dirks-1999][^janssen-1998] Tapered via walls, which the
  Motorola and Chartered patents make to improve metal step
  coverage,[^pat-sloped-motorola][^pat-taper-chartered] ease any of
  these.
* *The resistance does not contradict it.* The PDK's `via4` is 380 mΩ
  against 3 410 mΩ for the tungsten-plug `via3`;[^pdk-08] the sixteenfold
  larger area accounts for that difference without deciding the fill
  material (our arithmetic).

Which technique — a thick, conventionally sputtered film leaving a
dimple over each via, a heated or biased deposition, or a high-pressure
fill — SKY130 uses is not public. A hot fill near 500 °C would also
expose both {term}`MiM capacitor` levels and four aluminium levels to a
temperature above the 400–450 °C usually allowed for an aluminium back
end (industry-typical[^txt-05]), which argues for the gentler options
(the Applied Materials patent itself prefers stopping near
400 °C[^pat-al-multistep-amat]) (inference).

## Step category

`WTIAL5` is a {ref}`Thin-film deposition <category-deposition>` step of
the *PVD, multi-layer metal* class; {ref}`TIAL6 <step-112>` sets out the
sputtering of Ti, Al–Cu and Ti:W films, and {ref}`WTIAL3 <step-134>` what a
thick film changes. Two things are specific to this instance. It is the
thickest metal deposition of the flow, about 1.5 times metal 3 and 4
(1.26 µm against 0.845 µm[^pdk-04]), with the longer deposition, larger
grains, higher stress and {term}`hillock` tendency that go with it. And it is
the only metal level in the flow deposited onto open vias rather than
onto polished plugs, so its underlayer and early aluminium must cover
the via walls and floor as well as the flat oxide (inference from the
reading above and the via-4 rules[^pdk-periph]).

## Why this step exists

Metal 5 is the top routing level and the interface to the package:

* **Low resistance for power and long lines.** At 28.5 mΩ/sq[^pdk-07]
  metal 5 has about 60 % of the sheet resistance of metals 3 and 4
  (47 mΩ/sq[^pdk-08]); Bohr's argument that interconnect limits
  performance[^bohr-1995] and Stamper, Fuselier and Tian's account of
  wiring RC delay[^stamper-1998] explain why an aluminium back end puts
  its thickest metal on top, where the ITRS 2001 interconnect chapter
  places the global wires.[^itrs-02]
* **Inductors.** The PDK calls the technology "Inductor or
  Inductor-Capable";[^pdk-02] a thick top metal is the classic route to
  a high-{term}`quality-factor <quality factor>` spiral inductor, as Chu et al. showed for thick
  top metal with different passivation schemes.[^chu-2001] The periphery
  rules' `rdl` table "Defines the Cu Inductor" that "Connects to met5
  through the pad opening",[^pdk-periph] an option built on top of this
  level, which the PDK's nomenclature page lists as "s8phirs", "The base
  process plus rdl layer and rdl metal inductors".[^pdk-previous]
* **Bond pads.** Wire bonds and probe needles land on metal 5 through
  the `pad` opening (pad.2 spacing 1.270 µm).[^pdk-periph][^pdk-06] The
  pad metal and the oxide beneath it take the mechanical load of probing
  and bonding: Hunter et al. used wire bonding to reveal cracks from wafer probing in
  aluminium bond pads over SiO₂,[^hunter-2012] Marsh et al. compared
  copper ball bonds on two pad aluminium thicknesses,[^marsh-2016] and
  Hess et al. evaluated the wire-bond and package-stress reliability of
  bond-over-active pad layouts for 0.13 µm CMOS.[^hess-2003] If the cap is TiW it must be removed from the pad at the
  opening ({ref}`PDME <step-169>`); Danzl and McLaurin used hydrogen peroxide to remove a TiW
  anti-reflective coating from aluminium bond pads.[^danzl-1997]
* **Filling via 4 and contacting the second capacitor.** On our reading
  above, this deposition also makes the via-4 connections to metal 4
  and to the `cap2m` plates. Kwok et al. traced the shorter
  electromigration lifetime of tungsten-stud chains to the break in
  copper supply at the Al–Cu/W interface,[^kwok-1990] an interface an
  aluminium-filled via does not have;[^kikuta-1995] Matsuoka et al.,
  however, found tungsten-filled vias more reliable than unfilled vias,
  whose lifetime fell with diameter,[^matsuoka-1990] so the benefit
  depends on the aluminium filling the hole completely (inference).
* **Film functions.** Copper doping slows electromigration;[^ames-1970] a
  refractory underlayer promotes (111) texture;[^knorr-1996] the TiW cap
  suppresses hillocks and serves as the anti-reflective surface for
  {ref}`MM5 <step-162>`, the role Rocke and Schneegans
  documented;[^rocke-1988] Chaudhari analysed hillock growth, which rises
  with film thickness.[^chaudhari-1974][^zlatanovic-1990]

Without `WTIAL5` there is no top metal, no bond pads and no connection to
metal 4 or to the second capacitor.

## How it is typically performed

An industry-generic thick top-metal deposition for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public); the film-by-film account is at
{ref}`TIAL6 <step-112>`.

1. **Cluster tool.** A multi-chamber PVD platform — SkyWater's "AMAT PVD
   Metal" with "Sputter etch, degas"[^skw-01] — so that {term}`degas`, pre-clean
   and the depositions happen without an air break; the Endura is the
   200 mm-era Applied Materials platform.[^amat-endura]
2. **Degas.** A vacuum bake long enough to drive water from the via
   walls and the oxide; Taguchi, Maeda and Aoyama improved aluminium via
   filling by controlling that outgassing.[^taguchi-1998]
3. **Pre-clean.** A light argon {term}`sputter etch` to remove fluoride,
   polymer and oxide residue from the TiW floors of the vias (industry
   practice[^txt-05]); on a `cap2m` plate the same etch must not thin the
   plate (inference).
4. **Underlayer.** Ti or TiW; {term}`collimated titanium <collimated sputtering>`[^rossnagel-1991] places
   more of the film on the via floor, and an underlayer changes the
   grain structure and via fill of the aluminium above it, as Pramanik
   and Jain found for sputtered aluminium and Lee and Rha for a CVD–PVD
   aluminium plug.[^pramanik-1990][^lee-2003]
5. **Al–0.5%Cu, of the order of 1.2 µm.** Sputtered from an Al–Cu target
   in one or more passes; for a via fill, a cooler first layer followed
   by a hotter or biased one (the multistep and cold/hot
   schemes[^pat-al-multistep-amat][^deshmukh-2003]) or a separate
   high-pressure step[^pat-forcefill-electrotech] are the published
   options; grain size and texture follow the structure-zone
   relations.[^thornton-1974] Thickness inferred from the 1.26 µm
   stack[^pdk-04] and the 1.2 µm antenna value.[^pdk-03]
6. **TiW cap.** From a Ti:W target;[^pat-tiw-hitachi] its thickness is not
   public (the lower-level analogue is 300 Å[^cyp-qtp-123907]).
7. **Metrology.** Sheet resistance by {term}`four-point probe` (the PDK's
   28.5 mΩ/sq[^pdk-07]); thickness by XRF or profilometry; reflectivity;
   stress by wafer bow — the largest of the flow; via-fill cross-sections
   on monitors; via-4 chain resistance at {term}`e-test` after
   patterning, against 380 mΩ.[^pdk-08]

## Machines typically used

* **{ref}`PVD cluster tool <machine-pvd-cluster-tool>` with Ti/TiW, Al–Cu and TiW chambers**, 200 mm, with
  heated or biased aluminium chambers where hot fill is used: Applied
  Materials Endura,[^amat-endura] Novellus INOVA, Electrotech/Trikon
  high-pressure fill modules,[^pat-forcefill-electrotech] Ulvac and Anelva
  sputtering systems ({ref}`category-deposition`).
* **Degas and sputter-etch pre-clean chambers**.
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`**, **{ref}`XRF <machine-film-thickness-metrology>`**, **reflectometer**, **stress gauge**,
  **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **AMAT PVD Metal platform.** SkyWater lists "AMAT PVD Metal" with
  "Sputter etch, degas", "Aluminum both pure and Cu doped", "TiW",
  "Collimated Ti" and other films.[^skw-01] Strength: **strong** for the
  vendor and the films; the platform model (Endura[^amat-endura]), the
  underlayer and any hot or high-pressure fill capability are
  **inferences** or **not public**.
* **Metal etchers "Lam 9600, Al, TiW, TiN, Pt" and "Lam 2300 Versys, Al,
  TiW, TiN, Nb, Pt"**[^skw-01] corroborate that TiW-capped aluminium is
  etched in the fab (used at {ref}`MM5E <step-163>`).

## Resources required

* **{ref}`Sputter targets <material-sputter-targets>`** — titanium and/or Ti:W, Al–0.5 wt.% Cu, Ti:W
  (10 wt.% Ti[^pat-tiw-hitachi]); SkyWater's filings name Honeywell
  Electronic Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal
  2023 10-K) as sputter-target suppliers.[^sec-01][^sec-02] A 1.2 µm film
  consumes Al–Cu target material faster per wafer than any other level (our
  arithmetic from the thicknesses[^pdk-04]).
* **Argon** for sputtering and pre-clean; **nitrogen** for venting.
* **{ref}`Chamber shields <material-hardware-consumables>`, clamps and electrostatic-chuck consumables**.
* **{ref}`Monitor wafers <material-substrates>`** for sheet resistance, stress, reflectivity and
  via-fill cross-sections.

## Related steps and cross-references

* Previous: {ref}`VIM4E <step-160>` (the vias it fills, on our reading).
  Next: {ref}`MM5 <step-162>` (the mask) and {ref}`MM5E <step-163>` (the
  etch).
* The surface it lands on: {ref}`NCAPOX6 <step-158>`; the metal-4 lines
  and `cap2m` plates it contacts: {ref}`WTIAL4 <step-149>`,
  {ref}`CAPTIW2 <step-151>`.
* The passivation and pad opening above it: {ref}`NFUSOX <step-164>`,
  {ref}`PDM <step-168>`, {ref}`PDME <step-169>`.
* The thinner stacks: {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`,
  {ref}`WTIAL3 <step-134>`, {ref}`WTIAL4 <step-149>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Background* — "5 levels of metal (p - penta)";
  "Inductor or Inductor-Capable".[^pdk-02]
* SkyWater PDK, *Previous Nomenclature* — "s8pfhd", "5 metal layer
  backend stack"; "s8phirs", rdl metal inductors.[^pdk-previous]
* SkyWater PDK, *Process stack diagram* — `metal5` 1.26 µm; metal5 bottom
  5.3711 µm; via4 0.505 µm.[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — metal-5 antenna thicknesses
  1.2 µm and 2 µm.[^pdk-03]
* SkyWater PDK, *Antenna Rules* — Table Ig (S8P12-10R*/S8PIR-10R/S8PF-10R*)
  `met5.1` 1.200 µm; Table Ie (S8P-5R/SP8P-5R/S8P-10R*)
  `waffle_chip` 2.000 µm.[^pdk-11]
* SkyWater PDK, *Device Details* — `RSM5` 0.0285 Ω/sq.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — metal 5 29 mΩ/sq; `via4`
  380 mΩ; `via3` 3 410 mΩ.[^pdk-08]
* SkyWater PDK, *Periphery rules* — m5.1–m5.4; via4.1, via4.3, via4.4;
  pad.2; the `rdl` function text.[^pdk-periph]
* SkyWater PDK, *Layers Reference* — `met5` 72:20; `pad` 76:20.[^pdk-06]
* Edwards, 2021 lecture slides — metal5 1.26 µm.[^ann-16]
* Cypress, QTP 123907/132302/132301 — the S8DI 2.2 µm TiW/Al–Cu/TiW top
  metal.[^cyp-qtp-123907]
* SkyWater, *Facilities & Capabilities* — "AMAT PVD Metal" film list;
  metal etchers.[^skw-01]
* SkyWater, Form S-1 and 10-K — target suppliers.[^sec-01][^sec-02]
* Hitachi Metals, US 5,160,534 — Ti:W target composition.[^pat-tiw-hitachi]
* Applied Materials, *Endura PVD*.[^amat-endura]

### High-level understanding

* Wikipedia, *Sputter deposition*, *Wire bonding*, *Interconnect
  (integrated circuits)*.[^wiki-sputter][^wiki-wire-bonding][^wiki-interconnect]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  sputtering and aluminium metallisation.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — thick upper
  metals and via filling.[^txt-05]
* Kikuta, *MRS Bulletin* 1995 — a short review of aluminium reflow
  sputtering.[^kikuta-1995]

### Deep dive

* Wang (Applied Materials), US 5,108,570 — a multistep, biased, heated
  aluminium sputter process for stepped wafers.[^pat-al-multistep-amat]
* Dobson (Electrotech), US 5,527,561 — filling recesses by high pressure
  and temperature after closing them with sputtered
  metal.[^pat-forcefill-electrotech]
* Dirks et al., *J. Appl. Phys.* 1999, and Janssen et al., 1998 — the
  mechanisms of aluminium via fill by reflow and
  forcefill.[^dirks-1999][^janssen-1998]
* Skelly and Gruenke, *JVST A* 1986 — bias-sputtered aluminium in
  straight-walled vias.[^skelly-1986]
* Taylor, Jain and Cale, *JVST A* 1998 — temperature and rate dependence
  of Al–Cu step coverage.[^taylor-1998]
* Ono, Ushiku and Yoda, VMIC 1990; Hariu et al., IRPS 1989; Nishimura,
  Yamada and Ogawa, VMIC 1991 — planarised and high-temperature aluminium
  contact and via filling.[^ono-1990][^hariu-1989][^nishimura-1991]
* Deshmukh, *Thin Solid Films* 2003 — deposition-time ratio and via
  density in aluminium via fill.[^deshmukh-2003]
* Pramanik and Jain, VMIC 1990, and Lee and Rha, *Jpn. J. Appl. Phys.*
  2003 — underlayer effects on aluminium grain structure and via
  fill.[^pramanik-1990][^lee-2003]
* Gn, Liu and Guo, SPIE 1994 — tungsten versus aluminium plugs.[^gn-1994]
* Taguchi, Maeda and Aoyama, 1998 — water outgassing and aluminium via
  fill.[^taguchi-1998]
* Berglund et al. (Motorola), US 4,698,128, and Chou (Chartered),
  US 5,308,415 — sloped and tapered vias for metal step
  coverage.[^pat-sloped-motorola][^pat-taper-chartered]
* Kwok et al., VMIC 1990, and Matsuoka et al., *IEEE TED* 1990 —
  electromigration at tungsten-stud and tungsten-filled vias: the
  Al–Cu/W interface as a flux divergence, and tungsten-filled against
  unfilled vias.[^kwok-1990][^matsuoka-1990]
* Chu et al., VLSI-TSA 2001 — thick top metal for high-Q
  inductors.[^chu-2001]
* Hunter et al., IMAPS 2012; Marsh et al., ECTC 2016; Hess et al., ECTC
  2003 — probing, bonding and bond-over-active reliability of aluminium
  pads.[^hunter-2012][^marsh-2016][^hess-2003]
* Danzl and McLaurin, IEMT 1997 — removing a TiW cap from aluminium bond
  pads.[^danzl-1997]
* Rossnagel et al., *JVST A* 1991 — collimated sputtering for via-floor
  coverage.[^rossnagel-1991]

## Open questions

* **How via 4 is filled.** No public source states it; this reference
  reads the vias as filled by the metal-5 stack — by thick sputtering,
  heated or biased deposition, or a high-pressure step — as an inference
  from the via-4 and metal-5 rules and the published fill techniques,
  and describes no separate taper or fill module.
* **Metal-5 thickness.** The stack diagram and Edwards's slides give
  1.26 µm,[^pdk-04][^ann-16] the assumptions and antenna tables 1.2 µm or
  2 µm by flow;[^pdk-03][^pdk-11] that the 1.2 µm "S8PIR-10R" table
  applies to SKY130 is our reading (see {ref}`MM5 <step-162>`), and
  whether the 1.26 µm includes the refractory layers is not public.
* **Metal-5 minimum width.** That SKY130 is an S8PIR* flow, under which
  the minimum-CD table and periphery rules both give 1.6 µm, is our
  reading of the background page;[^pdk-02] neither table names SKY130's
  flow.
* The underlayer material, film thicknesses, deposition temperatures and
  whether the deposition is one pass or several are not public.

<!-- footnotes -->

[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (generic resistors),
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-11]: SkyWater PDK Authors, *SkyWater SKY130 Process Design Rules*
    index page and its *Antenna Rules* chapter, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules.html>,
    <https://skywater-pdk.readthedocs.io/en/main/rules/antenna.html>
[^pdk-previous]: SkyWater PDK Authors, *Previous Nomenclature*,
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/previous.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^pat-tiw-hitachi]: Hitachi Metals, *Titanium-tungsten target material
    for sputtering and manufacturing method therefor*, US 5,160,534 A,
    granted 1992-11-03.
    <https://patents.google.com/patent/US5160534A/en>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^wiki-wire-bonding]: Wikipedia, *Wire bonding*.
    <https://en.wikipedia.org/wiki/Wire_bonding>
[^wiki-interconnect]: Wikipedia, *Interconnect (integrated circuits)*.
    <https://en.wikipedia.org/wiki/Interconnect_(integrated_circuits)>
[^kikuta-1995]: K. Kikuta, "Aluminum Reflow Sputtering", *MRS Bulletin*
    **20**(11), 53–56 (1995).
    <https://doi.org/10.1557/S0883769400045577>
[^skelly-1986]: D. W. Skelly and L. A. Gruenke, "Significant improvement
    in step coverage using bias sputtered aluminum", *Journal of Vacuum
    Science & Technology A* **4**(3), 457–460 (1986).
    <https://doi.org/10.1116/1.573905>
[^taylor-1998]: D. S. Taylor, M. K. Jain and T. S. Cale, "Deposition rate
    dependence of step coverage of sputter deposited aluminum-(1.5%)
    copper films", *Journal of Vacuum Science & Technology A* **16**(5),
    3123–3126 (1998). <https://doi.org/10.1116/1.581476>
[^gn-1994]: F. H. Gn, L. Liu and M. Guo, "Comparison study between
    tungsten and aluminum plug for submicrometer contact via
    manufacturing", *Proc. SPIE* **2335**, Microelectronic Manufacturing,
    98–106 (1994). <https://doi.org/10.1117/12.186049>
[^ono-1990]: H. Ono, Y. Ushiku and T. Yoda, "Development of a planarized
    Al-Si contact filling technology", *Proc. Seventh International IEEE
    VLSI Multilevel Interconnection Conference (VMIC 1990)*, pp. 76–82.
    <https://doi.org/10.1109/VMIC.1990.127847>
[^hariu-1989]: T. Hariu, K. Watanabe, M. Inoue, T. Takada and
    H. Tsuchikawa, "The Properties of Al-Cu/Ti Films Sputter Deposited at
    Elevated Temperatures and High DC Bias", *27th International
    Reliability Physics Symposium (IRPS 1989)*, pp. 210–214.
    <https://doi.org/10.1109/IRPS.1989.363388>
[^nishimura-1991]: H. Nishimura, T. Yamada and S. Ogawa, "Reliable
    submicron vias using aluminum alloy high temperature sputter
    filling", *Proc. Eighth International IEEE VLSI Multilevel
    Interconnection Conference (VMIC 1991)*, pp. 170–176.
    <https://doi.org/10.1109/VMIC.1991.152982>
[^pat-al-multistep-amat]: C.-R. Wang (Applied Materials), *Multistep
    sputtering process for forming aluminum layer over stepped
    semiconductor wafer*, US 5,108,570 A, filed 1990-03-30, granted
    1992-04-28.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5108570>
[^deshmukh-2003]: A. R. Deshmukh, "The effect of ratio of deposition
    times and via density on via fill in aluminum multilayer
    metallization", *Thin Solid Films* **444**(1–2), 132–137 (2003).
    <https://doi.org/10.1016/j.tsf.2003.08.041>
[^pat-forcefill-electrotech]: C. D. Dobson (Electrotech Ltd), *Method for
    filing [sic] substrate recesses using elevated temperature and pressure*,
    US 5,527,561 A, priority 1991-05-28, filed 1994-08-16, granted
    1996-06-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5527561>
[^dirks-1999]: A. G. Dirks, M. N. Webster, P. Turner, P. Rich and
    D. C. Butler, "On the mechanism of aluminum via fill by reflow and
    forcefill as studied by transmission electron microscopy", *Journal
    of Applied Physics* **85**(1), 571–577 (1999).
    <https://doi.org/10.1063/1.369491>
[^janssen-1998]: G. C. A. M. Janssen, J. F. Jongste, J. P. Lokker,
    A. H. Verbruggen and S. Radelaar, "Aluminium via-fill at elevated
    pressure and temperature", in *Fourth International Workshop on
    Stress Induced Phenomena in Metallization*, AIP, 1998, pp. 349–358.
    <https://doi.org/10.1063/1.54655>
[^pat-sloped-motorola]: R. K. Berglund, K. E. Mautz and R. Tyldesley
    (Motorola), *Sloped contact etch process*, US 4,698,128 A, filed
    1986-11-17, granted 1987-10-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4698128>
[^pat-taper-chartered]: E.-N. Chou (Chartered Semiconductor
    Manufacturing), *Enhancing step coverage by creating a tapered
    profile through three dimensional resist pull back*, US 5,308,415 A,
    filed 1992-12-31, granted 1994-05-03.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5308415>
[^bohr-1995]: M. T. Bohr, "Interconnect scaling — the real limiter to
    high performance ULSI", *IEDM 1995 Technical Digest*, pp. 241–244.
    <https://doi.org/10.1109/IEDM.1995.499187>
[^stamper-1998]: A. K. Stamper, M. B. Fuselier and X. Tian, "Advanced
    wiring RC delay issues for sub-0.25-micron generation CMOS", *Proc.
    IEEE 1998 International Interconnect Technology Conference (IITC)*,
    pp. 62–64. <https://doi.org/10.1109/IITC.1998.704752>
[^itrs-02]: International Technology Roadmap for Semiconductors, *2001
    Edition: Interconnect*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Interconnect.pdf>
[^chu-2001]: S.-F. Chu, K. W. Chew, W. B. Loh, Y. M. Wang, B. G. Onn,
    Y. Ju, J. Zhang and K. Shao, "High quality factor silicon-integrated
    spiral inductors achieved by using thick top metal with different
    passivation schemes", *2001 International Symposium on VLSI
    Technology, Systems, and Applications (VLSI-TSA)*, pp. 154–157.
    <https://doi.org/10.1109/VTSA.2001.934506>
[^hunter-2012]: S. Hunter, J. L. Clark, D. Hornberger and L. Rubio, "Use
    of Wire Bonding to Study Bond Pad Damage from Wafer Probe",
    *International Symposium on Microelectronics* **2012**(1), 384–395
    (IMAPS, 2012). <https://doi.org/10.4071/isom-2012-TP41>
[^marsh-2016]: J. Marsh, A. Doutre, K. Syndergaard, P. Brown, K. I. Hoo,
    E. De Jesus and S. Hunter, "Copper Ball Bond over a Variety of Probe
    Marks in Two Pad Aluminum Thicknesses", *2016 IEEE 66th Electronic
    Components and Technology Conference (ECTC)*, pp. 2228–2232.
    <https://doi.org/10.1109/ECTC.2016.382>
[^hess-2003]: K. J. Hess, S. H. Downey, G. B. Halt, T. Lee, L. L. Mercado,
    J. W. Miter, W. C. Ng and D. G. Wontor, "Reliability of bond over
    active pad structures for 0.13-μm CMOS technology", *53rd Electronic
    Components and Technology Conference (ECTC 2003)*, pp. 1344–1349.
    <https://doi.org/10.1109/ECTC.2003.1216469>
[^danzl-1997]: R. B. Danzl and A. McLaurin, "The use of concentrated
    hydrogen peroxide for the removal of a TiW ARC from aluminum bond
    pads", *Proc. Twenty-First IEEE/CPMT International Electronics
    Manufacturing Technology Symposium (IEMT 1997)*, pp. 99–104.
    <https://doi.org/10.1109/IEMT.1997.626884>
[^kwok-1990]: T. Kwok, C. Tan, D. Moy, J. J. Estabil, H. S. Rathore and
    S. Basavaiah, "Electromigration in a two-level Al-Cu interconnection
    with W studs", *Proc. Seventh International IEEE VLSI Multilevel
    Interconnection Conference (VMIC 1990)*, pp. 106–112.
    <https://doi.org/10.1109/VMIC.1990.127852>
[^matsuoka-1990]: F. Matsuoka, H. Iwai, K. Hama, H. Itoh, R. Nakata,
    T. Nakakubo, K. Maeguchi and K. Kanzaki, "Electromigration
    reliability for a tungsten-filled via hole structure", *IEEE
    Transactions on Electron Devices* **37**(3), 562–568 (1990).
    <https://doi.org/10.1109/16.47758>
[^ames-1970]: I. Ames, F. M. d'Heurle and R. E. Horstmann, "Reduction of
    Electromigration in Aluminum Films by Copper Doping", *IBM Journal
    of Research and Development* **14**(4), 461–463 (1970).
    <https://doi.org/10.1147/rd.144.0461>
[^knorr-1996]: D. B. Knorr and K. P. Rodbell, "The role of texture in
    the electromigration behavior of pure aluminum lines", *Journal of
    Applied Physics* **79**(5), 2409–2417 (1996).
    <https://doi.org/10.1063/1.361168>
[^rocke-1988]: M. Rocke and M. Schneegans, "Titanium nitride for
    antireflection control and hillock suppression on aluminum silicon
    metallization", *Journal of Vacuum Science & Technology B* **6**(4),
    1113–1115 (1988). <https://doi.org/10.1116/1.584306>
[^chaudhari-1974]: P. Chaudhari, "Hillock growth in thin films",
    *Journal of Applied Physics* **45**(10), 4339–4346 (1974).
    <https://doi.org/10.1063/1.1663054>
[^zlatanovic-1990]: D. Zlatanović and G. Davinić, "Influence of
    heat-treatment temperature and aluminum thickness on hillocks
    formation in thin aluminum films", *Vacuum* **40**(1–2), 157–159
    (1990). <https://doi.org/10.1016/0042-207X(90)90144-N>
[^taguchi-1998]: M. Taguchi, K. Maeda and J. Aoyama, "Improvement of
    filling capability by control of water outgassing from via holes in
    high-pressure aluminum reflow technology", in *Fourth International
    Workshop on Stress Induced Phenomena in Metallization*, AIP, 1998,
    pp. 407–412. <https://doi.org/10.1063/1.54662>
[^rossnagel-1991]: S. M. Rossnagel, D. Mikalsen, H. Kinoshita and
    J. J. Cuomo, "Collimated magnetron sputter deposition", *Journal of
    Vacuum Science & Technology A* **9**(2), 261–265 (1991).
    <https://doi.org/10.1116/1.577531>
[^pramanik-1990]: D. Pramanik and V. Jain, "Effect of underlayer on
    sputtered aluminum grain structure and its correlation with step
    coverage in submicron vias", *Proc. Seventh International IEEE VLSI
    Multilevel Interconnection Conference (VMIC 1990)*, pp. 332–334.
    <https://doi.org/10.1109/VMIC.1990.127888>
[^lee-2003]: W.-J. Lee and S.-K. Rha, "Effect of Underlayer on the Via
    Filling and the Microstructure of the Aluminum Film in Aluminum Plug
    Process", *Japanese Journal of Applied Physics* **42**(6A), 3372–3376
    (2003). <https://doi.org/10.1143/JJAP.42.3372>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
