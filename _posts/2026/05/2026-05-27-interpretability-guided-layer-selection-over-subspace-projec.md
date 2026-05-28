---
title: "Interpretability-Guided Layer Selection over Subspace Projection: SAEs as Stethoscopes, Not Scalpels, for Raw Task Vector Model Editing"
date: 2026-05-27 15:52:39 +0000
category: research
subcategory: interpretability
company: "Google DeepMind"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28649v1"
arxiv_id: "2605.28649"
authors: ["Li Lei", "Madalina Ciobanu", "Qingqing Mao", "Ritankar Das"]
slug: interpretability-guided-layer-selection-over-subspace-projec
summary_word_count: 409
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing model editing techniques for large language models (LLMs), particularly in enhancing domain-specific capabilities without incurring the computational costs or risks of catastrophic forgetting associated with full fine-tuning. The authors identify a critical gap in the interpretability of Sparse Autoencoders (SAEs) when applied to model editing, specifically in the context of mathematical reasoning tasks on the Gemma-3-4B-IT dataset.

**Method**  
The core technical contribution is the introduction of an SAE-guided editing pipeline that reframes the use of SAEs from a direct intervention tool to a diagnostic instrument. The authors first evaluate the conventional approach of projecting task vectors onto SAE feature subspaces, which they find leads to significant information loss—approximately 97% of modification energy is discarded, resulting in no statistically significant improvements across seven mathematical subjects. They propose a new methodology where SAEs are utilized to identify specific layers for intervention based on a derived specificity score, allowing for the injection of unfiltered raw task vectors into these layers. This method is deterministic and does not incur additional inference costs, providing a principled framework for interpretability-guided model editing.

**Results**  
The proposed method demonstrates significant improvements in model performance on the Minerva Math benchmark. Specifically, the accuracy for Number Theory tasks increased from 29.6% to 39.4% (z=+3.41, p=0.0007). Overall, five out of seven mathematical subjects showed statistically significant improvements, while none exhibited significant degradation. These results highlight the effectiveness of the SAE-guided layer selection approach compared to traditional projection methods.

**Limitations**  
The authors acknowledge that their approach may not generalize across all types of tasks or datasets beyond mathematical reasoning. They also note the potential for overfitting to the specific layers identified by the SAE-derived specificity scores, which could limit the robustness of the model editing. Additionally, the study does not explore the scalability of this method to larger models or more complex tasks, which could be a significant consideration for future work.

**Why it matters**  
This work has important implications for the field of model editing in LLMs, particularly in enhancing interpretability and efficiency. By shifting the perspective on how SAEs can be utilized, the authors provide a novel framework that could lead to more effective and interpretable model modifications. This approach not only mitigates the risks associated with catastrophic forgetting but also opens avenues for further research into layer-specific interventions, potentially influencing future methodologies in model adaptation and fine-tuning.

Authors: Li Lei, Madalina Ciobanu, Qingqing Mao, Ritankar Das  
Source: arXiv:2605.28649  
URL: https://arxiv.org/abs/2605.28649v1
