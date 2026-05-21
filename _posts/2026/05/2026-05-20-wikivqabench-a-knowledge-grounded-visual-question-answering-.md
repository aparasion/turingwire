---
title: "WikiVQABench: A Knowledge-Grounded Visual Question Answering Benchmark from Wikipedia and Wikidata"
date: 2026-05-20 17:58:24 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21479v1"
arxiv_id: "2605.21479"
authors: ["Basel Shbita", "Pengyuan Li", "Anna Lisa Gentile"]
slug: wikivqabench-a-knowledge-grounded-visual-question-answering-
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
Current Visual Question Answering (VQA) benchmarks predominantly focus on tasks solvable through visual content alone, neglecting scenarios that necessitate external knowledge for accurate responses. This paper addresses this gap by introducing WikiVQABench, a knowledge-grounded VQA benchmark that integrates visual data from Wikipedia with structured knowledge from Wikidata. The authors highlight that existing benchmarks do not adequately evaluate the ability of models to leverage external knowledge, which is critical for real-world applications. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
WikiVQABench is constructed through a systematic pipeline that combines images from Wikipedia with their corresponding article captions and knowledge from Wikidata. The authors employ large language models (LLMs) to generate candidate multiple-choice question-answer pairs that require knowledge beyond the visual content. Each generated instance undergoes a rigorous curation process by human annotators to ensure factual accuracy, visual-text consistency, and the necessity of external knowledge for answering. The benchmark includes a diverse set of questions designed to evaluate knowledge-aware vision-language models (VLMs). The dataset comprises a substantial collection of images and curated questions, with the authors providing the dataset and benchmarking code publicly.

**Results**  
The evaluation of fifteen VLMs, ranging from 256 million to 90 billion parameters, reveals a significant performance disparity, with accuracy rates spanning from 24.7% to 75.6%. This wide range indicates that WikiVQABench effectively discriminates between model capabilities in knowledge-intensive reasoning tasks. The benchmark's design allows for a nuanced assessment of how well models can integrate visual and external knowledge, providing a more comprehensive evaluation than traditional VQA benchmarks.

**Limitations**  
The authors acknowledge several limitations, including the potential biases in the Wikipedia and Wikidata sources, which may affect the diversity and representativeness of the questions. Additionally, the reliance on human curation may introduce variability in the quality of the generated instances. The authors do not address the scalability of the curation process or the potential for overfitting to the specific types of knowledge represented in the dataset. Furthermore, the benchmark's focus on multiple-choice questions may limit its applicability to open-ended VQA scenarios.

**Why it matters**  
WikiVQABench has significant implications for advancing the field of knowledge-grounded VQA. By providing a benchmark that emphasizes the integration of external knowledge with visual data, it encourages the development of more sophisticated VLMs capable of reasoning beyond immediate visual cues. This work lays the groundwork for future research aimed at enhancing model performance in real-world applications where external knowledge is crucial. The availability of the dataset and benchmarking code facilitates further exploration and innovation in knowledge-aware VQA systems.

Authors: Basel Shbita, Pengyuan Li, Anna Lisa Gentile  
Source: arXiv:2605.21479  
URL: [https://arxiv.org/abs/2605.21479v1](https://arxiv.org/abs/2605.21479v1)
