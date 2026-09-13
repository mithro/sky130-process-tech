(step-039)=
# Step 039 — TUNME: Tunnel mask etch

| | |
|---|---|
| **Step number** | 39 of 171[^steps-sheet] |
| **Step code** | `TUNME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | FEOL — SONOS and gate dielectrics |
| **Previous step** | {ref}`DEPI <step-038>` |
| **Next step** | {ref}`ONO <step-040>` |

## What this step is

`TUNME` removes the oxide — we infer the pad oxide from
{ref}`BOX <step-002>` — from the tunnel windows so that the {term}`tunnel oxide`
of the {term}`SONOS` memory transistor can be grown on bare silicon at the next
step, {ref}`ONO <step-040>`. The resist patterned at
{ref}`TUNM <step-035>` — opened through its {term}`ARC` at
{ref}`TUNARCE <step-036>` and just used as the mask for the
{ref}`PTSI <step-037>` and {ref}`DEPI <step-038>` implants — now serves
a third time, as the mask for an oxide etch that we infer to be wet: the
Cypress patent uses HF chemistry,[^pat-04] and a plasma would damage the
silicon. Inside each window the oxide — the pad oxide, we infer;
10–20 nm in the Cypress patent[^pat-04] — is dissolved in dilute
hydrofluoric acid or buffered HF down to the silicon; outside the
windows the resist keeps the oxide intact.

The Cypress embedded-SONOS patent describes exactly this operation on
the way to its tunnel dielectric: a "patterned tunnel mask 220 is
formed on or overlying the pad oxide 209", the memory-transistor
channel is implanted "through a window or opening in the tunnel
mask", and then "The pad oxide 209 is removed, for example in a wet
clean process using a 10:1 buffered oxide etch (BOE) containing a
surfactant. Alternatively, the wet clean process can be performed
using a 20:1 BOE wet etch, a 50:1 hydrofluoric (HF) wet etch, a pad
etch, or any other similar hydrofluoric-based wet etching
chemistry."[^pat-04] The same patent notes that "A photoresist tunnel
mask 220 can be ashed or stripped using oxygen plasma."[^pat-04]

This reference treats the resist strip (by oxygen-plasma ash in the
Cypress patent[^pat-04]) and the pre-oxidation clean as the tail of
this step; they could equally be the head of the next. The sequence
below includes them.

## Step category

`TUNME` is an {ref}`Etch <category-etch>` step of the (inferred) *wet
oxide etch* type — the same class as {ref}`GOXETCH <step-046>` and
{ref}`SACETCH <step-095>`. The category page explains the choice: dilute
HF is used where a thin oxide must be removed "cleanly and gently with
very high selectivity … because a plasma would damage the exposed
silicon". Here the silicon being exposed will carry a tunnel oxide only
1–3 nm thick[^pat-04] whose quality decides the memory's endurance and
retention, so the etch is the gentlest available.

## Why this step exists

The tunnel oxide is the thinnest and most critical film in the SONOS
cell: the Cypress patents put it at "less than about 25 Å"[^pat-01] and
"from about 15 Å to about 22 Å",[^pat-02] and it has to pass
programming current by {term}`Fowler–Nordheim tunnelling` for 100 000 cycles
(the PDK guarantees "100K cycles")[^pdk-07] while blocking leakage for
years. Three things follow:

* **It must be grown, not left over.** A 10–20 nm[^pat-04] pad oxide
  that has been implanted through several times, plasma-exposed at
  {ref}`TUNARCE <step-036>`, and thinned by successive resist strips is
  not a tunnel oxide. Cypress's integration patent quantifies the
  damage: "approximately 0.5 nm of silicon dioxide may be removed during
  a conventional post-implant resist strip process", more "if the
  silicon dioxide received an implant", so that "between 1.5 nm and
  2.5 nm of silicon dioxide may be removed" over a flow's worth of
  implants.[^pat-03] The pad oxide must go, and a fresh oxide must be
  grown on clean crystal.
* **It must be removed only where the cells are.** Elsewhere the
  (inferred) pad oxide would continue to serve as the base on which the
  nitride of the {term}`ONO` stack will sit and be removed again
  ({ref}`ONOME <step-042>`), and as a protective layer over the logic
  silicon until the gate-oxide pre-clean. A masked etch does this; a
  blanket strip would not.
* **The surface must be perfect.** HF etching leaves silicon
  hydrogen-terminated and smooth;[^cerofolini-1998][^kern-1990] a
  plasma etch would leave a damaged, roughened surface that the tunnel
  oxide would inherit.

Without `TUNME` the tunnel oxide would be grown on top of the pad oxide,
giving a "tunnel" dielectric of 12–23 nm (the patent's ranges[^pat-04])
through which nothing would tunnel at the PDK's ±10.5 V programme/erase
conditions.[^pdk-07]

## How it is typically performed

An industry-generic masked pad-oxide removal for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

1. **Wet etch with resist in place.** Dilute HF (50:1 to 100:1) or
   surfactant-containing BOE in a wet bench or single-wafer spray tool.
   A 6:1 BOE etches thermal oxide at "approximately 2 nanometres per
   second at 25 degrees Celsius"[^wiki-boe] — far too fast to control
   for a 10–20 nm film — so more dilute chemistries with rates of
   typically a few nanometres per minute are used;[^kikuyama-1994] the
   etch rate scales with the HF and HF₂⁻ concentrations,[^judge-1971]
   and at very low concentrations the dissociation state of the acid
   controls the rate and the surface left behind.[^kikuyama-1994] A
   surfactant helps the liquid wet 0.4 µm windows in hydrophobic resist;
   Cypress specifies "a 10:1 buffered oxide etch (BOE) containing a
   surfactant".[^pat-04] The resist is not attacked by HF.
2. **{term}`Over-etch <over-etch>` and undercut.** The etch is timed for the oxide
   thickness plus an over-etch to clear thickness variation; being
   isotropic, it undercuts the resist edge by roughly the oxide
   thickness plus over-etch — tens of nanometres, small against the
   0.095 µm `tunm`
   extension beyond the gate (tunm.3).[^pdk-periph] Etch-rate test
   wafers track bath ageing ({ref}`category-etch`).
3. **Rinse and dry.** DI-water rinse; the freshly exposed silicon is
   hydrophobic.
4. **Resist strip.** The resist has seen two light implants and one
   plasma. An oxygen (or O₂/N₂, O₂/forming-gas) downstream {term}`ash` — "A
   photoresist tunnel mask 220 can be ashed or stripped using oxygen
   plasma"[^pat-04] — followed by a sulphuric-peroxide ({term}`SPM`) wet strip
   ({ref}`category-strip`). The ash regrows a thin oxide on the exposed
   silicon, which the next clean removes.
5. **Pre-oxidation clean.** An RCA-type sequence — {term}`SC-1` for particles
   and organics, {term}`SC-2` for metals[^wiki-rca] — with an HF-last or a
   deliberately grown chemical oxide as the final surface. The choice
   matters for a tunnel oxide of the 1.5–3 nm class the Cypress patents
   describe:[^pat-04] the Cypress patents describe SC-1 at "50 to 80° C.
   for about 10 minutes" and SC-2 as "a 1:1:10 solution of HCl, H₂O₂ and
   H₂O at about 50 to 80° C.",[^pat-04] and one of them replaces SC-1
   with "an ozonated water cleaning regime" in places where the ONO
   stack is exposed.[^pat-03] The room-temperature alternatives to the
   hot RCA sequence are reviewed by Ohmi.[^ohmi-1996]
6. **Queue time.** Wafers go to the tunnel oxidation promptly, because
   native oxide and airborne contamination grow on bare silicon within
   hours (industry practice; Reinhardt and Reidy[^reinhardt-2010]).

## Machines typically used

* **Automated wet bench** with dilute-HF/BOE, SPM, SC-1 and SC-2
  tanks and a rinser/dryer (Akrion, DNS/SCREEN, SCP), or a **spray
  processor** (FSI Mercury), or a **single-wafer wet tool** (SEZ, Lam
  DaVinci) ({ref}`category-etch`, {ref}`category-strip`).
* **Downstream asher** for the strip (Gasonics, Mattson, Axcelis/Fusion).
* **Ellipsometer** on monitor wafers for etch-rate control; **particle
  scanner** after the clean.

## Machines likely used at SkyWater

* **Akrion Gamma batch wet bench** — listed with "Sulfuric, SC1,
  phosphoric, BOE, spin or IPA dry".[^skw-01] BOE is the chemistry the
  Cypress patent names for this etch.[^pat-04] Strength: **strong** for
  the tool; **inference** for the assignment.
* **DNS wet bench** — "industry standard HF/SC1/SC2" and "dilute
  HF-last with IPA dry"[^skw-01] — the natural home of the pre-oxidation clean.
  Strength: strong for existence; inference for assignment.
* **FSI Mercury** ("HF/SC1/SC2 rotational") and **SEZ 223 / DaVinci
  single-wafer** ("HF, DSP+HF, titration controlled").[^skw-01]
  Strength: strong for existence; a SkyWater technician profile names
  the "SEZ etcher tool".[^skw-07]
* **Gasonics PEP, Iridia and Mattson Aspen 2 ashers**[^skw-01] for the
  strip. Strength: strong for existence.

## Resources required

* **Hydrofluoric acid (49 %)** diluted to 50:1–100:1, or **buffered
  oxide etch** (NH₄F/HF) with **surfactant**;[^pat-04][^wiki-boe]
  {term}`BOE` is on SkyWater's Akrion list.[^skw-01]
* **Sulphuric acid and hydrogen peroxide** (SPM), **ammonium
  hydroxide** (SC-1), **hydrochloric acid** (SC-2),[^wiki-rca]
  **ozone** if an ozonated-water clean is used.[^pat-03]
* **Oxygen, nitrogen, {term}`forming gas`** for the ash.[^skw-01]
* **Ultrapure DI water**, **isopropanol** for drying, **nitrogen**.
* SkyWater names KMG Chemicals and EMD Performance Materials among
  its chemical suppliers.[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`DEPI <step-038>` (last implant through the window);
  mask: {ref}`TUNM <step-035>`; ARC open: {ref}`TUNARCE <step-036>`.
* Next: {ref}`ONO <step-040>` grows the tunnel oxide on the cleared
  silicon.
* The same wet chemistry later strips the thick gate oxide from the
  1.8 V regions ({ref}`GOXETCH <step-046>`) and the sacrificial oxide
  before silicidation ({ref}`SACETCH <step-095>`).
* The oxide being removed is, we infer, the pad oxide grown at
  {ref}`BOX <step-002>`.
* Category pages: {ref}`Etch <category-etch>`,
  {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  tunnel mask, the BOE/HF pad-oxide removal, the oxygen-plasma strip,
  the SC-1/SC-2 conditions and the tunnel-oxide thickness.[^pat-04]
* Koutny et al. (Cypress), US 8,093,128 — oxide loss per resist
  strip, and the ozonated-water alternative to SC-1.[^pat-03]
* Ramkumar et al. (Cypress), US 6,969,689 and Levy et al. (Cypress),
  US 2009/0179253 — tunnel-oxide thickness ranges.[^pat-01][^pat-02]
* SkyWater PDK, *Device Details* — programme/erase voltages and the
  100K-cycle endurance.[^pdk-07]
* SkyWater PDK, *Periphery rules* — tunm.3.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — Akrion, DNS, FSI and SEZ wet
  tools; ashers.[^skw-01]
* SkyWater, *A Day in the Life of a SkyWater Maintenance Technician*
  — the SEZ etcher.[^skw-07]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]

### High-level understanding

* Wikipedia, *Buffered oxide etch* — BOE composition and etch
  rate.[^wiki-boe]
* Wikipedia, *RCA clean* — SC-1 and SC-2.[^wiki-rca]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  wet etching and wafer cleaning.[^txt-02]

### Deep dive

* Judge, *J. Electrochem. Soc.* 1971 — the dissolution kinetics of
  SiO₂ in acidic fluoride solutions.[^judge-1971]
* Kikuyama et al., *J. Electrochem. Soc.* 1994 — dissociation state
  and etching reaction of extremely dilute HF.[^kikuyama-1994]
* Monk, Soane and Howe, *J. Electrochem. Soc.* 1994 — HF etching of
  silicon dioxide, experiments and model.[^monk-1994]
* Cerofolini, *Appl. Surf. Sci.* 1998 — how HF etching leaves
  hydrogen-terminated silicon.[^cerofolini-1998]
* Kern, *J. Electrochem. Soc.* 1990 — the evolution of wafer cleaning
  and the RCA sequence.[^kern-1990]
* Ohmi, *J. Electrochem. Soc.* 1996 — room-temperature wet cleaning
  as an alternative to hot RCA.[^ohmi-1996]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — pre-gate cleans and post-implant strips.[^reinhardt-2010]
* Fujimura et al., *Jpn. J. Appl. Phys.* 1989 — ashing of
  ion-implanted resist.[^fujimura-1989]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — low-temperature
  stripping of implanted resist.[^pat-strip-mosel]
* Koutny et al. (Cypress), US 8,093,128 — why HF and SC-1 cleans are
  restricted once the ONO stack exists.[^pat-03]

## Open questions

* That the oxide under the resist/nitride is the pad oxide from
  {ref}`BOX <step-002>` rather than a later sacrificial oxide is
  inferred; its retention after {ref}`NS19 <step-013>` is not public.
* Whether the pad oxide is removed only inside the tunnel windows or
  everywhere after the resist is stripped is an open question; this
  page describes a masked etch, and the Cypress patent text can be
  read either way.[^pat-04]
* Where the resist strip and the pre-oxidation clean sit — in this
  step or in {ref}`ONO <step-040>` — is not stated publicly; this page
  treats them as part of this step.
* The HF dilution, etch time, over-etch and final surface state
  (HF-last or chemical oxide) are not public.

<!-- footnotes -->

[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^pat-01]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster
    (Cypress Semiconductor), *Method of manufacturing an
    oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*,
    US 6,969,689 B1, granted 2005-11-29.
    <https://patents.google.com/patent/US6969689B1/en>
[^pat-02]: S. Levy, K. Ramkumar, F. Jenne and S. Geha (Cypress
    Semiconductor), *Oxide-nitride-oxide stack having multiple
    oxynitride layers*, US 2009/0179253 A1, published 2009-07-16.
    <https://patents.google.com/patent/US20090179253A1/en>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^cerofolini-1998]: G. F. Cerofolini, "A study of the ionic route for
    hydrogen terminations resulting after SiO₂ etching by concentrated
    aqueous solutions of HF", *Applied Surface Science* **133**(1–2),
    108–114 (1998). <https://doi.org/10.1016/S0169-4332(98)00182-2>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^wiki-boe]: Wikipedia, *Buffered oxide etch*.
    <https://en.wikipedia.org/wiki/Buffered_oxide_etch>
[^judge-1971]: J. S. Judge, "A Study of the Dissolution of SiO₂ in
    Acidic Fluoride Solutions", *Journal of The Electrochemical
    Society* **118**(11), 1772 (1971). <https://doi.org/10.1149/1.2407835>
[^kikuyama-1994]: H. Kikuyama, M. Waki, M. Miyashita, T. Yabune,
    N. Miki, J. Takano and T. Ohmi, "A Study of the Dissociation State
    and the SiO₂ Etching Reaction for HF Solutions of Extremely Low
    Concentration", *Journal of The Electrochemical Society* **141**(2),
    366–374 (1994). <https://doi.org/10.1149/1.2054733>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^wiki-rca]: Wikipedia, *RCA clean*. <https://en.wikipedia.org/wiki/RCA_clean>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14. <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^monk-1994]: D. J. Monk, D. S. Soane and R. T. Howe, "Hydrofluoric
    Acid Etching of Silicon Dioxide Sacrificial Layers: I. Experimental
    Observations" and "II. Modeling", *Journal of The Electrochemical
    Society* **141**(1), 264–269 and 270–274 (1994).
    <https://doi.org/10.1149/1.2054696>, <https://doi.org/10.1149/1.2054697>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
