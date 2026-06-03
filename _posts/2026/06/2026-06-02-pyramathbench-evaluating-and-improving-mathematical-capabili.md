---
title: "PyraMathBench: Evaluating and Improving Mathematical Capability in Large Language Models"
date: 2026-06-02 16:32:53 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03858v1"
arxiv_id: "2606.03858"
authors: ["Zetian Ouyang", "Linlin Wang", "Gerard de Melo", "Liang He"]
slug: pyramathbench-evaluating-and-improving-mathematical-capabili
summary_word_count: 370
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces PyraMathBench, a benchmark for evaluating LLMs' mathematical capabilities, and proposes SOLVE and IRPO to enhance numerical reasoning."
---

**Problem**  
Current benchmarks inadequately assess the numerical reasoning capabilities of large language models (LLMs), which are critical for mathematical tasks. This gap limits the interpretability of LLM failures in mathematical contexts. The authors present PyraMathBench, a novel benchmark designed to evaluate LLMs' mathematical capabilities through a comprehensive set of 32,505 questions derived from 7,404 math word problems. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contributions include the development of the PyraMathBench benchmark and two novel modules: Smart Optimization & Learning-based VErsatile module (SOLVE) and Interactive Relative Policy Optimization (IRPO). PyraMathBench encompasses four cognitive aspects, 14 subcategories, and two modalities, providing a structured approach to evaluate LLMs' performance in mathematical reasoning. SOLVE enhances the numerical-mathematical synergy of LLMs by implementing efficient tool calls, including fuzzy matching and low-quality call rejection. IRPO optimizes the interaction between the model and the numerical tools, improving the overall performance in mathematical tasks. The training compute specifics are not disclosed, but the experiments utilize the Qwen-2.5 model as a baseline.

**Results**  
The introduction of SOLVE and IRPO led to a significant performance improvement in the Qwen-2.5 model, achieving a score increase of 5.0 on the PyraMathBench benchmark. This improvement highlights the effectiveness of the proposed methods in enhancing LLMs' capabilities in handling mathematical reasoning tasks. The results indicate that LLMs struggle with numerical computation and abstract numerical questions, underscoring the necessity of the proposed enhancements.

**Limitations**  
The authors acknowledge that while PyraMathBench provides a comprehensive evaluation framework, it may not cover all possible mathematical reasoning scenarios. Additionally, the reliance on the Qwen-2.5 model may limit the generalizability of the findings to other LLM architectures. The paper does not address potential biases in the dataset or the implications of model size and architecture on performance.

**Why it matters**  
The development of PyraMathBench and the proposed enhancements (SOLVE and IRPO) represent a significant step forward in evaluating and improving the mathematical capabilities of LLMs. By addressing the shortcomings in numerical reasoning, this work lays the groundwork for future research aimed at enhancing LLM performance in mathematical tasks. The findings have implications for applications in education, automated reasoning, and any domain where mathematical reasoning is essential, as published in [arXiv](https://arxiv.org/abs/2606.03858v1).
