(step-001)=
# Step 001 — SMAT: Starting material

| | |
|---|---|
| **Step number** | 1 of 171[^steps-sheet] |
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

* **Diameter.** SkyWater's Minnesota fab runs "200 mm
  equipment"[^skw-01] and its S130 platform table lists the wafer size
  as "200mm".[^skw-02] Cypress described Fab 4, where the 0.13 µm
  technology was ramped in 2003, as an "eight-inch wafer production
  facility".[^cyp-07] Wikipedia gives the standard 200 mm wafer
  thickness as 725 µm and notes that wafers of 200 mm and above carry
  "a single small notch to convey wafer orientation" rather than a
  flat.[^wiki-wafer]
* **Conductivity type.** The PDK process-stack drawing labels the
  bottom of the stack "p-substrate"[^pdk-04] and the 1.8 V NMOS
  cross-section drawing labels it "P-substrate".[^pdk-07] The wafer is
  therefore p-type (boron-doped).
* **Bulk, not epitaxial.** SkyWater's platform table gives the S130
  substrate as "Bulk", in contrast to the S90LN entry, which reads
  "4 µm EPI".[^skw-02] We read this as a polished bulk Czochralski ({term}`CZ`)
  wafer without an {term}`epitaxial layer`; see the open questions below.
* **Suppliers.** SkyWater's 2021 registration statement lists its
  principal silicon-wafer suppliers as "GlobalWafers Singapore Pte. Ltd.
  (silicon wafers)" and "SEH America, subsidiary of Shin-Etsu Handotai,
  Ltd. (silicon wafers)";[^sec-01] the 2023 annual report lists
  "Globalwafers Co. LTD." and "SEH America Inc, subsidiary of Shin-Etsu
  Handotai, Ltd." as the wafer suppliers.[^sec-02] In 2015 Cypress
  issued product-change notice
  PIN152804, "Qualification of GlobalWafer Silicon Wafers for 250nm,
  130nm and 90nm Technology Products at Cypress Fab 4", covering the
  "130nm C8/R8/S8/L8" families and stating that Cypress would use
  GlobalWafer wafers "in addition to wafers from other qualified
  suppliers".[^cyp-06] That notice is the clearest public link between
  a named wafer vendor and the S8 process that became SKY130.

Everything else about the wafer — resistivity, crystal orientation,
oxygen content, flatness grade — is not stated in any public SkyWater
or Cypress document and is discussed below as industry-typical.

## Step category

This is the only step in the
{ref}`Substrate / starting material <category-substrate>` category. What
is specific to SKY130 is that it is a *bulk* 200 mm p-type wafer for a
process that, unusually for a 130 nm-era logic technology, carries
5 V and 10–20 V devices, {term}`SONOS` memory and a deep N-well option on the
same substrate.[^pdk-07][^pdk-10]

## Why this step exists

The wafer specification fixes several things that the rest of the flow
depends on:

* **Substrate doping sets the baseline for every well.** The p-type
  background is what the N-well ({ref}`NWI <step-018>`), the deep N-well
  ({ref}`DNI <step-008>`) and the P-well ({ref}`PWI <step-027>`)
  implants are added to. The "free" substrate-collector PNP described
  in the PDK device details uses the substrate directly as its
  collector.[^pdk-07]
