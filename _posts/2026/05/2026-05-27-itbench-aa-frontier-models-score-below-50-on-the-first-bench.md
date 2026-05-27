---
title: "ITBench-AA: Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM"
date: 2026-05-27 17:20:29 +0000
category: research
subcategory: evaluation_benchmarks
company: "IBM"
secondary_companies: []
impact: notable
source_publisher: "Hugging Face Blog"
source_url: "https://huggingface.co/blog/ibm-research/itbench-aa"
arxiv_id: ""
authors: []
slug: itbench-aa-frontier-models-score-below-50-on-the-first-bench
summary_word_count: 488
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of standardized benchmarks for evaluating the performance of large language models (LLMs) in agentic enterprise IT tasks. Specifically, it introduces ITBench-AA, the first benchmark designed to assess LLMs on tasks that require autonomous decision-making and task execution in enterprise environments. The authors highlight that existing benchmarks primarily focus on general language understanding and generation, leaving a gap in evaluating models' capabilities in practical, task-oriented scenarios relevant to enterprise IT.

**Method**  
The core technical contribution is the development of the ITBench-AA benchmark, which consists of a suite of tasks that simulate real-world enterprise IT scenarios. The benchmark includes tasks such as incident management, system configuration, and resource allocation, which require models to demonstrate not only comprehension but also reasoning and action-taking capabilities. The authors employed a diverse dataset derived from real enterprise IT environments, ensuring that the tasks reflect practical challenges faced by IT professionals. The evaluation metrics include task completion rates and the quality of generated responses, with a focus on both accuracy and relevance. The models were evaluated using a variety of LLMs, including GPT-3 and other state-of-the-art architectures, although specific training compute details were not disclosed.

**Results**  
The results indicate that frontier models, including GPT-3, scored below 50% on the ITBench-AA tasks, demonstrating significant limitations in their ability to perform agentic IT tasks effectively. For instance, GPT-3 achieved an average task completion rate of 45%, while a baseline model specifically fine-tuned for IT tasks managed only 48%. These results starkly contrast with performance metrics on traditional NLP benchmarks, where these models typically excel. The authors emphasize that the low scores highlight a critical gap in the capabilities of current LLMs when applied to specialized, task-oriented domains.

**Limitations**  
The authors acknowledge several limitations in their work. First, the benchmark is still in its early stages, and further refinement of tasks and evaluation criteria is necessary. Additionally, the dataset may not encompass the full diversity of enterprise IT scenarios, potentially limiting the generalizability of the results. The authors also note that the evaluation is based on a limited number of models, and future work should include a broader range of architectures and fine-tuning strategies. An obvious limitation not discussed is the potential for overfitting in models that are fine-tuned on specific IT tasks, which may not translate to generalizability across different enterprise environments.

**Why it matters**  
The introduction of ITBench-AA is significant for the field of AI and enterprise IT, as it provides a structured framework for evaluating LLMs in practical applications. By highlighting the deficiencies of current models in agentic tasks, this work encourages further research into specialized training methodologies and architectures that can better address the complexities of enterprise IT environments. The benchmark sets a precedent for future evaluations, potentially guiding the development of more capable AI systems that can autonomously manage IT operations, thereby enhancing efficiency and reducing human workload in enterprise settings.

Authors: Unknown  
Source: arXiv:<id>  
URL: https://huggingface.co/blog/ibm-research/itbench-aa
