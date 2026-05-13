---
title: "MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering"
date: 2026-05-12 16:32:43 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12361v1"
arxiv_id: "2605.12361"
authors: ["Rezarta Islamaj", "Robert Leaman", "Joey Chan", "Nicholas Wan", "Qiao Jin", "Natalie Xie"]
slug: medhopqa-a-disease-centered-multi-hop-reasoning-benchmark-an
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacies of existing biomedical question answering (QA) benchmarks, particularly their inability to effectively evaluate multi-hop reasoning capabilities in large language models (LLMs). Current benchmarks often allow models to succeed through superficial pattern matching rather than genuine inference, leading to performance saturation and susceptibility to training data contamination. The authors highlight the need for a disease-centered benchmark that emphasizes multi-hop reasoning, which is critical for tasks such as diagnostic support and literature-based discovery. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce MedHopQA, a multi-hop reasoning benchmark comprising 1,000 expert-curated question-answer pairs. Each question necessitates the integration of information from two distinct Wikipedia articles, with answers provided in an open-ended format. The dataset construction involved a structured process that included human annotation, triage, iterative verification, and validation using LLMs as judges. To enhance evaluation robustness, gold annotations are supplemented with ontology-grounded synonym sets from MONDO, NCBI Gene, and NCBI Taxonomy, facilitating both lexical and concept-level assessments. To mitigate leaderboard gaming and contamination risks, the 1,000 scored questions are embedded within a larger set of 10,000 publicly downloadable questions, with answers withheld for integrity.

**Results**  
While specific performance metrics and comparisons to baseline models are not detailed in the abstract, the authors emphasize that MedHopQA is designed to resist performance saturation and contamination, which are common issues in existing benchmarks. The structured approach to dataset creation and the inclusion of ontology-grounded annotations are expected to enhance the benchmark's discriminative power as model capabilities evolve.

**Limitations**  
The authors acknowledge that the benchmark's reliance on Wikipedia articles may introduce biases inherent to the source material. Additionally, while the dataset is designed to be robust against gaming and contamination, the effectiveness of these measures in practice remains to be validated. The open-ended answer format may also complicate evaluation consistency, as it requires subjective interpretation of correctness.

**Why it matters**  
MedHopQA represents a significant advancement in the evaluation of LLMs within the biomedical domain, particularly by prioritizing multi-hop reasoning capabilities. This benchmark not only provides a tool for assessing current models but also establishes a framework for future biomedical QA datasets that can adapt to evolving model capabilities. By focusing on compositional reasoning and contamination resistance, MedHopQA sets a new standard for the development of benchmarks that can meaningfully evaluate the reasoning abilities of LLMs, thereby influencing downstream applications in clinical diagnostics and biomedical research.

Authors: Rezarta Islamaj, Robert Leaman, Joey Chan, Nicholas Wan, Qiao Jin, Natalie Xie, John Wilbur, Shubo Tian et al.  
Source: arXiv:2605.12361  
URL: [https://arxiv.org/abs/2605.12361v1](https://arxiv.org/abs/2605.12361v1)
