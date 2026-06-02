#!/usr/bin/env python3
"""
summarize_news.py — Generate news summaries using OpenAI gpt-4o-mini.

Processes articles classified as category=news from classified_articles.json.
Writes Jekyll-formatted Markdown post files to _posts/YYYY/MM/.
"""
from __future__ import annotations

import json
import logging
import os
import re
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
TEMPERATURE = 0.3
MIN_WORDS = 400
MAX_WORDS = 500

# Stage 1: extract structured facts from raw article body
EXTRACTOR_SYSTEM = (
    "You are a cold, analytical Data Extraction Engine. "
    "Your sole purpose is to ingest third-party articles and strip away all narrative flow, "
    "author bias, editorial voice, transitions, and stylistic choices. "
    "Output ONLY raw, verified facts, data points, entity definitions, and precise chronological milestones. "
    "Act as a firewall — the stylistic cadence, structure, or vocabulary of the source text must not pass through."
)

EXTRACTOR_USER = """Extract all verifiable facts from the article below. Output nothing except the structured schema.

### 1. HARD ENTITIES & ATTRIBUTES
[All specific people, companies, software tools, model names, or organizations with their exact role or context.]
- **Entity Name:** [Role / Exact Context]

### 2. DISCRETE DATAPOINTS & STATS
[Every percentage, monetary value, number, or statistical claim. Context under 15 words.]
- **[Data/Stat]:** [Exact context]

### 3. CHRONOLOGICAL MILESTONES
[All dates, historical comparisons, deadlines, or timelines.]
- **[Date/Timeframe]:** [Event or change]

### 4. DIRECT QUOTES & CLAIMS
[Verbatim quotes or specific technical claims by named individuals. Prefix unverified author opinions with [UNVERIFIED CLAIM BY SOURCE].]
- **Source Claim:** "[Quote or claim]" — Attributed to: [Name/Source]

Article title: {title}
Article body:
{body}"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
log = logging.getLogger("summarize_news")

SYSTEM_PROMPT = (
    "You are a senior tech journalist for an AI industry publication. "
    "Your audience is informed but not technical: founders, product managers, investors, "
    "engineers outside ML. Write summaries as a journalist who has read the source — "
    "never say 'the article says' or 'according to the article'."
)

USER_PROMPT = """Summarize the following AI industry article for a daily digest.

First line must be:
META: <one sentence, 120–155 characters, describing the news for search snippets. No quotes.>

Then the article body:
- Lead (2–3 sentences): what happened, who is involved, why it matters now.
- Body (3–4 paragraphs): key facts, numbers if cited, claims attributed to whom, competitive context (who else is affected), and the so-what — what changes for users, the market, or competitors. Include at least one data point or named comparison if the article provides one.
- Closing line (1 sentence): what to watch next.

Constraints:
- {min_words}–{max_words} words total (not counting the META line). Do not invent facts.
- If the source is speculative, say so explicitly.
- You MUST reference the source publication naturally within the body at least once using journalistic citation style — e.g. "according to [Publisher Name]({url})", "as [Publisher Name]({url}) reported", "[Publisher Name]({url}) noted that". Use a markdown hyperlink on the publisher name. Do not add a standalone source label or footer.

