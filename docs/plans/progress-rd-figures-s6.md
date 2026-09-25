# Progress — rd-figures-s6 (W1c, series S6: tips, halos, spacers and source/drain, steps 064–088)

Status: **complete**, awaiting review. 25 figures, one per step, on `topic/rd-figures-s6`.

## What was done

* **Generator** (`tools/gen_figures.py`), each with a selftest:
  * `close_up: [x0, x1]` on a cross-section: draws that window of the series state, enlarged by
    the same factor in x and y, so an implant's tilt survives. The series geometry is not
    touched. `highlight`, `callouts`, `dims` and `top@x` are written in series x and moved by
    the generator; `crop_depth` is in enlarged units; the substrate keeps the series depth, so
    an enlarged block never reaches into the next panel. Heights are interpolated between
    source columns of the same stack, so a sloped wall is not a staircase. A doped region or a
    beam wholly outside the window is dropped (an empty extent no longer reads as
    "everywhere"). Lint: the caption must say "close-up of …".
  * `deposit` with `flat: false` and `where`: a patterned film that follows the surface inside
    its ranges (the thin HV-tip resist, thinner than the gate stacks it covers).
  * Lint rule 16 (an ion label's leader may not cross a material) now counts a polygon only
    inside the clip rectangle of its own drawing: the substrate runs on below the crop, and an
    enlarged one reached into the next panel's label band.
  * `figure-authoring.md` documents both fields.
* **Tokens:** new material `tip-n`, "n-type tip (source/drain extension)", light blue with crossed
  hatching (light `#8cc3f2`, dark `#3b78b8`), in the `silicon` group, so a tip reads apart from
  the deep N⁺ source/drain. `sd-n`'s legend no longer says "n-tip". `palette`: 0 confusable pairs.
  Every SVG was regenerated once: in the existing figures only the CSS variable list changed; the
  legend gains one row.
* **Series** `data/figures/series-tips-sd.yaml`: ops 002–063 copied verbatim from
  `series-poly.yaml` (same ids, same label text), then the module. The header records every
  window and every illustrative choice.
* **25 specs** `data/figures/sd-064-ntm.yaml` … `sd-088-rtad.yaml`, SVGs and paste blocks; each
  block is pasted after the first paragraph of "What this step is". No page in 064–088 has a
  `{dropdown}` right after that paragraph, so the placement rule moves nothing.
* Commits: generator + tokens, the series, then figures 064–067, 068–071, 072–075, a window
  change, 076–079, 080–084, 085–088, this file.

## Geometry and reading choices (all declared in the captions)

* **Slice.** Inherited exactly from S5: 5 V NMOS on the left (no gate in this slice), the field
  with the P⁺ poly resistor, the 1.8 V NMOS with its gate at x 236–260 on the right. The slice
  has no PMOS and no SONOS transistor.
* **Close-up.** The 1.8 V gate is 24 u wide and ends 8 u from the drawing's right edge, too
  small for a tip, halo or spacer. Nine figures (065, 066, 075, 076, 077, 080, 086, 088 on
  x 197–268, z ≈ 3.8; 069 on the 5 V area, x 0–88) are close-ups; the other 16 are the full
  slice. 197 is chosen so the window starts clear of the film the spacer nitride builds against
  the field-oxide shoulder at 188–196.
* **Windows.** NTM open over the 1.8 V NMOS (Table F2b "-" on those rows, the page's
  created-covers reading); HVNTM open over the 5 V NMOS; LDNTM closed over the whole slice (LDASTI
  and LDBHI one-panel, beam stopped, the S5 UPRI precedent); NPCM open over the resistor, the
  slice read as passing through a contact head (rpm.5; **illustrative**, said so on 078 and 079);
  PSDM open over the resistor only (rpm.4, psd.8); NSDM open over both NMOS areas (rpm.6).
* **Doped regions.** Tip (ASTI) from the active edge to the poly edge, self-aligned to the gate;
  its reach under the gate (the page's reading of the 0.01 µm "N Tip (As)") is not drawn. Halo
  (BHI) with the pattern-only channel-implant material (`implant`): under the tip and 5 u under
  each gate edge; the shape is the page's industry-generic description, tagged *typical*.
  HV tip over the whole 5 V area (no gate there). Deep N⁺ from the active edge to the outer foot
  of the spacer oxide. Depth order only (tip < halo < S/D; HV tip deeper than the 1.8 V tip);
  none to scale.
* **Tilts.** 7° on ASTI (pdk-03), 40° on HVASTI (pdk-03; the 23° twist is out of plane, said so),
  0° on PSDI and NSDI (the PDK's "High current" 0°). Vertical, with the reason, on BHI, LDASTI,
  LDBHI (not public / only inferred) and 2PSDI (what it is is not public).
* **Spacers.** Square-dilation conformal film, so SPE leaves slab spacers; they keep a 5 u step
  where the IOX45 sidewall oxide (poly only, from S5) ends. The SPE over-etch clearing the
  stringers at the field-oxide shoulders is an explicit etch confined to the shoulders (the page's
  step 4). The cap is drawn unchanged by SPE. NPCME removes the oxide cap and cuts the nitride
  down to the poly in the window, which shortens the resistor's spacers to the poly top.
* **Thin HVNTM resist** drawn conformal at 10 u against 38 u (0.3 against 1.14 µm, pdk-03).
* **Labels hidden to keep leaders honest** (each declared in its caption): the caps, gate oxides,
  re-oxidation oxide and field oxide throughout (unchanged context; the right-edge gate would
  otherwise stack five dots at the drawing's edge); the halo in full-slice figures (its dot sits
  3–6 u from the tip's); the HV tip under full resist (071 after, 072, 073, 074 before: its over
  route would rise through the resist); the resistor body under the PSDI/2PSDI beams; the silicon
  on 069 (its leader ran beside the trench wall or across the beam); the spacer oxide in 087 after
  and the spacer nitride in 086 after (height budget).

## Per-figure checks

All 25 build with no LINT line; `--check` 368 files, 0 problems. Every figure was looked at in the
harness at desktop and at 400 px in light. Dark was sampled: desktop for 064–066, 069, 076, 077,
079, 080, 081, 086 and 088, 400 px for 076–080 (the dark 400 px tiles of the rest were shot but
not all opened). Checked for each: labels beside their layers, no leader through a film
or along an edge, the highlight on the changed surface only, dark boundaries visible, panels
aligned.

| Figure | View | Notes / compromises |
|---|---|---|
| 064 NTM | full | Resist over 0–176, flat-topped; 1.14 µm and 0.16 µm shadowing cited (pdk-03), not to scale |
| 065 ASTI | close-up | Arrows at 7°; rotation not public, tip drawn symmetric, shadowing not drawn |
| 066 BHI | close-up | Halo tagged *typical*; 20–45° typical (txt-04) in the caption, arrows vertical |
| 067 ASTIS | full | Before panel hides the BHI beam; highlight on the stripped surface |
| 068 HVNTM | full | Conformal thin resist; 0.3/1.14 µm and 0.232 µm cited (pdk-03) |
| 069 HVASTI | close-up of the 5 V area | 40° arrows; twist out of plane; silicon and (lower panel) gate oxide unlabelled |
| 070 HVASTIS | full | HV tip label takes the over route above the resistor (clean, long) |
| 071 LDNTM | full | No window in the slice (pdk-06 names SONOS devices) |
| 072 LDASTI | full, one panel | Beam stopped; 7° only inferred, arrows vertical |
| 073 LDBHI | full, one panel | Beam stopped; tilt not public |
| 074 LDASTIS | full | "every tip and halo in place" |
| 075 TIPRTAD | close-up, one panel | No depth public; nothing moves |
| 076 SPNIT | close-up | The film's step at the top of the poly sidewall is explained |
| 077 SPE | close-up | Slab spacer; stop on oxide is the reference's reading; resistor spacers and stringer clear outside the view, said so |
| 078 NPCM | full | Window over the resistor, illustrative slice choice; npc.4 keeps the gate closed |
| 079 NPCME | full | Cap removed, spacers shortened (not public how much), poly loss not drawn |
| 080 SPOX | close-up | 0.05 µm "oxide spacer" is the page's inference (tag *inferred*) |
| 081 PSDM | full | Resistor-only window (rpm.4, psd.8) |
| 082 PSDI | full, one panel | 0° (pdk-03); p-type body already drawn, so no new overlay: said so |
| 083 2PSDI | full, one panel | Readings listed; arrows vertical as on the first reading |
| 084 PDIS | full | Spacer oxide drawn unchanged (no HF, page's inference) |
| 085 NSDM | full | rpm.6 keeps the resistor covered |
| 086 NSDI | close-up | 0° (pdk-03); deep junction 0.1 µm (pdk-03) not to scale; N⁺ label takes the over route between two arrows (lint clean) |
| 087 NSDIS | full | — |
| 088 RTAD | close-up, one panel | The finished transistor edge; 0.1 µm XJ (pdk-03) not to scale |

Built pages 065, 069, 077 and 086 were shot at 1280 px and 400 px: the figure follows the lead
paragraph, its caption renders with working footnote markers, and prose follows it.

## Gates

`check_steps`, `check_refs`, `check_machines`, `check_materials`, `check_masks`,
`check_papers`, `check_patents`, `check_filings`, `check_inforce`: rc 0. `gen_papers`,
`gen_patents`, `gen_filings`, `gen_index_links`, `gen_steps`, `gen_figures` `--check`: rc 0.
`gen_figures --selftest` OK, `palette` 0. `sphinx-build -W`: rc 0.
`check_preserved.py --base bcccad02`: only ADDED lines (the blocks' own markers, numbers, quotes,
hedges and ids); `git diff bcccad02 -- docs/steps`: 200 lines added, 0 deleted.

## For the readability batch (page-internal points; page prose not changed)

* **S5's field-oxide step, carried forward.** The field oxide still stands 19 u proud of the
  1.8 V surface (S5 kept S4's height; no page says where the step comes down). In S6 it makes the
  spacer nitride build stringers at the shoulders, which the drawing clears with an explicit etch
  (SPE page step 4 supports that the over-etch clears them).
* **The halo has no p-type colour.** It uses the pattern-only channel-implant material, so the
  drawing does not say "p-type"; the label note does. If the owner wants a p-type pocket colour,
  that is a token decision (it must stay apart from `sd-p` and `well-p` for colour-blind readers).
* **079 lead vs step 5.** The lead says NPCME "stops on the poly, leaving bare polysilicon"; step 5
  says a few nanometres of poly loss are unavoidable. Not a contradiction; the figure draws no loss
  and the caption says so.
* **072 lead/category vs open questions.** The category says the 7° tip angle "applies, we infer";
  "Tilt and rotation" says "7° … with twist; two or four rotations, or 0° … — not public"; the
  open questions say whether it is 7° or 0° is not public. Consistent, but the category sentence
  reads more certain than the rest.
* **S6 slice has no PMOS**, so PSDI/2PSDI land only on the resistor head here; a later series that
  needs a PMOS source/drain will need a different slice (a coordinator decision, like S4's).

## Follow-ups (not done here)

* Conformal films use a square structuring element; a round one would give quarter-round spacer
  tops. It would change every existing conformal film, so it was not done.
* The resistor's sidewall re-oxidation (S5 ruling b, `beside:`) is still not drawn; S6's resistor
  spacers stand directly on the resistor sidewall.
