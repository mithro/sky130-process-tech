(step-087)=
# Step 087 — NSDIS: N+ source drain implant strip

| | |
|---|---|
| **Step number** | 87 of 171[^steps-sheet] |
| **Step code** | `NSDIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`NSDI <step-086>` |
| **Next step** | {ref}`RTAD <step-088>` |

## What this step is

`NSDIS` removes the photoresist patterned at {ref}`NSDM <step-085>`
after the N⁺ source/drain implant {ref}`NSDI <step-086>`, and cleans
the wafer for the source/drain activation anneal {ref}`RTAD <step-088>`
that follows directly. It is the second of the two source/drain strips
and the last resist strip of the front end before the first anneal of
the module; it is therefore also the *pre-anneal clean*, and anything
it leaves behind — organic residue, metals from the implanter,
arsenic-bearing crust (the species we infer on {ref}`NSDI <step-086>`)
— goes into the RTA with the wafer.

:::{figure} /_static/figures/sd-087-nsdis.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step resist covers the oxide-filled trench and a wide stack on it, and deep doped regions lie in both active areas. After it the resist is gone and a thin oxide covers everything.
:width: 560px
:name: fig-sd-087-nsdis

Before, the NSDM resist after the N⁺ implant; after, the resist stripped and the wafer given the clean before the source/drain anneal. On this reference's reading the surface under the resist is the spacer oxide throughout, which stays as the cap for the anneal (no HF step, as the page infers), so it is drawn unchanged; how much of it survives the two strips is not public. The resist's implanted crust is not drawn. The colours mark the type of the doping, not a depth profile. The spacers, the caps, the gate oxides, the re-oxidation oxide, the tips and the halo, and the field oxide (the oxide-filled trench in the middle) are drawn but not labelled, and the liner oxide is drawn faded; the P-well and the NCHI channel implant made earlier are not drawn. The spacer oxide is not labelled in the lower panel. In the upper panel the p-type resistor body under the resist is not labelled. Not to scale.
:::

The resist it removes has taken an arsenic dose of the order of
10¹⁵ cm⁻² (industry-typical for a source/drain[^txt-01]). Arsenic is
the heaviest ion the resists of this flow meet, so we infer that at a
given dose it leaves the hardest crust of any implant strip in the
process. Fujimura et al. traced the lower etching rate of high-dose
ion-implanted resist to "carbonization of polymers of the resist"; the
abstract does not compare implanted species.[^fujimura-1989] The
surface under the
resist is, on our reading of the flow, the {ref}`SPOX <step-080>`
oxide throughout — over the source/drain silicon, the spacers and
caps, the field, and the poly opened at {ref}`NPCME <step-079>` —
thinned slightly by the {ref}`PDIS <step-084>` clean but still
needed to cap the anneal.

## Step category

`NSDIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-high-dose-implant* type, the twin of {ref}`PDIS <step-084>`. The
category page explains the crust and the popping it causes when the
wafer is heated quickly ("build[s] up pressure beneath the
implant-hardened surface layer"[^pat-strip-mosel]); at an arsenic dose
of 10¹⁵ cm⁻² the crust is at its worst. What distinguishes this strip
from `PDIS` is what follows it: not another resist coat but a
1000 °C-class anneal (industry-typical; see {ref}`RTAD <step-088>`),
so the wet clean must leave the surface as free of metals as a
pre-gate-oxidation clean would, and must do so without removing the
oxide the anneal needs.

## Why this step exists

Two things must be true before {ref}`RTAD <step-088>`. The resist must
be entirely gone — organic residue carbonises in the anneal and
becomes an un-removable defect, and a popped flake of crust on a
source/drain region masks nothing at this point but becomes a particle
under the sacrificial PSG ({ref}`PSG <step-089>`) and the polish that
follows. And the wafer must be clean of metals: the implanter's
beam-line and disc sputter metal onto the resist and the exposed
oxide, and at a typical 1000 °C those metals diffuse into the silicon
and the junctions that have just been made. Fujimura et al. showed how
sodium contamination is kept out of downstream ashing,[^fujimura-1994]
and Kern's review explains why an SC-1/SC-2-type clean follows the
strip.[^kern-1990]

The arsenic itself is a consideration. The crust contains implanted
arsenic, the ash effluent and the wet-bench waste therefore carry it,
and a fab's exhaust scrubbing and waste handling are designed for it
(industry practice); this is a matter of facility design rather than
of the recipe, but it is why arsenic-implanted resist is often
stripped on dedicated tools or in dedicated chambers (industry
practice).

A poorly stripped implant resist shows up as popped flakes — "the
popping problem … causes the photoresist to become even
harder"[^pat-strip-mosel] — and, after the anneal, as junction
leakage where metal residue shadowed the clean. Without `NSDIS` the
resist would go into the RTA.

## How it is typically performed

An industry-generic high-dose implant strip and pre-anneal clean for
a 200 mm, 130 nm-era fab (SKY130's recipe is not public):

1. **Plasma ash, two steps.** Downstream microwave or RF oxygen
   plasma; a first step at low temperature — "removed by oxygen and
   nitrogen/hydrogen plasma in a low-temperature (<220° C.)
   environment"[^pat-strip-mosel] — takes the crust off without
   popping, then a hotter step removes the bulk. Nitrogen raises
   the ash rate,[^fujimura-1990] and forming gas or water vapour
   penetrates the crust;[^fujimura-1994] Chan, Chiu and Tao describe
   an ashing sequence designed around the "carbonized
   crust".[^pat-strip-tsmc] The downstream configuration keeps ions
   off the wafer: "monatomic oxygen is electrically neutral" and the
   remote plasma "prevents damage to the wafer surface".[^wiki-ash]
   SkyWater's three ashers — "Gasonic PEP, remote microwave plasma,
   N2, O2, 120C – 270C", "Iridia RF microwave, N2, O2, H2, CF4, NH3,
   H2/N2, 40C-270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2,
   up to 250C"[^skw-01] — cover the gases and temperatures such a
   recipe needs; the CF₄ options would, we infer, be left out to
   spare the oxide.
2. **Wet strip and clean.** SPM (H₂SO₄:H₂O₂, typically "3 parts of
   concentrated sulfuric acid and 1 part of 30 wt. % hydrogen
   peroxide solution"[^wiki-piranha]) to remove the last organics
   and ash residue; SC-1 for particles; and, we infer, SC-2 for
   metals, since the anneal follows — "6 parts of deionized water,
   1 part of aqueous HCl … 1 part of aqueous H2O2 … at 75 or
   80 °C".[^wiki-rca] Visintin, Korzenski and Baum describe liquid
   formulations developed for high-dose implanted resist,[^visintin-2006]
   and Ohmi's room-temperature sequence is the alternative.[^ohmi-1996]
   SkyWater's Akrion Gamma bench lists "Sulfuric, SC1" and its DNS
   bench and FSI Mercury "industry standard HF/SC1/SC2".[^skw-01] We
   infer no HF step: the {ref}`SPOX <step-080>` oxide is the anneal
   cap and, on our reading, part of the pre-LI dielectric stack.
3. **Rinse and dry.** Cascade DI-water rinse and spin-rinse or IPA
   dry; the wafer goes to the RTA with a hydrophilic, chemically
   oxidised surface.
4. **Inspection.** Patterned-wafer inspection for flakes and
   residue; this is the last chance to catch a strip problem before
   it is annealed in.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm single-wafer: GaSonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES,
  PSK;[^pat-asher-axcelis][^pat-asher-fusion] Stanford's user guide
  describes the downstream class.[^snf-strip]
* **{ref}`Batch wet bench <machine-wet-bench>`** (Akrion, DNS/SCREEN, SCP) or
  **{ref}`spray processor <machine-wet-bench>`** (FSI Mercury) with SPM, SC-1 and SC-2.
* **{ref}`Patterned-wafer inspection <machine-defect-inspection>`** (KLA-Tencor AIT class).

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia RF microwave and Mattson Aspen II ashers**
  — named on SkyWater's facilities page with their gases and
  temperatures.[^skw-01] Strength: **strong** for existence;
  assignment of this strip to any one is an inference, the Iridia's
  40 °C floor and hydrogen chemistries fitting a crust step best.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric,
  BOE"),[^skw-01] **DNS wet bench and FSI Mercury** ("industry
  standard HF/SC1/SC2").[^skw-01] Strength: strong for existence; the
  DNS and FSI Mercury benches, the only ones listed with SC-2, are the
  natural pre-anneal clean stations (inference), as at
  {ref}`PWDEIS <step-033>` and {ref}`LDASTIS <step-074>`.
* **KLA-Tencor AIT** inspection, our reading of "AIT"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {ref}`forming gas <material-anneal-ambients>` (H₂/N₂)**, possibly **{ref}`NH₃ <material-precursors>`** (listed
  for the Iridia) or **water vapour** (not among SkyWater's listed asher
  gases), for the two-step ash;[^skw-01][^fujimura-1994] **{ref}`CF₄ <material-etch-gases>`**, listed
  on the Iridia and Mattson ashers,[^skw-01] attacks the oxide and would,
  we infer, be omitted here; {ref}`arsenic-tolerant exhaust scrubbing <material-hardware-consumables>`.
* **Sulphuric acid and hydrogen peroxide** ({ref}`wet chemicals <material-wet-chemicals>`) for SPM; **ammonium
  hydroxide** for SC-1; **hydrochloric acid** for SC-2.[^wiki-rca]
* **{ref}`Ultrapure DI water <material-ultrapure-water>`**, **isopropanol**, **nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`NSDI <step-086>` (the implant); mask:
  {ref}`NSDM <step-085>`.
* Next: {ref}`RTAD <step-088>` (the anneal this clean prepares).
* Companion strip: {ref}`PDIS <step-084>`; the other high-dose
  strip: {ref}`P1IS <step-051>`; the earlier pre-anneal strip of the
  well module: {ref}`PWDEIS <step-033>` before {ref}`RTAI <step-034>`.
* The oxide the strip must preserve: {ref}`SPOX <step-080>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Plasma asher with microwave trap <patent-gp22748832>` — US 5,498,308 A (1994)
* {ref}`Cold processes for cleaning and stripping photoresist from surfaces of semiconductor wafers <patent-gp26794054>` — US 5,795,831 A (1996)
* {ref}`Low temperature dry process for stripping photoresist after high dose ion implantation <patent-gp25102092>` — US 5,811,358 A (1997)
* {ref}`Method of ashing a photoresist <patent-gp33298522>` — US 2004/0214448 A1 (2003)
* {ref}`Apparatus and plasma ashing process for increasing photoresist removal rate <patent-gp35448183>` — US 7,449,416 B2 (2004)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — GaSonics PEP, Iridia and
  Mattson Aspen II with gases and temperatures; Akrion Gamma; DNS and
  FSI benches.[^skw-01]
* [LinkedIn, SkyWater listings](<https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>) — the defect-metrology tool list
  "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* [Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358](<https://patents.google.com/patent/US5811358A/en>) — popping and
  the low-temperature first ash.[^pat-strip-mosel]
* [Chan, Chiu and Tao (TSMC), US 2004/0214448](<https://patents.google.com/patent/US20040214448A1/en>) — the carbonised
  crust.[^pat-strip-tsmc]

### High-level understanding

* [Wikipedia, *Plasma ashing*](<https://en.wikipedia.org/wiki/Plasma_ashing>) — downstream ashing and implanted
  resist.[^wiki-ash]
* Wikipedia, [*RCA clean*](<https://en.wikipedia.org/wiki/RCA_clean>) and [*Piranha solution*](<https://en.wikipedia.org/wiki/Piranha_solution>).[^wiki-rca][^wiki-piranha]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) —
  implanted-resist stripping.[^txt-05]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — source/drain
  doses and pre-anneal cleaning.[^txt-01]
* [Stanford Nanofabrication Facility, *Downstream/Remote Plasma Resist
  Removal*](<https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal>) — the tool class in a user guide.[^snf-strip]

### Deep dive

* [Fujimura et al. (Fujitsu), *JJAP* 1989](<https://doi.org/10.1143/JJAP.28.2130>) — the carbonised layer of
  high-dose implanted resist and a two-step ashing process
  (abstract).[^fujimura-1989]
* [Fujimura et al. (Fujitsu), *JJAP* 1990](<https://doi.org/10.1143/JJAP.29.2165>) — nitrogen in downstream
  ashing.[^fujimura-1990]
* [Fujimura et al. (Fujitsu), *JVST B* 1994](<https://doi.org/10.1116/1.587773>) — O₂+H₂O ashing without
  sodium contamination.[^fujimura-1994]
* [Roche, Michaud and Bruel, *MRS Proc.* 1985](<https://doi.org/10.1557/PROC-45-203>) — resist outgassing
  during implantation.[^roche-1985]
* [Horsky, IIT 1998](<https://doi.org/10.1109/IIT.1999.812201>) — outgassing in high-current implanters.[^horsky-1998]
* [Lukaszek, Reno and Bammi, IIT 1996](<https://doi.org/10.1109/IIT.1996.586135>) — what a high-current arsenic
  implant does to a resist-covered wafer.[^lukaszek-1996]
* [Visintin, Korzenski and Baum, *J. Electrochem. Soc.* 2006](<https://doi.org/10.1149/1.2195884>) — liquid
  formulations for high-dose implanted resist.[^visintin-2006]
* [Kern, *J. Electrochem. Soc.* 1990](<https://doi.org/10.1149/1.2086825>) — the RCA clean.[^kern-1990]
* [Kern, *Handbook of Silicon Wafer Cleaning Technology*](<https://doi.org/10.1016/b978-081551554-8.50004-5>) — the
  handbook overview of cleaning, including pre-anneal
  cleans.[^kern-handbook]
* [Ohmi, *J. Electrochem. Soc.* 1996](<https://doi.org/10.1149/1.1837133>) — room-temperature wet
  cleaning.[^ohmi-1996]
* [Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing*](<https://doi.org/10.1002/9781118071748>) — post-implant stripping.[^reinhardt-2010]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358; Chan, Chiu and
  Tao (TSMC), US 2004/0214448; Nakayama et al. (ULVAC), US 5,795,831
  — three approaches to stripping implanted
  resist.[^pat-strip-mosel][^pat-strip-tsmc][^pat-strip-ulvac]
* Becknell, Hammar and Ferris (Axcelis), US 7,449,416, and Kamarehi
  and Simpson (Fusion Systems), US 5,498,308 — asher
  designs.[^pat-asher-axcelis][^pat-asher-fusion]

## Open questions

* The SKY130 ash recipe and wet sequence, and whether the clean
  includes SC-2 or an HF step before the anneal, are not public.
* How much {ref}`SPOX <step-080>` oxide survives the two strips and
  enters the anneal is not public.
* Which asher and bench run this strip is inferred from the
  published gas and temperature ranges.[^skw-01]

<!-- footnotes -->

[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
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
[^snf-strip]: Stanford Nanofabrication Facility, *Downstream/Remote
    Plasma Resist Removal*, equipment guide.
    <https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal>
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
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic
    implant", *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 89–92.
    <https://doi.org/10.1109/IIT.1996.586135>
[^visintin-2006]: P. M. Visintin, M. B. Korzenski and T. H. Baum,
    "Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
    Photoresist from Microelectronic Devices", *Journal of The
    Electrochemical Society* **153**(7), G591 (2006).
    <https://doi.org/10.1149/1.2195884>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
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
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
