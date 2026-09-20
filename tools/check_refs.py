#!/usr/bin/env python3
"""Check footnote citations and reference tiers on written pages.

Rules (see docs/plans/citation-style.md):

* every ``[^label]`` reference has a definition and vice versa;
* no reference-style link definitions (``[label]: url``) remain;
* a written step page or per-mask page has at least 8 Deep dive
  entries, a category, machine, material or overview page and the masks
  index at least 12;
* every footnote label is a key in ``docs/references/public-sources.md``
  (keys are written there in upper case, e.g. ``**PDK-05**``).
* (rule 5, C4's invariant) every external URL written inline in the
  body of the page equals a URL inside one of that page's own footnote
  definitions, character for character, and every such inline link uses
  the angle-bracket form ``[text](<https://…>)``. The page is split at
  its first ``[^label]:`` definition line; everything before that is
  "body", everything from there on is "definitions". A markdown link
  whose target is not an ``http(s)`` URL (a ``{ref}``/relative link, an
  anchor, …) is not checked.

Stub pages (containing "This page is a stub." or "This section is a
stub.") are skipped.  Exit status
is non-zero on any violation.  Run with ``uv run tools/check_refs.py``.
Run with ``--selftest`` for the offline unit tests (touches no files).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

STUB_MARKERS = ("This page is a stub.", "This section is a stub.")
INVENTORY = DOCS / "references" / "public-sources.md"
KEY_RE = re.compile(r"^\*\*([A-Za-z0-9][A-Za-z0-9_-]*)\*\*", re.MULTILINE)
REF_RE = re.compile(r"\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\](?!:)")
DEF_RE = re.compile(r"^\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\]:", re.MULTILINE)
LINKDEF_RE = re.compile(r"^\[(?!\^)[^\]]+\]:\s*\S", re.MULTILINE)
BULLET_RE = re.compile(r"^\* ", re.MULTILINE)
FIRST_DEF_RE = re.compile(r"^\[\^[A-Za-z0-9][A-Za-z0-9_-]*\]:", re.MULTILINE)
DEF_URL_RE = re.compile(r"<(https?://[^<>\s]+)>")
BODY_LINK_RE = re.compile(r"\]\(([^)\n]*)\)")

TARGETS = [
    (DOCS / "steps", re.compile(r"^\d{3}-[a-z0-9-]+\.md$"), 8),
    (DOCS / "categories", re.compile(r"^(?!index)[a-z-]+\.md$"), 12),
    (DOCS / "machines", re.compile(r"^[a-z0-9-]+\.md$"), 12),
    (DOCS / "materials", re.compile(r"^[a-z0-9-]+\.md$"), 12),
    (DOCS / "masks", re.compile(r"^index\.md$"), 12),
    (DOCS / "masks", re.compile(r"^(?!index\.md$)[a-z0-9-]+\.md$"), 8),
    (DOCS / "overview", re.compile(r"^[a-z0-9-]+\.md$"), 12),
]


def deep_dive_count(text: str) -> int:
    m = re.search(r"^### Deep dive\n(.*?)(?=^## |^### |\Z)", text, re.S | re.M)
    if not m:
        return -1
    return len(BULLET_RE.findall(m.group(1)))


def inventory_keys() -> set[str]:
    return {k.lower() for k in KEY_RE.findall(INVENTORY.read_text())}


def split_body_and_defs(text: str) -> tuple[str, str]:
    """Split a page at its first footnote definition line.

    Everything before that line is "body" (prose, tables, reading lists);
    everything from it to the end of the page is "definitions". House
    style (citation-style.md rule 3) puts every definition at the very
    end of the page, so this is the boundary C4 describes.
    """
    m = FIRST_DEF_RE.search(text)
    if not m:
        return text, ""
    return text[: m.start()], text[m.start() :]


def inline_link_problems(text: str) -> list[str]:
    """C4's invariant: every inline external URL in the body must equal a
    URL in one of the page's own footnote definitions, and every such
    link must use the angle-bracket form ``[text](<https://…>)``.

    Returns ``"line N: ..."`` strings, one per offence; the caller (as
    every other problem in this checker) prefixes the page path.
    """
    body, defs = split_body_and_defs(text)
    def_urls = set(DEF_URL_RE.findall(defs))
    problems: list[str] = []
    for m in BODY_LINK_RE.finditer(body):
        target = m.group(1)
        bracketed = target.startswith("<") and target.endswith(">")
        url = target[1:-1] if bracketed else target
        if not url.startswith(("http://", "https://")):
            continue  # a {ref}/relative/anchor link, not an external URL
        lineno = body.count("\n", 0, m.start()) + 1
        if not bracketed:
            problems.append(
                f"line {lineno}: inline link not in angle-bracket form: "
                f"](<...>) required, found ]({target})"
            )
        if url not in def_urls:
            problems.append(
                f"line {lineno}: inline URL not in this page's own footnote "
                f"definitions: {url}"
            )
    return problems


def check(path: Path, min_deep: int, keys: set[str]) -> list[str]:
    text = path.read_text()
    problems: list[str] = []
    refs = set(REF_RE.findall(text))
    defs = DEF_RE.findall(text)
    dup = {d for d in defs if defs.count(d) > 1}
    defset = set(defs)
    if dup:
        problems.append(f"duplicate footnote definitions: {sorted(dup)}")
    if refs - defset:
        problems.append(f"undefined footnotes: {sorted(refs - defset)}")
    if defset - refs:
        problems.append(f"unreferenced footnotes: {sorted(defset - refs)}")
    if not refs:
        problems.append("no footnote citations")
    if refs - keys:
        problems.append(f"labels without inventory key: {sorted(refs - keys)}")
    if LINKDEF_RE.search(text):
        problems.append("reference-style link definitions present")
    n = deep_dive_count(text)
    if n < 0:
        problems.append("no '### Deep dive' section")
    elif n < min_deep:
        problems.append(f"Deep dive has {n} entries (minimum {min_deep})")
    problems.extend(inline_link_problems(text))
    return problems


def selftest() -> int:
    """Offline unit tests for the C4 inline-link invariant. Touches no files."""
    problems: list[str] = []

    def fail(msg: str) -> None:
        problems.append(msg)

    page_ok = (
        "Text with a link.[^a]\n\n"
        "## References\n\n"
        "### Deep dive\n\n"
        "* [Wikipedia, *Widget*](<https://en.wikipedia.org/wiki/Widget>) — a "
        "widget.[^a]\n\n"
        "[^a]: Wikipedia, *Widget*. <https://en.wikipedia.org/wiki/Widget>\n"
    )
    if inline_link_problems(page_ok):
        fail(f"a matching angle-bracket link was reported: {inline_link_problems(page_ok)}")

    # 1. An inline URL not present in any footnote definition is reported.
    page_mismatch = (
        "## References\n\n"
        "* [Wikipedia, *Widget*](<https://en.wikipedia.org/wiki/Gadget>) — a "
        "widget.[^a]\n\n"
        "[^a]: Wikipedia, *Widget*. <https://en.wikipedia.org/wiki/Widget>\n"
    )
    ps = inline_link_problems(page_mismatch)
    if not any("not in this page's own footnote" in p for p in ps):
        fail(f"a mismatched inline URL was not reported: {ps}")

    # 2. A bare (non-angle-bracket) inline link is reported, even when the
    #    URL itself matches a definition.
    page_bare = (
        "## References\n\n"
        "* [Wikipedia, *Widget*](https://en.wikipedia.org/wiki/Widget) — a "
        "widget.[^a]\n\n"
        "[^a]: Wikipedia, *Widget*. <https://en.wikipedia.org/wiki/Widget>\n"
    )
    ps = inline_link_problems(page_bare)
    if not any("not in angle-bracket form" in p for p in ps):
        fail(f"a bare-form inline link was not reported: {ps}")
    if any("not in this page's own footnote" in p for p in ps):
        fail(f"a bare-form link whose URL matches was wrongly reported as mismatched: {ps}")

    # 3. A {ref}/relative link (no http(s) target) is never reported.
    page_ref = (
        "See {ref}`step-006` and [the mask index](../masks/index.md).\n\n"
        "## References\n\n"
        "[^a]: Wikipedia, *Widget*. <https://en.wikipedia.org/wiki/Widget>\n"
    )
    ps = inline_link_problems(page_ref)
    if ps:
        fail(f"a non-external link was wrongly reported: {ps}")

    # 4. The body/definitions split happens at the *first* [^label]: line;
    #    a URL that appears only in a later definition still counts.
    page_multi_def = (
        "## References\n\n"
        "* [A](<https://a.example/>) — one.[^a]\n"
        "* [B](<https://b.example/>) — two.[^b]\n\n"
        "[^a]: A. <https://a.example/>\n"
        "[^b]: B. <https://b.example/>\n"
    )
    if inline_link_problems(page_multi_def):
        fail(f"a URL defined in a later footnote was wrongly reported: "
             f"{inline_link_problems(page_multi_def)}")

    if problems:
        for p in problems:
            print("FAIL:", p)
        return 1
    print("selftest OK")
    return 0


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return selftest()
    bad = 0
    checked = 0
    keys = inventory_keys()
    for directory, pattern, min_deep in TARGETS:
        if not directory.is_dir():
            continue
        for page in sorted(directory.iterdir()):
            if not pattern.match(page.name):
                continue
            text = page.read_text()
            if any(marker in text for marker in STUB_MARKERS):
                continue
            checked += 1
            problems = check(page, min_deep, keys)
            if problems:
                bad += 1
                for p in problems:
                    print(f"{page.relative_to(ROOT)}: {p}")
    print(f"{checked} written pages checked, {bad} with problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
