---
title: "Skill-Conditioned Gated Self-Distillation for LLM Reasoning"
date: 2026-05-27 17:49:52 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28791v1"
arxiv_id: "2605.28791"
authors: ["Jiazhen Huang", "Xiao Chen", "Xiao Luo", "Yong Dai", "Senkang Hu", "Yuzhi Zhao"]
slug: skill-conditioned-gated-self-distillation-for-llm-reasoning
summary_word_count: 427
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing on-policy self-distillation (SD) methods for large language models (LLMs) that rely on trusted privileged information (PI), such as reference answers or successful traces. The authors propose a novel approach that utilizes a skill bank derived from experience, which may contain irrelevant or misleading information. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Skill-Conditioned Gated Self-Distillation (SGSD), which reformulates skill-based SD as a process of teacher hypothesis validation rather than simple imitation. SGSD operates by retrieving skill-mistake pairs and constructing a multi-teacher pool. Each teacher in this pool evaluates the same student rollout based on a plain prompt. The validation process involves assessing each teacher's stance: if a teacher supports a success or suppresses a failure, it provides positive supervision; otherwise, the signal is reversed. The core technical contribution is a robust gated objective that distills informative disagreements between teachers and the student while mitigating the influence of uncertain or extreme signals. The training process leverages a diverse set of mathematical reasoning benchmarks, including AIME24, AIME25, and HMMT25.

**Results**  
SGSD demonstrates significant improvements over the baseline methods. Specifically, on the Qwen3-1.7B model, SGSD achieves an average performance increase of 6.2% over the Gradient Reinforcement Policy Optimization (GRPO) method and 1.7% over the answer-conditioned On-Policy Self-Distillation (OPSD) method across the aforementioned benchmarks. These results indicate that SGSD effectively enhances reasoning capabilities in LLMs under the assumption of weaker PI.

**Limitations**  
The authors acknowledge that the reliance on a skill bank may introduce noise due to the potential irrelevance or misleading nature of the retrieved skills. Additionally, the performance gains are evaluated on specific mathematical reasoning tasks, which may not generalize to other domains or tasks. The paper does not address the computational overhead associated with maintaining and querying the skill bank, nor does it explore the scalability of the multi-teacher pool in larger models.

**Why it matters**  
The implications of this work are significant for the development of more robust LLMs capable of reasoning under uncertainty. By shifting the paradigm from unconditional imitation to hypothesis validation, SGSD opens avenues for leveraging diverse and potentially noisy information sources in training. This approach could enhance the adaptability of LLMs in various applications, particularly in scenarios where high-quality supervision is scarce or expensive to obtain. Furthermore, the findings encourage further exploration of skill-based learning frameworks, potentially leading to more efficient and effective self-distillation techniques in the future.

Authors: Jiazhen Huang, Xiao Chen, Xiao Luo, Yong Dai, Senkang Hu, Yuzhi Zhao  
Source: arXiv:2605.28791  
URL: [https://arxiv.org/abs/2605.28791v1](https://arxiv.org/abs/2605.28791v1)
