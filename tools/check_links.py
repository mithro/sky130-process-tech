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

``--include-generated`` additionally scans the generated reference indexes
(``docs/references/{patents,papers,filings}/``), which cite sources as
inline links rather than footnotes (the documented exception in
``docs/plans/citation-style.md``); Espacenet and Google Patents record-page
links are sampled 1-in-50 rather than crawled, since a single family can
carry a pair of them and there are thousands of families -- every other
host cited there is still checked in full, and ``BLOCKED_HOSTS`` still
applies.

``--suggest-archive`` prints, for each token classified dead, the
ready-to-paste archive citation lines (R-WAYBACK / report-C.md C5 step 3)
and the files that repeat its URL -- a suggestion only: this tool never
rewrites a page or the inventory, and never gives a DOI an archive form.

A "dead" token's Wayback answer is never trusted negative for more than a
day (independent of ``--max-age-days``, which governs the surrounding HTTP
check): a stale negative lookup is quietly redone on the next run even
when the HTTP result itself is still considered fresh.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import re
import sys
import tempfile
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

# report-C.md C5 step 1: the availability API's timestamp when a citation
# carries no accessed/retrieved date of its own -- the inventory's own
# check date.
DEFAULT_WAYBACK_TIMESTAMP = "20260830"

# C5: "never cache a negative archive answer for more than a day" -- this
# is independent of --max-age-days, which governs the surrounding HTTP
# check.  A "dead" token whose last Wayback lookup came back negative (or
# was never done) more than this many days ago gets that lookup redone
# even when the HTTP result itself is still considered fresh.
WAYBACK_NEGATIVE_MAX_AGE_DAYS = 1

# --include-generated: directories of gen_*.py output scanned in addition
# to the hand-written pages (citation-style.md's documented exception --
# these pages link inline, not via footnotes).
GENERATED_DIRS = ("patents", "papers", "filings")

# Not content pages -- matches conf.py's own Sphinx `exclude_patterns`
# ("plans/**"). Internal planning docs illustrate citation forms with
# fenced-code-block examples (a literal <https://example.com/page>, an
# ellipsis-truncated placeholder host); a bare "starts a line with
# `[^label]:`" regex cannot tell that apart from a real footnote
# definition, so this scope must be excluded explicitly.
EXCLUDED_TOP_LEVEL_DIRS = {"plans"}

# Hosts cited so many times on generated pages (thousands of Espacenet /
# Google Patents record-page links per family) that checking every one
# would hammer those hosts; --include-generated samples them instead of
# crawling them, per report-C.md C5 and the coordinator's note on that
# open question.
SAMPLED_GENERATED_HOSTS = {"patents.google.com", "espacenet.com"}
SAMPLE_RATE = 50  # 1 in N

# "the citation's accessed/retrieved date" -- ordinary house-style wording
# ("accessed 2026-08-30." / "..., retrieved 2026-09-14.") found in the
# same footnote-definition or inventory-entry block as its URL(s).
ACCESS_DATE_RE = re.compile(r"\b(?:accessed|retrieved)\s+(\d{4})-(\d{2})-(\d{2})\b", re.IGNORECASE)

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
    "astm.org",  # 403 to scripted clients (verified 2026-09-19); Akamai bot check
    "cdc.gov",  # 403 to scripted clients (verified 2026-09-19); Wayback shows the pages live
    "appliedmaterials.com",  # 403 to scripted clients (verified 2026-09-19); Wayback shows the page live
    "forbes.com",  # 403 to scripted clients (verified 2026-09-19); Wayback shows the page live
    "businesswire.com",  # connection dropped for scripted clients (verified 2026-09-19); Wayback shows the page live
    "startribune.com",  # persistent 429 to scripted clients (verified 2026-09-19); Wayback shows the pages live and recent
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


def extract_access_date(text: str) -> str | None:
    """Return the block's ``accessed``/``retrieved YYYY-MM-DD`` date, compact.

    Used as the availability API's timestamp (C5 step 1); ``None`` if the
    block names no such date, in which case the caller falls back to
    ``DEFAULT_WAYBACK_TIMESTAMP``.
    """
    m = ACCESS_DATE_RE.search(text)
    if not m:
        return None
    return f"{m.group(1)}{m.group(2)}{m.group(3)}"


