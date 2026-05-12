---
title: "RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards"
date: 2026-05-11 17:40:38 +0000
category: research
subcategory: agents_robotics
company: "Meta"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10899v1"
arxiv_id: "2605.10899"
authors: ["Gaotang Li", "Bhavana Dalvi Mishra", "Zifeng Wang", "Jun Yan", "Yanfei Chen", "Chun-Liang Li"]
slug: rubricem-meta-rl-with-rubric-guided-policy-decomposition-bey
summary_word_count: 460
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional reinforcement learning (RL) frameworks in training deep research agents that engage in complex tasks such as planning, evidence evaluation, and long-form report synthesis. The authors highlight that existing methods often rely on verifiable rewards, which are inadequate for tasks lacking ground-truth answers. Furthermore, they note the challenge of reusing past experiences in a meaningful way, as standard post-training techniques do not facilitate effective learning from previous attempts. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose RubricEM, a novel meta-reinforcement learning framework that integrates rubric-guided policy decomposition with reflection-based meta-policy evolution. The architecture consists of two main components: a stage-aware policy that conditions various phases of the research process (planning, evidence gathering, review, and synthesis) on self-generated rubrics, and a Stage-Structured Generalized Policy Optimization (GRPO) mechanism that utilizes stage-specific rubric judgments to provide denser semantic feedback for long-horizon optimization. The framework also includes a shared-backbone reflection meta-policy that distills feedback from judged trajectories into reusable guidance for future attempts. The training process leverages a combination of self-generated rubrics and structured feedback to enhance the learning efficiency of the agent.

**Results**  
RubricEM-8B demonstrates superior performance across four long-form research benchmarks, significantly outperforming comparable open models and nearing the performance of proprietary deep-research systems. Specific results include improvements in task completion rates and quality of outputs, although exact numerical metrics are not disclosed in the abstract. The authors conduct extensive analyses to elucidate the contributions of various components of RubricEM, indicating that the integration of rubrics and structured feedback is crucial for achieving these performance gains.

**Limitations**  
The authors acknowledge that the reliance on self-generated rubrics may introduce variability in performance, as the quality of these rubrics can affect the learning process. Additionally, the framework's complexity may pose challenges in terms of scalability and generalization to other domains outside of the tested benchmarks. They do not address potential issues related to the computational overhead associated with the stage-structured approach or the implications of using a shared-backbone meta-policy across diverse tasks.

**Why it matters**  
RubricEM represents a significant advancement in the field of meta-reinforcement learning by proposing a structured approach to policy execution and feedback that transcends traditional reward mechanisms. The implications of this work extend to the development of more sophisticated AI systems capable of tackling complex, open-ended tasks in research and beyond. By enabling agents to learn from past experiences in a more meaningful way, RubricEM could facilitate the creation of more effective and adaptable AI systems, paving the way for future research in meta-learning and reinforcement learning applications.

Authors: Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang, Jun Yan, Yanfei Chen, Chun-Liang Li, Long T. Le, Rujun Han et al.  
Source: arXiv:2605.10899  
URL: [https://arxiv.org/abs/2605.10899v1](https://arxiv.org/abs/2605.10899v1)
