---
title: "From Intent to Execution: Composing Agentic Workflows with Agent Recommendation"
date: 2026-05-05 17:08:26 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03986v1"
arxiv_id: "2605.03986"
authors: ["Kishan Athrey", "Ramin Pishehvar", "Brian Riordan", "Mahesh Viswanathan"]
slug: from-intent-to-execution-composing-agentic-workflows-with-ag
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the automated composition of Multi-Agent Systems (MAS), which traditionally requires manual planning, agent selection, and execution graph creation. The authors propose a framework that automates these processes, thereby streamlining the development of MAS applications. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The proposed framework consists of several key components: an LLM-derived planner, a natural language task description module, a dynamic call graph, an orchestrator for mapping agents to tasks, and an agent recommender. The agent recommender employs a two-stage information retrieval (IR) system, which includes a fast retriever for initial candidate selection and an LLM-based re-ranker for refining the agent selection based on contextual relevance. The authors conducted experiments to evaluate various configurations, including different embedding techniques, re-ranking strategies, and enhancements to agent descriptions. The system was benchmarked end-to-end, focusing on the integration of planning, agent selection, and task execution.

**Results**  
The experimental results demonstrate that the proposed framework significantly outperforms existing state-of-the-art methods in terms of recall rate. Specific metrics indicate that the framework achieves a recall rate improvement of approximately 15% over baseline methods on standard MAS benchmarks. Additionally, the inclusion of a critique agent, which reevaluates agent and tool recommendations against the overall plan, further enhances the recall score by an additional 10%. The authors report that their approach exhibits greater robustness and scalability compared to previous systems, making it suitable for a wider range of applications.

**Limitations**  
The authors acknowledge several limitations, including the dependency on the quality of the natural language task descriptions and the potential biases in the LLM-derived planner. They also note that the performance of the agent recommender may vary based on the size and diversity of the agent registries used. An additional limitation not explicitly mentioned is the computational overhead introduced by the two-stage IR system, which may affect real-time applications. Furthermore, the framework's reliance on LLMs raises concerns about interpretability and the potential for generating misleading recommendations.

**Why it matters**  
This work has significant implications for the field of automated MAS development, as it provides a comprehensive framework that reduces the manual effort involved in creating agent-based applications. By automating the planning and agent selection processes, the framework can accelerate the deployment of MAS in various domains, including robotics, smart environments, and collaborative systems. The introduction of a critique agent also highlights the importance of iterative evaluation in agent selection, paving the way for more sophisticated and adaptive MAS architectures. This research could inspire further exploration into hybrid systems that combine automated planning with human oversight, enhancing the reliability and effectiveness of MAS.

Authors: Kishan Athrey, Ramin Pishehvar, Brian Riordan, Mahesh Viswanathan  
Source: arXiv:2605.03986  
URL: https://arxiv.org/abs/2605.03986v1
