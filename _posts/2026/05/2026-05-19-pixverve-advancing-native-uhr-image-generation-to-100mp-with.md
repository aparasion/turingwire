---
title: "PixVerve: Advancing Native UHR Image Generation to 100MP with a Large-Scale High-Quality Dataset"
date: 2026-05-19 17:35:09 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20147v1"
arxiv_id: "2605.20147"
authors: ["Haojun Chen", "Haoyang He", "Chengming Xu", "Qingdong He", "Junwei Zhu", "Yabiao Wang"]
slug: pixverve-advancing-native-uhr-image-generation-to-100mp-with
summary_word_count: 445
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of existing Text-to-Image (T2I) models to generate Ultra-High-Resolution (UHR) images, specifically those with a minimum pixel count of 100 million. While recent advancements have improved T2I models for 1K and 2K resolutions, the demand for UHR image generation has surged due to enhanced visual experiences and imaging technologies. The authors present a novel dataset, PixVerve-95K, to facilitate this advancement. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of the PixVerve-95K dataset, which consists of 95,000 high-quality images annotated across seven dimensions. The dataset is curated through a meticulously designed data pipeline to ensure diversity and quality. The authors extend various T2I foundation models to achieve native 100MP image generation using three distinct training schemes. These schemes are not explicitly detailed in the abstract, but they likely involve modifications to the model architecture and training protocols to accommodate the high-resolution output. Additionally, the authors propose the PixVerve-Bench benchmark, which incorporates both conventional image quality metrics and assessments based on multimodal large language models to evaluate visual quality and semantic alignment comprehensively.

**Results**  
The paper reports extensive experimental results on the PixVerve-Bench benchmark, demonstrating significant improvements in UHR image generation capabilities compared to existing baselines. While specific numerical results and effect sizes are not provided in the abstract, the authors claim that their approach yields superior performance in both visual fidelity and semantic coherence. The benchmark's comprehensive evaluation protocol is designed to facilitate comparisons with other state-of-the-art T2I models, although exact performance metrics against named baselines are not disclosed in the abstract.

**Limitations**  
The authors acknowledge the inherent challenges in UHR image generation, such as the complexity of high-resolution content and the potential for increased computational demands during training. They do not explicitly mention the limitations of their dataset, such as potential biases in the image selection process or the representativeness of the scenarios covered. Additionally, the scalability of their training schemes to even higher resolutions or different modalities remains unaddressed.

**Why it matters**  
This work has significant implications for the field of generative models, particularly in enhancing the capabilities of T2I systems to produce high-quality UHR images. The introduction of the PixVerve-95K dataset and the PixVerve-Bench benchmark provides a valuable resource for researchers aiming to push the boundaries of image generation. By addressing the challenges associated with UHR content, this research paves the way for future advancements in applications such as virtual reality, high-end visual media, and other domains requiring high-resolution imagery.

Authors: Haojun Chen, Haoyang He, Chengming Xu, Qingdong He, Junwei Zhu, Yabiao Wang, Zhucun Xue, Xianfang Zeng et al.  
Source: arXiv:2605.20147  
URL: [https://arxiv.org/abs/2605.20147v1](https://arxiv.org/abs/2605.20147v1)
