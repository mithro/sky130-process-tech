(step-075)=
# Step 075 — TIPRTAD: RTA tip activation

| | |
|---|---|
| **Step number** | 75 of 171[^steps-sheet] |
| **Step code** | `TIPRTAD` |
| **Category** | {ref}`Anneal / thermal processing <category-anneal>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`LDASTIS <step-074>` |
| **Next step** | {ref}`SPNIT <step-076>` |

## What this step is

`TIPRTAD` is the rapid thermal anneal that closes the tip module. Five
implants have gone into the wafer since the gate was etched — the
standard arsenic tip {ref}`ASTI <step-065>` and its boron {term}`halo`
{ref}`BHI <step-066>`, the tilted high-voltage tip
{ref}`HVASTI <step-069>`, and the lightly doped {term}`SONOS` tip
{ref}`LDASTI <step-072>` with its halo {ref}`LDBHI <step-073>` — and
none has been annealed. `TIPRTAD` heats the wafer — in an inert
ambient for seconds on the industry-typical recipe described below;
SKY130's own conditions are not public — to a temperature high enough
to regrow the arsenic-amorphised silicon, put the arsenic and boron
onto lattice sites, and dissolve the implant damage, while moving the
junctions as little as possible. This reference describes it as a
rapid thermal anneal for tip activation, as it does the later
{ref}`RTAD <step-088>` and {ref}`RTAD2 <step-092>`; the public
evidence for an RTA is set out below (SkyWater lists a single-wafer
lamp RTA,[^skw-01] and shallow extensions call for one[^stolk-1997]).
After it the {term}`spacer` nitride is deposited at
{ref}`SPNIT <step-076>`.

It is the second of the four activation anneals in the flow, after
{ref}`RTAI <step-034>` (wells and channels) and before
{ref}`RTAD <step-088>` and {ref}`RTAD2 <step-092>` (source/drain), and
the one with the shallowest, most abrupt profiles to preserve.

## Step category

`TIPRTAD` is an {ref}`Anneal / thermal processing <category-anneal>`
step of the *implant activation* type — a single-wafer, lamp-heated
{term}`RTA` — in its most demanding form: an {term}`extension` anneal, in
which the target is maximum activation with minimum diffusion. The
category page sets out the compromise: "the highest activation is
obtained by annealing hot and fast",[^gibbons-1972][^nobili-1983] and
transient enhanced diffusion
"is worst for slow, low-temperature anneals because the damage
dissolves while the dopant is still mobile"; the resolution "is the
RTA: seconds at 1000–1100 °C, or a 'spike' anneal with essentially
zero soak time".[^stolk-1997]

## Why this step exists

Three things depend on annealing the tips now, before the spacer, and
on doing it fast:

* **Activation and regrowth.** Implanted dopant is inactive until the
  lattice is restored;[^gibbons-1972][^txt-01] the arsenic tip, at a
  dose that amorphises the surface (typical),[^wiki-implant] regrows by
  {term}`solid-phase epitaxy` from the undamaged substrate at 500–600 °C with
  the arsenic incorporated substitutionally,[^csepregi-1978] and the
  boron halos in crystalline or regrown silicon need 800–1000 °C-class
  temperatures to dissolve their defect clusters.[^gibbons-1972] Above
  its solubility arsenic clusters and deactivates on
  cooling,[^nobili-1983] so the anneal is designed to activate as much
  as possible and then quench.
* **Junction position.** ITRS 2001 asks for a 27–45 nm extension
  junction with 7.2 nm/decade lateral abruptness for a 2001-year MPU
  whose physical gate length is 65 nm; its rule Xj = 0.55 × physical
  gate length puts SKY130's tip nearer 80 nm for its 0.15 µm drawn
  gate.[^itrs-01] The PDK publishes no depth for the tip, only the
  0.01 µm in the "Vertical Space" column of its "N Tip (As)" row, which
  we read as the lateral extent.[^pdk-03] The halo boron is the mobile species: the
  interstitials released as damage anneals[^eaglesham-1994] and as
  arsenic deactivates[^rousseau-1994] drive its transient enhanced
  diffusion,[^michel-1987][^stolk-1997] and the boron then smears
  into the channel and the tip. Agarwal and co-workers showed that
  faster ramps and shorter soaks — the *spike* anneal — give shallower
  boron junctions at equal activation,[^agarwal-1999][^agarwal-1998]
  and Shishiguchi's group demonstrated 400 °C/s ramps for the same
  purpose.[^shishiguchi-1997] Jones and Ishida's review covers the
  whole trade.[^rev-05]
* **Before the spacer.** The spacer film of {ref}`SPNIT <step-076>` is
  deposited hot for tens of minutes (a furnace {term}`LPCVD` nitride is
  typical of the era).[^txt-01] Unannealed tips and halos would spend
  that time in exactly the slow, warm regime where {term}`TED` is
  worst;[^stolk-1997] annealing first removes the damage so that the
  spacer deposition moves nothing. IBM's {term}`spike-anneal <spike anneal>` patent describes
  the same logic — extensions activated, then halos "implanted and
  activated preferably using spike annealing to prevent their
  diffusion".[^pat-spike-ibm]

Without `TIPRTAD` the tips would be annealed only at
{ref}`RTAD <step-088>` after a spacer deposition, with deeper, less
abrupt junctions, a smeared halo and — for the 1.8 V NMOS — worse
short-channel control and drive current.

## How it is typically performed

An industry-generic extension anneal for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):

* **Tool and ambient.** Single-wafer lamp-heated RTA in nitrogen or
  argon; {term}`RTP` "heats silicon wafers to temperatures exceeding 1,000°C
  for not more than a few seconds" with "in situ pyrometry to effect
  real time control".[^wiki-rtp] A small oxygen addition is sometimes
  used to suppress dopant loss and surface pitting; Applied Materials
  patented an "optimal spike anneal ambient" for exactly this
  question.[^pat-spike-amat-ambient] The {term}`screen oxide` from
  {ref}`IOX45 <step-063>`, if retained through
  {ref}`LDASTIS <step-074>`, caps the surface.
* **Temperature and time.** 950–1050 °C for seconds, or a spike to
  about 1000–1100 °C with no soak, is the 130 nm-era
  choice;[^txt-05][^txt-10][^fiory-2002] Agarwal's spike-anneal study
  used ramp-up rates from a few tens to hundreds of degrees per
  second,[^agarwal-1998] and Applied Materials' later patent describes
  sharpening the spike by faster cool-down.[^pat-spike-amat] The
  Heatpulse 8800-class tools ramp at "1 – 180°C per second".[^ag-8800]
* **Sequence.** Pre-anneal clean at {ref}`LDASTIS <step-074>`; load;
  purge; ramp; soak or spike; ramp-down under lamp control; unload.
* **Control.** Pyrometer emissivity calibration against
  thermocouple-instrumented wafers; edge-ring design against slip;
  sheet-resistance mapping of implanted monitor wafers after each lot
  to track activation and uniformity.[^txt-10][^roozeboom-1990]
* **Furnace alternative.** None in practice for extensions: the tens
  of minutes of a furnace anneal would place the boron far from where
  the halo was implanted (category page).[^stolk-1997]

## Machines typically used

* **{ref}`Rapid thermal processors <machine-rapid-thermal-processor>`**, 200 mm: AG Associates Heatpulse
  8108/8800 series, Applied Materials RTP Centura (XE/Radiance), Steag
  (later Mattson) RTP, Kokusai and TEL RTP ({ref}`category-anneal`).
* **{term}`Four-point probe <four-point probe>`** ({ref}`sheet-resistance metrology <machine-sheet-resistance-metrology>`) for {term}`sheet resistance`; **thermocouple wafers**
  for calibration.

## Machines likely used at SkyWater

* **AG Associates Heatpulse 8808.** SkyWater's facilities page lists
  under RTA "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"[^skw-01] —
  a single-wafer lamp RTA with the inert ambients and the temperature
  reach an extension anneal needs. Strength: **strong** for the tool
  (SkyWater statement); the assignment to `TIPRTAD` is an
  **inference** from the shallow-junction anneal this step needs and
  from the tool being the only
  RTA on the list. Reseller documentation for the Heatpulse 8800/8808
  family gives a "Recommended steady-state temperature range: 400 –
  1200°C", ramp-up "Programmable, 1 – 180°C per second", "2 banks of
  14 lamps" with "10-zone lamp control", and "Implant annealing" among
  the applications;[^ag-8800] the family specification PDF's Heatpulse
  8108 section gives the same 400–1200 °C range, a programmable
  1–180 °C/s ramp-up and a maximum ramp-down of 150 °C/s (its Heatpulse
  4100 section differs: 400–1300 °C, 10–200 °C/s ramp-up).[^ag-8108]
* **Aviza furnaces** ("Ar anneal to 1150C", "N2 anneal to
  1150C")[^skw-01] exist on site but are, for the reasons above, an
  unlikely home for a tip anneal. Strength: strong for existence; weak
  for assignment.

## Resources required

* **{ref}`Nitrogen <material-process-gases>` and argon** (likely ambient, our inference; SkyWater lists
  the Heatpulse's gases, "NH3, Ar, N2, O2", but no ambient for any
  step);[^skw-01] **oxygen** if a minor addition is used.
* **{ref}`Tungsten-halogen lamps <material-hardware-consumables>`, quartz chamber/window, edge rings**;
  pyrometer calibration and {ref}`thermocouple wafers <material-substrates>` (category page).
* **Cooling water and CDA/N₂** for lamp and chamber cooling.[^ag-8108]
* **Monitor wafers** for sheet resistance.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LDASTIS <step-074>` (strip and pre-anneal clean).
* Next: {ref}`SPNIT <step-076>` (spacer nitride), then the spacer etch
  and the source/drain module ({ref}`PSDM <step-081>`,
  {ref}`NSDM <step-085>`).
