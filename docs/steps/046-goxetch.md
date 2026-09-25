(step-046)=
# Step 046 — GOXETCH: Low V gate oxide etch

| | |
|---|---|
| **Step number** | 46 of 171[^steps-sheet] |
| **Step code** | `GOXETCH` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | {term}`FEOL` — SONOS and gate dielectrics |
| **Previous step** | {ref}`NCHI <step-045>` |
| **Next step** | {ref}`LVGOX <step-047>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** strips the thick gate oxide from the 1.8 V regions, using
  the resist already in place from `NCHI`.
* **Why:** a thin oxide cannot be grown on top of the thick one, so
  the thick oxide has to be removed first.
* **Public numbers:** none published for SKY130.
* **Likely SkyWater tool:** Akrion Gamma batch wet bench — strong
  (tool); inference (assignment).[^skw-01]
* **Not public:** HF dilution, etch time, and the resulting undercut
  (→ Open questions).
:::

## What this step is

`GOXETCH` strips the thick gate oxide grown at {ref}`GOX100 <step-043>`
from the low-voltage regions. With the {ref}`LVOM <step-044>` resist
still in place — it has just served as the mask for
{ref}`NCHI <step-045>` — the wafer is dipped in dilute hydrofluoric acid
or buffered HF until the thick oxide in the windows is
gone and bare silicon is exposed. (The thick oxide is thinner than the PDK's 110 Å
finished thick-oxide figure[^pdk-hv] by an amount that is not public;
see {ref}`GOX100 <step-043>`.) Under the resist, over the 5 V and
high-voltage transistors, the oxide stays. The resist is then stripped
and the wafer cleaned for the thin gate oxidation at
{ref}`LVGOX <step-047>`. It is the etch half of the {term}`dual-gate-oxide <dual gate oxide>`
process described on the {ref}`category-oxidation` page: "a mask and wet
etch to strip it from the low-voltage active areas".

:::{figure} /_static/figures/gates-046-goxetch.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step photoresist covers the left-hand part of the drawing and a thick oxide film covers the right-hand active area in the window, over a hatched band. After it the resist is gone, the thick oxide remains on the left-hand active area, and the right-hand active silicon is bare.
:width: 560px
:name: fig-gates-046-goxetch

Before, the LVOM resist with the thick oxide still in its window; after, the oxide gone from the 1.8 V area down to the silicon, the resist gone, and the thick oxide kept on the 5 V area. The etch is drawn as stopping at the silicon and leaving the trench oxide as it is; the undercut at the resist edge and any loss of trench oxide are not public and are not drawn. The resist is drawn stripped because this page treats the strip and clean as part of this step. The NMOS channel implant of NCHI is unchanged. The P-well is drawn but not labelled, and the liner oxide is drawn faded. Not to scale.
:::

Both Cypress flows describe the operation, and both patents are shown as
in force: they give the etchant, the order of etch, strip and clean, and
what the clean must not attack. The two passages are in the collapsed
note below. Following the sequence they set out, this reference treats
the strip and clean as part of this step.

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
In one, "The thick, first gate oxide 240 is etched in the exposed
regions by using a BOE etch … and the patterned mask layer 242 is then
removed"; afterwards "the substrate 206 is cleaned using a wet etch that
does not etch oxide in order to protect the first gate oxide 240 of the
HV MOS transistor 212, and the blocking oxide layer 238 of the gate
stack 236".[^pat-04] In the other, "any previously formed gate insulator
layers, such as gate insulator layer 314 … are selectively removed to
expose the substrate 302", a pre-clean is done "while the photoresist
layer 318 protects the ONO charge trapping dielectric stack 306", and
"the photoresist layer 318 is stripped … for example with conventional
piranha clean and/or plasma ash operations, subsequent to the selective
removal of the gate insulator layer(s)".[^pat-03]
:::

## Step category

`GOXETCH` is an {ref}`Etch <category-etch>` step of the *wet oxide
etch* type, like {ref}`TUNME <step-039>` and
{ref}`SACETCH <step-095>`. The category page gives the reasoning and
marks it as a reading: dilute HF "is the natural tool for, and we
infer is used at, stripping the thick gate oxide from the low-voltage
active areas … because a plasma would damage the exposed silicon"
({ref}`category-etch`). It is the most consequential wet etch in the flow,
because the silicon it exposes becomes the channel of every 1.8 V
transistor and the oxide edge it leaves becomes the boundary between
the two gate oxides.

## Why this step exists

The 1.8 V transistors need a ~4 nm gate oxide (the 1.8 V NMOS model
carries `toxe = 4.148e-9`[^pdk-model-nfet01v8]).

The thick oxide on
their active areas is thinner than the PDK's 110 Å finished
thick-oxide figure[^pdk-hv] by an amount that is not public. It must be
removed before the
thin one can be grown. A thin oxide cannot simply be grown on top:
oxidation adds to an existing oxide by the {term}`Deal–Grove <Deal–Grove model>` law rather than
replacing it ({ref}`category-oxidation`). The removal has to be:

* **Complete**, because any residue becomes part of the thin oxide;
* **Damage-free**, because the exposed surface is the channel. The
  plasma damage that ion bombardment leaves — "a few nanometres of
  damaged, sometimes amorphised silicon" ({ref}`category-etch`) —
  would sit exactly under the 1.8 V gate;
* **Selective and gentle to the resist edge**, because HF creeping
  along the resist–oxide interface thins the thick oxide beside the
  boundary.

  The pairing of resist and wet etch for dual gate oxide is
  a recognised integration problem;[^beverina-2003] the thinning of the
  thick oxide at {term}`STI` edges and at the mask boundary in a dual-oxide
  process has been characterised[^lee-1999-icvc] and STI schemes
  proposed to compensate it.[^kim-2001]

Without `GOXETCH` all transistors would carry the thick oxide and the
1.8 V core would not work as designed.

## How it is typically performed

*An industry-generic thick-oxide strip for a dual-gate-oxide process
in a 200 mm, 130 nm-era fab (SKY130's recipe is not public):*

1. **Wet etch with resist.** Dilute HF — the dilutions the Cypress
   patent names are in the collapsed note below this list — or
   surfactant-containing BOE in a wet bench or single-wafer spray
   tool.

   Rate control is the issue: 6:1 BOE etches thermal oxide at
   "approximately 2 nanometres per second at 25 degrees
   Celsius".[^wiki-boe] That is a 10 nm film in five seconds, so dilute
   solutions with rates of nanometres per minute are used. The rate
   follows the HF and HF₂⁻ concentrations[^judge-1971] and, at very low
   concentration, the dissociation state of the acid.[^kikuyama-1994]
   Monk, Soane and Howe give the kinetics and a model for HF etching
   of oxide films.[^monk-1994] What Cypress uses here is in the same
   note.
2. **{term}`Over-etch <over-etch>`.** Timed to clear the thickest oxide on the wafer plus
   margin; the hydrophobic (dewetting) silicon surface is the classic
   visual sign that the oxide is gone. Every second of over-etch
   widens the undercut under the resist edge, so the margin is kept
   small and the bath is tracked with etch-rate monitors
   ({ref}`category-etch`).
3. **Rinse.** DI water; the bare silicon is now hydrogen-terminated
   and hydrophobic.[^cerofolini-1998]
4. **Resist strip.** Oxygen-plasma {term}`ash` and {term}`SPM`, the
   combination the Cypress patent names (collapsed note below this list)
   — the resist has seen one light implant and an HF bath
   ({ref}`category-strip`).
5. **Pre-gate clean.** An RCA-type clean whose final surface state
   is chosen for the thin oxide: {term}`SC-1` for particles, {term}`SC-2` for
   metals,[^wiki-rca] then either an HF-last (hydrogen-terminated
   silicon) or a thin chemical oxide.

   Two constraints are public. The
   clean must not remove the thick oxide that is now exposed, and it
   must not attack the {term}`ONO` {term}`blocking oxide` of the memory
   cells. What the two Cypress patents say about each, including an
   etch rate and the dilution they prefer, is in the collapsed note
   below this list. Kern's
   review gives the chemistry of these cleans,[^kern-1990] Ohmi the
   room-temperature alternatives,[^ohmi-1996] and the handbook edited by
   Reinhardt and Reidy the pre-gate practice.[^reinhardt-2010]
6. **Queue time.** Straight to the thin oxidation; bare silicon
   regrows native oxide within hours (industry practice; Reinhardt and
   Reidy[^reinhardt-2010]).

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
The Cypress patent names "a 50:1 hydrofluoric (HF) wet etch" alongside
10:1 and 20:1 BOE, and uses "a BOE etch" here; its clean is "a wet etch
that does not etch oxide".[^pat-04] The resist is stripped "for example
with conventional piranha clean and/or plasma ash operations"; SC-1
etches the blocking oxide at "approximately 0.2 to 0.3 nm/minute" and
can roughen or pit it, so that an "ultra-dilute SC1" is
preferred.[^pat-03]
:::

## Machines typically used

* **{ref}`Automated wet bench <machine-wet-bench>`** with dilute-HF/BOE, SPM, SC-1 and SC-2
  tanks (Akrion, DNS/SCREEN, SCP), a **{ref}`spray processor <machine-wet-bench>`** (FSI
  Mercury) or a **{ref}`single-wafer wet tool <machine-single-wafer-spin-processor>`** (SEZ/Lam Da Vinci)
  ({ref}`category-etch`, {ref}`category-strip`).
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** for the strip.
* **{ref}`Ellipsometer <machine-film-thickness-metrology>`** for etch-rate monitors; **{ref}`particle scanner <machine-defect-inspection>`**
  after the clean.

## Machines likely used at SkyWater

| Tool | Evidence |
|---|---|
| Akrion Gamma batch wet bench | strong (tool); inference (assignment) |
| DNS wet bench | strong (existence); inference (assignment) |
| FSI Mercury / SEZ 223 / Da Vinci | strong (existence) |
| GaSonics PEP / Iridia / Mattson Aspen II ashers | strong (existence) |

* **Akrion Gamma batch wet bench**
  - *SkyWater says:* lists "Sulfuric, SC1, phosphoric,
    BOE, spin or IPA dry".[^skw-01]
  - *Tool exists:* **strong** — the bench carries the chemistry the
    Cypress patent names for this step (the collapsed note above).
  - *Runs this step:* **inference**.
* **DNS wet bench**
  - *SkyWater says:* lists "industry standard HF/SC1/SC2"; "dilute HF-last
    with IPA dry".[^skw-01]
  - *Tool exists:* strong for existence — a pre-gate clean with
    HF-last is exactly the option listed.
  - *Runs this step:* inference.
* **FSI Mercury / SEZ 223 / Da Vinci**
  - *SkyWater says:* lists "HF/SC1/SC2 rotational" and "HF, DSP+HF,
    titration controlled".[^skw-01] The SEZ is also named in a
    technician profile.[^skw-07]
  - *Tool exists:* strong for existence.
* **GaSonics PEP, Iridia, Mattson Aspen II ashers**
  - *SkyWater says:* lists them.[^skw-01]
  - *Tool exists:* strong for existence.

## Resources required

* **Hydrofluoric acid (49 %)** ({ref}`wet chemicals <material-wet-chemicals>`) diluted, or **BOE** (NH₄F/HF) with
  **surfactant**[^wiki-boe] (the collapsed note above); {term}`BOE` is
  on SkyWater's Akrion list.[^skw-01]
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide,
  hydrochloric acid** for SPM/SC-1/SC-2.[^wiki-rca]
* **{ref}`Oxygen <material-process-gases>`, nitrogen, {ref}`forming gas <material-anneal-ambients>`** for the ash.[^skw-01]
* **{ref}`Ultrapure DI water <material-ultrapure-water>`, isopropanol, nitrogen.**
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`NCHI <step-045>` (implant through the same
  window).
* Next: {ref}`LVGOX <step-047>` (thin oxide grown on the cleared
  silicon).
* Depends on: the oxide being removed, {ref}`GOX100 <step-043>`.
* Same category: sister wet oxide etches, {ref}`TUNME <step-039>`,
  {ref}`SACETCH <step-095>`.
* Mask: {ref}`LVOM <step-044>`.
* Category pages: {ref}`Etch <category-etch>`,
  {ref}`Resist strip / clean <category-strip>`,
  {ref}`Thermal oxidation <category-oxidation>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,093,128 B2 <patent-gp40072804>` — in force
* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, SPICE model of `nfet_01v8` — `toxe`
  4.148 nm.[^pdk-model-nfet01v8]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — Akrion, DNS, FSI and SEZ wet
  tools; ashers.[^skw-01]
* [SkyWater, *A Day in the Life of a SkyWater Maintenance Technician*](<https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>)
  — the SEZ etcher.[^skw-07]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — BOE
  etch of the first gate oxide through the mask; the oxide-safe clean
  before the second oxide.[^pat-04]
* Koutny et al. (Cypress), US 8,093,128 — selective removal of the
  first gate insulator, the protected pre-clean, the strip, and SC-1's
  effect on the blocking oxide.[^pat-03]
:::

### High-level understanding

* [Wikipedia, *Buffered oxide etch*](<https://en.wikipedia.org/wiki/Buffered_oxide_etch>) — BOE and its etch rate.[^wiki-boe]
* [Wikipedia, *RCA clean*](<https://en.wikipedia.org/wiki/RCA_clean>) — SC-1 and SC-2.[^wiki-rca]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  wet etching and cleaning.[^txt-02]

### Deep dive

* [Judge, *J. Electrochem. Soc.* 1971](<https://doi.org/10.1149/1.2407835>) — SiO₂ dissolution kinetics in
  acidic fluoride solutions.[^judge-1971]
* [Kikuyama et al., *J. Electrochem. Soc.* 1994](<https://doi.org/10.1149/1.2054733>) — extremely dilute HF
  and its etching reaction.[^kikuyama-1994]
* [Monk, Soane and Howe, *J. Electrochem. Soc.* 1994](<https://doi.org/10.1149/1.2054696>) — HF etching of
  oxide films: observations and model.[^monk-1994]
* [Cerofolini, *Appl. Surf. Sci.* 1998](<https://doi.org/10.1016/S0169-4332(98)00182-2>) — hydrogen termination after HF
  etching.[^cerofolini-1998]
* [Beverina et al. (STMicroelectronics), *Solid State Phenomena* 2003](<https://doi.org/10.4028/www.scientific.net/SSP.92.235>) —
  the resist / wet-etch couple for dual gate oxide.[^beverina-2003]
* [Lee et al., ICVC 1999](<https://doi.org/10.1109/ICVC.1999.820895>) — gate oxide thinning at the STI edge in the
  dual gate oxide process.[^lee-1999-icvc]
* [Kim et al., SSDM 2001](<https://doi.org/10.7567/SSDM.2001.A-6-6>) — an STI scheme to compensate thick-oxide
  thinning at the corner.[^kim-2001]
* [Lee (Hyundai), *Electrochem. Solid-State Lett.* 1999](<https://doi.org/10.1149/1.1390957>) — a dual gate
  oxide process with improved {term}`gate-oxide integrity <gate oxide integrity>`.[^lee-1999]
* [Kern, *J. Electrochem. Soc.* 1990](<https://doi.org/10.1149/1.2086825>) — wafer-cleaning chemistry.[^kern-1990]
* [Ohmi, *J. Electrochem. Soc.* 1996](<https://doi.org/10.1149/1.1837133>) — room-temperature
  cleaning.[^ohmi-1996]
* [Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing*](<https://doi.org/10.1002/9781118071748>) — pre-gate cleans.[^reinhardt-2010]

## Open questions

* **Etch chemistry.** HF dilution, etch time, over-etch and the
  resulting undercut at the thick/thin boundary are not public.
* **Pre-gate clean endpoint.** Whether the pre-gate clean ends
  HF-last or with a chemical oxide is not public; SkyWater's DNS bench
  offers "dilute HF-last".[^skw-01]
* **Where the resist is stripped.** Where the resist is stripped is
  not stated publicly; this page treats the strip as part of this
  step.
* **ONO protection.** How the ONO blocking oxide is protected during
  this etch and clean (resist coverage, sacrificial cap, or
  oxide-safe chemistry) is not public; both Cypress approaches are
  described above.

<!-- footnotes -->

[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^pdk-model-nfet01v8]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_01v8__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice>
[^beverina-2003]: A. Beverina, I. Guilmeau, J. P. Carrere, N. Emonet,
    F. Guyader, V. Huard, S. Petitdidier and R. Velard, "'Resist / Wet
    Etch' Couple for Dual Gate Oxide", *Solid State Phenomena* **92**,
    235–238 (2003). <https://doi.org/10.4028/www.scientific.net/SSP.92.235>
[^lee-1999-icvc]: S.-W. Lee, I. H. Cho, S. H. Park, H. G. Choi,
    N. G. Kim, J.-K. Kim, S. B. Han and K. Lee, "Gate oxide thinning
    effects at the edge of shallow trench isolation in the dual gate
    oxide process", *ICVC '99: 6th International Conference on VLSI
    and CAD*, pp. 249–252. <https://doi.org/10.1109/ICVC.1999.820895>
[^kim-2001]: S.-H. Kim, S.-H. Kim, S.-E. Kim, M.-S. Kim, J.-H. Park and
    E.-S. Kim, "New STI Scheme to Compensate Gate Oxide Thinning at STI
    Corner Edge for the Devices Using Thick Dual Gate Oxide", *Extended
    Abstracts of the 2001 International Conference on Solid State
    Devices and Materials (SSDM)*, 2001.
    <https://doi.org/10.7567/SSDM.2001.A-6-6>
[^wiki-boe]: Wikipedia, *Buffered oxide etch*.
    <https://en.wikipedia.org/wiki/Buffered_oxide_etch>
[^judge-1971]: J. S. Judge, "A Study of the Dissolution of SiO₂ in
    Acidic Fluoride Solutions", *Journal of The Electrochemical
    Society* **118**(11), 1772 (1971). <https://doi.org/10.1149/1.2407835>
[^kikuyama-1994]: H. Kikuyama, M. Waki, M. Miyashita, T. Yabune,
    N. Miki, J. Takano and T. Ohmi, "A Study of the Dissociation State
    and the SiO₂ Etching Reaction for HF Solutions of Extremely Low
    Concentration", *Journal of The Electrochemical Society* **141**(2),
    366–374 (1994). <https://doi.org/10.1149/1.2054733>
[^monk-1994]: D. J. Monk, D. S. Soane and R. T. Howe, "Hydrofluoric
    Acid Etching of Silicon Dioxide Sacrificial Layers: I. Experimental
    Observations" and "II. Modeling", *Journal of The Electrochemical
    Society* **141**(1), 264–269 and 270–274 (1994).
    <https://doi.org/10.1149/1.2054696>, <https://doi.org/10.1149/1.2054697>
[^cerofolini-1998]: G. F. Cerofolini, "A study of the ionic route for
    hydrogen terminations resulting after SiO₂ etching by concentrated
    aqueous solutions of HF", *Applied Surface Science* **133**(1–2),
    108–114 (1998). <https://doi.org/10.1016/S0169-4332(98)00182-2>
[^wiki-rca]: Wikipedia, *RCA clean*. <https://en.wikipedia.org/wiki/RCA_clean>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14. <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^lee-1999]: S.-W. Lee, "Novel Dual Gate Oxide Process with Improved
    Gate Oxide Integrity Reliability", *Electrochemical and Solid-State
    Letters* **3**(1), 56 (1999). <https://doi.org/10.1149/1.1390957>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
