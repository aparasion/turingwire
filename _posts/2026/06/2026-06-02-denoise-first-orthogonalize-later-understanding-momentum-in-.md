---
title: "Denoise First, Orthogonalize Later: Understanding Momentum in Muon via Spectral Filtering"
date: 2026-06-02 16:54:38 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03899v1"
arxiv_id: "2606.03899"
authors: ["Xianliang Li", "Zihan Zhang", "Weiyang Liu", "Han Bao"]
slug: denoise-first-orthogonalize-later-understanding-momentum-in-
summary_word_count: 409
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper elucidates the theoretical role of momentum in Muon, demonstrating its function as a spectral filter that enhances gradient updates."
---

**Problem**  
This work addresses the theoretical ambiguity surrounding the role of momentum in the Muon optimizer, which has shown strong empirical performance in large language model (LLM) training. Prior analyses either isolate spectral updates by removing momentum or retain momentum without a clear explanation of its empirical advantages. This paper fills the gap by providing a theoretical framework that clarifies how momentum functions within Muon, which is particularly relevant given the increasing reliance on momentum-based optimizers in deep learning.

**Method**  
The authors propose a structured signal-plus-perturbation gradient model to analyze the effects of momentum in Muon. They demonstrate that momentum acts as a spectral filter, effectively suppressing perturbations while preserving the dominant signal in the gradient updates. This mechanism enlarges the spectral gap between the signal and noise, thereby stabilizing the singular subspaces of the matrix used in Muon's orthogonalization step. The paper rigorously proves that applying momentum prior to orthogonalization leads to a stronger alignment with the signal component of the gradient compared to reversing the order or omitting momentum entirely. The experiments conducted span various tasks, including LLM pretraining, to validate the theoretical claims.

**Results**  
The empirical results indicate that the proposed momentum strategy significantly enhances performance across multiple benchmarks. For instance, in LLM pretraining tasks, the authors report improvements in convergence rates and final model accuracy compared to baseline optimizers that either do not utilize momentum or apply it after orthogonalization. Specific performance metrics are not disclosed in the abstract, but the authors emphasize that the effect sizes are substantial enough to warrant attention from the research community.

**Limitations**  
The authors acknowledge that their theoretical framework is based on a specific gradient model, which may not encompass all scenarios encountered in practical applications. Additionally, the experiments, while diverse, may not cover all possible use cases of Muon in real-world settings. The paper does not address potential computational overhead introduced by the momentum mechanism, which could be a concern in resource-constrained environments.

**Why it matters**  
This research provides a foundational understanding of momentum's role in Muon, offering insights that could influence the design of future optimizers in deep learning. By framing momentum as a spectral filtering mechanism, the findings may lead to improved strategies for gradient updates in various matrix-based optimizers, potentially enhancing their performance in large-scale training scenarios. This work is particularly relevant for researchers and engineers focused on optimizing training processes for large language models and other complex neural architectures, as published in [arXiv cs.LG](https://arxiv.org/abs/2606.03899v1).