Article title: {title}
Article body:
{body}
Source publisher: {source_name}
URL: {url}"""


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def _call(client: OpenAI, system: str, user: str, temperature: float = TEMPERATURE) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return (response.choices[0].message.content or "").strip()


def summarize_one(client: OpenAI, article: dict) -> tuple[str, str]:
    """Two-stage pipeline: extract facts → write article. Returns (description, summary_body)."""
    raw_body = (article.get("body") or "")[:6000]
    title = article.get("title", "")

    # Stage 1 — extract structured facts (temperature 0 for determinism)
    extracted = _call(
        client,
        EXTRACTOR_SYSTEM,
        EXTRACTOR_USER.format(title=title, body=raw_body),
        temperature=0,
    )
    log.debug("extracted facts (%d chars) for: %s", len(extracted), title)

    # Stage 2 — write article from structured facts
    prompt = USER_PROMPT.format(
        min_words=MIN_WORDS,
        max_words=MAX_WORDS,
        title=title,
        body=extracted,
        source_name=article.get("source_name", ""),
        url=article.get("url", ""),
    )
    raw = _call(client, SYSTEM_PROMPT, prompt)
    return _parse_meta(raw)


def _parse_meta(raw: str) -> tuple[str, str]:
    """Split META: first line from the article body."""
    lines = raw.splitlines()
    description = ""
    body_start = 0
    if lines and lines[0].startswith("META:"):
        description = lines[0][5:].strip().strip('"').strip("'")
        body_start = 1
        # skip blank line after META
        if len(lines) > 1 and lines[1].strip() == "":
            body_start = 2
    summary = "\n".join(lines[body_start:]).strip()
    return description, summary


def word_count(text: str) -> int:
    return len(text.split())


def has_source_link(summary: str) -> bool:
    """Return True if the summary contains at least one markdown hyperlink."""
    return bool(re.search(r'\[.+?\]\(https?://', summary))


def build_front_matter(article: dict, summary: str, pub_date: datetime, description: str = "") -> str:
    classification = article.get("classification", {})
    categories = article.get("categories", ["news"])
    company = classification.get("company") or article.get("source_company")
    secondary = classification.get("secondary_companies", [])
    impact = classification.get("impact", "notable")
    subcategory = classification.get("subcategory", "other")
    confidence = float(classification.get("confidence", 0.0))
    source_name = article.get("source_name", "")
    source_url = article.get("url", "")

    slug = slugify(article.get("title", "untitled"))[:60]
    wc = word_count(summary)

    # Escape any double quotes in title
    title = article.get("title", "").replace('"', '\\"')

    category_yaml = categories[0] if len(categories) == 1 else str(categories)
    secondary_yaml = json.dumps(secondary) if secondary else "[]"

    company_line = f'company: "{company}"' if company else "company: null"

    desc_escaped = description.replace('"', '\\"') if description else ""

    lines = [
        "---",
        f'title: "{title}"',
        f'date: {pub_date.strftime("%Y-%m-%d %H:%M:%S")} +0000',
        f"category: {category_yaml}",
        f"subcategory: {subcategory}",
        company_line,
        f"secondary_companies: {secondary_yaml}",
        f"impact: {impact}",
        f'source_publisher: "{source_name}"',
        f'source_url: "{source_url}"',
        f"slug: {slug}",
        f"summary_word_count: {wc}",
        f"classification_confidence: {confidence:.2f}",
        f"source_truncated: {str(article.get('source_truncated', False)).lower()}",
        f'layout: post',
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

    # Avoid overwriting if already exists (idempotency)
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

    # Load seen cache to update after writing posts
    seen: dict[str, str] = {}
    if SEEN_FILE.exists():
        with SEEN_FILE.open() as f:
            seen = json.load(f)

    client = OpenAI(api_key=api_key)
    news_articles = [a for a in articles if "news" in a.get("categories", [])]
    log.info("summarizing %d news articles", len(news_articles))

    new_posts = 0
    for article in news_articles:
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

        if not has_source_link(summary):
            log.warning("summary missing source hyperlink, skipping: %s", title)
            continue

        pub_str = article.get("published", "")
        try:
            pub_date = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
        except Exception:
            pub_date = datetime.now(timezone.utc)

        path = write_post(article, summary, pub_date, description)
        seen[article["guid"]] = datetime.now(timezone.utc).isoformat()

        log.info("wrote post: %s (%d words)", path.name, wc)
        new_posts += 1

        time.sleep(0.3)

    # Persist seen cache
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with SEEN_FILE.open("w") as f:
        json.dump(seen, f, indent=2)

    log.info("wrote %d new news posts", new_posts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
