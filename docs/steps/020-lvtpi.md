(step-020)=
# Step 020 — LVTPI: Low V P-channel implant

| | |
|---|---|
| **Step number** | 20 of 171[^steps-sheet] |
| **Step code** | `LVTPI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`NWI2 <step-019>` |
| **Next step** | {ref}`LVTPIS <step-021>` |

## What this step is

`LVTPI` is, in the sequence this reference describes, the third and last implant
placed through the N-well resist of {ref}`NWM <step-017>`, after the two
well implants {ref}`NWI <step-018>` and {ref}`NWI2 <step-019>`. Where
those set the buried profile of the N-well, `LVTPI` is a low-energy
*channel* implant that sets the surface doping under the future PMOS
gates — that is, the PMOS threshold voltage (inference, on the
arrangement of the IBM patent below). In this reference it is labelled
"Low V P-channel implant". Because it shares the
N-well window, it reaches every N-well region on the wafer: the 1.8 V
PMOS, the 5 V PMOS, the N-well rings and the drain extensions alike,
unless the {term}`reticle` is generated differently for some of them (not
public). It is the P-channel counterpart of {ref}`NCHI <step-045>`, the
N-channel implant that the 1.8 V NMOS receive later under the
low-voltage oxide mask.

The step's position is what makes it economical: no extra lithography is
needed because the N-well mask already outlines exactly the regions
where PMOS channels can exist. The IBM retrograde-well patent describes
the same arrangement, with a "low dose implant … (50 kEv, 5×10 E 11 per
cm²)" of phosphorus as the shallowest member of the N-well chain, placed
through the same mask.[^pat-well-ibm]

## Step category

`LVTPI` is an {ref}`Ion implantation <category-implant>` step of the
*{term}`threshold-adjust <threshold-adjust implant>`* class — light dose, tens of keV, medium-current
tool (category page) — even though it is grouped with the well
implants in the flow.

## Why this step exists

The PMOS threshold must be set independently of the well profile. The
buried N-well peak of {ref}`NWI <step-018>` is placed deep for latch-up
and {term}`punch-through` reasons and leaves the surface only lightly doped, so
a shallow channel implant sets the surface concentration to the value
that gives the wanted |{term}`Vt`| — an n-type dose that raises it under a p⁺
gate, or, under the n⁺ gate the gate pages infer for SKY130
({ref}`P1I <step-050>`), a p-type dose that {term}`counter-dopes <counter-doping>` the surface of
a {term}`buried-channel device <buried-channel PMOS>`. In the body-effect expression γ ∝ √N,[^wiki-vt]
and multi-Vt CMOS is made by "altering the concentration of dopant atoms
in the channel region beneath the gate oxide".[^wiki-mtcmos] The 2001
ITRS FEP table gives, as illustration of the magnitudes involved, a
"Uniform channel concentration … for Vt=0.4" of 0.8–1.5 × 10¹⁸ cm⁻³ for
the 2001 high-performance node and a "Retrograde channel depth" of
21–30 nm[^itrs-01] — SKY130's 1.8 V devices are a low-power,
longer-channel design and will not match those numbers, but the order of
magnitude is the same.

`LVTPI` therefore establishes the *baseline* PMOS: `pfet_01v8` and, we
infer, the 5 V `pfet_g5v0d10v5`. The other PMOS flavours are derived
from it — `pfet_01v8_hvt` by the additional implants of
{ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>` under
{ref}`HVTPM <step-022>`, and `pfet_01v8_lvt` through the `lvtn` blocking
layer[^pdk-07][^pdk-periph] (see {ref}`LVTNM <step-014>`).

In the published test-tile measurements the standard PMOS has a
threshold magnitude of 1.065 V at 7/8 µm and 0.798 V at 7/0.15 µm
(maximum-transconductance extrapolation at V_DS = −0.1 V, less half
the drain bias; our extraction from the published measurements),
within 0.02 V of the PDK's e-test nominals of −1.050 V and
−0.781 V.[^raw-data-lv-mosfets][^pdk-07] The measurements show where
the baseline threshold lies, not which implant sets it.

## How it is typically performed

An industry-generic PMOS threshold implant for a 200 mm, 130 nm-era
fab (SKY130 values are not public):

