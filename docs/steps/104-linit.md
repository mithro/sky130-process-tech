(step-104)=
# Step 104 — LINIT: Nitride cap deposition

| | |
|---|---|
| **Step number** | 104 of 171[^steps-sheet] |
| **Step code** | `LINIT` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`LI1ME <step-103>` |
| **Next step** | {ref}`NILD2 <step-105>` |

## What this step is

`LINIT` deposits a thin, conformal silicon nitride over the patterned
{term}`local interconnect`: over the tops and sidewalls of the TiN lines of
{ref}`LI1ME <step-103>`, the exposed {term}`cap oxide` between them, and any
tungsten-plug tops the lines leave uncovered. The PDK names the
film: the process stack diagram
labels the dielectric directly above `li` "LINT K=7.3" and
dimensions it 0.075 µm.[^pdk-04] The relative permittivity is that
of silicon nitride (7–7.5; the {ref}`SPNIT <step-076>` {term}`spacer` nitride
is labelled 7.5), so the film's identity is public even though its
deposition method is not.

Three things the nitride does are visible from the PDK's own
structure. It sits between the 0.1 µm `li` conductor and the
"NILD2" oxide[^pdk-04] that {ref}`NILD2 <step-105>` will deposit, so
it is the etch stop that the `mcon` contact etch ({ref}`CTME <step-108>`)
— which must land on 0.1 µm of TiN without punching through it —
will see before it reaches the local interconnect. It seals the TiN
against the oxidising and wet environments of the oxide deposition
and polish that follow. And its 7.3 permittivity is part of every
LI-to-metal-1 capacitance in the extraction tables.[^pdk-08]
Because it lies over TiN and tungsten, it must be deposited well
below the temperatures of a furnace nitride, which is the main
constraint on the recipe (inference from the materials present).

## Step category

`LINIT` is a {ref}`Thin-film deposition <category-deposition>` step —
a {term}`CVD` silicon nitride, in the family of {ref}`ISONIT <step-003>`,
{ref}`GATENIT <step-058>` and {ref}`SPNIT <step-076>` before it and
the {ref}`NTSD <step-167>` topside nitride at the end. What
distinguishes this instance is the substrate and the temperature:
the earlier nitrides were deposited on silicon and oxide at furnace
temperatures, while this one goes onto titanium nitride, tungsten
and oxide on a wafer whose thermal ceiling is now set by the
{term}`silicide` ({ref}`CSIL <step-098>`) and the metal films — so a plasma
deposition at 300–400 °C ({term}`PECVD`; category
page[^wiki-pecvd]) is the industry-typical choice, and we infer it
here. It is also the first nitride in the flow deposited *as* an
etch stop, the role the category page assigns to nitride under an
oxide contact etch.

## Why this step exists

A thin nitride over a local interconnect is a standard element of
the borderless-contact schemes of the era:

* **Etch stop for the `mcon` contact.** The metal-1 contact
  ({ref}`CTM1 <step-107>`, {ref}`CTME <step-108>`) is a fluorocarbon
  oxide etch through the NILD2 oxide that must stop on a 0.1 µm TiN
  line — and, where the contact is misaligned or the line is narrow,
  must not dig into the oxide beside the line. An oxide etch stops on
  nitride with the {term}`selectivity` that the fluorocarbon-film mechanism
  gives (Schaepkens et al.[^schaepkens-1999]); the nitride is then
  opened with a short, separate etch. Liao et al. compared etch-stop
  layers for {term}`borderless contacts <borderless contact>` and their effect on deep-submicron
  device performance,[^liao-2004] and Cacciato et al. describe the
  charging that a conductive etch-stop nitride can cause during a
  contact etch,[^cacciato-2003] which is one reason its composition
  and thickness matter. The PDK's rule that an `mcon` "must be
  enclosed by LI by at least" 0.000 µm (ct.4)[^pdk-periph] — a
  zero-enclosure, borderless contact — is, we infer, only possible
  because this nitride is there.
* **Sealing the TiN and tungsten.** Titanium nitride oxidises slowly
  in air and quickly in an oxygen plasma or a hot oxidising ambient,
  and the tungsten plugs oxidise to WO₃; the HDP or PECVD oxide
  deposition of {ref}`NILD2 <step-105>` and the polish and cleans of
  {ref}`CMPL <step-106>` are exactly such environments. A nitride
  deposited first keeps both metals as they are (industry practice;
  inference for SKY130).