* Anneals the tips and halos of {ref}`ASTI <step-065>`,
  {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`,
  {ref}`LDASTI <step-072>` and {ref}`LDBHI <step-073>`.
* Other RTAs: {ref}`RTAI <step-034>` before, {ref}`RTAD <step-088>`
  and {ref}`RTAD2 <step-092>` after.
* Category page: {ref}`Anneal / thermal processing <category-anneal>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "Ag Heatpulse 8808 NH3, Ar,
  N2, O2, up to 1200C"; Aviza furnaces.[^skw-01]
* SkyWater PDK, *Criteria & Assumptions* — "N Tip (As)" 0.01 µm, S/D
  junction depth 0.1 µm.[^pdk-03]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* SemiStar, *AG Associates Heatpulse 8800 / 8808* reseller page —
  temperature range, ramp rates and applications.[^ag-8800]
* SemiStar, *AG Associates Heatpulse 4100 / 8108 / 8800 / 8800i
  Specifications* (PDF) — operating specifications and facility
  table.[^ag-8108]
* ITRS 2001, *Front End Processes* — Table 51a extension depth and
  abruptness.[^itrs-01]

### High-level understanding

* Wikipedia, *Rapid thermal processing* — lamp heating, seconds above
  1000 °C, pyrometry.[^wiki-rtp]
* Wikipedia, *Ion implantation* — amorphisation and damage.[^wiki-implant]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 8
  (implantation, damage, TED) and the spacer deposition that
  follows.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — RTP.[^txt-05]

### Deep dive

* Fair (ed.), *Rapid Thermal Processing: Science and Technology* —
  junction formation by rapid thermal annealing.[^txt-10]
* Agarwal, Gossmann and Fiory, *J. Electron. Mater.* 1999 — ramp rate
  and boron ultra-shallow junctions, the case for spike
  anneals.[^agarwal-1999]
* Agarwal et al., *Mater. Sci. Semicond. Process.* 1998 — spike
  annealing in lamp and hot-wall systems and the effect of ramp-up
  rate.[^agarwal-1998]
* Shishiguchi et al. (NEC), VLSI 1997 — 400 °C/s RTA for boron shallow
  junctions.[^shishiguchi-1997]
* Stolk et al. (Bell Labs), *J. Appl. Phys.* 1997 — the physics of
  transient enhanced diffusion.[^stolk-1997]
* Michel et al. (IBM), *Appl. Phys. Lett.* 1987 — anomalous boron
  diffusion under rapid annealing, first reported.[^michel-1987]
* Eaglesham et al., *Appl. Phys. Lett.* 1994 — the interstitial source
  of boron TED.[^eaglesham-1994]
* Rousseau, Griffin and Plummer, *Appl. Phys. Lett.* 1994 — arsenic
  deactivation as an interstitial source.[^rousseau-1994]
* Nobili et al., *J. Electrochem. Soc.* 1983 — arsenic precipitation
  above its solubility.[^nobili-1983]
* Csepregi et al., *J. Appl. Phys.* 1978 — solid-phase epitaxial
  regrowth of amorphised silicon.[^csepregi-1978]
* Jones and Ishida, *Mater. Sci. Eng. R* 1998 — review of shallow
  junction formation by implantation and RTA.[^rev-05]
* Fiory, *J. Electron. Mater.* 2002 — RTP developments of the 130 nm
  era.[^fiory-2002]
* Roozeboom and Parekh (Philips), *J. Vac. Sci. Technol. B* 1990 — RTP
  systems and temperature control.[^roozeboom-1990]
* Ramachandran et al. (Applied Materials), US 6,897,131 — sharpening
  the spike by faster cool-down.[^pat-spike-amat]
* Jennings, Tallavarjula and Thakur (Applied Materials), US 6,803,297 —
  the anneal ambient for spike anneals.[^pat-spike-amat-ambient]
* Lee et al. (IBM), US 6,518,136 — extensions and halos activated by
  spike annealing to prevent their diffusion.[^pat-spike-ibm]
* Yu (AMD), US 6,521,502 — activating extensions and halos by
  solid-phase epitaxy at low temperature, the alternative
  philosophy.[^pat-spe-amd]
* Gronet and Gibbons (Applied Materials), US 5,155,336 — a lamp-heated
  single-wafer RTP chamber.[^pat-rtp-amat]

## Open questions

* The SKY130 anneal temperature, time (soak or spike) and ambient are
  not public.
* Whether the Heatpulse 8808 runs this step is inferred from the
  shallow-junction anneal this step needs and the tool being the only
  RTA on SkyWater's list.[^skw-01]
* Whether the screen oxide is present during the anneal depends on the
  clean at {ref}`LDASTIS <step-074>`, which is not public.
* The reseller PDF cited for the Heatpulse family[^ag-8108] documents
  the Heatpulse 4100 and 8108, not the 8808 itself; the 8808's own
  figures come from the reseller's product page.[^ag-8800]

<!-- footnotes -->

[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^gibbons-1972]: J. F. Gibbons, "Ion implantation in semiconductors —
    Part II: Damage production and annealing", *Proceedings of the IEEE*
    **60**(9), 1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^csepregi-1978]: L. Csepregi, E. F. Kennedy, J. W. Mayer and T. W.
    Sigmon, "Substrate-orientation dependence of the epitaxial regrowth
    rate from Si-implanted amorphous Si", *Journal of Applied Physics*
    **49**(7), 3906–3911 (1978). <https://doi.org/10.1063/1.325397>
