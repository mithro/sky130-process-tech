(step-074)=
# Step 074 — LDASTIS: LD ASTI implant strip

| | |
|---|---|
| **Step number** | 74 of 171[^steps-sheet] |
| **Step code** | `LDASTIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`LDBHI <step-073>` |
| **Next step** | {ref}`TIPRTAD <step-075>` |

## What this step is

`LDASTIS` removes the resist patterned at {ref}`LDNTM <step-071>` after
it has masked the lightly doped arsenic tip {ref}`LDASTI <step-072>`
and the boron {term}`halo` {ref}`LDBHI <step-073>` of the {term}`SONOS` memory
transistors, and cleans the wafer. It is the last strip of the tip
module and — because the next step is the activation anneal
{ref}`TIPRTAD <step-075>` — it is also the *pre-anneal clean* for every
tip and halo implanted since {ref}`NTM <step-064>`.

The resist is, we infer, the standard ~1 µm film (the PDK's nominal
1.14 µm),[^pdk-03] and it has received a moderate arsenic dose (of order 10¹³
cm⁻², typical of an {term}`LDD`)[^txt-04] plus a light, tilted boron dose: a
thinner {term}`crust <implant crust>` than after {ref}`ASTI <step-065>`, but a
crust nonetheless. Under it lies, we infer, the {term}`screen oxide` of
{ref}`IOX45 <step-063>` over silicon and polysilicon, now carrying, in
different regions, all three tips and both halos in their as-implanted,
unannealed state.

## Step category

`LDASTIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type, of medium difficulty, followed by the most
thorough clean of the module. The category page explains that
post-implant strips are "longer and more carefully engineered than
etch strips" because of the implanted crust; here the extra care goes
into the wet clean, since whatever is left on the surface will be
driven into the silicon by the anneal that follows.

## Why this step exists

Two reasons, one ordinary and one specific to its position.

The ordinary one: the resist must be gone, and its arsenic-bearing
crust with it, before the wafer is heated. Resist that survives an {term}`ash`
carbonises further in the anneal and becomes almost impossible to
remove; flakes of popped crust {term}`shadow <shadowing>` the {term}`spacer` deposition that
follows the anneal ({ref}`SPNIT <step-076>`).

The specific one: {ref}`TIPRTAD <step-075>` heats the wafer to
1000 °C-class temperatures for seconds (typical of a tip
anneal),[^stolk-1997][^agarwal-1999] and any metallic contamination on
the surface — from the implanter beam lines, the ashers, or handling —
diffuses into the junction regions at such temperatures and raises
junction leakage. The pre-anneal clean therefore includes a metal-
removing step: {term}`SC-2` (HCl/H₂O₂/H₂O) after {term}`SC-1` in the RCA
sequence,[^wiki-rca][^kern-1990] or an HCl- or HF-based
alternative.[^ohmi-1996] ITRS 2001's surface-preparation section sets
the metallic-contamination targets a front-end clean must
meet.[^itrs-01] The same role was played by {ref}`PWDEIS <step-033>`
before {ref}`RTAI <step-034>`.

## How it is typically performed

An industry-generic post-implant strip and pre-anneal clean for a
200 mm, 130 nm-era fab:

1. **Plasma ash.** Downstream microwave or RF oxygen plasma with
   nitrogen[^fujimura-1990] or water vapour[^fujimura-1994] additions;
   a cooler first stage — "low-temperature (<220 °C)"[^pat-strip-mosel]
   — to open the crust without {term}`popping`,[^pat-strip-mosel] then a hot
   stage to clear the bulk, with optical-emission {term}`endpoint` and a timed
   over-ash. SkyWater's ashers offer these chemistries: "Gasonic PEP,
   remote microwave plasma, N2, O2, 120C – 270C", "Iridia RF
   microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C" and "Mattson
   Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C".[^skw-01] Downstream
   operation avoids charging the exposed gates.[^wiki-ash]
