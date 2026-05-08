---
title: "DPM++: Dynamic Masked Metric Learning for Occluded Person Re-identification"
date: 2026-05-07 17:47:23 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.06637v1"
arxiv_id: "2605.06637"
authors: ["Lei Tan", "Yingshi Luan", "Pincong Zou", "Pingyang Dai", "Liujuan Cao"]
slug: dpm-dynamic-masked-metric-learning-for-occluded-person-re-id
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of occluded person re-identification (Re-ID), a significant gap in the literature that persists despite advancements in the field. Existing methods often rely on pre-trained models for estimating visible parts or augmenting data to simulate occlusions, but they lack a cohesive framework that effectively learns visibility-consistent matching under realistic occlusion conditions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose DPM++, a Dynamic Masked Metric Learning framework designed to tackle the occlusion problem in person Re-ID. The core technical contribution is the development of an input-adaptive masked metric that dynamically selects reliable identity subspaces for each occluded instance. This approach emphasizes visibility-consistent evidence while suppressing unreliable features. DPM++ employs a two-stage supervision scheme based on CLIP (Contrastive Language-Image Pretraining), where semantic priors are learned from the text branch and integrated into the classifier-prototype space for dynamic masked matching. Additionally, a saliency-guided patch transfer strategy is introduced to synthesize controllable and photo-realistic occluded samples during training, enhancing the model's exposure to realistic partial observations. The framework also incorporates occlusion-aware sample pairing and mask-guided optimization to improve stability and effectiveness.

**Results**  
DPM++ demonstrates superior performance on both occluded and holistic person Re-ID benchmarks compared to state-of-the-art methods. Specifically, it achieves a 5.2% improvement in mAP (mean Average Precision) and a 6.1% increase in Rank-1 accuracy on the Occluded DukeMTMC dataset compared to the previous best method. On the Market-1501 dataset, DPM++ shows a 3.4% improvement in mAP and a 4.5% increase in Rank-1 accuracy over existing approaches. These results indicate a significant enhancement in the model's ability to handle occlusions effectively.

**Limitations**  
The authors acknowledge that while DPM++ improves performance in occluded scenarios, it may still struggle with extreme occlusions where critical identity features are entirely missing. Additionally, the reliance on CLIP for semantic priors may limit the framework's applicability to domains where such pre-trained models are not available. The paper does not address the computational overhead introduced by the two-stage supervision scheme and the saliency-guided patch transfer strategy, which may affect training efficiency.

**Why it matters**  
The implications of this work are substantial for downstream applications in surveillance, autonomous driving, and human-computer interaction, where occlusion is a common challenge. By providing a unified framework for learning visibility-consistent matching, DPM++ paves the way for more robust Re-ID systems that can operate effectively in real-world scenarios. This research could inspire further exploration into adaptive metric learning techniques and the integration of semantic information in visual recognition tasks.

Authors: Lei Tan, Yingshi Luan, Pincong Zou, Pingyang Dai, Liujuan Cao  
Source: arXiv:2605.06637  
URL: https://arxiv.org/abs/2605.06637v1
