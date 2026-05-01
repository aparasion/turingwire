---
title: "Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows"
date: 2026-04-30 17:23:19 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28139v1"
arxiv_id: "2604.28139"
authors: ["Chenxin Li", "Zhengyang Tang", "Huangxin Lin", "Yunlong Lin", "Shijue Huang", "Shengyuan Liu"]
slug: claw-eval-live-a-live-agent-benchmark-for-evolving-real-worl
summary_word_count: 477
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing benchmarks for large language model (LLM) agents, which often rely on static task sets and primarily evaluate final outputs. Such benchmarks fail to account for the dynamic nature of real-world workflows and do not verify the execution of tasks. The authors propose Claw-Eval-Live, a live benchmark designed to adapt to evolving workflow demands while providing a reproducible evaluation framework. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Claw-Eval-Live introduces a dual-layer evaluation system that separates a refreshable signal layer from a reproducible release snapshot. The refreshable layer is updated based on public workflow-demand signals, while the snapshot consists of controlled tasks derived from these signals. The current release includes 105 tasks that span business services and local workspace repair, utilizing the ClawHub Top-500 skills. The evaluation process records execution traces, audit logs, service states, and post-run artifacts, employing deterministic checks when sufficient evidence is available. For semantic evaluation, structured LLM judging is applied. The benchmark evaluates 13 frontier models under a shared public pass rule, emphasizing the need for both external demand grounding and verifiable agent actions.

**Results**  
The experiments reveal that the leading model achieves a pass rate of only 66.7% across the 105 tasks, with no model surpassing the 70% threshold. The results indicate that reliable workflow automation remains a significant challenge. Task failures are categorized by family and execution surface, with human resources, management, and multi-system business workflows identified as persistent bottlenecks. In contrast, local workspace repair tasks are comparatively easier but remain underexplored. The authors note that leaderboard rankings based solely on pass rates can be misleading, as models with similar rates may exhibit divergent overall completion rates, particularly in a middle band of task difficulty.

**Limitations**  
The authors acknowledge that the benchmark's reliance on public workflow-demand signals may introduce variability in task relevance over time. Additionally, the evaluation framework may not fully capture the nuances of agent performance in highly complex or unstructured environments. The paper does not address potential biases in the selection of tasks or the representativeness of the ClawHub Top-500 skills. Furthermore, the focus on a limited set of tasks may not generalize to broader applications of LLM agents.

**Why it matters**  
Claw-Eval-Live has significant implications for the evaluation of workflow agents, emphasizing the necessity for benchmarks that reflect real-world dynamics and verify agent actions. By providing a structured approach to assess LLM agents in evolving workflows, this work encourages future research to focus on improving task execution reliability and understanding the intricacies of agent performance across diverse task families. The findings highlight the need for continuous adaptation in benchmarking methodologies to keep pace with the rapid evolution of AI capabilities.

Authors: Chenxin Li, Zhengyang Tang, Huangxin Lin, Yunlong Lin, Shijue Huang, Shengyuan Liu, Bowen Ye, Rang Li et al.  
Source: arXiv:2604.28139  
URL: [https://arxiv.org/abs/2604.28139v1](https://arxiv.org/abs/2604.28139v1)
