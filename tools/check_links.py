#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Check every URL and DOI cited in the documentation still resolves.

Sources scanned:

* every entry in ``docs/references/public-sources.md`` (blocks starting
  ``**KEY**`` at the start of a line, up to the next such block);
* the footnote *definitions* (``[^label]: ...`` blocks, house style per
  ``docs/plans/citation-style.md``) of every page under ``docs/``.

Generated index pages (``docs/references/papers/``,
``docs/references/patents/``, ``docs/references/filings/``) cite sources
as inline links in tables, not footnotes (the documented exception in
``docs/plans/citation-style.md``), so they are not scanned here — the
same scope ``tools/check_refs.py`` uses.

URLs and DOIs are deduplicated across both sources; a ``https://doi.org/
<doi>`` URL and a bare ``DOI 10.xxxx/yyyy`` mention collapse to the same
DOI token.  For each token this tool remembers which inventory key(s)
(``**KEY**`` entries) and which ``(page, footnote label)`` pairs cite it,
so the report can say who to fix.

Checking is polite:

* a per-host rate limit, default one request every 3 s per host
  (``--rate-limit``), 20 s for ``patents.google.com``
  (``--slow-host``, repeatable ``host=seconds``);
* at most 4 hosts are ever contacted concurrently (``--workers``);
* HEAD first, GET fallback (some servers reject/misreport HEAD);
* redirects are followed (by a custom handler that also paces the new
  host before following) and the whole chain is recorded;
* timeouts and 429/502/503/504 responses are retried with backoff;
* results are cached in a JSON file under the repo's gitignored ``tmp/``
  (``--cache``), written after every check, so a killed or interrupted
  run resumes; entries younger than ``--max-age-days`` (default 30) are
  not rechecked.

Classification, per token:

* **ok** — 2xx (following only temporary 302/303/307 redirects, if
  any), or a DOI that redirects to a publisher and gets 403 there
  ("resolves, access-controlled" — not dead);
* **redirected-permanently** — the chain includes a 301/308 hop and the
  request still succeeds; the report calls out the final URL so the
  citation can be updated;
* **blocked-to-scripts** — the original URL or any hop lands on a host
  in ``BLOCKED_HOSTS`` (sec.gov, linkedin.com, indeed.com and other
  hosts observed refusing scripted clients; extend the set as more are
  found);
* **dead** — anything else: 404/410/5xx after retries, connection
  failures, or an unresolvable 403/401 on a host not known to block
  scripts. Every dead token is looked up on the Wayback availability
  API (``archive.org/wayback/available``) and the closest snapshot (if
  any) is recorded.

Output is a Markdown report: summary counts, then one table per
problem category (dead / redirected-permanently / blocked-to-scripts),
each row naming the token, the inventory key(s)/pages that cite it, the
HTTP result and (for dead links) the Wayback snapshot. Exit status is
always 0 unless ``--strict`` is given, in which case it is non-zero
when any token is classified dead.

``--selftest`` runs the (offline) extraction-logic unit tests and exits;
no network access, no cache file is touched.

Run with ``uv run tools/check_links.py [options]``.  Useful options for
chunked, resumable runs: ``--only-host HOST`` / ``--skip-host HOST``
(repeatable), ``--list-hosts`` (print per-host pending counts and exit),
``--time-budget SECONDS`` (stop dispatching new checks after this long;
already-cached results are still reported), ``--force`` (ignore
``--max-age-days`` and recheck everything).
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INVENTORY = DOCS / "references" / "public-sources.md"
DEFAULT_CACHE = ROOT / "tmp" / "link-check-cache.json"
USER_AGENT = "sky130-process-tech docs checker"

