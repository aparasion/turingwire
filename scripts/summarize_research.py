#!/usr/bin/env python3
"""
summarize_research.py — Generate research summaries using OpenAI gpt-4o-mini.

Processes articles classified as category=research from classified_articles.json.
Uses structured headings: Problem, Method, Results, Limitations, Why it matters.
"""
from __future__ import annotations

import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI
from slugify import slugify
from tenacity import retry, stop_after_attempt, wait_exponential

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "_data"
CLASSIFIED_FILE = DATA_DIR / "classified_articles.json"
SEEN_FILE = DATA_DIR / "seen_articles.json"

MODEL = "gpt-4o-mini"
TEMPERATURE = 0.0
MIN_WORDS = 450
MAX_WORDS = 550

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
log = logging.getLogger("summarize_research")

SYSTEM_PROMPT = (
    "You are an ML research engineer with strong technical writing skills. "
    "Summarize papers for engineers and researchers deciding whether to read the full work. "
    "Use precise terminology. Do not soften jargon for a general audience."
)

USER_PROMPT = """Summarize the following AI research paper.

First line must be:
META: <one sentence, 120–155 characters, describing the paper's contribution for search snippets. No quotes.>

Then use these exact Markdown headings:

**Problem** — what gap in capability or literature does this address?
**Method** — the core technical contribution. Be specific: architecture, loss, data, training compute if disclosed.
**Results** — headline numbers vs named baselines on named benchmarks. Effect sizes, not just p-values.
**Limitations** — what the authors flag, plus any obvious ones they don't.
**Why it matters** — implications for downstream work. This section MUST include a natural contextual citation linking to the source: e.g. "as published in [{source_name}]({url})" or "available on [arXiv]({url})".

Constraints:
- {min_words}–{max_words} words total across all sections (not counting the META line).
- Use precise ML terminology. This is for an expert audience.
- If the work is preprint and unreviewed, state that in the Problem section.
- Do not add a standalone Authors/Source footer block — author names belong in the Method or Problem section if relevant.

Paper title: {title}
Authors: {authors}
Abstract / body:
{body}
Source: {source_name}
URL: {url}
arXiv ID: {arxiv_id}"""


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def summarize_one(client: OpenAI, article: dict) -> tuple[str, str]:
    """Returns (description, summary_body)."""
    body = (article.get("body") or "")[:5000]
    authors_str = ", ".join(article.get("authors", [])[:8])
    if len(article.get("authors", [])) > 8:
        authors_str += " et al."

    prompt = USER_PROMPT.format(
        min_words=MIN_WORDS,
        max_words=MAX_WORDS,
        title=article.get("title", ""),
        authors=authors_str or "unknown",
        body=body,
        source_name=article.get("source_name", ""),
        url=article.get("url", ""),
        arxiv_id=article.get("arxiv_id", ""),
    )
    response = client.chat.completions.create(
        model=MODEL,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    raw = (response.choices[0].message.content or "").strip()
    return _parse_meta(raw)


def _parse_meta(raw: str) -> tuple[str, str]:
    """Split META: first line from the article body."""
    lines = raw.splitlines()
    description = ""
    body_start = 0
    if lines and lines[0].startswith("META:"):
        description = lines[0][5:].strip().strip('"').strip("'")
        body_start = 1
        if len(lines) > 1 and lines[1].strip() == "":
            body_start = 2
    summary = "\n".join(lines[body_start:]).strip()
    return description, summary


def word_count(text: str) -> int:
    return len(text.split())


def build_front_matter(article: dict, summary: str, pub_date: datetime, description: str = "") -> str:
    classification = article.get("classification", {})
    company = classification.get("company") or article.get("source_company")
    secondary = classification.get("secondary_companies", [])
    impact = classification.get("impact", "notable")
    subcategory = classification.get("subcategory", "other")
    confidence = float(classification.get("confidence", 0.0))
    source_name = article.get("source_name", "")
    source_url = article.get("url", "")
    arxiv_id = article.get("arxiv_id", "")
    authors = article.get("authors", [])

    slug = slugify(article.get("title", "untitled"))[:60]
    wc = word_count(summary)
    title = article.get("title", "").replace('"', '\\"')
    secondary_yaml = json.dumps(secondary) if secondary else "[]"
    company_line = f'company: "{company}"' if company else "company: null"
    authors_yaml = json.dumps(authors[:6])

    desc_escaped = description.replace('"', '\\"') if description else ""

    lines = [
        "---",
        f'title: "{title}"',
        f'date: {pub_date.strftime("%Y-%m-%d %H:%M:%S")} +0000',
        f"category: research",
        f"subcategory: {subcategory}",
        company_line,
        f"secondary_companies: {secondary_yaml}",
        f"impact: {impact}",
        f'source_publisher: "{source_name}"',
        f'source_url: "{source_url}"',
        f'arxiv_id: "{arxiv_id}"',
        f"authors: {authors_yaml}",
        f"slug: {slug}",
        f"summary_word_count: {wc}",
        f"classification_confidence: {confidence:.2f}",
        f"source_truncated: false",
        f"layout: post",
    ]
    if desc_escaped:
        lines.append(f'description: "{desc_escaped}"')
    lines.append("---")
    return "\n".join(lines)


def write_post(article: dict, summary: str, pub_date: datetime, description: str = "") -> Path:
    year = pub_date.strftime("%Y")
    month = pub_date.strftime("%m")
    date_prefix = pub_date.strftime("%Y-%m-%d")
    slug = slugify(article.get("title", "untitled"))[:60]
    filename = f"{date_prefix}-{slug}.md"

    post_dir = ROOT / "_posts" / year / month
    post_dir.mkdir(parents=True, exist_ok=True)
    post_path = post_dir / filename

    if post_path.exists():
        log.debug("post already exists, skipping: %s", post_path)
        return post_path

    front_matter = build_front_matter(article, summary, pub_date, description)
    content = f"{front_matter}\n\n{summary}\n"

    with post_path.open("w") as f:
        f.write(content)

    return post_path


def main() -> int:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        log.error("OPENAI_API_KEY not set")
        return 1

    if not CLASSIFIED_FILE.exists():
        log.error("classified articles file not found: %s", CLASSIFIED_FILE)
        return 1

    with CLASSIFIED_FILE.open() as f:
        articles = json.load(f)

    seen: dict[str, str] = {}
    if SEEN_FILE.exists():
        with SEEN_FILE.open() as f:
            seen = json.load(f)

    client = OpenAI(api_key=api_key)
    research_articles = [a for a in articles if "research" in a.get("categories", [])]
    log.info("summarizing %d research articles", len(research_articles))

    new_posts = 0
    for article in research_articles:
        title = article.get("title", "")
        try:
            description, summary = summarize_one(client, article)
        except Exception as exc:
            log.warning("summarization failed for '%s': %s", title, exc)
            continue

        wc = word_count(summary)
        if wc < 100:
            log.warning("summary too short (%d words), skipping: %s", wc, title)
            continue

        pub_str = article.get("published", "")
        try:
            pub_date = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
        except Exception:
            pub_date = datetime.now(timezone.utc)

        path = write_post(article, summary, pub_date, description)
        seen[article["guid"]] = datetime.now(timezone.utc).isoformat()

        log.info("wrote research post: %s (%d words)", path.name, wc)
        new_posts += 1
        time.sleep(0.3)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with SEEN_FILE.open("w") as f:
        json.dump(seen, f, indent=2)

    log.info("wrote %d new research posts", new_posts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
