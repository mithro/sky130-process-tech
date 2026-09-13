(step-084)=
# Step 084 — PDIS: P+ source drain implant strip

| | |
|---|---|
| **Step number** | 84 of 171[^steps-sheet] |
| **Step code** | `PDIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`2PSDI <step-083>` |
| **Next step** | {ref}`NSDM <step-085>` |

## What this step is

`PDIS` removes the photoresist patterned at {ref}`PSDM <step-081>`
after it has masked the two p-type implants {ref}`PSDI <step-082>` and
{ref}`2PSDI <step-083>` (on our reading), and cleans the wafer so that
the N⁺ source/drain mask {ref}`NSDM <step-085>` can be coated on it.
It is the first of the two source/drain strips (the other is
{ref}`NSDIS <step-087>`), and the two of them are, with the poly
implant strip {ref}`P1IS <step-051>`, the hardest strips in the front
end: the resist has taken a dose of the order of 10¹⁵ cm⁻²
(industry-typical for a source/drain[^txt-01]) of boron or BF₂, an
order of magnitude beyond the channel and well implants, and its
surface has been converted to the carbonised crust that Fujimura et
al. characterised.[^fujimura-1989]

The surface under the resist is, on our reading of the flow, the
{ref}`SPOX <step-080>` oxide everywhere: over the source/drain
silicon, over the spacers and caps, over the field, and over the poly
opened by the {term}`nitride cut`. There is no exposed silicon, poly or
metal, so the full acid–peroxide sequence can be used; but the oxide
is thin, must still screen the N⁺ implant and cap the anneal, and so
must not be stripped or seriously thinned here.

## Step category

`PDIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-high-dose-implant* type. The category page explains the crust:
ions deposit their energy in the top 100–200 nm of the resist,
cross-linking and carbonising it,[^fujimura-1989] and if the wafer is
heated quickly the volatile bulk beneath "build[s] up pressure
beneath the implant-hardened surface layer" until the crust
pops.[^pat-strip-mosel] At 10¹⁵ cm⁻² the crust is at its thickest
and hardest, the implanted species (boron, fluorine) are embedded in
it, and any sputtered metal from the implanter's beam-line and disc
sits on top. The strip is therefore engineered around the crust rather
than around the bulk resist.

## Why this step exists

The resist must be gone before the wafer can be coated again, and it
must be gone *cleanly*: a popped flake that lands on a source/drain
region blocks the N⁺ implant locally, and a flake on a gate stack
becomes a defect at the contact etch. Popped crust "causes the
photoresist to become even harder"[^pat-strip-mosel] and turns a
routine ash into a residue problem; Chan, Chiu and Tao describe an
ashing sequence built around the "carbonized crust".[^pat-strip-tsmc]
The strip also removes the boron and fluorine trapped in the crust,
and whatever the implanter sputtered onto the wafer, before the
{ref}`RTAD <step-088>` anneal can drive any of it into the silicon;
Fujimura et al. showed how sodium contamination is avoided in
downstream ashing with O₂+H₂O plasmas,[^fujimura-1994] and Kern's
review sets out why a metal-removing wet clean follows.[^kern-1990]

A point specific to this strip is what the resist sat on. The poly
contact heads opened at {ref}`NPCME <step-079>` and the source/drain
silicon are both under the thin {ref}`SPOX <step-080>` oxide, so the
strip chemistry never touches doped silicon directly; that is one of
the reasons for depositing the oxide before the implant masks
(inference, {ref}`SPOX <step-080>`).

## How it is typically performed

An industry-generic high-dose implant strip for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

1. **Plasma ash, two steps.** Downstream microwave or RF oxygen
   plasma. First a *low-temperature* step — "removed by oxygen and
   nitrogen/hydrogen plasma in a low-temperature (<220 °C)
   environment"[^pat-strip-mosel] — until the crust is gone, so that
   the bulk cannot pop under it; then a hotter step to remove the
   bulk quickly. The nitrogen addition that Fujimura et al. studied
   raises the ash rate,[^fujimura-1990] and forming gas or water
   vapour in the plasma penetrates the crust.[^fujimura-1994]
   Downstream configuration is used because "monatomic oxygen is
   electrically neutral" and the remote plasma "prevents damage to
   the wafer surface".[^wiki-ash] SkyWater's ashers span exactly this
   range: "Gasonic PEP, remote microwave plasma, N2, O2, 120C –
   270C", "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2,
   40C-270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to
   250C".[^skw-01] The Iridia's 40 °C floor and its H₂/N₂ and NH₃
   options are what a crust step needs; the CF₄ additions available
   on two of the tools attack oxide and would, we infer, be omitted
   here.