* **Moisture and hydrogen barrier.** PECVD nitride is a good barrier
  to water, but it carries hydrogen: Smith et al. and Claassen et
  al. set out how the plasma conditions fix the composition,
  hydrogen content and stress of PECVD nitride,[^smith-1990][^claassen-1985]
  Habraken and Kuiper review the film properties,[^habraken-1994]
  and Shimaya traced hot-carrier degradation to water diffusing
  through nitride passivation.[^shimaya-1995] At 0.075 µm the
  hydrogen inventory of this film is small, but it is the closest
  nitride to the transistors after the spacer.
* **Stress.** A nitride over the gates strains the channel, as Ito
  et al. and Shimizu et al. showed for etch-stop nitrides at the
  130 nm generation;[^ito-2000][^shimizu-2001] here the film is
  separated from the gates by the cap oxide and the gate caps, so
  the effect is smaller, but the stress of a PECVD nitride — which
  Hughey and Cook showed can change irreversibly on later
  heating[^hughey-2003] — is still a recipe parameter.
* **Capacitance.** The film's 7.3 permittivity over 0.075 µm adds to
  the LI-to-metal-1 and LI-to-LI capacitances that the extraction
  tables carry;[^pdk-08] the thickness is therefore kept to what the
  etch stop needs.

Without `LINIT` the `mcon` etch would have no stop on the local
interconnect and the TiN would be oxidised by the steps that follow.

## How it is typically performed

