(step-010)=
# Step 010 — LINOX: LINOX oxidation

| | |
|---|---|
| **Step number** | 10 of 171 |
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

Public numbers for comparable flows: a Spansion/Cypress-lineage STI
patent grows a first liner "to a thickness of approximately 100-300 Å"
at "900-1100 degrees Celsius" and, in its double-liner variant, a
second of "approximately 100-500 Å" (PAT-STI-CR); a Lattice patent uses
"a high temperature (for example, in excess of approximately 1000
degrees C.) oxide growth process" to reach "a thickness in the range
of approximately 10 nm to approximately 30 nm" (PAT-STI-LATTICE); an
AmberWave Systems patent (now TSMC-owned) notes the alternative that
"the liner oxidation may take place in a wet, i.e., steam ambient
and/or at a low temperature, i.e., <1000° C." (PAT-STI-AMBERWAVE). No
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
   the grown oxide thickness lies below the original surface,
   WIKI-THOX) and buries it in a clean, stoichiometric SiO₂/Si
   interface. A 0.13 µm STI paper describes liner oxidation as
   included "to control the STI corner rounding to reduce the junction
   leakage and fix the damaged induced during STI plasma dry etch"
   (THUNG-2016).
2. **Rounds the corners.** Oxidation proceeds faster at convex corners
   and is retarded by stress at concave ones, so the sharp top corner
   of the trench is rounded — reducing the field crowding that causes
   the sub-threshold "double hump" and gate-oxide thinning at the
   active edge (ITRS-01, REV-01). The Spansion patent's whole subject
   is using "double liner oxidation" plus "double sacrificial
   oxidation" so that "corners of the trenches are substantially
   rounded by the four oxidation processes" (PAT-STI-CR).
3. **Provides a low-defect interface.** Junction leakage from the
   source/drain diffusions that later abut the trench depends on the
   quality of the trench-sidewall interface; thermal oxide has orders
   of magnitude fewer interface states than deposited oxide (TXT-01).
4. **Anneals the deep N-well implant.** In SKY130's order, `LINOX` is
   the first furnace step after {ref}`DNI <step-008>`; its temperature
   is high enough to remove the MeV implant damage and begin the
   diffusion that merges the buried layer with the later N-well ring
   (see the discussion at {ref}`DNM <step-007>`).

## How it is typically performed

An industry-generic liner oxidation for a 200 mm, 130 nm-era fab:

1. **Pre-oxidation clean.** After the resist strip
   ({ref}`DNIS <step-009>`), an SC-1/SC-2 clean and a *short* dilute-HF
   dip. The HF dip serves two purposes: it removes the chemical oxide
   so that the liner grows on clean silicon, and it deliberately
   undercuts the pad oxide at the nitride edge — "approximately
   100-300 Å of the pad oxide 26 is removed in the undercut"
   (PAT-STI-CR) — so that the liner oxidation can lift the nitride
   corner and round the top of the trench.
2. **Furnace oxidation.** Vertical furnace, dry O₂ at 900–1100 °C
   (PAT-STI-CR, PAT-STI-LATTICE), or a dilute-steam or in-situ-steam
   ambient at somewhat lower temperature (PAT-STI-AMBERWAVE). Thermal
   oxidation in general runs between 800 and 1200 °C (WIKI-THOX);
   SkyWater's furnaces offer "dry oxidation to 1150C" and "wet
   oxidation to 1150C" (SKW-01). A dry, high-temperature recipe gives
   the best corner rounding and viscous stress relief; an HCl or DCE
   addition is sometimes used for metallic gettering.
3. **Optional nitridation.** Some flows anneal the liner in NH₃ or NO
   to form a thin oxynitride, or deposit a thin nitride liner, to
   block oxidant diffusion during later oxidations and to stop the
   HDP oxide's hydrogen reaching the interface (NISHIMURA-2002 reports
   that hydrogen from the SiH₄ plasma is incorporated into HDP-CVD
   oxide and drifts into underlying thermal oxide, degrading gate-oxide
   reliability).
4. **Metrology.** Liner thickness on a bare monitor wafer by
   ellipsometry; corner shape by cross-section SEM on sample lots.

The liner is thin, so its silicon consumption (about 5–15 nm) barely
changes the trench dimensions, but it does slightly narrow the active
width because of the encroachment under the nitride edge.

## Machines typically used

* **Vertical oxidation furnace** (as for {ref}`BOX <step-002>`):
  SVG/Thermco–ASML–Aviza AVP/RVP, Kokusai, TEL Alpha-8, ASM A400.
  Some fabs use a single-wafer RTP tool for in-situ-steam liner
  oxidation instead.