KEY_RE = re.compile(r"^\*\*([A-Za-z0-9][A-Za-z0-9_-]*)\*\*", re.MULTILINE)
FOOTNOTE_DEF_RE = re.compile(
    r"^\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\]:(.*?)(?=^\[\^[A-Za-z0-9][A-Za-z0-9_-]*\]:|\Z)",
    re.MULTILINE | re.DOTALL,
)
BRACKETED_URL_RE = re.compile(r"<(https?://[^<>\s]+)>")
URL_RE = re.compile(r"https?://[^\s<>\)\]\"'`]+")
# Like BRACKETED_URL_RE, allow a DOI's own parentheses (pre-2000 Elsevier
# suffixes such as "0927-796X(98)00013-8"); only whitespace and the
# punctuation that could plausibly close an *enclosing* markdown
# construct end the match, and a trailing sentence '.' etc. is trimmed
# by rstrip(TRAILING_PUNCT) afterwards.
DOI_BARE_RE = re.compile(r"\bDOI:?\s+(10\.\d{4,9}/[^\s,;\]}>\"']+)", re.IGNORECASE)
TRAILING_PUNCT = ".,;:"

# Hosts known (from experience checking this documentation) to refuse
# scripted clients outright -- classified "blocked to scripts" rather
# than dead.  Extend this set as new ones are found; note why.
BLOCKED_HOSTS = {
    "sec.gov",  # EDGAR demands a contact in the User-Agent (Common rule 10); never fetched directly
    "linkedin.com",  # returns HTTP 999 to non-browser clients
    "indeed.com",  # Cloudflare/bot challenge for non-browser clients
    "glassdoor.com",  # Cloudflare/bot challenge for non-browser clients
    "researchgate.net",  # blocks non-browser clients with 403
    "astm.org",  # 403 to this UA, 307 to a browser UA (verified 2026-09-19); Akamai bot check
    "cdc.gov",  # 403 to curl regardless of User-Agent string (verified 2026-09-19); Wayback shows the pages live
    "appliedmaterials.com",  # 403 to curl regardless of User-Agent string (verified 2026-09-19); Wayback shows the page live
    "forbes.com",  # 403 to curl regardless of User-Agent string (verified 2026-09-19); Wayback shows the page live
    "businesswire.com",  # 403/connection-drop to every automated client tried, including Anthropic's own fetch infra (verified 2026-09-19); Wayback shows the page live
    "startribune.com",  # persistent 429 to curl regardless of User-Agent string (verified 2026-09-19); Wayback shows the pages live and recent
}

# Per-host request pacing, in seconds.  Anything not listed uses
# --rate-limit (default 3.0).
SLOW_HOSTS = {
    "patents.google.com": 20.0,
}

# Hosts where a HEAD request gets a different (and misleading) answer than
# a GET: verified 2026-09-19 that a HEAD to a resolved openlibrary.org book
# page 303s to /verify_human (a bot challenge) while a GET to the very same
# URL, same User-Agent, correctly 301s to the human-readable slug. Skip
# HEAD entirely for these and go straight to GET.
HEAD_UNRELIABLE_HOSTS = {
    "openlibrary.org",
}

# A redirect landing on one of these paths is a bot challenge, not a real
# new home for the content, no matter what HTTP status carried it there
# (openlibrary.org's is a 200 on the challenge page itself). Extend as more
# are found.
CHALLENGE_PATH_MARKERS = (
    "/verify_human",  # openlibrary.org / archive.org
)


