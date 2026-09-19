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
(ions per cm², from about 10¹¹ for a {term}`threshold adjust <threshold-adjust implant>` to several 10¹⁵
for a source/drain), tilt and twist angles, and the screen film through
which it is done; these ranges are typical industry values.[^txt-01] It
is always followed, sooner or later, by an anneal
({ref}`category-anneal`) that repairs the lattice damage and moves the
dopant onto substitutional sites where it is electrically active.

The SKY130 flow has 25 implants. In order: the deep n-well; the
threshold-adjust, well and drain-extension implants of the various
transistor flavours; the punch-through-stop and depletion implants
(which sit among the {term}`SONOS` steps); the n-channel implant; the poly gate
and {term}`poly resistor` implants; the arsenic tips and boron halos for the
1.8 V, high-voltage and lightly-doped transistors; and finally the p⁺
and n⁺ source/drain implants.

## Physics and engineering background

### Stopping and range: LSS theory

An ion entering silicon loses energy by two mechanisms: elastic
collisions with nuclei (nuclear stopping, {math}`S_n`), which dominate
at low energy and for heavy ions and which displace lattice atoms; and
inelastic interaction with electrons (electronic stopping,
{math}`S_e`), which dominates at high energy and behaves like viscous
drag, {math}`S_e \propto \sqrt{E}` in the {term}`LSS <LSS theory>` regime. The total range
is

```{math}
R = \int_0^{E_0} \frac{dE}{N\,[S_n(E) + S_e(E)]},
```

and what matters for a device is its projection on the beam axis, the
{term}`projected range` {math}`R_p`, together with the standard
deviation of the depth distribution, the {term}`straggle` {math}`\Delta
R_p`, and the lateral straggle {math}`\Delta R_\perp`. Lindhard, Scharff
and Schiøtt derived these quantities from screened Coulomb potentials in
1963,[^lindhard-1963] and Gibbons's reviews brought the theory into
semiconductor practice.[^gibbons-1968][^gibbons-1972] To first order the
as-implanted profile is Gaussian,

```{math}
N(x) = \frac{\Phi}{\sqrt{2\pi}\,\Delta R_p}
\exp\!\left[-\frac{(x - R_p)^2}{2\,\Delta R_p^2}\right],
```

with peak concentration {math}`N_{\max} \approx 0.4\,\Phi/\Delta R_p`
for dose {math}`\Phi`; real profiles are skewed (light ions such as
boron back-scatter and have a deep tail; heavy ions such as arsenic are
skewed towards the surface) and are fitted with Pearson IV distributions
or computed by Monte Carlo codes such as
SRIM/TRIM.[^srim][^ziegler-2010] Typical ion energies "are in the range
of 10 to 500 keV" and ranges "between 10 nanometers and 1
micrometer";[^wiki-implant] a 130 nm process spans a wider window, from
a few keV for source/drain extensions to over 1 MeV for deep n-wells
(typical).[^txt-01] Because BF₂⁺ dissociates on impact and only 11/49 of
its energy is carried by the boron atom, BF₂ is the way to implant boron
shallowly with a beam energy the tool can control well.[^txt-01]

### Channelling

"The range of an ion can be much longer if the ion travels exactly along
a particular direction", such as ⟨110⟩ in silicon, and the effect is
"highly nonlinear, with small variations from perfect orientation
resulting in extreme differences in implantation depth".[^wiki-implant]
Production implants therefore tilt the wafer, conventionally by 7°,
twist it to avoid planar channels, implant through a thin {term}`screen oxide`
that randomises the ion directions, or pre-amorphise the surface with a
germanium or silicon implant.[^wiki-channel][^txt-01] Tilt has a side
effect on a patterned wafer: the resist edge {term}`shadows <shadowing>` one side of each
opening, so {term}`halo` and other symmetric implants are done in two or
four rotations ("quad" implants).

