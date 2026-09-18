#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Check that patents which have not expired stay behind a collapsed block.

The owner's rule: a patent family that is not *certainly* expired is shown
only inside a collapsed block ("spoiler"), in the patent index and on the
process pages alike, so that a reader who must not read patents in force
can use the site without being shown their content.

This checker enforces the rule on the written pages:

* **The families.** Every family in ``data/patents.yaml`` whose ``expired``
  is not ``true`` is *restricted*: all of its member publication numbers and
  all of its titles (the family's and the members') are restricted strings.
* **The keys.** A restricted family is mapped to the inventory keys in
  ``docs/references/public-sources.md`` and to the footnote labels defined on
  the pages whose definition text names one of its numbers, so that a
  footnote reference such as ``[^pat-03]`` is recognised as a citation of a
  restricted patent even where the number itself is not written out.
* **The rule.** On every page under ``docs/`` outside
  ``docs/references/patents/`` and ``docs/plans/``, a footnote *reference* to
  such a label, a member's publication number in any of its usual spellings,
  or a restricted title, must sit inside a collapsed block — a ``{dropdown}``
  directive written as a colon fence or a backtick fence.
* **The exceptions.** A footnote *definition* at the foot of a page, and the
  patent's own entry in the inventory, may stay open — a citation must stay
  resolvable — but each must carry the flag sentence

      Shown as in force; estimated expiry YYYY-MM-DD (estimate from public
      records, not legal advice).

  (for a family whose status could not be bounded, the "status shown as
  unknown" wording) with the date the dataset gives, so the flag cannot
  drift away from the data.
* **The reverse report.** A collapsed note or a flag kept for a family that
  the dataset now shows as expired is reported, so the note can be opened up
  again. This is a report, not a failure.

Run with ``uv run tools/check_inforce.py [--selftest]``; the exit status is
non-zero when a problem is found.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "patents.yaml"
DOCS = ROOT / "docs"
INVENTORY = DOCS / "references" / "public-sources.md"
SKIP_DIRS = (DOCS / "references" / "patents", DOCS / "plans")

KEY_RE = re.compile(r"^\*\*([A-Z0-9][A-Z0-9_-]*)\*\*", re.M)
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([A-Za-z0-9][A-Za-z0-9-]*)\]:")
FOOTNOTE_REF_RE = re.compile(r"\[\^([A-Za-z0-9][A-Za-z0-9-]*)\](?!:)")
FENCE_OPEN_RE = re.compile(r"^\s*([:`]{3,})\{([A-Za-z0-9_-]+)\}")
FENCE_BARE_RE = re.compile(r"^\s*([:`]{3,})\s*$")
BACKTICK_CODE_RE = re.compile(r"^\s*(`{3,})(\S*)\s*$")

FLAG_IN_FORCE = ("Shown as in force; estimated expiry {date} "
                 "(estimate from public records, not legal advice).")
FLAG_UNKNOWN = ("Status shown as unknown; estimated expiry no later than {date} "
                "(estimate from public records, not legal advice).")
FLAG_RE = re.compile(
    r"(?:Shown as in force; estimated expiry (\d{4}-\d{2}-\d{2})"
    r"|Status shown as unknown; estimated expiry no later than (\d{4}-\d{2}-\d{2}))"
    r" \(estimate from public records, not legal advice\)\.")

# A title shorter than this many words is too generic to match safely in
# running prose ("Self-aligned shallow trench isolation"); the number is
# what catches those citations.
TITLE_MIN_WORDS = 5


# --------------------------------------------------------------------------
# dataset


def load_families(path: Path = DATA) -> list[dict]:
    data = yaml.safe_load(path.read_text())
    return data["families"]


def flag_for(fam: dict) -> str:
    date = fam["expiry"]["date"]
    tmpl = FLAG_IN_FORCE if fam["expired"] is False else FLAG_UNKNOWN
    return tmpl.format(date=date)


