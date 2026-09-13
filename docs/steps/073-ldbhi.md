(step-073)=
# Step 073 — LDBHI: LD B halo implant

| | |
|---|---|
| **Step number** | 73 of 171[^steps-sheet] |
| **Step code** | `LDBHI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`LDASTI <step-072>` |
| **Next step** | {ref}`LDASTIS <step-074>` |

## What this step is

`LDBHI` is the boron {term}`halo` implant of the {term}`SONOS` memory
transistors — the counterpart of {ref}`BHI <step-066>` made through the
{ref}`LDNTM <step-071>` resist after the lightly doped arsenic tip of
{ref}`LDASTI <step-072>`. A tilted boron beam places p-type {term}`pockets <pocket>`
around the memory transistor's tips, on the channel side of each
junction, self-aligned to the control-gate line. In this reference a
halo is described only with the `NTM` and `LDNTM` tips; the 5 V tip
({ref}`HVASTI <step-069>`) is described without one. The resist is removed at
{ref}`LDASTIS <step-074>` and every tip and halo of the module is
annealed at {ref}`TIPRTAD <step-075>`.

Species beyond "B", energy, dose, tilt and rotation are not public.
What distinguishes this halo from the logic halo is its host: a
transistor whose channel was set by its own {term}`punch-through stopper <punch-through>`
({ref}`PTSI <step-037>`) and depletion implant ({ref}`DEPI <step-038>`),
whose gate is poly over an {term}`ONO` stack, and whose tip is lightly doped
and, we infer, non-amorphising ({ref}`LDASTI <step-072>`).

## Step category

`LDBHI` is an {ref}`Ion implantation <category-implant>` step of the
*channel-engineering* class — boron at tens of keV and 10¹²–10¹³ cm⁻²
(typical)[^txt-01] at a tilt — placed by the gate geometry rather than
by a mask edge. It is the second of the two halo implants in the flow
and the last implant of the tip module.

## Why this step exists

The memory transistor needs a halo for the same reason the logic NMOS
does — Codella and Ogura's original purpose of holding the threshold up
as the channel shortens[^codella-1985] — and needs it more, for two
reasons:

* **Its tip is lightly doped.** A graded, lightly doped {term}`extension`
  ({ref}`LDASTI <step-072>`) has a longer depletion tail into the
  channel than an abrupt logic tip, so the drain's field reaches
  further under the gate; without a pocket the cell's threshold would
  roll off steeply across the 0.15–0.22 µm gate lengths of the two cell
  variants.[^pdk-07]
* **Its surface channel must stay lightly doped.** Cypress's own
  account of scaling the cell stresses "reduction of dopants in the
  surface of the channel" and "use of deeper channel implants with
  heavier species such as Indium … so as to keep surface dopant
  concentrations low",[^cyp-25] and the cell's depletion implant
  ({ref}`DEPI <step-038>`) makes the surface lightly doped by design.
  A halo is the way to add short-channel control *only at the ends* of
  the channel while leaving the middle alone — the same logic that
  Taur, Wann and Frank formalised as the super-halo.[^taur-1998]

A halo in a non-volatile cell also sets its disturb margins: a
programmed cell's threshold and an erased cell's leakage both depend on
how the pocket doping and the tip meet under the gate edge, and on how
much the anneal moves the boron. The {term}`reverse short-channel effect` —
threshold rising at short lengths through boron pile-up near the
junctions[^lu-1989-rsce][^rafferty-1993][^machala-1997] — is present here as
in logic and is absorbed into the cell's threshold targets.

Without `LDBHI`, the memory transistor would have to rely on its
punch-through stopper alone for short-channel control, and the lightly
doped tip would leave it with an unacceptable threshold roll-off at
the shorter cell.

## How it is typically performed

An industry-generic halo implant for a lightly doped, non-amorphised
extension, 200 mm, 130 nm era (SKY130's values are not public):

* **Species and source.** ¹¹B⁺ from BF₃, or BF₂⁺ for shallower
  placement;[^wiki-bf3][^txt-01] indium is the heavy alternative for a
  steeper pocket,[^shahidi-1993] which Cypress's article favours for
  the cell's channel,[^cyp-25] but SkyWater lists no indium
  source.[^skw-01]
* **Energy and dose.** Tens of keV and 10¹²–10¹³ cm⁻²
  (typical);[^txt-01] an AMD channel-engineering patent of the era
  gives "approximately 10-20 KeV for boron or 45-90 KeV for BF₂ at a
  concentration of about 1.0 to 2.5×10¹³ ions/cm²" for a channel
  implant,[^pat-vt-amd] and a halo sits in the same range.
* **Tilt and rotation.** Large tilt with two or four rotations to make
  the pocket symmetric[^pat-quad-tsmc] (20–45° is typical[^txt-04]); in
  the dense memory array the neighbouring control-gate lines {term}`shadow <shadowing>` a
  tilted beam,[^chen-1995] so the tilt and the array pitch are chosen
  together. The tilt is not public.
* **{term}`Channelling <channelling>`.** Because the lightly doped tip does not amorphise
  the surface (inference from an LDD-class dose), the boron enters
  crystalline silicon and is more prone to channelling than the logic
  halo; the twist, the {term}`screen oxide` and the tilt itself are the
  countermeasures.[^wiki-implant] Its damage is sub-amorphising point
  defects, the "+1" interstitials that drive transient enhanced
  diffusion of the boron itself during the anneal,[^eaglesham-1994]
  which is why a fast, hot {ref}`TIPRTAD <step-075>` matters as much
  here as for the logic halo.[^stolk-1997][^agarwal-1999]
* **Charge control and cooling.** Electron shower and electrostatic
  chuck ("ESC chuck, E shower" on SkyWater's medium-current
  tool);[^skw-01] platen cooling is industry practice.
* **Monitoring.** Thermal-wave measurement and tilt-angle
  calibration.[^smith-1985]

## Machines typically used

* **{ref}`Medium-current ion implanter <machine-medium-current-implanter>`**, 200 mm, single-wafer with a
  tilting, rotating platen: Axcelis (Eaton) 8250 class, Varian
  E220/E500 and VIISta 810, Applied Materials xR LEAP
  ({ref}`category-implant`); the 8250HT covers "3keV to 750keV" with
  beam currents "between 4µA and 3,500µA".[^axcelis-8250]
* **Thermal-wave** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter.** SkyWater lists "Axcelis
  8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14,
  0-60 deg tilt".[^skw-01] Boron and BF₂, the halo dose window and a
  tilt range to 60°. Strength: **strong** for the tool; **inference**
  for the assignment to `LDBHI`, as for {ref}`BHI <step-066>`.
* **Axcelis GSD implanters (high-current/high-energy and
  high-dose)**[^skw-01] — batch tools listed with "tilt/twist" capability;
  possible, less natural for a low-dose halo. Strength: strong for
  existence; weak for assignment.

## Resources required

* **Boron trifluoride (BF₃)** for ¹¹B⁺ or BF₂⁺.[^wiki-bf3]
* **Source-support gases**, source consumables, high-purity
  **nitrogen** for venting.
* **Helium** for platen cooling; **liquid nitrogen** or cryopump
  regeneration.
* **Monitor wafers**.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LDASTI <step-072>` (the lightly doped tip this halo
  surrounds); mask: {ref}`LDNTM <step-071>`.
