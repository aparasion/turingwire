---
title: "CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists"
date: 2026-05-25 16:57:06 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26029v1"
arxiv_id: "2605.26029"
authors: ["Junlin Yang", "Dylan Zhang", "Xiangchen Song", "Qirun Dai", "Xiao Liu", "Yuen Chen"]
slug: causalab-a-scalable-environment-for-interactive-causal-disco
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper presents CausaLab, a preprint environment designed to evaluate interactive causal discovery capabilities of large language model (LLM) agents. The gap addressed is the lack of comprehensive frameworks that assess not only the predictive accuracy of LLMs in causal inference tasks but also their understanding of the underlying causal mechanisms. Previous evaluations have primarily focused on prediction without adequately testing the agents' ability to formulate and validate causal hypotheses based on structural causal models (SCMs).

**Method**  
CausaLab operates within a synthetic laboratory setting where LLM agents are tasked with causal discovery. Each episode involves the agent receiving prior measurement records, performing interventions on a manipulator crystal, and predicting the resonance frequency of a reactor crystal influenced by the same causal mechanism. The hidden data-generating process is modeled as a randomly sampled SCM, necessitating the recovery of both causal graphs and structural equations. The environment includes a domain-specific language that allows agents to articulate their evolving SCM hypotheses, facilitating the inspection and comparison of their trajectories against ground truth. The authors explore various interaction strategies, particularly mixed observation-intervention approaches, to enhance structural fidelity in causal reasoning.

**Results**  
The evaluation reveals a significant disparity between predictive success and causal understanding. In a purely observational 6-node setting, the LLM GPT-5.2-high achieves a task accuracy of 92% but only an all-edge $F_1$ score of 0.471, indicating a failure to recover the causal structure accurately. In a mixed 6-node setting, the same model improves to 80% for both task accuracy and all-edge $F_1$. However, pure intervention strategies yield poor performance, highlighting the challenges agents face in designing informative interventions. The authors identify premature stopping as a critical limitation and demonstrate that prompting the model to verify the consistency of its hypotheses with historical data can alleviate this issue.

**Limitations**  
The authors acknowledge that the current framework may not fully capture the complexity of real-world causal inference tasks, as it relies on synthetic data and specific SCM structures. Additionally, the performance of LLMs in designing effective interventions remains suboptimal, which could limit their applicability in practical scenarios. The study also does not address the scalability of the approach to more complex causal structures beyond the 6-node setting.

**Why it matters**  
CausaLab provides a novel benchmark for assessing the causal reasoning capabilities of LLMs, distinguishing between mere predictive accuracy and genuine causal understanding. This work has implications for the development of AI systems that require robust causal reasoning, such as in scientific discovery and decision-making processes. By exposing the limitations of current LLMs as experimental causal reasoners, it paves the way for future research aimed at enhancing the causal inference capabilities of AI agents.

Authors: Junlin Yang, Dylan Zhang, Xiangchen Song, Qirun Dai, Xiao Liu, Yuen Chen, Aniket Vashishtha, Jing Shi et al.  
Source: arXiv:2605.26029  
URL: https://arxiv.org/abs/2605.26029v1
