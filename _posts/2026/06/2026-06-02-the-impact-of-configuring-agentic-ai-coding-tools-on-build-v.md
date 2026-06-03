---
title: "The Impact of Configuring Agentic AI Coding Tools on Build-vs-Buy Decisions: A Study Protocol"
date: 2026-06-02 17:01:28 +0000
category: research
subcategory: agents_robotics
company: "OpenAI"
secondary_companies: ["Anthropic"]
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03907v1"
arxiv_id: "2606.03907"
authors: ["Jai Lal Lulla", "Matthias Galster", "Jie M. Zhang", "Sebastian Baltes", "Christoph Treude"]
slug: the-impact-of-configuring-agentic-ai-coding-tools-on-build-v
summary_word_count: 438
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper presents a study protocol to investigate how configuration mechanisms in agentic AI coding tools influence build-versus-buy decisions."
---

**Problem** — This work addresses a significant gap in the literature regarding the decision-making processes of agentic AI coding tools, specifically concerning their build-versus-buy choices. Despite the increasing autonomy of these tools, no controlled experimental studies have systematically examined the factors that govern these decisions. The authors highlight the importance of understanding how configuration mechanisms can influence these choices, which have implications for software security, licensing compliance, performance, and long-term maintainability. This study is presented as a pre-registered protocol, indicating that it is unreviewed and aims to establish a foundation for future empirical research.

**Method** — The authors propose a controlled experimental design to investigate the impact of various configuration mechanisms on the build-versus-buy decisions made by two prominent agentic AI coding tools: Claude Code and OpenAI Codex. The study will utilize a benchmark of staged programming tasks, each designed to present identifiable build-versus-buy scenarios. The configuration mechanisms under investigation will range from no configuration to more complex setups, including context files with soft preferences, explicit prohibitions, Skills (instructions that can be autonomously discovered), MCP-enabled library discovery tools, and permission controls. The study will measure outcomes such as the libraries selected by the tools, the disclosure of newly introduced libraries, and the completeness and accuracy of those disclosures. The authors have formulated nine pre-registered hypotheses to guide their investigation, and they plan to release the resulting benchmark dataset and analysis pipeline as a reusable artifact.

**Results** — As this paper outlines a study protocol rather than presenting empirical results, no quantitative findings or comparisons to baseline models are provided. The authors emphasize the importance of the forthcoming experiments in generating data that will elucidate the influence of configuration mechanisms on build-versus-buy decisions in agentic AI coding tools.

**Limitations** — The authors acknowledge that their study is limited to two specific agentic AI coding tools, which may not generalize to all such tools in the market. Additionally, the reliance on a pre-registered protocol means that the findings will be contingent on the successful execution of the proposed experiments. The authors do not address potential biases in the selection of programming tasks or the inherent limitations of the tools being studied.

**Why it matters** — Understanding how configuration mechanisms affect build-versus-buy decisions in agentic AI coding tools is crucial for developers and organizations aiming to optimize software development practices. The insights gained from this research could lead to improved tool configurations that enhance software security and maintainability. Furthermore, the study's findings will contribute to the broader discourse on the responsible use of AI in software engineering, as highlighted in related works on AI-assisted programming tools, as published in [arXiv cs.AI](https://arxiv.org/abs/2606.03907v1).
