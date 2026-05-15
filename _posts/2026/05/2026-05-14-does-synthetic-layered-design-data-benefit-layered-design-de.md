---
title: "Does Synthetic Layered Design Data Benefit Layered Design Decomposition?"
date: 2026-05-14 17:55:11 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15167v1"
arxiv_id: "2605.15167"
authors: ["Kam Man Wu", "Haolin Yang", "Qingyu Chen", "Yihu Tang", "Jingye Chen", "Qifeng Chen"]
slug: does-synthetic-layered-design-data-benefit-layered-design-de
summary_word_count: 403
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in layered graphic design decomposition, particularly the limitations of existing methods that rely on proprietary layered assets or partially synthetic data derived from limited structural priors. These approaches struggle with scalability and flexibility in post-generation editing. The authors propose to investigate whether purely synthetic layered data can enhance the performance of layer decomposition frameworks, specifically in the context of graphic design where modular and semantically separable components are prevalent.

**Method**  
The authors introduce a synthetic dataset named SynLayers, which is constructed to facilitate the training of a state-of-the-art layer decomposition framework, CLD (Conditional Layer Decomposition). The dataset is generated using vision-language models (VLMs) to create textual supervision and automate inference inputs with predicted bounding boxes. The study emphasizes a data-centric approach, focusing on the scalability of synthetic data in comparison to traditional datasets like PrismLayersPro. The training process involves varying the scale of the synthetic dataset to evaluate performance improvements, with a specific focus on the layer-count distribution to mitigate the imbalances typically found in real-world datasets.

**Results**  
The findings indicate that training with purely synthetic data can outperform the non-scalable PrismLayersPro dataset, establishing SynLayers as a viable alternative. Performance metrics show consistent improvement with increased training data scale, with diminishing returns observed beyond approximately 50,000 samples. Additionally, the synthetic dataset allows for controlled layer-count distributions, addressing the imbalance issues present in real-world datasets. The results suggest that synthetic data can effectively enhance the capabilities of layered design decomposition systems.

**Limitations**  
The authors acknowledge that while synthetic data shows promise, it may not capture all the complexities of real-world design scenarios. They do not address potential overfitting to synthetic patterns or the generalizability of the model to diverse design styles. Furthermore, the reliance on VLMs for textual supervision may introduce biases based on the training data of the VLMs used.

**Why it matters**  
This work has significant implications for the field of graphic design and image generation, particularly in enhancing the usability of automated design tools. By demonstrating the effectiveness of synthetic data in layered design decomposition, the study encourages the adoption of synthetic datasets as a foundational element for developing more scalable and flexible design editing systems. This could lead to advancements in automated design workflows, enabling designers to leverage AI tools more effectively in their creative processes.

Authors: Kam Man Wu, Haolin Yang, Qingyu Chen, Yihu Tang, Jingye Chen, Qifeng Chen  
Source: arXiv:2605.15167  
URL: [https://arxiv.org/abs/2605.15167v1](https://arxiv.org/abs/2605.15167v1)
