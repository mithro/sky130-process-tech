(step-054)=
# Step 054 — PRIS: PRI implant resist strip

| | |
|---|---|
| **Step number** | 54 of 171[^steps-sheet] |
| **Step code** | `PRIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — gate and poly resistors |
| **Previous step** | {ref}`PRI <step-053>` |
| **Next step** | {ref}`URPM <step-055>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** removes the `RRPM` resist after the resistor implant `PRI`
  and cleans the wafer for the next mask.
* **Why:** the next resist cannot be coated over this one, and residue
  would be sealed under the nitride cap.
* **Public numbers:** none published for SKY130.
* **Likely SkyWater tool:** GaSonics PEP, Iridia or Mattson Aspen II
  asher — strong (existence); inference (assignment).[^skw-01]
* **Not public:** the ash and wet recipes, and which asher runs the
  strip (→ Open questions).
:::

## What this step is

`PRIS` removes the reverse resistor-protect resist printed at
{ref}`RRPM <step-052>` after it has masked the resistor implant
{ref}`PRI <step-053>`, and cleans the wafer for the next mask,
{ref}`URPM <step-055>`. It is the second of the three strips in the
gate module, sitting between {ref}`P1IS <step-051>` and
{ref}`UPRIS <step-057>`, and like them it works on a bare
amorphous-silicon surface with no oxide to spare.

:::{figure} /_static/figures/poly-054-pris.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step resist covers a continuous film everywhere except one window over the middle of the oxide-filled trench. After it the resist is gone and the film is bare across the whole slice.
:width: 560px
:name: fig-poly-054-pris

Before, the implanted RRPM resist with its window over the resistor body; after, the resist gone and the gate film bare, now carrying two doping types: the n⁺ gate film and the p-type resistor body. The thin chemical oxide of the clean is not drawn. The colours of the gate film mark the type of its doping, not a depth profile. The field oxide (the oxide-filled trench in the middle) and both gate oxides are drawn but not labelled, and the liner oxide is drawn faded; the P-well and the NCHI channel implant made earlier are not drawn. Not to scale.
:::


The resist being removed differs from the one at `P1IS` in two ways:

* It is a
  *field* of resist with small windows rather than small islands, so there is far
  more of it to remove per wafer and the {term}`crust <implant crust>` is
  continuous.
* It has taken a p-type implant — boron or BF₂ at a dose of order
  10¹⁴–10¹⁵ cm⁻² (illustrative, {ref}`PRI <step-053>`) — which is lighter than
  the gate implant but still in the range where a carbonised crust
  forms.[^orvek-1985]

If BF₂ is the species, the crust also contains
fluorine. Fujimura et al. found that O₂ ashing leaves residues that
are mainly the oxide of the implanted species,[^fujimura-1989] but no
public source describes the SKY130 case, or compares the residue
burden between species (as
at {ref}`PCHIS <step-025>`, after {ref}`PNCHI <step-024>`, if that
implant is also BF₂).

## Step category

`PRIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type.

On the category page's scale it lies between the
light channel-implant strips and the heavy source/drain strips: the
dose is high enough to need the crust-first ash sequence, but not so
high that {term}`popping` is a serious risk if the first step is kept cool.

## Why this step exists

Every argument on {ref}`P1IS <step-051>` applies: the next resist cannot
be coated over this one, residue would be sealed under the nitride cap,
and the implanted crust must be removed without particles.

Two points
are specific to this strip:

* First, the surface now carries *two* doping
  levels — n⁺ poly and the p-type resistor bodies — and the clean must not
  treat them differently.

  An {term}`SC-1` step etches silicon at a measurable
  rate,[^lee-kt-1999] and a differential loss of even a few nanometres
  between body and surroundings would change the resistor's effective
  thickness, on which its {term}`sheet resistance` depends linearly.
* Second, the
  resistor bodies are the most dose-sensitive structures on the wafer, so
  nothing in the strip may add or remove dopant — a constraint that
  excludes, for example, any hot step long enough to matter, and any
  chemistry that leaches boron from the surface.

## How it is typically performed

*An industry-generic post-implant strip on a bare poly surface, for a
200 mm, 130 nm-era fab:*

1. **Plasma ash.** Downstream O₂ plasma with N₂ or {term}`forming gas`,
   beginning at low temperature to remove the crust without
   popping[^pat-strip-mosel] and finishing hot for the
   bulk.

   Water-vapour-containing chemistries ash faster than dry
   oxygen,[^fujimura-1991] which is why a
   fab with a crust to remove reaches for them. Fujimura et al. measured roughly double the atomic-oxygen
   concentration with 10 % H₂O added, and a fall in the ashing
   activation energy from about 0.5 to 0.39 eV with more than 1 % H₂O
   added.[^fujimura-1991] Fujimura et al. also showed
   that O₂ + H₂O downstream ashing is free of the sodium contamination
   that some older ashers introduced,[^fujimura-1994] which matters when
   the next film to be deposited is a gate cap.

   SkyWater's three ashers
   cover this range — the Iridia and Mattson Aspen II list H₂ or H₂/N₂
   additions and the GaSonics PEP N₂/O₂ only, at 40–270 °C between
   them.[^skw-01] A "cold" process for stripping implanted resist is
   also described in the patent literature.[^pat-strip-ulvac]
2. **Wet clean.** {term}`SPM` (H₂SO₄/H₂O₂) for residual organics, then SC-1
   for particles, with the SC-1 time limited by its silicon etch
   rate,[^lee-kt-1999] and, optionally, {term}`SC-2` for metals. The
   category page and Kern's review give the
   chemistries;[^wiki-rca][^kern-1990] Ohmi's room-temperature
   sequence is the low-thermal-budget alternative.[^ohmi-1996]
   SkyWater's Akrion Gamma bench lists "Sulfuric, SC1".[^skw-01]
3. **Rinse and dry**; **inspection** for residue and particles.

As on {ref}`P1IS <step-051>`, we infer that no HF step is used: the
chemical oxide is thin and will be buried under the
{ref}`GATENIT <step-058>` cap.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm (GaSonics Aura/PEP, Mattson
  Aspen, Axcelis/Fusion ES, PSK).
* **{ref}`Batch wet bench <machine-wet-bench>`** (Akrion, DNS/SCREEN, SCP) or **{ref}`spray processor <machine-wet-bench>`**
  (FSI Mercury) with SPM and SC-1.
* **{ref}`Patterned-wafer inspection <machine-defect-inspection>`** (KLA-Tencor AIT class).

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia and Mattson Aspen II ashers**[^skw-01]
  - *Tool exists:* **strong** for existence.
  - *Runs this step:* the assignment of this strip to
    any one of them is an inference.
* **Akrion Gamma batch bench; DNS bench; FSI Mercury**[^skw-01]
  - *Tool exists:* strong for existence.
* **Patterned-wafer inspection — KLA-Tencor AIT (our reading)**
  - *SkyWater says:* reads "General operation of
    semiconductor defect metrology tools:
    SEM/AIT/KLA/SP1/EV300/1X" in a *Defect Technician 2*
    posting.[^job-06]
  - *Tool exists:* medium.

  We read "AIT" as KLA-Tencor's
  Surfscan AIT patterned inspector, and the posting expands none of the
  abbreviations.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {ref}`forming gas <material-anneal-ambients>` (H₂/N₂)**, possibly **{ref}`NH₃ <material-precursors>`** (listed
  for the Iridia) or **water vapour** (not among SkyWater's listed asher
  gases), for the ash;[^skw-01][^fujimura-1991] **{ref}`CF₄ <material-etch-gases>`**, listed on the
  Iridia and Mattson ashers,[^skw-01] would etch the exposed silicon
  film and would, we infer, be omitted here.
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide** ({ref}`wet chemicals <material-wet-chemicals>`) for
  SPM/SC-1; **hydrochloric acid** for an optional SC-2.[^wiki-rca]
* **{ref}`DI water <material-ultrapure-water>`, isopropanol, nitrogen.**
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`PRI <step-053>`; mask: {ref}`RRPM <step-052>`.
* Next: {ref}`URPM <step-055>`.
* Same module: companion strips {ref}`P1IS <step-051>`, {ref}`UPRIS <step-057>`.
* The strip after {ref}`PNCHI <step-024>` is {ref}`PCHIS <step-025>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Plasma asher with microwave trap <patent-gp22748832>` — US 5,498,308 A (1994)
* {ref}`Cold processes for cleaning and stripping photoresist from surfaces of semiconductor wafers <patent-gp26794054>` — US 5,795,831 A (1996)
* {ref}`Low temperature dry process for stripping photoresist after high dose ion implantation <patent-gp25102092>` — US 5,811,358 A (1997)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — ashers, gases, temperatures;
  wet benches.[^skw-01]
* [LinkedIn, SkyWater *Defect Technician 2* posting](<https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>) — the
  defect-metrology tool list read as KLA-Tencor AIT.[^job-06]
* SkyWater, Form S-1 and Form 10-K — chemical suppliers.[^sec-01][^sec-02]
* [Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358](<https://patents.google.com/patent/US5811358A/en>) — the cold first
  ash step.[^pat-strip-mosel]

### High-level understanding

* Wikipedia, [*Plasma ashing*](<https://en.wikipedia.org/wiki/Plasma_ashing>) and [*RCA clean*](<https://en.wikipedia.org/wiki/RCA_clean>).[^wiki-ash][^wiki-rca]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  stripping and cleaning.[^txt-02]
* [Reinhardt and Kern (eds.), *Handbook of Silicon Wafer Cleaning
  Technology*](<https://openlibrary.org/isbn/9780815515548>) — the standard handbook.[^reinhardt-2008]

### Deep dive

* [Orvek and Huffman, *NIM B* 1985](<https://doi.org/10.1016/0168-583X(85)90421-5>) — carbonised-layer formation in
  implanted resist.[^orvek-1985]
* [Fujimura et al., *Jpn. J. Appl. Phys.* 1989](<https://doi.org/10.1143/JJAP.28.2130>) — the carbonised layer
  of high-dose implanted resist, the residues of O₂ ashing and a
  two-step ashing process (abstract).[^fujimura-1989]
* [Fujimura et al., *J. Vac. Sci. Technol. B* 1991](<https://doi.org/10.1116/1.585575>) — O₂ + H₂O downstream
  stripping, the water-vapour chemistry.[^fujimura-1991]
* [Fujimura et al., *J. Vac. Sci. Technol. B* 1994](<https://doi.org/10.1116/1.587773>) — sodium-free
  ashing, why downstream O₂/H₂O is preferred before a gate
  cap.[^fujimura-1994]
* [Roche, Michaud and Bruel, *MRS Proc.* 1985](<https://doi.org/10.1557/PROC-45-203>) — resist outgassing
  during implantation, the origin of the crust.[^roche-1985]
* [Lee, *Electrochem. Solid-State Lett.* 1999](<https://doi.org/10.1149/1.1390773>) — silicon etch rate in
  SC-1, the limit on cleaning bare poly.[^lee-kt-1999]
* [Kern, *J. Electrochem. Soc.* 1990](<https://doi.org/10.1149/1.2086825>) — evolution of wafer
  cleaning.[^kern-1990]
* [Ohmi, *J. Electrochem. Soc.* 1996](<https://doi.org/10.1149/1.1837133>) — room-temperature wet
  cleaning.[^ohmi-1996]
* [Kern, "Overview and Evolution of Silicon Wafer Cleaning Technology"](<https://doi.org/10.1016/b978-081551554-8.50004-5>)
  — the handbook chapter on post-implant stripping.[^kern-handbook]
* [Nakayama et al. (ULVAC), US 5,795,831](<https://patents.google.com/patent/US5795831A/en>) — cold stripping of implanted
  resist.[^pat-strip-ulvac]
* [Kamarehi and Simpson (Fusion Systems), US 5,498,308](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>) — downstream
  microwave asher design.[^pat-asher-fusion]
* [Wang et al., *J. Electrochem. Soc.* 1997](<https://doi.org/10.1149/1.1838075>) — fluorine effects after
  BF₂ implantation, relevant if BF₂ is the resistor species.[^wang-1997]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — surface preparation.[^itrs-01]

## Open questions

* **Ash and wet recipes.** The SKY130 ash and wet recipes are not public.
* **Protection of the resistor bodies.** Whether the resistor bodies are given any protection (for example a
  shorter SC-1) to limit differential silicon loss is unknown.
* **Which asher.** Which asher runs this strip is not stated.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^reinhardt-2008]: K. A. Reinhardt and W. Kern (eds.), *Handbook of
    Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
    ISBN 978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548>
[^orvek-1985]: K. J. Orvek and C. Huffman, "Carbonized layer formation
    in ion implanted photoresist masks", *Nuclear Instruments and
    Methods in Physics Research B* **7–8**, 501–506 (1985).
    <https://doi.org/10.1016/0168-583X(85)90421-5>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^fujimura-1991]: S. Fujimura, K. Shinagawa, M. T. Suzuki and
    M. Nakamura, "Resist stripping in an O₂+H₂O plasma downstream",
    *Journal of Vacuum Science & Technology B* **9**(2), 357–361 (1991).
    <https://doi.org/10.1116/1.585575>
[^fujimura-1994]: S. Fujimura, M. T. Suzuki, K. Shinagawa and M.
    Nakamura, "Sodium contamination free ashing process using O₂+H₂O
    plasma downstream", *Journal of Vacuum Science & Technology B*
    **12**(4), 2409–2413 (1994). <https://doi.org/10.1116/1.587773>
[^roche-1985]: D. Roche, J. F. Michaud and M. Bruel, "Outgassing of
    Photoresist During Ion Implantation", *MRS Proceedings* **45**
    (1985). <https://doi.org/10.1557/PROC-45-203>
[^lee-kt-1999]: K. T. Lee, "Etch Rate of Silicon and Silicon Dioxide in
    Ammonia-Peroxide Solutions Measured by Quartz Crystal Microbalance
    Technique", *Electrochemical and Solid-State Letters* **2**(4), 172
    (1999). <https://doi.org/10.1149/1.1390773>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^pat-strip-ulvac]: I. Nakayama et al. (ULVAC Technologies), *Cold
    processes for cleaning and stripping photoresist from surfaces of
    semiconductor wafers*, US 5,795,831 A, granted 1998-08-18.
    <https://patents.google.com/patent/US5795831A/en>
[^pat-asher-fusion]: M. Kamarehi and J. E. Simpson (Fusion Systems),
    *Plasma asher with microwave trap*, US 5,498,308 A, granted
    1996-03-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
[^wang-1997]: L. Z. Wang, M. S.-C. Luo, H.-H. Tseng and S. A. Ajuria,
    "The Influence of Fluorine on Boron-Enhanced Diffusion in Silicon by
    BF₂⁺ Implantation Through Oxide during High Temperature Rapid
    Thermal Anneal", *Journal of The Electrochemical Society*
    **144**(11), L298–L301 (1997). <https://doi.org/10.1149/1.1838075>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
