#!/usr/bin/env python3
"""Check the per-mask pages against their template and the masks index.

The masks index ``docs/masks/index.md`` has the tables and passages this
checker reads:

* the table under "## Mask steps in this reference": one row per mask
  step, with the ``masks.csv`` entry (*PDK mask*), the mask-level and
  drawn layers, the *Patterns* cell (the steps that use the resist
  pattern) and the minimum CD;
* the opening paragraph of "## Plates recorded for the MPW runs", which
  names the "Run Mask IDs" rows that ``masks.csv`` does not have
  (``"Rev Resistor Protect, RRPM"``, …);
* the table under "### Runs, reticle sets and plate IDs" (the reticle set
  of each MPW run);
* the first table under "### Plates by mask" (plates recorded, plate
  number and rendered dies for each mask step);
* the opening paragraph of "### Mask types and plate labels" (the
  "Sheet4" mask-type code of each mask that has one).

For every ``docs/masks/*.md`` page except ``index.md``:

* **Title.** The page starts with a ``(mask-<file stem>)=`` label and a
  title ``# CODE — name`` whose code, in lower case, is the file stem.
  The name is the ``Mask`` field of the variant marked ``X`` in the
  index's *PDK mask* cell (or of the only variant, when none is marked);
  for a mask step the cell gives as *not listed*, it is the name the
  "Run Mask IDs" row has on the index (for example "Rev Resistor
  Protect" for RRPM).
* **Headings.** The H2 headings are exactly the template's, in order;
  the H3 headings under "Drawn layers and derivation" and "References"
  are exactly the template's; "Plates and reticle sets" may have only
  the optional H3s listed in ``OPTIONAL_H3``; no other H2 has H3s. The
  "Steps that use this mask" heading is preceded by a
  ``(mask-<stem>-steps)=`` label.
* **Quick facts.** The table before the first H2 has the header
  ``| | CODE — name |`` and exactly the rows of ``FACT_ROWS``, in order.
  Footnote references are ignored in every comparison.

  * "Mask step" links exactly one step, with the page's code as link
    text, the mask step the index gives for the code, and reads "step N
    of T" with T the number of step pages; the index row links the page
    as ``{ref}`CODE <mask-<stem>>``, and the mask step's own step page
    links it the same way.
  * "PDK mask (`masks.csv`)" gives each variant of the index cell as
    ``"Mask", `CODE`, marked `X` in `Used in SKY130``` or
    ``"Mask", `CODE`, unmarked``; for a *not listed* mask it starts
    "not listed" and quotes the "Run Mask IDs" name.
  * "Mask-level layer (`gds_layers.csv`)", "Drawn layer
    (`gds_layers.csv`)" and "Minimum CD, feature / space" contain, in
    the index's order, every code span, quotation, layer:datatype pair,
    number and "N/A" of the index cell; an index cell reading "none" or
    "none listed" is repeated exactly, and an index cell marked
    *(inference)* needs "inference" in the page's cell.
  * "Polarity and tone" is not empty; "Exposure class" links a machine
    page.
  * "Mask type (process-steps sheet)" starts with the mask's code span
    for a mask with a "Sheet4" type, and otherwise reads exactly
    ``NO_TYPE``.
  * "Plates recorded", "Plate no." and "Dies with shapes, MPW-1 to MPW-8
    (renders)" read exactly as the mask's cells in "Plates by mask".
  * "Steps that use the pattern" reads "N steps; see …" and links
    ``mask-<stem>-steps``, where N is the number of steps in the steps
    paragraph.
* **Renders.** Unless the mask is "not rendered", "In the public
  renders" says the renders are one derivation, "not SkyWater's", and
  quotes the site's "renders of *drawn* data".
* **Plates.** The plate table under "Plates and reticle sets" (header
  starting ``| Run |``) has one row per run, MPW-1 to MPW-8 in order,
  whose reticle-set cell is the index's set for the run and whose
  plate-ID cell is the plate ID implied by the index (the run's prefix —
  the set with its first two characters dropped and its final ``AC``
  replaced by ``AA`` — the plate number and ``A``) for a run with a plate
  recorded, or "none recorded" otherwise. Where the "Plates recorded"
  cell lists variants, only the segment labelled with the ``X``
  variant's name may record plates.
* **Steps.** The steps paragraph (the paragraph after a line reading
  "Steps:" in "Steps that use this mask") links the mask step followed
  by exactly the steps of the index row's *Patterns* cell, in
  ascending, consecutive order, each with its step code (from the title
  of its step page) as link text, all before the next mask step of the
  index table; every step after the mask step has a step page that
  links the mask step.
* **Owner constraints.** Neither the page nor the index contains any of
  ``FORBIDDEN`` (words that only the renders site's lot, custody and
  generator fields would bring in).

With ``--sheet FILE`` (a CSV export of the process-steps sheet's "Run
Mask IDs" tab, saved locally; the checker never fetches it), the
reticle sets of the index and the plate IDs of every page are also
compared with the sheet.

Exit status is non-zero on any problem.  Run with
``uv run tools/check_masks.py``; an optional positional argument names
another ``masks`` directory to check, whose sibling ``steps`` directory
holds the step pages (used to test the checker on a copy of ``docs``).
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASKS = ROOT / "docs" / "masks"

H2 = [
    "What the mask defines",
    "Drawn layers and derivation",
    "Plates and reticle sets",
    "Lithography and pattern transfer",
    "Steps that use this mask",
    "Design rules and critical dimensions",
    "Related pages",
    "References",
    "Open questions",
]
H3 = {
    "Drawn layers and derivation": ["In the PDK", "In the public renders"],
    "References": ["Cross-check", "High-level understanding", "Deep dive"],
}
OPTIONAL_H3 = {"Plates and reticle sets": ["The mask-type record"]}
STEPS_H2 = "Steps that use this mask"
STEPS_INTRO = "Steps:"
PDK_ROW = "PDK mask (`masks.csv`)"
MASK_LAYER_ROW = "Mask-level layer (`gds_layers.csv`)"
DRAWN_ROW = "Drawn layer (`gds_layers.csv`)"
CD_ROW = "Minimum CD, feature / space"
TONE_ROW = "Polarity and tone"
EXPOSURE_ROW = "Exposure class"
TYPE_ROW = "Mask type (process-steps sheet)"
INDEX_ROWS = ("Plates recorded", "Plate no.", "Dies with shapes, MPW-1 to MPW-8 (renders)")
FIRST_ROW = "Mask step"
LAST_ROW = "Steps that use the pattern"
FACT_ROWS = [FIRST_ROW, PDK_ROW, MASK_LAYER_ROW, DRAWN_ROW, CD_ROW, TONE_ROW,
             EXPOSURE_ROW, TYPE_ROW, *INDEX_ROWS, LAST_ROW]
NO_TYPE = "None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only"
NOT_RENDERED = "not rendered"
RENDERS_PHRASES = ("not SkyWater's", "renders of *drawn* data")
FORBIDDEN = ("custody", "shipment", "exp_ship")
NONE_RECORDED = "none recorded"
RUNS = [f"MPW-{n}" for n in range(1, 9)]

# {ref}`CODE <step-NNN>` (group 1 the text, group 2 the number) or {ref}`step-NNN`.
STEP_RE = re.compile(r"\{ref\}`(?:([^`<]*?)\s*<)?step-(\d{3})>?`")
MACHINE_RE = re.compile(r"\{ref\}`(?:[^`<]*<)?machine-[a-z0-9-]+>?`")
TITLE_RE = re.compile(r"^# Step (\d{3}) — (.+?):", re.MULTILINE)
FOOTNOTE_RE = re.compile(r"\[\^[A-Za-z0-9_-]+\]")
PAGE_TITLE_RE = re.compile(r"^# (\S+) — (\S.*)$", re.MULTILINE)
COUNT_RE = re.compile(r"^(\d+) steps?; see ")
STEP_OF_RE = re.compile(r"\bstep (\d+) of (\d+)\b")
PLATE_NO_RE = re.compile(r"`(\d{3})`")
OVERRIDE_RE = re.compile(r"(MPW-\d): `(\d{3})`")
CODE_CELL_RE = re.compile(r"^`([^`]+)`$")
VARIANT_RE = re.compile(
    r"^(.+), (?:\{ref\}`)?([A-Z0-9\[\]]+)(?: <mask-[a-z0-9]+>`)? — (`X`|\*blank\*)$")
SHEET_NAME_RE = re.compile(r'"([^"]+), ([A-Z0-9]+)"')
TYPE_CODE_RE = re.compile(r"`([A-Z]\d-\d{3}-[A-Z0-9-]+)`")
ACRONYM_RE = re.compile(r"`([A-Z][A-Z0-9]*)`")
# Code spans, quotations, layer:datatype pairs, N/A and free-standing numbers.
TOKEN_RE = re.compile(r'`[^`]+`|"[^"]+"|\d+:\d+|N/A|(?<![\w.\\])\d+(?:\.\d+)?(?![\w.])')


def sections(text: str, level: str) -> dict[str, str]:
    """Map each heading of the given level (``##`` or ``###``) to its body."""
    parts = re.split(rf"^{level} (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def clean(cell: str) -> str:
    return re.sub(r"\s+", " ", FOOTNOTE_RE.sub("", cell)).strip()


def table(body: str) -> list[list[str]]:
    """Cells of the header and data rows of the first Markdown table in ``body``."""
    rows, started = [], False
    for line in body.splitlines():
        if line.startswith("|"):
            started = True
            if not re.match(r"^\|[-| :]+\|$", line.strip()):
                rows.append(cells(line))
        elif started:
            break
    return rows


def table_rows(body: str) -> list[list[str]]:
    """Cells of the data rows of the first Markdown table in ``body``."""
    return table(body)[1:]


def is_subsequence(wanted: list[str], found: list[str]) -> bool:
    it = iter(found)
    return all(token in it for token in wanted)


def variants(cell: str) -> list[tuple[str, str, bool]] | None:
    """(name, acronym, marked) for each entry of a *PDK mask* cell (None if unreadable)."""
    out = []
    for part in clean(cell).split("; "):
        m = VARIANT_RE.match(part)
        if not m:
            return None
        out.append((m.group(1), m.group(2), m.group(3) == "`X`"))
    return out


def recorded_runs(cell: str, x_name: str | None) -> set[str] | None:
    """Runs with a plate, from a "Plates recorded" cell (None if unreadable).

    A cell with several ";"-separated segments lists variants
    ("Via 2-PLM: all eight; Via 2-TNV and Via 2-S8TM: not recorded");
    the segment whose label is, or is part of, the ``X`` variant's name
    is used, and every other segment must record no plates.
    """
    segments = [s.strip() for s in clean(cell).split(";")]
    if len(segments) > 1:
        if x_name is None:
            return None
        chosen, others = [], []
        for segment in segments:
            label, _, text = segment.partition(":")
            (chosen if label.strip() and label.strip() in x_name else others).append(text)
        if len(chosen) != 1 or any(t.strip() not in ("not recorded", "none") for t in others):
            return None
        text = chosen[0].strip()
    else:
        text = segments[0]
        text = text.split(":", 1)[1].strip() if ":" in text else text
    if text == "all eight":
        return set(RUNS)
    if text.startswith("all except "):
        return set(RUNS) - set(re.findall(r"MPW-\d", text))
    if text in ("not recorded", "none"):
        return set()
    runs = set(re.findall(r"MPW-\d", text))
    return runs or None


class Index:
    """The tables and passages of ``index.md`` that the pages depend on."""

    def __init__(self, masks: Path) -> None:
        self.problems: list[str] = []
        self.text = (masks / "index.md").read_text()
        h2 = sections(self.text, "##")
        # code -> (step number, pattern steps, row cells)
        self.mask_steps: dict[str, tuple[int, list[int], list[str]]] = {}
        for row in table_rows(h2.get("Mask steps in this reference", "")):
            m = STEP_RE.search(row[0])
            if not m or not m.group(1) or len(row) < 6:
                continue
            pattern = [int(n) for _, n in STEP_RE.findall(row[4])]
            self.mask_steps[m.group(1)] = (int(m.group(2)), pattern, row)
        if not self.mask_steps:
            self.problems.append("no mask-step table under '## Mask steps in this reference'")
        self.order = sorted(n for n, _, _ in self.mask_steps.values())

        intro = h2.get("Plates recorded for the MPW runs", "").split("\n### ", 1)[0]
        self.sheet_names = {code: name for name, code in
                            SHEET_NAME_RE.findall(re.sub(r"\s+", " ", intro))}

        h3 = sections(self.text, "###")
        self.sets: dict[str, str] = {}
        for row in table_rows(h3.get("Runs, reticle sets and plate IDs", "")):
            m = CODE_CELL_RE.match(row[1]) if len(row) > 1 else None
            if row[0] in RUNS and m:
                self.sets[row[0]] = m.group(1)
        if sorted(self.sets) != RUNS:
            self.problems.append("cannot read a reticle set for every run from the index")

        # code -> {column: cell}
        self.plates: dict[str, dict[str, str]] = {}
        for row in table_rows(h3.get("Plates by mask", "")):
            m = STEP_RE.search(row[0])
            if m and m.group(1) and len(row) == 5:
                self.plates[m.group(1)] = dict(zip(INDEX_ROWS, (row[2], row[3], row[4])))

        # code -> "Sheet4" mask type
        self.types: dict[str, str] = {}
        types_text = re.sub(r"\s+", " ", h3.get("Mask types and plate labels", "").strip().split("\n\n")[0])
        found = list(TYPE_CODE_RE.finditer(types_text))
        for i, m in enumerate(found):
            end = found[i + 1].start() if i + 1 < len(found) else types_text.find(".", m.end())
            for code in ACRONYM_RE.findall(types_text[m.end():end]):
                self.types[code] = m.group(1)
        if not self.types:
            self.problems.append("cannot read the mask types under '### Mask types and plate labels'")

        for word in FORBIDDEN:
            if word in self.text.lower():
                self.problems.append(f"contains {word!r}")

    def pdk_cell(self, code: str) -> str:
        entry = self.mask_steps.get(code)
        return clean(entry[2][1]) if entry else ""

    def mask_name(self, code: str) -> tuple[str | None, str | None]:
        """(title name, name of the X variant) for a mask step, or (None, None)."""
        cell = self.pdk_cell(code)
        if cell == "*not listed*":
            return self.sheet_names.get(code), None
        entries = variants(cell)
        if not entries:
            return None, None
        marked = [name for name, _, x in entries if x]
        if len(marked) == 1:
            return marked[0], marked[0]
        if not marked and len(entries) == 1:
            return entries[0][0], None
        return None, None

    def plate_ids(self, code: str) -> dict[str, str] | None:
        """Expected plate-ID cell per run for a mask (None if unreadable)."""
        row = self.plates.get(code)
        if row is None:
            return None
        runs = recorded_runs(row["Plates recorded"], self.mask_name(code)[1])
        numbers = PLATE_NO_RE.findall(row["Plate no."])
        if runs is None or (runs and not numbers):
            return None
        overrides = dict(OVERRIDE_RE.findall(row["Plate no."]))
        expected = {}
        for run in RUNS:
            if run not in runs:
                expected[run] = NONE_RECORDED
                continue
            prefix = self.sets.get(run, "??")[2:]
            prefix = prefix[:-2] + "AA" if prefix.endswith("AC") else prefix
            expected[run] = f"`{prefix}{overrides.get(run, numbers[0])}A`"
        return expected


def step_pages(steps: Path) -> dict[int, tuple[str, str]]:
    """Map a step number to (code from its title, page text)."""
    pages = {}
    for page in steps.glob("[0-9][0-9][0-9]-*.md"):
        text = page.read_text()
        m = TITLE_RE.search(text)
        if m:
            pages[int(m.group(1))] = (m.group(2).strip(), text)
    return pages


def paragraph_after(body: str, intro: str) -> str | None:
    """The paragraph that follows a line reading exactly ``intro``."""
    m = re.search(rf"^{re.escape(intro)}[ \t]*\n[ \t]*\n(.+?)(?:\n[ \t]*\n|\Z)",
                  body, flags=re.MULTILINE | re.DOTALL)
    return m.group(1) if m else None


def check_pdk_row(value: str, code: str, index: Index) -> list[str]:
    cell = index.pdk_cell(code)
    if cell == "*not listed*":
        name = index.sheet_names.get(code)
        if not value.startswith("not listed"):
            return [f"'{PDK_ROW}' does not start 'not listed', as the index's cell does"]
        if name is None:
            return [f"the index names no 'Run Mask IDs' row for {code}"]
        if f'"{name}"' not in value:
            return [f"'{PDK_ROW}' does not quote the 'Run Mask IDs' name \"{name}\""]
        return []
    entries = variants(cell)
    if entries is None:
        return [f"cannot read the index's PDK mask cell for {code}"]
    problems = []
    for name, acronym, marked in entries:
        mark = "marked `X` in `Used in SKY130`" if marked else "unmarked"
        if f'"{name}", `{acronym}`, {mark}' not in value:
            problems.append(f"'{PDK_ROW}' does not give '\"{name}\", `{acronym}`, {mark}'")
    return problems


def check_token_row(name: str, value: str, index_cell: str) -> list[str]:
    index_cell = clean(index_cell)
    if index_cell in ("none", "none listed"):
        return [] if value == index_cell else [f"{name!r} is {value!r}; the index gives {index_cell!r}"]
    problems = []
    wanted = TOKEN_RE.findall(index_cell)
    if not is_subsequence(wanted, TOKEN_RE.findall(value)):
        problems.append(f"{name!r} does not give, in order, the index's {' '.join(wanted)}")
    if "(inference)" in index_cell and "inference" not in value:
        problems.append(f"{name!r} does not mark the index's inference")
    return problems


def check_facts(text: str, stem: str, code: str, name: str, index: Index,
                pages: dict[int, tuple[str, str]]) -> tuple[list[str], int | None]:
    """Check the quick-facts table; return problems and the stated step count."""
    head = text.split("\n## ", 1)[0]
    all_rows = table(head)
    if len(all_rows) < 4:
        return ["no quick-facts table before the first H2"], None
    header, rows = all_rows[0], all_rows[1:]
    problems = []
    if header != ["", f"{code} — {name}"]:
        problems.append(f"quick-facts header {header} is not ['', '{code} — {name}']")
    names = [r[0] for r in rows]
    if names != FACT_ROWS:
        problems.append(f"quick-facts rows {names} differ from {FACT_ROWS}")
    facts = {r[0]: clean(r[1]) if len(r) > 1 else "" for r in rows}

    entry = index.mask_steps.get(code)
    links = STEP_RE.findall(facts.get(FIRST_ROW, ""))
    if entry is None:
        problems.append(f"code {code!r} is not a mask step in the index's mask-step table")
    elif len(links) != 1:
        problems.append(f"'{FIRST_ROW}' row links {len(links)} steps, not one")
    else:
        text_, number = links[0]
        if text_ != code or int(number) != entry[0]:
            problems.append(
                f"'{FIRST_ROW}' row links {text_!r} step {number}; the index gives "
                f"{code} step {entry[0]:03d}"
            )
        m = STEP_OF_RE.search(facts[FIRST_ROW])
        if not m or int(m.group(1)) != entry[0] or int(m.group(2)) != len(pages):
            problems.append(f"'{FIRST_ROW}' row does not read 'step {entry[0]} of {len(pages)}'")
    if entry is not None:
        link = f"{{ref}}`{code} <mask-{stem}>`"
        if link not in " | ".join(entry[2]):
            problems.append(f"the index's mask-step row for {code} does not contain {link}")
        step_page = pages.get(entry[0])
        if step_page is not None and link not in step_page[1]:
            problems.append(f"step page {entry[0]:03d} does not contain {link}")

        if PDK_ROW in facts:
            problems += check_pdk_row(facts[PDK_ROW], code, index)
        for row, column in ((MASK_LAYER_ROW, 2), (DRAWN_ROW, 3), (CD_ROW, 5)):
            if row in facts:
                problems += check_token_row(row, facts[row], entry[2][column])
    if TONE_ROW in facts and not facts[TONE_ROW]:
        problems.append(f"'{TONE_ROW}' row is empty")
    if EXPOSURE_ROW in facts and not MACHINE_RE.search(facts[EXPOSURE_ROW]):
        problems.append(f"'{EXPOSURE_ROW}' row links no machine page")
    if TYPE_ROW in facts:
        kind = index.types.get(code)
        if kind is not None and not facts[TYPE_ROW].startswith(f"`{kind}`"):
            problems.append(f"'{TYPE_ROW}' does not start with the index's `{kind}`")
        if kind is None and facts[TYPE_ROW] != NO_TYPE:
            problems.append(f"'{TYPE_ROW}' is {facts[TYPE_ROW]!r}, not {NO_TYPE!r}")

    index_row = index.plates.get(code)
    if index_row is None:
        problems.append(f"no row for {code} in the index's 'Plates by mask' table")
    for row in INDEX_ROWS:
        if row in facts and index_row is not None and facts[row] != clean(index_row[row]):
            problems.append(f"{row!r}: page {facts[row]!r}, index {clean(index_row[row])!r}")

    count = None
    if LAST_ROW in facts:
        m = COUNT_RE.match(facts[LAST_ROW])
        if not m:
            problems.append(f"'{LAST_ROW}' row does not read 'N steps; see …'")
        else:
            count = int(m.group(1))
        if f"<mask-{stem}-steps>" not in facts[LAST_ROW]:
            problems.append(f"'{LAST_ROW}' row does not link mask-{stem}-steps")
    return problems, count


def check_plates(body: str, code: str, index: Index,
                 sheet: dict[str, dict[str, str]] | None) -> list[str]:
    expected = index.plate_ids(code)
    if expected is None:
        return [f"cannot derive the plate IDs of {code} from the index"]
    problems = []
    if sheet is not None:
        if code not in sheet:
            problems.append(f"no single 'Run Mask IDs' row for {code} in the sheet")
        elif sheet[code] != expected:
            problems.append(f"plate IDs derived from the index {expected} differ from the sheet's {sheet[code]}")
    lines = body.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("| Run |")), None)
    if start is None:
        return problems + ["no plate table (header '| Run |') under 'Plates and reticle sets'"]
    rows = table_rows("\n".join(lines[start:]))
    runs = [r[0] for r in rows]
    if runs != RUNS:
        problems.append(f"plate table lists runs {runs}, not MPW-1 to MPW-8 in order")
    for row in rows:
        run = row[0]
        if run not in expected or len(row) < 3:
            continue
        reticle = clean(row[1])
        if reticle != f"`{index.sets.get(run)}`":
            problems.append(f"plate table {run}: reticle set {reticle}, index `{index.sets.get(run)}`")
        plate = clean(row[2])
        if plate != expected[run]:
            problems.append(f"plate table {run}: plate ID {plate!r}, expected {expected[run]!r}")
    return problems


