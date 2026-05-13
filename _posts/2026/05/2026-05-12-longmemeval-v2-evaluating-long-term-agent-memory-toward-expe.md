---
title: "LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues"
date: 2026-05-12 17:59:34 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12493v1"
arxiv_id: "2605.12493"
authors: ["Di Wu", "Zixiang Ji", "Asmi Kawatkar", "Bryan Kwan", "Jia-Chen Gu", "Nanyun Peng"]
slug: longmemeval-v2-evaluating-long-term-agent-memory-toward-expe
summary_word_count: 418
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of long-term memory systems for agents operating in specialized web environments. Existing benchmarks primarily focus on user histories, short traces, or downstream task success, failing to assess how effectively memory systems internalize environment-specific experiences. The authors introduce LongMemEval-V2 (LME-V2), a benchmark designed to evaluate the capability of memory systems to help agents acquire and utilize knowledge akin to experienced colleagues in customized environments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
LME-V2 comprises 451 manually curated questions that assess five core memory abilities: static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness. The benchmark is paired with history trajectories that include up to 500 trajectories and 115 million tokens. The authors propose two memory methods:  
1. **AgentRunbook-R**: A retrieval-augmented generation (RAG)-based memory system that utilizes knowledge pools for raw state observations, events, and strategy notes.  
2. **AgentRunbook-C**: This method stores trajectories as files and employs a coding agent to gather evidence in an augmented sandbox environment. The context gathering formulation allows memory systems to consume history trajectories and return compact evidence for downstream question answering. 

**Results**  
AgentRunbook-C demonstrates superior performance, achieving an average accuracy of 72.5% on the LME-V2 benchmark. This outperforms the strongest RAG baseline, which achieved 48.5%, and the off-the-shelf coding agent baseline, which reached 69.3%. The results indicate a significant effect size, with AgentRunbook-C advancing the accuracy-latency Pareto frontier, although the authors note that coding agent methods incur high latency costs.

**Limitations**  
The authors acknowledge that while AgentRunbook-C shows strong performance, there remains substantial room for improvement, particularly regarding latency. They do not explicitly address the potential scalability issues of their methods when applied to larger or more complex environments. Additionally, the reliance on manually curated questions may introduce bias or limit the generalizability of the benchmark.

**Why it matters**  
The introduction of LME-V2 establishes a rigorous framework for evaluating long-term memory systems in agents, which is crucial for developing intelligent systems capable of functioning effectively in specialized domains. By focusing on environment-specific experience, this work has implications for future research in agent design, particularly in enhancing memory systems to improve agent performance in complex, dynamic environments. The benchmark can serve as a foundation for subsequent studies aiming to refine memory architectures and methodologies, ultimately contributing to the advancement of autonomous agents in real-world applications.

Authors: Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang  
Source: arXiv:2605.12493  
URL: [https://arxiv.org/abs/2605.12493v1](https://arxiv.org/abs/2605.12493v1)
