---
title: "SafeDiffusion-R1: Online Reward Steering for Safe Diffusion Post-Training"
date: 2026-05-18 17:50:04 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18719v1"
arxiv_id: "2605.18719"
authors: ["Komal Kumar", "Ankan Deria", "Abhishek Basu", "Fahad Shamshad", "Hisham Cholakkal", "Karthik Nandakumar"]
slug: safediffusion-r1-online-reward-steering-for-safe-diffusion-p
summary_word_count: 469
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing methods for mitigating unsafe content in diffusion models, which typically rely on expensive supervised datasets, such as unsafe-text paired with safe-image ground truth or positive/negative image pairs. These methods are impractical for large-scale applications. Additionally, offline reinforcement learning and supervised fine-tuning approaches suffer from catastrophic forgetting, leading to degraded generation quality. The authors propose a novel online reinforcement learning framework to overcome these challenges. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce an online reinforcement learning framework utilizing Group Relative Policy Optimization (GRPO) to post-train diffusion models on both negative and positive text prompts. A key innovation is the steering reward mechanism, which leverages the properties of CLIP embeddings to guide text representations toward positive safety directions while steering away from negative ones in the embedding space. This approach allows the model to learn from a diverse set of prompts, including explicit unsafe content, without experiencing catastrophic forgetting. The training process is designed to be efficient, eliminating the need for fine-tuning specialized safe/unsafe reward models.

**Results**  
The proposed method demonstrates significant improvements in safety and generation quality. Specifically, the model reduces inappropriate content to 18.07%, compared to 48.9% for the baseline Stable Diffusion v1.4. For nudity detection, the model achieves a count of 15 instances, a substantial reduction from the baseline of 646. Additionally, the compositional generation quality improves from 42.08% to 47.83% on the GenEval benchmark. Notably, these safety improvements generalize across out-of-domain unsafe prompts spanning seven harm categories, achieving state-of-the-art performance without the need for supervised paired data or reward tuning.

**Limitations**  
The authors acknowledge that their approach may still be sensitive to the quality of the prompts used during training, as the steering mechanism relies on the inherent properties of CLIP embeddings. They do not address potential biases in the CLIP embeddings themselves, which could affect the steering process. Furthermore, the scalability of the online reinforcement learning framework in real-world applications remains to be evaluated. The paper does not discuss the computational resources required for training, which could be a concern for practitioners with limited access to high-performance computing.

**Why it matters**  
This work has significant implications for the deployment of diffusion models in safety-critical applications, such as content generation and moderation. By providing a scalable and efficient method for reducing unsafe content without the need for extensive supervised datasets, the authors pave the way for more responsible AI systems. The ability to generalize safety improvements across diverse prompts enhances the robustness of generative models, making them more suitable for real-world applications. This research could inspire further exploration into online reinforcement learning techniques and their integration with existing generative models.

Authors: Komal Kumar, Ankan Deria, Abhishek Basu, Fahad Shamshad, Hisham Cholakkal, Karthik Nandakumar  
Source: arXiv cs.CV  
URL: [https://arxiv.org/abs/2605.18719v1](https://arxiv.org/abs/2605.18719v1)