def check_steps(body: str, code: str, index: Index,
                pages: dict[int, tuple[str, str]]) -> tuple[list[str], int]:
    paragraph = paragraph_after(body, STEPS_INTRO)
    if paragraph is None:
        return [f"no paragraph after a '{STEPS_INTRO}' line in '{STEPS_H2}'"], 0
    links = [(t, int(n)) for t, n in STEP_RE.findall(paragraph)]
    steps = [n for _, n in links]
    entry = index.mask_steps.get(code)
    if entry is None:
        return [], len(steps)
    mask_step, pattern, _ = entry
    problems = []
    want = [mask_step] + pattern
    if steps != want:
        problems.append(f"steps {steps} differ from the mask step and index Patterns {want}")
    if not steps or steps != list(range(steps[0], steps[0] + len(steps))):
        problems.append("steps are not ascending and consecutive")
    later = [n for n in index.order if n > mask_step]
    if later and steps and max(steps) >= later[0]:
        problems.append(f"steps run into the next mask step, {later[0]:03d}")
    for text, number in links:
        page = pages.get(number)
        if page is None:
            problems.append(f"no step page for step {number:03d}")
            continue
        if not text:
            problems.append(f"link for step {number:03d} has no code text")
        elif text != page[0]:
            problems.append(f"link text {text!r} for step {number:03d} is not its code {page[0]!r}")
        if number != mask_step and f"step-{mask_step:03d}" not in page[1]:
            problems.append(f"step page {number:03d} does not link the mask step {mask_step:03d}")
    return problems, len(steps)


