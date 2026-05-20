---
title: "MetaEarth-MM: Unified Multimodal Remote Sensing Image Generation with Scene-centered Joint Modeling"
date: 2026-05-19 16:47:02 +0000
category: research
subcategory: multimodal
company: "Meta"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20090v1"
arxiv_id: "2605.20090"
authors: ["Zhiping Yu", "Chenyang Liu", "Jinqi Cao", "Qinzhe Yang", "Siwei Yu", "Zhengxia Zou"]
slug: metaearth-mm-unified-multimodal-remote-sensing-image-generat
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of generating multi-modal remote sensing images, particularly in scenarios where complete paired observations are scarce. Existing generative methods typically focus on isolated pairwise modality translation, which limits their scalability and versatility as the number of modalities and generation tasks increases. The authors propose a unified generative foundation model, MetaEarth-MM, to facilitate paired joint generation and any-to-any translation across five modalities, filling a gap in the literature regarding comprehensive multi-modal remote sensing image generation. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
MetaEarth-MM introduces a scene-centered joint modeling paradigm that emphasizes the intrinsic scene consistency of multi-modal observations. The architecture is decoupled into two main components: first, it infers a latent scene representation from the available observations, and second, it generates target modalities conditioned on this intermediate latent state. This approach contrasts with previous methods that rely on direct appearance-level cross-modal mapping. The model is trained on the EarthMM dataset, which consists of 2.8 million multi-resolution global images, including 2.2 million aligned pairs. The training process and specific loss functions are not detailed in the abstract, but the scale of the dataset suggests significant computational resources were utilized.

**Results**  
MetaEarth-MM demonstrates strong generative capabilities and robust generalization across various generation tasks. While specific quantitative results are not provided in the abstract, the authors claim that their model outperforms existing baselines in terms of generative quality and task versatility. The paper likely includes detailed comparisons against named benchmarks, which would provide insight into effect sizes and performance metrics, although these specifics are not disclosed in the summary.

**Limitations**  
The authors acknowledge that their model's performance may be contingent on the quality and diversity of the training dataset, EarthMM. They do not discuss potential biases in the dataset or limitations related to the generalizability of the model across different geographical regions or environmental conditions. Additionally, the reliance on a latent scene representation may introduce challenges in accurately capturing complex scene dynamics that are not well-represented in the training data.

**Why it matters**  
The development of MetaEarth-MM has significant implications for downstream applications in Earth observation, particularly in enhancing the capabilities of remote sensing technologies. By providing a unified framework for multi-modal image generation, this model can facilitate improved data synthesis for various applications, including environmental monitoring, urban planning, and disaster response. The ability to perform any-to-any translation across modalities also opens avenues for more flexible and efficient data utilization in remote sensing tasks, potentially leading to advancements in machine learning applications within this domain.

Authors: Zhiping Yu, Chenyang Liu, Jinqi Cao, Qinzhe Yang, Siwei Yu, Zhengxia Zou, Zhenwei Shi  
Source: arXiv:2605.20090  
URL: [https://arxiv.org/abs/2605.20090v1](https://arxiv.org/abs/2605.20090v1)