def number_spellings(number: str) -> list[str]:
    """Usual written spellings of one publication number, most specific first.

    ``US8093128B2`` -> ``US8093128B2``, ``US 8,093,128 B2``, ``8,093,128`` …
    ``US20090179253A1`` -> ``US 2009/0179253 A1`` …
    ``EP2104648B1`` -> ``EP 2 104 648 B1`` …
    """
    m = re.match(r"^([A-Z]{2})(\d+)([A-Z]\d?)?$", number)
    if not m:
        return [number]
    cc, digits, _kind = m.group(1), m.group(2), m.group(3) or ""
    cores = {digits}
    if cc == "US" and len(digits) == 11:                # published application
        cores.add(f"{digits[:4]}/{digits[4:]}")
    elif len(digits) in (7, 8):                         # granted patent
        cores.add(f"{int(digits):,}")
        if cc == "EP" and len(digits) == 7:
            cores.add(f"{digits[0]} {digits[1:4]} {digits[4:]}")
    return sorted(cores, key=len, reverse=True)


def number_pattern(number: str) -> re.Pattern:
    m = re.match(r"^([A-Z]{2})(\d+)([A-Z]\d?)?$", number)
    cc, kind = (m.group(1), m.group(3) or "") if m else ("", "")
    cores = "|".join(re.escape(c).replace(r"\ ", r"\s*") for c in number_spellings(number))
    cc_part = rf"(?:{cc}[\s .]*)?" if cc else ""
    kind_part = rf"(?:[\s ]*{kind})?" if kind else ""
    return re.compile(rf"(?<![0-9A-Za-z/,]){cc_part}(?:{cores}){kind_part}(?![0-9A-Za-z])")


def title_pattern(title: str) -> re.Pattern | None:
    words = title.split()
    if len(words) < TITLE_MIN_WORDS:
        return None
    return re.compile(r"\s+".join(re.escape(w) for w in words), re.I)


class Restricted:
    """One family that is not certainly expired, with its match patterns."""

    def __init__(self, fam: dict) -> None:
        self.id = fam["id"]
        self.representative = fam["representative"]
        self.expired = fam["expired"]
        self.expiry = fam["expiry"]["date"]
        self.flag = flag_for(fam)
        self.numbers = [m["number"] for m in fam["members"]]
        self.number_res = [(n, number_pattern(n)) for n in self.numbers]
        titles = {fam["title"]} | {m.get("title") or "" for m in fam["members"]}
        self.titles = sorted(t for t in titles if t)
        self.title_res = [(t, p) for t, p in
                          ((t, title_pattern(t)) for t in self.titles) if p]
        self.keys: set[str] = set()      # inventory keys
        self.labels: set[str] = set()    # footnote labels


def restricted_families(families: list[dict]) -> list[Restricted]:
    return [Restricted(f) for f in families if f["expired"] is not True]


def expired_families(families: list[dict]) -> list[Restricted]:
    return [Restricted(f) for f in families if f["expired"] is True]


# --------------------------------------------------------------------------
# page structure


def flatten(text: str) -> tuple[str, list[int]]:
    """Whitespace-normalised text plus, per character, its 1-based line number.

    Matching happens on the flattened text so that a number or a title split
    over a line break by Markdown re-wrapping is still found.
    """
    parts: list[str] = []
    lines: list[int] = []
    need_space = False
    for lineno, line in enumerate(text.split("\n"), start=1):
        toks = line.split()
        if not toks:
            continue
        if need_space:
            parts.append(" ")
            lines.append(lineno)
        joined = " ".join(toks)
        parts.append(joined)
        lines.extend([lineno] * len(joined))
        need_space = True
    return "".join(parts), lines