def parse_inventory(text: str) -> dict[str, tuple[set[str], set[str], str | None]]:
    """Return ``{KEY: (urls, dois, access_date)}`` for every ``**KEY**`` entry."""
    entries: dict[str, tuple[set[str], set[str], str | None]] = {}
    matches = list(KEY_RE.finditer(text))
    for i, m in enumerate(matches):
        key = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        urls, dois = extract_urls_and_dois(block)
        date = extract_access_date(block)
        eurls, edois, _ = entries.get(key, (set(), set(), None))
        eurls.update(urls)
        edois.update(dois)
        entries[key] = (eurls, edois, date)
    return entries


def parse_page_footnotes(text: str) -> dict[str, tuple[set[str], set[str], str | None]]:
    """Return ``{label: (urls, dois, access_date)}`` for every footnote def."""
    result: dict[str, tuple[set[str], set[str], str | None]] = {}
    for m in FOOTNOTE_DEF_RE.finditer(text):
        label = m.group(1)
        block = m.group(2)
        urls, dois = extract_urls_and_dois(block)
        date = extract_access_date(block)
        rurls, rdois, _ = result.get(label, (set(), set(), None))
        rurls.update(urls)
        rdois.update(dois)
        result[label] = (rurls, rdois, date)
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
        # token -> the first accessed/retrieved date (compact YYYYMMDD)
        # found citing it; feeds the Wayback availability timestamp (C5).
        self.access_dates: dict[str, str] = {}

    def _note_dates(self, urls: set[str], dois: set[str], access_date: str | None) -> None:
        if not access_date:
            return
        for u in urls:
            self.access_dates.setdefault(u, access_date)
        for d in dois:
            self.access_dates.setdefault(token_for(doi=d), access_date)

    def add_inventory(
        self, key: str, urls: set[str], dois: set[str], access_date: str | None = None
    ) -> None:
        for u in urls:
            self.inventory_keys[u].add(key)
        for d in dois:
            self.inventory_keys[token_for(doi=d)].add(key)
        self._note_dates(urls, dois, access_date)

    def add_page(
        self,
        page: str,
        label: str,
        urls: set[str],
        dois: set[str],
        access_date: str | None = None,
    ) -> None:
        for u in urls:
            self.pages[u][page].add(label)
        for d in dois:
            self.pages[token_for(doi=d)][page].add(label)
        self._note_dates(urls, dois, access_date)

    def tokens(self) -> set[str]:
        return set(self.inventory_keys) | set(self.pages)


def _sample_keep(token: str, rate: int = SAMPLE_RATE) -> bool:
    """Deterministic 1-in-``rate`` sample (stable across runs, for the cache)."""
    digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
    return int(digest, 16) % rate == 0


def _scan_generated(reg: Registry, docs_dir: Path) -> None:
    """Add inline links from the generated reference indexes (--include-generated).

    These pages cite sources as plain inline links, not footnotes
    (``docs/plans/citation-style.md``, "Exception: generated index
    pages"), so they are scanned as a whole rather than split into
    definition blocks.  Espacenet and Google Patents record-page links
    are sampled 1-in-``SAMPLE_RATE`` rather than crawled (thousands of
    them, one pair per patent family); every other host cited here is
    checked in full, same as a hand-written page's footnotes; hosts
    already in ``BLOCKED_HOSTS`` are still classified blocked-to-scripts
    as usual, not specially excluded.
    """
    for sub in GENERATED_DIRS:
        d = docs_dir / "references" / sub
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            urls, dois = extract_urls_and_dois(text)
            kept_urls = set()
            for u in urls:
                host = host_of(u)
                if any(host_matches(host, s) for s in SAMPLED_GENERATED_HOSTS):
                    if _sample_keep(u):
                        kept_urls.add(u)
                else:
                    kept_urls.add(u)
            reg.add_page(str(path.relative_to(docs_dir.parent)), "(generated)", kept_urls, dois)


