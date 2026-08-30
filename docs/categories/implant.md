(category-implant)=
# Ion implantation

## What this class of step does

Ion implantation puts dopant atoms into the silicon by firing them at
the wafer as a beam of ions. A gas such as boron trifluoride, phosphine
or arsine is ionised, the wanted ion is picked out by a magnet
according to its mass, accelerated to a chosen energy and scanned across
the wafer. Wherever the wafer is bare (or covered only by a thin screen
oxide) the ions bury themselves; wherever it is covered by thick
photoresist they stop harmlessly in the resist. The energy sets how deep
the dopant goes and the integrated beam current sets how much goes in.
Implantation is the only doping method in a modern CMOS flow because it
is precise, repeatable and cold: the dose is metered electrically to
better than one per cent and the depth is set by physics rather than by
a diffusion time at high temperature.

Precisely, an implant is specified by species (B⁺, BF₂⁺, P⁺, As⁺, In⁺,
Sb⁺, occasionally Ge⁺ or N⁺), energy (a few keV to a few MeV), dose
(ions per cm², from about 10¹¹ for a threshold adjust to several
10¹⁵ for a source/drain), tilt and twist angles, and the screen film
through which it is done; these ranges are typical industry values
(Plummer, Deal and Griffin, ch. 8). It is always followed, sooner or
later, by an
anneal ({ref}`category-anneal`) that repairs the lattice damage and
moves the dopant onto substitutional sites where it is electrically
active.

The SKY130 flow has 25 implants. In order: the deep n-well; the
threshold-adjust, well and drain-extension implants of the various
transistor flavours; the SONOS punch-through-stop and depletion
implants; the n-channel implant; the poly gate and poly resistor
implants; the arsenic tips and boron halos for the 1.8 V, high-voltage
and lightly-doped transistors; and finally the p⁺ and n⁺ source/drain
implants.

## Physics and engineering background

### Stopping and range: LSS theory

An ion entering silicon loses energy by two mechanisms: elastic
collisions with nuclei (nuclear stopping, {math}`S_n`), which dominate
at low energy and for heavy ions and which displace lattice atoms; and
inelastic interaction with electrons (electronic stopping,
{math}`S_e`), which dominates at high energy and behaves like viscous
drag, {math}`S_e \propto \sqrt{E}` in the LSS regime. The total range
is

```{math}
R = \int_0^{E_0} \frac{dE}{N\,[S_n(E) + S_e(E)]},
```

and what matters for a device is its projection on the beam axis, the
{term}`projected range` {math}`R_p`, together with the standard
deviation of the depth distribution, the {term}`straggle`
{math}`\Delta R_p`, and the lateral straggle {math}`\Delta R_\perp`.
Lindhard, Scharff and Schiøtt derived these quantities from screened
Coulomb potentials in 1963 ([Lindhard, Scharff and Schiøtt 1963][lss]),
and Gibbons's reviews brought the theory into semiconductor practice
([Gibbons 1968][gibbons1]; [Gibbons 1972][gibbons2]). To first order the
as-implanted profile is Gaussian,

```{math}
N(x) = \frac{\Phi}{\sqrt{2\pi}\,\Delta R_p}
\exp\!\left[-\frac{(x - R_p)^2}{2\,\Delta R_p^2}\right],
```

with peak concentration {math}`N_{\max} \approx 0.4\,\Phi/\Delta R_p`
for dose {math}`\Phi`; real profiles are skewed (light ions such as
boron back-scatter and have a deep tail; heavy ions such as arsenic are
skewed towards the surface) and are fitted with Pearson IV
distributions or computed by Monte Carlo codes such as SRIM/TRIM
([SRIM][srim]; [Ziegler, Ziegler and Biersack 2010][ziegler]). Typical
ion energies "are in the range of 10 to 500 keV" and ranges "between
10 nanometers and 1 micrometer" ([Wikipedia: Ion
implantation][wiki-implant]); a 130 nm process spans a wider window,
from a few keV for source/drain extensions to over 1 MeV for deep
n-wells. Because BF₂⁺ dissociates on impact and only 11/49 of its energy
is carried by the boron atom, BF₂ is the way to implant boron shallowly
with a beam energy the tool can control well (Plummer, Deal and
Griffin, ch. 8).

