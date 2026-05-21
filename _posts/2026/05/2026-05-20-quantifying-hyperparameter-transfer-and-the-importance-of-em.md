---
title: "Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate"
date: 2026-05-20 17:59:40 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21486v1"
arxiv_id: "2605.21486"
authors: ["Dayal Singh Kalra", "Maissam Barkeshli"]
slug: quantifying-hyperparameter-transfer-and-the-importance-of-em
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding hyperparameter transfer, particularly in the context of training large language models (LLMs). While existing literature discusses scaling laws and parameterization strategies, it lacks a comprehensive framework to quantify hyperparameter transfer across different model scales. The authors aim to elucidate the mechanisms behind effective hyperparameter transfer, specifically focusing on the learning rate of the embedding layer, which has been underexplored in prior work.

**Method**  
The authors propose a framework to quantify hyperparameter transfer using three metrics: (1) the quality of the scaling law fit, (2) robustness to extrapolation errors, and (3) the asymptotic loss penalty associated with parameterization choices. They introduce Maximal Update ($μ$P) as a parameterization strategy that enhances learning rate transfer compared to standard parameterization (SP). The core technical contribution lies in the empirical analysis of the embedding layer's learning rate, which is shown to be a critical factor in training stability and performance. The authors conduct a series of ablation studies to demonstrate that the benefits of $μ$P stem from its ability to maximize the embedding layer's learning rate, thereby alleviating bottlenecks that lead to training instabilities. The experiments utilize the AdamW optimizer, and while specific training compute details are not disclosed, the focus is on the comparative analysis of learning rates and weight decay effects.

**Results**  
The findings indicate that $μ$P significantly outperforms SP in terms of hyperparameter transfer efficiency. Specifically, the authors report that increasing the embedding layer learning rate by a factor proportional to model width leads to smoother training dynamics and improved scaling law fits. The results show that weight decay enhances the quality of scaling law fits but negatively impacts robustness in a fixed token-per-parameter setting. While exact numerical results are not provided in the summary, the qualitative improvements suggest a substantial effect size in favor of $μ$P over SP.

**Limitations**  
The authors acknowledge that their framework is primarily empirical and may not fully capture the theoretical underpinnings of hyperparameter transfer. They also note that while weight decay improves scaling law fits, it can compromise robustness, indicating a trade-off that requires further investigation. Additionally, the study does not explore the implications of varying other hyperparameters beyond the embedding layer learning rate, which could limit the generalizability of the findings.

**Why it matters**  
This work has significant implications for the training of large language models, particularly in optimizing hyperparameter settings across different scales. By providing a quantifiable framework for hyperparameter transfer, it enables researchers and practitioners to make informed decisions about parameterization strategies, potentially leading to more efficient training processes. The insights regarding the embedding layer's learning rate could influence future model architectures and training protocols, fostering advancements in LLM performance and scalability.

Authors: Dayal Singh Kalra, Maissam Barkeshli  
Source: arXiv:2605.21486  
URL: [https://arxiv.org/abs/2605.21486v1](https://arxiv.org/abs/2605.21486v1)
