---
title: "Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context"
date: 2026-05-13 17:52:53 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13831v1"
arxiv_id: "2605.13831"
authors: ["Zhaowei Wang", "Lishu Luo", "Haodong Duan", "Weiwei Liu", "Sijin Wu", "Ji Luo"]
slug: training-long-context-vision-language-models-effectively-wit
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in effective training methodologies for long-context vision-language models (LVLMs), particularly in the context of managing and generalizing across extended sequences beyond 128K tokens. While long-context modeling is critical for applications such as long-document understanding and video analysis, existing training recipes are insufficiently explored, especially regarding the design and balance of long-context data mixtures.

**Method**  
The authors propose a systematic approach to long-context continued pre-training, extending a 7B parameter model (Qwen2.5-VL-7B) from a context length of 32K to 128K tokens. The methodology includes extensive ablation studies on long-document data, focusing on three primary findings:  
1. A balanced sequence-length distribution in training data outperforms a target-length-focused approach, indicating that effective long-context modeling necessitates generalizable key-information retrieval across varying lengths and positions.  
2. Retrieval mechanisms are identified as the primary bottleneck, advocating for data mixtures that emphasize retrieval tasks while incorporating modest reasoning data to enhance task diversity.  
3. The use of instruction-formatted long data in pure long-document visual question answering (VQA) preserves short-context capabilities, reducing the necessity for short-context data mixing.  
The resulting model, termed MMProLong, is trained with a budget of 5 billion tokens and demonstrates improved long-document VQA performance.

**Results**  
MMProLong achieves a 7.1% improvement in long-document VQA scores compared to baseline models. It maintains robust performance at extended context lengths of 256K and 512K tokens, surpassing its original 128K training window without requiring additional training. The model also generalizes effectively to tasks such as webpage-based multimodal needle retrieval, long-context vision-text compression, and long-video understanding, all without task-specific supervision.

**Limitations**  
The authors acknowledge that their findings are based on a specific model architecture and training budget, which may not generalize across all LVLMs. They do not address potential limitations related to the scalability of their approach to even longer contexts or the impact of varying data quality in long-document datasets. Additionally, the reliance on retrieval-heavy mixtures may not be optimal for all applications, particularly those requiring nuanced reasoning.

**Why it matters**  
This work provides a foundational framework for advancing long-context capabilities in LVLMs, which are increasingly relevant in complex applications requiring sustained context management. The introduction of a practical LongPT recipe and empirical insights into data mixture strategies can inform future research and development in the field, potentially leading to more effective models for long-document understanding and multimodal tasks. The findings also suggest avenues for further exploration in optimizing retrieval mechanisms and enhancing generalization across diverse tasks.

Authors: Zhaowei Wang, Lishu Luo, Haodong Duan, Weiwei Liu, Sijin Wu, Ji Luo, Shen Yan, Shuai Peng et al.  
Source: arXiv:2605.13831  
URL: https://arxiv.org/abs/2605.13831v1
