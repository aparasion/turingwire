---
layout: page
title: "About"
description: "What Turing Wire is, who it's for, and how to get the most out of it."
permalink: /about/
---

Turing Wire is a dedicated news and research publication covering the AI ecosystem — tracking labs, hardware, papers, and markets in near-realtime. It surfaces, classifies, and distills content from across the field so you spend less time hunting and more time building.

## Who it's for

**The AI-aware practitioner.** If you're an engineer, ML researcher, or technical PM working in or adjacent to AI, Turing Wire is built for your daily rhythm. You follow lab releases because they change what you can build. You scan arXiv selectively but can't read 30 abstracts a day. You care about whether TSMC's yield issues will affect GPU availability in Q3. You want signal, not volume.

The feeds and tools serve distinct needs:

- **News** — What shipped, who got funded, what policy is coming. Organized by impact (Critical → Minor) so you can triage at a glance. Subscribe to the [Major+ RSS feed](/feed-major.xml) to get only the stuff worth stopping for.
- **Research** — Paper summaries structured for practitioners: problem, method, results, and *why it matters for what you're building*. Covers arXiv, Nature Machine Intelligence, JMLR, and major conference proceedings. Each summary links directly to the original and, where available, to the arXiv abstract.
- **AIStocks** — Semiconductor supply, hyperscaler capex, and enterprise AI deployment health — framed as ecosystem signals, not trading tips. When NVDA earnings disappoint or TSMC cuts guidance, it tells you something about where the compute supply chain is heading.
- **Stories** — Multi-source synthesis of evolving events. When a topic develops across multiple articles over days, a Story stitches the sources together at the claim level: each claim is tagged as corroborated, disputed, or single-source, with links back to every supporting or contradicting article. A trust score reflects how well the claims across sources agree. Stories are generated automatically and updated as new coverage arrives.
- **Missions** — Persistent tracking goals you define yourself. Specify companies, keywords, and a minimum impact level; Missions reruns against the full index on every visit and surfaces only items new since you last checked. Results can be exported as JSON or bookmarked as a pinnable URL. Missions also supports browser notifications for critical matches.

## Intelligence

The **Intelligence** section — [Stories](/stories/) and [Missions](/missions/) — is where Turing Wire goes beyond aggregation into active synthesis and tracking.

**Stories** exist because AI coverage is rarely a single event. A model launch becomes a week-long story as benchmarks are contested, safety evaluations are released, and competitors respond. Rather than leaving you to manually connect ten articles, a Story does it: it clusters related sources, extracts discrete claims, checks each claim across all sources, and presents the result with full provenance. Disagreements between sources are surfaced explicitly — you see what's settled and what's still contested.

**Missions** exist because most practitioners care deeply about a narrow slice of the field. A Mission lets you express that directly: "Show me everything about Anthropic enterprise deals above Major impact" or "Track inference cost across any lab, keyword: tokens per second." The Mission reruns automatically, remembers what you've already seen, and notifies you when something new matches. You can run multiple Missions in parallel, export their results, or share a Mission URL with a colleague.

## What it isn't

Turing Wire doesn't break news — it synthesizes what labs, publications, and researchers publish. It is not a primary source. Every summary links prominently to the original. For important topics, read the original.

Story synthesis and Mission matching are automated processes. They can miss nuance, misclassify claims, or surface false positives. Trust scores and claim-status labels are heuristics, not editorial verdicts.

It is also not financial advice. See the [disclaimer](/disclaimer/).

## How to use it

**Daily briefing:** The homepage shows the last three days grouped by date. The impact rating and subcategory let you decide in two seconds whether to click through.

**Follow an evolving event:** Check [Stories](/stories/) when a topic is developing across multiple sources. Each story card shows source count, claim count, and trust score so you can gauge depth before clicking in.

**Set up a Mission:** Go to [Missions](/missions/), name your goal, add companies or keywords, pick a minimum impact level, and save. Come back anytime — or enable browser notifications — to see what's new since your last visit.

**Track a company:** Every article is tagged by company. Use the [Companies directory](/companies/) or the tags in any article to see everything from a given lab or vendor.

**Stay current via RSS:** Multiple feeds are available — [all posts](/feed.xml), [Major+ only](/feed-major.xml), [News only](/news/feed.xml), and [Research only](/research/feed.xml). The Major+ feed is the lowest-noise option for a busy inbox.

**Search:** Full-text search across all articles is available at [/search/](/search/) or via the `/` shortcut anywhere on the site.

## Who maintains it

This is a personal project by a practitioner in the AI field. Articles are fetched from primary sources, classified by topic and impact, and distilled into structured summaries on a continuous basis. If you spot an error, want to suggest a source, or have any other question, use the [contact form](/contact/).

## Editorial methodology

Every article on Turing Wire is derived from a primary source. The editorial pipeline works as follows:

**Sources monitored.** The pipeline tracks RSS feeds and structured outputs from: arXiv (cs.AI, cs.LG, cs.CL, stat.ML), Nature Machine Intelligence, JMLR, NeurIPS/ICML/ICLR proceedings, TechCrunch, VentureBeat, The Information, Reuters Technology, MIT Technology Review, IEEE Spectrum, and approximately 30 additional specialised AI publications. All monitored sources are listed on the [Sources page](/sources/).

**Classification.** Each incoming article is classified by category (news or research), subcategory (e.g. model release, funding, regulation, inference optimisation), primary company, impact level (Critical → Minor), and confidence score. Classification is performed automatically and spot-checked.

**Summarisation.** News summaries are 400–500 words and follow a fixed structure: lead (what happened, who, why now), body (key facts, numbers, competitive context), and a closing forward-looking sentence. Research summaries are 450–550 words structured as: Problem, Method, Results, Limitations, Why it matters. Both formats are generated by a large language model guided by a fixed editorial prompt — they are AI-assisted drafts, not human-written prose.

**Source integrity.** Every summary cites its primary source within the body using standard journalistic attribution ("according to [Publisher]", "as [Publisher] reported"). Summaries do not invent claims or statistics not present in the source. If the source is a preprint, this is stated explicitly.

**Deduplication.** Duplicate coverage of the same event from multiple sources is merged or suppressed. A 30-day deduplication window prevents repeat coverage of recurring stories.

**Corrections.** If a summary contains an error, contact us via the [contact form](/contact/). Corrections are applied promptly and the publication date is updated to reflect the revision.

**What this publication is not.** Turing Wire does not break news, conduct original reporting, or serve as a primary source. For any important decision — technical, financial, or otherwise — read the original source linked in every article.
