---
title: "Unified Map Prior Encoder for Mapping and Planning"
date: 2026-05-04 16:01:30 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02762v1"
arxiv_id: "2605.02762"
authors: ["Zongzheng Zhang", "Sizhe Zou", "Guantian Zheng", "Zhenxin Zhu", "Yu Gao", "Guoxuan Chi"]
slug: unified-map-prior-encoder-for-mapping-and-planning
summary_word_count: 449
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing online mapping and end-to-end (E2E) planning systems in autonomous driving, which predominantly rely on sensor data while underutilizing diverse map priors such as high-definition (HD) and standard-definition (SD) vector maps, rasterized SD maps, and satellite imagery. The authors highlight issues related to the heterogeneity of these data sources, pose drift, and inconsistent availability during inference. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution is the Unified Map Prior Encoder (UMPE), which integrates multiple map priors into a unified framework for both mapping and planning tasks. UMPE consists of two main branches: a vector encoder and a raster encoder. The vector encoder employs a frame-wise SE(2) correction to pre-align HD/SD polylines, utilizing multi-frequency sinusoidal features to encode points and generate polyline tokens with associated confidence scores. The raster encoder, based on a ResNet-18 backbone conditioned by FiLM, performs SE(2) micro-alignment and incorporates map priors through zero-initialized residual fusion, ensuring the model starts from a neutral baseline. The architecture employs a vector-then-raster fusion strategy, reflecting a geometric-first, appearance-second inductive bias. The model is trained on a combination of map priors, enhancing its robustness and performance.

**Results**  
On the nuScenes dataset, UMPE improves the mean Average Precision (mAP) of MapTRv2 from 61.5 to 67.4 (+5.9) and MapQR from 66.4 to 71.7 (+5.3). In the Argoverse2 benchmark, UMPE achieves an additional +4.1 mAP over strong baseline models. For E2E planning using the VAD backbone on nuScenes, UMPE reduces average trajectory error from 0.72 m to 0.42 m (-0.30 m) and decreases the collision rate from 0.22% to 0.12% (-0.10%). These results demonstrate significant improvements over recent prior-injection methods, showcasing the effectiveness of a unified approach to heterogeneous map priors.

**Limitations**  
The authors acknowledge that the performance gains are contingent on the availability of multiple map priors during training, which may not always be feasible in real-world scenarios. Additionally, the reliance on a specific architecture (ResNet-18) may limit generalizability to other backbone networks. The paper does not address potential computational overhead introduced by the complex fusion mechanisms, which could impact real-time applications.

**Why it matters**  
The implications of this work are substantial for the field of autonomous driving, as it demonstrates that a unified, alignment-aware approach to integrating heterogeneous map priors can lead to significant enhancements in both mapping accuracy and planning reliability. This could pave the way for more robust autonomous systems capable of operating in diverse environments with varying data availability, ultimately improving safety and efficiency in real-world applications.

Authors: Zongzheng Zhang, Sizhe Zou, Guantian Zheng, Zhenxin Zhu, Yu Gao, Guoxuan Chi, Shuo Wang, Yuwen Heng et al.  
Source: arXiv:2605.02762  
URL: https://arxiv.org/abs/2605.02762v1
