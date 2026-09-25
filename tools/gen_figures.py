#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Generate every figure of this reference from a declarative description.

    uv run python tools/gen_figures.py build            # all specs in data/figures/
    uv run python tools/gen_figures.py build data/figures/sti-006-stie.yaml
    uv run python tools/gen_figures.py --check          # nothing committed is out of date
    uv run python tools/gen_figures.py palette          # colour-vision report on the palette
    uv run python tools/gen_figures.py preview          # tokens -> tmp/figures/preview.html
    uv run python tools/gen_figures.py harness NAME...  # QA pages for tools/shoot.py
    uv run python tools/gen_figures.py --selftest       # every lint rule fires on a bad spec

Where things live
-----------------

* ``data/figures/tokens.json`` — the **only** place colours, the type scale, spacing and
  stroke widths live.  The generator, the lint, the preview page and the reader-facing
  "Figure conventions" page all read it; no value of that kind is written in this file.
* ``data/figures/series-*.yaml`` — one evolving cross-section per process module.  A figure
  is "the state after step N" of its series, so consecutive figures share one geometry.
* ``data/figures/<id>.yaml`` — one figure.
* ``data/figures/myst/<id>.myst.txt`` — the generated block to paste into the page.
* ``docs/_static/figures/<id>.svg`` (follows the operating system), ``<id>.light.svg`` and
  ``<id>.dark.svg`` (forced, swapped in by ``docs/_static/figure-theme.js``).
* ``docs/figure-conventions.md`` — the reader-facing legend, generated from the tokens.

Design rules enforced here (see ``docs/plans/readability/report-D.md``)
----------------------------------------------------------------------

* one palette; no colour may appear in a figure that is not a token;
* in a cross-section all text lives OUTSIDE the drawing, in a right-hand label column;
  leaders are horizontal, or rise vertically out of the drawing to a header band, and never
  cross each other, any text, or a material edge;
* a figure may not say more than its page does: every label carries a ``basis``, every
  number carries a ``cite`` whose footnote key must already be defined on the target page,
  a value that is not public is never drawn to scale, and nothing may cite a patent family
  that ``tools/check_inforce.py`` treats as not certainly expired;
* every SVG carries light and dark values and paints its own ground.

No image library is needed: the advance widths of DejaVu Sans (the widest font in the
stack, so a real rendering is never wider than the lint assumed) are embedded below.
"""

from __future__ import annotations

import argparse
import difflib
import html
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SPEC_DIR = ROOT / "data" / "figures"
MYST_DIR = SPEC_DIR / "myst"
OUT_DIR = DOCS / "_static" / "figures"
CONVENTIONS = DOCS / "figure-conventions.md"
TOKENS_PATH = SPEC_DIR / "tokens.json"

TOK = json.loads(TOKENS_PATH.read_text(encoding="utf-8"))
SP, ST, TY = TOK["space"], TOK["stroke"], TOK["type"]["sizes"]
GROUPS = TOK.get("material-groups", {})
W = SP["canvas-width"]
M = SP["margin"]
DRAW_W = SP["drawing-width"]
GUT = SP["gutter"]
LABEL_X = M + DRAW_W + GUT
LABEL_W = W - M - LABEL_X
LANE0 = M + DRAW_W + SP["lane-inset"]              # x of the first (leftmost) leader lane
LANE_PITCH = SP["lane-pitch"]
LANE_MAX = LABEL_X - SP["lane-end-gap"]            # no lane may sit right of this
LANE_CAPACITY = max(1, int((LANE_MAX - LANE0) // LANE_PITCH) + 1)

BASIS_TAG = {
    "public": None,
    "reading": "our reading",
    "inferred": "inferred",
    "typical": "typical practice",
}
BASIS_MEANING = {
    "public": "the page states this, with a citation; no tag is printed",
    "reading": "this reference's reading of a public drawing or table; the page says so and the caption repeats it",
    "inferred": "inferred on the page from other public facts",
    "typical": "typical practice for this kind of step, not a statement about SKY130",
}
NOT_TO_SCALE = "Not to scale. Thin films are drawn thicker than they are."
# Reader words for the token names of the patterns printed over each colour.
PATTERN_WORDS = {
    "none": "plain colour, no pattern",
    "hatch": "diagonal lines, leaning right",
    "hatch-back": "diagonal lines, leaning left",
    "xhatch": "crossed diagonal lines",
    "hlines": "horizontal lines",
    "vlines": "vertical lines",
    "plus": "small crosses",
    "dots": "small dots",
    "vlines-ink": "vertical ink hatching, no fill of its own",
}
NOT_PUBLIC = "not public"
NO_CHANGE_TITLE = "State at this step (no drawn change)"
ROUTES = ("top", "right", "over")
PROFILES = ("conformal", "gapfill")          # how a blanket deposit meets the topography
NOTE_ORDERS = ("newest", "oldest")
GENERATED_BANNER = "<!-- generated by tools/gen_figures.py; do not edit -->"

KINDS = ("xsection", "flowmap", "stack", "chain")

# --------------------------------------------------------------------------- text metrics
# Advance widths of DejaVu Sans / Sans Bold / Sans Mono, in 1/1000 em, for the characters
# this site uses.  Kerning is deliberately ignored, which can only over-estimate a width.
_WIDTH_CHARS = (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`'
                'abcdefghijklmnopqrstuvwxyz{|}~\xa0\xa1\xa2\xa3\xa5\xa7\xa9\xab\xae\xb0'
                '\xb1\xb2\xb3\xb5\xb7\xbb\xbc\xbd\xd7\xc5\xc4\xd6\xdc\xe0\xe1\xe4\xe7\xe8'
                '\xe9\xea\xed\xf1\xf3\xf6\xf8\xfa\xfcΔΩαβγλ'
                'μσφ–—‘’“”†•…'
                '′″→←↔−≈≠≤≥\xb6₂'
                '₃₄₅\xaa\xba')
_WIDTH_SANS = "318,401,460,838,636,950,780,275,390,390,500,838,318,361,318,337,636,636,636,636,636,636,636,636,636,636,337,337,838,838,838,531,1000,684,686,698,770,632,575,775,752,295,295,656,557,863,748,787,603,787,695,635,611,732,684,989,685,611,685,390,337,390,838,500,500,613,635,550,635,615,352,635,634,278,278,579,278,974,634,612,635,635,411,521,392,634,592,818,592,592,525,636,337,636,838,318,401,636,636,636,500,1000,612,1000,500,838,401,401,636,318,612,969,969,838,684,684,787,732,613,613,613,550,615,615,615,278,634,612,612,612,634,634,684,764,659,638,592,592,636,634,660,500,1000,318,318,518,518,500,590,1000,227,374,838,838,838,838,838,838,838,838,636,401,401,401,401,471,471"
_WIDTH_BOLD = "348,456,521,838,696,1002,872,306,457,457,523,838,380,415,380,365,696,696,696,696,696,696,696,696,696,696,400,400,838,838,838,580,1000,774,762,734,830,683,683,821,837,372,372,775,637,995,837,850,733,850,770,720,682,812,774,1103,771,724,725,457,365,457,838,500,500,675,716,593,716,678,435,716,712,343,343,665,343,1042,712,687,716,716,493,595,478,712,652,924,645,652,582,712,365,712,838,348,456,696,696,696,500,1000,646,1000,500,838,438,438,736,380,646,1035,1035,838,774,774,850,812,675,675,675,593,678,678,678,343,712,687,687,687,712,712,774,850,687,716,681,633,736,779,782,500,1000,380,380,657,657,500,639,1000,264,447,838,838,838,838,838,838,838,838,636,438,438,438,438,564,564"
_MONO_ADVANCE = 602


def _table(src: str) -> dict[str, int]:
    return dict(zip(_WIDTH_CHARS, (int(v) for v in src.split(","))))


_W = {"sans": _table(_WIDTH_SANS), "bold": _table(_WIDTH_BOLD)}
# The widest advance anywhere in the font, not merely in the table above: a glyph the table
# does not carry is measured at that width, so an unknown character can never be measured
# too narrow and slip past the margin check.  UNKNOWN_GLYPHS records them for the lint.
_W_FALLBACK = {"sans": 1735, "bold": 2016}
UNKNOWN_GLYPHS: set[str] = set()


def text_w(s: str, size: float, bold: bool = False, mono: bool = False) -> float:
    """Conservative width estimate; DejaVu Sans is wider than every other font in the stack."""
    if mono:
        return len(s) * _MONO_ADVANCE * size / 1000.0
    key = "bold" if bold else "sans"
    tab, fb = _W[key], _W_FALLBACK[key]
    total = 0
    for ch in s:
        w = tab.get(ch)
        if w is None:
            UNKNOWN_GLYPHS.add(ch)
            w = fb
        total += w
    return total * size / 1000.0 + 0.05 * len(s)


def _greedy(s: str, size: float, maxw: float, bold: bool, mono: bool) -> list[str]:
    lines, cur = [], ""
    for word in s.split(" "):
        trial = (cur + " " + word).strip()
        if cur and text_w(trial, size, bold, mono) > maxw:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + ([cur] if cur else [])


def wrap(s: str, size: float, maxw: float, bold: bool = False, mono: bool = False) -> list[str]:
    """Greedy wrap, then balance: the narrowest width that still gives the same number of
    lines, so that no last line holds one orphaned word."""
    lines = _greedy(s, size, maxw, bold, mono)
    if len(lines) < 2:
        return lines
    lo, hi = maxw / len(lines), maxw
    for _ in range(12):
        mid = (lo + hi) / 2
        if len(_greedy(s, size, mid, bold, mono)) == len(lines):
            hi = mid
        else:
            lo = mid
    return _greedy(s, size, hi, bold, mono)


def f1(v: float) -> str:
    """Fixed one-decimal formatting; -0.0 never appears, so output is byte-stable."""
    return f"{v + 0.0:.1f}" if abs(v) > 5e-3 else "0.0"


def f2(v: float) -> str:
    return f"{v + 0.0:.2f}" if abs(v) > 5e-4 else "0.00"


# --------------------------------------------------------------------------- SVG assembly
class Svg:
    def __init__(self, kind: str, title: str, desc: str):
        self.kind, self.title, self.desc = kind, title, desc
        self.body: list[str] = []
        self.h = 0.0
        self.patterns_used: set[str] = set()
        self.ghosts = False
        self.cuts = False

    def add(self, s: str):
        self.body.append(s)

    def text(self, x, y, s, cls, anchor="start", owner="", mono=""):
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        o = f' data-owner="{owner}"' if owner else ""
        m = f'<tspan class="t-mono">{html.escape(mono)}</tspan>' if mono else ""
        self.add(f'<text x="{f1(x)}" y="{f1(y)}" class="{cls}"{a}{o}>{html.escape(s)}{m}</text>')

    def css(self, theme: str) -> str:
        def block(mode):
            out = []
            for k, v in TOK["theme"].items():
                out.append(f"--{k}:{v[mode]};")
            for k, v in TOK["materials"].items():
                out.append(f"--m-{k}:{v[mode]};")
            for k, v in TOK["phases"].items():
                out.append(f"--ph-{k}:{v[mode]};--pht-{k}:{v['tint'][mode]};")
            return "".join(out)

        fam, mono = TOK["type"]["family"], TOK["type"]["family-mono"]
        base = "dark" if theme == "dark" else "light"
        css = f":root{{{block(base)}}}\n"
        if theme == "auto":
            css += f"@media (prefers-color-scheme: dark){{:root{{{block('dark')}}}}}\n"
        css += f"text{{font-family:{fam};fill:var(--ink)}}\n"
        for name, t in TY.items():
            if isinstance(t, dict):
                css += f".t-{name}{{font-size:{t['size']}px;font-weight:{t['weight']}}}\n"
        css += f".t-mono{{font-family:{mono}}}\n"
        css += ".muted{fill:var(--ink-muted)}.tag{fill:var(--inferred);font-style:italic}.acc{fill:var(--accent)}\n"
        css += f".ground{{fill:var(--bg)}}.mat{{stroke:var(--ink);stroke-width:{ST['outline']};stroke-linejoin:round}}\n"
        css += f".pat{{stroke:var(--ink);stroke-width:{ST['pattern']};opacity:{ST['pattern-opacity']};fill:none}}"
        css += f".patdot{{fill:var(--ink);opacity:{ST['pattern-opacity']}}}\n"
        css += f".leader{{stroke:var(--ink-muted);stroke-width:{ST['leader']};fill:none}}"
        css += (f".halo{{stroke:var(--halo);stroke-width:{ST['leader-halo']};fill:none;"
                f"opacity:{ST['halo-opacity']}}}")
        css += ".dot{fill:var(--ink)}"
        # A faded layer is a hue-free ghost: no fill, a dashed muted outline, no pattern, so
        # it looks the same on every host and cannot be mistaken for any material.
        css += (f".mat.faded{{fill:none;stroke:var(--ink-muted);"
                f"stroke-dasharray:{ST['faded-dash']}}}\n")
        if self.cuts:
            css += (f".cutfill{{fill:var(--bg)}}.cutline{{stroke:var(--ink-muted);"
                    f"stroke-width:{ST['rule']};fill:none;stroke-linejoin:round}}\n")
        if self.ghosts:
            # ... except in a close-up, where the enlargement would turn an empty film into a
            # gap: there it keeps its own fill and loses only its outline and its label.
            css += (f".mat.ghost{{stroke:var(--ink-muted);"
                    f"stroke-dasharray:{ST['faded-dash']}}}\n")
        css += (f".patink{{stroke:var(--ink);stroke-width:{ST['ink-hatch']};"
                f"opacity:{ST['ink-hatch-opacity']};fill:none}}\n")
        css += f".dim{{stroke:var(--ink);stroke-width:{ST['dimension']};fill:none}}.dimhead{{fill:var(--ink)}}"
        css += f".witness{{stroke:var(--ink-muted);stroke-width:{ST['rule']};stroke-dasharray:3 2.5;fill:none}}\n"
        css += f".rule{{stroke:var(--rule);stroke-width:{ST['rule']};fill:none}}"
        css += (f".hl{{stroke:var(--accent);stroke-width:{ST['highlight']};fill:none;"
                f"stroke-linejoin:round;stroke-linecap:round}}")
        css += f".parrow{{stroke:var(--accent);stroke-width:{ST['process-arrow']};fill:none}}.pahead{{fill:var(--accent)}}\n"
        css += f".ion{{stroke:var(--accent);stroke-width:{ST['ion-arrow']};fill:none}}.ionhead{{fill:var(--accent)}}\n"
        css += (f".cbox{{fill:var(--bg);stroke:var(--ink);stroke-width:{ST['chain-box']};"
                f"stroke-linejoin:round}}")
        css += f".carrow{{stroke:var(--ink-muted);stroke-width:{ST['chain-arrow']};fill:none}}.cahead{{fill:var(--ink-muted)}}\n"
        for k, v in TOK["materials"].items():
            css += f".m-{k}{{fill:none}}" if v.get("fill") == "none" else f".m-{k}{{fill:var(--m-{k})}}"
        for k in TOK["phases"]:
            css += f".ph-{k}{{fill:var(--ph-{k})}}.pht-{k}{{fill:var(--pht-{k})}}"
        return css

    def defs(self) -> str:
        pw, po = ST["pattern"], ST["pattern-opacity"]
        p = {
            "hatch": f'<pattern id="p-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line class="pat" x1="0" y1="0" x2="0" y2="6"/></pattern>',
            "hatch-back": '<pattern id="p-hatch-back" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line class="pat" x1="0" y1="0" x2="0" y2="7"/></pattern>',
            "xhatch": '<pattern id="p-xhatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path class="pat" d="M0 0V6M0 0H6"/></pattern>',
            "hlines": '<pattern id="p-hlines" width="6" height="5" patternUnits="userSpaceOnUse"><line class="pat" x1="0" y1="2.5" x2="6" y2="2.5"/></pattern>',
            "vlines": '<pattern id="p-vlines" width="4" height="6" patternUnits="userSpaceOnUse"><line class="pat" x1="2" y1="0" x2="2" y2="6"/></pattern>',
            "plus": '<pattern id="p-plus" width="12" height="12" patternUnits="userSpaceOnUse"><path class="pat" d="M3 1V5M1 3H5M9 7V11M7 9H11"/></pattern>',
            "dots": '<pattern id="p-dots" width="7" height="7" patternUnits="userSpaceOnUse"><circle class="patdot" cx="1.75" cy="1.75" r="0.9"/><circle class="patdot" cx="5.25" cy="5.25" r="0.9"/></pattern>',
            "vlines-ink": '<pattern id="p-vlines-ink" width="3" height="6" patternUnits="userSpaceOnUse"><line class="patink" x1="1.5" y1="0" x2="1.5" y2="6"/></pattern>',
        }
        assert pw and po  # the widths live in the .pat class, from the tokens
        return "".join(p[k] for k in sorted(self.patterns_used))

    def render(self, theme: str) -> str:
        h = math.ceil(self.h)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" '
            f'role="img" data-kind="{self.kind}" data-theme="{theme}">\n'
            f"<title>{html.escape(self.title)}</title>\n<desc>{html.escape(self.desc)}</desc>\n"
            f"<style>\n{self.css(theme)}\n</style>\n<defs>{self.defs()}</defs>\n"
            f'<rect class="ground" x="0" y="0" width="{W}" height="{h}"/>\n' + "\n".join(self.body) + "\n</svg>\n"
        )


def fill_material(svg: Svg, mat: str, points: str, layer: str = "", faded: bool = False,
                  ghost: bool = False) -> None:
    """A material polygon: the token fill, its outline, and its pattern overlay.  A faded
    polygon is context the step does not touch: drawn, but quietly, and never labelled.  In
    a close-up (``ghost``) a faded polygon keeps its fill: enlarged, an empty film reads as a
    void."""
    lid = f' data-layer="{layer}"' if layer else ""
    fd = (" ghost" if ghost else " faded") if faded else ""
    if faded and ghost:
        svg.ghosts = True
    svg.add(f'<polygon class="mat m-{mat}{fd}"{lid} points="{points}"/>')
    pat = TOK["materials"][mat]["pattern"]
    if pat != "none" and not faded:
        svg.patterns_used.add(pat)
        svg.add(f'<polygon fill="url(#p-{pat})" points="{points}"/>')


def expand_materials(names) -> set[str]:
    """``materials:`` accepts a material key or the name of a group in the tokens."""
    out: set[str] = set()
    for n in names or []:
        out |= set(GROUPS[n]) if n in GROUPS else {n}
    return out


SILICON = set(GROUPS.get("silicon", ["si-sub"]))
# a film whose top falls faster than this (dy/dx) at the end of its run ends on a wall
WALL_SLOPE = 1.5


def _dilate_round(tops: list[float], t: float, dx: float) -> list[float]:
    """The upper envelope of a disc of radius ``t`` rolled over the surface ``tops``: a film
    of thickness ``t`` grown normal to the surface everywhere (conformal deposition)."""
    n = len(tops)
    k = int(math.floor(t / dx + 1e-9))
    offs = [(m, math.sqrt(max(0.0, t * t - (m * dx) ** 2))) for m in range(-k, k + 1)]
    out = []
    for i in range(n):
        best = -math.inf
        for m, h in offs:
            j = i + m
            if 0 <= j < n:
                v = tops[j] + h
                if v > best:
                    best = v
        out.append(best)
    return out


def _gapfill(tops: list[float], t: float, dx: float, facet_deg: float = 45.0,
             smooth: float = 0.0) -> list[float]:
    """A gap-filling deposit (HDP-CVD, where sputtering during the deposition faces off every
    outer corner): the film grows ``t`` upward from every surface, filling gaps from the
    bottom, and adds nothing on a vertical wall; over a raised line it rises from the line's
    edges in facets at ``facet_deg``, so it is flat (``t`` thick) over a wide line and peaked
    over a narrow one.  Where the film between lines grows above a low line's top, the two
    merge: the convex corners of ``tops + t`` are cut back to the same facets (the opening of
    ``tops + t`` by a cone of that slope).  Every point keeps a little film.  ``smooth`` (a
    length) then relaxes the surface as a flowing glass would, within the same bounds."""
    n = len(tops)
    f = [v + t for v in tops]
    sl = math.tan(math.radians(facet_deg))
    k = max(1, int(round(t / sl / dx)))
    er = [min(f[j] + abs(j - i) * dx * sl for j in range(max(0, i - k), min(n, i + k + 1)))
          for i in range(n)]
    opened = [max(er[j] - abs(j - i) * dx * sl for j in range(max(0, i - k), min(n, i + k + 1)))
              for i in range(n)]
    # the facets over each raised line: the film is as thick as the distance to the nearest
    # edge where the surface drops away (times the facet's slope), up to t
    hat = []
    for i in range(n):
        e = None
        for m in range(1, k + 1):
            if ((i - m >= 0 and tops[i - m] < tops[i] - GAPFILL_EDGE)
                    or (i + m < n and tops[i + m] < tops[i] - GAPFILL_EDGE)):
                e = m * dx
                break
        hat.append(tops[i] + (t if e is None else min(t, e * sl)))
    floor = [v + min(t, GAPFILL_MIN) for v in tops]
    out = [max(a, b, c) for a, b, c in zip(opened, hat, floor)]
    if smooth > 0:
        w = max(1, int(round(smooth / 2 / dx)))
        for _ in range(2):                      # two box passes: a triangular kernel
            pre = [0.0]
            for v in out:
                pre.append(pre[-1] + v)
            out = [(pre[min(n, i + w + 1)] - pre[max(0, i - w)]) / (min(n, i + w + 1) - max(0, i - w))
                   for i in range(n)]
        out = [min(max(a, b), c) for a, b, c in zip(out, floor, f)]
    return out


# a close-up cut off above the silicon: the caption's declaration, and the least height a film
# must show above the cut to be drawn at all
CUT_PHRASE = "the lower part of the slice is cut off"
CUT_SLIVER = 2.0

# a gap-filling deposit: a drop larger than this (u) is a line's edge; the least film anywhere
GAPFILL_EDGE = 1.0
GAPFILL_MIN = 2.0


# --------------------------------------------------------------------------- process emulator
class XSection:
    """Height-map process emulator.  x: 0..DRAW_W sampled every dx; y up, 0 = the original
    silicon surface.  A column is a bottom-to-top list of ``[layer id, y0, y1]`` segments;
    the segments of a column need not touch, so an undercut leaves a mask hanging."""

    def __init__(self, sub: dict, dx: float = 0.5):
        self.dx = dx
        self.n = int(round(DRAW_W / dx)) + 1
        self.layers: dict[str, dict] = {"sub": sub}
        self.cols = [[["sub", -float(sub["depth"]), 0.0]] for _ in range(self.n)]
        self.overlays: list[dict] = []
        self.ions: list[dict] = []

    def clone(self) -> "XSection":
        c = XSection.__new__(XSection)
        c.dx, c.n = self.dx, self.n
        c.layers = dict(self.layers)
        c.cols = [[list(s) for s in col] for col in self.cols]
        c.overlays = list(self.overlays)
        c.ions = list(self.ions)
        return c

    def window(self, a: float, b: float) -> "XSection":
        """A close-up: the part of this state between x = a and x = b, enlarged by the same
        factor in both directions so that it fills the drawing width.  Angles (an implant's
        tilt, a tapered wall) survive the enlargement; the series geometry is not touched,
        only this copy of it.  Every x in the result is ``(x - a) * zoom``, every y
        ``y * zoom``."""
        z = DRAW_W / (b - a)
        c = XSection.__new__(XSection)
        c.dx, c.n = self.dx, self.n

        def tx(v):
            return (float(v) - a) * z

        def twhere(rng):
            out = []
            for lo, hi in rng:
                lo, hi = max(float(lo), a), min(float(hi), b)
                if hi > lo:
                    out.append([tx(lo), tx(hi)])
            return out

        c.layers = {}
        for lid, layer in self.layers.items():
            lay = dict(layer)
            if lay.get("anchor_x") is not None:
                if a <= float(lay["anchor_x"]) <= b:
                    lay["anchor_x"] = tx(lay["anchor_x"])
                else:
                    lay.pop("anchor_x")
            if lay.get("anchor_y") is not None:
                lay["anchor_y"] = float(lay["anchor_y"]) * z
            if layer.get("op") == "dope":
                if layer.get("where"):
                    # a region wholly outside the window keeps an extent no column matches
                    # (an empty list would read as "everywhere")
                    lay["where"] = twhere(layer["where"]) or [[-2.0, -1.0]]
                for fld in ("y_top", "y_bot", "from_surface", "thickness"):
                    if lay.get(fld) is not None:
                        lay[fld] = float(lay[fld]) * z
            c.layers[lid] = lay
        c.overlays = [c.layers[ov["id"]] for ov in self.overlays]
        c.ions = []
        for op in self.ions:
            o = dict(op)
            o["where"] = twhere(op.get("where") or [[0, DRAW_W]])
            if not o["where"]:
                continue                  # the beam lands outside the close-up
            if o.get("label_x") is not None:
                o["label_x"] = tx(o["label_x"])
            c.ions.append(o)
        c.cols = []
        for i in range(c.n):
            # Between two source columns with the same stack, interpolate the heights, so a
            # sloped wall stays a slope instead of a staircase of enlarged samples.
            f = (a + c.x(i) / z) / self.dx
            j0 = max(0, min(self.n - 1, int(math.floor(f))))
            j1 = min(self.n - 1, j0 + 1)
            t = f - j0
            c0, c1 = self.cols[j0], self.cols[j1]
            if [s[0] for s in c0] == [s[0] for s in c1]:
                src = [[s0[0], s0[1] + (s1[1] - s0[1]) * t, s0[2] + (s1[2] - s0[2]) * t]
                       for s0, s1 in zip(c0, c1)]
            else:
                src = c0 if t < 0.5 else c1
            # The substrate keeps the series' own depth in drawing units: a close-up shows
            # less of it, not a taller block (and the block may not reach the next panel).
            bottom = -float(self.layers["sub"]["depth"])
            c.cols.append([[s[0], max(s[1] * z, bottom), s[2] * z] for s in src
                           if s[2] * z > bottom])
        c.zoom = z
        return c

    def x(self, i):
        return i * self.dx

    def idx(self, x):
        return max(0, min(self.n - 1, int(round(x / self.dx))))

    def top(self, i):
        return self.cols[i][-1][2] if self.cols[i] else -float(self.layers["sub"]["depth"])

    def mat(self, layer):
        return self.layers[layer]["material"]

    def silicon_top(self, i) -> float | None:
        for seg in reversed(self.cols[i]):
            if self.mat(seg[0]) in SILICON:
                return seg[2]
        return None

    def surface_ref(self, i) -> float | None:
        """The silicon surface a doped region is measured from: the silicon top, or, where a
        ``react`` product (a contact silicide) has replaced the top of the silicon, the top of
        that product.  The silicide consumes silicon; it does not push the junction down."""
        col = self.cols[i]
        for k in range(len(col) - 1, -1, -1):
            if self.mat(col[k][0]) in SILICON:
                return col[k][2]
            if (self.layers[col[k][0]].get("op") == "react" and k > 0
                    and self.mat(col[k - 1][0]) in SILICON):
                return col[k][2]
        return None

    def open_ranges(self, lid: str) -> list[list[float]]:
        """The x ranges in which layer ``lid`` is absent: the opening a patterned film makes.
        Deriving an implant's extent from this keeps the mask the single source of truth."""
        missing = [i for i in range(self.n) if not any(sg[0] == lid for sg in self.cols[i])]
        return [[self.x(a), self.x(b)] for a, b in self.runs(missing)]

    def apply(self, op: dict):
        if op["op"] != "ions":
            self.ions = []            # arrows belong to the state of their own step only
        if op.get("where_open"):
            src = op["where_open"]
            op = {k: v for k, v in op.items() if k != "where_open"}
            op["where"] = self.open_ranges(src)
        getattr(self, "op_" + op["op"])(op)

    # ---- operations
    def op_deposit(self, op):
        lid = op["id"]
        self.layers[lid] = op
        t = float(op.get("t", 0))
        where = op.get("where")
        tops = [self.top(i) for i in range(self.n)]
        new = list(tops)
        if "fill_to" in op:                                   # planarising fill
            new = [max(tp, float(op["fill_to"])) for tp in tops]
        elif where and op.get("flat", True):                   # patterned, flat-topped film (resist)
            # One coat: every block of it levels to the same top, set by the highest point
            # it covers anywhere.
            blocks = [[i for i in range(self.n) if a <= self.x(i) <= b] for a, b in where]
            lvl = max((tops[i] for ii in blocks for i in ii), default=0.0) + t
            for ii in blocks:
                for i in ii:
                    new[i] = lvl
        else:                                                  # conformal film
            k = int(round(t / self.dx))
            only = expand_materials(op.get("only_on"))
            if not only:
                # Normal growth: the surface moves out by t along its own normal (a round
                # structuring element), so a film has the same thickness on a sloped wall as
                # on the flat, rounds every outer corner and leaves a hole's bottom open.
                if op.get("profile") == "gapfill":
                    grown = _gapfill(tops, t, self.dx, float(op.get("facet_deg", 45)),
                                     float(op.get("smooth", 0)))
                else:
                    grown = _dilate_round(tops, t, self.dx)
            for i in range(self.n):
                # `flat: false` with `where`: a thin patterned film (a resist thinner than
                # the topography it covers) follows the surface inside its ranges only.
                if where and not any(a <= self.x(i) <= b for a, b in where):
                    continue
                lo, hi = max(0, i - k), min(self.n, i + k + 1)
                if only:
                    if not self.cols[i] or self.mat(self.cols[i][-1][0]) not in only:
                        continue
                    side = [s[2] for j in range(lo, hi) for s in self.cols[j] if self.mat(s[0]) in only]
                    new[i] = max(tops[i] + t, max(side))
                else:
                    new[i] = grown[i]
        for i in range(self.n):
            if new[i] > tops[i] + 1e-9:
                self.cols[i].append([lid, tops[i], new[i]])

    def op_etch(self, op):
        mats = expand_materials(op["materials"])
        if op.get("iso"):
            return self._etch_isotropic(op, mats)
        depth = op.get("depth")
        taper = math.tan(math.radians(float(op.get("taper_deg", 0))))
        r = float(op.get("corner_r", 0))
        for a, b in op.get("where") or [[0, DRAW_W]]:
            for i in range(self.n):
                x = self.x(i)
                if not (a <= x <= b):
                    continue
                lim = math.inf if depth is None else float(depth)
                if depth is not None and (taper or r):
                    u = min(x - a if a > 0 else math.inf, b - x if b < DRAW_W else math.inf)
                    d = float(depth)
                    u0 = (d - r) * taper
                    if u < u0:
                        lim = u / taper if taper else d
                    elif r and u < u0 + r:
                        lim = d - r + math.sqrt(max(0.0, r * r - (r - (u - u0)) ** 2))
                col = self.cols[i]
                while col and lim > 1e-9 and self.mat(col[-1][0]) in mats:
                    seg = col[-1]
                    th = seg[2] - seg[1]
                    if th <= lim + 1e-9:
                        col.pop()
                        lim -= th
                    else:
                        seg[2] -= lim
                        lim = 0

    def _etch_isotropic(self, op, mats):
        """A circular etch front: ``depth`` vertically and ``depth * iso`` laterally, so the
        etch reaches under the edge of a mask and leaves it overhanging."""
        iso = float(op["iso"])
        depth = float(op["depth"])
        where = op.get("where") or [[0, DRAW_W]]
        exposed = [i for i in range(self.n) if any(a <= self.x(i) <= b for a, b in where)]
        if not exposed:
            return
        surf = {}
        for i in exposed:
            col = self.cols[i]
            surf[i] = col[-1][2] if col and self.mat(col[-1][0]) in mats else None
        lat = depth * iso
        for i in range(self.n):
            floor = math.inf
            for j in exposed:
                if surf[j] is None:
                    continue
                d = abs(self.x(i) - self.x(j))
                if d > lat:
                    continue
                drop = depth * math.sqrt(max(0.0, 1.0 - (d / lat) ** 2)) if lat else depth
                floor = min(floor, surf[j] - drop)
            if floor is math.inf:
                continue
            col = self.cols[i]
            keep = []
            for seg in col:
                if self.mat(seg[0]) not in mats or seg[1] >= floor - 1e-9:
                    if self.mat(seg[0]) in mats and seg[1] >= floor - 1e-9:
                        continue
                    keep.append(seg)
                elif seg[2] > floor:
                    keep.append([seg[0], seg[1], floor])
                else:
                    keep.append(seg)
            self.cols[i] = keep

    def op_strip(self, op):
        mats = expand_materials(op["materials"])
        for col in self.cols:
            while col and self.mat(col[-1][0]) in mats:
                col.pop()

    def op_planarise(self, op):
        if "stop_on" in op:
            lvl = max(s[2] for col in self.cols for s in col if self.mat(s[0]) == op["stop_on"])
        else:
            lvl = float(op["to"])
        for col in self.cols:
            while col and col[-1][1] >= lvl - 1e-9:
                col.pop()
            if col and col[-1][2] > lvl:
                col[-1][2] = lvl

    def op_react(self, op):
        """A film reacts with what it stands on and makes a new one: silicide.  The product
        replaces ``t`` of the consumed material and sits under the unreacted film."""
        lid = op["id"]
        self.layers[lid] = op
        consumes = expand_materials(op["consumes"])
        under = expand_materials(op.get("under"))
        t = float(op["t"])
        where = op.get("where") or [[0, DRAW_W]]
        for i in range(self.n):
            if not any(a <= self.x(i) <= b for a, b in where):
                continue
            col = self.cols[i]
            k = len(col) - 1
            if under:
                if k < 1 or self.mat(col[k][0]) not in under:
                    continue
                k -= 1
            if k < 0 or self.mat(col[k][0]) not in consumes:
                continue
            seg = col[k]
            take = min(t, (seg[2] - seg[1]) * 0.9)
            if take <= 1e-9:
                continue
            seg[2] -= take
            col.insert(k + 1, [lid, seg[2], seg[2] + take])

    def op_dope(self, op):
        """A doped region: an overlay clipped to the silicon, so it never appears in a film
        and never floats above the surface."""
        self.layers[op["id"]] = op
        self.overlays.append(op)

    def op_ions(self, op):
        """A recorded implant, drawn as tilted arrows above the surface in the panel that
        names it."""
        self.ions = [op]

    def op_anneal(self, op):
        """A thermal step that changes nothing this drawing can show.  It exists so that the
        step has a state of its own; any movement of a doped region that a page supports is
        drawn by the ``dope`` operations, not here."""
        return None

    # ---- geometry extraction
    def present(self, lid):
        return [i for i in range(self.n) if any(s[0] == lid for s in self.cols[i])]

    def seg(self, i, lid):
        for s in self.cols[i]:
            if s[0] == lid:
                return s
        return None

    def runs(self, idxs):
        out, start, prev = [], None, None
        for i in idxs:
            if start is None:
                start = prev = i
            elif i == prev + 1:
                prev = i
            else:
                out.append((start, prev))
                start = prev = i
        if start is not None:
            out.append((start, prev))
        return out

    def polygons(self, lid):
        polys = []
        for i0, i1 in self.runs(self.present(lid)):
            xs0 = self.x(i0) - (self.dx / 2 if i0 > 0 else 3)
            xs1 = self.x(i1) + (self.dx / 2 if i1 < self.n - 1 else 3)
            bleed = 4 if lid == "sub" else 0
            t0, b0 = self.seg(i0, lid)[2], self.seg(i0, lid)[1] - bleed
            t1, b1 = self.seg(i1, lid)[2], self.seg(i1, lid)[1] - bleed
            top = [(self.x(i), self.seg(i, lid)[2]) for i in range(i0, i1 + 1)]
            bot = [(self.x(i), self.seg(i, lid)[1] - bleed) for i in range(i0, i1 + 1)]
            # A film that ends on a sloped wall (a tapered etch cuts its top down to nothing)
            # ends on that wall: its end edge continues the slope of its top down to its
            # bottom, instead of dropping vertically at the column boundary, so a wall cut
            # through a stack of films is one straight line at any scale.
            wall0 = wall1 = None
            if 0 < i0 < i1:
                sl = (self.seg(i0 + 1, lid)[2] - t0) / self.dx
                if sl > WALL_SLOPE:
                    wall0 = self.x(i0) - min(self.dx, (t0 - b0) / sl)
            if i0 < i1 < self.n - 1:
                sl = (t1 - self.seg(i1 - 1, lid)[2]) / self.dx
                if sl < -WALL_SLOPE:
                    wall1 = self.x(i1) + min(self.dx, (t1 - b1) / -sl)
            top = ([] if wall0 is not None else [(xs0, t0)]) + top + \
                  ([] if wall1 is not None else [(xs1, t1)])
            bot = [(xs0 if wall0 is None else wall0, b0)] + bot + [(xs1 if wall1 is None else wall1, b1)]
            polys.append(_simplify(_corners(top)) + _simplify(_corners(bot))[::-1])
        return polys

    # ---- doped overlays
    def overlay_band(self, ov, i) -> tuple[float, float] | None:
        """(bottom, top) of a doped overlay in column i, clipped to the silicon, or, with
        `host:`, to that deposited film (the whole of its thickness: an overlay in a film
        marks the type of the doping, not a depth profile)."""
        if not any(a <= self.x(i) <= b for a, b in (ov.get("where") or [[0, DRAW_W]])):
            return None
        if ov.get("host"):
            s = self.seg(i, ov["host"])
            return (s[1], s[2]) if s and s[2] - s[1] > 1e-6 else None
        st = self.silicon_top(i)
        if st is None:
            return None
        if ov.get("follow", "surface") == "flat":
            hi, lo = float(ov["y_top"]), float(ov["y_bot"])
        else:
            hi = self.surface_ref(i) - float(ov.get("from_surface", 0))
            lo = hi - float(ov["thickness"])
        hi = min(hi, st)
        lo = max(lo, -float(self.layers["sub"]["depth"]) - 4)
        return (lo, hi) if hi - lo > 1e-6 else None

    def overlay_columns(self, ov) -> list[int]:
        return [i for i in range(self.n) if self.overlay_band(ov, i)]

    def overlay_polygons(self, ov):
        polys = []
        for i0, i1 in self.runs(self.overlay_columns(ov)):
            xs0 = self.x(i0) - (self.dx / 2 if i0 > 0 else 3)
            xs1 = self.x(i1) + (self.dx / 2 if i1 < self.n - 1 else 3)
            bands = {i: self.overlay_band(ov, i) for i in range(i0, i1 + 1)}
            top = ([(xs0, bands[i0][1])] + [(self.x(i), bands[i][1]) for i in range(i0, i1 + 1)]
                   + [(xs1, bands[i1][1])])
            bot = ([(xs0, bands[i0][0])] + [(self.x(i), bands[i][0]) for i in range(i0, i1 + 1)]
                   + [(xs1, bands[i1][0])])
            polys.append(_simplify(top) + _simplify(bot)[::-1])
        return polys

    def ymax(self):
        return max(self.top(i) for i in range(self.n))