2. **Wet strip.** {term}`SPM` ("3 parts of concentrated sulfuric acid and 1
   part of 30 wt. % hydrogen peroxide solution" is
   typical)[^wiki-piranha] for the last organics and the arsenic-
   bearing residue; SkyWater's Akrion Gamma bench lists "Sulfuric,
   SC1".[^skw-01]
3. **Pre-anneal clean.** SC-1 (NH₄OH/H₂O₂/H₂O at 75–80 °C) for
   particles, then SC-2 (HCl/H₂O₂/H₂O) for metals,[^wiki-rca] the
   sequence Kern traced from its RCA origins;[^kern-1990] SkyWater's
   DNS bench and FSI Mercury offer "industry standard
   HF/SC1/SC2".[^skw-01] We infer that no HF step is used, or only a
   very dilute one: the screen oxide should remain as a cap during the
   anneal, where it limits dopant out-diffusion and keeps the silicon
   surface from roughening (see {ref}`TIPRTAD <step-075>`).
4. **Rinse and dry.** Cascade DI-water rinse; spin-rinse or IPA dry,
   with a short queue time to the anneal to limit re-contamination and
   native-oxide growth (industry practice).[^txt-02]
5. **Inspection.** Patterned-wafer inspection for residue and flakes.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm single-wafer: GaSonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES series, PSK
  ({ref}`category-strip`).
* **{ref}`Batch wet bench <machine-wet-bench>`** with SPM, SC-1 and SC-2 tanks and a
  rinser/dryer (Akrion, DNS/SCREEN, SCP), or a **{ref}`spray processor <machine-wet-bench>`**
  (FSI Mercury).
* **{ref}`Patterned-wafer inspection <machine-defect-inspection>`** (KLA-Tencor 2xxx/AIT class).

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia RF microwave and Mattson Aspen II ashers** —
  named on SkyWater's facilities page with their gases and
  temperatures.[^skw-01] Strength: **strong** for existence; the
  assignment of this strip to any one of them is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric,
  BOE").[^skw-01] Strength: strong for existence.
* **DNS wet bench and FSI Mercury** ("industry standard
  HF/SC1/SC2")[^skw-01] — the tools with the SC-2 chemistry the
  pre-anneal clean needs. Strength: strong for existence; the
  assignment is an inference from the chemistry list.
* **KLA-Tencor AIT** patterned-wafer inspection, our reading of "AIT"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-01]
  Strength: medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {term}`forming gas` ({ref}`H₂/N₂ <material-anneal-ambients>`)** for the
  ash;[^skw-01] **{ref}`CF₄ <material-etch-gases>`**, listed on the Iridia and Mattson
  ashers,[^skw-01] attacks the screen oxide and would, we infer, be
  omitted here (category page).
* **Sulphuric acid and hydrogen peroxide** ({ref}`wet chemicals <material-wet-chemicals>`) for SPM;[^wiki-piranha]
  **ammonium hydroxide** for SC-1; **hydrochloric acid** for
  SC-2.[^wiki-rca]
