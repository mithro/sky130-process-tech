#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Check the patent dataset ``data/patents.yaml``.

The schema is described in ``docs/plans/patent-index-design.md``.  The
checker verifies:

* **Schema.** Top-level ``schema_version`` (1), ``retrieved`` (a date)
  and ``families`` (a list).  Every family has the required keys with the
  right types; every member likewise.
* **Identifiers.** Family ids are unique; a publication number appears in
  one family only; the representative is one of the family's members; a
  member's ``country`` and ``kind`` agree with its number.
* **Dates.** Every date is an ISO 8601 date (``YYYY-MM-DD``); priority is
  not after filing, and filing not after grant.
* **Links.** Every member has an Espacenet and a Google Patents link of
  the expected shape for its own number; any other link is on an
  official or public patent database host.
* **Expiry.** ``expired`` is ``true``, ``false`` or ``unknown`` and agrees
  with the expiry date and the members' statuses as of today: a family
  marked ``false`` has an expiry date after today and a member shown as
  in force; a family marked ``true`` has no member shown as in force
  whose own expiry date is after today, and an expiry date after today
  only if every member is shown as lapsed, expired or abandoned (or is
  a published application shown as granted, whose term is that of the
  resulting patent).
* **Cross-references.** Every relevance ``target`` is a label defined in
  ``docs/`` as ``(label)=``; a ``cited-on-page`` target's page mentions a
  member's number; every inventory key exists in
  ``docs/references/public-sources.md`` and its entry mentions a
  member's number.
* **Wording.** Relevance reasons are one sentence and do not say that
  SkyWater uses a patent.

Run with ``uv run tools/check_patents.py [path]``; the exit status is non-zero
when a problem is found.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "patents.yaml"
DOCS = ROOT / "docs"
INVENTORY = DOCS / "references" / "public-sources.md"

TODAY = dt.date.today()
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PN_RE = re.compile(r"^([A-Z]{2})([A-Z0-9]*?\d)([A-Z]{1,2}\d?)?$")
ID_RE = re.compile(r"^GP\d+$")
VERIFIED_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \S.*$")
LABEL_RE = re.compile(r"^\(([A-Za-z0-9_-]+)\)=", re.M)
KEY_RE = re.compile(r"^\*\*([A-Z0-9][A-Z0-9_-]*)\*\*", re.M)

DOC_TYPES = {
    "granted-patent", "application", "international-application",
    "search-report", "utility-model", "translation-of-granted-patent",
    "reexamination-certificate", "design", "other",
}
RELATIONS = {"cited-on-page", "same-lineage-assignee", "technique-class"}
DISCOVERY = {"cited-in-docs", "assignee-search", "family-resolution",
             "cited-by-seed", "citing-seed"}
ENDED = {"Expired - Lifetime", "Expired - Fee Related", "Abandoned",
         "Ceased", "Withdrawn", "Revoked", "Expired"}
IN_FORCE = {"Active"}
APPLICATION_TYPES = {"application", "international-application", "search-report"}
LINK_HOSTS = (
    "https://worldwide.espacenet.com/", "https://patents.google.com/",
    "https://patentscope.wipo.int/", "https://ppubs.uspto.gov/",
    "https://image-ppubs.uspto.gov/", "https://register.epo.org/",
    "https://www.j-platpat.inpit.go.jp/", "https://pss-system.cponline.cnipa.gov.cn/",
    "https://www.kipris.or.kr/", "https://twpat.tipo.gov.tw/",
    "https://register.dpma.de/", "https://depatisnet.dpma.de/",
    "https://www.ipo.gov.uk/", "https://data.inpi.fr/",
)
USES_RE = re.compile(r"SkyWater (uses|used|practises|practices|licens)|used (at|by) SkyWater", re.I)

FAMILY_KEYS = {
    "id": str, "family": dict, "representative": str, "title": str,
    "assignees": dict, "inventors": list, "dates": dict,
    "legal_status": dict, "expiry": dict, "expired": (bool, str),
    "members": list, "relevance": list, "inventory_keys": list,
    "discovery": list, "verified": str,
}
OPTIONAL_FAMILY_KEYS = {"notes": list, "discovery_note": str}
MEMBER_KEYS = {
    "number": str, "country": str, "kind": (str, type(None)),
    "document_type": str, "publication_date": (str, type(None)),
    "status": (str, type(None)), "links": dict, "verified": str,
}
OPTIONAL_MEMBER_KEYS = {
    "title": (str, type(None)), "application_number": (str, type(None)),
    "filing_date": (str, type(None)), "expiry": dict, "note": str,
}


