#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Generate the academic paper index pages from ``data/papers.yaml``.

Writes ``docs/references/papers/``:

* ``index.md`` — scope, how to read an entry, counts, links to the other
  views and the one full entry per paper (under its stored ``label``);
* ``by-topic.md``, ``by-module.md``, ``by-year.md``, ``by-venue.md``,
  ``by-institution.md``, ``by-device.md`` — one line per paper, linking
  the full entry;
* ``fab-publications.md`` — "Fab publications (Bloomington)": the
  ``fab-manufacturing`` records, which appear on no topic or device page.

The pages are overwritten; do not edit them by hand.  ``--check``
generates into memory and fails if a committed page differs, if a page
in the directory is not generated, or if a paper's ``label`` differs from
the label it has in ``data/papers.yaml`` at git ``HEAD`` (labels are
stable link targets and must never change).

Run with ``uv run tools/gen_papers.py [--check]``.  See
``docs/plans/paper-index-design.md``.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers.yaml"
OUT = ROOT / "docs" / "references" / "papers"
HEADER = "<!-- Generated from data/papers.yaml by tools/gen_papers.py; do not edit. -->\n"

TOPIC_NAMES = {
    "pdk-models": "PDK models and parameter extraction",
    "device-characterisation": "Device characterisation",
    "test-structures": "Test structures and test vehicles",
    "reliability": "Reliability and harsh environments",
    "radiation": "Radiation effects",
    "cryogenic": "Cryogenic operation",
    "high-temperature": "High-temperature operation",
    "rram": "RRAM (ReRAM)",
    "sonos": "SONOS memory",
    "floating-gate": "Floating-gate devices",
    "beol-integration": "BEOL-integrated devices",
    "photonics": "Photonics",
    "mems": "MEMS",
    "analog-rf": "Analog and RF circuits",
    "mixed-signal": "Data converters and mixed-signal circuits",
    "power-management": "Power management",
    "digital": "Digital circuits",
    "memory": "Memory",
    "sensors": "Sensors",
    "quantum": "Quantum",
    "security": "Hardware security",
    "tooling": "Open-source tooling",
    "education-shuttles": "Shuttle programmes and education",
    "fab-manufacturing": "Fab manufacturing",
    "lineage-s8": "Cypress S8 lineage",
}
TOPIC_GROUPS = [
    ("Process, PDK and devices", ["pdk-models", "device-characterisation", "test-structures", "reliability",
                                  "radiation", "cryogenic", "high-temperature", "rram", "sonos",
                                  "floating-gate", "beol-integration", "photonics", "mems"]),
    ("Circuits fabricated on the process", ["analog-rf", "mixed-signal", "power-management", "digital",
                                            "memory", "sensors", "quantum", "security"]),
    ("Ecosystem and lineage", ["tooling", "education-shuttles", "lineage-s8"]),
]
DEVICE_GROUPS = [
    ("MOSFET models and cryogenic devices", ["pdk-models", "cryogenic"]),
    ("RRAM", ["rram"]),
    ("SONOS and floating-gate nonvolatile memory", ["sonos", "floating-gate"]),
    ("BEOL-integrated devices", ["beol-integration"]),
    ("Test structures, reliability and radiation", ["test-structures", "reliability", "radiation"]),
    ("Analog and RF circuits", ["analog-rf"]),
    ("Data converters and mixed-signal circuits", ["mixed-signal"]),
    ("Power converters and regulators", ["power-management"]),
    ("Digital logic, memory and security", ["digital", "memory", "security"]),
    ("Sensors and quantum interfaces", ["sensors", "quantum"]),
]
BASIS_TEXT = {
    "named-process": "process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry",
    "affiliation-inference": "affiliation inference — the process or fab is not named; the link rests on author affiliations",
    "lineage-inference": "lineage inference — the process is not named; the link rests on public Cypress statements about the S8 lineage",
}
BASIS_SHORT = {"affiliation-inference": "affiliation inference", "lineage-inference": "lineage inference"}
VENUE_TYPE_NAMES = [
    ("journal", "Journal articles"), ("magazine", "Magazine articles"), ("conference", "Conference papers"),
    ("workshop", "Workshop papers"), ("preprint", "Preprints"), ("report", "Reports"),
]
MODULE_GROUPS = [
    ("overview-", "Overview pages"), ("step-", "Step pages"), ("mask-", "Mask pages"),
    ("category-", "Category pages"), ("machine-", "Machine pages"), ("material-", "Material pages"),
]
SOURCE_TEXT = {"abstract": "quoted from the abstract", "full text (HTML)": "quoted from the HTML full text",
               "full text (PDF)": "quoted from the PDF full text"}
