---
title: "Rose-SQL: Role-State Evolution Guided Structured Reasoning for Multi-Turn Text-to-SQL"
date: 2026-05-05 13:06:51 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03720v1"
arxiv_id: "2605.03720"
authors: ["Le Zhou", "Feng Yao", "Fengcai Qiao", "Bo Xu", "Fangyuan Wang", "Boyan Xu"]
slug: rose-sql-role-state-evolution-guided-structured-reasoning-fo
summary_word_count: 395
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the underexplored application of Large Reasoning Models (LRMs) in multi-turn Text-to-SQL tasks, particularly focusing on the limitations of existing methods that either depend on unstable API-based inference or require costly fine-tuning on small-scale models. The authors present Rose-SQL as a training-free framework that leverages in-context learning to enhance context-dependent SQL parsing, filling a gap in the literature regarding efficient and effective multi-turn SQL generation.

**Method**  
Rose-SQL introduces the Role-State, a novel representation that serves as a structural blueprint to connect schema linking with SQL generation. This representation allows the model to maintain a fine-grained understanding of the evolving context throughout a conversation. The framework employs structural isomorphism checks to trace the evolution of Role-State, enabling the model to infer SQL compositions based on verified interaction trajectories. The architecture utilizes small-scale LRMs, specifically within the Qwen3 series, and operates without the need for extensive training compute or fine-tuning, relying instead on in-context learning to adapt to the conversational context.

**Results**  
Rose-SQL demonstrates significant performance improvements over various baselines. On the SParC and CoSQL benchmarks, it outperforms in-context learning baselines at the 4B parameter scale and achieves substantial gains over state-of-the-art fine-tuned models at the 8B and 14B scales. The authors report effect sizes that indicate consistent performance enhancements across different reasoning backbones, although specific numerical results are not detailed in the abstract.

**Limitations**  
The authors acknowledge that Rose-SQL's reliance on small-scale LRMs may limit its performance in highly complex SQL generation scenarios compared to larger models. Additionally, the framework's effectiveness is contingent on the quality of the initial context provided, which may not always be guaranteed in real-world applications. The paper does not address potential scalability issues when applied to larger datasets or more complex schemas, nor does it explore the implications of using Role-State in non-conversational contexts.

**Why it matters**  
The introduction of Rose-SQL has significant implications for the development of more efficient and effective systems for multi-turn Text-to-SQL tasks. By eliminating the need for extensive fine-tuning and leveraging in-context learning, this framework could lower the barrier to entry for deploying advanced SQL generation capabilities in conversational AI systems. Furthermore, the Role-State representation may inspire future research into structured reasoning in other domains, potentially leading to broader applications of LRMs in complex reasoning tasks.

Authors: Le Zhou, Feng Yao, Fengcai Qiao, Bo Xu, Fangyuan Wang, Boyan Xu  
Source: arXiv:2605.03720  
URL: https://arxiv.org/abs/2605.03720v1
