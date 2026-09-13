(step-095)=
# Step 095 — SACETCH: Sacrificial etch

| | |
|---|---|
| **Step number** | 95 of 171[^steps-sheet] |
| **Step code** | `SACETCH` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`LICM1E <step-094>` |
| **Next step** | {ref}`ALLY1 <step-096>` |

## What this step is

`SACETCH` — "sacrificial etch" — sits between the contact etch
({ref}`LICM1E <step-094>`) and the {term}`alloy anneal` ({ref}`ALLY1 <step-096>`)
that precedes the titanium {term}`liner`. The step list used in this
reference does not explain what the etch removes; we read it from its
place in the sequence this reference describes and from public
cleaning practice. At this point in the
sequence the contact holes are open, the resist has been (or is
being) stripped, and the next two steps are a hydrogen anneal and
the sputtering of titanium onto the silicon and poly at the bottom
of every hole. Whatever this etch removes, it is the last wet or dry
treatment those surfaces receive before metal meets them, and the
{ref}`category-etch` page reads it as "the sacrificial-oxide removal
before silicidation" performed in dilute HF, the same class as
{ref}`TUNME <step-039>` and {ref}`GOXETCH <step-046>`.

Three readings fit that place in the sequence; we set them out and
mark all three as inferences:

1. **Removal of the sacrificial oxide at the contact bottoms.** On
   the reading of the {ref}`SPOX <step-080>` and {ref}`LICM1E <step-094>`
   pages, a thin oxide — the implant screen of {ref}`SPOX <step-080>`
   and whatever {ref}`IOX45 <step-063>` left — lies on the
   source/drain silicon, and the plasma contact etch is stopped on or
   in it rather than driven into the silicon. A short dilute-HF dip
   then removes that oxide, together with the native oxide on the
   poly heads and the fluorocarbon-damaged skin of the oxide, leaving
   hydrogen-terminated silicon for the titanium. This is the
   "HF-last" pre-metal clean of the cleaning literature[^kern-1990][^ohmi-1996]
   and the reading the category page adopts.
2. **Removal of a deliberately grown sacrificial oxide.** Some flows
   grow or deposit a few nanometres of oxide in the open contacts
   after the plasma etch to consume the damaged silicon that Fonash
   and Oehrlein describe,[^fonash-1990][^oehrlein-1989] then strip it;
   the step would then be that strip. The {term}`thermal budget` argues
   against a grown oxide here (the junctions are 0.1 µm deep[^pdk-03]),
   but a low-temperature chemical oxide is possible.
3. **A sacrificial-layer etch in the resist sense.** The resist and
   the {term}`BARC` of {ref}`LICM1 <step-093>` are also sacrificial,
   and if their removal is folded into this step, the step could
   cover the strip-and-clean sequence. This reading is compatible with either
   of the first two.

On all three readings the chemistry that matters is a dilute
aqueous HF, and the surfaces that matter are the 0.08 µm contact
bottoms ("Standard Licon bottom CD"[^pdk-03]) at the foot of holes
about 0.5 µm deep.[^pdk-03]

## Step category

`SACETCH` is an {ref}`Etch <category-etch>` step of the *wet oxide
etch* type (inferred). The category page states the rule: dilute
HF is the tool where a thin oxide must be removed "cleanly and
gently with very high selectivity … because a plasma would damage
the exposed silicon". What distinguishes this instance from the
gate-oxide etches is geometry — the acid must reach the bottom of a
narrow, tapered hole and be rinsed out again — and consequence: the
oxide it leaves behind, if any, becomes a series resistance in every
contact, and the oxide it removes from the hole *walls* widens the
hole and thins the cap over the gates. Wet cleaning of contact holes
is treated in the handbooks edited by Reinhardt and Kern and by
Reinhardt and Reidy.[^reinhardt-2008][^reinhardt-2010]

## Why this step exists

