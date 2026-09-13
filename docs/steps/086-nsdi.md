(step-086)=
# Step 086 — NSDI: N+ source drain implant

| | |
|---|---|
| **Step number** | 86 of 171[^steps-sheet] |
| **Step code** | `NSDI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`NSDM <step-085>` |
| **Next step** | {ref}`NSDIS <step-087>` |

## What this step is

`NSDI` is the heavy n-type implant that forms the deep source and
drain of every NMOS transistor and all the other N⁺ diffusions of the
process — the n⁺ taps to the N-wells, the NPN emitter and collector
contacts, the PNP base contacts, the N⁺ diffusion resistors and the
n-side of the P-well diodes.[^pdk-07] It goes through the resist
windows of {ref}`NSDM <step-085>`, through the thin
{ref}`SPOX <step-080>` oxide (on our reading), and is self-aligned to
the nitride spacers, so that the heavy junction stands a spacer-width
off the gate edge and joins the shallow arsenic {term}`extension`
implanted before the spacer ({ref}`ASTI <step-065>`,
{ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`). The resist is
stripped at {ref}`NSDIS <step-087>` and the dopant activated at
{ref}`RTAD <step-088>`.

Unlike the p-type side, the n-type side is described in this
reference with a single implant. What the PDK says about the result
is the same as for the P⁺ junction: an "N+ or P+ S/D (XJ)" vertical
feature of 0.1 µm and a vertical space of 0.06 µm,[^pdk-03] a
high-current implant angle of 0°,[^pdk-03] and an N-diffusion sheet
resistance of 120 000 mΩ/sq (120 Ω/sq), lower than the 197 Ω/sq of
P-diffusion.[^pdk-08] The device page's e-test table gives `RSN` as
120 Ω/sq (limits 108–132) and the high-voltage N⁺ diffusion `RSNH` as
114 Ω/sq (102–126).[^pdk-07] Two-terminal sweeps of the test tile's
25-square "n+ resistor" structures, published in the SKY130 raw-data
repository, give 122.5 Ω and 120.7 Ω per square, and the "n+ high
voltage resistor" 116.7 Ω per square, contacts included — inside those
limits and, like the nominal values, lower for the high-voltage
structure (our extraction from the published measurements; the files
record no temperature, date or
wafer).[^raw-data-passives][^raw-data-testtile-pads] The NMOS
cross-section shows "N+" source/drain beside "N−"
extensions.[^pdk-07] Species, energy and dose are not
public: the "N+" name, the tool list and the sheet resistance are
what the public record offers, and industry practice supplies the
rest.

## Step category

`NSDI` is an {ref}`Ion implantation <category-implant>` step of the
*source/drain* class — high dose (of the order of 10¹⁵ cm⁻²,
industry-typical[^txt-01]), tens of keV, from a high-current tool,
self-aligned to a spacer, amorphising the surface
({ref}`category-implant`). Its partner is {ref}`PSDI <step-082>`.
What distinguishes it from the arsenic tip implant
({ref}`ASTI <step-065>`) is dose, depth and alignment; what
distinguishes it from the boron side is the ion: arsenic is heavy,
amorphises the silicon at a lower dose, diffuses slowly, and
deactivates by clustering rather than by precipitation alone.

## Why this step exists

