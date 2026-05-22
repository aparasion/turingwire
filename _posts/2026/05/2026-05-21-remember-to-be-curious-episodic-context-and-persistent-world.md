---
title: "Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration"
date: 2026-05-21 17:58:06 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22814v1"
arxiv_id: "2605.22814"
authors: ["Lily Goli", "Justin Kerr", "Daniele Reda", "Alec Jacobson", "Andrea Tagliasacchi", "Angjoo Kanazawa"]
slug: remember-to-be-curious-episodic-context-and-persistent-world
summary_word_count: 414
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of curiosity-driven reinforcement learning (RL) in complex, photorealistic 3D environments, where agents often become trapped in local loops and fail to explore effectively. The authors identify a gap in the literature regarding the need for spatial persistence and episodic context in the agent's exploration strategy, which is crucial for navigating long-horizon tasks with sparse rewards.

**Method**  
The authors propose a novel architecture that integrates an online 3D reconstruction as a persistent world model, allowing the agent to maintain an updated representation of its environment. The agent's policy is designed as a sequence model that processes RGB observations to retain episodic context. This dual approach enables the agent to explore effectively during training while relying solely on RGB frames for navigation during deployment. The training is conducted on the HM3D dataset, leveraging intrinsic rewards derived from the mismatch between the agent's predictive model and the actual environment. The authors do not disclose specific training compute details but emphasize the end-to-end nature of their policy, which facilitates adaptation to various downstream tasks.

**Results**  
The proposed method demonstrates significant performance improvements over baseline approaches. Specifically, the curiosity-driven agent outperforms RL-based active mapping baselines on the HM3D dataset. Additionally, it exhibits zero-shot generalization capabilities to the Gibson dataset and AI-generated environments. The end-to-end policy also shows superior performance in downstream tasks, such as apple picking and image-goal navigation, compared to from-scratch baselines, although specific metrics and effect sizes are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their approach may still struggle with certain aspects of exploration in highly dynamic environments or those with rapidly changing states. They do not address potential computational inefficiencies associated with maintaining an online 3D reconstruction or the scalability of their method to larger, more complex environments. Furthermore, the reliance on RGB observations may limit performance in scenarios where depth or additional sensory information is critical.

**Why it matters**  
This work has significant implications for the field of reinforcement learning, particularly in enhancing exploration strategies in complex environments. By demonstrating the importance of spatial persistence and episodic context, the authors provide a framework that could be applied to various tasks beyond 3D exploration, potentially improving the efficiency and effectiveness of RL agents in real-world applications. The ability to generalize to unseen environments and adapt to downstream tasks suggests a pathway for developing more robust and versatile AI systems.

Authors: Lily Goli, Justin Kerr, Daniele Reda, Alec Jacobson, Andrea Tagliasacchi, Angjoo Kanazawa  
Source: arXiv:2605.22814  
URL: https://arxiv.org/abs/2605.22814v1