class Loader(yaml.SafeLoader):
    """Safe loader that leaves dates as strings, so malformed ones can be reported."""


Loader.yaml_implicit_resolvers = {
    ch: [(tag, rx) for tag, rx in rs if tag != "tag:yaml.org,2002:timestamp"]
    for ch, rs in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def to_date(v) -> dt.date | None:
    """Return the date an ISO 8601 ``YYYY-MM-DD`` string denotes, else None."""
    if isinstance(v, str) and DATE_RE.match(v):
        try:
            return dt.date.fromisoformat(v)
        except ValueError:
            return None
    return None


def is_date(v) -> bool:
    return to_date(v) is not None


def add_years(d: dt.date, n: int) -> dt.date:
    try:
        return d.replace(year=d.year + n)
    except ValueError:
        return d.replace(year=d.year + n, day=28)


def earliest_family_filing(members: list) -> dt.date | None:
    """The earliest recorded ``filing_date`` among a family's members: the
    filing date a divisional or continuation's own term is measured from
    (Japanese Patent Act Art. 44(2)/67(1); the same principle bounds a US
    continuation, whose term likewise runs from the earliest non-provisional
    US filing in its own chain, 35 U.S.C. 154(a)(2)). Using the family's
    earliest member filing date, rather than the member's own, is a
    conservative generalisation of this: it never gives a *later* bound than
    the member's own filing date would."""
    dates = [to_date(m.get("filing_date")) for m in members if isinstance(m, dict)]
    dates = [d for d in dates if d]
    return min(dates) if dates else None


def member_end_bound(m: dict, fam: dict) -> dt.date | None:
    """The latest date by which a member's own term (if it has one) must have
    ended, per ``docs/plans/patent-index-design.md``'s "Status and expiry
    rules", using only what is recorded for the member and the family — not
    a live lookup. Returns ``None`` when the member has no term of its own
    (a reexamination certificate, or a published application shown as
    granted, whose term belongs to the granted patent, itself a member of
    the family) or when the member's own status already shows it ended, in
    which case it needs no forward bound. Otherwise returns the estimated
    upper bound so the caller can compare it with today."""
    t = m.get("document_type")
    status = m.get("status")
    if t in ("reexamination-certificate", "translation-of-granted-patent"):
        return None  # no term of its own; the term is that of the patent it amends or translates
    if t in APPLICATION_TYPES and status == "Granted":
        return None
    if status in ENDED:
        return None
    exp = m.get("expiry")
    if isinstance(exp, dict):
        d = to_date(exp.get("date"))
        if d:
            return d
    priority = to_date((fam.get("dates") or {}).get("priority"))
    candidates: list[dt.date] = []
    if t in APPLICATION_TYPES:
        # rule 2: a pending application (or one with no status recorded) is
        # bounded by 20 years from the earliest non-provisional filing date
        # in its own family — not necessarily its own filing date.
        basis_filing = earliest_family_filing(fam.get("members") or []) or to_date(m.get("filing_date"))
        if basis_filing:
            candidates.append(add_years(basis_filing, 20))
    else:
        # L3: a fetched grant with a known filing date but no recorded
        # expiry event is also bounded by 20 years from *its own* filing
        # date (the ordinary term formula) — tighter, and sometimes later
        # than the priority-based fallback below (for a national-phase
        # filing made well over a year after priority), than treating it
        # as if only the family's priority date were known.
        own_filing = to_date(m.get("filing_date"))
        if own_filing:
            candidates.append(add_years(own_filing, 20))
    if priority:
        # rule 3: a listed-only member, or a fetched member with no
        # recorded expiry event and a status that is neither `Active` nor
        # ended (including no legal-status data at all), is bounded by the
        # family's earliest priority date + 21 years.
        candidates.append(add_years(priority, 21))
        if (m.get("country") == "US" and t == "granted-patent" and priority < dt.date(1995, 6, 8)):
            pub = to_date(m.get("publication_date"))
            if pub:
                candidates.append(add_years(pub, 17))
    return max(candidates) if candidates else None


def family_max_estimate(fam: dict) -> tuple[dt.date, str] | None:
    """The latest term any member of the family could run to, taken over
    *every* member regardless of its own status (M3): a member's own
    recorded ``expiry.date`` counts even when its status shows a fee lapse
    or similar, because a lapsed US patent can be reinstated (M4) and the
    family's headline date should not understate the longest possible term.
    A member with no recorded expiry event contributes ``member_end_bound``
    only while it is not already shown ended (an already-ended member with
    no recorded date contributes nothing — there is no date to use). Returns
    ``(date, publication_number)`` of the governing member, or ``None`` if no
    member contributes a date at all."""
    best: tuple[dt.date, str] | None = None
    for m in fam.get("members") or []:
        if not isinstance(m, dict):
            continue
        exp = m.get("expiry")
        d = to_date(exp.get("date")) if isinstance(exp, dict) else None
        if d is None and m.get("status") not in ENDED:
            d = member_end_bound(m, fam)
        if d is not None and (best is None or d > best[0]):
            best = (d, m.get("number"))
    return best


def number_forms(pn: str) -> list[str]:
    """Forms in which a publication number may be written in the docs."""
    m = PN_RE.match(pn)
    if not m:
        return [pn]
    cc, num, _kind = m.groups()
    forms = [pn, f"{cc}{num}"]
    if cc == "US" and num.isdigit():
        if len(num) == 11:
            forms.append(f"{num[:4]}/{num[4:]}")
        else:
            forms.append(f"{int(num):,}")
    if cc == "EP" and num.isdigit() and len(num) == 7:
        forms.append(f"{num[0]} {num[1:4]} {num[4:]}")
    return forms


def mentions(text: str, pns: list[str]) -> bool:
    for pn in pns:
        for f in number_forms(pn):
            if re.search(r"(?<![\d,/])" + re.escape(f) + r"(?![\d,])", text):
                return True
    return False


def doc_labels() -> dict[str, Path]:
    labels: dict[str, Path] = {}
    for path in DOCS.rglob("*.md"):
        rel = path.relative_to(DOCS).as_posix()
        if rel.startswith("plans/") or rel.startswith("_build/"):
            continue
        for lab in LABEL_RE.findall(path.read_text()):
            labels.setdefault(lab, path)
    return labels


def inventory_entries() -> dict[str, str]:
    text = INVENTORY.read_text()
    entries: dict[str, str] = {}
    for para in re.split(r"\n\s*\n", text):
        m = KEY_RE.match(para)
        if m:
            entries[m.group(1)] = para
    return entries


def check_types(obj: dict, required: dict, optional: dict, where: str, problems: list[str]) -> None:
    for key, typ in required.items():
        if key not in obj:
            problems.append(f"{where}: missing key '{key}'")
        elif not isinstance(obj[key], typ):
            problems.append(f"{where}: '{key}' has type {type(obj[key]).__name__}")
    for key in obj:
        if key not in required and key not in optional:
            problems.append(f"{where}: unexpected key '{key}'")
    for key, typ in optional.items():
        if key in obj and not isinstance(obj[key], typ):
            problems.append(f"{where}: '{key}' has type {type(obj[key]).__name__}")


def check_date_field(value, where: str, problems: list[str], nullable: bool = True) -> None:
    if value is None:
        if not nullable:
            problems.append(f"{where}: date missing")
        return
    if not is_date(value):
        problems.append(f"{where}: {value!r} is not an ISO 8601 date")


def check_member(m: dict, fam_id: str, problems: list[str]) -> None:
    where = f"{fam_id} member {m.get('number', '?')}"
    check_types(m, MEMBER_KEYS, OPTIONAL_MEMBER_KEYS, where, problems)
    pn = m.get("number", "")
    mm = PN_RE.match(pn) if isinstance(pn, str) else None
    if not mm:
        problems.append(f"{where}: malformed publication number")
        return
    cc, _num, kind = mm.groups()
    if m.get("country") != cc:
        problems.append(f"{where}: country {m.get('country')} does not match number")
    if (m.get("kind") or None) != (kind or None):
        problems.append(f"{where}: kind {m.get('kind')} does not match number")
    if m.get("document_type") not in DOC_TYPES:
        problems.append(f"{where}: unknown document_type {m.get('document_type')!r}")
    check_date_field(m.get("publication_date"), f"{where} publication_date", problems)
    check_date_field(m.get("filing_date"), f"{where} filing_date", problems)
    links = m.get("links") or {}
    esp = f"https://worldwide.espacenet.com/patent/search?q=pn%3D{pn}"
    gp = f"https://patents.google.com/patent/{pn}/en"
    if links.get("espacenet") != esp:
        problems.append(f"{where}: Espacenet link should be {esp}")
    if links.get("google_patents") != gp:
        problems.append(f"{where}: Google Patents link should be {gp}")
    for name, url in links.items():
        if name in ("espacenet", "google_patents"):
            continue
        if not isinstance(url, str) or not url.startswith(LINK_HOSTS):
            problems.append(f"{where}: link '{name}' is not on a public patent database host")
    if not VERIFIED_RE.match(str(m.get("verified", ""))):
        problems.append(f"{where}: 'verified' must start with an ISO date and name the source")
    if "expiry" in m:
        e = m["expiry"]
        if not isinstance(e, dict) or set(e) != {"date", "estimated", "basis"}:
            problems.append(f"{where}: expiry must have date, estimated, basis")
        else:
            check_date_field(e["date"], f"{where} expiry date", problems)
            if e["estimated"] is not True:
                problems.append(f"{where}: expiry must be marked estimated: true")


def check_family(f: dict, labels: dict[str, Path], inventory: dict[str, str],
                 page_text: dict[Path, str], problems: list[str]) -> None:
    fid = f.get("id", "?")
    check_types(f, FAMILY_KEYS, OPTIONAL_FAMILY_KEYS, fid, problems)
    if not ID_RE.match(str(fid)):
        problems.append(f"{fid}: id must be 'GP' followed by the Google Patents family ID")
    fam = f.get("family") or {}
    if fam.get("source") != "Google Patents family ID" or f"GP{fam.get('google_family_id')}" != fid:
        problems.append(f"{fid}: family source/google_family_id do not match the id")
    if not str(f.get("title", "")).strip():
        problems.append(f"{fid}: empty title")
    ass = f.get("assignees") or {}
    if not isinstance(ass.get("original"), list) or not ass.get("original"):
        problems.append(f"{fid}: assignees.original must be a non-empty list")
    if not isinstance(ass.get("current"), list):
        problems.append(f"{fid}: assignees.current must be a list")
    dates = f.get("dates") or {}
    if set(dates) != {"priority", "filing", "grant"}:
        problems.append(f"{fid}: dates must have priority, filing, grant")
    check_date_field(dates.get("priority"), f"{fid} priority", problems, nullable=False)
    check_date_field(dates.get("filing"), f"{fid} filing", problems)
    check_date_field(dates.get("grant"), f"{fid} grant", problems)
    seq = [to_date(dates.get(k)) for k in ("priority", "filing", "grant")]
    seq = [d for d in seq if d]
    if seq != sorted(seq):
        problems.append(f"{fid}: dates out of order (priority <= filing <= grant)")
    ls = f.get("legal_status") or {}
    if set(ls) != {"status", "source"} or not ls.get("source"):
        problems.append(f"{fid}: legal_status must have status and source")

    members = f.get("members") or []
    numbers = []
    for m in members:
        if isinstance(m, dict):
            check_member(m, fid, problems)
            numbers.append(m.get("number"))
    if len(numbers) != len(set(numbers)):
        problems.append(f"{fid}: duplicate member numbers")
    if f.get("representative") not in numbers:
        problems.append(f"{fid}: representative is not a member")

    # expiry and expired
    exp = f.get("expiry") or {}
    if set(exp) != {"date", "estimated", "basis"}:
        problems.append(f"{fid}: expiry must have date, estimated, basis")
    check_date_field(exp.get("date"), f"{fid} expiry date", problems)
    if exp.get("estimated") is not True:
        problems.append(f"{fid}: expiry must be marked estimated: true")
    if not str(exp.get("basis", "")).strip():
        problems.append(f"{fid}: expiry basis missing")
    expired = f.get("expired")
    edate = to_date(exp.get("date"))
    live = [m for m in members if isinstance(m, dict) and m.get("status") in IN_FORCE]
    live_future = [m for m in live
                   if not (isinstance(m.get("expiry"), dict) and to_date(m["expiry"].get("date"))
                           and to_date(m["expiry"]["date"]) <= TODAY)]
    if expired is True:
        if live_future:
            problems.append(f"{fid}: expired: true but {live_future[0]['number']} is shown as in force")
        if edate and edate > TODAY and not all(
                m.get("status") in ENDED
                or m.get("document_type") == "reexamination-certificate"
                or (m.get("document_type") in APPLICATION_TYPES and m.get("status") == "Granted")
                for m in members if isinstance(m, dict)):
            problems.append(f"{fid}: expired: true but expiry date {edate} is after today")
        # H2: bound every member individually, not just the family's own
        # expiry.date — this catches a listed-only member, a fetched member
        # with no recorded legal status, or a still-pending application
        # whose own bound was never computed.
        for m in members:
            if not isinstance(m, dict):
                continue
            eb = member_end_bound(m, f)
            if eb is not None and eb > TODAY:
                problems.append(
                    f"{fid}: expired: true but member {m.get('number')} is not bounded ended until "
                    f"{eb.isoformat()} (design's per-member expiry rule)")
    elif expired is False:
        if not edate or edate <= TODAY:
            problems.append(f"{fid}: expired: false but expiry date {edate} is not after today")
        if not live_future:
            problems.append(f"{fid}: expired: false but no member is shown as in force")
    elif expired != "unknown":
        problems.append(f"{fid}: expired must be true, false or unknown")

    # M3/L5: expiry.date must be the latest estimate over *every* member,
    # not just the members shown as in force, and must name a real member.
    best = family_max_estimate(f)
    if edate and best and edate != best[0]:
        problems.append(
            f"{fid}: expiry date {edate} is not the latest member estimate "
            f"({best[0].isoformat()}, held by {best[1]})")
    if edate and numbers and not mentions(str(exp.get("basis", "")), [n for n in numbers if n]):
        problems.append(f"{fid}: expiry basis does not name any member of the family")

    # L6: legal_status.status must be the representative member's own status.
    rep_m = next((m for m in members if isinstance(m, dict) and m.get("number") == f.get("representative")), None)
    if rep_m is not None and ls.get("status") != rep_m.get("status"):
        problems.append(
            f"{fid}: legal_status.status ({ls.get('status')!r}) does not match the representative "
            f"member's own status ({rep_m.get('status')!r})")

    # relevance
    if not f.get("relevance"):
        problems.append(f"{fid}: no relevance entries")
    for r in f.get("relevance") or []:
        if not isinstance(r, dict) or set(r) != {"target", "relation", "reason"}:
            problems.append(f"{fid}: relevance entries need target, relation, reason")
            continue
        if r["relation"] not in RELATIONS:
            problems.append(f"{fid}: unknown relation {r['relation']!r}")
        if r["target"] not in labels:
            problems.append(f"{fid}: relevance target '{r['target']}' is not a docs label")
        elif r["relation"] == "cited-on-page":
            path = labels[r["target"]]
            if not mentions(page_text.setdefault(path, path.read_text()), numbers):
                problems.append(f"{fid}: page for '{r['target']}' does not mention a member number")
        reason = str(r["reason"]).strip()
        if not reason.endswith("."):
            problems.append(f"{fid}: reason for '{r['target']}' must be a sentence ending in '.'")
        if USES_RE.search(reason):
            problems.append(f"{fid}: reason for '{r['target']}' says SkyWater uses the patent")
    for key in f.get("inventory_keys") or []:
        if key not in inventory:
            problems.append(f"{fid}: inventory key {key} not in public-sources.md")
        elif not mentions(inventory[key], numbers):
            problems.append(f"{fid}: inventory entry {key} does not mention a member number")
    if any(d not in DISCOVERY for d in f.get("discovery") or []) or not f.get("discovery"):
        problems.append(f"{fid}: discovery must be a non-empty list of {sorted(DISCOVERY)}")
    if "cited-in-docs" in (f.get("discovery") or []) and not f.get("inventory_keys"):
        problems.append(f"{fid}: cited-in-docs family without an inventory key")
    if not VERIFIED_RE.match(str(f.get("verified", ""))):
        problems.append(f"{fid}: 'verified' must start with an ISO date and name the source")


def main() -> int:
    problems: list[str] = []
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DATA
    try:
        data = yaml.load(path.read_text(), Loader=Loader)
    except yaml.YAMLError as exc:
        print(f"{path}: YAML error: {exc}")
        print("0 patent families checked, 1 problems")
        return 1
    if not isinstance(data, dict):
        print("data/patents.yaml: not a mapping")
        return 1
    if data.get("schema_version") != 1:
        problems.append("schema_version must be 1")
    if not is_date(data.get("retrieved")):
        problems.append("retrieved must be an ISO date")
    families = data.get("families")
    if not isinstance(families, list):
        print("data/patents.yaml: families must be a list")
        return 1
    labels = doc_labels()
    inventory = inventory_entries()
    page_text: dict[Path, str] = {}
    seen_ids: set[str] = set()
    seen_numbers: dict[str, str] = {}
    for f in families:
        if not isinstance(f, dict):
            problems.append("family entry is not a mapping")
            continue
        fid = str(f.get("id"))
        if fid in seen_ids:
            problems.append(f"{fid}: duplicate family id")
        seen_ids.add(fid)
        for m in f.get("members") or []:
            pn = m.get("number") if isinstance(m, dict) else None
            if pn in seen_numbers and seen_numbers[pn] != fid:
                problems.append(f"{fid}: {pn} also listed in {seen_numbers[pn]}")
            seen_numbers.setdefault(pn, fid)
        check_family(f, labels, inventory, page_text, problems)
    for p in problems:
        print(p)
    print(f"{len(families)} patent families checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
