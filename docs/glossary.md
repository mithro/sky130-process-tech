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

anisotropy
    The degree to which an etch proceeds in one direction (normally
    vertically, into the wafer) rather than equally in all directions.
    A perfectly anisotropic etch has zero lateral etch rate; a purely
    chemical wet etch of an amorphous film is isotropic.

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

BEOL
    Back end of line: the interconnect portion of the process flow, from
    the first contact through the final passivation.

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

boron penetration
    Diffusion of boron from a p⁺ polysilicon gate through a thin gate
    oxide into the channel during the anneals that follow gate doping,
    which shifts the PMOS {term}`Vt` and degrades the oxide. It is
    suppressed by nitrogen in the gate oxide ({term}`oxynitride`) or
    avoided altogether by using an n⁺ gate on the PMOS
    ({term}`single-work-function gate`).

buried-channel PMOS
    A p-channel MOSFET with an n⁺ polysilicon gate whose channel has been
    {term}`counter-doping`-implanted so that the conducting layer lies a
    little below the silicon surface. It is the consequence of a
    {term}`single-work-function gate` process, in which the n⁺ gate work
    function would otherwise give the PMOS far too negative a threshold.
    Buried channels are more prone to {term}`punch-through` at short
    gate lengths than surface channels.

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

CMP
    Chemical-mechanical planarisation (or polishing): removal of material
    by pressing a rotating wafer against a polishing pad flooded with an
    abrasive, chemically active slurry.

control gate
    The gate of the memory transistor in a {term}`2-T cell`: the
    electrode above the {term}`ONO` stack that is biased to program,
    erase and read the {term}`SONOS` transistor.

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

Deal–Grove model
    The linear–parabolic model of thermal oxidation of silicon
    (Deal and Grove, 1965) in which oxide thickness
    {math}`x` obeys {math}`x^2 + Ax = B(t + \tau)`.

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

etch bias
    The difference between the width of a feature after etching and the
    width of the resist or {term}`hard mask` pattern that defined it. The
    lithography target is offset to compensate. A deliberately large
    bias, as in a {term}`resist trim`, prints gates shorter than the
    lithography alone can resolve.

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

loading effect
    Dependence of etch rate on the amount of material exposed to the
    plasma, either across the wafer (macro-loading) or between dense and
    isolated features (micro-loading).

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

MOL
    Middle of line: the contact and local-interconnect steps that bridge
    FEOL and BEOL.

NA
    Numerical aperture of the projection lens, {math}`n \sin\theta`; the
    larger the NA the finer the resolution and the shallower the depth
    of focus.

ONO
    Oxide–nitride–oxide: the tunnel oxide / charge-trapping nitride /
    blocking oxide stack of a SONOS non-volatile memory transistor.

OPC
    Optical proximity correction: pre-distortion of mask features (serifs,
    hammerheads, biasing) so that the printed image matches the intended
    layout despite diffraction.

over-etch
    The part of an etch that continues after the {term}`endpoint`, to
    clear the film from the places where it is thicker or etches more
    slowly (over steps, in dense features). It is set as a percentage of
    the main-etch time or as a fixed time, and is limited by the loss of
    the underlying film that the {term}`selectivity` allows.

overlay
    The positional error between a printed layer and a previously printed
    layer, measured on dedicated box-in-box or grating targets.

oxynitride
    Silicon dioxide containing nitrogen, either grown in a
    nitrogen-bearing ambient (N₂O or NO), made by nitriding an existing
    oxide in a plasma or in ammonia, or deposited by {term}`CVD`. As a
    gate dielectric a lightly nitrided oxide blocks
    {term}`boron penetration` and raises the dielectric constant; as a
    deposited film silicon oxynitride serves as an inorganic
    {term}`BARC` and as a {term}`hard mask`. Also "nitrided oxide".

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

plasma charging
    Build-up of charge on a wafer during plasma processing when the
    electron and ion currents collected by a conductor do not balance;
    a conductor connected to a gate then drives a damaging current
    through the thin gate oxide. Also "antenna effect", because the
    damage scales with the area of conductor connected to each gate.

pocket
    See {term}`halo`.

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

pre-amorphisation implant
    A heavy-ion implant (usually germanium or silicon) that turns the
    top of the silicon amorphous before a shallow dopant implant, so that
    the dopant cannot channel and the layer regrows by
    {term}`solid-phase epitaxy` with the dopant on lattice sites.
    Abbreviated PAI.

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

spike anneal
    An {term}`RTA` with no soak: the wafer is ramped as fast as the lamps
    allow to the peak temperature and cooled at once. The short time at
    high temperature activates dopants while limiting their diffusion,
    which is what shallow source/drain {term}`extension`s need.

SPM
    Sulfuric-peroxide mixture (also "piranha"): concentrated H₂SO₄ and
    30 % H₂O₂, typically 3:1 to 4:1, self-heating to above 100 °C, used
    to strip and oxidise organic residues (see {ref}`category-strip`).

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