* **{ref}`Ultrapure DI water <material-ultrapure-water>`**, **isopropanol**, **nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LDBHI <step-073>` (the last implant through this
  resist); mask: {ref}`LDNTM <step-071>`; the other implant through
  it: {ref}`LDASTI <step-072>`.
* Next: {ref}`TIPRTAD <step-075>` (the anneal this clean prepares
  for), then the spacer {ref}`SPNIT <step-076>`.
* Companion strips: {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`;
  the earlier pre-anneal clean: {ref}`PWDEIS <step-033>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — GaSonics PEP; Iridia; Mattson
  Aspen II; Akrion Gamma; DNS and FSI Mercury benches with
  "HF/SC1/SC2".[^skw-01]
* SkyWater PDK, *Criteria & Assumptions* — photoresist thickness
  1.14 µm.[^pdk-03]
* Indeed, SkyWater Technology Foundry listings — defect-metrology
  tools.[^job-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the two-stage
  low-temperature ash.[^pat-strip-mosel]

### High-level understanding

* Wikipedia, *Plasma ashing* — downstream ashing.[^wiki-ash]
* Wikipedia, *Piranha solution* and *RCA clean* — SPM, SC-1 and
  SC-2.[^wiki-piranha][^wiki-rca]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  resist stripping, wafer cleaning and queue times.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD doses that
  set the crust.[^txt-04]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — ash and
  wet-clean tools.[^txt-07]

### Deep dive

* Kern, *J. Electrochem. Soc.* 1990 — the evolution and chemistry of
  the {term}`RCA clean`, including SC-2's role against metals.[^kern-1990]
* Kern, *Handbook of Silicon Wafer Cleaning Technology* — cleaning
  chemistry and contamination control before thermal steps.[^kern-handbook]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — post-implant strip and pre-anneal cleaning.[^reinhardt-2010]
* Ohmi, *J. Electrochem. Soc.* 1996 — a room-temperature clean that
  replaces the hot RCA sequence.[^ohmi-1996]
* ITRS 2001, *Front End Processes* — surface-preparation
  requirements for metallic and particle contamination.[^itrs-01]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1989 — the carbonised
  layer of high-dose implanted resist, the residues of O₂ ashing and a
  two-step ashing process (abstract).[^fujimura-1989]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1990 — nitrogen in
  downstream ashing.[^fujimura-1990]
* Fujimura et al. (Fujitsu), *J. Vac. Sci. Technol. B* 1994 —
  sodium-free ashing with water vapour, a contamination argument
  relevant before an anneal.[^fujimura-1994]
* Orvek and Huffman, *NIM B* 1985 — the carbonised layer in
  implanted resist.[^orvek-1985]
* Stolk et al. (Bell Labs), *J. Appl. Phys.* 1997 — the anneal
  conditions this clean prepares the wafer for.[^stolk-1997]
* Agarwal, Gossmann and Fiory, *J. Electron. Mater.* 1999 — spike
  anneal ramp rates.[^agarwal-1999]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — low-temperature
  dry strip after implantation.[^pat-strip-mosel]
* Nakayama et al. (ULVAC), US 5,795,831 — a cold strip for implanted
  resist.[^pat-strip-ulvac]
* Becknell, Hammar and Ferris (Axcelis), US 7,449,416 — a plasma
  ashing process for higher removal rate.[^pat-asher-axcelis]

## Open questions

* The ash recipe and the exact wet sequence — in particular whether
  SC-2 or an HF-last step precedes the anneal, and whether the screen
  oxide is deliberately kept — are not public.
* Which asher and which wet bench run this strip is not stated
  publicly.
* The queue-time limit between this clean and {ref}`TIPRTAD <step-075>`
  is not public.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page; Defect Technician 2 posting),
    retrieved 2026-08-30; listings expire. <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
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
[^orvek-1985]: K. J. Orvek and C. Huffman, "Carbonized layer formation
    in ion implanted photoresist masks", *Nuclear Instruments and
    Methods in Physics Research B* **7–8**, 501–506 (1985).
    <https://doi.org/10.1016/0168-583X(85)90421-5>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^agarwal-1999]: A. Agarwal, H.-J. Gossmann and A. T. Fiory, "Effect of
    ramp rates during rapid thermal annealing of ion implanted boron for
    formation of ultra-shallow junctions", *Journal of Electronic
    Materials* **28**(12), 1333–1339 (1999).
    <https://doi.org/10.1007/s11664-999-0118-7>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^pat-strip-ulvac]: I. Nakayama et al. (ULVAC Technologies), *Cold
    processes for cleaning and stripping photoresist from surfaces of
    semiconductor wafers*, US 5,795,831 A, granted 1998-08-18.
    <https://patents.google.com/patent/US5795831A/en>
[^pat-asher-axcelis]: A. F. Becknell, P. Hammar and D. Ferris (Axcelis
    Technologies), *Apparatus and plasma ashing process for increasing
    photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
