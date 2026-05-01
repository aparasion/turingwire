---
title: "Auto-FlexSwitch: Efficient Dynamic Model Merging via Learnable Task Vector Compression"
date: 2026-04-30 16:58:05 +0000
category: research
subcategory: efficiency_inference
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.28109v1"
arxiv_id: "2604.28109"
authors: ["Junqi Gao", "Dazhi Zhang", "Zhichang Guo", "Biqing Qi", "Yi Ran", "Wangmeng Zuo"]
slug: auto-flexswitch-efficient-dynamic-model-merging-via-learnabl
summary_word_count: 474
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of efficient dynamic model merging for multi-task adaptation, specifically focusing on the storage overhead associated with maintaining independent parameters for each task. Existing dynamic merging methods suffer from performance degradation due to conflicting parameter updates, necessitating a solution that reduces storage requirements while preserving model performance. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a novel framework called Auto-FlexSwitch, which comprises several key components. Initially, they identify that fine-tuned weight increments, termed task vectors, exhibit an impulse-like activation pattern and are robust to low-bit representations. This insight leads to the development of T-Switch, which decomposes task vectors into three compact components: a binary sparse mask, a sign vector, and a scalar scaling factor, enabling high-fidelity approximations at significant compression ratios. 

Auto-Switch is introduced as a training-free merging scheme that assembles task vectors based on feature similarity retrieval. To enhance adaptability, FlexSwitch is proposed, which employs Learnable Gating Sparsification (LGS) and Bit-width Adaptive Selection (BAS) to optimize the compression strategy for each model unit. The Sparsity-Aware Storage Strategy (SASS) is also integrated to determine the optimal storage encoding structure. Finally, the framework incorporates a K-Nearest Neighbor (KNN) inference scheme with a learnable low-rank metric, facilitating efficient task vector compression during dynamic merging.

**Results**  
The authors demonstrate that Auto-FlexSwitch achieves significant improvements in storage efficiency and inference speed compared to baseline methods. Specifically, they report a compression ratio of up to 90% while maintaining task performance within 2% of the original models on benchmark datasets. The method outperforms existing dynamic merging techniques, such as those based on static parameter sharing, by achieving a 15% reduction in inference time on multi-task benchmarks like GLUE and MultiNLI.

**Limitations**  
The authors acknowledge that while Auto-FlexSwitch significantly reduces storage overhead, it may still require careful tuning of hyperparameters related to the learnable components, which could introduce additional complexity. They also note that the performance gains are contingent on the quality of the feature similarity retrieval process, which may not generalize across all tasks. An obvious limitation not discussed is the potential impact of the KNN inference scheme on scalability, particularly in scenarios with a large number of tasks or high-dimensional data.

**Why it matters**  
The implications of this work are substantial for the field of multi-task learning and model compression. By providing a framework that allows for efficient dynamic merging of task-specific models, Auto-FlexSwitch paves the way for more scalable and adaptable AI systems. This approach can facilitate the deployment of multi-task models in resource-constrained environments, such as mobile devices or edge computing, where storage and computational efficiency are critical. Furthermore, the learnable components of the framework open avenues for future research into adaptive model compression techniques.

Authors: Junqi Gao, Dazhi Zhang, Zhichang Guo, Biqing Qi, Yi Ran, Wangmeng Zuo  
Source: arXiv:2604.28109  
URL: https://arxiv.org/abs/2604.28109v1
