---
title: "Qiskit QuantumKatas: Adapting Microsoft's Quantum Computing exercises for LLM evaluation"
date: 2026-05-26 16:02:08 +0000
category: research
subcategory: evaluation_benchmarks
company: "Microsoft"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27210v1"
arxiv_id: "2605.27210"
authors: ["Juan Cruz-Benito", "Ismael Faro"]
slug: qiskit-quantumkatas-adapting-microsoft-s-quantum-computing-e
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of standardized benchmarks for evaluating large language models (LLMs) in the context of quantum computing. Specifically, it adapts Microsoft's QuantumKatas, a well-established quantum computing curriculum originally designed for Q#, to the Qiskit framework, which is more widely adopted in the quantum computing community. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors developed a benchmark comprising 350 tasks across 26 categories, covering a range of topics from fundamental quantum gates to advanced algorithms such as Grover's, Simon's, and Deutsch-Jozsa, as well as error correction and quantum games. Each task includes a natural language prompt, a canonical solution, and a deterministic test verification mechanism through classical circuit simulation. The evaluation framework allows for systematic assessment of LLMs, with 16 models evaluated across 7 prompting configurations, resulting in a total of 39,200 model runs. The authors leverage the pedagogical design of QuantumKatas to ensure a principled difficulty progression and comprehensive concept coverage while contributing the adaptation to Qiskit and the evaluation infrastructure.

**Results**  
The benchmark effectively differentiates model capabilities, with pass rates for the best configurations ranging from 32.3% to 83.1%. Notably, there is a 26.1 percentage point average gap between the performance of frontier models and open-source models. Performance on specific tasks reveals that models excel at implementing known algorithms, achieving 82.1% on Simon's Algorithm and 81.6% on Basic Gates. However, they struggle with problem encoding tasks, scoring only 34.4% on SolveSATWithGrover and 40.0% on DistinguishUnitaries. The study also finds that chain-of-thought prompting has a bimodal effect; it benefits three models (two of which are explicitly tuned for reasoning) but degrades performance for others, resulting in a mid-pack aggregate performance of 56.3%, slightly behind the few-shot-5 strategy at 57.8%.

**Limitations**  
The authors acknowledge that the benchmark is limited to the tasks derived from QuantumKatas, which may not encompass the full spectrum of quantum computing challenges. Additionally, the evaluation is constrained by the specific LLMs tested, and the results may not generalize to other models or architectures. The bimodal effect of prompting strategies suggests that further investigation is needed to understand the underlying reasons for performance variability across different models.

**Why it matters**  
This work provides a critical resource for researchers investigating LLM capabilities in quantum computing, offering a structured framework for evaluation that can facilitate comparative studies and model improvements. By releasing the benchmark and evaluation framework, the authors enable the community to explore the intersection of quantum computing and natural language processing, potentially leading to advancements in both fields. The findings regarding model performance on specific tasks can inform future research directions and the development of more effective prompting strategies.

Authors: Juan Cruz-Benito, Ismael Faro  
Source: arXiv:2605.27210  
URL: [https://arxiv.org/abs/2605.27210v1](https://arxiv.org/abs/2605.27210v1)
