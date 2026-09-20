(step-065)=
# Step 065 — ASTI: As tip implant

| | |
|---|---|
| **Step number** | 65 of 171[^steps-sheet] |
| **Step code** | `ASTI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`NTM <step-064>` |
| **Next step** | {ref}`BHI <step-066>` |

## What this step is

`ASTI` is the arsenic implant that forms the source/drain
{term}`extension` — the "tip" — of the standard 1.8 V NMOS transistors.
Through the resist windows opened at {ref}`NTM <step-064>`, arsenic ions
enter the active silicon on both sides of every polysilicon gate, passing
through the thin {term}`screen oxide` inferred to have been grown at
{ref}`IOX45 <step-063>`. The gate stack itself masks the channel, so
the implanted region begins at the gate edge and is *self-aligned* to
it; the gate poly is shielded by the nitride and oxide caps it still
carries from {ref}`GATENIT <step-058>` and {ref}`POC <step-059>` (see
{ref}`P1I <step-050>`), so the tip does not dope the gate. The result
is a shallow, heavily doped n-type layer that will link the channel to
the deep n⁺ source/drain formed later at {ref}`NSDI <step-086>`,
outside the {term}`spacer`.

That the tip is arsenic is stated publicly: the PDK's junction-depth
table has a row "N Tip (As)" carrying 0.01 µm in the table's "Vertical
Space" column (variable `LDNTIP`), which we read as the tip's lateral
extent because the same column holds the source/drain lateral diffusion
(`LD`, 0.06 µm) and the well junction "from drawn edge" (inference),
beside the deeper "N+ or P+ S/D (XJ)" row
at 0.1 µm vertical and 0.06 µm lateral;[^pdk-03] the same page gives the
"Angle for tip implant" as 7°.[^pdk-03] Energy and dose are not public.
The boron {term}`halo` {ref}`BHI <step-066>` follows through the same resist,
and the resist is stripped at {ref}`ASTIS <step-067>`.

## Step category

`ASTI` is an {ref}`Ion implantation <category-implant>` step of the
*extension* class: low energy (a few keV to about 20 keV, typical of the
node),[^txt-01][^rev-05] a dose of the order of 10¹⁴–10¹⁵ cm⁻²
(typical),[^txt-01] and a small tilt. It is the shallowest implant in
the flow — the category page notes that a 130 nm process spans "from a
few keV for source/drain extensions to over 1 MeV for deep
n-wells"[^txt-01] — and, with the deep source/drain implants
({ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`,
{ref}`NSDI <step-086>`), one of the implants that amorphise the silicon
surface at typical doses.

## Why this step exists

The extension does three jobs that the deep source/drain cannot:

* **Short-channel control.** The junction that faces the channel must
  be shallow so that the drain's depletion region does not reach under
  the gate and lower the source barrier (drain-induced barrier lowering, {term}`DIBL`); Wikipedia
  describes the regime in which "the depletion regions of the source
  and drain begin overlapping underneath the channel".[^wiki-sce] ITRS
  2001 sets the extension junction depth at "0.55*Physical Gate
  Length", i.e. 27–45 nm for its 2001 technology year, with a lateral
  abruptness of 7.2 nm/decade.[^itrs-01] Thompson and co-workers showed
  that as gate length shrinks the extension must become both shallower
  and *more* heavily doped to keep drive current.[^thompson-1998]
* **Series resistance.** The extension carries the full drain current
  from the channel to the deep junction under the spacer; ITRS 2001
  allocates "7% of the allowable source and drain parasitic
  resistances to the drain extensions" and sets a maximum (PMOS)
  drain-extension {term}`sheet resistance` of 400 Ω/sq for its 2001
  year.[^itrs-01] A lightly
  doped {term}`LDD` of the 1980 kind[^ogura-1980] would cost too much drive
  current at 1.8 V, which is why the modern "tip" is heavily doped.
