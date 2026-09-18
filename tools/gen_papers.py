#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Generate the academic paper index pages from ``data/papers.yaml``.

Writes ``docs/references/papers/``:

* ``index.md`` — scope, how to read an entry, counts, links to the other
  views and the one full entry per paper (under its stored ``label``);
* ``by-topic.md``, ``by-module.md`` (papers by related page),
  ``by-device.md``, ``by-year.md``, ``by-venue.md``, ``by-institution.md``
  — one line per paper, linking the full entry;
* ``fab-publications.md`` — "Fab publications (Bloomington)": the
  ``fab-manufacturing`` records, which the topic and device pages only
  point to.

The pages are overwritten; do not edit them by hand.  Before generating,
the dataset must pass ``tools/check_papers.py``'s offline checks
(including the append-only label map ``data/papers-labels.yaml``).

``--check`` generates into memory and fails if a committed page differs,
if a page in the directory is not generated, or if an entry of the label
map at the merge base with ``main`` (or ``HEAD`` when there is none) has
been removed or changed, so that a published label can never be dropped,
renamed or reused, even after the change is committed.

Run with ``uv run tools/gen_papers.py [--check]``.  See
``docs/plans/paper-index-design.md``.
"""

from __future__ import annotations

import datetime as dt
import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers.yaml"
LABELS = ROOT / "data" / "papers-labels.yaml"
OUT = ROOT / "docs" / "references" / "papers"
HEADER = "<!-- Generated from data/papers.yaml by tools/gen_papers.py; do not edit. -->\n"

sys.path.insert(0, str(ROOT / "tools"))
import check_papers  # noqa: E402

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
    ("Circuits designed for or fabricated on the process", ["analog-rf", "mixed-signal", "power-management",
                                                            "digital", "memory", "sensors", "quantum",
                                                            "security"]),
    ("Ecosystem and lineage", ["tooling", "education-shuttles", "lineage-s8"]),
]
# Pages of this reference that a topic section points to.
TOPIC_PAGES = {
    "rram": ["overview-sky130b-reram"],
    "beol-integration": ["overview-sky130b-reram"],
    "sonos": ["step-040"],
}
MEMORY_DEVICES = {"rram", "sonos", "floating-gate", "beol-integration"}
BASIS_TEXT = {
    "named-process": "the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry",
    "affiliation-inference": "the process or fab is not named; the link rests on author affiliations",
    "lineage-inference": "the process is not named; the link rests on public Cypress statements about the S8 lineage",
}
BASIS_NAME = {"named-process": "process named", "affiliation-inference": "affiliation inference",
              "lineage-inference": "lineage inference"}
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
HOST_NAMES = {
    "ieeexplore.ieee.org": "IEEE Xplore", "dl.acm.org": "ACM Digital Library", "pubs.aip.org": "AIP Publishing",
    "academic.oup.com": "Oxford Academic", "ietresearch.onlinelibrary.wiley.com": "Wiley Online Library",
    "onlinelibrary.wiley.com": "Wiley Online Library", "www.mdpi.com": "MDPI", "arxiv.org": "arXiv",
    "woset-workshop.github.io": "WOSET proceedings", "www.osti.gov": "OSTI", "escholarship.org": "eScholarship",
    "upcommons.upc.edu": "UPCommons", "www.authorea.com": "Authorea", "www.techrxiv.org": "TechRxiv",
}

_ESC = re.compile(r"([\\`*_\[\]<>|#${}])")


def esc(text: object) -> str:
    return _ESC.sub(r"\\\1", " ".join(str(text).split()))


def url(u: str) -> str:
    return u.replace("(", "%28").replace(")", "%29").replace(" ", "%20")


def link(text: str, target: str) -> str:
    return f"[{esc(text)}]({url(target)})"


def host_name(u: str) -> str:
    host = re.sub(r"^https://([^/]+)/?.*$", r"\1", u)
    return HOST_NAMES.get(host, host)


def plural(n: int, word: str = "paper") -> str:
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def join_names(names: list[str]) -> str:
    names = [esc(n) for n in names]
    if len(names) <= 2:
        return " and ".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]


def first_author(r: dict) -> str:
    a = r["authors"]
    return esc(a[0]) + (" et al." if len(a) > 2 else f" and {esc(a[1])}" if len(a) == 2 else "")


def fab(r: dict) -> bool:
    return "fab-manufacturing" in r["topics"]


def venue_display(v: str) -> str:
    v = re.sub(r"\s*\(Cat\.?\s*No\.?[^)]*\)", "", v)
    return v.rstrip(" .,")


def citation(r: dict) -> str:
    parts = [f"{join_names(r['authors'])}.", f"\"{esc(r['title_display'])}.\"", f"*{esc(venue_display(r['venue']))}*"]
    details = []
    if r.get("volume"):
        details.append(f"vol. {esc(r['volume'])}")
    if r.get("issue"):
        details.append(f"no. {esc(r['issue'])}")
    if r.get("pages"):
        p = str(r["pages"]).replace("-", "–")
        details.append(("pp. " if "–" in p else "p. ") + esc(p))
    if r.get("article_number"):
        details.append(f"art. no. {esc(r['article_number'])}")
    details.append(str(r["year"]))
    return " ".join(parts) + ", " + ", ".join(details) + "."


def line(r: dict, extra: str = "") -> str:
    s = f"* {{ref}}`{r['label']}` — {first_author(r)}, {esc(r['venue_series'])} {r['year']}"
    marks = []
    if r["free_full_text"]:
        marks.append("free copy")
    if r["basis"] != "named-process":
        marks.append(BASIS_NAME[r["basis"]])
    if marks:
        s += " (" + "; ".join(marks) + ")"
    if extra:
        s += " — " + extra
    return s


def checked_text(r: dict) -> str:
    date = r["verified"][:10]
    if r["id"].startswith("doi:"):
        src = "the Crossref record" + (" and the arXiv abstract page" if r.get("arxiv") else "")
    elif r["id"].startswith("arxiv:"):
        src = "the arXiv abstract page"
    else:
        src = "the proceedings page"
    return f"{date} against {src}"


def entry(r: dict) -> list[str]:
    out = [f"({r['label']})=", f"### {esc(r['title_display'])}", "", citation(r), ""]
    is_arxiv_only = bool(r.get("arxiv")) and r["landing_url"] == r["arxiv"]["url"]
    record = []
    if is_arxiv_only:
        record.append("arXiv " + link(r["arxiv"]["id"], r["arxiv"]["url"]) + " (preprint, free)")
    else:
        record.append(link(host_name(r["landing_url"]), r["landing_url"])
                      + (" (paywalled)" if r["paywalled"] else " (free to read)"))
    if r.get("doi"):
        record.append("DOI " + link(r["doi"], "https://doi.org/" + r["doi"]))
    if r.get("arxiv") and not is_arxiv_only:
        record.append("arXiv " + link(r["arxiv"]["id"], r["arxiv"]["url"]))
    out.append("* **Publication:** " + " · ".join(record))
    copies = []
    for c in r["free_full_text"]:
        if r.get("arxiv") and c["url"] == r["arxiv"]["url"]:
            if not is_arxiv_only:
                copies.append(f"arXiv preprint — {esc(c['oa_type'])}")
        elif c["url"] == r["landing_url"]:
            copies.append(f"the {esc(host_name(c['url']))} page above — {esc(c['oa_type'])}")
        else:
            copies.append(f"{link(host_name(c['url']), c['url'])} — {esc(c['oa_type'])}")
    if copies:
        out.append("* **Free copies:** " + "; ".join(copies))
    elif not is_arxiv_only:
        out.append("* **Free copies:** none located")
    if r["basis"] == "named-process":
        out.append("* **Basis:** process named (see {ref}`papers-scope`).")
    else:
        out.append(f"* **Basis:** {esc(BASIS_NAME[r['basis']])} — {esc(BASIS_TEXT[r['basis']])}. {esc(r['notes'])}")
    out.append("* **Topics:** " + ", ".join(
        f"{{ref}}`{TOPIC_NAMES[t]} <papers-topic-{t}>`" if t != "fab-manufacturing"
        else "{ref}`Fab manufacturing <papers-fab-publications>`" for t in r["topics"]))
    out.append("* **Institutions:** " + "; ".join(esc(i) for i in r["institutions"]))
    if r.get("fabrication"):
        f = r["fabrication"]
        out.append(f"* **Process and fabrication ({SOURCE_TEXT[f['source']]}):** \"{esc(f['quote'])}\"")
    if r["related_docs"]:
        out.append("* **Related pages:**")
        for d in r["related_docs"]:
            out.append(f"  * {{ref}}`{d['label']}` — {esc(d['reason'])}")
    if r.get("notes") and r["basis"] == "named-process":
        out.append(f"* **Note:** {esc(r['notes'])}")
    out.append(f"* **Checked:** {esc(checked_text(r))}.")
    out.append("")
    return out


def page(label: str, title: str, body: list[str]) -> str:
    return HEADER + "\n" + f"({label})=\n# {title}\n\n" + "\n".join(body).rstrip() + "\n"


def fab_note(n: int) -> list[str]:
    if not n:
        return []
    return [f"Also {plural(n, 'fab publication')} with this topic: see {{ref}}`papers-fab-publications`.", ""]


def gen_index(rs: list[dict]) -> str:
    n = len(rs)
    pay = [r for r in rs if r["paywalled"]]
    pay_free = sum(1 for r in pay if r["free_full_text"])
    years = Counter(r["year"] for r in rs)
    basis = Counter(r["basis"] for r in rs)
    fabs = [r for r in rs if fab(r)]
    topics = Counter(t for r in rs if not fab(r) for t in r["topics"])
    fab_topics = Counter(t for r in fabs for t in r["topics"])
    body = [
        "Academic papers whose subject is SKY130 or the SkyWater 130 nm process:",
        "device models and characterisation, test structures and reliability,",
        "devices and circuits designed for or fabricated on the process, and the",
        "Cypress S8 lineage and the Bloomington fab. The list is a catalogue: a",
        "paper is added to the {doc}`public sources inventory <../public-sources>`",
        "only when a page cites it.",
        "",
        f"The index holds {plural(n)}. The version of record is free to read for",
        f"{n - len(pay)} and paywalled for {len(pay)}; {pay_free} of the paywalled papers have a free",
        "preprint or repository copy. Every entry was checked against its Crossref,",
        "arXiv or proceedings record.",
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
        "* {ref}`papers-designed-on-sky130` — excluded papers that name the process",
        "  without reporting fabricated silicon; not part of the index proper.",
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
        "designed-on-sky130",
        "```",
        "",
        "(papers-scope)=",
        "## Scope",
        "",
        "A paper is included when its subject is the open PDK and its models, a",
        "device, test structure or reliability study on SKY130, a circuit",
        "fabricated on the process with silicon or process-specific results, or",
        "the S8 lineage and the Bloomington fab. Papers that only simulate with",
        "the PDK (unless they characterise the process or its models), report no",
        "silicon or process results, concern another SkyWater process, or are",
        "theses, datasets, slides or posters are left out. Marginal cases are",
        "marked \"Borderline inclusion\" in their entries.",
        "",
        "Each entry states its **basis**, how its link to the process is",
        "established:",
        "",
        f"* **Process named** ({plural(basis['named-process'])}): {esc(BASIS_TEXT['named-process'])}.",
        f"* **Affiliation inference** ({plural(basis['affiliation-inference'])}): {esc(BASIS_TEXT['affiliation-inference'])}; the entry explains the inference.",
        f"* **Lineage inference** ({plural(basis['lineage-inference'])}): {esc(BASIS_TEXT['lineage-inference'])}; the entry explains the inference.",
        "",
        "Process and fabrication statements are quoted from the paper itself.",
        "Free copies are limited to legitimate sources: arXiv, OSTI, institutional",
        "repositories, preprint servers, open proceedings pages and open-access",
        "publisher versions.",
        "",
        "## How to read an entry",
        "",
        "Each entry gives the full citation (authors, title, venue, volume, issue,",
        "pages and year); where it is published, with its host, access and DOI or",
        "arXiv link; the free copies with their open-access type; the basis; the",
        "topics; the institutions named in the author affiliations; a quotation",
        "naming the process or the fabrication where the paper gives one; the",
        "related pages of this reference; and the date and record it was checked",
        "against.",
        "",
        "## Counts",
        "",
        "By year: " + ", ".join(f"{{ref}}`{y} <papers-year-{y}>` ({years[y]})" for y in sorted(years)) + ".",
        "",
        "| Topic | Papers | Also among the fab publications |",
        "|---|---|---|",
    ]
    order = [t for _, ts in TOPIC_GROUPS for t in ts]
    for t in order:
        if topics[t] or fab_topics[t]:
            body.append(f"| {{ref}}`{TOPIC_NAMES[t]} <papers-topic-{t}>` | {topics[t]} | {fab_topics[t] or ''} |")
    body.append(f"| {{ref}}`Fab publications (Bloomington) <papers-fab-publications>` | {len(fabs)} | |")
    body += ["", "## All papers", "", "Sorted by first author's family name, then year.", ""]
    for r in sorted(rs, key=lambda r: r["label"]):
        body += entry(r)
    return page("papers-index", "Academic paper index", body)


def gen_topic(rs: list[dict]) -> str:
    body = [
        "Papers grouped by topic; a paper can appear under several topics. The",
        "fab publications are listed on {ref}`papers-fab-publications`, and each",
        "topic with fab publications says how many. Each line links the paper's",
        "full entry on {ref}`papers-index`.",
        "",
    ]
    rest = [r for r in rs if not fab(r)]
    empty = []
    for group, topics in TOPIC_GROUPS:
        sections = []
        for t in topics:
            items = [r for r in rest if t in r["topics"]]
            nfab = sum(1 for r in rs if fab(r) and t in r["topics"])
            if not items and not nfab:
                empty.append(TOPIC_NAMES[t])
                continue
            definition = check_papers.TOPICS[t]
            sections += [f"(papers-topic-{t})=", f"### {TOPIC_NAMES[t]}", "",
                         f"{esc(definition[0].upper() + definition[1:])}."]
            if t in TOPIC_PAGES:
                sections.append("Related pages: " + ", ".join(f"{{ref}}`{p}`" for p in TOPIC_PAGES[t]) + ".")
            sections.append("")
            sections += [line(r) for r in items] + ([""] if items else [])
            sections += fab_note(nfab)
        if sections:
            body += [f"## {group}", ""] + sections
    if empty:
        body += ["## Topics without papers", "", "No papers yet on: " + ", ".join(empty) + ".", ""]
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
    return page("papers-by-module", "Papers by related page", body)


def device_groups(r: dict) -> list[str]:
    t = set(r["topics"])
    out = []
    if "pdk-models" in t and "tooling" in t and not t & {"device-characterisation", "cryogenic"}:
        out.append("PDK and process overviews")
    elif t & {"pdk-models", "device-characterisation", "cryogenic"} and not t & MEMORY_DEVICES:
        out.append("Transistor models, characterisation and cryogenic operation")
    if "rram" in t:
        out.append("RRAM")
    if t & {"sonos", "floating-gate"}:
        out.append("SONOS and floating-gate nonvolatile memory")
    if "beol-integration" in t:
        out.append("BEOL-integrated devices")
    if t & {"test-structures", "reliability", "radiation"}:
        out.append("Test structures, reliability and radiation")
    if "analog-rf" in t:
        out.append("Analog and RF circuits")
    if "mixed-signal" in t:
        out.append("Data converters and mixed-signal circuits")
    if "power-management" in t:
        out.append("Power converters and regulators")
    if t & {"digital", "memory", "security"}:
        out.append("Digital logic, memory and security")
    if t & {"sensors", "quantum"}:
        out.append("Sensors and quantum interfaces")
    return out


DEVICE_ORDER = [
    "PDK and process overviews", "Transistor models, characterisation and cryogenic operation", "RRAM",
    "SONOS and floating-gate nonvolatile memory", "BEOL-integrated devices",
    "Test structures, reliability and radiation", "Analog and RF circuits",
    "Data converters and mixed-signal circuits", "Power converters and regulators",
    "Digital logic, memory and security", "Sensors and quantum interfaces",
]


def gen_device(rs: list[dict]) -> str:
    body = [
        "Papers grouped by the kind of device or circuit they study, derived from",
        "their topics; a paper can appear in several groups. Transistor models and",
        "cryogenic work on memory devices are listed under the memory device. The",
        "fab publications are listed on {ref}`papers-fab-publications`.",
        "",
    ]
    rest = [r for r in rs if not fab(r)]
    for heading in DEVICE_ORDER:
        items = [r for r in rest if heading in device_groups(r)]
        nfab = sum(1 for r in rs if fab(r) and heading in device_groups(r))
        if not items and not nfab:
            continue
        body += [f"## {heading}", ""] + [line(r) for r in items] + ([""] if items else []) + fab_note(nfab)
    others = [r for r in rest if not device_groups(r)]
    if others:
        body += ["## Other papers", ""] + [line(r) for r in others] + [""]
    return page("papers-by-device", "Papers by device or circuit type", body)


def gen_year(rs: list[dict]) -> str:
    body = ["Papers by year of publication, newest first.", ""]
    for y in sorted({r["year"] for r in rs}, reverse=True):
        body += [f"(papers-year-{y})=", f"## {y}", ""] + [line(r) for r in rs if r["year"] == y] + [""]
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


def fab_company(name: str) -> str | None:
    n = name.casefold()
    if "cypress" in n and "skywater" not in n:
        return "cypress"
    if "skywater" in n and "cypress" not in n:
        return "skywater"
    return None


def gen_institution(rs: list[dict]) -> str:
    body = [
        "Papers by the institutions named in their author affiliations. Cypress",
        "Semiconductor and SkyWater Technology come first; their Bloomington staff",
        "ran the fab. The other institutions are listed alphabetically in the",
        "table.",
        "",
    ]
    names = sorted({i for r in rs for i in r["institutions"]}, key=str.casefold)
    first = sorted([n for n in names if fab_company(n)], key=lambda n: (fab_company(n) != "cypress", n.casefold()))
    for n in first:
        body += [f"## {esc(n)}", ""] + [line(r) for r in rs if n in r["institutions"]] + [""]
    body += ["## Other institutions", "", "| Institution | Papers |", "|---|---|"]
    for n in names:
        if n in first:
            continue
        refs = ", ".join(f"{{ref}}`{r['label']}`" for r in rs if n in r["institutions"])
        body.append(f"| {esc(n)} | {refs} |")
    body.append("")
    return page("papers-by-institution", "Papers by institution", body)


def gen_fab(rs: list[dict]) -> str:
    items = [r for r in rs if fab(r)]
    body = [
        "Manufacturing, yield and process-control papers by staff of the fab in",
        "Bloomington, Minnesota, grouped by the company named in the authors'",
        "affiliations: Cypress Semiconductor (its Fab 4; see {ref}`the overview",
        "<overview-index>`) and, later, SkyWater Technology. None of them names",
        "the process it describes; each is included on the basis of those",
        "affiliations, which its full entry explains. The topic and device pages",
        "point here instead of listing them.",
        "",
    ]
    groups: dict[str, list[dict]] = {"cypress": [], "skywater": []}
    for r in items:
        companies = {fab_company(i) for i in r["institutions"]} - {None}
        if len(companies) != 1:
            raise SystemExit(f"{r['id']}: fab publication must name exactly one of Cypress or SkyWater")
        groups[companies.pop()].append(r)
    body += ["## Cypress Semiconductor", ""] + [line(r) for r in groups["cypress"]] + [""]
    body += ["## SkyWater Technology", ""] + [line(r) for r in groups["skywater"]] + [""]
    return page("papers-fab-publications", "Fab publications (Bloomington)", body)


def excluded_link(rid: str) -> str | None:
    if rid.startswith("doi:"):
        doi = rid[len("doi:"):]
        return link(doi, "https://doi.org/" + doi)
    if rid.startswith("arxiv:"):
        aid = rid[len("arxiv:"):]
        return link("arxiv:" + aid, "https://arxiv.org/abs/" + aid)
    return None


def gen_named_process(excluded: list[dict]) -> str:
    items = [r for r in excluded if r["names_process"]]
    body = [
        "These papers use the SKY130 PDK but report no fabricated silicon and no",
        "process-specific finding. They are listed for completeness and are",
        "deliberately not part of {ref}`the index proper <papers-scope>`: none of",
        "them meets its inclusion rules (Sec. 1 of the design). A record shown as",
        "**held** is awaiting a full-text check rather than settled as out of",
        "scope; see its reason.",
        "",
        f"{plural(len(items))} name the process out of {plural(len(excluded))} considered",
        "and excluded or held; the rest do not name SKY130 or the SkyWater 130 nm",
        "process at all. Generated from `data/papers-excluded.yaml` by",
        "`tools/gen_papers.py`; do not edit.",
        "",
    ]
    for y in sorted({r["year"] for r in items}, reverse=True):
        body += [f"## {y}", ""]
        for r in sorted(items, key=lambda r: r["title"].casefold()):
            if r["year"] != y:
                continue
            authors = join_names(r["authors"]) if r["authors"] else "authors not recorded"
            venue = esc(r["venue"]) if r["venue"] else "venue not recorded"
            lk = excluded_link(r["id"])
            head = f"**{esc(r['title'])}**. {authors}. {venue}, {r['year']}."
            if lk:
                head += " " + lk + "."
            if r["status"] == "held":
                head += " **Held.**"
            body.append(f"* {head} {esc(r['reason'])}")
        body.append("")
    return page("papers-designed-on-sky130", "Papers using the SKY130 PDK without fabrication results", body)


def generate() -> dict[str, str]:
    missing = set(check_papers.TOPICS) ^ set(TOPIC_NAMES)
    if missing:
        raise SystemExit(f"topic names out of step with check_papers.TOPICS: {sorted(missing)}")
    rs = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    if not isinstance(rs, list):
        raise SystemExit(f"{DATA}: top level must be a list")
    labels = check_papers.doc_labels()
    inv = set(check_papers.INV_KEY_RE.findall(check_papers.INVENTORY.read_text(encoding="utf-8")))
    today = dt.date.today()
    problems = [p for i, r in enumerate(rs) for p in check_papers.check_record(i, r, labels, inv, today)
                if "does not exist under docs/" not in p]
    label_map = yaml.safe_load(LABELS.read_text(encoding="utf-8"))
    excluded = yaml.safe_load(check_papers.EXCLUDED.read_text(encoding="utf-8")) or []
    problems += check_papers.check_labels(label_map, rs, excluded, today)
    for i, r in enumerate(excluded):
        problems += check_papers.check_excluded(i, r, today)
    if problems:
        print("\n".join(problems))
        raise SystemExit("data/papers.yaml fails tools/check_papers.py; fix it before generating pages")
    return {
        "index.md": gen_index(rs),
        "by-topic.md": gen_topic(rs),
        "by-module.md": gen_module(rs),
        "by-device.md": gen_device(rs),
        "by-year.md": gen_year(rs),
        "by-venue.md": gen_venue(rs),
        "by-institution.md": gen_institution(rs),
        "fab-publications.md": gen_fab(rs),
        "designed-on-sky130.md": gen_named_process(excluded),
    }


def git(*args: str) -> str | None:
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None


def label_map_changes() -> list[str]:
    """Label-map entries at the merge base with main and at HEAD must survive (previous_ids may grow)."""
    refs = []
    for ref in ("main", "origin/main"):
        out = git("merge-base", "HEAD", ref)
        if out:
            refs.append(out.strip())
            break
    head = git("rev-parse", "HEAD")
    if head and head.strip() not in refs:
        refs.append(head.strip())
    now = {e["label"]: e for e in yaml.safe_load(LABELS.read_text(encoding="utf-8")) or []}
    problems: list[str] = []
    for base in refs:
        old = git("show", f"{base}:data/papers-labels.yaml")
        if old is None:
            continue
        for e in yaml.safe_load(old) or []:
            cur = now.get(e["label"])
            if cur is None:
                msg = f"label {e['label']!r} (published at {base[:12]}) was removed from the label map"
            elif cur["id"] != e["id"] and e["id"] not in cur.get("previous_ids", []):
                msg = f"label {e['label']!r} now maps to {cur['id']!r}, not {e['id']!r}"
            elif cur["published"] != e["published"] or not set(e["previous_ids"]) <= set(cur["previous_ids"]):
                msg = f"label {e['label']!r}: published date or previous_ids changed"
            else:
                continue
            if msg not in problems:
                problems.append(msg)
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if committed pages differ from the generated ones")
    args = ap.parse_args()
    pages = generate()
    problems = label_map_changes()
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
    print(f"{plural(len(pages), 'page')} {verb}, {plural(len(problems), 'problem')}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
