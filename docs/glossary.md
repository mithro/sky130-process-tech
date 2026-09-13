(glossary)=
# Glossary

Terms and acronyms used throughout this reference. Each entry is
referenced from the pages that use it with the `{term}` role.

```{glossary}
2-T cell
    The two-transistor non-volatile memory cell of SKY130: a
    {term}`SONOS` memory transistor, whose gate is the
    {term}`control gate`, in series with an ordinary transistor whose
    gate is the {term}`select gate`. The select transistor connects the
    memory transistor to the bit line only when the cell is addressed,
    so that reading and programming one cell do not disturb its
    neighbours, at the cost of more area than a one-transistor cell.

alloy anneal
    A low-temperature (typically 350–450 °C; see {ref}`category-anneal`)
    anneal in hydrogen-bearing {term}`forming gas` performed after
    metallisation. It sinters the
    metal-to-silicon contacts and passivates interface traps at the
    Si/SiO₂ interface with hydrogen. Also called a sinter or
    forming-gas anneal.

aluminium via fill
    Filling a via with the aluminium alloy of the wiring level above it
    instead of with a separate tungsten plug. The aluminium is made to
    enter the hole by sputtering it onto a hot or biased wafer, by a
    cool seed layer followed by a hot deposition, or by closing the hole
    over and then forcing the metal in at high pressure and temperature.
    It avoids the Al/W interface and the plug steps but suits only vias
    of modest {term}`aspect ratio`. This reference reads SKY130's via 4
    as filled this way (see {ref}`step-161`).

anisotropy
    The degree to which an etch proceeds in one direction (normally
    vertically, into the wafer) rather than equally in all directions.
    A perfectly anisotropic etch has zero lateral etch rate; a purely
    chemical wet etch of an amorphous film is isotropic.

anti-reflective cap
    A thin, dull metal film sputtered on top of an aluminium
    interconnect so that the shiny aluminium does not reflect the
    exposure light back into the photoresist during the metal
    lithography. In SKY130's metal-1 stack the cap is titanium–tungsten
    (see {ref}`step-112`); it also suppresses {term}`hillock`s, resists
    corrosion and gives the {term}`via` etch a hard surface to land on.
    Also "ARC cap" or "TiW cap"; compare {term}`BARC`.

ARC
    Anti-reflective coating: a thin absorbing or interference layer
    placed above ({term}`TARC`) or below ({term}`BARC`) the photoresist
    to suppress standing waves and reflective notching during exposure.

ARDE
    Aspect-ratio-dependent etching: the tendency of a plasma etch rate
    to fall as the depth-to-width ratio of a feature rises, because
    ions and neutrals reach the bottom of narrow features less easily.
    Also called RIE lag.

ash
    Removal of organic photoresist by reaction with oxygen radicals from
    a plasma, leaving volatile CO, CO₂ and H₂O. Also "ashing" or
    "plasma strip".

aspect ratio
    The ratio of a feature's depth (or height) to its width, for example
    of a contact hole or a gap between metal lines.

attenuated PSM
    A {term}`PSM` in which the "dark" regions of the mask are a thin,
    partially transmitting film (usually a molybdenum silicide compound)
    instead of opaque chrome. The weak light that leaks through them is
    180° out of phase with the light through the clear regions, so the
    two cancel at the feature edge and the image is sharper. Also
    "attenuated phase-shift mask" or "half-tone PSM"; usually combined
    with {term}`OPC` and {term}`SRAF`s.

backside film removal
    Etching away the oxide, nitride and polysilicon that furnace and
    deposition steps leave on the back of a wafer, in a single-wafer spin
    tool that keeps the chemicals off the front. It restores a clean,
    flat back surface so that the wafer sits correctly on chucks and
    does not shed particles or contamination. See {ref}`step-060`.

BARC
    Bottom anti-reflective coating: an organic (spin-on) or inorganic
    (deposited, e.g. silicon oxynitride) layer under the photoresist that
    absorbs light reflected from the substrate.

barrier metal
    A thin refractory film — titanium nitride or titanium–tungsten —
    placed between a conductor and a material it must not react with:
    between aluminium and silicon, or between tungsten hexafluoride
    and the titanium or silicon beneath it during plug fill. It works by
    offering few fast diffusion paths and by staying chemically stable
    at back-end temperatures. Usually paired with a {term}`liner`.

BEOL
    Back end of line: the interconnect portion of the process flow, from
    the first contact through the final passivation.

Blech length
    The critical length below which an aluminium line on a rigid,
    conducting underlayer such as titanium nitride does not fail by
    {term}`electromigration`: the mechanical stress that builds up as
    atoms pile up at one end of the line pushes back as hard as the
    electron wind pushes forward, and net transport stops. Lines shorter
    than it are sometimes called "immortal". Named for I. A. Blech's
    experiments on aluminium over TiN (see {ref}`step-101`).

blocking oxide
    The top oxide of the {term}`ONO` stack of a {term}`SONOS`
    transistor, between the {term}`charge-trapping layer` and the gate.
    It must be thick and dense enough that stored charge does not leak
    to the gate during retention and that electrons are not injected
    from the gate during erase. Also "top oxide".

block mask
    A photoresist mask whose job is to keep an implant *out* of the
    regions it covers rather than to open windows for it: the implant is
    otherwise a blanket one. The P-well block mask of {ref}`step-026` is
    an example. Also "blocking mask".

BOE
    Buffered oxide etch: hydrofluoric acid buffered with ammonium
    fluoride (NH₄F), giving a stable, controlled etch rate for silicon
    dioxide.

bond pad
    An area of top-level metal, left exposed by an opening in the
    passivation, to which a bond wire is attached and on which probe
    needles land during wafer test. The pad metal and the dielectric
    beneath it must survive the mechanical load of probing and bonding.
    In SKY130 the pads are drawn in metal 5 and opened by the `pad`
    layer (see {ref}`step-161`, {ref}`step-162`).

borderless contact
    A contact that is allowed to overlap the edge of the diffusion, gate
    or local interconnect it lands on, rather than being enclosed by it
    with a margin. It is only safe if an {term}`etch-stop layer` under
    the dielectric keeps the contact etch from digging into the
    isolation or the gate beside the target; in exchange it saves the
    enclosure area a bordered contact costs. SKY130's nitride cap over
    the local interconnect plays this part for the metal contacts
    ({ref}`step-104`, {ref}`step-108`).

boron penetration
    Diffusion of boron from a p⁺ polysilicon gate through a thin gate
    oxide into the channel during the anneals that follow gate doping,
    which shifts the PMOS {term}`Vt` and degrades the oxide. It is
    suppressed by nitrogen in the gate oxide ({term}`oxynitride`) or
    avoided altogether by using an n⁺ gate on the PMOS
    ({term}`single-work-function gate`).

BPSG
    Borophosphosilicate glass: silicon dioxide doped with both boron and
    phosphorus. The boron lowers the temperature at which the glass
    softens and flows ({term}`reflow`) well below that of {term}`PSG`,
    so that a BPSG {term}`pre-metal dielectric` can be smoothed over the
    gates without harming the junctions beneath. This reference
    describes SKY130's pre-metal glass as PSG rather than BPSG (see
    {ref}`step-089`).

buried-channel PMOS
    A p-channel MOSFET with an n⁺ polysilicon gate whose channel has been
    {term}`counter-doping`-implanted so that the conducting layer lies a
    little below the silicon surface. It is the consequence of a
    {term}`single-work-function gate` process, in which the n⁺ gate work
    function would otherwise give the PMOS far too negative a threshold.
    Buried channels are more prone to {term}`punch-through` at short
    gate lengths than surface channels.

C49 TiSi₂
    The metastable, high-resistivity crystal form of titanium disilicide
    that forms first when titanium reacts with silicon. A second, hotter
    anneal converts it to the stable, low-resistivity C54 form; the
    conversion becomes harder as features shrink, because it starts from
    only a few nucleation sites in each line. The two-anneal titanium
    {term}`silicide` process exists to manage this transition (see
    {ref}`step-098`).

C54 TiSi₂
    See {term}`C49 TiSi₂`.

cap oxide
    A thin undoped CVD oxide deposited over a doped glass or a freshly
    polished dielectric to seal it: it keeps the phosphorus or boron of
    a {term}`PSG` or {term}`BPSG` layer away from the films above, gives
    a clean, stable surface for the next lithography and blocks
    moisture. This reference describes one over the gates
    ({ref}`step-059`), one over the planarised pre-metal glass
    ({ref}`step-091`) and one over the polished oxide of each metal
    level, the first of them {ref}`step-117`.

CAR
    Chemically amplified resist: a photoresist in which exposure creates
    a photo-acid that, during the post-exposure bake, catalytically
    deprotects many polymer sites per photon. Used for deep-UV (248 nm
    and 193 nm) lithography.

CD
    Critical dimension: the width of the smallest or most important
    printed feature on a given layer, for instance the gate length on
    the poly layer.

CD-SEM
    Critical-dimension scanning electron microscope: a low-voltage SEM
    fitted with automated pattern recognition and measurement software,
    used to measure line widths in the fab.

CESL
    See {term}`contact etch-stop layer`.

chained implant
    A sequence of implants of one species at several energies and doses,
    run one after another on the same wafer without leaving the
    implanter, to build a deeper or flatter profile than a single implant
    can give. It is the usual way to make a {term}`retrograde well`.

channelling
    Steering of implanted ions along open directions (axes or planes) in
    a crystal, which greatly increases their range. Suppressed by tilting
    the wafer, by implanting through a screen oxide, or by
    pre-amorphisation.

charge-trapping layer
    The silicon nitride in the middle of the {term}`ONO` stack of a
    {term}`SONOS` transistor. Electrons or holes injected through the
    {term}`tunnel oxide` are held in deep traps in the nitride, so the
    stored charge is localised and a single defect in the tunnel oxide
    cannot drain the whole cell, as it would in a floating-gate device.

cluster tool
    A vacuum platform with a central wafer-handling robot surrounded by
    several process chambers, so that a wafer can be degassed,
    sputter-cleaned and coated with two or three films in turn without
    seeing air between them. Nearly all {term}`PVD` and much CVD of the
    back end is done this way; the sequence of chambers a wafer visits
    is the recipe of the step (see {ref}`step-097`).

CMP
    Chemical-mechanical planarisation (or polishing): removal of material
    by pressing a rotating wafer against a polishing pad flooded with an
    abrasive, chemically active slurry.

collimated sputtering
    A {term}`PVD` variant in which a honeycomb plate — the collimator —
    sits between the target and the wafer and lets through only atoms
    travelling nearly perpendicular to the wafer. More of the flux
    therefore reaches the bottom of deep contact holes, at the cost of
    a lower deposition rate and material lost on the collimator. It was
    the usual way to line contacts before {term}`IMP` sources (see
    {ref}`step-097`).

composite spacer
    A {term}`spacer` built from two films, usually a thin oxide liner
    under a thicker nitride. The nitride gives the spacer its etch
    selectivity and stability; the oxide keeps the nitride, with its
    charge traps and stress, away from the gate edge and the silicon,
    which improves hot-carrier lifetime. Also "oxide/nitride spacer";
    see {ref}`step-076` for how SKY130's spacer is read.

contact etch-stop layer
    A silicon nitride blanket deposited over the finished transistors,
    or over the local interconnect, before the dielectric above it. The
    contact etch, which cannot tell one oxide from another, stops on the
    nitride; a short nitride etch then opens the holes. It makes
    {term}`borderless contact`s possible and, because it is deposited
    under stress, also strains the channel. Abbreviated CESL. SKY130's
    nitride cap over the local interconnect ({ref}`step-104`) plays this
    part for the metal contacts.

contact silicide
    A {term}`silicide` formed only at the bottom of the contact holes,
    where the titanium of the plug liner touches silicon or
    polysilicon, rather than over every exposed gate and source/drain
    as in a {term}`salicide` process. It lowers the contact resistance
    but leaves the sheet resistance of the diffusions and gates
    unchanged. SKY130 is read as using a contact-only silicide (see
    {ref}`step-098`).

control gate
    The gate of the memory transistor in a {term}`2-T cell`: the
    electrode above the {term}`ONO` stack that is biased to program,
    erase and read the {term}`SONOS` transistor.

coring
    A tungsten {term}`CMP` defect in which the polish pulls tungsten out
    of the seam at the centre of a plug, where the two growth fronts of
    the fill met, leaving a hollow core. It raises the plug's resistance
    and can trap slurry. Fills that close their seam cleanly, and
    polishes that stop soon after the tungsten clears, avoid it (see
    {ref}`step-100`).

counter-doping
    An implant of the opposite type to the doping already present, which
    lowers the net concentration or locally reverses the type. Used, for
    example, to lower the {term}`Vt` of a PMOS under an n⁺ gate
    ({term}`buried-channel PMOS`) or to make a {term}`depletion-mode`
    transistor.

CVD
    Chemical vapour deposition: growth of a solid film from gaseous
    precursors that react on or near a heated surface.

CZ
    Czochralski: the crystal-growth technique in which a seed crystal is
    slowly pulled from a melt of silicon, producing the boules from which
    almost all IC wafers are cut.

damascene
    A way of making metal wiring by etching trenches or holes into the
    dielectric, overfilling them with metal and polishing the excess
    away, so that metal remains only in the recesses. It is the opposite
    of {term}`subtractive metallisation` and is how copper wiring is
    made; SKY130's aluminium lines are subtractive, but its tungsten
    plugs are filled and polished in the damascene manner
    ({ref}`step-099`, {ref}`step-100`).

Deal–Grove model
    The linear–parabolic model of thermal oxidation of silicon
    (Deal and Grove, 1965) in which oxide thickness
    {math}`x` obeys {math}`x^2 + Ax = B(t + \tau)`.

degas
    A bake in vacuum given to a wafer just before a {term}`PVD`
    deposition, to drive out the moisture and other volatiles absorbed
    by the dielectrics and left by the cleans. Without it the gases
    would leave the wafer during sputtering, raising the chamber
    pressure and oxidising the growing film. Degas is usually the first
    station of a {term}`cluster tool` sequence.

DEMOS
    Drain-extended MOS: a high-voltage transistor built from a
    conventional gate whose drain contact is moved away from the gate
    edge by a lightly doped {term}`drift region`, so that most of the
    drain voltage is dropped across the drift region rather than across
    the gate oxide or the channel junction. The high-voltage transistors
    of SKY130 are of this kind (see {ref}`step-030`). Also
    "extended-drain MOS" (EDMOS).

depletion-mode
    A MOSFET that conducts at zero gate voltage and must be driven to
    turn off, because its channel is doped the same type as its source
    and drain; the opposite of the usual enhancement-mode transistor.
    The SKY130 {term}`SONOS` memory transistor is a depletion-mode device
    whose channel is set by the implant of {ref}`step-038`.

DIBL
    Drain-induced barrier lowering: the fall in threshold voltage of a
    short-channel MOSFET as the drain voltage rises, because the drain's
    depletion region reaches far enough to lower the potential barrier
    at the source. A {term}`halo` and a {term}`punch-through` stop limit
    it.

dishing
    In {term}`CMP`, the excess recession of the centre of a soft feature
    (a wide metal line or an oxide-filled trench) relative to the
    surrounding harder surface.

disposable spacer
    A {term}`spacer` that is used to offset an implant and then
    stripped, so that it does not remain in the finished transistor. It
    lets the deep source/drain be implanted before the extension, or a
    spacer material that must not stay be used; the alternative, which
    SKY130 follows, is a permanent spacer.

dose loss
    The fraction of a shallow implant — arsenic especially — that does
    not end up electrically active in the silicon, because it segregates
    to the surface oxide and the interface, or evaporates, during the
    activation anneal. It is worse for lower energies and longer
    anneals; an oxide kept in place over the silicon during the anneal
    and a short {term}`spike anneal` limit it (see {ref}`step-086`).

drift region
    The lightly doped region between the channel and the heavily doped
    drain contact of a {term}`DEMOS` transistor. It depletes at high
    drain voltage and absorbs most of that voltage, protecting the gate
    oxide and the channel junction.

dual gate oxide
    A process that grows gate oxides of two thicknesses on one wafer: a
    thin one for the core logic and a thicker one for the higher-voltage
    I/O and analogue transistors. The first oxide is grown everywhere
    and stripped through a mask from the thin-oxide regions
    ({ref}`step-046`); the second growth then thickens the surviving
    oxide and grows the thin one.

DUV
    Deep ultraviolet: exposure wavelengths shorter than the mercury
    i-line (365 nm), in practice the KrF excimer laser at 248 nm and
    ArF at 193 nm.

EBR
    Edge-bead removal: dissolving the thick rim of resist that forms at
    the wafer edge during spin coating, using a solvent stream or an
    exposure of the edge.

electromigration
    The slow transport of metal atoms along a conductor by the momentum
    of the electrons flowing through it, which at high current density
    thins the line at one point until it opens and piles up metal at
    another until it shorts or cracks the dielectric. Aluminium resists
    it better with a little copper in the alloy, a refractory underlayer
    and cap ({term}`Blech length`) and a preferred grain orientation.
    Also "EM".

electrostatic chuck
    A wafer holder that grips the wafer by electrostatic attraction
    through a thin dielectric instead of clamping its edge, and usually
    cools it with helium flowing between chuck and wafer. It leaves the
    whole front face free for processing and keeps the wafer at a
    controlled temperature in plasma-etch, implant and sputter tools.
    Abbreviated ESC.

endpoint
    The moment at which an etch (or polish) has removed the target film;
    detected optically (emission spectroscopy, interferometry), by motor
    torque in CMP, or by timing.

EOT
    Equivalent oxide thickness: the thickness of pure silicon dioxide
    that would give the same capacitance per unit area as the actual
    gate dielectric. It lets an {term}`oxynitride` or a high-k dielectric
    be compared with plain oxide.

epitaxial layer
    A single-crystal silicon layer grown on a silicon wafer by
    {term}`CVD`, continuing the substrate's crystal lattice but with an
    independently chosen doping.

erosion
    In {term}`CMP`, thinning of the hard surface (for example the oxide
    between dense tungsten plugs) in regions of high pattern density.

ESC
    See {term}`electrostatic chuck`.

etch bias
    The difference between the width of a feature after etching and the
    width of the resist or {term}`hard mask` pattern that defined it. The
    lithography target is offset to compensate. A deliberately large
    bias, as in a {term}`resist trim`, prints gates shorter than the
    lithography alone can resolve.

etch-stop layer
    A film of different chemistry from the layer being etched — commonly
    silicon nitride under an oxide — on which an etch of good
    {term}`selectivity` can land. It makes the {term}`endpoint` tolerant
    of thickness variation and {term}`over-etch` and protects whatever
    lies beneath. The {term}`contact etch-stop layer` is one example; a
    CMP stop layer plays the same part for a polish.

e-test
    Electrical test: automated DC measurement of transistors, resistors,
    capacitors and interconnect test structures on the wafer using a
    parametric tester and a probe card. Also called parametric test or
    {term}`WAT`.

extension
    The shallow, moderately doped part of the source/drain that extends
    under the gate edge; formed by a low-energy implant self-aligned to
    the gate before the spacer. Also "tip" or {term}`LDD`.

FEOL
    Front end of line: the portion of the process flow that forms the
    transistors and other devices in the silicon, up to but excluding
    the first interconnect level.

field stop
    An implant under the field oxide (or under the {term}`STI`) of the
    same type as the surrounding well, which raises the doping there so
    that a conductor crossing the isolation cannot invert the silicon
    beneath it and form a parasitic channel. Also "channel stop".

footing
    A wedge of material left at the base of an etched feature where the
    etch slows or stops on the underlying film, so that the feature is
    wider at its foot than at its top. In gate etching, footing at the
    poly/oxide interface lengthens the electrical gate; the opposite
    defect, in which the base is undercut, is called notching.

forming gas
    A mixture of a few per cent hydrogen in nitrogen (commonly 4–10 % H₂;
    see {ref}`category-anneal`) used for the {term}`alloy anneal`.

four-point probe
    A sheet-resistance measurement in which current is forced through two
    outer probes and voltage sensed on two inner ones, eliminating the
    contact resistance from the result.

Fowler–Nordheim tunnelling
    Quantum-mechanical tunnelling of electrons through the triangular
    barrier that a thin oxide presents when a high field is applied
    across it. It is the mechanism by which a {term}`SONOS` cell is
    programmed and erased through its {term}`tunnel oxide`, and it is
    also a leakage and wear-out mechanism in any thin gate oxide.

gap fill
    The ability of a dielectric deposition to fill the narrow space
    between adjacent lines or gates without leaving a void or seam. It
    depends on the {term}`aspect ratio` of the gap and on the process:
    {term}`HDP-CVD`, ozone–TEOS {term}`SACVD` and flowing doped glasses
    ({term}`reflow`) all exist mainly for gap fill.

gate oxide integrity
    The ability of a gate oxide to withstand voltage and charge stress
    without breaking down, measured by charge-to-breakdown and
    time-dependent dielectric breakdown tests on capacitor structures.
    Substrate defects, contamination, the grain structure of the poly
    above it and {term}`plasma charging` all affect it. Abbreviated GOI.

gettering
    Deliberate trapping of metallic contaminants away from the active
    device region, for example by oxygen precipitates in the wafer bulk
    or by damage on the wafer backside.

GIDL
    Gate-induced drain leakage: current from the drain to the substrate
    that flows when the field between the gate and the drain under the
    gate edge is strong enough for band-to-band tunnelling. It rises with
    heavier drain doping at the gate edge and with thinner gate oxide.

graded junction
    A junction whose doping falls off gradually with distance rather than
    stepping abruptly. In a high-voltage MOSFET it lowers the peak
    electric field at the drain, raising the breakdown voltage and
    reducing {term}`hot-carrier injection`; the {term}`LDD` and
    {term}`LATID` drains are ways of grading the drain junction.

halo
    A pocket implant of the opposite type to the source/drain, placed at
    an angle around the extension so that the channel doping rises as
    gate length shrinks, suppressing short-channel effects. Also
    "pocket".

hard mask
    An inorganic film (oxide, nitride or oxynitride) that is patterned
    through the photoresist and then serves as the mask for etching the
    film beneath it. It withstands aggressive plasmas and long etches
    better than resist, and can be thinner than the resist, which helps
    resolution.

HDP-CVD
    High-density-plasma chemical vapour deposition: an inductively coupled
    plasma {term}`CVD` in which simultaneous sputtering by biased argon
    ions keeps narrow gaps open while they fill, used for STI and
    inter-metal dielectric gap fill.

HF-last
    A wet clean whose final chemical step is dilute hydrofluoric acid,
    so that the wafer leaves the bath with its chemical oxide stripped
    and the silicon surface terminated by hydrogen. That surface is what
    silicide and contact-liner depositions want, but it re-oxidises in
    air within hours, which sets a {term}`queue time` to the next step
    (see {ref}`step-095`).

hillock
    A small bump of aluminium pushed up out of a film when compressive
    stress — from heating a metal that expands more than the substrate
    beneath it — is relieved by atoms diffusing to the surface. Hillocks
    can short through a thin dielectric to the level above. A refractory
    {term}`anti-reflective cap` and copper in the alloy suppress them.

HMDS
    Hexamethyldisilazane, a vapour-phase adhesion promoter that makes the
    wafer surface hydrophobic before resist coating.

hot-carrier injection
    Degradation of a MOSFET by carriers that gain enough energy in the
    high-field region near the drain to be injected into the gate oxide,
    where they create interface traps or trapped charge that shift
    {term}`Vt` and drive current over the life of the device. Lowering the
    drain field with an {term}`LDD` or a {term}`graded junction` is the
    standard remedy. Abbreviated HCI.

HTO
    High-temperature oxide: silicon dioxide deposited by {term}`LPCVD`
    from dichlorosilane and nitrous oxide at furnace temperature, giving
    a denser, more thermal-oxide-like film than {term}`TEOS` oxide. Used
    where a deposited oxide must behave like a grown one, for example as
    the {term}`blocking oxide` of an {term}`ONO` stack.

ICP
    Inductively coupled plasma: a high-density plasma excited by an RF
    coil, with ion energy controlled independently by a separate bias
    on the wafer chuck.

ILD
    Inter-level dielectric: the insulating film (usually silicon
    dioxide-based) between conducting levels. Also IMD (inter-metal
    dielectric).

IMD
    See {term}`inter-metal dielectric`.

IMP
    Ionised metal plasma: a {term}`PVD` variant in which a secondary RF
    plasma ionises the sputtered metal atoms so that a wafer bias can
    draw them vertically into high-aspect-ratio holes.

implant crust
    The hardened, carbon-rich skin that forms on photoresist during a
    high-dose implant as the ion beam breaks the polymer's bonds and
    drives out hydrogen. It ashes far more slowly than the resist under
    it, and if that resist is heated before the crust is gone it can
    rupture ({term}`popping`). See {ref}`category-strip`.

inter-metal dielectric
    The insulating layer between two levels of metal wiring, through
    which the {term}`via`s pass. It must fill the gaps between the lines
    beneath it and be planarised for the lithography above; SKY130's is
    a CVD oxide polished by {term}`CMP` ({ref}`step-115`,
    {ref}`step-116`). Abbreviated IMD; the term {term}`ILD` covers both
    it and the {term}`pre-metal dielectric`.

ISSG
    In-situ steam generation: growth of thin oxides in a single-wafer
    rapid-thermal chamber where H₂ and O₂ react at the wafer to produce
    steam and highly reactive atomic oxygen.

k1
    The dimensionless process factor in the resolution equation
    {math}`CD = k_1 \lambda / NA`; it captures how far resist,
    illumination and mask enhancements push resolution below the
    diffraction limit.

Kelvin structure
    A four-terminal test structure that measures the resistance of a
    single contact or via while excluding the series resistance of the
    leads.

keyhole
    A void left along the centre line of a plug or gap when the film
    growing in from the two side walls closes over at the top before the
    bottom has filled. In a tungsten plug the keyhole, or seam, is
    exposed by the CMP and can be pulled open ({term}`coring`); in a
    dielectric it can fill with metal at the next step and short
    adjacent lines. Conformal deposition and a tapered profile avoid it.

knock-on implantation
    Recoil of atoms from a surface film into the substrate by the
    implanted ions, for example oxygen knocked out of a
    {term}`screen oxide` into the silicon. The recoiled atoms create
    defects or change the properties of the shallow layer. Also "recoil
    implantation".

LATID
    Large-angle-tilt implanted drain: an {term}`LDD` variant in which the
    extension is implanted at a large tilt so that it reaches well under
    the gate edge, giving a gate-overlapped, {term}`graded junction` with
    a low peak field and a long hot-carrier lifetime. Its cost is
    sensitivity to {term}`shadowing`.

LDD
    Lightly doped drain: the earlier name for the source/drain
    {term}`extension`.

LER
    Line-edge roughness: the random deviation of a printed line's edge
    from a straight line, quoted as a standard deviation or a
    peak-to-peak value along the edge. It transfers from the resist into
    the etched gate and becomes a source of transistor variability at
    short gate lengths. The related line-width roughness (LWR) combines
    the two edges.

LI
    See {term}`local interconnect`.

liner
    A thin conformal film deposited into a contact, via or trench before
    the fill: for a tungsten plug, a titanium layer that makes ohmic
    contact and a titanium nitride layer that protects the titanium and
    the silicon from the tungsten hexafluoride and gives the tungsten a
    surface to nucleate on. Also the first film of a
    {term}`composite spacer` or the thin oxide under an HDP fill.
    Compare {term}`barrier metal`.

loading effect
    Dependence of etch rate on the amount of material exposed to the
    plasma, either across the wafer (macro-loading) or between dense and
    isolated features (micro-loading).

local interconnect
    A short-range wiring level below the first metal, used to join gates
    and diffusions to each other within a cell and to carry the contacts
    up to metal-1. In SKY130 it is a thin titanium nitride layer (`li1`)
    patterned by its own mask and sitting between two layers of contacts
    ({ref}`step-101` to {ref}`step-103`). Its resistance is far higher
    than a metal's, so it is used only over short distances.
    Abbreviated LI.

LOCOS
    Local oxidation of silicon: the pre-STI isolation scheme in which a
    thick field oxide is grown through openings in a nitride mask.

LPCVD
    Low-pressure chemical vapour deposition: thermally driven
    {term}`CVD` at a fraction of atmospheric pressure, usually in a
    batch furnace, giving highly conformal films such as polysilicon,
    silicon nitride and TEOS oxide.

LSS theory
    The Lindhard–Scharff–Schiøtt theory of ion stopping and range, which
    predicts the projected range and straggle of implanted ions from
    nuclear and electronic stopping powers.

mask-proximity effect
    A shift in the characteristics of a transistor that lies close to
    the edge of an implant's resist mask, caused by ions scattering out
    of the resist sidewall into the nearby silicon and by the resist
    edge shadowing a tilted beam. It is the source/drain-mask
    counterpart of the {term}`well proximity effect`, and layout rules
    keep matched devices the same distance from mask edges (see
    {ref}`step-081`).

metal fuse
    A narrow link in a metal wiring level that can be blown open after
    fabrication — by a laser through the passivation or by a current
    pulse — to trim a circuit or select redundant elements. The SKY130
    PDK's metal-fuse rules name metal 4 as the fuse level for the
    SKY130P* flow (see {ref}`step-149`, {ref}`step-154`).

MiM capacitor
    Metal–insulator–metal capacitor: two metal plates separated by a
    thin deposited dielectric, built in the back end. Because its
    plates have no depletion layer its capacitance changes little with
    bias, and its series resistance is low. In SKY130 the bottom plate
    is a metal level and the top plate a thin film patterned by the
    `capm` or `cap2m` mask (see {ref}`step-135` to {ref}`step-138` and
    {ref}`step-150` to {ref}`step-153`).
    Also "MIM capacitor".

MOL
    Middle of line: the contact and local-interconnect steps that bridge
    FEOL and BEOL.

NA
    Numerical aperture of the projection lens, {math}`n \sin\theta`; the
    larger the NA the finer the resolution and the shallower the depth
    of focus.

nitride cut
    SKY130's name for the opening of the nitride that covers the
    polysilicon gates and resistors — the *nitride poly cut* of
    {ref}`step-078` and {ref}`step-079` — so that the local-interconnect
    contacts can reach the poly wherever the `npc` layer is drawn.
    Elsewhere the nitride stays in place as an {term}`etch-stop layer`.
    Also "poly cut".

notching
    A plasma-etch defect in which the foot of a line is eaten sideways
    at its interface with the underlying insulator, most often on the
    outer lines of an array. It is caused by charge building up on the
    insulator and deflecting ions towards the line, and worsens during
    the {term}`over-etch` of high-density-plasma etches of polysilicon
    and aluminium (see {ref}`step-114`).

nucleation layer
    The thin first layer of a CVD tungsten fill, deposited with silane
    or diborane reducing the tungsten hexafluoride, on which the thick
    hydrogen-reduced bulk film can then grow. Without it tungsten grows
    slowly and unevenly on titanium nitride and the fluorine attacks
    the liner. A {term}`pulsed nucleation layer` is one way of forming
    it (see {ref}`step-099`).

ONO
    Oxide–nitride–oxide: the tunnel oxide / charge-trapping nitride /
    blocking oxide stack of a SONOS non-volatile memory transistor.

OPC
    Optical proximity correction: pre-distortion of mask features (serifs,
    hammerheads, biasing) so that the printed image matches the intended
    layout despite diffraction.

overburden
    The film deposited beyond what is needed to fill the gaps between
    lines — the excess that the following {term}`CMP` removes. It must
    be thick enough that the polish reaches a flat surface before it
    exposes the lines, and uniform enough that the polish time is the
    same everywhere (see {ref}`step-115`).

over-etch
    The part of an etch that continues after the {term}`endpoint`, to
    clear the film from the places where it is thicker or etches more
    slowly (over steps, in dense features). It is set as a percentage of
    the main-etch time or as a fixed time, and is limited by the loss of
    the underlying film that the {term}`selectivity` allows.

overlay
    The positional error between a printed layer and a previously printed
    layer, measured on dedicated box-in-box or grating targets.

oxide bias
    A parameter of the PDK's *Criteria & Assumptions* table, given per
    metal level ("Oxide Bias for MM1" to "Oxide Bias for MM4": 0.6 for
    metals 1 and 2, 1.15 for metals 3 and 4) and listed with the
    pattern-density limits for the oxide polishes. The PDK does not
    define it; the pages of this reference read it as a density-related
    allowance for the dielectric {term}`CMP` over each metal level
    rather than as a drawn-layer bias (see {ref}`step-116` and
    {ref}`step-142`).

oxynitride
    Silicon dioxide containing nitrogen, either grown in a
    nitrogen-bearing ambient (N₂O or NO), made by nitriding an existing
    oxide in a plasma or in ammonia, or deposited by {term}`CVD`. As a
    gate dielectric a lightly nitrided oxide blocks
    {term}`boron penetration` and raises the dielectric constant; as a
    deposited film silicon oxynitride serves as an inorganic
    {term}`BARC` and as a {term}`hard mask`. Also "nitrided oxide".

pattern density
    The fraction of the area within some window that is covered by
    raised features — metal lines, or the oxide over them. Because a
    {term}`CMP` pad presses harder on a sparse pattern than on a dense
    one, the local removal rate and the final thickness depend on it,
    which is why PDKs set minimum and maximum densities and add dummy
    fill. The window over which the density matters is the
    {term}`planarisation length`.

PCM
    Process control monitor: the set of electrical test structures placed
    in the scribe lines (or in dedicated drop-in sites) of every wafer
    and measured at {term}`e-test`.

PEB
    Post-exposure bake: the hot-plate step after exposure that drives the
    acid-catalysed reaction in a {term}`CAR` and smooths standing waves
    in a conventional resist.

PECVD
    Plasma-enhanced chemical vapour deposition: {term}`CVD` in which an RF
    plasma supplies the energy to dissociate precursors, allowing
    deposition at 250–400 °C on wafers that already carry metal (see
    {ref}`category-deposition`).

planarisation length
    The lateral distance over which a {term}`CMP` process averages the
    {term}`pattern density`: features closer together than this polish
    as if they were one, features farther apart polish independently.
    It is a property of the pad, slurry and pressure, and it is the
    characteristic length in the density-based CMP models (see
    {ref}`step-090`).

plasma charging
    Build-up of charge on a wafer during plasma processing when the
    electron and ion currents collected by a conductor do not balance;
    a conductor connected to a gate then drives a damaging current
    through the thin gate oxide. Also "antenna effect", because the
    damage scales with the area of conductor connected to each gate.

plasma flood gun
    A device on a high-current ion implanter that fills the space in
    front of the wafer with a low-energy plasma, usually of argon or
    xenon, so that electrons from it neutralise the positive charge the
    ion beam leaves on the resist-covered, insulated areas of the wafer.
    Without it the charge can break down thin gate oxides. Abbreviated
    PFG (see {ref}`step-082`).

plug recess
    The dip of the top of a tungsten plug below the surrounding oxide
    after the tungsten {term}`CMP` or etch-back, because the tungsten
    polishes faster than the oxide once the field has cleared. A deep
    recess thins the liner and the metal that must fill it at the next
    step and raises the contact resistance (see {ref}`step-100`).

PMD
    See {term}`pre-metal dielectric`.

PNL
    See {term}`pulsed nucleation layer`.

pocket
    See {term}`halo`.

poly cut
    See {term}`nitride cut`.

poly depletion
    The thin depletion layer that forms in a polysilicon gate next to
    the gate oxide when the transistor is turned on, because poly cannot
    be doped heavily enough to behave as a metal. It adds to the
    effective oxide thickness and reduces drive current; the remedy is
    to dope the gate as heavily as the process allows.

poly re-oxidation
    A short thermal oxidation after the gate etch that grows a thin
    oxide on the poly sidewalls and on the exposed silicon. It rounds the
    gate corner, repairs oxide damaged by the etch and thickens the gate
    oxide at the gate edge, which reduces {term}`hot-carrier injection`.
    See {ref}`step-063`.

poly resistor
    A resistor made from a strip of the gate polysilicon, given a
    controlled doping by a dedicated implant and kept free of
    {term}`silicide` where a high resistance is wanted. The doping level
    sets its {term}`sheet resistance`, its temperature coefficient and
    its voltage coefficient.

popping
    Rupture of the {term}`implant crust` on photoresist during an ash or
    a bake, when solvent and gases trapped in the resist beneath the
    crust expand and blow flakes of crust across the wafer. It is
    avoided by ashing at low temperature until the crust is gone, or by
    curing the resist before the implant. See {ref}`category-strip`.

post-CMP clean
    The brush scrub and chemical rinse that follow every {term}`CMP`
    step, to remove the slurry particles and metal ions the polish
    leaves behind before they dry on. After an oxide polish the
    chemistry is dilute ammonia or a surfactant; after a tungsten polish
    a dilute acid or amine removes the metal and abrasive residues (see
    {ref}`step-090`).

pre-amorphisation implant
    A heavy-ion implant (usually germanium or silicon) that turns the
    top of the silicon amorphous before a shallow dopant implant, so that
    the dopant cannot channel and the layer regrows by
    {term}`solid-phase epitaxy` with the dopant on lattice sites.
    Abbreviated PAI.

pre-metal dielectric
    The insulator between the transistors and the first level of wiring,
    in which the contacts are etched. It is usually a doped glass
    ({term}`PSG` or {term}`BPSG`), for {term}`gettering` and
    {term}`gap fill`, sealed with a {term}`cap oxide` and planarised by
    {term}`CMP`. In SKY130 the layers from {ref}`step-089` to
    {ref}`step-091`, and the oxide of {ref}`step-105` above the local
    interconnect, play this part. Abbreviated PMD.

Preston coefficient
    The proportionality constant {math}`k_p` of the
    {term}`Preston equation`, which lumps together everything about the
    pad, slurry and film that is not pressure or velocity. It is found
    by experiment for each polish process.

Preston equation
    The empirical {term}`CMP` removal-rate law {math}`R = k_p\,P\,v`, in
    which removal rate is proportional to applied pressure and to
    relative pad–wafer velocity.

program inhibit
    The bias condition applied to memory cells that share a word line
    with a cell being programmed but must not be programmed themselves,
    and by extension the threshold-voltage state of such cells. In the
    {term}`2-T cell` the {term}`select gate` and the bit-line bias
    provide the inhibit.

projected range
    The mean depth {math}`R_p` at which implanted ions come to rest,
    measured along the beam direction; its spread is the straggle
    {math}`\Delta R_p`.

PSG
    Phosphosilicate glass: silicon dioxide doped with a few weight per
    cent phosphorus, used as a gettering and flowable pre-metal
    dielectric.

PSM
    Phase-shift mask: a photomask in which selected features transmit
    light with a 180° phase difference so that destructive interference
    sharpens the image.

pulsed nucleation layer
    Novellus's name for a tungsten {term}`nucleation layer` grown by
    alternating short pulses of tungsten hexafluoride and a reducing gas
    (silane or diborane) rather than by flowing them together. Each
    cycle adds a thin, conformal layer, so the nucleation film can be
    made very thin with good {term}`step coverage` in narrow holes.
    Abbreviated PNL (see {ref}`step-099`).

punch-through
    Leakage between the source and drain of a short-channel MOSFET,
    beyond the control of the gate, that occurs when the drain's
    depletion region reaches the source. The remedy is to raise the
    doping below the channel with a punch-through stop implant, or around
    the extensions with a {term}`halo`.

PVD
    Physical vapour deposition: deposition of a film from atoms ejected
    from a solid target, in IC manufacturing almost always by magnetron
    sputtering in argon.

quad implant
    A tilted implant delivered in four equal doses at wafer rotations
    90° apart, so that every gate receives the same tilted dose on both
    sides whatever its orientation on the wafer; the usual way to make
    {term}`halo` and {term}`LATID` implants symmetric. Also
    "quad-rotation" or "four-rotation" implant.

quality factor
    Q: for a capacitor or inductor, the ratio of the energy it stores
    to the energy it dissipates per cycle, for a capacitor
    {math}`1/(\omega R C)` with {math}`R` the series resistance. Plate
    and contact resistance lower the Q of a {term}`MiM capacitor` at
    radio frequencies.

queue time
    The maximum time a wafer may wait between two steps, set by how
    quickly a surface degrades: an {term}`HF-last` silicon surface
    re-oxidises, a freshly polished oxide absorbs moisture, an exposed
    resist loses its latent image. Wafers that exceed it are cleaned
    again or reworked.

radical oxidation
    Oxidation by atomic oxygen radicals generated from hydrogen and
    oxygen at low pressure, either in a single-wafer {term}`ISSG` chamber
    or in a furnace. Radicals oxidise silicon nitride and poly grain
    boundaries far more readily than molecular oxygen does, and give a
    uniform oxide on top of a nitride, as in an {term}`ONO` stack.

RCA clean
    The two-step wet clean of Kern and Puotinen: {term}`SC-1`
    (NH₄OH/H₂O₂/H₂O) to remove particles and organics, then {term}`SC-2`
    (HCl/H₂O₂/H₂O) to remove metals.

reactive sputtering
    Sputtering a metal target in a mixture of argon and a reactive gas,
    usually nitrogen or oxygen, so that the compound — titanium nitride
    from a titanium target — forms on the wafer. The process has a
    hysteresis: above a certain gas flow the target itself nitrides and
    the rate falls, so the flow is controlled to stay near that
    transition (see {ref}`step-101`).

reflow
    Heating a doped glass ({term}`PSG` or {term}`BPSG`) until it softens
    and flows, which rounds sharp steps and fills the gaps between gates
    or lines. The temperature needed falls as the dopant content rises;
    the constraint is the {term}`thermal budget` of the junctions
    beneath. {term}`CMP` has largely replaced reflow as the way of
    planarising, but a short reflow can still be used for gap fill (see
    {ref}`step-092`). In metallisation the word also names aluminium
    reflow: aluminium deposited onto, or heated on, a wafer at several
    hundred degrees Celsius so that it flows into contact and via holes
    (see {term}`aluminium via fill`, {ref}`step-161`).

resist trim
    A short isotropic plasma etch of the developed resist before the
    gate etch, which narrows the resist lines below the width the
    lithography printed. It lets a process print gates shorter than its
    lithography can resolve, at the cost of tighter control of
    {term}`LER` and of resist collapse.

reticle
    The photomask used in a reduction stepper or scanner; it carries one
    field of the layout at 4× or 5× magnification.

retrograde well
    A well whose doping peaks at some depth below the surface and falls
    towards it, the opposite of a diffused well. It is made by
    high-energy ion implantation, usually as a {term}`chained implant`,
    and needs only a light anneal; the low surface concentration gives a
    well-behaved channel and the deep peak suppresses
    {term}`punch-through` and latch-up.

reverse short-channel effect
    A rise in {term}`Vt` as the gate length shrinks, the opposite of the
    usual roll-off. It is caused by dopant piling up near the gate edges,
    either through {term}`TED` of the channel dopant towards the
    source/drain damage or through the two {term}`halo` implants
    overlapping in a short channel. Abbreviated RSCE.

RIE
    Reactive-ion etching: plasma etching in which the wafer sits on the
    RF-driven electrode so that energetic ions strike it vertically,
    giving anisotropic profiles.

RTA
    Rapid thermal anneal: a single-wafer anneal in a lamp-heated chamber
    with ramp rates of tens to hundreds of degrees per second and a
    soak of seconds (see {ref}`category-anneal`). RTA is one application
    of {term}`RTP`.

RTP
    Rapid thermal processing: the family of single-wafer lamp-heated
    processes (anneal, oxidation, nitridation, silicidation).

SACVD
    Sub-atmospheric chemical vapour deposition: thermal CVD of silicon
    dioxide from {term}`TEOS` and ozone at a pressure well above that of
    {term}`LPCVD` but below atmospheric. The ozone–TEOS reaction gives a
    film that flows into narrow gaps as it deposits, which makes it a
    gap-filling alternative to {term}`HDP-CVD` for pre-metal and
    inter-metal dielectrics (see {ref}`step-089`).

salicide
    Self-aligned silicide: a metal (Ti, Co, Ni) deposited over the whole
    wafer reacts with exposed silicon and polysilicon during an anneal,
    while unreacted metal on oxide and nitride is stripped away.

SC-1
    Standard clean 1 (also APM): ammonium hydroxide, hydrogen peroxide
    and water, typically 1:1:5 to 1:2:50 at 40–80 °C; removes particles
    and organic residues (see {ref}`category-strip`).

SC-2
    Standard clean 2 (also HPM): hydrochloric acid, hydrogen peroxide and
    water, typically 1:1:6 at 70–80 °C; removes metallic contamination
    (see {ref}`category-strip`).

screen oxide
    A thin oxide left on, or grown on, the silicon before an implant. It
    protects the surface from contamination and sputtering, randomises
    the ion directions to reduce {term}`channelling`, and keeps the
    resist's outgassing off the silicon. Its cost is
    {term}`knock-on implantation` of oxygen.

scribe line
    The streets between dies on a wafer that will be cut by the dicing
    saw; used to hold {term}`PCM` structures and alignment targets.

select gate
    The gate of the ordinary transistor in series with the memory
    transistor of a {term}`2-T cell`. Turning it on connects the memory
    transistor to the bit line for reading or programming; turning it
    off isolates the cells that are not selected.

selectivity
    The ratio of the etch rate of the film being removed to the etch rate
    of the mask or of the underlying film that must be preserved.

shadowing
    Loss of a tilted implant next to a tall feature (a gate, a resist
    wall) that casts a "shadow" the tilted beam cannot reach. It makes
    the two sides of a transistor differ unless the implant is rotated
    ({term}`quad implant`), and it sets a minimum distance between resist
    edges and gates for tilted implants such as the {term}`halo`.

sheet resistance
    The resistance of a square of a thin film, {math}`R_s = \rho / t`,
    expressed in ohms per square (Ω/□).

silicide
    A compound of a metal with silicon (TiSi₂, CoSi₂, NiSi) formed on
    gates and source/drains to lower their sheet and contact resistance.

single-work-function gate
    A gate process in which the polysilicon is doped one type (n⁺) for
    both NMOS and PMOS, rather than n⁺ on the NMOS and p⁺ on the PMOS
    ("dual work function"). It saves masks and avoids
    {term}`boron penetration`, but forces a {term}`buried-channel PMOS`.

soft landing
    The final stage of a plasma etch, run at reduced ion energy as the
    film clears, so that the layer underneath (the thin gate oxide under
    a poly gate) is neither punched through nor damaged. It is followed
    by the {term}`over-etch`.

solid-phase epitaxy
    Regrowth of an amorphous silicon layer into single crystal from the
    crystalline silicon beneath it, proceeding layer by layer at a
    temperature well below the melting point. Dopants in the amorphous
    layer are placed on lattice sites as the interface passes, giving
    high activation with little diffusion. Abbreviated SPE.

SONOS
    Silicon–oxide–nitride–oxide–silicon: a non-volatile memory
    transistor whose gate dielectric is an {term}`ONO` stack, with the
    data stored as charge in the nitride {term}`charge-trapping layer`.
    SKY130 descends from a Cypress SONOS technology, and its memory
    module is described on the pages from {ref}`step-035` to
    {ref}`step-042`.

spacer
    A dielectric sidewall (nitride or oxide) left on the gate edge by an
    anisotropic etch-back of a conformal film; it offsets the deep
    source/drain implant and the silicide from the channel.

SPC
    Statistical process control: charting of in-line measurements against
    control limits so that drift is detected before it affects yield.

SPE
    Solid-phase epitaxy; see {term}`solid-phase epitaxy`. In the step
    list used in this reference `SPE` is also the code of the spacer
    nitride etch ({ref}`step-077`), which has nothing to do with
    epitaxy.

spike anneal
    An {term}`RTA` with no soak: the wafer is ramped as fast as the lamps
    allow to the peak temperature and cooled at once. The short time at
    high temperature activates dopants while limiting their diffusion,
    which is what shallow source/drain {term}`extension`s need.

SPM
    Sulfuric-peroxide mixture (also "piranha"): concentrated H₂SO₄ and
    30 % H₂O₂, typically 3:1 to 4:1, self-heating to above 100 °C, used
    to strip and oxidise organic residues (see {ref}`category-strip`).

sputter etch
    A short argon-ion bombardment of the wafer in a {term}`PVD`
    chamber, just before the metal is deposited, to remove the native
    oxide and contamination from the surface the film must contact. It
    is the in-vacuum counterpart of an {term}`HF-last` wet clean; too
    much of it redeposits material on the walls of the holes. Also
    "pre-clean" or "sputter clean".

SRAF
    Sub-resolution assist feature: a narrow bar placed on the mask next
    to an isolated feature, too small to print itself, which changes the
    diffraction pattern so that the isolated feature prints more like a
    dense one. Also "scattering bar".

step coverage
    The ratio of film thickness on the sidewall or bottom of a step to
    that on the flat top surface; a measure of conformality.

stepper
    A projection exposure tool that images one reticle field at a time
    and steps the wafer between exposures. A scanner additionally scans
    the reticle and wafer through a slit during each exposure.

STI
    Shallow trench isolation: device isolation formed by etching trenches
    into silicon, filling them with deposited oxide and planarising by
    {term}`CMP`.

straggle
    See {term}`projected range`.

stress-induced voiding
    The opening of voids in a metal line, with no current flowing, as
    the tensile stress locked into it by cooling from the deposition or
    dielectric temperature relaxes by atoms diffusing away from one
    point. It is a reliability failure of aluminium lines under stiff
    dielectrics; a refractory underlayer keeps the line conducting
    across the void. Also "stress migration".

subtractive metallisation
    Making wiring by depositing a blanket metal film, printing the lines
    in resist and etching away the metal between them, after which the
    dielectric is deposited over the lines and planarised. It is how
    aluminium levels are made, including SKY130's ({ref}`step-113`,
    {ref}`step-114`); the alternative is {term}`damascene`.

swing curve
    The periodic rise and fall of a photoresist's sensitivity, and hence
    of the printed linewidth, as the resist thickness changes, caused by
    interference between light reflected from the top of the resist and
    light reflected from the substrate beneath it. Its amplitude is
    largest on shiny substrates such as metal; a {term}`BARC` or
    {term}`TARC` flattens it (see {ref}`step-113`).

TARC
    Top anti-reflective coating: a thin, low-index layer spun on top of
    the resist to reduce reflection at the air–resist interface.

TCP
    Transformer-coupled plasma: Lam Research's name for its inductively
    coupled plasma etch reactors.

TED
    Transient enhanced diffusion: the temporary, many-fold increase in
    dopant diffusivity caused by the excess silicon interstitials left
    by an implant, which decays as the damage anneals out.

TEOS
    Tetraethyl orthosilicate, Si(OC₂H₅)₄: a liquid precursor vaporised to
    deposit conformal silicon dioxide by {term}`LPCVD` (around 700 °C)
    or {term}`PECVD` (around 400 °C); see {ref}`category-deposition`.

thermal budget
    The combined time-at-temperature of all the heat treatments a wafer
    receives after a given dopant or film is in place, which sets how
    far that dopant diffuses or how much the film changes. Every step is
    limited by the thermal budget that the junctions and films already
    present can tolerate.

threshold-adjust implant
    A low-dose, shallow implant into the channel region that shifts the
    {term}`Vt` of one transistor type to its target; separate masks give
    the low-, standard- and high-Vt flavours their own adjust implants.
    Also "Vt-adjust" or "channel implant".

tunnel oxide
    The bottom oxide of the {term}`ONO` stack of a {term}`SONOS`
    transistor, between the channel and the {term}`charge-trapping layer`.
    It is thin enough for carriers to pass through it by
    {term}`Fowler–Nordheim tunnelling` during program and erase, yet must
    hold them back during retention; its thickness and quality dominate
    the memory's endurance and retention.

van der Pauw structure
    A symmetric four-contact test structure (Greek cross or cloverleaf)
    from which the sheet resistance of a film is obtained by van der
    Pauw's theorem, independent of the structure's size.

via
    A hole through an {term}`inter-metal dielectric`, filled with metal,
    that connects one level of wiring to the next. In SKY130 vias 1–3
    are tungsten-filled ({term}`W plug`); via 4 is 0.8 µm wide, this
    reference describes no tungsten plug for it, and it is read here as
    filled by the metal-5 aluminium (see {ref}`step-161`). The word
    "contact" is kept for the connections from metal-1 down to the local interconnect
    and from the local interconnect down to silicon and poly.

via poisoning
    A via that ends up open or highly resistive because moisture or
    other volatiles from the surrounding dielectric outgassed into the
    hole while the metal was being deposited and oxidised its base.
    Dielectrics that absorb water — spin-on glasses, porous or
    hydrogen-rich oxides — are the usual cause; a dense
    {term}`cap oxide` and a {term}`degas` before deposition prevent it
    (see {ref}`step-117`).

voltage coefficient
    The relative change of a passive component's value with applied
    voltage. For a capacitor it is written as
    {math}`C(V) = C_0 (1 + \alpha V + \beta V^2)`, with the linear and
    quadratic coefficients usually quoted in ppm/V and ppm/V²; a
    {term}`MiM capacitor` is valued for keeping them small.

Vt
    Threshold voltage: the gate voltage at which a MOSFET turns on; set
    by channel doping, oxide thickness and gate work function.

wafer sort
    Functional testing of every die on a wafer with automatic test
    equipment before dicing, in contrast to parametric {term}`e-test`.

WAT
    Wafer acceptance test: the parametric {term}`e-test` whose results
    decide whether a wafer is shipped.

well proximity effect
    A shift in the {term}`Vt` of transistors placed close to the edge of
    a well mask, caused by ions scattering off the resist sidewall during
    the high-energy well implant and landing in the nearby channel.
    Layout rules keep sensitive devices away from well edges.

W plug
    A contact or via filled with CVD tungsten over a Ti/TiN liner and
    planarised by {term}`CMP`.

```
