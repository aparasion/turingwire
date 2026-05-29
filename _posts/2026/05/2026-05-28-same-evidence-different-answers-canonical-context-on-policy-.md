---
title: "Same Evidence, Different Answers: Canonical-Context On-Policy Distillation for Multi-Turn Language Models"
date: 2026-05-28 17:14:29 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30251v1"
arxiv_id: "2605.30251"
authors: ["Zizhuo Lin", "Quanling Liu", "Jinsheng Quan", "Chao Zhang", "Yifan Zhu", "Xing Shi"]
slug: same-evidence-different-answers-canonical-context-on-policy-
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the performance gap in large language models (LLMs) when tasked with multi-turn conversations versus single-turn prompts. Specifically, it highlights the phenomenon of self-anchored drift, where models generate responses based on partial information, leading to unsupported assumptions that distort final answers. The authors identify the need for a method that allows LLMs to maintain consistency in responses when evidence is presented incrementally across turns, as opposed to all at once in a full prompt.

**Method**  
The authors propose Canonical-Context On-Policy Distillation (CCOPD), a novel training approach that utilizes a dual-role framework. In this setup, a frozen teacher model is conditioned on a clean FULL prompt, while a trainable student model receives the same evidence incrementally through a multi-turn conversation. The training objective aligns the student's responses with the teacher's canonical behavior, effectively distilling the full-context understanding into the student model. The training is conducted exclusively on math problem conversations, leveraging a dataset that emphasizes the incremental presentation of information. The authors do not disclose specific details regarding the architecture, loss functions, or compute resources used in the training process.

**Results**  
CCOPD demonstrates a significant performance enhancement, achieving a 32% average relative improvement in RAW-SHARDED performance over the original base model across various tasks, including five zero-shot out-of-domain task families. Notably, the method preserves the model's performance on full-context prompts, indicating that the distillation process does not compromise the model's ability to handle complete information. The results suggest that CCOPD effectively mitigates the negative impact of self-anchored drift, enhancing the model's grounding in user evidence and reducing sensitivity to earlier conversational turns.

**Limitations**  
The authors acknowledge that their approach is limited to math problem conversations, which may restrict the generalizability of the findings to other domains. Additionally, the reliance on a single base model for both teacher and student roles may introduce biases inherent to that model. The paper does not address potential scalability issues or the computational overhead associated with the dual-role training framework. Furthermore, the long-term implications of using CCOPD in real-world applications remain unexplored.

**Why it matters**  
The implications of this work are significant for the development of more robust conversational agents that can handle multi-turn interactions without losing coherence or accuracy. By addressing the self-anchored drift phenomenon, CCOPD paves the way for improved LLM performance in scenarios where information is revealed gradually, which is common in real-world applications. This research could influence future work on training methodologies for LLMs, particularly in enhancing their ability to maintain context and consistency across extended dialogues.

Authors: Zizhuo Lin, Quanling Liu, Jinsheng Quan, Chao Zhang, Yifan Zhu, Xing Shi, Jingtao Xu, Zhihui Li et al.  
Source: arXiv:2605.30251  
URL: [https://arxiv.org/abs/2605.30251v1](https://arxiv.org/abs/2605.30251v1)
