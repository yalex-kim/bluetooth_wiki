#!/usr/bin/env python3
"""Download PDF documents listed on Bluetooth Core Specification pages.

The script reads each version page, extracts the Documents section, and stores
PDF files under sources/specs/<version>/. It can optionally use a Netscape
cookies.txt file exported from a logged-in browser session.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from http.cookiejar import MozillaCookieJar
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import HTTPCookieProcessor, Request, build_opener


DEFAULT_VERSIONS = ("5.0", "5.1", "5.2", "5.3", "5.4", "6.0", "6.1", "6.2")
BASE_PAGE = "https://www.bluetooth.com/specifications/specs/core-specification-{slug}/"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)


@dataclass(frozen=True)
class DocumentLink:
    title: str
    url: str
    extension: str


class DocumentSectionParser(HTMLParser):
    """Minimal parser for the Bluetooth spec Documents section."""

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.in_documents = False
        self._pending_href: str | None = None
        self._anchor_text: list[str] = []
        self._recent_text: list[str] = []
        self.documents: list[DocumentLink] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self._pending_href = urljoin(self.base_url, href)
            self._anchor_text = []

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if not text:
            return
        if text == "Documents":
            self.in_documents = True
            self._recent_text.clear()
            return
        if self.in_documents and text in {"Company information", "English"}:
            self.in_documents = False
            return
        if self._pending_href:
            self._anchor_text.append(text)
        elif self.in_documents:
            self._recent_text.append(text)
            self._recent_text = self._recent_text[-6:]

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or not self._pending_href:
            return

        href = self._pending_href
        link_text = " ".join(self._anchor_text).strip()
        extension = link_text.upper()
        if self.in_documents and extension == "PDF":
            self.documents.append(
                DocumentLink(
                    title=self._title_before_link(),
                    url=href,
                    extension=extension.lower(),
                )
            )
        elif self.in_documents and link_text:
            self._recent_text.append(link_text)
            self._recent_text = self._recent_text[-6:]

        self._pending_href = None
        self._anchor_text = []

    def _title_before_link(self) -> str:
        for text in reversed(self._recent_text):
            if text.upper() not in {"PDF", "HTML", "XLS", "ZIP"}:
                return text
        return "document"


def version_page_url(version: str) -> str:
    return BASE_PAGE.format(slug=version.replace(".", "-"))


def sanitize_filename(value: str, fallback: str = "document") -> str:
    cleaned = re.sub(r"[^\w.\-+() ]+", "_", value, flags=re.ASCII)
    cleaned = re.sub(r"\s+", "_", cleaned).strip("._ ")
    return cleaned or fallback


def content_filename(response_url: str, content_disposition: str | None) -> str | None:
    if content_disposition:
        match = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)"?', content_disposition)
        if match:
            return sanitize_filename(match.group(1))

    name = Path(urlparse(response_url).path).name
    if name.lower().endswith(".pdf"):
        return sanitize_filename(name)
    return None


def make_opener(cookies: Path | None):
    if not cookies:
        return build_opener()
    jar = MozillaCookieJar(str(cookies))
    jar.load(ignore_discard=True, ignore_expires=True)
    return build_opener(HTTPCookieProcessor(jar))


def load_download_cache(output_dir: Path) -> dict[str, Path]:
    cache: dict[str, Path] = {}
    for manifest in output_dir.glob("*/manifest.json"):
        try:
            entries = json.loads(manifest.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for entry in entries:
            if entry.get("status") not in {"downloaded", "skipped", "copied"}:
                continue
            path = Path(entry.get("path", ""))
            if path.exists() and path.suffix.lower() == ".pdf":
                cache.setdefault(entry.get("url", ""), path)
    return cache


def read_url(opener, url: str) -> tuple[bytes, str, object]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Referer": "https://www.bluetooth.com/"})
    response = opener.open(request, timeout=60)
    return response.read(), response.geturl(), response.headers


def parse_documents(opener, version: str) -> list[DocumentLink]:
    page_url = version_page_url(version)
    body, final_url, _headers = read_url(opener, page_url)
    parser = DocumentSectionParser(final_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.documents


def copy_cached_document(doc: DocumentLink, output_dir: Path, cache: dict[str, Path]) -> dict[str, str] | None:
    cached_path = cache.get(doc.url)
    if not cached_path:
        cached_path = find_cached_by_slug(doc.url, output_dir.parent)
    if not cached_path or not cached_path.exists():
        return None

    output_path = output_dir / cached_path.name
    if not output_path.exists():
        shutil.copy2(cached_path, output_path)
    return {"title": doc.title, "url": doc.url, "path": str(output_path), "status": "copied"}


def filename_from_files_slug(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.netloc != "files.bluetooth.com":
        return None
    slug = parsed.path.strip("/").split("/")[-1]
    if not slug.endswith("-pdf"):
        return None
    parts = slug.removesuffix("-pdf").split("-")
    if len(parts) < 3:
        return None
    revision = parts[-1]
    kind = parts[-2].upper()
    component = "".join(parts[:-2]).upper()
    if kind not in {"TS", "ICS"} or not re.fullmatch(r"p\d+", revision):
        return None
    return f"{component}.{kind}.{revision}.pdf"


def find_cached_by_slug(url: str, specs_dir: Path) -> Path | None:
    filename = filename_from_files_slug(url)
    if not filename:
        return None
    for candidate in specs_dir.glob(f"*/{filename}"):
        if candidate.is_file():
            return candidate
    return None


def download_document(
    opener,
    doc: DocumentLink,
    output_dir: Path,
    dry_run: bool,
    cache: dict[str, Path],
) -> dict[str, str]:
    cached = copy_cached_document(doc, output_dir, cache)
    if cached:
        return cached

    body, final_url, headers = read_url(opener, doc.url)
    resolved_name = content_filename(final_url, headers.get("Content-Disposition"))
    filename = resolved_name or f"{sanitize_filename(doc.title)}.pdf"
    if not filename.lower().endswith(".pdf"):
        filename = f"{filename}.pdf"

    output_path = output_dir / filename
    if output_path.exists():
        return {"title": doc.title, "url": doc.url, "path": str(output_path), "status": "skipped"}

    content_type = headers.get("Content-Type", "")
    if not body.startswith(b"%PDF") and "pdf" not in content_type.lower():
        raise ValueError(f"download did not look like a PDF: {doc.url}")

    if not dry_run:
        output_path.write_bytes(body)
    cache[doc.url] = output_path
    return {"title": doc.title, "url": doc.url, "path": str(output_path), "status": "downloaded"}


def normalize_versions(values: Iterable[str]) -> list[str]:
    versions = []
    for value in values:
        if not re.fullmatch(r"\d+\.\d+", value):
            raise ValueError(f"invalid version: {value}")
        versions.append(value)
    return versions


def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("versions", nargs="*", help="Versions to download, e.g. 6.1 6.2")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=repo_root / "sources" / "specs",
        help="Root output directory. Version subfolders are created here.",
    )
    parser.add_argument("--cookies", type=Path, help="Netscape cookies.txt from a logged-in browser")
    parser.add_argument("--dry-run", action="store_true", help="List detected PDFs without writing files")
    args = parser.parse_args(argv)

    versions = normalize_versions(args.versions or DEFAULT_VERSIONS)
    opener = make_opener(args.cookies)
    cache = load_download_cache(args.output_dir)
    summary: dict[str, list[dict[str, str]]] = {}

    for version in versions:
        version_dir = args.output_dir / version
        if not args.dry_run:
            version_dir.mkdir(parents=True, exist_ok=True)

        print(f"=== Core Specification {version} ===")
        documents = parse_documents(opener, version)
        pdfs = [doc for doc in documents if doc.extension == "pdf"]
        print(f"Found {len(pdfs)} PDF links on {version_page_url(version)}")
        summary[version] = []

        for doc in pdfs:
            try:
                result = (
                    {"title": doc.title, "url": doc.url, "path": "", "status": "found"}
                    if args.dry_run
                    else download_document(opener, doc, version_dir, args.dry_run, cache)
                )
                print(f"  [{result['status'].upper()}] {doc.title}")
                summary[version].append(result)
            except (HTTPError, URLError, TimeoutError, ValueError) as exc:
                print(f"  [ERROR] {doc.title}: {exc}", file=sys.stderr)
                summary[version].append({"title": doc.title, "url": doc.url, "path": "", "status": "error"})

        if not args.dry_run:
            manifest = version_dir / "manifest.json"
            manifest.write_text(json.dumps(summary[version], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
