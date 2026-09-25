(step-025)=
# Step 025 — PCHIS: P-channel BF2 implant strip

| | |
|---|---|
| **Step number** | 25 of 171[^steps-sheet] |
| **Step code** | `PCHIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`PNCHI <step-024>` |
| **Next step** | {ref}`PWBM <step-026>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** strips the `HVTPM` resist after the two high-Vt PMOS
  channel implants and cleans the wafer for `PWBM`.
* **Why:** a fresh resist cannot be spun over the old one, and residue
  would block the P-well implants and reach the RTAI anneal.
* **Public numbers:** none published for SKY130.
* **Likely SkyWater tool:** GaSonics PEP / Iridia RF microwave /
  Mattson Aspen II ashers — strong (existence); inference
  (assignment).[^skw-01]
* **Not public:** the SKY130 strip recipe (→ Open questions).
:::

## What this step is

`PCHIS` strips the photoresist patterned at {ref}`HVTPM <step-022>`
after it has masked the two high-Vt PMOS channel implants
{ref}`PCHI <step-023>` and {ref}`PNCHI <step-024>`, and cleans the wafer
for the P-well {term}`block mask` {ref}`PWBM <step-026>`. The step list used in
this reference names it after the last implant ("P-channel BF2 implant
strip").

:::{figure} /_static/figures/wells-025-pchis.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step resist covers the left-hand part of the drawing. After it the resist is gone and the oxide surface is bare across the slice; the N-well and the implanted surface bands are unchanged.
:width: 560px
:name: fig-wells-025-pchis

Before, the HVTPM resist after its two implants; after, the resist gone and the oxide bare, with the well and the PMOS channel implants untouched. The page infers that the pad oxide is still present and has to survive as the screen for the implants still to come, so it is drawn in place. The NMOS channel implant and the liner oxide are drawn faded. Not to scale.
:::

The resist is the i-line implant-block resist (roughly 1 µm, inferred on
the {ref}`HVTPM <step-022>` page). It has received two keV-class channel
implants at light doses (of order 10¹²–10¹³ cm⁻² each, illustrative;
{ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`), the second of them BF₂ on
this reference's reading. As at
{ref}`LVTNIS <step-016>` this is a *light* implant strip: the {term}`crust <implant crust>` is
thin and the {term}`popping` risk low compared with the high-energy well strips
({ref}`LVTPIS <step-021>`, {ref}`PWIS <step-029>`).

One detail is
specific to it: BF₂ implants leave fluorine in the resist crust, and
fluorinated residues can be more tenacious in a pure-oxygen {term}`ash`, which
is one reason implant-strip recipes add hydrogen or water vapour
(category page).[^txt-05]

The surface under the resist is, we infer, still entirely oxide — pad oxide over
the active areas, trench oxide over the field — so the acid–peroxide
sequence can be used without restriction.

## Step category

`PCHIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type. The category page explains the general recipe.

**Specific to this step:**

* The next step is a *thick-resist* well mask, so the surface must be
  free of the particles that would cause pinholes or coating defects
  in a thick (2 µm-class, inferred on the {ref}`PWBM <step-026>` page)
  film.

## Why this step exists

A fresh resist for {ref}`PWBM <step-026>` cannot be spun over the old
one, and any residue left behind would block the P-well implants
locally. The crust of implanted resist is a different material from the
bulk: "the top portion of the photoresist layer is transformed into a
carbonized crust that is difficult to remove because of its low
solubility in wet strippers".[^pat-strip-tsmc] Even at light doses it
must be removed by plasma before the wet steps can finish the job, and
the implanted species and sputtered metals it contains must not be
carried into the {ref}`RTAI <step-034>` anneal.

## How it is typically performed

*An industry-generic light-implant strip for a 200 mm, 130 nm-era fab:*

1. **Plasma ash.** Downstream oxygen plasma with a nitrogen or
   forming-gas addition. For light doses a single-stage recipe is
   typical, at a temperature in the 200–270 °C class
   (industry-typical).[^txt-02]

   SkyWater's published asher ranges
   (120–270 °C, 40–270 °C and up to 250 °C) span it,[^skw-01] which is
   a capability, not a recipe. Fabs that run one standard
   implant-strip recipe use the two-stage sequence anyway — a first
   stage below about 220 °C "by oxygen and nitrogen/hydrogen plasma"
   until the crust is gone, then a hotter bulk stage.[^pat-strip-mosel]

   The remote configuration lets "electrically charged particles time to
   recombine before they reach the wafer surface".[^wiki-ash] SkyWater's
   ashers span "120C – 270C" (GaSonics PEP), "40C-270C" (Iridia) and "up
   to 250C" (Mattson Aspen II), with N₂, O₂, H₂/N₂ and CF₄
   options.[^skw-01]
2. **Wet strip.** {term}`SPM` (H₂SO₄:H₂O₂) — "used to clean organic residues off
   substrates" (category page, citing Wikipedia) — on a batch bench;
   SkyWater's Akrion Gamma lists "Sulfuric".[^skw-01]
3. **Clean.** {term}`SC-1` for particles, optionally {term}`SC-2` for metals.[^wiki-rca]
   No HF: the pad oxide (which we infer is still present) must survive
   as the screen for the four implants still to come.
4. **Rinse, dry, inspect.** Cascade rinse, spin or IPA dry, particle
   scan.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm single-wafer (GaSonics
  Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK) (category page).
* **{ref}`Batch wet bench <machine-wet-bench>`** (SPM, SC-1, SC-2) or **{ref}`spray processor <machine-wet-bench>`**.
* **{ref}`Surface scanner <machine-defect-inspection>`** (KLA-Tencor Surfscan class) for particles.

## Machines likely used at SkyWater

| Tool | Evidence |
|---|---|
| GaSonics PEP, Iridia RF microwave, Mattson Aspen II | strong (existence); inference (assignment) |
| Akrion Gamma batch wet bench | strong (existence) |
| DNS wet bench / FSI Mercury | strong (existence) |
| KLA-Tencor SP1 | medium |

* **GaSonics PEP, Iridia RF microwave, Mattson Aspen II**
  - *SkyWater says:* lists them.[^skw-01]
  - *Tool exists:* strong.
  - *Runs this step:* inference.
* **Akrion Gamma batch wet bench**
  - *SkyWater says:* lists "Sulfuric, SC1".[^skw-01]
  - *Tool exists:* strong for existence.
* **DNS wet bench / FSI Mercury**
  - *SkyWater says:* lists them.[^skw-01]
  - *Tool exists:* strong for existence.
* **KLA-Tencor SP1** (unpatterned surface scanner)
  - *SkyWater says:* lists "SEM/AIT/KLA/SP1/EV300/1X" in a job
    posting.[^job-06]
  - *Tool exists:* medium.
  - *Runs this step:* "SP1" is our reading of that list.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {term}`forming gas` ({ref}`H₂/N₂ <material-anneal-ambients>`)** for the ash; **{ref}`CF₄ <material-etch-gases>`**,
  listed on the Iridia and Mattson ashers,[^skw-01] attacks the pad and
  trench oxide and would, we infer, be omitted here (category page).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide, hydrochloric
  acid** ({ref}`wet chemicals <material-wet-chemicals>`)[^wiki-rca] (category page).
* **{ref}`DI water <material-ultrapure-water>`, isopropanol, nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`PNCHI <step-024>`. The resist came from
  {ref}`HVTPM <step-022>` and also masked {ref}`PCHI <step-023>`.
* Next: {ref}`PWBM <step-026>` (thick-resist P-well block mask).
* Same category: sister strips — {ref}`LVTNIS <step-016>`,
  {ref}`LVTPIS <step-021>`, {ref}`PWIS <step-029>`,
  {ref}`PWDEIS <step-033>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Cold processes for cleaning and stripping photoresist from surfaces of semiconductor wafers <patent-gp26794054>` — US 5,795,831 A (1996)
* {ref}`Low temperature dry process for stripping photoresist after high dose ion implantation <patent-gp25102092>` — US 5,811,358 A (1997)
* {ref}`Method of ashing a photoresist <patent-gp33298522>` — US 2004/0214448 A1 (2003)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the site tool list.[^skw-01]
* [LinkedIn, SkyWater Technology Foundry listings](<https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>) —
  "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* [Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358](<https://patents.google.com/patent/US5811358A/en>) — the popping
  mechanism and a low-temperature O₂/N₂/H₂ first ash
  stage.[^pat-strip-mosel]
* [Chan, Chiu and Tao (TSMC), US 2004/0214448](<https://patents.google.com/patent/US20040214448A1/en>) — the "carbonized crust" of
  implanted resist.[^pat-strip-tsmc]

### High-level understanding

* [Wikipedia, *Plasma ashing*](<https://en.wikipedia.org/wiki/Plasma_ashing>) — downstream ashing and implanted-resist
  problems.[^wiki-ash]
* [Wikipedia, *RCA clean*](<https://en.wikipedia.org/wiki/RCA_clean>) — SC-1 and SC-2 compositions and
  temperatures.[^wiki-rca]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — lithography
  tools, implanted-resist stripping and {term}`RTP` of the 0.25–0.13 µm
  generations.[^txt-05]

### Deep dive

* [Kern, *J. Electrochem. Soc.* 1990](<https://doi.org/10.1149/1.2086825>) — the history and chemistry of the
  {term}`RCA clean`.[^kern-1990]
* [Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1989](<https://doi.org/10.1143/JJAP.28.2130>) — the carbonised
  layer of high-dose implanted resist, the residues of O₂ ashing and a
  two-step ashing process (abstract).[^fujimura-1989]
* [Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1990](<https://doi.org/10.1143/JJAP.29.2165>) — why nitrogen
  is added to oxygen in downstream ashing.[^fujimura-1990]
* [Fujimura et al. (Fujitsu), *J. Vac. Sci. Technol. B* 1994](<https://doi.org/10.1116/1.587773>) —
  water-vapour addition to downstream ashing, the origin of the H₂O/H₂
  chemistries on modern ashers.[^fujimura-1994]
* [Ohmi, *J. Electrochem. Soc.* 1996](<https://doi.org/10.1149/1.1837133>) — a room-temperature alternative to
  the hot SPM/SC-1/SC-2 sequence.[^ohmi-1996]
* [Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing*](<https://doi.org/10.1002/9781118071748>) — a modern handbook treatment of post-implant stripping
  and wet cleaning.[^reinhardt-2010]
* [Nakayama et al. (ULVAC), US 5,795,831](<https://patents.google.com/patent/US5795831A/en>) — a cold process for stripping
  implanted resist, showing the alternatives to hot
  ashing.[^pat-strip-ulvac]
* [Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358](<https://patents.google.com/patent/US5811358A/en>) — the two-stage
  low-temperature ash for implanted resist.[^pat-strip-mosel]
* [Chan, Chiu and Tao (TSMC), US 2004/0214448](<https://patents.google.com/patent/US20040214448A1/en>) — an ashing sequence
  designed around the carbonised crust.[^pat-strip-tsmc]

## Open questions

* **Strip recipe.** The SKY130 strip recipe is not public.
* **Recipe tailoring.** Whether the fab uses one generic implant-strip
  recipe for all light and heavy implants, or tailors it, is unknown.

<!-- footnotes -->

[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
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
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
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
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
