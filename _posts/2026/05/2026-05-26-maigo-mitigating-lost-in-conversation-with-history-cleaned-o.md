---
title: "MAIGO: Mitigating Lost-in-Conversation with History-Cleaned On-Policy Self-Distillation"
date: 2026-05-26 15:38:46 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27186v1"
arxiv_id: "2605.27186"
authors: ["Haoyu Zheng", "Yun Zhu", "Shu Yuan", "Shangming Chen", "Qing Wang", "Wenqiao Zhang"]
slug: maigo-mitigating-lost-in-conversation-with-history-cleaned-o
summary_word_count: 407
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the "lost-in-conversation" (LiC) gap observed in large language models (LLMs), where performance degrades during multi-turn interactions compared to single-turn tasks. The authors identify self-contamination as a significant factor contributing to this degradation, where intermediate model outputs are incorporated into subsequent context, perpetuating early errors. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose MAIGO, an on-policy self-distillation technique designed to mitigate self-contamination by utilizing history-cleaned references from the model's own policy. The architecture involves two distinct phases: for middle turns, MAIGO removes previous assistant replies while retaining the user-visible prefix, thereby preventing the propagation of errors. For answer turns, it distills from paired full-view references that are conditioned on the completed user dialogue. A reliability weight is introduced to downweight middle-turn samples that conflict with the cleaned reference, enhancing the model's adherence to accurate responses. Notably, MAIGO does not require external verifier rewards, state labels, or additional scaffolding during inference, making it a streamlined approach.

**Results**  
MAIGO was evaluated using the LiC paired-view protocol with deterministic verifiers. The results demonstrate a significant improvement in the Qwen2.5-7B-Instruct model's SHARDED accuracy, increasing from 52.8% to 66.1%. Additionally, the SHARDED/FULL accuracy ratio improved from 66.5% to 84.1%, while maintaining FULL accuracy within a margin of 2.3 points. These results indicate that self-contamination can be effectively addressed through the proposed self-distillation method, showcasing a tangible reduction in the LiC gap.

**Limitations**  
The authors acknowledge that MAIGO's reliance on the model's own policy for history-cleaned references may limit its applicability to scenarios where the model's initial performance is suboptimal. Furthermore, the method's effectiveness in diverse conversational contexts beyond the evaluated benchmarks remains to be explored. The paper does not address potential computational overhead introduced by the self-distillation process, which could impact scalability in real-world applications.

**Why it matters**  
The implications of this work are significant for the development of more robust conversational agents. By demonstrating that self-contamination is a trainable aspect of the LiC gap, MAIGO provides a novel framework for improving multi-turn dialogue performance in LLMs. This approach could pave the way for future research focused on enhancing conversational coherence and accuracy, ultimately leading to more effective human-computer interactions. The findings encourage further exploration of self-distillation techniques in various contexts, potentially influencing the design of next-generation LLMs.

Authors: Haoyu Zheng, Yun Zhu, Shu Yuan, Shangming Chen, Qing Wang, Wenqiao Zhang, Jun Xiao, Yueting Zhuang  
Source: arXiv:2605.27186  
URL: [https://arxiv.org/abs/2605.27186v1](https://arxiv.org/abs/2605.27186v1)