* **Latch-up and noise isolation.** A lightly doped bulk substrate has
  a higher substrate resistance than a p/p⁺ epitaxial wafer, which
  historically made epi the choice for logic (the 2001 ITRS:
  "high-performance logic ICs are generally manufactured on more costly
  epitaxial wafers … (e.g., latch-up suppression capability)"[^itrs-01]).
  The same roadmap notes that this "may no longer be as critical due to
  the implementation of shallow trench isolation (STI) and the
  development of alternate doping means for achieving latch-up
  suppression"[^itrs-01] — which is exactly the combination SKY130
  uses: {term}`STI` plus {term}`retrograde wells <retrograde well>` plus an optional deep N-well.
* **Defect density and {term}`gate-oxide integrity <gate oxide integrity>`.** Crystal-originated
  particles, metallic contamination and surface micro-roughness of the
  incoming wafer propagate directly into gate-oxide yield; the ITRS
  starting-materials tables exist for this reason.[^itrs-01]
* **Mechanical and {term}`thermal budget`.** The 725 µm thickness and the
  oxygen content of a CZ wafer govern warpage through the high-
  temperature isolation and well steps that follow.

## How it is typically performed

For the fab, `SMAT` is a receiving and pre-processing operation rather
than a wafer-manufacturing one. A 200 mm, 130 nm-era CMOS fab would
typically:

1. **Specify the wafer to the vendor** — diameter 200 mm, thickness
   725 µm,[^wiki-wafer] p-type boron-doped CZ silicon, (100) surface
   orientation. Textbooks give (100) as the standard orientation for
   MOS devices because it yields the lowest Si/SiO₂ interface-state
   density, and describe lightly doped p-type substrates in the range
   of a few to a few tens of Ω·cm as the usual choice for a bulk CMOS
   process.[^txt-01][^txt-03][^txt-07] These are industry-typical
   values and are **not** a SkyWater statement.
2. **Choose polished versus epitaxial.** The 2001 ITRS contrasts
   "lower cost Cz polished wafers" with "more costly epitaxial wafers",
   and states that "200 mm will still be prevalent through the 130 nm
   node".[^itrs-01] SkyWater's "Bulk" label for S130[^skw-02] points to
   the polished option.
3. **Receive and inspect.** Incoming lots are checked against the
   specification: particle count and haze on an unpatterned-wafer laser
   scanner, resistivity by {term}`four-point probe` or eddy current, flatness
   and thickness, and bow/warp.[^txt-07]
4. **Mark and sort.** Each wafer is laser-scribed with a lot and wafer
   identifier near the notch so that it can be tracked through the
   flow; wafers are sorted into 25-wafer lots.
5. **Initial clean.** Before the first furnace step
   ({ref}`BOX <step-002>`) the wafers receive a standard RCA-type
   clean. The RCA sequence is {term}`SC-1` (NH₄OH : H₂O₂ : H₂O, typically
   1 : 1 : 5 at 75–80 °C for about 10 min), an optional dilute HF dip,
   and {term}`SC-2` (HCl : H₂O₂ : H₂O, 1 : 1 : 6 at 75–80 °C).[^wiki-rca]

## Machines typically used

* **Crystal pullers, wire saws, lapping/polishing lines** — at the
  wafer vendor, not in the fab.[^wiki-wafer][^txt-07]
* **{ref}`Unpatterned-wafer surface scanner <machine-starting-material>`** ({ref}`laser light scattering <machine-defect-inspection>`) for
  incoming particle inspection; the KLA-Tencor Surfscan family was the
  200 mm-era standard.
* **{ref}`Wafer laser marker / scribe <machine-starting-material>`** for identification.
* **{ref}`Wafer sorter <machine-starting-material>`** for lot assembly and slot mapping.
* **{ref}`Batch wet bench <machine-wet-bench>`** for the {term}`RCA clean`.

## Machines likely used at SkyWater

* **Laser scribe — Lumonics Superclean.** SkyWater's capability list
  names "Lumonics Superclean" under scribe.[^skw-01] Strength: strong
  (a SkyWater statement), though the page does not say which step uses
  it.
* **Unpatterned-wafer inspection — KLA-Tencor SP1 (our reading).** A SkyWater Defect
  Technician posting reads "General operation of semiconductor defect
  metrology tools: SEM/AIT/KLA/SP1/EV300/1X";[^job-01] we read "SP1" as
  KLA-Tencor's Surfscan SP1, and the posting expands none of the
  abbreviations. Strength: medium
  (a job listing retrieved 2026-08-30; listings expire).
* **Pre-furnace clean — DNS or FSI Mercury wet bench.** SkyWater's
  capability list names "DNS wet bench industry standard HF/SC1/SC2"
  and "FSI Mercury industry standard HF/SC1/SC2 rotational" under
  pre-clean.[^skw-01] Strength: strong for existence; the assignment
  is an inference (below) from their HF/SC1/SC2 chemistry, SC-2 being
  listed only for these two benches.
* **Wafers themselves — GlobalWafers and SEH America**,[^sec-01][^sec-02]
  with GlobalWafers qualified for S8 at Fab 4 in 2015.[^cyp-06]
  Strength: strong.

None of these sources states that the tool in question is the one used
at `SMAT`; the association is our inference from the tool's function.

## Resources required

* **Silicon wafers** — 200 mm, 725 µm, p-type CZ,
  polished.[^skw-02][^wiki-wafer]
* **Ultra-pure water** for rinsing.
* **SC-1 chemicals** ({ref}`wet chemicals <material-wet-chemicals>`) — ammonium hydroxide, hydrogen peroxide.
* **SC-2 chemicals** — hydrochloric acid, hydrogen peroxide.
* **Dilute HF** for the optional native-oxide strip.[^wiki-rca]
* **Nitrogen** for drying and cassette purging.

SkyWater's filings name its chemical and gas suppliers (Air Products,
Praxair, KMG Chemicals in the 2021 S-1;[^sec-01] Linde, Airgas, EMD
Performance Materials in the fiscal 2023 10-K[^sec-02]) but do not tie
any product to a step.

