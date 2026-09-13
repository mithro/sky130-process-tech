(step-150)=
# Step 150 — CAPILD2: Capacitor ILD oxynitride deposition

| | |
|---|---|
| **Step number** | 150 of 171[^steps-sheet] |
| **Step code** | `CAPILD2` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`WTIAL4 <step-149>` |
| **Next step** | {ref}`CAPTIW2 <step-151>` |

## What this step is

`CAPILD2` deposits the dielectric of SKY130's second
{term}`metal–insulator–metal (MiM) capacitor <MiM capacitor>`. Straight after the blanket
metal-4 stack of {ref}`WTIAL4 <step-149>` is sputtered — and before that
metal is patterned — a thin dielectric film is laid over the whole
wafer by {term}`PECVD`. This reference describes the film as a PECVD
silicon {term}`oxynitride`; the public record does not single that
material out — SkyWater lists PECVD oxide, nitride and oxynitride with
"range of R.I." options,[^skw-01] PECVD nitride and oxynitride have both
served as MiM dielectrics,[^kar-roy-1999][^ng-2003] and the PDK does
not name the material. A thin top-plate film follows at
{ref}`CAPTIW2 <step-151>`; the two are cut into capacitor top
plates by the second capacitor mask and etch ({ref}`CAP2M <step-152>`,
{ref}`CAP2ME <step-153>`), and only then is metal 4 patterned
({ref}`MM4 <step-154>`, {ref}`MM4E <step-155>`). The sequence repeats
the first capacitor module one metal level higher
({ref}`CAPILD <step-135>` to {ref}`CAPME <step-138>`).

The PDK documents this second capacitor in several places. Its device
page describes the MiM as "a thin dielectric over metal, followed by a
thin conductor layer on top of the dielectric", lists "CAPM over
Metal-3" and "CAP2M over Metal-4" as the two constructions, and says
that "The constructions are identical, and the capacitors may be
stacked to maximize total capacitance"; it names the cells
`sky130_fd_pr__cap_mim_m3__base` and `sky130_fd_pr__cap_mim_m4__base`
and gives the second capacitor its own parameters, `CMIM2A` 2 fF/µm²
(limits 1.8–2.2), `CMIM2P` 0.19 fF/µm and a "MiM2 top plate sheet
resistance" of 5.8 Ω/sq, identical to the first.[^pdk-07] The layer
table defines `cap2m` (GDS 97:44) as "MiM capacitor plate over
metal 4",[^pdk-06] the process stack diagram draws `cap2m` between
`metal4` and `metal5` beside `via4`,[^pdk-04] and the device's
cross-section — drawn for the "stacked" arrangement — labels the thin
film under `CAP2M` "CAPILD", as it labels the film under
`CAPM`.[^pdk-07]

As at the first capacitor, nothing public gives the film's thickness
or composition. SkyWater lists "PECVD silane oxide/nitride/oxynitride,
C1" with "low temp" and "range of R.I." options.[^skw-01] The
capacitance density bounds the thickness: with
{math}`C/A = \varepsilon_0 k / d`, 2 fF/µm² requires
{math}`d \approx 4.4\,\mathrm{nm} \times k` — about 18 nm for
{math}`k = 4`, 22–27 nm for an oxynitride of {math}`k \approx 5`–6 and
33 nm for the {math}`k = 7.5` the stack diagram gives its nitride
films[^pdk-04] (our arithmetic with an assumed permittivity). Because
the PDK gives both capacitors the same area capacitance and calls them
identical,[^pdk-07] we read this film as the same deposition as
{ref}`CAPILD <step-135>` (inference).

