(step-016)=
# Step 016 — LVTNIS: Low Vt NMOS implant strip

| | |
|---|---|
| **Step number** | 16 of 171[^steps-sheet] |
| **Step code** | `LVTNIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`LVTNI <step-015>` |
| **Next step** | {ref}`NWM <step-017>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** strips the implanted resist from `LVTNI` and cleans the
  wafer for the next mask.
* **Why:** photoresist must be gone before recoating, and implant
  residue must be removed before the next implant and the RTAI
  anneal.
* **Public numbers:** none published for SKY130.
* **Likely SkyWater tool:** GaSonics PEP / Iridia RF microwave /
  Mattson Aspen II ashers — strong (existence); inference
  (assignment).[^skw-01]
* **Not public:** the SKY130 ash recipe and wet sequence (→ Open
  questions).
:::

## What this step is

`LVTNIS` removes the photoresist that was patterned at
{ref}`LVTNM <step-014>` and used as the implant mask at
{ref}`LVTNI <step-015>`, then cleans the wafer so that the next mask,
{ref}`NWM <step-017>`, can be coated on a bare, particle-free oxide
surface. It is the second implant-resist strip of the flow (after
{ref}`DNIS <step-009>`) and the first of five in the well and channel
module; this reference pairs every implant mask with such a strip
step.

:::{figure} /_static/figures/wells-016-lvtnis.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step implanted photoresist covers the right-hand part of the drawing and a thin hatched band lies under the left-hand active surface. After it the resist is gone, the pad oxide and the trench oxide are bare across the whole slice, and the band is unchanged.
:width: 560px
:name: fig-wells-016-lvtnis

Before, the implanted LVTNM resist; after, the resist gone and the oxide surface bare across the slice, with the NMOS channel implant untouched beneath it. The pad oxide is drawn as left in place, as the page infers: an HF dip is avoided here because the same oxide still has to screen the implants that follow. The liner oxide is drawn faded. Not to scale.
:::

The resist being removed is the roughly 1 µm i-line implant resist
inferred on the {ref}`LVTNM <step-014>` page. It has received a
channel-type implant — tens of keV, of order 10¹²–10¹³ cm⁻²
(illustrative values, {ref}`LVTNI <step-015>`) — which is a *light*
implant by strip standards. The wafer surface under it is, we infer,
entirely oxide: pad oxide over the active areas and trench oxide over
the field, with no bare silicon and no metal, so the full acid–peroxide
clean sequence can be used without restriction.

## Step category

`LVTNIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type.

The category page explains why implant strips are
"longer and more carefully engineered than etch strips": the ion beam
carbonises the top of the resist into a {term}`crust <implant crust>` that {term}`ashes <ash>` slowly and can
{term}`pop <popping>`.

For this particular strip the crust is thin, because the dose is
low and the energy modest. The strips after the well masks
({ref}`LVTPIS <step-021>`, {ref}`PWIS <step-029>`), which have seen
hundreds of keV to MeV ions and summed doses near 10¹³ cm⁻², and above
all the source/drain strips ({ref}`PDIS <step-084>`,
{ref}`NSDIS <step-087>`) at several 10¹⁵ cm⁻² (illustrative), are the
difficult ones.

## Why this step exists

Photoresist must be gone before the wafer can be coated again: a new
resist cannot be spun over an old one, and any organic residue under the
{ref}`NWM <step-017>` resist would print as a defect or block the MeV
well implant locally. The resist also carries the implanted species in
its crust and whatever metals the implanter's beam-line has sputtered
onto it; both must be removed before the wafer sees the next implant
and, eventually, the {ref}`RTAI <step-034>` anneal.

A poorly stripped
implant resist shows up as popped flakes — the patent literature notes
that "the popping problem … causes the photoresist to become even
harder"[^pat-strip-mosel] and as threshold-voltage outliers where
residue {term}`shadowed <shadowing>` a later implant.

## How it is typically performed

*An industry-generic implant-strip sequence for a 200 mm, 130 nm-era
fab:*

1. **Plasma ash.** Downstream (remote) microwave or RF oxygen plasma.

   The problem specific to implanted resist is that "the top portion of
   the photoresist layer is transformed into a carbonized crust that is
   difficult to remove".[^pat-strip-tsmc] During a conventional
   "high temperature (>200° C.) dry ashing" the volatile bulk resist can
   "build up pressure beneath the implant-hardened surface layer" until
   it pops.[^pat-strip-mosel]

   The standard countermeasure is a two-step
   recipe: a first step at low temperature — "removed by oxygen and
   nitrogen/hydrogen plasma in a low-temperature (<220° C.)
   environment"[^pat-strip-mosel] — until the crust is gone, then a
   hotter bulk step. For a low-dose channel implant like `LVTNI` many
   fabs use a single-step recipe, because the crust is thin (industry
   practice).[^txt-05]

   SkyWater's list describes ashers with exactly
   this gas set and temperature range: "Gasonic PEP, remote microwave
   plasma, N2, O2, 120C – 270C", "Iridia RF microwave, N2, O2, H2, CF4,
   NH3, H2/N2, 40C-270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2,
   up to 250C".[^skw-01] Downstream configuration is chosen because
   "monatomic oxygen is electrically neutral" and the remote plasma
   "prevents damage to the wafer surface".[^wiki-ash]
2. **Wet strip and clean.** Sulphuric acid–hydrogen peroxide ({term}`SPM`,
   "piranha") to dissolve the last organics.

   The category page, citing Wikipedia, gives "a typical mixture is 3
   parts of concentrated sulfuric acid and 1 part of 30 wt. % hydrogen
   peroxide solution". This is followed by
   {term}`SC-1` (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles and, optionally, {term}`SC-2`
   (HCl/H₂O₂/H₂O) for metals.[^wiki-rca] SkyWater's Akrion Gamma bench
   lists "Sulfuric, SC1" among its chemistries.[^skw-01]
3. **Rinse and dry.** Cascade DI-water rinse, spin-rinse or IPA
   (Marangoni) dry.
4. **Inspection.** Patterned-wafer optical inspection for residue and
   particles.

We infer that the pad oxide is left in place: a dilute-HF "oxide-last"
step is avoided here because the same oxide must still screen the three
implants that follow ({ref}`NWI <step-018>` to {ref}`LVTPI <step-020>`).
Some flows accept a small oxide loss in SC-1 as the price of
cleanliness.[^txt-02]

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm single-wafer: GaSonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES series, PSK
  (category page).
* **{ref}`Batch wet bench <machine-wet-bench>`** with SPM, SC-1, SC-2 tanks and a rinser/dryer
  (Akrion, DNS/SCREEN, SCP), or a **{ref}`spray processor <machine-wet-bench>`** (FSI Mercury).
* **{ref}`Patterned-wafer inspection <machine-defect-inspection>`** (KLA-Tencor 2xxx/AIT class).

## Machines likely used at SkyWater

| Tool | Evidence |
|---|---|
| GaSonics PEP, Iridia RF microwave, Mattson Aspen II | strong (existence); inference (assignment) |
| Akrion Gamma batch wet bench | strong (existence) |
| DNS wet bench and FSI Mercury | strong (existence) |
| KLA-Tencor AIT | medium |

* **GaSonics PEP, Iridia RF microwave and Mattson Aspen II ashers**
  - *SkyWater says:* all named on SkyWater's facilities page with
    their gases and temperatures.[^skw-01]
  - *Tool exists:* strong.
  - *Runs this step:* the assignment of this particular strip to any
    one of them is an inference.
* **Akrion Gamma batch wet bench**
  - *SkyWater says:* lists "Sulfuric, SC1, phosphoric, BOE".[^skw-01]
  - *Tool exists:* strong for existence, for the SPM/SC-1 sequence.
* **DNS wet bench and FSI Mercury**
  - *SkyWater says:* lists "industry standard HF/SC1/SC2".[^skw-01]
  - *Tool exists:* strong for existence, as alternative clean tools.
* **KLA-Tencor AIT** (patterned-wafer inspection)
  - *SkyWater says:* our reading of "AIT" in a SkyWater job posting's
    "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  - *Tool exists:* medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {term}`forming gas` ({ref}`H₂/N₂ <material-anneal-ambients>`)** for the ash; **{ref}`CF₄ <material-etch-gases>`**,
  listed on the Iridia and Mattson ashers,[^skw-01] attacks the pad and
  trench oxide and would, we infer, be omitted here (category page).
* **Sulphuric acid and hydrogen peroxide** (semiconductor-grade
  concentrated acid and 30 % peroxide, the usual SPM
  reagents[^wiki-piranha]) ({ref}`wet chemicals <material-wet-chemicals>`);
  **ammonium hydroxide** for SC-1; **hydrochloric acid**
  for SC-2[^wiki-rca] (category page).
* **{ref}`Ultrapure DI water <material-ultrapure-water>`**, **isopropanol** for drying, **nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LVTNI <step-015>` (the implant whose resist is
  stripped).
