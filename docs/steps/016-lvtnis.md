(step-016)=
# Step 016 — LVTNIS: Low Vt NMOS implant strip

| | |
|---|---|
| **Step number** | 16 of 171 |
| **Step code** | `LVTNIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`LVTNI <step-015>` |
| **Next step** | {ref}`NWM <step-017>` |

## What this step is

`LVTNIS` removes the photoresist that was patterned at
{ref}`LVTNM <step-014>` and used as the implant mask at
{ref}`LVTNI <step-015>`, then cleans the wafer so that the next mask,
{ref}`NWM <step-017>`, can be coated on a bare, particle-free oxide
surface. It is the second implant-resist strip of the flow (after
{ref}`DNIS <step-009>`) and the first of five in the well and channel
module; the step list used in this reference pairs every implant mask
with such an "…IS" step.

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
*post-implant* type. The category page explains why implant strips are
"longer and more carefully engineered than etch strips": the ion beam
carbonises the top of the resist into a {term}`crust <implant crust>` that {term}`ashes <ash>` slowly and can
{term}`pop <popping>`. For this particular strip the crust is thin, because the dose is
low and the energy modest; the strips after the well masks
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
and, eventually, the {ref}`RTAI <step-034>` anneal. A poorly stripped
implant resist shows up as popped flakes — the patent literature notes
that "the popping problem … causes the photoresist to become even
harder"[^pat-strip-mosel] and as threshold-voltage outliers where
residue {term}`shadowed <shadowing>` a later implant.

## How it is typically performed

An industry-generic implant-strip sequence for a 200 mm, 130 nm-era
fab:

1. **Plasma ash.** Downstream (remote) microwave or RF oxygen plasma.
   The problem specific to implanted resist is that "the top portion of
   the photoresist layer is transformed into a carbonized crust that is
   difficult to remove"[^pat-strip-tsmc] and that during a conventional
   "high temperature (>200° C.) dry ashing" the volatile bulk resist can
   "build up pressure beneath the implant-hardened surface layer" until
   it pops.[^pat-strip-mosel] The standard countermeasure is a two-step
   recipe: a first step at low temperature — "removed by oxygen and
   nitrogen/hydrogen plasma in a low-temperature (<220 °C)
   environment"[^pat-strip-mosel] — until the crust is gone, then a
   hotter bulk step. For a low-dose channel implant like `LVTNI` many
   fabs use a single-step recipe, because the crust is thin (industry
   practice).[^txt-05] SkyWater's list describes ashers with exactly
   this gas set and temperature range: "Gasonic PEP, remote microwave
   plasma, N2, O2, 120C – 270C", "Iridia RF microwave, N2, O2, H2, CF4,
   NH3, H2/N2, 40C-270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2,
   up to 250C".[^skw-01] Downstream configuration is chosen because
   "monatomic oxygen is electrically neutral" and the remote plasma
   "prevents damage to the wafer surface".[^wiki-ash]
2. **Wet strip and clean.** Sulphuric acid–hydrogen peroxide ({term}`SPM`,
   "piranha") to dissolve the last organics — "a typical mixture is 3
   parts of concentrated sulfuric acid and 1 part of 30 wt. % hydrogen
   peroxide solution" (category page, citing Wikipedia) — followed by
   {term}`SC-1` (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles and, optionally, {term}`SC-2`
   (HCl/H₂O₂/H₂O) for metals.[^wiki-rca] SkyWater's Akrion Gamma bench
   lists "Sulfuric, SC1" among its chemistries.[^skw-01]
3. **Rinse and dry.** Cascade DI-water rinse, spin-rinse or IPA
   (Marangoni) dry.
4. **Inspection.** Patterned-wafer optical inspection for residue and
   particles.

We infer that the pad oxide is left in place: a dilute-HF "oxide-last"
step is avoided here because the same oxide must still screen the four
implants that follow ({ref}`NWI <step-018>` to {ref}`LVTPI <step-020>`);
some flows accept a small oxide loss in SC-1 as the price of
cleanliness.[^txt-02]

## Machines typically used

* **Downstream plasma asher**, 200 mm single-wafer: Gasonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES series, PSK
  (category page).
* **Batch wet bench** with SPM, SC-1, SC-2 tanks and a rinser/dryer
  (Akrion, DNS/SCREEN, SCP), or a **spray processor** (FSI Mercury).
* **Patterned-wafer inspection** (KLA-Tencor 2xxx/AIT class).

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia RF microwave and Mattson Aspen 2 ashers** — all
  named on SkyWater's facilities page with their gases and
  temperatures.[^skw-01] Strength: **strong** for existence; the
  assignment of this particular strip to any one of them is an
  inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric,
  BOE")[^skw-01] for the SPM/SC-1 sequence. Strength: strong for
  existence.
* **DNS wet bench and FSI Mercury** ("industry standard
  HF/SC1/SC2")[^skw-01] as alternative clean tools. Strength: strong for
  existence.
* **KLA-Tencor AIT** patterned-wafer inspection, from a SkyWater job
  posting.[^job-01] Strength: medium.

## Resources required

* **Oxygen, nitrogen, {term}`forming gas` (H₂/N₂)** for the ash; small **CF₄**
  additions are available on the Mattson and Iridia tools[^skw-01] but
  attack oxide and would normally be omitted here.
* **Sulphuric acid (96–98 %) and hydrogen peroxide (30 %)** for
  SPM;[^wiki-rca] **ammonium hydroxide** for SC-1; **hydrochloric acid**
  for SC-2[^wiki-rca] (category page).
* **Ultrapure DI water**, **isopropanol** for drying, **nitrogen**.
* SkyWater names KMG Chemicals and EMD Performance Materials among its
  chemical suppliers.[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LVTNI <step-015>` (the implant whose resist is
  stripped); mask: {ref}`LVTNM <step-014>`.
