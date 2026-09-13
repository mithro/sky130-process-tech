(step-091)=
# Step 091 — NCAPOX: Cap oxide deposition

| | |
|---|---|
| **Step number** | 91 of 171[^steps-sheet] |
| **Step code** | `NCAPOX` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`CMPP <step-090>` |
| **Next step** | {ref}`RTAD2 <step-092>` |

## What this step is

`NCAPOX` deposits an undoped silicon-dioxide "cap" over the polished
phosphosilicate glass of {ref}`CMPP <step-090>`. It is a blanket,
unpatterned {term}`CVD` oxide on a surface that is now flat, so its only
geometric task is to be uniform; its purpose is chemical and
structural — to seal the doped glass, to re-bury whatever the polish
exposed, and to provide the clean, undoped oxide that the
local-interconnect contacts ({ref}`LICM1E <step-094>`) will be
etched through first and that the {term}`local interconnect`
({ref}`LITIN <step-101>`) will lie on. This reference describes a
similar cap after each inter-level oxide and its polish at the metal
levels — {ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`,
{ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>` — above the
dielectrics the PDK names `NILD3`…`NILD6`.[^pdk-04]

The PDK does not name the cap separately. On our reading of the
stack diagram, the cap is part of the interval it labels "PSG" —
0.4299 µm over field poly, up to the `li` bottom at 0.9361 µm[^pdk-04]
— and part of the 0.5 µm "Pre-LI ILD thickness" of the assumptions
table.[^pdk-03] If the polish stops on the 0.2 µm gate caps (the
reading of the {ref}`CMPP <step-090>` page), the {term}`cap oxide` is what
separates the cap tops from the local interconnect, and its
thickness is of the order of 0.2–0.3 µm (inferred from those two
numbers; not public). The film's identity — an undoped {term}`PECVD` oxide
from {term}`TEOS` or silane — is likewise an inference, from the industry
practice set out below and from SkyWater's "PECVD TEOS, C2 and
Producer" and "PECVD silane oxide … C1" entries.[^skw-01]

## Step category

`NCAPOX` is a {ref}`Thin-film deposition <category-deposition>` step
— a plasma CVD oxide, in the family of {ref}`POC <step-059>` and
{ref}`SPOX <step-080>` before it and the `NCAPOX*` caps after. What
distinguishes it from the {ref}`PSG <step-089>` deposition two steps
earlier is that it has no gap to fill and must *not* be doped;
what distinguishes it from the earlier thin caps is that it is
deposited on a surface with buried junctions and a 0.1 µm[^pdk-03]
source/drain depth beneath it, so it must be a low-temperature film
(PECVD, 350–450 °C, typical[^wiki-pecvd][^txt-02]) rather than a
furnace oxide.

## Why this step exists

An undoped cap over a doped pre-metal glass is standard practice
for reasons the literature spells out:

* **Sealing the PSG against moisture.** Phosphosilicate glass
  absorbs water, and Levin showed that the absorption and the
  densification that reverses it depend on the glass's history;[^levin-1982]
  absorbed water plus phosphorus gives phosphoric acid, the
  aluminium-corrosion mechanism Paulson and Kirk described.[^paulson-1974]
  A dense undoped oxide over the glass keeps ambient moisture out
  during the {term}`queue times <queue time>` of the contact module.
* **Keeping phosphorus away from the contacts.** The contact etch
  ({ref}`LICM1E <step-094>`) opens holes whose upper sidewalls are
  cap oxide and whose lower sidewalls are {term}`PSG`; phosphorus at the
  surface of the etched hole could out-diffuse into the titanium
  {term}`liner` or the silicon during the {term}`silicide` anneal
  ({ref}`CSIL <step-098>`) — the phosphorus out-diffusion from HDP
  PSG is a known integration concern (Hsiao, Liu and Wang study its
  thermal-budget dependence[^hsiao-2005]). A cap moves the doped
  glass away from the surface the liner is sputtered onto.
* **Restoring a dielectric over the polish stop.** If
  {ref}`CMPP <step-090>` lands on the gate caps, the tops of every
  poly line are at the polished surface. The local interconnect
  that will be patterned on this surface must be insulated from
  every gate it crosses; the cap oxide is that insulator, and its
  thickness, together with the nitride cap, sets the gate-to-LI
  capacitance the PDK's extraction tables carry.[^pdk-08]
* **Burying polish defects.** Micro-scratches and residual slurry
  particles from the polish are covered rather than transferred into
  the contact etch; the same reasoning applies at every `NCAPOX*`
  step after a metal-level polish.

Without `NCAPOX` the local interconnect would sit on doped,
hygroscopic glass and, on the cap-stop reading, directly on the gate
caps.

## How it is typically performed

Industry-generic routes for an undoped cap oxide in a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

* **PECVD TEOS oxide.** TEOS vapour with O₂ in a capacitively
  coupled 13.56 MHz plasma at 350–400 °C and a few Torr, the
  workhorse inter-level oxide of the era; Nguyen et al. set out the
  plasma- and thermal-assisted reaction mechanisms,[^nguyen-1990]
  Raupp, Cale and Hey the role of oxygen excitation,[^raupp-1992] and
  Becker et al. the film quality obtainable from TEOS
  pyrolysis.[^becker-1987] The film is smooth, moderately
  conformal and, after a short anneal, close to thermal oxide in wet
  etch rate. SkyWater lists "PECVD TEOS, C2 and Producer".[^skw-01]
* **PECVD silane oxide.** SiH₄ with N₂O at 300–400 °C, faster and
  less conformal, with a few per cent hydrogen; Adams et al.
  characterised the plasma-deposited film.[^adams-1981-pecvd]
  SkyWater lists "PECVD silane oxide/nitride/oxynitride, C1".[^skw-01]
* **SACVD TEOS/ozone.** Sub-atmospheric TEOS with ozone, more
  conformal but hygroscopic and usually reserved for {term}`gap fill`;
  Fujino et al. describe the chemistry[^fujino-1990] and Kwok et al.
  its integration with PECVD.[^kwok-1994] Unlikely for a cap on a
  flat surface (inference).
* **Thickness.** Of the order of 0.2–0.3 µm on the reading above;
  not public.
* **Sequence.** Post-CMP clean (at {ref}`CMPP <step-090>`) with a
  dilute-HF touch to remove slurry residue and a {term}`degas`; deposition,
  typically in a single-wafer chamber with an in-situ NF₃ clean
  between wafers;[^txt-09] optional short plasma treatment to
  densify the surface.
* **Metrology.** Thickness and refractive index by ellipsometry on
  product and monitors; wet-etch rate ratio as a density check;
  stress by wafer bow; particles.

## Machines typically used

* **{ref}`PECVD system <machine-pecvd>`**, 200 mm: Applied Materials Producer or Centura
  DxZ (TEOS and silane oxides), Novellus Concept One/Two and
  Sequel;[^novellus-history] the Trikon Delta 201, a "single-chamber
  production system for producing films, including silicon dioxide or
  silicon nitride" from Electrotech (the 10-K does not say whether it is
  plasma-enhanced);[^trikon-10k-1996] Trikon "later merged
  with Aviza Technology Inc in 2005".[^semitoday-spts-2009]
