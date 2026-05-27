---
title: "Not All Tokens Matter Equally: Dynamic In-context Vector Distillation with Decisive-Token Supervision for Long-form Medical Report Generation"
date: 2026-05-26 15:46:00 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27194v1"
arxiv_id: "2605.27194"
authors: ["Ning Wu", "Rui Liu", "Xinkun Lin", "Weixing Chen", "Jinxi Xiang", "Tao Wei"]
slug: not-all-tokens-matter-equally-dynamic-in-context-vector-dist
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the literature regarding the limitations of token-level distillation in long-form medical report generation (MRG). Existing multimodal distillation methods have primarily focused on short-form tasks, where the output is limited to a few tokens. The authors highlight that current approaches treat all output tokens as equally informative, which is problematic for long-form generation where the quality is determined by a sparse set of decisive tokens, particularly in the medical domain. Specifically, pathology-related tokens and the end-of-sequence (EOS) token are critical for ensuring diagnostic accuracy and proper report termination, yet they receive inadequate supervision under traditional uniform cross-entropy loss.

**Method**  
The authors propose DIVE (Dynamic In-context Vector Distillation), a novel framework for distilling knowledge in long-form MRG. DIVE employs two key mechanisms:  
1. **Decisive-token supervision**: This approach upweights the cross-entropy loss for pathology-related tokens and the EOS token, ensuring that these critical components are prioritized during training. This addresses the imbalance in supervision that arises from treating all tokens uniformly.  
2. **State-conditioned dynamic steering**: Instead of using fixed open-loop residuals, this mechanism introduces hidden-state-dependent adapters that allow the model to adjust the injected signal dynamically as decoding progresses. This adaptation helps maintain fidelity to the teacher model even as the generation drifts from teacher-forced trajectories.

**Results**  
DIVE was evaluated on the MIMIC-CXR and CheXpert Plus datasets using two medical vision-language model (VLM) backbones. The results demonstrate that DIVE consistently outperforms existing methods across various metrics. Specifically, it achieves the highest BLEU-4, ROUGE-L, and RadGraph F1 scores in all dataset-backbone configurations. Additionally, it remains competitive on the CheXbert F1 score, which assesses coarse label-level performance. The effect sizes indicate a substantial improvement in report quality, underscoring the effectiveness of the proposed supervision and steering mechanisms.

**Limitations**  
The authors acknowledge that while DIVE improves upon existing methods, it may still be limited by the quality of the underlying VLM backbones used. Additionally, the reliance on specific token types (pathology and EOS) may not generalize to other domains or tasks where different decisive tokens are critical. The paper does not explore the computational overhead introduced by the dynamic steering mechanism, which could impact scalability in real-world applications.

**Why it matters**  
The implications of this work are significant for the field of medical report generation and beyond. By addressing the shortcomings of token-level distillation in long-form outputs, DIVE provides a framework that can enhance the fidelity and relevance of generated content in critical applications. This approach could pave the way for more effective distillation techniques in other domains requiring long-form generation, potentially improving the quality of automated reporting systems in healthcare and other fields.

Authors: Ning Wu, Rui Liu, Xinkun Lin, Weixing Chen, Jinxi Xiang, Tao Wei, Lina Yao, Mingjie Li  
Source: arXiv:2605.27194  
URL: [https://arxiv.org/abs/2605.27194v1](https://arxiv.org/abs/2605.27194v1)
