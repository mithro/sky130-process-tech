(step-067)=
# Step 067 — ASTIS: As tip implant strip

| | |
|---|---|
| **Step number** | 67 of 171[^steps-sheet] |
| **Step code** | `ASTIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`BHI <step-066>` |
| **Next step** | {ref}`HVNTM <step-068>` |

## What this step is

`ASTIS` removes the photoresist patterned at {ref}`NTM <step-064>`
after it has masked two implants — the arsenic tip
{ref}`ASTI <step-065>` and the boron {term}`halo` {ref}`BHI <step-066>` — and
cleans the wafer so that the next tip mask, {ref}`HVNTM <step-068>`, can
be coated on a bare, particle-free surface. It is the first
stand-alone resist strip after the gate etch — the gate-etch resist is
stripped inside {ref}`P1ME <step-062>` — and the first of the three
strips in the tip module; in this reference each tip mask is followed
by such a strip ({ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`).

The resist being removed is the roughly 1 µm i-line implant resist
inferred on the {ref}`NTM <step-064>` page (the PDK's nominal
photoresist thickness is 1.14 µm).[^pdk-03] It has received a heavy
arsenic dose — of order 10¹⁴–10¹⁵ cm⁻² (typical of an {term}`extension`
implant)[^txt-01] — and a light, tilted boron dose. That makes it a
*hard* strip by the standards of the flow: the arsenic has turned the
top of the resist into a carbonised {term}`crust <implant crust>`,[^orvek-1985]
the kind of carbonised layer high-dose implantation forms,[^fujimura-1989]
and the crust contains arsenic. The surface under the resist is, we
infer, the thin {term}`screen oxide` from {ref}`IOX45 <step-063>` over silicon
and over the capped polysilicon gates; no metal is present, so the full
acid–peroxide sequence is available, but the screen oxide must survive
because two more tip implants will be made through it.

## Step category

`ASTIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type, at the difficult end of that class. The category
page explains that implanted resist is "a different material from
freshly developed resist": Fujimura et al. traced the lower etching
rate of high-dose ion-implanted resist to "carbonization of polymers of
the resist",[^fujimura-1989] and, on the category page's account, if
the crusted wafer is heated quickly the soft resist underneath blows
the crust off in flakes ("popping"). The channel-implant strips of the
well module ({ref}`LVTNIS <step-016>`) saw doses a hundred times
smaller; only the source/drain strips ({ref}`PDIS <step-084>`,
{ref}`NSDIS <step-087>`) are harder than this one.

## Why this step exists

Resist must be gone before the next coat, and residue matters more here
than after most masks. The {ref}`HVNTM <step-068>` resist that follows
is, per the PDK's assumptions page, only 0.3 µm thick ("Photoresist
thickness for HV Tip Implants")[^pdk-03] — a film that a flake of popped
crust or a ridge of residue would easily disturb, and whose 40° tilted
implant[^pdk-03] would be {term}`shadowed <shadowing>` by any particle standing on the
surface. The crust also carries the implanted arsenic and whatever
metals the beam line has sputtered onto it; both must leave the wafer
before the {ref}`TIPRTAD <step-075>` anneal can drive them in. A
poorly stripped implant resist shows up as hard-to-remove flakes — one
patent has the implant-hardened surface "first stripped by oxygen and
nitrogen/hydrogen plasma at a lower temperature (<220° C.) to prevent
popping problem"[^pat-strip-mosel] — and, after this particular strip,
as tip and halo doping missing from whichever transistors the flakes
landed on.

## How it is typically performed

An industry-generic high-dose implant-strip sequence for a 200 mm,
130 nm-era fab:

1. **Plasma {term}`ash`, two stages.** Downstream (remote) microwave or RF
   oxygen plasma. Because "the top portion of the photoresist layer is
   transformed into a carbonized crust that is difficult to
   remove"[^pat-strip-tsmc] and a conventional "high temperature
   (>200° C.) dry ashing" lets the volatile bulk "build up pressure
   beneath the implant-hardened surface layer",[^pat-strip-mosel] the
   first stage runs cool — "removed by oxygen and nitrogen/hydrogen
   plasma in a low-temperature (<220° C.) environment"[^pat-strip-mosel]
   — until the crust is opened, after which a hotter bulk stage
   finishes the film. Fujimura's group showed why nitrogen[^fujimura-1990]
   and water vapour[^fujimura-1991] are added to the oxygen for
   implanted resist, and Yegnasubramanian et al. showed by TEM what is
   left when the ash is not adequate.[^yegnasubramanian-1992]
   SkyWater's ashers offer exactly these chemistries: "Gasonic PEP,
   remote microwave plasma, N2, O2, 120C – 270C", "Iridia RF microwave,
   N2, O2, H2, CF4, NH3, H2/N2, 40C-270C" and "Mattson Aspen2, RF
   plasma, O2, CF4, H2>N2, up to 250C".[^skw-01] Downstream operation
   is used because "monatomic oxygen is electrically neutral" and the
   remote plasma "prevents damage to the wafer surface"[^wiki-ash] —
   which matters with gate oxide and gate edges now exposed.
2. **Wet strip and clean.** Sulphuric acid–hydrogen peroxide ({term}`SPM`,
   "piranha"), "a typical mixture is 3 parts of concentrated sulfuric
   acid and 1 part of 30 wt. % hydrogen peroxide solution",[^wiki-piranha]
   dissolves the remaining organics and the arsenic-bearing residue;
   {term}`SC-1` (NH₄OH/H₂O₂/H₂O at 75–80 °C) then removes particles, with an
   optional {term}`SC-2` (HCl/H₂O₂/H₂O) for metals.[^wiki-rca] SkyWater's Akrion
   Gamma bench lists "Sulfuric, SC1" among its chemistries.[^skw-01]
   Sulphur-trioxide[^bergman-2009] and formulated
   solvent-based[^visintin-2006] strippers are the published
   alternatives for high-dose implanted resist.
3. **Rinse and dry.** Cascade DI-water rinse, spin-rinse or IPA dry.
4. **Inspection.** Patterned-wafer optical inspection for flakes and
   residue.

We infer that no HF step is used: the screen oxide must remain as the
screen for {ref}`HVASTI <step-069>` and {ref}`LDASTI <step-072>`, and
SC-1's slow oxide etch is the only thinning budgeted (industry
practice).[^txt-02]

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm single-wafer: GaSonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES series, PSK
  ({ref}`category-strip`).
* **{ref}`Batch wet bench <machine-wet-bench>`** with SPM, SC-1, SC-2 tanks and a rinser/dryer
  (Akrion, DNS/SCREEN, SCP), or a **{ref}`spray processor <machine-wet-bench>`** (FSI Mercury).
* **{ref}`Patterned-wafer inspection <machine-defect-inspection>`** (KLA-Tencor 2xxx/AIT class).

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia RF microwave and Mattson Aspen II ashers** —
  all named on SkyWater's facilities page with their gases and
  temperatures.[^skw-01] Strength: **strong** for existence; the
  assignment of this strip to any one of them is an inference. The
  Iridia's H₂/N₂ chemistry and 40 °C lower limit fit a cool first
  stage best.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric,
  BOE")[^skw-01] for the SPM/SC-1 sequence. Strength: strong for
  existence.
* **DNS wet bench and FSI Mercury** ("industry standard
  HF/SC1/SC2")[^skw-01] as alternative clean tools. Strength: strong for
  existence.
* **KLA-Tencor AIT** patterned-wafer inspection, our reading of "AIT"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {term}`forming gas` ({ref}`H₂/N₂ <material-anneal-ambients>`)** for the
  ash;[^skw-01] **{ref}`CF₄ <material-etch-gases>`**, listed on the Iridia and Mattson
  ashers,[^skw-01] attacks the screen oxide and would, we infer, be
  omitted here (category page).
* **Sulphuric acid and hydrogen peroxide** (semiconductor-grade
  concentrated acid and 30 % peroxide, the usual SPM
  reagents[^wiki-piranha]) ({ref}`wet chemicals <material-wet-chemicals>`);
  **ammonium hydroxide** for SC-1; **hydrochloric
  acid** for SC-2.[^wiki-rca]
* **{ref}`Ultrapure DI water <material-ultrapure-water>`**, **isopropanol** for drying, **nitrogen**.
* Arsenic-bearing resist ash and spent acid go to the fab's
  {ref}`hazardous exhaust and waste-acid systems <material-hardware-consumables>` (general practice).
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`BHI <step-066>` (the last implant through this
  resist); the resist was patterned at {ref}`NTM <step-064>` and also
  masked {ref}`ASTI <step-065>`.
* Next: {ref}`HVNTM <step-068>` (the thin HV-tip resist coated on the
  cleaned surface).
* Companion strips in this module: {ref}`HVASTIS <step-070>`,
  {ref}`LDASTIS <step-074>`; the next high-dose strips are
  {ref}`PDIS <step-084>` and {ref}`NSDIS <step-087>`.
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

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — GaSonics PEP; Iridia; Mattson
  Aspen II; Akrion Gamma; DNS and FSI Mercury benches.[^skw-01]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — photoresist thickness
  1.14 µm; 0.3 µm resist and 40° angle for the HV tip that
  follows.[^pdk-03]
* [LinkedIn, SkyWater Technology Foundry listings](<https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>) — the defect-metrology
  tool list.[^job-06]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* [Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358](<https://patents.google.com/patent/US5811358A/en>) — the {term}`popping`
  mechanism and a low-temperature first ash stage.[^pat-strip-mosel]
* [Chan, Chiu and Tao (TSMC), US 2004/0214448](<https://patents.google.com/patent/US20040214448A1/en>) — the "carbonized crust" of
  implanted resist.[^pat-strip-tsmc]

### High-level understanding

* [Wikipedia, *Plasma ashing*](<https://en.wikipedia.org/wiki/Plasma_ashing>) — downstream ashing and implanted-resist
  problems.[^wiki-ash]
* Wikipedia, [*Piranha solution*](<https://en.wikipedia.org/wiki/Piranha_solution>) and [*RCA clean*](<https://en.wikipedia.org/wiki/RCA_clean>) — SPM, SC-1 and SC-2
  compositions.[^wiki-piranha][^wiki-rca]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  resist stripping and wafer cleaning.[^txt-02]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — extension
  implant doses that set the crust.[^txt-01]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) — ash and
  wet-clean tools.[^txt-07]

### Deep dive

* [Orvek and Huffman, *NIM B* 1985](<https://doi.org/10.1016/0168-583X(85)90421-5>) — the carbonised layer formed in
  ion-implanted resist masks.[^orvek-1985]
* [Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1989](<https://doi.org/10.1143/JJAP.28.2130>) — the
  carbonised layer of high-dose implanted resist and a two-step ashing
  process (abstract).[^fujimura-1989]
* [Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1990](<https://doi.org/10.1143/JJAP.29.2165>) — why nitrogen
  is added to oxygen in downstream ashing.[^fujimura-1990]
* [Fujimura et al. (Fujitsu), *J. Vac. Sci. Technol. B* 1991](<https://doi.org/10.1116/1.585575>) — resist
  stripping in an O₂ + H₂O downstream plasma.[^fujimura-1991]
* [Yegnasubramanian, Draper and Pearce, *MRS Proc.* 1992](<https://doi.org/10.1557/PROC-265-295>) — TEM of the
  implanted-resist residues left after oxygen-plasma ashing.[^yegnasubramanian-1992]
* [Rubin et al. (Varian), IIT 2000](<https://doi.org/10.1109/IIT.2000.924279>) — UV photostabilisation of resist
  before high-dose implants, the implant-side half of the
  problem.[^rubin-2000]
* [Lukaszek, Reno and Bammi, IIT 1996](<https://doi.org/10.1109/IIT.1996.586135>) — resist and wafer charging
  during high-current arsenic implants.[^lukaszek-1996]
* [Bergman and Leonhard, *Solid State Phenomena* 2009](<https://doi.org/10.4028/www.scientific.net/SSP.145-146.281>) — wet stripping
  of high-dose implanted resist with sulphur trioxide.[^bergman-2009]
* [Visintin, Korzenski and Baum, *J. Electrochem. Soc.* 2006](<https://doi.org/10.1149/1.2195884>) —
  formulated liquid strippers for high-dose implanted resist.[^visintin-2006]
* [Kern, *J. Electrochem. Soc.* 1990](<https://doi.org/10.1149/1.2086825>) — history and chemistry of the RCA
  clean.[^kern-1990]
* [Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing*](<https://doi.org/10.1002/9781118071748>) — post-implant stripping and wet cleaning.[^reinhardt-2010]
* [Nakayama et al. (ULVAC), US 5,795,831](<https://patents.google.com/patent/US5795831A/en>) — a cold process for stripping
  implanted resist.[^pat-strip-ulvac]
* [Kamarehi and Simpson (Fusion Systems), US 5,498,308](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>) — a downstream
  microwave asher design.[^pat-asher-fusion]
* [Becknell, Hammar and Ferris (Axcelis), US 7,449,416](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>) — a plasma
  ashing process tuned for removal rate.[^pat-asher-axcelis]

## Open questions

* The SKY130 ash recipe (stage temperatures, gases, whether H₂O or
  H₂/N₂ is used) and the wet sequence are not public.
* Whether an oxide-thinning budget is assigned to this clean, and how
  the screen oxide thickness is tracked across the three tip strips, is
  not public.
* Which of the three ashers on SkyWater's public tool list[^skw-01]
  runs the high-dose strips is not stated publicly.
* The tip dose that determines how hard this strip is remains an
  inference from node-typical values ({ref}`ASTI <step-065>`).

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^orvek-1985]: K. J. Orvek and C. Huffman, "Carbonized layer formation
    in ion implanted photoresist masks", *Nuclear Instruments and
    Methods in Physics Research B* **7–8**, 501–506 (1985).
    <https://doi.org/10.1016/0168-583X(85)90421-5>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^fujimura-1990]: S. Fujimura, K. Shinagawa, M. Nakamura and H. Yano,
    "Additive Nitrogen Effects on Oxygen Plasma Downstream Ashing",
    *Japanese Journal of Applied Physics* **29**(10R), 2165 (1990).
    <https://doi.org/10.1143/JJAP.29.2165>
[^fujimura-1991]: S. Fujimura, K. Shinagawa, M. T. Suzuki and
    M. Nakamura, "Resist stripping in an O₂+H₂O plasma downstream",
    *Journal of Vacuum Science & Technology B* **9**(2), 357–361 (1991).
    <https://doi.org/10.1116/1.585575>
[^yegnasubramanian-1992]: S. Yegnasubramanian, C. W. Draper and C. W.
    Pearce, "Tem Investigation of Implanted Photoresist Residues
    Remaining After Oxygen Plasma Ashing", *MRS Online Proceedings
    Library* **265**, 295–300 (1992).
    <https://doi.org/10.1557/PROC-265-295>
[^rubin-2000]: L. Rubin, D. Whiteside, C. Norton, A. Stevenson and
    C. Ukah, "Improved photoresist integrity by UV photostabilization
    for high dose, high energy ion implants", *Proc. 2000 International
    Conference on Ion Implantation Technology*, pp. 817–820.
    <https://doi.org/10.1109/IIT.2000.924279>
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic implant",
    *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 89–92.
    <https://doi.org/10.1109/IIT.1996.586135>
[^bergman-2009]: E. J. Bergman and J. D. Leonhard, "Novel Methods for
    Wet Stripping High Dose Implanted Photoresist Using Sulfur
    Trioxide", *Solid State Phenomena* **145–146**, 281–284 (2009).
    <https://doi.org/10.4028/www.scientific.net/SSP.145-146.281>
[^visintin-2006]: P. M. Visintin, M. B. Korzenski and T. H. Baum,
    "Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
    Photoresist from Microelectronic Devices", *Journal of The
    Electrochemical Society* **153**(7), G591 (2006).
    <https://doi.org/10.1149/1.2195884>
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
[^pat-asher-fusion]: M. Kamarehi and J. E. Simpson (Fusion Systems),
    *Plasma asher with microwave trap*, US 5,498,308 A, granted
    1996-03-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
[^pat-asher-axcelis]: A. F. Becknell, P. Hammar and D. Ferris (Axcelis
    Technologies), *Apparatus and plasma ashing process for increasing
    photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
