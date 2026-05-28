---
title: "The Abstraction Gap in Vision-Language Causal Reasoning"
date: 2026-05-27 17:38:10 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28779v1"
arxiv_id: "2605.28779"
authors: ["Chinh Hoang", "Mohammad Rashedul Hasan"]
slug: the-abstraction-gap-in-vision-language-causal-reasoning
summary_word_count: 414
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of existing evaluation methodologies for Vision-Language Models (VLMs) in distinguishing between linguistic plausibility and faithful causal reasoning. The authors highlight that current benchmarks do not effectively measure a model's ability to generate causal explanations that are not only linguistically coherent but also grounded in causal relationships. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors propose a dual-probe methodology to evaluate VLMs, consisting of two distinct probes: the Text-Only Probe and the Chain-Text Probe. The Text-Only Probe assesses the linguistic quality of the generated explanations, while the Chain-Text Probe requires models to produce explicit causal chains before generating explanations. The Abstraction Gap (AG) metric is introduced to quantify the normalized performance difference between these two probes. The evaluation is conducted on the Causal Abstraction Gap Evaluation (CAGE) benchmark, which comprises 49,500 questions across 5,500 images, designed to span Judea Pearl's causal hierarchy. The study also investigates the impact of fine-tuning on 45,000 chain-annotated examples to determine if it can mitigate the AG.

**Results**  
The evaluation of eight VLMs reveals that seven of them exhibit an AG exceeding 0.50, indicating a significant disparity between their text scores (ranging from 6 to 8) and chain scores (below 2.5). Notably, one model achieves a near-zero AG, suggesting that the capability for faithful causal reasoning exists within current VLM architectures. The results indicate that the performance gap is influenced by pretraining and architectural choices rather than merely the quantity of training data.

**Limitations**  
The authors acknowledge that their methodology may not capture all dimensions of causal reasoning and that the reliance on pretraining and architecture may limit the generalizability of their findings. Additionally, the benchmark CAGE, while comprehensive, may not encompass all possible causal scenarios, potentially constraining the evaluation's applicability. The authors do not discuss the computational resources required for training or evaluating the models, which could be a significant factor for practitioners.

**Why it matters**  
This work has significant implications for the development and evaluation of VLMs, particularly in applications requiring robust causal reasoning, such as automated reasoning systems and decision-making frameworks. By providing a diagnostic tool (CAGE) for assessing faithful causal reasoning, the authors pave the way for future research to focus on bridging the abstraction gap in VLMs. This could lead to advancements in model architectures and training methodologies that prioritize causal understanding, ultimately enhancing the reliability of VLMs in real-world applications.

Authors: Chinh Hoang, Mohammad Rashedul Hasan  
Source: arXiv:2605.28779  
URL: [https://arxiv.org/abs/2605.28779v1](https://arxiv.org/abs/2605.28779v1)
