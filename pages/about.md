---
layout: page
title: "About"
description: "What Turing Wire is, how it works, and who it's for."
permalink: /about/
---

Turing Wire is an automated news aggregator focused on artificial intelligence — labs, hardware, research, and markets. It publishes near-realtime summaries of articles from across the AI ecosystem, organized into three feeds and tagged by company.

## What it covers

**News** — Product launches, model releases, funding rounds, policy and regulation, safety and alignment, infrastructure and compute, partnerships, and editorial commentary from leading AI publications.

**Research** — Paper summaries from arXiv (cs.AI, cs.LG, cs.CL, cs.CV, cs.NE), Nature Machine Intelligence, JMLR, and major conference proceedings. Each summary uses a structured format: Problem, Method, Results, Limitations, and Why it matters.

**AIStocks** — A dashboard tracking 28 AI-adjacent equities including semiconductor manufacturers, hyperscalers, and enterprise AI companies. Includes the TW AI Index, a custom equal-weighted index of the full universe.

## How it works

Every hour, a pipeline:

1. **Fetches** RSS/Atom feeds and arXiv API results from ~40 sources.
2. **Deduplicates** articles by URL, title similarity, and body prefix to avoid publishing the same story multiple times.
3. **Classifies** each article via OpenAI gpt-4o-mini — assigning category, subcategory, impact level, and company tags.
4. **Summarizes** news articles in 250–350 words and research papers in 450–550 words using structured templates.
5. **Publishes** new posts to this site via GitHub Actions.

Stock data updates every 15 minutes during US market hours via Finnhub. The pipeline code is open-source at [github.com/aparasion/turingwire](https://github.com/aparasion/turingwire).

## Impact levels

Articles are rated on a four-level scale:

- **Critical** — market-moving, field-shifting, or governance-changing events.
- **Major** — significant for industry watchers but not field-changing.
- **Notable** — worth covering; incremental progress.
- **Minor** — archived for completeness; not prominently surfaced.

The homepage and feed defaults surface Critical and Major items first.

## What it isn't

Turing Wire doesn't break news — it synthesizes what labs, publications, and researchers publish. It is not a primary source. Every summary links prominently to the original. For important topics, read the original.

It is also not financial advice. See the [disclaimer](/disclaimer/).

## Who maintains it

This is a personal project. The pipeline is fully automated; a human reviews the output periodically. If you spot an error, a missing source, or a miscategorized article, [open an issue on GitHub](https://github.com/aparasion/turingwire/issues).
