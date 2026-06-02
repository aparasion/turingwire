---
title: "VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization"
date: 2026-06-01 17:54:26 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.02564v1"
arxiv_id: "2606.02564"
authors: ["Junhao Cheng", "Liang Hou", "Tianxiong Zhong", "Xin Tao", "Pengfei Wan", "Kun Gai"]
slug: vlms-are-good-teachers-for-video-reasoning-via-adaptive-test
summary_word_count: 377
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces a novel approach where Vision-Language Models act as teachers for Video Generation Models, enhancing video reasoning capabilities through adaptive optimization."
---

**Problem**  
The paper addresses the limitations of existing Video Generation Models (VGMs) in executing task-specific reasoning due to their inability to understand intricate spatiotemporal instructions. While prior work has attempted to utilize Vision-Language Models (VLMs) as pre-solvers to generate textual guidance, these descriptions often lack the necessary detail for VGMs to follow complex instructions effectively. This work is a preprint and has not undergone peer review.

**Method**  
The authors propose a paradigm shift where VLMs are utilized as "teachers" rather than solvers. The VLM teacher extracts task-specific rules to create differentiable rewards that guide the VGM Reasoner. This is achieved through test-time online optimization of a lightweight Low-Rank Adaptation (LoRA) module, which allows for adaptive adjustments during inference. The method leverages the VLM's strong perception capabilities to evaluate the satisfaction of process constraints and the achievement of final goals, thereby enhancing the reasoning capabilities of VGMs beyond their intrinsic limitations.

**Results**  
The proposed method was evaluated on two benchmarks: the symbolic VBVR-Bench and the general-purpose RULER-Bench. The results indicate a significant performance improvement, with an average gain of 16.7 points over the baseline. Specifically, it outperformed the VLM-as-Solver paradigm by 0.4 points and the Best-of-N scaling approach by 2.2 points, all while maintaining comparable test-time computational costs. These results demonstrate the effectiveness of integrating VLMs as teachers in enhancing video reasoning tasks.

**Limitations**  
The authors acknowledge that their approach may still be limited by the inherent capabilities of the VGMs and the complexity of the tasks. They do not address potential scalability issues when applying this method to more complex or diverse reasoning scenarios. Additionally, the reliance on differentiable rewards may introduce challenges in environments where task-specific rules are not easily quantifiable.

**Why it matters**  
This work has significant implications for the field of video reasoning, suggesting that the role of VLMs can be effectively redefined to improve the performance of VGMs. By demonstrating that VLMs can serve as adaptive teachers, the authors open avenues for further research into hybrid models that combine the strengths of both VLMs and VGMs. This approach could lead to more robust systems capable of handling complex reasoning tasks in dynamic environments, as discussed in related literature on multimodal learning and reasoning. For further details, see the full paper available on [arXiv](https://arxiv.org/abs/2606.02564v1).