PRIORITY_INSTITUTIONS = ("SkyWater Technology", "Cypress Semiconductor")

_ESC = re.compile(r"([\\`*_\[\]<>|#${}])")


def esc(text: str) -> str:
    return _ESC.sub(r"\\\1", str(text))


def url(u: str) -> str:
    return u.replace("(", "%28").replace(")", "%29").replace(" ", "%20")


def link(text: str, target: str) -> str:
    return f"[{esc(text)}]({url(target)})"


def join_names(names: list[str]) -> str:
    names = [esc(n) for n in names]
    if len(names) <= 2:
        return " and ".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]


def first_author(r: dict) -> str:
    a = r["authors"]
    return esc(a[0]) + (" et al." if len(a) > 2 else f" and {esc(a[1])}" if len(a) == 2 else "")


def plural(n: int) -> str:
    return f"{n} paper" if n == 1 else f"{n} papers"


def fab(r: dict) -> bool:
    return "fab-manufacturing" in r["topics"]


def citation(r: dict) -> str:
    parts = [f"{join_names(r['authors'])}.", f"\"{esc(r['title_display'])}.\"", f"*{esc(r['venue'])}*"]
    details = []
    if r.get("volume"):
        details.append(f"vol. {esc(r['volume'])}")
    if r.get("issue"):
        details.append(f"no. {esc(r['issue'])}")
    if r.get("pages"):
        p = str(r["pages"]).replace("-", "–")
        details.append(("p. " if "–" not in p else "pp. ") + esc(p))
    if r.get("article_number"):
        details.append(f"art. no. {esc(r['article_number'])}")
    details.append(str(r["year"]))
    return " ".join(parts) + ", " + ", ".join(details) + "."


def line(r: dict, extra: str = "") -> str:
    bits = [f"{{ref}}`{r['label']}`", f"{first_author(r)}, {esc(r['venue_series'])} {r['year']}"]
    marks = []
    if r["free_full_text"]:
        marks.append("free copy")
    if r["basis"] in BASIS_SHORT:
        marks.append(BASIS_SHORT[r["basis"]])
    s = "* " + " — ".join(bits)
    if marks:
        s += " (" + "; ".join(marks) + ")"
    if extra:
        s += " — " + extra
    return s


def entry(r: dict) -> list[str]:
    out = [f"({r['label']})=", f"### {esc(r['title_display'])}", "", citation(r), ""]
    links = []
    if r.get("doi"):
        links.append("DOI " + link(r["doi"], "https://doi.org/" + r["doi"]))
    if r.get("arxiv"):
        links.append("arXiv " + link(r["arxiv"]["id"], r["arxiv"]["url"]))
    if not (r.get("arxiv") and r["landing_url"] == r["arxiv"]["url"]):
        links.append(link("publisher or proceedings page", r["landing_url"]))
    out.append("* **Links:** " + " · ".join(links))
    copies = []
    for c in r["free_full_text"]:
        if c["url"] == r["landing_url"]:
            copies.append(f"free at the publisher or proceedings page ({esc(c['host'])}; {esc(c['oa_type'])})")
        elif r.get("arxiv") and c["url"] == r["arxiv"]["url"]:
            copies.append(f"arXiv ({esc(c['host'])}; {esc(c['oa_type'])})")
        else:
            copies.append(f"{link(c['host'], c['url'])} ({esc(c['oa_type'])})")
    out.append("* **Free copies:** " + ("; ".join(copies) if copies else "none located"))
    out.append("* **Access:** " + ("paywalled" if r["paywalled"] else "free to read"))
    basis = f"* **Basis:** {esc(BASIS_TEXT[r['basis']])}."
    if r["basis"] != "named-process" and r.get("notes"):
        basis += " " + esc(r["notes"])
    out.append(basis)
    out.append("* **Topics:** " + ", ".join(
        f"{{ref}}`{TOPIC_NAMES[t]} <papers-topic-{t}>`" if t != "fab-manufacturing"
        else "{ref}`Fab manufacturing <papers-fab-publications>`" for t in r["topics"]))
    out.append("* **Institutions:** " + "; ".join(esc(i) for i in r["institutions"]))
    if r.get("fabrication"):
        f = r["fabrication"]
        out.append(f"* **Fabrication ({SOURCE_TEXT[f['source']]}):** \"{esc(f['quote'])}\"")
    if r["related_docs"]:
        out.append("* **Related pages:**")
        for d in r["related_docs"]:
            out.append(f"  * {{ref}}`{d['label']}` — {esc(d['reason'])}")
    if r.get("notes") and r["basis"] == "named-process":
        out.append(f"* **Note:** {esc(r['notes'])}")
    out.append(f"* **Verified:** {esc(r['verified'])}")
    out.append("")
    return out


