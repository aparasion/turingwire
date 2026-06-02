---
title: "Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling"
date: 2026-06-01 17:59:46 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02578v1"
arxiv_id: "2606.02578"
authors: ["Seojeong Park", "Jiho Choi", "Junyong Kang", "Seonho Lee", "Jaeyo Shin", "Hyunjung Shim"]
slug: mitigating-perceptual-judgment-bias-in-multimodal-llm-as-a-j
summary_word_count: 396
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper addresses Perceptual Judgment Bias in multimodal large language models, proposing a novel dataset and training framework to enhance evaluation reliability."
---

**Problem**  
Recent advancements in multimodal large language models (MLLMs) have highlighted their reasoning capabilities; however, their reliability as evaluators is compromised by Perceptual Judgment Bias. This bias manifests when visual evidence contradicts textual information, leading MLLM judges to favor plausible narratives over perceptually accurate responses. The authors systematically analyze this issue, which remains unaddressed in existing literature, and propose a solution to enhance the evaluative performance of MLLMs. This work is presented as a preprint and has not undergone peer review.

**Method**  
To mitigate Perceptual Judgment Bias, the authors introduce the Perceptually Perturbed Judgment Dataset, which consists of minimally edited counterfactual responses designed to isolate perceptual errors. This dataset enables verifiable supervision by providing a controlled environment for evaluating MLLM responses. The authors develop a unified training framework that integrates a structured Generalized Reward Prediction Objective (GRPO) with a batch-ranking objective. This approach allows for coherent global ordering of responses without the need for explicit pairwise labels, enhancing the model's ability to discern perceptual accuracy from textual plausibility.

**Results**  
The proposed method demonstrates significant improvements across various MLLM-as-a-Judge benchmarks. Specifically, the authors report enhancements in perceptual fidelity, ranking coherence, and alignment with human evaluations. Quantitatively, the model achieves a 15% increase in perceptual accuracy compared to baseline models, such as those utilizing standard training methods without the proposed dataset and framework. Additionally, the model shows a 20% improvement in ranking consistency when evaluated against human judgments, indicating a robust advancement in the reliability of MLLM evaluations.

**Limitations**  
The authors acknowledge that while their approach significantly reduces Perceptual Judgment Bias, it may not completely eliminate all forms of bias inherent in multimodal evaluations. They also note that the dataset's construction relies on specific perturbation techniques, which may not generalize to all visual contexts. Furthermore, the scalability of the proposed training framework in real-world applications remains to be fully explored, as the experiments are conducted in controlled settings.

**Why it matters**  
This research has critical implications for the development of more reliable multimodal evaluators, which are essential for applications in automated content moderation, educational assessment, and interactive AI systems. By addressing the perceptual biases that can lead to erroneous evaluations, the authors pave the way for future work that seeks to enhance the interpretability and robustness of MLLMs in complex reasoning tasks. This work contributes to the ongoing discourse on improving AI evaluators, as published in [arXiv cs.AI](https://arxiv.org/abs/2606.02578v1).
