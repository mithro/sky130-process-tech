(step-056)=
# Step 056 — UPRI: UPRI implant

| | |
|---|---|
| **Step number** | 56 of 171 |
| **Step code** | `UPRI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — gate and poly resistors |
| **Previous step** | {ref}`URPM <step-055>` |
| **Next step** | {ref}`UPRIS <step-057>` |

## What this step is

`UPRI` is the implant that sets the sheet resistance of the SKY130
ultra-high-resistance poly resistor. Through the windows of
{ref}`URPM <step-055>` it places a light p-type dose into the still
undoped bodies of the `res_xhigh_po` devices; the resist covers the
n⁺ gate film and the 300 Ω/sq bodies doped at {ref}`PRI <step-053>`.
The resist is stripped at {ref}`UPRIS <step-057>`, after which the
poly doping of the process is complete and the film can be capped.

The target is public and unusually explicit: the PDK says of the
"P− poly precision resistors" that "a separate implant is used to set
the sheet resistance to 2000 ohm/sq",[^pdk-07] the extraction table
gives 2000 Ω/sq for the "UHR poly resistor",[^pdk-08] and the drawn
layer `urpm` is described as the "2000 ohms/square polysilicon
resistor implant".[^pdk-06] Species, energy and dose are not public.
For a 0.18 µm film[^pdk-03] the target corresponds to a resistivity of
about 36 mΩ·cm, which on the published resistivity-versus-doping
curves for boron-doped poly lies in the region just above the
grain-boundary trap-filling threshold — the steepest part of the
curve[^seto-1975][^kamins-1998] — and to a dose of order 10¹⁴ cm⁻² or
somewhat below (an illustrative estimate by dose × thickness, not a
SkyWater number).

## Step category

`UPRI` is an {ref}`Ion implantation <category-implant>` step of the
*poly and resistor implant* class, and the most precision-critical
implant in the module: a smaller dose than {ref}`PRI <step-053>`,
placed on the part of the resistance curve where a few percent of
dose error is tens of percent of resistance. It is also, we infer, the
last implant the resistor bodies receive before the film is capped and
patterned.

## Why this step exists

The reason for a 2000 Ω/sq film is given on {ref}`URPM <step-055>`:
megohm-class resistors in small area for bias and reference circuits.
The reason it is a *separate* implant rather than a lower dose of the
300 Ω/sq recipe is control. In Seto's model the conductivity of doped
poly rises by orders of magnitude as the doping passes the level at
which the grain-boundary traps are filled;[^seto-1975] Mandurah,
Saraswat and Kamins add the segregation of dopant to the boundaries,
which removes part of the dose from conduction
altogether.[^mandurah-1981] A 2000 Ω/sq resistor sits where both
effects are strong, so its value is set by the *net* active dose after
segregation and by the grain size after all later anneals. A dedicated
implant lets the dose be tuned for this device on its own, and lets its
TCR be brought toward zero — the trade-off Lu et al. and Lane and
Wrixon describe[^lu-1981][^lane-1989] and that co-implantation studies
have since refined.[^ashuah-2009]

The same sensitivity is why the PDK, at the time its documentation was
written, gave the P− resistor's electrical specifications as
"TBD".[^pdk-07] Chen et al. show that the voltage coefficient of a
lightly doped poly resistor is large and can be improved by
stress,[^chen-2000] and Tsang et al. analyse the variation of
high-value resistor banks;[^tsang-2014] both are consequences of the
same barrier-limited conduction that this implant sets up.

## How it is typically performed

An industry-generic light poly-resistor implant for a 200 mm,
130 nm-era fab (SKY130 values are not public):

* **Species.** Boron (¹¹B⁺ or BF₂⁺ from BF₃[^wiki-bf3]); SkyWater's
  implanters offer both "B11" and "BF2".[^skw-01] For a light dose,
  boron's lower mass and its diffusion along grain boundaries help
  spread a small quantity of dopant uniformly through the
  film.[^kamins-1972]
* **Energy.** Tens of keV, keeping the profile inside the 0.18 µm
  film; the amorphous film gives no channelling tail
  ({ref}`P1I <step-050>`).
* **Dose.** Of order 10¹⁴ cm⁻² or below (illustrative estimate above),
  squarely in the range of SkyWater's medium-current implanter
  ("Axcelis 8250 Mid current B11, BF2, As … 1e11 to 1e14"[^skw-01]),
  whose class is specified with dose repeatability suited to
  threshold-adjust work.[^axcelis-8250] A high-dose tool can also run
  it, at low beam current.
* **Tilt.** Normal or near-normal incidence; window widths follow the
  `rpm` rules (1.270 µm minimum[^pdk-periph]), so shadowing is
  negligible, but straggle at the resist edge blurs the doped
  length.[^hook-2003]
* **Anneal.** None dedicated; activation happens in the later thermal
  steps. Because the final value depends on grain growth as well as
  activation, the resistor is characterised at e-test on finished
  wafers.
* **Monitoring.** Sheet resistance on monitor wafers after a standard
  anneal; the implanter's dose integrator and, for crystalline
  monitors, thermal-wave measurement.[^smith-1985]

## Machines typically used

* **Medium-current implanter** (Axcelis/Eaton 8250, Varian E220/E500,
  Applied Materials xR80) — the natural tool for a light, precise
  dose (category page).
* **Four-point probe** for monitor sheet resistance.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter.** SkyWater lists it with
  B11 and BF2 species and a dose range of 10¹¹–10¹⁴ cm⁻².[^skw-01]
  Strength: **strong** for the tool; the assignment to this implant
  is an inference from the estimated dose. The GSD high-dose tool
  ("5e12 to 5e16"[^skw-01]) overlaps the range and is the
  alternative.

## Resources required

* **Boron trifluoride (BF₃)**[^wiki-bf3] or a solid boron source.
* **Source consumables**, cooling water and helium, cryopump nitrogen.
* **Monitor wafers** for sheet resistance.

## Related steps and cross-references

* Previous: {ref}`URPM <step-055>`. Next: {ref}`UPRIS <step-057>`.
* The companion resistor implant is {ref}`PRI <step-053>`; the gate
  implant is {ref}`P1I <step-050>`.
* The resistor bodies are capped at {ref}`GATENIT <step-058>`, cut at
  {ref}`P1ME <step-062>`, and contacted through
  {ref}`NPCM <step-078>` and {ref}`LICM1 <step-093>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater PDK, *Device Details* — "a separate implant is used to set
  the sheet resistance to 2000 ohm/sq"; specifications
  "TBD".[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — UHR poly
  2000 Ω/sq.[^pdk-08]
* SkyWater PDK, *Layers Reference* — `urpm` 79:20.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — poly 0.18 µm.[^pdk-03]
* SkyWater PDK, *Periphery rules* — `rpm` geometry.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — the 8250 and GSD implanters
  with species and dose ranges.[^skw-01]
* Semiconductor Online, 8250HT — the medium-current class.[^axcelis-8250]

### High-level understanding

* Wikipedia, *Ion implantation*, *Boron trifluoride*, *Sheet
  resistance*.[^wiki-implant][^wiki-bf3][^wiki-rs]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implantation.[^txt-02]
* Kamins, *Polycrystalline Silicon for Integrated Circuits and
  Displays* — resistivity of lightly doped poly.[^kamins-1998]

### Deep dive

* Seto, *J. Appl. Phys.* 1975 — grain-boundary trapping: the physics
  of a lightly doped poly resistor.[^seto-1975]
* Mandurah, Saraswat and Kamins, *IEEE TED* 1981 — dopant segregation
  to grain boundaries, which removes part of a light dose from
  conduction.[^mandurah-1981]
* Kamins, Manoliu and Tucker, *J. Appl. Phys.* 1972 — grain-boundary
  diffusion, which spreads the dose.[^kamins-1972]
* Lu, Gerzberg, Lu and Meindl, *IEEE TED* 1981 — optimisation of poly
  resistors, including the high-value regime.[^lu-1981]
* Lane and Wrixon, *IEEE TED* 1989 — analogue poly resistor
  design.[^lane-1989]
* Ashuah, Shauly and Shacham-Diamand, *IEEE TSM* 2009 — TCR
  engineering of boron-implanted poly resistors by
  co-implantation.[^ashuah-2009]
* Chen et al., *Solid-State Electronics* 2000 — voltage coefficient
  of poly resistors.[^chen-2000]
* Tsang et al., *IEEE TSM* 2014 — variation of high-value poly
  resistors in manufacturing.[^tsang-2014]
* Wright et al., *J. Vac. Sci. Technol. B* 2010 — high-sheet-resistance
  low-TCR films.[^wright-2010]
* Hook et al., *IEEE TED* 2003 — straggle at resist edges.[^hook-2003]
* Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985 —
  thermal-wave dose monitoring.[^smith-1985]
* Current, *Mater. Sci. Semicond. Process.* 2017 — implantation review
  with dose control.[^current-2017]
* ITRS 2001, *Front End Processes* — doping requirements.[^itrs-01]

## Open questions

* Species, energy, dose and tilt are not public; the 10¹⁴ cm⁻²-class
  estimate is illustrative.
* Whether the `urpm` bodies receive only this implant (the reading
  used here) is inferred from the resistance values, not stated.
* Whether the implant is run on the medium-current or the high-dose
  tool is not public.
* Whether the ultra-high resistor is a process option that some flows
  omit (the *Background* page's `r` suffix) is not stated.

<!-- footnotes -->

[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-bf3]: Wikipedia, *Boron trifluoride*.
    <https://en.wikipedia.org/wiki/Boron_trifluoride>
[^wiki-rs]: Wikipedia, *Sheet resistance*.
    <https://en.wikipedia.org/wiki/Sheet_resistance>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^kamins-1998]: T. Kamins, *Polycrystalline Silicon for Integrated
    Circuits and Displays*, 2nd ed., Kluwer Academic, 1998.
    <https://doi.org/10.1007/978-1-4615-5577-3>
[^seto-1975]: J. Y. W. Seto, "The electrical properties of
    polycrystalline silicon films", *Journal of Applied Physics*
    **46**(12), 5247–5254 (1975). <https://doi.org/10.1063/1.321593>
[^mandurah-1981]: M. M. Mandurah, K. C. Saraswat and T. I. Kamins, "A
    model for conduction in polycrystalline silicon — Part I: Theory",
    *IEEE Transactions on Electron Devices* **28**(10), 1163–1171
    (1981). <https://doi.org/10.1109/T-ED.1981.20504>
[^kamins-1972]: T. I. Kamins, J. Manoliu and R. N. Tucker, "Diffusion
    of Impurities in Polycrystalline Silicon", *Journal of Applied
    Physics* **43**(1), 83–91 (1972). <https://doi.org/10.1063/1.1660842>
[^lu-1981]: N. C.-C. Lu, L. Gerzberg, C.-Y. Lu and J. D. Meindl,
    "Modeling and optimization of monolithic polycrystalline silicon
    resistors", *IEEE Transactions on Electron Devices* **28**(7),
    818–830 (1981). <https://doi.org/10.1109/T-ED.1981.20437>
[^lane-1989]: W. A. Lane and G. T. Wrixon, "The design of thin-film
    polysilicon resistors for analog IC applications", *IEEE
    Transactions on Electron Devices* **36**(4), 738–744 (1989).
    <https://doi.org/10.1109/16.22479>
[^ashuah-2009]: I. Ashuah, E. N. Shauly and Y. Shacham-Diamand,
    "Improvement of Temperature Coefficient of Resistance by
    Co-Implantation of Argon or Xenon or Fluorine in Boron Implanted
    Polysilicon Resistors", *IEEE Transactions on Semiconductor
    Manufacturing* **22**(2), 305–316 (2009).
    <https://doi.org/10.1109/TSM.2009.2017655>
[^chen-2000]: C.-H. Chen, Y.-K. Fang, M.-H. Kuo, Y.-L. Hsu and
    S.-L. Hsu, "A DC current stress method to improve the voltage
    coefficient of resistance of the polysilicon resistor in high
    voltage CMOS technology", *Solid-State Electronics* **44**(10),
    1743–1746 (2000). <https://doi.org/10.1016/S0038-1101(00)00138-6>
[^tsang-2014]: Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
    "Characterization and Understanding of High Valued Polysilicon
    Resistor Resistance Variation Across a Resistor Bank With Parallel
    Resistor Fingers", *IEEE Transactions on Semiconductor
    Manufacturing* **27**(2), 294–300 (2014).
    <https://doi.org/10.1109/TSM.2014.2311375>
[^wright-2010]: S. W. Wright, C. P. Judge, M. J. Lee, D. F. Bowers,
    M. Dunbar and C. D. Wilson, "High sheet resistance, low temperature
    coefficient of resistance resistor films for integrated circuits",
    *Journal of Vacuum Science & Technology B* **28**(4), 834–840
    (2010). <https://doi.org/10.1116/1.3466531>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^current-2017]: M. I. Current, "Ion implantation of advanced silicon
    devices: Past, present and future", *Materials Science in
    Semiconductor Processing* **62**, 13–22 (2017).
    <https://doi.org/10.1016/j.mssp.2016.10.045>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
