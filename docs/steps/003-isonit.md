(step-003)=
# Step 003 — ISONIT: Iso nitride deposition

| | |
|---|---|
| **Step number** | 3 of 171 |
| **Step code** | `ISONIT` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`BOX <step-002>` |
| **Next step** | {ref}`FOM <step-004>` |

## What this step is

`ISONIT` ("isolation nitride") deposits a blanket film of silicon
nitride (Si₃N₄) by low-pressure chemical vapour deposition (LPCVD) on
top of the pad oxide from {ref}`BOX <step-002>`. The nitride is the
hard mask of the STI module: it is patterned at
{ref}`FOM <step-004>`/{ref}`STINITE <step-005>`, protects the future
active areas during the silicon trench etch ({ref}`STIE <step-006>`)
and the liner oxidation ({ref}`LINOX <step-010>`), and acts as the
polish stop for the oxide CMP ({ref}`CMPNIT <step-012>`). It is removed
at {ref}`NS19 <step-013>`.

Precisely: a stoichiometric LPCVD nitride of the order of 100–200 nm
is deposited in a furnace from dichlorosilane and ammonia. An AmberWave
Systems STI patent gives the mask nitride as "500-2000 Å"
(PAT-STI-AMBERWAVE); Wikipedia's
STI outline calls it the "protective nitride" (WIKI-STI). No public
SkyWater source gives the SKY130 value. The thickness is a compromise:
thick enough to survive the trench etch and the CMP with margin, thin
enough to keep the trench aspect ratio (trench depth *plus* nitride,
divided by trench width) manageable for the HDP fill — a paper on
0.13 µm STI defines the fill aspect ratio exactly that way, as "the
ratio of the sum of the STI trench depth and pad nitride thickness to
the minimum space design rule critical dimension" (THUNG-2016).

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
  LOCOS mask; WIKI-SIN illustrates "local silicon oxidation through an
  Si₃N₄ mask");
* a **CMP stop** — the oxide fill polishes much faster than nitride in
  a suitable slurry, so the polish at {ref}`CMPNIT <step-012>` can be
  stopped on it across the whole wafer (an AmberWave Systems STI
  patent, now TSMC-owned, describes "planarizing the substrate,
  typically via chemical-mechanical polishing (CMP), using the silicon
  nitride layer over the active area as a stop layer",
  PAT-STI-AMBERWAVE);
* a **plasma-etch mask** for the silicon trench etch, with good
  selectivity against HBr/Cl₂ chemistry (TXT-05);
* **selectively removable** afterwards in hot phosphoric acid, which
  etches nitride at ~100 Å/min while barely touching oxide (VGH-1967).

Its thickness also sets the height of the oxide "fence" left standing
above the silicon after the nitride is stripped, which is why the final
field-oxide step height above the active surface (0.07 µm under poly,
PDK-03) is tied to the choices made here.

## How it is typically performed

An industry-generic recipe for a 200 mm, 130 nm-era fab:

* **Deposition chemistry.** Dichlorosilane (SiH₂Cl₂, "DCS") and ammonia:
  3 SiCl₂H₂ + 4 NH₃ → Si₃N₄ + 6 HCl + 6 H₂ (WIKI-SIN, WIKI-CVD). LPCVD
  nitride is deposited at roughly 700–800 °C and a few hundred mTorr in
  a hot-wall furnace; an NH₃ : DCS ratio well above the stoichiometric
  4 : 3 is used to keep the film silicon-poor and stoichiometric
  (TXT-02). The Cypress ONO patents describe the same DCS/NH₃ LPCVD
  chemistry for the SONOS nitride, at "about 700° C. to about 875° C."
  (PAT-01) and 700–850 °C, 5–500 mTorr (PAT-02), which shows that this
  chemistry is native to the Cypress furnace set.
* **Film properties.** Stoichiometric LPCVD nitride is under about
  1 GPa of tensile stress and has a refractive index near 2.0; both are
  monitored as process-control signals (TXT-02).
* **Sequence.** Load 100–150 wafers, pump down, leak check, ramp to
  temperature under N₂, stabilise NH₃, add DCS for the deposition time,
  purge, back-fill, unload. Deposition rates are of the order of a few
  nm/min, so a 150 nm film takes tens of minutes.
* **Metrology.** Thickness and index by ellipsometry; stress by wafer
  bow on monitor wafers; particle scan.

SkyWater's capability page lists LPCVD nitride explicitly among its
furnace processes (SKW-01), along with BTBAS low-temperature nitride,
which is a different (later-generation) precursor.

## Machines typically used

