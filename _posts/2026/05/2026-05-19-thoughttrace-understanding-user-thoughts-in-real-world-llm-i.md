---
title: "ThoughtTrace: Understanding User Thoughts in Real-World LLM Interactions"
date: 2026-05-19 16:42:06 +0000
category: research
subcategory: other
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20087v1"
arxiv_id: "2605.20087"
authors: ["Chuanyang Jin", "Binze Li", "Haopeng Xie", "Cathy Mengying Fang", "Tianjian Li", "Shayne Longpre"]
slug: thoughttrace-understanding-user-thoughts-in-real-world-llm-i
summary_word_count: 464
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the literature regarding the understanding of user cognition during interactions with conversational AI. Existing datasets primarily capture the verbal exchanges between users and AI, neglecting the underlying thoughts that inform user prompts and reactions. The authors introduce ThoughtTrace, a novel dataset that includes self-reported user thoughts alongside multi-turn conversations, thereby providing insights into the cognitive processes that drive user behavior. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
ThoughtTrace is constructed from a dataset comprising 1,058 users, 2,155 conversations, 17,058 turns, and 10,174 thought annotations, collected across 20 different language models. The dataset captures a wide range of interactions, emphasizing long-horizon and topic diversity. The authors analyze the semantic distinction between user thoughts and conversational messages, revealing that thoughts are often not inferable from the context provided by the conversation. The paper proposes two primary applications for the dataset: (1) enhancing user-behavior prediction by incorporating thoughts as inference-time context, and (2) utilizing thought-guided rewrites to provide fine-grained alignment signals for training personalized AI assistants. The authors do not disclose specific architectural details, loss functions, or training compute used in their experiments.

**Results**  
The authors demonstrate that incorporating user thoughts significantly improves the accuracy of user-behavior predictions compared to baseline models that do not utilize this additional context. While specific numerical results are not provided in the abstract, the paper claims that the improvements are substantial enough to warrant the introduction of this new data modality. Additionally, the thought-guided rewrites are shown to enhance the performance of personalized assistants, although exact metrics and comparisons to named baselines are not detailed in the summary.

**Limitations**  
The authors acknowledge that the dataset may not capture all possible user thoughts, potentially limiting its generalizability. They also note that the reliance on self-reported thoughts may introduce biases, as users may not always accurately articulate their cognitive processes. Furthermore, the dataset's focus on specific language models may restrict its applicability across diverse AI systems. An additional limitation not mentioned by the authors is the potential for variability in user interpretation of their own thoughts, which could affect the consistency of the annotations.

**Why it matters**  
The introduction of ThoughtTrace represents a significant advancement in the study of human-AI interaction by providing a new lens through which to understand user cognition. By establishing user thoughts as a distinct data modality, this work lays the groundwork for future research aimed at developing AI systems that can better comprehend and adapt to users' latent goals, preferences, and needs. The implications extend to improving user experience in conversational AI, enabling more personalized and context-aware interactions.

Authors: Chuanyang Jin, Binze Li, Haopeng Xie, Cathy Mengying Fang, Tianjian Li, Shayne Longpre, Hongxiang Gu, Maximillian Chen et al.  
Source: arXiv:2605.20087  
URL: https://arxiv.org/abs/2605.20087v1
