(step-001)=
# Step 001 — SMAT: Starting material

| | |
|---|---|
| **Step number** | 1 of 171 |
| **Step code** | `SMAT` |
| **Category** | {ref}`Substrate / starting material <category-substrate>` |
| **Phase** | FEOL — isolation |
| **Previous step** | — |
| **Next step** | {ref}`BOX <step-002>` |

## What this step is

`SMAT` is not a process step in the sense of a tool recipe; it is the
point at which a cassette of bare, polished 200 mm silicon wafers enters
the SKY130 flow. Everything that follows — isolation, wells, gates,
contacts and five levels of aluminium — is built into and on top of the
material chosen here, so the wafer specification is the first process
decision of the technology.

What can be said publicly about the SKY130 starting wafer:

* **Diameter.** SkyWater's Minnesota fab runs "200 mm equipment"
  (SKW-01) and its S130 platform table lists the wafer size as "200mm"
  (SKW-02). Cypress described Fab 4, where the 0.13 µm technology was
  ramped in 2003, as an "eight-inch wafer production facility" (CYP-07).
  Wikipedia gives the standard 200 mm wafer thickness as 725 µm and notes
  that wafers of 200 mm and above carry "a single small notch to convey
  wafer orientation" rather than a flat (WIKI-WAFER).
* **Conductivity type.** The PDK process-stack drawing labels the
  bottom of the stack "p-substrate" (PDK-04) and the 1.8 V NMOS
  cross-section drawing labels it "P-substrate" (PDK-07). The wafer is
  therefore p-type (boron-doped).
* **Bulk, not epitaxial.** SkyWater's platform table gives the S130
  substrate as "Bulk", in contrast to the S90LN entry, which reads
  "4 µm EPI" (SKW-02). We read this as a polished bulk Czochralski (CZ)
  wafer without an epitaxial layer; see the open questions below.
* **Suppliers.** SkyWater's 2021 registration statement lists its
  principal silicon-wafer suppliers as "GlobalWafers Singapore Pte. Ltd.
  (silicon wafers)" and "SEH America, subsidiary of Shin-Etsu Handotai,
  Ltd. (silicon wafers)" (SEC-01); the 2023 annual report repeats both
  names (SEC-02). In 2015 Cypress issued product-change notice
  PIN152804, "Qualification of GlobalWafer Silicon Wafers for 250nm,
  130nm and 90nm Technology Products at Cypress Fab 4", covering the
  "130nm C8/R8/S8/L8" families and stating that Cypress would use
  GlobalWafer wafers "in addition to wafers from other qualified
  suppliers" (CYP-06). That notice is the clearest public link between
  a named wafer vendor and the S8 process that became SKY130.

Everything else about the wafer — resistivity, crystal orientation,
oxygen content, flatness grade — is not stated in any public SkyWater
or Cypress document and is discussed below as industry-typical.

## Step category

This is the only step in the
{ref}`Substrate / starting material <category-substrate>` category. What
is specific to SKY130 is that it is a *bulk* 200 mm p-type wafer for a
process that, unusually for a 130 nm-era logic technology, carries
5 V and 10–20 V devices, SONOS memory and a deep N-well option on the
same substrate (PDK-07, PDK-10).

## Why this step exists

The wafer specification fixes several things that the rest of the flow
depends on:

* **Substrate doping sets the baseline for every well.** The p-type
  background is what the N-well ({ref}`NWI <step-018>`), the deep N-well
  ({ref}`DNI <step-008>`) and the P-well ({ref}`PWI <step-027>`)
  implants are added to. The "free" substrate-collector PNP described
  in the PDK device details uses the substrate directly as its
  collector (PDK-07).
