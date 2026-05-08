---
title: "Crafting Reversible SFT Behaviors in Large Language Models"
date: 2026-05-07 17:44:07 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06632v1"
arxiv_id: "2605.06632"
authors: ["Yuping Lin", "Pengfei He", "Yue Xing", "Yingqian Cui", "Jiayuan Ding", "Subhabrata Mukherjee"]
slug: crafting-reversible-sft-behaviors-in-large-language-models
summary_word_count: 461
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the interpretability and controllability of behaviors induced by supervised fine-tuning (SFT) in large language models (LLMs). Existing methods, such as circuit attribution, identify subnetworks correlated with SFT-induced behaviors but do not establish causal relationships, limiting the ability to control these behaviors during inference. The authors propose a framework to create a sparse, mechanistically necessary subnetwork, termed a *carrier*, that encapsulates SFT-induced behaviors and allows for their selective control without modifying model weights.

**Method**  
The authors introduce two key contributions:  
1. **Loss-Constrained Dual Descent (LCDD)**: This method constructs carriers by jointly optimizing routing masks and model weights under a defined utility budget. The optimization process ensures that the resulting sparse carriers maintain the desired SFT-induced behaviors while being amenable to control.
2. **SFT-Eraser**: A soft prompt designed to reverse the SFT-induced behavior by matching activations on the extracted carrier channels. This mechanism allows for the selective suppression of behaviors without altering the underlying model weights.

The training process involves a dual descent approach that balances the trade-off between behavior preservation and sparsity, ensuring that the carriers are both effective and efficient.

**Results**  
The proposed methods were evaluated across various behaviors—safety, fixed-response, and style—on multiple model families. The results demonstrate that LCDD successfully generates sparse carriers that preserve the target behaviors while enabling effective reversion through SFT-Eraser. Notably, the authors report that the sparse structure is critical for the success of the reversal; attempts to apply the same trigger optimization on standard SFT models yielded no significant results. This indicates that the structural properties of the carriers are essential for their functionality, providing a clear distinction from traditional SFT approaches.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of behaviors or model architectures, as the effectiveness of the carriers is contingent on the specific SFT-induced behaviors being targeted. Additionally, the computational overhead associated with the dual optimization process may limit scalability in larger models or more complex tasks. The paper does not address potential impacts on model performance metrics beyond the targeted behaviors, nor does it explore the long-term stability of the carriers post-deployment.

**Why it matters**  
This work has significant implications for the field of interpretability and control in LLMs. By establishing a method to create causally necessary subnetworks for SFT-induced behaviors, it opens avenues for more systematic approaches to behavior localization and suppression in deployed models. This could enhance the safety and reliability of LLMs in sensitive applications, where unintended behaviors must be mitigated without extensive retraining or model modification. The findings encourage further exploration into the structural properties of neural networks and their role in behavior management.

Authors: Yuping Lin, Pengfei He, Yue Xing, Yingqian Cui, Jiayuan Ding, Subhabrata Mukherjee, Hui Liu, Zhen Xiang  
Source: arXiv:2605.06632  
URL: https://arxiv.org/abs/2605.06632v1
