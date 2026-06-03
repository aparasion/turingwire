---
title: "Synthesize and Reward -- Reinforcement Learning for Multi-Step Tool Use in Live Environments"
date: 2026-06-02 16:52:31 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03892v1"
arxiv_id: "2606.03892"
authors: ["Ibrahim Abdelaziz", "Asim Munawar", "Kinjal Basu", "Maxwell Crouse", "Chulaka Gunasekara", "Suneet Katrekar"]
slug: synthesize-and-reward-reinforcement-learning-for-multi-step-
summary_word_count: 404
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces PROVE, a framework for training LLMs in multi-step tool use through realistic environments and innovative reward mechanisms."
---

**Problem**  
The paper addresses significant limitations in training large language models (LLMs) for orchestrating multi-step tool calls in realistic environments. Existing methods struggle due to the high cost of building stateful execution environments, the disconnection between synthetic training queries and actual server states, and the inefficiency of recall-based reinforcement learning (RL) rewards that promote verbose tool-calling patterns. This work is a preprint and has not undergone peer review.

**Method**  
The authors propose the PROVE (Programmatic Rewards On Verified Environments) framework, which encompasses three main contributions: 
1. A library of 20 stateful Model Context Protocol (MCP) servers that expose 343 tools, facilitating live-execution RL training with session-scoped state isolation.
2. An automated data synthesis pipeline that generates validated multi-turn tool-call trajectories. This is achieved through dependency-graph-guided conversation simulation, which is grounded in live-sampled server states, ensuring that generated queries reference existing entities.
3. A multi-component programmatic reward system that includes graduated validity scoring, dependency-aware coverage, an adaptive efficiency penalty with a complexity-scaled call budget, a tool-name signal, and an argument-value matching bonus. This reward system operates without the need for an external judge model.

The authors trained four models (Qwen3-4B, Qwen3-8B, Qwen2.5-7B, Granite-4.1-8B) using the GRPO (Gradient Reinforcement Policy Optimization) method with consistent reward hyperparameters across models and approximately 13,000 training examples. The only hyperparameter tuned per model family was the learning rate, which was optimized through a three-point sweep.

**Results**  
The PROVE framework demonstrated significant improvements on multiple benchmarks: 
- On the BFCL Multi-Turn benchmark, PROVE achieved an increase of +10.2 points.
- For tau2-bench, the improvement was +6.8 points.
- On T-Eval, the framework yielded a +6.5 point enhancement. 

These results indicate that the compact programmatic reward system effectively enhances multi-step tool orchestration across different model families.

**Limitations**  
The authors acknowledge that the framework's reliance on a specific set of MCP servers may limit generalizability to other environments. Additionally, the automated data synthesis pipeline's effectiveness is contingent on the quality of the dependency-graph-guided simulations. The paper does not address potential scalability issues when applied to larger or more complex environments.

**Why it matters**  
The PROVE framework represents a significant advancement in the training of LLMs for multi-step tool use, providing a robust solution to the challenges of realistic environment simulation and effective reward mechanisms. This work has implications for future research in RL and LLM training, particularly in enhancing the efficiency and effectiveness of tool orchestration in dynamic environments, as published in [arXiv](https://arxiv.org/abs/2606.03892v1).
