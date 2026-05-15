---
title: "OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation"
date: 2026-05-14 17:57:40 +0000
category: research
subcategory: reasoning
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.15177v1"
arxiv_id: "2605.15177"
authors: ["Shang Zhou", "Wenhao Chai", "Kaiyuan Liu", "Huanzhi Mao", "Qiuyang Mang", "Jingbo Shang"]
slug: opendeepthink-parallel-reasoning-via-bradley-terry-aggregati
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of improving reasoning capabilities in large language models (LLMs) during test-time computation. Existing methodologies primarily focus on scaling the depth of reasoning by extending a single trace, which limits the exploration of diverse candidate solutions. The authors identify a significant gap in the literature regarding the selection of optimal candidates from multiple parallel reasoning traces, particularly in the absence of a reliable ground-truth verifier. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose OpenDeepThink, a novel population-based framework that employs pairwise comparisons using the Bradley-Terry model to rank candidate solutions. In each generation, the LLM evaluates random pairs of candidates, aggregating the results into a global ranking. The top-ranked candidates are preserved, while the bottom quarter is discarded. The remaining candidates undergo mutation based on natural-language critiques generated during the pairwise comparisons. This method allows for a breadth-first exploration of reasoning candidates while mitigating the selection bottleneck inherent in pointwise evaluations. The framework is designed to be model-agnostic, enabling it to transfer across various LLM architectures without the need for retuning.

**Results**  
OpenDeepThink demonstrates a significant improvement in performance, raising the effective Elo rating of the Gemini 3.1 Pro model by +405 points on the Codeforces platform after eight sequential LLM-call rounds, which took approximately 27 minutes of wall-clock time. The authors also report that the framework's gains are particularly pronounced in objectively verifiable domains on the multi-domain HLE benchmark, while performance appears to reverse in more subjective domains. The authors provide CF-73, a curated dataset of 73 expert-rated Codeforces problems, which includes International Grandmaster annotations and achieves 99% local-evaluation agreement with official verdicts.

**Limitations**  
The authors acknowledge that the performance gains are domain-dependent, with notable improvements in objective tasks but regressions in subjective evaluations. They do not address potential scalability issues related to the number of candidates evaluated or the computational overhead introduced by the pairwise comparison mechanism. Additionally, the reliance on natural-language critiques for mutation may introduce variability based on the LLM's interpretative capabilities.

**Why it matters**  
The implications of OpenDeepThink extend to enhancing the reasoning capabilities of LLMs in real-world applications, particularly in competitive programming and other domains requiring robust decision-making under uncertainty. By providing a framework that effectively balances breadth and depth in reasoning, this work paves the way for future research on population-based reasoning strategies in LLMs. The methodology could inspire further exploration into hybrid models that leverage both generative and evaluative capabilities, potentially leading to more sophisticated AI systems capable of complex problem-solving.

Authors: Shang Zhou, Wenhao Chai, Kaiyuan Liu, Huanzhi Mao, Qiuyang Mang, Jingbo Shang  
Source: arXiv:2605.15177  
URL: https://arxiv.org/abs/2605.15177v1
