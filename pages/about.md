---
layout: page
title: "About"
description: "What Turing Wire is, who it's for, and how to get the most out of it."
permalink: /about/
---

Turing Wire is an automated AI news aggregator and research briefing — tracking labs, hardware, papers, and markets in near-realtime. It surfaces, classifies, and summarizes content from across the AI ecosystem so you spend less time hunting and more time building.

## Who it's for

**The AI-aware practitioner.** If you're an engineer, ML researcher, or technical PM working in or adjacent to AI, Turing Wire is built for your daily rhythm. You follow lab releases because they change what you can build. You scan arXiv selectively but can't read 30 abstracts a day. You care about whether TSMC's yield issues will affect GPU availability in Q3. You want signal, not volume.

The three feeds serve three distinct needs:

- **News** — What shipped, who got funded, what policy is coming. Organized by impact (Critical → Minor) so you can triage at a glance. Subscribe to the [Major+ RSS feed](/feed-major.xml) to get only the stuff worth stopping for.
- **Research** — Paper summaries structured for practitioners: problem, method, results, and *why it matters for what you're building*. Covers arXiv, Nature Machine Intelligence, JMLR, and major conference proceedings. Each summary links directly to the original and, where available, to the arXiv abstract.
- **AIStocks** — Semiconductor supply, hyperscaler capex, and enterprise AI deployment health — framed as ecosystem signals, not trading tips. When NVDA earnings disappoint or TSMC cuts guidance, it tells you something about where the compute supply chain is heading.

## What it isn't

Turing Wire doesn't break news — it synthesizes what labs, publications, and researchers publish. It is not a primary source. Every summary links prominently to the original. For important topics, read the original.

It is also not financial advice. See the [disclaimer](/disclaimer/).

## How to use it

**Daily briefing:** The homepage shows the last three days grouped by date. The impact rating and subcategory let you decide in two seconds whether to click through.

**Track a company:** Every article is tagged by company. Use the [Companies directory](/companies/) or the tags in any article to see everything from a given lab or vendor.

**Stay current via RSS:** Multiple feeds are available — [all posts](/feed.xml), [Major+ only](/feed-major.xml), [News only](/news/feed.xml), and [Research only](/research/feed.xml). The Major+ feed is the lowest-noise option for a busy inbox.

**Search:** Full-text search across all articles is available at [/search/](/search/) or via the `/` shortcut anywhere on the site.

## Who maintains it

This is a personal project. The pipeline is fully automated — articles are fetched, classified, and summarized hourly by GPT-4o-mini. A human reviews the output periodically. If you spot an error or want to suggest a source, file an issue on GitHub.
