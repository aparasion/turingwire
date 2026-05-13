---
title: "ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging"
date: 2026-05-12 17:14:04 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12419v1"
arxiv_id: "2605.12419"
authors: ["Neha Verma", "Nikhil Mehta", "Shao-Chuan Wang", "Naijing Zhang", "Alicia Tsai", "Li Wei"]
slug: orbit-preserving-foundational-language-capabilities-in-genre
summary_word_count: 424
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the issue of catastrophic forgetting in large language models (LLMs) during fine-tuning for specific tasks, particularly in the context of Generative Retrieval (GenRetrieval). Despite advancements in LLMs, fine-tuning often leads to a significant loss of foundational language capabilities. The authors highlight that this forgetting occurs rapidly and is correlated with the distance between the fine-tuned model parameters and the original model parameters. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce ORBIT, a novel approach designed to mitigate catastrophic forgetting during GenRetrieval fine-tuning. ORBIT actively monitors the distance between the fine-tuned model weights and the original model weights. When this distance exceeds a predefined threshold, ORBIT employs a weight averaging strategy to constrain model drift. This method allows the model to retain its foundational capabilities while adapting to the specific GenRetrieval task. The architecture details, loss functions, and specific training compute requirements are not disclosed in the abstract, but the focus is on the dynamic adjustment of model weights based on their distance from the original parameters.

**Results**  
ORBIT demonstrates superior performance compared to several baseline methods, including common continual learning approaches and other regularization techniques that utilize weight averaging. The authors report that ORBIT retains substantial text and retrieval performance, although specific headline numbers and effect sizes against named baselines on established benchmarks are not provided in the abstract. The results suggest that ORBIT effectively balances the retention of foundational language capabilities with the adaptation required for GenRetrieval tasks.

**Limitations**  
The authors acknowledge that while ORBIT shows promise in preserving foundational capabilities, the approach may still be sensitive to the choice of the distance threshold and the specific weight averaging strategy employed. Additionally, the paper does not address the scalability of ORBIT to larger models or more complex tasks beyond GenRetrieval. There is also no discussion of the computational overhead introduced by the distance tracking mechanism, which could impact training efficiency.

**Why it matters**  
The implications of this work are significant for the field of natural language processing and machine learning, particularly in applications where LLMs are fine-tuned for specific tasks. By providing a method to retain foundational language capabilities, ORBIT could enhance the robustness and versatility of LLMs in real-world applications. This research opens avenues for further exploration into continual learning strategies and weight management techniques, potentially leading to more effective fine-tuning practices across various domains.

Authors: Neha Verma, Nikhil Mehta, Shao-Chuan Wang, Naijing Zhang, Alicia Tsai, Li Wei, Lukasz Heldt, Lichan Hong et al.  
Source: arXiv:2605.12419  
URL: [https://arxiv.org/abs/2605.12419v1](https://arxiv.org/abs/2605.12419v1)