def dropdown_lines(text: str) -> set[int]:
    """1-based line numbers that sit inside a collapsed ``{dropdown}`` block."""
    inside: set[int] = set()
    stack: list[tuple[str, int, bool]] = []   # (fence char, length, is dropdown)
    for lineno, line in enumerate(text.splitlines(), start=1):
        if stack and any(d for _, _, d in stack):
            inside.add(lineno)
        m = FENCE_OPEN_RE.match(line)
        if m:
            marker, name = m.group(1), m.group(2)
            stack.append((marker[0], len(marker), name == "dropdown"))
            if name == "dropdown":
                # the directive line carries the dropdown's own title, which
                # is where the number and status legitimately appear
                inside.add(lineno)
            continue
        m = FENCE_BARE_RE.match(line)
        if m:
            marker = m.group(1)
            if stack and stack[-1][0] == marker[0] and len(marker) >= stack[-1][1]:
                stack.pop()
                continue
        m = BACKTICK_CODE_RE.match(line)
        if m and not FENCE_OPEN_RE.match(line):
            marker = m.group(1)
            if stack and stack[-1][0] == "`" and len(marker) >= stack[-1][1]:
                stack.pop()
            else:
                stack.append(("`", len(marker), False))
    return inside


def dropdown_blocks(text: str) -> list[tuple[int, str, set[int]]]:
    """Every ``{dropdown}``: (title line, title text, lines of its body)."""
    blocks: list[tuple[int, str, set[int]]] = []
    stack: list[tuple[str, int, int | None]] = []
    bodies: dict[int, set[int]] = {}
    titles: dict[int, str] = {}
    for lineno, line in enumerate(text.splitlines(), start=1):
        for _, _, start in stack:
            if start is not None:
                bodies[start].add(lineno)
        m = FENCE_OPEN_RE.match(line)
        if m:
            marker, name = m.group(1), m.group(2)
            start = lineno if name == "dropdown" else None
            if start is not None:
                bodies[start] = set()
                titles[start] = line.split("}", 1)[1].strip()
            stack.append((marker[0], len(marker), start))
            continue
        m = FENCE_BARE_RE.match(line)
        if m:
            marker = m.group(1)
            if stack and stack[-1][0] == marker[0] and len(marker) >= stack[-1][1]:
                stack.pop()
                continue
        m = BACKTICK_CODE_RE.match(line)
        if m and not FENCE_OPEN_RE.match(line):
            marker = m.group(1)
            if stack and stack[-1][0] == "`" and len(marker) >= stack[-1][1]:
                stack.pop()
            else:
                stack.append(("`", len(marker), None))
    for start, body in bodies.items():
        blocks.append((start, titles[start], body))
    return sorted(blocks)


def footnote_defs(text: str) -> dict[str, tuple[int, set[int], str]]:
    """label -> (first line, all its lines, its full text)."""
    lines = text.splitlines()
    defs: dict[str, tuple[int, set[int], str]] = {}
    i = 0
    while i < len(lines):
        m = FOOTNOTE_DEF_RE.match(lines[i])
        if not m:
            i += 1
            continue
        label = m.group(1)
        own = {i + 1}
        body = [lines[i]]
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip():
                if j + 1 < len(lines) and lines[j + 1].startswith("    "):
                    own.add(j + 1)
                    body.append(nxt)
                    j += 1
                    continue
                break
            if not nxt.startswith("    ") or FOOTNOTE_DEF_RE.match(nxt):
                break
            own.add(j + 1)
            body.append(nxt)
            j += 1
        defs[label] = (i + 1, own, "\n".join(body))
        i = j
    return defs


def inventory_entries(text: str) -> dict[str, tuple[set[int], str]]:
    """Inventory key -> (its line numbers, its paragraph text)."""
    entries: dict[str, tuple[set[int], str]] = {}
    lineno = 1
    for para in re.split(r"(\n\s*\n)", text):
        if para.startswith("\n"):
            lineno += para.count("\n")
            continue
        n = para.count("\n") + 1
        m = KEY_RE.match(para)
        if m:
            entries[m.group(1)] = (set(range(lineno, lineno + n)), para)
        lineno += para.count("\n")
    return entries


# --------------------------------------------------------------------------
# mapping restricted families to keys and labels


def pages(docs: Path = DOCS) -> list[Path]:
    out = []
    for p in sorted(docs.rglob("*.md")):
        if any(skip in p.parents for skip in SKIP_DIRS):
            continue
        out.append(p)
    return out