def _corners(pts):
    """Where a sampled curve turns sharply between two straight pieces (a flat film top meeting
    a tapered etch wall between two samples), put back the corner the sampling cut off: the
    intersection of the two pieces, if it falls between the samples."""
    def slope(p, q):
        return (q[1] - p[1]) / (q[0] - p[0]) if q[0] != p[0] else math.inf

    out = list(pts[:3])
    for k in range(3, len(pts) - 2):
        a0, a1, b0, b1 = pts[k - 2], pts[k - 1], pts[k], pts[k + 1]
        s_a, s_b = slope(a0, a1), slope(b0, b1)
        if (math.isfinite(s_a) and math.isfinite(s_b) and abs(s_a - s_b) > WALL_SLOPE
                and abs(slope(pts[k - 3], a0) - s_a) < 1e-6 and abs(slope(b1, pts[k + 2]) - s_b) < 1e-6):
            x = (b0[1] - a1[1] + s_a * a1[0] - s_b * b0[0]) / (s_a - s_b)
            if a1[0] + 1e-9 < x < b0[0] - 1e-9:
                out.append((x, a1[1] + s_a * (x - a1[0])))
        out.append(b0)
    out.extend(pts[max(3, len(pts) - 2):])
    return out


def _simplify(pts, tol=0.02):
    out = [pts[0]]
    for k in range(1, len(pts) - 1):
        (x0, y0), (x1, y1), (x2, y2) = out[-1], pts[k], pts[k + 1]
        cross = abs((x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0))
        if cross > tol * max(1.0, math.hypot(x2 - x0, y2 - y0)):
            out.append(pts[k])
    out.append(pts[-1])
    return out


# --------------------------------------------------------------------------- labels
class Label:
    def __init__(self, key, spec):
        self.key = key
        self.spec = spec
        self.basis = spec.get("basis", "public")
        self.route = "right"
        self.hang = "right"           # top-routed labels: text hangs left or right of the riser
        self.ax = self.ay = 0.0       # anchor, SVG coords
        self.ax_min = self.ax_max = 0.0   # the x range the anchor dot may be staggered inside
        self.lo = self.hi = 0.0       # range the anchor may slide in (SVG y), right route only
        self.stub = 0.0
        self.lane = LANE_MAX          # x of this leader's own vertical lane in the gutter
        self.y = 0.0                  # SVG y of the centre of the first line
        self.is_dim = False
        self.dot_y = self.dot_svg = 0.0   # an over-routed label's dot, drawing and SVG y
        self.note_lines = 0
        self.wrap(LABEL_W)

    def wrap(self, maxw):
        self.lines = [("t-label-title", ln)
                      for ln in wrap(self.spec["title"], TY["label-title"]["size"], maxw, bold=True)]
        notes = wrap(self.spec.get("note", ""), TY["label-note"]["size"], maxw)
        self.note_lines = len(notes)
        self.lines += [("t-label-note muted", ln) for ln in notes]
        tag = BASIS_TAG[self.basis]
        if tag:
            self.lines += [("t-label-note tag", ln) for ln in wrap(tag, TY["label-note"]["size"], maxw)]
        self.height = TY["label-title"]["line"] + TY["label-note"]["line"] * (len(self.lines) - 1)


def _own_columns(xs: XSection, lid: str, pres: list[int]) -> list[int]:
    """A film that carries doped overlays (`dope` with `host:`) is drawn as the overlay
    where it is doped, so its own dot belongs where no overlay covers it, if anywhere does."""
    hosted = [ov for ov in xs.overlays if ov.get("host") == lid]
    if not hosted:
        return pres

    def covered(i):
        s = xs.seg(i, lid)
        m = (s[1] + s[2]) / 2
        return any((b := xs.overlay_band(ov, i)) and b[0] <= m <= b[1] for ov in hosted)
    return [i for i in pres if not covered(i)] or pres


