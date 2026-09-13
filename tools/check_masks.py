#!/usr/bin/env python3
"""Check the per-mask pages against their template and the masks index.

The masks index ``docs/masks/index.md`` has three tables this checker
reads: the table under "## Mask steps in this reference" (one row per
mask step, whose *Patterns* cell lists the steps that use the resist
pattern), the table under "### Runs, reticle sets and plate IDs" (the
reticle set of each MPW run) and the first table under "### Plates by
mask" (plates recorded, plate number and rendered dies for each mask
step).

For every ``docs/masks/*.md`` page except ``index.md``:

* the page starts with a ``(mask-<file stem>)=`` label and a title
  ``# CODE — name`` whose code, in lower case, is the file stem;
* the H2 headings are exactly the template's, in order, and the H3
  headings under "Drawn layers and derivation" and "References" are
  exactly the template's; the "Steps that use this mask" heading is
  preceded by a ``(mask-<stem>-steps)=`` label;
* the quick-facts table before the first H2 starts with a "Mask step"
  row that links exactly one step, with the page's code as link text,
  and that step is the mask step the index's mask-step table gives for
  the code; the index row links the page (``<mask-<stem>>``);
* the table's "Plates recorded", "Plate no." and "Dies with shapes,
  MPW-1 to MPW-8 (renders)" rows read exactly as the mask's cells in the
  index's "Plates by mask" table (footnote references are ignored);
* the table ends with a "Steps that use the pattern" row reading
  "N steps; see …" and linking ``mask-<stem>-steps``, where N is the
  number of steps in the steps paragraph;
* the plate table under "Plates and reticle sets" (the table whose
  header starts ``| Run |``) has one row per run, MPW-1 to MPW-8 in
  order, whose reticle-set cell is the index's set for the run and
  whose plate-ID cell is the plate ID implied by the index (the run's
  prefix — the set with its first two characters dropped and its final
  ``AC`` replaced by ``AA`` — the plate number and ``A``) for a run with
  a plate recorded, or "none recorded" otherwise;
* the steps paragraph (the paragraph after a line reading "Steps:" in
  "Steps that use this mask") links the mask step followed by exactly
  the steps of the index row's *Patterns* cell, in ascending,
  consecutive order, each with its step code (from the title of its
  step page) as link text, all before the next mask step of the index
  table; and every step after the mask step has a step page that links
  the mask step.

Exit status is non-zero on any problem.  Run with
``uv run tools/check_masks.py``; an optional argument names another
``masks`` directory to check (used to test the checker on a copy).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASKS = ROOT / "docs" / "masks"
STEPS = ROOT / "docs" / "steps"

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
STEPS_H2 = "Steps that use this mask"
STEPS_INTRO = "Steps:"
FIRST_ROW = "Mask step"
INDEX_ROWS = ("Plates recorded", "Plate no.", "Dies with shapes, MPW-1 to MPW-8 (renders)")
LAST_ROW = "Steps that use the pattern"
NONE_RECORDED = "none recorded"
RUNS = [f"MPW-{n}" for n in range(1, 9)]

# {ref}`CODE <step-NNN>` (group 1 the text, group 2 the number) or {ref}`step-NNN`.
STEP_RE = re.compile(r"\{ref\}`(?:([^`<]*?)\s*<)?step-(\d{3})>?`")
TITLE_RE = re.compile(r"^# Step (\d{3}) — (.+?):", re.MULTILINE)
FOOTNOTE_RE = re.compile(r"\[\^[A-Za-z0-9_-]+\]")
PAGE_TITLE_RE = re.compile(r"^# (\S+) — \S.*$", re.MULTILINE)
COUNT_RE = re.compile(r"^(\d+) steps?; see ")
PLATE_NO_RE = re.compile(r"`(\d{3})`")
OVERRIDE_RE = re.compile(r"(MPW-\d): `(\d{3})`")
CODE_CELL_RE = re.compile(r"^`([^`]+)`$")


def sections(text: str, level: str) -> dict[str, str]:
    """Map each heading of the given level (``##`` or ``###``) to its body."""
    parts = re.split(rf"^{level} (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def clean(cell: str) -> str:
    return re.sub(r"\s+", " ", FOOTNOTE_RE.sub("", cell)).strip()


def table_rows(body: str) -> list[list[str]]:
    """Cells of the data rows of the first Markdown table in ``body``."""
    rows, started = [], False
    for line in body.splitlines():
        if line.startswith("|"):
            started = True
            if not re.match(r"^\|[-| :]+\|$", line.strip()):
                rows.append(cells(line))
        elif started:
            break
    return rows[1:]


def recorded_runs(cell: str) -> set[str] | None:
    """Runs with a plate, from a "Plates recorded" cell (None if unreadable)."""
    text = cell.split(";")[0]
    text = text.split(":", 1)[1] if ":" in text else text
    text = text.strip()
    if text == "all eight":
        return set(RUNS)
    if text.startswith("all except "):
        return set(RUNS) - set(re.findall(r"MPW-\d", text))
    if text in ("not recorded", "none"):
        return set()
    runs = set(re.findall(r"MPW-\d", text))
    return runs or None


class Index:
    """The mask-step, reticle-set and plates tables of ``index.md``."""

    def __init__(self, masks: Path) -> None:
        self.problems: list[str] = []
        text = (masks / "index.md").read_text()
        h2 = sections(text, "##")
        # code -> (step number, pattern steps, row text)
        self.mask_steps: dict[str, tuple[int, list[int], str]] = {}
        for row in table_rows(h2.get("Mask steps in this reference", "")):
            m = STEP_RE.search(row[0])
            if not m or not m.group(1):
                continue
            pattern = [int(n) for _, n in STEP_RE.findall(row[4])] if len(row) > 4 else []
            self.mask_steps[m.group(1)] = (int(m.group(2)), pattern, " | ".join(row))
        if not self.mask_steps:
            self.problems.append("no mask-step table under '## Mask steps in this reference'")
        self.order = sorted(n for n, _, _ in self.mask_steps.values())

        h3 = sections(text, "###")
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

    def plate_ids(self, code: str) -> dict[str, str] | None:
        """Expected plate-ID cell per run for a mask (None if unreadable)."""
        row = self.plates.get(code)
        if row is None:
            return None
        runs = recorded_runs(row["Plates recorded"])
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


def step_pages() -> dict[int, tuple[str, str]]:
    """Map a step number to (code from its title, page text)."""
    pages = {}
    for page in STEPS.glob("[0-9][0-9][0-9]-*.md"):
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


def check_facts(text: str, stem: str, code: str, index: Index) -> tuple[list[str], int | None]:
    """Check the quick-facts table; return problems and the stated step count."""
    head = text.split("\n## ", 1)[0]
    rows = table_rows(head)
    if len(rows) < 3:
        return ["no quick-facts table before the first H2"], None
    problems = []
    facts = {r[0]: r[1] if len(r) > 1 else "" for r in rows}
    if rows[0][0] != FIRST_ROW:
        problems.append(f"quick-facts table starts with {rows[0][0]!r}, not {FIRST_ROW!r}")
    links = STEP_RE.findall(facts.get(FIRST_ROW, ""))
    entry = index.mask_steps.get(code)
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
    if entry is not None and f"<mask-{stem}>" not in entry[2]:
        problems.append(f"the index's mask-step row for {code} does not link mask-{stem}")

    index_row = index.plates.get(code)
    if index_row is None:
        problems.append(f"no row for {code} in the index's 'Plates by mask' table")
    for name in INDEX_ROWS:
        if name not in facts:
            problems.append(f"quick-facts table has no {name!r} row")
        elif index_row is not None and clean(facts[name]) != clean(index_row[name]):
            problems.append(
                f"{name!r}: page {clean(facts[name])!r}, index {clean(index_row[name])!r}"
            )

    count = None
    if rows[-1][0] != LAST_ROW:
        problems.append(f"quick-facts table ends with {rows[-1][0]!r}, not {LAST_ROW!r}")
    else:
        last = rows[-1][1] if len(rows[-1]) > 1 else ""
        m = COUNT_RE.match(last)
        if not m:
            problems.append(f"'{LAST_ROW}' row does not read 'N steps; see …'")
        else:
            count = int(m.group(1))
        if f"<mask-{stem}-steps>" not in last:
            problems.append(f"'{LAST_ROW}' row does not link mask-{stem}-steps")
    return problems, count


def check_plates(body: str, code: str, index: Index) -> list[str]:
    expected = index.plate_ids(code)
    if expected is None:
        return [f"cannot derive the plate IDs of {code} from the index"]
    lines = body.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("| Run |")), None)
    if start is None:
        return ["no plate table (header '| Run |') under 'Plates and reticle sets'"]
    rows = table_rows("\n".join(lines[start:]))
    problems = []
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
        if text and text != page[0]:
            problems.append(f"link text {text!r} for step {number:03d} is not its code {page[0]!r}")
        if number != mask_step and f"step-{mask_step:03d}" not in page[1]:
            problems.append(f"step page {number:03d} does not link the mask step {mask_step:03d}")
    return problems, len(steps)


