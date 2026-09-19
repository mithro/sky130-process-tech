(step-010)=
# Step 010 — LINOX: LINOX oxidation

| | |
|---|---|
| **Step number** | 10 of 171[^steps-sheet] |
| **Step code** | `LINOX` |
| **Category** | {ref}`Thermal oxidation <category-oxidation>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`DNIS <step-009>` |
| **Next step** | {ref}`FILOX <step-011>` |

## What this step is

`LINOX` (liner oxidation) grows a thin thermal oxide on the exposed
silicon inside the isolation trenches — the floor and sidewalls cut at
{ref}`STIE <step-006>` — before the trenches are filled with deposited
oxide at {ref}`FILOX <step-011>`. The active areas, still covered by
the nitride from {ref}`ISONIT <step-003>`, do not oxidise (apart from
a small encroachment at the nitride edge). The result is a *trench
liner* of the order of 10–30 nm of high-quality thermal SiO₂ lining
every trench.

Public numbers for comparable flows: a Spansion STI patent that later
passed to Cypress, contemporaneous with the 130 nm node but not
evidence for S8 (see *Open questions*), grows a first liner "to a
thickness of approximately 100-300 Å"
at "900-1100 degrees Celsius" and, in its double-liner variant, a
second of "approximately 100-500 Å";[^pat-sti-cr] a Lattice patent
(scoped to "90 nm or less") grows a 3 nm liner everywhere and then
thickens it, with "a high temperature (for example, in excess of
approximately 1000 degrees C.) oxide growth process", to "a thickness
in the range of approximately 10 nm to approximately 30 nm" in the
trenches beside its high-voltage transistors;[^pat-sti-lattice] an
AmberWave Systems patent (now TSMC-owned) notes the alternative that
"the liner oxidation may take place in a wet, i.e., steam ambient
and/or at a low temperature, i.e., <1000° C.".[^pat-sti-amberwave] No
SkyWater source gives the SKY130 liner
thickness or temperature.

## Step category

`LINOX` is a {ref}`Thermal oxidation <category-oxidation>` step, like
{ref}`BOX <step-002>` before it, but its purpose is different: it is
grown on *etched* silicon, on vertical and sloped surfaces, and its
main job is to repair and passivate rather than to buffer stress.
In SKY130 it is also, by position, the first high-temperature step
after the deep N-well implant ({ref}`DNI <step-008>`), so it doubles
as that implant's first anneal.

## Why this step exists

The liner oxidation does four things that a deposited fill oxide
cannot:

1. **Removes etch damage.** The HBr/Cl₂ plasma leaves the trench
   surfaces amorphised, rough and contaminated with bromine and
   carbon. Growing a thermal oxide consumes the damaged layer (46 % of
   the grown oxide thickness lies below the original
   surface[^wiki-thox]) and buries it in a clean, stoichiometric
   SiO₂/Si interface. A 0.13 µm STI paper describes liner oxidation as
   included "to control the STI corner rounding to reduce the junction
   leakage and fix the damaged induced during STI plasma dry
   etch".[^thung-2016]
2. **Rounds the corners.** A sharp convex corner is consumed from two
   sides at once, and above about 1000 °C the oxide flows viscously
   enough to relieve the stress that non-planar growth builds up, so
   the sharp top corner of the trench is rounded — reducing the field
   crowding that causes the sub-threshold "double hump" and gate-oxide
   thinning at the active edge.[^itrs-01][^rev-01][^txt-01] Oxidation
   on curved surfaces is in fact *retarded* relative to planar silicon:
   Kao et al. found the retardation strongest "at low temperatures and
   sharp curvatures" and "more severe on concave than convex
   structures",[^kao-1987][^kao-1988] which is one reason a hot liner
   oxidation rounds better. The Spansion patent's whole subject
   is using "double liner oxidation" plus "double sacrificial
   oxidation" so that "corners of the trenches are substantially
   rounded by the four oxidation processes".[^pat-sti-cr]
3. **Provides a low-defect interface.** Junction leakage from the
   source/drain diffusions that later abut the trench depends on the
   quality of the trench-sidewall interface; thermal oxide has orders
   of magnitude fewer interface states than deposited oxide.[^txt-01]
4. **Anneals the deep N-well implant.** In SKY130's order, `LINOX` is
   the first furnace step after {ref}`DNI <step-008>`; its temperature
   is high enough to remove the MeV implant damage and begin the
   diffusion that merges the buried layer with the later N-well ring
   (see the discussion at {ref}`DNM <step-007>`).

## How it is typically performed

An industry-generic liner oxidation for a 200 mm, 130 nm-era fab:

1. **Pre-oxidation clean.** After the resist strip
   ({ref}`DNIS <step-009>`), an {term}`SC-1`/{term}`SC-2` clean and a *short* dilute-HF
   dip. The HF dip serves two purposes: it removes the chemical oxide
   so that the liner grows on clean silicon, and it deliberately
   undercuts the pad oxide at the nitride edge — "approximately
   100-300 Å of the pad oxide 26 is removed in the
   undercut"[^pat-sti-cr] — so that the liner oxidation can lift the
   nitride corner and round the top of the trench.
2. **Furnace oxidation.** Vertical furnace, dry O₂ at
   900–1100 °C,[^pat-sti-cr][^pat-sti-lattice] or a dilute-steam or
   in-situ-steam ambient at somewhat lower
   temperature.[^pat-sti-amberwave] Thermal oxidation in general runs
   between 800 and 1200 °C;[^wiki-thox] SkyWater's furnaces offer "dry
   oxidation to 1150C" and "wet oxidation to 1150C".[^skw-01] A dry,
   high-temperature recipe gives the best corner rounding and viscous
   stress relief; an HCl or DCE addition is sometimes used for
   metallic {term}`gettering`.
3. **Optional nitridation.** Some flows anneal the liner in NH₃ or NO
   to form a thin {term}`oxynitride`, or deposit a thin nitride liner, to
   block oxidant diffusion during later oxidations and to stop the
   HDP oxide's hydrogen reaching the interface (silane-based HDP oxide
   retains some hydrogen, and keeping it away from the Si/SiO₂
   interface is one motive[^txt-05]).
4. **Metrology.** Liner thickness on a bare monitor wafer by
   ellipsometry; corner shape by cross-section SEM on sample lots.

The liner is thin, so its silicon consumption (about 5–15 nm) barely
changes the trench dimensions, but it does slightly narrow the active
width because of the encroachment under the nitride edge.

## Machines typically used

* **{ref}`Vertical oxidation furnace <machine-vertical-furnace-oxidation>`** (as for {ref}`BOX <step-002>`):
  SVG/Thermco–ASML–Aviza AVP/RVP, Kokusai, TEL Alpha-8, ASM A400.
  Some fabs use a {ref}`single-wafer <machine-rapid-thermal-processor>` {term}`RTP` tool for in-situ-steam liner
  oxidation instead.
* **{ref}`Wet bench <machine-wet-bench>`** for the pre-oxidation clean and HF dip.
* **{ref}`Ellipsometer <machine-film-thickness-metrology>`**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **Aviza furnace.** SkyWater states "Furnaces are all made by Aviza",
  with dry and wet oxidation to 1150 °C.[^skw-01] Strength: strong for
  the furnace fleet; assignment of `LINOX` to a furnace rather than an
  RTP tool is our inference (SkyWater's RTP tool, the "Ag Heatpulse
  8808", is listed with NH₃/Ar/N₂/O₂ to 1200 °C,[^skw-01] so an RTP
  liner is not excluded; strength: weak for the Heatpulse as an
  alternative).
* **DNS / FSI Mercury HF/SC1/SC2 bench** for the pre-oxidation
  clean.[^skw-01] Strength: strong for existence; the assignment is an
  inference from their HF/SC1/SC2 chemistry, SC-2 being listed only for
  these two benches.

## Resources required

* **{ref}`Oxygen <material-process-gases>`** (dry) and possibly **hydrogen** for steam.[^wiki-thox]
* **Nitrogen** for purge and ramp.
* **Optional HCl or trans-dichloroethylene (DCE)** for chlorine
  gettering; **{ref}`NH₃ <material-precursors>` or NO** if a nitridation is used.[^txt-01]
* **Dilute HF, SC-1, SC-2 chemicals** ({ref}`wet chemicals <material-wet-chemicals>`) for the pre-clean.[^wiki-rca]
* {ref}`Quartz consumables <material-hardware-consumables>` and {ref}`monitor wafers <material-substrates>`.

## Related steps and cross-references

* Previous: {ref}`DNIS <step-009>` (clean wafer with open trenches).
* Next: {ref}`FILOX <step-011>` (HDP oxide fill over this liner).
* Trench cut at {ref}`STIE <step-006>`; nitride mask from
  {ref}`ISONIT <step-003>`; pad oxide from {ref}`BOX <step-002>`.
* First anneal of {ref}`DNI <step-008>`.
* Category page: {ref}`Thermal oxidation <category-oxidation>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.** 20 families concern this page (12 unknown, 8 expired); see {ref}`patents-by-module` for the full, grouped list (families still in force or of unknown status are collapsed there too).
<!-- index-links:end -->

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — Aviza furnaces; oxidation to
  1150 °C; Heatpulse 8808 RTP; pre-clean benches.[^skw-01]
