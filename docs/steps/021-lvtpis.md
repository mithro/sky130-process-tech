(step-021)=
# Step 021 — LVTPIS: P-channel implant strip

| | |
|---|---|
| **Step number** | 21 of 171 |
| **Step code** | `LVTPIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`LVTPI <step-020>` |
| **Next step** | {ref}`HVTPM <step-022>` |

## What this step is

`LVTPIS` removes the thick N-well photoresist that was patterned at
{ref}`NWM <step-017>` and has since masked three implants — the two
MeV-class phosphorus well implants {ref}`NWI <step-018>` and
{ref}`NWI2 <step-019>` and the keV P-channel threshold implant
{ref}`LVTPI <step-020>` — and then cleans the wafer for the next
lithography, {ref}`HVTPM <step-022>`. The step list names it after the
last implant it follows ("P-channel implant strip"), but the resist it
removes is the N-well resist.

This is the hardest strip of the module. The resist is the thickest
in the flow so far (2–3 µm class, inferred on the
{ref}`NWM <step-017>` page), it has been bombarded by high-energy
ions for the longest cumulative time, and the summed dose is of order
10¹³ cm⁻² (illustrative; {ref}`NWI <step-018>`). All three conditions
thicken the carbonised crust and raise the risk of popping. The wafer
surface under the resist is, we infer, still all oxide (pad oxide and trench
oxide), which allows the full SPM/SC-1 sequence.

## Step category

`LVTPIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type; it is the direct analogue of
{ref}`DNIS <step-009>`, which removed the resist of the deep N-well
implant, and shares its recipe considerations.

## Why this step exists

The resist has to go before the next coat, and it has to go
completely: residue over a future high-Vt PMOS region would block the
{ref}`PCHI <step-023>` implant locally and produce a transistor with
the wrong threshold. The crust of an MeV-implanted resist is the
obstacle. Ion bombardment turns "the top portion of the photoresist
layer … into a carbonized crust that is difficult to remove because
of its low solubility in wet strippers" (PAT-STRIP-TSMC); beneath it
the "subsurface resist generally contains more volatile, shorter
molecular weight polymer" whose vapours "build up pressure beneath
the implant-hardened surface layer" until "this pressure can
violently rupture the skin, an event that spreads particles of the
implant-hardened cross-link hydrogen deficient surface layer material
throughout the stripping chamber" (PAT-STRIP-MOSEL). Wikipedia's
summary is that problems arise "when this photoresist has undergone
an implant step previously and heavy metal are embedded in the
photoresist and it has experienced high temperatures causing it to be
resistant to oxidizing" (WIKI-ASH).

## How it is typically performed

An industry-generic MeV-implant-resist strip for a 200 mm, 130 nm-era
fab:

1. **Two-stage plasma ash.** A first stage below the popping
   threshold — "removed by oxygen and nitrogen/hydrogen plasma in a
   low-temperature (<220 °C) environment", preferably 150–220 °C
   (PAT-STRIP-MOSEL) — until the crust is consumed, then a hotter
   oxygen stage for the bulk of the 2–3 µm film. The forming-gas
   addition helps because hydrogen penetrates and reduces the
   carbonised layer (category page). SkyWater's ashers offer exactly
   this: "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C";
   "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C";
   "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C" (SKW-01).
   Downstream plasma is used so that the neutral atomic oxygen does
   the work and charged species recombine before reaching the wafer
   (WIKI-ASH). Endpoint on the CO emission line, then a timed
   over-ash.
2. **Wet strip.** SPM (H₂SO₄:H₂O₂, roughly 3:1 to 4:1, self-heated to
   above 100 °C) to dissolve the remaining organics and any popped
   flakes (category page; TXT-02). SkyWater's Akrion Gamma bench lists
   "Sulfuric" (SKW-01).
3. **Clean.** SC-1 (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles, SC-2
   (HCl/H₂O₂/H₂O) for the metals that an implanter's beam-line and
   disc can sputter onto the resist (WIKI-RCA). The pad oxide is
   preserved for the remaining implants.
4. **Rinse, dry, inspect.** Cascade rinse, spin or IPA dry; laser
   surface scan and patterned-wafer inspection for flakes.

The resist's thickness also matters for cycle time: at typical
downstream-asher rates of a few micrometres per minute (TXT-07) a
thick implant resist takes noticeably longer than an etch resist, and
the crust stage cannot be hurried.

## Machines typically used

* **Downstream plasma asher** with a two-step, forming-gas-capable
  recipe: Gasonics Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK
  (category page).
* **Batch wet bench** (SPM, SC-1, SC-2) or **spray processor**.
* **Surface scanner / patterned inspection**.

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia RF microwave, Mattson Aspen 2** (SKW-01) —
  the Iridia's "H2/N2" and the Mattson's "H2>N2" options are the
  forming-gas chemistries used for implant crusts. Strength: **strong**
  for existence; assignment is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1", SKW-01).
  Strength: strong for existence.
* **DNS wet bench / FSI Mercury** for HF/SC1/SC2 (SKW-01). Strength:
  strong for existence.
* **KLA-Tencor SP1 and AIT** (JOB-01: "SEM/AIT/KLA/SP1/EV300/1X") for
  particle and residue inspection. Strength: medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)**; **CF₄** is available but
  attacks the oxide surface and is normally omitted (SKW-01; category
  page).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide,
  hydrochloric acid** (WIKI-RCA; category page).
* **DI water, isopropanol, nitrogen**.
* Chemical suppliers named by SkyWater: KMG Chemicals, EMD
  Performance Materials (SEC-01, SEC-02).

## Related steps and cross-references

* Previous: {ref}`LVTPI <step-020>`; the resist came from
  {ref}`NWM <step-017>` and masked {ref}`NWI <step-018>` and
  {ref}`NWI2 <step-019>` as well.
* Next: {ref}`HVTPM <step-022>`.
* The comparable heavy-implant-resist strips are {ref}`DNIS <step-009>` and
  {ref}`PWIS <step-029>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (ashers with gases and temperatures; Akrion,
  DNS, FSI benches).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **JOB-01** — Indeed, SkyWater Technology Foundry listings, retrieved
  2026-08-30.
  <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
* **SEC-01 / SEC-02** — SkyWater Technology, Inc., Form S-1 (2021) and
  Form 10-K (fiscal 2023).
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>,
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
* **PAT-STRIP-MOSEL** — US 5,811,358 A (Mosel Vitelic), *Low
  temperature dry process for stripping photoresist after high dose
  ion implantation*, granted 1998-09-22.
  <https://patents.google.com/patent/US5811358A/en>
* **PAT-STRIP-TSMC** — US 2004/0214448 A1 (TSMC), *Method of ashing a
  photoresist*, published 2004-10-28.
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
* **TXT-07** — M. Quirk and J. Serda, *Semiconductor Manufacturing
  Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
  <https://openlibrary.org/isbn/9780130815200>

### Deep dive

* **KERN-HANDBOOK** — K. A. Reinhardt and W. Kern (eds.), *Handbook of
  Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
  ch. 1. <https://doi.org/10.1016/b978-081551554-8.50004-5>
* **ITRS-01** — ITRS 2001, *Front End Processes* (surface
  preparation).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>

## Open questions

* The ash recipe (stages, temperatures, gases) and wet sequence are
  not public.
* Whether the three implants really share one resist, and hence
  whether this is the strip of the N-well resist, is inferred from
  the step order.
* How much pad oxide is lost per strip/clean cycle, and whether that
  loss is budgeted against a later sacrificial-oxide step, is unknown
  (see the open question on {ref}`NS19 <step-013>`).
