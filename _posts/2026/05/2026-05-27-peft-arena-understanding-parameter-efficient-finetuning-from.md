---
title: "PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective"
date: 2026-05-27 17:59:51 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28819v1"
arxiv_id: "2605.28819"
authors: ["Yangyi Huang", "Ruotian Peng", "Zeju Qiu", "Jiale Kang", "Yandong Wen", "Bernhard Sch\u00f6lkopf"]
slug: peft-arena-understanding-parameter-efficient-finetuning-from
summary_word_count: 452
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the evaluation of parameter-efficient finetuning (PEFT) methods for large language models, particularly the lack of a comprehensive framework that balances downstream task performance with the retention of pretrained capabilities. The authors argue that existing evaluations focus predominantly on accuracy metrics, neglecting the critical aspect of stability-plasticity, which refers to the trade-off between adapting to target tasks and resisting catastrophic forgetting of general capabilities. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce PEFT-Arena, a benchmark designed to jointly assess downstream performance and general capability retention. The core technical contributions include a detailed analysis of PEFT methods through two geometric perspectives: weight space and activation space. In weight space, spectral analysis is employed to investigate how different parameterizations interact with the pretrained singular-value structure. In activation space, retention metrics are developed to evaluate whether finetuning preserves or distorts general-capability representations. The study also identifies that forgetting is associated with non-isometric representation distortion. The authors propose a post-hoc improvement strategy involving path-wise rewinding to enhance target retention after finetuning.

**Results**  
The evaluation of various PEFT methods reveals distinct stability-plasticity profiles, with orthogonal finetuning achieving the most favorable Pareto frontier under comparable parameter budgets. The authors provide quantitative results demonstrating that orthogonal finetuning outperforms other methods in terms of both downstream task accuracy and retention of pretrained capabilities. Specific performance metrics are not disclosed in the abstract, but the findings indicate that traditional finetuning approaches often lead to significant forgetting, while orthogonal methods maintain a better balance between adaptation and retention.

**Limitations**  
The authors acknowledge that their analysis is limited to the methods evaluated within the PEFT-Arena framework and that the findings may not generalize to all PEFT techniques. They also note that the spectral analysis and retention metrics are sensitive to the choice of pretrained model and task, which could influence the results. Additionally, the paper does not explore the computational overhead associated with the proposed path-wise rewinding strategy, which may limit its practical applicability in resource-constrained environments.

**Why it matters**  
This work has significant implications for the field of transfer learning and model adaptation, as it provides a structured approach to evaluate PEFT methods beyond mere accuracy. By framing the evaluation within the stability-plasticity dilemma, the authors encourage future research to consider both adaptation and retention, potentially leading to the development of more robust finetuning strategies. The introduction of PEFT-Arena as a benchmark could standardize evaluations in this area, fostering advancements in the design of parameter-efficient methods that maintain general capabilities while achieving high performance on specific tasks.

Authors: Yangyi Huang, Ruotian Peng, Zeju Qiu, Jiale Kang, Yandong Wen, Bernhard Schölkopf, Weiyang Liu  
Source: arXiv:2605.28819  
URL: [https://arxiv.org/abs/2605.28819v1](https://arxiv.org/abs/2605.28819v1)