def check(page: Path, index: Index, pages: dict[int, tuple[str, str]],
          sheet: dict[str, dict[str, str]] | None) -> list[str]:
    text = page.read_text()
    stem = page.stem
    problems = []
    if not text.startswith(f"(mask-{stem})=\n"):
        problems.append(f"page does not start with a (mask-{stem})= label")
    title = PAGE_TITLE_RE.search(text)
    if not title:
        return problems + ["no '# CODE — name' title"]
    code, name = title.group(1), title.group(2).strip()
    if code.lower() != stem:
        problems.append(f"title code {code!r} does not match the file name {stem!r}")
    wanted_name = index.mask_name(code)[0]
    if wanted_name is None:
        problems.append(f"cannot read the mask name of {code} from the index")
    elif name != wanted_name:
        problems.append(f"title name {name!r} is not the index's {wanted_name!r}")

    h2 = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    if h2 != H2:
        problems.append(f"H2 headings {h2} differ from the template")
    body = sections(text, "##")
    for parent in H2:
        h3 = re.findall(r"^### (.+)$", body.get(parent, ""), flags=re.MULTILINE)
        if parent in H3:
            if h3 != H3[parent]:
                problems.append(f"H3 under '{parent}' {h3} differ from {H3[parent]}")
        elif any(h not in OPTIONAL_H3.get(parent, []) for h in h3):
            problems.append(f"H3 under '{parent}' {h3} are not among {OPTIONAL_H3.get(parent, [])}")
    if not re.search(rf"^\(mask-{re.escape(stem)}-steps\)=\n## {STEPS_H2}$", text,
                     flags=re.MULTILINE):
        problems.append(f"'## {STEPS_H2}' is not preceded by a (mask-{stem}-steps)= label")

    fact_problems, count = check_facts(text, stem, code, name, index, pages)
    problems += fact_problems

    renders = re.sub(r"\s+", " ", sections(body.get("Drawn layers and derivation", ""), "###")
                     .get("In the public renders", ""))
    dies = clean(index.plates.get(code, {}).get(INDEX_ROWS[2], ""))
    if dies != NOT_RENDERED:
        for phrase in RENDERS_PHRASES:
            if phrase not in renders:
                problems.append(f"'In the public renders' does not say {phrase!r}")

    problems += check_plates(body.get("Plates and reticle sets", ""), code, index, sheet)
    step_problems, n_steps = check_steps(body.get(STEPS_H2, ""), code, index, pages)
    problems += step_problems
    if count is not None and count != n_steps:
        problems.append(f"quick-facts table gives {count} steps, the steps paragraph has {n_steps}")
    for word in FORBIDDEN:
        if word in text.lower():
            problems.append(f"contains {word!r}")
    return problems


