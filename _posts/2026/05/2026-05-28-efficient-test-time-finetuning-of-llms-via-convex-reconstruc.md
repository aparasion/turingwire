---
title: "Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching"
date: 2026-05-28 17:59:01 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30337v1"
arxiv_id: "2605.30337"
authors: ["Alaa Khamis", "Alaa Maalouf"]
slug: efficient-test-time-finetuning-of-llms-via-convex-reconstruc
summary_word_count: 429
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing test-time finetuning (TTFT) methods for large language models (LLMs), which struggle with the trade-off between speed and quality. Current approaches often rely on fast retrieval mechanisms that can lead to redundancy, while more sophisticated diversity-aware selection methods incur significant computational costs per query. The authors propose HullFT, a novel TTFT framework that aims to optimize both retrieval efficiency and model adaptation speed. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
HullFT employs a geometric approach to TTFT by representing the query embedding as a sparse convex combination of a limited number of training sequences. This is achieved through projection-free Frank-Wolfe optimization, which efficiently identifies a support set of relevant and diverse examples. The fractional convex weights derived from this process are then transformed into an exact integer multiset for finetuning via a geometric integerization procedure. This transformation results in repeated examples that facilitate Gradient Reuse, allowing the amortization of forward-backward computations across multiple finetuning iterations. The authors detail the architecture and optimization techniques used, although specific training compute requirements are not disclosed.

**Results**  
HullFT demonstrates significant improvements over existing TTFT methods on benchmark tasks. The authors report a reduction in bits-per-byte, indicating enhanced efficiency in model adaptation. While specific numerical results are not provided in the abstract, the paper claims that HullFT achieves lower total runtime compared to state-of-the-art TTFT techniques, suggesting a favorable quality-efficiency trade-off. The authors compare HullFT against named baselines, although detailed performance metrics and effect sizes are expected to be elaborated in the full paper.

**Limitations**  
The authors acknowledge that HullFT's reliance on a geometric approach may introduce complexity in the integerization process, which could limit its applicability in certain scenarios. Additionally, the method's performance may vary depending on the characteristics of the training data and the specific tasks at hand. The paper does not address potential scalability issues when applied to very large datasets or the impact of model size on the efficiency gains. Furthermore, as a preprint, the findings have yet to be validated through peer review.

**Why it matters**  
HullFT has significant implications for the deployment of LLMs in real-time applications where rapid adaptation to user queries is essential. By improving the efficiency of TTFT, this work could enable more responsive AI systems capable of fine-tuning on-the-fly without incurring prohibitive computational costs. The techniques introduced may also inspire further research into geometric optimization methods in machine learning, particularly in the context of adaptive learning and online model updates.

Authors: Alaa Khamis, Alaa Maalouf  
Source: arXiv:2605.30337  
URL: [https://arxiv.org/abs/2605.30337v1](https://arxiv.org/abs/2605.30337v1)
