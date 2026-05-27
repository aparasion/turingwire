---
title: "Real Images, Worse Judgments: Evaluating Vision-Language Models on Concreteness and Imagery"
date: 2026-05-26 17:24:59 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27315v1"
arxiv_id: "2605.27315"
authors: ["Yifan Jiang", "Ruoxi Ning", "Sheng Yao", "Freda Shi"]
slug: real-images-worse-judgments-evaluating-vision-language-model
summary_word_count: 474
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the efficacy of visual inputs in enhancing language comprehension within vision-language models (VLMs). Specifically, it questions the assumption that real images consistently improve lexical judgments by evaluating how VLMs discern relevant visual evidence from incidental context. The study focuses on human ratings of concreteness and imagery, which vary across a spectrum of word types, from abstract to concrete. The authors highlight that existing literature lacks a thorough examination of the impact of visual context on lexical judgments, particularly in terms of alignment with human evaluations.

**Method**  
The authors employ a combination of human ratings and quantitative analyses to assess the performance of VLMs. They utilize human-conducted concreteness and imagery ratings as benchmarks, spanning a range of lexical items. The core technical contributions include probing techniques and canonical correlation analysis to investigate the representational shifts induced by real-image contexts. An attribution case study is also conducted to illustrate how VLMs respond to visual cues. The authors propose a method where models are instructed to prioritize textual content during inference, aiming to mitigate the negative effects of irrelevant visual information. The training compute and specific architectures used in the experiments are not disclosed.

**Results**  
The findings reveal that real-image contexts do not consistently enhance VLM performance and can, in fact, degrade alignment with human ratings, particularly for words with low visual relevance. The authors report that the introduction of visual context leads to representational shifts that increase sensitivity to spurious visual cues, resulting in a weaker recovery of targeted lexical properties. Notably, when models are instructed to focus solely on textual content, there are significant improvements in performance, especially for the most vulnerable subsets of words. The results indicate that the performance of VLMs is not uniformly enhanced by visual inputs, challenging the prevailing assumption in the field.

**Limitations**  
The authors acknowledge that their study is limited by the scope of the datasets used for human ratings and the specific VLMs evaluated. They do not explore the potential effects of different types of visual inputs or the impact of varying model architectures on the observed results. Additionally, the lack of disclosure regarding training compute and model specifics may hinder reproducibility and generalization of the findings. The study also does not address the long-term implications of these findings on the design of future VLMs.

**Why it matters**  
This work has significant implications for the development of VLMs, particularly in refining how visual context is integrated into language understanding tasks. The findings suggest that current instruction-tuned VLMs require improved calibration mechanisms to discern when visual information is beneficial for lexical judgments. This could lead to more robust models that better align with human cognitive processes, ultimately enhancing applications in natural language processing, multimodal understanding, and human-computer interaction.

Authors: Yifan Jiang, Ruoxi Ning, Sheng Yao, Freda Shi  
Source: arXiv:2605.27315  
URL: [https://arxiv.org/abs/2605.27315v1](https://arxiv.org/abs/2605.27315v1)