Industry-generic routes for a thin etch-stop nitride over metal in a
200 mm, 130 nm-era fab (SKY130's recipe is not public):

* **PECVD from silane and ammonia (or nitrogen).** Single-wafer or
  multi-station reactor, 300–400 °C, a few Torr, 13.56 MHz (often
  with a low-frequency component to tune stress); SiH₄/NH₃/N₂
  chemistry,[^wiki-pecvd] with hydrogen content and stress set by
  the plasma conditions.[^smith-1990][^claassen-1985] SkyWater lists
  "PECVD nitride C1" and "PECVD silane oxide/nitride/oxynitride,
  C1".[^skw-01] This is the route we infer for `LINIT`: it is the
  only nitride deposition on the public list that fits the thermal
  ceiling of a TiN/tungsten wafer.
* **Low-temperature LPCVD.** A BTBAS/NH₃ furnace nitride at
  550–600 °C (Gumpher et al.[^gumpher-2004]) — which SkyWater also
  lists on its Aviza furnaces[^skw-01] — is conformal and
  hydrogen-lean but hot for a wafer carrying TiSi₂ contacts and
  tungsten; a single-wafer thermal nitride at similar temperatures
  (Teasdale et al.[^teasdale-2001]) is the same trade-off.
  Possible, but less likely (inference).
* **Thickness.** 0.075 µm (PDK).[^pdk-04]
* **Conformality.** The film must cover the 0.1 µm-tall TiN
  sidewalls without thinning to nothing at their feet, which a
  PECVD nitride at this thickness can do at a 0.34 µm pitch
  (li.1 + li.3[^pdk-periph]); {term}`step coverage` is checked by
  cross-section SEM.
* **Sequence.** Post-etch clean (at {ref}`LI1ME <step-103>`); load;
  a short {term}`degas` or N₂/NH₃ plasma pre-treatment to remove TiN
  surface oxide; deposition; in-situ NF₃ chamber clean between
  wafers.[^txt-09]
* **Metrology.** Thickness and refractive index by spectroscopic
  ellipsometry on monitors and unpatterned test pads; stress by
  wafer bow; hydrogen content by FTIR when the recipe is being
  qualified; particles.

## Machines typically used

* **{ref}`PECVD system <machine-pecvd>`**, 200 mm: Novellus Concept One/Two and Sequel
  (multi-station),[^novellus-history] Applied Materials Producer or
  Centura DxZ (category page).
* **{ref}`Vertical LPCVD furnace <machine-vertical-furnace-lpcvd>`** with BTBAS/NH₃ as the alternative.
* **{ref}`Spectroscopic ellipsometer <machine-film-thickness-metrology>`**, **stress gauge**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **"C1" PECVD system, nitride.** SkyWater lists "PECVD nitride C1"
  and "PECVD silane oxide/nitride/oxynitride, C1" — a Novellus
  Concept One-class system, we infer from the abbreviation; SkyWater
  gives only "C1".[^skw-01] Strength: **strong** for the existence
  of a PECVD nitride process; assignment to `LINIT` is an
  **inference** from the thermal-budget argument above.
* **Aviza furnace, BTBAS nitride.**[^skw-01] Strength: strong for
  existence; weak for this step.

## Resources required

* **Silane, ammonia and nitrogen** (PECVD),[^wiki-pecvd] or **BTBAS
  and ammonia** (low-temperature {term}`LPCVD`).[^gumpher-2004]
* **NF₃** (with argon or oxygen) chamber clean; **helium** or
  **argon** diluent.[^txt-09]
* **Chamber consumables** — showerheads, heater and liner parts.
* **Monitor wafers** (SEMI M8 class)[^semi-m8] for thickness, stress
  and particle control.
* Gas suppliers named in SkyWater's 2021 S-1: Air Products,
  Praxair.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`LI1ME <step-103>` (the patterned TiN it covers).
  Next: {ref}`NILD2 <step-105>` (the oxide over it), then
  {ref}`CMPL <step-106>`.
* The etch it will stop: {ref}`CTM1 <step-107>`,
  {ref}`CTME <step-108>`.
* The film it seals: {ref}`LITIN <step-101>`; the plugs beneath:
  {ref}`WDEP <step-099>`, {ref}`WCMPLI <step-100>`.
* Other nitrides: {ref}`ISONIT <step-003>`, {ref}`GATENIT <step-058>`,
  {ref}`SPNIT <step-076>`, {ref}`NTSD <step-167>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, process stack diagram — "LINT K=7.3", 0.075 µm,
  between `li` and "NILD2".[^pdk-04]
* SkyWater PDK, *Parasitic Layout Extraction* — the LI capacitance
  tables the film enters.[^pdk-08]
* SkyWater PDK, *Periphery rules* — ct.4 ("Mcon must be enclosed by
  LI by at least" 0.000 µm); li.1, li.3.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — "PECVD nitride C1";
  "PECVD silane oxide/nitride/oxynitride, C1"; Aviza BTBAS
  nitride.[^skw-01]
* SkyWater, Form S-1 — gas suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Silicon nitride*, *Plasma-enhanced chemical vapor
  deposition*.[^wiki-sin][^wiki-pecvd]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  PECVD nitride.[^txt-02]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — PECVD equipment and chamber cleaning.[^txt-09]
* Encyclopedia.com, *Novellus Systems, Inc.* — the Concept One/Two
  product history.[^novellus-history]

### Deep dive

* Liao et al., *Thin Solid Films* 2004 — etch-stop layers for
  borderless contacts and device performance.[^liao-2004]
* Schaepkens et al., *JVST A* 1999 — the SiO₂-to-Si₃N₄ selectivity
  mechanism that makes the film an etch stop.[^schaepkens-1999]
* Cacciato et al., P2ID 2003 — charging through a conductive
  borderless nitride during contact etch.[^cacciato-2003]
* Smith et al., *J. Electrochem. Soc.* 1990, and Claassen et al.,
  *J. Electrochem. Soc.* 1985 — PECVD nitride mechanism, composition
  and stress.[^smith-1990][^claassen-1985]
* Habraken and Kuiper, *Mater. Sci. Eng. R* 1994 — nitride and
  oxynitride film properties and hydrogen.[^habraken-1994]
* Hughey and Cook, *MRS Proc.* 2003 — irreversible stress change in
  PECVD nitride on heating.[^hughey-2003]
* Shimaya (NTT), IRPS 1995 — water diffusion through nitride and
  hot-carrier degradation.[^shimaya-1995]
* Ito et al. (NEC), IEDM 2000, and Shimizu et al. (Hitachi), IEDM
  2001 — etch-stop nitride stress and transistor
  performance.[^ito-2000][^shimizu-2001]
* Gumpher et al., *J. Electrochem. Soc.* 2004 — BTBAS
  low-temperature LPCVD nitride, the furnace alternative.[^gumpher-2004]
* Teasdale et al., *Electrochem. Solid-State Lett.* 2001 —
  single-wafer thermal nitride from DCS/NH₃.[^teasdale-2001]

## Open questions

* The deposition route (PECVD or low-temperature LPCVD), precursor,
  temperature, stress and hydrogen content are not public; the
  PECVD reading is an inference from the materials present and
  SkyWater's capability list.
* Whether the film is opened by the `mcon` etch itself or by a
  separate nitride etch is not stated publicly (see
  {ref}`CTME <step-108>`).
* Whether a pre-treatment removes the TiN surface oxide before the
  nitride is deposited is not public.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram). <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^liao-2004]: H. Liao, P. S. Lee, L. N. L. Goh, H. Liu, J. L. Sudijono,
    Q. Elgin and C. Sanford, "The impact of etch-stop layer for
    borderless contacts on deep submicron CMOS device performance — a
    comparative study", *Thin Solid Films* **462–463**, 29–33 (2004).
    <https://doi.org/10.1016/j.tsf.2004.05.035>
[^schaepkens-1999]: M. Schaepkens, T. E. F. M. Standaert, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
    SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
    fluorocarbon plasmas and a comparison with the SiO₂-to-Si
    mechanism", *Journal of Vacuum Science & Technology A* **17**(1),
    26–37 (1999). <https://doi.org/10.1116/1.582108>
[^cacciato-2003]: A. Cacciato, A. Scarpa, S. Evseev and M. Diekema,
    "Charging damage during contact etch triggered by increased
    borderless nitride conductivity", *Proc. 2003 8th International
    Symposium on Plasma- and Process-Induced Damage*, pp. 20–23.
    <https://doi.org/10.1109/PPID.2003.1199721>
[^smith-1990]: D. L. Smith, A. S. Alimonda, C.-C. Chen, S. E. Ready and
    B. Wacker, "Mechanism of SiNₓHᵧ Deposition from NH₃-SiH₄ Plasma",
    *Journal of The Electrochemical Society* **137**(2), 614–623 (1990).
    <https://doi.org/10.1149/1.2086517>
[^claassen-1985]: W. A. P. Claassen, W. G. J. N. Valkenburg,
    M. F. C. Willemsen and W. M. v. d. Wijgert, "Influence of Deposition
    Temperature, Gas Pressure, Gas Phase Composition, and RF Frequency
    on Composition and Mechanical Stress of Plasma Silicon Nitride
    Layers", *Journal of The Electrochemical Society* **132**(4),
    893–898 (1985). <https://doi.org/10.1149/1.2113980>
[^habraken-1994]: F. H. P. M. Habraken and A. E. T. Kuiper, "Silicon
    nitride and oxynitride films", *Materials Science and Engineering:
    R: Reports* **12**(3), 123–175 (1994).
    <https://doi.org/10.1016/0927-796X(94)90006-X>
[^hughey-2003]: M. P. Hughey and R. F. Cook, "Irreversible Tensile
    Stress Development in PECVD Silicon Nitride Films", *MRS
    Proceedings* **795** (2003). <https://doi.org/10.1557/PROC-795-U1.6>
[^shimaya-1995]: M. Shimaya, "Water diffusion model for the enhancement
    of hot-carrier-induced degradation due to silicon nitride
    passivation in submicron MOSFET's", *33rd IEEE International
    Reliability Physics Symposium Proceedings* (1995), pp. 292–296.
    <https://doi.org/10.1109/RELPHY.1995.513694>
[^ito-2000]: S. Ito, H. Namba, K. Yamaguchi, T. Hirata, K. Ando,
    S. Koyama, S. Kuroki, N. Ikezawa, T. Suzuki, T. Saitoh and
    T. Horiuchi, "Mechanical stress effect of etch-stop nitride and its
    impact on deep submicron transistor design", *IEDM 2000 Technical
    Digest*, pp. 247–250. <https://doi.org/10.1109/IEDM.2000.904303>
[^shimizu-2001]: A. Shimizu, K. Hachimine, N. Ohki, H. Ohta,
    M. Koguchi, Y. Nonaka, H. Sato and F. Ootsuka, "Local
    mechanical-stress control (LMC): a new technique for
    CMOS-performance enhancement", *IEDM 2001 Technical Digest*,
    pp. 19.4.1–19.4.4. <https://doi.org/10.1109/IEDM.2001.979529>
[^gumpher-2004]: J. Gumpher, W. Bather, N. Mehta and D. Wedel,
    "Characterization of Low-Temperature Silicon Nitride LPCVD from
    Bis(tertiary-butylamino)silane and Ammonia", *Journal of The
    Electrochemical Society* **151**(5), G353 (2004).
    <https://doi.org/10.1149/1.1690294>
[^teasdale-2001]: D. Teasdale, Y. Senzaki, R. Herring, G. Hoeye,
    L. Page and P. Schubert, "LPCVD of Silicon Nitride from
    Dichlorosilane and Ammonia by Single Wafer Rapid Thermal
    Processing", *Electrochemical and Solid-State Letters* **4**(5),
    F11 (2001). <https://doi.org/10.1149/1.1359056>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
