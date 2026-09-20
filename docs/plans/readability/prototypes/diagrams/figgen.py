#!/usr/bin/env python3
"""figgen - generate every figure of the SKY130 reference from a declarative YAML description.

    uv run -q --with pyyaml --with pillow python figgen.py build figures/sti-006-stie.yaml
    uv run -q --with pyyaml --with pillow python figgen.py lint  out/sti-006-stie.svg
    uv run -q --with pyyaml --with pillow python figgen.py preview      # tokens.json -> preview.html
    uv run -q --with pyyaml --with pillow python figgen.py harness      # qa/*.html pages for shoot.py

Design rules enforced here (see report-D.md, "Style specification"):
  * one palette (tokens.json); no colour may appear in a figure that is not a token;
  * all text lives OUTSIDE the drawing, in a right-hand label column; leaders are
    horizontal, or (for the top-most / open features) rise vertically out of the drawing
    and run to the label column above it; leaders never cross each other or any text;
  * cross-sections are produced by a small process emulator (deposit / etch / strip /
    planarise on a height map), so consecutive figures of a series share one geometry;
  * every SVG carries light and dark values (CSS variables + prefers-color-scheme) and
    paints its own ground, so it is readable on either furo background.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from PIL import ImageFont

HERE = Path(__file__).resolve().parent
TOK = json.loads((HERE / "tokens.json").read_text())
SP, ST, TY = TOK["space"], TOK["stroke"], TOK["type"]["sizes"]
W = SP["canvas-width"]
M = SP["margin"]
DRAW_W = SP["drawing-width"]
GUT = SP["gutter"]
LABEL_X = M + DRAW_W + GUT
LABEL_W = W - M - LABEL_X

BASIS_TAG = {
    "public": None,
    "reading": "our reading",
    "inferred": "inferred",
    "typical": "typical practice",
}

# --------------------------------------------------------------------------- text metrics
_FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
_FONTS: dict = {}


def text_w(s: str, size: float, bold: bool = False, mono: bool = False) -> float:
    """Conservative width estimate: DejaVu Sans is wider than Arial/Helvetica/Segoe/SF."""
    name = "DejaVuSansMono.ttf" if mono else ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    if name not in _FONTS:
        _FONTS[name] = ImageFont.truetype(str(_FONT_DIR / name), 200)
    return _FONTS[name].getlength(s) * size / 200.0


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
    """Greedy wrap, then balance: the narrowest width that still gives the same number of lines
    (avoids a last line holding one orphaned word)."""
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


# --------------------------------------------------------------------------- SVG assembly
class Svg:
    def __init__(self, kind: str, title: str, desc: str):
        self.kind, self.title, self.desc = kind, title, desc
        self.body: list[str] = []
        self.h = 0.0
        self.patterns_used: set[str] = set()

    def add(self, s: str):
        self.body.append(s)

    def text(self, x, y, s, cls, anchor="start", owner="", mono=""):
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        o = f' data-owner="{owner}"' if owner else ""
        m = f'<tspan class="t-mono">{html.escape(mono)}</tspan>' if mono else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}{o}>{html.escape(s)}{m}</text>')

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
        css += f".halo{{stroke:var(--halo);stroke-width:{ST['leader-halo']};fill:none;opacity:.85}}"
        css += ".dot{fill:var(--ink)}\n"
        css += f".dim{{stroke:var(--ink);stroke-width:{ST['dimension']};fill:none}}.dimhead{{fill:var(--ink)}}"
        css += f".witness{{stroke:var(--ink-muted);stroke-width:{ST['rule']};stroke-dasharray:3 2.5;fill:none}}\n"
        css += f".rule{{stroke:var(--rule);stroke-width:{ST['rule']};fill:none}}"
        css += f".hl{{stroke:var(--accent);stroke-width:2.4;fill:none;stroke-linejoin:round;stroke-linecap:round}}"
        css += f".parrow{{stroke:var(--accent);stroke-width:{ST['process-arrow']};fill:none}}.pahead{{fill:var(--accent)}}\n"
        for k in TOK["materials"]:
            css += f".m-{k}{{fill:var(--m-{k})}}"
        for k in TOK["phases"]:
            css += f".ph-{k}{{fill:var(--ph-{k})}}.pht-{k}{{fill:var(--pht-{k})}}"
        return css

    def defs(self) -> str:
        p = {
            "hatch": '<pattern id="p-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line class="pat" x1="0" y1="0" x2="0" y2="6"/></pattern>',
            "hatch-back": '<pattern id="p-hatch-back" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line class="pat" x1="0" y1="0" x2="0" y2="7"/></pattern>',
            "xhatch": '<pattern id="p-xhatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path class="pat" d="M0 0V6M0 0H6"/></pattern>',
            "hlines": '<pattern id="p-hlines" width="6" height="5" patternUnits="userSpaceOnUse"><line class="pat" x1="0" y1="2.5" x2="6" y2="2.5"/></pattern>',
            "vlines": '<pattern id="p-vlines" width="4" height="6" patternUnits="userSpaceOnUse"><line class="pat" x1="2" y1="0" x2="2" y2="6"/></pattern>',
            "plus": '<pattern id="p-plus" width="12" height="12" patternUnits="userSpaceOnUse"><path class="pat" d="M3 1V5M1 3H5M9 7V11M7 9H11"/></pattern>',
            "dots": '<pattern id="p-dots" width="7" height="7" patternUnits="userSpaceOnUse"><circle class="patdot" cx="1.75" cy="1.75" r="0.9"/><circle class="patdot" cx="5.25" cy="5.25" r="0.9"/></pattern>',
        }
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


# --------------------------------------------------------------------------- process emulator
class XSection:
    """Height-map process emulator. x: 0..DRAW_W, sampled every dx; y: up, 0 = original silicon surface."""

    def __init__(self, sub: dict, dx: float = 0.5):
        self.dx = dx
        self.n = int(round(DRAW_W / dx)) + 1
        self.layers: dict[str, dict] = {"sub": sub}
        self.cols = [[["sub", -float(sub["depth"]), 0.0]] for _ in range(self.n)]
        self.overlays: list[dict] = []

    def clone(self) -> "XSection":
        c = XSection.__new__(XSection)
        c.dx, c.n = self.dx, self.n
        c.layers = dict(self.layers)
        c.cols = [[list(s) for s in col] for col in self.cols]
        c.overlays = list(self.overlays)
        return c

    def x(self, i):
        return i * self.dx

    def idx(self, x):
        return max(0, min(self.n - 1, int(round(x / self.dx))))

    def top(self, i):
        return self.cols[i][-1][2]

    def mat(self, layer):
        return self.layers[layer]["material"]

    def _in(self, i, where):
        if not where:
            return True
        x = self.x(i)
        return any(a <= x <= b for a, b in where)

    def apply(self, op: dict):
        kind = op["op"]
        getattr(self, "op_" + kind)(op)

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
            for a, b in where:
                ii = [i for i in range(self.n) if a <= self.x(i) <= b]
                lvl = max(tops[i] for i in ii) + t
                for i in ii:
                    new[i] = lvl
        else:                                                  # conformal film
            k = int(round(t / self.dx))
            only = set(op.get("only_on", []))
            for i in range(self.n):
                lo, hi = max(0, i - k), min(self.n, i + k + 1)
                if only:
                    if self.mat(self.cols[i][-1][0]) not in only:
                        continue
                    side = [s[2] for j in range(lo, hi) for s in self.cols[j] if self.mat(s[0]) in only]
                    new[i] = max(tops[i] + t, max(side))
                else:
                    new[i] = max(tops[lo:hi]) + t
        for i in range(self.n):
            if new[i] > tops[i] + 1e-9:
                self.cols[i].append([lid, tops[i], new[i]])

    def op_etch(self, op):
        mats = set(op["materials"])
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

    def op_strip(self, op):
        mats = set(op["materials"])
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

    def op_dope(self, op):
        self.layers[op["id"]] = op
        self.overlays.append(op)

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
            top = [(xs0, self.seg(i0, lid)[2])] + [(self.x(i), self.seg(i, lid)[2]) for i in range(i0, i1 + 1)] + [(xs1, self.seg(i1, lid)[2])]
            bleed = 4 if lid == "sub" else 0
            bot = [(xs0, self.seg(i0, lid)[1] - bleed)] + [(self.x(i), self.seg(i, lid)[1] - bleed) for i in range(i0, i1 + 1)] + [(xs1, self.seg(i1, lid)[1] - bleed)]
            polys.append(_simplify(top) + _simplify(bot)[::-1])
        return polys

    def ymax(self):
        return max(self.top(i) for i in range(self.n))


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
        self.lo = self.hi = 0.0       # range the anchor may slide in (SVG y), right route only
        self.stub = 0.0
        self.y = 0.0                  # SVG y of the centre of the first line
        self.is_dim = False
        self.wrap(LABEL_W)

    def wrap(self, maxw):
        self.lines = [("t-label-title", ln) for ln in wrap(self.spec["title"], TY["label-title"]["size"], maxw, bold=True)]
        self.lines += [("t-label-note muted", ln) for ln in wrap(self.spec.get("note", ""), TY["label-note"]["size"], maxw)]
        tag = BASIS_TAG[self.basis]
        if tag:
            self.lines += [("t-label-note tag", ln) for ln in wrap(tag, TY["label-note"]["size"], maxw)]
        self.height = TY["label-title"]["line"] + TY["label-note"]["line"] * (len(self.lines) - 1)


def choose_anchor(xs: XSection, lid: str, prefer: str | None):
    """Return (route, x, y_lo, y_hi, crossings) in drawing coordinates (y up)."""
    pres = xs.present(lid)
    i0, i1 = xs.runs(pres)[-1]
    inset = min(8.0, (i1 - i0) * xs.dx / 2)
    ir = xs.idx(xs.x(i1) - inset)
    s = xs.seg(ir, lid)
    mid = (s[1] + s[2]) / 2
    crossed = {t[0] for j in range(ir + 1, xs.n) for t in xs.cols[j] if t[0] != lid and t[1] < mid < t[2]}
    pad = 3.5 if s[2] - s[1] > 9 else (s[2] - s[1]) / 2
    right = ("right", xs.x(ir), max(s[1] + pad, -xs.layers["sub"]["depth"] + 8), s[2] - pad, len(crossed))
    tops = [i for i in pres if xs.cols[i][-1][0] == lid]
    top = None
    if tops:
        a, b = max(xs.runs(tops), key=lambda r: (r[1] - r[0], r[1]))
        s = xs.seg((a + b) // 2, lid)
        yv = s[2] - min((s[2] - s[1]) / 2, 8.0)
        top = ("top", xs.x((a + b) // 2), yv, yv, 0)
    if prefer == "top" and top:
        return top
    if prefer == "right" or right[4] == 0 or top is None:
        return right
    return top


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


def layout_right_labels(labels: list[Label], floor: float) -> float:
    """Right-routed labels: keep the order of the layers, keep a minimum distance, and move each label as
    little as possible from a height at which its leader is horizontal. The anchor then slides inside its
    layer to meet the label. Returns the y below the last label."""
    rights = sorted([l for l in labels if l.route == "right"], key=lambda l: (l.lo + l.hi) / 2)
    if not rights:
        return floor
    gap = SP["label-gap"]
    off, acc = [], 0.0
    for l in rights:
        off.append(acc)
        acc += l.height + gap
    des = [min(l.hi, max(l.lo, l.lo + 6)) for l in rights]
    for _ in range(8):
        z = _isotonic([d - o for d, o in zip(des, off)])
        ys = [max(v, floor) + o for v, o in zip(z, off)]
        des = [min(l.hi, max(l.lo, yv)) for l, yv in zip(rights, ys)]
    for l, yv in zip(rights, ys):
        l.y = yv
        l.ay = min(l.hi, max(l.lo, yv))
    return ys[-1] + rights[-1].height + gap


def draw_label(svg: Svg, l: Label, x_draw_right: float, halo: bool):
    first = TY["label-title"]["size"]
    y = l.y + first * 0.35
    top = l.route == "top"
    tx = LABEL_X if not top else (l.ax + l.stub + 9 if l.hang == "right" else l.ax + l.stub - 9)
    for n, (cls, s) in enumerate(l.lines):
        svg.text(tx, y, s, cls, anchor="end" if top and l.hang == "left" else "start", owner=l.key)
        y += TY["label-note"]["line"]
    if not top:
        xg0, xg1 = x_draw_right + 3, LABEL_X - 4
        if halo:
            svg.add(f'<path class="halo" d="M{l.ax + 3:.1f} {l.ay:.1f}H{x_draw_right:.1f}"/>')
        d = f"M{l.ax:.1f} {l.ay:.1f}H{xg0:.1f}" + (f"L{xg1:.1f} {l.y:.1f}" if abs(l.y - l.ay) > 0.05 else f"H{xg1:.1f}")
    else:
        rx = l.ax + l.stub
        d = f"M{l.ax:.1f} {l.ay:.1f}" + (f"H{rx:.1f}" if l.stub else "") + f"V{l.y:.1f}H{rx + (5 if l.hang == 'right' else -5):.1f}"
    svg.add(f'<path class="leader" data-owner="{l.key}" d="{d}"/>')
    if not l.is_dim:
        svg.add(f'<circle class="dot" cx="{l.ax:.1f}" cy="{l.ay:.1f}" r="{ST["anchor-dot-radius"]}"/>')


# --------------------------------------------------------------------------- cross-section figure
def eval_y(xs: XSection, expr):
    if isinstance(expr, (int, float)):
        return float(expr)
    m = re.fullmatch(r"top@([\d.]+)", str(expr))
    if m:
        return xs.top(xs.idx(float(m.group(1))))
    raise ValueError(f"bad y expression {expr!r}")


def build_xsection(spec: dict, base: Path) -> Svg:
    series = yaml.safe_load((base / spec["series"]).read_text())
    svg = Svg("xsection", spec["alt"], spec["alt"])
    states = {}
    xs = XSection(series["substrate"])
    states["000"] = xs.clone()
    for op in series["ops"]:
        xs.apply(op)
        states[str(op["step"])] = xs.clone()          # state after the LAST op of that step

    def state(step):
        return states[[k for k in sorted(states) if k <= str(step)][-1]]

    panels = spec["panels"]
    depth = float(series["substrate"]["depth"])
    X0 = M
    x_right = X0 + DRAW_W
    y = M
    seen: set[str] = set()
    for pi, p in enumerate(panels):
        st = state(p["state_after"])
        ymax = st.ymax() + 4                                 # per panel: no empty band where a film was removed
        draw_h = ymax + depth
        dims, notes = p.get("dims", []), p.get("callouts", [])
        labels: list[Label] = []
        for lid, layer in st.layers.items():
            if lid in p.get("hide_labels", []) or "label" not in layer or not st.present(lid):
                continue
            lspec = {**layer["label"], **p.get("labels", {}).get(lid, {})}
            if pi > 0 and lid in seen and lid not in p.get("labels", {}):
                lspec = {k: v for k, v in lspec.items() if k != "note"}      # a note is given once per figure
            seen.add(lid)
            labels.append(Label(lid, lspec))
        for k, dm in enumerate(dims):
            labels.append(Label(f"dim{k}", dm["label"]))
            labels[-1].is_dim = True
        for k, c in enumerate(notes):
            labels.append(Label(f"callout{k}", c["label"]))
        # ---- anchors in drawing coordinates; routes
        geo = {}
        for lab in labels:
            if lab.is_dim:
                dm = dims[int(lab.key[3:])]
                ya, yb = eval_y(st, dm["y0"]), eval_y(st, dm["y1"])
                geo[lab.key] = ("top", dm["x"], (ya + yb) / 2, (ya + yb) / 2, 0)
                lab.stub = float(dm.get("stub", 12))
            elif lab.key.startswith("callout"):
                c = notes[int(lab.key[7:])]
                yv = eval_y(st, c["y"])
                geo[lab.key] = ("top", c["x"], yv, yv, 0)
            else:
                geo[lab.key] = choose_anchor(st, lab.key, st.layers[lab.key].get("route"))
            lab.route = geo[lab.key][0]
        # ---- header band for the top-routed labels (at most two: one hangs left, one right)
        tops = sorted([l for l in labels if l.route == "top"], key=lambda l: geo[l.key][1] + l.stub)
        if len(tops) > 2:
            raise SystemExit(f"{spec['id']}: more than two top-routed labels in panel {pi + 1}")
        for k, lab in enumerate(tops):
            rx = X0 + geo[lab.key][1] + lab.stub
            lab.hang = "left" if (len(tops) == 2 and k == 0) or (len(tops) == 1 and rx > X0 + DRAW_W * 0.6) else "right"
            lab.wrap(min(200.0, rx - 9 - M) if lab.hang == "left" else min(230.0, W - M - rx - 9))
        title_y = y + TY["panel-title"]["size"]
        svg.text(M, title_y, p["title"], "t-panel-title")
        band_top = title_y + 12
        band_h = max([l.height for l in tops], default=0)
        y_draw_top = band_top + band_h + (8 if tops else 0)
        y0 = y_draw_top + ymax                              # SVG y of the datum

        def sx(v):
            return X0 + v

        def sy(v):
            return y0 - v

        # ---- drawing
        cid = f"clip{pi + 1}"
        svg.add(f'<clipPath id="{cid}"><rect x="{X0}" y="{y_draw_top:.1f}" width="{DRAW_W}" height="{draw_h:.1f}"/></clipPath>')
        svg.add(f'<g class="drawing" data-rect="{X0},{y_draw_top:.1f},{DRAW_W},{draw_h:.1f}" clip-path="url(#{cid})">')
        for lid, layer in st.layers.items():
            mat = layer["material"]
            pat = TOK["materials"][mat]["pattern"]
            for poly in st.polygons(lid):
                pts = " ".join(f"{sx(px):.2f},{sy(py):.2f}" for px, py in poly)
                svg.add(f'<polygon class="mat m-{mat}" data-layer="{lid}" points="{pts}"/>')
                if pat != "none":
                    svg.patterns_used.add(pat)
                    svg.add(f'<polygon fill="url(#p-{pat})" points="{pts}"/>')
        for a, b in (p.get("highlight") or {}).get("where", []):
            pts = _simplify([(sx(st.x(i)), sy(st.top(i))) for i in range(st.idx(a), st.idx(b) + 1)])
            svg.add('<polyline class="hl" points="' + " ".join(f"{px:.2f},{py:.2f}" for px, py in pts) + '"/>')
        svg.add("</g>")
        for k, dm in enumerate(dims):
            ya, yb, xd = eval_y(st, dm["y0"]), eval_y(st, dm["y1"]), sx(dm["x"])
            for a, b in dm.get("witness", []):
                svg.add(f'<path class="witness" d="M{sx(a):.1f} {sy(yb):.1f}H{sx(b):.1f}"/>')
            ah, aw = ST["arrowhead"]["length"], ST["arrowhead"]["width"] / 2
            svg.add(f'<path class="dim" d="M{xd:.1f} {sy(ya) - ah + 1:.1f}V{sy(yb) + ah - 1:.1f}"/>')
            svg.add(f'<path class="dimhead" d="M{xd:.1f} {sy(ya) - 1.2:.1f}l{-aw} {-ah}h{2 * aw}z"/>')
            svg.add(f'<path class="dimhead" d="M{xd:.1f} {sy(yb):.1f}l{-aw} {ah}h{2 * aw}z"/>')
        # ---- label positions
        for lab in labels:
            r, gx, glo, ghi, ncross = geo[lab.key]
            lab.ax = sx(gx)
            lab.lo, lab.hi = sy(ghi), sy(glo)                # SVG y grows downwards
            lab.ay = (lab.lo + lab.hi) / 2
            if lab.route == "top":
                lab.y = band_top + TY["label-title"]["size"] * 0.5
        bottom = layout_right_labels(labels, y_draw_top + 7)
        for lab in labels:
            halo = False
            if lab.route == "right":
                yv = y0 - lab.ay
                i_a = st.idx(lab.ax - X0)
                halo = any(t[0] != lab.key and t[1] < yv < t[2] for j in range(i_a + 1, st.n) for t in st.cols[j])
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
            svg.add(f'<path class="parrow" d="M{cx} {ya0}V{ya1 - ah + 1}"/>')
            svg.add(f'<path class="pahead" d="M{cx} {ya1}l{-aw} {-ah}h{2 * aw}z"/>')
            svg.text(cx + 16, ya0 + 11, a["title"], "t-label-title acc")
            for k, ln in enumerate(note):
                svg.text(cx + 16, ya0 + 11 + 15 * (k + 1), ln, "t-label-note muted")
            y = ya1 + 14
        else:
            y += SP["panel-gap"] - 6
    svg.text(M, y + 10, "Not to scale. Thin films are drawn thicker than they are.", "t-label-note muted")
    svg.h = y + 10 + M
    return svg


# --------------------------------------------------------------------------- flow map figure
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
    RANGE_W = text_w("000\u2013000", TY["label-title"]["size"]) + 10
    for m in spec["modules"]:
        name = wrap(m["name"], TY["label-title"]["size"], TW - RANGE_W, bold=True)
        n = m["last"] - m["first"] + 1
        rng = f"{m['first']:03d}\u2013{m['last']:03d}"
        nm = len(m["masks"])
        l3a = f"{n} steps \u00b7 {nm} mask{'s' if nm != 1 else ''}:"
        l3 = ", ".join(m["masks"])
        split = text_w(l3a + " ", TY["label-note"]["size"]) + text_w(l3, TY["mono"]["size"], mono=True) > TW
        h = 7 + TY["label-title"]["line"] * len(name) + TY["label-note"]["line"] * (2 if split else 1) + 5
        rows.append(dict(m=m, name=name, rng=rng, l3a=l3a, l3=l3, h=h, n=n, split=split))
    H = sum(r["h"] for r in rows)
    # strip + fans + rows
    ry = top
    for k, r in enumerate(rows):
        m = r["m"]
        s0 = top + H * (m["first"] - 1) / total
        s1 = top + H * m["last"] / total
        ph = m["phase"]
        if k % 2 == 0:
            svg.add(f'<polygon class="pht-{ph}" points="{X_S1},{s0:.1f} {X_F1},{ry:.1f} {W - M},{ry:.1f} {W - M},{ry + r["h"]:.1f} {X_F1},{ry + r["h"]:.1f} {X_S1},{s1:.1f}"/>')
        svg.add(f'<path class="rule" d="M{X_S1} {s0:.1f}L{X_F1} {ry:.1f}H{W - M}"/>')
        if k == len(rows) - 1:
            svg.add(f'<path class="rule" d="M{X_S1} {s1:.1f}L{X_F1} {ry + r["h"]:.1f}H{W - M}"/>')
        svg.add(f'<rect class="mat ph-{ph}" x="{X_S0}" y="{s0:.1f}" width="{X_S1 - X_S0}" height="{s1 - s0:.1f}"/>')
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
    # phase brackets
    for ph in spec["phases"]:
        p0 = top + H * (ph["first"] - 1) / total
        p1 = top + H * ph["last"] / total
        svg.add(f'<path class="leader" d="M{X_BR + 3} {p0 + 1.5:.1f}H{X_BR}V{p1 - 1.5:.1f}H{X_BR + 3}"/>')
        cy = (p0 + p1) / 2
        svg.text(X_PH, cy - 2, TOK["phases"][ph["id"]]["label"], "t-label-title")
        svg.text(X_PH, cy + 13, f"{ph['last'] - ph['first'] + 1} steps", "t-label-note muted")
    y = top + H + 18
    for ln in wrap(spec["footer"], TY["label-note"]["size"], TW):
        svg.text(X_T, y, ln, "t-label-note muted")
        y += TY["label-note"]["line"]
    svg.h = y - TY["label-note"]["line"] + M
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


def lint_svg(path: Path) -> list[str]:
    errs = []
    raw = path.read_text()
    ns = {"s": "http://www.w3.org/2000/svg"}
    root = ET.fromstring(raw)
    vb = [float(v) for v in root.get("viewBox").split()]
    if vb[2] != W:
        errs.append(f"canvas width {vb[2]} != {W}")
    if not (root.find("s:title", ns) is not None and (root.find("s:desc", ns).text or "").strip()):
        errs.append("missing <title>/<desc>")
    allowed = {v[m].lower() for grp in ("theme", "materials", "phases") for v in TOK[grp].values() for m in ("light", "dark")}
    allowed |= {v["tint"][m].lower() for v in TOK["phases"].values() for m in ("light", "dark")}
    for col in set(re.findall(r"#[0-9a-fA-F]{6}\b", raw)):
        if col.lower() not in allowed:
            errs.append(f"colour {col} is not a token")
    if re.search(r'(fill|stroke)="(?!none|url)[^"]+"', raw):
        errs.append("literal fill/stroke attribute found; use token classes")
    texts = [(el, _bbox(el)) for el in root.iter("{http://www.w3.org/2000/svg}text")]
    for el, b in texts:
        if b is None:
            errs.append(f"text without a type-scale class: {el.text!r}")
    texts = [(el, b) for el, b in texts if b]
    for el, b in texts:
        if b[4] < TY["min-size"]:
            errs.append(f"text below minimum size: {el.text!r}")
        if b[0] < M - 0.5 or b[2] > W - M + 0.5 or b[1] < 0 or b[3] > vb[3]:
            errs.append(f"text escapes the canvas margins ({b[0]:.0f}..{b[2]:.0f}): {el.text!r}")
    c = SP["text-clearance"]
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i][1], texts[j][1]
            if a[0] < b[2] + c and b[0] < a[2] + c and a[1] < b[3] and b[1] < a[3]:
                errs.append(f"text overlap: {texts[i][0].text!r} / {texts[j][0].text!r}")
    rects = [[float(v) for v in g.get("data-rect").split(",")] for g in root.iter("{http://www.w3.org/2000/svg}g") if g.get("data-rect")]
    for el, b in texts:
        for rx, ry, rw, rh in rects:
            if b[0] < rx + rw and rx < b[2] and b[1] < ry + rh and ry < b[3]:
                errs.append(f"text inside a drawing area: {el.text!r}")
    leaders = [(p.get("data-owner", ""), _segments(p.get("d"))) for p in root.iter("{http://www.w3.org/2000/svg}path") if p.get("class") in ("leader", "dim")]
    for owner, segs in leaders:
        for seg in segs:
            for el, b in texts:
                if _seg_hits_box(seg, b, 1.0):
                    errs.append(f"leader of {owner!r} touches text {el.text!r}")
    for i in range(len(leaders)):
        for j in range(i + 1, len(leaders)):
            if any(_cross(a, b) for a in leaders[i][1] for b in leaders[j][1]):
                errs.append(f"leaders cross: {leaders[i][0]!r} x {leaders[j][0]!r}")
    # a vertical leader must not run alongside a near-vertical material edge (it would read as a boundary)
    edges = []
    for pg in root.iter("{http://www.w3.org/2000/svg}polygon"):
        if "mat" in (pg.get("class") or "").split():
            pts = [tuple(float(v) for v in q.split(",")) for q in pg.get("points").split()]
            for a, b in zip(pts, pts[1:] + pts[:1]):
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
    if root.get("data-kind") == "xsection" and "Not to scale" not in raw:
        errs.append("cross-section without the 'Not to scale' line")
    return errs


def lint_spec(spec: dict, base: Path) -> list[str]:
    errs = []
    alt = spec.get("alt", "")
    if not 60 <= len(alt) <= 450:
        errs.append(f"alt text must be 60-450 characters (is {len(alt)})")
    if not spec.get("caption"):
        errs.append("caption missing")
    page = spec.get("page")
    defined = set()
    if page:
        repo = HERE.parents[2]
        defined = set(re.findall(r"^\[\^([^\]]+)\]:", (repo / page).read_text(), re.M))
    labs = []
    if spec["kind"] == "xsection":
        series = yaml.safe_load((base / spec["series"]).read_text())
        labs += [("substrate", series["substrate"].get("label"))]
        for op in series["ops"]:
            if op.get("t") is not None and op["op"] == "deposit" and float(op["t"]) < SP["min-layer-thickness"]:
                errs.append(f"layer {op['id']} drawn thinner than {SP['min-layer-thickness']} u")
            if op.get("material") and op["material"] not in TOK["materials"]:
                errs.append(f"unknown material {op['material']}")
            labs.append((op.get("id", op["op"]), op.get("label")))
        for p in spec["panels"]:
            labs += [("dim", d["label"]) for d in p.get("dims", [])] + [("callout", c["label"]) for c in p.get("callouts", [])]
    for key, lab in labs:
        if not lab:
            continue
        if lab.get("basis", "public") not in BASIS_TAG:
            errs.append(f"{key}: unknown basis")
        if re.search(r"\d", re.sub(r"steps? \d{3}((, | and |\u2013)\d{3})*", "", lab.get("note", ""))) and not lab.get("cite"):
            errs.append(f"{key}: a label that states a number needs cite:")
        if lab.get("cite") and page and lab["cite"] not in defined:
            errs.append(f"{key}: cite key [^{lab['cite']}] is not defined on {page}")
    for key in re.findall(r"\[\^([^\]]+)\]", spec.get("caption", "")):
        if page and key not in defined:
            errs.append(f"caption cites [^{key}], which is not defined on {page}")
    return errs


# --------------------------------------------------------------------------- CVD check on the palette
def _lab(hexcol, sim=None):
    r, g, b = (int(hexcol[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    if sim:                                                    # Machado et al. 2009, severity 1.0
        mtx = {"deutan": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
               "protan": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]]}[sim]
        lin = [max(0.0, min(1.0, sum(mtx[r_][c_] * lin[c_] for c_ in range(3)))) for r_ in range(3)]
    x = (0.4124 * lin[0] + 0.3576 * lin[1] + 0.1805 * lin[2]) / 0.95047
    yv = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    z = (0.0193 * lin[0] + 0.1192 * lin[1] + 0.9505 * lin[2]) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    return (116 * f(yv) - 16, 500 * (f(x) - f(yv)), 200 * (f(yv) - f(z)))


def palette_report() -> list[str]:
    """Pairs of materials that are hard to tell apart (dE76 < 14) for normal, deutan or protan vision and
    that also share a pattern. Such pairs must never touch in a figure."""
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
                if worst < 14:
                    out.append(f"{mode}: {keys[i]} / {keys[j]} dE={worst:.1f} with the same pattern")
    return out


# --------------------------------------------------------------------------- preview + harness
def preview_html() -> str:
    def sw(mode):
        cells = []
        for k, v in TOK["materials"].items():
            pat = "" if v["pattern"] == "none" else f'<rect width="72" height="40" fill="url(#pp-{mode}-{v["pattern"]})"/>'
            cells.append(
                f'<div class="sw"><svg width="72" height="40" viewBox="0 0 72 40"><rect width="72" height="40" fill="{v[mode]}" stroke="{TOK["theme"]["ink"][mode]}"/>{pat}</svg>'
                f'<div><b>{k}</b><br>{html.escape(v["label"])}<br><code>{v[mode]}</code> · {v["pattern"]}</div></div>')
        return "".join(cells)

    def pats(mode):
        ink = TOK["theme"]["ink"][mode]
        o = ST["pattern-opacity"]
        return (f'<svg width="0" height="0" style="position:absolute"><defs>'
                f'<pattern id="pp-{mode}-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="{ink}" stroke-width=".7" opacity="{o}"/></pattern>'
                f'<pattern id="pp-{mode}-hatch-back" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line x1="0" y1="0" x2="0" y2="7" stroke="{ink}" stroke-width=".7" opacity="{o}"/></pattern>'
                f'<pattern id="pp-{mode}-xhatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V6M0 0H6" stroke="{ink}" stroke-width=".7" opacity="{o}" fill="none"/></pattern>'
                f'<pattern id="pp-{mode}-hlines" width="6" height="5" patternUnits="userSpaceOnUse"><line x1="0" y1="2.5" x2="6" y2="2.5" stroke="{ink}" stroke-width=".7" opacity="{o}"/></pattern>'
                f'<pattern id="pp-{mode}-vlines" width="4" height="6" patternUnits="userSpaceOnUse"><line x1="2" y1="0" x2="2" y2="6" stroke="{ink}" stroke-width=".7" opacity="{o}"/></pattern>'
                f'<pattern id="pp-{mode}-plus" width="12" height="12" patternUnits="userSpaceOnUse"><path d="M3 1V5M1 3H5M9 7V11M7 9H11" stroke="{ink}" stroke-width=".7" opacity="{o}" fill="none"/></pattern>'
                f'<pattern id="pp-{mode}-dots" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="1.75" cy="1.75" r=".9" fill="{ink}" opacity="{o}"/><circle cx="5.25" cy="5.25" r=".9" fill="{ink}" opacity="{o}"/></pattern>'
                f'</defs></svg>')

    def themecells(mode):
        return "".join(f'<div class="sw"><span class="chip" style="background:{v[mode]}"></span><div><b>{k}</b><br><code>{v[mode]}</code><br>{html.escape(v["use"])}</div></div>' for k, v in TOK["theme"].items())

    def phasecells(mode):
        return "".join(f'<div class="sw"><span class="chip" style="background:{v[mode]}"></span><span class="chip" style="background:{v["tint"][mode]}"></span><div><b>{k}</b> + tint<br><code>{v[mode]}</code> <code>{v["tint"][mode]}</code></div></div>' for k, v in TOK["phases"].items())

    typ = "".join(f'<tr><td><code>{k}</code></td><td>{v["size"]} u</td><td>{v["weight"]}</td><td>{v["line"]} u</td><td style="font-size:{v["size"] * 1.25}px;font-weight:{v["weight"]}">Nitride hard mask 0.33 µm</td></tr>' for k, v in TY.items() if isinstance(v, dict))
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
<p>Generated from <code>tokens.json</code> ({html.escape(TOK['meta']['version'])}) by <code>figgen.py preview</code>. Do not edit by hand. {html.escape(TOK['meta']['note'])}</p></header>
{sect}
<div class="tables"><h2>Type scale</h2><p>Family: <code>{html.escape(TOK['type']['family'])}</code></p>
<table><tr><th>token</th><th>size</th><th>weight</th><th>line</th><th>sample at desktop scale</th></tr>{typ}</table>
<h2>Spacing (u)</h2><table>{spc}</table><h2>Strokes (u)</h2><table>{stk}</table></div>
"""