* Kim et al. (Spansion), US 7,439,141 — liner thickness and
  temperature, pad-oxide undercut, double liner
  oxidation.[^pat-sti-cr]
* Mehta, Logie and Fong (Lattice), US 7,985,656 — a 10–30 nm liner
  grown above 1000 °C.[^pat-sti-lattice]
* Currie and Lochtefeld (AmberWave), US 6,960,781 — the wet / below
  1000 °C liner alternative.[^pat-sti-amberwave]

### High-level understanding

* Wikipedia, *Thermal oxidation* — temperatures and silicon
  consumption.[^wiki-thox]
* Wikipedia, *RCA clean* — the pre-oxidation clean.[^wiki-rca]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — oxidation;
  two-dimensional oxidation at corners.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — STI liner and
  corner rounding.[^txt-05]

### Deep dive

* Nandakumar et al., IEDM 1998 — corner rounding and liner choices in
  the STI review.[^rev-01]
* ITRS 2001, *Front End Processes* — STI corner rounding by thermal
  versus etch processes.[^itrs-01]
* Thung et al., *JTEC* 2016 — the liner oxidation's role in a 0.13 µm
  STI module.[^thung-2016]
* Kao et al., *IEEE TED* 1987 — experiments on two-dimensional
  oxidation of curved silicon, showing retardation at corners.[^kao-1987]
