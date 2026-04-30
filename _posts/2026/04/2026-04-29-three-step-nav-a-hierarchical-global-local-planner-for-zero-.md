---
title: "Three-Step Nav: A Hierarchical Global-Local Planner for Zero-Shot Vision-and-Language Navigation"
date: 2026-04-29 17:55:05 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.26946v1"
arxiv_id: "2604.26946"
authors: ["Wanrong Zheng", "Yunhao Ge", "Laurent Itti"]
slug: three-step-nav-a-hierarchical-global-local-planner-for-zero-
summary_word_count: 452
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing zero-shot Vision-and-Language Navigation (VLN) agents powered by multimodal large language models (MLLMs), which often exhibit issues such as trajectory drift, premature halting, and low success rates in navigating unknown environments. The authors highlight that while MLLMs have made significant strides in vision-based navigation, they still struggle with maintaining accurate course tracking and effective planning. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Three-Step Nav framework, which employs a hierarchical global-local planning approach. The method consists of three distinct phases:  
1. **Look Forward**: This phase involves extracting global landmarks from the current visual input to create a coarse navigation plan.  
2. **Look Now**: In this phase, the model aligns the current visual observation with the next sub-goal, providing fine-grained guidance for navigation.  
3. **Look Backward**: This final step audits the entire trajectory to correct any accumulated drift before the agent halts.  
The framework is designed to integrate seamlessly into existing VLN pipelines without requiring gradient updates or task-specific fine-tuning, thus minimizing computational overhead. The authors do not disclose specific training compute or architectural details, focusing instead on the procedural aspects of the planner.

**Results**  
Three-Step Nav achieves state-of-the-art performance on the R2R-CE and RxR-CE datasets, outperforming previous zero-shot VLN agents. The paper reports a significant improvement in success rates, although specific numerical results and effect sizes are not detailed in the abstract. The authors claim that their method effectively reduces drift and enhances overall navigation success compared to baseline models, although exact comparisons to named baselines are not provided in the summary.

**Limitations**  
The authors acknowledge that their approach may still be susceptible to challenges inherent in zero-shot learning scenarios, such as the reliance on the quality of the visual input and the potential for misalignment between the language instructions and visual cues. Additionally, the method's performance in highly dynamic or cluttered environments is not explicitly tested. An obvious limitation not flagged by the authors is the lack of detailed quantitative results, which could provide clearer insights into the performance gains over existing methods.

**Why it matters**  
The implications of this work are significant for the field of autonomous navigation and robotics, particularly in enhancing the robustness of VLN agents in real-world applications. By addressing the common pitfalls of trajectory drift and premature halting, Three-Step Nav could pave the way for more reliable navigation systems that leverage MLLMs. This framework may also inspire further research into hierarchical planning methods and their integration with multimodal models, potentially leading to advancements in other areas of AI that require complex decision-making in uncertain environments.

Authors: Wanrong Zheng, Yunhao Ge, Laurent Itti  
Source: arXiv:2604.26946  
URL: https://arxiv.org/abs/2604.26946v1