def build_registry(
    docs_dir: Path = DOCS, inventory: Path = INVENTORY, include_generated: bool = False
) -> Registry:
    reg = Registry()
    if inventory.exists():
        for key, (urls, dois, date) in parse_inventory(inventory.read_text(encoding="utf-8")).items():
            reg.add_inventory(key, urls, dois, date)
    for path in sorted(docs_dir.rglob("*.md")):
        rel_parts = path.relative_to(docs_dir).parts
        if rel_parts and rel_parts[0] in EXCLUDED_TOP_LEVEL_DIRS:
            # Not a hand-written or generated content page (Sphinx's own
            # conf.py excludes "plans/**" from the build the same way):
            # planning docs quote example citations -- including a fenced
            # R-WAYBACK template with a literal <https://example.com/page>
            # -- as illustrative markdown, not real footnote definitions to
            # check.
            continue
        if include_generated:
            if len(rel_parts) >= 2 and rel_parts[0] == "references" and rel_parts[1] in GENERATED_DIRS:
                continue  # scanned whole-file by _scan_generated instead
        text = path.read_text(encoding="utf-8")
        for label, (urls, dois, date) in parse_page_footnotes(text).items():
            reg.add_page(str(path.relative_to(docs_dir.parent)), label, urls, dois, date)
    if include_generated:
        _scan_generated(reg, docs_dir)
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


