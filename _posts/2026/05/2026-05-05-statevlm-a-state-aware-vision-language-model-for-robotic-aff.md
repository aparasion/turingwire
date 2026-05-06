---
title: "StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning"
date: 2026-05-05 16:19:02 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.03927v1"
arxiv_id: "2605.03927"
authors: ["Xiaowen Sun", "Matthias Kerzel", "Mengdi Li", "Xufeng Zhao", "Paul Striker", "Stefan Wermter"]
slug: statevlm-a-state-aware-vision-language-model-for-robotic-aff
summary_word_count: 423
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Vision-Language Models (VLMs) in robotic applications, particularly their deficiencies in numerical reasoning related to object detection and object-state localization. The authors highlight that while VLMs excel in various tasks, they struggle with tasks requiring precise numerical outputs, which is critical for robotic affordance reasoning. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel training strategy for VLMs, introducing the State-aware Vision-Language Model (StateVLM). The core technical contribution is the Auxiliary Regression Loss (ARL), which is integrated into the fine-tuning process of the model. This loss function utilizes box decoder outputs to enhance the model's ability to perform regression tasks related to object detection and state localization. During inference, the model maintains standard sequence prediction, allowing it to leverage both the regression capabilities and the language understanding inherent in VLMs. The training process involves fine-tuning on a newly introduced benchmark, the Object State Affordance Reasoning (OSAR), which consists of 1,172 scenes and 7,746 objects with corresponding bounding boxes.

**Results**  
StateVLM demonstrates significant improvements over baseline models. On adapted benchmarks (RefCOCO, RefCOCO+, and RefCOCOg), the introduction of ARL yields an average performance increase of 1.6%. More notably, on the OSAR benchmark, StateVLM with ARL achieves an average performance boost of 5.2% compared to models lacking ARL. The results indicate that ARL is particularly beneficial for complex affordance reasoning tasks, enhancing the consistency of model outputs in this context.

**Limitations**  
The authors acknowledge that the OSAR benchmark is newly introduced and may require further validation and expansion to ensure robustness. Additionally, the reliance on a specific training strategy may limit the generalizability of StateVLM to other tasks or domains not covered by the benchmark. The paper does not address potential computational overhead introduced by the ARL during training, which could impact scalability in real-world applications.

**Why it matters**  
This work has significant implications for the field of robotic affordance reasoning, as it provides a structured approach to integrating numerical reasoning into VLMs. By introducing ARL and the OSAR benchmark, the authors pave the way for future research that can build upon these advancements, potentially leading to more capable robotic systems that can understand and interact with their environments in a nuanced manner. The findings suggest that enhancing VLMs with regression capabilities can bridge the gap between perception and action in robotics, opening avenues for more sophisticated applications in autonomous systems.

Authors: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter  
Source: arXiv:2605.03927  
URL: [https://arxiv.org/abs/2605.03927v1](https://arxiv.org/abs/2605.03927v1)