### Channelling

"The range of an ion can be much longer if the ion travels exactly
along a particular direction", such as ⟨110⟩ in silicon, and the effect
is "highly nonlinear, with small variations from perfect orientation
resulting in extreme differences in implantation depth"
([Wikipedia: Ion implantation][wiki-implant]). Production implants
therefore tilt the wafer, conventionally by 7°, twist it to avoid
planar channels, implant through a thin screen oxide that randomises the
ion directions, or pre-amorphise the surface with a germanium or
silicon implant ([Wikipedia: Channelling (physics)][wiki-channel];
Plummer, Deal and Griffin, ch. 8). Tilt has a side effect on a
patterned wafer: the resist edge shadows one side of each opening, so
{term}`halo` and other symmetric implants are done in two or four
rotations ("quad" implants).

### Damage, amorphisation and transient enhanced diffusion

Every ion displaces hundreds to thousands of silicon atoms; at doses
above roughly 10¹⁴–10¹⁵ cm⁻² for arsenic, "the amount of
crystallographic damage can be enough to completely amorphize the
surface" ([Wikipedia: Ion implantation][wiki-implant]). An amorphous
layer regrows epitaxially from the undamaged substrate at 500–600 °C
(solid-phase epitaxy), leaving end-of-range defects at the old
amorphous/crystalline boundary. Below the amorphisation threshold the
implant leaves a supersaturation of silicon self-interstitials, which
during the anneal raise the diffusivity of boron and phosphorus by
orders of magnitude for a few seconds to minutes — transient enhanced
diffusion ({term}`TED`). Eaglesham and co-workers identified the
"+1" interstitials from the implant as the source ([Eaglesham et al.
1994][eaglesham]) and Stolk and co-workers set out the physical
mechanisms ([Stolk et al. 1997][stolk]). TED is the reason that
shallow junctions at the 130 nm node need low thermal budgets and
rapid thermal anneals rather than furnaces, and why the order of
implants and anneals in a flow is not arbitrary.

### Dose control and charging

The dose is measured by integrating the beam current collected in
Faraday cups, corrected for the fraction of the scan that lies on the
wafer; secondary electrons and neutralised ions are the main error
sources. Positive charge delivered to a wafer whose surface is covered
by insulating resist can rupture gate oxides, so implanters flood the
wafer with low-energy electrons from a plasma flood gun. Heavy resist
outgassing at high dose alters the beam neutralisation and is limited
by hard-baking the resist. Dose and energy are verified on bare monitor
wafers by {term}`four-point probe` {term}`sheet resistance` after an
anneal, by modulated-reflectance ("Therma-Wave") measurements for
low-dose implants, and periodically by SIMS profiling
(Plummer, Deal and Griffin, ch. 8; Current [current]).

### Implant classes in a 130 nm CMOS flow

The energies and doses given below are typical industry values for the
node (Plummer, Deal and Griffin, ch. 8; Wolf and Tauber, ch. 9);
SKY130's own implant recipes are not public.

* **Wells and deep wells** (n-well {ref}`NWI <step-018>`, p-well
  {ref}`PWI <step-027>`, deep n-well {ref}`DNI <step-008>`): phosphorus
  or boron at hundreds of keV to over 1 MeV, doses of order
  10¹²–10¹³ cm⁻², from a high-energy implanter. A "retrograde" well
  whose peak lies below the channel gives latch-up immunity and
  punch-through control; ITRS 2001 notes that "the retrograde well
  profile must be less than 0.5 times the drain extension depth to
  improve short channel effects" ([ITRS 2001, Front End
  Processes][itrs2001-fep]). We infer that multiple energies are chained
  (the "NWI2" and "PWI2" steps) to shape the profile.
* **Threshold-adjust and channel implants** (low-Vt, high-Vt, channel,
  punch-through-stop): light doses of order 10¹²–10¹³ cm⁻² of BF₂, B,
  As or P at tens of keV, placed just under the gate oxide to set
  {term}`Vt`, from a medium-current implanter.
