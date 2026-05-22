---
title: "Cambrian-P: Pose-Grounded Video Understanding"
date: 2026-05-21 17:59:45 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22819v1"
arxiv_id: "2605.22819"
authors: ["Jihan Yang", "Zifan Zhao", "Xichen Pan", "Shusheng Yang", "Junyi Zhang", "Bingyi Kang"]
slug: cambrian-p-pose-grounded-video-understanding
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in video understanding models, particularly multimodal large language models (MLLMs), which typically treat video frames as isolated 2D images without leveraging the spatial context provided by camera pose. The authors argue that the absence of a shared spatial coordinate frame limits the models' ability to reason about the physical world in a coherent manner. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Cambrian-P, a video MLLM that incorporates camera pose as a supervisory signal. The architecture includes per-frame learnable camera tokens and a pose regression head, which allows the model to capture the spatial relationships between frames. The training process employs a novel sampling scheme to effectively utilize the pose information. The model is trained on a dataset that includes pseudo-annotated poses derived from in-the-wild video, enhancing its performance on various video question answering (QA) tasks. The loss function is not explicitly detailed in the abstract, but the integration of pose information suggests a focus on improving spatial reasoning capabilities.

**Results**  
Cambrian-P demonstrates significant improvements on spatial reasoning benchmarks, achieving gains of 4.5-6.5% on VSI-Bench compared to baseline models. Additionally, it generalizes well across eight other spatial and general video QA benchmarks, indicating robust performance across diverse tasks. The model also sets a new state-of-the-art in streaming pose estimation on the ScanNet dataset, showcasing its effectiveness in both video understanding and pose estimation tasks. The results suggest that incorporating camera pose not only enhances spatial reasoning but also contributes positively to general video QA performance.

**Limitations**  
The authors acknowledge that while the integration of camera pose improves model performance, the reliance on pseudo-annotated poses may introduce noise or inaccuracies that could affect generalizability. They do not discuss the computational cost associated with training the model or the potential limitations of the sampling scheme used for pose integration. Additionally, the performance on specific edge cases or complex scenes is not evaluated, which could be a concern for real-world applications.

**Why it matters**  
This work highlights the importance of camera pose as a fundamental signal in video understanding, suggesting that future models should consider spatial context to improve reasoning about dynamic scenes. The findings could influence the design of subsequent MLLMs and video processing architectures, encouraging the integration of additional spatial information. Furthermore, the success of Cambrian-P in both video QA and pose estimation may lead to advancements in applications such as robotics, augmented reality, and autonomous navigation, where understanding spatial relationships is crucial.

Authors: Jihan Yang, Zifan Zhao, Xichen Pan, Shusheng Yang, Junyi Zhang, Bingyi Kang, Hu Xu, Saining Xie  
Source: arXiv:2605.22819  
URL: https://arxiv.org/abs/2605.22819v1