2. **Wet strip and clean.** SPM (H₂SO₄:H₂O₂, "3 parts of concentrated
   sulfuric acid and 1 part of 30 wt. % hydrogen peroxide solution"
   is typical[^wiki-piranha]) to dissolve residual organics and the
   ash's residue, then SC-1 for particles and, optionally, SC-2 for
   metals;[^wiki-rca] Visintin, Korzenski and Baum describe the
   liquid formulations developed specifically for high-dose
   implanted resist,[^visintin-2006] and the Ohmi room-temperature
   sequence is the low-consumption alternative.[^ohmi-1996] SkyWater's
   Akrion Gamma bench lists "Sulfuric, SC1".[^skw-01] We infer no HF
   step: the {ref}`SPOX <step-080>` oxide must survive for the N⁺
   implant and the anneal. SC-1 consumes a little oxide; that loss
   is, we infer, budgeted.
3. **Rinse and dry.** Cascade DI-water rinse, spin-rinse or IPA dry.
4. **Inspection.** Patterned-wafer optical inspection for popped
   flakes and residue; a residue map after a high-dose strip is one
   of the standard defect monitors.

## Machines typically used

* **Downstream plasma asher**, 200 mm single-wafer: GaSonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK;
  Axcelis's asher patent describes a design aimed at raising the
  removal rate of implanted resist,[^pat-asher-axcelis] and the
  Fusion microwave asher is the downstream archetype.[^pat-asher-fusion]
* **Batch wet bench** (Akrion, DNS/SCREEN, SCP) or **spray
  processor** (FSI Mercury) with SPM, SC-1, SC-2.
* **Patterned-wafer inspection** (KLA-Tencor AIT class).

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia RF microwave and Mattson Aspen II ashers** —
  named with their gases and temperatures on SkyWater's facilities
  page.[^skw-01] Strength: **strong** for existence; the assignment
  of this strip to any one of them is an inference, the Iridia's
  low-temperature and hydrogen options making it the most natural
  fit for a crust step.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric,
  BOE")[^skw-01] for SPM/SC-1. Strength: strong for existence.
* **DNS wet bench and FSI Mercury** ("industry standard
  HF/SC1/SC2")[^skw-01] as alternatives. Strength: strong for
  existence.
* **KLA-Tencor AIT** inspection, from a SkyWater job posting.[^job-01]
  Strength: medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)**, possibly **NH₃** (listed
  for the Iridia) or **water vapour** (not among SkyWater's listed asher
  gases), for the two-step ash;[^skw-01][^fujimura-1994] **CF₄**, listed
  on the Iridia and Mattson ashers,[^skw-01] attacks the oxide and would,
  we infer, be omitted here.
* **Sulphuric acid (96–98 %) and hydrogen peroxide (30 %)** for SPM;
  **ammonium hydroxide** for SC-1; **hydrochloric acid** for
  SC-2.[^wiki-rca]
* **Ultrapure DI water**, **isopropanol**, **nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`2PSDI <step-083>` (the last implant through the
  resist); mask: {ref}`PSDM <step-081>`; first implant:
  {ref}`PSDI <step-082>`.
* Next: {ref}`NSDM <step-085>` (coated on the cleaned surface).
* The companion strip: {ref}`NSDIS <step-087>`; the other high-dose
  strip: {ref}`P1IS <step-051>`; light-dose strips for contrast:
  {ref}`LVTNIS <step-016>`, {ref}`ASTIS <step-067>`.
