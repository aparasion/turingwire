---
title: "PSK at SemEval-2026 Task 9: Multilingual Polarization Detection Using Ensemble Gemma Models with Synthetic Data Augmentation"
date: 2026-05-06 17:29:14 +0000
category: research
subcategory: evaluation_benchmarks
company: "Google DeepMind"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.05159v1"
arxiv_id: "2605.05159"
authors: ["Srikar Kashyap Pulipaka"]
slug: psk-at-semeval-2026-task-9-multilingual-polarization-detecti
summary_word_count: 422
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of multilingual polarization detection, a binary classification task across 22 languages, as part of SemEval-2026 Task 9. The authors identify a gap in existing methodologies for effectively leveraging large language models (LLMs) in this context, particularly in terms of data scarcity and model generalization across diverse languages. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose an ensemble approach utilizing two variants of the Gemma model (12B and 27B parameters) fine-tuned for each language using Low-Rank Adaptation (LoRA). They augment the training data with synthetic samples generated through three strategies: direct generation, paraphrasing, and contrastive pair creation, all facilitated by the GPT-4o-mini model. A multi-stage quality filtering pipeline is employed, which includes embedding-based deduplication to ensure the integrity of the synthetic data. The authors implement per-language threshold tuning on the development set, achieving F1 score improvements of 2 to 4% without the need for retraining. The final predictions are derived from a weighted ensemble of the two model sizes, with a strategy selection tailored to each language.

**Results**  
The proposed system achieves a mean macro-F1 score of 0.811 across all 22 languages, securing 2nd place overall among participating teams. Notably, the system ranks 1st in three languages and finishes in the top three for eight languages. In contrast, alternative architectures such as XLM-RoBERTa and Qwen3, which performed well on the development set, experienced significant F1 score drops of 30 to 50% on the test set, underscoring the importance of model robustness and generalization capabilities.

**Limitations**  
The authors acknowledge that their approach relies heavily on the quality of synthetic data, which may introduce biases or inaccuracies. Additionally, the performance of the ensemble method is contingent on the effectiveness of the threshold tuning process, which may not generalize well across all languages. The paper does not address the computational costs associated with training and fine-tuning large models, nor does it explore the potential limitations of the synthetic data generation strategies in depth.

**Why it matters**  
This work contributes to the field of multilingual NLP by demonstrating the efficacy of ensemble methods and synthetic data augmentation in polarization detection tasks. The findings highlight the critical role of model selection and generalization in achieving robust performance across diverse languages. The insights gained from this study can inform future research on multilingual model training and the development of more effective data augmentation techniques, ultimately enhancing the capabilities of LLMs in low-resource language settings.

Authors: Srikar Kashyap Pulipaka  
Source: arXiv:2605.05159  
URL: https://arxiv.org/abs/2605.05159v1
