---
title: "Does Code Cleanliness Affect Coding Agents? A Controlled Minimal-Pair Study"
date: 2026-05-19 16:06:26 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20049v1"
arxiv_id: "2605.20049"
authors: ["Priyansh Trivedi", "Olivier Schmitt"]
slug: does-code-cleanliness-affect-coding-agents-a-controlled-mini
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the evaluation of autonomous coding agents, specifically regarding the impact of code cleanliness on their performance. While existing literature primarily focuses on task completion rates with fixed codebases, it neglects the influence of structural and stylistic quality of the code on an agent's ability to navigate and modify it. The authors propose a controlled experimental framework to isolate the effects of code cleanliness from the inherent capabilities of the coding agents.

**Method**  
The authors introduce a novel evaluation protocol based on minimal pairs, which are repositories that are matched on architecture, dependencies, and external behavior but differ in terms of static-analysis rule violations and cognitive complexity. They constructed six pairs of repositories, each evaluated through 33 tasks designed to assess the agents' performance. The evaluation involved two agent pipelines: one that degrades a clean repository and another that cleans a messy one. The coding agent used for the experiments is Claude Code, and the evaluation was conducted over 660 trials. The metrics of interest include pass rates, token usage, and file revisitations, providing a comprehensive view of the agents' operational efficiency in relation to code cleanliness.

**Results**  
The results indicate that code cleanliness does not significantly affect the pass rate of the coding agent, as the completion rates remained consistent across both clean and messy codebases. However, the operational footprint of the agent was notably impacted; agents working with cleaner code utilized 7 to 8% fewer tokens and exhibited a 34% reduction in file revisitations. These findings suggest that while the ability to complete tasks may not be influenced by code cleanliness, the efficiency and resource consumption of coding agents are significantly improved when operating on cleaner code.

**Limitations**  
The authors acknowledge that their study is limited to the specific coding agent (Claude Code) and the particular tasks designed for the evaluation. The generalizability of the findings to other coding agents or more complex coding tasks remains uncertain. Additionally, the study does not explore the long-term effects of code cleanliness on agent performance or the potential for different coding paradigms to influence results. The minimal pair approach, while effective for isolating variables, may not capture the full spectrum of real-world coding scenarios.

**Why it matters**  
This research underscores the continued relevance of traditional software maintainability principles in the context of AI-driven development. The findings suggest that code cleanliness is a critical factor influencing the computational cost and navigational efficiency of coding agents, alongside model choice, harness, and prompting strategies. As autonomous coding agents become more prevalent, understanding the implications of code quality on their performance will be essential for optimizing their deployment in software development workflows.

Authors: Priyansh Trivedi, Olivier Schmitt  
Source: arXiv:2605.20049  
URL: [https://arxiv.org/abs/2605.20049v1](https://arxiv.org/abs/2605.20049v1)
