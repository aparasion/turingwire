---
title: "Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools"
date: 2026-06-01 16:53:19 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02483v1"
arxiv_id: "2606.02483"
authors: ["Bardia Mohammadi", "Lars Klein", "Akhil Arora", "Laurent Bindschaedler"]
slug: ghost-tool-calls-issue-time-privacy-for-speculative-agent-to
summary_word_count: 471
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces Speculative Tool Privacy Contracts to mitigate privacy risks from speculative tool calls in language agents, addressing user intent leakage."
---

**Problem**  
The paper addresses a significant gap in the privacy of tool-augmented language agents, specifically the issue of "ghost tool calls." These calls are speculative invocations made by agents to reduce latency, which inadvertently disclose inferred user intent to external services before the agent commits to the action. This problem is particularly pressing as it remains unaddressed in existing literature, with no prior work focusing on the implications of timing in speculative tool calls. The authors highlight that conventional privacy measures, such as commit-time cleanup and access-control allow-lists, fail to mitigate the risks associated with these premature disclosures. This work is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors propose a novel runtime abstraction termed Speculative Tool Privacy Contracts, which treats the observation of speculative calls as a first-class effect, separate from state mutation. This abstraction allows for the implementation of various policies that can modify or suppress the arguments or destinations of speculative calls before they are dispatched. The authors developed a prototype runtime to evaluate the effectiveness of twelve different privacy policies across three distinct corpora. The evaluation focuses on how these policies can alter the information that external observers can infer about user intent based on the speculative calls made by the agent.

**Results**  
The evaluation reveals that speculative dispatch significantly increases the potential for observers to infer user intent. The authors demonstrate that traditional post-hoc privacy measures, such as read-only restrictions and access-control allow-lists, do not effectively reduce this inference risk. In contrast, the issue-time policies that modify or suppress the speculative call's arguments or destination before dispatch show a marked reduction in the leakage of user intent. While specific numerical results are not disclosed in the abstract, the qualitative findings suggest a clear advantage for the proposed issue-time policies over existing methods.

**Limitations**  
The authors acknowledge that their approach may introduce additional complexity in the design and implementation of language agents, as it requires careful consideration of the timing and nature of speculative calls. Furthermore, the evaluation is limited to three corpora, which may not fully represent the diversity of use cases in real-world applications. The paper does not address potential performance trade-offs associated with implementing these privacy contracts, nor does it explore the implications of these policies on the overall efficiency of tool-augmented agents.

**Why it matters**  
This work has significant implications for the design of privacy-preserving mechanisms in AI systems, particularly those that utilize speculative execution to enhance performance. By introducing Speculative Tool Privacy Contracts, the authors provide a framework that can be leveraged to improve user privacy in language agents, thereby fostering greater trust in AI applications. The findings underscore the necessity of addressing timing-related privacy issues, which could inform future research and development in the field of AI privacy, as published in [arXiv cs.AI](https://arxiv.org/abs/2606.02483v1).
