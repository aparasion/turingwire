---
title: "Concept-Based Abductive and Contrastive Explanations for Behaviors of Vision Models"
date: 2026-05-07 17:51:13 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06640v1"
arxiv_id: "2605.06640"
authors: ["Ronaldo Canizales", "Divya Gopinath", "Corina P\u0103s\u0103reanu", "Ravi Mangal"]
slug: concept-based-abductive-and-contrastive-explanations-for-beh
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the need for high-level, human-understandable explanations of deep neural network predictions that establish causal connections between concepts and model outcomes. Existing methods either lack causal grounding or are limited to single concepts, while formal abductive and contrastive explanations focus on low-level features, such as pixels, without leveraging high-level concepts. The authors propose a novel framework that integrates these two approaches to enhance interpretability in vision models.

**Method**  
The authors introduce *concept-based abductive and contrastive explanations*, which aim to identify minimal sets of high-level concepts that are causally relevant to model predictions. The core technical contribution includes a family of algorithms that utilize *concept erasure* procedures to establish causal relationships between concepts and outcomes. The algorithms enumerate all minimal explanations, allowing for both individual image analysis and collective behavior analysis across multiple images. The training compute and specific datasets used for evaluation are not disclosed, but the approach is tested across various models and behaviors, indicating a broad applicability.

**Results**  
The proposed method demonstrates significant improvements in generating user-friendly explanations compared to baseline methods. While specific numerical results are not detailed in the abstract, the authors claim effectiveness across multiple models and datasets, suggesting a robust performance in computing explanations that are both informative and aligned with user-specified behaviors. The results indicate that the method can effectively capture the causal relationships between high-level concepts and model predictions, enhancing interpretability.

**Limitations**  
The authors acknowledge that their approach may still face challenges in scalability when applied to very large datasets or complex models, as the enumeration of minimal explanations could become computationally intensive. Additionally, the reliance on concept erasure procedures may introduce biases if the concepts are not well-defined or if the erasure process does not accurately reflect the causal relationships. The paper does not address potential limitations related to the generalizability of the explanations across different domains or the subjective nature of high-level concepts.

**Why it matters**  
This work has significant implications for the field of explainable AI, particularly in enhancing the interpretability of vision models. By bridging the gap between low-level feature analysis and high-level concept explanations, the proposed framework allows for a more nuanced understanding of model behavior. This can facilitate trust in AI systems, improve user interaction, and guide future research in developing more interpretable models. The integration of causal reasoning into concept-based explanations could also inspire new methodologies for evaluating and refining model architectures in various applications.

Authors: Ronaldo Canizales, Divya Gopinath, Corina Păsăreanu, Ravi Mangal  
Source: arXiv:2605.06640  
URL: https://arxiv.org/abs/2605.06640v1
