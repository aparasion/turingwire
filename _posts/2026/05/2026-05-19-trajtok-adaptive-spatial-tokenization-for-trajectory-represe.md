---
title: "TrajTok: Adaptive Spatial Tokenization for Trajectory Representation Learning"
date: 2026-05-19 17:18:32 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20134v1"
arxiv_id: "2605.20134"
authors: ["Zhen Xiong", "Shang-Ling Hsu", "Cyrus Shahabi"]
slug: trajtok-adaptive-spatial-tokenization-for-trajectory-represe
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of learning generalizable trajectory representations from raw GPS traces, which are inherently continuous, noisy, and irregularly sampled. The authors highlight the limitations of existing spatial tokenization methods, where fine grids lead to sparse cell embeddings and coarse grids amalgamate heterogeneous movement patterns, resulting in suboptimal representation learning. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution is TrajTok, a trajectory encoder that employs a multi-resolution hexagonal cell partitioning strategy to convert noisy GPS sequences into discrete cell tokens. This approach allows for a more nuanced representation of spatial data. The architecture utilizes a factorized transformer encoder that incorporates early per-modality self-attention blocks and cross-attention fusion layers, alongside spatiotemporal rotary position embeddings (ST-RoPE) to effectively encode both the geometric and kinematic aspects of the trajectory data. TrajTok is pretrained using a masked-token modeling approach, which aims to recover geometric structures and kinematic patterns from partial trajectory observations. The pretraining recipe is designed to enhance the transferability of the learned embeddings across various tasks.

**Results**  
The authors evaluate TrajTok on the Porto dataset, demonstrating its efficacy in multiple trajectory-related tasks, including trajectory similarity search, classification, estimated time of arrival, and full travel-time regression. The frozen TrajTok encoder, augmented with lightweight task adapters, achieves superior performance compared to several task-specific baselines. Notably, it outperforms methods tailored for either geometry-dominated or kinematics-dominated tasks, indicating that TrajTok effectively captures transferable trajectory structures rather than relying on task-specific heuristics. The results suggest a significant improvement in performance metrics, although specific numerical values and effect sizes are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while TrajTok shows promise, it may still be limited by the quality and representativeness of the GPS data used for training. Additionally, the reliance on hexagonal cell partitioning may not be optimal for all types of trajectory data, and the generalizability of the model to other datasets or domains remains to be fully validated. The paper does not address potential computational costs associated with the pretraining phase or the scalability of the model to larger datasets.

**Why it matters**  
The implications of this work are significant for the development of general-purpose trajectory foundation models. By demonstrating that a single frozen encoder can effectively handle diverse trajectory tasks, TrajTok paves the way for more efficient and transferable models in trajectory representation learning. This approach could facilitate advancements in various applications, including autonomous navigation, urban planning, and transportation systems, where understanding and predicting movement patterns is crucial.

Authors: Zhen Xiong, Shang-Ling Hsu, Cyrus Shahabi  
Source: arXiv:2605.20134  
URL: [https://arxiv.org/abs/2605.20134v1](https://arxiv.org/abs/2605.20134v1)