* **Latch-up and noise isolation.** A lightly doped bulk substrate has
  a higher substrate resistance than a p/p⁺ epitaxial wafer, which
  historically made epi the choice for logic (ITRS-01: "high-performance
  logic ICs are generally manufactured on more costly epitaxial wafers
  … (e.g., latch-up suppression capability)"). The same roadmap notes
  that this "may no longer be as critical due to the use of shallow
  trench isolation (STI) and the development of alternate doping means
  for achieving latch-up suppression" (ITRS-01) — which is exactly the
  combination SKY130 uses: STI plus retrograde wells plus an optional
  deep N-well.
* **Defect density and gate-oxide integrity.** Crystal-originated
  particles, metallic contamination and surface micro-roughness of the
  incoming wafer propagate directly into gate-oxide yield; the ITRS
  starting-materials tables exist for this reason (ITRS-01).
* **Mechanical and thermal budget.** The 725 µm thickness and the
  oxygen content of a CZ wafer govern warpage through the high-
  temperature isolation and well steps that follow.

## How it is typically performed

For the fab, `SMAT` is a receiving and pre-processing operation rather
than a wafer-manufacturing one. A 200 mm, 130 nm-era CMOS fab would
typically:

1. **Specify the wafer to the vendor** — diameter 200 mm, thickness
   725 µm (WIKI-WAFER), p-type boron-doped CZ silicon, (100) surface
   orientation. Textbooks give (100) as the standard orientation for
   MOS devices because it yields the lowest Si/SiO₂ interface-state
   density, and describe lightly doped p-type substrates in the range
   of a few to a few tens of Ω·cm as the usual choice for a bulk CMOS
   process (TXT-01, TXT-03, TXT-07). These are industry-typical values
   and are **not** a SkyWater statement.
2. **Choose polished versus epitaxial.** The 2001 ITRS contrasts
   "lower cost Cz polished wafers" with "more costly epitaxial wafers",
   and states that "200 mm will still be prevalent through the 130 nm
   node" (ITRS-01). SkyWater's "Bulk" label for S130 (SKW-02) points to
   the polished option.
3. **Receive and inspect.** Incoming lots are checked against the
   specification: particle count and haze on an unpatterned-wafer laser
   scanner, resistivity by four-point probe or eddy current, flatness
   and thickness, and bow/warp (TXT-07).
4. **Mark and sort.** Each wafer is laser-scribed with a lot and wafer
   identifier near the notch so that it can be tracked through the
   flow; wafers are sorted into 25-wafer lots.
5. **Initial clean.** Before the first furnace step
   ({ref}`BOX <step-002>`) the wafers receive a standard RCA-type
   clean. The RCA sequence is SC-1 (NH₄OH : H₂O₂ : H₂O, typically
   1 : 1 : 5 at 75–80 °C for about 10 min), an optional dilute HF dip,
   and SC-2 (HCl : H₂O₂ : H₂O, 1 : 1 : 6 at 75–80 °C) (WIKI-RCA).

## Machines typically used

* **Crystal pullers, wire saws, lapping/polishing lines** — at the
  wafer vendor, not in the fab (WIKI-WAFER, TXT-07).
* **Unpatterned-wafer surface scanner** (laser light scattering) for
  incoming particle inspection; the KLA-Tencor Surfscan family was the
  200 mm-era standard.
* **Wafer laser marker / scribe** for identification.
* **Wafer sorter** for lot assembly and slot mapping.
* **Batch wet bench** for the RCA clean.

## Machines likely used at SkyWater

* **Laser scribe — Lumonics Superclean.** SKW-01 lists "Lumonics
  Superclean" under scribe. Strength: strong (a SkyWater statement),
  though the page does not say which step uses it.
* **Unpatterned-wafer inspection — KLA-Tencor SP1.** A SkyWater Defect
  Technician posting reads "General operation of semiconductor defect
  metrology tools: SEM/AIT/KLA/SP1/EV300/1X" (JOB-01). Strength: medium
  (a retrievable job posting).
* **Pre-furnace clean — DNS or FSI Mercury wet bench.** SKW-01 lists
  "DNS wet bench industry standard HF/SC1/SC2" and "FSI Mercury
  industry standard HF/SC1/SC2 rotational" under pre-clean. Strength:
  strong.
* **Wafers themselves — GlobalWafers and SEH America** (SEC-01,
  SEC-02), with GlobalWafers qualified for S8 at Fab 4 in 2015 (CYP-06).
  Strength: strong.

None of these sources states that the tool in question is the one used
at `SMAT`; the association is our inference from the tool's function.

## Resources required

* **Silicon wafers** — 200 mm, 725 µm, p-type CZ, polished
  (SKW-02, WIKI-WAFER).
* **Ultra-pure water** for rinsing.
* **SC-1 chemicals** — ammonium hydroxide, hydrogen peroxide.
* **SC-2 chemicals** — hydrochloric acid, hydrogen peroxide.
* **Dilute HF** for the optional native-oxide strip (WIKI-RCA).
* **Nitrogen** for drying and cassette purging.

SkyWater's filings name its chemical and gas suppliers (Air Products,
Praxair, KMG Chemicals in SEC-01; Linde, Airgas, EMD Performance
Materials in SEC-02) but do not tie any product to a step.

