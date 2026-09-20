(step-033)=
# Step 033 — PWDEIS: PWDEIS implant strip

| | |
|---|---|
| **Step number** | 33 of 171[^steps-sheet] |
| **Step code** | `PWDEIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`PWDEI2 <step-032>` |
| **Next step** | {ref}`RTAI <step-034>` |

## What this step is

`PWDEIS` removes the thick photoresist patterned at
{ref}`PWDEM <step-030>` after it has masked the two {term}`drain-extended <DEMOS>`
P-well implants {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>`,
and cleans the wafer for the {ref}`RTAI <step-034>` anneal. It is the
last of the five implant strips of the well and channel module, and
the only one that is followed not by another lithography but by a
high-temperature step — which raises its cleanliness requirement to
the "pre-furnace" level of {ref}`DNIS <step-009>`.

The resist is a thick implant resist (2 µm class, inferred on the
{ref}`PWDEM <step-030>` page) that has received two light boron implants
— of order 10¹² cm⁻² each, illustrative ({ref}`PWDEI1 <step-031>`) — at
energies, illustratively, up to a few hundred keV. The {term}`crust <implant crust>` is
therefore modest by the standards of {ref}`LVTPIS <step-021>`, and
because `pwde` regions are small the open area of the mask is small too:
the strip removes almost a full wafer's worth of resist. The surface
beneath is, we infer, all oxide (pad oxide on active, trench oxide on
field).

## Step category

`PWDEIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type with a *pre-anneal clean* role. The category page
notes that the state in which the surface is left "must match what
the next step expects"; here the next step is an {term}`RTA` in which any
organic or metallic residue would be baked into the silicon.

## Why this step exists

Photoresist cannot go into an anneal chamber: at the ~1000 °C of a
typical activation anneal it would carbonise, contaminate the chamber
and leave the wafer covered in particles, and the mobile-ion and organic
contamination it carries would be driven into the channels that every
implant of this module has just defined. The strip must therefore remove
all resist and its crust — "transformed into a carbonized crust that is
difficult to remove"[^pat-strip-tsmc] — without
{term}`popping`,[^pat-strip-mosel] and the clean must take off the metals
sputtered onto the wafer over ten implants. ITRS 2001 treats front-end
surface preparation as a first-order concern for exactly this
reason.[^itrs-01] A residue left here would be sealed under the gate
oxides grown at {ref}`GOX100 <step-043>` and {ref}`LVGOX <step-047>`.

## How it is typically performed

An industry-generic strip-and-pre-anneal-clean sequence for a 200 mm,
130 nm-era fab:

1. **Plasma {term}`ash`.** Downstream oxygen plasma with a forming-gas addition;
   a two-stage recipe if the fab runs one for all implant strips — first
   stage "in a low-temperature (<220° C.) environment" with "oxygen and
   nitrogen/hydrogen plasma" until the crust is gone,[^pat-strip-mosel]
   then a hotter bulk stage. SkyWater's ashers cover this range:
   "Gasonic PEP … N2, O2, 120C – 270C", "Iridia … H2/N2, 40C-270C",
   "Mattson Aspen2 … O2, CF4, H2>N2, up to 250C".[^skw-01] The remote
   plasma keeps charged species off the wafer.[^wiki-ash]
2. **Wet strip.** {term}`SPM` (H₂SO₄:H₂O₂) for residual organics (category page;
   "Sulfuric" on the Akrion Gamma[^skw-01]).
3. **Full RCA-type clean.** {term}`SC-1` (NH₄OH/H₂O₂/H₂O, 75–80 °C) for
   particles and {term}`SC-2` (HCl/H₂O₂/H₂O, 75–80 °C) for
   metals[^wiki-rca][^kern-1990] — the SC-2 step matters more here than
   after the earlier strips because the anneal follows. SkyWater lists
   "DNS wet bench industry standard HF/SC1/SC2" and "FSI Mercury
   industry standard HF/SC1/SC2 rotational".[^skw-01]
4. **HF or not?** Whether the pad oxide is removed before the anneal is
   a real choice. Keeping it protects the silicon surface during the RTA
   and avoids dopant out-diffusion; removing it now would require a
   fresh sacrificial oxide before gate oxidation. This reference
   describes no sacrificial oxidation before {ref}`GOX100 <step-043>`
   and so treats the pad oxide as *kept* through the anneal (an
   assumption; see the open question on {ref}`NS19 <step-013>`).
5. **Rinse, dry, inspect.** Cascade rinse, IPA (Marangoni) or spin dry;
   laser surface scan for particles.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** (GaSonics Aura/PEP, Mattson Aspen,
  Axcelis/Fusion ES, PSK).
* **{ref}`Batch wet bench <machine-wet-bench>`** with SPM, SC-1, SC-2 and rinser/dryer, or a
  **{ref}`spray <machine-wet-bench>`/{ref}`single-wafer processor <machine-single-wafer-spin-processor>`** for the {term}`RCA clean`.
* **{ref}`Surface scanner <machine-defect-inspection>`** (KLA-Tencor Surfscan class).

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia RF microwave, Mattson Aspen II**.[^skw-01]
  Strength: **strong** for existence; assignment is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1")[^skw-01] for the
  SPM/SC-1 steps. Strength: strong for existence.
* **DNS wet bench / FSI Mercury** ("HF/SC1/SC2")[^skw-01] for the
  pre-anneal RCA clean. Strength: strong for existence; the SC-2
  capability is explicitly listed only for these two tools, which makes
  them the natural pre-anneal clean stations (inference).
* **KLA-Tencor SP1** surface scanner, our reading of "SP1"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {term}`forming gas` ({ref}`H₂/N₂ <material-anneal-ambients>`)** for the ash; **{ref}`CF₄ <material-etch-gases>`**,
  listed on the Iridia and Mattson ashers,[^skw-01] attacks the pad and
  trench oxide and would, we infer, be omitted here (category page).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide, hydrochloric
  acid** ({ref}`wet chemicals <material-wet-chemicals>`)[^wiki-rca] (category page); **dilute HF** only if the oxide is
  removed.
* **{ref}`Ultrapure DI water <material-ultrapure-water>`**, **isopropanol**, **nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`PWDEI2 <step-032>`; the resist came from
  {ref}`PWDEM <step-030>` and also masked {ref}`PWDEI1 <step-031>`.
* Next: {ref}`RTAI <step-034>` (the anneal this clean prepares for).
* Earlier module strips: {ref}`LVTNIS <step-016>`,
  {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`,
  {ref}`PWIS <step-029>`; the analogous pre-furnace strip in the
  isolation module is {ref}`DNIS <step-009>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,795,831 A <patent-gp26794054>` — Cold processes for cleaning and stripping photoresist from surfaces of semiconductor wafers (1996)
