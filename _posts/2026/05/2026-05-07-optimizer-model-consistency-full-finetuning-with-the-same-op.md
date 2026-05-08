---
title: "Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less"
date: 2026-05-07 17:57:02 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06654v1"
arxiv_id: "2605.06654"
authors: ["Yuxing Liu", "Jianyu Wang", "Tong Zhang"]
slug: optimizer-model-consistency-full-finetuning-with-the-same-op
summary_word_count: 422
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a gap in understanding the impact of optimizer choice on the learning-forgetting tradeoff during the finetuning of large language models (LLMs). Specifically, it investigates how using the same optimizer for both pretraining and supervised finetuning (SFT) can mitigate the forgetting of knowledge acquired during pretraining. The authors introduce the concept of "optimizer-model consistency," which has not been extensively explored in the literature.

**Method**  
The authors conduct controlled experiments and theoretical analyses to substantiate their claims. They analyze the regularization effects of different optimizers on model activations, which influence the optimization landscape around pretrained checkpoints. The study specifically compares the performance of Muon and AdamW optimizers when applied consistently across both pretraining and SFT stages. The experiments reveal that the weight updates during SFT should adhere to specific structures that align with the regularization effects of the pretraining optimizer to minimize forgetting. The paper also includes a synthetic language modeling experiment to illustrate the limitations of Muon, particularly its propensity for rote memorization, which can hinder effective pattern acquisition in low-data scenarios.

**Results**  
The findings indicate that full finetuning with the same optimizer as pretraining results in significantly less forgetting while maintaining or improving performance on downstream tasks compared to other optimizers and methods like LoRA. While specific numerical results are not detailed in the abstract, the authors emphasize that the performance gains are substantial enough to warrant further investigation. The comparative analysis of Muon and AdamW highlights that Muon underperforms in reasoning tasks, suggesting that optimizer choice can critically influence task-specific performance.

**Limitations**  
The authors acknowledge that their findings are based on controlled experiments, which may not fully capture the complexities of real-world applications. They also note that while Muon shows weaknesses in certain contexts, it may still be beneficial in other scenarios not covered in their analysis. Additionally, the study does not explore the effects of other optimizers or hybrid approaches that could potentially yield better results. The implications of optimizer choice on model interpretability and generalization are also not addressed.

**Why it matters**  
This work has significant implications for the training of LLMs, particularly in optimizing the finetuning process. By establishing a clear link between optimizer consistency and reduced forgetting, the findings encourage researchers and practitioners to reconsider their choice of optimizers during the finetuning phase. This could lead to more effective training protocols that preserve knowledge from pretraining while adapting to new tasks, ultimately enhancing the performance and robustness of LLMs in diverse applications.

Authors: Yuxing Liu, Jianyu Wang, Tong Zhang  
Source: arXiv:2605.06654  
URL: https://arxiv.org/abs/2605.06654v1
