---
title: "ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents"
date: 2026-05-12 17:57:04 +0000
category: research
subcategory: agents_robotics
company: "UiPath"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12481v1"
arxiv_id: "2605.12481"
authors: ["Xuhao Hu", "Xi Zhang", "Haiyang Xu", "Kyle Qiao", "Jingyi Yang", "Xuanjing Huang"]
slug: toolcua-towards-optimal-gui-tool-path-orchestration-for-comp
summary_word_count: 424
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of optimal path selection in hybrid action spaces for Computer Use Agents (CUAs), which can perform both atomic GUI actions and high-level tool calls. The authors highlight a significant gap in the literature regarding the scarcity of high-quality interleaved GUI-Tool trajectories, which complicates the decision-making process for CUAs. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose ToolCUA, an end-to-end agent that employs a staged training paradigm to learn optimal GUI-Tool path selection. The methodology consists of three main components:

1. **Interleaved GUI-Tool Trajectory Scaling Pipeline**: This component repurposes existing static GUI trajectories and synthesizes a grounded tool library, enabling the generation of diverse GUI-Tool trajectories without the need for manual engineering or the collection of real tool trajectories.

2. **Tool-Bootstrapped GUI Reinforcement Fine-Tuning (RFT)**: This approach combines warmup Supervised Fine-Tuning (SFT) with single-turn Reinforcement Learning (RL) to enhance decision-making at critical points where the agent must switch between GUI actions and tool calls.

3. **Online Agentic Reinforcement Learning**: ToolCUA is further optimized in a high-fidelity GUI-Tool environment using a Tool-Efficient Path Reward, which incentivizes the agent to utilize tools appropriately and to minimize execution paths.

**Results**  
ToolCUA achieves an accuracy of 46.85% on the OSWorld-MCP benchmark, representing a relative improvement of approximately 66% over the baseline models. This performance establishes a new state of the art among models of comparable scale. Additionally, ToolCUA demonstrates a 3.9% improvement over settings that utilize only GUI actions, indicating effective orchestration between GUI and tool usage.

**Limitations**  
The authors acknowledge several limitations, including the reliance on synthetic data for training, which may not fully capture the complexities of real-world interactions. Additionally, the performance metrics are evaluated in a controlled environment, which may not generalize to all practical applications. The paper does not address potential scalability issues when deploying ToolCUA in more complex or varied environments.

**Why it matters**  
The implications of this work are significant for the development of more capable digital agents that can navigate complex tasks involving both GUI and tool interactions. By demonstrating that training in a hybrid action space can lead to improved performance, this research paves the way for future work in optimizing agent decision-making processes. The findings suggest that integrating diverse action modalities can enhance the efficiency and effectiveness of CUAs, which is crucial for applications in automation, user assistance, and intelligent systems.

Authors: Xuhao Hu, Xi Zhang, Haiyang Xu, Kyle Qiao, Jingyi Yang, Xuanjing Huang, Jing Shao, Ming Yan et al.  
Source: arXiv:2605.12481  
URL: https://arxiv.org/abs/2605.12481v1
