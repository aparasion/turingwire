---
title: "The Structural Origin of Attention Sink: Variance Discrepancy, Super Neurons, and Dimension Disparity"
date: 2026-05-07 17:28:55 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06611v1"
arxiv_id: "2605.06611"
authors: ["Siquan Li", "Kaiqi Jiang", "Jiacheng Sun", "Tianyang Hu"]
slug: the-structural-origin-of-attention-sink-variance-discrepancy
summary_word_count: 423
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the attention sink phenomenon observed in Large Language Models (LLMs), where initial tokens disproportionately dominate attention scores. Despite its prevalence, the structural origins of this phenomenon have not been thoroughly elucidated in existing literature. The authors aim to provide a mechanistic explanation for attention sinks, identifying the underlying processes that contribute to this behavior.

**Method**  
The authors propose a causal framework linking attention sinks to the value aggregation process in self-attention mechanisms, which leads to a systematic variance discrepancy. They identify that the activation of super neurons in Feed-Forward Network (FFN) layers exacerbates this discrepancy. Specifically, the channel-sparse down-projections create a dimension disparity in the representation of the first token, necessitating the formation of attention sinks as a structural anchor. To validate their hypothesis, the authors conduct two controlled interventions: (i) modifying attention masks to isolate the aggregation effect and (ii) amplifying the variance of targeted token representations. These interventions successfully replicate attention sinks at arbitrary positions. Additionally, they introduce a novel architectural modification termed head-wise RMSNorm, which aims to stabilize value aggregation outputs during pre-training, thereby restoring statistical parity across token positions and accelerating convergence.

**Results**  
The authors report that their head-wise RMSNorm modification leads to a significant improvement in convergence rates during pre-training compared to standard normalization techniques. While specific numerical results are not disclosed in the abstract, the implication is that the proposed method effectively mitigates the attention sink phenomenon, enhancing model performance. The experiments demonstrate that the proposed interventions can consistently replicate attention sinks, indicating a robust understanding of the underlying mechanisms.

**Limitations**  
The authors acknowledge that their study primarily focuses on the structural origins of attention sinks without exploring the broader implications of these findings on model interpretability or generalization. They do not address potential scalability issues of the proposed head-wise RMSNorm modification in larger models or its impact on downstream tasks. Additionally, the reliance on controlled interventions may limit the generalizability of their findings to real-world scenarios where attention patterns are more complex.

**Why it matters**  
This work provides a foundational understanding of the structural causes of attention sinks, which can inform future research on improving LLM architectures. By elucidating the mechanisms behind attention distribution, the findings have implications for designing more robust attention mechanisms that mitigate the dominance of initial tokens. The proposed head-wise RMSNorm modification offers a practical approach to enhance convergence during pre-training, potentially leading to more efficient training processes and improved model performance in downstream applications.

Authors: Siquan Li, Kaiqi Jiang, Jiacheng Sun, Tianyang Hu  
Source: arXiv:2605.06611  
URL: https://arxiv.org/abs/2605.06611v1