* **Gate overlap.** The extension must reach a few nanometres under the
  gate edge — the PDK's 0.01 µm "N Tip (As)" figure, which we read as
  the tip's lateral extent (inference, above)[^pdk-03] —
  so that the channel is not separated from the source by an
  undoped gap; too much overlap adds Miller capacitance.

**Arsenic rather than phosphorus.** Arsenic is the n-type dopant of
choice for extensions because it is heavy (mass 75): at a given energy
its range is short and its profile skewed towards the surface,[^txt-01]
and it diffuses slowly and mainly by vacancies, so the junction stays
abrupt through the anneals.[^rev-05] Its drawbacks are electrical: above
roughly 2 × 10²⁰ cm⁻³ arsenic clusters and deactivates on annealing
(typical value)[^txt-01]; Nobili and co-workers identified precipitation
as the mechanism.[^nobili-1983] The deactivation itself injects
interstitials that enhance the diffusion of nearby
boron[^rousseau-1994] — the halo. Kasnavi, Griffin and Plummer measured
the sheet-resistance and junction-depth limits of very-low-energy
arsenic implants for exactly this application.[^kasnavi-2000]

Without `ASTI` the 1.8 V NMOS would have only the deep n⁺ junction
outside the spacer: a channel separated from its source by an undoped
gap under the spacer, and, if the deep junction were pulled to the
gate edge instead, severe short-channel effects at 0.15 µm.

## How it is typically performed

