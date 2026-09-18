(step-003)=
# Step 003 — ISONIT: Iso nitride deposition

| | |
|---|---|
| **Step number** | 3 of 171[^steps-sheet] |
| **Step code** | `ISONIT` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`BOX <step-002>` |
| **Next step** | {ref}`FOM <step-004>` |

## What this step is

`ISONIT` ("isolation nitride") deposits a blanket film of silicon
nitride (Si₃N₄) by low-pressure chemical vapour deposition ({term}`LPCVD`) on
top of the pad oxide from {ref}`BOX <step-002>`. The nitride is the
{term}`hard mask` of the {term}`STI` module: it is patterned at
{ref}`FOM <step-004>`/{ref}`STINITE <step-005>`, protects the future
active areas during the silicon trench etch ({ref}`STIE <step-006>`)
and the liner oxidation ({ref}`LINOX <step-010>`), and acts as the
polish stop for the oxide {term}`CMP` ({ref}`CMPNIT <step-012>`). It is removed
at {ref}`NS19 <step-013>`.

Precisely: a stoichiometric LPCVD nitride of the order of 150 nm — the
working figure used throughout this module, not a SkyWater number — is
deposited in a furnace from dichlorosilane and ammonia. An AmberWave
Systems STI patent gives the mask nitride as "500-2000 Å"
(50–200 nm);[^pat-sti-amberwave] Wikipedia's STI outline calls it the
"protective nitride".[^wiki-sti] No public SkyWater source gives the
SKY130 value, and the 150 nm used as a working figure on the later
pages of this module ({ref}`STINITE <step-005>`, {ref}`STIE <step-006>`,
{ref}`NS19 <step-013>`) sits in the upper half of the patent's range and is not a
SkyWater number. The thickness is a compromise: thick enough to survive
the trench etch and the CMP with margin, thin enough to keep the trench
{term}`aspect ratio` (trench depth *plus* nitride, divided by trench width)
manageable for the HDP fill — a paper on 0.13 µm STI defines the fill
aspect ratio exactly that way, as "the ratio of the sum of the STI
trench depth and pad nitride thickness to the minimum space design rule
critical dimension".[^thung-2016]

## Step category

`ISONIT` is a {ref}`Thin-film deposition <category-deposition>` step —
specifically a furnace LPCVD step, like the later
{ref}`SAGD <step-048>` polysilicon and {ref}`GATENIT <step-058>`
depositions. What is specific to this instance is that the film is
sacrificial and its mechanical properties (stress, density, polish
rate, wet-etch rate) matter more than its electrical ones.

## Why this step exists

Silicon nitride is used because it is the one common film that is
simultaneously:

