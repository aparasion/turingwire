---
title: "WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation"
date: 2026-05-11 17:49:43 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10912v1"
arxiv_id: "2605.10912"
authors: ["Shuangrui Ding", "Xuanlang Dai", "Long Xing", "Shengyuan Ding", "Ziyu Liu", "Yang JingYi"]
slug: wildclawbench-a-benchmark-for-real-world-long-horizon-agent-
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating AI agents in realistic, long-horizon tasks within their native runtime environments. Existing benchmarks predominantly utilize synthetic environments, short-horizon tasks, and mock-service APIs, which do not accurately reflect the complexities and challenges faced by agents in real-world applications. The authors present WildClawBench, a preprint benchmark designed to assess the performance of agents in a more authentic context, highlighting the inadequacies of current evaluation methodologies.

**Method**  
WildClawBench comprises 60 human-authored, bilingual, multimodal tasks categorized into six thematic areas. Each task is designed to take approximately 8 minutes to complete and involves an average of over 20 tool calls. The evaluation framework operates within a reproducible Docker container that hosts various CLI agent harnesses, including OpenClaw, Claude Code, Codex, and Hermes Agent, allowing agents to interact with real tools instead of mock services. The grading methodology is hybrid, incorporating deterministic rule-based checks, environment-state auditing to assess side effects, and semantic verification through a language model (LLM) or vision-language model (VLM) judge. This multifaceted approach aims to provide a comprehensive evaluation of agent performance in long-horizon tasks.

**Results**  
The evaluation of 19 frontier models revealed that the best-performing model, Claude Opus 4.7, achieved an overall success rate of 62.2% when evaluated under the OpenClaw harness. Notably, all other models tested fell below the 60% threshold. The results also indicated that switching the harness could significantly impact performance, with a single model's score varying by up to 18 points depending on the environment. These findings underscore the challenges faced by current models in executing long-horizon tasks effectively.

**Limitations**  
The authors acknowledge several limitations, including the potential for task difficulty to vary significantly across the six thematic categories, which may affect model performance comparability. Additionally, the reliance on human-authored tasks may introduce biases or inconsistencies in task design. The benchmark's focus on specific agent harnesses may limit generalizability to other environments or tools. Furthermore, the evaluation framework's hybrid grading system, while comprehensive, may still miss nuanced aspects of agent performance.

**Why it matters**  
WildClawBench represents a significant advancement in the evaluation of AI agents, particularly in the context of long-horizon tasks that reflect real-world applications. By providing a benchmark that emphasizes native-runtime evaluation, this work encourages the development of more robust and capable agents. The findings highlight the current limitations of frontier models, prompting further research into improving agent performance in complex, multimodal environments. The release of the tasks, code, and containerized tooling facilitates reproducible evaluation, fostering collaboration and innovation in the field.

Authors: Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu, Yang JingYi, Penghui Yang, Zhixiong Zhang et al.  
Source: arXiv:2605.10912  
URL: [https://arxiv.org/abs/2605.10912v1](https://arxiv.org/abs/2605.10912v1)
