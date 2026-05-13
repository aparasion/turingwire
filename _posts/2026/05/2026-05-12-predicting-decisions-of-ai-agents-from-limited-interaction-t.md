---
title: "Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling"
date: 2026-05-12 17:09:32 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12411v1"
arxiv_id: "2605.12411"
authors: ["Eilam Shapira", "Moshe Tennenholtz", "Roi Reichart"]
slug: predicting-decisions-of-ai-agents-from-limited-interaction-t
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of predicting the decisions of AI agents in negotiation scenarios with limited interaction data. Specifically, it focuses on the situation where an AI agent must infer the decision-making process of an unfamiliar counterpart, whose internal logic and strategies are opaque. The authors highlight a gap in existing literature regarding the effectiveness of prediction models in such contexts, particularly when real-world logging confounds are absent. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach termed target-adaptive text-tabular prediction. In this framework, each decision point is represented as a table row that integrates structured game state information, offer history, and dialogue context. The model leverages $K$ previous interactions with the same target agent as labeled adaptation examples. The architecture is based on a tabular foundation model that combines game-state features with text representations derived from a large language model (LLM). A key innovation is the introduction of an LLM-as-Observer, which processes the decision-time state and dialogue to generate a hidden state that serves as an additional feature for decision-making, rather than directly predicting outcomes. The model was trained on 13 frontier LLM agents and evaluated on 91 held-out scaffolded agents, demonstrating its adaptability and effectiveness in predicting counterpart behavior.

**Results**  
The proposed model significantly outperforms baseline methods, including direct LLM-as-Predictor prompting and traditional game+text feature combinations. Notably, at $K=16$, the inclusion of Observer features enhances response-prediction area under the curve (AUC) by approximately 4 points across both tasks and reduces bargaining offer-prediction error by 14%. These results indicate that the target-adaptive text-tabular formulation effectively captures decision-relevant signals that are not accessible through direct prompting methods.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a controlled experimental setup that may not fully capture the complexities of real-world negotiations. Additionally, the model's performance may vary with different types of agents or negotiation contexts not represented in the training data. The generalizability of the findings to broader applications in diverse negotiation scenarios remains to be validated.

**Why it matters**  
This research has significant implications for the development of AI agents capable of engaging in complex negotiations with minimal prior knowledge of their counterparts. By framing the prediction task as a target-adaptive text-tabular problem, the work opens avenues for more robust and adaptable AI systems in various domains, including e-commerce, procurement, and automated negotiation platforms. The insights gained from the hidden representations of LLMs could lead to improved strategies for agent design and interaction modeling, enhancing the overall efficacy of AI in decision-making tasks.

Authors: Eilam Shapira, Moshe Tennenholtz, Roi Reichart  
Source: arXiv:2605.12411  
URL: https://arxiv.org/abs/2605.12411v1