### Damage, amorphisation and transient enhanced diffusion

Every ion displaces hundreds to thousands of silicon atoms; at doses
above roughly 10¹⁴–10¹⁵ cm⁻² for arsenic, "the amount of
crystallographic damage can be enough to completely amorphize the
surface".[^wiki-implant] An amorphous layer regrows epitaxially from the
undamaged substrate at 500–600 °C ({term}`solid-phase epitaxy`),[^txt-01]
leaving end-of-range defects at the old amorphous/crystalline boundary.
Below the amorphisation threshold the implant leaves a supersaturation
of silicon self-interstitials, which during the anneal raise the
diffusivity of boron and phosphorus by orders of magnitude for a few
seconds to minutes — transient enhanced diffusion ({term}`TED`).
Eaglesham and co-workers identified the "+1" interstitials from the
implant as the source[^eaglesham-1994] and Stolk and co-workers set out
the physical mechanisms.[^stolk-1997] TED is the reason that shallow
junctions at the 130 nm node need low {term}`thermal budgets <thermal budget>` and rapid thermal
anneals rather than furnaces, and why the order of implants and anneals
in a flow is not arbitrary.

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
low-dose implants, and periodically by SIMS profiling.[^txt-01][^current-2017]

### Implant classes in a 130 nm CMOS flow

The energies and doses given below are typical industry values for the
node;[^txt-01][^txt-02]
SKY130's own implant recipes are not public.

* **Wells and deep wells** (n-well {ref}`NWI <step-018>`, p-well
  {ref}`PWI <step-027>`, deep n-well {ref}`DNI <step-008>`): phosphorus
  or boron at hundreds of keV to over 1 MeV, doses of order 10¹²–10¹³
  cm⁻², from a high-energy implanter. A "retrograde" well whose peak
  lies below the channel gives latch-up immunity and {term}`punch-through`
  control; ITRS 2001 notes that "the retrograde well profile must be
  less than 0.5 times the drain extension depth to improve short channel
  effects".[^itrs-01] We infer that multiple energies are chained (the
  "NWI2" and "PWI2" steps) to shape the profile.
* **Threshold-adjust and channel implants** (low-Vt, high-Vt, channel,
  punch-through-stop): light doses of order 10¹²–10¹³ cm⁻² of BF₂, B, As
  or P at tens of keV, placed just under the gate oxide to set
  {term}`Vt`, from a medium-current implanter.
* **Poly and resistor implants** ({ref}`P1I <step-050>`, {ref}`PRI
  <step-053>`, {ref}`UPRI <step-056>`): the gate must be degenerately
  doped (high 10¹⁵ cm⁻²) to avoid {term}`poly depletion`, whereas precision
  resistors need lower, carefully split doses to hit a target sheet
  resistance.
* **Extensions ("tips") and halos** ({ref}`ASTI <step-065>`, {ref}`BHI
  <step-066>`): arsenic at a few keV and about 10¹⁴–10¹⁵ cm⁻²
  self-aligned to the gate edge forms the shallow n-type
  {term}`extension`; boron (or indium) at a large tilt forms the halo
  around it. ITRS 2001 gives extension junction depths for the 130 nm
  node in its Table 51 and treats the p-type boron extension as the most
  challenging junction.[^itrs-01]
* **Source/drain** ({ref}`NSDI <step-086>`, {ref}`PSDI <step-082>`):
  arsenic and boron/BF₂ at several 10¹⁵ cm⁻² and tens of keV, after the
  {term}`spacer`, from a high-current implanter; these amorphise the surface and
  set the contact resistance.

### Typical implanter classes

Beam-line implanters are classified by current and energy:
"medium current" tools deliver beam currents between about 10 µA and
2 mA with serial (one-wafer) end stations and are used for the
low-dose, tilt-sensitive channel and halo implants; "high current"
tools deliver up to about 30 mA with batch spinning-disc end stations
for source/drain and poly implants; and "high energy" tools use a
radio-frequency linear accelerator or tandem stage to reach 200 keV to
several MeV for wells.[^wiki-implant][^current-2017]