* Kao et al., *IEEE TED* 1988 — the viscous-stress model of corner
  oxidation in wet oxides.[^kao-1988]
* Deal and Grove, *J. Appl. Phys.* 1965 — the planar oxidation model
  that the corner results are measured against.[^deal-1965]
* Marcus and Sheng, *J. Electrochem. Soc.* 1982 — the first systematic
  study of oxidising shaped (trenched and stepped) silicon
  surfaces.[^marcus-1982]
* Kooi, van Lierop and Appels, *J. Electrochem. Soc.* 1976 — what
  happens at the nitride edge during oxidation (the Kooi
  effect).[^kooi-1976]
* Hu, *J. Appl. Phys.* 1991 — the stress fields generated by oxidising
  under a nitride mask and around trench corners.[^hu-1991]
* Bryant, Hänsch and Mii, IEDM 1994 — device consequences of the
  trench edge: leakage, hump and gate-oxide thinning.[^bryant-1994]
* Matsuda et al. (Toshiba), IEDM 1998 — a corner-rounding process that
  complements the liner oxidation.[^matsuda-1998]
* Watanabe et al., IEDM 1996 — corner-rounded STI to reduce
  stress-induced oxide leakage.[^watanabe-1996]
* Ohashi, Kubota and Nakajima, *IEEE EDL* 2007 — an argon anneal that
  suppresses gate-oxide thinning at the STI edge, a later view of the
  same problem.[^ohashi-2007]
* Nandakumar et al., IEDM 1997 — STI for sub-0.13 µm CMOS, including
  the liner and corner engineering.[^nandakumar-1997]
* Stanford Nanofabrication Facility, *Oxide Growth (furnace)* — a
  facility-level description of furnace oxidation practice.[^snf-oxide]

## Open questions

* The SKY130 liner thickness, ambient and temperature are not public;
  the 10–30 nm / 900–1100 °C figures are from third-party and
  Spansion-lineage patents.
* Whether SKY130 uses a single liner oxidation or a double liner /
  sacrificial-oxidation scheme of the Spansion-patent type[^pat-sti-cr]
  is unknown (that patent came into Cypress through Spansion in 2015,
  long after S8 was developed, and is not evidence for S8).
* Whether a nitride or oxynitride liner follows the oxide liner is not
  public.
* Whether the step is a furnace or an RTP oxidation is inferred.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pat-sti-cr]: U. Kim, Y. Sun, M. S. Chang et al. (Spansion LLC; later
    Cypress Semiconductor / Infineon), *Shallow trench isolation
    approach for improved STI corner rounding*, US 7,439,141 B2,
    priority 2001-12-27, granted 2008-10-21.
    <https://patents.google.com/patent/US7439141B2/en>
[^pat-sti-lattice]: S. Mehta, S. Logie and S. Fong (Lattice
    Semiconductor), *Shallow trench isolation (STI) with trench liner of
    increased thickness*, US 7,985,656 B1, granted 2011-07-26.
    <https://patents.google.com/patent/US7985656B1/en>
