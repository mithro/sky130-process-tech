(step-029)=
# Step 029 — PWIS: P-well implant strip

| | |
|---|---|
| **Step number** | 29 of 171[^steps-sheet] |
| **Step code** | `PWIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWI2 <step-028>` |
| **Next step** | {ref}`PWDEM <step-030>` |

## What this step is

`PWIS` removes the thick P-well block resist patterned at
{ref}`PWBM <step-026>`, which has masked the two boron well implants
{ref}`PWI <step-027>` and {ref}`PWI2 <step-028>`, and cleans the wafer
for the last mask of the module, {ref}`PWDEM <step-030>`.

The resist is a thick (about 2 µm class, inferred on the
{ref}`PWBM <step-026>` page) implant resist that has absorbed boron at a
few hundred keV and a summed dose of order 10¹³ cm⁻² (both illustrative;
{ref}`PWI <step-027>`). It is therefore a *heavy* implant strip of the
same kind as {ref}`LVTPIS <step-021>` and {ref}`DNIS <step-009>`, with a
carbonised {term}`crust <implant crust>` and a real {term}`popping` risk, although boron — light and
with a long range — deposits less of its energy in the top of the resist
than phosphorus does, so the crust is somewhat thinner than after the
N-well implants[^txt-01] (inference). Because `PWBM` is a *block* mask,
the resist covered only the N-wells and the 20 V regions: most of the
wafer was open and the resist area to be removed is smaller than for a
normal mask.

The surface beneath is, we infer, still all oxide (pad oxide on active, trench
oxide on field), so the full {term}`SPM`/{term}`SC-1`/{term}`SC-2` sequence is available.

## Step category

`PWIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type, the fourth of five in this module. The category
page's discussion of the crust and of two-stage {term}`ashing <ash>` applies in
full.

## Why this step exists

The next lithography, {ref}`PWDEM <step-030>`, is another thick implant
resist that must be coated on a clean surface; any residue of this
resist would print as a defect and would block the {term}`drain-extended <DEMOS>` P-well
implants locally — in a 20 V device, exactly where the doping is most
critical. The crust must be removed by plasma first: "the top portion of
the photoresist layer is transformed into a carbonized crust that is
difficult to remove because of its low solubility in wet
strippers".[^pat-strip-tsmc] And it must be removed without popping,
which "spreads particles of the implant-hardened cross-link hydrogen
deficient surface layer material throughout the stripping
chamber".[^pat-strip-mosel] Finally, the metals that a batch implanter's
disc and beam-line sputter onto the resist must be cleaned off before
the wafer reaches the {ref}`RTAI <step-034>` anneal, where they would be
driven into the silicon.

## How it is typically performed

An industry-generic heavy-implant-resist strip for a 200 mm,
130 nm-era fab:

1. **Two-stage plasma ash.** First stage below the popping threshold
   with oxygen plus {term}`forming gas` — "removed by oxygen and
   nitrogen/hydrogen plasma in a low-temperature (<220° C.)
   environment"[^pat-strip-mosel] — until the crust has gone, then a hot
   oxygen stage for the bulk. Downstream plasma so that neutral atomic
   oxygen does the work.[^wiki-ash] SkyWater's ashers: "Gasonic PEP,
   remote microwave plasma, N2, O2, 120C – 270C"; "Iridia RF microwave,
   N2, O2, H2, CF4, NH3, H2/N2, 40C-270C"; "Mattson Aspen2, RF plasma,
   O2, CF4, H2>N2, up to 250C".[^skw-01] {term}`Endpoint <endpoint>` on CO emission, timed
   over-ash.
2. **Wet strip.** SPM (H₂SO₄:H₂O₂ about 3:1–4:1, above 100 °C) to
   dissolve residual organics and flakes (category page);[^txt-02]
   "Sulfuric" on SkyWater's Akrion Gamma bench.[^skw-01]
3. **Clean.** SC-1 for particles and SC-2 for metals;[^wiki-rca] no HF,
   because the pad oxide is, we infer, still the screen for the two
   drain-extended implants and must remain.
4. **Rinse, dry, inspect.** Cascade rinse, spin or IPA dry; laser
   surface scan for particles and patterned inspection for residue.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** with forming-gas capability (GaSonics
  Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK).
* **{ref}`Batch wet bench <machine-wet-bench>`** (SPM, SC-1, SC-2) or **{ref}`spray processor <machine-wet-bench>`**.
* **{ref}`Surface scanner <machine-defect-inspection>`** and **patterned-wafer inspection**.

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia RF microwave, Mattson Aspen II**,[^skw-01] the
  latter two with hydrogen-bearing chemistries. Strength: **strong** for
  existence; assignment is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1").[^skw-01] Strength:
  strong for existence.
* **DNS wet bench / FSI Mercury**.[^skw-01] Strength: strong for
  existence.
* **KLA-Tencor SP1 / AIT**, our reading of "SP1" and "AIT"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {ref}`forming gas <material-anneal-ambients>` (H₂/N₂)** for the ash; **{ref}`CF₄ <material-etch-gases>`**,
  listed on the Iridia and Mattson ashers,[^skw-01] attacks the pad and
  trench oxide and would, we infer, be omitted here (category page).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide, hydrochloric
  acid** ({ref}`wet chemicals <material-wet-chemicals>`).[^wiki-rca]
* **{ref}`DI water <material-ultrapure-water>`, isopropanol, nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`PWI2 <step-028>`; the resist came from
  {ref}`PWBM <step-026>` and also masked {ref}`PWI <step-027>`.
* Next: {ref}`PWDEM <step-030>`.
* Comparable heavy-implant strips: {ref}`DNIS <step-009>`,
  {ref}`LVTPIS <step-021>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — the site tool list.[^skw-01]