* Next: {ref}`NWM <step-017>` (the N-well mask coated on the cleaned
  surface).
* Companion strips in this module: {ref}`LVTPIS <step-021>`,
  {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`,
  {ref}`PWDEIS <step-033>`; the earlier {ref}`DNIS <step-009>`
  stripped an MeV-implanted resist.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — Gasonic PEP; Iridia; Mattson
  Aspen2; Akrion Gamma; DNS and FSI Mercury benches.[^skw-01]
* Indeed, SkyWater Technology Foundry listings — the defect-metrology
  tool list "SEM/AIT/KLA/SP1/EV300/1X".[^job-01]
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
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  resist stripping; wafer cleaning.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — implanted-resist
  stripping.[^txt-05]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — ash and
  wet-clean tools.[^txt-07]

### Deep dive

* Kern, *J. Electrochem. Soc.* 1990 — the history and chemistry of the
  {term}`RCA clean`.[^kern-1990]
* ITRS 2001, *Front End Processes* — surface preparation.[^itrs-01]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1989 — the measured
  crust-and-popping mechanism of ion-implanted resist that every implant
  strip has to defeat.[^fujimura-1989]
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
* Roche, Michaud and Bruel, *MRS Proc.* 1985 — resist outgassing during
  implantation, the origin of the hardened crust the strip
  removes.[^roche-1985]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the two-stage
  low-temperature ash recipe for implanted resist.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — an ashing sequence
  designed around the carbonised crust.[^pat-strip-tsmc]

## Open questions

* The SKY130 ash recipe (single- or two-step, temperatures, gases) and
  wet sequence are not public.
* Whether the clean includes an SC-2 step, and whether any oxide
  thinning is budgeted here, is unknown.
* Which of the three ashers on SkyWater's public tool list[^skw-01] runs
  implant strips is not stated publicly.

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
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page), retrieved 2026-08-30.
    <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
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
