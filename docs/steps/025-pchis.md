(step-025)=
# Step 025 — PCHIS: P-channel BF2 implant strip

| | |
|---|---|
| **Step number** | 25 of 171 |
| **Step code** | `PCHIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PNCHI <step-024>` |
| **Next step** | {ref}`PWBM <step-026>` |

## What this step is

`PCHIS` strips the photoresist patterned at {ref}`HVTPM <step-022>`
after it has masked the two high-Vt PMOS channel implants
{ref}`PCHI <step-023>` and {ref}`PNCHI <step-024>`, and cleans the
wafer for the P-well block mask {ref}`PWBM <step-026>`. The step list
names it after the last implant ("P-channel BF2 implant strip").

The resist is the roughly 1 µm i-line resist of an implant-block
layer ({ref}`HVTPM <step-022>`). It has received two keV-class
channel implants at light doses (of order 10¹²–10¹³ cm⁻² each,
illustrative; {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`), one of
them BF₂. As at {ref}`LVTNIS <step-016>` this is a *light* implant
strip: the crust is thin and the popping risk low compared with the
MeV-well strips ({ref}`LVTPIS <step-021>`, {ref}`PWIS <step-029>`).
One detail is specific to it: BF₂ implants leave fluorine in the
resist crust, and fluorinated residues can be more tenacious in a
pure-oxygen ash, which is one reason implant-strip recipes add
hydrogen or water vapour (category page; TXT-05).

The surface under the resist is still entirely oxide — pad oxide over
the active areas, trench oxide over the field — so the acid–peroxide
sequence can be used without restriction.

## Step category

`PCHIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type. The category page explains the general recipe;
what is specific here is that the next step is a *thick-resist* well
mask, so the surface must be free of the particles that would cause
pinholes or coating defects in a 2–3 µm film.

## Why this step exists

A fresh resist for {ref}`PWBM <step-026>` cannot be spun over the old
one, and any residue left behind would block the P-well implants
locally. The crust of implanted resist is a different material from
the bulk: "the top portion of the photoresist layer is transformed
into a carbonized crust that is difficult to remove because of its
low solubility in wet strippers" (PAT-STRIP-TSMC). Even at light
doses it must be removed by plasma before the wet steps can finish
the job, and the implanted species and sputtered metals it contains
must not be carried into the {ref}`RTAI <step-034>` anneal.

## How it is typically performed

An industry-generic light-implant strip for a 200 mm, 130 nm-era fab:

1. **Plasma ash.** Downstream oxygen plasma with a nitrogen or
   forming-gas addition. For light doses a single-stage recipe at
   200–270 °C is common; fabs that run one standard implant-strip
   recipe use the two-stage sequence anyway — a first stage below
   about 220 °C "by oxygen and nitrogen/hydrogen plasma" until the
   crust is gone, then a hotter bulk stage (PAT-STRIP-MOSEL). The
   remote configuration lets "electrically charged particles time to
   recombine before they reach the wafer surface" (WIKI-ASH).
   SkyWater's ashers span "120C – 270C" (Gasonic PEP), "40C-270C"
   (Iridia) and "up to 250C" (Mattson Aspen2), with N₂, O₂, H₂/N₂ and
   CF₄ options (SKW-01).
2. **Wet strip.** SPM (H₂SO₄:H₂O₂) — "used to clean organic residues
   off substrates" (category page, citing Wikipedia) — on a batch
   bench; SkyWater's Akrion Gamma lists "Sulfuric" (SKW-01).
3. **Clean.** SC-1 for particles, optionally SC-2 for metals
   (WIKI-RCA). No HF: the pad oxide must survive as the screen for
   the four implants still to come.
4. **Rinse, dry, inspect.** Cascade rinse, spin or IPA dry, particle
   scan.

## Machines typically used

* **Downstream plasma asher**, 200 mm single-wafer (Gasonics
  Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK) (category page).
* **Batch wet bench** (SPM, SC-1, SC-2) or **spray processor**.
* **Surface scanner** (KLA-Tencor Surfscan class) for particles.

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia RF microwave, Mattson Aspen 2** (SKW-01).
  Strength: **strong** for existence; assignment is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1", SKW-01).
  Strength: strong for existence.
* **DNS wet bench / FSI Mercury** (SKW-01). Strength: strong for
  existence.
* **KLA-Tencor SP1** unpatterned surface scanner (JOB-01). Strength:
  medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)** for the ash (SKW-01).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide,
  hydrochloric acid** (WIKI-RCA; category page).
* **DI water, isopropanol, nitrogen**.
* Chemical suppliers named by SkyWater: KMG Chemicals, EMD
  Performance Materials (SEC-01, SEC-02).

## Related steps and cross-references

* Previous: {ref}`PNCHI <step-024>`; the resist came from
  {ref}`HVTPM <step-022>` and also masked {ref}`PCHI <step-023>`.
* Next: {ref}`PWBM <step-026>` (thick-resist P-well block mask).
* Sister strips: {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`,
  {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **JOB-01** — Indeed, SkyWater Technology Foundry listings, retrieved
  2026-08-30 ("SEM/AIT/KLA/SP1/EV300/1X").
  <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
* **SEC-01 / SEC-02** — SkyWater Technology, Inc., Form S-1 (2021) and
  Form 10-K (fiscal 2023).
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>,
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
* **PAT-STRIP-MOSEL** — US 5,811,358 A (Mosel Vitelic), granted
  1998-09-22.
  <https://patents.google.com/patent/US5811358A/en>
* **PAT-STRIP-TSMC** — US 2004/0214448 A1 (TSMC), published
  2004-10-28.
  <https://patents.google.com/patent/US20040214448A1/en>

### High-level understanding

* **WIKI-ASH** — Wikipedia, *Plasma ashing*.
  <https://en.wikipedia.org/wiki/Plasma_ashing>
* **WIKI-RCA** — Wikipedia, *RCA clean*.
  <https://en.wikipedia.org/wiki/RCA_clean>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4.
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1.
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **KERN-1990** — W. Kern, "The Evolution of Silicon Wafer Cleaning
  Technology", *J. Electrochem. Soc.*, vol. 137, pp. 1887–1892, 1990,
  DOI 10.1149/1.2086825.
  <https://doi.org/10.1149/1.2086825>

## Open questions

* The SKY130 strip recipe is not public.
* Whether the fab uses one generic implant-strip recipe for all light
  and heavy implants, or tailors it, is unknown.