def map_keys_and_labels(fams: list[Restricted], page_text: dict[Path, str]) -> None:
    matcher = Matcher(fams)
    inv = inventory_entries(page_text.get(INVENTORY, ""))
    for key, (_lines, para) in inv.items():
        for _m, owners, kind, _v in matcher.finditer(flatten(para)[0]):
            if kind == "number":
                owners[0].keys.add(key)
                owners[0].labels.add(key.lower())
    for path, text in page_text.items():
        if path == INVENTORY:
            continue
        for label, (_l, _ls, body) in footnote_defs(text).items():
            for _m, owners, kind, _v in matcher.finditer(flatten(body)[0]):
                if kind == "number":
                    owners[0].labels.add(label)


# --------------------------------------------------------------------------
# the check


CANDIDATE_RE = re.compile(
    r"(?<![0-9A-Za-z])(?:(?P<cc>[A-Z]{2})[\s\u00a0.]{0,2})?"
    r"(?P<num>\d(?:[\d,/]*\d)?(?:[\s\u00a0]\d{3})*)"
    r"(?:[\s\u00a0]?(?P<kind>[A-Z]\d?))?(?![0-9A-Za-z])")


def normalise_number(cc: str | None, num: str, kind: str | None) -> tuple[str, str]:
    digits = re.sub(r"[^0-9]", "", num)
    return (cc or "") + digits + (kind or ""), digits


class Matcher:
    """Finds restricted numbers and titles in a flattened page, in one pass.

    Numbers are found by scanning for anything shaped like a publication
    number and normalising it (``US 8,093,128 B2`` and ``8093128`` both
    normalise to the dataset's ``US8093128B2``), which is linear in the page
    length however many families are restricted. Titles are pre-filtered on
    their longest word before the full pattern is tried.
    """

    def __init__(self, fams: list[Restricted]) -> None:
        self.fams = fams
        self.by_number: dict[str, Restricted] = {}
        for fam in fams:
            for n in fam.numbers:
                self.by_number[n] = fam
                m = re.match(r"^[A-Z]{2}(\d+)[A-Z]?\d?$", n)
                if m:
                    self.by_number.setdefault(m.group(1), fam)
        # sibling families often share a title, so a title match names every
        # restricted family that carries it: the citation is legitimate if
        # any one of them owns the line.
        shared: dict[str, list[Restricted]] = {}
        for fam in fams:
            for tt, _pat in fam.title_res:
                shared.setdefault(tt.lower(), []).append(fam)
        self.titles: list[tuple[str, re.Pattern, tuple[Restricted, ...]]] = []
        seen: set[str] = set()
        for fam in fams:
            for tt, pat in fam.title_res:
                if tt.lower() in seen:
                    continue
                seen.add(tt.lower())
                anchor = max(tt.replace("-", " ").split(), key=len).lower()
                self.titles.append((anchor, pat, tuple(shared[tt.lower()])))

    def finditer(self, flat: str):
        for m in CANDIDATE_RE.finditer(flat):
            full, digits = normalise_number(m.group("cc"), m.group("num"),
                                            m.group("kind"))
            fam = self.by_number.get(full) or self.by_number.get(digits)
            if fam is not None:
                yield m, (fam,), "number", full
        low = flat.lower()
        for anchor, pat, owners in self.titles:
            if anchor not in low:
                continue
            for m in pat.finditer(flat):
                yield m, owners, "title", m.group(0)


