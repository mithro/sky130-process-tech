(step-012)=
# Step 012 — CMPNIT: CMP over nitride

| | |
|---|---|
| **Step number** | 12 of 171 |
| **Step code** | `CMPNIT` |
| **Category** | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`FILOX <step-011>` |
| **Next step** | {ref}`NS19 <step-013>` |

## What this step is

`CMPNIT` (chemical-mechanical polish, stopping on nitride) removes the
fill oxide from {ref}`FILOX <step-011>` everywhere *except* inside the
trenches. The wafer is pressed face-down against a rotating polishing
pad flooded with abrasive slurry until the oxide over the active
areas is gone and the polish lands on the nitride from
{ref}`ISONIT <step-003>`, which polishes far more slowly. What is left
is a planar surface of nitride islands (future active areas) and
oxide-filled trenches (future field oxide), level with one another.

This is the step that gives STI its defining advantage over LOCOS —
a flat surface — and Wikipedia's STI outline lists it as "Chemical-
mechanical polishing of the oxide" followed by "Removal of the
protective nitride" (WIKI-STI). Because the oxide is later recessed
slightly during the nitride/pad-oxide removal and subsequent cleans,
the final field-oxide step above the active silicon is small — 0.07 µm
under poly in the PDK's assumptions (PDK-03).

## Step category