* **Wet bench** for the pre-oxidation clean and HF dip.
* **Ellipsometer**, **cross-section SEM**.

## Machines likely used at SkyWater

* **Aviza furnace.** SKW-01: "Furnaces are all made by Aviza"; dry and
  wet oxidation to 1150 °C. Strength: strong for the furnace fleet;
  assignment of `LINOX` to a furnace rather than an RTP tool is our
  inference (SkyWater's RTP tool, the "Ag Heatpulse 8808", is listed
  with NH₃/Ar/N₂/O₂ to 1200 °C, SKW-01, so an RTP liner is not
  excluded).
* **DNS / FSI Mercury HF/SC1/SC2 bench** for the pre-oxidation clean
  (SKW-01). Strength: strong for existence.

## Resources required

* **Oxygen** (dry) and possibly **hydrogen** for steam (WIKI-THOX).
* **Nitrogen** for purge and ramp.
* **Optional HCl or trans-dichloroethylene (DCE)** for chlorine
  gettering; **NH₃ or NO** if a nitridation is used (TXT-01).
* **Dilute HF, SC-1, SC-2 chemicals** for the pre-clean (WIKI-RCA).
* Quartz consumables and monitor wafers.

## Related steps and cross-references

* Previous: {ref}`DNIS <step-009>` (clean wafer with open trenches).
* Next: {ref}`FILOX <step-011>` (HDP oxide fill over this liner).
* Trench cut at {ref}`STIE <step-006>`; nitride mask from
  {ref}`ISONIT <step-003>`; pad oxide from {ref}`BOX <step-002>`.
* First anneal of {ref}`DNI <step-008>`.
* Category page: {ref}`Thermal oxidation <category-oxidation>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (Aviza furnaces; oxidation to 1150 °C; Heatpulse
  8808 RTP).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **PAT-STI-CR** — U. Kim et al. (Spansion LLC; later Cypress /
  Infineon), US 7,439,141 B2, *Shallow trench isolation approach for
  improved STI corner rounding*, granted 2008-10-21.
  <https://patents.google.com/patent/US7439141B2/en>
* **PAT-STI-LATTICE** — S. Mehta, S. Logie and S. Fong (Lattice),
  US 7,985,656 B1, *Shallow trench isolation (STI) with trench liner
  of increased thickness*, granted 2011-07-26.
  <https://patents.google.com/patent/US7985656B1/en>
* **PAT-STI-AMBERWAVE** — M. T. Currie and A. J. Lochtefeld (AmberWave
  Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
  Co. on 2010-01-26), US 6,960,781 B2, *Shallow trench isolation
  process*, granted 2005-11-01.
  <https://patents.google.com/patent/US6960781B2/en>

### High-level understanding

* **WIKI-THOX** — Wikipedia, *Thermal oxidation*.
  <https://en.wikipedia.org/wiki/Thermal_oxidation>
* **WIKI-RCA** — Wikipedia, *RCA clean*.
  <https://en.wikipedia.org/wiki/RCA_clean>
* **TXT-01** — J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon
  VLSI Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9
  (oxidation; two-dimensional oxidation at corners).
  <https://openlibrary.org/isbn/9780130850379>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (STI liner and corner
  rounding).
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **REV-01** — M. Nandakumar et al., "Shallow trench isolation for
  advanced ULSI CMOS technologies", *IEDM 1998*, pp. 133–136,
  DOI 10.1109/IEDM.1998.746297 (corner rounding).
* **ITRS-01** — ITRS 2001, *Front End Processes* (STI corner rounding
  by thermal versus etch processes).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* **THUNG-2016** — B. J. Thung et al., "Challenges for 0.13µm Generation
  Shallow Trench Isolation on 0.18µm Equipment Platform", *JTEC* 8(5),
  2016, pp. 15–21.
  <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>
* **NISHIMURA-2002** — H. Nishimura, S. Takagi, M. Fujino and N. Nishi,
  "Gap-Fill Process of Shallow Trench Isolation for 0.13 µm
  Technologies", *Japanese Journal of Applied Physics* 41 (2002)
  2886–2893, DOI 10.1143/JJAP.41.2886.

## Open questions

* The SKY130 liner thickness, ambient and temperature are not public;
  the 10–30 nm / 900–1100 °C figures are from third-party and
  Spansion-lineage patents.
* Whether SKY130 uses a single liner oxidation or a double liner /
  sacrificial-oxidation scheme of the PAT-STI-CR type is unknown (that
  patent came into Cypress through Spansion in 2015, long after S8 was
  developed, and is not evidence for S8).
* Whether a nitride or oxynitride liner follows the oxide liner is not
  public.
* Whether the step is a furnace or an RTP oxidation is inferred.
