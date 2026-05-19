---
title: "STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics"
date: 2026-05-18 15:27:52 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18548v1"
arxiv_id: "2605.18548"
authors: ["Tingfeng Hui", "Hao Xu", "Pengyu Zhu", "Hongsheng Xin", "Kun Zhan", "Sen Su"]
slug: stt-arena-a-more-realistic-environment-for-tool-using-with-s
summary_word_count: 481
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the capability of large language models (LLMs) to adaptively replan in the presence of spatio-temporal dynamics during task execution. While existing benchmarks primarily focus on the detection of temporal changes, the challenge of adaptive replanning when faced with abrupt state shifts remains largely unexplored. The authors introduce STT-Arena, a new benchmark designed to evaluate LLMs on 227 interactive tasks that incorporate spatio-temporal conflict types and varying levels of solvability. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the STT-Arena benchmark, which consists of 227 tasks categorized into nine spatio-temporal conflict types and four solvability levels. Each task is situated in a realistic, executable environment that includes spatio-temporal triggers capable of invalidating ongoing plans. The evaluation of existing state-of-the-art (SOTA) models, including Claude-4.6-Opus, reveals that these models achieve less than 40% accuracy on the benchmark, indicating a substantial challenge in spatio-temporal dynamic reasoning. The authors identify three primary error modes: Stale-State Execution, Misdiagnosis of Dynamic Triggers, and Missing Post-Adaptation Verification. To address these issues, they propose an iterative trajectory refinement technique that removes these failure patterns from the training data. This is combined with online reinforcement learning (RL) to develop STT-Agent-4B, which is specifically designed to outperform existing LLMs on the STT-Arena tasks.

**Results**  
The authors report that STT-Agent-4B significantly outperforms existing LLMs on the STT-Arena benchmark, although specific numerical results and comparisons against named baselines are not disclosed in the abstract. The systematic analysis of failure modes provides insights into the limitations of current models, emphasizing the need for improved adaptive reasoning capabilities in dynamic environments. The results underscore the fundamental difficulty of spatio-temporal reasoning, as even the best-performing proprietary models struggle to achieve satisfactory performance.

**Limitations**  
The authors acknowledge that their proposed benchmark and model may not fully capture all aspects of real-world spatio-temporal dynamics, as the tasks are still constrained within a defined set of scenarios. Additionally, the reliance on iterative trajectory refinement and online RL may introduce complexities in training and deployment that are not addressed in the paper. The lack of detailed performance metrics and comparisons in the abstract limits the ability to fully assess the effectiveness of STT-Agent-4B against specific baselines.

**Why it matters**  
The introduction of STT-Arena represents a critical advancement in the evaluation of LLMs for real-world applications that require adaptive replanning under dynamic conditions. By highlighting the limitations of current models and proposing a novel benchmark, this work lays the groundwork for future research aimed at enhancing the robustness and adaptability of LLMs in agentic tasks. The findings could inform the development of more sophisticated models capable of handling complex, real-time decision-making scenarios, thereby expanding the applicability of LLMs in various domains.

Authors: Tingfeng Hui, Hao Xu, Pengyu Zhu, Hongsheng Xin, Kun Zhan, Sen Su, Chunxiao Liu, Ning Miao  
Source: arXiv:2605.18548  
URL: [https://arxiv.org/abs/2605.18548v1](https://arxiv.org/abs/2605.18548v1)