def page(label: str, title: str, body: list[str]) -> str:
    return HEADER + "\n" + f"({label})=\n# {title}\n\n" + "\n".join(body).rstrip() + "\n"


def by_author(rs: list[dict]) -> list[dict]:
    return sorted(rs, key=lambda r: (r["label"], r["year"]))


def gen_index(rs: list[dict]) -> str:
    n = len(rs)
    free = sum(1 for r in rs if r["free_full_text"])
    pay = sum(1 for r in rs if r["paywalled"])
    years = Counter(r["year"] for r in rs)
    basis = Counter(r["basis"] for r in rs)
    topics = Counter(t for r in rs for t in r["topics"])
    body = [
        "Academic papers whose subject is SKY130 or the SkyWater 130 nm process:",
        "device models and characterisation, test structures and reliability,",
        "devices and circuits fabricated on the process with silicon results, and",
        "the Cypress S8 lineage and the Bloomington fab. The list is a catalogue:",
        "a paper is added to the {doc}`public sources inventory <../public-sources>`",
        "only when a page cites it.",
        "",
        f"The index holds {n} papers: {pay} paywalled, {n - pay} free to read, and",
        f"{free} with at least one free copy (preprint, repository or publisher).",
        "Every entry was checked against its Crossref, arXiv or proceedings record.",
        "",
        "## Other views",
        "",
        "* {ref}`papers-by-topic`",
        "* {ref}`papers-by-module`",
        "* {ref}`papers-by-device`",
        "* {ref}`papers-by-year`",
        "* {ref}`papers-by-venue`",
        "* {ref}`papers-by-institution`",
        "* {ref}`papers-fab-publications`",
        "",
        "```{toctree}",
        ":hidden:",
        "",
        "by-topic",
        "by-module",
        "by-device",
        "by-year",
        "by-venue",
        "by-institution",
        "fab-publications",
        "```",
        "",
        "## Scope",
        "",
        "A paper is included when its subject is the open PDK and its models, a",
        "device, test structure or reliability study on SKY130, a circuit",
        "fabricated on the process with silicon or process-specific results, or",
        "the S8 lineage and the Bloomington fab. Papers that only simulate with",
        "the PDK, report no silicon or process results, concern another SkyWater",
        "process, or are theses, datasets, slides or posters are left out.",
        "",
        "Each entry states its **basis**, how its link to the process is",
        "established:",
        "",
        f"* **Process named** ({plural(basis['named-process'])}): {esc(BASIS_TEXT['named-process'].split(' — ', 1)[1])}.",
        f"* **Affiliation inference** ({plural(basis['affiliation-inference'])}): {esc(BASIS_TEXT['affiliation-inference'].split(' — ', 1)[1])}, as the entry's note explains.",
        f"* **Lineage inference** ({plural(basis['lineage-inference'])}): {esc(BASIS_TEXT['lineage-inference'].split(' — ', 1)[1])}, as the entry's note explains.",
        "",
        "Fabrication statements are quoted from the paper itself. Free copies are",
        "limited to legitimate sources: arXiv, OSTI, institutional repositories,",
        "preprint servers, open proceedings pages and open-access publisher",
        "versions.",
        "",
        "## How to read an entry",
        "",
        "Each entry gives the full citation (authors, title, venue, volume,",
        "issue, pages and year), the DOI, arXiv and publisher links, the free",
        "copies with their host and open-access type, whether the version of",
        "record is paywalled, the basis, the topics, the institutions named in",
        "the author affiliations, the fabrication statement where the paper",
        "gives one, the related pages of this reference, and the date and",
        "source of verification.",
        "",
        "## Counts",
        "",
        "| Year | Papers |",
        "|---|---|",
    ]
    body += [f"| {y} | {years[y]} |" for y in sorted(years)]
    body += ["", "| Topic | Papers |", "|---|---|"]
    order = [t for _, ts in TOPIC_GROUPS for t in ts] + ["fab-manufacturing"]
    body += [f"| {TOPIC_NAMES[t]} | {topics[t]} |" for t in order if topics[t]]
    body += ["", "## All papers", "", "Sorted by first author's family name, then year.", ""]
    for r in by_author(rs):
        body += entry(r)
    return page("papers-index", "Academic paper index", body)