def check_page(path: Path, text: str, matcher: Matcher, label_fam: dict[str, Restricted],
               key_fam: dict[str, Restricted], expired: Matcher,
               problems: list[str], reverse: list[str]) -> None:
    rel = path.relative_to(ROOT) if ROOT in path.parents else path.name
    flat, linemap = flatten(text)
    inside = dropdown_lines(text)
    defs = footnote_defs(text)
    inv = inventory_entries(text) if path.name == INVENTORY.name else {}

    def line_of(pos: int) -> int:
        return linemap[pos] if pos < len(linemap) else (linemap[-1] if linemap else 1)

    # lines that may name a restricted family in the open, per family id
    own_lines: dict[str, set[int]] = {}
    for label, fam in label_fam.items():
        if label in defs:
            own_lines.setdefault(fam.id, set()).update(defs[label][1])
    for key, fam in key_fam.items():
        if key in inv:
            own_lines.setdefault(fam.id, set()).update(inv[key][0])

    # (a) footnote references
    for m in FOOTNOTE_REF_RE.finditer(text):
        fam = label_fam.get(m.group(1))
        if fam is None:
            continue
        lineno = text[:m.start()].count("\n") + 1
        if lineno in inside or lineno in own_lines.get(fam.id, ()):
            continue
        problems.append(
            f"{rel}:{lineno}: footnote reference [^{m.group(1)}] to "
            f"{fam.representative} ({fam.id}) outside a collapsed block")

    # (b) publication numbers, (c) titles
    for m, owners, kind, _value in matcher.finditer(flat):
        lineno = line_of(m.start())
        if lineno in inside or any(lineno in own_lines.get(f.id, ()) for f in owners):
            continue
        fam = owners[0]
        problems.append(
            f"{rel}:{lineno}: {kind} of {fam.representative} ({fam.id}) "
            f"outside a collapsed block: {flat[m.start():m.end()][:60]!r}")

    # the flag on footnote definitions and on the inventory entry
    for label, fam in sorted(label_fam.items()):
        if label not in defs:
            continue
        lineno, _, body = defs[label]
        check_flag(f"{rel}:{lineno}: footnote definition [^{label}]", body, fam, problems)
    for key, fam in sorted(key_fam.items()):
        if key not in inv:
            continue
        lines, body = inv[key]
        check_flag(f"{rel}:{min(lines)}: inventory entry {key}", body, fam, problems)

    # reverse report: collapsed notes and flags kept for a family that the
    # dataset now shows as expired, so they can be opened up again.
    blocks = dropdown_blocks(text)
    for start, title, _body in blocks:
        tflat = flatten(title)[0]
        if "in force" not in tflat.lower():
            continue
        for _m, owners, kind, _v in expired.finditer(tflat):
            if kind != "number":
                continue
            fam = owners[0]
            reverse.append(
                f"{rel}:{start}: collapsed note for {fam.representative} "
                f"({fam.id}), now shown as expired — it can be opened up")
            break
    for label, (lineno, _, body) in defs.items():
        bflat = flatten(body)[0]
        if not FLAG_RE.search(bflat):
            continue
        for _m, owners, kind, _v in expired.finditer(bflat):
            if kind != "number":
                continue
            fam = owners[0]
            reverse.append(
                f"{rel}:{lineno}: in-force flag on [^{label}] for "
                f"{fam.representative} ({fam.id}), now shown as expired")
            break
    for key, (lines, body) in inv.items():
        bflat = flatten(body)[0]
        if not FLAG_RE.search(bflat):
            continue
        for _m, owners, kind, _v in expired.finditer(bflat):
            if kind != "number":
                continue
            fam = owners[0]
            reverse.append(
                f"{rel}:{min(lines)}: in-force flag on inventory entry {key} "
                f"for {fam.representative} ({fam.id}), now shown as expired")
            break


def check_flag(where: str, body: str, fam: Restricted, problems: list[str]) -> None:
    flat = flatten(body)[0]
    m = FLAG_RE.search(flat)
    if not m:
        problems.append(f"{where}: cites {fam.representative} ({fam.id}) but "
                        f"carries no status flag; expected {fam.flag!r}")
        return
    if m.group(0) != fam.flag:
        problems.append(f"{where}: status flag {m.group(0)!r} does not match "
                        f"the dataset; expected {fam.flag!r}")


