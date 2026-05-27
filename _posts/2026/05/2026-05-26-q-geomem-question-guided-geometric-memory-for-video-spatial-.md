---
title: "Q-GeoMem: Question-Guided Geometric Memory for Video Spatial Reasoning"
date: 2026-05-26 17:26:29 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27318v1"
arxiv_id: "2605.27318"
authors: ["Xianqiang Gao", "Qizhi Chen", "Delin Qu", "Haoming Song", "Zhigang Wang", "Bin Zhao"]
slug: q-geomem-question-guided-geometric-memory-for-video-spatial-
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing spatial video-language models in video spatial reasoning, particularly their treatment of memory as a generic temporal cache. This approach can lead to the inclusion of redundant or irrelevant geometric information, which undermines long-horizon reasoning capabilities. The authors propose a novel framework, Q-GeoMem, to enhance the retention of relevant information while accumulating viewpoint-dependent evidence over time. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Q-GeoMem introduces a question-guided geometric memory architecture that integrates camera-conditioned geometry into visual tokens. The framework maintains two distinct memory banks: the Fine-Grained Context Bank, which stores recent dense features and camera states, and the Semantic-Geometric Evidence Bank, which retains compact long-range evidence. The model employs a Q-Former-based mechanism to score candidate frames based on their relevance to the posed question and their novelty concerning the retained memory. This scoring system is crucial for determining which frames to keep in memory, utilizing a capacity-based replacement rule to ensure the banks remain compact. During the reasoning phase, both memory banks are read before updating the current frame representation, allowing for adaptive fusion of information.

**Results**  
Q-GeoMem demonstrates state-of-the-art performance on the VSI-Bench and VSTI-Bench benchmarks, outperforming existing spatial reasoning models. Specific performance metrics include an improvement of 5.2% on the VSI-Bench and 4.8% on the VSTI-Bench compared to the best baseline models. The ablation studies conducted by the authors confirm the significance of the proposed evidence scoring mechanism, indicating that the question-guided approach substantially enhances reasoning accuracy.

**Limitations**  
The authors acknowledge that the framework's reliance on the Q-Former for scoring may introduce biases based on the quality of the question representation. Additionally, the capacity-based replacement rule could lead to the loss of potentially useful information if not optimally tuned. The paper does not address the computational overhead introduced by maintaining two separate memory banks, which may impact real-time applications. Furthermore, the generalizability of the model across diverse video datasets remains untested.

**Why it matters**  
The introduction of Q-GeoMem has significant implications for advancing video spatial reasoning tasks, particularly in applications requiring nuanced understanding of dynamic environments, such as robotics and autonomous navigation. By effectively integrating question relevance into memory management, this framework paves the way for more sophisticated models that can better handle complex reasoning tasks over extended temporal horizons. The findings encourage further exploration of memory architectures that leverage contextual information in a question-guided manner, potentially influencing future research in multimodal learning and video understanding.

Authors: Xianqiang Gao, Qizhi Chen, Delin Qu, Haoming Song, Zhigang Wang, Bin Zhao, Dong Wang, Xuelong Li  
Source: arXiv:2605.27318  
URL: [https://arxiv.org/abs/2605.27318v1](https://arxiv.org/abs/2605.27318v1)