## Related steps and cross-references

* Next: {ref}`BOX <step-002>` grows the pad oxide on the cleaned wafer.
* The substrate doping is the background for {ref}`DNI <step-008>`,
  {ref}`NWI <step-018>` and {ref}`PWI <step-027>`.
* The wafer is finally characterised electrically at
  {ref}`HPETEST <step-171>`.
* Category page: {ref}`Substrate / starting material <category-substrate>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SKW-02** — SkyWater Technology, *Mixed-Signal CMOS & Read Out IC
  (ROIC)* platform table ("S130 … 200mm … Substrates: Bulk"), accessed
  2026-08-30. <https://www.skywatertechnology.com/cmos/>
* **SEC-01** — SkyWater Technology, Inc., Form S-1, filed 2021-03-22,
  "Raw Materials" section.
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
* **SEC-02** — SkyWater Technology, Inc., Form 10-K for fiscal 2023.
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
* **CYP-06** — Cypress Semiconductor, PIN152804, *Qualification of
  GlobalWafer Silicon Wafers for 250nm, 130nm and 90nm Technology
  Products at Cypress Fab 4*, 2015-07-12.
  <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
* **CYP-07** — Cypress Semiconductor Corp., Form 10-Q/A for Q1 2003.
  <https://www.sec.gov/Archives/edgar/data/0000791915/000120677403000508/d12840.htm>
* **PDK-04** — SkyWater PDK Authors, *Process stack diagram*
  (`metal_stack.svg`), "p-substrate" label.
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
* **PDK-07** — SkyWater PDK Authors, *Device Details* and the
  `nfet_01v8` cross-section drawing ("P-substrate", "Deep N-well").
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
* **PDK-10** — google/skywater-pdk README.
  <https://github.com/google/skywater-pdk>
* **JOB-01** — Indeed, SkyWater Technology Foundry listings,
  Bloomington MN (Defect Technician 2), retrieved 2026-08-30.
  <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>

### High-level understanding

* **WIKI-WAFER** — Wikipedia, *Wafer (electronics)*.
  <https://en.wikipedia.org/wiki/Wafer_(electronics)>
* **WIKI-RCA** — Wikipedia, *RCA clean*.
  <https://en.wikipedia.org/wiki/RCA_clean>
* **TXT-01** — J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon
  VLSI Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9
  (chapters on crystal growth and the CMOS process flow).
  <https://openlibrary.org/isbn/9780130850379>
* **TXT-03** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 2:
  Process Integration*, Lattice Press, 1990, ISBN 978-0-9616721-4-0
  (CMOS substrate choice and latch-up).
  <https://openlibrary.org/isbn/9780961672140>
* **TXT-07** — M. Quirk and J. Serda, *Semiconductor Manufacturing
  Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0 (wafer
  specification and incoming inspection).
  <https://openlibrary.org/isbn/9780130815200>

### Deep dive

* **ITRS-01** — *International Technology Roadmap for Semiconductors
  2001: Front End Processes*, "Starting Materials" section and Table
  "Starting Materials Technology Requirements".
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* **PAT-04** — K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress),
  US 8,796,098 B1, *Embedded SONOS based memory cells*, granted
  2014-08-05 — states the substrate "may be a bulk wafer … or may
  include a top epitaxial layer".
  <https://patents.google.com/patent/US8796098B1/en>

## Open questions

* **Resistivity and orientation.** No public source gives the SKY130
  wafer resistivity, boron concentration or surface orientation. The
  (100) orientation and few-to-tens-of-Ω·cm range above are textbook
  norms, not SkyWater data.
* **Bulk versus epitaxial.** SKW-02's "Bulk" entry is the only public
  statement and it is a marketing table written years after the S8
  flow was developed. Whether the original Cypress S8 wafer was
  polished CZ or a thin p/p⁻ epi wafer cannot be confirmed; the Cypress
  SONOS patent (PAT-04) deliberately allows both.
* **Wafer vendor at the time of development.** CYP-06 shows
  GlobalWafers being *added* in 2015 alongside "other qualified
  suppliers"; who the original supplier was is not public.
* **Incoming-inspection tooling.** The KLA SP1 reference (JOB-01) is a
  job posting, and the Lumonics scribe (SKW-01) is not tied to any
  step.
