---
title: "ScriptHOI: Learning Scripted State Transitions for Open-Vocabulary Human-Object Interaction Detection"
date: 2026-05-06 15:52:35 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05057v1"
arxiv_id: "2605.05057"
authors: ["Minh Anh Nguyen", "Quang Huy Tran", "Bao Ngoc Le", "SuiYang Guang", "Tuan Kiet Pham", "Linh Chi Vo"]
slug: scripthoi-learning-scripted-state-transitions-for-open-vocab
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing vision-language human-object interaction (HOI) detection models, particularly their reliance on object affordance and phrase-level co-occurrence, which can lead to inaccurate predictions. The authors highlight that current models often fail to verify the contextual integrity of interactions, such as whether the hand, tool, target, contact pattern, and object state collectively support the predicted action. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce ScriptHOI, a structured framework that models interaction phrases as soft scripted state transitions. Instead of treating interaction phrases as single class tokens, ScriptHOI decomposes them into multiple slots: body-role, contact, geometry, affordance, motion, and object-state. A visual state tokenizer is employed to parse detected human-object pairs into corresponding state tokens. The framework includes a slot-wise matcher that estimates script coverage and script conflict, which are used to calibrate HOI logits and expose missing visual evidence. To handle incomplete annotations without suppressing valid unannotated interactions, the authors propose interval partial-label learning, which constrains unannotated candidates with script-derived probability bounds. Additionally, a counterfactual script contrast loss is introduced to discourage reliance on object-only shortcuts by swapping individual script slots during training.

**Results**  
ScriptHOI demonstrates significant improvements over baseline models on several benchmarks, including HICO-DET and V-COCO. Specifically, it achieves a 5.2% increase in mean Average Precision (mAP) on HICO-DET for rare interactions and a 7.1% increase for unseen interactions compared to the best-performing baseline. The model also reduces affordance-conflict false positives by 15%, indicating a more reliable detection of interactions that are not solely based on object presence.

**Limitations**  
The authors acknowledge that the reliance on scripted state transitions may introduce biases if the scripts do not comprehensively cover all possible interactions. Additionally, the model's performance may be limited by the quality and diversity of the training data, particularly for rare interactions. The paper does not address potential computational overhead introduced by the slot-wise matching and interval partial-label learning processes, which could affect scalability in real-time applications.

**Why it matters**  
The implications of ScriptHOI extend to various applications in robotics, human-computer interaction, and video understanding, where accurate detection of human-object interactions is crucial. By improving the model's ability to recognize rare and unseen interactions, this work paves the way for more robust and flexible systems that can operate in dynamic environments. The structured approach to modeling interactions also opens avenues for future research in open-vocabulary learning and the integration of more complex interaction dynamics.

Authors: Minh Anh Nguyen, Quang Huy Tran, Bao Ngoc Le, SuiYang Guang, Tuan Kiet Pham, Linh Chi Vo  
Source: arXiv:2605.05057  
URL: https://arxiv.org/abs/2605.05057v1
