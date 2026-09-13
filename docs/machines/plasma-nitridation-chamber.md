(machine-plasma-nitridation-chamber)=
# Plasma nitridation chamber

A plasma nitridation chamber exposes a finished thin gate oxide, for
seconds, to a low-pressure nitrogen plasma, so that nitrogen is
incorporated near the top surface of the oxide without heating the
wafer to the temperatures a thermal nitridation needs. The nitrogen
blocks boron from a p⁺ polysilicon gate and lowers gate leakage; kept
near the top surface, it can avoid the mobility loss that nitrogen at the
silicon interface causes,[^pat-rpn-ti][^hattangady-1998] although a heavy
plasma nitridation can itself cost transconductance.[^lek-2002] The
class arrived as a production tool around the 130 nm
node.[^amat-dpn-2001] This page describes the class in general, lists
representative models, and then says what SkyWater has published and
which SKY130 step this reference associates with the class. Nitrided
oxides in general are on the {ref}`oxidation category page
<category-oxidation>`.

| | Plasma nitridation chamber |
|---|---|
| What it does | Incorporates nitrogen into the surface of an ultra-thin gate oxide "to prevent boron penetration and reduce leakage current", in Applied Materials' description of its DPN chamber for "130nm and below device designs".[^amat-dpn-2001] |
| Plasma source | A remote He–N₂ plasma;[^hattangady-1995] "a helicon plasma source";[^kraft-1997] inductive coupling in Applied Materials' Decoupled Plasma Nitridation (DPN);[^pat-pna-amat] later, a microwave "slot plane antenna (SPA) plasma source".[^pat-spa-tel] |
| Pressure, power and time | "about 5-20 mTorr", "200-800 Watt" and "pulse at about 5-15 kHz" for DPN;[^pat-pna-amat] "around 4 mTorr" and "around 1-60 seconds" in a Texas Instruments high-density plasma process.[^pat-rpn-ti] |
| Nitrogen profile | "approximately 15 at. % nitrogen into the top 0.5 nm" of an oxide "in 10 s";[^kraft-1997] nitrogen "confined to the immediate vicinity of the surface".[^hattangady-1995] |
| Wafer temperature | Remote plasma nitridation "at low temperatures, 23 and 300 °C";[^hattangady-1995] 300 °C in a later remote-plasma study.[^niimi-2002] |
| Wafer handling | Single wafer, on a cluster tool with the other gate-stack chambers: DPN "can be easily integrated on a single cluster tool platform with our other single-wafer gate fabrication technologies".[^amat-dpn-2001] |
| 200 mm era | Applied Materials' DPN chamber, introduced for "130nm and below device designs" in 2001 with "over a dozen DPN chambers in use for production" (wafer size not stated);[^amat-dpn-2001] the DPN Centura.[^pat-pna-amat] |
| SkyWater-listed tool | None named; SkyWater lists "Nitrided gate oxide" as a special module without a tool[^skw-01] |
| SKY130 steps | No step as the process tool, 1 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-plasma-nitridation-chamber-steps>` |

## What the machine class is and how it works

### Why plasma rather than heat

Nitrogen can be put into an oxide thermally. Ito, Nozaki and Ishikawa
showed that oxide "can be converted directly to silicon nitride or
oxynitride at the surface" by heating in ammonia, with graded films "At
temperatures above 900°C";[^ito-1980] rapid thermal processing in N₂O gives
an oxynitride with "nitrogen pileup at the Si/SiO₂ interface" and
"excellent diffusion barrier properties" against boron.[^hwang-1991] A
Texas Instruments patent sets out the drawbacks that plasma nitridation
was meant to remove: with ammonia, "in order to get the ammonia to
penetrate the gate oxide, temperatures in excess of 1000° C. are
required", once the reaction has begun "it is difficult to control the
concentration of the nitrogen", and "Excessive nitrogen near the
interface between the semiconductor substrate and the gate oxide can
adversely affect the threshold voltage and degrade the channel
mobility".[^pat-rpn-ti] Ammonia also brings hydrogen, which Hori et al.
removed by rapid reoxidation to improve charge trapping.[^hori-1989] A
plasma supplies reactive nitrogen at the surface at low wafer temperature,
and the ion energy, flux and exposure time set how deep it goes.

### Remote plasma nitridation

In a remote plasma the discharge is struck away from the wafer and
neutral excited species and a reduced ion flux reach the oxide.
Hattangady, Niimi and Lucovsky incorporated nitrogen "selectively at the
top surface of a conventional thermal gate oxide by nitridation with a
remote He–N₂ plasma", with the concentration set "by a combination of
substrate temperature and duration of plasma exposure"; a subsequent
"Rapid thermal annealing (RTA) of the nitrided oxide at 900 °C in N₂ and
N₂O does not change the N content".[^hattangady-1995] Niimi et al. later
separated the mechanisms: at 0.1 Torr an upstream He/N₂ plasma
"incorporates nitrogen at the top surface", at 0.3 Torr "a lower
concentration of nitrogen distributed throughout the film is obtained",
and "N₂⁺ species are primarily responsible for top surface nitridation at
0.1 Torr".[^niimi-2002]

Texas Instruments' group listed the attractions for production: "the
ability to start with a relatively thicker oxide where thickness targeting
and process control is easier", "an essentially self-limiting process
leading to 'built-in' uniformity of that of starting oxide", and
nitrided oxides that "do not show the typical mobility and transconductance
degradation observed (particularly in PMOS devices) with thermally grown
oxynitride and nitride films".[^hattangady-1998] Kapila et al. modelled the
process to maximise "the nitrogen concentration at the top surface and the
total integrated nitrogen dose (for prevention of boron penetration)" while
"minimizing nitrogen concentration at the bottom interface".[^kapila-1999]

### High-density and decoupled plasma nitridation

A high-density source brings a large flux of low-energy ions to the wafer.
Kraft et al. used "a high density nitrogen plasma generated with a helicon
plasma source" to put "approximately 15 at. % nitrogen into the top 0.5 nm"
of an oxide "in 10 s with a high flux of low energy ions … accelerated in
the plasma sheath towards … an electrically floating silicon dioxide
surface"; "The nitrogen ion energy, ion current density, and exposure time
determine the nitrogen range and dose".[^kraft-1997] The related Texas
Instruments patent names the candidate sources — "a helicon source, a
helical-resonator source, electron-cyclotron resonance source, or an
inductively coupled source" — and nitrogen sources "N₂, NH₃, NO, N₂O, or
a mixture thereof", at a pressure "around 4 mTorr" and an exposure of
"around 1-60 seconds".[^pat-rpn-ti]

Applied Materials' Decoupled Plasma Nitridation became the production form
of the class. An Applied Materials patent describes it as "a technology
using inductive coupling to generate nitrogen plasma and incorporate a high
level of nitrogen into an oxide film", in which the oxide "is bombarded with
nitrogen ions which break the SiO₂ film forming a silicon oxynitride film",
run at "about 5-20 mTorr or 10-20 mTorr, with a plasma power of 200-800
Watt", with "a pulse radio frequency plasma process at about 10-20 MHz and
pulse at about 5-15 kHz", and names the "DPN Centura™" as a suitable
chamber.[^pat-pna-amat] The modulation of the source power shapes the
plasma's electron temperature: a further Applied Materials patent uses a
"smooth-varying modulated RF power source to reduce electron temperature
spike", and reports that "channel mobility and gate leakage current results
are improved" compared with square-wave modulation.[^pat-dpn-rf-amat]

### The post-nitridation anneal

A plasma-nitrided oxide is annealed before the gate is deposited. A
Chartered Semiconductor patent reports that the conventional anneal "in
pure helium to remove structural defects in the oxide" degraded device
performance, and replaces it with an anneal "in a 1:4 oxygen-nitrogen
mixture (1,050° C. at about 10 torr)".[^pat-dpn-anneal-chartered] Applied
Materials later proposed two steps, the first in "an inert ambient with a
first partial pressure of oxygen" and the second with a greater oxygen
partial pressure.[^pat-pna-amat] A 1050 °C, 10-torr anneal is a
single-wafer rapid thermal condition (inference;
{ref}`machine-rapid-thermal-processor`), and Applied Materials presented
DPN as a chamber to be integrated "on a single cluster tool platform with
our other single-wafer gate fabrication technologies".[^amat-dpn-2001]

### Microwave slot-antenna plasma

A later form uses a microwave plasma of very low electron temperature. A
Tokyo Electron and IBM patent describes a "slot plane antenna (SPA) plasma
source" whose plasma "is characterized by low electron temperature (less
than about 1.5 eV) and high plasma density (e.g., >about 1×10¹²/cm³), that
enables damage-free processing of gate stacks", naming "a TRIAS™ SPA
processing system".[^pat-spa-tel] Tokyo Electron describes its Trias SPA
series as generating "high-density, low-electron temperature plasma to
enable, low-damage, low-temperature" processing, and its current successor
as a 300 mm system.[^tel-triase]

## Representative 200 mm-era models

* **Applied Materials.** The DPN chamber, introduced for "130nm and below
  device designs", with "over a dozen DPN chambers in use for production,
  as well as in 100nm-generation gate development" at the time of the
  announcement (Light Reading's copy is dated 2001-11-28);[^amat-dpn-2001]
  sold as the DPN Centura.[^pat-pna-amat]
* **Texas Instruments (process development).** The helicon and remote
  plasma nitridation work of Hattangady, Kraft and co-workers, which
  describes processes rather than a commercial tool.[^kraft-1997][^hattangady-1998][^pat-rpn-ti]
* **Tokyo Electron.** The Trias SPA series, whose slot-plane-antenna plasma
  is described for nitrided gate dielectrics in a patent filed in
  2005;[^pat-spa-tel][^tel-triase] this is a later, 300 mm-oriented
  tool.

Plasma nitridation arrived near the end of the 200 mm era, and the device
papers cited on this page name the process (DPN, RPN) rather than a
chamber model.[^lek-2002][^chen-2002-rpn]

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page names no plasma nitridation
tool. Among its "Special Modules" it lists:[^skw-01]

> "Nitrided gate oxide"

without a tool, a method or a gate-oxide thickness. The nitriding gases
the page mentions elsewhere are "NH3" on the "Ag Heatpulse 8808" and on
the "Iridia" asher, and "LPCVD nitride, with NH3 and also DH3" on the
furnaces; no N₂O or NO is listed, and no plasma tool is described as
nitriding.[^skw-01] The {ref}`LVGOX <step-047>` page calls the Heatpulse's
NH₃ capability "the one public hint of how SkyWater's 'Nitrided gate oxide'
module might be run".

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` there
is **no evidence** of a plasma nitridation chamber at SkyWater: no
SkyWater page, filing, posting or profile names one. The special module is
**strong** evidence that SkyWater offers a nitrided gate oxide,[^skw-01]
but not of how it is made, and not that SKY130 uses it. The caveats that
apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`; the
machines index lists this class among those "with no named SkyWater
tool".

(machine-plasma-nitridation-chamber-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a plasma nitridation
chamber as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

*alternative:* {ref}`LVGOX <step-047>`

How the step pages grade the SkyWater tools that could provide a nitrided
oxide ("Machines likely used at SkyWater"), as collected on the machines
index:

* **Special modules "Nitrided gate oxide", "Ti and Co Silicide", "W plug
  dual damascene"** — *inference for use in SKY130 (nitrided oxide):* {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`; *strong for the capability (silicide, W plug):* {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>`
* **"Ag Heatpulse 8808 …"** — *weak:* {ref}`LVGOX <step-047>`,
  {ref}`IOX45 <step-063>` (the LVGOX page names its NH₃ line as the one
  public hint); see {ref}`machine-rapid-thermal-processor`.

No step page grades a plasma nitridation tool at SkyWater, because none is
named.

## Consumables and facilities

The process gases and precursors are described on the
{ref}`process gases <material-process-gases>` and
{ref}`precursors <material-precursors>` pages.
None of the SkyWater sources describes a nitridation process; what the
class needs is summarised from the public process descriptions.

* **Process gases.** Nitrogen, often diluted in helium for remote
  plasmas;[^hattangady-1995][^niimi-2002] N₂ at "about 100-200 sccm" for
  DPN;[^pat-pna-amat] other nitrogen sources (NH₃, NO, N₂O) in the Texas
  Instruments process.[^pat-rpn-ti]
* **RF or microwave power and vacuum.** An inductively coupled RF source
  pulsed at kHz rates for DPN,[^pat-pna-amat][^pat-dpn-rf-amat] or a
  microwave slot antenna;[^pat-spa-tel] a pumping system for operation at
  millitorr pressures.[^pat-pna-amat]
* **Post-nitridation anneal gases.** Oxygen and nitrogen, or an inert gas
  with a controlled oxygen partial pressure, for the anneal that
  follows.[^pat-dpn-anneal-chartered][^pat-pna-amat]
* **Nitrogen metrology.** Nitrogen dose and profile by XPS and SIMS in
  development;[^hattangady-1995][^kapila-1999] boron penetration through a
  DPN oxide measured by backside SIMS.[^yeo-2003]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. Whether SKY130's gate oxides are nitrided,
and how, is not public.

* **Three routes, one open question.** The {ref}`LVGOX <step-047>` page
  describes thermal nitridation in NH₃, rapid thermal nitridation in NO or
  N₂O, and plasma nitridation as the public routes to a nitrided thin
  oxide, and treats nitridation itself as an inference from SkyWater's
  special module. Only the ammonia route uses a gas SkyWater lists on a
  thermal tool.[^skw-01]
* **Where the nitrogen goes.** Plasma nitridation places nitrogen at the
  top of the oxide, where it blocks boron from the p⁺ gate: Lek et al.
  attribute DPN's success in "blocking boron penetration" to "its
  capability in incorporating a high level of nitrogen to near the top
  interface", but also measured "a degradation in transconductance" and
  higher interface-trap density than with thermal nitridation.[^lek-2002]
  Thermal N₂O nitridation instead piles nitrogen up at the silicon
  interface.[^hwang-1991]
* **A limit on oxide thickness.** Chen et al. observed "the radical-induced
  re-oxidation effect … as the base-oxide thickness less than 20 Å", found
  that remote plasma nitridation still reduced equivalent oxide thickness
  for base oxides "thicker than 17 Å", and put the limit at "14 Å
  EOT".[^chen-2002-rpn] The {ref}`LVGOX <step-047>` page gives about 4 nm
  as the industry-typical thickness of such a thin oxide, above that
  range.
* **An anneal after nitridation.** A plasma-nitrided oxide needs a
  post-nitridation anneal in a controlled oxygen and nitrogen
  ambient;[^pat-dpn-anneal-chartered][^pat-pna-amat] SkyWater's Heatpulse
  lists O₂ and N₂,[^skw-01] so the anneal half of such a sequence would fit
  the listed RTA (inference); the plasma half has no listed tool.
* **The 5 V oxide.** The class is aimed at ultra-thin oxides;[^amat-dpn-2001]
  no step page proposes plasma nitridation for the thick
  {ref}`GOX100 <step-043>` oxide.

## Related pages

* {ref}`category-oxidation` — nitrided oxides and ONO stacks in context.
* {ref}`machine-vertical-furnace-oxidation` — the furnace in which the
  base oxide would be grown.
* {ref}`machine-rapid-thermal-processor` — the Heatpulse, its NH₃ line
  and the post-nitridation anneal.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`category-implant` — the p⁺ gate doping whose boron the nitrogen
  is meant to stop.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.
* {ref}`material-precursors` — silane, dichlorosilane, TEOS, BTBAS,
  ammonia, SiF₄, ozone and WF₆.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "Nitrided gate
  oxide" special module and the absence of a nitridation tool.[^skw-01]
* Applied Materials, DPN chamber announcement (Light Reading, 2001) — the
  purpose, node and installed base of the first production
  chamber.[^amat-dpn-2001]
* Olsen (Applied Materials), US 7,429,538 — DPN described with its
  pressure, power, pulsing and the DPN Centura.[^pat-pna-amat]
* Kraft, Hattangady and Grider (Texas Instruments), US 6,136,654 — plasma
  sources and conditions for nitriding gate oxides.[^pat-rpn-ti]
* Tokyo Electron, *Trias e+ Series* — the SPA plasma series and its
  successor.[^tel-triase]

### High-level understanding

* Green et al., *J. Appl. Phys.* 2001 — the review of SiO₂ and oxynitride
  gate dielectrics that sets out why nitrogen is added.[^green-2001]
* Buchanan, *IBM J. Res. Dev.* 1999 — oxynitrides against boron
  penetration and leakage in gate-dielectric scaling.[^buchanan-1999]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — gate oxides and
  their processing.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — gate dielectrics
  in deep-submicron flows.[^txt-05]

### Deep dive

* Hattangady, Niimi and Lucovsky, *Appl. Phys. Lett.* 1995 — remote
  plasma nitridation of the gate-oxide surface.[^hattangady-1995]
* Kraft et al., *JVST B* 1997 — helicon high-density nitrogen plasma
  nitridation of SiO₂.[^kraft-1997]
* Hattangady et al., *Proc. SPIE* 1998 — remote-plasma nitrided oxides for
  ultrathin gate dielectrics.[^hattangady-1998]
* Kapila et al., *J. Electrochem. Soc.* 1999 — modelling and optimising the
  nitrogen profile of remote plasma nitridation.[^kapila-1999]
* Niimi et al., *J. Appl. Phys.* 2002 — the species behind surface and
  sub-surface remote plasma nitridation.[^niimi-2002]
* Chen et al. (TSMC), *IEEE TED* 2002 — the base-oxide limit of remote
  plasma nitridation.[^chen-2002-rpn]
* Lek et al., *Semicond. Sci. Technol.* 2002 — DPN against thermal
  nitridation in p-channel MOSFETs.[^lek-2002]
* Yeo et al., *JVST B* 2003 — boron penetration through DPN oxide by
  backside SIMS.[^yeo-2003]
* Ito, Nozaki and Ishikawa, *J. Electrochem. Soc.* 1980 — thermal
  nitridation of oxide in ammonia.[^ito-1980]
* Hori, Iwasaki and Tsuji, *IEEE TED* 1989 — reoxidised nitrided oxides and
  hydrogen.[^hori-1989]
* Hwang et al., *Appl. Phys. Lett.* 1991 — RTP N₂O oxynitride and interface
  nitrogen pile-up.[^hwang-1991]
* Zhong et al. (Chartered), US 2003/0170956 — an oxygen–nitrogen anneal
  after DPN.[^pat-dpn-anneal-chartered]
* Kraus and Chua (Applied Materials), US 7,514,373 — smooth-modulated RF to
  limit electron-temperature spikes in plasma nitridation.[^pat-dpn-rf-amat]
* Igeta et al. (Tokyo Electron, IBM), US 7,501,352 — oxynitride formation
  with a slot-plane-antenna plasma.[^pat-spa-tel]

## Open questions

* Whether SKY130's 1.8 V gate oxide is nitrided, and if so whether by
  plasma, NH₃, NO or N₂O, is not public; SkyWater's "Nitrided gate oxide"
  special module names no method.[^skw-01]
* Whether SkyWater has a plasma nitridation chamber at all is not stated.
* The model list above is incomplete: it covers the Applied Materials and
  Tokyo Electron tools and the Texas Instruments process work for which a
  public description was found, not every plasma nitridation tool.

<!-- footnotes -->

[^amat-dpn-2001]: Light Reading, *Applied Materials Nitridates*
    (reproducing Applied Materials' announcement of its DPN chamber),
    2001-11-28, accessed 2026-09-13.
    <https://www.lightreading.com/business-management/applied-materials-nitridates>
[^hattangady-1995]: S. V. Hattangady, H. Niimi and G. Lucovsky,
    "Controlled nitrogen incorporation at the gate oxide surface",
    *Applied Physics Letters* **66**(25), 3495–3497 (1995).
    <https://doi.org/10.1063/1.113775>
[^kraft-1997]: R. Kraft, T. P. Schneider, W. W. Dostalik and
    S. Hattangady, "Surface nitridation of silicon dioxide with a high
    density nitrogen plasma", *Journal of Vacuum Science & Technology
    B* **15**(4), 967–970 (1997). <https://doi.org/10.1116/1.589516>
[^pat-pna-amat]: C. S. Olsen (Applied Materials), *Manufacturing method
    for two-step post nitridation annealing of plasma nitrided gate
    dielectric*, US 7,429,538 B2, filed 2005-06-27, granted 2008-09-30.
    <https://patents.google.com/patent/US7429538B2/en>
[^pat-spa-tel]: M. Igeta, C. Wajda, D. L. O'Meara, K. Scheer and
    T. Eurakawa (Tokyo Electron; International Business Machines),
    *Method and system for forming an oxynitride layer*, US 7,501,352 B2,
    filed 2005-03-30, granted 2009-03-10.
    <https://patents.google.com/patent/US7501352B2/en>
[^pat-rpn-ti]: R. Kraft, S. Hattangady and D. T. Grider (Texas
    Instruments), *Method of forming thin silicon nitride or silicon
    oxynitride gate dielectrics*, US 6,136,654 A, filed 1997-12-04,
    granted 2000-10-24. <https://patents.google.com/patent/US6136654A/en>
[^niimi-2002]: H. Niimi, A. Khandelwal, H. H. Lamb and G. Lucovsky,
    "Reaction pathways in remote plasma nitridation of ultrathin SiO₂
    films", *Journal of Applied Physics* **91**(1), 48–55 (2002).
    <https://doi.org/10.1063/1.1419208>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; special modules and thermal entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^ito-1980]: T. Ito, T. Nozaki and H. Ishikawa, "Direct Thermal
    Nitridation of Silicon Dioxide Films in Anhydrous Ammonia Gas",
    *Journal of The Electrochemical Society* **127**(9), 2053–2057
    (1980). <https://doi.org/10.1149/1.2130065>
[^hwang-1991]: H. Hwang, W. Ting, D.-L. Kwong and J. Lee, "A physical
    model for boron penetration through an oxynitride gate dielectric
    prepared by rapid thermal processing in N₂O", *Applied Physics
    Letters* **59**(13), 1581–1582 (1991).
    <https://doi.org/10.1063/1.106290>
[^hori-1989]: T. Hori, H. Iwasaki and K. Tsuji, "Electrical and physical
    properties of ultrathin reoxidized nitrided oxides prepared by rapid
    thermal processing", *IEEE Transactions on Electron Devices*
    **36**(2), 340–350 (1989). <https://doi.org/10.1109/16.19935>
[^hattangady-1998]: S. Hattangady, D. T. Grider, R. Kraft, W.-T. Shiau,
    M. A. Douglas, P. Nicollian, M. Rodder, G. A. Brown, A. Chatterjee,
    J. C. Hu, S. Aur, H.-L. Tsai, R. A. Chapman, R. H. Eklund, I.-C. Chen
    and M. F. Pas, "Remote plasma nitrided oxides for ultrathin gate
    dielectric applications", *Proc. SPIE* **3506**, 30 (1998).
    <https://doi.org/10.1117/12.323956>
[^kapila-1999]: D. Kapila, S. Hattangady, M. Douglas, R. Kraft and
    M. Gribelyuk, "Modeling and Optimization of Oxynitride Gate
    Dielectrics Formation by Remote Plasma Nitridation of Silicon
    Dioxide", *Journal of The Electrochemical Society* **146**(3),
    1111–1116 (1999). <https://doi.org/10.1149/1.1391730>
[^pat-dpn-rf-amat]: P. A. Kraus and T. C. Chua (Applied Materials),
    *Method and apparatus for plasma nitridation of gate dielectrics using
    amplitude modulated radio-frequency energy*, US 7,514,373 B2, filed
    2006-05-31 (priority 2003-05-28), granted 2009-04-07.
    <https://patents.google.com/patent/US7514373B2/en>
[^pat-dpn-anneal-chartered]: D. Zhong, Y. Tan, C. Ang and J. Zheng
    (Chartered Semiconductor Manufacturing), *Ultra-thin gate oxide
    through post decoupled plasma nitridation anneal*, US 2003/0170956 A1,
    filed 2002-03-06, published 2003-09-11.
    <https://patents.google.com/patent/US20030170956A1/en>
[^tel-triase]: Tokyo Electron, *Deposition Trias e+ Series*, product
    page, accessed 2026-09-13. <https://www.tel.com/product/triase.html>
[^lek-2002]: C. M. Lek, B. J. Cho, C. H. Ang, S. S. Tan, W. Y. Loh,
    J. Z. Zhen and L. Chan, "Impact of decoupled plasma nitridation of
    ultra-thin gate oxide on the performance of p-channel MOSFETs",
    *Semiconductor Science and Technology* **17**(6), L25–L28 (2002).
    <https://doi.org/10.1088/0268-1242/17/6/101>
[^chen-2002-rpn]: C.-H. Chen, Y.-K. Fang, S.-F. Ting, W.-T. Hsieh,
    C.-W. Yang, T.-H. Hsu, M.-C. Yu, T.-L. Lee, S.-C. Chen, C.-H. Yu and
    M.-S. Liang, "Downscaling limit of equivalent oxide thickness in
    formation of ultrathin gate dielectric by thermal-enhanced remote
    plasma nitridation", *IEEE Transactions on Electron Devices*
    **49**(5), 840–846 (2002). <https://doi.org/10.1109/16.998593>
[^yeo-2003]: K. L. Yeo, A. T. S. Wee, R. Liu, F. F. Zhou and A. See,
    "Investigation of boron penetration through decoupled plasma nitrided
    gate oxide using backside secondary ion mass spectrometry depth
    profiling", *Journal of Vacuum Science & Technology B* **21**(1),
    193–197 (2003). <https://doi.org/10.1116/1.1535925>
[^green-2001]: M. L. Green, E. P. Gusev, R. Degraeve and E. L.
    Garfunkel, "Ultrathin (<4 nm) SiO₂ and Si–O–N gate dielectric layers
    for silicon microelectronics: Understanding the processing,
    structure, and physical and electrical limits", *Journal of Applied
    Physics* **90**(5), 2057–2121 (2001).
    <https://doi.org/10.1063/1.1385803>
[^buchanan-1999]: D. A. Buchanan, "Scaling the gate dielectric:
    Materials, integration, and reliability", *IBM Journal of Research and
    Development* **43**(3), 245–264 (1999).
    <https://doi.org/10.1147/rd.433.0245>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
