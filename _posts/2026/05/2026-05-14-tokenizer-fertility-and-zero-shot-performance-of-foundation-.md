---
title: "Tokenizer Fertility and Zero-Shot Performance of Foundation Models on Ukrainian Legal Text: A Comparative Study"
date: 2026-05-14 14:35:05 +0000
category: research
subcategory: evaluation_benchmarks
company: "Meta"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.14890v1"
arxiv_id: "2605.14890"
authors: ["Volodymyr Ovcharov"]
slug: tokenizer-fertility-and-zero-shot-performance-of-foundation-
summary_word_count: 423
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the lack of systematic comparisons of tokenizer efficiency and zero-shot performance of foundation models specifically applied to Ukrainian legal text. Prior literature has not adequately explored how different models handle tokenization in this domain, which is critical for optimizing API costs and performance in legal applications.

**Method**  
The study benchmarks seven foundation models from five providers on a dataset of 273 validated court decisions from Ukraine's state registry (EDRSR). The core technical contributions include the measurement of tokenizer fertility—defined as the number of tokens generated per input text—and the evaluation of zero-shot performance across three distinct tasks. The models evaluated include Qwen3 and Llama-family models, among others. The authors employ a composite scoring system to quantify performance, with a focus on both tokenization efficiency and task accuracy. Training compute details are not disclosed, but the models vary significantly in parameter counts, with NVIDIA Nemotron Super 3 (120B parameters) and Mistral Large 3 (675B parameters) being key comparisons.

**Results**  
The findings reveal that tokenizer fertility varies by a factor of 1.6, with Qwen3 models consuming 60% more tokens than Llama-family models for the same input. In terms of performance, NVIDIA Nemotron Super 3 achieves the highest composite score of 83.1, surpassing Mistral Large 3, which has 5.6 times more total parameters and 3.4 times more active parameters per token, at only one-third of the API cost. Additionally, the study finds that few-shot prompting can degrade performance by up to 26 percentage points, with stratified and prompt-sensitivity ablations indicating that this degradation is intrinsic to the Ukrainian language rather than a result of example selection.

**Limitations**  
The authors acknowledge that their analysis is limited to a specific legal domain and may not generalize to other types of Ukrainian text or other languages. They also note that the performance degradation observed with few-shot prompting is specific to the morphological characteristics of the Ukrainian language, which may not apply universally. Furthermore, the study does not explore the impact of different training datasets or fine-tuning strategies on model performance.

**Why it matters**  
This work has significant implications for practitioners in the field of natural language processing, particularly those working with morphologically rich languages like Ukrainian. The findings suggest that careful analysis of tokenizer efficiency should precede model selection to optimize API costs. Additionally, the results indicate that zero-shot performance may be a more reliable approach than few-shot prompting in this context, guiding future research and application development in legal and other domains where Ukrainian text is prevalent.

Authors: Volodymyr Ovcharov  
Source: arXiv:2605.14890  
URL: [https://arxiv.org/abs/2605.14890v1](https://arxiv.org/abs/2605.14890v1)