## Typical equipment

* **{ref}`High-current <machine-high-current-implanter>`**: Axcelis
  (formerly Eaton and Nova) NV-10 series and NV-GSD/200 series batch
  implanters[^axcelis-history] (the GSD line continues as the GSD
  Ovation, "for general high current applications");[^axcelis-gsd-page]
  Varian VIISta 80 and
  VIISta HC single-wafer high-current implanters;[^semimarket-viista]
  Applied Materials xR series.
* **{ref}`Medium-current <machine-medium-current-implanter>`**: Varian
  E220 and E500 series; Axcelis (Eaton) 8250 and 8200P;[^axcelis-history]
  Nissin.
* **{ref}`High-energy <machine-high-energy-implanter>`**: Axcelis NV-GSD/HE and GSD/VHE ("10 stage LINAC with
  energies up to 3 MeV" and "14 stage LINAC with energies up to 4.9
  MeV");[^axcelis-gsd-page] Varian VIISta 3000 and Genus/Varian tandem
  machines.
* **{ref}`Dose metrology <machine-sheet-resistance-metrology>`**: four-point probes (KLA-Tencor RS-series OmniMap),
  Therma-Wave TP-series modulated-reflectance monitors, and SIMS at an
  analytical laboratory.

The vendor landscape is summarised in the Wikipedia articles on Axcelis
and Varian;[^wiki-axcelis][^wiki-varian] a historical survey of
commercial implanters is given by Current.[^current-2017]

## Typical consumables

* **Source gases**, supplied in sub-atmospheric (SDS) or dilute
  cylinders for safety: boron trifluoride (BF₃) for B⁺ and BF₂⁺,
  phosphine (PH₃) for P⁺, arsine (AsH₃) for As⁺, germane (GeH₄) for
  {term}`pre-amorphisation <pre-amorphisation implant>`, and hydrogen or xenon as
  co-gases.[^wiki-bf3][^wiki-ph3][^wiki-ash3]
* **Solid sources**: elemental arsenic, phosphorus, antimony or indium
  in vaporiser ovens, for species without a convenient gas.
* **Ion-source parts**: tungsten filaments or indirectly heated
  cathodes, arc chambers, extraction electrodes and insulators, all
  eroded by the plasma and replaced every few hundred hours.
* **Beam-line and end-station parts**: graphite or silicon apertures and
  beam stops, Faraday-cup liners, disc pads, clamp rings, and
  wafer-cooling backside gas.
* **Photoresist** thick enough to stop the ions (a 1 µm resist stops MeV
  phosphorus only marginally,[^lee-1996] so deep-well masks may need
  thicker resist) and the strip chemistry that removes it afterwards
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

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.** 18 families concern this page (12 unknown, 6 expired); see {ref}`patents-by-module` for the full, grouped list (families still in force or of unknown status are collapsed there too).
<!-- index-links:end -->

## References

### Cross-check

* Lindhard, Scharff and Schiøtt, *Mat. Fys. Medd.* 1963 — the LSS
  range theory.[^lindhard-1963]
* Gibbons, *Proc. IEEE* 1968 — range distributions in
  semiconductors.[^gibbons-1968]
* Gibbons, *Proc. IEEE* 1972 — damage production and
  annealing.[^gibbons-1972]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — the SRIM
  code.[^ziegler-2010]
* Ziegler, *SRIM* software and documentation.[^srim]
* ITRS 2001, *Front End Processes* — Table 51, doping technology
  requirements, retrograde-well and extension notes.[^itrs-01]
* Axcelis, *GSD Ovation* product page — high-current and high-energy
  batch implanter classes and LINAC energies.[^axcelis-gsd-page]
* Axcelis, *Our History* — dates of the Nova, Eaton and Axcelis
  high-current and medium-current implanters.[^axcelis-history]
* Legacy Semi, Varian VIISta HC listing.[^semimarket-viista]
* Shockley, US 2,787,564 — the original patent on forming devices by
  ion bombardment.[^pat-shockley]

### High-level understanding

* Wikipedia, *Ion implantation* — energies, ranges, {term}`channelling`,
  amorphisation and implanter classes.[^wiki-implant]
* Wikipedia, *Stopping and Range of Ions in Matter*.[^wiki-srim]
* Wikipedia, *Channelling (physics)*.[^wiki-channel]
* Wikipedia, *Dopant*.[^wiki-dopant]
* Wikipedia, *Threshold voltage*.[^wiki-vt]
* Wikipedia, *Boron trifluoride*.[^wiki-bf3]
* Wikipedia, *Phosphine*.[^wiki-ph3]
* Wikipedia, *Arsine*.[^wiki-ash3]
* Wikipedia, *Axcelis Technologies*.[^wiki-axcelis]
* Wikipedia, *Varian Semiconductor*.[^wiki-varian]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 8 ("Ion
  Implantation").[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ch. 9 ("Ion Implantation for VLSI").[^txt-02]
* Sze and Lee, *Semiconductor Devices: Physics and Technology* —
  ch. 13.[^sze-2012]
* Campbell, *Fabrication Engineering at the Micro- and Nanoscale* —
  ch. 5.[^campbell-2013]
* Quirk and Serda, *Semiconductor Manufacturing Technology* —
  ch. 17.[^txt-07]

### Deep dive

* Eaglesham, Stolk, Gossmann and Poate, *APL* 1994 — the "+1"
  interstitials as the source of transient enhanced
  diffusion.[^eaglesham-1994]
* Stolk et al., *JAP* 1997 — the physical mechanisms of transient
  enhanced diffusion.[^stolk-1997]
* Jones and Ishida, *Mater. Sci. Eng. R* 1998 — review of shallow
  junction doping: low-energy implantation, TED, extension and halo
  formation.[^rev-05]
* Current, *Mater. Sci. Semicond. Process.* 2017 — implantation for
  advanced silicon devices, past to future.[^current-2017]
* Current, *JVST A* 1996 — production implanters from a vacuum
  perspective: sources, beam lines, end stations.[^current-1996]
* Smith, Rosencwaig and Willenborg, *APL* 1985 — the thermal-wave
  implant monitor.[^smith-1985]
* Dennard et al., *IEEE JSSC* 1974 — the ion-implanted MOSFET scaling
  paper.[^dennard-1974]
* MacPherson, *APL* 1971 — the original threshold-adjust-by-implant
  paper.[^macpherson-1971]
* Tsukamoto et al., *NIM B* 1991 — review of high-energy implantation
  for {term}`retrograde wells <retrograde well>` and buried layers.[^tsukamoto-1991]
* Morris and Rubin, IIT 2000 — batch high-energy against serial
  medium-current implanters for multiple modulated well implants, in
  device performance and cost.[^morris-2000]
* Rubin, Morris and Jasper, IIT 2002 — process-control issues for
  well implants.[^rubin-2002]
* Hook et al. (IBM), *IEEE TED* 2003 — lateral straggle and the mask
  proximity effect.[^hook-2003]
* Horsky, IIT 1998 — resist outgassing in high-energy and high-current
  implantation.[^horsky-1998]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation and its production impact.[^lee-1996]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — retrograde N-well
  and P-well energies and doses.[^pat-well-ibm]
* Oh (Hynix), US 6,806,133 — a triple-well recipe with MeV phosphorus
  energies and doses.[^pat-dnw-hynix]
* Borland (Genus), US 5,821,589 — the BILLI buried-layer approach to
  latch-up suppression.[^pat-billi-genus]
* Yang (UMC), US 5,393,679 — doubly charged phosphorus at 380–400 keV
  for a retrograde-process punch-through implant.[^pat-umc-dc]
* Ryssel and Ruge, *Ion Implantation* — the classic monograph on
  range theory, damage, annealing and equipment.[^ryssel-1986]
* Hössinger, PhD thesis (TU Wien, 2000) — Monte Carlo simulation of
  implantation for ULSI technology.[^hoessinger-2000]
* MIT OpenCourseWare 6.774 — lecture notes on implantation, damage
  and TED.[^ocw-6774]

<!-- footnotes -->

[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^lindhard-1963]: J. Lindhard, M. Scharff and H. E. Schiøtt, "Range
    Concepts and Heavy Ion Ranges", *Matematisk-fysiske Meddelelser, Det
    Kongelige Danske Videnskabernes Selskab* **33**(14), 1–42 (1963).
    <https://gymarkiv.sdu.dk/MFM/kdvs/mfm%2030-39/mfm-33-14.pdf>
[^gibbons-1968]: J. F. Gibbons, "Ion implantation in semiconductors —
    Part I: Range distribution theory and experiments", *Proceedings of
    the IEEE* **56**(3), 295–319 (1968).
    <https://doi.org/10.1109/PROC.1968.6273>
[^gibbons-1972]: J. F. Gibbons, "Ion implantation in semiconductors —
    Part II: Damage production and annealing", *Proceedings of the IEEE*
    **60**(9), 1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
[^srim]: J. F. Ziegler, *SRIM — The Stopping and Range of Ions in
    Matter* (software and documentation). <http://www.srim.org/>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-channel]: Wikipedia, *Channelling (physics)*.
    <https://en.wikipedia.org/wiki/Channelling_(physics)>
[^eaglesham-1994]: D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and J.
    M. Poate, "Implantation and transient B diffusion in Si: The source
    of the interstitials", *Applied Physics Letters* **65**(18),
    2305–2307 (1994). <https://doi.org/10.1063/1.112725>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^current-2017]: M. I. Current, "Ion implantation of advanced silicon
    devices: Past, present and future", *Materials Science in
    Semiconductor Processing* **62**, 13–22 (2017).
    <https://doi.org/10.1016/j.mssp.2016.10.045>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^axcelis-gsd-page]: Axcelis Technologies, *GSD Ovation — High Current &
    High Energy Batch Ion Implanters*, product page, accessed
    2026-08-30. <https://www.axcelis.com/products/gsd-ovation/>
[^axcelis-history]: Axcelis Technologies, *Our History* ("45 Years of
    Innovation"), company web page, accessed 2026-09-13.
    <https://www.axcelis.com/about/our-history/>
[^semimarket-viista]: Legacy Semi, *Varian VIISta HC High Current
    Implanter* (listing).
    <https://www.semimarket.com/item/varian-viista-hc-high-current-implanter/94062>
[^wiki-axcelis]: Wikipedia, *Axcelis Technologies*.
    <https://en.wikipedia.org/wiki/Axcelis_Technologies>
[^wiki-varian]: Wikipedia, *Varian Semiconductor*.
    <https://en.wikipedia.org/wiki/Varian_Semiconductor>
[^wiki-bf3]: Wikipedia, *Boron trifluoride*.
    <https://en.wikipedia.org/wiki/Boron_trifluoride>
[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^pat-shockley]: W. Shockley, *Forming semiconductive devices by ionic
    bombardment*, US 2,787,564 A, granted 1957.
    <https://patents.google.com/patent/US2787564A/en>
[^wiki-srim]: Wikipedia, *Stopping and Range of Ions in Matter*.
    <https://en.wikipedia.org/wiki/Stopping_and_Range_of_Ions_in_Matter>
[^wiki-dopant]: Wikipedia, *Dopant*. <https://en.wikipedia.org/wiki/Dopant>
[^wiki-vt]: Wikipedia, *Threshold voltage*.
    <https://en.wikipedia.org/wiki/Threshold_voltage>
[^sze-2012]: S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics
    and Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7.
    <https://www.wiley.com/en-us/Semiconductor+Devices%3A+Physics+and+Technology%2C+3rd+Edition-p-9780470537947>
[^campbell-2013]: S. A. Campbell, *Fabrication Engineering at the Micro-
    and Nanoscale*, 4th ed., Oxford University Press, 2013,
    ISBN 978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^rev-05]: E. C. Jones and E. Ishida, "Shallow junction doping
    technologies for ULSI", *Materials Science and Engineering: R*
    **24**(1–2), 1–80 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00013-8>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^dennard-1974]: R. H. Dennard, F. H. Gaensslen, H.-N. Yu, V. L.
    Rideout, E. Bassous and A. R. LeBlanc, "Design of ion-implanted
    MOSFET's with very small physical dimensions", *IEEE Journal of
    Solid-State Circuits* **9**(5), 256–268 (1974).
    <https://doi.org/10.1109/JSSC.1974.1050511>
[^macpherson-1971]: M. R. MacPherson, "The adjustment of MOS transistor
    threshold voltage by ion implantation", *Applied Physics Letters*
    **18**(11), 502–504 (1971). <https://doi.org/10.1063/1.1653513>
[^tsukamoto-1991]: K. Tsukamoto, S. Komori, T. Kuroi and Y. Akasaka,
    "High-energy ion implantation for ULSI", *Nuclear Instruments and
    Methods in Physics Research B* **59–60**, 584–591 (1991).
    <https://doi.org/10.1016/0168-583X(91)95283-J>
[^morris-2000]: W. Morris and L. Rubin, "Technical and economic
    considerations for retrograde well and channel implants", *Proc.
    2000 International Conference on Ion Implantation Technology*, pp.
    73–76. <https://doi.org/10.1109/IIT.2000.924093>
[^rubin-2002]: L. M. Rubin, W. Morris and C. Jasper, "Process control
    issues for retrograde well implants for narrow n+/p+ isolation in
    CMOS", *Proc. 2002 International Conference on Ion Implantation
    Technology*, pp. 17–20. <https://doi.org/10.1109/IIT.2002.1257927>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23.
    <https://patents.google.com/patent/US6667205B2/en>
[^pat-dnw-hynix]: J.-G. Oh (Hynix Semiconductor), *Method for fabricating
    semiconductor device with triple well structure*, US 6,806,133 B2,
    granted 2004-10-19. <https://patents.google.com/patent/US6806133B2/en>
[^pat-billi-genus]: J. O. Borland (Genus Inc.), *Method for CMOS
    latch-up improvement by MeV BILLI (buried implanted layer for
    lateral isolation) plus buried layer implantation*, US 5,821,589 A,
    granted 1998-10-13. <https://patents.google.com/patent/US5821589A/en>
[^pat-umc-dc]: S.-H. Yang (United Microelectronics), *Use of double
    charge implant to improve retrograde process PMOS punch through
    voltage*, US 5,393,679 A, granted 1995-02-28.
    <https://patents.google.com/patent/US5393679A/en>
[^ryssel-1986]: H. Ryssel and I. Ruge, *Ion Implantation*, Wiley, 1986,
    ISBN 978-0-471-10311-0. <https://openlibrary.org/isbn/9780471103110>
[^hoessinger-2000]: A. Hössinger, *Simulation of Ion Implantation for
    ULSI Technology*, PhD thesis, TU Wien, 2000.
    <https://www.iue.tuwien.ac.at/phd/hoessinger/>
[^ocw-6774]: MIT OpenCourseWare, *6.774 Physics of Microfabrication:
    Front End Processing*, Fall 2004 (lecture notes on oxidation,
    diffusion, implantation and annealing).
    <https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/>
