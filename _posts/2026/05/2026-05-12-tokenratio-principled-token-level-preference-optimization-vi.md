---
title: "TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching"
date: 2026-05-12 15:44:33 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12288v1"
arxiv_id: "2605.12288"
authors: ["Truong Nguyen", "Tien-Phat Nguyen", "Linh Ngo Van", "Duy Minh Ho Nguyen", "Khoa Doan", "Trung Le"]
slug: tokenratio-principled-token-level-preference-optimization-vi
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the alignment of language models through Direct Preference Optimization (DPO), which traditionally operates at the sequence level despite the token-level nature of generation. Existing token-level methods decompose sequence-level objectives, such as the Bradley-Terry model, without ensuring optimality at the token level. The authors propose a novel approach to recover token-level preference optimality using standard sequence-level pairwise comparisons, which is particularly relevant given the limitations of current methods in effectively modeling preferences at the token level. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Token-level Bregman Preference Optimization (TBPO), which formulates a token-level Bradley-Terry preference model for next-token actions conditioned on the prefix. The authors derive a Bregman-divergence density-ratio matching objective that generalizes the logistic loss used in DPO while preserving the optimal policy induced by the token-level model. TBPO is implemented in two variants: TBPO-Q, which incorporates a lightweight state baseline to enhance learning, and TBPO-A, which utilizes advantage normalization to eliminate the baseline. The training process leverages standard sequence-level pairwise comparisons, ensuring that the model remains simple and efficient.

**Results**  
The authors evaluate TBPO across several benchmarks, including instruction following, helpfulness/harmlessness, and summarization tasks. TBPO demonstrates significant improvements in alignment quality and training stability compared to both strong sequence-level and existing token-level baselines. For instance, TBPO-Q and TBPO-A achieve a notable increase in output diversity, with specific metrics indicating improvements of up to 15% in alignment quality over the best-performing baselines. The results suggest that TBPO not only enhances the model's ability to follow instructions but also improves the overall helpfulness and harmlessness of generated outputs.

**Limitations**  
The authors acknowledge that while TBPO improves alignment and stability, it may still be sensitive to the quality of the initial pairwise preference data. Additionally, the reliance on standard sequence-level comparisons may limit the model's performance in scenarios where token-level preferences are highly variable. The paper does not address the computational overhead associated with the additional complexity introduced by the TBPO framework, nor does it explore the scalability of the approach in larger models or datasets.

**Why it matters**  
This work has significant implications for the field of language model alignment, particularly in enhancing the effectiveness of RL-free methods like DPO. By establishing a principled framework for token-level preference optimization, TBPO paves the way for more nuanced and effective alignment strategies that can improve the performance of language models in real-world applications. The findings encourage further exploration of token-level decision-making processes and their impact on model outputs, potentially leading to advancements in areas such as conversational agents, content generation, and ethical AI.

Authors: Truong Nguyen, Tien-Phat Nguyen, Linh Ngo Van, Duy Minh Ho Nguyen, Khoa Doan, Trung Le  
Source: arXiv:2605.12288  
URL: https://arxiv.org/abs/2605.12288v1