* {ref}`US 5,811,358 A <patent-gp25102092>` — Low temperature dry process for stripping photoresist after high dose ion implantation (1997)
* {ref}`US 2004/0214448 A1 <patent-gp33298522>` — Method of ashing a photoresist (2003)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — ashers; Akrion; DNS and FSI
  "HF/SC1/SC2".[^skw-01]
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
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — wet
  cleaning.[^txt-02]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — fab-floor
  view of ash and wet-clean tools.[^txt-07]

### Deep dive

* Kern, *J. Electrochem. Soc.* 1990 — the history and chemistry of the
  RCA clean.[^kern-1990]
* ITRS 2001, *Front End Processes* — surface preparation.[^itrs-01]
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
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the two-stage
  low-temperature ash for implanted resist.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — an ashing sequence
  designed around the carbonised crust.[^pat-strip-tsmc]
* Kern, in Reinhardt and Kern (eds.), *Handbook of Silicon Wafer
  Cleaning Technology* — the overview chapter on wet-cleaning chemistry
  and metallic contamination before thermal steps.[^kern-handbook]

## Open questions

* Whether the pad oxide is retained through {ref}`RTAI <step-034>` or
  removed here is not stated publicly; this page assumes it is
  retained.
* Whether the pre-anneal clean is part of this step or belongs to
  {ref}`RTAI <step-034>` is unknown.
* The strip recipe is not public.

<!-- footnotes -->

[^pat-strip-tsmc]: B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), *Method
    of ashing a photoresist*, US 2004/0214448 A1, published 2004-10-28.
    <https://patents.google.com/patent/US20040214448A1/en>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
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
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
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
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