`CMPNIT` is a {ref}`Chemical-mechanical planarisation <category-cmp>`
step — an oxide polish with a nitride stop. The later polishes in the
flow ({ref}`CMPP <step-090>` over poly, {ref}`CMPL <step-106>`,
{ref}`CMPM <step-116>` over metal levels, and the tungsten polishes
{ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`) planarise
interlevel dielectrics or clear metal; only this one uses a nitride
stop and only this one determines the height of the silicon islands.

## Why this step exists

Without planarisation the STI module would leave 0.5 µm of oxide
topography over every active area, which no lithography or gate etch
could handle. Beyond simply flattening, the polish controls:

* **Active-area nitride thickness after polish**, which sets how much
  oxide is left standing above the silicon once the nitride is
  stripped at {ref}`NS19 <step-013>`.
* **Dishing** of the oxide in wide trenches and **erosion** of the
  nitride in dense active regions. Dishing lowers the field oxide
  below the active surface locally and produces divots at active edges;
  erosion thins the nitride and the silicon beneath it. Both are
  pattern-density effects, and they are the reason wide field regions
  are filled with dummy active "waffles" (PDK-06: "fom_waffles" of
  0.5–4.08 µm) and the reason some flows once used a reverse-mask
  etch-back before the polish — Wikipedia mentions "the combination of
  resist etching-back (REB) and chemical mechanical polishing (CMP)"
  for STI (WIKI-CMP).
* **Defectivity** — scratches and residual slurry particles at this
  step become gate-oxide and poly defects.

## How it is typically performed

An industry-generic STI polish for a 200 mm, 130 nm-era fab:

1. **Tool.** Rotary multi-platen polisher with polyurethane pads; the
   pads "should be rigid in order to uniformly polish the wafer
   surface" and, being consumed, "must be regularly reconditioned"
   with a diamond conditioner (WIKI-CMP). Wafers are held in a carrier
   head with a retaining ring and, on 200 mm-era tools, a multi-zone
   pressure membrane.
2. **Slurry.** Two options, both in production use at the 130 nm node
   (REV-02):
   * *Fumed or colloidal silica* in an alkaline (KOH or NH₄OH)
     solution — the classic oxide slurry, with oxide : nitride
     selectivity of only about 3–4 : 1, which needs endpoint control or
     a reverse-mask scheme to avoid over-polishing the nitride.
   * *Ceria (CeO₂)* with surfactant additives — Wikipedia notes that
     "Typically, CMP uses cerium dioxide as the abrasive" (WIKI-CMP) —
     giving oxide : nitride selectivity of tens to one and a
     self-stopping polish, the "direct STI" approach that removed the
     reverse mask.
3. **Recipe.** A first platen removes the bulk oxide at high rate; a
   second platen with the selective slurry clears the oxide over the
   active areas and stops on nitride; a final platen buffs with
   DI water or a dilute slurry to remove particles. Down-force of a few
   psi and platen speeds of tens of rpm are typical (TXT-05).
4. **Endpoint.** Motor-current or optical (in-situ reflectometry)
   endpoint detects the transition from oxide to nitride; Wikipedia
   remarks that without endpoint "a lack of end points requires blind
   polishing" (WIKI-CMP). The remaining nitride thickness is checked
   post-polish by optical metrology.
5. **Post-CMP clean.** Double-sided brush scrub with dilute NH₄OH or
   surfactant, sometimes with a dilute HF step, then spin-rinse-dry —
   slurry residue must be removed before the wafer dries.
6. **Metrology.** Nitride and trench-oxide thickness maps; dishing and
   erosion by profilometry or AFM on test structures; defect scan.

SkyWater's capability page lists "AMAT Mirra CMP – oxide – nitride –
niobium – aluminum – tungsten" (SKW-01) — an oxide/nitride-capable
polisher, which is what this step needs.

## Machines typically used

* **Rotary CMP polisher**, 200 mm: Applied Materials Mirra (the
  200 mm-era multi-platen standard; SKW-01 lists it for oxide and
  nitride), Ebara EPO-222/EPO-300, Strasbaugh 6EC, SpeedFam-IPEC
  Avanti 472, Lam Teres.
* **Post-CMP brush scrubber** (OnTrak/Lam Synergy, SEZ/Lam DaVinci).
* **Film-thickness metrology** (Nanometrics, KLA-Tencor, Rudolph)
  and **profilometer/AFM**.

## Machines likely used at SkyWater

* **Applied Materials Mirra CMP.** SKW-01 names it and lists oxide and
  nitride among its applications. Strength: strong (SkyWater
  statement). Unverified job-board snippets also mention "AMAT Mirra
  and Mirra Mesa" (public-sources §4); weak.
* **Post-CMP clean** — SKW-01 lists the "SEZ223, Davinci" single-wafer
  tools (HF, DSP+HF) and SKW-07 mentions "the SEZ etcher tool".
  Strength: strong for existence; a brush scrubber is not named on
  any public page (open question).

## Resources required

* **Slurry** — silica-based or ceria-based STI slurry (REV-02,
  WIKI-CMP).
* **Polishing pads** (polyurethane) and **pad conditioners** (diamond
  discs) (WIKI-CMP).
* **DI water** in large volumes; **dilute NH₄OH / surfactant / dilute
  HF** for post-CMP cleaning.
* **Carrier-head consumables** — membranes, retaining rings.
* **Slurry supply and waste treatment** — CMP is one of the largest
  water and waste-water consumers in the fab (TXT-07).

## Related steps and cross-references

* Previous: {ref}`FILOX <step-011>` (film being polished).
* Next: {ref}`NS19 <step-013>` (nitride strip that exposes the active
  silicon and leaves the oxide standing).
* Nitride stop from {ref}`ISONIT <step-003>`; pattern-density
  "waffles" from {ref}`FOM <step-004>`.
* Other CMP steps: {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`,
  {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`,
  {ref}`CMPM <step-116>`.
* Category page: {ref}`Chemical-mechanical planarisation <category-cmp>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 ("AMAT Mirra CMP – oxide – nitride – niobium –
  aluminum – tungsten"; SEZ223 / DaVinci).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SKW-07** — SkyWater Technology, *A Day in the Life of a SkyWater
  Maintenance Technician*, 2023-12-14.
  <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions* (field
  oxide 0.07 µm above silicon under poly).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **PDK-06** — SkyWater PDK Authors, *Layers Reference*
  ("fom_waffles").
  <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>
* **PAT-STI-AMBERWAVE** — M. T. Currie and A. J. Lochtefeld (AmberWave
  Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
  Co. on 2010-01-26), US 6,960,781 B2, granted 2005-11-01
  ("chemical-mechanical polishing
  (CMP), using the silicon nitride layer over the active area as a
  stop layer").
  <https://patents.google.com/patent/US6960781B2/en>
* **PAT-STI-CR** — U. Kim et al. (Spansion), US 7,439,141 B2, granted
  2008-10-21 (isolation oxide "polished back … approximately level
  with the nitride mask").
  <https://patents.google.com/patent/US7439141B2/en>

### High-level understanding

* **WIKI-CMP** — Wikipedia, *Chemical-mechanical polishing*.
  <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
* **WIKI-STI** — Wikipedia, *Shallow trench isolation*.
  <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (CMP chapter; STI CMP).
  <https://openlibrary.org/isbn/9780961672171>
* **TXT-07** — M. Quirk and J. Serda, *Semiconductor Manufacturing
  Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0 (CMP tools
  and consumables).
  <https://openlibrary.org/isbn/9780130815200>

### Deep dive

* **REV-02** — M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
  Mechanical Planarization: Slurry Chemistry, Materials, and
  Mechanisms", *Chemical Reviews* 110 (2010) 178–204,
  DOI 10.1021/cr900170z (silica and ceria slurries for oxide/STI).
* **REV-01** — M. Nandakumar et al., "Shallow trench isolation for
  advanced ULSI CMOS technologies", *IEDM 1998*, pp. 133–136,
  DOI 10.1109/IEDM.1998.746297 (STI planarisation).
* **THUNG-2016** — B. J. Thung et al., "Challenges for 0.13µm Generation
  Shallow Trench Isolation on 0.18µm Equipment Platform", *JTEC* 8(5),
  2016, pp. 15–21.
  <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>

## Open questions

* Whether SKY130 uses a silica or a ceria (high-selectivity) slurry,
  and whether a reverse-mask etch-back was ever part of the S8 flow,
  is not public.
* The target post-polish nitride thickness and the allowed dishing /
  erosion are not public.
* The post-CMP cleaning tool is not identified on any public SkyWater
  page.
* Applied Materials' own Mirra product pages could not be retrieved
  during writing (HTTP 403), so no vendor description of the tool is
  cited; SKW-01 is the only source used for it.
