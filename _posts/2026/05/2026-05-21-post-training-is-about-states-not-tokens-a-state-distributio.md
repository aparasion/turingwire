---
title: "Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation"
date: 2026-05-21 17:03:22 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22731v1"
arxiv_id: "2605.22731"
authors: ["Dong Nie"]
slug: post-training-is-about-states-not-tokens-a-state-distributio
summary_word_count: 479
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a gap in the understanding of post-training methods for large language models (LLMs), specifically focusing on the state distribution rather than solely on loss functions. Traditional analyses of supervised fine-tuning (SFT), reinforcement learning (RL), and on-policy distillation (OPD) have primarily centered on the optimization objectives (e.g., maximum likelihood, policy gradients). The authors propose that the state distribution—defined as the combination of prompts and generated text—plays a critical role in the effectiveness of these training paradigms. This perspective is particularly relevant as it may influence how practitioners approach model fine-tuning and evaluation.

**Method**  
The authors formalize post-training as a process of state-distribution shaping. They conduct a controlled small-scale study using the Qwen3-0.6B-Base model on the GSM8K dataset, with TruthfulQA and MMLU serving as retention evaluation benchmarks. The study contrasts three training paradigms: a mild SFT run, a stress SFT run, and OPD from a degraded SFT teacher. The mild SFT is characterized by minimal changes to the model, while the stress SFT involves more aggressive training, leading to potential forgetting. The OPD approach utilizes the SFT teacher as the sole supervision source, emphasizing the importance of the state distribution induced by the current learner. The training compute details are not disclosed, but the experiments are designed to isolate the effects of state distribution on performance.

**Results**  
The findings reveal three key phenomena:  
1. The mild SFT run yields a significant improvement on GSM8K with minimal forgetting, indicating effective retention of prior knowledge.  
2. The stress SFT run results in substantial retention loss, demonstrating the risks associated with aggressive fine-tuning.  
3. OPD from a degraded SFT teacher outperforms the teacher itself across all evaluated benchmarks (GSM8K, TruthfulQA, and MMLU), suggesting that the state distribution from the learner can enhance performance even when the teacher is suboptimal.  
4. A lightweight on-policy RL run also improves GSM8K while maintaining retention, further supporting the state-centric view.

**Limitations**  
The authors acknowledge that their study is limited by its small scale and the specific model used (Qwen3-0.6B-Base). The generalizability of the results to larger models or different architectures remains untested. Additionally, the controlled nature of the experiments may not fully capture the complexities of real-world applications. The authors do not address potential overfitting to the GSM8K dataset or the implications of state distribution on other tasks beyond those evaluated.

**Why it matters**  
This work has significant implications for the design and evaluation of post-training strategies in LLMs. By shifting the focus from loss functions to state distributions, it encourages researchers and practitioners to reconsider how they structure training data and supervision signals. This perspective could lead to more effective fine-tuning methodologies that prioritize the quality and relevance of training states, potentially improving model performance and retention across various tasks. The findings may also inform future research on the interplay between state distribution and model generalization.

Authors: Dong Nie  
Source: arXiv:2605.22731  
URL: https://arxiv.org/abs/2605.22731v1
