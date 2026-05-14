---
title: "RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation"
date: 2026-05-13 13:52:42 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13542v1"
arxiv_id: "2605.13542"
authors: ["Chengzhi Shen", "Weixiang Shen", "Tobias Susetzky", "Chen", "Chen", "Jun Li"]
slug: realicu-do-llm-agents-understand-long-context-icu-data-a-ben
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of existing benchmarks for evaluating large language models (LLMs) in the context of Intensive Care Units (ICUs). Traditional benchmarks rely on historical clinician actions as ground truth, which are often based on incomplete information and limited temporal context, leading to potentially suboptimal decision-making. The authors present RealICU, a hindsight-annotated benchmark that evaluates LLMs under realistic ICU conditions, where labels are derived from comprehensive reviews of patient trajectories by senior physicians. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the RealICU benchmark, which includes two datasets: RealICU-Gold and RealICU-Scale. RealICU-Gold consists of 930 annotated 30-minute windows from 94 patients in the MIMIC-IV database, while RealICU-Scale extends this with 11,862 windows using Oracle, a physician-validated LLM that generates hindsight labels. The authors define four tasks for evaluation: assessing Patient Status, identifying Acute Problems, recommending Actions, and flagging Red Flags that could lead to unsafe outcomes. The study also introduces ICU-Evo, a structured-memory agent designed to enhance long-horizon reasoning in LLMs, although it does not completely mitigate safety failures.

**Results**  
The evaluation reveals that existing LLMs, including those augmented with memory capabilities, perform poorly on the RealICU benchmark. The authors identify two significant failure modes: a recall-safety tradeoff in clinical recommendations and an anchoring bias towards initial patient interpretations. Specific performance metrics are not disclosed in the abstract, but the results indicate that current models struggle to meet the demands of high-stakes clinical decision-making, highlighting the need for improved reasoning capabilities in LLMs.

**Limitations**  
The authors acknowledge that while RealICU provides a more clinically relevant evaluation framework, it still has limitations. The reliance on hindsight annotations may introduce biases, and the structured-memory approach in ICU-Evo does not fully resolve safety issues. Additionally, the benchmark's performance metrics and the generalizability of findings across different clinical settings are not extensively discussed, which could limit the applicability of the results.

**Why it matters**  
RealICU represents a significant advancement in the evaluation of AI systems for clinical decision support, particularly in high-stakes environments like ICUs. By providing a more realistic assessment of LLM capabilities, it lays the groundwork for future research aimed at enhancing AI reasoning in healthcare. The findings underscore the critical need for AI systems that can effectively integrate long-context clinical data and make safe, informed recommendations, which is essential for improving patient outcomes in intensive care settings.

Authors: Chengzhi Shen, Weixiang Shen, Tobias Susetzky, Chen Chen, Jun Li, Yuyuan Liu, Xuepeng Zhang et al.  
Source: arXiv:2605.13542v1  
URL: https://arxiv.org/abs/2605.13542v1
