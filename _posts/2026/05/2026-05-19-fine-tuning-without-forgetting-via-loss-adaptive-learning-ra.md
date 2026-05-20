---
title: "Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates"
date: 2026-05-19 15:36:52 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20005v1"
arxiv_id: "2605.20005"
authors: ["Parjanya Prajakta Prashant", "Jiongli Zhu", "Aldan Creo", "Babak Salimi"]
slug: fine-tuning-without-forgetting-via-loss-adaptive-learning-ra
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the issue of catastrophic forgetting during the fine-tuning of large language models (LLMs) on new datasets, a gap that remains inadequately addressed in the literature. Existing strategies often suppress high-loss tokens to mitigate forgetting, which can hinder the learning of new tasks that may not have been well-represented during pretraining. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach called FINCH (Fine-Tuning with Loss-Adaptive Learning Rates), which introduces a loss-adaptive learning rate schedule. The core mechanism is based on the observation that per-step forgetting is influenced by the product of the learning rate and the square root of the current training loss. Specifically, FINCH reduces the learning rate for high-loss batches, thereby controlling forgetting without altering the fine-tuning objective. As the model converges, the learning rate is gradually increased. The authors do not disclose specific details regarding the architecture of the models used or the exact compute resources for training, focusing instead on the adaptive learning rate mechanism.

**Results**  
FINCH demonstrates a significant reduction in forgetting, achieving an average decrease of 93% across various benchmarks, including knowledge acquisition, science, and low-resource language adaptation tasks. Notably, on the Qwen3-4B knowledge acquisition benchmark, FINCH reduces the degradation in performance on the TruthfulQA task by a factor of 5 and successfully reverses degradation on the HaluEval benchmark. Additionally, the method maintains task performance comparable to standard fine-tuning, indicating that it effectively balances the trade-off between learning new tasks and retaining pre-existing knowledge.

**Limitations**  
The authors acknowledge that while FINCH significantly mitigates forgetting, it may not completely eliminate it, particularly in scenarios with extreme domain shifts or highly divergent tasks. They do not discuss the potential computational overhead introduced by the adaptive learning rate mechanism, which could impact training efficiency. Furthermore, the generalizability of FINCH across all types of LLMs and tasks remains to be validated, as the experiments are limited to specific benchmarks.

**Why it matters**  
The implications of this work are substantial for the field of transfer learning and fine-tuning in NLP. By demonstrating that learning-rate schedules can be effectively utilized to manage forgetting, this research opens avenues for further exploration into adaptive training methodologies. It suggests that future work could focus on refining learning rate strategies to enhance model robustness during fine-tuning, particularly in low-resource settings or when adapting to novel tasks. This could lead to more efficient use of pretrained models, ultimately improving their applicability across diverse applications.

Authors: Parjanya Prajakta Prashant, Jiongli Zhu, Aldan Creo, Babak Salimi  
Source: arXiv:2605.20005  
URL: [https://arxiv.org/abs/2605.20005v1](https://arxiv.org/abs/2605.20005v1)
