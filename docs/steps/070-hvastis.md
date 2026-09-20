(step-070)=
# Step 070 — HVASTIS: HV As N-tip implant strip

| | |
|---|---|
| **Step number** | 70 of 171[^steps-sheet] |
| **Step code** | `HVASTIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`HVASTI <step-069>` |
| **Next step** | {ref}`LDNTM <step-071>` |

## What this step is

`HVASTIS` removes the thin resist patterned at {ref}`HVNTM <step-068>`
after it has masked the tilted arsenic implant {ref}`HVASTI <step-069>`,
and cleans the wafer for the third and last tip mask,
{ref}`LDNTM <step-071>`. It is the second of the three strips in the tip
module.

Two things distinguish it from {ref}`ASTIS <step-067>`. The resist is thin —
the PDK's "Photoresist thickness for HV Tip Implants" is 0.3 µm, against
1.14 µm for the standard resist[^pdk-03] — and the implant it has absorbed is,
we infer from the LDD-type dose of the step, one to two orders of magnitude
lighter than the 1.8 V tip (of order 10¹³ cm⁻², typical of an
{term}`LDD`,[^txt-04] against 10¹⁴–10¹⁵ cm⁻²). The
{term}`crust <implant crust>` is correspondingly thinner and the strip easier.
On the other hand the ions arrived at 40°,[^pdk-03] so the resist sidewalls
facing the beam have been implanted along their whole height, and
we read the PDK's 0.02 µm "Photoresist tilted implant
penetration"[^pdk-03] as saying the ions reach 0.02 µm laterally into
the resist edge, so the sidewalls facing the beam are implanted through
their whole height (inference).
The surface under the resist is, we infer, the
{term}`screen oxide` from {ref}`IOX45 <step-063>` over silicon and poly, which
must survive once more for {ref}`LDASTI <step-072>`.

## Step category

`HVASTIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type, of medium difficulty: an implanted crust is
present, so the low-temperature first {term}`ash` stage that guards against
{term}`popping` is still prudent, but the total resist volume is a quarter of
the usual and the dose is moderate. The category page's generic
post-implant sequence — downstream ash, {term}`SPM`, {term}`SC-1` — applies without
special measures.

## Why this step exists

The next mask, {ref}`LDNTM <step-071>`, is coated on this surface, and
the arsenic-bearing resist and its crust must be gone before the wafer
is heated at {ref}`TIPRTAD <step-075>`. A thin implanted resist has its
own failure mode: if the ash is tuned for the thick standard film, the
thin film is over-ashed for most of the cycle, and the exposed screen
oxide, gate oxide edges and poly sidewalls see the plasma for longer
than necessary — one reason downstream (charge-free) ashing is
preferred over direct plasma exposure once gates exist.[^wiki-ash]
Residue matters as it did after `ASTIS`: a flake left here blocks the
{term}`SONOS` tip implant on whichever cell it lands.

## How it is typically performed

An industry-generic post-implant strip for a thin resist after a
moderate-dose tilted implant, 200 mm, 130 nm era:

1. **Plasma ash.** Downstream microwave or RF oxygen plasma, with
   nitrogen[^fujimura-1990] or water vapour[^fujimura-1991] added as
   Fujimura's group established for implanted resist. A short,
   cooler first stage opens the thin crust — the "low-temperature
   (<220° C.)" first step of the two-stage recipe[^pat-strip-mosel] —
   and a hot stage clears the remaining film; {term}`endpoint` by optical
   emission followed by a timed over-ash, kept short because the film
   is thin. Horsky's and Roche's studies of resist outgassing and
   carbonisation during implantation explain what the ash is
   removing.[^horsky-1998][^roche-1985] SkyWater's ashers offer the
   needed chemistries: "Gasonic PEP, remote microwave plasma, N2, O2,
   120C – 270C", "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2,
   40C-270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to
   250C".[^skw-01]
