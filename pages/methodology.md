---
layout: page
title: "Methodology"
description: "How Turing Wire classifies, summarizes, and indexes AI content."
permalink: /methodology/
---

This page documents the editorial and index methodology so that outputs are reproducible and auditable.

## Editorial process

### 1. Fetch

Sources are listed in `feeds/news_sources.yml` and `feeds/research_sources.yml`. Each source declares:

- `url` — RSS/Atom/API endpoint
- `type` — `rss`, `atom`, or `api`
- `priority` — 1 (publisher), 2 (publication), 3 (aggregator)
- `requires_full_text_fetch` — whether to follow the link and scrape body text

HTTP requests honor `ETag` and `If-Modified-Since` to minimize redundant fetches. Article GUIDs are cached for 30 days to prevent republishing.

### 2. Deduplicate

Within each batch, duplicates are removed in three passes:

1. **URL match** — canonical URLs (tracking parameters stripped) are compared. When a cluster has multiple sources, the most publisher-proximate source (lowest priority number) is kept.
2. **Title cosine similarity ≥ 0.85** — using TF-IDF vectors. Aggregator rewrites of a primary source are dropped.
3. **Body prefix match** — first 200 characters of extracted text.

After deduplication, batches are capped at 50 articles per run. Excess is written to a backlog file.

### 3. Classify

Each article is analyzed to produce a structured classification:

```json
{
  "category": "news | research | stocks | skip",
  "subcategory": "<see below>",
  "company": "<string or null>",
  "secondary_companies": ["<string>"],
  "impact": "critical | major | notable | minor",
  "confidence": 0.92,
  "rationale": "one sentence"
}
```

Articles with `confidence < 0.60` are routed to a review queue and held for editorial review before publishing.

An article can be classified as both `news` and `stocks` if it is market-relevant (e.g., a major model release that moves NVDA).

**Impact rubric anchors** (in prompt verbatim):

| Level | News anchors | Research anchors |
|-------|-------------|-----------------|
| critical | Flagship model release (GPT-5, Claude 5); M&A/IPO >$1B; major regulatory action; security incident | New SOTA on GPQA/ARC-AGI/FrontierMath/SWE-bench by non-trivial margin; new paradigm comparable to Transformer |
| major | Non-flagship model from top-5 lab; $500M+ funding; senior leadership change | Meaningful eval improvement; novel methodology from DeepMind/OpenAI/Anthropic/FAIR |
| notable | Incremental features; $10–500M funding; mid-tier lab announcements | Solid incremental research; mid-tier open-weight releases |
| minor | Patch notes; UI changes; rebranding | Routine arXiv submissions without strong novelty |

When in doubt between two levels, the lower level is chosen.

### 4. Company tagging

1. Deterministic alias lookup against `feeds/company_aliases.yml` on title + first 500 chars of body.
2. If exactly one match: done.
3. If zero or 2+ matches: LLM verification call.

Articles with no identifiable primary company have `company: null` and appear in the main feed but not on company pages.

### 5. Summarize

**News** — Target 250–350 words. Structured as: Lead → Body → Closing line. No invented facts. Speculative claims flagged.

**Research** — Target 450–550 words. Structured as: Problem → Method → Results → Limitations → Why it matters. Technical audience, no softening of jargon.

---

## AI Index {#ai-index}

The **TW AI Index** is an equal-weighted index of {{ site.data.tickers.tickers | size }} AI-related equities.

### Formula

```
indexed_i(t) = price_i(t) / price_i(base) × 100

index(t) = mean( indexed_i(t) for all i in universe )
```

Each ticker is individually indexed to its base-date closing price. The mean of these indexed values is the index level. Equal-weighting means no single ticker dominates regardless of market cap.

### Base date

`{{ site.data.ai_index_history.base_date | default: site.ai_index_base_date }}`

Base level: 100.

### Universe

See the [Sources](/sources/) page for the full ticker list with sectors and inclusion dates.

Tickers are added when a company becomes relevant to the AI ecosystem. When added after the base date, the ticker is assigned its price on the inclusion date as its base — it enters the index at level 100 from that point. The mean is computed over all currently-included tickers.

### Data source

Finnhub (free tier). Quotes are delayed up to 15 minutes during market hours. Close prices are captured at the 21:00 UTC workflow run.

### Reproducibility

The full computation is in `scripts/compute_ai_index.py`. Base prices are stored in `_data/ai_index_history.json` (committed to the `main` branch). Anyone can clone the repository and recompute the index from the stored base prices.

---

## Limitations and known issues

- **arXiv flood risk**: On days with many high-profile preprints, the 30/day cap per category may miss some papers. The 50-article-per-run hard cap means very active days will have backlog.
- **Paywalled sources**: For sources marked `source_truncated: true`, summaries are based on the abstract/headline only and may miss important context.
- **Impact calibration drift**: The LLM assigns impact per-article without awareness of the day's news cycle. In slow news weeks, articles may be inflated to "major"; in busy weeks some may be underrated. Spot-checking is done periodically.
- **Company tagging accuracy**: The alias lookup is deterministic but not exhaustive. Uncommon company names or newly founded organizations may be missed until aliases are added.