The deep N⁺ junction carries the NMOS current from the contact to
the extension with the lowest possible series resistance — the term
that Ng and Lynch showed limits scaling[^ng-1986] — and provides the
degenerately doped surface that a contact or silicide needs. Its
depth (the PDK's 0.1 µm[^pdk-03]) keeps the contact etch and
silicidation ({ref}`CSIL <step-098>`) out of the junction, and its
offset from the gate, set by the spacer of
{ref}`SPNIT <step-076>`/{ref}`SPE <step-077>`, keeps that depth from
degrading short-channel control, which is the whole point of the LDD
structure of Ogura et al.[^ogura-1980] and the spacer of Tsang et
al.[^tsang-1982]

The choice of arsenic, and the question of whether phosphorus is
added, is a well-documented trade. Arsenic gives an abrupt, shallow,
highly active junction, but its activation is limited by clustering:
Nobili et al. identified precipitation as the reason for electrically
inactive arsenic,[^nobili-1983] Angelucci et al. measured arsenic
precipitation and diffusivity together,[^angelucci-1985] Luning et al.
the kinetics of high-concentration deactivation at moderate
temperatures,[^luning-1992] and Rousseau, Griffin and Plummer showed
that arsenic deactivation *injects interstitials* — so an over-active
arsenic layer that relaxes during a later thermal step enhances the
diffusion of everything around it,[^rousseau-1994] with consequences
for bipolar devices[^rousseau-1996] that matter to the NPN whose
emitter this implant makes. Adding a lighter phosphorus component
grades the junction and lowers its resistance: Lee and Lee's As/P
double-implanted source/drain for 0.25 µm technology[^lee-1999-edl]
and Augendre et al.'s As/P co-implantation for gate and source/drain
engineering[^augendre-2001] set out the benefits and the leakage
cost. Whether SKY130 uses arsenic alone or with phosphorus is not
public; both are on SkyWater's implanter species lists.[^skw-01]

Two things this implant does *not* do, on the reading used
throughout this reference: it does not dope the gates, which are
capped ("poly cap after SPE" 0.2 µm[^pdk-03]) and were doped n⁺ at
{ref}`P1I <step-050>` — although, since the gates are n⁺ already, an
N⁺ source/drain reaching them would do no harm, which is one reason
the capped-gate reading is hard to test from the NMOS side; and it
does not dope the precision resistors, which rpm.6 keeps 0.200 µm
clear of `nsdm`.[^pdk-periph] It *does* dope, on the
{ref}`NPCM <step-078>` reading, the n⁺ poly contact heads exposed by
the {term}`nitride cut` inside `nsdm`.

Without `NSDI` there would be no NMOS source/drain, no N-well
contacts and no NPN.

## How it is typically performed

An industry-generic N⁺ source/drain implant for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

* **Species and source.** Arsenic (⁷⁵As⁺) from arsine gas,[^wiki-ash3]
  optionally followed by phosphorus (³¹P⁺) from phosphine[^wiki-ph3]
  under the same resist. Both gases are highly toxic and are
  delivered from sub-atmospheric cylinders in monitored gas cabinets.
* **Energy and dose.** Tens of keV and a few 10¹⁵ cm⁻² for arsenic
  (industry-typical[^txt-01][^txt-02]); the screen oxide of
  {ref}`SPOX <step-080>` takes part of the range. Arsenic at these
  doses amorphises the silicon — above roughly 10¹⁴–10¹⁵ cm⁻² "the
  amount of crystallographic damage can be enough to completely
  amorphize the surface"[^wiki-implant] — and the layer regrows by
  solid-phase epitaxy during the anneal, at a rate that depends on
  orientation[^csepregi-1978] and on the arsenic concentration
  itself.[^jeon-1989]
* **Tilt.** 0°, per the PDK's "High current" implant-angle
  entry;[^pdk-03] the amorphisation makes channelling a smaller
  concern than for boron, and zero tilt avoids the shadowing beside
  roughly 0.4 µm-tall (0.18 µm poly plus the ~0.2 µm cap[^pdk-03]) capped gates that Krieger et al. analysed for tilted
  arsenic source/drain implants.[^krieger-1989] On a spinning-disc
  batch tool the effective angle still varies across the
  disc.[^jones-1996]
* **Wafer handling.** Batch spinning-disc end station with wafer
  cooling; the beam power at several mA (typical) heats the resist
  (Smith,[^smith-1983] Romig et al.[^romig-1996]). Charging control
  by {term}`plasma flood gun` is critical for an arsenic implant on a
  resist-covered wafer — Lukaszek, Reno and Bammi measured the
  influence of resist on charging during high-current arsenic
  implants,[^lukaszek-1996] Current et al. the current–voltage
  characteristics of charging control during high-current As⁺
  implantation,[^current-1998] and Mehta et al. the negative-charging
  side of flood-gun operation.[^mehta-1996]
* **Dose loss.** A fraction of a shallow arsenic implant is lost to
  the surface during the anneal; Farhane et al. quantified the loss
  in nitrogen anneals[^farhane-2003] and Shibahara et al. its
  origins,[^shibahara-1998] which is one function of the oxide cap
  the implant passes through.
* **Monitoring.** Sheet resistance by {term}`four-point probe` on
  monitor wafers after a monitor anneal; particle and resist
  inspection. The e-test `nfet_01v8` parameters are the device-level
  monitor.[^pdk-07]
* **Anneal.** None here; {ref}`RTAD <step-088>` follows the strip.

## Machines typically used

* **{ref}`High-current ion implanter <machine-high-current-implanter>`**, 200 mm: Axcelis/Eaton GSD and
  NV-GSD (batch), Applied Materials xR and Quantum, Varian VIISta 80
  (single-wafer[^mezack-2000]); Current's overviews of production
  implanters.[^current-1996][^current-2017]
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`**; **{ref}`particle inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **Axcelis GSD high-dose implanter.** "Axcelis GSD Hi dose B11, BF2,
  P, As 2-180kev, 5e12 to 5e16, tilt/twist" and "Axcelis GSD High
  current/energy B11, BF2, P, As, 10-3000kev, 1e11 to 5e15,
  tilt/twist".[^skw-01] Strength: **strong** for the tools and their
  species (both list P and As); the assignment of `NSDI` to the "Hi
  dose" tool is an **inference** from the dose required, which lies
  beyond the medium-current 8250's "1e11 to 1e14".[^skw-01] Axcelis
  describes the GSD family as "the industry benchmark for the longest
  manufactured and supported batch ion implanter".[^axcelis-gsd]

## Resources required

* **Arsine (AsH₃)** for arsenic and, if used, **phosphine (PH₃)** for
  phosphorus;[^wiki-ash3][^wiki-ph3] both toxic, in sub-atmospheric
  cylinders with gas-cabinet monitoring and scrubbed exhaust.
* **Source-support gases** (argon, xenon); **liquid nitrogen** for
  cryopumps; **nitrogen** vent gas; platen cooling water.
* **Source consumables** — filaments/cathodes, arc-chamber liners
  (arsenic deposits require careful maintenance), extraction
  electrodes; disc pads; flood-gun consumables.
* **Monitor wafers** (SEMI M8 class).[^semi-m8]

## Related steps and cross-references

* Previous: {ref}`NSDM <step-085>` (the mask). Next:
  {ref}`NSDIS <step-087>` (strip), then {ref}`RTAD <step-088>`
  (activation) and later {ref}`RTAD2 <step-092>`.
* Complementary implant: {ref}`PSDI <step-082>`/{ref}`2PSDI <step-083>`.
* The extensions it joins: {ref}`ASTI <step-065>`,
  {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`; the halos
  around them: {ref}`BHI <step-066>`, {ref}`LDBHI <step-073>`.
* The offset it is aligned to: {ref}`SPNIT <step-076>`,
  {ref}`SPE <step-077>`; the screen it passes through:
  {ref}`SPOX <step-080>`; the poly heads it dopes:
  {ref}`NPCME <step-079>`.
* The n⁺ gate it does not need to dope: {ref}`P1I <step-050>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — S/D junction depth
  entries; implant angle "High current" 0°; "poly cap after SPE"
  0.2 µm.[^pdk-03]
* SkyWater PDK, *Device Details* — NMOS cross-section with "N+" and
  "N−" regions; NPN, PNP, diode and `res_generic_nd`
  descriptions; `RSN` and `RSNH` e-test limits.[^pdk-07]
* SKY130 raw-data repository — two-terminal sweeps of the test tile's
  N⁺ diffusion resistors and the pad list that describes them; the
  sheet resistances quoted here are our
  extraction.[^raw-data-passives][^raw-data-testtile-pads]
* SkyWater PDK, *Parasitic Layout Extraction* — N-diffusion
  120 000 mΩ/sq.[^pdk-08]
* SkyWater PDK, *Periphery rules* — rpm.6, nsd.*.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — Axcelis GSD implanters
  with P and As among their species; the 8250's dose range.[^skw-01]
* Axcelis, GSD Ovation press release — the GSD family.[^axcelis-gsd]

### High-level understanding

* Wikipedia, *Ion implantation* — amorphisation thresholds,
  channelling.[^wiki-implant]
* Wikipedia, *Arsine* and *Phosphine* — the source gases.[^wiki-ash3][^wiki-ph3]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — arsenic
  source/drains, solid-phase epitaxy.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implantation practice.[^txt-02]

### Deep dive

* Ogura et al. (IBM), *IEEE TED* 1980, and Tsang et al. (IBM), *IEEE
  TED* 1982 — the LDD structure and its spacer.[^ogura-1980][^tsang-1982]
* Ng and Lynch (AT&T), *IEEE TED* 1986 — series resistance.[^ng-1986]
* Nobili et al., *J. Electrochem. Soc.* 1983 — precipitation as the
  cause of inactive arsenic.[^nobili-1983]
* Angelucci et al., *J. Electrochem. Soc.* 1985 — arsenic
  precipitation and diffusivity.[^angelucci-1985]
* Luning et al. (Stanford), IEDM 1992 — kinetics of arsenic
  deactivation.[^luning-1992]
* Rousseau, Griffin and Plummer (Stanford), *Appl. Phys. Lett.* 1994,
  and Rousseau et al., *IEEE TED* 1996 — arsenic deactivation as an
  interstitial source and its device consequences.[^rousseau-1994][^rousseau-1996]
* Lee and Lee, *IEEE EDL* 1999 — As/P double-implanted
  source/drain.[^lee-1999-edl]
* Augendre et al. (IMEC), ESSDERC 2001 — As/P co-implantation.[^augendre-2001]
* Csepregi et al., *J. Appl. Phys.* 1978, and Jeon, Becker and
  Walser, *MRS Proc.* 1989 — solid-phase epitaxial regrowth and its
  arsenic-concentration dependence.[^csepregi-1978][^jeon-1989]
* Farhane et al., RTP 2003, and Shibahara et al., *MRS Proc.* 1998 —
  arsenic dose loss during annealing.[^farhane-2003][^shibahara-1998]
* Krieger et al., *IEEE TED* 1989 — shadowing of tilted arsenic
  source/drain implants.[^krieger-1989]
* Jones and Sinclair, IIT 1996 — channelling variation on
  spinning-disc implanters.[^jones-1996]
* Lukaszek, Reno and Bammi, IIT 1996; Current et al., IIT 1998; Mehta
  et al., IIT 1996 — charging control during high-current arsenic
  implants.[^lukaszek-1996][^current-1998][^mehta-1996]
* Smith, 1983, and Romig, Bishop and Rio, IIT 1996 — wafer cooling
  and resist burning.[^smith-1983][^romig-1996]
* Mezack et al. (Varian), IIT 2000; Current, *JVST A* 1996 and
  *Mater. Sci. Semicond. Process.* 2017 — implanter
  classes.[^mezack-2000][^current-1996][^current-2017]
* ITRS 2001, *Front End Processes* — junction requirements.[^itrs-01]

## Open questions

* Species (arsenic alone or with phosphorus), energy and dose are
  not public; the values given are industry-typical.
* Whether the SONOS cell source/drain is made by this implant is
  inferred from the cell being an NMOS device.
* Whether the capped gates are entirely shielded is inferred; for
  the n⁺ gates it makes no electrical difference and is therefore
  not testable from the NMOS side.
* Which implanter runs the step is inferred from dose capability.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the per-device cross-section drawings.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://github.com/google/skywater-pdk/tree/main/docs/rules/device-details>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^axcelis-gsd]: Axcelis Technologies, *Axcelis Announces Introduction Of
    The 'GSD Ovation' High Current And High Energy Batch Implanters*, PR
    Newswire, 2021-11-02. <https://www.prnewswire.com/news-releases/axcelis-announces-introduction-of-the-gsd-ovation-high-current-and-high-energy-batch-implanters-301412520.html>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^tsang-1982]: P. J. Tsang, S. Ogura, W. W. Walker, J. F. Shepard and
    D. L. Critchlow, "Fabrication of high-performance LDDFET's with
    oxide sidewall-spacer technology", *IEEE Transactions on Electron
    Devices* **29**(4), 590–596 (1982).
    <https://doi.org/10.1109/T-ED.1982.20748>
[^ng-1986]: K. K. Ng and W. T. Lynch, "Analysis of the
    gate-voltage-dependent series resistance of MOSFET's", *IEEE
    Transactions on Electron Devices* **33**(7), 965–972 (1986).
    <https://doi.org/10.1109/T-ED.1986.22602>
[^nobili-1983]: D. Nobili, A. Carabelas, G. Celotti and S. Solmi,
    "Precipitation as the Phenomenon Responsible for the Electrically
    Inactive Arsenic in Silicon", *Journal of The Electrochemical
    Society* **130**(4), 922–928 (1983).
    <https://doi.org/10.1149/1.2119859>
[^angelucci-1985]: R. Angelucci, G. Celotti, D. Nobili and S. Solmi,
    "Precipitation and Diffusivity of Arsenic in Silicon", *Journal of
    The Electrochemical Society* **132**(11), 2726–2730 (1985).
    <https://doi.org/10.1149/1.2113654>
[^luning-1992]: S. Luning, P. M. Rousseau, P. B. Griffin, P. G. Carey
    and J. D. Plummer, "Kinetics of high concentration arsenic
    deactivation at moderate to low temperatures", *IEDM 1992
    Technical Digest*, pp. 457–460.
    <https://doi.org/10.1109/IEDM.1992.307400>
[^rousseau-1994]: P. M. Rousseau, P. B. Griffin and J. D. Plummer,
    "Electrical deactivation of arsenic as a source of point defects",
    *Applied Physics Letters* **65**(5), 578–580 (1994).
    <https://doi.org/10.1063/1.112301>
[^rousseau-1996]: P. M. Rousseau, P. B. Griffin, S. C. Kuehne and
    J. D. Plummer, "Enhanced diffusion by electrical deactivation of
    arsenic and its implications for bipolar devices", *IEEE
    Transactions on Electron Devices* **43**(4), 547–553 (1996).
    <https://doi.org/10.1109/16.485536>
[^lee-1999-edl]: H.-D. Lee and Y.-J. Lee, "Arsenic and phosphorus
    double ion implanted source/drain junction for 0.25- and
    sub-0.25-μm MOSFET technology", *IEEE Electron Device Letters*
    **20**(1), 42–44 (1999). <https://doi.org/10.1109/55.737568>
[^augendre-2001]: E. Augendre, A. De Keersgieter, S. Kubicek,
    A. Redolfi, J. Van Laer and G. Badenes, "Arsenic and Phosphorus
    co-Implantation for Deep Submicron CMOS Gate and Source/Drain
    Engineering", *Proc. 31st European Solid-State Device Research
    Conference (ESSDERC 2001)*, pp. 115–118.
    <https://doi.org/10.1109/ESSDERC.2001.195214>
[^csepregi-1978]: L. Csepregi, E. F. Kennedy, J. W. Mayer and T. W.
    Sigmon, "Substrate-orientation dependence of the epitaxial regrowth
    rate from Si-implanted amorphous Si", *Journal of Applied Physics*
    **49**(7), 3906–3911 (1978). <https://doi.org/10.1063/1.325397>
[^jeon-1989]: Y.-J. Jeon, M. F. Becker and R. M. Walser, "Concentration
    Dependence of Arsenic on Solid Phase Epitaxial Regrowth of
    Amorphous Silicon", *MRS Proceedings* **157** (1989).
    <https://doi.org/10.1557/PROC-157-745>
[^farhane-2003]: R. Farhane, F. Salvetti, F. Wacquant, C. Laviron,
    B. Froment, A. Muller, A. Pouydebasque and A. Halimaoui,
    "Investigation of the dose loss during annealing in nitrogen of
    shallow-implanted arsenic", *Proc. 11th IEEE International
    Conference on Advanced Thermal Processing of Semiconductors (RTP
    2003)*, pp. 173–176. <https://doi.org/10.1109/RTP.2003.1249144>
[^shibahara-1998]: K. Shibahara, H. Furumoto, K. Egusa, M. Koh and
    S. Yokoyama, "Dopant Loss Origins of Low Energy Implanted Arsenic
    and Antimony for Ultra Shallow Junction Formation", *MRS
    Proceedings* **532** (1998). <https://doi.org/10.1557/PROC-532-23>
[^krieger-1989]: G. Krieger, G. Spadini, P. Cuevas and J. Schuur,
    "Shadowing effects due to tilted arsenic source/drain implant",
    *IEEE Transactions on Electron Devices* **36**(11), 2458–2461
    (1989). <https://doi.org/10.1109/16.43667>
[^jones-1996]: M. Jones and F. Sinclair, "Across-wafer channeling
    variations on batch implanters: a graphical technique to analyze
    spinning disk systems", *Proc. 11th International Conference on
    Ion Implantation Technology* (1996), pp. 264–267.
    <https://doi.org/10.1109/IIT.1996.586257>
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic
    implant", *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 89–92.
    <https://doi.org/10.1109/IIT.1996.586135>
[^current-1998]: M. I. Current, M. Foad, S. Brown, W. Lukaszek and
    M. Vella, "Photoresist effects on wafer charging control:
    current-voltage characteristics measured with Charm-2 monitors
    during high-current As⁺ implantation", *Proc. 1998 International
    Conference on Ion Implantation Technology*, vol. 1, pp. 490–493.
    <https://doi.org/10.1109/IIT.1999.812159>
[^mehta-1996]: S. Mehta, B. Axan, S. Walther and S. Felch,
    "Investigation of negative charging with plasma flood gun (PFG)
    during high current implantation", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 73–76.
    <https://doi.org/10.1109/IIT.1996.586128>
[^smith-1983]: T. C. Smith, "Wafer Cooling and Photoresist Masking
    Problems in Ion Implantation", in *Ion Implantation: Equipment and
    Techniques*, Springer Series in Electrophysics, Springer, 1983,
    pp. 196–213. <https://doi.org/10.1007/978-3-642-69156-0_25>
[^romig-1996]: T. Romig, M. Bishop and V. Rio, "Exploration and
    prevention of photo resist burning in a high current ion
    implanter", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 190–193.
    <https://doi.org/10.1109/IIT.1996.586181>
[^mezack-2000]: G. Mezack, T. Callahan, S. Mehta and U. Jeong,
    "Advantages of the Varian VIISta single wafer high current ion
    implanter for advanced device fabrication", *Proc. 2000
    International Conference on Ion Implantation Technology*,
    pp. 431–434. <https://doi.org/10.1109/IIT.2000.924180>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^current-2017]: M. I. Current, "Ion implantation of advanced silicon
    devices: Past, present and future", *Materials Science in
    Semiconductor Processing* **62**, 13–22 (2017).
    <https://doi.org/10.1016/j.mssp.2016.10.045>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-passives]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the poly, diffusion
    and well resistors, MiM capacitors, varactors and bipolar
    transistors of the test tile, IC-CAP `.mdm` files in
    `sky130_fd_pr/cells/unsorted/`, `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