def harness(names: list[str]):
    qa = HERE / "qa"
    qa.mkdir(exist_ok=True)
    for mode in ("light", "dark"):
        bg, fg = TOK["theme"]["bg"][mode], TOK["theme"]["ink"][mode]
        for width, col in (("desktop", "736px"), ("phone", "100%")):
            figs = "".join(
                f'<figure style="margin:0"><img src="../out/{n}.{mode}.svg" alt="" style="width:600px;max-width:100%;height:auto"><figcaption>{n} ({mode}, {width})</figcaption></figure>'
                for n in names)
            (qa / f"{mode}-{width}.html").write_text(
                f'<!doctype html><meta name="viewport" content="width=device-width"><body style="margin:0;background:{bg};color:{fg};font:16px/1.5 sans-serif">'
                f'<div style="width:{col};margin:0 auto;padding:16px;box-sizing:border-box">'
                f'<p>Body text of the page at furo size, for comparison with the label text in the figure below.</p>{figs}</div>')


# --------------------------------------------------------------------------- CLI
def cmd_build(path: Path):
    spec = yaml.safe_load(path.read_text())
    if "kind" not in spec:                       # a series file, not a figure
        return 0
    errs = lint_spec(spec, path.parent)
    svg = build_xsection(spec, path.parent) if spec["kind"] == "xsection" else build_flowmap(spec)
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    name = spec["id"]
    for theme, suffix in (("auto", ""), ("light", ".light"), ("dark", ".dark")):
        (out / f"{name}{suffix}.svg").write_text(svg.render(theme))
    errs += lint_svg(out / f"{name}.svg")
    cap = " ".join(spec["caption"].split())
    (out / f"{name}.myst.txt").write_text(
        f":::{{figure}} /figures/{spec.get('dir', 'misc')}/{name}.svg\n:alt: {' '.join(alt_clean(spec['alt']).split())}\n"
        f":width: {SP['display-width-px']}px\n:name: fig-{name}\n\n{cap}\n:::\n")
    print(f"{name}: wrote out/{name}[.light|.dark].svg, height {math.ceil(svg.h)} u")
    for e in errs:
        print("  LINT:", e)
    return len(errs)


def alt_clean(s):
    return s.replace("\n", " ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "lint", "preview", "harness", "palette"])
    ap.add_argument("paths", nargs="*")
    a = ap.parse_args()
    bad = 0
    if a.cmd == "build":
        for p in a.paths:
            bad += cmd_build(Path(p))
    elif a.cmd == "lint":
        for p in a.paths:
            for e in lint_svg(Path(p)):
                print(f"{p}: {e}")
                bad += 1
    elif a.cmd == "preview":
        (HERE / "preview.html").write_text(preview_html())
        print("wrote preview.html")
    elif a.cmd == "palette":
        for line in palette_report():
            print(line)
    elif a.cmd == "harness":
        harness(a.paths)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
