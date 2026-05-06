---
title: "Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards"
date: 2026-05-05 15:24:40 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03862v1"
arxiv_id: "2605.03862"
authors: ["Tianyang Han", "Hengyu Shi", "Junjie Hu", "Xu Yang", "Zhiling Wang", "Junhao Su"]
slug: correct-is-not-enough-training-reasoning-planners-with-execu
summary_word_count: 474
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the reinforcement learning (RL) literature concerning the evaluation of reasoning in large language models (LLMs). While existing methods often rely on final-answer correctness as a reward signal, this approach fails to ensure that the reasoning traces generated are faithful, reliable, and useful. The authors argue that rewarding only the correctness of the final answer can lead to the reinforcement of incorrect reasoning paths, overemphasis on shortcuts, and the propagation of flawed intermediate states in multi-step reasoning tasks. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel training framework called TraceLift, which integrates a planner-executor architecture. In this framework, the planner generates tagged reasoning traces, while a frozen executor evaluates these traces to produce the final output. The key innovation is the introduction of an executor-grounded reward mechanism that combines a rubric-based Reasoning Reward Model (RM) score with an uplift metric derived from the executor's performance. This dual reward system incentivizes the generation of high-quality reasoning traces that are not only correct but also beneficial for the executor's performance. To facilitate this, the authors introduce TRACELIFT-GROUPS, a dataset comprising rubric-annotated reasoning examples derived from math and code problems. Each example consists of a high-quality reference trace and several flawed traces, allowing for targeted evaluation of reasoning quality.

**Results**  
The experimental results demonstrate that the TraceLift framework significantly outperforms traditional execution-only training methods. On benchmarks related to code and math reasoning, the executor-grounded reward led to measurable improvements in the planner-executor system's performance. Specific metrics and effect sizes are not disclosed in the abstract, but the authors emphasize that the improvements are substantial enough to suggest that reasoning supervision should focus on both the quality of the reasoning traces and their utility for the downstream model.

**Limitations**  
The authors acknowledge several limitations, including the potential for the executor's performance to be overly reliant on the quality of the reasoning traces, which may not generalize across all tasks. Additionally, the dataset TRACELIFT-GROUPS, while comprehensive, may not cover the full spectrum of reasoning tasks encountered in real-world applications. The authors do not discuss the computational overhead introduced by the dual reward mechanism or the scalability of the framework to larger, more complex reasoning tasks.

**Why it matters**  
This work has significant implications for the development of more robust reasoning capabilities in LLMs. By emphasizing the importance of intermediate reasoning quality, the TraceLift framework provides a pathway for improving the interpretability and reliability of AI systems that rely on complex reasoning processes. The introduction of executor-grounded rewards could lead to more effective training paradigms that prioritize not just correctness but also the fidelity of reasoning, potentially influencing future research in RL and LLMs.

Authors: Tianyang Han, Hengyu Shi, Junjie Hu, Xu Yang, Zhiling Wang, Junhao Su  
Source: arXiv:2605.03862  
URL: [https://arxiv.org/abs/2605.03862v1](https://arxiv.org/abs/2605.03862v1)