[^nobili-1983]: D. Nobili, A. Carabelas, G. Celotti and S. Solmi,
    "Precipitation as the Phenomenon Responsible for the Electrically
    Inactive Arsenic in Silicon", *Journal of The Electrochemical
    Society* **130**(4), 922–928 (1983).
    <https://doi.org/10.1149/1.2119859>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^eaglesham-1994]: D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and J.
    M. Poate, "Implantation and transient B diffusion in Si: The source
    of the interstitials", *Applied Physics Letters* **65**(18),
    2305–2307 (1994). <https://doi.org/10.1063/1.112725>
[^rousseau-1994]: P. M. Rousseau, P. B. Griffin and J. D. Plummer,
    "Electrical deactivation of arsenic as a source of point defects",
    *Applied Physics Letters* **65**(5), 578–580 (1994).
    <https://doi.org/10.1063/1.112301>
[^michel-1987]: A. E. Michel, W. Rausch, P. A. Ronsheim and R. H. Kastl,
    "Rapid annealing and the anomalous diffusion of ion implanted boron
    into silicon", *Applied Physics Letters* **50**(7), 416–418 (1987).
    <https://doi.org/10.1063/1.98160>
[^agarwal-1999]: A. Agarwal, H.-J. Gossmann and A. T. Fiory, "Effect of
    ramp rates during rapid thermal annealing of ion implanted boron for
    formation of ultra-shallow junctions", *Journal of Electronic
    Materials* **28**(12), 1333–1339 (1999).
    <https://doi.org/10.1007/s11664-999-0118-7>