* LinkedIn, SkyWater Technology Foundry listings — the defect-metrology
  tool list "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the popping
  mechanism and a low-temperature O₂/N₂/H₂ first ash
  stage.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — the "carbonized crust" of
  implanted resist.[^pat-strip-tsmc]

### High-level understanding

* Wikipedia, *Plasma ashing* — downstream ashing and implanted-resist
  problems.[^wiki-ash]
* Wikipedia, *RCA clean* — SC-1 and SC-2 compositions and
  temperatures.[^wiki-rca]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — energy
  deposition of light versus heavy ions.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — lithography
  tools, implanted-resist stripping and {term}`RTP` of the 0.25–0.13 µm
  generations.[^txt-05]

### Deep dive

* Kern, in Reinhardt and Kern (eds.), *Handbook of Silicon Wafer
  Cleaning Technology* — overview chapter on wet-cleaning chemistry and
  contamination.[^kern-handbook]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1989 — the carbonised
  layer of high-dose implanted resist, the residues of O₂ ashing and a
  two-step ashing process (abstract).[^fujimura-1989]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1990 — why nitrogen
  is added to oxygen in downstream ashing.[^fujimura-1990]
* Fujimura et al. (Fujitsu), *J. Vac. Sci. Technol. B* 1994 —
  water-vapour addition to downstream ashing, the origin of the H₂O/H₂
  chemistries on modern ashers.[^fujimura-1994]
* Ohmi, *J. Electrochem. Soc.* 1996 — a room-temperature alternative to
  the hot SPM/SC-1/SC-2 sequence.[^ohmi-1996]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — a modern handbook treatment of post-implant stripping
  and wet cleaning.[^reinhardt-2010]
* Nakayama et al. (ULVAC), US 5,795,831 — a cold process for stripping
  implanted resist, showing the alternatives to hot
  ashing.[^pat-strip-ulvac]
* Lee et al. (Genus), IIT 1996 — outgassing of thick resists during MeV
  implantation.[^lee-1996]
* Horsky (Eaton), IIT 1998 — resist outgassing in high-energy and
  high-current implanters.[^horsky-1998]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the two-stage
  low-temperature ash for high-dose implanted resist.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — an ashing sequence
  designed around the carbonised crust.[^pat-strip-tsmc]

## Open questions

* The strip recipe and wet sequence are not public.
* Whether an SC-2 metal clean is included here or deferred to the
  pre-anneal clean before {ref}`RTAI <step-034>` is unknown.

<!-- footnotes -->

[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^pat-strip-tsmc]: B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), *Method
    of ashing a photoresist*, US 2004/0214448 A1, published 2004-10-28.
    <https://patents.google.com/patent/US20040214448A1/en>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
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
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^pat-strip-ulvac]: I. Nakayama et al. (ULVAC Technologies), *Cold
    processes for cleaning and stripping photoresist from surfaces of
    semiconductor wafers*, US 5,795,831 A, granted 1998-08-18.
    <https://patents.google.com/patent/US5795831A/en>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
