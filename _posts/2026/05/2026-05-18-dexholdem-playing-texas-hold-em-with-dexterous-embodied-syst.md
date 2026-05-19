---
title: "DexHoldem: Playing Texas Hold'em with Dexterous Embodied System"
date: 2026-05-18 17:51:34 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18727v1"
arxiv_id: "2605.18727"
authors: ["Feng Chen", "Tianzhe Chu", "Li Sun", "Pei Zhou", "Zhuxiu Xu", "Shenghua Gao"]
slug: dexholdem-playing-texas-hold-em-with-dexterous-embodied-syst
summary_word_count: 471
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating embodied systems on real dexterous hardware, specifically in the context of complex tasks like Texas Hold'em. Existing benchmarks often focus on isolated skills rather than the integration of perception, action, and decision-making in dynamic environments. The authors introduce DexHoldem, a novel benchmark that assesses the performance of agents in a real-world setting, requiring them to perceive a changing tabletop scene, select appropriate actions, and execute them with dexterous manipulation. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
DexHoldem comprises a comprehensive framework that includes 1,470 teleoperated demonstrations across 14 manipulation primitives relevant to Texas Hold'em. The benchmark is divided into two main components: a standardized physical policy benchmark and an agentic perception benchmark. The physical policy benchmark evaluates the agents' ability to execute manipulation tasks, while the agentic perception benchmark tests the agents' capability to recover the structured game state necessary for decision-making. The authors report performance metrics for various policies, including $π_{0.5}$ and $π_0$, which are evaluated based on task completion rates and scene-preserving success rates. The training compute details are not disclosed, but the framework emphasizes the integration of perception and action in a shared physical environment.

**Results**  
The results indicate that the policy $π_{0.5}$ achieves the highest task completion rate of 61.2% on primitive execution tasks. Both $π_{0.5}$ and $π_0$ achieve a scene-preserving success rate of 47.5%. In terms of agentic perception, the model Opus 4.7 achieves a strict problem-level accuracy of 34.3%, while GPT 5.5 demonstrates superior average field-wise accuracy at 66.8%. These results highlight a significant gap between isolated visual capabilities and the comprehensive recovery of routing-relevant state information, underscoring the challenges in integrating perception with action in embodied systems.

**Limitations**  
The authors acknowledge several limitations, including the reliance on teleoperated demonstrations, which may not fully capture the complexities of autonomous decision-making in real-world scenarios. Additionally, the performance metrics reveal that the accuracy of state recovery remains low, indicating that current models struggle with the integration of perception and action. The paper does not address the scalability of the benchmark or the potential for generalization to other dexterous manipulation tasks beyond Texas Hold'em.

**Why it matters**  
DexHoldem represents a significant advancement in the evaluation of embodied systems, providing a structured approach to assess dexterous manipulation and agentic perception in a shared physical environment. The implications of this work extend to the development of more capable embodied agents that can operate in complex, dynamic settings, enhancing the understanding of how perception and action can be effectively integrated. This benchmark could serve as a foundation for future research in embodied AI, particularly in tasks requiring nuanced decision-making and manipulation skills.

Authors: Feng Chen, Tianzhe Chu, Li Sun, Pei Zhou, Zhuxiu Xu, Shenghua Gao, Yuexiang Zhai, Yanchao Yang et al.  
Source: arXiv:2605.18727  
URL: https://arxiv.org/abs/2605.18727v1
