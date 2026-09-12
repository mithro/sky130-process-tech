(step-029)=
# Step 029 — PWIS: P-well implant strip

| | |
|---|---|
| **Step number** | 29 of 171 |
| **Step code** | `PWIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWI2 <step-028>` |
| **Next step** | {ref}`PWDEM <step-030>` |

## What this step is

`PWIS` removes the thick P-well block resist patterned at
{ref}`PWBM <step-026>`, which has masked the two boron well implants
{ref}`PWI <step-027>` and {ref}`PWI2 <step-028>`, and cleans the wafer
for the last mask of the module, {ref}`PWDEM <step-030>`.

The resist is a thick (about 2 µm class, inferred on the
{ref}`PWBM <step-026>` page) implant resist that has absorbed boron
at a few hundred keV and a summed dose of order 10¹³ cm⁻²
(illustrative; {ref}`PWI <step-027>`). It is therefore a *heavy*
implant strip of the same kind as {ref}`LVTPIS <step-021>` and
{ref}`DNIS <step-009>`, with a carbonised crust and a real popping
risk, although boron — light and with a long range — deposits less of
its energy in the top of the resist than phosphorus does, so the crust
is somewhat thinner than after the N-well implants (TXT-01, ch. 8;
inference). Because `PWBM` is a *block* mask, the resist covered only
the N-wells and the 20 V regions: most of the wafer was open and the
resist area to be removed is smaller than for a normal mask.

The surface beneath is, we infer, still all oxide (pad oxide on active, trench
oxide on field), so the full SPM/SC-1/SC-2 sequence is available.

## Step category

`PWIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type, the fourth of five in this module. The category
page's discussion of the crust and of two-stage ashing applies in
full.

## Why this step exists

The next lithography, {ref}`PWDEM <step-030>`, is another thick
implant resist that must be coated on a clean surface; any residue of
this resist would print as a defect and would block the drain-extended
P-well implants locally — in a 20 V device, exactly where the doping
is most critical. The crust must be removed by plasma first: "the top
portion of the photoresist layer is transformed into a carbonized
crust that is difficult to remove because of its low solubility in
wet strippers" (PAT-STRIP-TSMC). And it must be removed without
popping, which "spreads particles of the implant-hardened cross-link
hydrogen deficient surface layer material throughout the stripping
chamber" (PAT-STRIP-MOSEL). Finally, the metals that a batch
implanter's disc and beam-line sputter onto the resist must be
cleaned off before the wafer reaches the {ref}`RTAI <step-034>`
anneal, where they would be driven into the silicon.

## How it is typically performed

An industry-generic heavy-implant-resist strip for a 200 mm,
130 nm-era fab:

1. **Two-stage plasma ash.** First stage below the popping threshold
   with oxygen plus forming gas — "removed by oxygen and
   nitrogen/hydrogen plasma in a low-temperature (<220 °C)
   environment" (PAT-STRIP-MOSEL) — until the crust has gone, then a
   hot oxygen stage for the bulk. Downstream plasma so that neutral
   atomic oxygen does the work (WIKI-ASH). SkyWater's ashers:
   "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C";
   "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C";
   "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C" (SKW-01).
   Endpoint on CO emission, timed over-ash.
2. **Wet strip.** SPM (H₂SO₄:H₂O₂ about 3:1–4:1, above 100 °C) to
   dissolve residual organics and flakes (category page; TXT-02);
   "Sulfuric" on SkyWater's Akrion Gamma bench (SKW-01).
3. **Clean.** SC-1 for particles and SC-2 for metals (WIKI-RCA); no
   HF, because the pad oxide is still the screen for the two
   drain-extended implants and must remain.
4. **Rinse, dry, inspect.** Cascade rinse, spin or IPA dry; laser
   surface scan for particles and patterned inspection for residue.

## Machines typically used

* **Downstream plasma asher** with forming-gas capability (Gasonics
  Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK).
* **Batch wet bench** (SPM, SC-1, SC-2) or **spray processor**.
* **Surface scanner** and **patterned-wafer inspection**.

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia RF microwave, Mattson Aspen 2** (SKW-01),
  the latter two with hydrogen-bearing chemistries. Strength:
  **strong** for existence; assignment is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1", SKW-01).
  Strength: strong for existence.
* **DNS wet bench / FSI Mercury** (SKW-01). Strength: strong for
  existence.
* **KLA-Tencor SP1 / AIT** (JOB-01). Strength: medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)** (SKW-01; category page).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide,
  hydrochloric acid** (WIKI-RCA).
* **DI water, isopropanol, nitrogen**.
* Chemical suppliers named by SkyWater: KMG Chemicals, EMD
  Performance Materials (SEC-01, SEC-02).

## Related steps and cross-references

* Previous: {ref}`PWI2 <step-028>`; the resist came from
  {ref}`PWBM <step-026>` and also masked {ref}`PWI <step-027>`.
* Next: {ref}`PWDEM <step-030>`.
* Comparable heavy-implant strips: {ref}`DNIS <step-009>`,
  {ref}`LVTPIS <step-021>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **JOB-01** — Indeed, SkyWater Technology Foundry listings, retrieved
  2026-08-30.
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
* **TXT-01** — J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon
  VLSI Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 8
  (energy deposition of light versus heavy ions).
  <https://openlibrary.org/isbn/9780130850379>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4.
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1.
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **KERN-HANDBOOK** — K. A. Reinhardt and W. Kern (eds.), *Handbook of
  Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
  ch. 1. <https://doi.org/10.1016/b978-081551554-8.50004-5>

## Open questions

* The strip recipe and wet sequence are not public.
* Whether an SC-2 metal clean is included here or deferred to the
  pre-anneal clean before {ref}`RTAI <step-034>` is unknown.