Published measurements bear on that reading without settling it. The
SKY130 raw-data repository holds capacitance–voltage sweeps of the test
tile's "CAP2M over M4" capacitors beside the first-level
ones.[^raw-data-testtile-pads][^raw-data-passives] The two large
second-level capacitors (11 plates, 17 600 µm²) measure 35.27 pF and
35.29 pF at 0 V, 2.00 fF/µm² including periphery, against 33.26 pF and
33.28 pF for the first-level ones; one of the two second-level files is
named `large_mim_cap`, but its module is the one the pad list describes
as CAP2M over M4, and its value matches the other second-level
capacitor. The area-intensive structures differ by only about 1 %
(1.91 against 1.89 fF/µm² including periphery), while the second-level
periphery-intensive structure measures less than its first-level
counterpart (9.91 against 10.37 pF), so the levels do not differ by a
simple area capacitance, and an area-plus-periphery model fitted to the
three second-level structures leaves errors of up to about 4 % and a
periphery term close to zero. Fitted over
±3.3 V, their quadratic voltage coefficients are +47 to +51 ppm/V²,
against +32 to +40 ppm/V² at the first level (our extraction from the
published measurements, with no correction for pad and wiring
capacitance; the files record no measurement frequency, temperature,
date or wafer).[^raw-data-passives]

**Where the public record is inconsistent.** Other PDK tables do not
match this picture. The mask table lists "Capacitor MiM, CAPM" but no
second capacitor mask,[^pdk-05] the minimum-CD table gives only
`CAPMCD` and `CAPMCDSP`,[^pdk-03] and the periphery rules contain a
`capm` rule set, phrased in terms of `met2` and `via2`, and no rule
set for `cap2m` at all.[^pdk-periph] The via-2 rule table says via 2
connects "met2/capm to met3 in the SKY130DI* flow",[^pdk-periph] and
the extraction page lists a two-terminal
`sky130_fd_pr__cap_mim_m3_2` and a three-terminal
`sky130_fd_pr__model__cap_mim` with via-2, metal-3 and "capm-m2"
parasitic terms.[^pdk-08] Those texts describe a capacitor one level
lower than the device page, layer table and stack diagram do, and none
of them describes `cap2m`. The PDK's *Previous Nomenclature* page sides
with the device page: it describes an "s8phrc" variant as "The base
process plus dual MiM cap layers on metal 3 and metal 4".[^pdk-previous]
This page follows those sources and reads the other entries as carried
over from a flow variant with a capacitor over metal 2 (inference);
which extraction model corresponds to the metal-4 capacitor is not
stated in any public source.

## Step category

`CAPILD2` is a {ref}`Thin-film deposition <category-deposition>` step of
the *PECVD dielectric* class, and one of the two PECVD films in the
flow — with {ref}`CAPILD <step-135>` — deposited as a device layer, whose
thickness sets a capacitance the models promise rather than a spacing
the design rules bound. Uniformity, repeatability, pinhole density,
breakdown at 5 V across some 20–30 nm (a field of order 2 MV/cm; our
arithmetic from the 0–5.0 V model range[^pdk-07]), leakage and
{term}`voltage coefficient` matter as they would for a gate oxide, and
{term}`step coverage` does not, because the film lies on a blanket,
planar metal surface.

What is specific to this instance is its history and its partner. The
wafer under this film already carries a finished first capacitor, its
plates buried in the via-3 dielectric, and four aluminium levels. If
both capacitors are to be stacked, as the device page
allows,[^pdk-07] the two dielectrics must match: in a stacked pair the
PDK's cross-section connects the `CAPM` plate to the metal-4 shape
under `CAP2M` and the metal-3 bottom plate to the metal-5 shape over
`CAP2M`,[^pdk-07] so the two capacitors add in parallel and any
difference in thickness or permittivity between this film and
{ref}`CAPILD <step-135>` becomes a difference between the two halves.

## Why this step exists

* **Twice the capacitance per unit area.** A MiM capacitor at
  2 fF/µm²[^pdk-07] is large; the second capacitor, stacked over the
  first, doubles the capacitance available on the same footprint (our
  arithmetic from the identical `CMIMA` and `CMIM2A`[^pdk-07]). The
  test tile has such a pair — "CAPM-M3 and CAP2M-M4 capacitors, stacked
  on top of each other and connected together", 11 pairs of 40 × 40 µm
  plates[^raw-data-testtile-pads] — and its published measurement,
  68.78 pF, is 0.3–0.4 % more than the sum of the separately measured
  single-level large capacitors (our extraction).[^raw-data-passives] The
  Newport Fab patent builds exactly such a composite capacitor "perpendicular
  to the surface of the die", with upper and lower MiMs sharing a
  middle electrode and joined in parallel,[^pat-mim-stack-newportfab]
  and the TSMC patent cross-connects stacked plates through filled vias
  for the same purpose.[^pat-mim-stack-tsmc] Sul and Pyo model the RF
  behaviour of stacked MiMs.[^sul-2014]
