---
title: "MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems"
date: 2026-05-07 17:35:26 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06623v1"
arxiv_id: "2605.06623"
authors: ["Zhexuan Wang", "Xuebo Liu", "Li Wang", "Zifei Shan", "Yutong Wang", "Zhenxi Song"]
slug: maspo-joint-prompt-optimization-for-llm-based-multi-agent-sy
summary_word_count: 436
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of optimizing role-specific prompts in large language model (LLM)-based multi-agent systems (MAS), a gap in the literature that has not been adequately explored. The authors highlight the misalignment between local agent objectives and the overarching goals of the system, which complicates the joint optimization of prompts across interacting agents. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose MASPO, a framework that iteratively refines prompts for multiple agents through a joint evaluation mechanism. This mechanism evaluates prompts based on their effectiveness in facilitating downstream success for subsequent agents, rather than solely on local validity. This approach allows for a more holistic optimization process that does not depend on ground-truth labels. MASPO employs a data-driven evolutionary beam search algorithm to efficiently explore the high-dimensional space of prompts, optimizing them in a manner that aligns local interactions with global system performance. The architecture and specific training compute details are not disclosed, but the focus on evolutionary search suggests a computationally intensive optimization process.

**Results**  
MASPO was empirically evaluated across six diverse tasks, demonstrating a consistent performance improvement over existing state-of-the-art prompt optimization methods. The framework achieved an average accuracy improvement of 2.9 percentage points compared to baseline methods, although specific baseline models and benchmarks are not named in the summary. This improvement indicates a significant enhancement in the effectiveness of prompt optimization in MAS, suggesting that the joint evaluation mechanism is a key contributor to the observed performance gains.

**Limitations**  
The authors acknowledge that the lack of reliance on ground-truth labels may limit the applicability of MASPO in scenarios where such labels are available and could enhance performance. Additionally, the paper does not discuss the scalability of the evolutionary beam search method in larger or more complex multi-agent environments, nor does it address potential computational overheads associated with the iterative refinement process. The generalizability of the results across different types of tasks and agent configurations is also not explored.

**Why it matters**  
The implications of this work are significant for the development of more effective multi-agent systems that leverage LLMs. By providing a framework for joint prompt optimization, MASPO can enhance the collaborative capabilities of agents in complex tasks, potentially leading to advancements in areas such as automated negotiation, cooperative problem-solving, and interactive AI systems. The methodology could serve as a foundation for future research aimed at improving agent coordination and performance in multi-agent environments, particularly in scenarios where traditional optimization techniques fall short.

Authors: Zhexuan Wang, Xuebo Liu, Li Wang, Zifei Shan, Yutong Wang, Zhenxi Song, Min Zhang  
Source: arXiv:2605.06623  
URL: https://arxiv.org/abs/2605.06623v1