* **Species.** If, as the gate pages infer ({ref}`P1I <step-050>`),
  SKY130 uses n⁺ poly on the PMOS, the baseline threshold implant is a
  *p-type* counter-doping (boron or BF₂) that brings a buried-channel
  PMOS from the roughly −1.2 V that an uncompensated n⁺-gate PMOS of this oxide thickness and well doping would show (an illustrative estimate, not a published value) towards the
  PDK's −1.05 V long-channel value;[^pdk-07] if the gate were p⁺, an
  *n-type* species (arsenic or phosphorus) would set the threshold
  instead — the Round Rock/Micron patent uses "an implant of
  Arsenic",[^pat-vt-rrr] IBM 50 keV phosphorus at
  5 × 10¹¹ cm⁻².[^pat-well-ibm] Which SKY130 uses is not public.
* **Energy and dose.** Tens of keV and 10¹²–10¹³ cm⁻² are typical for
  threshold adjusts (category page; an LSI Logic patent gives 1 × 10¹²–1
  × 10¹³ cm⁻² for the boron equivalent,[^pat-vt-lsi] an AMD patent
  1.0–2.5 × 10¹³ cm⁻²[^pat-vt-amd]).
* **Tilt and twist.** 7° with twist;[^wiki-implant][^txt-02] the implant
  is symmetric, so no rotation is needed.
* **{term}`Screen oxide <screen oxide>`.** Through the pad oxide of 10–20 nm that a Cypress
  patent describes under its well and channel implants.[^pat-04]
* **Charge control.** Electron shower; the resist is thick and already
  charged by two high-energy (MeV-class, we infer) implants (SkyWater
  lists "E shower" on the 8250).[^skw-01]
* **Anneal.** {ref}`RTAI <step-034>` — "a rapid thermal anneal is
  performed after implanting both the n-well and p-well" and "any number
  of channel implants may also be performed … to adjust threshold
  voltages" before it.[^pat-03]

## Machines typically used

* **{ref}`Medium-current implanter <machine-medium-current-implanter>`** with serial end station and tilt: Axcelis
  (Eaton) 8250/8250HT ("3keV to 750keV"),[^axcelis-8250] Varian
  E220/E500, Nissin (category page).
* If the batch {ref}`high-energy tool <machine-high-energy-implanter>` has just run `NWI`/`NWI2`, some fabs run
  the channel implant on it too to avoid a cassette move; both tool
  classes cover tens of keV.
* **{ref}`Thermal-wave <machine-sheet-resistance-metrology>`** metrology for dose control.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** — "B11, BF2, As, ESC chuck, E shower,
  1e11 to 1e14, 0-60 deg tilt":[^skw-01] boron and BF₂ (the species of
  the n⁺-gate reading) and arsenic (of the p⁺-gate reading) are all
  available and the dose window fits. Strength: **strong** for the tool;
  assignment is an **inference**. Note that phosphorus is *not* in the
  8250's public species list.
* **Axcelis GSD high-current/high-energy implanter** — "B11, BF2, P,
  As, 10-3000kev"[^skw-01] (the entry whose dose range starts below the
  Hi dose entry's 5e12) could run either species. Strength: strong for
  existence.

## Resources required

* **Boron trifluoride (BF₃)** source gas for the p-type implant of the
  n⁺-gate reading; **arsine (AsH₃)** or **phosphine (PH₃)** if the
  implant is n-type.[^wiki-implant]
* Support gases, cryopump and source consumables, monitor wafers
  (category page).
* No new resist: the {ref}`NWM <step-017>` resist is reused.

## Related steps and cross-references

* Previous: {ref}`NWI2 <step-019>`; next: {ref}`LVTPIS <step-021>`
  (strip of the N-well resist).
