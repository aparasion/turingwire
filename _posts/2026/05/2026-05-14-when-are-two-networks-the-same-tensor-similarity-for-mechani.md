---
title: "When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability"
date: 2026-05-14 17:58:27 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15183v1"
arxiv_id: "2605.15183"
authors: ["ML Nissen Gonzalez", "Melwina Albuquerque", "Laurence Wroe", "Jacob Meyer Cohen", "Logan Riggs Smith", "Thomas Dooms"]
slug: when-are-two-networks-the-same-tensor-similarity-for-mechani
summary_word_count: 408
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in mechanistic interpretability within deep learning, specifically the challenge of verifying whether two neural network components perform the same computation. Existing similarity measures either focus on empirical behavior, which can fail to generalize to out-of-distribution scenarios, or rely on basis-dependent parameters that overlook weight-space symmetries. This work proposes a novel approach to overcome these limitations by introducing a weight-based metric that is invariant to such symmetries.

**Method**  
The authors introduce a new metric termed "tensor similarity," which quantifies the similarity between tensor-based models. This metric is designed to capture global functional equivalence and is computed using an efficient recursive algorithm that accounts for cross-layer mechanisms. The tensor similarity metric is formulated to be invariant to transformations that do not affect the underlying computation, thus providing a more robust measure of similarity. The authors detail the algorithmic implementation, although specific training compute requirements are not disclosed.

**Results**  
Empirical evaluations demonstrate that tensor similarity outperforms existing similarity metrics in tracking functional training dynamics, such as grokking and backdoor insertion. The authors report that their metric achieves a higher fidelity in measuring similarity compared to traditional methods, although specific numerical results and effect sizes against named baselines are not provided in the abstract. The paper suggests that tensor similarity reduces the problem of measuring similarity and verifying faithfulness to an algebraic computation rather than relying on empirical approximations.

**Limitations**  
The authors acknowledge that while tensor similarity provides a more robust framework for measuring similarity, it may still be limited by the assumptions inherent in tensor-based models. Additionally, the recursive algorithm's efficiency may vary depending on the architecture's complexity, which is not thoroughly explored. The paper does not address potential scalability issues when applied to very large models or the implications of using this metric in practice across diverse architectures.

**Why it matters**  
This work has significant implications for the field of mechanistic interpretability, as it provides a systematic approach to verifying the equivalence of neural network components. By framing similarity measurement as an algebraic problem, it opens avenues for more rigorous analysis of model behavior and enhances our understanding of how different parts of a model contribute to its overall functionality. This could lead to improved interpretability tools and methodologies, fostering trust in AI systems and facilitating the development of more robust models.

Authors: ML Nissen Gonzalez, Melwina Albuquerque, Laurence Wroe, Jacob Meyer Cohen, Logan Riggs Smith, Thomas Dooms  
Source: arXiv cs.LG  
URL: https://arxiv.org/abs/2605.15183v1