* **{ref}`Ellipsometer <machine-film-thickness-metrology>`**, **stress gauge**, **{ref}`unpatterned defect inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **"C2 and Producer" PECVD TEOS.** SkyWater lists "PECVD TEOS, C2
  and Producer" — a Novellus Concept Two-class system (we infer from
  the abbreviation; SkyWater gives only "C2") and an Applied
  Materials Producer.[^skw-01] Strength: **strong** for the
  existence of a PECVD TEOS process on those tools; assignment to
  `NCAPOX` is an **inference** from the film's role (an undoped oxide
  over doped glass) and industry practice.
* **"C1" PECVD silane oxide.**[^skw-01] Strength: strong for
  existence; medium for this step — a silane oxide is an equally
  plausible cap.

## Resources required

* **TEOS** (liquid, vaporised) and **oxygen**, or **silane** and
  **N₂O** for the silane route;[^wiki-teos][^wiki-pecvd] **helium**,
  **nitrogen** or **argon** as carrier or diluent (typical; the PECVD
  article describes TEOS deposition "in an oxygen or oxygen-argon
  plasma"[^wiki-pecvd]).
* **NF₃** chamber clean (with argon or oxygen); **helium** backside
  cooling.[^txt-09]
* **{ref}`Chamber consumables <material-hardware-consumables>`** — showerheads, heater and liner parts.
* **{ref}`Monitor wafers <material-substrates>`** (SEMI M8 class)[^semi-m8] for thickness, stress
  and particle control.
* Gas suppliers named in SkyWater's 2021 S-1: Air Products,
  Praxair.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`CMPP <step-090>` (the polish it covers). Next:
  {ref}`RTAD2 <step-092>` (the anneal that, on our reading, densifies
  cap and glass together).
* The glass it seals: {ref}`PSG <step-089>`. What is etched through
  it: {ref}`LICM1 <step-093>`, {ref}`LICM1E <step-094>`. What lies
  on it: {ref}`LITIN <step-101>`.
* Earlier CVD oxide caps: {ref}`POC <step-059>`,
  {ref}`SPOX <step-080>`. Later caps of the same name pattern:
  {ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`,
  {ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, process stack diagram — "PSG K=3.9" interval,
  0.4299 µm over field poly; `li` bottom 0.9361 µm; NILD naming.[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — "Pre-LI ILD thickness"
  0.5 µm; S/D junction depth 0.1 µm.[^pdk-03]
* SkyWater PDK, *Parasitic Layout Extraction* — the poly/li
  capacitance tables the cap thickness feeds.[^pdk-08]
* SkyWater, *Facilities & Capabilities* — "PECVD TEOS, C2 and
  Producer"; "PECVD silane oxide/nitride/oxynitride, C1".[^skw-01]
* SkyWater, Form S-1 — gas suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Plasma-enhanced chemical vapor deposition*.[^wiki-pecvd]
* Wikipedia, *Tetraethyl orthosilicate*.[^wiki-teos]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  PECVD oxides.[^txt-02]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — PECVD equipment and chamber cleaning.[^txt-09]
* Encyclopedia.com, *Novellus Systems, Inc.* — the Concept One/Two
  product history.[^novellus-history]

### Deep dive

* Nguyen et al. (IBM), *J. Electrochem. Soc.* 1990 — reaction
  mechanisms of plasma and thermal TEOS oxide deposition.[^nguyen-1990]
* Raupp, Cale and Hey, *JVST B* 1992 — oxygen excitation and loss
  in PECVD TEOS.[^raupp-1992]
* Becker et al., *JVST B* 1987 — high-quality SiO₂ from TEOS
  pyrolysis.[^becker-1987]
* Adams et al., *J. Electrochem. Soc.* 1981 — characterisation of
  plasma-deposited silicon dioxide.[^adams-1981-pecvd]
* Fujino et al., *J. Electrochem. Soc.* 1990 — TEOS/ozone oxide at
  atmospheric pressure.[^fujino-1990]
* Kwok et al. (Applied Materials), *J. Electrochem. Soc.* 1994 —
  integrated PECVD/ozone-TEOS films and their surface
  effects.[^kwok-1994]
* Levin, *J. Electrochem. Soc.* 1982 — water absorption and
  densification of PSG, the problem a cap solves.[^levin-1982]
* Paulson and Kirk, IRPS 1974 — phosphorus glass, moisture and
  aluminium corrosion.[^paulson-1974]
* Hsiao, Liu and Wang, *JVST B* 2005 — thermal-budget behaviour of
  HDP PSG under a cap.[^hsiao-2005]
* Nguyen, *IBM J. Res. Dev.* 1999 — HDP-CVD dielectrics, the
  alternative cap route.[^nguyen-1999]

## Open questions

* The cap's thickness, precursor (TEOS or silane) and deposition
  temperature are not public; the PECVD TEOS reading is an
  inference from SkyWater's capability list and industry practice.
* Whether the cap is deposited directly on the polished gate caps
  (the {ref}`CMPP <step-090>` cap-stop reading) or on residual PSG
  is not public.

<!-- footnotes -->
[^trikon-10k-1996]: Trikon Technologies, Inc., *Annual Report on Form
    10-K for the fiscal year ended December 31, 1996*; copy on
    GetFilings.com, Wayback Machine capture of 2008-10-12.
    <http://web.archive.org/web/20081012193325/http://www.getfilings.com/o0000898430-97-001539.html>
[^semitoday-spts-2009]: Semiconductor Today, *Sumitomo Precision
    Products completes acquisition of Aviza*, news item, 2009-10-19.
    <https://www.semiconductor-today.com/news_items/2009/OCT/STS_191009.htm>

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram). <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^nguyen-1990]: S. Nguyen, D. Dobuzinsky, D. Harmon, R. Gleason and
    S. Fridmann, "Reaction Mechanisms of Plasma- and Thermal-Assisted
    Chemical Vapor Deposition of Tetraethylorthosilicate Oxide Films",
    *Journal of The Electrochemical Society* **137**(7), 2209–2215
    (1990). <https://doi.org/10.1149/1.2086914>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