An industry-generic arsenic extension implant for a 200 mm, 130 nm-era
fab (SKY130's energy and dose are not public):

* **Species and source.** ⁷⁵As⁺, from arsine (AsH₃) gas or a solid
  arsenic charge; Wikipedia lists "Arsine gas or phosphine gas" as the
  sources for arsenic and phosphorus.[^wiki-implant] The PDK's "N Tip
  (As)" row confirms the species for SKY130.[^pdk-03]
* **Energy.** A few keV to a few tens of keV (typical of the
  node).[^txt-01][^rev-05] ITRS 2001 defines the extension junction
  depth at the channel as 0.55 times the physical gate length; for
  SKY130's 0.15 µm drawn gate that rule gives roughly 80 nm, against the
  27–45 nm its 2001 column tabulates for a 65 nm-gate MPU, so the
  SKY130 tip is deeper than the roadmap's leading-edge entry and the
  energy is correspondingly higher (our reading of the
  roadmap).[^itrs-01] The implant passes through the screen oxide, which
  absorbs part of the range and randomises the beam.
* **Dose.** Of order 10¹⁴–10¹⁵ cm⁻² (typical).[^txt-01] Above roughly
  10¹⁴ cm⁻² at room temperature, a heavy ion such as arsenic amorphises
  the silicon surface (typical value);[^txt-01][^rev-05] "the amount of
  crystallographic damage can be enough to completely amorphize the
  surface",[^wiki-implant] so the implanted layer is amorphous and
  regrows by {term}`solid-phase epitaxy` at
  {ref}`TIPRTAD <step-075>`, which gives high activation but leaves
  end-of-range defects at the old amorphous/crystalline boundary
  ({ref}`category-implant`).
* **Tilt and twist.** The PDK records 7° for the tip implant.[^pdk-03] A
  tilted beam is {term}`shadowed <shadowing>` on one side of each gate by the gate stack —
  0.18 µm of poly[^pdk-03] plus a cap that the
  {ref}`GATENIT <step-058>` page reads as at least the PDK's 0.2 µm
  "poly cap after SPE" (the PDK's figure is the thickness that survives
  the spacer etch at {ref}`SPE <step-077>`, so the cap here is no
  thinner)[^pdk-03] — so a 7° beam is blocked for at least
  about 0.38 µm × tan 7° ≈ 47 nm beside the gate, and symmetric source
  and drain tips require either two or four wafer rotations or a 0°
  implant through a screen oxide (category page). Yoneda and Niwayama
  showed how an angle error of the implanter turns this shadowing into
  a measurable source/drain asymmetry at 130 nm.[^yoneda-2002] SKY130's
  rotation scheme is not public.
* **Charge control and cooling.** The wafer is largely resist-covered;
  an electron shower or plasma flood neutralises the beam, and
  Lukaszek et al. showed that the resist itself changes wafer charging
  during high-current arsenic implants.[^lukaszek-1996] The platen is
  cooled to keep the resist below its flow temperature.
* **Anneal.** None here; the tip, its halo and the two other tip
  flavours are activated together at {ref}`TIPRTAD <step-075>`.
* **Monitoring.** Sheet resistance on bare monitor wafers after a
  monitor anneal (the dose is high enough for a {term}`four-point probe`), and
  thermal-wave measurement on product.[^smith-1985]

## Machines typically used

* **{ref}`High-current ion implanter <machine-high-current-implanter>`**, 200 mm, batch: Axcelis (Eaton)
  NV-GSD/200 and GSD series, Varian VIISta 80, Applied Materials
  xR80/Quantum ({ref}`category-implant`) — the usual home of
  10¹⁴–10¹⁵ cm⁻² implants.
* **{ref}`Medium-current ion implanter <machine-medium-current-implanter>`**, single-wafer: Axcelis 8250 class,
  Varian E220/E500 — used for extension implants when the dose is at
  the low end and a precise tilt is wanted; the 8250HT covers "3keV to
  750keV" with beam currents "between 4µA and 3,500µA".[^axcelis-8250]
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`** and **thermal-wave** metrology.

## Machines likely used at SkyWater

* **Axcelis GSD implanters (high-current/high-energy and high-dose).**
  SkyWater lists two: "Axcelis GSD High current/energy B11, BF2, P, As,
  10-3000kev, 1e11 to 5e15, tilt/twist" and "Axcelis GSD Hi dose B11, BF2,
  P, As 2-180kev, 5e12 to 5e16, tilt/twist"[^skw-01] — both offer arsenic
  and reach the 10¹⁵ cm⁻² decade, and the Hi dose tool's 2 keV floor covers
  even a very shallow tip. Strength: **strong** for the tools; **inference**
  for the assignment.
* **Axcelis 8250 medium-current implanter.** SkyWater lists "Axcelis
  8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14,
  0-60 deg tilt".[^skw-01] It offers arsenic and the 7° tilt; the
  platform's energy floor is 3 keV on the later 8250HT variant, for
  which a published specification exists[^axcelis-8250] — SkyWater's own
  listing gives no energy range. Its quoted dose ceiling of
  10¹⁴ cm⁻² would put a heavier tip out of reach. Strength: strong for
  the tool; **weak** for assignment — which tool runs `ASTI`
  depends on the (non-public) dose.

## Resources required

* **{ref}`Arsine <material-dopant-sources>` (AsH₃)** in sub-atmospheric or dilute cylinders, or a
  **solid arsenic** source charge;[^wiki-implant][^wiki-ash3] arsine is
  highly toxic and is handled in monitored gas cabinets.
* **Source-support gases** ({ref}`argon <material-process-gases>`, xenon), source consumables
  (filaments, arc-chamber liners, extraction electrodes).
* **Helium** for platen cooling; **liquid nitrogen** or cryopump
  regeneration; high-purity **nitrogen** for venting.
* **{ref}`Monitor wafers <material-substrates>`** for sheet-resistance and thermal-wave control.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`NTM <step-064>` (the resist mask); the screen oxide:
  {ref}`IOX45 <step-063>`; the gates: {ref}`P1ME <step-062>`.
* Next: {ref}`BHI <step-066>` (the halo through the same resist), then
  {ref}`ASTIS <step-067>` (strip).
* The other tip implants: {ref}`HVASTI <step-069>` (5 V NMOS) and
  {ref}`LDASTI <step-072>` ({term}`SONOS` transistors).
* Activation: {ref}`TIPRTAD <step-075>`; spacer:
  {ref}`SPNIT <step-076>`; deep n⁺ junction: {ref}`NSDI <step-086>`.
* Category page: {ref}`Ion implantation <category-implant>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Solid phase epitaxy activation process for source/drain junction extensions and halo regions <patent-gp24538683>` — US 6,521,502 B1 (2000)
* {ref}`Double LDD devices for improved DRAM refresh <patent-gp24577983>` — US 6,759,288 B2 (2000)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — "N Tip (As)" 0.01 µm, S/D
  XJ 0.1 µm, tip implant angle 7°, poly thickness 0.18 µm.[^pdk-03]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — the 1.8 V NMOS family this tip
  serves.[^pdk-07]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the Axcelis GSD and 8250
  species, energy, dose and tilt ranges.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* [Semiconductor Online, *8250HT Medium Current Ion Implanter*](<https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>) — the
  energy and current range of the medium-current class.[^axcelis-8250]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — Table 51a extension depth, sheet
  resistance and abruptness.[^itrs-01]

### High-level understanding

* [Wikipedia, *Ion implantation*](<https://en.wikipedia.org/wiki/Ion_implantation>) — sources, amorphisation, tilt.[^wiki-implant]
* [Wikipedia, *Short-channel effect*](<https://en.wikipedia.org/wiki/Short-channel_effect>) — depletion-region overlap and
  DIBL.[^wiki-sce]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — ch. 8
  (implantation) and the extension-junction discussion.[^txt-01]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 3](<https://openlibrary.org/isbn/9780961672157>) — LDD and
  extension engineering.[^txt-04]
* [Taur and Ning, *Fundamentals of Modern VLSI Devices*](<https://doi.org/10.1017/CBO9781139195065>) — source/drain
  series resistance and short-channel physics.[^taur-2009]

### Deep dive

* [Ogura et al. (IBM), *IEEE TED* 1980](<https://doi.org/10.1109/T-ED.1980.20040>) — the lightly doped drain, the
  first self-aligned extension.[^ogura-1980]
* [Thompson et al. (Intel), VLSI 1998](<https://doi.org/10.1109/VLSIT.1998.689229>) — extension depth and doping
  scaling for 0.1 µm and below.[^thompson-1998]
* [Kasnavi, Griffin and Plummer, VLSI 2000](<https://doi.org/10.1109/VLSIT.2000.852790>) — the limits of ultra-low
  energy arsenic implants on sheet resistance and junction
  depth.[^kasnavi-2000]
* [Jones and Ishida, *Mater. Sci. Eng. R* 1998](<https://doi.org/10.1016/S0927-796X(98)00013-8>) — review of shallow
  junction formation: low-energy implantation, {term}`TED` and {term}`RTA`.[^rev-05]
* [Nobili et al., *J. Electrochem. Soc.* 1983](<https://doi.org/10.1149/1.2119859>) — precipitation as the
  cause of electrically inactive arsenic above its solubility.[^nobili-1983]
* [Rousseau, Griffin and Plummer, *Appl. Phys. Lett.* 1994](<https://doi.org/10.1063/1.112301>) — arsenic
  deactivation as a source of interstitials that enhance diffusion of
  neighbouring dopants.[^rousseau-1994]
* [Taur et al., *Proc. IEEE* 1997](<https://doi.org/10.1109/5.573737>) — why junction depth and abruptness
  govern scaling.[^taur-1997]
* [Yoneda and Niwayama, IWJT 2002](<https://doi.org/10.1109/IWJT.2002.1225190>) — extension-implant shadowing and
  drain-current asymmetry at 130 nm.[^yoneda-2002]
* [Lukaszek, Reno and Bammi, IIT 1996](<https://doi.org/10.1109/IIT.1996.586135>) — wafer charging through resist
  during high-current arsenic implants.[^lukaszek-1996]
* [Hook et al. (IBM), *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — lateral {term}`straggle` at implant
  edges.[^hook-2003]
* [Yu (AMD), US 6,521,502](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6521502>) — activating extensions and halos by
  solid-phase epitaxy of an amorphised layer.[^pat-spe-amd]
* [Tran, McQueen and Kerr (Micron), US 6,759,288](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6759288>) — a masked second LDD
  implant with explicit device motivation.[^pat-ldd-micron]
* [Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985](<https://doi.org/10.1063/1.96079>) — the
  thermal-wave implant monitor.[^smith-1985]

## Open questions

* The SKY130 tip energy and dose are not public; the values above are
  node-typical. Whether the dose exceeds the 10¹⁴ cm⁻² ceiling SkyWater
  quotes for its medium-current tool, and hence which implanter runs
  the step, cannot be settled from public data.
* The rotation scheme (0°, two or four rotations at the published 7°
  tilt) is not public.
* Whether a germanium or silicon {term}`pre-amorphisation <pre-amorphisation implant>` is used is an
  open question; this page describes none.
* Whether the tip precedes or follows the halo within the resist
  window — this reference describes the arsenic first — affects the
  amorphous layer the boron sees; see
  {ref}`BHI <step-066>`.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^wiki-sce]: Wikipedia, *Short-channel effect*.
    <https://en.wikipedia.org/wiki/Short-channel_effect>
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
[^rev-05]: E. C. Jones and E. Ishida, "Shallow junction doping
    technologies for ULSI", *Materials Science and Engineering: R*
    **24**(1–2), 1–80 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00013-8>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^thompson-1998]: S. Thompson, P. Packan, T. Ghani, M. Stettler,
    M. Alavi, I. Post, S. Tyagi, S. Ahmed, S. Yang and M. Bohr,
    "Source/drain extension scaling for 0.1 μm and below channel length
    MOSFETs", *1998 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 132–133. <https://doi.org/10.1109/VLSIT.1998.689229>
[^kasnavi-2000]: R. Kasnavi, P. B. Griffin and J. D. Plummer, "Ultra
    low energy arsenic implant limits on sheet resistance and junction
    depth", *2000 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 112–113. <https://doi.org/10.1109/VLSIT.2000.852790>
[^nobili-1983]: D. Nobili, A. Carabelas, G. Celotti and S. Solmi,
    "Precipitation as the Phenomenon Responsible for the Electrically
    Inactive Arsenic in Silicon", *Journal of The Electrochemical
    Society* **130**(4), 922–928 (1983).
    <https://doi.org/10.1149/1.2119859>
[^rousseau-1994]: P. M. Rousseau, P. B. Griffin and J. D. Plummer,
    "Electrical deactivation of arsenic as a source of point defects",
    *Applied Physics Letters* **65**(5), 578–580 (1994).
    <https://doi.org/10.1063/1.112301>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^yoneda-2002]: K. Yoneda and M. Niwayama, "The drain current asymmetry
    of 130 nm MOSFETs due to extension implant shadowing originated by
    mechanical angle error in high current implanter", *Extended
    Abstracts of the Third International Workshop on Junction
    Technology (IWJT 2002)*, pp. 19–22.
    <https://doi.org/10.1109/IWJT.2002.1225190>
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic implant",
    *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 89–92.
    <https://doi.org/10.1109/IIT.1996.586135>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^pat-spe-amd]: B. Yu (Advanced Micro Devices), *Solid phase epitaxy
    activation process for source/drain junction extensions and halo
    regions*, US 6,521,502 B1, granted 2003-02-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6521502>
[^pat-ldd-micron]: L. C. Tran, M. McQueen and R. Kerr (Micron
    Technology), *Double LDD devices for improved DRAM refresh*, US
    6,759,288 B2, granted 2004-07-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6759288>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