* **Poly and resistor implants** ({ref}`P1I <step-050>`,
  {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`): the gate must be
  degenerately doped (high 10¹⁵ cm⁻²) to avoid poly depletion, whereas
  precision resistors need lower, carefully split doses to hit a target
  sheet resistance.
* **Extensions ("tips") and halos** ({ref}`ASTI <step-065>`,
  {ref}`BHI <step-066>`): arsenic at a few keV and about 10¹⁴–10¹⁵ cm⁻²
  self-aligned to the gate edge forms the shallow n-type
  {term}`extension`; boron (or indium) at a large tilt forms the halo
  around it. ITRS 2001 gives extension junction depths for the 130 nm
  node in its Table 51 and treats the p-type boron extension as the
  most challenging junction ([ITRS 2001, Front End Processes][itrs2001-fep]).
* **Source/drain** ({ref}`NSDI <step-086>`, {ref}`PSDI <step-082>`):
  arsenic and boron/BF₂ at several 10¹⁵ cm⁻² and tens of keV, after
  the spacer, from a high-current implanter; these amorphise the
  surface and set the contact resistance.

### Typical implanter classes

Beam-line implanters are classified by current and energy:
"medium current" tools deliver beam currents between about 10 µA and
2 mA with serial (one-wafer) end stations and are used for the
low-dose, tilt-sensitive channel and halo implants; "high current"
tools deliver up to about 30 mA with batch spinning-disc end stations
for source/drain and poly implants; and "high energy" tools use a
radio-frequency linear accelerator or tandem stage to reach 200 keV to
several MeV for wells ([Wikipedia: Ion implantation][wiki-implant];
Current [current]).

## Typical equipment

* **High-current**: Axcelis (formerly Eaton) NV-GSD/200 series batch
  implanters (the GSD line continues as the GSD Ovation, "for general
  high current applications" [axcelis-gsd]); Varian VIISta 80 and
  VIISta HC single-wafer high-current implanters ([Varian VIISta
  HC][viista]); Applied Materials xR series.
* **Medium-current**: Varian E220 and E500 series; Axcelis (Eaton)
  8250 and NV-10; Nissin.
* **High-energy**: Axcelis NV-GSD/HE and GSD/VHE ("10 stage LINAC with
  energies up to 3 MeV" and "14 stage LINAC with energies up to
  4.9 MeV" [axcelis-gsd]); Varian VIISta 3000 and Genus/Varian tandem
  machines.
* **Dose metrology**: four-point probes (KLA-Tencor RS-series
  OmniMap), Therma-Wave TP-series modulated-reflectance monitors, and
  SIMS at an analytical laboratory.

The vendor landscape is summarised in [Wikipedia: Axcelis
Technologies][wiki-axcelis] and [Wikipedia: Varian
Semiconductor][wiki-varian]; a historical survey of commercial
implanters is given by Current [current].

## Typical consumables

* **Source gases**, supplied in sub-atmospheric (SDS) or dilute
  cylinders for safety: boron trifluoride (BF₃) for B⁺ and BF₂⁺,
  phosphine (PH₃) for P⁺, arsine (AsH₃) for As⁺, germane (GeH₄) for
  pre-amorphisation, and hydrogen or xenon as co-gases
  ([Wikipedia: Boron trifluoride][wiki-bf3]; [Wikipedia:
  Phosphine][wiki-ph3]; [Wikipedia: Arsine][wiki-ash3]).
* **Solid sources**: elemental arsenic, phosphorus, antimony or indium
  in vaporiser ovens, for species without a convenient gas.
* **Ion-source parts**: tungsten filaments or indirectly heated
  cathodes, arc chambers, extraction electrodes and insulators, all
  eroded by the plasma and replaced every few hundred hours.
* **Beam-line and end-station parts**: graphite or silicon apertures
  and beam stops, Faraday-cup liners, disc pads, clamp rings, and
  wafer-cooling backside gas.
* **Photoresist** thick enough to stop the ions (a 1 µm resist stops
  MeV phosphorus only marginally, so deep-well masks may need thicker
  resist) and the strip chemistry that removes it afterwards
  ({ref}`category-strip`).

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 8 | {ref}`DNI <step-008>` | Deep N+ implant |
| 15 | {ref}`LVTNI <step-015>` | Low Vt NMOS implantation |
| 18 | {ref}`NWI <step-018>` | N-well implant |
| 19 | {ref}`NWI2 <step-019>` | NWI2 implant |
| 20 | {ref}`LVTPI <step-020>` | Low V P-channel implant |
| 23 | {ref}`PCHI <step-023>` | P-channel implant |
| 24 | {ref}`PNCHI <step-024>` | P-channel BF2 implant |
| 27 | {ref}`PWI <step-027>` | P-well implant |
| 28 | {ref}`PWI2 <step-028>` | PWI2 implant |
| 31 | {ref}`PWDEI1 <step-031>` | PWDEI1 implant |
| 32 | {ref}`PWDEI2 <step-032>` | PWDEI2 implant |
| 37 | {ref}`PTSI <step-037>` | Punch-through stop implant |
| 38 | {ref}`DEPI <step-038>` | Depletion implant |
| 45 | {ref}`NCHI <step-045>` | N-channel implant |
| 50 | {ref}`P1I <step-050>` | Poly1 implant |
| 53 | {ref}`PRI <step-053>` | PRI implant splits |
| 56 | {ref}`UPRI <step-056>` | UPRI implant |
| 65 | {ref}`ASTI <step-065>` | As tip implant |
| 66 | {ref}`BHI <step-066>` | B halo implant |
| 69 | {ref}`HVASTI <step-069>` | HV As N-tip implant |
| 72 | {ref}`LDASTI <step-072>` | LD ASTI implant |
| 73 | {ref}`LDBHI <step-073>` | LD B halo implant |
| 82 | {ref}`PSDI <step-082>` | P+ source drain implant |
| 83 | {ref}`2PSDI <step-083>` | 2nd P+ source drain implant |
| 86 | {ref}`NSDI <step-086>` | N+ source drain implant |

## References

### Cross-check

* J. Lindhard, M. Scharff and H. E. Schiøtt, "Range Concepts and Heavy
  Ion Ranges", *Matematisk-fysiske Meddelelser, Det Kongelige Danske
  Videnskabernes Selskab* **33**(14), 1–42 (1963).
  <https://gymarkiv.sdu.dk/MFM/kdvs/mfm%2030-39/mfm-33-14.pdf>
* J. F. Gibbons, "Ion implantation in semiconductors — Part I: Range
  distribution theory and experiments", *Proceedings of the IEEE*
  **56**(3), 295–319 (1968). <https://doi.org/10.1109/PROC.1968.6273>
* J. F. Gibbons, "Ion implantation in semiconductors — Part II: Damage
  production and annealing", *Proceedings of the IEEE* **60**(9),
  1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
* J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM — The stopping
  and range of ions in matter (2010)", *Nuclear Instruments and Methods
  in Physics Research B* **268**, 1818–1823 (2010).
  <https://doi.org/10.1016/j.nimb.2010.02.091>
* J. F. Ziegler, *SRIM — The Stopping and Range of Ions in Matter*
  (software and documentation). <http://www.srim.org/>
* *ITRS 2001 Edition: Front End Processes* (Table 51, doping
  technology requirements).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* Axcelis Technologies, "GSD Ovation — High Current & High Energy
  Batch Ion Implanters". <https://www.axcelis.com/products/gsd-ovation/>
* Legacy Semi, "Varian VIISta HC High Current Implanter" (listing).
  <https://www.semimarket.com/item/varian-viista-hc-high-current-implanter/94062>
* W. Shockley, "Forming semiconductive devices by ionic bombardment",
  US Patent 2,787,564 (1957).
  <https://patents.google.com/patent/US2787564A/en>

### High-level

* Wikipedia, "Ion implantation".
  <https://en.wikipedia.org/wiki/Ion_implantation>
* Wikipedia, "Stopping and Range of Ions in Matter".
  <https://en.wikipedia.org/wiki/Stopping_and_Range_of_Ions_in_Matter>
* Wikipedia, "Channelling (physics)".
  <https://en.wikipedia.org/wiki/Channelling_(physics)>
* Wikipedia, "Dopant". <https://en.wikipedia.org/wiki/Dopant>
* Wikipedia, "Threshold voltage".
  <https://en.wikipedia.org/wiki/Threshold_voltage>
* Wikipedia, "Boron trifluoride".
  <https://en.wikipedia.org/wiki/Boron_trifluoride>
* Wikipedia, "Phosphine". <https://en.wikipedia.org/wiki/Phosphine>
* Wikipedia, "Arsine". <https://en.wikipedia.org/wiki/Arsine>
* Wikipedia, "Axcelis Technologies".
  <https://en.wikipedia.org/wiki/Axcelis_Technologies>
* Wikipedia, "Varian Semiconductor".
  <https://en.wikipedia.org/wiki/Varian_Semiconductor>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 8
  ("Ion Implantation").
* S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI Era,
  Vol. 1*, 2nd ed., Lattice Press, 2000, ISBN 978-0-9616721-6-4, ch. 9
  ("Ion Implantation for VLSI").
* S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics and
  Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7, ch. 13.
* S. A. Campbell, *Fabrication Engineering at the Micro- and
  Nanoscale*, 4th ed., Oxford University Press, 2013,
  ISBN 978-0-19-986122-4, ch. 5.
* M. Quirk and J. Serda, *Semiconductor Manufacturing Technology*,
  Prentice Hall, 2001, ISBN 978-0-13-081520-0, ch. 17.

### Deep dive

* D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and J. M. Poate,
  "Implantation and transient B diffusion in Si: The source of the
  interstitials", *Applied Physics Letters* **65**, 2305–2307 (1994).
  <https://doi.org/10.1063/1.112725>
* P. A. Stolk et al., "Physical mechanisms of transient enhanced
  dopant diffusion in ion-implanted silicon", *Journal of Applied
  Physics* **81**, 6031–6050 (1997). <https://doi.org/10.1063/1.364452>
* M. I. Current, "Ion implantation of advanced silicon devices: Past,
  present and future", *Materials Science in Semiconductor Processing*
  **62**, 13–22 (2017). <https://doi.org/10.1016/j.mssp.2016.10.045>
* R. H. Dennard et al., "Design of ion-implanted MOSFET's with very
  small physical dimensions", *IEEE Journal of Solid-State Circuits*
  **9**(5), 256–268 (1974). <https://doi.org/10.1109/JSSC.1974.1050511>
* A. Hössinger, *Simulation of Ion Implantation for ULSI Technology*,
  PhD thesis, TU Wien, 2000.
  <https://www.iue.tuwien.ac.at/phd/hoessinger/>

[wiki-implant]: https://en.wikipedia.org/wiki/Ion_implantation
[wiki-channel]: https://en.wikipedia.org/wiki/Channelling_(physics)
[wiki-bf3]: https://en.wikipedia.org/wiki/Boron_trifluoride
[wiki-ph3]: https://en.wikipedia.org/wiki/Phosphine
[wiki-ash3]: https://en.wikipedia.org/wiki/Arsine
[wiki-axcelis]: https://en.wikipedia.org/wiki/Axcelis_Technologies
[wiki-varian]: https://en.wikipedia.org/wiki/Varian_Semiconductor
[lss]: https://gymarkiv.sdu.dk/MFM/kdvs/mfm%2030-39/mfm-33-14.pdf
[gibbons1]: https://doi.org/10.1109/PROC.1968.6273
[gibbons2]: https://doi.org/10.1109/PROC.1972.8854
[srim]: http://www.srim.org/
[ziegler]: https://doi.org/10.1016/j.nimb.2010.02.091
[eaglesham]: https://doi.org/10.1063/1.112725
[stolk]: https://doi.org/10.1063/1.364452
[current]: https://doi.org/10.1016/j.mssp.2016.10.045
[itrs2001-fep]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf
[axcelis-gsd]: https://www.axcelis.com/products/gsd-ovation/
[viista]: https://www.semimarket.com/item/varian-viista-hc-high-current-implanter/94062
