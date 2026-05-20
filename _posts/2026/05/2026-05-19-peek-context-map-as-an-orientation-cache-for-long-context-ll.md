---
title: "PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents"
date: 2026-05-19 14:51:32 +0000
category: research
subcategory: efficiency_inference
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.19932v1"
arxiv_id: "2605.19932"
authors: ["Zhuohan Gu", "Qizheng Zhang", "Omar Khattab", "Samuel Madden"]
slug: peek-context-map-as-an-orientation-cache-for-long-context-ll
summary_word_count: 464
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of large language model (LLM) agents to effectively manage and utilize long and recurring external contexts, such as document corpora and code repositories. Existing methods either focus on preserving the agent's trajectory, provide passive access to raw materials, or employ task-level strategies. However, they fail to maintain reusable orientation knowledge about the context itself, which is crucial for repeated same-context workloads. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce PEEK, a system designed to cache and maintain orientation knowledge through a context map—a compact, constant-sized artifact embedded in the agent's prompt. This context map provides persistent insights into the external context, including its contents, organization, and historically useful entities. PEEK employs a programmable cache policy consisting of three main components:  
1. **Distiller**: Extracts transferable knowledge from inference-time signals.  
2. **Cartographer**: Translates the extracted knowledge into structured edits for the context map.  
3. **Evictor**: Implements a priority-based mechanism to enforce a fixed token budget, ensuring efficient use of the context map.  
The architecture is designed to enhance long-context reasoning and information aggregation while minimizing computational costs.

**Results**  
PEEK demonstrates significant improvements over strong baselines, achieving enhancements of 6.3-34.0% in performance metrics while utilizing 93-145 fewer iterations and incurring 1.7-5.8x lower costs compared to the state-of-the-art prompt-learning framework, ACE. In terms of context learning, PEEK shows a 6.0-14.0% increase in solving rate and a 7.8-12.1% improvement in rubric accuracy, all at a 1.4x lower cost than ACE. These performance gains are consistent across various LLMs and agent architectures, including OpenAI Codex, indicating the robustness of the approach.

**Limitations**  
The authors acknowledge that while PEEK improves efficiency and accuracy, it may still be limited by the fixed token budget imposed by the Evictor, which could restrict the amount of context retained. Additionally, the reliance on inference-time signals for knowledge extraction may introduce variability based on the specific tasks or contexts encountered. The paper does not address potential scalability issues when applied to extremely large contexts or the implications of the context map's size on the overall model performance.

**Why it matters**  
The introduction of PEEK and its context map mechanism has significant implications for the development of LLM agents that operate in environments requiring long-term context management. By enabling agents to maintain reusable orientation knowledge, PEEK enhances their ability to interact with recurring external contexts more accurately and efficiently. This advancement could lead to improved performance in various applications, including document analysis, code generation, and other tasks that necessitate a deep understanding of extensive contextual information. The findings encourage further exploration of context management strategies in LLMs, potentially influencing future research directions in the field.

Authors: Zhuohan Gu, Qizheng Zhang, Omar Khattab, Samuel Madden  
Source: arXiv:2605.19932  
URL: [https://arxiv.org/abs/2605.19932v1](https://arxiv.org/abs/2605.19932v1)
