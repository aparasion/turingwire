---
title: "Can LLMs Time Travel? Enhancing Temporal Consistency in Legal Agentic Search through Reinforcement Learning"
date: 2026-05-25 14:57:13 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.25920v1"
arxiv_id: "2605.25920"
authors: ["Wei Fan", "Yining Zhou", "Mufan Zhang", "Yanbing Weng", "Yiran HU", "Tianshi Zheng"]
slug: can-llms-time-travel-enhancing-temporal-consistency-in-legal
summary_word_count: 401
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in temporal consistency within legal reasoning frameworks utilizing large language models (LLMs). Current LLMs, while effective in agentic search for legal applications, fail to account for the temporal context of laws, leading to potential misapplications of statutes due to their training data's cutoff. The authors highlight that existing legal LLMs exhibit temporal bias and that typical web search methods do not yield the precise legal citations necessary for accurate legal reasoning.

**Method**  
The authors introduce LegalSearch-R1, an end-to-end reinforcement learning framework designed to enhance temporal consistency in legal searches. The architecture integrates a local statute retrieval-augmented generation (RAG) component for precise article matching with an online web search module to access broader legal knowledge. The model is trained on temporally-indexed datasets that encompass multiple amendment periods, ensuring that the temporal context is respected during the retrieval process. The training process leverages reinforcement learning techniques to optimize the model's performance on legal tasks, focusing on temporal alignment and accuracy.

**Results**  
LegalSearch-R1, with 7 billion parameters, demonstrates significant improvements over state-of-the-art deep learning frameworks and specialized legal LLMs. The model achieves performance gains ranging from 12.9% to 29.8% across 13 legal tasks compared to existing baselines. Notably, it excels in temporal consistency, outperforming benchmarks by 57.7% to 80.3%. Additionally, the model exhibits robust out-of-domain generalization, indicating its effectiveness across varied legal contexts and tasks.

**Limitations**  
The authors acknowledge that while LegalSearch-R1 improves temporal consistency, it may still be limited by the quality and comprehensiveness of the temporally-indexed training data. Furthermore, the reliance on reinforcement learning may introduce challenges in convergence and stability during training. The paper does not address potential biases in the underlying datasets or the implications of model interpretability in legal contexts, which are critical for deployment in real-world applications.

**Why it matters**  
This work has significant implications for the development of legal AI systems, particularly in ensuring that legal reasoning adheres to the temporal constraints inherent in law. By addressing the temporal bias in LLMs, LegalSearch-R1 paves the way for more reliable legal search tools that can provide accurate citations and reasoning aligned with the current legal context. This advancement could enhance the efficacy of legal research, support legal practitioners in case analysis, and ultimately contribute to more just legal outcomes.

Authors: Wei Fan, Yining Zhou, Mufan Zhang, Yanbing Weng, Yiran HU, Tianshi Zheng, Baixuan Xu, Chunyang Li et al.  
Source: arXiv:2605.25920  
URL: https://arxiv.org/abs/2605.25920v1
