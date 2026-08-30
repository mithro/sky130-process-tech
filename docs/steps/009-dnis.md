(step-009)=
# Step 009 — DNIS: High V deep N-well implant strip

| | |
|---|---|
| **Step number** | 9 of 171 |
| **Step code** | `DNIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`DNI <step-008>` |
| **Next step** | {ref}`LINOX <step-010>` |

## What this step is

`DNIS` removes the thick photoresist that masked the deep N-well
implant at {ref}`DNI <step-008>`, and cleans the wafer so that it can
go into the liner-oxidation furnace at {ref}`LINOX <step-010>`. It is
the first of the many *implant strip* steps in SKY130 (the step list
used in this reference pairs almost every implant mask with an "…IS"
strip). The step name we use, "High V deep N-well implant strip",
indicates that the
deep N-well is associated with the high-voltage device family (see
{ref}`DNM <step-007>`).

What makes this strip different from an ordinary post-etch strip is
the state of the resist and of the wafer:

* the resist has been bombarded by MeV phosphorus ions, which
  carbonise its top surface into a hard crust that ordinary O₂ ashing
  removes slowly and that can pop or flake during heating (TXT-02);
* the wafer has open silicon trenches with bare, plasma-damaged
  sidewalls, so the clean must be gentle enough not to roughen or
  etch them, and thorough enough that no organic or metallic residue
  goes into the 900–1100 °C furnace that follows.

## Step category

`DNIS` is a {ref}`Resist strip / clean <category-strip>` step — an
implant-resist strip followed by a pre-furnace clean. The same
combination recurs after every masked implant
({ref}`LVTNIS <step-016>`, {ref}`PWIS <step-029>`,
{ref}`PDIS <step-084>`, …), but this instance is followed directly by
a high-temperature oxidation, which raises the cleanliness
requirement.

## Why this step exists

Photoresist cannot survive a furnace: it would carbonise, contaminate
the tube and leave the wafer covered in particles. It also holds
mobile-ion and organic contamination that must not reach the
silicon–oxide interface formed at {ref}`LINOX <step-010>`. The strip
therefore has to remove every trace of the resist, the implant crust
and any sputtered material, and the clean has to leave a
hydrophilic, particle-free surface — inside the trenches as well as
on the nitride.

A residue left here would be sealed under the liner oxide and the HDP
fill, where it can cause voids, leakage or gate-oxide defects at the
active edge much later in the flow.

## How it is typically performed

An industry-generic implant-strip sequence for a 200 mm, 130 nm-era
fab:

1. **Plasma ash.** Downstream (remote) microwave or RF O₂ plasma at
   150–270 °C. Fabs commonly use a two-stage recipe for high-dose or
   high-energy implant resist: a low-temperature first stage, often
   with a forming-gas (H₂/N₂) or N₂/O₂ addition, that breaks up the
   carbonised crust without popping, then a hotter O₂ stage to remove
   the bulk resist (TXT-02, TXT-05). SkyWater's own list describes its
   ashers as "Gasonic PEP, remote microwave plasma, N2, O2, 120C –
   270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"
   (SKW-01) — exactly the gas set for this kind of recipe.
2. **Wet strip / clean.** Sulphuric-peroxide mixture (H₂SO₄ : H₂O₂,
   "piranha" or SPM) at roughly 100–130 °C (TXT-02) to remove the last
   organics, then
   SC-1 (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles and SC-2
   (HCl/H₂O₂/H₂O) for metals (WIKI-RCA). Because the nitride and the
   trench silicon are both exposed, the sequence avoids any long HF
   step that would undercut the pad oxide beneath the nitride (some
   flows do use a controlled short HF dip for exactly that reason,
   PAT-STI-CR, but that belongs to the liner-oxidation preparation and
   is discussed at {ref}`LINOX <step-010>`).
3. **Rinse and dry.** DI-water rinse and spin or IPA (Marangoni) dry —
   SKW-01 describes both spin and IPA drying on its Akrion bench.
4. **Inspection.** Bright-field or laser-scatter inspection for resist
   residue and particles; sometimes a monitor check of the nitride
   thickness to confirm the clean has not thinned it.

## Machines typically used

* **Downstream plasma asher**, 200 mm single-wafer: Gasonics (Novellus)
  Aura/PEP series, Mattson Aspen, Axcelis/Fusion ES series, PSK.
* **Batch wet bench** with SPM, SC-1 and SC-2 tanks and a rinser/dryer;
  or a single-wafer spray tool.
* **Defect inspection** (patterned-wafer optical inspection).

## Machines likely used at SkyWater

* **Gasonics PEP** and **Mattson Aspen 2** ashers — both named on
  SKW-01 with their gases and temperatures. Strength: strong for
  existence; assignment to this step is inference.
* **Iridia RF microwave** — also listed under resist removal on
  SKW-01. Strength: strong for existence.
* **Akrion Gamma batch wet bench** — SKW-01 lists it with sulphuric,
  SC1, phosphoric and BOE chemistries and spin and IPA drying.
  Strength: strong. A sulphuric (SPM) + SC-1 sequence on this bench is
  the natural post-implant clean.
* **DNS / FSI Mercury** HF/SC1/SC2 benches (SKW-01) as the pre-furnace
  clean. Strength: strong for existence.
* **Patterned-wafer inspection — KLA-Tencor AIT** (JOB-01). Strength:
  medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)** and, for some recipes, a
  small **CF₄** addition to the ash (SKW-01).
* **Sulphuric acid and hydrogen peroxide** (SPM).
* **Ammonium hydroxide, hydrochloric acid, hydrogen peroxide**
  (SC-1/SC-2) (WIKI-RCA).
* **DI water**, **isopropanol** for drying (SKW-01).
* **Nitrogen** for drying/purge.

## Related steps and cross-references

* Previous: {ref}`DNI <step-008>` (the implant whose resist is
  stripped); mask: {ref}`DNM <step-007>`.
* Next: {ref}`LINOX <step-010>` (liner oxidation — the reason the
  clean must be furnace-grade).
* The next implant strips in the flow: {ref}`LVTNIS <step-016>`,
  {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (Gasonic PEP; Mattson Aspen2; Iridia; Akrion
  Gamma with sulphuric/SC1/phosphoric/BOE and spin/IPA dry; DNS and
  FSI Mercury HF/SC1/SC2).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **JOB-01** — Indeed, SkyWater Technology Foundry listings (Defect
  Technician 2: "SEM/AIT/KLA/SP1/EV300/1X"), retrieved 2026-08-30.
  <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
* **PAT-STI-CR** — U. Kim et al. (Spansion), US 7,439,141 B2, granted
  2008-10-21 (pad-oxide undercut of 100–300 Å before liner
  oxidation).
  <https://patents.google.com/patent/US7439141B2/en>

### High-level understanding

* **WIKI-RCA** — Wikipedia, *RCA clean* (SC-1, SC-2 compositions and
  temperatures).
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

* **REV-01** — M. Nandakumar et al., "Shallow trench isolation for
  advanced ULSI CMOS technologies", *IEDM 1998*, pp. 133–136,
  DOI 10.1109/IEDM.1998.746297 (STI flow and defectivity).
* **THUNG-2016** — B. J. Thung et al., "Challenges for 0.13µm Generation
  Shallow Trench Isolation on 0.18µm Equipment Platform", *JTEC* 8(5),
  2016, pp. 15–21 (post-trench-etch wet clean).
  <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>

## Open questions

* The actual SKY130 ash recipe (single or two-stage, temperatures) and
  wet sequence are not public.
* Whether the post-trench-etch polymer clean (see
  {ref}`STIE <step-006>`) is performed here, at `STIE`, or before
  {ref}`DNM <step-007>` is not distinguishable from the public step
  list.
* Whether `DNIS` includes the pre-liner-oxidation HF treatment or
  whether that belongs to {ref}`LINOX <step-010>` is unknown.
