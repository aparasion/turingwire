---
title: "SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation"
date: 2026-05-21 14:25:15 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22536v1"
arxiv_id: "2605.22536"
authors: ["Xiaolong Zhou", "Yifei Liu", "Ziyang Gong", "Jiarui Li", "Qiyue Zhao", "Muyao Niu"]
slug: spacedg-benchmarking-spatial-intelligence-under-visual-degra
summary_word_count: 488
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of spatial intelligence in Multimodal Large Language Models (MLLMs) by introducing the SpaceDG dataset, which focuses on the impact of visual degradation on spatial reasoning. Existing benchmarks predominantly utilize pristine visual inputs, neglecting the real-world conditions that introduce various forms of degradation, such as motion blur, low light, adverse weather, lens distortion, and compression artifacts. This oversight raises concerns about the robustness of MLLMs in practical applications. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose SpaceDG, a large-scale dataset designed for degradation-aware spatial understanding. The dataset is generated using a physically grounded degradation synthesis engine that integrates the degradation formation process into 3D Gaussian Splatting (3DGS) rendering. This approach allows for the realistic simulation of nine types of visual degradation. SpaceDG comprises approximately 1 million question-answer pairs derived from nearly 1,000 indoor scenes. Additionally, the authors introduce SpaceDG-Bench, a human-verified benchmark featuring 1,102 questions across 11 reasoning categories and 9 visual degradation types, resulting in over 10,000 Visual Question Answering (VQA) instances. The evaluation of 25 MLLMs, both open-source and closed-source, reveals the detrimental effects of visual degradation on spatial reasoning capabilities. Furthermore, the authors demonstrate that fine-tuning MLLMs on the SpaceDG dataset significantly enhances their robustness to visual degradation, achieving performance that can exceed human levels under degraded conditions while maintaining performance on clean images.

**Results**  
The evaluation results indicate that visual degradations lead to substantial impairments in spatial reasoning across all tested MLLMs. Specific performance metrics are not disclosed in the abstract, but the authors emphasize the critical robustness gap exposed by the degradation conditions. Fine-tuning on SpaceDG resulted in marked improvements in degradation robustness, with some models surpassing human performance in degraded scenarios. The paper suggests that this training approach does not compromise performance on clean images, indicating a dual benefit of degradation-aware training.

**Limitations**  
The authors acknowledge that the SpaceDG dataset, while comprehensive, may not encompass all possible real-world degradation scenarios. Additionally, the reliance on synthetic degradation may not fully capture the complexities of real-world visual inputs. The paper does not discuss potential biases in the dataset or the generalizability of the findings across different MLLM architectures. Furthermore, the evaluation is limited to a specific set of MLLMs, which may not represent the entire landscape of spatial reasoning models.

**Why it matters**  
The introduction of SpaceDG and its benchmarking framework has significant implications for the development of robust MLLMs capable of operating under real-world conditions. By highlighting the vulnerabilities of current models to visual degradation, this work encourages future research to focus on enhancing robustness through degradation-aware training methodologies. The findings underscore the necessity for datasets that reflect real-world challenges, ultimately contributing to the advancement of spatial intelligence in AI systems.

Authors: Xiaolong Zhou, Yifei Liu, Ziyang Gong, Jiarui Li, Qiyue Zhao, Muyao Niu, Yuanyuan Gao, Le Ma et al.  
Source: arXiv:2605.22536  
URL: https://arxiv.org/abs/2605.22536v1