[^pat-sti-amberwave]: M. T. Currie and A. J. Lochtefeld (AmberWave
    Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
    Co. on 2010-01-26), *Shallow trench isolation process*,
    US 6,960,781 B2, granted 2005-11-01.
    <https://patents.google.com/patent/US6960781B2/en>
[^wiki-thox]: Wikipedia, *Thermal oxidation*.
    <https://en.wikipedia.org/wiki/Thermal_oxidation>
[^wiki-rca]: Wikipedia, *RCA clean*. <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9. <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://jtec.utem.edu.my/jtec/article/view/697> (times out as of
    2026-09-19; a Wayback Machine copy from 2026-04-11 confirms it was
    up; the PDF link below still works directly) (PDF:
    <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>).
[^kao-1987]: D.-B. Kao, J. P. McVittie, W. D. Nix and K. C. Saraswat,
    "Two-dimensional thermal oxidation of silicon — I. Experiments",
    *IEEE Transactions on Electron Devices* **34**(5), 1008–1017 (1987).
    <https://doi.org/10.1109/T-ED.1987.23037>
[^kao-1988]: D.-B. Kao, J. P. McVittie, W. D. Nix and K. C. Saraswat,
    "Two-dimensional thermal oxidation of silicon. II. Modeling stress
    effects in wet oxides", *IEEE Transactions on Electron Devices*
    **35**(1), 25–37 (1988). <https://doi.org/10.1109/16.2412>
[^deal-1965]: B. E. Deal and A. S. Grove, "General Relationship for the
    Thermal Oxidation of Silicon", *Journal of Applied Physics*
    **36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945>
[^marcus-1982]: R. B. Marcus and T. T. Sheng, "The Oxidation of Shaped
    Silicon Surfaces", *Journal of The Electrochemical Society*
    **129**(6), 1278–1282 (1982). <https://doi.org/10.1149/1.2124118>
[^kooi-1976]: E. Kooi, J. G. van Lierop and J. A. Appels, "Formation of
    Silicon Nitride at a Si–SiO₂ Interface during Local Oxidation of
    Silicon and during Heat-Treatment of Oxidized Silicon in NH₃ Gas",
    *Journal of The Electrochemical Society* **123**(7), 1117–1120
    (1976). <https://doi.org/10.1149/1.2133008>
[^hu-1991]: S. M. Hu, "Stress-related problems in silicon technology",
    *Journal of Applied Physics* **70**(6), R53–R80 (1991).
    <https://doi.org/10.1063/1.349282>
[^bryant-1994]: A. Bryant, W. Hänsch and T. Mii, "Characteristics of
    CMOS device isolation for the ULSI age", *Proc. 1994 IEEE
    International Electron Devices Meeting*, pp. 671–674.
    <https://doi.org/10.1109/IEDM.1994.383292>
[^matsuda-1998]: S. Matsuda, T. Sato, H. Yoshimura, Y. Takegawa,
    A. Sudo, I. Mizushima, Y. Tsunashima and Y. Toyoshima, "Novel
    corner rounding process for shallow trench isolation utilizing MSTS
    (Micro-Structure Transformation of Silicon)", *IEDM 1998 Technical
    Digest*, pp. 137–140. <https://doi.org/10.1109/IEDM.1998.746298>
[^watanabe-1996]: H. Watanabe, K. Shimizu, Y. Takeuchi and S. Aritome,
    "Corner-rounded shallow trench isolation technology to reduce the
    stress-induced tunnel oxide leakage current for highly reliable
    flash memories", *IEDM 1996 Technical Digest*, pp. 833–836.
    <https://doi.org/10.1109/IEDM.1996.554109>
[^ohashi-2007]: T. Ohashi, T. Kubota and A. Nakajima, "Ar Annealing for
    Suppression of Gate Oxide Thinning at Shallow Trench Isolation
    Edge", *IEEE Electron Device Letters* **28**(7), 562–564 (2007).
    <https://doi.org/10.1109/LED.2007.899328>
[^nandakumar-1997]: M. Nandakumar, S. Sridhar, S. Nag, P. Mei,
    D. Rogers, M. Hanratty, A. Amerasekera and I.-C. Chen, "A shallow
    trench isolation for sub-0.13 µm CMOS technologies", *IEDM 1997
    Technical Digest*, pp. 657–660.
    <https://doi.org/10.1109/IEDM.1997.650469>
[^snf-oxide]: Stanford Nanofabrication Facility, *Oxide Growth
    (furnace)*, processing-technique page.
    <https://snfguide.stanford.edu/guide/equipment/processing-technique/annealing-oxidation/oxide-growth-furnace>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
