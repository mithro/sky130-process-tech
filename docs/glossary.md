(glossary)=
# Glossary

Terms and acronyms used throughout this reference. Each entry is
referenced from the pages that use it with the `{term}` role.

```{glossary}
alloy anneal
    A low-temperature (typically 350–450 °C) anneal in hydrogen-bearing
    {term}`forming gas` performed after metallisation. It sinters the
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

BARC
    Bottom anti-reflective coating: an organic (spin-on) or inorganic
    (deposited, e.g. silicon oxynitride) layer under the photoresist that
    absorbs light reflected from the substrate.

BEOL
    Back end of line: the interconnect portion of the process flow, from
    the first contact through the final passivation.

BOE
    Buffered oxide etch: hydrofluoric acid buffered with ammonium
    fluoride (NH₄F), giving a stable, controlled etch rate for silicon
    dioxide.

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

channelling
    Steering of implanted ions along open directions (axes or planes) in
    a crystal, which greatly increases their range. Suppressed by tilting
    the wafer, by implanting through a screen oxide, or by
    pre-amorphisation.

CMP
    Chemical-mechanical planarisation (or polishing): removal of material
    by pressing a rotating wafer against a polishing pad flooded with an
    abrasive, chemically active slurry.

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

dishing
    In {term}`CMP`, the excess recession of the centre of a soft feature
    (a wide metal line or an oxide-filled trench) relative to the
    surrounding harder surface.

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

epitaxial layer
    A single-crystal silicon layer grown on a silicon wafer by
    {term}`CVD`, continuing the substrate's crystal lattice but with an
    independently chosen doping.

erosion
    In {term}`CMP`, thinning of the hard surface (for example the oxide
    between dense tungsten plugs) in regions of high pattern density.

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

forming gas
    A mixture of a few per cent hydrogen in nitrogen (commonly 4–10 % H₂)
    used for the {term}`alloy anneal`.

four-point probe
    A sheet-resistance measurement in which current is forced through two
    outer probes and voltage sensed on two inner ones, eliminating the
    contact resistance from the result.

gettering
    Deliberate trapping of metallic contaminants away from the active
    device region, for example by oxygen precipitates in the wafer bulk
    or by damage on the wafer backside.

halo
    A pocket implant of the opposite type to the source/drain, placed at
    an angle around the extension so that the channel doping rises as
    gate length shrinks, suppressing short-channel effects. Also
    "pocket".

HDP-CVD
    High-density-plasma chemical vapour deposition: an inductively coupled
    plasma {term}`CVD` in which simultaneous sputtering by biased argon
    ions keeps narrow gaps open while they fill, used for STI and
    inter-metal dielectric gap fill.

HMDS
    Hexamethyldisilazane, a vapour-phase adhesion promoter that makes the
    wafer surface hydrophobic before resist coating.

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

LDD
    Lightly doped drain: the earlier name for the source/drain
    {term}`extension`.

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

overlay
    The positional error between a printed layer and a previously printed
    layer, measured on dedicated box-in-box or grating targets.

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
    deposition at 300–450 °C on wafers that already carry metal.

Preston equation
    The empirical {term}`CMP` removal-rate law {math}`R = k_p\,P\,v`, in
    which removal rate is proportional to applied pressure and to
    relative pad–wafer velocity.

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

PVD
    Physical vapour deposition: deposition of a film from atoms ejected
    from a solid target, in IC manufacturing almost always by magnetron
    sputtering in argon.

RCA clean
    The two-step wet clean of Kern and Puotinen: {term}`SC-1`
    (NH₄OH/H₂O₂/H₂O) to remove particles and organics, then {term}`SC-2`
    (HCl/H₂O₂/H₂O) to remove metals.

reticle
    The photomask used in a reduction stepper or scanner; it carries one
    field of the layout at 4× or 5× magnification.

RIE
    Reactive-ion etching: plasma etching in which the wafer sits on the
    RF-driven electrode so that energetic ions strike it vertically,
    giving anisotropic profiles.

RTA
    Rapid thermal anneal: a single-wafer anneal in a lamp-heated chamber
    with ramp rates of tens to hundreds of degrees per second and a
    soak of seconds. RTA is one application of {term}`RTP`.

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
    and organic residues.

SC-2
    Standard clean 2 (also HPM): hydrochloric acid, hydrogen peroxide and
    water, typically 1:1:6 at 70–80 °C; removes metallic contamination.

scribe line
    The streets between dies on a wafer that will be cut by the dicing
    saw; used to hold {term}`PCM` structures and alignment targets.

selectivity
    The ratio of the etch rate of the film being removed to the etch rate
    of the mask or of the underlying film that must be preserved.

sheet resistance
    The resistance of a square of a thin film, {math}`R_s = \rho / t`,
    expressed in ohms per square (Ω/□).

silicide
    A compound of a metal with silicon (TiSi₂, CoSi₂, NiSi) formed on
    gates and source/drains to lower their sheet and contact resistance.

SPC
    Statistical process control: charting of in-line measurements against
    control limits so that drift is detected before it affects yield.

spacer
    A dielectric sidewall (nitride or oxide) left on the gate edge by an
    anisotropic etch-back of a conformal film; it offsets the deep
    source/drain implant and the silicide from the channel.

SPM
    Sulfuric-peroxide mixture (also "piranha"): concentrated H₂SO₄ and
    30 % H₂O₂, typically 3:1 to 4:1, self-heating to above 100 °C, used
    to strip and oxidise organic residues.

step coverage
    The ratio of film thickness on the sidewall or bottom of a step to
    that on the flat top surface; a measure of conformality.

STI
    Shallow trench isolation: device isolation formed by etching trenches
    into silicon, filling them with deposited oxide and planarising by
    {term}`CMP`.

stepper
    A projection exposure tool that images one reticle field at a time
    and steps the wafer between exposures. A scanner additionally scans
    the reticle and wafer through a slit during each exposure.

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
    or {term}`PECVD` (around 400 °C).

Vt
    Threshold voltage: the gate voltage at which a MOSFET turns on; set
    by channel doping, oxide thickness and gate work function.

wafer sort
    Functional testing of every die on a wafer with automatic test
    equipment before dicing, in contrast to parametric {term}`e-test`.

WAT
    Wafer acceptance test: the parametric {term}`e-test` whose results
    decide whether a wafer is shipped.

W plug
    A contact or via filled with CVD tungsten over a Ti/TiN liner and
    planarised by {term}`CMP`.
```
