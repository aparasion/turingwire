---
title: "VL-DPO: Vision-Language-Guided Finetuning for Preference-Aligned Autonomous Driving"
date: 2026-05-19 16:36:34 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20082v1"
arxiv_id: "2605.20082"
authors: ["Zhefan Xu", "Ghassen Jerfel", "Marina Haliem", "Qi Zhao", "Jeonhyung Kang", "Khaled S. Refaat"]
slug: vl-dpo-vision-language-guided-finetuning-for-preference-alig
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in aligning autonomous driving models with human driving preferences, which is not adequately captured by traditional imitation learning objectives. The authors highlight that while large-scale pretraining of motion forecasting models has shown strong performance, it lacks the nuanced understanding of human preferences in driving behavior. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the VL-DPO framework, which integrates vision-language models (VLMs) to enhance the finetuning of motion forecasting models. The approach utilizes a VLM as a zero-shot reasoner to generate preference pairs from the rollouts of a pretrained model. These preference pairs are then employed to finetune the model using Direct Preference Optimization (DPO). The authors specifically finetune their models on the Waymo Open End-to-End Driving Dataset (WOD-E2E). The architecture details of the VLM and the specific configurations for DPO are not disclosed, but the method emphasizes the use of human-like preference generation to improve model alignment with human driving behavior.

**Results**  
The VL-DPO model demonstrates significant improvements over the baseline pretrained model. Specifically, it achieves an 11.94% increase in the rater feedback score (RFS) and a 10.01% reduction in average displacement error (ADE). These metrics indicate that the model's trajectory selections are more aligned with human preferences compared to the baseline, suggesting that the integration of VLMs effectively enhances the model's performance in preference alignment tasks.

**Limitations**  
The authors acknowledge that the reliance on a VLM for generating preference pairs may introduce biases inherent to the VLM's training data, which could affect the quality of the generated preferences. Additionally, the paper does not address the scalability of the approach to other datasets or driving scenarios beyond the WOD-E2E. The potential computational overhead associated with using VLMs for preference generation is also not discussed, which could impact real-time applications in autonomous driving.

**Why it matters**  
The implications of this work are significant for the field of autonomous driving, as it provides a novel approach to aligning motion forecasting models with human preferences, potentially leading to safer and more intuitive driving behaviors. By leveraging advances in vision-language models, this research opens avenues for further exploration in preference learning and human-centric AI systems in autonomous vehicles. The findings could influence future work on integrating human feedback into machine learning models, particularly in dynamic and complex environments.

Authors: Zhefan Xu, Ghassen Jerfel, Marina Haliem, Qi Zhao, Jeonhyung Kang, Khaled S. Refaat  
Source: arXiv:2605.20082  
URL: https://arxiv.org/abs/2605.20082v1