## Related steps and cross-references

* Next: {ref}`BOX <step-002>` grows the pad oxide on the cleaned wafer.
* The substrate doping is the background for {ref}`DNI <step-008>`,
  {ref}`NWI <step-018>` and {ref}`PWI <step-027>`.
* The wafer is finally characterised electrically at
  {ref}`HPETEST <step-171>`.
* Category page: {ref}`Substrate / starting material <category-substrate>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "200 mm equipment", the
  Lumonics scribe and the DNS / FSI pre-clean benches.[^skw-01]
* SkyWater, *Mixed-Signal CMOS & ROIC* platform table — "S130 … 200mm …
  Substrates: Bulk".[^skw-02]
* SkyWater, Form S-1 (2021) — the "Raw materials." run-in paragraph
  naming the wafer, gas and chemical suppliers.[^sec-01]
* SkyWater, Form 10-K for fiscal 2023 — the updated supplier
  list.[^sec-02]
* Cypress, PIN152804 (2015) — GlobalWafers qualified for the
  "130nm C8/R8/S8/L8" families at Fab 4.[^cyp-06]
* Cypress, Form 10-Q/A for Q1 2003 — Fab 4 as an "eight-inch wafer
  production facility".[^cyp-07]
* SkyWater PDK, process stack diagram — the "p-substrate"
  label.[^pdk-04]
* SkyWater PDK, *Device Details* and the `nfet_01v8` cross-section
  drawing — "P-substrate", "Deep N-well", and the substrate-collector
  PNP.[^pdk-07]
* SkyWater PDK, *Criteria & Assumptions* — the "background
  concentration" among the n-well entries (variable `NWBCONC`) of its
  basic-parameters table.[^pdk-03]
* SKY130 raw-data repository — I–V sweeps of the 20 V zero-Vt NMOS on
  the test tile, from which the effective body doping quoted in the
  open questions is our extraction.[^raw-data-hv-mosfets]
* google/skywater-pdk README — the device and option list built on the
  one substrate.[^pdk-10]
* Indeed, SkyWater Defect Technician 2 posting — the
  "SEM/AIT/KLA/SP1/EV300/1X" tool list.[^job-01]

### High-level understanding

* Wikipedia, *Wafer (electronics)* — 200 mm wafer thickness and the
  notch convention.[^wiki-wafer]
* Wikipedia, *RCA clean* — SC-1 and SC-2 compositions and
  temperatures.[^wiki-rca]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — chapters on
  crystal growth and the CMOS process flow.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 2 — CMOS substrate
  choice and latch-up.[^txt-03]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — wafer
  specification and incoming inspection.[^txt-07]

### Deep dive

* ITRS 2001, *Front End Processes* — the "Starting Materials" section
  and its technology-requirements table: polished versus epitaxial,
  200 mm through the 130 nm node, defect and contamination
  limits.[^itrs-01]
* Ramkumar et al. (Cypress), US 8,796,098 — states that the substrate
  "may be a bulk wafer … or may include a top epitaxial layer", i.e. the
  Cypress SONOS flow deliberately allows both.[^pat-04]
* SEMI M1, *Specification for Polished Single Crystal Silicon Wafers* —
  the industry standard that defines the diameter, thickness, notch,
  flatness and resistivity classes a fab orders against.[^semi-m1]
* Shimura, *Semiconductor Silicon Crystal Technology* — the standard
  monograph on CZ growth, dopant and oxygen incorporation, and wafer
  characterisation.[^shimura-1989]
* Zulehner, *J. Crystal Growth* 1983 — a review of Czochralski silicon
  growth from the wafer-maker's side: melt, pulling, dopant and oxygen
  control.[^zulehner-1983]
* Falster and Voronkov, *Mater. Sci. Eng. B* 2000 — how vacancy- and
  interstitial-rich growth regimes are engineered to control
  crystal-originated defects in polished wafers.[^falster-2000]
* Ryuta et al., *Jpn. J. Appl. Phys.* 1990 — the paper that identified
  "crystal-originated singularities" (COPs) revealed by SC-1 cleaning,
  the defect class that gate-oxide yield depends on.[^ryuta-1990]
* Borghesi et al., *J. Appl. Phys.* 1995 — a review of oxygen
  precipitation in CZ silicon, the basis of internal {term}`gettering` and a
  driver of wafer warpage through the thermal budget.[^borghesi-1995]
* Kang and Schroder, *J. Appl. Phys.* 1989 — a review of gettering
  mechanisms (intrinsic and extrinsic) that a bulk-wafer process relies
  on to keep metals away from junctions.[^kang-1989]
* Troutman, *Latchup in CMOS Technology* — the monograph on why
  substrate resistance matters and how epitaxial substrates, guard
  rings and wells suppress latch-up.[^troutman-1986]
* Kern, *J. Electrochem. Soc.* 1990 — the history and chemistry of the
  RCA clean used as the incoming-wafer clean.[^kern-1990]

## Open questions

* **Resistivity and orientation.** No public source gives the SKY130
  wafer resistivity, boron concentration or surface orientation. The
  (100) orientation and few-to-tens-of-Ω·cm range above are textbook
  norms, not SkyWater data. Two indirect figures exist. The PDK's
  process assumptions give a "background concentration" of
  8 × 10¹⁴ cm⁻³ among the n-well entries (variable `NWBCONC`) of their
  basic-parameters table without saying that it is the wafer doping.[^pdk-03] And the 20 V zero-Vt NMOS, whose P-well and
  threshold implants are blocked,[^pdk-07] has a body-effect coefficient
  of about 0.07 √V on SkyWater's test tile, which with a uniform-doping
  model and the 11.3 nm electrical oxide thickness we extracted from the
  tile's C–V data corresponds to an effective body doping of about 1.4 × 10¹⁵ cm⁻³ (our extraction
  from the published measurements; see {ref}`PWBM <step-026>`).[^raw-data-hv-mosfets]
  Neither is a wafer specification, and neither gives the orientation.
* **Bulk versus epitaxial.** SkyWater's "Bulk" entry[^skw-02] is the
  only public statement and it is a marketing table written years
  after the S8 flow was developed. Whether the original Cypress S8
  wafer was polished CZ or a thin p/p⁻ epi wafer cannot be confirmed;
  the Cypress SONOS patent deliberately allows both.[^pat-04]
* **Wafer vendor at the time of development.** The 2015 Cypress notice
  shows GlobalWafers being *added* alongside "other qualified
  suppliers";[^cyp-06] who the original supplier was is not public.
* **Incoming-inspection tooling.** The KLA SP1 is our reading of a job
  posting that expands none of its abbreviations,[^job-01] and the Lumonics scribe[^skw-01] is not tied to any
  step.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-08-30. <https://www.skywatertechnology.com/cmos/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^cyp-06]: Cypress Semiconductor, Product Information Notification
    PIN152804, *Qualification of GlobalWafer Silicon Wafers for 250nm,
    130nm and 90nm Technology Products at Cypress Fab 4*, 2015-07-12
    (copy hosted by Future Electronics). <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^cyp-07]: Cypress Semiconductor Corp., Form 10-Q/A for Q1 2003.
    <https://www.sec.gov/Archives/edgar/data/0000791915/000120677403000508/d12840.htm>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository. <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page; Defect Technician 2 posting),
    retrieved 2026-08-30; listings expire. <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
[^wiki-wafer]: Wikipedia, *Wafer (electronics)*.
    <https://en.wikipedia.org/wiki/Wafer_(electronics)>
[^wiki-rca]: Wikipedia, *RCA clean*. <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9. <https://openlibrary.org/isbn/9780130850379>
[^txt-03]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 2:
    Process Integration*, Lattice Press, 1990, ISBN 978-0-9616721-4-0.
    <https://openlibrary.org/isbn/9780961672140>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
[^semi-m1]: SEMI, *SEMI M1 — Specification for Polished Single Crystal
    Silicon Wafers*, SEMI Standards store listing.
    <https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>
[^shimura-1989]: F. Shimura, *Semiconductor Silicon Crystal Technology*,
    Academic Press, 1989, ISBN 978-0-12-640045-8.
    <https://openlibrary.org/isbn/9780126400458>
[^zulehner-1983]: W. Zulehner, "Czochralski growth of silicon",
    *Journal of Crystal Growth* **65**(1–3), 189–213 (1983).
    <https://doi.org/10.1016/0022-0248(83)90051-9>
[^falster-2000]: R. Falster and V. V. Voronkov, "The engineering of
    intrinsic point defects in silicon wafers and crystals", *Materials
    Science and Engineering: B* **73**(1–3), 87–94 (2000).
    <https://doi.org/10.1016/S0921-5107(99)00439-0>
[^ryuta-1990]: J. Ryuta, E. Morita, T. Tanaka and Y. Shimanuki,
    "Crystal-Originated Singularities on Si Wafer Surface after SC1
    Cleaning", *Japanese Journal of Applied Physics* **29**(11A), L1947
    (1990). <https://doi.org/10.1143/JJAP.29.L1947>
[^borghesi-1995]: A. Borghesi, B. Pivac, A. Sassella and A. Stella,
    "Oxygen precipitation in silicon", *Journal of Applied Physics*
    **77**(9), 4169–4244 (1995). <https://doi.org/10.1063/1.359479>
[^kang-1989]: J. S. Kang and D. K. Schroder, "Gettering in silicon",
    *Journal of Applied Physics* **65**(8), 2974–2985 (1989).
    <https://doi.org/10.1063/1.342714>
[^troutman-1986]: R. R. Troutman, *Latchup in CMOS Technology: The
    Problem and Its Cure*, Kluwer Academic Publishers, 1986,
    ISBN 978-0-89838-215-7. <https://doi.org/10.1007/978-1-4757-1887-4>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^raw-data-hv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 5 V, 10/16 V and
    20 V transistors, the native, zero-Vt and ESD NMOS and the thick-oxide
    gate capacitors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_g5v0d10v5`, `pfet_g5v0d10v5`, `nfet_g5v0d16v0`,
    `pfet_g5v0d16v0`, `nfet_g5v0d20v0`, `pfet_g5v0d20v0`,
    `nfet_03v3_nvt`, `nfet_05v0_nvt`, `nfet_20v0_nvt`, `esd_nfet_01v8`,
    `esd_nfet_g5v0d10v5`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
