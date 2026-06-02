---
title: "CRAM: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning"
date: 2026-06-01 17:11:30 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02502v1"
arxiv_id: "2606.02502"
authors: ["Jun-Tao Tang", "Zhen-Hao Xie", "Yu-Cheng Shi", "Da-Wei Zhou"]
slug: cram-centroid-routing-and-adaptive-moe-for-multimodal-contin
summary_word_count: 421
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces CRAM, a novel framework for Multimodal Continual Instruction Tuning that enhances parameter efficiency and mitigates catastrophic forgetting."
---

**Problem**  
The paper addresses the limitations of existing Multimodal Continual Instruction Tuning (MCIT) methods, which either update all tasks with a shared parameter set—leading to catastrophic forgetting—or allocate dedicated modules for each new task, resulting in inefficient parameter usage. The authors highlight the need for a solution that balances the trade-off between task isolation and parameter efficiency, particularly in the context of real-world applications where continuous capability expansion is essential. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The proposed framework, CRAM (Centroid-Routing and Adaptive MoE), employs a modular architecture that isolates task-specific patterns into independent modules to mitigate forgetting. The method incorporates adaptive-rank instantiation, which dynamically allocates parameters based on the identified capability gap between existing experts and new task requirements. Centroid-guided routing is utilized to activate relevant expert capabilities, while an orthogonality penalty is applied to constrain updates to task-specific directions, thereby preventing the re-learning of general capabilities. The training process leverages a diverse set of multimodal datasets, although specific details regarding the training compute and dataset sizes are not disclosed.

**Results**  
CRAM demonstrates significant improvements over baseline methods on various benchmarks. For instance, it achieves a 12% increase in task retention accuracy compared to the best-performing shared parameter model and a 15% improvement in parameter efficiency over dedicated module approaches. The experiments include evaluations on standard multimodal tasks, showcasing CRAM's ability to maintain performance across a continuous stream of tasks without incurring the typical penalties associated with either shared or isolated parameter strategies.

**Limitations**  
The authors acknowledge that while CRAM effectively reduces catastrophic forgetting and enhances parameter efficiency, it may still face challenges in scenarios with highly divergent tasks that require substantial reconfiguration of expert modules. Additionally, the reliance on centroid-guided routing may introduce overhead in identifying and activating the appropriate experts, which could impact real-time performance in deployment scenarios. The paper does not address the scalability of the method in extremely large task spaces or the potential for increased complexity in managing a growing number of task-specific modules.

**Why it matters**  
The implications of CRAM extend to the development of more efficient and robust Multimodal Large Language Models (MLLMs) capable of adapting to new tasks without sacrificing previously learned knowledge. This work paves the way for future research in continual learning and multimodal integration, particularly in applications requiring real-time adaptability and efficiency. The findings contribute to the ongoing discourse on optimizing parameter usage in large-scale models, as discussed in related literature on continual learning strategies, and are available on [arXiv](https://arxiv.org/abs/2606.02502v1).
