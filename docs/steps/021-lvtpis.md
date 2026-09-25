(step-021)=
# Step 021 — LVTPIS: P-channel implant strip

| | |
|---|---|
| **Step number** | 21 of 171[^steps-sheet] |
| **Step code** | `LVTPIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`LVTPI <step-020>` |
| **Next step** | {ref}`HVTPM <step-022>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** strips the thick N-well resist after three implants
  (`NWI`, `NWI2`, `LVTPI`) and cleans the wafer for `HVTPM`.
* **Why:** residue would block the next implant (`PCHI`) and shift
  its threshold; this is the hardest strip in the module because of
  the resist's thickness and total absorbed dose.
* **Public numbers:** none published for SKY130.
* **Likely SkyWater tool:** GaSonics PEP / Iridia RF microwave /
  Mattson Aspen II ashers — strong (existence); inference
  (assignment).[^skw-01]
* **Not public:** the SKY130 ash recipe and wet sequence (→ Open
  questions).
:::

## What this step is

`LVTPIS` removes the thick N-well photoresist that was patterned at
{ref}`NWM <step-017>` and has since masked three implants. These are
the two well implants (MeV-class phosphorus, we infer)
{ref}`NWI <step-018>` and {ref}`NWI2 <step-019>` and the keV P-channel
threshold implant {ref}`LVTPI <step-020>`. It then cleans the wafer for
the next lithography, {ref}`HVTPM <step-022>`. The step list used in this
reference names it after the last implant it follows ("P-channel implant
strip"); the resist it removes is, we infer, the N-well resist.

:::{figure} /_static/figures/wells-021-lvtpis.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step the thick implanted resist covers the left-hand part of the drawing. After it the resist is gone and the oxide surface is bare across the slice; the N-well and the implanted surface bands are unchanged.
:width: 560px
:name: fig-wells-021-lvtpis

Before, the N-well resist after its three implants; after, the resist gone and the oxide bare, with the well and the PMOS channel implant untouched. That NWI, NWI2 and LVTPI share this one resist, and so that this is the strip of the N-well resist, is this reference's reading. The pad oxide is drawn as still in place, which the page infers. The NMOS channel implant and the liner oxide are drawn faded. Not to scale.
:::

This is the hardest strip of the module. The resist is as thick as any
in the flow so far, the same 2–3 µm class inferred for the deep N-well
resist at {ref}`DNM <step-007>` and for this one at
{ref}`NWM <step-017>`. Unlike that one, it has masked three
implants rather than one. It has, we infer, absorbed more total dose
than any earlier implant resist as a result, with a summed dose of
order 10¹³ cm⁻² (illustrative; {ref}`NWI <step-018>`).

Both conditions
thicken the carbonised {term}`crust <implant crust>` and raise the risk of {term}`popping`. The wafer
surface under the resist is, we infer, still all oxide (pad oxide and trench
oxide), which allows the full {term}`SPM`/{term}`SC-1` sequence.

## Step category

`LVTPIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type; it is the direct analogue of
{ref}`DNIS <step-009>`, which removed the resist of the deep N-well
implant, and shares its recipe considerations.

## Why this step exists

The resist has to go before the next coat, and it has to go completely:
residue over a future high-Vt PMOS region would block the
{ref}`PCHI <step-023>` implant locally and produce a transistor with the
wrong threshold. The crust of an MeV-implanted resist is the obstacle.

Ion bombardment turns "the top portion of the photoresist layer … into a
carbonized crust that is difficult to remove because of its low
solubility in wet strippers".[^pat-strip-tsmc] Beneath it the
"subsurface resist generally contains more volatile, shorter molecular
weight polymer" whose vapours "build up pressure beneath the
implant-hardened surface layer". This continues
until "this pressure can violently
rupture the skin, an event that spreads particles of the
implant-hardened cross-link hydrogen deficient surface layer material
throughout the stripping chamber".[^pat-strip-mosel]

Wikipedia's summary
is that problems arise "when this photoresist has undergone an implant
step previously and heavy metal are embedded in the photoresist and it
has experienced high temperatures causing it to be resistant to
oxidizing".[^wiki-ash]

## How it is typically performed

*An industry-generic MeV-implant-resist strip for a 200 mm, 130 nm-era
fab:*

1. **Two-stage plasma {term}`ash`.** A first stage below the popping threshold —
   "removed by oxygen and nitrogen/hydrogen plasma in a low-temperature
   (<220° C.) environment", preferably 150–220 °C[^pat-strip-mosel] —
   until the crust is consumed, then a hotter oxygen stage for the bulk
   of the 2–3 µm film.

   The forming-gas addition helps because hydrogen
   penetrates and reduces the carbonised layer (category page).

   SkyWater's ashers offer exactly this: "Gasonic PEP, remote microwave
   plasma, N2, O2, 120C – 270C"; "Iridia RF microwave, N2, O2, H2, CF4,
   NH3, H2/N2, 40C-270C"; "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up
   to 250C".[^skw-01]

   Downstream plasma is used so that the neutral
   atomic oxygen does the work and charged species recombine before
   reaching the wafer.[^wiki-ash] {term}`Endpoint <endpoint>` on the CO emission line, then
   a timed over-ash.
2. **Wet strip.** SPM (H₂SO₄:H₂O₂, roughly 3:1 to 4:1, self-heated to
   above 100 °C) to dissolve the remaining organics and any popped
   flakes (category page).[^txt-02] SkyWater's Akrion Gamma bench lists
   "Sulfuric".[^skw-01]
3. **Clean.** SC-1 (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles, {term}`SC-2`
   (HCl/H₂O₂/H₂O) for the metals that an implanter's beam-line and disc
   can sputter onto the resist.[^wiki-rca] The pad oxide is preserved
   for the remaining implants.
4. **Rinse, dry, inspect.** Cascade rinse, spin or IPA dry; laser
   surface scan and patterned-wafer inspection for flakes.

The resist's thickness also matters for cycle time: at typical
downstream-asher rates of a few micrometres per minute[^txt-07] a thick
implant resist takes noticeably longer than an etch resist, and the
crust stage cannot be hurried.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** with a two-step, forming-gas-capable
  recipe: GaSonics Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK
  (category page).
* **{ref}`Batch wet bench <machine-wet-bench>`** (SPM, SC-1, SC-2) or **{ref}`spray processor <machine-wet-bench>`**.
* **{ref}`Surface scanner <machine-defect-inspection>` / patterned inspection**.

## Machines likely used at SkyWater

| Tool | Evidence |
|---|---|
| GaSonics PEP, Iridia RF microwave, Mattson Aspen II | strong (existence); inference (assignment) |
| Akrion Gamma batch wet bench | strong (existence) |
| DNS wet bench / FSI Mercury | strong (existence) |
| KLA-Tencor SP1 and AIT | medium |

* **GaSonics PEP, Iridia RF microwave, Mattson Aspen II**
  - *SkyWater says:* lists them.[^skw-01] The Iridia's "H2/N2" and the
    Mattson's "H2>N2" options are the forming-gas chemistries used for
    implant crusts.
  - *Tool exists:* strong.
  - *Runs this step:* assignment is an inference.
* **Akrion Gamma batch wet bench**
  - *SkyWater says:* lists "Sulfuric, SC1".[^skw-01]
  - *Tool exists:* strong for existence.
* **DNS wet bench / FSI Mercury**
  - *SkyWater says:* lists them for HF/SC1/SC2.[^skw-01]
  - *Tool exists:* strong for existence.
* **KLA-Tencor SP1 and AIT** (particle and residue inspection)
  - *SkyWater says:* our reading of "SP1" and "AIT" in a SkyWater job
    posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  - *Tool exists:* medium.

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

* Previous: {ref}`LVTPI <step-020>`. The resist came from
  {ref}`NWM <step-017>` and masked {ref}`NWI <step-018>` and
  {ref}`NWI2 <step-019>` as well.
* Next: {ref}`HVTPM <step-022>`.
* Same category: the comparable heavy-implant-resist strips are
  {ref}`DNIS <step-009>` and {ref}`PWIS <step-029>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Cold processes for cleaning and stripping photoresist from surfaces of semiconductor wafers <patent-gp26794054>` — US 5,795,831 A (1996)
* {ref}`Low temperature dry process for stripping photoresist after high dose ion implantation <patent-gp25102092>` — US 5,811,358 A (1997)
* {ref}`Method of ashing a photoresist <patent-gp33298522>` — US 2004/0214448 A1 (2003)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — ashers with gases and
  temperatures; Akrion, DNS, FSI benches.[^skw-01]
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
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — lithography
  tools, implanted-resist stripping and {term}`RTP` of the 0.25–0.13 µm
  generations.[^txt-05]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) — fab-floor
  view of ash and wet-clean tools.[^txt-07]

### Deep dive

* [Kern, in Reinhardt and Kern (eds.), *Handbook of Silicon Wafer
  Cleaning Technology*](<https://doi.org/10.1016/b978-081551554-8.50004-5>) — overview chapter on wet-cleaning chemistry and
  contamination.[^kern-handbook]
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
* [Lee et al. (Genus), IIT 1996](<https://doi.org/10.1109/IIT.1996.586180>) — outgassing of thick resists during MeV
  implantation, what the resist has been through before this
  strip.[^lee-1996]
* [Horsky (Eaton), IIT 1998](<https://doi.org/10.1109/IIT.1999.812201>) — resist outgassing in high-energy and
  high-current implanters.[^horsky-1998]
* [Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358](<https://patents.google.com/patent/US5811358A/en>) — the two-stage
  low-temperature ash for high-dose implanted resist.[^pat-strip-mosel]
* [Chan, Chiu and Tao (TSMC), US 2004/0214448](<https://patents.google.com/patent/US20040214448A1/en>) — an ashing sequence
  designed around the carbonised crust.[^pat-strip-tsmc]

## Open questions

* **Ash and wet-sequence recipe.** The ash recipe (stages,
  temperatures, gases) and wet sequence are not public.
* **Shared resist.** Whether the three implants really share one
  resist, and hence whether this is the strip of the N-well resist, is
  this reference's reading, following the usual single-mask
  retrograde-well practice (see {ref}`NWM <step-017>`).
* **Pad-oxide budget.** How much pad oxide is lost per strip/clean
  cycle, and whether that loss is budgeted against a later
  sacrificial-oxide step, is unknown (see the open question on
  {ref}`NS19 <step-013>`).

<!-- footnotes -->

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
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
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