* **Vertical LPCVD furnace** with vacuum pumping, DCS and NH₃ gas
  panel and HCl-tolerant exhaust scrubbing. Representative 200 mm-era
  tools: SVG/Thermco–ASML–Aviza AVP/RVP series, Kokusai DD/Vertron,
  TEL Alpha-8S, ASM A400.
* **Ellipsometer** and **stress gauge** for process control.

## Machines likely used at SkyWater

* **Aviza furnace running LPCVD nitride.** SKW-01: "Furnaces are all
  made by Aviza", with LPCVD nitride among the listed processes.
  Strength: strong. Vertical configuration: weak (job-board snippet and
  a used-equipment listing for the AVP-8000, AVIZA-AVP).
* No public source names the specific tube used for the isolation
  nitride versus the gate-stack or spacer nitrides.

## Resources required

* **Dichlorosilane (SiH₂Cl₂)** and **ammonia (NH₃)** process gases
  (WIKI-SIN).
* **Nitrogen** for purge and ramp.
* **HCl-tolerant exhaust / scrubber** — the reaction by-product is HCl
  and ammonium chloride condenses in the pump lines, a well-known
  maintenance load on nitride tubes (TXT-02).
* **Quartz or silicon-carbide tube and boat**; tube-cleaning
  chemistry (typically NF₃ or a wet HF clean, TXT-02).
* **Monitor wafers.**

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

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (Aviza furnaces; LPCVD nitride; BTBAS nitride).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions* ("field
  oxide (above silicon surface) … underneath poly" 0.07 µm).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **PAT-01** — K. Ramkumar et al. (Cypress), US 6,969,689 B1, *Method
  of manufacturing an oxide-nitride-oxide (ONO) dielectric for
  SONOS-type devices*, granted 2005-11-29 (DCS/NH₃ LPCVD nitride).
  <https://patents.google.com/patent/US6969689B1/en>
* **PAT-02** — S. Levy et al. (Cypress), US 2009/0179253 A1,
  *Oxide-nitride-oxide stack having multiple oxynitride layers*,
  published 2009-07-16 (LPCVD 700–850 °C, 5–500 mTorr).
  <https://patents.google.com/patent/US20090179253A1/en>
* **PAT-STI-AMBERWAVE** — M. T. Currie and A. J. Lochtefeld (AmberWave
  Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
  Co. on 2010-01-26), US 6,960,781 B2, *Shallow trench isolation
  process*, granted 2005-11-01 (nitride mask 500–2000 Å).
  <https://patents.google.com/patent/US6960781B2/en>
* **VGH-1967** — W. van Gelder and V. E. Hauser, *J. Electrochem. Soc.*
  114 (1967) 869, DOI 10.1149/1.2426757.
  <https://iopscience.iop.org/article/10.1149/1.2426757>
* **AVIZA-AVP** — Moov listing, *Aviza / SVG / Thermco AVP-8000*,
  accessed 2026-08-30.
  <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>

### High-level understanding

* **WIKI-SIN** — Wikipedia, *Silicon nitride* (LPCVD reaction, hot
  H₃PO₄ etch, oxidation mask).
  <https://en.wikipedia.org/wiki/Silicon_nitride>
* **WIKI-CVD** — Wikipedia, *Chemical vapor deposition*.
  <https://en.wikipedia.org/wiki/Chemical_vapor_deposition>
* **WIKI-STI** — Wikipedia, *Shallow trench isolation*.
  <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4 (CVD chapter: LPCVD nitride).
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (STI chapter).
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **THUNG-2016** — B. J. Thung, K. Ibrahim, N. A. Manap and
  F. Salehuddin, "Challenges for 0.13µm Generation Shallow Trench
  Isolation on 0.18µm Equipment Platform", *Journal of
  Telecommunication, Electronic and Computer Engineering* 8(5), 2016,
  pp. 15–21.
  <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>
* **REV-01** — M. Nandakumar et al., "Shallow trench isolation for
  advanced ULSI CMOS technologies", *IEDM 1998*, pp. 133–136,
  DOI 10.1109/IEDM.1998.746297.

## Open questions

* The SKY130 isolation-nitride thickness, deposition temperature and
  pressure are not public; 100–200 nm and 700–800 °C are era-typical
  values from the cited patents and textbooks.
* Whether a thin oxide cap or anti-reflective layer is deposited on the
  nitride before {ref}`FOM <step-004>` (some fabs do, to control
  reflectivity at 248 nm) is unknown.
* Whether SkyWater's nitride tube is a dedicated one or shared with the
  ONO and spacer nitrides is not public.