2. **Wet strip and clean.** SPM ("3 parts of concentrated sulfuric
   acid and 1 part of 30 wt. % hydrogen peroxide solution" is
   typical)[^wiki-piranha] for residual organics, then SC-1
   (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles and, optionally,
   {term}`SC-2` for metals;[^wiki-rca] SkyWater's
   Akrion Gamma bench lists "Sulfuric, SC1".[^skw-01] Room-temperature
   alternatives to the hot sequence exist.[^ohmi-1996]
3. **Rinse and dry.** Cascade DI-water rinse and spin or IPA dry.
4. **Inspection.** Patterned-wafer inspection for residue.

No HF step is used (inference): the screen oxide is still needed for
the {ref}`LDASTI <step-072>` and {ref}`LDBHI <step-073>` implants.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm single-wafer: GaSonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES series, PSK
  ({ref}`category-strip`).
* **{ref}`Batch wet bench <machine-wet-bench>`** with SPM and SC-1 tanks and a rinser/dryer
  (Akrion, DNS/SCREEN, SCP), or a **{ref}`spray processor <machine-wet-bench>`** (FSI Mercury).
* **{ref}`Patterned-wafer inspection <machine-defect-inspection>`** (KLA-Tencor 2xxx/AIT class).

## Machines likely used at SkyWater

* **GaSonics PEP, Iridia RF microwave and Mattson Aspen II ashers** —
  named on SkyWater's facilities page with their gases and
  temperatures.[^skw-01] Strength: **strong** for existence; the
  assignment of this strip to any one of them is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric,
  BOE")[^skw-01] for SPM/SC-1. Strength: strong for existence.
* **DNS wet bench and FSI Mercury** ("industry standard
  HF/SC1/SC2").[^skw-01] Strength: strong for existence.
* **KLA-Tencor AIT** patterned-wafer inspection, our reading of "AIT"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {term}`forming gas` ({ref}`H₂/N₂ <material-anneal-ambients>`)** for the
  ash;[^skw-01] **{ref}`CF₄ <material-etch-gases>`**, listed on the Iridia and Mattson
  ashers,[^skw-01] attacks the screen oxide and would, we infer, be
  omitted here (category page).
* **Sulphuric acid and hydrogen peroxide** ({ref}`wet chemicals <material-wet-chemicals>`) for SPM;[^wiki-piranha]
  **ammonium hydroxide** for SC-1; **hydrochloric acid** for an
  optional SC-2.[^wiki-rca]
* **{ref}`Ultrapure DI water <material-ultrapure-water>`**, **isopropanol**, **nitrogen**.
* Chemical suppliers named in SkyWater's filings: KMG Chemicals (2021
  S-1), EMD Performance Materials (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`HVASTI <step-069>` (the implant whose resist is
  stripped); mask: {ref}`HVNTM <step-068>`.
* Next: {ref}`LDNTM <step-071>` (the SONOS tip mask coated on the
  cleaned surface).
* Companion strips: {ref}`ASTIS <step-067>` before,
  {ref}`LDASTIS <step-074>` after.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

**Related patents.**

* {ref}`Plasma asher with microwave trap <patent-gp22748832>` — US 5,498,308 A (1994)
* {ref}`Low temperature dry process for stripping photoresist after high dose ion implantation <patent-gp25102092>` — US 5,811,358 A (1997)
* {ref}`Method of ashing a photoresist <patent-gp33298522>` — US 2004/0214448 A1 (2003)
* {ref}`Apparatus and plasma ashing process for increasing photoresist removal rate <patent-gp35448183>` — US 7,449,416 B2 (2004)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — 0.3 µm HV-tip resist, 40°
  angle, 0.02 µm penetration.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — GaSonics PEP; Iridia; Mattson
  Aspen II; Akrion Gamma; DNS and FSI Mercury benches.[^skw-01]
* LinkedIn, SkyWater Technology Foundry listings — defect-metrology
  tools.[^job-06]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the two-stage
  low-temperature ash.[^pat-strip-mosel]

### High-level understanding

* Wikipedia, *Plasma ashing* — downstream ashing.[^wiki-ash]
* Wikipedia, *Piranha solution* and *RCA clean* — the wet
  chemistries.[^wiki-piranha][^wiki-rca]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  resist stripping and cleaning.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD doses that
  set the crust.[^txt-04]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — ash and
  wet-clean tools.[^txt-07]

### Deep dive

* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1989 — the carbonised
  layer of high-dose implanted resist, the residues of O₂ ashing and a
  two-step ashing process (abstract).[^fujimura-1989]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1990 — nitrogen
  addition in downstream ashing.[^fujimura-1990]
* Fujimura et al. (Fujitsu), *J. Vac. Sci. Technol. B* 1991 — O₂ + H₂O
  downstream stripping.[^fujimura-1991]
* Fujimura et al. (Fujitsu), *J. Vac. Sci. Technol. B* 1994 —
  sodium-free ashing with water vapour.[^fujimura-1994]
* Horsky, IIT 1998 — resist outgassing in high-energy and high-current
  implanters.[^horsky-1998]
* Roche, Michaud and Bruel, *MRS Proc.* 1985 — outgassing of resist
  during implantation.[^roche-1985]
* Ohmi, *J. Electrochem. Soc.* 1996 — room-temperature wet cleaning as
  an alternative to hot SPM/SC-1.[^ohmi-1996]
* Kern, *Handbook of Silicon Wafer Cleaning Technology* — overview of
  cleaning chemistry and contamination.[^kern-handbook]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — post-implant strip and clean.[^reinhardt-2010]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the
  low-temperature dry strip after implantation.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — ashing designed around
  the carbonised crust.[^pat-strip-tsmc]
* Kamarehi and Simpson (Fusion Systems), US 5,498,308 — a downstream
  microwave asher.[^pat-asher-fusion]
* Becknell, Hammar and Ferris (Axcelis), US 7,449,416 — a plasma
  ashing process for higher removal rate.[^pat-asher-axcelis]

## Open questions

* The ash recipe for the thin HV-tip resist, and whether it differs
  from the standard implant strip, is not public.
* The HV tip dose that determines the crust is an inference from
  LDD-typical values ({ref}`HVASTI <step-069>`).
* Which asher and wet bench run this strip is not stated publicly.

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
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
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
[^fujimura-1994]: S. Fujimura, M. T. Suzuki, K. Shinagawa and M.
    Nakamura, "Sodium contamination free ashing process using O₂+H₂O
    plasma downstream", *Journal of Vacuum Science & Technology B*
    **12**(4), 2409–2413 (1994). <https://doi.org/10.1116/1.587773>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^roche-1985]: D. Roche, J. F. Michaud and M. Bruel, "Outgassing of
    Photoresist During Ion Implantation", *MRS Proceedings* **45**
    (1985). <https://doi.org/10.1557/PROC-45-203>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
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
[^pat-asher-fusion]: M. Kamarehi and J. E. Simpson (Fusion Systems),
    *Plasma asher with microwave trap*, US 5,498,308 A, granted
    1996-03-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
[^pat-asher-axcelis]: A. F. Becknell, P. Hammar and D. Ferris (Axcelis
    Technologies), *Apparatus and plasma ashing process for increasing
    photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