* The oxide the strip must preserve: {ref}`SPOX <step-080>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — GaSonics PEP, Iridia and
  Mattson Aspen II with gases and temperatures; Akrion Gamma; DNS and
  FSI benches.[^skw-01]
* Indeed, SkyWater listings — defect-metrology tools including
  AIT.[^job-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — popping and
  the low-temperature first ash.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — the carbonised
  crust.[^pat-strip-tsmc]

### High-level understanding

* Wikipedia, *Plasma ashing* — downstream ashing and implanted
  resist.[^wiki-ash]
* Wikipedia, *RCA clean* and *Piranha solution* — the wet
  chemistries.[^wiki-rca][^wiki-piranha]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 —
  implanted-resist stripping.[^txt-05]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — source/drain
  doses.[^txt-01]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — ash
  and wet-clean tools.[^txt-07]

### Deep dive

* Fujimura et al. (Fujitsu), *JJAP* 1989 — the crust-and-popping
  mechanism of implanted resist.[^fujimura-1989]
* Fujimura et al. (Fujitsu), *JJAP* 1990 — nitrogen addition in
  downstream ashing.[^fujimura-1990]
* Fujimura et al. (Fujitsu), *JVST B* 1994 — O₂+H₂O downstream ashing
  without sodium contamination.[^fujimura-1994]
* Roche, Michaud and Bruel, *MRS Proc.* 1985 — resist outgassing
  during implantation, the origin of the crust.[^roche-1985]
* Horsky, IIT 1998, and Carpenter and Fecteau, IIT 2002 —
  outgassing in high-current implanters and its management.[^horsky-1998][^carpenter-2002]
* Romig, Bishop and Rio, IIT 1996 — resist burning in a high-current
  implanter, the worst case a strip can meet.[^romig-1996]
* Visintin, Korzenski and Baum, *J. Electrochem. Soc.* 2006 — liquid
  formulations for high-dose implanted resist.[^visintin-2006]
* Kern, *J. Electrochem. Soc.* 1990 — the RCA clean and its
  evolution.[^kern-1990]
* Ohmi, *J. Electrochem. Soc.* 1996 — room-temperature wet
  cleaning.[^ohmi-1996]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — post-implant stripping.[^reinhardt-2010]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the two-stage
  low-temperature ash.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — ashing around the
  crust.[^pat-strip-tsmc]
* Nakayama et al. (ULVAC), US 5,795,831 — a cold stripping
  process.[^pat-strip-ulvac]
* Becknell, Hammar and Ferris (Axcelis), US 7,449,416, and Kamarehi
  and Simpson (Fusion Systems), US 5,498,308 — asher
  designs.[^pat-asher-axcelis][^pat-asher-fusion]

## Open questions

* The SKY130 ash recipe (temperatures, gases, step times) and wet
  sequence are not public.
* Whether the clean includes SC-2, and how much
  {ref}`SPOX <step-080>` oxide loss is budgeted, is not public.
* Which asher runs the high-dose strips is inferred from the
  published gas and temperature ranges.[^skw-01]

<!-- footnotes -->

[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page), retrieved 2026-08-30; listings expire.
    <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^fujimura-1990]: S. Fujimura, K. Shinagawa, M. Nakamura and H. Yano,
    "Additive Nitrogen Effects on Oxygen Plasma Downstream Ashing",
    *Japanese Journal of Applied Physics* **29**(10R), 2165 (1990).
    <https://doi.org/10.1143/JJAP.29.2165>
[^fujimura-1994]: S. Fujimura, M. T. Suzuki, K. Shinagawa and M.
    Nakamura, "Sodium contamination free ashing process using O₂+H₂O
    plasma downstream", *Journal of Vacuum Science & Technology B*
    **12**(4), 2409–2413 (1994). <https://doi.org/10.1116/1.587773>
[^roche-1985]: D. Roche, J. F. Michaud and M. Bruel, "Outgassing of
    Photoresist During Ion Implantation", *MRS Proceedings* **45**
    (1985). <https://doi.org/10.1557/PROC-45-203>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^carpenter-2002]: N. Carpenter and T. Fecteau, "Process and
    productivity improvements during high pressure photoresist
    outgassing", *Proc. 14th International Conference on Ion
    Implantation Technology* (2002), pp. 507–510.
    <https://doi.org/10.1109/IIT.2002.1258053>
[^romig-1996]: T. Romig, M. Bishop and V. Rio, "Exploration and
    prevention of photo resist burning in a high current ion
    implanter", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 190–193.
    <https://doi.org/10.1109/IIT.1996.586181>
[^visintin-2006]: P. M. Visintin, M. B. Korzenski and T. H. Baum,
    "Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
    Photoresist from Microelectronic Devices", *Journal of The
    Electrochemical Society* **153**(7), G591 (2006).
    <https://doi.org/10.1149/1.2195884>
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
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^pat-strip-tsmc]: B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), *Method
    of ashing a photoresist*, US 2004/0214448 A1, published 2004-10-28.
    <https://patents.google.com/patent/US20040214448A1/en>
[^pat-strip-ulvac]: I. Nakayama et al. (ULVAC Technologies), *Cold
    processes for cleaning and stripping photoresist from surfaces of
    semiconductor wafers*, US 5,795,831 A, granted 1998-08-18.
    <https://patents.google.com/patent/US5795831A/en>
[^pat-asher-axcelis]: A. F. Becknell, P. Hammar and D. Ferris (Axcelis
    Technologies), *Apparatus and plasma ashing process for increasing
    photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
[^pat-asher-fusion]: M. Kamarehi and J. E. Simpson (Fusion Systems),
    *Plasma asher with microwave trap*, US 5,498,308 A, granted
    1996-03-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
