---
title: "BAMI: Training-Free Bias Mitigation in GUI Grounding"
date: 2026-05-07 17:59:31 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06664v1"
arxiv_id: "2605.06664"
authors: ["Borui Zhang", "Bo Zhang", "Bo Wang", "Wenzhao Zheng", "Yuhao Cheng", "Liang Tang"]
slug: bami-training-free-bias-mitigation-in-gui-grounding
summary_word_count: 408
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing GUI grounding models, particularly in complex scenarios exemplified by the ScreenSpot-Pro benchmark. The authors identify two primary sources of error: precision bias due to high image resolution and ambiguity bias stemming from intricate interface elements. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Bias-Aware Manipulation Inference (BAMI) framework, which operates in a training-free manner. BAMI employs two manipulations: coarse-to-fine focus and candidate selection. The coarse-to-fine focus method refines the attention mechanism to prioritize relevant interface elements, while candidate selection narrows down potential actions based on contextual cues. The authors utilize the Masked Prediction Distribution (MPD) attribution method to analyze error sources and validate the effectiveness of BAMI. The framework is designed to enhance the performance of existing models without requiring additional training data or retraining, making it particularly useful for real-time applications.

**Results**  
BAMI demonstrates significant performance improvements on the ScreenSpot-Pro benchmark. Specifically, when applied to the TianXi-Action-7B model, the accuracy increases from 51.9% to 57.8%, representing an effect size of approximately 11.3%. The authors conduct ablation studies to confirm the robustness of BAMI across various parameter configurations, indicating that the method consistently enhances model performance regardless of the specific architecture used.

**Limitations**  
The authors acknowledge that while BAMI effectively mitigates biases in GUI grounding, it may not address all forms of bias present in different contexts or datasets. Additionally, the training-free nature of the method may limit its applicability in scenarios where model retraining could yield better performance. The paper does not explore the computational efficiency of BAMI in terms of inference time or resource consumption, which could be critical for deployment in resource-constrained environments.

**Why it matters**  
The implications of this work are significant for the development of robust GUI agents capable of executing complex tasks in real-world applications. By providing a training-free solution to bias mitigation, BAMI opens avenues for enhancing the reliability of GUI grounding models without the need for extensive retraining or additional data collection. This could accelerate the deployment of intelligent agents in various domains, including customer service, automation, and accessibility technologies. The findings encourage further exploration of bias mitigation techniques in other areas of machine learning, particularly where high-dimensional input data and ambiguous contexts are prevalent.

Authors: Borui Zhang, Bo Zhang, Bo Wang, Wenzhao Zheng, Yuhao Cheng, Liang Tang, Yiqiang Yan, Jie Zhou et al.  
Source: arXiv cs.AI  
URL: https://arxiv.org/abs/2605.06664v1
