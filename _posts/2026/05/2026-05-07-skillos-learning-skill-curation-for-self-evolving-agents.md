---
title: "SkillOS: Learning Skill Curation for Self-Evolving Agents"
date: 2026-05-07 17:31:50 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06614v1"
arxiv_id: "2605.06614"
authors: ["Siru Ouyang", "Jun Yan", "Yanfei Chen", "Rujun Han", "Zifeng Wang", "Bhavana Dalvi Mishra"]
slug: skillos-learning-skill-curation-for-self-evolving-agents
summary_word_count: 460
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing LLM-based agents in learning from past interactions, particularly in the context of skill curation for self-evolving agents. Current methodologies either depend on manual curation, heuristic operations, or short-horizon training, which fail to effectively learn complex long-term curation policies from indirect and delayed feedback. The authors propose SkillOS as a solution to this gap, focusing on the automation of skill curation through reinforcement learning (RL). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
SkillOS introduces an experience-driven RL framework for skill curation in self-evolving agents. The architecture consists of two main components: a frozen agent executor that retrieves and applies skills, and a trainable skill curator that updates an external SkillRepo based on accumulated experience. The training process employs composite rewards designed to provide learning signals for curation, utilizing grouped task streams that reflect skill-relevant task dependencies. Earlier trajectories contribute to the SkillRepo, while subsequent related tasks evaluate the effectiveness of these updates. The authors do not disclose specific training compute details but emphasize the efficiency of their approach in learning from multi-turn and single-turn tasks.

**Results**  
SkillOS demonstrates significant improvements over both memory-free and strong memory-based baselines across various benchmarks. The authors report that their method consistently outperforms these baselines in terms of both effectiveness and efficiency. Notably, the learned skill curator exhibits generalization capabilities across different executor backbones and task domains. Further analysis reveals that the skill curator facilitates more targeted skill utilization, and the skills within the SkillRepo evolve into structured Markdown files that encapsulate higher-level meta-skills over time. Specific quantitative results are not provided in the abstract, but the qualitative improvements suggest a substantial effect size.

**Limitations**  
The authors acknowledge that their approach may still struggle with certain complex tasks that require nuanced understanding beyond the current skill curation framework. Additionally, the reliance on grouped task streams may limit the applicability of SkillOS in scenarios with highly variable task dependencies. The paper does not address potential scalability issues when applied to larger task sets or the computational overhead associated with maintaining the SkillRepo.

**Why it matters**  
The implications of SkillOS extend to the development of more autonomous and adaptable AI agents capable of evolving their skill sets based on past experiences. By automating skill curation, this work paves the way for more sophisticated self-evolving agents that can handle a wider range of tasks with improved efficiency. The structured representation of skills in the SkillRepo also opens avenues for future research into meta-learning and hierarchical skill acquisition, potentially enhancing the robustness and versatility of AI systems in dynamic environments.

Authors: Siru Ouyang, Jun Yan, Yanfei Chen, Rujun Han, Zifeng Wang, Bhavana Dalvi Mishra, Rui Meng, Chun-Liang Li et al.  
Source: arXiv:2605.06614  
URL: [https://arxiv.org/abs/2605.06614v1](https://arxiv.org/abs/2605.06614v1)