* **An analogue capacitor with metal plates.** SkyWater and Google list
  MiM capacitors among SKY130's features — "Optional MiM capacitors" in
  the PDK README,[^pdk-10] "MiM Capacitor" in the S130 platform
  table[^skw-02] and "MiM capacitors" among the "normally optional
  features" SKY130 offers "as standard".[^ann-11] Metal plates have no depletion
  layer, so capacitance barely changes with bias; Kar-Roy et al.
  (Conexant) and Babcock et al. (Texas Instruments) describe PECVD-nitride
  MiMs added to aluminium back ends for mixed-signal and RF
  circuits,[^kar-roy-1999][^babcock-2001] and Ng et al. (Chartered)
  review MiM integration in Al–Cu and copper back ends.[^ng-2005]
* **Why the dielectric goes on unpatterned metal 4.** Depositing the
  dielectric on the blanket metal and defining the top plate before the
  bottom metal is etched gives a planar bottom plate with no sidewall
  under the thin film. The Newport Fab patent deposits its dielectric
  and top-plate metal on the unpatterned interconnect metal and etches
  the top plate before the bottom plate,[^pat-mim-newportfab] and the sequence described in this reference builds its capacitors in the same order; Freescale's patent, by contrast, builds a separate MiM
  stack over a planarised dielectric.[^pat-mim-freescale] The price is that the metal-4 etch must
  later cut through whatever dielectric remains ({ref}`MM4E <step-155>`).
* **Oxynitride, oxide or nitride.** PECVD silicon nitride gives the most
  capacitance per thickness, but Van Huylenbroeck et al. showed that
  PECVD dielectrics can give a frequency-dependent capacitance and
  investigated how to avoid it;[^van-huylenbroeck-2002] Ng, Chew and
  Chu compared PECVD nitride and oxynitride as MiM dielectrics and found
  both suitable.[^ng-2003] The composition — and hence {math}`k` — of a
  PECVD oxynitride is set by the N₂O/NH₃ flow ratio, which Denisse et al.
  showed covers the whole range from oxide to nitride,[^denisse-1986]
  and Bose, Bose and Basa relate composition to refractive
  index;[^bose-2002] SkyWater's "range of R.I."[^skw-01] is the public
  trace of a tunable film.
* **Voltage coefficient and charging.** The models are valid to
  5 V;[^pdk-07] Blonkowski and Gonon and Vallée give the physics of the
  {math}`C(V)` curvature in amorphous dielectrics.[^blonkowski-2007][^gonon-2007]
  Wang, Ackaert et al. showed that floating MiM capacitors are damaged by
  {term}`plasma charging` according to the antenna areas connected to each
  plate,[^wang-2004-mim] a concern for every plasma step between this
  deposition and the via that finally connects the plate.

Without `CAPILD2` there would be nothing between metal 4 and the
top-plate film of {ref}`CAPTIW2 <step-151>`, and the second capacitor mask would define a
short rather than a capacitor.

## How it is typically performed