[^agarwal-1998]: A. Agarwal, A. T. Fiory, H.-J. L. Gossmann, C. S.
    Rafferty and P. Frisella, "Ultra-shallow junction formation by spike
    annealing in a lamp-based or hot-walled rapid thermal annealing
    system: effect of ramp-up rate", *Materials Science in Semiconductor
    Processing* **1**(3–4), 237–241 (1998).
    <https://doi.org/10.1016/S1369-8001(98)00030-4>
[^shishiguchi-1997]: S. Shishiguchi, A. Mineji, T. Hayashi and S. Saito,
    "Boron Implanted Shallow Junction Formation By
    High-temperature/Short-time/high-ramping-rate (400 °C/sec) RTA",
    *1997 Symposium on VLSI Technology, Digest of Technical Papers*,
    pp. 89–90. <https://doi.org/10.1109/VLSIT.1997.623709>
[^rev-05]: E. C. Jones and E. Ishida, "Shallow junction doping
    technologies for ULSI", *Materials Science and Engineering: R*
    **24**(1–2), 1–80 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00013-8>
[^pat-spike-ibm]: K. L. Lee, Y. Zhang, M. Surendra and E. M. Sikorski
    (IBM), *Sacrificial polysilicon sidewall process and rapid thermal
    spike annealing for advance CMOS fabrication*, US 6,518,136 B2,
    granted 2003-02-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6518136>