def host_of(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.lower()


def host_matches(host: str, base: str) -> bool:
    return host == base or host.endswith("." + base)


def is_blocked_host(host: str) -> bool:
    return any(host_matches(host, b) for b in BLOCKED_HOSTS)


# --------------------------------------------------------------------------
# Extraction
# --------------------------------------------------------------------------


def _classify_url(u: str, urls: set[str], dois: set[str]) -> None:
    host = host_of(u)
    if host in ("doi.org", "dx.doi.org"):
        doi = urllib.parse.unquote(u.split("doi.org/", 1)[-1]).rstrip(TRAILING_PUNCT)
        if doi:
            dois.add(doi.lower())
    else:
        urls.add(u)


def extract_urls_and_dois(text: str) -> tuple[set[str], set[str]]:
    """Return (urls, dois) found in a block of text.

    House style (``docs/plans/citation-style.md``) always wraps a
    citation URL in angle brackets (``<https://...>``); that delimiter
    is unambiguous, so it is tried first and takes the *whole* interior,
    parentheses and all -- many pre-2000 Elsevier DOIs
    (``10.1016/0022-0248(82)90456-2``) and Wikipedia article titles
    (``Wafer_(electronics)``) contain literal parentheses that a
    punctuation-trimming bare-URL regex would truncate. Any text not
    inside angle brackets still falls back to the punctuation-trimming
    regex, in case a page ever strays from house style.

    A ``https://doi.org/<doi>`` (or ``dx.doi.org``) URL contributes only
    a DOI, not a URL, so it merges with a bare ``DOI 10.xxxx/yyyy``
    mention of the same identifier.
    """
    urls: set[str] = set()
    dois: set[str] = set()
    spans: list[tuple[int, int]] = []
    for m in BRACKETED_URL_RE.finditer(text):
        spans.append((m.start(), m.end()))
        _classify_url(m.group(1), urls, dois)
    if spans:
        chars = list(text)
        for s, e in spans:
            for i in range(s, e):
                chars[i] = " "
        remainder = "".join(chars)
    else:
        remainder = text
    for u in URL_RE.findall(remainder):
        _classify_url(u.rstrip(TRAILING_PUNCT), urls, dois)
    for m in DOI_BARE_RE.finditer(text):
        dois.add(m.group(1).rstrip(TRAILING_PUNCT).lower())
    return urls, dois


def parse_inventory(text: str) -> dict[str, tuple[set[str], set[str]]]:
    """Return ``{KEY: (urls, dois)}`` for every ``**KEY**`` entry."""
    entries: dict[str, tuple[set[str], set[str]]] = {}
    matches = list(KEY_RE.finditer(text))
    for i, m in enumerate(matches):
        key = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        urls, dois = extract_urls_and_dois(text[start:end])
        eurls, edois = entries.setdefault(key, (set(), set()))
        eurls.update(urls)
        edois.update(dois)
    return entries


def parse_page_footnotes(text: str) -> dict[str, tuple[set[str], set[str]]]:
    """Return ``{label: (urls, dois)}`` for every footnote definition."""
    result: dict[str, tuple[set[str], set[str]]] = {}
    for m in FOOTNOTE_DEF_RE.finditer(text):
        label = m.group(1)
        urls, dois = extract_urls_and_dois(m.group(2))
        rurls, rdois = result.setdefault(label, (set(), set()))
        rurls.update(urls)
        rdois.update(dois)
    return result


def token_for(url: str | None = None, doi: str | None = None) -> str:
    if doi is not None:
        return f"doi:{doi.lower()}"
    assert url is not None
    return url


class Registry:
    """token -> citers (inventory keys, and (page, label) pairs)."""

    def __init__(self) -> None:
        self.inventory_keys: dict[str, set[str]] = defaultdict(set)
        self.pages: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))

    def add_inventory(self, key: str, urls: set[str], dois: set[str]) -> None:
        for u in urls:
            self.inventory_keys[u].add(key)
        for d in dois:
            self.inventory_keys[token_for(doi=d)].add(key)

    def add_page(self, page: str, label: str, urls: set[str], dois: set[str]) -> None:
        for u in urls:
            self.pages[u][page].add(label)
        for d in dois:
            self.pages[token_for(doi=d)][page].add(label)

    def tokens(self) -> set[str]:
        return set(self.inventory_keys) | set(self.pages)


