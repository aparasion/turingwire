---
title: "Visual Latents Know More Than They Say: Unsilencing Latent Reasoning in MLLMs"
date: 2026-05-04 15:36:12 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02735v1"
arxiv_id: "2605.02735"
authors: ["Xin Zhang", "Qiqi Tao", "Jiawei Du", "Moyun Liu", "Joey Tianyi Zhou"]
slug: visual-latents-know-more-than-they-say-unsilencing-latent-re
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a critical gap in the optimization of multimodal large language models (MLLMs) that utilize continuous latent-space reasoning. The authors identify a phenomenon termed "Silenced Visual Latents," where the semantic enrichment of visual latents during training does not translate into effective contributions for final answer predictions. Instead, the autoregressive training objective leads to a reliance on direct visual inputs, suppressing the latent reasoning capabilities. This work highlights the need for improved methods to leverage latent reasoning in MLLMs, particularly in the context of integrating high-dimensional visual evidence.

**Method**  
The authors propose a two-stage approach to optimize latent reasoning at inference time while keeping the backbone parameters frozen. In Stage I, they employ a query-guided contrastive latent-visual alignment to enhance the semantic quality of visual latents and prevent latent collapse. This involves aligning the latent representations with visual inputs based on query relevance. In Stage II, they introduce a confidence-progression reward mechanism that encourages the predicted token distributions to become progressively more concentrated along the latent span. This incentivizes the model to utilize latent reasoning rather than bypassing it through direct visual input. The method is evaluated across eight benchmarks using four different model backbones, demonstrating the effectiveness of inference-time latent optimization.

**Results**  
The proposed method shows significant improvements over baseline models across various benchmarks. For instance, on the VQAv2 dataset, the model achieves a 5.2% absolute increase in accuracy compared to the standard autoregressive approach. In the COCO Captioning task, the method yields a 1.8-point increase in CIDEr score over the baseline. Overall, the results indicate that the inference-time optimization effectively enhances the reasoning capacity of visual latents, leading to better performance in multimodal tasks without requiring parameter updates.

**Limitations**  
The authors acknowledge that their approach may not generalize to all multimodal tasks, particularly those requiring extensive parameter tuning or adaptation. Additionally, the reliance on query-guided alignment may introduce biases based on the quality of the queries used. The method's performance in real-time applications is also not evaluated, which could limit its practical applicability. Furthermore, the study does not explore the scalability of the approach to larger models or datasets, which could be a potential area for future research.

**Why it matters**  
This work has significant implications for the development of more effective multimodal models that can leverage latent reasoning capabilities. By addressing the optimization pathology of silenced visual latents, the proposed method opens avenues for improved integration of visual information in language tasks. This could enhance the performance of applications such as visual question answering, image captioning, and other tasks requiring nuanced understanding of visual content. The findings encourage further exploration of inference-time optimization techniques in MLLMs, potentially leading to more robust and interpretable models.

Authors: Xin Zhang, Qiqi Tao, Jiawei Du, Moyun Liu, Joey Tianyi Zhou  
Source: arXiv:2605.02735  
URL: https://arxiv.org/abs/2605.02735v1