def run(docs: Path = DOCS) -> int:
    families = load_families()
    fams = restricted_families(families)
    expired = expired_families(families)
    page_text = {p: p.read_text() for p in pages(docs)}
    map_keys_and_labels(fams, page_text)
    label_fam = {l: f for f in fams for l in f.labels}
    key_fam = {k: f for f in fams for k in f.keys}
    matcher = Matcher(fams)
    expired_matcher = Matcher(expired)
    problems: list[str] = []
    reverse: list[str] = []
    for path, text in page_text.items():
        check_page(path, text, matcher, label_fam, key_fam, expired_matcher,
                   problems, reverse)
    for p in problems:
        print(p)
    for r in reverse:
        print("note:", r)
    print(f"{len(fams)} families not certainly expired "
          f"({len(key_fam)} inventory keys, {len(label_fam)} footnote labels), "
          f"{len(page_text)} pages checked, {len(problems)} problems, "
          f"{len(reverse)} notes that can be opened up")
    return 1 if problems else 0


# --------------------------------------------------------------------------
# self-test


def _fam(fid="GPX", expired=False, number="US8093128B2", expiry="2028-10-22",
         title="Integration of non-volatile charge trap memory devices"):
    return {"id": fid, "representative": number, "expired": expired,
            "expiry": {"date": expiry}, "title": title,
            "members": [{"number": number, "title": title}]}