* an **oxidation barrier** — oxygen does not diffuse through it, so
  the active silicon stays unoxidised during the liner oxidation at
  {ref}`LINOX <step-010>` (this is the same property that made it the
  {term}`LOCOS` mask; Wikipedia illustrates "local silicon oxidation through an
  Si₃N₄ mask"[^wiki-sin]);
* a **CMP stop** — the oxide fill polishes much faster than nitride in
  a suitable slurry, so the polish at {ref}`CMPNIT <step-012>` can be
  stopped on it across the whole wafer (an AmberWave Systems STI
  patent, now TSMC-owned, describes "planarizing the substrate,
  typically via chemical-mechanical polishing (CMP), using the silicon
  nitride layer over the active area as a stop
  layer"[^pat-sti-amberwave]);
* a **plasma-etch mask** for the silicon trench etch, with good
  {term}`selectivity` against HBr/Cl₂ chemistry;[^txt-05]
* **selectively removable** afterwards in hot phosphoric acid, which
  etches nitride at ~100 Å/min while barely touching oxide.[^vgh-1967]

Its thickness also sets the height of the oxide "fence" left standing
above the silicon immediately after the nitride is stripped. We read
the PDK's finished field-oxide step height above the active surface
(0.07 µm under poly, `FOXSTEP`[^pdk-03]) as the residue of that fence
after the CMP, the strip and the later oxide losses; no public source
states the relation.

## How it is typically performed

An industry-generic recipe for a 200 mm, 130 nm-era fab:

* **Deposition chemistry.** Dichlorosilane (SiH₂Cl₂, "DCS") and ammonia:
  3 SiCl₂H₂ + 4 NH₃ → Si₃N₄ + 6 HCl + 6 H₂.[^wiki-sin][^wiki-cvd] LPCVD
  nitride is deposited at roughly 700–800 °C and a few hundred mTorr in
  a hot-wall furnace; an NH₃ : DCS ratio well above the stoichiometric
  4 : 3 is used to keep the film silicon-poor and
  stoichiometric.[^txt-02] The same DCS/NH₃ LPCVD chemistry is used for
  the {term}`SONOS` nitride: one embodiment of US 6,969,689 forms the
  nitride at temperatures "from about 700° C. to about 875° C."[^pat-01]
  A later Cypress patent that may still be in force gives conditions for
  the closely related oxynitride deposition, in the collapsed note below
  this list, so the precursor set is native to the Cypress furnaces.
* **Film properties.** Stoichiometric LPCVD nitride is under about
  1 GPa of tensile stress and has a refractive index near 2.0; both are
  monitored as process-control signals.[^txt-02]
* **Sequence.** Load 100–150 wafers, pump down, leak check, ramp to
  temperature under N₂, stabilise NH₃, add DCS for the deposition time,
  purge, back-fill, unload. Deposition rates are of the order of a few
  nm/min, so a 150 nm film takes tens of minutes.
* **Metrology.** Thickness and index by ellipsometry; stress by wafer
  bow on monitor wafers; particle scan.

:::{dropdown} From a patent shown as in force (US 2009/0179253; estimated expiry 2027-06-17) — open to read
A later Cypress patent gives 700–850 °C and 5–500 mTorr for the
closely related N₂O/NH₃/DCS oxynitride deposition.[^pat-02]
:::

SkyWater's capability page lists LPCVD nitride explicitly among its
furnace processes,[^skw-01] along with BTBAS low-temperature nitride,
which is a different (later-generation) precursor.

## Machines typically used

* **{ref}`Vertical LPCVD furnace <machine-vertical-furnace-lpcvd>`** with vacuum pumping, DCS and NH₃ gas
  panel and HCl-tolerant exhaust scrubbing. Representative 200 mm-era
  tools: SVG/Thermco–ASML–Aviza AVP/RVP series, Kokusai DD/Vertron,
  TEL Alpha-8S, ASM A400.
* **{ref}`Ellipsometer <machine-film-thickness-metrology>`** and **stress gauge** for process control.

## Machines likely used at SkyWater

* **Aviza furnace running LPCVD nitride.** SkyWater states "Furnaces
  are all made by Aviza", with LPCVD nitride among the listed
  processes.[^skw-01] Strength: strong. Vertical configuration: not
  stated publicly; a used-equipment listing for the
  AVP-8000[^aviza-avp] shows the vendor's vertical 200 mm furnace
  (weak).
* No public source names the specific tube used for the isolation
  nitride versus the gate-stack or {term}`spacer` nitrides.

## Resources required

* **{ref}`Dichlorosilane <material-precursors>` (SiH₂Cl₂)** and **ammonia (NH₃)** process
  gases.[^wiki-sin]
* **{ref}`Nitrogen <material-process-gases>`** for purge and ramp.
* **{ref}`HCl-tolerant exhaust <material-hardware-consumables>` / scrubber** — the reaction by-product is HCl
  and ammonium chloride condenses in the pump lines, a well-known
  maintenance load on nitride tubes.[^txt-02]
* **Quartz or silicon-carbide tube and boat**; tube-cleaning
  chemistry (typically {ref}`NF₃ <material-etch-gases>` or a wet {ref}`HF clean <material-wet-chemicals>`).[^txt-02]
* **{ref}`Monitor wafers <material-substrates>`.**

## Related steps and cross-references

* Previous: {ref}`BOX <step-002>` (pad oxide under the nitride).
* Next: {ref}`FOM <step-004>` prints the active/field pattern on it.
* Etched at {ref}`STINITE <step-005>`; used as the mask at
  {ref}`STIE <step-006>` and {ref}`LINOX <step-010>`; polish stop at
  {ref}`CMPNIT <step-012>`; removed at {ref}`NS19 <step-013>`.
* Other nitride depositions: {ref}`ONO <step-040>` (SONOS charge-trap
  nitride), {ref}`GATENIT <step-058>`, {ref}`SPNIT <step-076>`,
  {ref}`LINIT <step-104>`, {ref}`NTSD <step-167>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 6,969,689 B1 <patent-gp35405131>` — Method of manufacturing an oxide-nitride-oxide (ONO) dielectric for SONOS-type devices (2002)
* {ref}`US 6,960,781 B2 <patent-gp32990685>` — Shallow trench isolation process (2003)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 2009/0179253 A1 <patent-gp40849883>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — Aviza furnaces; LPCVD
  nitride; BTBAS nitride.[^skw-01]
* SkyWater PDK, *Criteria & Assumptions* — "field oxide (above silicon
  surface) … underneath poly" 0.07 µm.[^pdk-03]
* Ramkumar et al. (Cypress), US 6,969,689 — DCS/NH₃ LPCVD nitride in
  the ONO stack.[^pat-01]
* Currie and Lochtefeld (AmberWave), US 6,960,781 — nitride mask
  500–2000 Å; CMP stop on nitride.[^pat-sti-amberwave]
* van Gelder and Hauser, *J. Electrochem. Soc.* 1967 — hot phosphoric
  etch rates.[^vgh-1967]
* Moov marketplace, Aviza / SVG / Thermco AVP-8000 listing
  (weak).[^aviza-avp]

:::{dropdown} From a patent shown as in force (US 2009/0179253; estimated expiry 2027-06-17) — open to read
* Levy et al. (Cypress), US 2009/0179253 — LPCVD at 700–850 °C,
  5–500 mTorr.[^pat-02]
:::

### High-level understanding

* Wikipedia, *Silicon nitride* — the LPCVD reaction, hot H₃PO₄ etch
  and use as an oxidation mask.[^wiki-sin]
* Wikipedia, *Chemical vapor deposition* — LPCVD in
  context.[^wiki-cvd]
* Wikipedia, *Shallow trench isolation* — the "protective
  nitride".[^wiki-sti]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — the
  {term}`CVD` chapter on LPCVD nitride.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — the STI
  chapter.[^txt-05]

### Deep dive

* Thung et al., *JTEC* 2016 — the fill-aspect-ratio definition that
  ties the nitride thickness to the HDP fill window.[^thung-2016]
* Nandakumar et al., IEDM 1998 — the STI review, including the
  stack and its role in corner rounding and CMP.[^rev-01]
* Roenigk and Jensen, *J. Electrochem. Soc.* 1987 — a reactor model of
  LPCVD nitride from DCS/NH₃, explaining thickness uniformity along a
  hot-wall tube.[^roenigk-1987]
* Peev, Zambov and Yanakiev, *Thin Solid Films* 1990 — the kinetics of
  the DCS–NH₃ reaction and how the deposition rate depends on gas
  ratio, pressure and temperature.[^peev-1990]
* Temple-Boyer et al., *J. Vac. Sci. Technol. A* 1998 — residual stress
  in LPCVD SiNₓ as a function of composition, the reason
  stoichiometric films are highly tensile.[^temple-boyer-1998]
* Habraken and Kuiper, *Mater. Sci. Eng. R* 1994 — a review of silicon
  nitride and {term}`oxynitride` films: growth, composition, hydrogen content
  and etch behaviour.[^habraken-1994]
* Stoney, *Proc. R. Soc. A* 1909 — the wafer-curvature relation used to
  turn a bow measurement into a film stress.[^stoney-1909]
* Hu, *J. Appl. Phys.* 1991 — how nitride stress on a pad oxide
  generates dislocations during later oxidation.[^hu-1991]
* Kooi, van Lierop and Appels, *J. Electrochem. Soc.* 1976 — the
  nitride mask's edge behaviour during oxidation (the Kooi
  effect).[^kooi-1976]
