---
title: "Orchard: An Open-Source Agentic Modeling Framework"
date: 2026-05-14 16:35:12 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: critical
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15040v1"
arxiv_id: "2605.15040"
authors: ["Baolin Peng", "Wenlin Yao", "Qianhui Wu", "Hao Cheng", "Xiao Yu", "Rui Yang"]
slug: orchard-an-open-source-agentic-modeling-framework
summary_word_count: 490
classification_confidence: 0.90
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in open-source frameworks for agentic modeling, which aims to enhance large language models (LLMs) into autonomous agents capable of complex task execution through planning, reasoning, and tool use. The authors note that existing high-performing systems often rely on proprietary resources, while current open-source efforts primarily focus on orchestration and evaluation rather than scalable training. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Orchard framework, which includes Orchard Env, a lightweight environment service designed for sandbox lifecycle management across various task domains. Orchard provides reusable primitives that facilitate the development of agentic models. The authors introduce three specific agentic modeling recipes:

1. **Orchard-SWE**: Targets coding agents by distilling 107K trajectories from MiniMax-M2.5 and Qwen3.5-397B. It employs a credit-assignment supervised fine-tuning (SFT) method to learn from productive segments of unresolved trajectories and utilizes Balanced Adaptive Rollout for reinforcement learning (RL). Starting from the Qwen3-30B-A3B-Thinking model, Orchard-SWE achieves a performance of 64.3% on the SWE-bench Verified benchmark after SFT and 67.5% after SFT combined with RL.

2. **Orchard-GUI**: Focuses on a vision-language computer-use agent, trained with only 0.4K distilled trajectories and 2.2K open-ended tasks. It achieves success rates of 74.1%, 67.0%, and 64.0% on the WebVoyager, Online-Mind2Web, and DeepShop benchmarks, respectively, marking it as the strongest open-source model in this domain while remaining competitive with proprietary systems.

3. **Orchard-Claw**: Aims at personal assistant agents, trained with 0.2K synthetic tasks. It achieves a pass@3 rate of 59.6% on Claw-Eval and 73.9% when paired with a more robust ZeroClaw harness.

**Results**  
The results demonstrate that Orchard-SWE sets a new state of the art among open-source models of comparable size with a 67.5% success rate on SWE-bench Verified. Orchard-GUI outperforms existing open-source models with success rates of 74.1%, 67.0%, and 64.0% on its respective benchmarks. Orchard-Claw achieves competitive performance with a pass@3 rate of 73.9% when enhanced by ZeroClaw. These results collectively illustrate the effectiveness of the Orchard framework in enabling scalable agentic modeling.

**Limitations**  
The authors acknowledge that the framework's reliance on distilled trajectories may limit the diversity of training data. Additionally, the performance of the models may be constrained by the synthetic nature of some tasks, particularly in Orchard-Claw. The paper does not address potential scalability issues when applied to more complex environments or tasks beyond those tested.

**Why it matters**  
The introduction of Orchard as an open-source agentic modeling framework has significant implications for the field of AI. It democratizes access to advanced agentic modeling techniques, enabling researchers and engineers to build upon a robust infrastructure without the constraints of proprietary systems. This could accelerate advancements in autonomous agents capable of complex interactions and problem-solving across various domains, fostering innovation in applications such as coding assistance, personal assistants, and interactive systems.

Authors: Baolin Peng, Wenlin Yao, Qianhui Wu, Hao Cheng, Xiao Yu, Rui Yang, Tao Ge, Alessandrio Sordoni et al.  
Source: arXiv:2605.15040  
URL: [https://arxiv.org/abs/2605.15040v1](https://arxiv.org/abs/2605.15040v1)