def choose_anchor(xs: XSection, lid: str, prefer: str | None, floor_y: float | None = None):
    """Return (route, x, y_lo, y_hi, crossings, x_min) in drawing coordinates (y up).

    ``x_min`` is how far left the anchor dot may be staggered inside its own layer, which is
    what keeps the dots of two thin films that sit a few units apart distinguishable."""
    pres = xs.present(lid)
    pres = _own_columns(xs, lid, pres)
    i0, i1 = xs.runs(pres)[-1]
    inset = min(4.0, (i1 - i0) * xs.dx / 2)
    ir = xs.idx(xs.x(i1) - inset)
    # A film whose right-hand end is a thin wedge (a trench fill meeting a tapered wall) can
    # name where its dot sits instead, so the dot can slide to the label's height rather than
    # pinning the leader against the film above or below.
    if xs.layers[lid].get("anchor_x") is not None:
        ir = max(i0, min(i1, xs.idx(float(xs.layers[lid]["anchor_x"]))))
    s = xs.seg(ir, lid)
    mid = (s[1] + s[2]) / 2
    crossed = {t[0] for j in range(ir + 1, xs.n) for t in xs.cols[j] if t[0] != lid and t[1] < mid < t[2]}
    if floor_y is None:
        floor_y = -float(xs.layers["sub"]["depth"]) + 8
    # Silicon under a doped overlay is drawn as the overlay, so a dot there would sit on the
    # wrong material: keep the dot of a silicon layer to the largest stretch of its column
    # that no overlay covers.
    lo_s, hi_s = s[1], s[2]
    if xs.mat(lid) in SILICON and xs.overlays:
        free = [(lo_s, hi_s)]
        for ov in xs.overlays:
            band = xs.overlay_band(ov, ir)
            if not band:
                continue
            nxt = []
            for a, c in free:
                if band[1] <= a or band[0] >= c:
                    nxt.append((a, c))
                    continue
                if band[0] > a:
                    nxt.append((a, band[0]))
                if band[1] < c:
                    nxt.append((band[1], c))
            free = nxt
        free = [f for f in free if f[1] - max(f[0], floor_y) > 1]
        if free:
            lo_s, hi_s = max(free, key=lambda f: f[1] - max(f[0], floor_y))
    pad = 3.5 if hi_s - lo_s > 9 else (hi_s - lo_s) / 2
    x_min = xs.x(i0) + min(4.0, (i1 - i0) * xs.dx / 2)
    right = ("right", xs.x(ir), max(lo_s + pad, floor_y), hi_s - pad, len(crossed), x_min)
    if xs.layers[lid].get("anchor_y") is not None:       # ... and at what height, inside it
        ya = max(right[2], min(right[3], float(xs.layers[lid]["anchor_y"])))
        right = ("right", right[1], ya, ya, right[4], right[5])
    tops = [i for i in pres if xs.cols[i] and xs.cols[i][-1][0] == lid]
    top = None
    if tops:
        a, b = max(xs.runs(tops), key=lambda r: (r[1] - r[0], r[1]))
        s = xs.seg((a + b) // 2, lid)
        yv = s[2] - min((s[2] - s[1]) / 2, 8.0)
        top = ("top", xs.x((a + b) // 2), yv, yv, 0, xs.x((a + b) // 2))
    if prefer == "top" and top:
        return top
    if prefer in ("right", "over") or right[4] == 0 or top is None:
        return right
    return top


def _visible_run(xs: XSection, ov: dict, i: int) -> tuple[float, float] | None:
    """The longest stretch of column i in which the overlay is what is painted on top: a
    later (higher-z) overlay over part of it hides that part."""
    band = xs.overlay_band(ov, i)
    if not band:
        return None
    ys = [y for y in _frange(band[0], band[1], 0.5) if _visible(xs, i, y, set()) == ov["id"]]
    if not ys:
        return None
    runs, cur = [], [ys[0], ys[0]]
    for y in ys[1:]:
        if y - cur[1] <= 0.51:
            cur[1] = y
        else:
            runs.append(cur)
            cur = [y, y]
    runs.append(cur)
    lo, hi = max(runs, key=lambda r: r[1] - r[0])
    return (lo, hi) if hi - lo >= 1.0 else None


def overlay_anchor(xs: XSection, ov: dict, floor_y: float | None = None):
    cols = xs.overlay_columns(ov)
    i0, i1 = xs.runs(cols)[-1]
    inset = min(4.0, (i1 - i0) * xs.dx / 2)
    ir = xs.idx(xs.x(i1) - inset)
    if ov.get("anchor_x") is not None:
        ir = max(i0, min(i1, xs.idx(float(ov["anchor_x"]))))
    x_min = xs.x(i0) + min(4.0, (i1 - i0) * xs.dx / 2)
    lo, hi = xs.overlay_band(ov, ir)
    vis = _visible_run(xs, ov, ir)
    if vis is None or vis[1] - vis[0] < min(6.0, (hi - lo) * 0.8):
        # Partly painted over: take the column, nearest the right-hand end, where the most
        # of the overlay shows, and keep the dot there (no stagger into the covered part).
        best = None
        for j in sorted(cols, key=lambda c: -c):
            v = _visible_run(xs, ov, j)
            if v and (best is None or v[1] - v[0] > best[1][1] - best[1][0] + 1.0):
                best = (j, v)
        if best:
            ir, vis = best
            lo, hi = vis
            x_min = xs.x(ir)
    elif vis:
        lo, hi = vis
    pad = 3.5 if hi - lo > 9 else (hi - lo) / 2
    if floor_y is not None:
        lo = max(lo, floor_y - pad)
    if ov.get("anchor_y") is not None:      # a thin band: keep the leader clear of the film above
        ya = max(lo + pad, min(hi - pad, float(ov["anchor_y"])))
        return ("right", xs.x(ir), ya, ya, 0, x_min)
    return ("right", xs.x(ir), min(lo + pad, hi - pad), hi - pad, 0, x_min)


def _frange(a: float, b: float, step: float) -> list[float]:
    n = int(math.floor((b - a) / step + 1e-9))
    return [a + k * step for k in range(n + 1)] if b >= a else []


def _visible(xs: XSection, i: int, y: float, hidden: set) -> str | None:
    """The layer a reader sees at column i and height y: overlays are painted over films,
    in their ``z`` order, so the top-most one that covers the point wins."""
    for ov in sorted(xs.overlays, key=lambda o: float(o.get("z", 0)), reverse=True):
        if ov["id"] in hidden:
            continue
        band = xs.overlay_band(ov, i)
        if band and band[0] <= y <= band[1]:
            return ov["id"]
    for s in xs.cols[i]:
        if s[0] not in hidden and s[1] <= y <= s[2]:
            return s[0]
    return None


def _named(xs: XSection, lid: str, i: int, y: float, hidden: set) -> bool:
    return _visible(xs, i, y, hidden) == lid


def _traverse(xs: XSection, lid: str, x: float, y: float, hidden: set,
              ion_xs=(), ion_tail=None, step: int = 4) -> float:
    """How far a horizontal leader from (x, y) to the right-hand edge runs through materials
    other than the layer it names.  Crossing an ion arrow costs more than any budget."""
    total = 0.0
    for i in range(xs.idx(x) + 1, xs.n, step):
        v = _visible(xs, i, y, hidden)
        if v is not None and v != lid:
            total += step * xs.dx
    for xv in ion_xs or ():
        if xv > x and ion_tail is not None and xs.top(xs.idx(xv)) < y < ion_tail + 1:
            total += 1000.0
    return total


def _film_run(xs: XSection, lid: str, x: float, y: float, hidden: set, step: int = 2) -> float:
    """The longest stretch a horizontal leader from (x, y) to the right-hand edge runs inside
    ONE other film: leaving its layer sideways into the next film and running along inside
    it, a leader reads as that film's boundary, even where its total traverse is short."""
    best, cur, cur_lid = 0.0, 0.0, None
    for i in range(xs.idx(x) + 1, xs.n, step):
        v = _visible(xs, i, y, hidden)
        if v is not None and v != lid and v == cur_lid:
            cur += step * xs.dx
        else:
            cur_lid, cur = v, (step * xs.dx if v is not None and v != lid else 0.0)
        best = max(best, cur)
    return best


def _edge_run(xs: XSection, lid: str, x: float, y: float, hidden: set, step: int = 4,
              highlight=()) -> float:
    """How far a horizontal leader from (x, y) runs within the edge clearance of, and
    parallel to, a horizontal material boundary or the accent trace of a highlight (which
    sits `highlight-offset` above the surface and reads as a line just as much)."""
    clear = SP["edge-clearance"]
    total = 0.0
    for i in range(xs.idx(x) + 1, xs.n, step):
        edges = [xs.top(i)]
        if any(a <= xs.x(i) <= b for a, b in highlight):
            hl = xs.top(i) + SP["highlight-offset"]
            if abs(hl - y) < (SP["highlight-clearance"] if y > hl else SP["edge-clearance"]):
                total += step * xs.dx
                continue
        edges += [e for s in xs.cols[i] if s[0] not in hidden for e in (s[1], s[2])]
        for ov in xs.overlays:
            if ov["id"] in hidden:
                continue
            band = xs.overlay_band(ov, i)
            if band:
                edges += list(band)
        if any(abs(e - y) < clear for e in edges):
            total += step * xs.dx
    return total


def _plan_over(xs: XSection, lid: str, hidden: set, ion_xs, ion_tail, ion_cx, tops_x, taken=()):
    """Where a label's dot should sit when no horizontal leader to the right can avoid other
    materials: the column of the layer with the least material above it, clear of walls,
    ion arrows and the risers of labels above the drawing.  Returns (x, dot y, over height)."""
    ov = xs.layers[lid] if xs.layers[lid].get("op") == "dope" else None
    cols = xs.overlay_columns(ov) if ov else _own_columns(xs, lid, xs.present(lid))
    if not cols:
        return None
    colset = set(cols)
    k8 = int(round(8 / xs.dx))
    best = None
    for i in cols[::4]:
        x = xs.x(i)
        if any((j not in colset) for j in range(max(0, i - k8), min(xs.n, i + k8 + 1))):
            continue                                        # too near the layer's own end
        if x < 8 or x > DRAW_W - 8:
            continue                                        # too near the drawing's edge
        if any(abs(x - tx) < 10 for tx in taken):
            continue                                        # another label already rises here
        if ov:
            lo, hi = xs.overlay_band(ov, i)
        else:
            s = xs.seg(i, lid)
            lo, hi = s[1], s[2]
        oy = hi - min(3.5, (hi - lo) / 2)
        h = max(xs.top(j) for j in range(i, xs.n)) + SP["over-gap"]
        # the riser may not run beside a wall or a mask edge anywhere on its way up
        k12 = int(round(12 / xs.dx))
        near = [j for j in (i - k12, i - k8, i - k8 // 2, i + k8 // 2, i + k8, i + k12) if 0 <= j < xs.n]
        if any(_visible(xs, j, yv, hidden) != _visible(xs, i, yv, hidden)
               for yv in _frange(oy, h, 2.0) for j in near):
            continue
        if any(abs(x - xv) < 10 for xv in ion_xs or ()):
            continue
        if ion_cx is not None and (abs(x - ion_cx) < 8 or x < ion_cx):
            continue                                        # its over-run would cut the beam's label
        if any(x < tx + 8 for tx, _ in tops_x):
            continue
        burden = xs.top(i) - hi
        if ion_tail is not None and any(xv > x - 6 for xv in ion_xs or ()):
            h = max(h, ion_tail + SP["over-gap"])
        key = (burden, -x)
        if best is None or key < best[0]:
            best = (key, (x, oy, h))
    return best[1] if best else None


def _halo_runs(xs: XSection, l: "Label", hidden: set, sx, sy, y0) -> list:
    """The stretches of a leader, in SVG coordinates, where it crosses a material other
    than the one it names: only those get a halo, never the leader's own layer."""
    out = []

    def add_run(pts):
        run = None
        for (px, py), other in pts:
            if other:
                run = run or [px, py]
                end = (px, py)
            elif run:
                out.append((run[0], run[1], end[0], end[1]))
                run = None
        if run:
            out.append((run[0], run[1], end[0], end[1]))

    x_d = l.ax - M
    if l.route == "over":
        ys = _frange(y0 - l.dot_svg, y0 - l.ay, 0.5)
        i = xs.idx(x_d)
        pts = []
        for yv in ys:
            v = _visible(xs, i, yv, hidden)
            pts.append(((l.ax, sy(yv)), v is not None and v != l.key))
        add_run(pts)
    else:
        yv = y0 - l.ay
        pts = []
        for i in range(xs.idx(x_d) + 1, xs.n):
            v = _visible(xs, i, yv, hidden)
            pts.append(((sx(xs.x(i)), l.ay), v is not None and v != l.key))
        add_run(pts)
    return [r for r in out if abs(r[2] - r[0]) + abs(r[3] - r[1]) > 0.9]


def _geometry(xs: XSection, hidden: set) -> tuple:
    """What a panel draws, apart from arrows and labels: every film and overlay polygon."""
    out = []
    for lid, layer in xs.layers.items():
        if lid in hidden or layer.get("op") in ("dope", "ions"):
            continue
        out.append((lid, tuple(tuple((round(a, 2), round(b, 2)) for a, b in poly)
                               for poly in xs.polygons(lid))))
    for ov in xs.overlays:
        if ov["id"] not in hidden:
            out.append((ov["id"], tuple(tuple((round(a, 2), round(b, 2)) for a, b in poly)
                                        for poly in xs.overlay_polygons(ov))))
    return tuple(out)


def _anchor_errs(xs: XSection, lid: str) -> list[str]:
    """A named anchor has to fall at least 3 u inside its own layer; a value that the tool
    would silently clamp to the layer's edge is a mistake in the spec."""
    layer = xs.layers[lid]
    ax, ay = layer.get("anchor_x"), layer.get("anchor_y")
    if ax is None and ay is None:
        return []
    is_ov = layer.get("op") == "dope"
    cols = xs.overlay_columns(layer) if is_ov else xs.present(lid)
    if not cols:
        return []
    out = []
    if ax is not None:
        inside = [i for i in cols if all(j in set(cols) for j in (xs.idx(xs.x(i) - 3), xs.idx(xs.x(i) + 3)))]
        if xs.idx(float(ax)) not in inside:
            out.append(f"{lid}: anchor_x {ax} is not at least 3 u inside the layer")
        i = xs.idx(float(ax))
    else:
        i = cols[-1]
    if ay is not None and i in set(cols):
        lo, hi = xs.overlay_band(layer, i) if is_ov else xs.seg(i, lid)[1:]
        if not lo + 3 <= float(ay) <= hi - 3:
            out.append(f"{lid}: anchor_y {ay} is not at least 3 u inside the layer "
                       f"({lo:.0f}..{hi:.0f} at that x)")
    return out


def _isotonic(z):
    """Pool-adjacent-violators: the non-decreasing sequence closest (least squares) to z."""
    blocks = []
    for v in z:
        blocks.append([v, 1])
        while len(blocks) > 1 and blocks[-2][0] > blocks[-1][0]:
            v2, n2 = blocks.pop()
            v1, n1 = blocks.pop()
            blocks.append([(v1 * n1 + v2 * n2) / (n1 + n2), n1 + n2])
    return [v for v, n in blocks for _ in range(n)]


def _place_right(rights: list[Label], floor: float) -> float:
    gap = SP["label-gap"]
    off, acc = [], 0.0
    for l in rights:
        off.append(acc)
        acc += l.height + gap
    des = [min(l.hi, max(l.lo, l.lo + 6)) for l in rights]
    ys = list(des)
    for _ in range(8):
        z = _isotonic([d - o for d, o in zip(des, off)])
        ys = [max(v, floor) + o for v, o in zip(z, off)]
        des = [min(l.hi, max(l.lo, yv)) for l, yv in zip(rights, ys)]
    for l, yv in zip(rights, ys):
        l.y = yv
        l.ay = min(l.hi, max(l.lo, yv))
    return ys[-1] + rights[-1].height + gap


def layout_right_labels(labels: list[Label], floor: float) -> float:
    """Right-routed labels: keep the order of the layers, keep a minimum distance, and move
    each label as little as possible from a height at which its leader is horizontal.  The
    anchor then slides inside its layer to meet the label.

    An anchor that has slid can end up out of order with its neighbour, so the placement is
    repeated with the labels re-ordered by where their anchors actually landed until that
    order is stable.  Each leader is then given its own vertical lane in the gutter and, when
    two anchors end up within a few units of each other, its dot is staggered left inside its
    own layer, so that no two leaders ever run side by side.  Returns the y below the last
    label."""
    rights = sorted([l for l in labels if l.route in ("right", "over")],
                    key=lambda l: ((l.lo + l.hi) / 2, l.key))
    if not rights:
        return floor
    bottom = _place_right(rights, floor)
    for _ in range(4):
        order = sorted(rights, key=lambda l: (l.ay, l.key))
        if [l.key for l in order] == [l.key for l in rights]:
            break
        rights = order
        bottom = _place_right(rights, floor)
    # Lanes right to left: the topmost label takes the lane nearest its text, so a leader's
    # last horizontal run never meets the lane of a label below it.  (Proof by the ordering:
    # a lane further left belongs to a label further down, whose vertical span lies below.)
    n = len(rights)
    for i, l in enumerate(rights):
        k = min(n - 1 - i, LANE_CAPACITY - 1)
        l.lane = LANE0 + k * LANE_PITCH
    # Push the anchors apart in y as far as each layer allows, so that two leaders never
    # leave the drawing on the same line...
    clear = SP["leader-lane-clearance"] + 1
    for i in range(1, len(rights)):
        prev, l = rights[i - 1], rights[i]
        if l.ay - prev.ay < clear:
            l.ay = min(l.hi, prev.ay + clear)
    for i in range(len(rights) - 2, -1, -1):
        nxt, l = rights[i + 1], rights[i]
        if nxt.ay - l.ay < clear:
            l.ay = max(l.lo, nxt.ay - clear)
    # ... and, where a layer is too thin for that, stagger the dots sideways instead, so the
    # two dots are visibly on different films.
    step = SP["anchor-stagger"]
    cluster = 0
    for i, l in enumerate(rights):
        if i and abs(rights[i - 1].ay - l.ay) < SP["anchor-separation-y"]:
            cluster += 1
        else:
            cluster = 0
        if cluster:
            l.ax = max(l.ax_min, l.ax - cluster * step)
    _untangle_lanes(rights)
    return bottom


def _right_leader(l: Label, lane: float) -> list:
    """The segments of a right-column leader, as ``draw_label`` draws them: an over-route
    first rises from its dot to its crossing height."""
    rise = [((l.ax, l.dot_svg), (l.ax, l.ay))] if l.route == "over" else []
    return rise + [((l.ax, l.ay), (lane, l.ay)), ((lane, l.ay), (lane, l.y)), ((lane, l.y), (LABEL_X - 4, l.y))]


def _untangle_lanes(rights: list[Label]) -> None:
    """The right-to-left lane order cannot cross only while every label sits at or below
    its anchor.  Where labels have been pushed up above their anchors (thin films crowded at
    the surface, under a tall label above them) two leaders can cross; the lanes are then
    re-dealt, keeping the default order where it works and otherwise taking the first order,
    nearest the default, in which no two leaders cross."""
    import itertools

    clear = SP["leader-lane-clearance"]

    def beside(a, b):
        (a0, a1), (b0, b1) = a, b
        if abs(a0[1] - a1[1]) < 0.01 and abs(b0[1] - b1[1]) < 0.01 and abs(a0[1] - b0[1]) < clear:
            return min(a0[0], a1[0]) < max(b0[0], b1[0]) - 1 and min(b0[0], b1[0]) < max(a0[0], a1[0]) - 1
        if abs(a0[0] - a1[0]) < 0.01 and abs(b0[0] - b1[0]) < 0.01 and abs(a0[0] - b0[0]) < clear:
            return min(a0[1], a1[1]) < max(b0[1], b1[1]) - 1 and min(b0[1], b1[1]) < max(a0[1], a1[1]) - 1
        return False

    def crossings(lanes):
        segs = [_right_leader(l, ln) for l, ln in zip(rights, lanes)]
        return sum(1 for i in range(len(segs)) for j in range(i + 1, len(segs))
                   if any(_cross(a, b) or beside(a, b) for a in segs[i] for b in segs[j]))

    lanes = [l.lane for l in rights]
    if len(rights) < 2 or len(rights) > 7 or not crossings(lanes):
        return
    best = None
    for perm in itertools.permutations(sorted(lanes, reverse=True)):
        c = crossings(perm)
        if best is None or c < best[0]:
            best = (c, perm)
        if c == 0:
            break
    for l, ln in zip(rights, best[1]):
        l.lane = ln


def draw_label(svg: Svg, l: Label, x_draw_right: float, halo):
    """A right-routed leader is orthogonal: out of the dot, along its own lane, into the
    label.  An over-routed one first rises out of its layer and crosses above the surface.
    A top-routed one rises out of the drawing into the header band.  ``halo`` is the list of
    (x0, y0, x1, y1) stretches where the leader crosses a material other than its own."""
    first = TY["label-title"]["size"]
    y = l.y + first * 0.35
    top = l.route == "top"
    tx = LABEL_X if not top else (l.ax + l.stub + 9 if l.hang == "right" else l.ax + l.stub - 9)
    for cls, s in l.lines:
        svg.text(tx, y, s, cls, anchor="end" if top and l.hang == "left" else "start", owner=l.key)
        y += TY["label-note"]["line"]
    if not top:
        for hx0, hy0, hx1, hy1 in halo or []:
            svg.add(f'<path class="halo" d="M{f1(hx0)} {f1(hy0)}L{f1(hx1)} {f1(hy1)}"/>')
        d = (f"M{f1(l.ax)} {f1(l.dot_svg)}V{f1(l.ay)}" if l.route == "over" else f"M{f1(l.ax)} {f1(l.ay)}")
        d += f"H{f1(l.lane)}"
        if abs(l.y - l.ay) > 0.05:
            d += f"V{f1(l.y)}"
        d += f"H{f1(LABEL_X - 4)}"
    else:
        rx = l.ax + l.stub
        d = (f"M{f1(l.ax)} {f1(l.ay)}" + (f"H{f1(rx)}" if l.stub else "")
             + f"V{f1(l.y)}H{f1(rx + (5 if l.hang == 'right' else -5))}")
    svg.add(f'<path class="leader" data-owner="{l.key}" d="{d}"/>')
    if not l.is_dim:
        cy = l.dot_svg if l.route == "over" else l.ay
        svg.add(f'<circle class="dot" data-owner="{l.key}" cx="{f1(l.ax)}" '
                f'cy="{f1(cy)}" r="{ST["anchor-dot-radius"]}"/>')


# --------------------------------------------------------------------------- cross-section
def eval_y(xs: XSection, expr, errs: list[str] | None = None):
    """A y position: a number, ``top@<x>`` (the top surface at x) or ``si@<x>`` (the silicon
    surface at x).  An expression that does not parse is a lint error, never a traceback."""
    if isinstance(expr, (int, float)):
        return float(expr)
    m = re.fullmatch(r"top@([\d.]+)", str(expr))
    if m:
        return xs.top(xs.idx(float(m.group(1))))
    m = re.fullmatch(r"si@([\d.]+)", str(expr))
    if m:
        v = xs.silicon_top(xs.idx(float(m.group(1))))
        return 0.0 if v is None else v
    msg = f"bad y expression {expr!r}; use a number, top@<x> or si@<x>"
    if errs is None:
        raise ValueError(msg)
    errs.append(msg)
    return 0.0


def _ion_tails(xs: XSection, ion_xs, tail_y: float, tilt: float) -> list[float]:
    """The x (drawing units) at which each arrow of a beam starts, at the beam's tail height."""
    return sorted(xv + (tail_y - xs.top(xs.idx(xv)) - SP["ion-arrow-gap"]) * math.tan(tilt)
                  for xv in ion_xs)


def _snap_to_gap(cx: float, tails: list[float]) -> float:
    """Move a beam label's riser to the middle of the gap between the two arrow tails it
    falls between, so that the riser and an arrow never read as one line."""
    if not tails:
        return cx
    if cx < tails[0]:
        return cx if tails[0] - cx >= 6 else max(2.0, tails[0] - 8)
    if cx > tails[-1]:
        return cx if cx - tails[-1] >= 6 else tails[-1] + 8
    for a, b in zip(tails, tails[1:]):
        if a <= cx <= b:
            return (a + b) / 2
    return cx


def ion_arrow(hx: float, hy: float, rise: float, tilt: float) -> tuple[str, str]:
    """One implant arrow in SVG coordinates: its tip at (hx, hy) on the surface, its tail
    ``rise`` drawing units higher and, for a tilted beam, to the right.  The head's base sits
    on the tail side of the tip, so the arrow points the way the ions travel, and the shaft
    ends at that base."""
    ux, uy = math.sin(tilt), -math.cos(tilt)        # screen direction from the tip to the tail
    run = rise / max(math.cos(tilt), 1e-6)
    tail = (hx + run * ux, hy + run * uy)
    bx, by = hx + 6.0 * ux, hy + 6.0 * uy           # centre of the head's base
    px, py = -uy, ux
    shaft = f"M{f1(tail[0])} {f1(tail[1])}L{f1(bx)} {f1(by)}"
    head = (f"M{f1(hx)} {f1(hy)}L{f1(bx + 3.0 * px)} {f1(by + 3.0 * py)}"
            f"L{f1(bx - 3.0 * px)} {f1(by - 3.0 * py)}Z")
    return shaft, head


def _zoom_panel(p: dict, a: float, z: float) -> dict:
    """A panel's positions moved into a close-up's coordinates: x -> (x - a) * z, a height
    -> y * z, and ``top@x`` / ``si@x`` re-aimed at the moved x."""
    import copy
    q = copy.deepcopy(p)

    def tx(v):
        return (float(v) - a) * z

    def ty(expr):
        if isinstance(expr, (int, float)):
            return float(expr) * z
        m = re.fullmatch(r"(top|si)@([\d.]+)", str(expr))
        return f"{m.group(1)}@{tx(m.group(2)):.2f}" if m else expr

    if q.get("highlight"):
        q["highlight"]["where"] = [[max(0.0, tx(lo)), min(float(DRAW_W), tx(hi))]
                                   for lo, hi in q["highlight"].get("where", [])
                                   if tx(hi) > 0 and tx(lo) < DRAW_W]
    for c in q.get("callouts", []):
        if "x" in c:
            c["x"] = tx(c["x"])
        if "y" in c:
            c["y"] = ty(c["y"])
    for d in q.get("dims", []):
        d["x"] = tx(d["x"])
        d["y0"], d["y1"] = ty(d["y0"]), ty(d["y1"])
        if d.get("witness"):
            d["witness"] = [[tx(lo), tx(hi)] for lo, hi in d["witness"]]
    return q


def series_states(series: dict, dx: float = 0.5) -> tuple[dict[str, XSection], dict[str, str]]:
    """The state after every step of a series, plus the step at which each layer appeared.
    ``dx`` is the sampling step (finer for a close-up)."""
    states = {}
    born: dict[str, str] = {"sub": "000"}
    xs = XSection(series["substrate"], dx)
    states["000"] = xs.clone()
    for op in series["ops"]:
        xs.apply(op)
        if op.get("id") and op["id"] not in born:
            born[op["id"]] = str(op["step"])
        states[str(op["step"])] = xs.clone()          # state after the LAST op of that step
    return states, born


def build_xsection(spec: dict, series: dict, errs: list[str]) -> Svg:
    svg = Svg("xsection", spec["alt"], spec["alt"])
    # `routes`: this figure's own leader routes for some layers, over the series' (a close-up
    # crops a film at the drawing's edge, where a series `over` route would rise up the edge).
    if spec.get("routes"):
        ids = {o.get("id") for o in series["ops"]}
        series = dict(series, ops=[dict(o) for o in series["ops"]])
        for lid, rt in spec["routes"].items():
            if rt not in ROUTES + ("auto",) or lid not in ids:
                errs.append(f"routes: {lid!r}: {rt!r} is not a layer of the series and a route "
                            f"({', '.join(ROUTES)} or auto)")
                continue
            for o in series["ops"]:
                if o.get("id") == lid:
                    if rt == "auto":
                        o.pop("route", None)        # the generator chooses, panel by panel
                    else:
                        o["route"] = rt
    close = spec.get("close_up")
    fine = 1
    if (isinstance(close, list) and len(close) == 2
            and all(isinstance(v, (int, float)) for v in close) and close[1] - close[0] > 0):
        # a close-up enlarges every sample: build the series on a finer grid, so a sloped wall
        # is still drawn at the full-slice resolution and does not turn into a staircase
        fine = max(1, math.ceil(DRAW_W / (close[1] - close[0])))
    states, born = series_states(series, 0.5 / fine)
    last_step = max(states)
    series_ids = {"sub"} | {o["id"] for o in series["ops"] if o.get("id")}
    newest = series.get("note_order") == "newest"

    def state(step):
        key = str(step)
        if not re.fullmatch(r"\d{3}", key):
            errs.append(f"state_after {step!r} is not a three-digit step number")
            return states["000"], "000"
        if key > last_step:
            errs.append(f"state_after {key!r} is beyond the last step of the series ({last_step})")
            return states[last_step], last_step
        keys = [k for k in sorted(states) if k <= key]
        return states[keys[-1]], keys[-1]

    # A close-up draws a window of the series state, enlarged; the panels, their
    # highlights, callouts and dimensions are written in the series' own x, and moved here.
    close = spec.get("close_up")
    zoom = 1.0
    if close is not None:
        if (not isinstance(close, list) or len(close) != 2
                or not all(isinstance(v, (int, float)) for v in close)
                or not 0 <= close[0] < close[1] <= DRAW_W or close[1] - close[0] < 40):
            errs.append(f"close_up must be [x0, x1] inside 0..{DRAW_W}, at least 40 u wide; "
                        f"got {close!r}")
            close = None
        else:
            zoom = DRAW_W / (close[1] - close[0])

    def view(xs):
        return xs.window(close[0], close[1]) if close else xs

    panels = [_zoom_panel(p, close[0], zoom) if close else p for p in spec["panels"]]
    sub_depth = float(series["substrate"]["depth"])
    depth = float(spec.get("crop_depth", sub_depth))
    # a drawing cut off above the silicon: a close-up of the upper films, or (S9 on) a full
    # slice of a tall back-end stack whose lower part would push the figure past its height
    cut = depth < 0
    floor_y = -depth + 8
    X0 = M
    x_right = X0 + DRAW_W
    y = M
    seen: set[str] = set()
    # A layer keeps one route for the whole figure, and may be labelled from above only when
    # it is the top-most layer in every panel that labels it: a reader should not meet the
    # same layer labelled two different ways in one picture.
    routes: dict[str, str] = {}
    for p in panels:
        st_pre = view(state(p["state_after"])[0])
        hid = (set(p.get("hide_layers", [])) | set(p.get("hide_labels", []))
               | set(p.get("dim_layers", [])))
        for lid, layer in st_pre.layers.items():
            if lid in hid or "label" not in layer or layer.get("op") in ("dope", "ions"):
                continue
            if not st_pre.present(lid):
                continue
            nat = choose_anchor(st_pre, lid, layer.get("route"), -float(spec.get("crop_depth", sub_depth)) + 8)[0]
            routes[lid] = "top" if nat == "top" and routes.get(lid, "top") == "top" else "right"
    for pi, p in enumerate(panels):
        if "crop_depth" in p:
            errs.append("crop_depth belongs to the figure, not to a panel; move it up one level")
        st, st_step = state(p["state_after"])
        st = view(st)
        # A hidden overlay is not drawn, so nothing may be anchored around it either.
        hidden_ov = set(p.get("hide_layers", []))
        if any(ov["id"] in hidden_ov for ov in st.overlays):
            st = st.clone()
            st.overlays = [ov for ov in st.overlays if ov["id"] not in hidden_ov]
        ions = st.ions if p.get("show_ions", True) and st.ions else []
        # ---- ion beam: evenly spaced arrows sharing one tail height, so it reads as a beam
        ion_xs: list[float] = []
        ion_windows = []
        ion_tilt = 0.0
        ion_tail_y = None
        if ions:
            ion_tilt = math.radians(float(ions[0].get("tilt_deg", 0)))
            pitch = float(ions[0].get("pitch", SP["ion-arrow-pitch"]))
            ion_windows = ions[0].get("where") or [[0, DRAW_W]]
            for a, b in ion_windows:
                n = max(1, int(round((b - a) / pitch)))
                gapx = (b - a) / n
                for k in range(n):
                    ion_xs.append(a + gapx * (k + 0.5))
            if ion_xs:
                ion_tail_y = (max(st.top(st.idx(xv)) for xv in ion_xs)
                              + SP["ion-arrow-gap"] + SP["ion-arrow-length"] * math.cos(ion_tilt))
        ymax = max([st.ymax()] + ([ion_tail_y] if ion_tail_y is not None else [])) + 4
        draw_h = ymax + depth
        dims, notes = p.get("dims", []), p.get("callouts", [])
        labels: list[Label] = []
        hidden = set(p.get("hide_layers", []))
        # Faded layers: context this step does not touch, drawn quietly and not labelled, so
        # that a module with many doped regions stays inside the label budget.  The layer
        # this step made may never be one of them.
        faded = set(p.get("dim_layers", []))
        for lid in sorted(faded):
            if lid not in series_ids:
                errs.append(f"panel {pi + 1}: dim_layers names no layer of this series ({lid!r})")
            elif born.get(lid) == st_step and st_step == str(p["state_after"]):
                errs.append(f"panel {pi + 1}: {lid!r} is the layer this step made; "
                            "it must be labelled, not faded")
        for lid in st.layers:
            if lid not in hidden:
                errs += _anchor_errs(st, lid)
        material_labels: list[Label] = []
        for lid, layer in st.layers.items():
            if lid in hidden or lid in faded or lid in p.get("hide_labels", []) or "label" not in layer:
                continue
            if layer.get("op") == "dope":
                if not st.overlay_columns(layer):
                    continue
            elif layer.get("op") == "ions":
                continue
            elif not st.present(lid):
                continue
            lspec = {**layer["label"], **p.get("labels", {}).get(lid, {})}
            if pi > 0 and lid in seen and lid not in p.get("labels", {}):
                lspec = {k: v for k, v in lspec.items() if k != "note"}   # a note is given once per figure
            seen.add(lid)
            lab = Label(lid, lspec)
            labels.append(lab)
            material_labels.append(lab)
        # ---- the noted-label budget: at most N labels in a panel carry a note, the layer
        # this step made first, then the rest in layer order.  A series that declares
        # `note_order: newest` puts a label the figure overrides for this panel second and
        # then the most recently made layers, which are what a page in the middle of a long
        # module is about.  Everything else prints its title only, which is what keeps the
        # label column from growing taller than the drawing beside it.
        cap = int(SP["max-noted-labels"])
        noted = [l for l in material_labels if l.spec.get("note")]
        if len(noted) > cap:
            if newest:
                noted.sort(key=lambda l: (born.get(l.key) != st_step, l.key not in p.get("labels", {}),
                                          -list(st.layers).index(l.key)))
            else:
                noted.sort(key=lambda l: (born.get(l.key) != st_step, list(st.layers).index(l.key)))
            for l in noted[cap:]:
                l.spec = {k: v for k, v in l.spec.items() if k != "note"}
                l.wrap(LABEL_W)
        if len(material_labels) > int(SP["max-labelled-layers"]):
            errs.append(f"panel {pi + 1} labels {len(material_labels)} layers; "
                        f"at most {int(SP['max-labelled-layers'])}")
        for k, dm in enumerate(dims):
            labels.append(Label(f"dim{k}", dm["label"]))
            labels[-1].is_dim = True
        for k, c in enumerate(notes):
            labels.append(Label(f"callout{k}", c["label"]))
        ion_label = None
        if ions and ions[0].get("label") and ion_xs:
            ion_label = Label("ions", ions[0]["label"])
            labels.append(ion_label)
        # ---- anchors in drawing coordinates; routes
        geo = {}
        for lab in labels:
            if lab.is_dim:
                dm = dims[int(lab.key[3:])]
                ya, yb = eval_y(st, dm["y0"], errs), eval_y(st, dm["y1"], errs)
                geo[lab.key] = ("top", dm["x"], (ya + yb) / 2, (ya + yb) / 2, 0, dm["x"])
                lab.stub = float(dm.get("stub", 12))
            elif lab.key.startswith("callout"):
                c = notes[int(lab.key[7:])]
                if "y" not in c:
                    errs.append(f"callout {c.get('label', {}).get('title', '?')!r} has no y:")
                yv = eval_y(st, c.get("y", 0), errs)
                geo[lab.key] = ("top", c.get("x", DRAW_W / 2), yv, yv, 0, c.get("x", DRAW_W / 2))
            elif lab is ion_label:
                mid = max(ion_windows, key=lambda w: w[1] - w[0])
                cx = float(ions[0].get("label_x", (mid[0] + mid[1]) / 2))
                cx = _snap_to_gap(cx, _ion_tails(st, ion_xs, ion_tail_y, ion_tilt))
                geo[lab.key] = ("top", cx, ion_tail_y, ion_tail_y, 0, cx)
            elif st.layers[lab.key].get("op") == "dope":
                geo[lab.key] = overlay_anchor(st, st.layers[lab.key], floor_y)
            else:
                geo[lab.key] = choose_anchor(st, lab.key, st.layers[lab.key].get("route"), floor_y)
            want = routes.get(lab.key, geo[lab.key][0])
            if want != geo[lab.key][0] and not lab.is_dim and not lab.key.startswith("callout") \
                    and lab is not ion_label:
                geo[lab.key] = choose_anchor(st, lab.key, want, floor_y)
            lab.route = geo[lab.key][0]
            routes.setdefault(lab.key, lab.route)
        # ---- traverses: a right-column leader may not run a long way through other
        # materials, nor alongside a material edge, where it reads as a film boundary.  Keep
        # its dot to the heights at which it does neither; where there are none, the leader
        # leaves its layer upwards and crosses to the label column above the surface.
        tops_x = [(geo[l.key][1] + l.stub, geo[l.key][2]) for l in labels if l.route == "top"]
        ion_cx = geo["ions"][1] if ion_label is not None else None
        overs = []
        for lab in labels:
            if lab.route != "right" or lab.is_dim or lab.key.startswith("callout") or lab is ion_label:
                continue
            layer = st.layers[lab.key]
            if layer.get("route") == "right":
                continue
            r, gx, glo, ghi, nc, gxmin = geo[lab.key]
            ok = [] if layer.get("route") == "over" else [
                yv for yv in _frange(glo, ghi, 1.0)
                if _traverse(st, lab.key, gx, yv, hidden, ion_xs, ion_tail_y) <= SP["max-leader-traverse"]
                and _film_run(st, lab.key, gx, yv, hidden) <= SP["max-film-traverse"]
                and _edge_run(st, lab.key, gx, yv, hidden,
                             highlight=(p.get("highlight") or {}).get("where", []))
                <= SP["max-edge-run"]]
            if ok:
                runs_ok, cur = [], [ok[0]]
                for yv in ok[1:]:
                    if yv - cur[-1] <= 1.01:
                        cur.append(yv)
                    else:
                        runs_ok.append(cur)
                        cur = [yv]
                runs_ok.append(cur)
                best = max(runs_ok, key=lambda rr: (rr[-1] - rr[0], rr[-1]))
                geo[lab.key] = (r, gx, best[0], best[-1], nc, gxmin)
                continue
            plan = _plan_over(st, lab.key, hidden, ion_xs, ion_tail_y, ion_cx, tops_x,
                              [pl[0] for _l, pl in overs])
            if plan is None:
                continue                      # nothing better; the SVG lint will say so
            overs.append((lab, plan))
        # Over-runs: the leftmost crosses highest, so it passes above the risers of the others.
        h_prev = None
        # A riser that has to climb through an ion beam gets a lane: the arrows within
        # three quarters of a pitch of it are left out, so it cannot be read as one more arrow.
        if ion_xs and overs:
            pitch_eff = min((b - a for a, b in zip(sorted(ion_xs), sorted(ion_xs)[1:])),
                            default=SP["ion-arrow-pitch"])
            lane = 0.75 * pitch_eff
            keep = []
            for xv in ion_xs:
                x_tail = xv + (ion_tail_y - st.top(st.idx(xv)) - SP["ion-arrow-gap"]) * math.tan(ion_tilt)
                lo_x, hi_x = min(xv, x_tail), max(xv, x_tail)
                if any(lo_x - lane < ox < hi_x + lane for _l, (ox, _oy, _b) in overs):
                    continue
                keep.append(xv)
            ion_xs = keep
        # Over-runs: the leftmost crosses highest, so it passes above the risers of the others;
        # two of them stay a clear 11 u apart, so they never read as a pair of lines.
        for lab, (ox, oy, base) in sorted(overs, key=lambda t: -t[1][0]):
            h = base if h_prev is None else max(base, h_prev + 11)
            h_prev = h
            lab.route = "over"
            lab.dot_y = oy
            geo[lab.key] = ("over", ox, h, h, 0, ox)
            ymax = max(ymax, h + 4)
        draw_h = ymax + depth
        # ---- header band for the top-routed labels
        max_top = int(SP["max-header-callouts"])
        tops = sorted([l for l in labels if l.route == "top"], key=lambda l: (geo[l.key][1] + l.stub, l.key))
        if len(tops) > max_top:
            errs.append(f"panel {pi + 1} has {len(tops)} labels routed above the drawing; "
                        f"at most {max_top}")
            for l in tops[max_top:]:
                l.route = "right"
                routes[l.key] = "right"
            tops = tops[:max_top]
        rxs = [X0 + geo[l.key][1] + l.stub for l in tops]
        for k, lab in enumerate(tops):
            rx = rxs[k]
            lab.hang = "left" if (len(tops) == 2 and k == 0) or (len(tops) == 1 and rx > X0 + DRAW_W * 0.6) else "right"
            width = min(200.0, rx - 9 - M) if lab.hang == "left" else min(230.0, W - M - rx - 9)
            # The left one of two hangs left of its riser; when the riser is so close to the
            # canvas edge that the text would be squeezed into a narrow column, it hangs right
            # instead, in the gap before the second riser, if that gap is wider.
            if len(tops) == 2 and k == 0 and width < SP["min-hang-width"] and rxs[1] - rx - 18 > width:
                lab.hang = "right"
                width = min(230.0, rxs[1] - rx - 18)
            lab.wrap(width)
            if lab.note_lines > int(SP["max-callout-note-lines"]):
                errs.append(f"the label above the drawing, {lab.spec['title']!r}, wraps to "
                            f"{lab.note_lines} note lines; at most "
                            f"{int(SP['max-callout-note-lines'])} — shorten the note")
        band_h = max([l.height for l in tops], default=0)
        # A header band taller than the drawing it labels reads as a caption with a picture
        # attached; route those labels to the right-hand column instead.
        if tops and band_h > draw_h:
            for l in tops:
                if l.is_dim:
                    continue
                l.route = "right"
                routes[l.key] = "right"
                l.wrap(LABEL_W)
                gx = geo[l.key][1]
                yv = geo[l.key][2]
                geo[l.key] = ("right", gx, yv - 3.5, yv + 3.5, 0, gx)
            tops = [l for l in tops if l.route == "top"]
            band_h = max([l.height for l in tops], default=0)
        tlines = wrap(p["title"], TY["panel-title"]["size"], W - 2 * M, bold=True)
        title_y = y + TY["panel-title"]["size"]
        for ln in tlines:
            svg.text(M, title_y, ln, "t-panel-title")
            title_y += TY["panel-title"]["line"]
        title_y -= TY["panel-title"]["line"]
        band_top = title_y + 12
        y_draw_top = band_top + band_h + (SP["header-band-gap"] if tops else 0)
        y0 = y_draw_top + ymax                              # SVG y of the datum

        def sx(v):
            return X0 + v

        def sy(v):
            return y0 - v

        # ---- drawing
        cid = f"clip{pi + 1}"
        i_clip = len(svg.body)
        svg.add(f'<clipPath id="{cid}"><rect x="{X0}" y="{f1(y_draw_top)}" width="{DRAW_W}" height="{f1(draw_h)}"/></clipPath>')
        svg.add(f'<g class="drawing" data-rect="{X0},{f1(y_draw_top)},{DRAW_W},{f1(draw_h)}" clip-path="url(#{cid})">')
        for lid, layer in st.layers.items():
            if layer.get("op") in ("dope", "ions") or lid in hidden:
                continue
            for poly in st.polygons(lid):
                # a close-up cut off above the silicon: a film that shows less than
                # CUT_SLIVER above the cut is a sliver of something the figure does not draw
                if cut and max(py for _px, py in poly) < -depth + CUT_SLIVER:
                    continue
                fill_material(svg, layer["material"], " ".join(f"{f2(sx(px))},{f2(sy(py))}" for px, py in poly),
                              lid, faded=lid in faded, ghost=zoom > 1)
        # Doped overlays are painted in order of ``z`` (default 0), then of creation: a thin
        # channel implant made before a well is still drawn over that well.
        for ov in sorted(st.overlays, key=lambda o: float(o.get("z", 0))):
            if ov["id"] in hidden:
                continue
            for poly in st.overlay_polygons(ov):
                if cut and max(py for _px, py in poly) < -depth + CUT_SLIVER:
                    continue
                fill_material(svg, ov["material"], " ".join(f"{f2(sx(px))},{f2(sy(py))}" for px, py in poly),
                              ov["id"], faded=ov["id"] in faded, ghost=zoom > 1)
        if cut:
            # the cut is drawn as a break: a zigzag edge with the page's ground below it, so the
            # figure itself shows that the slice goes on further down
            zz = [(0.0, -depth + 1.0)]
            xv, k = 0.0, 0
            while xv < DRAW_W:
                xv = min(float(DRAW_W), xv + 4.0)
                k += 1
                zz.append((xv, -depth + (3.5 if k % 2 else 1.0)))
            pts = " ".join(f"{f2(sx(px))},{f2(sy(py))}" for px, py in zz)
            svg.cuts = True
            svg.add(f'<polygon class="cutfill" points="{pts} {f2(sx(DRAW_W))},{f2(sy(-depth - 4))} '
                    f'{f2(sx(0))},{f2(sy(-depth - 4))}"/>')
            svg.add(f'<polyline class="cutline" points="{pts}"/>')
        # The accent traces the surface this step made, drawn just clear of it, so that it
        # marks a 5 u film instead of covering it.
        off = SP["highlight-offset"]
        for a, b in (p.get("highlight") or {}).get("where", []):
            cols = list(range(st.idx(a), st.idx(b) + 1))
            ys = [st.top(i) + off for i in cols]
            # A range that ends on a wall would otherwise poke the trace ``off`` past the top
            # corner of the wall: end the wall's segment at the material's own top instead.
            if len(cols) > 1 and abs(st.top(cols[0]) - st.top(cols[1])) > off:
                ys[0] = st.top(cols[0]) if st.top(cols[0]) > st.top(cols[1]) else ys[0]
            if len(cols) > 1 and abs(st.top(cols[-1]) - st.top(cols[-2])) > off:
                ys[-1] = st.top(cols[-1]) if st.top(cols[-1]) > st.top(cols[-2]) else ys[-1]
            pts = _simplify([(sx(st.x(i)), sy(y)) for i, y in zip(cols, ys)])
            svg.add('<polyline class="hl" points="' + " ".join(f"{f2(px)},{f2(py)}" for px, py in pts) + '"/>')
        # ---- ion arrows
        if ions and ion_xs:
            gap, tilt = SP["ion-arrow-gap"], ion_tilt
            for xv in ion_xs:
                tipy = st.top(st.idx(xv)) + gap
                shaft, head = ion_arrow(sx(xv), sy(tipy), ion_tail_y - tipy, tilt)
                svg.add(f'<path class="ion" d="{shaft}"/>')
                svg.add(f'<path class="ionhead" d="{head}"/>')
        svg.add("</g>")
        for k, dm in enumerate(dims):
            ya, yb, xd = eval_y(st, dm["y0"], errs), eval_y(st, dm["y1"], errs), sx(dm["x"])
            for a, b in dm.get("witness", []):
                svg.add(f'<path class="witness" d="M{f1(sx(a))} {f1(sy(yb))}H{f1(sx(b))}"/>')
            ah, aw = ST["arrowhead"]["length"], ST["arrowhead"]["width"] / 2
            svg.add(f'<path class="dim" d="M{f1(xd)} {f1(sy(ya) - ah + 1)}V{f1(sy(yb) + ah - 1)}"/>')
            svg.add(f'<path class="dimhead" d="M{f1(xd)} {f1(sy(ya) - 1.2)}l{-aw} {-ah}h{2 * aw}z"/>')
            svg.add(f'<path class="dimhead" d="M{f1(xd)} {f1(sy(yb))}l{-aw} {ah}h{2 * aw}z"/>')
        # ---- label positions
        for lab in labels:
            r, gx, glo, ghi, ncross, gxmin = geo[lab.key]
            lab.ax = sx(gx)
            lab.ax_min = sx(gxmin)
            lab.lo, lab.hi = sy(ghi), sy(glo)                # SVG y grows downwards
            lab.ay = (lab.lo + lab.hi) / 2
            if lab.route == "top":
                lab.y = band_top + TY["label-title"]["size"] * 0.5
            if lab.route == "over":
                lab.dot_svg = sy(lab.dot_y)
        bottom = layout_right_labels(labels, y_draw_top + 7)
        # A label column taller than the drawing would leave its lowest labels hanging below
        # the picture on long leaders: show more of the substrate instead, so that every
        # label starts beside the drawing (presentation only; no geometry moves).
        lowest = max([l.y - TY["label-title"]["size"] * 0.45 for l in labels
                      if l.route in ("right", "over")], default=0.0)
        want = lowest - y_draw_top - SP["max-label-drop"] + 1
        room = ymax + sub_depth
        if want > draw_h + 1 and room > draw_h and not cut:
            new_h = min(want, room)
            for k in (i_clip, i_clip + 1):
                svg.body[k] = svg.body[k].replace(f'{f1(draw_h)}"', f'{f1(new_h)}"', 1)
            draw_h = new_h
        for lab in labels:
            halo = []
            if lab.route in ("right", "over"):
                halo = _halo_runs(st, lab, hidden, sx, sy, y0)
            # A riser that climbs across the accent trace cuts it: the trace is broken for
            # the leader's width, so the two never read as one bent line.
            if lab.route == "over":
                xd = lab.ax - M
                for a, b in (p.get("highlight") or {}).get("where", []):
                    if a <= xd <= b:
                        yh = sy(st.top(st.idx(xd)) + SP["highlight-offset"])
                        if min(lab.dot_svg, lab.ay) < yh < max(lab.dot_svg, lab.ay):
                            halo.append((lab.ax, yh - 3.0, lab.ax, yh + 3.0))
            draw_label(svg, lab, x_right, halo)
        y = max(y_draw_top + draw_h, bottom - SP["label-gap"]) + 6
        # ---- process arrow between panels
        if pi < len(panels) - 1 and "arrow" in spec:
            a = spec["arrow"]
            cx = X0 + 22
            ya0 = y + 6
            ah, aw = 9, 5.5
            note = wrap(a.get("note", ""), TY["label-note"]["size"], W - M - cx - 16)
            ya1 = ya0 + max(30, 16 + 15 * len(note))
            svg.add(f'<path class="parrow" d="M{cx} {f1(ya0)}V{f1(ya1 - ah + 1)}"/>')
            svg.add(f'<path class="pahead" d="M{cx} {f1(ya1)}l{-aw} {-ah}h{2 * aw}z"/>')
            svg.text(cx + 16, ya0 + 11, a["title"], "t-label-title acc")
            for k, ln in enumerate(note):
                svg.text(cx + 16, ya0 + 11 + 15 * (k + 1), ln, "t-label-note muted")
            y = ya1 + 14
        else:
            y += SP["panel-gap"] - 6
    sigs = [_geometry(state(pnl["state_after"])[0], set(pnl.get("hide_layers", []))) for pnl in panels]
    if len(panels) == 2 and sigs[0] == sigs[1]:
        errs.append("the two panels have identical geometry; draw one panel with "
                    "no_drawn_change: true")
    if spec.get("no_drawn_change") and panels:
        st_now, k_now = state(panels[0]["state_after"])
        earlier = [k for k in sorted(states) if k < k_now]
        if earlier and _geometry(states[earlier[-1]], set(panels[0].get("hide_layers", []))) != sigs[0]:
            errs.append(f"no_drawn_change, but the state at step {k_now} differs from step "
                        f"{earlier[-1]}; draw it before and after")
    shows_ions = any(state(pnl["state_after"])[0].ions and pnl.get("show_ions", True) for pnl in panels)
    if shows_ions and "tilt" not in spec.get("caption", "").lower():
        errs.append("the figure draws an ion beam but the caption says nothing about the tilt "
                    "(say whether the page gives one)")
    films = any(lid != "sub" for pnl in panels for lid in state(pnl["state_after"])[0].layers
                if state(pnl["state_after"])[0].present(lid) and lid != "sub")
    if close:
        # A close-up says so on the figure itself, not only in the caption below it.
        what = spec.get("close_up_name", "part of the slice")
        tail = "; the lower part of the slice is not drawn" if cut else ""
        for ln in wrap(f"Close-up of {what}, enlarged about {zoom:.1f}\u00d7{tail}.",
                       TY["label-title"]["size"], W - 2 * M, bold=True):
            svg.text(M, y + 10, ln, "t-label-title")
            y += TY["label-title"]["line"]
    elif cut:
        # a full slice cut off above the silicon says so on the figure too
        svg.text(M, y + 10, "The lower part of the slice is not drawn.", "t-label-title")
        y += TY["label-title"]["line"]
    svg.text(M, y + 10, NOT_TO_SCALE if films else NOT_TO_SCALE.split(".")[0] + ".",
             "t-label-note muted")
    svg.h = y + 10 + M
    if svg.h > SP["max-figure-height"]:
        errs.append(f"the figure is {math.ceil(svg.h)} u tall; at most {SP['max-figure-height']} u "
                    "— drop a note or split it into two figures")
    return svg


# --------------------------------------------------------------------------- flow map
def build_flowmap(spec: dict) -> Svg:
    svg = Svg("flowmap", spec["alt"], spec["alt"])
    total = spec["total_steps"]
    X_PH, X_BR, X_S0, X_S1, X_F1, X_T = M, 76, 82, 102, 130, 140
    TW = W - M - X_T
    y = M + TY["label-note"]["size"]
    svg.text(X_PH, y, spec["strip_header"], "t-label-note muted")
    svg.text(X_T, y, spec["rows_header"], "t-label-note muted")
    y += 10
    top = y
    rows = []
    RANGE_W = text_w("000–000", TY["label-title"]["size"]) + 10
    for m in spec["modules"]:
        name = wrap(m["name"], TY["label-title"]["size"], TW - RANGE_W, bold=True)
        n = m["last"] - m["first"] + 1
        rng = f"{m['first']:03d}–{m['last']:03d}"
        nm = len(m["masks"])
        l3a = f"{n} steps · {nm} mask{'s' if nm != 1 else ''}:"
        l3 = ", ".join(m["masks"])
        split = text_w(l3a + " ", TY["label-note"]["size"]) + text_w(l3, TY["mono"]["size"], mono=True) > TW
        h = 7 + TY["label-title"]["line"] * len(name) + TY["label-note"]["line"] * (2 if split else 1) + 5
        rows.append(dict(m=m, name=name, rng=rng, l3a=l3a, l3=l3, h=h, n=n, split=split))
    H = sum(r["h"] for r in rows)
    ry = top
    for k, r in enumerate(rows):
        m = r["m"]
        s0 = top + H * (m["first"] - 1) / total
        s1 = top + H * m["last"] / total
        ph = m["phase"]
        if k % 2 == 0:
            svg.add(f'<polygon class="pht-{ph}" points="{X_S1},{f1(s0)} {X_F1},{f1(ry)} {W - M},{f1(ry)} '
                    f'{W - M},{f1(ry + r["h"])} {X_F1},{f1(ry + r["h"])} {X_S1},{f1(s1)}"/>')
        svg.add(f'<path class="rule" d="M{X_S1} {f1(s0)}L{X_F1} {f1(ry)}H{W - M}"/>')
        if k == len(rows) - 1:
            svg.add(f'<path class="rule" d="M{X_S1} {f1(s1)}L{X_F1} {f1(ry + r["h"])}H{W - M}"/>')
        svg.add(f'<rect class="mat ph-{ph}" x="{X_S0}" y="{f1(s0)}" width="{X_S1 - X_S0}" height="{f1(s1 - s0)}"/>')
        ty = ry + 7 + TY["label-title"]["size"] * 0.8
        svg.text(W - M - 4, ty, r["rng"], "t-label-note muted", anchor="end")
        for ln in r["name"]:
            svg.text(X_T, ty, ln, "t-label-title")
            ty += TY["label-title"]["line"]
        if r["split"]:
            svg.text(X_T, ty - 1, r["l3a"], "t-label-note muted")
            svg.text(X_T, ty - 1 + TY["label-note"]["line"], "", "t-label-note muted", mono=r["l3"])
        else:
            svg.text(X_T, ty - 1, r["l3a"] + " ", "t-label-note muted", mono=r["l3"])
        ry += r["h"]
    for ph in spec["phases"]:
        p0 = top + H * (ph["first"] - 1) / total
        p1 = top + H * ph["last"] / total
        svg.add(f'<path class="leader" d="M{X_BR + 3} {f1(p0 + 1.5)}H{X_BR}V{f1(p1 - 1.5)}H{X_BR + 3}"/>')
        cy = (p0 + p1) / 2
        svg.text(X_PH, cy - 2, TOK["phases"][ph["id"]]["label"], "t-label-title")
        svg.text(X_PH, cy + 13, f"{ph['last'] - ph['first'] + 1} steps", "t-label-note muted")
    y = top + H + 18
    for ln in wrap(spec["footer"], TY["label-note"]["size"], TW):
        svg.text(X_T, y, ln, "t-label-note muted")
        y += TY["label-note"]["line"]
    svg.h = y - TY["label-note"]["line"] + M
    return svg


# --------------------------------------------------------------------------- stack chart
def build_stack(spec: dict) -> Svg:
    """A to-scale layer chart with a vertical axis.  Every thickness is a cited public
    number: the lint refuses a layer whose basis is anything but ``public``."""
    svg = Svg("stack", spec["alt"], spec["alt"])
    axis = spec["axis"]
    layers = spec["layers"]
    total = sum(float(l["t"]) for l in layers)
    barw = SP["stack-bar-width"]
    tickw = SP["stack-tick-length"]
    axis_text_w = max(text_w(f"{v:g}", TY["label-note"]["size"])
                      for v in (0, total, float(axis["tick"]))) + 2
    x_bar0 = M + axis_text_w + SP["stack-axis-gap"] + tickw
    barw = min(barw, LABEL_X - GUT - x_bar0)      # the label column and its gutter stay clear
    x_bar1 = x_bar0 + barw
    scale = SP["stack-max-height"] / total
    y = M + TY["panel-title"]["size"]
    svg.text(M, y, spec["title"], "t-panel-title")
    y += 14
    hdr = wrap(f'{axis["label"]} ({axis["unit"]})', TY["label-note"]["size"], W - 2 * M)
    for ln in hdr:
        svg.text(M, y, ln, "t-label-note muted")
        y += TY["label-note"]["line"]
    y_top = y + 4
    y_base = y_top + total * scale

    def sy(v):                      # v in axis units above the datum
        return y_base - v * scale

    svg.add(f'<g class="drawing" data-rect="{f1(x_bar0)},{f1(y_top)},{f1(barw)},{f1(total * scale)}">')
    acc = 0.0
    bands = []
    for l in layers:
        t = float(l["t"])
        bands.append((acc, acc + t))
        pts = (f"{f2(x_bar0)},{f2(sy(acc + t))} {f2(x_bar1)},{f2(sy(acc + t))} "
               f"{f2(x_bar1)},{f2(sy(acc))} {f2(x_bar0)},{f2(sy(acc))}")
        fill_material(svg, l["material"], pts, l.get("id", ""))
        acc += t
    svg.add("</g>")
    # axis
    svg.add(f'<path class="dim" d="M{f1(x_bar0 - tickw)} {f1(sy(0))}H{f1(x_bar0)}"/>')
    tick = float(axis["tick"])
    k = 0
    while tick * k <= total + 1e-9:
        v = tick * k
        svg.add(f'<path class="witness" d="M{f1(x_bar0 - tickw)} {f1(sy(v))}H{f1(x_bar1)}"/>')
        svg.text(x_bar0 - tickw - 3, sy(v) + TY["label-note"]["size"] * 0.35,
                 f"{v:g}", "t-label-note muted", anchor="end")
        k += 1
    # labels in the right-hand column
    labels = []
    for l, (lo, hi) in zip(layers, bands):
        if not l.get("label"):
            continue
        lab = Label(l.get("id", l["material"]), l["label"])
        span = (hi - lo) * scale
        pad = min(3.5, span / 2)
        lab.ax = x_bar1
        lab.ax_min = x_bar0 + 4
        lab.lo, lab.hi = sy(hi) + pad, sy(lo) - pad
        lab.ay = (lab.lo + lab.hi) / 2
        labels.append(lab)
    bottom = layout_right_labels(labels, y_top)
    for lab in labels:
        draw_label(svg, lab, x_bar1, False)
    y = max(y_base + 12, bottom - SP["label-gap"]) + 6
    for ln in wrap(spec["footer"], TY["label-note"]["size"], W - 2 * M):
        svg.text(M, y + 10, ln, "t-label-note muted")
        y += TY["label-note"]["line"]
    svg.h = y + 10 + M - TY["label-note"]["line"]
    return svg


# --------------------------------------------------------------------------- chain
def build_chain(spec: dict) -> Svg:
    """Vertical boxes joined by arrows, with optional side branches.  Text sits inside the
    boxes, which are painted in the page ground: a chain has no drawing area in the sense a
    cross-section has, so the "no text in the drawing" rule does not apply to it."""
    svg = Svg("chain", spec["alt"], spec["alt"])
    nodes = spec["nodes"]
    pad = SP["chain-box-padding"]
    arrow = SP["chain-arrow-length"]
    has_branch = any(n.get("branch") for n in nodes)
    full = W - 2 * M
    main_w = full * (1 - SP["chain-branch-fraction"]) - SP["chain-branch-gutter"] if has_branch else full
    branch_w = full - main_w - SP["chain-branch-gutter"]
    x0 = M
    x1 = M + main_w
    y = M + TY["panel-title"]["size"]
    svg.text(M, y, spec["title"], "t-panel-title")
    y += 12

    def box(bx, bw, node, cls):
        lines = [("t-label-title", ln)
                 for ln in wrap(node["title"], TY["label-title"]["size"], bw - 2 * pad, bold=True)]
        lines += [("t-label-note muted", ln)
                  for ln in wrap(node.get("note", ""), TY["label-note"]["size"], bw - 2 * pad)]
        tag = BASIS_TAG[node.get("basis", "public")]
        if tag:
            lines += [("t-label-note tag", ln) for ln in wrap(tag, TY["label-note"]["size"], bw - 2 * pad)]
        h = 2 * pad + TY["label-title"]["line"] + TY["label-note"]["line"] * (len(lines) - 1)
        return lines, h

    for k, node in enumerate(nodes):
        lines, h = box(x0, main_w, node, "cbox")
        bh = h
        br = node.get("branch")
        if br:
            blines, bhh = box(x1 + SP["chain-branch-gutter"], branch_w, br, "cbox")
            bh = max(bh, bhh)
        svg.add(f'<rect class="cbox" x="{f1(x0)}" y="{f1(y)}" width="{f1(main_w)}" height="{f1(h)}" rx="3"/>')
        ty = y + pad + TY["label-title"]["size"] * 0.85
        for cls, s in lines:
            svg.text(x0 + pad, ty, s, cls)
            ty += TY["label-note"]["line"] if cls != "t-label-title" else TY["label-title"]["line"]
        if br:
            bx = x1 + SP["chain-branch-gutter"]
            svg.add(f'<rect class="cbox" x="{f1(bx)}" y="{f1(y)}" width="{f1(branch_w)}" height="{f1(bhh)}" rx="3"/>')
            ty = y + pad + TY["label-title"]["size"] * 0.85
            for cls, s in blines:
                svg.text(bx + pad, ty, s, cls)
                ty += TY["label-note"]["line"] if cls != "t-label-title" else TY["label-title"]["line"]
            cy = y + min(h, bhh) / 2
            ah = 6
            svg.add(f'<path class="carrow" d="M{f1(bx - 2)} {f1(cy)}H{f1(x1 + ah - 1)}"/>')
            svg.add(f'<path class="cahead" d="M{f1(x1)} {f1(cy)}l{ah} {-3.4}v{6.8}z"/>')
        y += bh
        if k < len(nodes) - 1:
            cx = x0 + main_w / 2
            ah = 7
            svg.add(f'<path class="carrow" d="M{f1(cx)} {f1(y + 2)}V{f1(y + arrow - ah + 1)}"/>')
            svg.add(f'<path class="cahead" d="M{f1(cx)} {f1(y + arrow)}l{-3.8} {-ah}h{7.6}z"/>')
            y += arrow
    y += 12
    for ln in wrap(spec["footer"], TY["label-note"]["size"], full):
        svg.text(M, y, ln, "t-label-note muted")
        y += TY["label-note"]["line"]
    svg.h = y - TY["label-note"]["line"] + M
    return svg


# --------------------------------------------------------------------------- palette legend
def build_legend() -> Svg:
    """The site-wide legend on the "Figure conventions" page, straight from the tokens."""
    mats = TOK["materials"]
    alt = ("A key to the colours used in every cross-section on this site: one swatch per material, "
           "with the material's name beside it and the pattern that is printed over the colour, so that "
           "colour is never the only thing that tells two materials apart.")
    svg = Svg("legend", "Figure palette", alt)
    sw_w, sw_h, gap = 46.0, 19.0, 8.0
    tx = M + sw_w + 10
    tw = W - M - tx
    y = M
    for key, v in mats.items():
        title = wrap(v["label"], TY["label-title"]["size"], tw, bold=True)
        note = PATTERN_WORDS.get(v["pattern"], v["pattern"])
        lines = [("t-label-title", ln) for ln in title] + [("t-label-note muted", note)]
        th = TY["label-title"]["line"] * len(title) + TY["label-note"]["line"]
        h = max(sw_h, th)
        pts = (f"{f1(M)},{f1(y + (h - sw_h) / 2)} {f1(M + sw_w)},{f1(y + (h - sw_h) / 2)} "
               f"{f1(M + sw_w)},{f1(y + (h + sw_h) / 2)} {f1(M)},{f1(y + (h + sw_h) / 2)}")
        fill_material(svg, key, pts, key)
        ty = y + (h - th) / 2 + TY["label-title"]["size"] * 0.85
        for cls, ln in lines:
            svg.text(tx, ty, ln, cls)
            ty += TY["label-title"]["line"] if cls == "t-label-title" else TY["label-note"]["line"]
        y += h + gap
    svg.h = y - gap + M
    return svg


# --------------------------------------------------------------------------- lint
SIZE_BY_CLASS = {f"t-{k}": v for k, v in TY.items() if isinstance(v, dict)}


def _bbox(el):
    cls = el.get("class", "").split()
    size = next((SIZE_BY_CLASS[c]["size"] for c in cls if c in SIZE_BY_CLASS), None)
    bold = any(SIZE_BY_CLASS.get(c, {}).get("weight", 400) >= 600 for c in cls)
    mono = "t-mono" in cls
    if size is None:
        return None
    w = text_w(el.text or "", size, bold, mono)
    for ch in el:
        w += text_w(ch.text or "", TY["mono"]["size"], False, True) + text_w(ch.tail or "", size, bold, mono)
    x, y = float(el.get("x")), float(el.get("y"))
    if el.get("text-anchor") == "end":
        x -= w
    elif el.get("text-anchor") == "middle":
        x -= w / 2
    return (x, y - size * 0.8, x + w, y + size * 0.25, size)


def _segments(d):
    toks = re.findall(r"[MLHVZ]|-?[\d.]+", d)
    segs, cur, i, cmd = [], (0.0, 0.0), 0, None
    while i < len(toks):
        if toks[i] in "MLHVZ":
            cmd = toks[i]
            i += 1
            continue
        if cmd in "ML":
            nxt = (float(toks[i]), float(toks[i + 1]))
            i += 2
        elif cmd == "H":
            nxt = (float(toks[i]), cur[1])
            i += 1
        else:
            nxt = (cur[0], float(toks[i]))
            i += 1
        if cmd != "M":
            segs.append((cur, nxt))
        else:
            cmd = "L"
        cur = nxt
    return segs


def _seg_hits_box(seg, box, pad):
    (x0, y0), (x1, y1) = seg
    bx0, by0, bx1, by1 = box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad
    for k in range(41):
        t = k / 40
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        if bx0 <= x <= bx1 and by0 <= y <= by1:
            return True
    return False


def _cross(s1, s2):
    def o(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    a, b = s1
    c, d = s2
    return o(a, b, c) * o(a, b, d) < -1e-6 and o(c, d, a) * o(c, d, b) < -1e-6


def lint_svg_text(raw: str, name: str = "") -> list[str]:
    """The eighteen mechanical rules of report D, on the finished SVG."""
    errs = []
    ns = {"s": "http://www.w3.org/2000/svg"}
    root = ET.fromstring(raw)
    vb = [float(v) for v in root.get("viewBox").split()]
    if vb[2] != W:                                                        # 1
        errs.append(f"canvas width {vb[2]} != {W}")
    if not (root.find("s:title", ns) is not None                          # 2
            and (root.find("s:desc", ns).text or "").strip()):
        errs.append("missing <title>/<desc>")
    allowed = {v[m].lower() for grp in ("theme", "materials", "phases")    # 3
               for v in TOK[grp].values() for m in ("light", "dark")}
    allowed |= {v["tint"][m].lower() for v in TOK["phases"].values() for m in ("light", "dark")}
    for col in sorted(set(re.findall(r"#[0-9a-fA-F]{6}\b", raw))):
        if col.lower() not in allowed:
            errs.append(f"colour {col} is not a token")
    if re.search(r'(fill|stroke)="(?!none|url)[^"]+"', raw):               # 4
        errs.append("literal fill/stroke attribute found; use token classes")
    texts = [(el, _bbox(el)) for el in root.iter("{http://www.w3.org/2000/svg}text")]
    for el, b in texts:                                                   # 5
        if b is None:
            errs.append(f"text without a type-scale class: {el.text!r}")
    texts = [(el, b) for el, b in texts if b]
    for el, b in texts:
        if b[4] < TY["min-size"]:                                         # 6
            errs.append(f"text below minimum size: {el.text!r}")
        if b[0] < M - 0.5 or b[2] > W - M + 0.5 or b[1] < 0 or b[3] > vb[3]:   # 7
            errs.append(f"text escapes the canvas margins ({b[0]:.0f}..{b[2]:.0f}): {el.text!r}")
    c = SP["text-clearance"]
    for i in range(len(texts)):                                           # 8
        for j in range(i + 1, len(texts)):
            a, b = texts[i][1], texts[j][1]
            if a[0] < b[2] + c and b[0] < a[2] + c and a[1] < b[3] and b[1] < a[3]:
                errs.append(f"text overlap: {texts[i][0].text!r} / {texts[j][0].text!r}")
    rects = [[float(v) for v in g.get("data-rect").split(",")]
             for g in root.iter("{http://www.w3.org/2000/svg}g") if g.get("data-rect")]
    for el, b in texts:                                                   # 9
        for rx, ry, rw, rh in rects:
            if b[0] < rx + rw and rx < b[2] and b[1] < ry + rh and ry < b[3]:
                errs.append(f"text inside a drawing area: {el.text!r}")
    leaders = [(p.get("data-owner", ""), _segments(p.get("d")))
               for p in root.iter("{http://www.w3.org/2000/svg}path") if p.get("class") in ("leader", "dim")]
    for owner, segs in leaders:                                           # 10
        for seg in segs:
            for el, b in texts:
                if _seg_hits_box(seg, b, 1.0):
                    errs.append(f"leader of {owner!r} touches text {el.text!r}")
    for i in range(len(leaders)):                                         # 11
        for j in range(i + 1, len(leaders)):
            if any(_cross(a, b) for a in leaders[i][1] for b in leaders[j][1]):
                errs.append(f"leaders cross: {leaders[i][0]!r} x {leaders[j][0]!r}")
    edges = []                                                            # 12
    draw_right = max([rx + rw for rx, ry, rw, rh in rects], default=W)
    for pg in root.iter("{http://www.w3.org/2000/svg}polygon"):
        if "mat" in (pg.get("class") or "").split():
            pts = [tuple(float(v) for v in q.split(",")) for q in pg.get("points").split()]
            for a, b in zip(pts, pts[1:] + pts[:1]):
                if max(a[0], b[0]) > draw_right - 0.5:
                    continue                      # the bleed off the edge of the drawing
                if abs(a[1] - b[1]) > 6 and abs(a[0] - b[0]) < 0.35 * abs(a[1] - b[1]):
                    edges.append((a, b))
    for owner, segs in leaders:
        start = segs[0][0] if segs else None
        for (p0, p1) in segs:
            if abs(p0[0] - p1[0]) > 0.01:
                continue
            ylo, yhi = sorted((p0[1], p1[1]))
            for a, b in edges:
                for k in range(21):
                    ey = a[1] + (b[1] - a[1]) * k / 20
                    ex = a[0] + (b[0] - a[0]) * k / 20
                    if ylo < ey < yhi and abs(ex - p0[0]) < 5 and math.hypot(ex - start[0], ey - start[1]) > 8:
                        errs.append(f"leader of {owner!r} runs within 5 u of a material edge at y={ey:.0f}")
                        break
                else:
                    continue
                break
    if root.get("data-kind") == "xsection" and "Not to scale" not in raw:  # 13
        errs.append("cross-section without the 'Not to scale' line")
    heads = [t for t in texts if "t-panel-title" in (t[0].get("class") or "")]
    if root.get("data-kind") == "xsection" and not heads:
        errs.append("cross-section without a panel title")
    # 14: two leaders may never run side by side.  With orthogonal lane routing every leader
    # owns a distinct vertical x, so a pair that comes within the lane clearance and overlaps
    # in extent is a layout regression, not a drawing an author can trace.
    clear = SP["leader-lane-clearance"]
    flat_segs = [(owner, seg) for owner, segs in leaders for seg in segs]
    for i in range(len(flat_segs)):
        for j in range(i + 1, len(flat_segs)):
            (oa, (a0, a1)), (ob, (b0, b1)) = flat_segs[i], flat_segs[j]
            if oa == ob:
                continue
            va, vb = abs(a0[0] - a1[0]) < 0.01, abs(b0[0] - b1[0]) < 0.01
            ha, hb = abs(a0[1] - a1[1]) < 0.01, abs(b0[1] - b1[1]) < 0.01
            if va and vb and abs(a0[0] - b0[0]) < clear:
                if min(a0[1], a1[1]) < max(b0[1], b1[1]) - 1 and min(b0[1], b1[1]) < max(a0[1], a1[1]) - 1:
                    errs.append(f"leaders of {oa!r} and {ob!r} run side by side "
                                f"{abs(a0[0] - b0[0]):.1f} u apart; give each its own lane")
            elif ha and hb and abs(a0[1] - b0[1]) < clear:
                if min(a0[0], a1[0]) < max(b0[0], b1[0]) - 1 and min(b0[0], b1[0]) < max(a0[0], a1[0]) - 1:
                    errs.append(f"leaders of {oa!r} and {ob!r} run side by side "
                                f"{abs(a0[1] - b0[1]):.1f} u apart; stagger their anchors")
    # 14b: two gutter legs that descend side by side for a long way, a lane apart, are the
    # same fault seen vertically: the eye cannot tell which leg leads where.
    if root.get("data-kind") == "xsection":
        pitch = SP["lane-pitch"] + 2.5
        legs = [(o, (min(a[1], b[1]), max(a[1], b[1])), a[0]) for o, (a, b) in flat_segs
                if abs(a[0] - b[0]) < 0.01 and a[0] > draw_right - 0.5]
        for i in range(len(legs)):
            for j in range(i + 1, len(legs)):
                (oa, (a0, a1), ax), (ob, (b0, b1), bx) = legs[i], legs[j]
                if oa == ob or abs(ax - bx) >= pitch:
                    continue
                run = min(a1, b1) - max(a0, b0)
                if run > SP["max-parallel-leg"]:
                    errs.append(f"leaders of {oa!r} and {ob!r} descend side by side for "
                                f"{run:.0f} u, {abs(ax - bx):.1f} u apart; at most "
                                f"{SP['max-parallel-leg']:.0f} u")
    # 14c: a label belongs beside its drawing; one pushed well below the drawing's bottom
    # edge leaves its leader hanging down the side of the picture.
    if root.get("data-kind") == "xsection" and rects:
        canvas_h = float(root.get("viewBox").split()[3])
        srt = sorted(rects, key=lambda r: r[1])
        for k, (rx, ry, rw, rh) in enumerate(srt):
            # the right-hand column of a panel starts level with its drawing and ends
            # before the next panel's drawing begins
            lo, hi = ry, srt[k + 1][1] if k + 1 < len(srt) else canvas_h + 1
            for el, b in texts:
                if "t-label-title" not in (el.get("class") or "") or b[0] < rx + rw:
                    continue
                if lo <= b[1] < hi and b[1] > ry + rh + SP["max-label-drop"]:
                    errs.append(f"panel {k + 1}: the label {el.text!r} sits {b[1] - ry - rh:.0f} u below the "
                                f"bottom of its drawing; at most {SP['max-label-drop']:.0f} u")
    # 15: two anchor dots that sit almost on top of each other cannot be told apart.
    dots = [(c.get("data-owner", ""), float(c.get("cx")), float(c.get("cy")))
            for c in root.iter("{http://www.w3.org/2000/svg}circle") if c.get("class") == "dot"]
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            (oa, ax, ay), (ob, bx, by) = dots[i], dots[j]
            if abs(ax - bx) < SP["anchor-separation-x"] and abs(ay - by) < SP["anchor-separation-y"]:
                errs.append(f"the anchors of {oa!r} and {ob!r} are "
                            f"{math.hypot(ax - bx, ay - by):.1f} u apart; "
                            "stagger one of them inside its own layer")
    # 18b: a leader may not climb inside an ion beam beside the arrows (it reads as one more
    # arrow), and a beam label's riser may not start on an arrow's tail.
    shafts = [_segments(pth.get("d"))[0] for pth in root.iter("{http://www.w3.org/2000/svg}path")
              if pth.get("class") == "ion" and _segments(pth.get("d"))]
    for owner, segs in leaders:
        for (a, b) in segs:
            if abs(a[0] - b[0]) > 0.05 or abs(a[1] - b[1]) < 10:
                continue
            ylo, yhi = sorted((a[1], b[1]))
            for (s0, s1) in shafts:
                olo, ohi = max(ylo, min(s0[1], s1[1])), min(yhi, max(s0[1], s1[1]))
                if ohi - olo < 10:
                    continue
                ym = (olo + ohi) / 2
                t = (ym - s0[1]) / ((s1[1] - s0[1]) or 1e-9)
                xs_at = s0[0] + (s1[0] - s0[0]) * t
                if owner != "ions" and abs(xs_at - a[0]) < 12:
                    errs.append(f"the leader of {owner!r} rises inside the ion beam, "
                                f"{abs(xs_at - a[0]):.0f} u from an arrow; open a lane or route it clear")
                    break
    for owner, cx, cy in dots:
        if owner != "ions":
            continue
        for (s0, s1) in shafts:
            tail = s0 if s0[1] < s1[1] else s1
            if math.hypot(tail[0] - cx, tail[1] - cy) < 3.0:
                errs.append(f"the beam label's dot sits on an arrow's tail ({math.hypot(tail[0] - cx, tail[1] - cy):.1f} u)")
    # 18c: two horizontal leader runs closer than 10 u for more than 40 u read as a pair.
    hruns = [(owner, min(a[0], b[0]), max(a[0], b[0]), a[1]) for owner, segs in leaders
             for (a, b) in segs if abs(a[1] - b[1]) < 0.05 and abs(a[0] - b[0]) > 40]
    for i in range(len(hruns)):
        for j in range(i + 1, len(hruns)):
            oa, a0, a1, ay = hruns[i]
            ob, b0, b1, by = hruns[j]
            if oa != ob and 0 < abs(ay - by) < 10 and min(a1, b1) - max(a0, b0) > 40:
                errs.append(f"the leaders of {oa!r} and {ob!r} run {abs(ay - by):.1f} u apart for "
                            f"{min(a1, b1) - max(a0, b0):.0f} u; at least 10 u apart")
    # 15b: a label's dot must sit on the material it names, as a reader sees it: the last
    # (top-most) polygon painted at the dot, inside the dot's own drawing, faded ghosts aside.
    painted = []
    for grp in root.iter("{http://www.w3.org/2000/svg}g"):
        if "drawing" not in (grp.get("class") or "").split() or not grp.get("data-rect"):
            continue
        gx, gy, gw, gh = (float(v) for v in grp.get("data-rect").split(","))
        for pg in grp.iter("{http://www.w3.org/2000/svg}polygon"):
            cls = (pg.get("class") or "").split()
            if "mat" in cls and "faded" not in cls and pg.get("data-layer"):
                pts = [tuple(float(v) for v in q.split(",")) for q in pg.get("points").split()]
                painted.append((pg.get("data-layer"), pts, (gx, gy, gx + gw, gy + gh)))
    names = {lay for lay, _p, _r in painted}
    # 15c: a dot on (or within 3 u of) its drawing's left or right edge is half outside the
    # picture, and its leader climbs the edge.
    # (a stack chart's dots sit on its bar's edge by design)
    rects_d = {r for _l, _p, r in painted} if root.get("data-kind") == "xsection" else set()
    for owner, cx, cy in dots:
        if owner == "ions" or owner.startswith(("dim", "callout")):
            continue
        for (x0, y0, x1, y1) in rects_d:
            if y0 <= cy <= y1 and x0 <= cx <= x1 and min(cx - x0, x1 - cx) < 3.0:
                errs.append(f"the dot of {owner!r} sits {min(cx - x0, x1 - cx):.1f} u from its "
                            "drawing's edge; at least 3 u inside")
    for owner, cx, cy in dots:
        if owner not in names:
            continue
        top = None
        for lay, pts, (x0, y0, x1, y1) in painted:
            if x0 <= cx <= x1 and y0 <= cy <= y1 and _point_in((cx, cy), pts):
                top = lay
        if top is not None and top != owner:
            errs.append(f"the top-most material painted at the dot of {owner!r} is {top!r}; "
                        "the dot names what a reader sees there")
    # 16: an implant label may never be drawn over the material that blocks the implant.
    # A material polygon is seen only inside the clip rectangle of its drawing (the substrate
    # runs on below the crop), so a point counts as inside it only within that rectangle.
    polys = []
    clip_of = {}
    for grp in root.iter("{http://www.w3.org/2000/svg}g"):
        if "drawing" in (grp.get("class") or "").split() and grp.get("data-rect"):
            gx, gy, gw, gh = (float(v) for v in grp.get("data-rect").split(","))
            for pg in grp.iter("{http://www.w3.org/2000/svg}polygon"):
                clip_of[id(pg)] = (gx, gy, gx + gw, gy + gh)
    for pg in root.iter("{http://www.w3.org/2000/svg}polygon"):
        cls = (pg.get("class") or "").split()
        if "mat" not in cls:
            continue
        mat = next((c[2:] for c in cls if c.startswith("m-")), "")
        if "faded" in cls or TOK["materials"].get(mat, {}).get("fill") == "none":
            mat = "~" + mat                  # drawn without a colour of its own
        pts = [tuple(float(v) for v in q.split(",")) for q in pg.get("points").split()]
        polys.append((mat, pts))
        clip_of[len(polys) - 1] = clip_of.get(id(pg), (-math.inf, -math.inf, math.inf, math.inf))
    for owner, segs in leaders:
        if owner != "ions":
            continue
        for (p0, p1) in segs:
            for k in range(21):
                q = (p0[0] + (p1[0] - p0[0]) * k / 20, p0[1] + (p1[1] - p0[1]) * k / 20)
                hit = next((mt for k2, (mt, pts) in enumerate(polys)
                            if clip_of[k2][0] <= q[0] <= clip_of[k2][2]
                            and clip_of[k2][1] <= q[1] <= clip_of[k2][3] and _point_in(q, pts)), None)
                if hit:
                    errs.append(f"the ion-beam label's leader runs through {hit}; "
                                "route it above the surface, clear of every mask")
                    break
            else:
                continue
            break
    # 19: a label leader may not cut through the arrows of an ion beam.
    ion_segs = [seg for p in root.iter("{http://www.w3.org/2000/svg}path")
                if p.get("class") == "ion" for seg in _segments(p.get("d"))]
    for owner, segs in leaders:
        if owner == "ions":
            continue
        if any(_cross(a, b) for a in segs for b in ion_segs):
            errs.append(f"leader of {owner!r} cuts through the ion beam")
    # 18: a leader may not run a long way through materials other than the one it names,
    # nor alongside a material edge: either way it reads as the boundary of a film.
    # As in rule 16, a polygon counts only inside the clip rectangle of its own drawing: the
    # substrate runs on below a close-up's crop, into the next panel.
    layered = []
    for pg in root.iter("{http://www.w3.org/2000/svg}polygon"):
        cls = (pg.get("class") or "").split()
        if "mat" in cls:
            pts = [tuple(float(v) for v in q.split(",")) for q in pg.get("points").split()]
            layered.append((pg.get("data-layer") or "", pts,
                            clip_of.get(id(pg), (-math.inf, -math.inf, math.inf, math.inf))))
    hedges = []
    for _lid, pts, clip in layered:
        for a, b in zip(pts, pts[1:] + pts[:1]):
            if abs(a[1] - b[1]) < 0.3 and abs(a[0] - b[0]) > 0.5 and clip[1] <= a[1] <= clip[3]:
                hedges.append((min(a[0], b[0]), max(a[0], b[0]), a[1], SP["edge-clearance"]))
    # The accent trace of a highlight is a line on the drawing too: a leader beside it reads
    # as one more film edge.
    for pl in root.iter("{http://www.w3.org/2000/svg}polyline"):
        if "hl" not in (pl.get("class") or "").split():
            continue
        pts = [tuple(float(v) for v in q.split(",")) for q in pl.get("points").split()]
        for a, b in zip(pts, pts[1:]):
            if abs(a[1] - b[1]) < 0.3 and abs(a[0] - b[0]) > 0.5:
                hedges.append((min(a[0], b[0]), max(a[0], b[0]), a[1], "hl"))

    def in_rect(q):
        return any(rx <= q[0] <= rx + rw and ry <= q[1] <= ry + rh for rx, ry, rw, rh in rects)

    for owner, segs in leaders:
        if owner in ("ions",) or owner.startswith(("dim", "callout")):
            continue
        through, along, rise, rise_layers = 0, set(), 0, set()
        single = (0, None)
        for (p0, p1) in segs:
            if abs(p0[0] - p1[0]) < 0.01 and abs(p0[1] - p1[1]) > 0.01:
                # a riser: a vertical line up through a stack of films reads as a feature
                # (a contact, a plug), so it has a limit of its own
                ya, yb = sorted((p0[1], p1[1]))
                for k in range(int(ya) + 1, int(yb)):
                    q = (p0[0], k + 0.5)
                    if not in_rect(q):
                        continue
                    vis = None
                    for lid, pts, clip in layered:
                        if clip[0] <= q[0] <= clip[2] and clip[1] <= q[1] <= clip[3] and _point_in(q, pts):
                            vis = lid
                    if vis is not None and vis != owner:
                        rise += 1
                        rise_layers.add(vis)
                continue
            if abs(p0[1] - p1[1]) > 0.01:
                continue
            xa, xb = sorted((p0[0], p1[0]))
            run_lid, run_len = None, 0
            for k in range(int(xa) + 1, int(xb)):
                q = (k + 0.5, p0[1])
                if not in_rect(q):
                    run_lid, run_len = None, 0
                    continue
                vis = None
                for lid, pts, clip in layered:
                    if clip[0] <= q[0] <= clip[2] and clip[1] <= q[1] <= clip[3] and _point_in(q, pts):
                        vis = lid
                if vis is not None and vis != owner:
                    through += 1
                # the longest stretch inside ONE other film: a leader that leaves its layer
                # sideways and runs along inside the next film reads as that film's boundary
                if vis is not None and vis != owner and vis == run_lid:
                    run_len += 1
                else:
                    run_lid, run_len = vis, (1 if vis is not None and vis != owner else 0)
                if run_len > single[0]:
                    single = (run_len, run_lid)
                # Above a highlight (in the air over the new surface) a run needs the larger
                # clearance; below it, inside the film the trace marks, the material one.
                if any(e0 <= q[0] <= e1 and abs(ey - q[1]) < (
                        (SP["highlight-clearance"] if q[1] < ey else SP["edge-clearance"])
                        if clr == "hl" else clr) for e0, e1, ey, clr in hedges):
                    along.add(k)
        if through > SP["max-leader-traverse"]:
            errs.append(f"leader of {owner!r} runs {through} u through other materials; at most "
                        f"{int(SP['max-leader-traverse'])} — it reads as a film boundary")
        if len(along) > SP["max-edge-run"]:
            errs.append(f"leader of {owner!r} runs {len(along)} u alongside a material edge; at most "
                        f"{int(SP['max-edge-run'])}")
        if single[0] > SP["max-film-traverse"]:
            errs.append(f"leader of {owner!r} runs {single[0]} u inside {single[1]!r}; at most "
                        f"{int(SP['max-film-traverse'])} u inside one other film — it reads as "
                        "that film's boundary")
        # A riser up through one fill or one mask reads as a leader; a long one up through a
        # stack of films reads as a contact or a plug cut through them.
        if rise > SP["max-riser-traverse"] and len(rise_layers) > SP["max-riser-layers"]:
            errs.append(f"leader of {owner!r} rises {rise} u through {len(rise_layers)} other layers; "
                        f"at most {int(SP['max-riser-traverse'])} u through more than "
                        f"{int(SP['max-riser-layers'])} — a vertical line through a stack of films "
                        "reads as a contact or a plug")
    # 17: two materials that are hard to tell apart may only touch when their patterns
    # differ and both are thick enough for that pattern to show.
    boxes = [(mt, min(x for x, _ in pts), min(y for _, y in pts),
              max(x for x, _ in pts), max(y for _, y in pts)) for mt, pts in polys]
    seen_pairs = set()
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            ma, ax0, ay0, ax1, ay1 = boxes[i]
            mb, bx0, by0, bx1, by1 = boxes[j]
            if ma == mb or ma not in TOK["materials"] or mb not in TOK["materials"]:
                continue
            touch = (min(ax1, bx1) - max(ax0, bx0) > 1
                     and (abs(ay1 - by0) < 1.5 or abs(by1 - ay0) < 1.5))
            if not touch or (ma, mb) in seen_pairs:
                continue
            seen_pairs.add((ma, mb))
            va, vb = TOK["materials"][ma], TOK["materials"][mb]
            de = min(min(math.dist(_lab(va[mode], sim), _lab(vb[mode], sim))
                         for sim in (None, "deutan", "protan")) for mode in ("light", "dark"))
            if de >= 14:
                continue
            if va["pattern"] == vb["pattern"]:
                errs.append(f"{ma} and {mb} touch, are {de:.1f} apart in colour and share "
                            f"a pattern; one of them needs its own pattern")
            else:
                # Only a patterned film needs the height for its pattern to show; a plain film
                # reads as its flat colour, inked, at any thickness (a thin oxide under PSG).
                thin = [m for m, b in ((ma, boxes[i]), (mb, boxes[j]))
                        if b[4] - b[2] < 10 and TOK["materials"][m]["pattern"] != "none"]
                if thin:
                    errs.append(f"{ma} and {mb} touch and are {de:.1f} apart in colour, so the "
                                f"pattern is the only thing between them, but {', '.join(thin)} "
                                "is drawn thinner than 10 u, where a pattern may not show")
    return [f"{name}: {e}" if name else e for e in errs]


def _point_in(q, pts) -> bool:
    x, y = q
    inside = False
    n = len(pts)
    for i in range(n):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % n]
        if (y0 > y) != (y1 > y) and x < (x1 - x0) * (y - y0) / (y1 - y0 + 1e-12) + x0:
            inside = not inside
    return inside


# --------------------------------------------------------------------------- spec lint
_INFORCE: tuple[set[str], object] | None = None


def _inforce():
    """The footnote labels and the text matcher of ``tools/check_inforce.py``, for families it
    does not treat as certainly expired.  Both the data loading and the matching are that
    checker's own code, imported, not a copy of it."""
    global _INFORCE
    if _INFORCE is None:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import check_inforce                                       # noqa: PLC0415
        fams = check_inforce.restricted_families(check_inforce.load_families())
        texts = {p: p.read_text(encoding="utf-8") for p in check_inforce.pages()}
        texts[check_inforce.INVENTORY] = check_inforce.INVENTORY.read_text(encoding="utf-8")
        check_inforce.map_keys_and_labels(fams, texts)
        _INFORCE = ({lab for f in fams for lab in f.labels}, check_inforce.Matcher(fams))
    return _INFORCE


def restricted_labels() -> set[str]:
    return _inforce()[0]


def inforce_hits(text: str, where: str) -> list[str]:
    """Every publication number, patent title or restricted phrase of a family that is not
    certainly expired, found anywhere in a string that will end up in a figure.  A figure
    cannot sit inside a collapsed note, so there is nowhere for any of it to go."""
    if not text:
        return []
    matcher = _inforce()[1]
    flat = " ".join(str(text).split())
    out = []
    for _m, owners, kind, value in matcher.finditer(flat):
        out.append(f"{where}: {kind} {value!r} belongs to patent family "
                   f"{owners[0].id}, which is not shown as certainly expired; "
                   "a figure may never carry it")
    return sorted(set(out))


def spec_strings(spec: dict, series: dict | None):
    """Every free-text string of a spec that ends up in the SVG, the caption or the alt."""
    out: list[tuple[str, str]] = []

    def lab(prefix, d):
        if not d:
            return
        for field in ("title", "note"):
            if d.get(field):
                out.append((f"{prefix} {field}", d[field]))

    out.append(("caption", spec.get("caption", "")))
    out.append(("alt text", spec.get("alt", "")))
    for field in ("title", "footer"):
        if spec.get(field):
            out.append((field, spec[field]))
    if spec.get("axis", {}).get("label"):
        out.append(("axis label", spec["axis"]["label"]))
    for field in ("strip_header", "rows_header"):
        if spec.get(field):
            out.append((field, spec[field]))
    for m in spec.get("modules", []) or []:
        out.append((f"module {m.get('name', '')[:20]}", m.get("name", "")))
    lab("arrow", spec.get("arrow"))
    for p in spec.get("panels", []) or []:
        out.append((f"panel title {p.get('title', '')[:20]}", p.get("title", "")))
        for d in p.get("dims", []) or []:
            lab("dimension label", d.get("label"))
        for c in p.get("callouts", []) or []:
            lab("callout label", c.get("label"))
        for over in (p.get("labels") or {}).values():
            lab("panel label override", over)
    for l in spec.get("layers", []) or []:
        lab(f"layer {l.get('id', '')}", l.get("label"))
    for n in spec.get("nodes", []) or []:
        lab(f"node {n.get('title', '')[:20]}", n)
        lab("branch", n.get("branch"))
    if series:
        lab("series substrate", series["substrate"].get("label"))
        for op in series.get("ops", []):
            lab(f"series layer {op.get('id', op['op'])}", op.get("label"))
    return out


STEP_REF_RE = re.compile(r"steps? \d{3}((, | and |–)\d{3})*")
# Step and level codes are identifiers, not numbers: NILD3, TIN2, WDEP2, NCAPOX3, NILD3_C.
IDENT_RE = re.compile(r"\b[A-Z]{2,}[A-Z0-9_]*\d[A-Z0-9_]*\b")


def _has_number(note: str) -> bool:
    return re.search(r"\d", IDENT_RE.sub("", STEP_REF_RE.sub("", note))) is not None


def _label_errs(key: str, lab: dict, defined: set[str], restricted: set[str],
                page: str | None, to_scale: bool) -> list[str]:
    errs = []
    basis = lab.get("basis", "public")
    if basis not in BASIS_TAG:
        errs.append(f"{key}: unknown basis {basis!r}")
    note = lab.get("note", "")
    if _has_number(note) and not lab.get("cite"):
        errs.append(f"{key}: a label that states a number needs cite:")
    cite = lab.get("cite")
    if cite and page and cite not in defined:
        errs.append(f"{key}: cite key [^{cite}] is not defined on {page}")
    if cite and cite in restricted:
        errs.append(f"{key}: cite key [^{cite}] is a patent shown as in force; "
                    "a figure may never carry it")
    if basis != "public" and _has_number(note):
        if not note.lower().startswith(NOT_PUBLIC):
            errs.append(f"{key}: a value that is not public must say "
                        f"{NOT_PUBLIC!r} first and the reading second")
        if to_scale:
            errs.append(f"{key}: a value that is not public may not be drawn to scale")
    title = lab.get("title", "")
    if len(title) > SP["max-title-chars"]:
        errs.append(f"{key}: the title is {len(title)} characters; "
                    f"at most {SP['max-title-chars']}")
    # The arrow note runs the full width between the panels, so it has a budget of its own;
    # every other note shares the 140 u label column and has to stay short.
    budget = SP["max-arrow-note-chars"] if key == "arrow" else SP["max-note-chars"]
    if len(note) > budget:
        errs.append(f"{key}: the note is {len(note)} characters; "
                    f"at most {int(budget)} — the rest belongs in the caption")
    return errs


def lint_spec(spec: dict, series: dict | None) -> list[str]:
    errs = []
    kind = spec.get("kind")
    if kind not in KINDS:
        return [f"unknown kind {kind!r}"]
    alt = " ".join(spec.get("alt", "").split())
    if not 60 <= len(alt) <= 450:
        errs.append(f"alt text must be 60-450 characters (is {len(alt)})")
    if re.search(r"\[\^", alt):
        errs.append("alt text must not carry citations")
    if not spec.get("caption"):
        errs.append("caption missing")
    page = spec.get("page")
    defined: set[str] = set()
    restricted = restricted_labels()
    if page:
        p = ROOT / page
        if not p.exists():
            errs.append(f"page {page} does not exist")
        else:
            defined = set(re.findall(r"^\[\^([^\]]+)\]:", p.read_text(encoding="utf-8"), re.M))
    to_scale = bool(spec.get("to_scale"))
    labs: list[tuple[str, dict]] = []
    if kind == "xsection":
        # the series' own faults (its base and templates, resolved when it was loaded)
        errs += series.get("_errors", [])
        if not series.get("substrate") or not isinstance(series.get("ops"), list):
            return errs
        # a layer id names one layer; the flow runs forward (a template instantiated twice
        # with the same ids, or in the wrong place, is caught here)
        ids_seen: set[str] = set()
        prev_step = "000"
        for op in series["ops"]:
            if op.get("id"):
                if op["id"] in ids_seen:
                    errs.append(f"layer id {op['id']!r} is used twice in the series")
                ids_seen.add(op["id"])
            st_op = str(op.get("step", ""))
            if re.fullmatch(r"\d{3}", st_op):
                if st_op < prev_step:
                    errs.append(f"operation {op.get('op')} at step {st_op} comes after step "
                                f"{prev_step}; the ops of a series run in step order")
                prev_step = max(prev_step, st_op)
        labs.append(("substrate", series["substrate"].get("label")))
        if series["substrate"]["material"] not in TOK["materials"]:
            errs.append(f"unknown material {series['substrate']['material']}")
        steps = {"000"}
        for op in series["ops"]:
            if op["op"] not in OPS:
                errs.append(f"unknown operation {op['op']!r}; one of {', '.join(sorted(OPS))}")
                continue
            for field in op:
                if field not in OPS[op["op"]] | COMMON_OP_FIELDS:
                    errs.append(f"operation {op['op']} at step {op.get('step')}: "
                                f"unknown field {field!r}")
            if not re.fullmatch(r"\d{3}", str(op.get("step", ""))):
                errs.append(f"operation {op['op']}: step {op.get('step')!r} is not three digits")
            steps.add(str(op.get("step")))
            if op["op"] == "deposit" and op.get("profile", "conformal") not in PROFILES:
                errs.append(f"operation deposit at step {op.get('step')}: profile "
                            f"{op['profile']!r} is not one of {', '.join(PROFILES)}")
            if op["op"] == "deposit" and (op.get("facet_deg") is not None or op.get("smooth")) \
                    and op.get("profile") != "gapfill":
                errs.append(f"operation deposit at step {op.get('step')}: facet_deg and smooth "
                            "belong to profile: gapfill")
            if op["op"] == "deposit" and op.get("t") is not None and float(op["t"]) < SP["min-layer-thickness"]:
                errs.append(f"layer {op['id']} drawn thinner than {SP['min-layer-thickness']} u")
            if op.get("material") and op["material"] not in TOK["materials"]:
                errs.append(f"unknown material {op['material']}")
            for mat in (op.get("materials") or []) + (op.get("only_on") or []) + (op.get("consumes") or []):
                if mat not in TOK["materials"] and mat not in GROUPS:
                    errs.append(f"operation {op['op']} at step {op.get('step')}: "
                                f"unknown material or group {mat!r}")
            if op.get("where_open") and op["where_open"] not in {o.get("id") for o in series["ops"]}:
                errs.append(f"operation {op['op']} at step {op.get('step')}: "
                            f"where_open names no layer of this series ({op['where_open']!r})")
            labs.append((op.get("id", op["op"]), op.get("label")))
        for pn in spec.get("panels", []):
            sa = str(pn.get("state_after", ""))
            if not re.fullmatch(r"\d{3}", sa):
                errs.append(f"state_after {pn.get('state_after')!r} is not a three-digit step number")
            elif sa > max(steps):
                errs.append(f"state_after {sa!r} is beyond the last step of the series "
                            f"({max(steps)})")
        # A doped overlay in a film (`host:`) needs that film to exist where it is made.
        made: set[str] = set()
        host_states = None
        for op in series["ops"]:
            if op["op"] == "dope" and op.get("host"):
                if op["host"] not in made:
                    errs.append(f"operation dope at step {op.get('step')}: host {op['host']!r} names no "
                                "film deposited earlier in this series")
                else:
                    if host_states is None:
                        host_states = series_states(series)[0]
                    st_h = host_states.get(str(op.get("step")))
                    lay = st_h.layers.get(op.get("id")) if st_h else None
                    if lay is not None and not st_h.overlay_columns(lay):
                        errs.append(f"operation dope at step {op.get('step')}: host "
                                    f"{op['host']!r} is absent everywhere the overlay is made")
            if op["op"] in ("deposit", "react") and op.get("id"):
                made.add(op["id"])
        # A faded layer carries no label, so the caption has to tell the reader what the
        # quiet shapes are, by name, as it must for a hidden layer.
        titles = {"sub": (series["substrate"].get("label") or {}).get("title", "")}
        titles.update({o["id"]: (o.get("label") or {}).get("title", "")
                       for o in series["ops"] if o.get("id")})
        faded_ids = sorted({lid for pn in spec.get("panels", []) for lid in pn.get("dim_layers", [])})
        cap_l = " ".join(spec.get("caption", "").lower().split())
        if faded_ids and "faded" not in cap_l:
            errs.append("a panel fades layers (dim_layers) but the caption does not say which "
                        "are drawn faded")
        for lid in faded_ids:
            t = titles.get(lid, "").lower()
            if t and t not in cap_l:
                errs.append(f"{lid!r} is drawn faded but the caption does not name it "
                            f"({t!r}); a faded layer carries no label of its own")
        # A close-up is a different scale from the full slice beside it on the next page:
        # the reader is told, in words, what the enlarged window is.
        if spec.get("close_up") is not None and "close-up" not in cap_l:
            errs.append("the figure draws a close-up (close_up:) but the caption does not say "
                        "so ('close-up of …')")
        # A negative crop_depth starts the drawing above the original silicon surface (a
        # close-up of the upper films, or a full slice of a tall back-end stack): the caption
        # says the rest is cut off, and the figure marks the cut itself.
        cd = spec.get("crop_depth")
        if isinstance(cd, (int, float)) and cd < 0 and CUT_PHRASE not in cap_l:
            errs.append("crop_depth is negative but the caption does not say "
                        f"'{CUT_PHRASE}'")
        # A step that changes nothing the drawing can show gets one panel, not two copies.
        if spec.get("no_drawn_change"):
            if len(spec.get("panels", [])) != 1:
                errs.append("no_drawn_change: the figure has exactly one panel")
            elif spec["panels"][0].get("title") != NO_CHANGE_TITLE:
                errs.append(f"no_drawn_change: the panel is titled {NO_CHANGE_TITLE!r}")
            if spec.get("arrow"):
                errs.append("no_drawn_change: a one-panel figure has no arrow; fold its text "
                            "into the caption")
        # Series fields: known values of the right type, never a traceback.
        if series.get("note_order") is not None and series["note_order"] not in NOTE_ORDERS:
            errs.append(f"series note_order {series['note_order']!r} is not one of "
                        f"{', '.join(NOTE_ORDERS)}")
        for key in series:
            if key not in ("substrate", "ops", "note_order", "_templates", "_errors"):
                errs.append(f"series: unknown top-level field {key!r}")
        for op in series["ops"]:
            for fld in ("z", "anchor_x", "anchor_y", "tilt_deg", "label_x", "t", "depth",
                        "thickness", "from_surface", "y_top", "y_bot", "fill_to", "pitch"):
                if fld in op and not isinstance(op[fld], (int, float)):
                    errs.append(f"operation {op['op']} at step {op.get('step')}: {fld} must be "
                                f"a number, not {op[fld]!r}")
            if "route" in op and op["route"] not in ROUTES:
                errs.append(f"operation {op['op']} at step {op.get('step')}: route "
                            f"{op['route']!r} is not one of {', '.join(ROUTES)}")
        if len(spec["panels"]) > (3 if spec.get("three_panels_allowed") else 2):
            errs.append(f"{len(spec['panels'])} panels; at most two (three only for a "
                        "deposit/pattern/etch summary on a category page)")
        if spec.get("arrow"):
            labs.append(("arrow", spec["arrow"]))
        for p in spec["panels"]:
            labs += [(f"dim in {p['title'][:24]}", d["label"]) for d in p.get("dims", [])]
            labs += [(f"callout in {p['title'][:24]}", c["label"]) for c in p.get("callouts", [])]
            labs += [(f"override in {p['title'][:24]}", o) for o in (p.get("labels") or {}).values()]
            n_top = len(p.get("dims", [])) + len(p.get("callouts", []))
            if n_top > SP["max-header-callouts"]:
                errs.append(f"panel {p['title'][:24]!r} has {n_top} header callouts; "
                            f"at most {int(SP['max-header-callouts'])}")
            if len(p.get("title", "")) > SP["max-panel-title-chars"]:
                errs.append(f"the panel title {p['title'][:30]!r} is {len(p['title'])} "
                            f"characters; at most {int(SP['max-panel-title-chars'])}")
    elif kind == "stack":
        if not to_scale:
            errs.append("a stack chart must declare to_scale: true")
        for l in spec["layers"]:
            if l["material"] not in TOK["materials"]:
                errs.append(f"unknown material {l['material']}")
            labs.append((l.get("id", l["material"]), l.get("label")))
    elif kind == "chain":
        for n in spec["nodes"]:
            labs.append((n["title"][:24], n))
            if n.get("branch"):
                labs.append((n["branch"]["title"][:24], n["branch"]))
    elif kind == "flowmap":
        pass
    for key, lab in labs:
        if lab:
            errs += _label_errs(key, lab, defined, restricted, page, to_scale)
    cap = spec.get("caption", "")
    for key in re.findall(r"\[\^([^\]]+)\]", cap):
        if page and key not in defined:
            errs.append(f"caption cites [^{key}], which is not defined on {page}")
        if key in restricted:
            errs.append(f"caption cites [^{key}], a patent shown as in force")
    if kind == "xsection" and "Not to scale" not in cap:
        errs.append("the caption of a cross-section must end with 'Not to scale.'")
    if kind == "stack" and "To scale" not in cap:
        errs.append("the caption of a to-scale chart must say 'To scale'")
    # Nothing from a patent that is not certainly expired may reach the SVG, the caption or
    # the alt text — in any form, not only as a footnote key.
    for where, text in spec_strings(spec, series):
        errs += inforce_hits(text, where)
    # A caption should say what the picture shows, not re-run the paragraph above it.
    if page:
        errs += caption_echo(spec, ROOT / page)
    if UNKNOWN_GLYPHS:
        errs.append("characters with no entry in the embedded width table, measured at the "
                    "font's widest advance: " + " ".join(sorted(UNKNOWN_GLYPHS)))
    return errs


OPS = {
    "deposit": {"id", "material", "t", "where", "flat", "fill_to", "only_on", "label", "route",
                "anchor_x", "anchor_y", "profile", "facet_deg", "smooth"},
    "etch": {"materials", "where", "depth", "taper_deg", "corner_r", "iso"},
    "strip": {"materials"},
    "planarise": {"to", "stop_on"},
    "react": {"id", "material", "consumes", "under", "t", "where", "label", "route"},
    "dope": {"id", "material", "where", "from_surface", "thickness", "follow", "y_top",
             "y_bot", "anchor_x", "anchor_y", "label", "route", "z", "host"},
    "ions": {"where", "tilt_deg", "pitch", "label", "label_x"},
    "anneal": set(),
}
COMMON_OP_FIELDS = {"op", "step", "where_open"}


def _sentences(text: str) -> list[str]:
    return [t.strip() for t in re.split(r"(?<=[.;])\s+", " ".join(str(text).split())) if t.strip()]


def _plain(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", str(text).lower())


def caption_echo(spec: dict, page: Path) -> list[str]:
    """A caption that repeats a run of eight words from the paragraph it sits under makes the
    reader read the same sentence twice; say what the picture shows instead."""
    if not page.exists():
        return []
    text = page.read_text(encoding="utf-8")
    m = re.search(rf"^:name: fig-{re.escape(spec['id'])}$", text, re.M)
    if not m:
        return []
    before = text[:text.rfind(":::{figure}", 0, m.start())]
    para = " ".join(before.rstrip().split("\n\n")[-1].split())
    words = _plain(para).split()
    windows = {" ".join(words[i:i + 8]) for i in range(max(0, len(words) - 7))}
    out = []
    for sent in _sentences(spec.get("caption", "")):
        sw = _plain(sent).split()
        for i in range(max(0, len(sw) - 7)):
            if " ".join(sw[i:i + 8]) in windows:
                out.append("the caption repeats the paragraph it sits under "
                           f"({' '.join(sw[i:i + 8])!r}); say what the picture shows instead")
                break
    return sorted(set(out))


# --------------------------------------------------------------------------- colour vision
def _lab(hexcol, sim=None):
    r, g, b = (int(hexcol[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    if sim:                                                    # Machado et al. 2009, severity 1.0
        mtx = {"deutan": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413],
                          [-0.011820, 0.042940, 0.968881]],
               "protan": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216],
                          [-0.003882, -0.048116, 1.051998]]}[sim]
        lin = [max(0.0, min(1.0, sum(mtx[r_][c_] * lin[c_] for c_ in range(3)))) for r_ in range(3)]
    x = (0.4124 * lin[0] + 0.3576 * lin[1] + 0.1805 * lin[2]) / 0.95047
    yv = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    z = (0.0193 * lin[0] + 0.1192 * lin[1] + 0.9505 * lin[2]) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    return (116 * f(yv) - 16, 500 * (f(x) - f(yv)), 200 * (f(yv) - f(z)))


def palette_report() -> list[str]:
    """Pairs of materials that are hard to tell apart (dE76 < 14) for normal, deutan or
    protan vision and that also share a pattern.  Such a pair must never touch in a figure."""
    out = []
    mats = TOK["materials"]
    keys = list(mats)
    for mode in ("light", "dark"):
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = mats[keys[i]], mats[keys[j]]
                if a["pattern"] != b["pattern"]:
                    continue
                worst = min(math.dist(_lab(a[mode], s), _lab(b[mode], s)) for s in (None, "deutan", "protan"))
                if worst < 14 and "none" not in (a.get("fill"), b.get("fill")):
                    out.append(f"{mode}: {keys[i]} / {keys[j]} dE={worst:.1f} with the same pattern")
    out += faded_report()
    return out


FADE_HOSTS = ("si-sub", "well-n", "well-p", "well-dn")


def _mix(fg: str, bg: str, a: float) -> str:
    f = [int(fg[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(bg[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(a * x + (1 - a) * y):02x}" for x, y in zip(f, b))


def faded_report(alpha: float | None = None) -> list[str]:
    """A faded layer, and a material with no fill of its own, is seen over whatever lies
    beneath it.  Composite each over every host (the page ground and each kind of silicon)
    and report any result that a reader could take for a different material: a faded layer
    must add no colour of its own."""
    a = float(ST["faded-fill-opacity"]) if alpha is None else alpha
    mats = TOK["materials"]
    out = []
    for mode in ("light", "dark"):
        hosts = {h: mats[h][mode] for h in FADE_HOSTS}
        hosts["ground"] = TOK["theme"]["bg"][mode]
        for m, v in mats.items():
            alpha_m = 0.0 if v.get("fill") == "none" else a
            for hname, hcol in hosts.items():
                seen = _mix(v[mode], hcol, alpha_m)
                if min(math.dist(_lab(seen, sm), _lab(hcol, sm)) for sm in (None, "deutan", "protan")) < 1:
                    continue                  # it shows only its host: no colour of its own
                for o, ov in mats.items():
                    if o in (m, hname) or ov.get("fill") == "none":
                        continue
                    de = min(math.dist(_lab(seen, sm), _lab(ov[mode], sm)) for sm in (None, "deutan", "protan"))
                    if de < 14:
                        out.append(f"{mode}: {m} drawn faded over {hname} looks like {o} (dE={de:.1f})")
    return out


# --------------------------------------------------------------------------- build
def load_spec(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- series templates
# A series file may be written in three parts (added for the via and metal levels, S9, where
# one sequence of steps repeats once per level):
#
#   base: series-metal1.yaml      the ops of that series come first, unchanged (and its
#                                 substrate and note_order, unless this file gives its own)
#   templates:                    named, parameterised lists of ops
#     via-hole:
#       params: [mask_step, ...]  required parameters
#       defaults: {resist_t: 30}  optional ones, with their values
#       ops: [...]                ops in which "${name}" (or "${name.key}" into a mapping
#                                 parameter) stands for a parameter
#   ops:                          plain ops, and instantiations in their place in the flow:
#     - use: via-hole
#       with: {mask_step: "118", ...}
#
# A scalar that is exactly "${name}" takes the parameter's value with its type (a number, a
# list of ranges); inside a longer string the value is written as text ("mask, step ${step}").
# The expansion is done when the series is loaded, so everything downstream (the emulator,
# the lint, the in-force screen) sees ordinary ops.
SERIES_KEYS = ("substrate", "ops", "note_order", "base", "templates")
TEMPLATE_KEYS = ("params", "defaults", "ops")
USE_KEYS = ("use", "with")
PARAM_RE = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)((?:\.[A-Za-z0-9_]+)*)\}")


def _param_refs(obj) -> set[str]:
    """Every parameter name a template body refers to."""
    if isinstance(obj, str):
        return {m.group(1) for m in PARAM_RE.finditer(obj)}
    if isinstance(obj, list):
        return set().union(*(_param_refs(x) for x in obj)) if obj else set()
    if isinstance(obj, dict):
        return set().union(*(_param_refs(v) for v in obj.values())) if obj else set()
    return set()


def _substitute(obj, params: dict, errs: list[str], where: str):
    import copy

    def look(m):
        name, path = m.group(1), [k for k in m.group(2).split(".") if k]
        if name not in params:
            errs.append(f"{where}: ${{{name}}} is not a parameter of the template")
            return None
        v = params[name]
        for k in path:
            if not isinstance(v, dict) or k not in v:
                errs.append(f"{where}: ${{{m.group(1)}{m.group(2)}}}: the parameter has no key {k!r}")
                return None
            v = v[k]
        return v

    if isinstance(obj, str):
        whole = PARAM_RE.fullmatch(obj)
        if whole:
            return copy.deepcopy(look(whole))

        def rep(m):
            v = look(m)
            if isinstance(v, (dict, list)):
                errs.append(f"{where}: {m.group(0)} is a list or mapping and cannot stand inside text")
                return m.group(0)
            return "" if v is None else str(v)
        return PARAM_RE.sub(rep, obj)
    if isinstance(obj, list):
        return [_substitute(x, params, errs, where) for x in obj]
    if isinstance(obj, dict):
        return {k: _substitute(v, params, errs, where) for k, v in obj.items()}
    return obj


def expand_series(raw: dict, name: str, _chain: tuple[str, ...] = ()) -> dict:
    """A series file with its ``base`` and ``templates`` resolved into plain ops.  Faults go
    into ``_errors`` (the lint reports them); ``_templates`` keeps the templates in scope, so
    a series built on this one may instantiate them too."""
    import copy
    errs: list[str] = []
    out: dict = {"substrate": raw.get("substrate"), "ops": []}
    if raw.get("note_order") is not None:
        out["note_order"] = raw["note_order"]
    for k in raw:
        if k not in SERIES_KEYS:
            errs.append(f"{name}: unknown series field {k!r} (one of {', '.join(SERIES_KEYS)})")
    templates: dict = {}
    if raw.get("base"):
        bname = str(raw["base"])
        bpath = SPEC_DIR / bname
        if bname in _chain + (name,):
            errs.append(f"{name}: base {bname!r} loops back ({' -> '.join(_chain + (name, bname))})")
        elif not bpath.exists() or "kind" in (load_spec(bpath) or {}):
            errs.append(f"{name}: base {bname!r} is not a series file in {SPEC_DIR.name}/")
        else:
            base = expand_series(load_spec(bpath), bname, _chain + (name,))
            errs += base.get("_errors", [])
            out["ops"] = copy.deepcopy(base["ops"])
            if out["substrate"] is None:
                out["substrate"] = base["substrate"]
            if "note_order" not in out and base.get("note_order") is not None:
                out["note_order"] = base["note_order"]
            templates.update(base.get("_templates", {}))
    own = raw.get("templates") or {}
    if not isinstance(own, dict):
        errs.append(f"{name}: templates must be a mapping of name to template")
        own = {}
    for tname, tpl in own.items():
        where = f"{name}: template {tname!r}"
        if not isinstance(tpl, dict) or not isinstance(tpl.get("ops"), list):
            errs.append(f"{where}: a template is a mapping with a list of ops")
            continue
        for k in tpl:
            if k not in TEMPLATE_KEYS:
                errs.append(f"{where}: unknown field {k!r} (one of {', '.join(TEMPLATE_KEYS)})")
        req = list(tpl.get("params") or [])
        dfl = dict(tpl.get("defaults") or {})
        both = set(req) & set(dfl)
        if both:
            errs.append(f"{where}: {', '.join(sorted(both))} both required and defaulted")
        refs = _param_refs(tpl["ops"])
        for r in sorted(refs - set(req) - set(dfl)):
            errs.append(f"{where}: its ops use ${{{r}}}, which is not declared in params or defaults")
        for p in sorted((set(req) | set(dfl)) - refs):
            errs.append(f"{where}: parameter {p!r} is declared but its ops never use it")
        templates[tname] = tpl
    if out["substrate"] is None:
        errs.append(f"{name}: no substrate (give one, or a base series)")
    for k, item in enumerate(raw.get("ops") or []):
        if not isinstance(item, dict):
            errs.append(f"{name}: ops entry {k + 1} is not a mapping")
            continue
        if "use" not in item:
            out["ops"].append(item)
            continue
        where = f"{name}: use of {item.get('use')!r} (ops entry {k + 1})"
        for f in item:
            if f not in USE_KEYS:
                errs.append(f"{where}: unknown field {f!r} (one of {', '.join(USE_KEYS)})")
        tpl = templates.get(item["use"])
        if tpl is None:
            errs.append(f"{where}: no such template")
            continue
        given = dict(item.get("with") or {})
        declared = set(tpl.get("params") or []) | set(tpl.get("defaults") or {})
        for p in sorted(set(given) - declared):
            errs.append(f"{where}: {p!r} is not a parameter of the template")
        for p in tpl.get("params") or []:
            if p not in given:
                errs.append(f"{where}: required parameter {p!r} is missing")
        params = dict(tpl.get("defaults") or {})
        params.update(given)
        out["ops"] += _substitute(tpl["ops"], params, errs, where)
    out["_templates"] = templates
    if errs:
        out["_errors"] = list(dict.fromkeys(errs))
    return out


def load_series(name: str) -> dict:
    return expand_series(load_spec(SPEC_DIR / name), name)


def myst_block(spec: dict) -> str:
    cap = " ".join(spec["caption"].split())
    alt = " ".join(spec["alt"].split())
    return (f":::{{figure}} /_static/figures/{spec['id']}.svg\n"
            f":alt: {alt}\n"
            f":width: {SP['display-width-px']}px\n"
            f":name: fig-{spec['id']}\n\n{cap}\n:::\n")


def render_spec(spec: dict, series_cache: dict[str, dict]) -> tuple[Svg, list[str]]:
    kind = spec["kind"]
    series = None
    if kind == "xsection":
        sp = spec["series"]
        if sp not in series_cache:
            series_cache[sp] = load_series(sp)
        series = series_cache[sp]
    errs = lint_spec(spec, series)
    if kind == "xsection":
        svg = build_xsection(spec, series, errs)
    elif kind == "flowmap":
        svg = build_flowmap(spec)
    elif kind == "stack":
        svg = build_stack(spec)
    else:
        svg = build_chain(spec)
    return svg, errs


def artefacts(paths: list[Path] | None = None) -> tuple[dict[Path, str], list[str]]:
    """Every file the specs generate, as {path: text}, plus the lint lines."""
    files: dict[Path, str] = {}
    errs: list[str] = []
    cache: dict[str, dict] = {}
    specs = sorted(paths) if paths else sorted(SPEC_DIR.glob("*.yaml"))
    ids: set[str] = set()
    for path in specs:
        spec = load_spec(path)
        if "kind" not in spec:                       # a series file, not a figure
            continue
        if spec["id"] != path.stem:
            errs.append(f"{path.name}: id {spec['id']!r} does not match the file name")
        if spec["id"] in ids:
            errs.append(f"{path.name}: duplicate figure id {spec['id']!r}")
        ids.add(spec["id"])
        svg, e = render_spec(spec, cache)
        errs += [f"{spec['id']}: {x}" for x in e]
        for theme, suffix in (("auto", ""), ("light", ".light"), ("dark", ".dark")):
            files[OUT_DIR / f"{spec['id']}{suffix}.svg"] = svg.render(theme)
        errs += lint_svg_text(files[OUT_DIR / f"{spec['id']}.svg"], spec["id"])
        files[MYST_DIR / f"{spec['id']}.myst.txt"] = myst_block(spec)
    if paths is None:
        legend = build_legend()
        for theme, suffix in (("auto", ""), ("light", ".light"), ("dark", ".dark")):
            files[OUT_DIR / f"legend-palette{suffix}.svg"] = legend.render(theme)
        errs += lint_svg_text(files[OUT_DIR / "legend-palette.svg"], "legend-palette")
        files[CONVENTIONS] = conventions_page()
    return files, list(dict.fromkeys(errs))   # one line per fault, not one per theme


# --------------------------------------------------------------------------- pages
def conventions_page() -> str:
    mats = TOK["materials"]
    rows = "\n".join(f"| {v['label']} | {PATTERN_WORDS.get(v['pattern'], v['pattern'])} |"
                     for k, v in mats.items())
    tags = "\n".join(f"| {BASIS_TAG[k] or '*(no tag)*'} | {BASIS_MEANING[k]} |" for k in BASIS_TAG)
    legend = (f":::{{figure}} /_static/figures/legend-palette.svg\n"
              f":alt: {' '.join(build_legend().desc.split())}\n"
              f":width: {SP['display-width-px']}px\n"
              f":name: fig-legend-palette\n\n"
              f"The palette used by every cross-section on this site. "
              f"Colour is never the only channel: each material also carries an outline, a pattern "
              f"and a label of its own.\n:::\n")
    return f"""{GENERATED_BANNER}
# Figure conventions

Every diagram on this site is generated from a written description, in one style, by
`tools/gen_figures.py`. No diagram is drawn by hand and none is edited by hand. This page is
the key to them; it is generated from the same token file the figures are, so it cannot drift
away from what you see.

## What a cross-section shows

A cross-section is a slice through the wafer, drawn as the wafer would look if it were cut
and you looked at the cut face. Usually two panels are shown, one above the other: the state
before the step, then the state after it. The blue arrow between them names the step and says
in one sentence what it does. A step with nothing before it, such as the arrival of the wafer,
gets one panel; so does a step that changes nothing the drawing can show (an implant whose
depth is not public, an anneal), titled "{NO_CHANGE_TITLE}", with what the step does in
the caption.

The panels of one module are all cut at the same place, so a feature keeps its position from
one step page to the next.

**Blue is what changed.** The same accent blue marks the one thing the step did and nothing
else: the arrow between the panels, the ion arrows of an implant, and a thin blue trace just
clear of the surface the step made. If a surface is traced in blue, that surface is new.

## Not to scale

**Cross-sections are not to scale.** Thin films are drawn far thicker than they are, or they
would be invisible. Every cross-section says so in its own bottom-left corner and again in its
caption.

A chart that *is* to scale says "To scale" and carries an axis with units instead.

## Materials

{legend}
| Material | What is printed over the colour |
|---|---|
{rows}

## Where a figure's numbers come from

A figure may never say more than its page does. Every label that is not a plain public fact
carries a tag in amber:

| Tag | What it means |
|---|---|
{tags}

Every number in a figure carries the same footnote as the sentence it comes from, and that
footnote is defined on the page the figure sits on. A dimension that is not public is never
drawn to scale, and its label says "not public" before it gives this reference's reading.

Nothing taken from a patent that is shown as in force ever appears in a figure.

## Light and dark

Each figure is written three times: one file that follows your operating system's light or
dark setting on its own, and two that are forced. When you use the theme switch at the top of
the page, a small script swaps in the forced file, so a figure always matches the page around
it.

## Text, labels and leaders

Text never sits on top of a drawing. Material labels stand in a column to the right of the
drawing, in the order of the layers, joined to the layer they name by a thin line ending in a
dot on the layer itself. Each of those lines runs out of its dot, down a track of its own, and
into its label, so two labels can always be told apart; where two films are too thin to give
their dots separate heights, the dots are shifted sideways instead.

Features that are open at the top — a trench, a contact hole, a polished surface, a beam of
ions — are labelled from above instead, from a band over the drawing. There are never more
than two of those in one panel.

A label line never crosses another one, never crosses text, and never runs alongside the edge
of a film, where it could be mistaken for one. Where a line has to cross a material to reach
its label, it is drawn with a narrow halo in the page colour so that it cannot be read as a
boundary.

## Other marks

| Mark | What it means |
|---|---|
| A thin line with an arrowhead at each end | a dimension: the distance between the two surfaces it touches |
| A dashed line running sideways from a dimension | a witness line, marking the surface the dimension is measured to |
| A short line ending in a dot | a label leader; the dot sits on the material the label names |
| Blue arrows pointing at the surface | an implant; the arrows lean only if the page gives a SKY130 tilt, and the caption says which |
| A blue trace just above a surface | the surface this step made |
| A dashed grey outline with no fill and no label | a layer that is present but untouched by this step, drawn faded; it is named on the figure of the step that made it, and the caption names it. In a close-up it keeps its own colour inside the dashed outline, because an enlarged empty film would look like a gap |

A label with no tag is a plain public fact. A label in amber carries one of the three tags in
the table above, and the figure's caption repeats the same hedge in words.
"""


# --------------------------------------------------------------------------- preview / harness
def preview_html() -> str:
    def sw(mode):
        cells = []
        for k, v in TOK["materials"].items():
            pat = "" if v["pattern"] == "none" else f'<rect width="72" height="40" fill="url(#pp-{mode}-{v["pattern"]})"/>'
            cells.append(
                f'<div class="sw"><svg width="72" height="40" viewBox="0 0 72 40"><rect width="72" height="40" '
                f'fill="{v[mode]}" stroke="{TOK["theme"]["ink"][mode]}"/>{pat}</svg>'
                f'<div><b>{k}</b><br>{html.escape(v["label"])}<br><code>{v[mode]}</code> · {v["pattern"]}</div></div>')
        return "".join(cells)

    def pats(mode):
        ink = TOK["theme"]["ink"][mode]
        o, pw = ST["pattern-opacity"], ST["pattern"]
        defs = {
            "hatch": f'width="6" height="6" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="{ink}" stroke-width="{pw}" opacity="{o}"/>',
            "hatch-back": f'width="7" height="7" patternTransform="rotate(-45)"><line x1="0" y1="0" x2="0" y2="7" stroke="{ink}" stroke-width="{pw}" opacity="{o}"/>',
            "xhatch": f'width="6" height="6" patternTransform="rotate(45)"><path d="M0 0V6M0 0H6" stroke="{ink}" stroke-width="{pw}" opacity="{o}" fill="none"/>',
            "hlines": f'width="6" height="5"><line x1="0" y1="2.5" x2="6" y2="2.5" stroke="{ink}" stroke-width="{pw}" opacity="{o}"/>',
            "vlines": f'width="4" height="6"><line x1="2" y1="0" x2="2" y2="6" stroke="{ink}" stroke-width="{pw}" opacity="{o}"/>',
            "plus": f'width="12" height="12"><path d="M3 1V5M1 3H5M9 7V11M7 9H11" stroke="{ink}" stroke-width="{pw}" opacity="{o}" fill="none"/>',
            "dots": f'width="7" height="7"><circle cx="1.75" cy="1.75" r=".9" fill="{ink}" opacity="{o}"/><circle cx="5.25" cy="5.25" r=".9" fill="{ink}" opacity="{o}"/>',
        }
        body = "".join(f'<pattern id="pp-{mode}-{k}" patternUnits="userSpaceOnUse" {v}</pattern>'
                       for k, v in defs.items())
        return f'<svg width="0" height="0" style="position:absolute"><defs>{body}</defs></svg>'

    def themecells(mode):
        return "".join(f'<div class="sw"><span class="chip" style="background:{v[mode]}"></span>'
                       f'<div><b>{k}</b><br><code>{v[mode]}</code><br>{html.escape(v["use"])}</div></div>'
                       for k, v in TOK["theme"].items())

    def phasecells(mode):
        return "".join(f'<div class="sw"><span class="chip" style="background:{v[mode]}"></span>'
                       f'<span class="chip" style="background:{v["tint"][mode]}"></span>'
                       f'<div><b>{k}</b> + tint<br><code>{v[mode]}</code> <code>{v["tint"][mode]}</code></div></div>'
                       for k, v in TOK["phases"].items())

    typ = "".join(f'<tr><td><code>{k}</code></td><td>{v["size"]} u</td><td>{v["weight"]}</td><td>{v["line"]} u</td>'
                  f'<td style="font-size:{v["size"] * 1.25}px;font-weight:{v["weight"]}">Nitride hard mask 0.33 µm</td></tr>'
                  for k, v in TY.items() if isinstance(v, dict))
    spc = "".join(f"<tr><td><code>{k}</code></td><td>{v}</td></tr>" for k, v in SP.items())
    stk = "".join(f"<tr><td><code>{k}</code></td><td>{v}</td></tr>" for k, v in ST.items())
    sect = ""
    for mode in ("light", "dark"):
        t = TOK["theme"]
        sect += (f'<section style="background:{t["bg"][mode]};color:{t["ink"][mode]}">{pats(mode)}<h2>{mode} theme</h2>'
                 f'<h3>Materials</h3><div class="grid">{sw(mode)}</div><h3>Theme</h3><div class="grid">{themecells(mode)}</div>'
                 f'<h3>Phases</h3><div class="grid">{phasecells(mode)}</div></section>')
    return f"""<title>SKY130 figure tokens</title>
<style>
body{{margin:0;font:14px/1.45 {TOK['type']['family']};}}
section,header,.tables{{padding-block:20px;padding-inline:max(16px,calc(50% - 520px))}}
h1{{font-size:22px;margin:0 0 6px}} h2{{font-size:17px;margin:0 0 10px;text-transform:capitalize}} h3{{font-size:14px;margin:18px 0 8px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px 18px}}
.sw{{display:flex;gap:10px;align-items:flex-start;font-size:12px}} .sw svg{{flex:none}}
.chip{{flex:none;width:34px;height:34px;border-radius:4px;border:1px solid #8888}}
code{{font-family:{TOK['type']['family-mono']};font-size:11.5px}}
table{{border-collapse:collapse;margin-bottom:14px}} td,th{{padding:3px 12px 3px 0;text-align:left;border-bottom:1px solid #ccc}}
.tables{{background:#fff;color:#1b1f24;overflow-x:auto}}
</style>
<header style="background:#fff;color:#1b1f24"><h1>SKY130 figure tokens</h1>
<p>Generated from <code>tokens.json</code> ({html.escape(TOK['meta']['version'])}) by
<code>gen_figures.py preview</code>. Do not edit by hand. {html.escape(TOK['meta']['note'])}</p></header>
{sect}
<div class="tables"><h2>Type scale</h2><p>Family: <code>{html.escape(TOK['type']['family'])}</code></p>
<table><tr><th>token</th><th>size</th><th>weight</th><th>line</th><th>sample at desktop scale</th></tr>{typ}</table>
<h2>Spacing (u)</h2><table>{spc}</table><h2>Strokes (u)</h2><table>{stk}</table></div>
"""


QA_DIR = ROOT / "tmp" / "figures" / "qa"


def harness(names: list[str]):
    if not names:
        names = sorted(p.stem for p in SPEC_DIR.glob("*.yaml") if "kind" in load_spec(p))
        names.append("legend-palette")
    QA_DIR.mkdir(parents=True, exist_ok=True)
    rel = Path("../../..") / OUT_DIR.relative_to(ROOT)
    for mode in ("light", "dark"):
        bg, fg = TOK["theme"]["bg"][mode], TOK["theme"]["ink"][mode]
        for width, col in (("desktop", "736px"), ("phone", "100%")):
            figs = "".join(
                f'<figure style="margin:0 0 26px"><img src="{rel}/{n}.{mode}.svg" alt="" '
                f'style="width:{SP["display-width-px"]}px;max-width:100%;height:auto">'
                f'<figcaption style="font-size:13px;opacity:.7">{n} ({mode}, {width})</figcaption></figure>'
                for n in names)
            (QA_DIR / f"{mode}-{width}.html").write_text(
                f'<!doctype html><meta name="viewport" content="width=device-width">'
                f'<body style="margin:0;background:{bg};color:{fg};font:16px/1.5 sans-serif">'
                f'<div style="width:{col};max-width:100%;margin:0 auto;padding:16px;box-sizing:border-box">'
                f'<p>Body text of the page at furo size, for comparison with the label text in the figures below.</p>'
                f'{figs}</div>', encoding="utf-8")
    print(f"wrote {QA_DIR.relative_to(ROOT)}/[light|dark]-[desktop|phone].html for {len(names)} figures")


# --------------------------------------------------------------------------- page blocks
FIG_BLOCK_RE = re.compile(r"^:::\{figure\}[^\n]*\n(?:[^\n]*\n)*?:::\n", re.M)


def page_block_problems(spec: dict, text: str) -> list[str]:
    """The block must be present in the page and must be the generated one, character for
    character: a deleted block, or one whose :name:, :alt: or caption was edited by hand, is
    a page that no longer says what the figure says."""
    blocks = page_blocks(text)
    want = myst_block(spec)
    got = blocks.get(f"fig-{spec['id']}")
    if got is None:
        return [f"{spec['page']}: no {{figure}} block named fig-{spec['id']} is pasted into "
                f"this page; paste data/figures/myst/{spec['id']}.myst.txt into it"]
    out = []
    after = text[text.index(got) + len(got):].lstrip("\n")
    if after.startswith(":::{dropdown}") or after.startswith("```{dropdown}"):
        out.append(f"{spec['page']}: fig-{spec['id']} sits between a paragraph and the "
                   "{dropdown} that follows it; a dropdown right after the lead belongs to the "
                   "lead, so the figure goes after it")
    if got == want:
        return out
    out += [f"{spec['page']}: the figure block for fig-{spec['id']} is not the generated one"]
    out += ["    " + line for line in list(difflib.unified_diff(
        got.splitlines(), want.splitlines(), "in the page", "generated", lineterm="", n=0))[:12]]
    return out


def page_blocks(text: str) -> dict[str, str]:
    """Every ``{figure}`` block on a page, keyed by its ``:name:``."""
    out = {}
    for m in FIG_BLOCK_RE.finditer(text):
        n = re.search(r"^:name: (\S+)$", m.group(0), re.M)
        if n:
            out[n.group(1)] = m.group(0)
    return out


# --------------------------------------------------------------------------- commands
def write_files(files: dict[Path, str]) -> int:
    n = 0
    for path, text in sorted(files.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
            n += 1
    return n


def cmd_build(paths: list[Path]) -> int:
    files, errs = artefacts(paths or None)
    n = write_files(files)
    print(f"{len(files)} files generated, {n} written")
    for e in errs:
        print("  LINT:", e)
    return 1 if errs else 0


def cmd_check() -> int:
    files, errs = artefacts()
    bad = 0
    for e in errs:
        print("LINT:", e)
        bad += 1
    for path, text in sorted(files.items()):
        rel = path.relative_to(ROOT)
        if not path.exists():
            print(f"{rel}: missing; run tools/gen_figures.py build")
            bad += 1
        elif path.read_text(encoding="utf-8") != text:
            print(f"{rel}: out of date; run tools/gen_figures.py build")
            for line in list(difflib.unified_diff(
                    path.read_text(encoding="utf-8").splitlines(), text.splitlines(),
                    "committed", "generated", lineterm="", n=0))[:12]:
                print("   ", line)
            bad += 1
    # Anything under the generated directories that no spec accounts for, whatever its
    # extension: a stray file there is either a leftover or something hand-made.
    stale = {q for q in OUT_DIR.iterdir() if q.is_file()} - set(files)
    stale |= {q for q in MYST_DIR.iterdir() if q.is_file()} - set(files)
    for q in sorted(stale):
        print(f"{q.relative_to(ROOT)}: no spec generates this file")
        bad += 1
    # The block pasted into a page must be present, and must be the generated one, character
    # for character: a deleted block, or one whose :name:, :alt: or caption was edited, is a
    # page that no longer says what the figure says.
    for spec_path in sorted(SPEC_DIR.glob("*.yaml")):
        spec = load_spec(spec_path)
        if "kind" not in spec or not spec.get("page"):
            continue
        page = ROOT / spec["page"]
        if not page.exists():
            print(f"{spec['page']}: the target page of fig-{spec['id']} does not exist")
            bad += 1
            continue
        for line in page_block_problems(spec, page.read_text(encoding="utf-8")):
            print(line)
            bad += 1
    # Nothing from a patent that is not certainly expired may sit in a committed SVG either:
    # the label and panel text lives only there, where no page checker would ever read it.
    for q in sorted(OUT_DIR.glob("*.svg")):
        try:
            root = ET.fromstring(q.read_text(encoding="utf-8"))
        except ET.ParseError as exc:
            print(f"{q.relative_to(ROOT)}: not well-formed XML ({exc})")
            bad += 1
            continue
        strings = [el.text or "" for el in root.iter() if el.text]
        for hit in inforce_hits(" ".join(strings), str(q.relative_to(ROOT))):
            print(hit)
            bad += 1
    print(f"{len(files)} generated files checked, {bad} problem(s)")
    return 1 if bad else 0


# --------------------------------------------------------------------------- selftest
_SERIES_OK = {
    "substrate": {"material": "si-sub", "depth": 60,
                  "label": {"title": "Silicon wafer", "note": "p-type substrate", "basis": "public"}},
    "ops": [
        {"step": "002", "op": "deposit", "id": "padox", "material": "oxide-thermal", "t": 6,
         "label": {"title": "Pad oxide", "note": "step 002", "basis": "public"}},
    ],
}


def _spec_ok() -> dict:
    return {
        "id": "selftest", "kind": "xsection", "page": None, "series": "x.yaml",
        "alt": "A test cross-section used only by the self-test of the figure generator, long "
               "enough to satisfy the minimum alt-text length that the lint enforces.",
        "caption": "A self-test figure. Not to scale.",
        "panels": [{"state_after": "002", "title": "Only panel"}],
    }


def selftest() -> int:
    import copy
    cases: list[tuple[str, dict, dict, str]] = []

    def case(name, mutate, needle, series=None):
        s = _spec_ok()
        ser = copy.deepcopy(series or _SERIES_OK)
        mutate(s, ser)
        cases.append((name, s, ser, needle))

    case("alt too short", lambda s, r: s.update(alt="Too short."), "alt text must be 60-450")
    case("alt with a citation",
         lambda s, r: s.update(alt=s["alt"] + " See[^pdk-04] for the numbers behind this drawing."),
         "must not carry citations")
    case("caption missing", lambda s, r: s.update(caption=""), "caption missing")
    case("no 'Not to scale' in the caption",
         lambda s, r: s.update(caption="A self-test figure."), "must end with 'Not to scale.'")
    case("unknown kind", lambda s, r: s.update(kind="doodle"), "unknown kind")
    case("a close-up the caption does not declare",
         lambda s, r: s.update(close_up=[100, 200]), "does not say so ('close-up of")
    case("a full slice cut off at the bottom the caption does not declare",
         lambda s, r: s.update(crop_depth=-20), "does not say 'the lower part")
    case("a close-up cut off at the bottom the caption does not declare",
         lambda s, r: s.update(close_up=[100, 200], crop_depth=-20,
                               caption="A close-up of part of the slice. Not to scale."),
         "does not say 'the lower part")
    case("a cut-off close-up whose caption only mentions a cut",
         lambda s, r: s.update(close_up=[100, 200], crop_depth=-20,
                               caption="A close-up of part of the slice; the resist is cut off. Not to scale."),
         "does not say 'the lower part")
    case("unknown basis",
         lambda s, r: r["ops"][0]["label"].update(basis="guess"), "unknown basis")
    case("a number beside a step code, without a cite",
         lambda s, r: r["ops"][0]["label"].update(note="NILD3_C, 0.030 µm"), "needs cite:")
    case("a thickness beside a step code, without a cite",
         lambda s, r: r["ops"][0]["label"].update(note="TIN2 liner, 20 nm"), "needs cite:")
    case("a number without a cite",
         lambda s, r: r["ops"][0]["label"].update(note="about 0.12 µm thick"),
         "needs cite:")
    case("a film thinner than the minimum",
         lambda s, r: r["ops"][0].update(t=2), "drawn thinner than")
    case("unknown material",
         lambda s, r: r["ops"][0].update(material="unobtainium"), "unknown material")
    case("three panels",
         lambda s, r: s.update(panels=[dict(state_after="002", title=f"Panel {i}") for i in range(3)]),
         "at most two")
    case("three header callouts",
         lambda s, r: s["panels"][0].update(callouts=[
             {"x": 30 + 60 * i, "y": 0, "label": {"title": f"Callout {i}", "basis": "public"}}
             for i in range(3)]),
         "header callouts; at most 2")
    case("a reading not marked 'not public'",
         lambda s, r: r["ops"][0]["label"].update(basis="reading", note="about 0.12 µm", cite="pdk-04"),
         "must say 'not public' first")
    case("a stack chart that is not to scale",
         lambda s, r: s.update(kind="stack", to_scale=False, layers=[], axis={}, title="t", footer="f"),
         "must declare to_scale: true")
    case("a to-scale chart without 'To scale' in the caption",
         lambda s, r: s.update(kind="stack", to_scale=True, title="t", footer="f",
                               axis={"unit": "µm", "label": "l", "tick": 1},
                               layers=[{"material": "si-sub", "t": 1}],
                               caption="A self-test chart."),
         "must say 'To scale'")
    case("a value that is not public drawn to scale",
         lambda s, r: s.update(kind="stack", to_scale=True, title="t", footer="f",
                               axis={"unit": "µm", "label": "l", "tick": 1},
                               caption="A self-test chart. To scale.",
                               layers=[{"material": "si-sub", "t": 1,
                                        "label": {"title": "L", "note": "not public; about 1 µm",
                                                  "basis": "reading", "cite": "pdk-04"}}]),
         "may not be drawn to scale")

    bad = 0
    for name, spec, series, needle in cases:
        errs = lint_spec(spec, series)
        if not any(needle in e for e in errs):
            print(f"SELFTEST FAIL: {name!r} did not report {needle!r}; got {errs}")
            bad += 1
    # ---- series templates and bases (S9: one via/metal sequence, instantiated per level)
    def tpl_raw():
        return {
            "substrate": copy.deepcopy(_SERIES_OK["substrate"]),
            "templates": {"film": {
                "params": ["s", "t", "code", "steps"],
                "defaults": {"mat": "oxide-dep"},
                "ops": [{"step": "${s}", "op": "deposit", "id": "f${s}", "material": "${mat}",
                         "t": "${t}", "label": {"title": "Film", "note": "${code}, step ${steps.dep}",
                                                "basis": "public"}}]}},
            "ops": [{"use": "film", "with": {"s": "002", "t": 6, "code": "NILD3",
                                              "steps": {"dep": "002"}}},
                    {"use": "film", "with": {"s": "003", "t": 7, "code": "NILD4", "mat": "nitride",
                                              "steps": {"dep": "003"}}}],
        }
    ex = expand_series(tpl_raw(), "selftest.yaml")
    want = [{"step": "002", "op": "deposit", "id": "f002", "material": "oxide-dep", "t": 6,
             "label": {"title": "Film", "note": "NILD3, step 002", "basis": "public"}},
            {"step": "003", "op": "deposit", "id": "f003", "material": "nitride", "t": 7,
             "label": {"title": "Film", "note": "NILD4, step 003", "basis": "public"}}]
    if ex.get("_errors") or ex["ops"] != want:
        print(f"SELFTEST FAIL: a template did not expand as written: {ex.get('_errors')} {ex['ops']}")
        bad += 1
    elif lint_spec(_spec_ok(), ex):
        print(f"SELFTEST FAIL: a clean templated series reported {lint_spec(_spec_ok(), ex)}")
        bad += 1
    iso = load_spec(SPEC_DIR / "series-isolation.yaml")
    based = expand_series({"base": "series-isolation.yaml",
                           "ops": [{"step": "014", "op": "strip", "materials": ["resist"]}]},
                          "selftest.yaml")
    if based.get("_errors") or based["ops"] != iso["ops"] + [
            {"step": "014", "op": "strip", "materials": ["resist"]}] \
            or based["substrate"] != iso["substrate"]:
        print(f"SELFTEST FAIL: a base series was not prepended unchanged: {based.get('_errors')}")
        bad += 1

    def tcase(name, mutate, needle):
        nonlocal bad
        raw = tpl_raw()
        mutate(raw)
        e = lint_spec(_spec_ok(), expand_series(raw, raw.pop("_name", "selftest.yaml")))
        if not any(needle in x for x in e):
            print(f"SELFTEST FAIL: {name!r} did not report {needle!r}; got {e}")
            bad += 1

    tops = lambda r: r["templates"]["film"]["ops"][0]              # noqa: E731
    tcase("a template refers to an undeclared parameter",
          lambda r: tops(r).update(t="${thick}"), "not declared in params or defaults")
    tcase("a template declares a parameter it never uses",
          lambda r: r["templates"]["film"]["params"].append("spare"), "declared but its ops never use it")
    tcase("a use leaves out a required parameter",
          lambda r: r["ops"][0]["with"].pop("t"), "required parameter 't' is missing")
    tcase("a use passes a parameter the template does not have",
          lambda r: r["ops"][0]["with"].update(tt=5), "'tt' is not a parameter of the template")
    tcase("a use names no template",
          lambda r: r["ops"][0].update(use="flim"), "no such template")
    tcase("a use with a stray field",
          lambda r: r["ops"][0].update(width=3), "unknown field 'width'")
    tcase("a dotted parameter without the key",
          lambda r: r["ops"][0]["with"].update(steps={}), "the parameter has no key 'dep'")
    tcase("a list parameter inside text",
          lambda r: r["ops"][0]["with"].update(code=[[0, 1]]), "cannot stand inside text")
    tcase("a template instantiated twice with the same ids",
          lambda r: r["ops"][1]["with"].update(s="002"), "is used twice in the series")
    tcase("ops out of step order",
          lambda r: r["ops"].reverse(), "the ops of a series run in step order")
    tcase("an unknown series field",
          lambda r: r.update(tempaltes={}), "unknown series field 'tempaltes'")
    tcase("an unknown template field",
          lambda r: r["templates"]["film"].update(param=["s"]), "unknown field 'param'")
    tcase("a base that is not a series file",
          lambda r: r.update(base="series-nosuch.yaml"), "is not a series file")
    tcase("a base that loops back",
          lambda r: r.update(base="series-isolation.yaml", _name="series-isolation.yaml"),
          "loops back")
    # cite keys are checked against the real page, and a restricted key is refused
    real = _spec_ok()
    real["page"] = "docs/steps/006-stie.md"
    ser = json.loads(json.dumps(_SERIES_OK))
    ser["ops"][0]["label"] = {"title": "Pad oxide", "note": "about 0.12 µm", "basis": "public",
                              "cite": "no-such-key"}
    if not any("is not defined on" in e for e in lint_spec(real, ser)):
        print("SELFTEST FAIL: an undefined cite key was accepted")
        bad += 1
    restricted = sorted(restricted_labels())
    if restricted:
        ser2 = json.loads(json.dumps(_SERIES_OK))
        ser2["ops"][0]["label"] = {"title": "Pad oxide", "note": "about 0.12 µm", "basis": "public",
                                   "cite": restricted[0]}
        real2 = _spec_ok()
        real2["page"] = None
        if not any("shown as in force" in e for e in lint_spec(real2, ser2)):
            print(f"SELFTEST FAIL: the in-force key {restricted[0]!r} was accepted")
            bad += 1
    else:
        print("SELFTEST NOTE: no restricted patent labels in the dataset; the in-force rule was not exercised")
    # H2: text baked into the SVG, the caption or the alt is screened with check_inforce's
    # own matcher, not only the cite key.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import check_inforce as _ci                                        # noqa: PLC0415
    fams = _ci.restricted_families(_ci.load_families())
    if fams:
        num = fams[0].numbers[0]
        phrase = (_ci.PHRASES.get(fams[0].representative) or [None])[0]
        probes = {"panel title": num, "arrow note": num}
        if phrase:
            probes["label note"] = phrase
        for where, text in probes.items():
            if not inforce_hits(text, where):
                print(f"SELFTEST FAIL: an in-force {where} ({text!r}) was accepted")
                bad += 1
        spec_bad = _spec_ok()
        spec_bad["panels"] = [{"state_after": "002", "title": f"Only panel, {num}"}]
        if not any("may never carry it" in e for e in lint_spec(spec_bad, _SERIES_OK)):
            print("SELFTEST FAIL: an in-force number in a panel title was accepted")
            bad += 1
        ser_arrow = json.loads(json.dumps(_SERIES_OK))
        spec_arrow = _spec_ok()
        spec_arrow["arrow"] = {"title": "T", "note": f"see {num}"}
        if not any("may never carry it" in e for e in lint_spec(spec_arrow, ser_arrow)):
            print("SELFTEST FAIL: an in-force number in the arrow note was accepted")
            bad += 1
    else:
        print("SELFTEST NOTE: no restricted patent families in the dataset; H2 was not exercised")
    # H3: a missing or hand-edited page block is a failure, not a silent pass.
    blk_spec = {"id": "selftest", "page": "docs/steps/006-stie.md", "caption": "A caption.",
                "alt": "An alt text long enough to pass the length rule that the lint applies "
                       "to every figure on this site."}
    if not any("no {figure} block named" in e for e in page_block_problems(blk_spec, "# a page\n")):
        print("SELFTEST FAIL: a missing figure block was accepted")
        bad += 1
    renamed = myst_block(blk_spec).replace(":name: fig-selftest", ":name: fig-something-else")
    if not any("no {figure} block named" in e for e in page_block_problems(blk_spec, renamed)):
        print("SELFTEST FAIL: a renamed figure block was accepted")
        bad += 1
    edited = myst_block(blk_spec).replace("A caption.", "A different caption.")
    if not any("is not the generated one" in e for e in page_block_problems(blk_spec, edited)):
        print("SELFTEST FAIL: a hand-edited figure block was accepted")
        bad += 1
    # H5: a state_after that is not a three-digit step, or is past the end of the series.
    for bad_state, needle in (("5", "not a three-digit"), ("999", "beyond the last step")):
        sp = _spec_ok()
        sp["panels"] = [{"state_after": bad_state, "title": "Only panel"}]
        if not any(needle in e for e in lint_spec(sp, _SERIES_OK)):
            print(f"SELFTEST FAIL: state_after {bad_state!r} was accepted")
            bad += 1
    # H6: three header callouts report a lint line and never abort the build.
    sp = _spec_ok()
    sp["panels"] = [{"state_after": "002", "title": "Only panel", "callouts": [
        {"x": 30 + 60 * i, "y": 0, "label": {"title": f"Callout {i}", "basis": "public"}}
        for i in range(3)]}]
    e3 = lint_spec(sp, _SERIES_OK)
    build_errs: list[str] = []
    build_xsection(sp, _SERIES_OK, build_errs)          # must not raise
    if not any("at most 2" in e for e in e3 + build_errs):
        print("SELFTEST FAIL: three header callouts did not report a lint line")
        bad += 1
    # An unknown operation, field, material and where_open are all errors.
    for mutate, needle in (
            (lambda r: r["ops"].append({"step": "003", "op": "sputter"}), "unknown operation"),
            (lambda r: r["ops"][0].update(colour="blue"), "unknown field"),
            (lambda r: r["ops"][0].update(only_on=["unobtainium"]), "unknown material or group"),
            (lambda r: r["ops"][0].update(where_open="nosuchlayer"), "where_open names no layer"),
            (lambda r: r["ops"][0].update(step="3"), "is not three digits"),
            (lambda r: r["ops"].append({"step": "003", "op": "dope", "id": "pn", "material": "sd-n",
                                        "host": "nosuchfilm"}), "names no film deposited earlier"),
            (lambda r: r["ops"].append({"step": "003", "op": "dope", "id": "pn", "material": "sd-n",
                                        "host": "padox", "where": [[300, 400]]}),
             "is absent everywhere the overlay is made")):
        ser = json.loads(json.dumps(_SERIES_OK))
        mutate(ser)
        if not any(needle in e for e in lint_spec(_spec_ok(), ser)):
            print(f"SELFTEST FAIL: {needle!r} was not reported")
            bad += 1
    # A doped overlay in a film (host:) fills that film, and nothing else, and follows it when a
    # later etch removes part of the film.
    ser_h = json.loads(json.dumps(_SERIES_OK))
    ser_h["ops"] += [
        {"step": "003", "op": "dope", "id": "pn", "material": "sd-n", "host": "padox", "where": [[0, 100]]},
        {"step": "004", "op": "etch", "materials": ["oxide-thermal"], "where": [[50, 268]]}]
    st_h = series_states(ser_h)[0]
    for key, xmax in (("003", 100), ("004", 50)):
        xs_h = st_h[key]
        ov_h = xs_h.layers["pn"]
        cols_h = xs_h.overlay_columns(ov_h)
        if (not cols_h or max(xs_h.x(i) for i in cols_h) > xmax
                or any(xs_h.overlay_band(ov_h, i) != tuple(xs_h.seg(i, "padox")[1:]) for i in cols_h)):
            print(f"SELFTEST FAIL: a hosted overlay does not fill its film only (state {key})")
            bad += 1
    # A bad y expression is a lint line, not a traceback.
    sp = _spec_ok()
    sp["panels"] = [{"state_after": "002", "title": "Only panel", "callouts": [
        {"x": 100, "y": "surface@100", "label": {"title": "C", "basis": "public"}}]}]
    ye: list[str] = []
    build_xsection(sp, _SERIES_OK, ye)
    if not any("bad y expression" in e for e in ye):
        print("SELFTEST FAIL: a bad y expression did not report a lint line")
        bad += 1
    # Faded layers: the caption must say so, the step's own layer may not be faded, and an
    # unknown id is an error.  An anneal gives its step a state; a dope ``z`` changes only
    # the painting order.
    ser_d = json.loads(json.dumps(_SERIES_OK))
    ser_d["ops"] += [
        {"step": "003", "op": "dope", "id": "band", "material": "implant", "follow": "surface",
         "from_surface": 0, "thickness": 8, "z": 1,
         "label": {"title": "Band", "note": "a thin implant", "basis": "public"}},
        {"step": "004", "op": "dope", "id": "well", "material": "well-p", "follow": "flat",
         "y_top": 0, "y_bot": -30, "label": {"title": "Well", "basis": "public"}},
        {"step": "005", "op": "anneal"}]
    sp = _spec_ok()
    sp["panels"] = [{"state_after": "005", "title": "Only panel", "dim_layers": ["band"]}]
    if not any("does not say which are drawn faded" in e for e in lint_spec(sp, ser_d)):
        print("SELFTEST FAIL: faded layers without a caption that says so were accepted")
        bad += 1
    sp["caption"] = "A self-test figure; the band is drawn faded. Not to scale."
    if lint_spec(sp, ser_d):
        print(f"SELFTEST FAIL: a clean spec with an anneal, a z and a faded layer reported "
              f"{lint_spec(sp, ser_d)}")
        bad += 1
    de: list[str] = []
    svg_d = build_xsection(sp, ser_d, de).render("auto")
    if de or svg_d.find('data-layer="band"') < svg_d.find('data-layer="well"'):
        print(f"SELFTEST FAIL: a z-ordered overlay was not painted over the later well ({de})")
        bad += 1
    if 'class="mat m-implant faded"' not in svg_d or ">Band<" in svg_d:
        print("SELFTEST FAIL: a faded layer was not drawn faded, or was labelled")
        bad += 1
    # The substrate's dot never lands on a well drawn over it.
    st_d = series_states(ser_d)[0]["005"]
    r_sub = choose_anchor(st_d, "sub", None)
    if r_sub[3] > -30 + 1e-6:
        print(f"SELFTEST FAIL: the substrate's dot may sit on the well above it ({r_sub})")
        bad += 1
    for panel, needle in (({"state_after": "003", "title": "P", "dim_layers": ["band"]},
                           "it must be labelled, not faded"),
                          ({"state_after": "005", "title": "P", "dim_layers": ["nosuch"]},
                           "dim_layers names no layer")):
        sp = _spec_ok()
        sp["caption"] = "Drawn faded. Not to scale."
        sp["panels"] = [panel]
        de = []
        build_xsection(sp, ser_d, de)
        if not any(needle in e for e in de):
            print(f"SELFTEST FAIL: {needle!r} was not reported; got {de}")
            bad += 1
    # The one-panel rule, the faded-name rule, the tilt rule and the series field checks.
    ser_n = json.loads(json.dumps(ser_d))
    ser_n["ops"].append({"step": "006", "op": "ions", "where": [[0, 100]],
                         "label": {"title": "Beam", "basis": "public"}})
    two = _spec_ok()
    two["caption"] = "Two copies. Not to scale."
    two["panels"] = [{"state_after": "004", "title": "A"}, {"state_after": "005", "title": "B"}]
    e_two: list[str] = []
    build_xsection(two, ser_n, e_two)
    one = _spec_ok()
    one.update(no_drawn_change=True, caption="One panel; no mention of the beam's lean. Not to scale.",
               arrow={"title": "T", "note": "n"},
               panels=[{"state_after": "006", "title": "Wrong title"}, {"state_after": "006", "title": "x"}])
    e_one = lint_spec(one, ser_n)
    changed = _spec_ok()
    changed.update(no_drawn_change=True, panels=[{"state_after": "004", "title": NO_CHANGE_TITLE}])
    e_changed: list[str] = []
    build_xsection(changed, ser_n, e_changed)
    beam = _spec_ok()
    beam["panels"] = [{"state_after": "006", "title": "P"}]
    e_beam: list[str] = []
    build_xsection(beam, ser_n, e_beam)
    named = _spec_ok()
    named.update(caption="Something is drawn faded. Not to scale.",
                 panels=[{"state_after": "005", "title": "P", "dim_layers": ["well"]}])
    ser_bad = json.loads(json.dumps(ser_d))
    ser_bad["ops"][1]["z"] = "high"
    ser_bad["ops"][1]["route"] = "sideways"
    ser_bad["note_order"] = "newset"
    ser_bad["colour"] = "blue"
    e_bad = lint_spec(_spec_ok(), ser_bad)
    ser_anc = json.loads(json.dumps(ser_d))
    ser_anc["ops"][2]["anchor_y"] = -300
    anc = _spec_ok()
    anc["panels"] = [{"state_after": "005", "title": "P"}]
    e_anc: list[str] = []
    build_xsection(anc, ser_anc, e_anc)
    for got, needle in ((e_two, "identical geometry"), (e_one, "exactly one panel"),
                        (e_one, "has no arrow"), (e_changed, "differs from step"),
                        (e_beam, "nothing about the tilt"), (lint_spec(named, ser_d), "does not name it"),
                        (e_bad, "z must be a number"), (e_bad, "route 'sideways'"),
                        (e_bad, "note_order 'newset'"), (e_bad, "unknown top-level field"),
                        (e_anc, "anchor_y -300 is not at least 3 u inside")):
        if not any(needle in e for e in got):
            print(f"SELFTEST FAIL: {needle!r} was not reported; got {got}")
            bad += 1
    one_ok = _spec_ok()
    one_ok.update(no_drawn_change=True, panels=[{"state_after": "005", "title": NO_CHANGE_TITLE}])
    e_ok: list[str] = []
    build_xsection(one_ok, ser_n, e_ok)
    if e_ok or lint_spec(one_ok, ser_n):
        print(f"SELFTEST FAIL: a clean no_drawn_change figure reported {e_ok + lint_spec(one_ok, ser_n)}")
        bad += 1
    # A figure between a lead and the dropdown that follows it.
    blk2 = {"id": "selftest", "page": "docs/steps/006-stie.md", "caption": "A caption.",
            "alt": "An alt text long enough to pass the length rule that the lint applies "
                   "to every figure on this site."}
    page_txt = "Lead.\n\n" + myst_block(blk2) + "\n:::{dropdown} Note\nx\n:::\n"
    if not any("goes after it" in e for e in page_block_problems(blk2, page_txt)):
        print("SELFTEST FAIL: a figure between a lead and its dropdown was accepted")
        bad += 1
    # Faded layers must add no colour; with a fill they would, and the palette check says so.
    if faded_report() or not faded_report(0.35):
        print("SELFTEST FAIL: the faded-layer palette check does not separate a ghost from a tint")
        bad += 1
    # Leaders: a long run through another material, a run along an edge, a cut through a beam.
    base = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 200" data-kind="chain"><title>t</title>'
            f'<desc>d</desc><g data-rect="12,10,268,180"></g>')
    lint_cases = [
        (base + '<polygon class="mat m-si-sub" data-layer="sub" points="12,10 280,10 280,190 12,190"/>'
                '<polygon class="mat m-well-n" data-layer="nw" points="20,50 30,50 30,60 20,60"/>'
                '<path class="leader" data-owner="nw" d="M25 55H300"/></svg>', "through other materials"),
        (base + '<polygon class="mat m-si-sub" data-layer="a" points="12,10 280,10 280,100 12,100"/>'
                '<path class="leader" data-owner="a" d="M40 102H300"/></svg>', "alongside a material edge"),
        # the accent trace of a highlight counts as an edge, and 5 u off is still too close
        (base + '<polyline class="hl" points="30,150 280,150"/>'
                '<path class="leader" data-owner="a" d="M40 145H300"/></svg>', "alongside a material edge"),
        (base + '<path class="ion" d="M100 20L100 80"/>'
                '<path class="leader" data-owner="a" d="M40 50H300"/></svg>', "cuts through the ion beam"),
        (base.replace('data-kind="chain"', 'data-kind="xsection"')
         + '<path class="leader" data-owner="a" d="M270 20H290V150H300"/>'
           '<path class="leader" data-owner="b" d="M270 24H296V160H300"/></svg>', "descend side by side"),
        (base.replace('data-kind="chain"', 'data-kind="xsection"').replace("12,10,268,180", "12,10,268,60")
         + '<text x="12" y="8" class="t-panel-title">P</text>'
           '<text x="300" y="150" class="t-label-title">Low</text></svg>', "below the bottom of its drawing"),
    ]
    for raw, needle in lint_cases:
        if not any(needle in e for e in lint_svg_text(raw)):
            print(f"SELFTEST FAIL: SVG case {needle!r} was not reported; got {lint_svg_text(raw)}")
            bad += 1
    # The text-overlap rule is reachable from a real figure, not only from hand-written SVG.
    _real = _place_right
    try:
        globals()["_place_right"] = lambda rights, floor: (
            [setattr(l, "y", floor + 2) or setattr(l, "ay", floor + 2) for l in rights],
            floor + 2)[1]
        ovl: list[str] = []
        svg = build_xsection(_spec_ok(), _SERIES_OK, ovl)
        if not any("text overlap" in e for e in lint_svg_text(svg.render("auto"))):
            print("SELFTEST FAIL: the text-overlap rule did not fire with a broken placer")
            bad += 1
    finally:
        globals()["_place_right"] = _real
    # the SVG lint fires on a broken SVG
    svg_cases = [
        ("canvas width", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 100" data-kind="xsection">'
                         f'<title>t</title><desc>d</desc></svg>', "canvas width"),
        ("colour not a token", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain">'
                               f'<title>t</title><desc>d</desc><style>.x{{fill:#ff00ff}}</style></svg>',
         "is not a token"),
        ("literal fill", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain">'
                         f'<title>t</title><desc>d</desc><rect fill="#123456"/></svg>', "literal fill/stroke"),
        ("missing title", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain">'
                          f'<desc>d</desc></svg>', "missing <title>"),
        ("text below the minimum size",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain"><title>t</title>'
         f'<desc>d</desc><text x="20" y="20" class="t-tiny">x</text></svg>', "type-scale class"),
        ("text outside the margins",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain"><title>t</title>'
         f'<desc>d</desc><text x="2" y="20" class="t-label-note">outside</text></svg>', "escapes the canvas"),
        ("text overlap",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain"><title>t</title>'
         f'<desc>d</desc><text x="20" y="20" class="t-label-note">aaaa</text>'
         f'<text x="22" y="21" class="t-label-note">bbbb</text></svg>', "text overlap"),
        ("text inside a drawing",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain"><title>t</title>'
         f'<desc>d</desc><g data-rect="12,10,200,60"></g><text x="20" y="40" class="t-label-note">in</text></svg>',
         "inside a drawing area"),
        ("leader touching text",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain"><title>t</title>'
         f'<desc>d</desc><text x="60" y="40" class="t-label-note">hit</text>'
         f'<path class="leader" data-owner="a" d="M20 38H120"/></svg>', "touches text"),
        ("leaders crossing",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="chain"><title>t</title>'
         f'<desc>d</desc><path class="leader" data-owner="a" d="M20 20L120 60"/>'
         f'<path class="leader" data-owner="b" d="M20 60L120 20"/></svg>', "leaders cross"),
        ("a riser hugging a material edge",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 200" data-kind="chain"><title>t</title>'
         f'<desc>d</desc><polygon class="mat m-si-sub" points="100,40 102,40 102,160 100,160"/>'
         f'<path class="leader" data-owner="a" d="M99 150V30"/></svg>', "within 5 u of a material edge"),
        ("a cross-section with no 'Not to scale'",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="xsection"><title>t</title>'
         f'<desc>d</desc></svg>', "without the 'Not to scale' line"),
        ("a cross-section with no panel title",
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" data-kind="xsection"><title>t</title>'
         f'<desc>d</desc><text x="12" y="40" class="t-label-note">{NOT_TO_SCALE}</text></svg>',
         "without a panel title"),
    ]
    hdr = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 400" data-kind="chain"><title>t</title>'
           f'<desc>d</desc>')
    svg_cases += [
        ("a dot on its drawing's edge",
         hdr.replace('data-kind="chain"', 'data-kind="xsection"')
         + '<g class="drawing" data-rect="12,20,268,100">'
         '<polygon class="mat m-barrier" data-layer="m" points="12,40 280,40 280,60 12,60"/></g>'
         '<circle class="dot" data-owner="m" cx="280" cy="50" r="1.9"/></svg>',
         "from its drawing's edge"),
        ("a dot on the material painted over the one it names",
         hdr + '<g class="drawing" data-rect="12,20,268,100">'
         '<polygon class="mat m-implant" data-layer="halo" points="20,40 200,40 200,80 20,80"/>'
         '<polygon class="mat m-tip-n" data-layer="tipn" points="20,40 200,40 200,60 20,60"/></g>'
         '<circle class="dot" data-owner="halo" cx="100" cy="50" r="1.9"/></svg>',
         "the top-most material painted at the dot of 'halo' is 'tipn'"),
        ("an ion label's leader through a material inside its drawing",
         hdr + '<g class="drawing" data-rect="12,20,268,100">'
         '<polygon class="mat m-si-sub" data-layer="sub" points="12,60 280,60 280,380 12,380"/></g>'
         '<path class="leader" data-owner="ions" d="M150 90V70"/></svg>',
         "the ion-beam label's leader runs through"),
    ]
    svg_cases += [
        ("a leader rising inside an ion beam",
         hdr + '<path class="ion" d="M100 20L100 90"/><path class="ion" d="M130 20L130 90"/>'
         '<path class="leader" data-owner="x" d="M108 95V15H300"/></svg>', "rises inside the ion beam"),
        ("a beam label's dot on an arrow tail",
         hdr + '<path class="ion" d="M100 20L100 90"/>'
         '<circle class="dot" data-owner="ions" cx="100" cy="20" r="1.9"/></svg>', "sits on an arrow's tail"),
        ("two over-runs a pair of lines apart",
         hdr + '<path class="leader" data-owner="a" d="M40 90V30H300"/>'
         '<path class="leader" data-owner="b" d="M60 90V37H300"/></svg>', "at least 10 u apart"),
    ]
    # ... but not through the part of a polygon that runs on below its drawing's clip
    clipped = (hdr + '<g class="drawing" data-rect="12,20,268,100">'
               '<polygon class="mat m-si-sub" data-layer="sub" points="12,60 280,60 280,380 12,380"/></g>'
               '<path class="leader" data-owner="ions" d="M150 300V250"/></svg>')
    if any("ion-beam label's leader runs through" in e for e in lint_svg_text(clipped)):
        print("SELFTEST FAIL: rule 16 counts a polygon outside its drawing's clip rectangle")
        bad += 1
    # rule 18 likewise: a run through the next panel's drawing does not cross the substrate of
    # the panel above, which runs on below its own clip; a run inside that drawing does
    two = (hdr + '<g class="drawing" data-rect="12,20,268,100">'
           '<polygon class="mat m-si-sub" data-layer="sub" points="12,60 280,60 280,380 12,380"/></g>'
           '<g class="drawing" data-rect="12,250,268,100"></g>'
           '<path class="leader" data-owner="x" d="M20 {y}H270"/></svg>')
    # rule 18, risers: a long riser up through a stack of four films is refused; the same
    # riser up through one thick fill is not
    stack4 = "".join(f'<polygon class="mat m-oxide-dep" data-layer="f{k}" '
                     f'points="12,{30 + 20 * k} 280,{30 + 20 * k} 280,{50 + 20 * k} 12,{50 + 20 * k}"/>'
                     for k in range(4))
    fill1 = '<polygon class="mat m-oxide-dep" data-layer="f0" points="12,30 280,30 280,110 12,110"/>'
    for body, want in ((stack4, True), (fill1, False)):
        raw = (hdr + '<g class="drawing" data-rect="12,20,268,120">' + body
               + '<polygon class="mat m-si-sub" data-layer="own" points="12,110 280,110 280,140 12,140"/></g>'
               '<path class="leader" data-owner="own" d="M150 120V22H300"/></svg>')
        got = any("reads as a contact or a plug" in e for e in lint_svg_text(raw))
        if got != want:
            print(f"SELFTEST FAIL: rule 18 risers: {'stack' if want else 'fill'} reported={got}")
            bad += 1
    # rule 18, one film: a leader that runs 30 u along inside one other film is refused (the
    # rounded shoulder of a gate film beside a resistor body); 20 u across one is not
    for width, want in ((30, True), (20, False)):
        raw = (hdr + '<g class="drawing" data-rect="12,20,268,120">'
               f'<polygon class="mat m-poly" data-layer="g" points="100,40 {100 + width},40 '
               f'{100 + width},60 100,60"/></g>'
               '<path class="leader" data-owner="own" d="M90 50H300"/></svg>')
        got = any("inside one other film" in e for e in lint_svg_text(raw))
        if got != want:
            print(f"SELFTEST FAIL: rule 18 one film: a {width} u run reported={got}")
            bad += 1
    for y_run, want in ((300, False), (90, True)):
        got = any("runs" in e and "through other materials" in e
                  for e in lint_svg_text(two.format(y=y_run)))
        if got != want:
            print(f"SELFTEST FAIL: rule 18 clip: a run at y {y_run} reported={got}")
            bad += 1
    for name, raw, needle in svg_cases:
        errs = lint_svg_text(raw)
        if not any(needle in e for e in errs):
            print(f"SELFTEST FAIL: SVG case {name!r} did not report {needle!r}; got {errs}")
            bad += 1
    # a close-up enlarges one window of a state, in both directions, and moves nothing else
    xs0 = XSection({"material": "si-sub", "depth": 40})
    xs0.apply({"op": "deposit", "id": "f", "material": "oxide-thermal", "t": 6, "where": [[100, 140]]})
    xs0.apply({"op": "dope", "id": "d", "material": "sd-n", "where": [[120, 200]], "thickness": 5})
    zx = xs0.window(94, 161)
    zf = DRAW_W / 67
    col_in = zx.cols[zx.idx((110 - 94) * zf)]
    if not (abs(col_in[-1][2] - 6 * zf) < 1e-6 and abs(col_in[0][1] + 40) < 1e-6):
        print(f"SELFTEST FAIL: a close-up does not scale heights by the zoom: {col_in}")
        bad += 1
    if abs(zx.overlays[0]["where"][0][0] - (120 - 94) * zf) > 1e-6 or xs0.overlays[0]["where"] != [[120, 200]]:
        print("SELFTEST FAIL: a close-up must move a doped region's extent and leave the series' own alone")
        bad += 1
    # an ion arrow points the way the ions travel: down, and for a tilted beam to the left
    for tilt_deg in (0.0, 7.0, 40.0):
        shaft, head = ion_arrow(100.0, 200.0, 40.0, math.radians(tilt_deg))
        hp = [float(v) for v in re.findall(r"-?[\d.]+", head)]
        cx, cy = (hp[0] + hp[2] + hp[4]) / 3, (hp[1] + hp[3] + hp[5]) / 3
        tail = [float(v) for v in re.findall(r"-?[\d.]+", shaft)][:2]
        if not (cy < hp[1] and (tail[0] - hp[0]) * (cx - hp[0]) + (tail[1] - hp[1]) * (cy - hp[1]) > 0):
            print(f"SELFTEST FAIL: the ion arrowhead at {tilt_deg} degrees points back up the beam")
            bad += 1
    # a close-up moves a panel's positions into its own coordinates
    zp = _zoom_panel({"highlight": {"where": [[100, 150]]}, "callouts": [{"x": 120, "y": "top@120"}],
                      "dims": [{"x": 110, "y0": 0, "y1": 10, "witness": [[100, 130]]}]}, 100, 2.0)
    if (zp["highlight"]["where"] != [[0.0, 100.0]] or zp["callouts"][0]["x"] != 40.0
            or zp["callouts"][0]["y"] != "top@40.00" or zp["dims"][0]["y1"] != 20.0
            or zp["dims"][0]["witness"] != [[0.0, 60.0]]):
        print(f"SELFTEST FAIL: _zoom_panel moved the panel's positions wrongly: {zp}")
        bad += 1
    # a close-up window has to be a sensible range
    for rng in ([100, 120], [200, 100], [0, 400], "wide"):
        e: list[str] = []
        sp = _spec_ok()
        sp["close_up"] = rng
        build_xsection(sp, copy.deepcopy(_SERIES_OK), e)
        if not any("close_up must be" in x for x in e):
            print(f"SELFTEST FAIL: close_up {rng!r} was accepted")
            bad += 1
    # a thin patterned film follows the surface only inside its ranges
    xs1 = XSection({"material": "si-sub", "depth": 40})
    xs1.apply({"op": "deposit", "id": "g", "material": "poly", "t": 20, "where": [[60, 80]]})
    xs1.apply({"op": "deposit", "id": "r", "material": "resist", "t": 6, "flat": False,
               "where": [[40, 120]]})
    if not (xs1.top(xs1.idx(70)) == 26 and xs1.top(xs1.idx(100)) == 6 and xs1.top(xs1.idx(20)) == 0):
        print("SELFTEST FAIL: a conformal patterned film (flat: false, where) is wrong")
        bad += 1
    # a contact silicide replaces the top of the silicon under the liner, only where the liner
    # touches silicon, and a doped region under it keeps its depth from the original surface
    xs2 = XSection({"material": "si-sub", "depth": 60})
    xs2.apply({"op": "deposit", "id": "ox", "material": "oxide-dep", "t": 20, "where": [[0, 100]]})
    xs2.apply({"op": "deposit", "id": "m", "material": "barrier", "t": 5})
    xs2.apply({"op": "dope", "id": "sd", "material": "sd-n", "follow": "surface",
               "from_surface": 0, "thickness": 14})
    xs2.apply({"op": "react", "id": "s", "material": "silicide", "consumes": ["si-sub"],
               "under": ["barrier"], "t": 5})
    i_on, i_off = xs2.idx(200), xs2.idx(50)
    band = xs2.overlay_band(xs2.layers["sd"], i_on)
    if not (xs2.seg(i_on, "s") == ["s", -5.0, 0.0] and xs2.seg(i_off, "s") is None
            and band == (-14.0, -5.0) and xs2.overlay_band(xs2.layers["sd"], i_off) == (-14.0, 0.0)):
        print("SELFTEST FAIL: react (a contact silicide) or the doped region under it is wrong")
        bad += 1
    # a conformal film grows normal to the surface: in a tapered hole it keeps its thickness on
    # the wall, rounds the top corner and leaves the bottom open (a square element would fill
    # the bottom corners and stand t higher at the corner)
    xs3 = XSection({"material": "si-sub", "depth": 60})
    xs3.apply({"op": "deposit", "id": "ox", "material": "oxide-dep", "t": 40})
    xs3.apply({"op": "etch", "materials": ["oxide-dep"], "where": [[100, 140]], "depth": 40,
               "taper_deg": 10})
    xs3.apply({"op": "deposit", "id": "m", "material": "barrier", "t": 5})
    tn10 = math.tan(math.radians(10))
    x_wall = 100 + 20 * tn10 + 5 / math.cos(math.radians(10))      # the film face at height 20
    corner = xs3.top(xs3.idx(100 + 5 / math.sqrt(2)))
    if not (xs3.seg(xs3.idx(120), "m") == ["m", 0.0, 5.0]
            and abs(xs3.top(xs3.idx(x_wall)) - 20) < 1.5
            and abs(corner - (40 + 5 / math.sqrt(2))) < 0.6):
        print(f"SELFTEST FAIL: a conformal film is not grown normal to the surface: bottom "
              f"{xs3.seg(xs3.idx(120), 'm')}, wall {xs3.top(xs3.idx(x_wall)):.2f} (20), corner "
              f"{corner:.2f} ({40 + 5 / math.sqrt(2):.2f})")
        bad += 1
    # a tapered wall cut through a stack of films is one straight line in the drawing: every
    # vertex of every film's polygon that lies on the wall sits on the wall's line
    xs4 = XSection({"material": "si-sub", "depth": 60})
    for lid, th in (("a", 7), ("b", 13), ("c", 3), ("d", 17)):
        xs4.apply({"op": "deposit", "id": lid, "material": "oxide-dep", "t": th})
    xs4.apply({"op": "etch", "materials": ["oxide-dep"], "where": [[100, 160]], "depth": 40,
               "taper_deg": 10})
    worst = 0.0
    for lid in "abcd":
        for poly in xs4.polygons(lid):
            for x, y in poly:
                if 99 < x < 100 + 40 * tn10 + 1 and 0 < y < 40:     # the left wall's band
                    worst = max(worst, abs(x - (100 + (40 - y) * tn10)))
    if worst > 0.05:
        print(f"SELFTEST FAIL: a tapered wall through a stack of films is not straight "
              f"(a vertex {worst:.2f} u off the wall's line)")
        bad += 1
    # a gap-filling deposit fills from the bottom, adds nothing on a wall, is t over a wide
    # line with facets from its edges, and peaks over a narrow line
    xs5 = XSection({"material": "si-sub", "depth": 60})
    xs5.apply({"op": "deposit", "id": "p", "material": "poly", "t": 20, "where": [[50, 60]]})
    xs5.apply({"op": "deposit", "id": "q", "material": "poly", "t": 20, "where": [[100, 180]]})
    xs5.apply({"op": "deposit", "id": "g", "material": "psg", "t": 10, "profile": "gapfill"})
    got = [round(xs5.top(xs5.idx(x)), 2) for x in (55, 64, 104, 140, 250)]
    # (the line [50, 60] covers the samples 50..60, so its edges lie a quarter-sample outside)
    if any(abs(a - b) > 0.6 for a, b in zip(got, (25.0, 10.0, 24.0, 30.0, 10.0))):
        print(f"SELFTEST FAIL: a gap-filling deposit has the wrong profile: {got}, "
              "expected [25.0, 10.0, 24.0, 30.0, 10.0]")
        bad += 1
    xs5.apply({"op": "deposit", "id": "h", "material": "psg", "t": 10, "profile": "gapfill",
               "smooth": 30})
    thick = [xs5.top(i) - xs5.seg(i, "g")[2] for i in range(xs5.n)]
    if min(thick) < GAPFILL_MIN - 1e-6 or max(thick) > 10 + 1e-6:
        print(f"SELFTEST FAIL: a flowed gap-filling deposit leaves its bounds: {min(thick):.2f}..{max(thick):.2f}")
        bad += 1
    # a deposit profile must be a known one
    for bad_op, needle in (({"profile": "blob"}, "is not one of"),
                           ({"facet_deg": 30}, "belong to profile: gapfill")):
        ser = copy.deepcopy(_SERIES_OK)
        ser["ops"][0].update(bad_op)
        if not any(needle in e for e in lint_spec(_spec_ok(), ser)):
            print(f"SELFTEST FAIL: a deposit with {bad_op} was accepted")
            bad += 1
    # lint 17: a thin plain film may touch a thick patterned film of a similar colour; a thin
    # patterned one may not
    for t_ox, t_psg, want in ((5, 30, False), (30, 5, True)):
        ser = {"substrate": {"material": "si-sub", "depth": 60},
               "ops": [{"step": "002", "op": "deposit", "id": "ox", "material": "oxide-dep",
                        "t": t_ox, "label": {"title": "Oxide", "basis": "public"}},
                       {"step": "003", "op": "deposit", "id": "pg", "material": "psg",
                        "t": t_psg, "label": {"title": "Glass", "basis": "public"}}]}
        sp = _spec_ok()
        sp["panels"] = [{"state_after": "003", "title": "Only panel"}]
        e = []
        raw = build_xsection(sp, ser, e).render("auto")
        got = any("where a pattern may not show" in x for x in lint_svg_text(raw))
        if got != want:
            print(f"SELFTEST FAIL: lint 17 on {t_ox} u oxide under {t_psg} u PSG: fired={got}")
            bad += 1
    # a step or level code is an identifier, not a number: no cite, no "not public" first
    for note, basis in (("polished at NILD3", "public"), ("NILD3", "reading")):
        ser = copy.deepcopy(_SERIES_OK)
        ser["ops"][0]["label"].update(note=note, basis=basis)
        e = [x for x in lint_spec(_spec_ok(), ser) if "needs cite" in x or "not public" in x]
        if e:
            print(f"SELFTEST FAIL: the note {note!r} ({basis}) was read as a number: {e}")
            bad += 1
    # a clean spec must lint clean
    clean = _spec_ok()
    if lint_spec(clean, _SERIES_OK):
        print(f"SELFTEST FAIL: the clean spec reported {lint_spec(clean, _SERIES_OK)}")
        bad += 1
    # every kind renders and passes the SVG lint
    demo = {
        "stack": {"id": "d", "kind": "stack", "to_scale": True, "title": "Demo stack",
                  "axis": {"unit": "µm", "label": "Height above the silicon surface", "tick": 0.5},
                  "layers": [{"id": "a", "material": "si-sub", "t": 0.4,
                              "label": {"title": "Silicon", "basis": "public"}},
                             {"id": "b", "material": "oxide-dep", "t": 0.9,
                              "label": {"title": "Oxide", "basis": "public"}}],
                  "footer": "To scale.",
                  "alt": "A demonstration stack chart used by the self-test of the figure generator, with two "
                         "layers drawn to scale beside a vertical axis in micrometres.",
                  "caption": "A demonstration chart. To scale."},
        "chain": {"id": "d", "kind": "chain", "title": "Demo chain",
                  "nodes": [{"title": "First block", "note": "what it does", "basis": "public"},
                            {"title": "Second block", "note": "what it does next", "basis": "typical",
                             "branch": {"title": "Side feed", "note": "an input", "basis": "public"}},
                            {"title": "Third block", "basis": "public"}],
                  "footer": "Only the blocks the cited text names, in its order.",
                  "alt": "A demonstration block chain used by the self-test of the figure generator: three "
                         "boxes one above the other, joined by arrows, with one side branch.",
                  "caption": "A demonstration chain."},
    }
    for kind, spec in demo.items():
        svg = build_stack(spec) if kind == "stack" else build_chain(spec)
        e = lint_svg_text(svg.render("auto"), f"demo-{kind}")
        if e:
            print(f"SELFTEST FAIL: the demo {kind} figure does not lint clean: {e}")
            bad += 1
    print("selftest: OK" if not bad else f"selftest: {bad} failure(s)")
    return 1 if bad else 0


# --------------------------------------------------------------------------- CLI
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", nargs="?", default="build",
                    choices=["build", "palette", "preview", "harness"])
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--check", action="store_true",
                    help="fail if any committed figure, paste block or page is out of date")
    ap.add_argument("--selftest", action="store_true", help="every lint rule fires on a bad spec")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.check:
        return cmd_check()
    if a.cmd == "build":
        return cmd_build([Path(p) for p in a.paths])
    if a.cmd == "palette":
        lines = palette_report()
        for line in lines:
            print(line)
        print(f"palette: {len(lines)} confusable pair(s) sharing a pattern")
        return 1 if lines else 0
    if a.cmd == "preview":
        out = ROOT / "tmp" / "figures" / "preview.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(preview_html(), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")
        return 0
    harness(a.paths)
    return 0


if __name__ == "__main__":
    sys.exit(main())
