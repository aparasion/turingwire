---
title: "Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents"
date: 2026-05-27 15:37:02 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28629v1"
arxiv_id: "2605.28629"
authors: ["Zheng Wu", "Pengzhou Cheng", "Zongru Wu", "Yuan Guo", "Tianjie Ju", "Aston Zhang"]
slug: mobile-aptus-confidence-driven-proactive-and-robust-interact
summary_word_count: 397
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing interactive mobile-using agents that rely on multimodal large language models (MLLMs) for task execution. Specifically, it identifies the issues of over-execution, where agents attempt to complete tasks beyond their capabilities, and over-soliciting, where they excessively request human intervention. The authors propose a solution to these problems through a novel framework, Mobile-Aptus, which is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of Mobile-Aptus is a two-stage universal confidence integration framework designed to enhance the interaction capabilities of MLLM-based mobile agents. The first stage, interaction capability empowerment, involves supervised fine-tuning where agents are trained to output both actions and corresponding confidence scores. The second stage, confidence bias correction, refines the accuracy of these confidence scores by integrating semantic similarity retrieval with direct preference optimization. This dual-stage approach aims to balance proactive task execution with appropriate levels of human interaction, thereby reducing both over-execution and over-soliciting behaviors.

**Results**  
Mobile-Aptus demonstrates significant improvements over existing baselines across four established benchmarks: OS-Kairos, AITZ, Meta-GUI, and AndroidControl. In offline evaluations, Mobile-Aptus achieves an average task success rate improvement of over 17% compared to baseline models. In dynamic real-world experiments, it surpasses the best baseline by 26% in task success rate while maintaining a low intervention requirement of only 0.64 intervention steps per instruction. These results indicate a robust enhancement in the operational efficiency and reliability of mobile-using agents.

**Limitations**  
The authors acknowledge that the proposed framework may still be susceptible to certain edge cases where confidence estimation could fail, potentially leading to suboptimal task execution. Additionally, the reliance on supervised fine-tuning may limit the generalizability of the model to unseen tasks or environments. The paper does not address the computational overhead introduced by the dual-stage training process, which could impact deployment in resource-constrained mobile environments.

**Why it matters**  
The implications of this work are significant for the development of autonomous mobile agents, particularly in applications requiring reliable human-agent interaction. By effectively addressing the dual challenges of over-execution and over-soliciting, Mobile-Aptus paves the way for more robust and user-friendly mobile agents capable of operating in complex, dynamic environments. This research could inform future studies on confidence-driven decision-making in AI systems, enhancing their applicability in real-world scenarios.

Authors: Zheng Wu, Pengzhou Cheng, Zongru Wu, Yuan Guo, Tianjie Ju, Aston Zhang, Gongshen Liu, Zhuosheng Zhang  
Source: arXiv:2605.28629  
URL: https://arxiv.org/abs/2605.28629v1