* Teasdale et al., *Electrochem. Solid-State Lett.* 2001 — single-wafer
  RTCVD of DCS/NH₃ nitride, the alternative to a batch
  furnace.[^teasdale-2001]
* Stanford Nanofabrication Facility, *Tystar LPCVD Tube Training* — a
  university facility guide to running a hot-wall LPCVD nitride
  tube.[^snf-lpcvd]

## Open questions

* The SKY130 isolation-nitride thickness, deposition temperature and
  pressure are not public; 50–200 nm from the cited patent and
  700–800 °C from the cited patents and textbooks are era-typical
  values.
* Whether a thin oxide cap or anti-reflective layer is deposited on the
  nitride before {ref}`FOM <step-004>` (some fabs do, to control
  reflectivity at 248 nm) is unknown.
* Whether SkyWater's nitride tube is a dedicated one or shared with the
  ONO and spacer nitrides is not public.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pat-01]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster
    (Cypress Semiconductor), *Method of manufacturing an
    oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*,
    US 6,969,689 B1, granted 2005-11-29.
    <https://patents.google.com/patent/US6969689B1/en>
[^pat-02]: S. Levy, K. Ramkumar, F. Jenne and S. Geha (Cypress
    Semiconductor), *Oxide-nitride-oxide stack having multiple
    oxynitride layers*, US 2009/0179253 A1, published 2009-07-16.
    <https://patents.google.com/patent/US20090179253A1/en>
    Shown as in force; estimated expiry 2027-06-17 (estimate from public
    records, not legal advice).