An industry-generic PECVD MiM-dielectric deposition on an aluminium
back end (SKY130's recipe is not public); the sequence is that of
{ref}`CAPILD <step-135>`.

1. **Surface.** The wafer comes from the {term}`PVD` cluster with the
   TiW cap of {ref}`WTIAL4 <step-149>` exposed; that surface is the
   bottom electrode, and its roughness and cleanliness set the leakage.
   The Philips patent treats the bottom electrode in an ammonia plasma
   before the insulator is deposited,[^pat-mim-philips] and the queue
   time from PVD to deposition is limited (industry practice[^txt-05]).
2. **Chamber and temperature.** A single-wafer or multi-station PECVD
   reactor at 300–400 °C (industry-typical for films on
   aluminium[^txt-05][^chapple-sokol-1989]); SkyWater's "C1" silane
   chamber with its "low temp" option[^skw-01] is the candidate.
3. **Chemistry.** SiH₄ with N₂O and NH₃ (and N₂ or He) in an RF plasma;
   the N₂O:NH₃ ratio moves the film between oxide and nitride, with
   refractive index and permittivity following
   composition.[^denisse-1986][^bose-2002] Lieberman and Lichtenberg
   treat the discharge physics.[^lieberman-2005]
4. **Thickness.** Not public; 18–33 nm by the arithmetic above for
   2 fF/µm²,[^pdk-07] controlled to a few per cent because capacitance
   scales inversely with it. For a stacked pair the target is the same
   as {ref}`CAPILD <step-135>` (inference from the identical
   specification[^pdk-07]).
5. **Thermal budget.** By this step the first capacitor has already
   been through the via-3 dielectric, tungsten and metal-4 depositions
   (the first capacitor lies below via 3 and metal 4 on the PDK's stack
diagram[^pdk-04]); the aluminium limit of roughly
   400–450 °C (industry-typical[^txt-05]) bounds this deposition and
   every later one.
6. **Metrology.** Thickness and refractive index by ellipsometry on
   monitors; capacitance density, leakage, breakdown, {math}`C(V)` and
   matching on capacitor test structures at {term}`e-test`, against the
   `CMIM2A` and `CMIM2P` limits.[^pdk-07]

## Machines typically used

* **{ref}`PECVD dielectric system <machine-pecvd>`**, 200 mm: Novellus Concept One/Two or
  Sequel,[^novellus-history] Applied Materials Producer or Centura
  DxZ[^amat-10k] ({ref}`category-deposition`).
* **{ref}`Spectroscopic ellipsometer <machine-film-thickness-metrology>`** for thickness and index; **{ref}`C–V and leakage probers <machine-parametric-tester>`** at e-test.

## Machines likely used at SkyWater

* **PECVD silane "C1" chamber.** SkyWater lists "PECVD silane
  oxide/nitride/oxynitride, C1" with low-temperature and
  refractive-index options.[^skw-01] Strength: **strong** for the
  capability; the assignment of this chamber to this step, and the
  reading of "C1" as a Novellus Concept One,[^novellus-history] are
  **inferences**.
* **PECVD TEOS "C2 and Producer"**[^skw-01] is an oxide source; it
  would fit only if the dielectric were an oxide (weak).
* SkyWater's "HP 4062UX" parametric tester with "capacitance"
  measurement[^skw-01] is the public candidate for the capacitor
  e-test (inference).

## Resources required

* **Silane, nitrous oxide, ammonia**, with **nitrogen or helium**
  diluent.[^denisse-1986][^wiki-pecvd] Gas suppliers named in SkyWater's
  filings: Air Products and Praxair (2021 S-1), Linde and Airgas (fiscal
  2023 10-K).[^sec-01][^sec-02]
* **NF₃** for the chamber clean; **nitrogen** purge.
* **{ref}`Showerhead, heater and liner consumables <material-hardware-consumables>`**; **{ref}`monitor wafers <material-substrates>`** with
  the metal-4 stack for thickness and capacitance checks.

## Related steps and cross-references

* Previous: {ref}`WTIAL4 <step-149>` (the metal-4 stack that is the
  bottom plate). Next: {ref}`CAPTIW2 <step-151>` (the top-plate metal),
  then {ref}`CAP2M <step-152>` and {ref}`CAP2ME <step-153>`.
* The etch that later removes this film outside the capacitors:
  {ref}`MM4E <step-155>`; the via that contacts the finished top plate:
  {ref}`VIM4 <step-159>`, {ref}`VIM4E <step-160>`.
* The first capacitor, whose dielectric this repeats:
  {ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`,
  {ref}`CAPM <step-137>`, {ref}`CAPME <step-138>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Device Details* — MiM construction, "CAP2M over
  Metal-4", "identical" constructions that "may be stacked"; `CMIM2A`,
  `CMIM2P`, MiM2 top-plate 5.8 Ω/sq; the stacked `cap_mim`
  cross-section.[^pdk-07]
* SkyWater PDK, *Layers Reference* — `cap2m` 97:44 "MiM capacitor
  plate over metal 4".[^pdk-06]
* SkyWater PDK, *Process stack diagram* — `cap2m` between `metal4` and
  `metal5`; nitride permittivities 7.3–7.5.[^pdk-04]
* SkyWater PDK, *Masks* — "Capacitor MiM, CAPM" only.[^pdk-05]
* SkyWater PDK, *Criteria & Assumptions* — `CAPMCD` and `CAPMCDSP`
  only.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `capm` rules in terms of met2
  and via2; the via-2 function text; no `cap2m` rules.[^pdk-periph]
* SkyWater PDK, *Parasitic Layout Extraction* — the
  `sky130_fd_pr__cap_mim_m3_2` and `sky130_fd_pr__model__cap_mim`
  entries.[^pdk-08]
* SkyWater PDK, *Previous Nomenclature* — "s8phrc": "dual MiM cap
  layers on metal 3 and metal 4".[^pdk-previous]
* SkyWater PDK, README — "Optional MiM capacitors".[^pdk-10]
* SkyWater, S130 platform table — "MiM Capacitor".[^skw-02]
* SkyWater / Efabless, first MPW shuttle release.[^ann-11]
* SKY130 raw-data repository — C–V sweeps of the first-level,
  second-level and stacked MiM test capacitors and the pad list that
  describes them; the values quoted here are our
  extraction.[^raw-data-passives][^raw-data-testtile-pads]
* SkyWater, *Facilities & Capabilities* — PECVD silane
  oxide/nitride/oxynitride "C1"; HP 4062UX.[^skw-01]

### High-level understanding

* Wikipedia, *Capacitor*, *Silicon oxynitride*, *Silicon nitride*,
  *Plasma-enhanced chemical vapor deposition*.[^wiki-capacitor][^wiki-sion][^wiki-sin][^wiki-pecvd]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — PECVD
  dielectrics and passive components in the back end.[^txt-05]
* Edwards, WOSET 2020 — the SKY130 stack from the open-PDK
  side.[^ann-15]

### Deep dive

* Kar-Roy, Racanelli and Kempf (Newport Fab), US 7,078,310 — a
  composite of two stacked MiMs sharing a middle electrode, joined in
  parallel.[^pat-mim-stack-newportfab]
* Chang, Lee and Chen (TSMC), US 7,317,221 — stacked MiM plates
  cross-connected through filled vias.[^pat-mim-stack-tsmc]
* Sul and Pyo, *IEEE TED* 2014 — RF model extraction for stacked MiM
  capacitors.[^sul-2014]
* Kar-Roy et al. (Conexant), IITC 1999 — high-density PECVD-nitride
  MiMs for mixed-signal and RF circuits.[^kar-roy-1999]
* Babcock et al. (TI), *IEEE EDL* 2001 — analogue characteristics of
  PECVD-nitride MiMs.[^babcock-2001]
* Van Huylenbroeck et al. (IMEC), *IEEE EDL* 2002 — PECVD dielectrics
  for non-dispersive MiMs.[^van-huylenbroeck-2002]
* Ng, Chew and Chu (Chartered), *IEEE EDL* 2003 — PECVD nitride and
  oxynitride compared as MiM dielectrics.[^ng-2003]
* Ng et al. (Chartered), *IEEE TED* 2005 — MiM integration in Al–Cu and
  copper back ends reviewed.[^ng-2005]
* Denisse et al., *J. Appl. Phys.* 1986, and Bose, Bose and Basa,
  *Mater. Lett.* 2002 — composition and index of PECVD
  oxynitride.[^denisse-1986][^bose-2002]
* Blonkowski, *Appl. Phys. Lett.* 2007, and Gonon and Vallée, *Appl.
  Phys. Lett.* 2007 — the physics of the voltage
  coefficient.[^blonkowski-2007][^gonon-2007]
* Wang, Ackaert et al., *IEEE TED* 2004 — plasma-charging damage of
  floating MiM capacitors.[^wang-2004-mim]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028; Roberts and
  Huffman (Freescale), US 7,375,002; Olewine and Saiz (Philips),
  US 6,717,193 — three MiM constructions: on unpatterned interconnect
  metal, as a separate stack over planarised dielectric, and with an
  ammonia-plasma-treated TiN bottom electrode.[^pat-mim-newportfab][^pat-mim-freescale][^pat-mim-philips]
* Chapple-Sokol, Tierney and Batey (IBM), MRS 1989 — RF-power
  dependence of PECVD film properties.[^chapple-sokol-1989]
* Lieberman and Lichtenberg — the plasma physics of the
  deposition.[^lieberman-2005]

## Open questions

* The dielectric's composition, permittivity, thickness and deposition
  conditions are not public; 18–33 nm is our estimate from the PDK's
  2 fF/µm²[^pdk-07] with an assumed {math}`k`, and the reading that it
  repeats {ref}`CAPILD <step-135>` rests on the PDK calling the two
  constructions identical. The published test-tile measurements show
  the two levels within a few per cent of each other but not
  identical, and cannot separate thickness, permittivity and plate
  geometry.[^raw-data-passives]
* The PDK is inconsistent about the capacitors' levels: the device
  page, layer table and stack diagram place `cap2m` over metal 4, while
  the mask table, minimum-CD table and periphery rules have no `cap2m`
  entries and the `capm` rules, via-2 function text and extraction
  entries refer to metal 2, via 2 and metal
  3.[^pdk-07][^pdk-06][^pdk-04][^pdk-05][^pdk-03][^pdk-periph][^pdk-08]
  The level reading on this page is an inference, supported by the
  "dual MiM cap layers on metal 3 and metal 4" of the nomenclature
  page[^pdk-previous] and by the "CAP2M over M4" of the test tile's
  pad documentation.[^raw-data-testtile-pads]
* The design rules for `cap2m` — width, spacing, enclosure by metal 4
  and of via 4 — are not published.[^pdk-periph]
* Whether every SKY130 lot carries the second capacitor module is not
  public: the README lists "Optional MiM capacitors" and also counts MiM
  capacitors among the "normally *optional* features" SKY130 includes
  "as standard",[^pdk-10] and the capacitor mask is not
  flagged.[^pdk-05]

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
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
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page,
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^pdk-previous]: SkyWater PDK Authors, *Previous Nomenclature*,
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/previous.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-08-30. <https://www.skywatertechnology.com/cmos/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^ann-11]: SkyWater / Efabless, *First Google-Sponsored MPW Shuttle
    Launched at SkyWater with 40 Open Source Community Submitted
    Designs*, 2021-04-06.
    <https://skywatertechnology.com/press-releases/first-google-sponsored-mpw-shuttle-launched-at-skywater-with-40-open-source-community-submitted-designs>
[^ann-15]: R. T. Edwards (Efabless), "Google/SkyWater and the Promise of
    the Open PDK", *Workshop on Open-Source EDA Technology (WOSET)
    2020*. <https://woset-workshop.github.io/PDFs/2020/a03.pdf>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^wiki-capacitor]: Wikipedia, *Capacitor*.
    <https://en.wikipedia.org/wiki/Capacitor>
[^wiki-sion]: Wikipedia, *Silicon oxynitride*.
    <https://en.wikipedia.org/wiki/Silicon_oxynitride>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^pat-mim-stack-newportfab]: A. Kar-Roy, M. Racanelli and P. Kempf
    (Newport Fab, LLC), *Method for fabricating a high density composite
    MIM capacitor with flexible routing in semiconductor dies*,
    US 7,078,310 B1, filed 2004-05-19, granted 2006-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7078310>
[^pat-mim-stack-tsmc]: K.-L. Chang, C.-Y. Lee and C.-H. Chen (Taiwan
    Semiconductor Manufacturing Co.), *High density MIM capacitor
    structure and fabrication process*, US 7,317,221 B2, filed
    2003-12-04, granted 2008-01-08.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7317221>
[^sul-2014]: W. S. Sul and S. G. Pyo, "RF Characteristic Analysis Model
    Extraction on the Stacked Metal–Insulator–Metal Capacitors for Radio
    Frequency Applications", *IEEE Transactions on Electron Devices*
    **61**(8), 3011–3013 (2014). <https://doi.org/10.1109/TED.2014.2330842>
[^kar-roy-1999]: A. Kar-Roy, C. Hu, M. Racanelli, C. A. Compton,
    P. Kempf, G. Jolly, P. N. Sherman, J. Zheng, Z. Zhang and A. Yin,
    "High density metal insulator metal capacitors using PECVD nitride
    for mixed signal and RF circuits", *Proc. IEEE 1999 International
    Interconnect Technology Conference (IITC)*, pp. 245–247.
    <https://doi.org/10.1109/IITC.1999.787134>
[^babcock-2001]: J. A. Babcock, S. G. Balster, A. Pinto, C. Dirnecker,
    P. Steinmann, R. Jumpertz and B. El-Kareh, "Analog characteristics
    of metal-insulator-metal capacitors using PECVD nitride
    dielectrics", *IEEE Electron Device Letters* **22**(5), 230–232
    (2001). <https://doi.org/10.1109/55.919238>
[^van-huylenbroeck-2002]: S. Van Huylenbroeck, S. Decoutere,
    R. Venegas, S. Jenei and G. Winderickx, "Investigation of PECVD
    dielectrics for nondispersive metal-insulator-metal capacitors",
    *IEEE Electron Device Letters* **23**(4), 191–193 (2002).
    <https://doi.org/10.1109/55.992835>
[^ng-2003]: C. H. Ng, K. W. Chew and S. F. Chu, "Characterization and
    comparison of PECVD silicon nitride and silicon oxynitride
    dielectric for MIM capacitors", *IEEE Electron Device Letters*
    **24**(8), 506–508 (2003). <https://doi.org/10.1109/LED.2003.815154>
[^ng-2005]: C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
    Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
    Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
    <https://doi.org/10.1109/TED.2005.850642>
[^denisse-1986]: C. M. M. Denisse, K. Z. Troost, J. B. Oude Elferink,
    F. H. P. M. Habraken, W. F. van der Weg and M. Hendriks,
    "Plasma-enhanced growth and composition of silicon oxynitride
    films", *Journal of Applied Physics* **60**(7), 2536–2542 (1986).
    <https://doi.org/10.1063/1.337117>
[^bose-2002]: M. Bose, D. N. Bose and D. K. Basa, "Plasma enhanced
    growth, composition and refractive index of silicon oxynitride
    films", *Materials Letters* **52**(6), 417–422 (2002).
    <https://doi.org/10.1016/S0167-577X(01)00436-0>
[^blonkowski-2007]: S. Blonkowski, "Nonlinear capacitance variations in
    amorphous oxide metal-insulator-metal structures", *Applied Physics
    Letters* **91**(17) (2007). <https://doi.org/10.1063/1.2800291>
[^gonon-2007]: P. Gonon and C. Vallée, "Modeling of nonlinearities in
    the capacitance-voltage characteristics of high-k
    metal-insulator-metal capacitors", *Applied Physics Letters*
    **90**(14) (2007). <https://doi.org/10.1063/1.2719618>
[^wang-2004-mim]: Z. Wang, J. Ackaert, C. Salm, F. G. Kuper, M. Tack,
    E. De Backer, P. Coppens, L. De Schepper and B. Vlachakis,
    "Plasma-charging damage of floating MIM capacitors", *IEEE
    Transactions on Electron Devices* **51**(6), 1017–1024 (2004).
    <https://doi.org/10.1109/TED.2004.829518>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
[^pat-mim-freescale]: D. R. Roberts and G. L. Huffman (Freescale
    Semiconductor), *MIM capacitor in a semiconductor device and method
    therefor*, US 7,375,002 B2, filed 2005-06-28, granted 2008-05-20.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>
[^pat-mim-philips]: M. C. Olewine and K. F. Saiz (Koninklijke Philips
    Electronics), *Metal-insulator-metal (MIM) capacitor structure and
    methods of fabricating same*, US 6,717,193 B2, filed 2001-10-09,
    granted 2004-04-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6717193>
[^chapple-sokol-1989]: J. D. Chapple-Sokol, E. Tierney and J. Batey,
    "RF Power Dependence of the Material Properties of PECVD Silicon
    Dioxide", *MRS Proceedings* **165** (1989).
    <https://doi.org/10.1557/PROC-165-113>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles
    of Plasma Discharges and Materials Processing*, 2nd ed., Wiley,
    2005, ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-passives]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the poly, diffusion
    and well resistors, MiM capacitors, varactors and bipolar
    transistors of the test tile, IC-CAP `.mdm` files in
    `sky130_fd_pr/cells/unsorted/`, `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
