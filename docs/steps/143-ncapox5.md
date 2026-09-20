(step-143)=
# Step 143 — NCAPOX5: CAPOX deposition

| | |
|---|---|
| **Step number** | 143 of 171[^steps-sheet] |
| **Step code** | `NCAPOX5` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | {term}`BEOL` — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`CMPM3 <step-142>` |
| **Next step** | {ref}`VIM3 <step-144>` |

## What this step is

`NCAPOX5` deposits a *{term}`cap oxide`* on the polished inter-level
dielectric over metal 3. After {ref}`CMPM3 <step-142>` the
{ref}`NILD5 <step-141>` oxide is flat, but its thickness above the
metal-3 lines and above the {term}`MiM capacitor` plates is whatever the
polish left, and its surface carries the scratches, slurry residue and
hydrated layer of a polish. A thin plasma oxide deposited over it
seals that surface and, we infer (as at {ref}`NCAPOX3 <step-117>`),
brings the dielectric above metal 3 to its final thickness before the
via-3 mask ({ref}`VIM3 <step-144>`) is printed. The
finished number is public: the PDK's stack diagram places the bottom
of `met4` 1.235 µm above the bottom of `met3`, which with the 0.845 µm
metal leaves a via-3 height of 0.39 µm.[^pdk-04] The cap's own
thickness is not. The same cap is described at
{ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>` and
{ref}`NCAPOX4 <step-128>`, and recurs as {ref}`NCAPOX6 <step-158>`.

One public difference from the two levels below is worth noting. At
NILD3 and NILD4 the stack diagram draws a thin "_C" film of
permittivity 3.5 and thickness 0.030 µm beside the main dielectric,
which could be a cap or a liner; at NILD5 it draws only "NILD5
K=4.1".[^pdk-04] Whatever the "_C" films represent, the diagram does
not show one here, and so offers no hint of this cap's thickness
(see *Open questions*). What the cap prepares for is a 0.20 µm via
(via3.1[^pdk-periph]) etched 0.39 µm deep to metal 3 — an
{term}`aspect ratio` of about 1.95:1, a little below via 2's 2.1:1 —
and, over each capacitor, a shallower via to the TiW top plate (the
PDK's `cap_mim` cross-section draws vias from metal 4 landing on "CAPM"
and on "M3 (plate 1)"; it labels the via that lands on "CAPM" — the
only via it labels — "Via3"[^pdk-07]).

## Step category

`NCAPOX5` is a {ref}`Thin-film deposition <category-deposition>` step
of the *{term}`PECVD` oxide* class — the category page's PECVD
section — and, like its predecessors, the simplest deposition in its
module: a blanket, thin, low-temperature oxide on a flat surface with
no gap to fill. What is specific to this instance is that the
dielectric it completes contains a device: the capacitor top plates
sit inside the via-3 dielectric, so the cap's thickness adds directly
to the oxide over the plates as well as over the lines, and the wafer
now carries three aluminium levels and a thin capacitor dielectric
whose temperature and plasma exposure it must respect (roughly
400–450 °C for Al–Cu, industry-typical[^txt-05]).

## Why this step exists

A polish alone does not give a via level what it needs;
{ref}`NCAPOX3 <step-117>` sets out the reasons, which apply here with
the via-3 numbers:

* **Thickness control.** The {ref}`CMPM3 <step-142>` polish is stopped
  by removal amount and varies with pattern density — the variation
  Boning et al. and Chang et al. characterised.[^boning-1994][^chang-1995]
  Polishing slightly below target and adding a cap of well-controlled
  thickness tightens the final 0.39 µm[^pdk-04] (industry
  practice[^txt-05]), and with it both via-3 depths the
  {ref}`VIM3E <step-145>` etch must reach: to the metal-3 cap and to
  the capacitor plate.
* **Restoring cover over the plates.** Where the polish has thinned
  the oxide over dense capacitor arrays, a deposited cap of known
  thickness restores a minimum distance between the plate and metal 4
  (inference from the construction; the estimate of the remaining
  oxide is at {ref}`CMPM3 <step-142>`).
* **Sealing the polished surface.** Oxide CMP leaves micro-scratches,
  embedded particles — Devriendt et al. relate them to the post-CMP
  clean[^devriendt-1998] — and a hydroxyl-rich surface layer;[^moon-2016]
  a fresh plasma oxide buries them so that they do not seed via-etch
  defects or release water into the vias, the outgassing that
  poisons tungsten nucleation.[^kobayakawa-1991]
* **A known surface for lithography.** The {ref}`VIM3 <step-144>`
  resist and BARC are tuned to a reproducible oxide thickness over
  reflective metal and TiW plates; the swing-curve reflectivity
  depends on it.[^brunner-1991]

Without `NCAPOX5` the via-3 lithography and etch would work on a
surface whose thickness varied with the polish, and the oxide over
some capacitor plates would be thinner than intended.

## How it is typically performed

An industry-generic cap-oxide deposition for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public); the sequence is that of
{ref}`NCAPOX3 <step-117>`.

1. **Chamber.** A single-wafer or twin-chamber PECVD reactor at
   350–400 °C (industry-typical[^txt-05][^raupp-1992]); SkyWater lists
   "PECVD TEOS, C2 and Producer – low temp options" and "PECVD silane
   oxide/nitride/oxynitride, C1 – low temp, range of R.I.
   options".[^skw-01] Applied Materials' Producer[^amat-10k] and
   Novellus's Concept/Sequel family[^novellus-history] are the 200 mm-era
   tools.
2. **Precursor.** {term}`TEOS`/O₂ plasma oxide — Raupp, Cale and Hey
   analyse its kinetics[^raupp-1992] — or SiH₄/N₂O plasma oxide, whose
   properties depend on RF power as Chapple-Sokol, Tierney and Batey
   measured.[^chapple-sokol-1989] The Cypress Fab 4 reports list a
   "1000A TEOS" film under a PECVD nitride in the passivation
   stack,[^cyp-qtp-123907][^cyp-qtp-014807] which shows a TEOS oxide
   of cap-like thickness in the same fab; that it is a plasma rather
   than a thermal TEOS is our inference from the aluminium underneath,
   and that this cap is of the same kind is a further inference.
3. **Thickness.** Not public; a cap of the order of 0.05–0.15 µm is
   typical of the practice (industry-typical value[^txt-05]), sized so
   that polished NILD5 plus cap reaches the 0.39 µm via-3 height[^pdk-04].
4. **Film properties.** A dense, low-hydrogen film; hydrogen evolution
   from plasma oxide on later heating changes its stress,[^mani-2007]
   and a wet cap defeats its purpose. LPCVD TEOS[^adams-1979][^becker-1987]
   would give a denser film but at 650–750 °C, far above the aluminium
   limit (inference from the temperature).
5. **Plasma exposure.** The deposition plasma reaches a wafer whose
   capacitor plates are still floating under the dielectric; a gentle,
   low-bias PECVD step, rather than an HDP one, limits the charging
   Cheung described for plasma-enhanced dielectric
   deposition[^cheung-2000] (inference that it matters here; Wang,
   Ackaert et al. document the MiM case[^wang-2004-mim]).
6. **Clean and metrology.** The wafer comes from the post-CMP scrub
   (Philipossian and Sun on the brushes[^philipossian-2009]); after
   deposition, thickness and index by ellipsometry on monitors and
   product pads, total dielectric over metal-3 pads, stress by wafer
   bow, particles; NF₃ chamber clean.

## Machines typically used

* **{ref}`PECVD oxide system <machine-pecvd>`**, 200 mm: Applied Materials Producer or
  Centura DxZ,[^amat-10k] Novellus Concept One/Two,
  Sequel[^novellus-history] ({ref}`category-deposition`).
* **{ref}`Ellipsometer <machine-film-thickness-metrology>` / reflectometer**, **stress gauge**, **{ref}`particle inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **PECVD TEOS "C2 and Producer" with "low temp options".**[^skw-01]
  Strength: **strong** for the capability; the assignment of the cap
  to the TEOS process rather than the silane "C1" oxide is an
  **inference** from practice and from the TEOS oxide in the Cypress
  passivation description.[^cyp-qtp-123907] "C2" as a Novellus Concept
  Two and "Producer" as an Applied Materials Producer are readings of
  the names, not stated.
* **PECVD silane oxide "C1"**[^skw-01] as the alternative (medium).

## Resources required

* **{ref}`TEOS <material-precursors>`** (liquid, vaporised) and **{ref}`oxygen <material-process-gases>`**, or **silane** and
  **N₂O** for the silane route;[^wiki-teos][^wiki-pecvd] **helium**,
  **nitrogen** or **argon** as carrier or diluent (typical; the PECVD
  article describes TEOS deposition "in an oxygen or oxygen-argon
  plasma"[^wiki-pecvd]).
* **{ref}`NF₃ <material-etch-gases>`** for the chamber clean; **nitrogen** purge.
* **{ref}`Showerhead, heater and liner consumables <material-hardware-consumables>`**; **{ref}`monitor wafers <material-substrates>`**.

## Related steps and cross-references

* Previous: {ref}`CMPM3 <step-142>` (the polish it seals). Next:
  {ref}`VIM3 <step-144>` (the via-3 mask printed on it), then
  {ref}`VIM3E <step-145>`.
* The dielectric it completes: {ref}`NILD5 <step-141>`; the metal and
  capacitors beneath: {ref}`MM3E <step-140>`, {ref}`CAPME <step-138>`.
* The other cap oxides: {ref}`NCAPOX <step-091>`,
  {ref}`NCAPOX3 <step-117>` (where the reasoning is set out in full),
  {ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX6 <step-158>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Process stack diagram* — "NILD5 K=4.1" with no "_C"
  film; met3 and met4 bottom levels; `met3` 0.845 µm.[^pdk-04]
* SkyWater PDK, *Periphery rules* — via3.1 0.200 µm.[^pdk-periph]
* SkyWater PDK, *Device Details* — the `cap_mim` cross-section with
  vias landing on "CAPM" and on "M3 (plate 1)", the former labelled
  "Via3".[^pdk-07]
* SkyWater, *Facilities & Capabilities* — "PECVD TEOS, C2 and Producer
  – low temp options"; "PECVD silane oxide/nitride/oxynitride, C1".[^skw-01]
* Cypress, QTP 123907/132302/132301 and QTP 014807 — "1000A TEOS" in
  the Fab 4 passivation stack.[^cyp-qtp-123907][^cyp-qtp-014807]
* Applied Materials, Form 10-K (2003); Encyclopedia.com, *Novellus
  Systems, Inc.*[^amat-10k][^novellus-history]

### High-level understanding

* Wikipedia, *Plasma-enhanced chemical vapor deposition*, *Tetraethyl
  orthosilicate*.[^wiki-pecvd][^wiki-teos]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — PECVD oxides
  in the back end.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — ILD stacks,
  CMP and cap layers.[^txt-05]

### Deep dive

* Boning et al., SPIE 1994, and Chang et al., IEDM 1995 — the ILD
  thickness variation a cap is added to control.[^boning-1994][^chang-1995]
* Raupp, Cale and Hey, *JVST B* 1992 — PECVD TEOS oxide kinetics.[^raupp-1992]
* Chapple-Sokol, Tierney and Batey (IBM), MRS 1989 — RF-power
  dependence of PECVD oxide properties.[^chapple-sokol-1989]
* Mani and Saif, *Thin Solid Films* 2007 — stress from hydrogen
  evolution in plasma oxide.[^mani-2007]
* Adams and Capio, 1979, and Becker et al., 1987 — the LPCVD TEOS
  oxides the low-temperature cap cannot use.[^adams-1979][^becker-1987]
* Devriendt et al. (IMEC), 1998, and Philipossian and Sun, 2009 —
  oxide-CMP defects and the scrub before the cap.[^devriendt-1998][^philipossian-2009]
* Moon, in *Advances in CMP* — the chemistry of the polished oxide
  surface.[^moon-2016]
* Kobayakawa et al., VMIC 1991 — dielectric outgassing and via
  poisoning.[^kobayakawa-1991]
* Brunner, SPIE 1991 — the swing-curve dependence on the oxide under
  the resist.[^brunner-1991]
* Cheung, P2ID 2000, and Wang, Ackaert et al., *IEEE TED* 2004 —
  charging during plasma dielectric deposition and its effect on
  floating MiM capacitors.[^cheung-2000][^wang-2004-mim]

## Open questions

* The cap's precursor, thickness and deposition conditions are not
  public.
* How the 0.39 µm via-3 height[^pdk-04] is divided between the polished
  {ref}`NILD5 <step-141>` and this cap is not public.
* Why the stack diagram draws "_C" films at NILD3 and NILD4 but not
  at NILD5[^pdk-04] — and therefore whether the cap oxides differ
  between levels — is not public.
* Whether "C2" denotes a Novellus Concept Two is an inference from the
  vendor's product names.[^novellus-history]

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology
    Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005
    (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^boning-1994]: D. S. Boning, T. Maung, J. E. Chung, K.-J. Chang,
    S.-Y. Oh and D. Bartelink, "Statistical metrology for interlevel
    dielectric thickness variation", *Proc. SPIE* **2334**, Advanced
    Microelectronic Manufacturing, 316–327 (1994).
    <https://doi.org/10.1117/12.186764>
[^chang-1995]: E. Chang, B. Stine, T. Maung, R. Divecha, D. Boning,
    J. Chung, K. Chang, G. Ray, D. Bradbury, O. S. Nakagawa, S. Oh and
    D. Bartelink, "Using a statistical metrology framework to identify
    systematic and random sources of die- and wafer-level ILD
    thickness variation in CMP processes", *IEDM 1995 Technical
    Digest*, pp. 499–502. <https://doi.org/10.1109/IEDM.1995.499247>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
[^chapple-sokol-1989]: J. D. Chapple-Sokol, E. Tierney and J. Batey,
    "RF Power Dependence of the Material Properties of PECVD Silicon
    Dioxide", *MRS Proceedings* **165** (1989).
    <https://doi.org/10.1557/PROC-165-113>
[^mani-2007]: S. Mani and T. Saif, "Stress development in
    plasma-deposited silicon dioxide thin-films due to hydrogen
    evolution", *Thin Solid Films* **515**(5), 3120–3125 (2007).
    <https://doi.org/10.1016/j.tsf.2006.08.025>
[^adams-1979]: A. C. Adams and C. D. Capio, "The Deposition of Silicon
    Dioxide Films at Reduced Pressure", *Journal of The Electrochemical
    Society* **126**(6), 1042–1046 (1979).
    <https://doi.org/10.1149/1.2129171>
[^becker-1987]: F. S. Becker, D. Pawlik, H. Anzinger and A. Spitzer,
    "Low-pressure deposition of high-quality SiO₂ films by pyrolysis of
    tetraethylorthosilicate", *Journal of Vacuum Science & Technology B*
    **5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
[^devriendt-1998]: K. Devriendt, E. Vrancken, N. Heylen, J. Grillaert,
    M. Meuris, M. M. Heyns and Z. C. Lin, "Relation between Oxide-CMP
    Induced Defects and Post-CMP Cleaning Strategies", *Solid State
    Phenomena* **65–66**, 173–176 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.173>
[^philipossian-2009]: A. Philipossian and T. Sun, "Frictional Analysis
    of Various Poly(vinyl alcohol) Brush Roller Designs for
    Post-Interlevel Dielectric CMP Scrubbing Applications",
    *Electrochemical and Solid-State Letters* **12**(3), H84 (2009).
    <https://doi.org/10.1149/1.3058994>
[^moon-2016]: Y. Moon, "Chemical and physical mechanisms of dielectric
    chemical mechanical polishing (CMP)", in *Advances in Chemical
    Mechanical Planarization (CMP)*, Woodhead Publishing, 2016,
    pp. 3–26, ISBN 978-0-08-100165-3.
    <https://doi.org/10.1016/B978-0-08-100165-3.00001-2>
[^kobayakawa-1991]: M. Kobayakawa, A. Arimatsu, F. Yokoyama, N. Hirashita
    and T. Ajioka, "A study of outgassing from spin-on-glass films used
    for planarization", *Proc. Eighth International IEEE VLSI Multilevel
    Interconnection Conference (VMIC 1991)*, pp. 454–456.
    <https://doi.org/10.1109/VMIC.1991.153054>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^cheung-2000]: K. P. Cheung, "On the mechanism of plasma enhanced
    dielectric deposition charging damage", *Proc. 2000 5th
    International Symposium on Plasma Process-Induced Damage (P2ID)*,
    pp. 161–163. <https://doi.org/10.1109/PPID.2000.870658>
[^wang-2004-mim]: Z. Wang, J. Ackaert, C. Salm, F. G. Kuper, M. Tack,
    E. De Backer, P. Coppens, L. De Schepper and B. Vlachakis,
    "Plasma-charging damage of floating MIM capacitors", *IEEE
    Transactions on Electron Devices* **51**(6), 1017–1024 (2004).
    <https://doi.org/10.1109/TED.2004.829518>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