def check_one(token: str, limiter: RateLimiter, timeout: float, access_date: str | None = None) -> dict:
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
    # A dead DOI is still looked up (the report keeps saying whether a
    # snapshot exists, as before), but --suggest-archive never turns that
    # into a citation: a DOI is never replaced by an archive URL (C5 step
    # 5, rule 11) -- a dead DOI keeps the DOI and a dated note by hand.
    if category == "dead":
        result["wayback"] = wayback_lookup(url, limiter, timeout, access_date=access_date)
        result["wayback_checked"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


def _swap_scheme(url: str) -> str:
    if url.startswith("https://"):
        return "http://" + url[len("https://") :]
    if url.startswith("http://"):
        return "https://" + url[len("http://") :]
    return url


def _toggle_www(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    host = parts.netloc
    new_host = host[4:] if host.lower().startswith("www.") else "www." + host
    return urllib.parse.urlunsplit((parts.scheme, new_host, parts.path, parts.query, parts.fragment))


def _accept_snapshot(data: dict | None) -> dict | None:
    """Return the ``closest`` snapshot dict iff it is a positive, well-formed hit.

    C5 step 1: accept only ``available: true`` and ``status: "200"``.
    """
    if not isinstance(data, dict):
        return None
    snaps = data.get("archived_snapshots")
    if not isinstance(snaps, dict):
        return None
    closest = snaps.get("closest")
    if not isinstance(closest, dict):
        return None
    if closest.get("available") is True and str(closest.get("status")) == "200":
        return closest
    return None


def _availability_json(url: str, timestamp: str, limiter: RateLimiter, timeout: float) -> dict | None:
    """Real network call to the Wayback availability API. Returns the parsed
    JSON body (which may legitimately be ``{}`` -- see ``wayback_lookup``),
    or ``None`` if the HTTP request itself failed."""
    api = (
        "https://archive.org/wayback/available?url="
        + urllib.parse.quote(url, safe="")
        + "&timestamp="
        + timestamp
    )
    status, _final, _chain, _err, body = fetch_with_retries(
        api, "GET", limiter, timeout, retries=2, read_body=True
    )
    if status != 200 or not body:
        return None
    try:
        return json.loads(body.decode("utf-8", "replace"))
    except ValueError:
        return None


def _cdx_lookup(url: str, limiter: RateLimiter, timeout: float) -> dict | None:
    """Real network call to the CDX API; returns an already-formatted
    snapshot result (matching wayback_lookup's return shape), or ``None``."""
    api = (
        "https://web.archive.org/cdx/search/cdx?url="
        + urllib.parse.quote(url, safe="")
        + "&output=json&filter=statuscode:200&limit=-3&fl=timestamp,original"
    )
    status, _final, _chain, _err, body = fetch_with_retries(
        api, "GET", limiter, timeout, retries=2, read_body=True
    )
    if status != 200 or not body:
        return None
    try:
        rows = json.loads(body.decode("utf-8", "replace"))
    except ValueError:
        return None
    if not isinstance(rows, list) or len(rows) < 2:
        return None
    timestamp, original = rows[-1][0], rows[-1][1]  # most recent 200 capture
    return {
        "available": True,
        "url": f"https://web.archive.org/web/{timestamp}/{original}",
        "timestamp": timestamp,
        "status": "200",
    }


def wayback_lookup(
    url: str,
    limiter: RateLimiter,
    timeout: float,
    access_date: str | None = None,
    query_availability=_availability_json,
    query_cdx=_cdx_lookup,
    sleep=time.sleep,
) -> dict:
    """C5 step 1, fixed.

    Query the availability API with the citation's own accessed/retrieved
    date as the timestamp (else ``DEFAULT_WAYBACK_TIMESTAMP``). Accept only
    ``available: true`` and ``status: "200"``. The API intermittently
    answers a bare, structurally empty ``{}`` under load rather than its
    normal "nothing archived" shape (``{"url": ..., "archived_snapshots":
    {}, "timestamp": ...}``) -- report-C.md's C5 finding, confirmed by this
    tool's earlier behaviour of caching that glitch as a permanent "no
    snapshot". On that exact ``{}``, retry once after 10 s. If there is
    still no accepted snapshot (whether from the glitch or a genuine miss),
    fall through, in order and without looping, to: the other URL scheme,
    then the URL with/without a leading ``www.``, then the CDX API. At most
    five network calls total.
    """
    timestamp = access_date or DEFAULT_WAYBACK_TIMESTAMP

    def result_from(snap: dict) -> dict:
        return {
            "available": True,
            "url": snap.get("url"),
            "timestamp": snap.get("timestamp"),
            "status": snap.get("status"),
        }

    data = query_availability(url, timestamp, limiter, timeout)
    snap = _accept_snapshot(data)
    if snap:
        return result_from(snap)

    if data == {}:
        sleep(10)
        data = query_availability(url, timestamp, limiter, timeout)
        snap = _accept_snapshot(data)
        if snap:
            return result_from(snap)

    data = query_availability(_swap_scheme(url), timestamp, limiter, timeout)
    snap = _accept_snapshot(data)
    if snap:
        return result_from(snap)

    data = query_availability(_toggle_www(url), timestamp, limiter, timeout)
    snap = _accept_snapshot(data)
    if snap:
        return result_from(snap)

    cdx = query_cdx(url, limiter, timeout)
    if cdx:
        return cdx

    return {"available": False}


def wayback_is_stale_negative(entry: dict, max_age_days: int = WAYBACK_NEGATIVE_MAX_AGE_DAYS) -> bool:
    """True if a "dead" entry's cached Wayback answer is a negative one
    older than ``max_age_days`` -- C5: "never cache a negative archive
    answer for more than a day", independent of --max-age-days on the
    surrounding HTTP check."""
    wb = entry.get("wayback")
    if wb is None or wb.get("available"):
        return False
    checked = entry.get("wayback_checked") or entry.get("checked")
    if not checked:
        return True
    try:
        when = dt.datetime.fromisoformat(checked)
    except ValueError:
        return True
    if when.tzinfo is None:
        when = when.replace(tzinfo=dt.timezone.utc)
    age = dt.datetime.now(dt.timezone.utc) - when
    return age >= dt.timedelta(days=max_age_days)


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
    access_dates: dict[str, str] | None = None,
) -> None:
    access_dates = access_dates or {}

    def token_host(t: str) -> str:
        return "doi.org" if t.startswith("doi:") else host_of(t)

    def host_filtered_out(t: str) -> bool:
        h = token_host(t)
        if only_hosts and not any(host_matches(h, o) for o in only_hosts):
            return True
        if skip_hosts and any(host_matches(h, s) for s in skip_hosts):
            return True
        return False

    pending = []
    for t in sorted(tokens):
        if host_filtered_out(t):
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
                result = check_one(t, limiter, timeout, access_date=access_dates.get(t))
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

    if pending:
        print(f"checking {len(pending)} tokens across {len(groups)} hosts (workers={workers})", file=sys.stderr)
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
                futs = [ex.submit(worker, toks) for toks in groups.values()]
                concurrent.futures.wait(futs)
        except KeyboardInterrupt:
            stop.set()
            raise
    else:
        print("nothing to check (all fresh or filtered out)", file=sys.stderr)

    # C5: "never cache a negative archive answer for more than a day",
    # independent of --max-age-days above. A "dead" token that was not
    # rechecked in full just now, but whose last Wayback lookup was
    # negative and is stale, gets just that lookup redone (no re-fetch of
    # the original, still-dead URL).
    refresh = [
        t
        for t in sorted(tokens)
        if t not in pending
        and not host_filtered_out(t)
        and t in cache
        and cache[t].get("category") == "dead"
        and wayback_is_stale_negative(cache[t])
    ]
    if refresh:
        print(f"refreshing {len(refresh)} stale negative Wayback lookups", file=sys.stderr)
        for t in refresh:
            entry = cache[t]
            entry["wayback"] = wayback_lookup(entry["url"], limiter, timeout, access_date=access_dates.get(t))
            entry["wayback_checked"] = dt.datetime.now(dt.timezone.utc).isoformat()
            cache[t] = entry
            save_cache(cache_path, cache)
            print(f"    wayback  {'found' if entry['wayback'].get('available') else 'none'}  {t}", file=sys.stderr)


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


def _files_citing(reg: Registry, token: str) -> list[str]:
    files = sorted(reg.pages.get(token, {}))
    if token in reg.inventory_keys:
        files = [str(INVENTORY.relative_to(ROOT))] + files
    return files


def render_suggestions(reg: Registry, cache: dict, tokens: set[str]) -> str:
    """``--suggest-archive``: for each dead token, the ready-to-paste C5
    step-3 citation lines and the files that repeat its URL. Never rewrites
    a file -- printing only; step 2 (verifying the snapshot) is a judgement
    call for a person, not this tool, and DOIs are never given an archive
    form (C5 step 5)."""
    lines = ["## Suggested archive citations (--suggest-archive)", ""]
    dead = sorted(t for t in tokens if cache.get(t, {}).get("category") == "dead")
    if not dead:
        lines.append("No dead tokens.")
        lines.append("")
        return "\n".join(lines)

    for t in dead:
        entry = cache[t]
        files = _files_citing(reg, t)
        lines.append(f"### `{t}`")
        lines.append("")
        lines.append(f"Cited by: {', '.join(files) if files else '(unreferenced)'}")
        lines.append("")
        if t.startswith("doi:"):
            lines.append(
                "DOI -- never replace with an archive URL (C5 step 5). Keep the DOI plus a "
                "dated note (rule 11 of `docs/plans/agent-briefs.md`)."
            )
            lines.append("")
            continue
        wb = entry.get("wayback") or {}
        if not wb.get("available"):
            lines.append("No snapshot found (also try `archive.ph/newest/<url>` by hand). Apply rule 11 of "
                         "`docs/plans/agent-briefs.md` unchanged.")
            lines.append("")
            continue
        dead_since = entry.get("checked", "")[:10]
        ts = wb.get("timestamp") or ""
        capture_date = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}" if len(ts) >= 8 else "unknown-date"
        archive_url = (wb.get("url") or "").replace("http://web.archive.org", "https://web.archive.org", 1)
        lines.append("Verify the snapshot (C5 step 2) before pasting -- fetch the `id_` form once and confirm "
                      "the title, or a string the pages quote, is present.")
        lines.append("")
        lines.append("```markdown")
        lines.append(f"    <{archive_url}>")
        lines.append(f"    (Wayback Machine capture of {capture_date}; original, dead since {dead_since}:")
        lines.append(f"    `{t}`).")
        lines.append("```")
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
        entries.get("PDK-01", (set(), set(), None))[0] == {"https://skywater-pdk.readthedocs.io/"},
    )
    urls2, dois2, _date2 = entries.get("PDK-02", (set(), set(), None))
    check("PDK-02 dedups doi.org URL and bare DOI", dois2 == {"10.1109/proc.1972.8854"})
    check("PDK-02 other url kept", urls2 == {"https://example.org/mirror"})

    access_text = """
**ACC-01** — *Some page*, accessed 2026-08-30.
<https://example.org/a>.
Tier: cross-check.

**ACC-02** — *Some other page*, retrieved 2026-04-11.
<https://example.org/b>.
Tier: cross-check.

**ACC-03** — *No date given*.
<https://example.org/c>.
Tier: cross-check.
"""
    check("accessed date extracted compact", extract_access_date("accessed 2026-08-30.") == "20260830")
    check("retrieved date extracted compact", extract_access_date("retrieved 2026-04-11.") == "20260411")
    check("no date found is None", extract_access_date("no date here.") is None)
    acc_entries = parse_inventory(access_text)
    check("ACC-01 access date", acc_entries["ACC-01"][2] == "20260830")
    check("ACC-02 access date", acc_entries["ACC-02"][2] == "20260411")
    check("ACC-03 has no access date", acc_entries["ACC-03"][2] is None)
    acc_reg = Registry()
    for key, (urls, dois, date) in acc_entries.items():
        acc_reg.add_inventory(key, urls, dois, date)
    check(
        "registry records the access date per token (feeds the Wayback timestamp)",
        acc_reg.access_dates.get("https://example.org/a") == "20260830"
        and acc_reg.access_dates.get("https://example.org/b") == "20260411"
        and "https://example.org/c" not in acc_reg.access_dates,
    )

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

    # build_registry() must not scan docs/plans/ (matches conf.py's own
    # Sphinx exclude_patterns): a planning doc's fenced-code-block example
    # citation (R-WAYBACK's own template, verbatim) is not a real
    # footnote to check -- it is not a content page at all. Filesystem
    # only, no network.
    with tempfile.TemporaryDirectory() as tmp:
        tmp_docs = Path(tmp) / "docs"
        (tmp_docs / "steps").mkdir(parents=True)
        (tmp_docs / "plans").mkdir(parents=True)
        (tmp_docs / "steps" / "001-real.md").write_text(
            "Claim.[^wiki-x]\n\n[^wiki-x]: Wikipedia, *X*.\n    <https://en.wikipedia.org/wiki/X>\n",
            encoding="utf-8",
        )
        (tmp_docs / "plans" / "readability-guide.md").write_text(
            "Example template:\n\n```\n[^key]: Author, *Title*.\n"
            "    <https://web.archive.org/web/20260411150120/https://example.com/page>\n"
            "    (original: `https://example.com/page`).\n```\n",
            encoding="utf-8",
        )
        tmp_reg = build_registry(docs_dir=tmp_docs, inventory=Path(tmp) / "nonexistent.md")
        check("real content page is scanned", "https://en.wikipedia.org/wiki/X" in tmp_reg.tokens())
        check(
            "docs/plans/ is excluded (illustrative example, not a real citation)",
            "https://example.com/page" not in tmp_reg.tokens()
            and not any("web.archive.org" in t for t in tmp_reg.tokens()),
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

    # -- wayback_lookup() fallback chain (C5 step 1), all offline: canned
    # query functions stand in for the two network calls it makes, and
    # `sleep` is captured rather than actually waited on.

    def fake_limiter() -> RateLimiter:
        return RateLimiter(0.0, {})

    check("swap scheme https->http", _swap_scheme("https://a.example/x") == "http://a.example/x")
    check("swap scheme http->https", _swap_scheme("http://a.example/x") == "https://a.example/x")
    check("toggle www adds it", _toggle_www("https://a.example/x") == "https://www.a.example/x")
    check("toggle www removes it", _toggle_www("https://www.a.example/x") == "https://a.example/x")

    good_snapshot = {
        "archived_snapshots": {"closest": {"available": True, "status": "200", "url": "https://web.archive.org/web/20260411000000/https://a.example/x", "timestamp": "20260411000000"}}
    }
    not_found = {"url": "https://a.example/x", "archived_snapshots": {}, "timestamp": "20260830"}
    unavailable = {
        "archived_snapshots": {"closest": {"available": False, "status": "404", "url": "x", "timestamp": "20260101"}}
    }

    # 1. First query already succeeds -- no fallback calls made at all.
    calls = []

    def q_first_ok(url, ts, limiter, timeout):
        calls.append(url)
        return good_snapshot

    def cdx_should_not_be_called(url, limiter, timeout):
        failures.append("cdx called when the first query already succeeded")
        return None

    r = wayback_lookup(
        "https://a.example/x", fake_limiter(), 5.0, query_availability=q_first_ok, query_cdx=cdx_should_not_be_called, sleep=lambda s: None
    )
    check("first-query success is accepted", r == {"available": True, "url": good_snapshot["archived_snapshots"]["closest"]["url"], "timestamp": "20260411000000", "status": "200"})
    check("first-query success makes exactly one call", calls == ["https://a.example/x"])

    # 2. Empty `{}` on the first call -> retry once after a (mocked) sleep,
    #    which then succeeds; no scheme/www/CDX fallback needed.
    calls = []
    sleeps = []

    def q_empty_then_ok(url, ts, limiter, timeout):
        calls.append(url)
        return {} if len(calls) == 1 else good_snapshot

    r = wayback_lookup(
        "https://a.example/x",
        fake_limiter(),
        5.0,
        query_availability=q_empty_then_ok,
        query_cdx=cdx_should_not_be_called,
        sleep=lambda s: sleeps.append(s),
    )
    check("retries once after a bare {} answer", calls == ["https://a.example/x", "https://a.example/x"])
    check("sleeps 10s before the retry", sleeps == [10])
    check("retry success is accepted", r["available"] is True)

    # 3. Never finds anything positive -> falls through scheme, www, then
    #    CDX, in that order, and stops as soon as one accepts; never loops
    #    (bounded at exactly the calls below).
    calls = []

    def q_track_variants(url, ts, limiter, timeout):
        calls.append(url)
        return not_found  # well-formed "nothing archived", every time

    def cdx_hit(url, limiter, timeout):
        return {"available": True, "url": f"https://web.archive.org/web/20250101000000/{url}", "timestamp": "20250101000000", "status": "200"}

    r = wayback_lookup(
        "https://a.example/x", fake_limiter(), 5.0, query_availability=q_track_variants, query_cdx=cdx_hit, sleep=lambda s: None
    )
    check(
        "tries original, other scheme, then www-toggle before CDX (bounded, no retry loop on a well-formed miss)",
        calls == ["https://a.example/x", "http://a.example/x", "https://www.a.example/x"],
    )
    check("CDX fallback result is used when nothing else accepts", r["available"] is True and r["timestamp"] == "20250101000000")

    # 4. Nothing anywhere, CDX included -> a clean negative, not a crash or
    #    an infinite loop.
    r = wayback_lookup(
        "https://a.example/x",
        fake_limiter(),
        5.0,
        query_availability=lambda *a: unavailable,
        query_cdx=lambda *a: None,
        sleep=lambda s: None,
    )
    check("no snapshot anywhere is a clean negative", r == {"available": False})

    # 5. The citation's own accessed/retrieved date is used as the
    #    timestamp; falls back to DEFAULT_WAYBACK_TIMESTAMP otherwise.
    seen_ts = []

    def q_record_ts(url, ts, limiter, timeout):
        seen_ts.append(ts)
        return good_snapshot

    wayback_lookup("https://a.example/x", fake_limiter(), 5.0, access_date="20260411", query_availability=q_record_ts, sleep=lambda s: None)
    wayback_lookup("https://a.example/x", fake_limiter(), 5.0, access_date=None, query_availability=q_record_ts, sleep=lambda s: None)
    check("uses the citation's own access date as the timestamp", seen_ts[0] == "20260411")
    check("falls back to the inventory's check date", seen_ts[1] == DEFAULT_WAYBACK_TIMESTAMP)

    # -- stale-negative cache rule: never trust a negative Wayback answer
    # for more than a day, independent of --max-age-days.
    now = dt.datetime.now(dt.timezone.utc)
    fresh_negative = {"wayback": {"available": False}, "wayback_checked": now.isoformat()}
    stale_negative = {
        "wayback": {"available": False},
        "wayback_checked": (now - dt.timedelta(days=2)).isoformat(),
    }
    positive = {"wayback": {"available": True}, "wayback_checked": (now - dt.timedelta(days=30)).isoformat()}
    check("a same-day negative is not stale", wayback_is_stale_negative(fresh_negative) is False)
    check("a two-day-old negative is stale", wayback_is_stale_negative(stale_negative) is True)
    check("a positive answer is never 'stale negative', however old", wayback_is_stale_negative(positive) is False)

    # -- deterministic sampling for --include-generated (same subset every
    # run, so the cache stays useful; never every token, never zero).
    sample_tokens = [f"https://patents.google.com/patent/US{n}A/en" for n in range(2000)]
    kept = [t for t in sample_tokens if _sample_keep(t)]
    check("sampling keeps roughly 1-in-N, not all or none", 0 < len(kept) < len(sample_tokens))
    check(
        "sampling is deterministic across calls (stable cache)",
        kept == [t for t in sample_tokens if _sample_keep(t)],
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
    ap.add_argument(
        "--include-generated",
        action="store_true",
        help="also scan docs/references/{patents,papers,filings}/ (inline links, "
        "citation-style.md's documented exception); Espacenet and Google Patents "
        f"record-page links are sampled 1-in-{SAMPLE_RATE} rather than crawled",
    )
    ap.add_argument(
        "--suggest-archive",
        action="store_true",
        help="print, for each dead token, the ready-to-paste C5 step-3 citation "
        "lines and the files citing it (does not write any file)",
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

    reg = build_registry(include_generated=args.include_generated)
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
        access_dates=reg.access_dates,
    )

    report = render_report(reg, cache, tokens)
    if args.suggest_archive:
        report = report.rstrip("\n") + "\n\n" + render_suggestions(reg, cache, tokens)
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
