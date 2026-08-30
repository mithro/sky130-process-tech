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
module; the step list pairs every implant mask with such an "…IS"
step.

The resist being removed is the roughly 1 µm i-line implant resist
inferred on the {ref}`LVTNM <step-014>` page. It has received a
channel-type implant — tens of keV, of order 10¹²–10¹³ cm⁻²
(illustrative values, {ref}`LVTNI <step-015>`) — which is a *light*
implant by strip standards. The wafer surface under it is entirely
oxide: pad oxide over the active areas and trench oxide over the
field, with no bare silicon and no metal, so the full acid–peroxide
clean sequence can be used without restriction.

## Step category

`LVTNIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type. The category page explains why implant strips are
"longer and more carefully engineered than etch strips": the ion beam
carbonises the top of the resist into a crust that ashes slowly and
can pop. For this particular strip the crust is thin, because the dose
is low and the energy modest; the strips after the well masks
({ref}`LVTPIS <step-021>`, {ref}`PWIS <step-029>`), which have seen
MeV ions and summed doses near 10¹³ cm⁻², and above all the
source/drain strips ({ref}`PDIS <step-084>`,
{ref}`NSDIS <step-087>`) at several 10¹⁵ cm⁻², are the difficult ones.

## Why this step exists

Photoresist must be gone before the wafer can be coated again: a new
resist cannot be spun over an old one, and any organic residue under
the {ref}`NWM <step-017>` resist would print as a defect or block the
MeV well implant locally. The resist also carries the implanted
species in its crust and whatever metals the implanter's beam-line has
sputtered onto it; both must be removed before the wafer sees the next
implant and, eventually, the {ref}`RTAI <step-034>` anneal. A poorly
stripped implant resist shows up as "popped" flakes that are
"especially hard to clean from the wafer surface" (PAT-STRIP-MOSEL)
and as threshold-voltage outliers where residue shadowed a later
implant.

## How it is typically performed

An industry-generic implant-strip sequence for a 200 mm, 130 nm-era
fab:

1. **Plasma ash.** Downstream (remote) microwave or RF oxygen plasma.
   The problem specific to implanted resist is that "the top portion
   of the photoresist layer is transformed into a carbonized crust
   that is difficult to remove" (PAT-STRIP-TSMC) and that at wafer
   temperatures "above 150 to above 200 °C" the bulk resist can
   outgas so that "the entire photoresist can then 'pop'"
   (PAT-STRIP-MOSEL). The standard countermeasure is a two-step
   recipe: a first step at low temperature — "removed by oxygen and
   nitrogen/hydrogen plasma in a low-temperature (<220 °C)
   environment" (PAT-STRIP-MOSEL) — until the crust is gone, then a
   hotter bulk step. For a low-dose channel implant like `LVTNI`
   many fabs use a single-step recipe, because the crust is thin
   (industry practice; TXT-05). SkyWater's list describes ashers with
   exactly this gas set and temperature range: "Gasonic PEP, remote
   microwave plasma, N2, O2, 120C – 270C", "Iridia RF microwave, N2,
   O2, H2, CF4, NH3, H2/N2, 40C-270C" and "Mattson Aspen2, RF plasma,
   O2, CF4, H2>N2, up to 250C" (SKW-01). Downstream configuration is
   chosen because "monatomic oxygen is electrically neutral" and the
   remote plasma "prevents damage to the wafer surface" (WIKI-ASH).
2. **Wet strip and clean.** Sulphuric acid–hydrogen peroxide (SPM,
   "piranha") to dissolve the last organics — "a typical mixture is 3
   parts of concentrated sulfuric acid and 1 part of 30 wt. % hydrogen
   peroxide solution" (category page, citing Wikipedia) — followed by
   SC-1 (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles and, optionally,
   SC-2 (HCl/H₂O₂/H₂O) for metals (WIKI-RCA). SkyWater's Akrion Gamma
   bench lists "Sulfuric, SC1" among its chemistries (SKW-01).
3. **Rinse and dry.** Cascade DI-water rinse, spin-rinse or IPA
   (Marangoni) dry.
4. **Inspection.** Patterned-wafer optical inspection for residue and
   particles.

The pad oxide is left in place: a dilute-HF "oxide-last" step is
avoided here because the same oxide must still screen the four
implants that follow ({ref}`NWI <step-018>` to
{ref}`LVTPI <step-020>`); some flows accept a small oxide loss in SC-1
as the price of cleanliness (TXT-02).

## Machines typically used

* **Downstream plasma asher**, 200 mm single-wafer: Gasonics
  (Novellus) Aura/PEP, Mattson Aspen, Axcelis/Fusion ES series, PSK
  (category page).
* **Batch wet bench** with SPM, SC-1, SC-2 tanks and a rinser/dryer
  (Akrion, DNS/SCREEN, SCP), or a **spray processor** (FSI Mercury).
* **Patterned-wafer inspection** (KLA-Tencor 2xxx/AIT class).

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia RF microwave and Mattson Aspen 2 ashers** —
  all named on SKW-01 with their gases and temperatures. Strength:
  **strong** for existence; the assignment of this particular strip
  to any one of them is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric, BOE",
  SKW-01) for the SPM/SC-1 sequence. Strength: strong for existence.
* **DNS wet bench and FSI Mercury** ("industry standard HF/SC1/SC2",
  SKW-01) as alternative clean tools. Strength: strong for existence.
* **KLA-Tencor AIT** patterned-wafer inspection, from a SkyWater job
  posting (JOB-01). Strength: medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)** for the ash; small
  **CF₄** additions are available on the Mattson and Iridia tools
  (SKW-01) but attack oxide and would normally be omitted here.
* **Sulphuric acid (96–98 %) and hydrogen peroxide (30 %)** for SPM;
  **ammonium hydroxide** for SC-1; **hydrochloric acid** for SC-2
  (WIKI-RCA; category page).
* **Ultrapure DI water**, **isopropanol** for drying, **nitrogen**.
* SkyWater names KMG Chemicals and EMD Performance Materials among its
  chemical suppliers (SEC-01, SEC-02).

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

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (Gasonic PEP; Iridia; Mattson Aspen2; Akrion
  Gamma; DNS and FSI Mercury benches).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **JOB-01** — Indeed, SkyWater Technology Foundry listings (Defect
  Technician 2: "SEM/AIT/KLA/SP1/EV300/1X"), retrieved 2026-08-30.
  <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
* **SEC-01 / SEC-02** — SkyWater Technology, Inc., Form S-1
  (2021-03-22) and Form 10-K for fiscal 2023 (chemical suppliers).
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>,
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
* **PAT-STRIP-MOSEL** — M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
  Vitelic), US 5,811,358 A, *Low temperature dry process for
  stripping photoresist after high dose ion implantation*, granted
  1998-09-22.
  <https://patents.google.com/patent/US5811358A/en>
* **PAT-STRIP-TSMC** — B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC),
  US 2004/0214448 A1, *Method of ashing a photoresist*, published
  2004-10-28 ("carbonized crust").
  <https://patents.google.com/patent/US20040214448A1/en>

### High-level understanding

* **WIKI-ASH** — Wikipedia, *Plasma ashing*.
  <https://en.wikipedia.org/wiki/Plasma_ashing>
* **WIKI-RCA** — Wikipedia, *RCA clean*.
  <https://en.wikipedia.org/wiki/RCA_clean>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4 (resist stripping; wafer cleaning).
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (implanted-resist
  stripping).
  <https://openlibrary.org/isbn/9780961672171>
* **TXT-07** — M. Quirk and J. Serda, *Semiconductor Manufacturing
  Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0 (ash and
  wet-clean tools).
  <https://openlibrary.org/isbn/9780130815200>

### Deep dive

* **KERN-1990** — W. Kern, "The Evolution of Silicon Wafer Cleaning
  Technology", *Journal of the Electrochemical Society*, vol. 137,
  pp. 1887–1892, 1990, DOI 10.1149/1.2086825.
  <https://doi.org/10.1149/1.2086825>
* **ITRS-01** — ITRS 2001, *Front End Processes* (surface
  preparation).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>

## Open questions

* The SKY130 ash recipe (single- or two-step, temperatures, gases) and
  wet sequence are not public.
* Whether the clean includes an SC-2 step, and whether any oxide
  thinning is budgeted here, is unknown.
* Which of the three ashers on SKW-01 runs implant strips is not
  stated publicly.