* Next: {ref}`LDASTIS <step-074>` (strip), then
  {ref}`TIPRTAD <step-075>` (activation of all tips and halos).
* The logic halo: {ref}`BHI <step-066>`; the memory transistor's other
  channel implants: {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater PDK, *Device Details* — SONOS cell W/L, programme/erase
  conditions.[^pdk-07]
* SkyWater PDK, *Layers Reference* — `ldntm` "N-tip implant on SONOS
  devices".[^pdk-06]
* SkyWater, *Facilities & Capabilities* — the Axcelis 8250 species,
  dose and "0-60 deg tilt"; no indium listed.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* Ramkumar, Prabhakar and Kapre (Cypress), Semiconductor Digest —
  low surface doping and deeper, heavier channel implants for the
  cell.[^cyp-25]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  tool class.[^axcelis-8250]
* Krivokapic and Milic (AMD), US 6,238,982 — era-typical boron and BF₂
  channel-implant energies and doses.[^pat-vt-amd]

### High-level understanding

* Wikipedia, *Ion implantation* — tilt, channelling and
  damage.[^wiki-implant]
* Wikipedia, *Boron trifluoride* — the boron source gas.[^wiki-bf3]
* Wikipedia, *SONOS* — the cell.[^wiki-sonos]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — halo and
  pocket engineering.[^txt-04]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — implantation
  and {term}`TED`.[^txt-01]
* Taur and Ning, *Fundamentals of Modern VLSI Devices* — non-uniform
  channel doping and short-channel thresholds.[^taur-2009]

### Deep dive

* Codella and Ogura (IBM), IEDM 1985 — the original halo.[^codella-1985]
* Hori and Kurimoto, *IEEE EDL* 1988 — the large-tilt punch-through
  stopper.[^hori-1988]
* Taur, Wann and Frank (IBM), IEDM 1998 — super-halo design: pockets
  at the channel ends, light doping in between.[^taur-1998]
* Lu and Sung, *IEEE EDL* 1989 — the reverse short-channel
  effect.[^lu-1989-rsce]
* Rafferty et al. (AT&T), IEDM 1993 — its explanation by defect
  gradients.[^rafferty-1993]
* Machala et al. (TI), SISPAD 1997 — boron segregation and TED in the
  reverse short-channel effect.[^machala-1997]
* Shahidi et al. (IBM), *IEEE EDL* 1993 — indium for steep p-type
  profiles.[^shahidi-1993]
* Eaglesham et al., *Appl. Phys. Lett.* 1994 — the "+1" interstitial
  source of boron TED after sub-amorphising implants.[^eaglesham-1994]
* Stolk et al. (Bell Labs), *J. Appl. Phys.* 1997 — the physics of
  transient enhanced diffusion.[^stolk-1997]
* Agarwal, Gossmann and Fiory, *J. Electron. Mater.* 1999 — ramp rate
  and boron junction movement, the case for a {term}`spike anneal`.[^agarwal-1999]
* White, Adams and Bu, *IEEE Circuits & Devices* 2000 — SONOS cell
  operation and the disturb mechanisms the pocket affects.[^pap-01]
* Chen et al., *Solid-State Electronics* 1995 — shadowing of tilted
  implants by neighbouring gates.[^chen-1995]
* Pan (Chartered), US 5,595,919 — a self-aligned halo with limited
  junction-capacitance penalty.[^pat-halo-chartered]
* Lin, Yoo and Liang (TSMC), US 5,372,957 — multiple tilted-angle
  implantation with rotation.[^pat-quad-tsmc]
* Hwang (Goldstar), US 5,364,807 — an {term}`LDD` transistor with a halo
  punch-through stopper.[^pat-halo-goldstar]
* Yu (AMD), US 6,630,385 — differential halo implants and
  anneals.[^pat-halo-amd-diff]

## Open questions

* The halo species (B⁺ or BF₂⁺), energy, dose, tilt and rotations are
  not public, as is whether they differ from the logic halo's.
* Whether the lightly doped tip leaves the surface crystalline, and
  hence how much channelling and TED this halo sees, is an inference
  from LDD-typical doses.
* Whether the select transistor of the {term}`2-T cell` receives this halo is
  not public.
* How the halo, the punch-through stopper and the depletion implant
  combine to set the erased and programmed thresholds is not
  described publicly beyond the PDK's threshold targets.[^pdk-07]

<!-- footnotes -->

[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (AMD), *Multiple threshold
    voltage semiconductor device fabrication technology*, US 6,238,982
    B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-bf3]: Wikipedia, *Boron trifluoride*.
    <https://en.wikipedia.org/wiki/Boron_trifluoride>
[^wiki-sonos]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^shahidi-1993]: G. G. Shahidi, B. Davari, T. J. Bucelot, P. A.
    Ronsheim, P. J. Coane, S. Pollack, C. R. Blair, B. Clark and H. H.
    Hansen, "Indium channel implant for improved short-channel behavior
    of submicrometer NMOSFETs", *IEEE Electron Device Letters*
    **14**(8), 409–411 (1993). <https://doi.org/10.1109/55.225595>
