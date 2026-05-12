---
title: "Count Anything at Any Granularity"
date: 2026-05-11 17:32:37 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.10887v1"
arxiv_id: "2605.10887"
authors: ["Chang Liu", "Haoning Wu", "Weidi Xie"]
slug: count-anything-at-any-granularity
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing open-world object counting methods, which struggle to accurately count objects based on user intent due to the implicit nature of counting granularity. Current approaches typically treat counting as a single category-level matching problem, failing to accommodate the diverse ways users may specify what to count—ranging from specific identities to abstract concepts. The authors highlight a critical gap in the literature regarding the need for a framework that explicitly incorporates multi-grained counting, as well as the lack of suitable datasets that support this granularity.

**Method**  
The authors propose a novel framework for multi-grained counting, where visual exemplars define target appearances and fine-grained text prompts specify the intended semantic granularity across five levels. To facilitate this, they introduce KubriCount, a large-scale dataset created through an innovative data-scaling pipeline that combines controllable 3D synthesis, consistent image editing, and vision-language model (VLM)-based filtering. This dataset is designed to include multi-category scenes, controlled distractors, and instance-level annotations. The core technical contribution is the HieraCount model, which integrates both text and visual exemplars to enhance counting accuracy. The training process leverages the newly constructed KubriCount dataset, although specific details on training compute are not disclosed.

**Results**  
HieraCount demonstrates significant improvements in multi-grained counting accuracy compared to existing multimodal large language models and specialist counting models. The authors report that HieraCount outperforms baseline models on the KubriCount dataset, achieving a marked increase in accuracy across various granularity levels. While exact numerical results are not provided in the abstract, the systematic benchmarking indicates that prior models exhibit severe prompt-following failures when faced with fine-grained distinctions, underscoring the effectiveness of HieraCount in addressing these challenges.

**Limitations**  
The authors acknowledge that the reliance on a newly constructed dataset may introduce biases inherent to the data generation process. Additionally, while HieraCount improves upon existing models, it may still struggle with edge cases or highly ambiguous prompts that do not fit neatly into the defined granularity levels. The paper does not discuss potential computational inefficiencies or scalability issues that may arise when deploying HieraCount in real-world applications.

**Why it matters**  
This work has significant implications for the field of computer vision and natural language processing, particularly in applications requiring precise object counting in complex environments. By explicitly addressing counting granularity and providing a comprehensive dataset, the authors pave the way for future research that can build upon their findings. The introduction of HieraCount could enhance various downstream tasks, such as autonomous navigation, robotic manipulation, and interactive AI systems, where accurate object counting is critical for performance.

Authors: Chang Liu, Haoning Wu, Weidi Xie  
Source: arXiv:2605.10887  
URL: https://arxiv.org/abs/2605.10887v1