def gen_topic(rs: list[dict]) -> str:
    body = [
        "Papers grouped by topic; a paper can appear under several topics. The",
        "fab-manufacturing papers are listed only on {ref}`papers-fab-publications`.",
        "Each line links the paper's full entry on {ref}`papers-index`.",
        "",
    ]
    rest = [r for r in rs if not fab(r)]
    for group, topics in TOPIC_GROUPS:
        body += [f"## {group}", ""]
        for t in topics:
            items = [r for r in rest if t in r["topics"]]
            body += [f"(papers-topic-{t})=", f"### {TOPIC_NAMES[t]}", ""]
            body += [f"{esc(TOPICS_DEF[t][0].upper() + TOPICS_DEF[t][1:])}.", ""]
            body += [line(r) for r in items] if items else ["No papers yet."]
            body.append("")
    return page("papers-by-topic", "Papers by topic", body)


def gen_module(rs: list[dict]) -> str:
    body = [
        "Papers grouped by the pages of this reference they relate to, with the",
        "reason for each link. Papers without a related page are listed at the end.",
        "",
    ]
    groups: dict[str, list[tuple[dict, str]]] = defaultdict(list)
    for r in rs:
        for d in r["related_docs"]:
            groups[d["label"]].append((r, d["reason"]))
    for prefix, heading in MODULE_GROUPS:
        labels = sorted(l for l in groups if l.startswith(prefix))
        if not labels:
            continue
        body += [f"## {heading}", ""]
        for lab in labels:
            body.append(f"* {{ref}}`{lab}`")
            for r, reason in groups[lab]:
                body.append("  " + line(r, esc(reason)))
        body.append("")
    none = [r for r in rs if not r["related_docs"]]
    body += ["## Papers without a related page", ""] + [line(r) for r in none] + [""]
    return page("papers-by-module", "Papers by process module", body)


def gen_device(rs: list[dict]) -> str:
    body = [
        "Papers grouped by the kind of device or circuit they study, derived from",
        "their topics; a paper can appear in several groups. The fab-manufacturing",
        "papers are listed only on {ref}`papers-fab-publications`.",
        "",
    ]
    rest = [r for r in rs if not fab(r)]
    for heading, topics in DEVICE_GROUPS:
        items = [r for r in rest if set(topics) & set(r["topics"])]
        body += [f"## {heading}", ""]
        body += [line(r) for r in items] if items else ["No papers yet."]
        body.append("")
    others = [r for r in rest if not any(set(t) & set(r["topics"]) for _, t in DEVICE_GROUPS)]
    if others:
        body += ["## Other papers", ""] + [line(r) for r in others] + [""]
    return page("papers-by-device", "Papers by device or circuit type", body)


def gen_year(rs: list[dict]) -> str:
    body = ["Papers by year of publication, newest first.", ""]
    for y in sorted({r["year"] for r in rs}, reverse=True):
        body += [f"## {y}", ""] + [line(r) for r in rs if r["year"] == y] + [""]
    return page("papers-by-year", "Papers by year", body)


