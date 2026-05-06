---
title: "TriBench-Ko: Evaluating LLM Risks in Judicial Workflows"
date: 2026-05-05 14:20:28 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03792v1"
arxiv_id: "2605.03792"
authors: ["Haesung Lee", "Gyubin Choi", "Eun-Ju Lee", "So-Min Lee", "Youkang Ko", "Dogyoon Lim"]
slug: tribench-ko-evaluating-llm-risks-in-judicial-workflows
summary_word_count: 499
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of large language models (LLMs) within judicial workflows, particularly in the context of Korean legal systems. Existing benchmarks primarily focus on proxy tasks, such as bar examination performance or classification metrics, which do not adequately reflect the complexities and risks associated with real-world judicial processes. The authors present TriBench-Ko, a novel benchmark designed to assess the deployment risks of LLMs in verified judicial tasks, highlighting the need for a more nuanced evaluation framework that captures both performance and risk factors in legal contexts. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
TriBench-Ko encompasses four core tasks relevant to judicial workflows: jurisprudence summarization, precedent retrieval, legal issue extraction, and evidence analysis. The benchmark is structured to evaluate model performance across multiple risk categories, including inaccuracy (e.g., hallucination, omission, statutory misapplication), biases (demographic biases, overcompliance), inconsistencies (prompt sensitivity, non-determinism), and adjudicative overreach. Each task is designed to systematically assess both the model's output quality and the associated risks based on real judicial decisions. The authors employ a range of contemporary LLMs for evaluation, although specific architectures, loss functions, and training compute details are not disclosed in the paper.

**Results**  
The evaluation reveals that many contemporary LLMs exhibit significant risks when applied to judicial tasks. Notably, models struggle with precedent retrieval, often failing to capture critical legal information necessary for accurate legal reasoning. The authors provide a comprehensive diagnosis of the evaluated models, indicating that performance on TriBench-Ko is suboptimal, particularly in tasks that require precise legal knowledge and contextual understanding. While specific numerical performance metrics are not detailed in the abstract, the qualitative assessment suggests that the risks identified are substantial enough to warrant caution in deploying LLMs in judicial contexts.

**Limitations**  
The authors acknowledge that the benchmark is limited to the Korean legal system, which may restrict its applicability to other jurisdictions. Additionally, the evaluation does not account for the full spectrum of LLMs available, potentially overlooking models that may perform better in these tasks. The paper also does not provide detailed statistical analyses or comparisons against baseline models, which could strengthen the findings. Furthermore, the reliance on real judicial decisions for task structuring may introduce biases based on the specific cases selected.

**Why it matters**  
The introduction of TriBench-Ko has significant implications for the integration of LLMs in legal workflows. By systematically evaluating the risks associated with LLM outputs in judicial contexts, this benchmark provides a critical tool for legal practitioners and researchers to assess the reliability and safety of deploying LLMs in sensitive legal environments. The findings underscore the necessity for rigorous inspection of LLM-generated outputs, particularly in high-stakes scenarios where inaccuracies can lead to severe consequences. This work paves the way for future research aimed at improving LLM performance in legal applications and developing more robust evaluation frameworks.

Authors: Haesung Lee, Gyubin Choi, Eun-Ju Lee, So-Min Lee, Youkang Ko, Dogyoon Lim, Sung-Kyoung Jang, Yohan Jo  
Source: arXiv cs.CL  
URL: [https://arxiv.org/abs/2605.03792v1](https://arxiv.org/abs/2605.03792v1)