def read_sheet(path: Path, index: Index) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Plate-ID cells per run for each acronym of a "Run Mask IDs" CSV export.

    Where an acronym has several rows, the row marked ``X`` in the "Used
    in SKY130" column is used (none is returned if not exactly one is).
    """
    rows = list(csv.reader(path.open(newline="")))
    problems = []
    if len(rows) < 4:
        return {}, [f"{path}: too few rows for a 'Run Mask IDs' export"]
    columns = {}
    for run in RUNS:
        if run not in rows[0]:
            problems.append(f"{path}: no {run} column")
            continue
        col = rows[0].index(run)
        columns[run] = col
        if rows[2][col + 1:col + 2] != ["Plate ID"]:
            problems.append(f"{path}: no 'Plate ID' column for {run}")
        if rows[1][col] != index.sets.get(run):
            problems.append(f"sheet reticle set for {run} is {rows[1][col]!r}, index {index.sets.get(run)!r}")
    by_code: dict[str, list[list[str]]] = {}
    for row in rows[3:]:
        if len(row) > 2 and row[1]:
            by_code.setdefault(row[1], []).append(row)
    plates = {}
    for code, entries in by_code.items():
        marked = [r for r in entries if r[2].strip() == "X"]
        chosen = marked if len(entries) > 1 else entries
        if len(chosen) != 1:
            continue
        row = chosen[0]
        plates[code] = {run: (f"`{row[col + 1]}`" if len(row) > col + 1 and row[col + 1] else NONE_RECORDED)
                        for run, col in columns.items()}
    return plates, problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the per-mask pages.")
    parser.add_argument("masks", nargs="?", type=Path, default=MASKS,
                        help="masks directory (its sibling 'steps' holds the step pages)")
    parser.add_argument("--sheet", type=Path,
                        help="local CSV export of the sheet's 'Run Mask IDs' tab")
    args = parser.parse_args()
    index = Index(args.masks)
    pages = step_pages(args.masks.parent / "steps")
    bad = 0
    for problem in index.problems:
        bad += 1
        print(f"index.md: {problem}")
    sheet = None
    if args.sheet:
        sheet, sheet_problems = read_sheet(args.sheet, index)
        for problem in sheet_problems:
            bad += 1
            print(f"sheet: {problem}")
    mask_pages = sorted(p for p in args.masks.glob("*.md") if p.name != "index.md")
    for page in mask_pages:
        for problem in check(page, index, pages, sheet):
            bad += 1
            print(f"{page.name}: {problem}")
    link_problems: list[str] = []
    if args.masks == MASKS:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import gen_index_links
        link_problems = gen_index_links.stale_pages_in("masks")
        for p in link_problems:
            print(p)
    print(f"{len(mask_pages)} mask pages checked, {bad} problems, "
          f"{len(link_problems)} with a stale index-links block")
    return 1 if bad or link_problems else 0


if __name__ == "__main__":
    sys.exit(main())
