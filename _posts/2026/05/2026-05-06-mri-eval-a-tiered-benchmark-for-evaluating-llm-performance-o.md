---
title: "MRI-Eval: A Tiered Benchmark for Evaluating LLM Performance on MRI Physics and GE Scanner Operations Knowledge"
date: 2026-05-06 17:42:01 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.05175v1"
arxiv_id: "2605.05175"
authors: ["Perry E. Radau"]
slug: mri-eval-a-tiered-benchmark-for-evaluating-llm-performance-o
summary_word_count: 427
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of systematic benchmarks for evaluating large language models (LLMs) on MRI physics and vendor-specific GE scanner operations knowledge. Existing benchmarks primarily utilize multiple-choice questions (MCQs) from review books, where top-performing models achieve high scores, limiting their discriminative power. The authors note that no prior work has comprehensively assessed the operational knowledge critical for MRI practice, particularly in the context of GE scanners. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce MRI-Eval, a tiered benchmark comprising 1,365 scored items categorized into nine domains and three difficulty levels. The items are sourced from textbooks, GE scanner manuals, programming course materials, and expert-generated questions. The evaluation involved five model families: GPT-5.4, Claude Opus 4.6, Claude Sonnet 4.6, Gemini 2.5 Pro, and Llama 3.3 70B. The primary evaluation method was MCQ, supplemented by two additional analyses: a stem-only format that removed answer options and employed an independent LLM judge, and a primed stem-only format that tested model responses to incorrect user claims. 

**Results**  
The overall accuracy for the MCQ format ranged from 93.2% to 97.1% across the evaluated models. However, performance on GE scanner operations was notably lower, with accuracies between 88.2% and 94.6%. In the stem-only format, the accuracy of frontier models dropped significantly to between 58.4% and 61.1%, with Llama 3.3 70B achieving only 37.1%. The stem-only accuracy for GE scanner operations was particularly poor, ranging from 13.8% to 29.8%. These results indicate that high performance in MCQs can obscure deficiencies in free-text recall, especially regarding vendor-specific operational knowledge.

**Limitations**  
The authors acknowledge that MRI-Eval is primarily a relative comparison benchmark rather than an absolute measure of competency. They caution against relying solely on raw LLM outputs for GE-specific protocol guidance due to the observed discrepancies in performance across different evaluation formats. An additional limitation not explicitly mentioned is the potential bias introduced by the selection of questions and the specific model families evaluated, which may not generalize to other LLMs or MRI contexts.

**Why it matters**  
The development of MRI-Eval has significant implications for the evaluation of LLMs in specialized domains such as medical imaging. By highlighting the discrepancies between MCQ performance and free-text recall, this work underscores the necessity for more nuanced assessment methods that can accurately reflect a model's operational knowledge. This benchmark can guide future research in improving LLMs for medical applications, particularly in enhancing their understanding of vendor-specific protocols and operational intricacies, ultimately contributing to safer and more effective clinical practices.

Authors: Perry E. Radau  
Source: arXiv:2605.05175  
URL: [https://arxiv.org/abs/2605.05175v1](https://arxiv.org/abs/2605.05175v1)