The {term}`contact silicide` ({ref}`CSIL <step-098>`) forms only where
titanium touches clean silicon. The reasons a wet etch is inserted
before the liner:

* **Native and residual oxide.** A silicon surface exposed to air
  regrows an oxide within hours — Morita et al. measured the growth
  of native oxide on silicon in air and in water[^morita-1990] — and
  the plasma etch leaves a fluorine-rich, damaged oxide and
  fluorocarbon residue on every surface it touched.[^fonash-1990] A
  nanometre of oxide under the titanium raises the contact
  resistance and, worse, makes it variable; the specific contact
  resistivity models of Berger[^berger-1972] assume an intimate
  interface. Dilute HF removes these layers at rates of nanometres
  per minute, set by the HF and HF₂⁻ concentrations[^judge-1971] and,
  at very low concentration, by the acid's dissociation
  state,[^kikuyama-1994] and leaves a hydrogen-terminated
  surface.[^cerofolini-1998]
* **Screen oxide at the contact bottom.** If the plasma etch stops
  on the {ref}`SPOX <step-080>` oxide to protect the silicon (the
  {ref}`LICM1E <step-094>` reading), that oxide has to come off here;
  Monk, Soane and Howe give the kinetics of HF etching of thin oxide
  films in confined geometries.[^monk-1994]
* **What must survive.** The nitride {term}`spacers <spacer>` and the gate caps are
  exposed on the walls of the diffusion contacts; nitride etches
  slowly in HF, with the mechanism Knotter and Denteneer
  describe,[^knotter-2001] but the {term}`PSG` and {term}`cap oxide` of the walls
  etch quickly — doped glass faster than undoped — so the dip is
  short and the {term}`over-etch` small. Every nanometre removed from
  the walls widens the hole the liner must cover.
* **Particles and metals.** The clean also removes the polish
  residue and etch particles that the contact module cannot
  tolerate — the reason a wet clean rather than a plasma-only
  treatment is used; Kern's reviews set out the chemistry of the
  {term}`SC-1` and {term}`SC-2` steps that often accompany the
  HF.[^kern-1990][^kern-handbook]

Without `SACETCH`, on this reading, every contact would carry an
interfacial oxide and the {term}`silicide` anneal would give high, variable
contact resistance.

## How it is typically performed

An industry-generic pre-liner contact clean for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

