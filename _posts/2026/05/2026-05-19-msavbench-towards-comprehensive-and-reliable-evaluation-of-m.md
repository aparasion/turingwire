---
title: "MSAVBench: Towards Comprehensive and Reliable Evaluation of Multi-Shot Audio-Video Generation"
date: 2026-05-19 17:59:33 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20183v1"
arxiv_id: "2605.20183"
authors: ["Yujie Wei", "Yujin Han", "Zhekai Chen", "Yongming Li", "Kaixun Jiang", "Zhihang Liu"]
slug: msavbench-towards-comprehensive-and-reliable-evaluation-of-m
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of comprehensive evaluation frameworks for multi-shot audio-video (MSAV) generation models, which have evolved from single-shot synthesis to more complex narratives. Existing benchmarks are limited in their scope, data diversity, and evaluation methodologies, which hampers the systematic assessment of modern MSAV models. The authors present MSAVBench, a novel benchmark and evaluation framework designed to fill these gaps. This work is currently a preprint and has not undergone peer review.

**Method**  
MSAVBench introduces a hybrid evaluation framework that encompasses four dimensions: video, audio, shot, and reference. It supports diverse task settings and varying shot counts, accommodating up to 15 shots. The framework incorporates an adaptive self-correction mechanism for shot segmentation, which enhances robustness in evaluation. Additionally, it employs instance-wise rubrics for subjective metrics and tool-grounded evidence extraction to facilitate complex judgments. The benchmark is designed to align closely with human evaluations, achieving a Spearman rank correlation of 91.5% with human judgments. The authors systematically evaluate 19 state-of-the-art models, both closed- and open-source, to assess their performance against the new benchmark.

**Results**  
The evaluation reveals that current MSAV models exhibit significant deficiencies in director-level control and fine-grained audio-visual synchronization. The results indicate that while some models perform adequately in generating coherent narratives, they struggle with the nuanced integration of audio and video elements. The authors highlight that modular or agentic generation pipelines show promise in bridging the performance gap between open- and closed-source models. Specific performance metrics and comparisons to baseline models are not disclosed in the abstract, but the high correlation with human judgments suggests that the benchmark effectively captures qualitative aspects of MSAV generation.

**Limitations**  
The authors acknowledge that while MSAVBench provides a more robust evaluation framework, it may still be limited by the inherent challenges of subjective assessments in audio-video generation. The reliance on human judgments, despite high correlation, introduces variability that could affect reproducibility. Additionally, the benchmark's focus on specific task settings may not encompass all potential use cases in MSAV generation. The authors do not discuss potential biases in the dataset or the generalizability of the evaluation framework across different domains.

**Why it matters**  
The introduction of MSAVBench is significant for advancing the field of multi-shot audio-video generation. By providing a comprehensive and adaptive evaluation framework, it enables researchers to systematically assess and compare the performance of various models, fostering innovation and improvement in this area. The benchmark's alignment with human judgments enhances its utility for guiding future research directions and model development. The release of the benchmark data and evaluation code will facilitate further exploration and experimentation, potentially leading to breakthroughs in audio-video synthesis technologies.

Authors: Yujie Wei, Yujin Han, Zhekai Chen, Yongming Li, Kaixun Jiang, Zhihang Liu, Quanhao Li, Zhiwu Qing et al.  
Source: arXiv:2605.20183  
URL: https://arxiv.org/abs/2605.20183v1