[^wiki-rtp]: Wikipedia, *Rapid thermal processing*.
    <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
[^pat-spike-amat-ambient]: D. Jennings, S. Tallavarjula and R. Thakur
    (Applied Materials), *Optimal spike anneal ambient*, US 6,803,297
    B2, granted 2004-10-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6803297>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-10]: R. B. Fair (ed.), *Rapid Thermal Processing: Science and
    Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7; R. B.
    Fair, "Junction Formation in Silicon by Rapid Thermal Annealing",
    pp. 169–226. <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
[^fiory-2002]: A. T. Fiory, "Recent developments in rapid thermal
    processing", *Journal of Electronic Materials* **31**(10), 981–987
    (2002). <https://doi.org/10.1007/s11664-002-0031-9>
[^pat-spike-amat]: B. Ramachandran, R. Jallepally, R. C. Boas,
    S. Ramamurthy, A. Al-Bayati, H. Graoui and J. M. Spear (Applied
    Materials), *Advances in spike anneal processes for ultra shallow
    junctions*, US 6,897,131 B2, granted 2005-05-24.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6897131>
[^ag-8800]: SemiStar Corp., *AG Associates Heatpulse 8800 / 8808 Rapid
    Thermal Processing* (reseller specification page), accessed
    2026-08-30.
    <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
[^roozeboom-1990]: F. Roozeboom and N. Parekh, "Rapid thermal processing
    systems: A review with emphasis on temperature control", *Journal of
    Vacuum Science & Technology B* **8**(6), 1249–1259 (1990).
    <https://doi.org/10.1116/1.584902>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^ag-8108]: SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 / 8800
    / 8800i Specifications* (reseller PDF; operating specifications for
    the Heatpulse 4100 and 8108), accessed 2026-08-30.
    <https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pat-spe-amd]: B. Yu (Advanced Micro Devices), *Solid phase epitaxy
    activation process for source/drain junction extensions and halo
    regions*, US 6,521,502 B1, granted 2003-02-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6521502>
[^pat-rtp-amat]: C. M. Gronet and J. F. Gibbons (Applied Materials),
    *Rapid thermal heating apparatus and method*, US 5,155,336 A,
    granted 1992-10-13.
    <https://patents.google.com/patent/US5155336A/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