[^codella-1985]: C. F. Codella and S. Ogura, "Halo doping effects in
    submicron DI-LDD device design", *IEDM 1985 Technical Digest*,
    pp. 230–233. <https://doi.org/10.1109/IEDM.1985.190938>
[^hori-1988]: T. Hori and K. Kurimoto, "A new p-channel MOSFET with
    large-tilt-angle implanted punchthrough stopper (LATIPS)", *IEEE
    Electron Device Letters* **9**(12), 641–643 (1988).
    <https://doi.org/10.1109/55.20422>
[^taur-1998]: Y. Taur, C. H. Wann and D. J. Frank, "25 nm CMOS design
    considerations", *IEDM 1998 Technical Digest*, pp. 789–792.
    <https://doi.org/10.1109/IEDM.1998.746474>
[^lu-1989-rsce]: C.-Y. Lu and J. M. Sung, "Reverse short-channel effects on
    threshold voltage in submicrometer salicide devices", *IEEE
    Electron Device Letters* **10**(10), 446–448 (1989).
    <https://doi.org/10.1109/55.43095>
[^rafferty-1993]: C. S. Rafferty, H.-H. Vuong, S. A. Eshraghi, M. D.
    Giles, M. R. Pinto and S. J. Hillenius, "Explanation of reverse
    short channel effect by defect gradients", *IEDM 1993 Technical
    Digest*, pp. 311–314. <https://doi.org/10.1109/IEDM.1993.347345>