* Next: {ref}`NWM <step-017>` (the N-well mask coated on the cleaned
  surface).
* Mask: {ref}`LVTNM <step-014>`.
* Same category: companion strips in this module —
  {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`,
  {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`; the earlier
  {ref}`DNIS <step-009>` stripped an MeV-implanted resist.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Cold processes for cleaning and stripping photoresist from surfaces of semiconductor wafers <patent-gp26794054>` — US 5,795,831 A (1996)
* {ref}`Low temperature dry process for stripping photoresist after high dose ion implantation <patent-gp25102092>` — US 5,811,358 A (1997)
* {ref}`Method of ashing a photoresist <patent-gp33298522>` — US 2004/0214448 A1 (2003)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — GaSonics PEP; Iridia; Mattson
  Aspen II; Akrion Gamma; DNS and FSI Mercury benches.[^skw-01]
* [LinkedIn, SkyWater Technology Foundry listings](<https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>) — the defect-metrology
  tool list "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
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
  resist stripping; wafer cleaning.[^txt-02]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — implanted-resist
  stripping.[^txt-05]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) — ash and
  wet-clean tools.[^txt-07]

### Deep dive

* [Kern, *J. Electrochem. Soc.* 1990](<https://doi.org/10.1149/1.2086825>) — the history and chemistry of the
  {term}`RCA clean`.[^kern-1990]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — surface preparation.[^itrs-01]
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
* [Roche, Michaud and Bruel, *MRS Proc.* 1985](<https://doi.org/10.1557/PROC-45-203>) — resist outgassing during
  implantation, the origin of the hardened crust the strip
  removes.[^roche-1985]
* [Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358](<https://patents.google.com/patent/US5811358A/en>) — the two-stage
  low-temperature ash recipe for implanted resist.[^pat-strip-mosel]
* [Chan, Chiu and Tao (TSMC), US 2004/0214448](<https://patents.google.com/patent/US20040214448A1/en>) — an ashing sequence
  designed around the carbonised crust.[^pat-strip-tsmc]

## Open questions

* **Ash and wet-sequence recipe.** The SKY130 ash recipe (single- or
  two-step, temperatures, gases) and wet sequence are not public.
* **SC-2 and oxide budget.** Whether the clean includes an SC-2 step,
  and whether any oxide thinning is budgeted here, is unknown.
* **Asher assignment.** Which of the three ashers on SkyWater's public
  tool list[^skw-01] runs implant strips is not stated publicly.

<!-- footnotes -->

[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^pat-strip-tsmc]: B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), *Method
    of ashing a photoresist*, US 2004/0214448 A1, published 2004-10-28.
    <https://patents.google.com/patent/US20040214448A1/en>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
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
[^roche-1985]: D. Roche, J. F. Michaud and M. Bruel, "Outgassing of
    Photoresist During Ion Implantation", *MRS Proceedings* **45**
    (1985). <https://doi.org/10.1557/PROC-45-203>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
