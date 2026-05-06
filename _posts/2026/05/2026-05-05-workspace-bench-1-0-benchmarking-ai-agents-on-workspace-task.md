---
title: "Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies"
date: 2026-05-05 10:17:06 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03596v1"
arxiv_id: "2605.03596"
authors: ["Zirui Tang", "Xuanhe Zhou", "Yumou Liu", "Linchun Li", "Weizheng Wang", "Hongzhang Huang"]
slug: workspace-bench-1-0-benchmarking-ai-agents-on-workspace-task
summary_word_count: 481
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating AI agents on workspace tasks that involve complex file dependencies, a critical aspect of real-world applications. Existing benchmarks primarily focus on pre-specified or synthesized files, which do not accurately reflect the intricacies of actual work environments. The authors introduce Workspace-Bench, a novel benchmark designed to assess AI agents' capabilities in handling large-scale file dependencies, which has been largely overlooked in the literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of Workspace-Bench, which includes a comprehensive dataset comprising 20,476 files across 74 file types, organized into realistic workspaces for 5 distinct worker profiles. The benchmark features 388 tasks, each defined by its own file dependency graph, and is evaluated using 7,399 rubrics that necessitate cross-file retrieval, contextual reasoning, and adaptive decision-making. To facilitate broader accessibility, the authors also provide Workspace-Bench-Lite, a subset containing 100 tasks that maintains the benchmark's distribution while reducing evaluation costs by approximately 70%. The evaluation involved four popular agent harnesses and seven foundation models, although specific architectures and training details for these models are not disclosed.

**Results**  
The experimental results indicate that current AI agents are significantly underperforming in workspace learning tasks. The best-performing agent achieved an accuracy of 68.7%, which is notably lower than the human benchmark of 80.7%. The average performance across all evaluated agents was only 47.4%, highlighting a substantial gap in the ability of existing models to effectively manage workspace tasks with complex file dependencies. These results underscore the challenges faced by AI agents in real-world scenarios, where nuanced understanding and reasoning over file relationships are crucial.

**Limitations**  
The authors acknowledge several limitations, including the potential for the benchmark to be influenced by the specific configurations of the tasks and the inherent complexity of the file dependency graphs. They also note that the performance metrics may vary based on the specific agent architectures employed. An additional limitation not explicitly mentioned is the lack of diversity in the worker profiles, which may not encompass the full range of real-world scenarios. Furthermore, the benchmark's reliance on a curated set of tasks may not fully capture the variability encountered in actual work environments.

**Why it matters**  
The introduction of Workspace-Bench has significant implications for future research in AI agent development, particularly in the context of workspace learning. By providing a robust framework for evaluating agents on tasks that mirror real-world complexities, this benchmark can guide the design of more capable AI systems that can effectively manage file dependencies. The findings highlight the need for improved methodologies in training and evaluating AI agents, paving the way for advancements in areas such as automated document processing, collaborative work environments, and intelligent personal assistants.

Authors: Zirui Tang, Xuanhe Zhou, Yumou Liu, Linchun Li, Weizheng Wang, Hongzhang Huang, Jun Zhou, Jiachen Song et al.  
Source: arXiv:2605.03596  
URL: [https://arxiv.org/abs/2605.03596v1](https://arxiv.org/abs/2605.03596v1)