def check(page: Path, index: Index, pages: dict[int, tuple[str, str]]) -> list[str]:
    text = page.read_text()
    stem = page.stem
    problems = []
    if not text.startswith(f"(mask-{stem})=\n"):
        problems.append(f"page does not start with a (mask-{stem})= label")
    title = PAGE_TITLE_RE.search(text)
    if not title:
        return problems + ["no '# CODE — name' title"]
    code = title.group(1)
    if code.lower() != stem:
        problems.append(f"title code {code!r} does not match the file name {stem!r}")

    h2 = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    if h2 != H2:
        problems.append(f"H2 headings {h2} differ from the template")
    body = sections(text, "##")
    for parent, wanted in H3.items():
        h3 = re.findall(r"^### (.+)$", body.get(parent, ""), flags=re.MULTILINE)
        if h3 != wanted:
            problems.append(f"H3 under '{parent}' {h3} differ from {wanted}")
    if not re.search(rf"^\(mask-{re.escape(stem)}-steps\)=\n## {STEPS_H2}$", text,
                     flags=re.MULTILINE):
        problems.append(f"'## {STEPS_H2}' is not preceded by a (mask-{stem}-steps)= label")

    fact_problems, count = check_facts(text, stem, code, index)
    problems += fact_problems
    problems += check_plates(body.get("Plates and reticle sets", ""), code, index)
    step_problems, n_steps = check_steps(body.get(STEPS_H2, ""), code, index, pages)
    problems += step_problems
    if count is not None and count != n_steps:
        problems.append(f"quick-facts table gives {count} steps, the steps paragraph has {n_steps}")
    return problems


def main() -> int:
    masks = Path(sys.argv[1]) if len(sys.argv) > 1 else MASKS
    index = Index(masks)
    pages = step_pages()
    mask_pages = sorted(p for p in masks.glob("*.md") if p.name != "index.md")
    bad = 0
    for problem in index.problems:
        bad += 1
        print(f"index.md: {problem}")
    for page in mask_pages:
        for problem in check(page, index, pages):
            bad += 1
            print(f"{page.name}: {problem}")
    print(f"{len(mask_pages)} mask pages checked, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