[^pat-sti-amberwave]: M. T. Currie and A. J. Lochtefeld (AmberWave
    Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
    Co. on 2010-01-26), *Shallow trench isolation process*,
    US 6,960,781 B2, granted 2005-11-01.
    <https://patents.google.com/patent/US6960781B2/en>
[^vgh-1967]: W. van Gelder and V. E. Hauser, "The Etching of Silicon
    Nitride in Phosphoric Acid with Silicon Dioxide as a Mask", *Journal
    of The Electrochemical Society* **114**(8), 869 (1967).
    <https://doi.org/10.1149/1.2426757>
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco
    AVP 8000* listing, accessed 2026-08-30.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^wiki-cvd]: Wikipedia, *Chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Chemical_vapor_deposition>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://jtec.utem.edu.my/jtec/article/view/697> (times out as of
    2026-09-19; a Wayback Machine copy from 2026-04-11 confirms it was
    up; the PDF link below still works directly) (PDF:
    <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>).
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^roenigk-1987]: K. F. Roenigk and K. F. Jensen, "Low Pressure CVD of
    Silicon Nitride", *Journal of The Electrochemical Society*
    **134**(7), 1777–1785 (1987). <https://doi.org/10.1149/1.2100756>
[^peev-1990]: G. Peev, L. Zambov and Y. Yanakiev, "Kinetics of the
    chemical reaction between dichlorosilane and ammonia during silicon
    nitride film deposition", *Thin Solid Films* **189**(2), 275–282
    (1990). <https://doi.org/10.1016/0040-6090(90)90456-N>
[^temple-boyer-1998]: P. Temple-Boyer, C. Rossi, E. Saint-Etienne and
    E. Scheid, "Residual stress in low pressure chemical vapor
    deposition SiNₓ films deposited from silane and ammonia", *Journal
    of Vacuum Science & Technology A* **16**(4), 2003–2007 (1998).
    <https://doi.org/10.1116/1.581302>
[^habraken-1994]: F. H. P. M. Habraken and A. E. T. Kuiper, "Silicon
    nitride and oxynitride films", *Materials Science and Engineering:
    R: Reports* **12**(3), 123–175 (1994).
    <https://doi.org/10.1016/0927-796X(94)90006-X>
[^stoney-1909]: G. G. Stoney, "The tension of metallic films deposited
    by electrolysis", *Proceedings of the Royal Society of London A*
    **82**(553), 172–175 (1909). <https://doi.org/10.1098/rspa.1909.0021>
[^hu-1991]: S. M. Hu, "Stress-related problems in silicon technology",
    *Journal of Applied Physics* **70**(6), R53–R80 (1991).
    <https://doi.org/10.1063/1.349282>
[^kooi-1976]: E. Kooi, J. G. van Lierop and J. A. Appels, "Formation of
    Silicon Nitride at a Si–SiO₂ Interface during Local Oxidation of
    Silicon and during Heat-Treatment of Oxidized Silicon in NH₃ Gas",
    *Journal of The Electrochemical Society* **123**(7), 1117–1120
    (1976). <https://doi.org/10.1149/1.2133008>
[^teasdale-2001]: D. Teasdale, Y. Senzaki, R. Herring, G. Hoeye,
    L. Page and P. Schubert, "LPCVD of Silicon Nitride from
    Dichlorosilane and Ammonia by Single Wafer Rapid Thermal
    Processing", *Electrochemical and Solid-State Letters* **4**(5),
    F11 (2001). <https://doi.org/10.1149/1.1359056>
[^snf-lpcvd]: Stanford Nanofabrication Facility, *Tystar LPCVD Tube
    Training*, equipment training page.
    <https://snfguide.stanford.edu/guide/equipment/training/tystar-lpcvd-tube-training>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