def build_registry(docs_dir: Path = DOCS, inventory: Path = INVENTORY) -> Registry:
    reg = Registry()
    if inventory.exists():
        for key, (urls, dois) in parse_inventory(inventory.read_text(encoding="utf-8")).items():
            reg.add_inventory(key, urls, dois)
    for path in sorted(docs_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for label, (urls, dois) in parse_page_footnotes(text).items():
            reg.add_page(str(path.relative_to(ROOT)), label, urls, dois)
    return reg


# --------------------------------------------------------------------------
# Polite fetching
# --------------------------------------------------------------------------


class RateLimiter:
    def __init__(self, default_delay: float, slow_hosts: dict[str, float]) -> None:
        self.default_delay = default_delay
        self.slow_hosts = slow_hosts
        self._last: dict[str, float] = {}
        self._locks: dict[str, threading.Lock] = defaultdict(threading.Lock)
        self._map_lock = threading.Lock()

    def _lock_for(self, host: str) -> threading.Lock:
        with self._map_lock:
            return self._locks[host]

    def delay_for(self, host: str) -> float:
        for h, d in self.slow_hosts.items():
            if host_matches(host, h):
                return d
        return self.default_delay

    def wait(self, host: str) -> None:
        delay = self.delay_for(host)
        lock = self._lock_for(host)
        with lock:
            now = time.monotonic()
            last = self._last.get(host, 0.0)
            remaining = delay - (now - last)
            if remaining > 0:
                time.sleep(remaining)
            self._last[host] = time.monotonic()


class ChainRecorder(urllib.request.HTTPRedirectHandler):
    def __init__(self, limiter: RateLimiter) -> None:
        super().__init__()
        self.limiter = limiter
        self.chain: list[tuple[int, str]] = []

    def redirect_request(self, req, fp, code, msg, hdrs, newurl):  # noqa: N802,ANN001,ANN201
        self.chain.append((code, newurl))
        self.limiter.wait(host_of(newurl))
        return super().redirect_request(req, fp, code, msg, hdrs, newurl)


def _fetch(
    url: str, method: str, limiter: RateLimiter, timeout: float, read_body: bool = False
) -> tuple[int, str, list[tuple[int, str]], str | None, bytes]:
    limiter.wait(host_of(url))
    rec = ChainRecorder(limiter)
    opener = urllib.request.build_opener(rec)
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with opener.open(req, timeout=timeout) as resp:
            body = resp.read(200_000) if read_body else b""
            return resp.status, resp.geturl(), rec.chain, None, body
    except urllib.error.HTTPError as e:
        body = b""
        if read_body:
            try:
                body = e.read(200_000)
            except Exception:  # noqa: BLE001
                body = b""
        return e.code, e.geturl() or url, rec.chain, None, body
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        return 0, url, rec.chain, str(e), b""


def fetch_with_retries(
    url: str,
    method: str,
    limiter: RateLimiter,
    timeout: float,
    retries: int = 3,
    read_body: bool = False,
) -> tuple[int, str, list[tuple[int, str]], str | None, bytes]:
    status = 0
    final_url = url
    chain: list[tuple[int, str]] = []
    err: str | None = None
    body = b""
    for attempt in range(retries + 1):
        status, final_url, chain, err, body = _fetch(url, method, limiter, timeout, read_body)
        if status == 429 and attempt < retries:
            time.sleep(15 * (attempt + 1))
            continue
        if status in (0, 502, 503, 504) and attempt < retries:
            time.sleep(5 * (attempt + 1))
            continue
        return status, final_url, chain, err, body
    return status, final_url, chain, err, body


def hosts_in_chain(url: str, chain: list[tuple[int, str]], final_url: str) -> set[str]:
    hosts = {host_of(url), host_of(final_url)}
    hosts.update(host_of(u) for _, u in chain)
    return hosts


def is_challenge_url(u: str) -> bool:
    return any(marker in u for marker in CHALLENGE_PATH_MARKERS)


def classify(
    url: str,
    is_doi: bool,
    status: int,
    final_url: str,
    chain: list[tuple[int, str]],
    err: str | None,
) -> str:
    hosts = hosts_in_chain(url, chain, final_url)
    blocked = any(is_blocked_host(h) for h in hosts)

    if status == 0:
        return "blocked-to-scripts" if blocked else "dead"
    # A 200 that landed on a bot-challenge page (e.g. openlibrary.org's HEAD
    # *and* GET occasionally 303ing a perfectly good book URL to
    # /verify_human -- verified 2026-09-19, apparently IP-request-volume
    # triggered rather than UA-based) is not a real "it moved here"
    # redirect: the numeric status lies, so check the actual URLs in the
    # chain regardless of status.
    if is_challenge_url(final_url) or any(is_challenge_url(u) for _, u in chain):
        return "blocked-to-scripts"
    if blocked and status in (403, 401, 429, 999):
        return "blocked-to-scripts"
    if is_doi:
        # The doi.org -> publisher hop is the DOI resolver doing its job, not
        # a citation to fix: the citation stays "the DOI", forever, regardless
        # of how the redirect happens to be coded today. Only the final
        # outcome matters.
        if 200 <= status < 400:
            return "ok"
        if status == 403:
            return "ok"  # resolves, access-controlled
        return "dead"
    permanent = any(code in (301, 308) for code, _ in chain)
    if 200 <= status < 300:
        return "redirected-permanently" if permanent else "ok"
    return "dead"


def check_one(token: str, limiter: RateLimiter, timeout: float) -> dict:
    is_doi = token.startswith("doi:")
    url = f"https://doi.org/{urllib.parse.quote(token[4:], safe='/:')}" if is_doi else token

    if any(host_matches(host_of(url), h) for h in HEAD_UNRELIABLE_HOSTS):
        status, final_url, chain, err, _ = fetch_with_retries(url, "GET", limiter, timeout)
    else:
        status, final_url, chain, err, _ = fetch_with_retries(url, "HEAD", limiter, timeout)
        if status == 0 or status >= 400:
            # Any HEAD failure gets a GET second opinion before being
            # believed: some CDNs (media.asml.com's, verified 2026-09-19)
            # answer HEAD with a bare 404 for a resource that a GET to the
            # exact same URL serves fine (200).
            status_g, final_g, chain_g, err_g, _ = fetch_with_retries(url, "GET", limiter, timeout)
            if status_g != 0:
                status, final_url, chain, err = status_g, final_g, chain_g, err_g
            elif status == 0:
                err = err or err_g

    category = classify(url, is_doi, status, final_url, chain, err)
    result = {
        "url": url,
        "status": status,
        "final_url": final_url,
        "chain": chain,
        "error": err,
        "category": category,
        "checked": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    if category == "dead":
        result["wayback"] = wayback_lookup(url, limiter, timeout)
    return result


def wayback_lookup(url: str, limiter: RateLimiter, timeout: float) -> dict | None:
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    status, _final, _chain, _err, body = fetch_with_retries(
        api, "GET", limiter, timeout, retries=2, read_body=True
    )
    if status != 200 or not body:
        return None
    try:
        data = json.loads(body.decode("utf-8", "replace"))
    except ValueError:
        return None
    snap = (data.get("archived_snapshots") or {}).get("closest")
    if not snap:
        return {"available": False}
    return {
        "available": bool(snap.get("available")),
        "url": snap.get("url"),
        "timestamp": snap.get("timestamp"),
        "status": snap.get("status"),
    }


# --------------------------------------------------------------------------
# Cache
# --------------------------------------------------------------------------


def load_cache(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_cache(path: Path, cache: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(cache, indent=1, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def is_fresh(entry: dict, max_age_days: int) -> bool:
    checked = entry.get("checked")
    if not checked:
        return False
    try:
        when = dt.datetime.fromisoformat(checked)
    except ValueError:
        return False
    if when.tzinfo is None:
        when = when.replace(tzinfo=dt.timezone.utc)
    age = dt.datetime.now(dt.timezone.utc) - when
    return age.days < max_age_days


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------


def run_checks(
    tokens: set[str],
    cache: dict,
    cache_path: Path,
    limiter: RateLimiter,
    timeout: float,
    max_age_days: int,
    force: bool,
    workers: int,
    time_budget: float | None,
    only_hosts: set[str] | None,
    skip_hosts: set[str] | None,
) -> None:
    def token_host(t: str) -> str:
        return "doi.org" if t.startswith("doi:") else host_of(t)

    pending = []
    for t in sorted(tokens):
        h = token_host(t)
        if only_hosts and not any(host_matches(h, o) for o in only_hosts):
            continue
        if skip_hosts and any(host_matches(h, s) for s in skip_hosts):
            continue
        if not force and t in cache and is_fresh(cache[t], max_age_days):
            continue
        pending.append(t)

    groups: dict[str, list[str]] = defaultdict(list)
    for t in pending:
        groups[token_host(t)].append(t)

    deadline = time.monotonic() + time_budget if time_budget else None
    save_lock = threading.Lock()
    stop = threading.Event()

    def worker(toks: list[str]) -> None:
        for t in toks:
            if stop.is_set() or (deadline and time.monotonic() > deadline):
                return
            try:
                result = check_one(t, limiter, timeout)
            except Exception as e:  # noqa: BLE001
                result = {
                    "url": t,
                    "status": 0,
                    "final_url": t,
                    "chain": [],
                    "error": f"internal error: {e}",
                    "category": "dead",
                    "checked": dt.datetime.now(dt.timezone.utc).isoformat(),
                }
            with save_lock:
                cache[t] = result
                save_cache(cache_path, cache)
                print(f"{result['category']:>20}  {result.get('status', 0):>3}  {t}", file=sys.stderr)

    if not pending:
        print("nothing to check (all fresh or filtered out)", file=sys.stderr)
        return

    print(f"checking {len(pending)} tokens across {len(groups)} hosts (workers={workers})", file=sys.stderr)
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            futs = [ex.submit(worker, toks) for toks in groups.values()]
            concurrent.futures.wait(futs)
    except KeyboardInterrupt:
        stop.set()
        raise


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------


def citers_for(reg: Registry, token: str) -> str:
    bits = []
    keys = sorted(reg.inventory_keys.get(token, ()))
    if keys:
        bits.append(", ".join(keys))
    for page, labels in sorted(reg.pages.get(token, {}).items()):
        for label in sorted(labels):
            bits.append(f"{page}#{label}")
    return "; ".join(bits) if bits else "(unreferenced)"


def render_report(reg: Registry, cache: dict, tokens: set[str]) -> str:
    by_cat: dict[str, list[str]] = defaultdict(list)
    unchecked = 0
    n_urls = sum(1 for t in tokens if not t.startswith("doi:"))
    n_dois = sum(1 for t in tokens if t.startswith("doi:"))
    for t in sorted(tokens):
        entry = cache.get(t)
        if not entry:
            unchecked += 1
            continue
        by_cat[entry["category"]].append(t)

    lines = ["# Link check report", ""]
    lines.append(f"Generated {dt.datetime.now(dt.timezone.utc).date().isoformat()}.")
    lines.append("")
    lines.append(f"* Tokens: {len(tokens)} ({n_urls} URLs, {n_dois} DOIs)")
    for cat in ("ok", "redirected-permanently", "blocked-to-scripts", "dead"):
        lines.append(f"* {cat}: {len(by_cat.get(cat, []))}")
    if unchecked:
        lines.append(f"* unchecked (no cache entry): {unchecked}")
    lines.append("")

    for cat, heading in (
        ("dead", "## Dead"),
        ("redirected-permanently", "## Redirected permanently"),
        ("blocked-to-scripts", "## Blocked to scripts"),
    ):
        toks = by_cat.get(cat, [])
        lines.append(heading)
        lines.append("")
        if not toks:
            lines.append("None.")
            lines.append("")
            continue
        if cat == "dead":
            lines.append("| Token | Cited by | HTTP / error | Wayback |")
            lines.append("| --- | --- | --- | --- |")
        else:
            lines.append("| Token | Cited by | Final URL |")
            lines.append("| --- | --- | --- |")
        for t in sorted(toks):
            entry = cache[t]
            cited = citers_for(reg, t)
            if cat == "dead":
                httpbit = entry.get("error") or f"HTTP {entry.get('status')}"
                wb = entry.get("wayback") or {}
                if wb.get("available"):
                    wtext = f"[{wb.get('timestamp')}]({wb.get('url')})"
                else:
                    wtext = "no snapshot"
                lines.append(f"| {t} | {cited} | {httpbit} | {wtext} |")
            else:
                lines.append(f"| {t} | {cited} | {entry.get('final_url')} |")
        lines.append("")

    lines.append("## OK")
    lines.append("")
    lines.append(f"{len(by_cat.get('ok', []))} tokens resolved normally (not listed individually).")
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------


def run_selftest() -> int:
    failures = []

    def check(name: str, cond: bool) -> None:
        if not cond:
            failures.append(name)

    inv_text = """
## 1. Section

**PDK-01** — *Root doc*.
<https://skywater-pdk.readthedocs.io/>.
Tier: cross-check.

**PDK-02** — *Paper*.
See DOI 10.1109/PROC.1972.8854. Also <https://doi.org/10.1109/PROC.1972.8854>
and <https://example.org/mirror>.
Tier: deep dive.
"""
    entries = parse_inventory(inv_text)
    check("PDK-01 present", "PDK-01" in entries)
    check(
        "PDK-01 url",
        entries.get("PDK-01", (set(), set()))[0] == {"https://skywater-pdk.readthedocs.io/"},
    )
    urls2, dois2 = entries.get("PDK-02", (set(), set()))
    check("PDK-02 dedups doi.org URL and bare DOI", dois2 == {"10.1109/proc.1972.8854"})
    check("PDK-02 other url kept", urls2 == {"https://example.org/mirror"})

    paren_text = "See <https://doi.org/10.1016/0022-0248(82)90456-2> and " "<https://en.wikipedia.org/wiki/Wafer_(electronics)>."
    urls3, dois3 = extract_urls_and_dois(paren_text)
    check(
        "bracketed DOI keeps its parentheses",
        dois3 == {"10.1016/0022-0248(82)90456-2"},
    )
    check(
        "bracketed URL keeps its parentheses",
        urls3 == {"https://en.wikipedia.org/wiki/Wafer_(electronics)"},
    )
    _urls4, dois4 = extract_urls_and_dois(
        "no. 1-2, pp. 1-80, 1998, DOI 10.1016/S0927-796X(98)00013-8. Low-energy"
    )
    check(
        "bare DOI mention keeps its parentheses and drops the trailing sentence period",
        dois4 == {"10.1016/s0927-796x(98)00013-8"},
    )

    page_text = """
Some claim.[^wiki-fick][^pdk-01]

<!-- footnotes -->

[^wiki-fick]: Wikipedia, *Fick's laws of diffusion*.
    <https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion>
[^pdk-01]: SkyWater PDK Authors, *root doc*.
    <https://skywater-pdk.readthedocs.io/>
"""
    footnotes = parse_page_footnotes(page_text)
    check("two footnote defs found", set(footnotes) == {"wiki-fick", "pdk-01"})
    check(
        "wiki-fick url",
        footnotes["wiki-fick"][0] == {"https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion"},
    )

    reg = Registry()
    reg.add_inventory("PDK-01", *entries["PDK-01"])
    reg.add_inventory("PDK-02", *entries["PDK-02"])
    reg.add_page("docs/x.md", "wiki-fick", *footnotes["wiki-fick"])
    reg.add_page("docs/x.md", "pdk-01", *footnotes["pdk-01"])
    check(
        "registry merges the shared URL",
        reg.pages["https://skywater-pdk.readthedocs.io/"]["docs/x.md"] == {"pdk-01"},
    )
    check("registry keeps inventory key", reg.inventory_keys["https://skywater-pdk.readthedocs.io/"] == {"PDK-01"})
    check(
        "doi token merges bare-DOI and doi.org URL forms",
        reg.inventory_keys[token_for(doi="10.1109/proc.1972.8854")] == {"PDK-02"},
    )

    # classify() unit cases, no network.
    check("plain 200 is ok", classify("https://a/", False, 200, "https://a/", [], None) == "ok")
    check(
        "301 then 200 is redirected-permanently",
        classify("https://a/", False, 200, "https://b/", [(301, "https://b/")], None)
        == "redirected-permanently",
    )
    check(
        "302 then 200 stays ok",
        classify("https://a/", False, 200, "https://b/", [(302, "https://b/")], None) == "ok",
    )
    check(
        "doi 403 after redirect is ok",
        classify("https://doi.org/x", True, 403, "https://pub/x", [(302, "https://pub/x")], None) == "ok",
    )
    check(
        "doi 301 redirect is ok, not redirected-permanently (the DOI is the permanent citation)",
        classify("https://doi.org/x", True, 200, "https://pub/x", [(301, "https://pub/x")], None) == "ok",
    )
    check(
        "sec.gov 403 is blocked-to-scripts",
        classify("https://www.sec.gov/x", False, 403, "https://www.sec.gov/x", [], None)
        == "blocked-to-scripts",
    )
    check("404 is dead", classify("https://a/", False, 404, "https://a/", [], None) == "dead")
    check(
        "a 200 landing on a bot-challenge page is blocked-to-scripts, not ok",
        classify(
            "https://openlibrary.org/isbn/x",
            False,
            200,
            "https://openlibrary.org/verify_human?next=/books/OLxM",
            [(302, "https://openlibrary.org/books/OLxM"), (303, "https://openlibrary.org/verify_human?next=/books/OLxM")],
            None,
        )
        == "blocked-to-scripts",
    )
    check(
        "connection failure is dead",
        classify("https://a/", False, 0, "https://a/", [], "timed out") == "dead",
    )

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("selftest ok")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true", help="run offline extraction self-tests and exit")
    ap.add_argument("--cache", type=Path, default=DEFAULT_CACHE, help="cache JSON file (default tmp/link-check-cache.json)")
    ap.add_argument("--max-age-days", type=int, default=30, help="skip rechecking entries newer than this")
    ap.add_argument("--force", action="store_true", help="ignore cache freshness and recheck everything")
    ap.add_argument("--rate-limit", type=float, default=3.0, help="seconds between requests to the same host")
    ap.add_argument(
        "--slow-host",
        action="append",
        default=[],
        metavar="HOST=SECONDS",
        help="override the per-host delay (repeatable); patents.google.com=20 is built in",
    )
    ap.add_argument("--timeout", type=float, default=25.0, help="per-request timeout in seconds")
    ap.add_argument("--workers", type=int, default=4, help="max hosts contacted in parallel")
    ap.add_argument("--time-budget", type=float, default=None, help="stop dispatching new checks after this many seconds")
    ap.add_argument("--only-host", action="append", default=[], help="only check tokens on this host (repeatable)")
    ap.add_argument("--skip-host", action="append", default=[], help="skip tokens on this host (repeatable)")
    ap.add_argument("--list-hosts", action="store_true", help="print pending-check counts per host and exit")
    ap.add_argument("--report", type=Path, default=None, help="write the Markdown report here (default: stdout)")
    ap.add_argument("--strict", action="store_true", help="exit non-zero if any token is classified dead")
    ap.add_argument(
        "--reclassify",
        action="store_true",
        help="recompute every cached entry's category from its stored HTTP result "
        "(no network access) -- use after a classify() logic change, then rerun "
        "normally to fill in anything newly dead (e.g. a missing wayback lookup)",
    )
    args = ap.parse_args()

    if args.selftest:
        return run_selftest()

    if args.reclassify:
        cache = load_cache(args.cache)
        changed = 0
        for t, entry in cache.items():
            new_cat = classify(
                entry["url"], t.startswith("doi:"), entry["status"], entry["final_url"], entry["chain"], entry.get("error")
            )
            if new_cat != entry.get("category"):
                changed += 1
                entry["category"] = new_cat
        save_cache(args.cache, cache)
        print(f"reclassified {len(cache)} entries, {changed} changed", file=sys.stderr)
        return 0

    reg = build_registry()
    tokens = reg.tokens()

    slow_hosts = dict(SLOW_HOSTS)
    for spec in args.slow_host:
        host, _, secs = spec.partition("=")
        slow_hosts[host] = float(secs)

    cache = load_cache(args.cache)

    if args.list_hosts:
        def token_host(t: str) -> str:
            return "doi.org" if t.startswith("doi:") else host_of(t)

        counts: dict[str, int] = defaultdict(int)
        pending: dict[str, int] = defaultdict(int)
        for t in tokens:
            h = token_host(t)
            counts[h] += 1
            if args.force or t not in cache or not is_fresh(cache[t], args.max_age_days):
                pending[h] += 1
        for h, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"{n:5d} total  {pending.get(h, 0):5d} pending  {h}")
        return 0

    limiter = RateLimiter(args.rate_limit, slow_hosts)
    run_checks(
        tokens,
        cache,
        args.cache,
        limiter,
        args.timeout,
        args.max_age_days,
        args.force,
        args.workers,
        args.time_budget,
        set(args.only_host) or None,
        set(args.skip_host) or None,
    )

    report = render_report(reg, cache, tokens)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
    else:
        print(report)

    if args.strict:
        dead = sum(1 for t in tokens if cache.get(t, {}).get("category") == "dead")
        if dead:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
