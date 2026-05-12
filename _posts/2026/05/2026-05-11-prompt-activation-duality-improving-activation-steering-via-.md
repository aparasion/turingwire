---
title: "Prompt-Activation Duality: Improving Activation Steering via Attention-Level Interventions"
date: 2026-05-11 14:44:32 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10664v1"
arxiv_id: "2605.10664"
authors: ["Diancheng Kang", "Zheyuan Liu", "Ningshan Ma", "Yue Huang", "Zhaoxuan Tan", "Meng Jiang"]
slug: prompt-activation-duality-improving-activation-steering-via-
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of activation steering in language models, particularly in the context of stateful dialogue systems. The authors identify KV-cache contamination as a significant failure mode, where the effects of steered token states accumulate over time, leading to degradation in coherence and trait expression. This issue has not been adequately addressed in existing literature, making it a pertinent gap for improving the reliability of activation steering techniques. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach called Gated Cropped Attention-Delta steering (GCAD). This method leverages the contributions of system prompts to self-attention mechanisms to extract steering signals. The core technical contribution involves applying these signals through token-level gating, which allows for more precise control over the activation steering process. The architecture remains within the framework of existing transformer models, but the intervention mechanism is specifically designed to mitigate the effects of KV-cache contamination. The training compute details are not disclosed, but the focus is on enhancing the coherence of long-horizon dialogues through this new steering method.

**Results**  
GCAD was evaluated on a multi-turn dialogue benchmark, demonstrating significant improvements over baseline methods. The average coherence drift was reduced from -18.6 to -1.9, indicating a substantial enhancement in the model's ability to maintain coherence over extended interactions. Additionally, the trait expression at turn 10 improved from 78.0 to 93.1, showcasing the effectiveness of GCAD in preserving the intended persona traits throughout the dialogue. These results suggest that the proposed method outperforms standard residual-stream steering techniques, particularly in maintaining coherence and trait fidelity in stateful dialogue scenarios.

**Limitations**  
The authors acknowledge that while GCAD improves coherence and trait expression, it may still be sensitive to the quality of the initial prompts and the underlying model architecture. They do not discuss potential scalability issues or the computational overhead introduced by the token-level gating mechanism. Additionally, the generalizability of GCAD to other tasks beyond persona steering is not explored, which could limit its applicability in broader contexts. The paper does not address the potential for overfitting to specific dialogue scenarios, which could affect performance in more diverse conversational settings.

**Why it matters**  
The implications of this work are significant for the development of more reliable and coherent dialogue systems. By addressing the KV-cache contamination issue, GCAD provides a pathway for enhancing activation steering techniques, which are crucial for maintaining user engagement and satisfaction in conversational AI applications. This research opens avenues for further exploration of prompt-mediated interventions in language models, potentially leading to more robust and contextually aware AI systems. The findings could influence future work on dialogue management, persona consistency, and the overall design of interactive AI systems.

Authors: Diancheng Kang, Zheyuan Liu, Ningshan Ma, Yue Huang, Zhaoxuan Tan, Meng Jiang  
Source: arXiv:2605.10664  
URL: [https://arxiv.org/abs/2605.10664v1](https://arxiv.org/abs/2605.10664v1)
