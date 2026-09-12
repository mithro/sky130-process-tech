(step-033)=
# Step 033 — PWDEIS: PWDEIS implant strip

| | |
|---|---|
| **Step number** | 33 of 171 |
| **Step code** | `PWDEIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWDEI2 <step-032>` |
| **Next step** | {ref}`RTAI <step-034>` |

## What this step is

`PWDEIS` removes the thick photoresist patterned at
{ref}`PWDEM <step-030>` after it has masked the two drain-extended
P-well implants {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>`,
and cleans the wafer for the {ref}`RTAI <step-034>` anneal. It is the
last of the five implant strips of the well and channel module, and
the only one that is followed not by another lithography but by a
high-temperature step — which raises its cleanliness requirement to
the "pre-furnace" level of {ref}`DNIS <step-009>`.

The resist is a thick implant resist (2 µm class, inferred on the
{ref}`PWDEM <step-030>` page) that has received two light boron
implants — of order 10¹² cm⁻² each, illustrative
({ref}`PWDEI1 <step-031>`) — at energies up to a few hundred keV.
The crust is therefore modest by the standards of
{ref}`LVTPIS <step-021>`, and because `pwde` regions are small the
open area of the mask is small too: the strip removes almost a full
wafer's worth of resist. The surface beneath is, we infer, all oxide (pad oxide
on active, trench oxide on field).

## Step category

`PWDEIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type with a *pre-anneal clean* role. The category page
notes that the state in which the surface is left "must match what
the next step expects"; here the next step is an RTA in which any
organic or metallic residue would be baked into the silicon.

## Why this step exists

Photoresist cannot go into an anneal chamber: at 1000 °C it would
carbonise, contaminate the chamber and leave the wafer covered in
particles, and the mobile-ion and organic contamination it carries
would be driven into the channels that every implant of this module
has just defined. The strip must therefore remove all resist and its
crust — "transformed into a carbonized crust that is difficult to
remove" (PAT-STRIP-TSMC) — without popping (PAT-STRIP-MOSEL), and the
clean must take off the metals sputtered onto the wafer over ten
implants. ITRS 2001 treats front-end surface preparation as a
first-order concern for exactly this reason (ITRS-01). A residue left
here would be sealed under the gate oxides grown at
{ref}`GOX100 <step-043>` and {ref}`LVGOX <step-047>`.

## How it is typically performed

An industry-generic strip-and-pre-anneal-clean sequence for a 200 mm,
130 nm-era fab:

1. **Plasma ash.** Downstream oxygen plasma with a forming-gas
   addition; a two-stage recipe if the fab runs one for all implant
   strips — first stage "in a low-temperature (<220 °C) environment"
   with "oxygen and nitrogen/hydrogen plasma" until the crust is gone
   (PAT-STRIP-MOSEL), then a hotter bulk stage. SkyWater's ashers
   cover this range: "Gasonic PEP … N2, O2, 120C – 270C", "Iridia …
   H2/N2, 40C-270C", "Mattson Aspen2 … O2, CF4, H2>N2, up to 250C"
   (SKW-01). The remote plasma keeps charged species off the wafer
   (WIKI-ASH).
2. **Wet strip.** SPM (H₂SO₄:H₂O₂) for residual organics (category
   page; "Sulfuric" on the Akrion Gamma, SKW-01).
3. **Full RCA-type clean.** SC-1 (NH₄OH/H₂O₂/H₂O, 75–80 °C) for
   particles and SC-2 (HCl/H₂O₂/H₂O, 75–80 °C) for metals (WIKI-RCA;
   KERN-1990) — the SC-2 step matters more here than after the
   earlier strips because the anneal follows. SkyWater lists "DNS wet
   bench industry standard HF/SC1/SC2" and "FSI Mercury industry
   standard HF/SC1/SC2 rotational" (SKW-01).
4. **HF or not?** Whether the pad oxide is removed before the anneal
   is a real choice. Keeping it protects the silicon surface during
   the RTA and avoids dopant out-diffusion; removing it now would
   require a fresh sacrificial oxide before gate oxidation. The
   step list used in this reference has no sacrificial-oxide step before
   {ref}`GOX100 <step-043>`, so we infer that the pad oxide is *kept*
   through the anneal (see the open question on
   {ref}`NS19 <step-013>`).
5. **Rinse, dry, inspect.** Cascade rinse, IPA (Marangoni) or spin
   dry; laser surface scan for particles.

## Machines typically used

* **Downstream plasma asher** (Gasonics Aura/PEP, Mattson Aspen,
  Axcelis/Fusion ES, PSK).
* **Batch wet bench** with SPM, SC-1, SC-2 and rinser/dryer, or a
  **spray/single-wafer processor** for the RCA clean.
* **Surface scanner** (KLA-Tencor Surfscan class).

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia RF microwave, Mattson Aspen 2** (SKW-01).
  Strength: **strong** for existence; assignment is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1", SKW-01) for the
  SPM/SC-1 steps. Strength: strong for existence.
* **DNS wet bench / FSI Mercury** ("HF/SC1/SC2", SKW-01) for the
  pre-anneal RCA clean. Strength: strong for existence; the SC-2
  capability is explicitly listed only for these two tools, which
  makes them the natural pre-anneal clean stations (inference).
* **KLA-Tencor SP1** surface scanner (JOB-01). Strength: medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)** (SKW-01).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide,
  hydrochloric acid** (WIKI-RCA; category page); **dilute HF** only if
  the oxide is removed.
* **Ultrapure DI water**, **isopropanol**, **nitrogen**.
* Chemical suppliers named by SkyWater: KMG Chemicals, EMD
  Performance Materials (SEC-01, SEC-02).

## Related steps and cross-references

* Previous: {ref}`PWDEI2 <step-032>`; the resist came from
  {ref}`PWDEM <step-030>` and also masked {ref}`PWDEI1 <step-031>`.
* Next: {ref}`RTAI <step-034>` (the anneal this clean prepares for).
* Earlier module strips: {ref}`LVTNIS <step-016>`,
  {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`,
  {ref}`PWIS <step-029>`; the analogous pre-furnace strip in the
  isolation module is {ref}`DNIS <step-009>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (ashers; Akrion; DNS and FSI "HF/SC1/SC2").
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
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4, ch. 15 (wet cleaning).
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-07** — M. Quirk and J. Serda, *Semiconductor Manufacturing
  Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
  <https://openlibrary.org/isbn/9780130815200>

### Deep dive

* **KERN-1990** — W. Kern, "The Evolution of Silicon Wafer Cleaning
  Technology", *J. Electrochem. Soc.*, vol. 137, pp. 1887–1892, 1990,
  DOI 10.1149/1.2086825.
  <https://doi.org/10.1149/1.2086825>
* **ITRS-01** — ITRS 2001, *Front End Processes* (surface
  preparation).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>

## Open questions

* Whether the pad oxide is retained through {ref}`RTAI <step-034>`
  or removed here is inferred from the absence of a sacrificial-oxide
  step in the public list.
* Whether the pre-anneal clean is part of this step or belongs to
  {ref}`RTAI <step-034>` in the fab's own grouping is unknown.
* The strip recipe is not public.