* Threshold companions: {ref}`LVTNI <step-015>` (NMOS low-Vt),
  {ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>` (PMOS high-Vt),
  {ref}`NCHI <step-045>` (N-channel baseline).
* Activated at {ref}`RTAI <step-034>`; the PMOS gate oxide grows at
  {ref}`GOX100 <step-043>`/{ref}`LVGOX <step-047>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — Axcelis 8250 species and dose
  range; GSD.[^skw-01]
* SkyWater PDK, *Device Details* — `pfet_01v8`, `pfet_01v8_lvt`,
  `pfet_01v8_hvt`, `pfet_g5v0d10v5`.[^pdk-07]
* SkyWater PDK, *Periphery rules* — `lvtn` and `hvtp` function
  text.[^pdk-periph]
* Koutny et al. (Cypress), US 8,093,128 — channel implants and {term}`RTA`
  before the {term}`SONOS` module.[^pat-03]
* Ramkumar et al. (Cypress), US 8,796,098 — implants through a 10–20 nm
  pad oxide.[^pat-04]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  Eaton/Axcelis 8250HT energy and beam-current ranges.[^axcelis-8250]
* SKY130 raw-data repository, 1.8 V transistor files — measured
  `pfet_01v8` thresholds at the e-test geometries (our
  extraction).[^raw-data-lv-mosfets]

### High-level understanding

* Wikipedia, *Ion implantation* — energies, sources, {term}`channelling` and
  tilt in one page.[^wiki-implant]
* Wikipedia, *Threshold voltage* — the body-effect parameter containing
  the channel doping.[^wiki-vt]
* Wikipedia, *Multi-threshold CMOS* — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — surface- versus
  buried-channel PMOS, dual-gate CMOS.[^txt-04]

### Deep dive

* ITRS 2001, *Front End Processes* — Table 51: channel concentration,
  retrograde channel depth.[^itrs-01]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — 50 keV phosphorus
  channel-side implant through the N-well mask.[^pat-well-ibm]
* Helm and Zhou (Round Rock Research), US 2011/0006372 — arsenic first
  Vt adjust.[^pat-vt-rrr]
* Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801 — Vt-adjust
  boron at 1e12–1e13 cm⁻² and 50–100 keV, chained punch-through
  barriers, a 900 °C furnace anneal.[^pat-vt-lsi]
* Krivokapic and Milic (AMD), US 6,238,982 — channel-implant energies
  and doses for boron and BF₂.[^pat-vt-amd]
* MacPherson, *Appl. Phys. Lett.* 1971 — the original
  threshold-adjust-by-implantation paper.[^macpherson-1971]
* Taur et al., *Proc. IEEE* 1997 — super-steep retrograde channels and
  multiple thresholds at 0.1 µm.[^taur-1997]
* Taur and Ning, *Fundamentals of Modern VLSI Devices* — threshold
  voltage versus channel doping and the body effect a channel implant
  sets.[^taur-2009]
* Rafferty et al. (AT&T), IEDM 1993 — how implant damage and the anneal
  reshape the channel doping.[^rafferty-1993]
* Thompson, Packan and Bohr (Intel), VLSI 1996 — the drive-current
  trade-offs of super-steep retrograde channel
  engineering.[^thompson-1996]
* Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985 — the
  thermal-wave monitor used for light channel implants.[^smith-1985]

## Open questions

* The step list used in this reference does not explain "Low V"; we
  read the step as the baseline PMOS channel implant for all N-wells,
  following the arrangement of the IBM retrograde-well
  patent.[^pat-well-ibm] Whether the implant also reaches the 5 V PMOS
  regions is not stated publicly.
* Species (boron or BF₂ versus arsenic or phosphorus), energy and dose
  are not public.
* SKY130's PMOS gate is read on the gate pages as n⁺ poly
  (buried-channel PMOS), inferred from the PDK's "N+ doped gate poly",
  the absence of a P⁺ poly mask, the capped gate and the −1.05 V
  long-channel threshold; the species reading above follows from that
  inference.

<!-- footnotes -->

[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23.
    <https://patents.google.com/patent/US6667205B2/en>
[^wiki-vt]: Wikipedia, *Threshold voltage*.
    <https://en.wikipedia.org/wiki/Threshold_voltage>
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13 (priority
    2002-07-08). <https://patents.google.com/patent/US20110006372A1/en>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pat-vt-lsi]: S. Aronowitz, L. Khan and J. Kimball (LSI Logic), *Method
    of forming retrograde well structures and punch-through barriers
    using low energy implants*, US 5,963,801 A, granted 1999-10-05.
    <https://patents.google.com/patent/US5963801A/en>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (AMD), *Multiple threshold
    voltage semiconductor device fabrication technology*, US 6,238,982
    B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
[^macpherson-1971]: M. R. MacPherson, "The adjustment of MOS transistor
    threshold voltage by ion implantation", *Applied Physics Letters*
    **18**(11), 502–504 (1971). <https://doi.org/10.1063/1.1653513>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^rafferty-1993]: C. S. Rafferty, H.-H. Vuong, S. A. Eshraghi, M. D.
    Giles, M. R. Pinto and S. J. Hillenius, "Explanation of reverse
    short channel effect by defect gradients", *IEDM 1993 Technical
    Digest*, pp. 311–314. <https://doi.org/10.1109/IEDM.1993.347345>
[^thompson-1996]: S. E. Thompson, P. A. Packan and M. T. Bohr, "Linear
    versus saturated drive current: tradeoffs in super steep retrograde
    well engineering", *1996 Symposium on VLSI Technology, Digest of
    Technical Papers*, pp. 154–155.
    <https://doi.org/10.1109/VLSIT.1996.507830>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-lv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 1.8 V
    transistors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_01v8`, `nfet_01v8_lvt`, `pfet_01v8`, `pfet_01v8_hvt`,
    `pfet_01v8_lvt`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
