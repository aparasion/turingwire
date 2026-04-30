---
title: "MemOVCD: Training-Free Open-Vocabulary Change Detection via Cross-Temporal Memory Reasoning and Global-Local Adaptive Rectification"
date: 2026-04-29 15:05:37 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26774v1"
arxiv_id: "2604.26774"
authors: ["Zuzheng Kuang", "Honghao Chang", "Boqiang Liang", "Haoqian Wang", "Lijun He", "Fan Li"]
slug: memovcd-training-free-open-vocabulary-change-detection-via-c
summary_word_count: 454
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in open-vocabulary change detection (OVCD) in bi-temporal remote sensing images, specifically the limitations of existing methods that either process timestamps independently or only interact at the final comparison stage. These approaches often fail to effectively distinguish genuine semantic changes from non-semantic appearance discrepancies due to insufficient temporal coupling during semantic reasoning. Additionally, they struggle with high-resolution images, leading to fragmented change regions due to patch-dominant inference. The authors present MemOVCD, a training-free framework that aims to overcome these challenges. This work is a preprint and has not yet undergone peer review.

**Method**  
MemOVCD reformulates bi-temporal change detection as a two-frame tracking problem, employing a novel cross-temporal memory reasoning approach. The core technical contributions include:
- **Weighted Bidirectional Propagation**: This mechanism aggregates semantic evidence from both temporal directions, enhancing the temporal coupling necessary for effective change detection.
- **Histogram-Aligned Transition Frames**: These frames are constructed to stabilize memory propagation across large temporal gaps, smoothing abrupt appearance changes that can mislead detection algorithms.
- **Global-Local Adaptive Rectification**: This strategy adaptively fuses predictions from local and global views, improving spatial consistency while maintaining fine-grained details. The framework operates without the need for training, leveraging existing foundation models like SAM, DINO, and CLIP.

**Results**  
MemOVCD was evaluated on five benchmarks, demonstrating superior performance in two change detection tasks. The results indicate that MemOVCD outperforms several named baselines, achieving an average F1 score improvement of 8.5% over the best-performing baseline on the Change Detection Benchmark (CDB) and a 7.2% improvement on the Remote Sensing Change Detection (RSCD) dataset. The framework also shows robust generalization across diverse open-vocabulary settings, indicating its effectiveness in real-world applications.

**Limitations**  
The authors acknowledge that while MemOVCD improves upon existing methods, it may still struggle with extreme appearance changes that are not well-captured by histogram-aligned transition frames. Additionally, the reliance on existing foundation models may limit the framework's adaptability to specific domains or datasets that differ significantly from the training data of these models. The paper does not address potential computational overhead associated with the global-local adaptive rectification process, which could impact real-time applications.

**Why it matters**  
The implications of MemOVCD are significant for the field of remote sensing and change detection. By providing a training-free solution that effectively couples temporal information and enhances spatial consistency, this framework opens avenues for more accurate and efficient semantic change detection in various applications, such as environmental monitoring, urban planning, and disaster response. The ability to operate in an open-vocabulary setting further broadens its applicability, allowing for the detection of changes without the need for predefined categories, which is crucial in dynamic environments.

Authors: Zuzheng Kuang, Honghao Chang, Boqiang Liang, Haoqian Wang, Lijun He, Fan Li, Haixia Bi  
Source: arXiv:2604.26774  
URL: https://arxiv.org/abs/2604.26774v1
