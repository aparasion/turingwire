---
title: "The First Token Knows: Single-Decode Confidence for Hallucination Detection"
date: 2026-05-06 17:34:00 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.05166v1"
arxiv_id: "2605.05166"
authors: ["Mina Gabriel"]
slug: the-first-token-knows-single-decode-confidence-for-hallucina
summary_word_count: 448
classification_confidence: 0.75
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing hallucination detection methods in language models, particularly the inefficiencies of self-consistency and semantic self-consistency approaches. Self-consistency relies on generating multiple sampled answers to assess agreement, which incurs high computational costs and is sensitive to lexical variations. Semantic self-consistency improves upon this by clustering answers based on meaning through natural language inference, but it also adds sampling overhead. The authors propose a novel metric, first-token confidence (phi_first), which can detect hallucinations without the need for multiple decodings or external inference, thus filling a gap in efficient hallucination detection methods. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of the first-token confidence metric, phi_first, which is derived from the normalized entropy of the top-K logits at the first content-bearing token of a single greedy decode. The authors evaluate phi_first across three instruction-tuned models with 7-8 billion parameters on two benchmarks for closed-book short-answer factual question answering. The training compute details are not disclosed, but the method emphasizes a single-pass decoding approach, contrasting with the multi-sample strategies of existing methods. The authors also conduct a subsumption test to analyze the correlation between phi_first and semantic agreement.

**Results**  
The evaluation shows that phi_first achieves a mean Area Under the Receiver Operating Characteristic (AUROC) score of 0.820, outperforming semantic agreement (0.793) and standard surface-form self-consistency (0.791). The correlation analysis indicates that phi_first is moderately to strongly correlated with semantic agreement, suggesting that the uncertainty information captured by multi-sample agreement is largely encapsulated in the initial token distribution. The combination of phi_first with semantic agreement yields only a marginal improvement in AUROC, indicating that phi_first alone is a robust indicator of hallucination detection.

**Limitations**  
The authors acknowledge that while phi_first shows promise, it may not capture all nuances of hallucination detection, particularly in more complex or nuanced queries where semantic agreement might still provide additional insights. They do not address potential biases in the training data or the generalizability of phi_first across different model architectures or tasks. Furthermore, the reliance on a single greedy decode may overlook variability that could be captured through more diverse sampling methods.

**Why it matters**  
The introduction of phi_first as a low-cost baseline for hallucination detection has significant implications for the efficiency of language model applications. By reducing the need for multiple decodings and external inference, this method can streamline the deployment of models in real-time applications where computational resources are constrained. The findings suggest that future research can build upon phi_first to enhance hallucination detection mechanisms without incurring substantial overhead, potentially leading to more reliable and efficient AI systems.

Authors: Mina Gabriel  
Source: arXiv:2605.05166  
URL: [https://arxiv.org/abs/2605.05166v1](https://arxiv.org/abs/2605.05166v1)
