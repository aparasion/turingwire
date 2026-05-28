---
title: "Agent Explorative Policy Optimization for Multimodal Agentic Reasoning"
date: 2026-05-27 17:36:39 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28774v1"
arxiv_id: "2605.28774"
authors: ["Minki Kang", "Shizhe Diao", "Ryo Hachiuma", "Sung Ju Hwang", "Pavlo Molchanov", "Yu-Chiang Frank Wang"]
slug: agent-explorative-policy-optimization-for-multimodal-agentic
summary_word_count: 447
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing vision-language models in handling complex real-world problems that necessitate external tool usage. The authors identify a significant gap in capability, termed the Thinking-Acting Gap, which arises from the structural asymmetry between internal reasoning (thinking) and external tool utilization (acting). They highlight that standard reinforcement learning (RL) approaches, such as Generalized Recurrent Policy Optimization (GRPO), fail to effectively bridge this gap, as evidenced by low tool usage rates (~30% of rollouts) and high error rates (~40% incorrect responses) during tool-using attempts. This preprint work seeks to enhance agentic reasoning by optimizing policy exploration in multimodal contexts.

**Method**  
The core technical contribution is the introduction of Agent eXplorative Policy Optimization (AXPO), which aims to improve the efficacy of tool usage in agentic reasoning tasks. AXPO operates by fixing the thinking prefix of tool-using rollouts that yield incorrect results and resampling the tool call along with its continuation. This method incorporates uncertainty-based prefix selection to enhance the learning signal during training. The authors evaluate AXPO across nine multimodal benchmarks and three scales of the Qwen3-VL-Thinking model, specifically focusing on the SFT (Supervised Fine-Tuning) framework combined with AXPO as opposed to SFT with GRPO.

**Results**  
The experimental results demonstrate that SFT+AXPO outperforms SFT+GRPO, achieving an average improvement of +1.8 percentage points (pp) on both Pass@1 and Pass@4 metrics at the 8B parameter scale. Notably, the 8B model with SFT+AXPO surpasses the performance of the 32B Base model on the Pass@4 metric while utilizing four times fewer parameters. These results indicate a significant enhancement in the model's ability to effectively utilize tools in multimodal reasoning tasks, showcasing the effectiveness of the proposed AXPO method.

**Limitations**  
The authors acknowledge that their approach may still be limited by the inherent challenges of tool selection and the quality of the tools themselves. They do not address potential scalability issues when applying AXPO to larger models or more complex tasks beyond the evaluated benchmarks. Additionally, the reliance on uncertainty-based prefix selection may introduce biases depending on the training data distribution, which could affect generalization to unseen scenarios.

**Why it matters**  
The implications of this work are substantial for the development of more capable multimodal AI systems that can effectively integrate reasoning and tool usage. By addressing the Thinking-Acting Gap, AXPO provides a framework that can enhance the performance of vision-language models in real-world applications, where external tools are often necessary. This research paves the way for future explorations into agentic reasoning, potentially leading to more robust AI systems capable of complex decision-making and problem-solving in dynamic environments.

Authors: Minki Kang, Shizhe Diao, Ryo Hachiuma, Sung Ju Hwang, Pavlo Molchanov, Yu-Chiang Frank Wang, Byung-Kwan Lee  
Source: arXiv:2605.28774  
URL: [https://arxiv.org/abs/2605.28774v1](https://arxiv.org/abs/2605.28774v1)