[^becker-1987]: F. S. Becker, D. Pawlik, H. Anzinger and
    A. Spitzer, "Low-pressure deposition of high-quality SiO₂ films by
    pyrolysis of tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **5**(6), 1555–1563 (1987).
    <https://doi.org/10.1116/1.583673>
[^adams-1981-pecvd]: A. C. Adams, F. B. Alexander, C. D. Capio and
    T. E. Smith, "Characterization of Plasma-Deposited Silicon
    Dioxide", *Journal of The Electrochemical Society* **128**(7),
    1545–1551 (1981). <https://doi.org/10.1149/1.2127680>
[^fujino-1990]: K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
    "Silicon Dioxide Deposition by Atmospheric Pressure and
    Low-Temperature CVD Using TEOS and Ozone", *Journal of The
    Electrochemical Society* **137**(9), 2883–2887 (1990).
    <https://doi.org/10.1149/1.2087093>
[^kwok-1994]: K. Kwok, E. Yieh, S. Robles and B. C. Nguyen, "Surface
    Related Phenomena in Integrated PECVD/Ozone-TEOS SACVD Processes
    for Sub-Half Micron Gap Fill: Electrostatic Effects", *Journal of
    The Electrochemical Society* **141**(8), 2172–2177 (1994).
    <https://doi.org/10.1149/1.2055081>
[^levin-1982]: R. M. Levin, "Water Absorption and Densification of
    Phosphosilicate Glass Films", *Journal of The Electrochemical
    Society* **129**(8), 1765–1770 (1982).
    <https://doi.org/10.1149/1.2124289>
[^paulson-1974]: W. M. Paulson and R. W. Kirk, "The Effects of
    Phosphorus-Doped Passivation Glass on the Corrosion of Aluminum",
    *12th International Reliability Physics Symposium* (1974),
    pp. 172–179. <https://doi.org/10.1109/IRPS.1974.362644>
[^hsiao-2005]: W.-C. Hsiao, C.-P. Liu and Y.-L. Wang, "Influence of
    thermal budget on phosphosilicate glass prepared by high-density
    plasma chemical-vapor deposition", *Journal of Vacuum Science &
    Technology B* **23**(5), 2146–2150 (2005).
    <https://doi.org/10.1116/1.2050670>
[^nguyen-1999]: S. V. Nguyen, "High-density plasma chemical vapor
    deposition of silicon-based dielectric films for integrated
    circuits", *IBM Journal of Research and Development* **43**(1.2),
    109–126 (1999). <https://doi.org/10.1147/rd.431.0109>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