[^machala-1997]: C. Machala, R. Wise, D. Mercer and A. Chatterjee, "The
    role of boron segregation and transient enhanced diffusion on
    reverse short channel effect", *Proc. SISPAD 1997*, pp. 141–143.
    <https://doi.org/10.1109/SISPAD.1997.621357>
[^eaglesham-1994]: D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and J.
    M. Poate, "Implantation and transient B diffusion in Si: The source
    of the interstitials", *Applied Physics Letters* **65**(18),
    2305–2307 (1994). <https://doi.org/10.1063/1.112725>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^agarwal-1999]: A. Agarwal, H.-J. Gossmann and A. T. Fiory, "Effect of
    ramp rates during rapid thermal annealing of ion implanted boron for
    formation of ultra-shallow junctions", *Journal of Electronic
    Materials* **28**(12), 1333–1339 (1999).
    <https://doi.org/10.1007/s11664-999-0118-7>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^pat-halo-chartered]: Y. Pan (Chartered Semiconductor Manufacturing),
    *Method of making self-aligned halo process for reducing junction
    capacitance*, US 5,595,919 A, granted 1997-01-21.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5595919>
[^pat-quad-tsmc]: M.-S. Lin, C.-S. Yoo and M.-S. Liang (Taiwan
    Semiconductor Manufacturing Company), *Multiple tilted angle ion
    implantation MOSFET method*, US 5,372,957 A, granted 1994-12-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5372957>
[^pat-halo-goldstar]: H. S. Hwang (Goldstar Electron), *Method for
    fabricating LDD transitor utilizing halo implant*, US 5,364,807 A,
    granted 1994-11-15.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5364807>
[^pat-halo-amd-diff]: B. Yu (Advanced Micro Devices), *MOSFET with
    differential halo implant and annealing strategy*, US 6,630,385 B1,
    granted 2003-10-07.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6630385>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
