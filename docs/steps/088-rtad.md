(step-088)=
# Step 088 — RTAD: RTA source drain implant anneal

| | |
|---|---|
| **Step number** | 88 of 171[^steps-sheet] |
| **Step code** | `RTAD` |
| **Category** | {ref}`Anneal / thermal processing <category-anneal>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`NSDIS <step-087>` |
| **Next step** | {ref}`PSG <step-089>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** heats the wafer so that the amorphous layers regrow, the
  dopant moves onto lattice sites and the junctions reach their
  designed depth.
* **Why:** implanted dopant does nothing until the lattice is repaired.
* **Public numbers:** "N+ or P+ S/D (XJ)" 0.1 µm;[^pdk-03] sheet
  resistance 120 Ω/sq (N-diffusion) and 197 Ω/sq
  (P-diffusion).[^pdk-08]
* **Likely SkyWater tool:** AG Associates Heatpulse 8808 — strong (tool,
  SkyWater statement); inference (assignment).[^skw-01]
* **Not public:** the anneal temperature, time, ramp rates and ambient,
  and why the flow has two source/drain anneals (→ Open questions).
:::

## What this step is

`RTAD` is the source/drain activation anneal. The three heavy implants
of the module — {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>` and
{ref}`NSDI <step-086>` — have left the source/drain silicon amorphised
and its dopant electrically inactive. This step heats the wafer so that
the amorphous layers regrow, the dopant moves onto lattice sites, the
end-of-range damage is dissolved as far as it can be, and the
junctions reach their designed depth and no further. It does so in an
inert ambient for seconds at around 1000 °C on the industry-typical
recipe described below; SKY130's own conditions are not public.

The designed depth is the PDK's 0.1 µm for "N+ or P+
S/D (XJ)".[^pdk-03] This reference describes `RTAD`,
like {ref}`RTAI <step-034>` and {ref}`TIPRTAD <step-075>`, as a rapid
thermal anneal, and the public evidence for that is good (below). It
is the third RTA described in this reference; the next,
{ref}`RTAD2 <step-092>`, is a second source/drain anneal
placed after the sacrificial PSG, the polish and the {term}`cap oxide`.

:::{figure} /_static/figures/sd-088-rtad.svg
:alt: One enlarged cross-section of one transistor edge. A capped gate with a nitride block and a thin oxide on its sidewall stands on a thin oxide. In the silicon a deep doped region runs from the left edge of the view to the outer foot of the sidewall films, and a shallow doped layer and a hatched region continue under them to the gate edge. The drawing is the same as the state before the step.
:width: 560px
:name: fig-sd-088-rtad

A close-up of the 1.8 V NMOS gate edge at the source/drain anneal, the finished front-end transistor edge of this module: the deep N⁺ source/drain outside the spacer, the tip under it, the halo around the tip, the nitride spacer and the spacer oxide over it. The anneal regrows the implanted silicon and activates the dopant; the deep junction's designed depth is 0.1 µm in the PDK's junction table ("N+ or P+ S/D (XJ)"), which is not drawn to scale.[^pdk-03] How far the junctions and the tip move is not public, and nothing the drawing shows moves. The temperature, time and ambient are not public; the page describes an industry-typical rapid thermal anneal. The colours mark the type of the doping, and the hatching where the halo implant is, not their profiles. The caps, the re-oxidation oxide, the gate oxide and the spacer oxide are drawn but not labelled, and the liner oxide is drawn faded; the P-well and the NCHI channel implant made earlier are not drawn. Not to scale.
:::

On the reading of the {ref}`NPCM <step-078>` page, the anneal is also
the thermal step that finishes the doping of the poly heads opened at
{ref}`NPCME <step-079>`. It re-anneals the
extensions and halos that {ref}`TIPRTAD <step-075>` activated, and
sets the final position of every front-end junction relative to the
gate edge. After it, the front end is electrically complete; what
follows is dielectric, contact and interconnect.

## Step category

`RTAD` is an {ref}`Anneal / thermal processing <category-anneal>` step
of the *implant activation* type — the same family as
{ref}`RTAI <step-034>` and {ref}`TIPRTAD <step-075>`, but with the
tightest constraint of the three:

* The well anneal could be hot and
  long.
* The tip anneal had shallow, light profiles to protect.
* This one
  has to activate doses of the order of 10¹⁵ cm⁻² to a low sheet
  resistance (the PDK's 120 Ω/sq for N-diffusion and 197 Ω/sq for
  P-diffusion[^pdk-08]). It has to do so while moving the deep junctions by only tens of
  nanometres and the extensions, which see this anneal for a second
  time, by less.

`RTAD` is the anneal for which the *spike* RTA was
developed.

## Why this step exists

Implanted dopant does nothing until the lattice is repaired.
Amorphised layers regrow by solid-phase epitaxy from about 500 °C,
at a rate that depends on orientation[^csepregi-1978] and, for
arsenic, on concentration,[^jeon-1989] incorporating the dopant
substitutionally up to and beyond its solubility. Partially damaged
layers need 800–1000 °C to dissolve the defect clusters, as the
category page sets out from Gibbons's review of damage production and
annealing[^gibbons-1972] and Plummer, Deal and Griffin[^txt-01].

Two
effects make the choice of
temperature and time a compromise, as the category page explains:

* **Transient enhanced diffusion.** The interstitials released as the
  damage dissolves raise boron's diffusivity many-fold for a short
  time.

  Michel et al. first reported the anomalous diffusion under
  rapid annealing,[^michel-1987] Eaglesham et al. traced it to the
  implant's own interstitials,[^eaglesham-1994] and Stolk et al. set
  out the mechanisms.[^stolk-1997] {term}`TED` is worst for slow,
  cool anneals, so the resolution is to go hot and fast.

  Agarwal,
  Gossmann and Fiory showed how the ramp rate of a rapid thermal
  anneal sets the depth of a boron junction,[^agarwal-1999] with
  Agarwal et al. comparing lamp-based and hot-walled spike
  anneals,[^agarwal-1998] and Agarwal reviewing ultra-shallow
  junction formation with conventional implantation and RTA.[^agarwal-2000]
  Fiory's review covers the RTP developments of the 130 nm
  era,[^fiory-2002] and Gerritsen the spike anneal as reduced-budget
  RTP.[^gerritsen-2000]
* **Activation and deactivation.** Above the solid solubility the
  dopant clusters or precipitates and becomes inactive — Nobili et al.
  for arsenic[^nobili-1983] — and arsenic that was over-activated by a
  fast anneal relaxes during later thermal steps, injecting
  interstitials as it does so.[^rousseau-1994][^luning-1992]

  The
  highest activation is obtained by annealing hot and fast; the most
  *stable* activation may not be, which is one reading of why a second
  source/drain anneal ({ref}`RTAD2 <step-092>`) exists in this flow
  (inference; no public source describes a second anneal).
  Camillo-Castillo et al. studied what a two-step
  anneal does to end-of-range defects.[^camillo-castillo-2002]

Josse et al. describe optimising the spike anneal for a 0.13 µm CMOS
platform with both digital and analogue devices,[^josse-2002] and
Matsuda, Shishiguchi and Kitajima an RTA process for shallow junctions
with high controllability[^matsuda-2002] — the class of recipe this
step belongs to.

The fluorine from BF₂ implants changes boron's
behaviour in exactly this anneal.[^wang-1997] The surrounding
films matter: boron out-diffuses into oxide and nitride spacers at
different rates.[^pelletier-2008] Shallow arsenic loses dose to
the surface during a nitrogen anneal,[^farhane-2003] which is, we infer, one reason
the {ref}`SPOX <step-080>` oxide is left in place as a cap (its
retention is not public).

Without `RTAD` the source/drains would be amorphous, inactive and
several orders of magnitude too resistive; every transistor, resistor
and diode in the PDK depends on it.

## How it is typically performed

*An industry-generic source/drain activation anneal for a 200 mm,
130 nm-era fab (SKY130's recipe is not public):*

* **Tool and ambient.** Single-wafer lamp-heated RTA in nitrogen or
  argon: RTP "heats silicon wafers to temperatures exceeding 1,000°C
  for not more than a few seconds" with "high intensity lamps" and
  "in situ pyrometry to effect real time control".[^wiki-rtp]

  A
  small oxygen addition is sometimes used to limit dopant
  out-diffusion; a pure inert ambient avoids growing oxide on the
  poly heads and source/drain (category page).
* **Temperature and time.** A soak of 1000–1050 °C for a few seconds,
  or a spike with no soak — a ramp of 100–250 °C/s to a peak near
  1050 °C and immediate cooling — are the typical 130 nm-era
  choices.[^txt-05][^txt-10]

  ITRS 2001 sets the junction depth,
  abruptness and sheet resistance that the anneal must meet
  together.[^itrs-01] Ramp rates of "1 – 180°C per second" are the
  range of the AG Associates Heatpulse 8800-class tools.[^ag-8800]
* **Sequence.** Pre-anneal clean (at {ref}`NSDIS <step-087>`); load;
  purge; a low-temperature stabilisation step for pyrometer lock;
  ramp; soak or spike; controlled ramp-down; unload.
* **Control.** The pyrometer must be corrected for the wafer's
  emissivity, which depends on its films and temperature.

  Sorrell
  and Gyurcsik describe model-based emissivity correction,[^sorrell-1993]
  and Chen et al. measured the effects of wafer emissivity on RTP
  temperature measurement.[^chen-2002-rtp] Vandenabeele and Renken
  report model-based control holding a 1000 °C, 2 s, 100 °C/s spike
  to ±0.1 °C.[^vandenabeele-1998] Roozeboom and Parekh review RTP
  systems with emphasis on temperature control.[^roozeboom-1990]
  Edge-ring design avoids slip; sheet-resistance maps of monitor
  wafers after each lot track activation and uniformity.[^txt-10]
* **Diffusion budget.** The junction movement is, to first order,
  the integral of diffusivity over the thermal cycle plus the TED
  contribution; a spike keeps both small.

  The PDK's out-diffusion
  limits next to an isolation edge — 0.007 µm, or 0.05 µm for the
  6 V devices — and the 0.06 µm "vertical space" entry for the
  source/drain[^pdk-03] are the design-rule expression of that
  budget.
* **Furnace alternative.** A furnace anneal at 900–1000 °C for tens
  of minutes[^txt-01] would activate the dopant but drive the
  junctions far beyond 0.1 µm and defeat the extensions;
  "Increasingly, furnace anneals are being supplanted by Rapid
  Thermal Anneal".[^wiki-furnace] The 0.1 µm junction depth and the
  evidence below make an RTA the only plausible reading (inference).

## Machines typically used

* **{ref}`Rapid thermal processors <machine-rapid-thermal-processor>`**, 200 mm: AG Associates Heatpulse
  8108/8800 series, Applied Materials RTP Centura (the lamp-heated
  chamber of Gronet and Gibbons[^pat-rtp-amat]), Steag/Mattson RTP,
  Kokusai and TEL RTP (category page).
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`** for sheet resistance; **thermocouple wafers**
  for calibration.

## Machines likely used at SkyWater

* **AG Associates Heatpulse 8808**
  - *SkyWater says:* lists under RTA "Ag Heatpulse 8808 NH3, Ar, N2,
    O2, up to 1200C".[^skw-01]
  - *Tool exists:* **strong** for the tool (SkyWater statement).
  - *Runs this step:* assignment to `RTAD` is an **inference** from the
    Heatpulse being the only RTA on SkyWater's list, and a source/drain
    activation is the archetypal use of such a tool.

  The Heatpulse 8808 is a
  single-wafer RTA with the inert ambients and the temperature reach
  this step needs.

  Reseller documentation for the
  Heatpulse 8800/8808
  family gives "Recommended steady-state temperature range: 400 –
  1200°C", ramp-up "Programmable, 1 – 180°C per second", "2 banks of
  14 lamps" with "10-zone lamp control" and lists "Implant annealing"
  among its applications.[^ag-8800] A vendor blog post describes
  the 8800/8108 family.[^plasmatherm-ag] The reseller's family
  specification PDF gives, in its Heatpulse 8108 section, the same
  400–1200 °C range, a programmable 1–180 °C/s ramp-up and a maximum
  ramp-down of 150 °C/s (its Heatpulse 4100 section differs:
  400–1300 °C, 10–200 °C/s ramp-up).[^ag-8108]
* **Aviza furnaces** ("Ar anneal to 1150C", "N2 anneal to
  1150C"[^skw-01]) are the batch alternative but, for the reasons
  above, an unlikely one for this step.
  - *Tool exists:* strong for existence.
  - *Runs this step:* weak for assignment.

## Resources required

* **{ref}`Nitrogen <material-process-gases>` and argon** (likely ambient, our inference; SkyWater lists
  the Heatpulse's gases, "NH3, Ar, N2, O2", but no ambient for any
  step);[^skw-01] **oxygen** if a minor addition is used.
* **{ref}`Tungsten-halogen lamps <material-hardware-consumables>`, quartz window and chamber, edge rings**;
  pyrometer calibration and {ref}`thermocouple wafers <material-substrates>` (category page).
* **Cooling water and CDA/N₂** for lamp and chamber cooling
  (facility table for the Heatpulse family).[^ag-8108]
* **Monitor wafers** (SEMI M8 class)[^semi-m8] implanted with the
  product doses for sheet-resistance tracking.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`NSDIS <step-087>` (strip and pre-anneal clean).
* Next: {ref}`PSG <step-089>` (sacrificial PSG), then
  {ref}`CMPP <step-090>`, {ref}`NCAPOX <step-091>` and the second
  source/drain anneal {ref}`RTAD2 <step-092>`.
* Same module: the cap during the anneal, {ref}`SPOX <step-080>`; the
  spacers the dopant meets, {ref}`SPNIT <step-076>`.
* Anneals the implants of {ref}`PSDI <step-082>`,
  {ref}`2PSDI <step-083>` and {ref}`NSDI <step-086>`, and re-anneals
  the tips and halos of {ref}`ASTI <step-065>` to
  {ref}`LDBHI <step-073>` and the poly heads doped through
  {ref}`NPCME <step-079>`.
* Same category: earlier RTAs, {ref}`RTAI <step-034>`,
  {ref}`TIPRTAD <step-075>`.
* Category page: {ref}`Anneal / thermal processing <category-anneal>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Rapid thermal heating apparatus and method <patent-gp27042189>` — US 5,155,336 A (1990)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — "Ag Heatpulse 8808 NH3, Ar,
  N2, O2, up to 1200C"; Aviza Ar/N₂ anneals to 1150 °C.[^skw-01]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — S/D junction depth 0.1 µm;
  0.06 µm vertical space; out-diffusion limits next to isolation
  (0.007 µm; 0.05 µm for 6 V devices).[^pdk-03]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — N- and P-diffusion
  sheet resistances.[^pdk-08]
* [SemiStar, *AG Associates Heatpulse 8800 / 8808*](<https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>) — temperature range,
  ramp rates, lamp banks, applications.[^ag-8800]
* [SemiStar, *AG Associates Heatpulse 4100 / 8108 / 8800 / 8800i
  Specifications* (PDF)](<https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>) — the Heatpulse 4100 and 8108 operating and
  facility specifications.[^ag-8108]
* [Plasma-Therm, *Product Spotlight: AG Heatpulse 8800 / 8108
  RTP*](<https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>).[^plasmatherm-ag]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]

### High-level understanding

* [Wikipedia, *Rapid thermal processing*](<https://en.wikipedia.org/wiki/Rapid_thermal_processing>).[^wiki-rtp]
* [Wikipedia, *Furnace anneal*](<https://en.wikipedia.org/wiki/Diffusion_furnace>).[^wiki-furnace]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — dopant
  activation and diffusion.[^txt-01]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — RTP and
  source/drain anneals.[^txt-05]
* [Taur et al., *Proc. IEEE* 1997](<https://doi.org/10.1109/5.573737>) — why junctions must stay
  shallow.[^taur-1997]

### Deep dive

* [Fair (ed.), *Rapid Thermal Processing: Science and Technology*](<https://doi.org/10.1016/b978-0-12-247690-7.50009-3>) —
  junction formation by RTA.[^txt-10]
* [Agarwal, Gossmann and Fiory, *J. Electron. Mater.* 1999](<https://doi.org/10.1007/s11664-999-0118-7>) — ramp
  rate and boron junction depth.[^agarwal-1999]
* [Agarwal et al., *Mater. Sci. Semicond. Process.* 1998](<https://doi.org/10.1016/S1369-8001(98)00030-4>) — spike
  annealing in lamp-based and hot-walled systems.[^agarwal-1998]
* [Agarwal, IIT 2000](<https://doi.org/10.1109/IIT.2000.924147>) — ultra-shallow junctions by conventional
  implantation and RTA.[^agarwal-2000]
* [Fiory, *J. Electron. Mater.* 2002](<https://doi.org/10.1007/s11664-002-0031-9>) — RTP developments of the 130 nm
  era.[^fiory-2002]
* [Gerritsen, *Microelectron. Eng.* 2000](<https://doi.org/10.1016/S0167-9317(99)00275-0>) — the spike anneal.[^gerritsen-2000]
* [Josse et al. (STMicroelectronics), ESSDERC 2002](<https://doi.org/10.1109/ESSDERC.2002.194906>) — spike-anneal
  optimisation for a 0.13 µm platform.[^josse-2002]
* [Matsuda, Shishiguchi and Kitajima (NEC), *JJAP* 2002](<https://doi.org/10.1143/JJAP.41.451>) — an
  optimised RTA for shallow junctions.[^matsuda-2002]
* Stolk et al. (Bell Labs), [*J. Appl. Phys.*](<https://doi.org/10.1063/1.364452>) 1997; Michel et al.
  (IBM), [*Appl. Phys. Lett.*](<https://doi.org/10.1063/1.98160>) 1987; Eaglesham et al. (AT&T), [*Appl.
  Phys. Lett.*](<https://doi.org/10.1063/1.112725>) 1994 — transient enhanced diffusion.[^stolk-1997][^michel-1987][^eaglesham-1994]
* Nobili et al., *J. Electrochem. Soc.* 1983; Luning et al., IEDM
  1992; Rousseau, Griffin and Plummer, *Appl. Phys. Lett.* 1994 —
  arsenic activation, deactivation and its point-defect
  consequences.[^nobili-1983][^luning-1992][^rousseau-1994]
* [Camillo-Castillo et al., *MRS Proc.* 2002](<https://doi.org/10.1557/PROC-717-C1.4>) — two-step anneals and
  end-of-range defects.[^camillo-castillo-2002]
* Csepregi et al., [*J. Appl. Phys.*](<https://doi.org/10.1063/1.325397>) 1978, and Jeon, Becker and
  Walser, [*MRS Proc.*](<https://doi.org/10.1557/PROC-157-745>) 1989 — solid-phase epitaxial regrowth.[^csepregi-1978][^jeon-1989]
* [Wang et al., *J. Electrochem. Soc.* 1997](<https://doi.org/10.1149/1.1838075>) — fluorine and boron
  diffusion in the RTA.[^wang-1997]
* Pelletier et al., *Mater. Sci. Eng. B* 2008, and Farhane et al.,
  RTP 2003 — dopant loss into spacers and to the
  surface.[^pelletier-2008][^farhane-2003]
* Vandenabeele and Renken, *MRS Proc.* 1998; Sorrell and Gyurcsik,
  *IEEE TSM* 1993; Chen et al., RTP 2002 — temperature control and
  emissivity in RTP.[^vandenabeele-1998][^sorrell-1993][^chen-2002-rtp]
* [Roozeboom and Parekh (Philips), *JVST B* 1990](<https://doi.org/10.1116/1.584902>) — RTP systems
  review.[^roozeboom-1990]
* [Gronet and Gibbons (Applied Materials), US 5,155,336](<https://patents.google.com/patent/US5155336A/en>) — a
  lamp-heated RTP chamber.[^pat-rtp-amat]
* [Gibbons, *Proc. IEEE* 1972](<https://doi.org/10.1109/PROC.1972.8854>) — damage production and annealing.[^gibbons-1972]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — junction depth, abruptness and
  sheet-resistance targets.[^itrs-01]

## Open questions

* **Temperature, time and ambient.** The SKY130 anneal temperature, time (soak or spike), ramp rates
  and ambient are not public; the figures above are industry-typical.
* **Why two anneals.** Why the flow has two source/drain anneals — this step and
  {ref}`RTAD2 <step-092>` after the PSG and polish — is not public;
  the activation-stability reading above is an inference.
* **Heatpulse 8808.** Whether the Heatpulse 8808 runs this step is inferred from the
  tool's published capability and its being the only RTA on
  SkyWater's list.[^skw-01][^ag-8800]
* **Specification PDF.** The reseller's specification PDF cited for the Heatpulse
  family[^ag-8108] documents the Heatpulse 4100, 8108, 8800 and 8800i, not the 8808 itself;
  the 8808's own data sheet is not public.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^ag-8800]: SemiStar Corp., *AG Associates Heatpulse 8800 / 8808 Rapid
    Thermal Processing* (reseller specification page), accessed
    2026-08-30.
    <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
[^ag-8108]: SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 / 8800
    / 8800i Specifications* (reseller PDF; operating specifications for
    the Heatpulse 4100 and 8108), accessed 2026-08-30.
    <https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>
[^plasmatherm-ag]: Plasma-Therm, *Product Spotlight: AG Heatpulse 8800 /
    8108 RTP*, blog post.
    <https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^wiki-rtp]: Wikipedia, *Rapid thermal processing*.
    <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
[^wiki-furnace]: Wikipedia, *Furnace anneal*.
    <https://en.wikipedia.org/wiki/Diffusion_furnace>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-10]: R. B. Fair (ed.), *Rapid Thermal Processing: Science and
    Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7; R. B.
    Fair, "Junction Formation in Silicon by Rapid Thermal Annealing",
    pp. 169–226. <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^agarwal-1999]: A. Agarwal, H.-J. Gossmann and A. T. Fiory, "Effect of
    ramp rates during rapid thermal annealing of ion implanted boron for
    formation of ultra-shallow junctions", *Journal of Electronic
    Materials* **28**(12), 1333–1339 (1999).
    <https://doi.org/10.1007/s11664-999-0118-7>
[^agarwal-1998]: A. Agarwal, A. T. Fiory, H.-J. L. Gossmann,
    C. S. Rafferty and P. Frisella, "Ultra-shallow junction formation
    by spike annealing in a lamp-based or hot-walled rapid thermal
    annealing system: effect of ramp-up rate", *Materials Science in
    Semiconductor Processing* **1**(3–4), 237–241 (1998).
    <https://doi.org/10.1016/S1369-8001(98)00030-4>
[^agarwal-2000]: A. Agarwal, "Ultra-shallow junction formation using
    conventional ion implantation and rapid thermal annealing", *Proc.
    2000 International Conference on Ion Implantation Technology*,
    pp. 293–299. <https://doi.org/10.1109/IIT.2000.924147>
[^fiory-2002]: A. T. Fiory, "Recent developments in rapid thermal
    processing", *Journal of Electronic Materials* **31**(10), 981–987
    (2002). <https://doi.org/10.1007/s11664-002-0031-9>
[^gerritsen-2000]: E. Gerritsen, "Spike anneal: RTP processing at
    reduced thermal budget with applications to TiSi₂ formation towards
    0.1-μm linewidths", *Microelectronic Engineering* **50**(1–4),
    147–151 (2000). <https://doi.org/10.1016/S0167-9317(99)00275-0>
[^josse-2002]: E. Josse, F. Arnaud, F. Wacquant, D. Lenoble, O. Menut
    and E. Robilliart, "Spike Anneal Optimization for Digital and
    Analogue High Performance 0.13 μm CMOS Platform", *Proc. 32nd
    European Solid-State Device Research Conference (ESSDERC 2002)*,
    pp. 207–210. <https://doi.org/10.1109/ESSDERC.2002.194906>
[^matsuda-2002]: T. Matsuda, S. Shishiguchi and H. Kitajima, "Ultra
    Shallow Junction Formation with High Process Controllability Using
    Optimized Rapid Thermal Anneal Process", *Japanese Journal of
    Applied Physics* **41**(2A), 451–457 (2002).
    <https://doi.org/10.1143/JJAP.41.451>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^michel-1987]: A. E. Michel, W. Rausch, P. A. Ronsheim and R. H. Kastl,
    "Rapid annealing and the anomalous diffusion of ion implanted boron
    into silicon", *Applied Physics Letters* **50**(7), 416–418 (1987).
    <https://doi.org/10.1063/1.98160>
[^eaglesham-1994]: D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and J.
    M. Poate, "Implantation and transient B diffusion in Si: The source
    of the interstitials", *Applied Physics Letters* **65**(18),
    2305–2307 (1994). <https://doi.org/10.1063/1.112725>
[^nobili-1983]: D. Nobili, A. Carabelas, G. Celotti and S. Solmi,
    "Precipitation as the Phenomenon Responsible for the Electrically
    Inactive Arsenic in Silicon", *Journal of The Electrochemical
    Society* **130**(4), 922–928 (1983).
    <https://doi.org/10.1149/1.2119859>
[^luning-1992]: S. Luning, P. M. Rousseau, P. B. Griffin, P. G. Carey
    and J. D. Plummer, "Kinetics of high concentration arsenic
    deactivation at moderate to low temperatures", *IEDM 1992
    Technical Digest*, pp. 457–460.
    <https://doi.org/10.1109/IEDM.1992.307400>
[^rousseau-1994]: P. M. Rousseau, P. B. Griffin and J. D. Plummer,
    "Electrical deactivation of arsenic as a source of point defects",
    *Applied Physics Letters* **65**(5), 578–580 (1994).
    <https://doi.org/10.1063/1.112301>
[^camillo-castillo-2002]: R. A. Camillo-Castillo, K. S. Jones, M. E. Law
    and L. M. Rubin, "Study of the Effects of a Two-Step Anneal on the
    End of Range Defects in Silicon", *MRS Proceedings* **717** (2002).
    <https://doi.org/10.1557/PROC-717-C1.4>
[^csepregi-1978]: L. Csepregi, E. F. Kennedy, J. W. Mayer and T. W.
    Sigmon, "Substrate-orientation dependence of the epitaxial regrowth
    rate from Si-implanted amorphous Si", *Journal of Applied Physics*
    **49**(7), 3906–3911 (1978). <https://doi.org/10.1063/1.325397>
[^jeon-1989]: Y.-J. Jeon, M. F. Becker and R. M. Walser, "Concentration
    Dependence of Arsenic on Solid Phase Epitaxial Regrowth of
    Amorphous Silicon", *MRS Proceedings* **157** (1989).
    <https://doi.org/10.1557/PROC-157-745>
[^wang-1997]: L. Z. Wang, M. S.-C. Luo, H.-H. Tseng and S. A. Ajuria,
    "The Influence of Fluorine on Boron-Enhanced Diffusion in Silicon by
    BF₂⁺ Implantation Through Oxide during High Temperature Rapid
    Thermal Anneal", *Journal of The Electrochemical Society*
    **144**(11), L298–L301 (1997). <https://doi.org/10.1149/1.1838075>
[^pelletier-2008]: B. Pelletier, M. Juhel, C. Trouiller, D. Beucher,
    J. Autran and P. Morin, "Boron out-diffusion mechanism in oxide and
    nitride CMOS sidewall spacer: Impact of the materials properties",
    *Materials Science and Engineering: B* **154–155**, 252–255 (2008).
    <https://doi.org/10.1016/j.mseb.2008.09.025>
[^farhane-2003]: R. Farhane, F. Salvetti, F. Wacquant, C. Laviron,
    B. Froment, A. Muller, A. Pouydebasque and A. Halimaoui,
    "Investigation of the dose loss during annealing in nitrogen of
    shallow-implanted arsenic", *Proc. 11th IEEE International
    Conference on Advanced Thermal Processing of Semiconductors (RTP
    2003)*, pp. 173–176. <https://doi.org/10.1109/RTP.2003.1249144>
[^vandenabeele-1998]: P. Vandenabeele and W. Renken, "Model Based
    Temperature Control in RTP Yielding ±0.1 °C accuracy on A 1000 °C,
    2 second, 100 °C/s Spike Anneal", *MRS Proceedings* **525** (1998).
    <https://doi.org/10.1557/PROC-525-109>
[^sorrell-1993]: F. Y. Sorrell and R. S. Gyurcsik, "Model-based
    emissivity correction in pyrometer temperature control of rapid
    thermal processing systems", *IEEE Transactions on Semiconductor
    Manufacturing* **6**(3), 273–276 (1993).
    <https://doi.org/10.1109/66.238178>
[^chen-2002-rtp]: D. Chen, D. DeWitt, B. Tsai, K. Kreider and W. Kimes,
    "Effects of wafer emissivity on rapid thermal processing
    temperature measurement", *Proc. 10th IEEE International Conference
    on Advanced Thermal Processing of Semiconductors (RTP 2002)*,
    pp. 59–67. <https://doi.org/10.1109/RTP.2002.1039440>
[^roozeboom-1990]: F. Roozeboom and N. Parekh, "Rapid thermal processing
    systems: A review with emphasis on temperature control", *Journal of
    Vacuum Science & Technology B* **8**(6), 1249–1259 (1990).
    <https://doi.org/10.1116/1.584902>
[^pat-rtp-amat]: C. M. Gronet and J. F. Gibbons (Applied Materials),
    *Rapid thermal heating apparatus and method*, US 5,155,336 A,
    granted 1992-10-13.
    <https://patents.google.com/patent/US5155336A/en>
[^gibbons-1972]: J. F. Gibbons, "Ion implantation in semiconductors —
    Part II: Damage production and annealing", *Proceedings of the IEEE*
    **60**(9), 1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