def gen_venue(rs: list[dict]) -> str:
    body = ["Papers by type of venue, then by venue series.", ""]
    for vt, heading in VENUE_TYPE_NAMES:
        items = [r for r in rs if r["venue_type"] == vt]
        if not items:
            continue
        body += [f"## {heading}", ""]
        for s in sorted({r["venue_series"] for r in items}, key=str.casefold):
            body += [f"### {esc(s)}", ""] + [line(r) for r in items if r["venue_series"] == s] + [""]
    return page("papers-by-venue", "Papers by venue", body)


def gen_institution(rs: list[dict]) -> str:
    body = [
        "Papers by the institutions named in their author affiliations. SkyWater",
        "Technology and Cypress Semiconductor, whose staff worked at the fab, come",
        "first; the rest are alphabetical.",
        "",
    ]
    names = sorted({i for r in rs for i in r["institutions"]}, key=str.casefold)
    first = [n for n in names if n.startswith(PRIORITY_INSTITUTIONS)]
    for n in first + [n for n in names if n not in first]:
        body += [f"## {esc(n)}", ""] + [line(r) for r in rs if n in r["institutions"]] + [""]
    return page("papers-by-institution", "Papers by institution", body)


def gen_fab(rs: list[dict]) -> str:
    items = [r for r in rs if fab(r)]
    body = [
        "Manufacturing, yield and process-control papers by staff of the fab in",
        "Bloomington, Minnesota, grouped by the company named in the authors'",
        "affiliations: Cypress Semiconductor (Fab 4) and, later, SkyWater",
        "Technology. None of them names the process it describes; each is included",
        "on the basis of those affiliations, which its full entry explains. They are",
        "listed here and not on the topic or device pages.",
        "",
        "## Cypress Semiconductor",
        "",
    ]
    sky = [r for r in items if "SkyWater Technology" in r["institutions"]]
    body += [line(r) for r in items if r not in sky] + ["", "## SkyWater Technology", ""]
    body += [line(r) for r in sky] + [""]
    return page("papers-fab-publications", "Fab publications (Bloomington)", body)


TOPICS_DEF: dict[str, str] = {}


def generate() -> dict[str, str]:
    global TOPICS_DEF
    sys.path.insert(0, str(ROOT / "tools"))
    import check_papers  # noqa: PLC0415

    TOPICS_DEF = check_papers.TOPICS
    rs = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    return {
        "index.md": gen_index(rs),
        "by-topic.md": gen_topic(rs),
        "by-module.md": gen_module(rs),
        "by-device.md": gen_device(rs),
        "by-year.md": gen_year(rs),
        "by-venue.md": gen_venue(rs),
        "by-institution.md": gen_institution(rs),
        "fab-publications.md": gen_fab(rs),
    }


def label_changes() -> list[str]:
    try:
        old = subprocess.run(["git", "show", "HEAD:data/papers.yaml"], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return []
    before = {r["id"]: r.get("label") for r in yaml.safe_load(old) or [] if isinstance(r, dict)}
    now = {r["id"]: r.get("label") for r in yaml.safe_load(DATA.read_text(encoding="utf-8"))}
    return [f"{i}: label changed from {before[i]!r} to {now[i]!r}" for i in now
            if i in before and before[i] and before[i] != now[i]]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if committed pages differ from the generated ones")
    args = ap.parse_args()
    pages = generate()
    problems = label_changes()
    if args.check:
        for name, text in pages.items():
            p = OUT / name
            if not p.exists():
                problems.append(f"{p.relative_to(ROOT)}: missing")
            elif p.read_text(encoding="utf-8") != text:
                problems.append(f"{p.relative_to(ROOT)}: differs from generated output")
        if OUT.is_dir():
            for p in sorted(OUT.iterdir()):
                if p.name not in pages:
                    problems.append(f"{p.relative_to(ROOT)}: not generated by tools/gen_papers.py")
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        for name, text in pages.items():
            (OUT / name).write_text(text, encoding="utf-8")
    for p in problems:
        print(p)
    verb = "checked" if args.check else "written"
    print(f"{len(pages)} pages {verb}, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