1. **Strip.** If not already done at {ref}`LICM1E <step-094>`:
   oxygen or H₂/N₂ downstream plasma {term}`ash` of the resist and
   BARC at 40–270 °C (the range SkyWater's ashers list[^skw-01]),
   followed by a solvent or {term}`SPM` clean for the implant-free
   but fluorocarbon-crusted resist ({ref}`category-strip`).
2. **Polymer removal.** A dilute SC-1 or a proprietary
   post-etch-residue remover (amine/hydroxylamine class; SkyWater
   lists "EKS265, EKC270 solvents" [sic][^skw-01]) for fluorocarbon
   residue on the hole walls.
3. **HF dip.** Dilute HF, typically 100:1 to 500:1 (industry
   practice[^reinhardt-2010]), for tens of seconds — long enough to
   remove a few nanometres of oxide from the contact bottoms, short
   enough to take little from the walls; the etch rate follows the
   acid concentration.[^judge-1971] {term}`BOE` is the alternative where a
   more stable rate is wanted (6:1 BOE etches thermal oxide at
   "approximately 2 nanometres per second"[^wiki-boe], too fast for
   this purpose undiluted).
4. **Rinse and dry.** DI-water rinse and spin or IPA dry; the
   silicon is left hydrophobic and hydrogen-terminated.[^cerofolini-1998]
5. **Queue time.** The wafers go to the anneal and the liner within
   hours, before the native oxide regrows.[^morita-1990]
6. **Metrology.** Etch-rate monitors in the bath; contact-chain
   resistance after the plug module is the electrical proof
   ({ref}`category-test`).

## Machines typically used

* **Automated wet bench** with dilute-HF, SC-1 and solvent tanks
  (Akrion, DNS/SCREEN, SCP), a **spray processor** (FSI Mercury) or a
  **single-wafer wet tool** (SEZ/Lam Da Vinci) ({ref}`category-etch`).
* **Downstream asher** for the strip ({ref}`category-strip`).
* **Ellipsometer** for etch-rate monitors; **particle scanner**.

## Machines likely used at SkyWater

* **DNS wet bench and FSI Mercury.** SkyWater lists "DNS wet bench
  industry standard HF/SC1/SC2" and "FSI Mercury industry standard
  HF/SC1/SC2 rotational" under pre-clean.[^skw-01] Strength:
  **strong** for the existence of dilute-HF cleaning; assignment to
  `SACETCH` is an **inference** from its place in the sequence this
  reference describes, before the liner, and from the HF-last
  pre-metal clean of the cleaning literature.[^kern-1990]
* **SEZ 223 / Da Vinci.** Single-wafer "HF, DSP+HF, titration
  controlled".[^skw-01] Strength: strong for existence; medium for a
  contact-hole clean.
* **Akrion Gamma batch bench** ("Sulfuric, SC1, phosphoric, BOE,
  spin or IPA dry") and the **EKC265/EKC270** solvent bench.[^skw-01]
  Strength: strong for existence.
* Ashers: **GaSonics PEP, Iridia, Mattson Aspen II**.[^skw-01]
  Strength: strong for existence.

## Resources required

* **Dilute HF** (or **BOE**),[^wiki-hf][^wiki-boe] **DI water**,
  **IPA** or nitrogen for drying.
* **SC-1 chemicals** (NH₄OH, H₂O₂)[^wiki-rca] and/or a
  **post-etch-residue remover** (EKC265/EKC270 class[^skw-01]).
* **O₂, N₂, H₂/N₂** for the strip;[^skw-01] **SPM** (H₂SO₄/H₂O₂)
  if a wet strip is used.[^wiki-piranha]
* **Etch-rate monitor wafers** with thermal oxide.[^semi-m8]
* Chemical suppliers named by SkyWater: KMG Chemicals.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`LICM1E <step-094>` (the etch whose residue and
  stop oxide this step removes). Next: {ref}`ALLY1 <step-096>`,
  then {ref}`TI/TIN1 <step-097>` (the liner that must meet clean
  silicon) and {ref}`CSIL <step-098>`.
* The oxide that may be the "sacrificial" film: {ref}`SPOX <step-080>`,
  {ref}`IOX45 <step-063>`.
* The other wet oxide etches: {ref}`TUNME <step-039>`,
  {ref}`GOXETCH <step-046>`.
* The resist and BARC being stripped: {ref}`LICM1 <step-093>`.
* Category pages: {ref}`Etch <category-etch>`,
  {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — "Standard Licon bottom
  CD" 0.08 µm; "Pre-LI ILD thickness" 0.5 µm; S/D junction
  0.1 µm.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — DNS wet bench, FSI
  Mercury, SEZ 223/Da Vinci, Akrion Gamma, EKC solvents,
  ashers.[^skw-01]
* SkyWater, Form S-1 — chemical suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Hydrofluoric acid*, *Buffered oxide etch*, *RCA
  clean*, *Piranha solution*.[^wiki-hf][^wiki-boe][^wiki-rca][^wiki-piranha]
* Kern, *J. Electrochem. Soc.* 1990 — the evolution of wafer
  cleaning.[^kern-1990]
* Reinhardt and Kern (eds.), *Handbook of Silicon Wafer Cleaning
  Technology*.[^reinhardt-2008]

### Deep dive

* Judge, *J. Electrochem. Soc.* 1971 — dissolution of SiO₂ in
  acidic fluoride solutions.[^judge-1971]
* Kikuyama et al., *J. Electrochem. Soc.* 1994 — etching in HF of
  extremely low concentration.[^kikuyama-1994]
* Monk, Soane and Howe, *J. Electrochem. Soc.* 1994 — HF etching of
  sacrificial oxide layers, experiment and model.[^monk-1994]
* Knotter and Denteneer, *J. Electrochem. Soc.* 2001 — how nitride
  etches in HF, the exposed-spacer question.[^knotter-2001]
* Cerofolini, *Appl. Surf. Sci.* 1998 — hydrogen termination after
  HF etching.[^cerofolini-1998]
* Morita et al., *J. Appl. Phys.* 1990 — native oxide regrowth on
  silicon, the queue-time constraint.[^morita-1990]
* Ohmi, *J. Electrochem. Soc.* 1996 — room-temperature wet
  cleaning.[^ohmi-1996]
* Kern, in Reinhardt and Kern (eds.), *Handbook of Silicon Wafer
  Cleaning Technology* — overview of cleaning chemistry.[^kern-handbook]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in
  Semiconductor Manufacturing* — pre-metal and contact
  cleans.[^reinhardt-2010]
* Fonash, *J. Electrochem. Soc.* 1990, and Oehrlein, *Mater. Sci.
  Eng. B* 1989 — the etch damage and residue a sacrificial etch
  addresses.[^fonash-1990][^oehrlein-1989]
* Berger, *Solid-State Electron.* 1972 — contact models that assume
  a clean interface.[^berger-1972]

## Open questions

* What this etch removes — the {term}`screen oxide` at the contact
  bottoms, a deliberately formed post-etch oxide, or the resist and
  BARC — is not stated publicly; all three readings above are
  inferences.
* The chemistry (dilute HF or BOE, concentration, time), the tool
  and whether the step includes the resist strip are not public.
* Whether a chemical oxide is deliberately left on the contact
  bottoms (some liner processes prefer it) rather than an {term}`HF-last`
  surface is not public.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-hf]: Wikipedia, *Hydrofluoric acid*.
    <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
[^wiki-boe]: Wikipedia, *Buffered oxide etch*.
    <https://en.wikipedia.org/wiki/Buffered_oxide_etch>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^reinhardt-2008]: K. A. Reinhardt and W. Kern (eds.), *Handbook of
    Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
    ISBN 978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
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
[^knotter-2001]: D. M. Knotter and T. J. J. Denteneer, "Etching
    Mechanism of Silicon Nitride in HF-Based Solutions", *Journal of The
    Electrochemical Society* **148**(3), F43 (2001).
    <https://doi.org/10.1149/1.1348262>
[^cerofolini-1998]: G. F. Cerofolini, "A study of the ionic route for
    hydrogen terminations resulting after SiO₂ etching by concentrated
    aqueous solutions of HF", *Applied Surface Science* **133**(1–2),
    108–114 (1998). <https://doi.org/10.1016/S0169-4332(98)00182-2>
[^morita-1990]: M. Morita, T. Ohmi, E. Hasegawa, M. Kawakami and
    M. Ohwada, "Growth of native oxide on a silicon surface", *Journal
    of Applied Physics* **68**(3), 1272–1281 (1990).
    <https://doi.org/10.1063/1.347181>
[^fonash-1990]: S. J. Fonash, "An Overview of Dry Etching Damage and
    Contamination Effects", *Journal of The Electrochemical Society*
    **137**(12), 3885–3892 (1990). <https://doi.org/10.1149/1.2086322>
[^oehrlein-1989]: G. S. Oehrlein, "Dry etching damage of silicon: A
    review", *Materials Science and Engineering: B* **4**(1–4), 441–450
    (1989). <https://doi.org/10.1016/0921-5107(89)90284-5>
[^berger-1972]: H. H. Berger, "Models for contacts to planar devices",
    *Solid-State Electronics* **15**(2), 145–158 (1972).
    <https://doi.org/10.1016/0038-1101(72)90048-2>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