def selftest() -> int:
    problems: list[str] = []

    def fail(msg):
        problems.append(msg)

    # 1. Number spellings.
    sp = number_spellings("US8093128B2")
    if "8,093,128" not in sp or "8093128" not in sp:
        fail(f"US granted spellings wrong: {sp}")
    if "2009/0179253" not in number_spellings("US20090179253A1"):
        fail("US application slash spelling missing")
    if "2 104 648" not in number_spellings("EP2104648B1"):
        fail("EP spaced spelling missing")
    pat = number_pattern("US8093128B2")
    for good in ["US8093128B2", "US 8,093,128 B2", "US 8,093,128", "8,093,128",
                 "US8093128"]:
        if not pat.search(good):
            fail(f"number pattern missed {good!r}")
    for bad in ["18,093,128", "US 8,093,1284", "US8093128B2X"]:
        if pat.search(bad):
            fail(f"number pattern matched {bad!r}")
    if number_pattern("US20090179253A1").search("US 2009/0179253 A1") is None:
        fail("application pattern missed the slash spelling")

    # 2. Titles shorter than the word minimum are not matched.
    if title_pattern("Self-aligned shallow trench isolation") is not None:
        fail("a four-word title should be too generic to match")
    tp = title_pattern("MOS transistor with ramped gate oxide thickness")
    if tp is None or not tp.search("a mos TRANSISTOR with ramped gate oxide thickness"):
        fail("title match is not case-insensitive")

    # 3. Flattening finds a number split over a line break.
    flat, lines = flatten("see US\n8,093,128 B2 here\n")
    if not number_pattern("US8093128B2").search(flat):
        fail("a number split over a line break was not found")
    if lines[flat.index("8,093,128")] != 2:
        fail("line map wrong for a wrapped match")

    # 4. Dropdown detection, colon and backtick fences, and nesting.
    text = ("a\n"
            ":::{dropdown} t\n"
            "b\n"
            ":::\n"
            "c\n"
            "````{dropdown} u\n"
            "```\n"
            "d\n"
            "```\n"
            "````\n"
            "e\n")
    inside = dropdown_lines(text)
    if inside != {2, 3, 4, 6, 7, 8, 9, 10}:
        fail(f"dropdown line set wrong: {sorted(inside)}")
    blocks = dropdown_blocks(text)
    if [t for _, t, _ in blocks] != ["t", "u"]:
        fail(f"dropdown titles wrong: {blocks}")

    # 5. Footnote definitions and their continuation lines.
    d = footnote_defs("x\n\n[^a]: one\n    two\n[^b]: three\n")
    if set(d) != {"a", "b"} or d["a"][1] != {3, 4}:
        fail(f"footnote definition parsing wrong: {d}")

    # 6. The flag sentence and its date.
    fam = Restricted(_fam())
    if fam.flag != ("Shown as in force; estimated expiry 2028-10-22 "
                    "(estimate from public records, not legal advice)."):
        fail(f"in-force flag wording wrong: {fam.flag!r}")
    unknown = Restricted(_fam(expired="unknown"))
    if "Status shown as unknown" not in unknown.flag:
        fail("unknown-status flag wording wrong")
    ps: list[str] = []
    check_flag("w", "[^pat-03]: US 8,093,128 B2. " + fam.flag, fam, ps)
    if ps:
        fail(f"a correct flag was rejected: {ps}")
    check_flag("w", "[^pat-03]: US 8,093,128 B2.", fam, ps)
    if len(ps) != 1 or "no status flag" not in ps[0]:
        fail(f"a missing flag was not reported: {ps}")
    ps.clear()
    check_flag("w", "[^x]: " + fam.flag.replace("2028-10-22", "2030-01-01"), fam, ps)
    if len(ps) != 1 or "does not match" not in ps[0]:
        fail(f"a stale flag date was not reported: {ps}")

    # 7. End to end on a synthetic page tree.
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        docs = Path(td)
        (docs / "references").mkdir()
        (docs / "references" / "public-sources.md").write_text(
            "# Inventory\n\n**PAT-03** — US 8,093,128 B2, a patent. " + fam.flag + "\n")
        good = ("# Page\n\n"
                "The step grows an oxide.[^pdk-01]\n\n"
                ":::{dropdown} From a patent shown as in force "
                "(US 8,093,128; estimated expiry 2028-10-22) — open to read\n"
                "It gives a range.[^pat-03]\n"
                ":::\n\n"
                "## References\n\n"
                "<!-- footnotes -->\n"
                "[^pdk-01]: The PDK.\n"
                "[^pat-03]: US 8,093,128 B2, a patent. " + fam.flag + "\n")
        (docs / "good.md").write_text(good)
        fams = [Restricted(_fam())]
        fams[0].keys.add("PAT-03")
        fams[0].labels.add("pat-03")
        matcher = Matcher(fams)
        label_fam = {"pat-03": fams[0]}
        key_fam = {"PAT-03": fams[0]}
        none = Matcher([])
        ps, rev = [], []
        check_page(docs / "good.md", good, matcher, label_fam, key_fam, none, ps, rev)
        if ps:
            fail(f"a compliant page was rejected: {ps}")
        inv_text = (docs / "references" / "public-sources.md").read_text()
        ps = []
        check_page(docs / "public-sources.md", inv_text, matcher, label_fam,
                   key_fam, none, ps, rev)
        if ps:
            fail(f"a flagged inventory entry was rejected: {ps}")
        ps = []
        check_page(docs / "public-sources.md",
                   inv_text.replace(" " + fams[0].flag, ""), matcher, label_fam,
                   key_fam, none, ps, rev)
        if not any("inventory entry" in p and "no status flag" in p for p in ps):
            fail(f"an unflagged inventory entry was not reported: {ps}")
        bad = good.replace("It gives a range.[^pat-03]\n:::",
                           ":::\n\nIt gives a range.[^pat-03]")
        ps = []
        check_page(docs / "bad.md", bad, matcher, label_fam, key_fam, none, ps, rev)
        if not any("footnote reference" in p for p in ps):
            fail(f"an open footnote reference was not reported: {ps}")
        bare = "# P\n\nThe patent US 8,093,128 B2 says so.\n\n## References\n"
        ps = []
        check_page(docs / "bare.md", bare, matcher, label_fam, key_fam, none, ps, rev)
        if not any("number of" in p for p in ps):
            fail(f"an open publication number was not reported: {ps}")
        # reverse report
        rev = []
        gone = Matcher([Restricted(_fam(expired=True))])
        check_page(docs / "good.md", good, Matcher([]), {}, {}, gone, [], rev)
        if not any("can be opened up" in r for r in rev):
            fail(f"the reverse report missed a now-expired collapsed note: {rev}")

    if problems:
        for p in problems:
            print("SELFTEST FAIL:", p)
        print(f"{len(problems)} selftest problem(s)")
        return 1
    print("selftest OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true",
                    help="run the offline self-test and exit; touches no files")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    return run()


if __name__ == "__main__":
    sys.exit(main())
