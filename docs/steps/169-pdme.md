(step-169)=
# Step 169 — PDME: Pad mask etch

| | |
|---|---|
| **Step number** | 169 of 171[^steps-sheet] |
| **Step code** | `PDME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | BEOL — passivation, pads, alloy, test |
| **Previous step** | {ref}`PDM <step-168>` |
| **Next step** | {ref}`ALLY <step-170>` |

## What this step is

`PDME` opens the passivation over the pads. Through the resist openings
of {ref}`PDM <step-168>` — the `pad` layer, "Passivation cut (opening
over pads)"[^pdk-06] — a fluorine-based plasma removes the passivation
nitride of {ref}`NTSD <step-167>`, then the thin oxide of
{ref}`NFUSOX <step-164>`, and stops on the metal-5 pad. The resist is
then stripped and the pads are cleaned; this reference treats the strip
and clean as part of this step. It is the last etch in the flow: after
it the wafer is annealed ({ref}`ALLY <step-170>`) and tested
({ref}`HPETEST <step-171>`).

The films to be cleared are public only approximately. The PDK's stack
diagram draws a "glass cut" through "TOPNIT K=7.5" (0.54 µm over the
metal) and "TOPOX K=3.9" (0.09 µm) down to `metal5`,[^pdk-04] while
Cypress reports for other processes at the same fab give 7000–9000 Å of
nitride over 1000 Å of TEOS oxide.[^cyp-qtp-014807][^cyp-qtp-123907][^cyp-qtp-113005]
Under the oxide lies the top of the metal-5 stack. The PDK does not give its films; this reference reads it, with the lower levels, as a
TiW-capped Al–Cu stack ({ref}`WTIAL5 <step-161>`; inference from the
300 Å TiW caps of the S8 stacks in a Cypress report[^cyp-qtp-113005]
and from Cypress's 2014 report, which moved the lower levels to Ti/TiN
caps but qualified the S8P change "excluding top metal layers" and kept
"300A TiW" on the S8DI top metal[^cyp-qtp-123907]). If so, the etch or
a following clean must remove the TiW over the pad: Danzl and McLaurin
report that TiW left on pads causes wire-bond non-sticks and that
plasma etching alone left a residue.[^danzl-1997] How SKY130 does this
is not public. The openings are large: in SkyWater's GPIO pad cell the
opening is 60 µm × 70 µm inside a 65.4 µm × 75.4 µm metal-5
pad,[^pdk-io-gpiov2] and the smallest allowed opening is 2 µm
(`PDMCD`[^pdk-03]).

## Step category

`PDME` is an {ref}`Etch <category-etch>` step of the *dielectric,
fluorine-chemistry* class — the category page's silicon nitride and
silicon dioxide entries in sequence — ending on a metal. What is
specific to this instance is the floor. Every earlier dielectric etch
through to metal (the via etches, such as {ref}`VIM3E <step-145>`)
lands on a refractory cap and is followed by a liner, plug or next
metal that covers the floor; this one lands on the surface that a wire bond or
probe needle will touch, and nothing covers it afterwards. Aluminium is
not etched by fluorine — it forms involatile AlF₃, as Hess
explained[^hess-1982] — which makes the stop easy but leaves fluorine on
the pad; residues that a via etch can tolerate under a liner are
defects here. The etch also sets the edge of the passivation, the seal
around every pad.

## Why this step exists

* **Bondable, probeable pads.** The pads must be clean metal: a Micron
  patent describes how, after a fluorine-based pad etch, "Fluorine (F)
  from the etch process is deposited onto the aluminum of the bond
  pads", forming an oxide layer that produces "gummy pads" and probe
  failures, and removes it in situ with an argon (or oxygen) plasma
  after the nitride etch;[^pat-pad-fluorine-micron] a TSMC patent
  attributes non-optimal wire bonds and failed bondability tests to the
  resulting aluminium–fluorine–oxide deposits and removes them by
  reactive ion etching.[^pat-pad-fluorine-tsmc] Teo et al. evaluated
  TOF-SIMS for measuring fluorine contamination on aluminium bond
  pads.[^teo-2015]
* **Removing a refractory cap (if present).** A TiW or TiN
  {term}`anti-reflective cap` on aluminium is not a good bond surface; Danzl
  and McLaurin describe using concentrated hydrogen peroxide to remove a
  TiW ARC from aluminium bond pads,[^danzl-1997] and TiW is also etched
  in fluorine-containing plasmas, as Liu and Kuo showed for CF₄-based
  mixtures and Turban et al. for tungsten in SF₆.[^liu-2007-tiw][^turban-1989]
* **A clean passivation edge.** The nitride and oxide must be cut
  completely, with no stringers over the pad and no undercut of the
  oxide under the nitride that would open a path along the interface
  (inference from the construction; Comizzoli et al. review the
  corrosion that exposed aluminium suffers[^comizzoli-1986]).
* **Undamaged pads for test.** Probing at {ref}`HPETEST <step-171>`
  and bonding at assembly load the pad and the oxide beneath it; Hunter
  et al. describe how probe cracks in the oxide under aluminium pads
  can be hidden and later grow during bonding.[^hunter-2012] A pad that
  has been thinned or roughened by the etch is less tolerant (inference).

## How it is typically performed

An industry-generic pad-opening etch for a 200 mm, 130 nm-era fab with
an aluminium top metal (SKY130's recipe is not public):

1. **Chamber.** A single-wafer plasma etcher with fluorine chemistry —
   a nitride-capable {term}`TCP` or ICP etcher, or a capacitively
   coupled dielectric etcher ({ref}`category-etch`); helium backside
   cooling to protect the resist.
2. **Nitride etch.** CF₄/O₂ (with N₂ or CHF₃) or SF₆-based chemistry;
   Kastenmeier et al. give nitride and oxide rates in CF₄/O₂/N₂ and the
   conditions for high nitride selectivity.[^kastenmeier-1996][^kastenmeier-1999]
   The Micron and TSMC patents name "fluorine containing gases, such as
   CHF3" and "CHF3, CF4, C2F6, C2F2, C4F8" for the passivation nitride
   etch.[^pat-pad-fluorine-micron][^pat-pad-fluorine-tsmc]
3. **Oxide etch.** A fluorocarbon step through the thin oxide, whose
   mechanism Oehrlein et al. and Schaepkens et al.
   describe;[^oehrlein-1994b][^schaepkens-1999] in practice nitride and
   oxide are often cleared in one chemistry with a timed
   {term}`over-etch`.
4. **Metal floor.** The etch stops on aluminium (AlF₃ does not
   volatilise[^hess-1982]); a TiW cap, if present, is removed by the
   fluorine over-etch or by a separate wet or plasma step
   (industry practice;[^liu-2007-tiw][^danzl-1997] SKY130's choice is not
   public). {term}`Endpoint <endpoint>` by optical emission as the
   nitride clears; the pad
   area is a small fraction of the wafer, the low-open-area condition
   Wodecki discusses.[^wodecki-1999]
5. **Fluorine removal.** An in-situ argon, O₂ or mixed plasma after the
   main etch to remove Al–F–O residue from the pads, the methods of the
   Micron and TSMC patents.[^pat-pad-fluorine-micron][^pat-pad-fluorine-tsmc]
6. **Strip and clean.** Downstream O₂/N₂ {term}`ash` and a solvent
   clean compatible with exposed aluminium (SkyWater lists GaSonics,
   Iridia and Mattson strippers and "EKS265, EKC270
   solvents"[^skw-01]); DI rinse and dry.
7. **Metrology.** Visual and automated inspection of every pad for
   residue, discolouration and incomplete opening; opening size;
   on monitors, surface fluorine (for example by TOF-SIMS[^teo-2015])
   and wire-bond pull/shear tests.

## Machines typically used

* **Plasma etcher for nitride and oxide**, 200 mm: Lam TCP 9400-class
  nitride-capable etchers,[^snf-9400][^lam-10k] Lam Exelan dielectric
  etchers,[^lam-exelan] Applied Materials and TEL equivalents
  ({ref}`category-etch`).
* **Downstream asher**; **solvent wet bench**.
* **Automated pad inspection**, **TOF-SIMS / XPS** for surface
  analysis, **wire-bond pull tester** on monitors.

## Machines likely used at SkyWater

* **Lam 9400 TCP.** SkyWater lists "Lam 9400 TCP, poly/nitride, HBr,
  CF4, SF6, O2".[^skw-01] Strength: **medium** — the list ties this
  etcher to nitride and gives it CF₄, SF₆ and O₂; assignment to the pad
  etch is an **inference**, since the list names no steps.
* **Lam 4400** ("HBr, Cl2, C2F6, CF4, SF6, O2") and **AMAT DPSII**
  ("HBR, Cl2, NF3, CF4, CHF3, O2").[^skw-01] Strength: weak.
* **Lam 9600 / Lam 2300 Versys**, listed for "TiW",[^skw-01] if a
  separate cap removal is done by plasma (weak).
* **Strip and clean — GaSonics PEP, Iridia, Mattson Aspen II; batch
  rotational tools with "EKS265, EKC270 solvents".**[^skw-01] Strength:
  strong for existence.

## Resources required

* **CF₄**, **CHF₃**, **SF₆**, **O₂**, **N₂** and **Ar** for the etch and
  the fluorine-removal plasma (industry practice;[^nojiri-2015] SkyWater
  names CF₄, CHF₃, SF₆ and O₂ on its listed etchers[^skw-01]); **He**
  backside cooling.
* **O₂/N₂** for the ash;[^skw-01] **aluminium-compatible solvent** and
  DI water; possibly **hydrogen peroxide** if a TiW cap is removed
  wet.[^danzl-1997]
* **Chamber consumables**; **fluorine abatement**; **monitor wafers**
  with passivated metal-5 pads for rate, residue and bond tests.

## Related steps and cross-references

* Previous: {ref}`PDM <step-168>` (the mask). Next:
  {ref}`ALLY <step-170>` (the anneal), then {ref}`HPETEST <step-171>`
  (the probing of the pads just opened).
* The films it cuts: {ref}`NTSD <step-167>`, {ref}`NFUSOX <step-164>`;
  the pad metal it lands on: {ref}`WTIAL5 <step-161>`,
  {ref}`MM5E <step-163>`.
* The other etch through the passivation: {ref}`NSME <step-166>`.
* Other nitride etches: {ref}`STINITE <step-005>`, {ref}`SPE <step-077>`.
* Category page: {ref}`Etch <category-etch>`.

## References

### Cross-check

* SkyWater PDK, *Layers Reference* — `pad` 76:20 "Passivation cut
  (opening over pads)".[^pdk-06]
* SkyWater PDK, *Process stack diagram* — "glass cut" through TOPNIT and
  TOPOX to `metal5`.[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — `PDMCD` 2 µm.[^pdk-03]
* SkyWater I/O library, `sky130_fd_io__top_gpiov2` GDS — the 60 µm ×
  70 µm pad opening.[^pdk-io-gpiov2]
* Cypress, QTP 014807, QTP 123907/132302/132301, QTP 113005 — passivation
  and metal caps at Fab 4.[^cyp-qtp-014807][^cyp-qtp-123907][^cyp-qtp-113005]
* SkyWater, *Facilities & Capabilities* — etchers and gases, strippers,
  solvents.[^skw-01]
* Lam Research, Form 10-K (2003) and Exelan press release; Stanford
  Nanofabrication Facility, *Lam TCP 9400*.[^lam-10k][^lam-exelan][^snf-9400]

### High-level understanding

* Wikipedia, *Reactive-ion etching*, *Silicon nitride*.[^wiki-rie][^wiki-sin]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — passivation and
  pad processing.[^txt-05]
* Nojiri, *Dry Etching Technology for Semiconductors* — dielectric etch
  chemistry.[^nojiri-2015]

### Deep dive

* Kastenmeier et al., *JVST A* 1996 and 1999 — nitride and oxide etching
  in fluorine plasmas and nitride selectivity.[^kastenmeier-1996][^kastenmeier-1999]
* Oehrlein et al., *JVST A* 1994, and Schaepkens et al., *JVST A* 1999 —
  fluorocarbon etching of oxide and the oxide/nitride selectivity
  mechanism.[^oehrlein-1994b][^schaepkens-1999]
* Hess, *Plasma Chem. Plasma Process.* 1982 — why fluorine does not etch
  aluminium.[^hess-1982]
* Liu and Kuo, *J. Electrochem. Soc.* 2007, and Turban, Coulon and
  Mutsukura, *Thin Solid Films* 1989 — fluorine-plasma etching of TiW
  and tungsten.[^liu-2007-tiw][^turban-1989]
* Danzl and McLaurin, IEMT 1997 — removing a TiW ARC from aluminium bond
  pads.[^danzl-1997]
* Jones, Crane, Gilchrist and Langley (Micron), US 5,380,401 — fluorine
  residues on bond pads after the nitride pad etch.[^pat-pad-fluorine-micron]
* Tsai and Liu (TSMC), US 7,055,532 — reactive ion etching of Al–F–O
  deposits on bond pads.[^pat-pad-fluorine-tsmc]
* Teo et al., IPFA 2015 — TOF-SIMS measurement of fluorine on aluminium
  bond pads.[^teo-2015]
* Hunter et al., IMAPS 2012 — probe and bond damage in aluminium
  pads.[^hunter-2012]
* Wodecki, SPIE 1999 — endpoint at low open area.[^wodecki-1999]
* Comizzoli et al., *Science* 1986 — corrosion of electronic
  metallisation.[^comizzoli-1986]

## Open questions

* Whether the metal-5 stack has a TiW (or other) cap, and whether it is
  removed from the pads by this etch, by a wet step or not at all, is not
  public.
* The etch chemistry, tool, endpoint and any fluorine-removal treatment
  are not public.
* The passivation thickness to be etched is uncertain: 0.63 µm (0.54
  µm TOPNIT plus 0.09 µm TOPOX, our arithmetic) on the PDK
  diagram[^pdk-04] against about 0.7–1.0 µm in the Cypress reports for
  other processes.[^cyp-qtp-014807][^cyp-qtp-123907][^cyp-qtp-113005]
* Whether the same etch opens laser-fuse windows (see
  {ref}`PDM <step-168>`) is not public.
* This page treats the resist strip and clean as part of the etch.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-io-gpiov2]: SkyWater PDK Authors, *skywater-pdk-libs-sky130_fd_io*
    repository, cell `sky130_fd_io__top_gpiov2`, GDS layout
    `sky130_fd_io__top_gpiov2.gds` and LEF abstract
    `sky130_fd_io__top_gpiov2.lef`, retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-libs-sky130_fd_io/tree/main/cells/top_gpiov2>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
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
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^lam-10k]: Lam Research Corporation, Form 10-K for the fiscal year
    ended 2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
    <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
[^lam-exelan]: Lam Research, *Lam Research Corporation Advances
    Dielectric Etch Capabilities With Launch Of Exelan High
    Performance*, press release, 2001-07-09.
    <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400
    Poly Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^kastenmeier-1996]: B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
    and G. S. Oehrlein, "Chemical dry etching of silicon nitride and
    silicon dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **14**(5), 2802–2813 (1996).
    <https://doi.org/10.1116/1.580203>
[^kastenmeier-1999]: B. E. E. Kastenmeier, P. J. Matsuo and
    G. S. Oehrlein, "Highly selective etching of silicon nitride over
    silicon and silicon dioxide", *Journal of Vacuum Science &
    Technology A* **17**(6), 3179–3184 (1999).
    <https://doi.org/10.1116/1.582097>
[^oehrlein-1994b]: G. S. Oehrlein, Y. Zhang, D. Vender and O. Joubert,
    "Fluorocarbon high-density plasmas. II. Silicon dioxide and silicon
    etching using CF₄ and CHF₃", *Journal of Vacuum Science &
    Technology A* **12**(2), 333–344 (1994).
    <https://doi.org/10.1116/1.578877>
[^schaepkens-1999]: M. Schaepkens, T. E. F. M. Standaert, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
    SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
    fluorocarbon plasmas and a comparison with the SiO₂-to-Si
    mechanism", *Journal of Vacuum Science & Technology A* **17**(1),
    26–37 (1999). <https://doi.org/10.1116/1.582108>
[^hess-1982]: D. W. Hess, "Plasma etch chemistry of aluminum and
    aluminum alloy films", *Plasma Chemistry and Plasma Processing*
    **2**(2), 141–155 (1982). <https://doi.org/10.1007/BF00633130>
[^liu-2007-tiw]: G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
    Tungsten Thin Films", *Journal of The Electrochemical Society*
    **154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631>
[^turban-1989]: G. Turban, J. F. Coulon and N. Mutsukura, "A
    mechanistic study of SF₆ reactive ion etching of tungsten", *Thin
    Solid Films* **176**(2), 289–308 (1989).
    <https://doi.org/10.1016/0040-6090(89)90102-8>
[^danzl-1997]: R. B. Danzl and A. McLaurin, "The use of concentrated
    hydrogen peroxide for the removal of a TiW ARC from aluminum bond
    pads", *Proc. Twenty-First IEEE/CPMT International Electronics
    Manufacturing Technology Symposium (IEMT 1997)*, pp. 99–104.
    <https://doi.org/10.1109/IEMT.1997.626884>
[^pat-pad-fluorine-micron]: C. S. Jones, W. J. Crane, R. L. Gilchrist
    and R. C. Langley (Micron Technology), *Method to remove fluorine
    residues from bond pads*, US 5,380,401 A, filed 1993-01-14, granted
    1995-01-10.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5380401>
[^pat-pad-fluorine-tsmc]: H.-C. Tsai and H.-H. Liu (Taiwan Semiconductor
    Manufacturing Co.), *Method to remove fluorine residue from bond
    pads*, US 7,055,532 B2, filed 2003-12-18, granted 2006-06-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7055532>
[^teo-2015]: H. W. Teo, Y. Yang, Y. Wang, L. Zhu, Z. Q. Mo, S. P. Zhao
    and J. Lam, "Feasibility study of TOF-SIMS surface measurement for
    Aluminum bond pad fluorine contamination", *Proc. 2015 IEEE 22nd
    International Symposium on the Physical and Failure Analysis of
    Integrated Circuits (IPFA)*, pp. 61–63.
    <https://doi.org/10.1109/IPFA.2015.7224333>
[^hunter-2012]: S. Hunter, J. L. Clark, D. Hornberger and L. Rubio, "Use
    of Wire Bonding to Study Bond Pad Damage from Wafer Probe",
    *International Symposium on Microelectronics* **2012**(1), 384–395
    (IMAPS, 2012). <https://doi.org/10.4071/isom-2012-TP41>
[^wodecki-1999]: N. Wodecki, "Low open area multilayered dielectric
    film etch endpoint detection using EndPoint Plus", *Proc. SPIE*
    **3882**, Process, Equipment, and Materials Control in Integrated
    Circuit Manufacturing V, 231 (1999).
    <https://doi.org/10.1117/12.361313>
[^comizzoli-1986]: R. B. Comizzoli, R. P. Frankenthal, P. C. Milner and
    J. D. Sinclair, "Corrosion of Electronic Materials and Devices",
    *Science* **234**(4774), 340–345 (1986).
    <https://doi.org/10.1126/science.234.4774.340>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
