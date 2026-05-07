---
title: "FlowDIS: Language-Guided Dichotomous Image Segmentation with Flow Matching"
date: 2026-05-06 16:12:07 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05077v1"
arxiv_id: "2605.05077"
authors: ["Andranik Sargsyan", "Shant Navasardyan"]
slug: flowdis-language-guided-dichotomous-image-segmentation-with-
summary_word_count: 380
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Dichotomous Image Segmentation (DIS) methods, which often struggle to maintain fine-grained details and accurately capture the semantic structure of foreground objects. The authors highlight that current approaches do not effectively leverage language guidance for improved segmentation performance. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is FlowDIS, a novel segmentation framework that employs flow matching to learn a time-dependent vector field. This vector field is designed to transport the image distribution to the corresponding mask distribution, with the option to condition the process on a text prompt. The architecture integrates a Position-Aware Instance Pairing (PAIP) training strategy, which enhances the model's controllability and allows for precise, pixel-level segmentation based on textual descriptions. The authors do not disclose specific details regarding the training compute or dataset sizes used in their experiments.

**Results**  
FlowDIS demonstrates significant improvements over state-of-the-art DIS methods. On the DIS-TE test set, it achieves a 5.5% increase in the $F_β^ω$ measure compared to the best prior DIS method, indicating enhanced segmentation accuracy. Additionally, it reports a 43% reduction in Mean Absolute Error (MAE, denoted as $\mathcal{M}$), showcasing its effectiveness in minimizing segmentation errors. These results are particularly notable given the dual evaluation of performance with and without language guidance, underscoring the robustness of the proposed method.

**Limitations**  
The authors acknowledge that while FlowDIS improves segmentation performance, it may still face challenges in extremely complex scenes where multiple overlapping objects exist. They do not discuss potential computational inefficiencies or the scalability of the model to larger datasets. Furthermore, the reliance on text prompts may limit usability in scenarios where such guidance is not available or practical.

**Why it matters**  
The implications of this work are significant for downstream applications in computer vision, particularly in areas requiring high precision in object segmentation, such as autonomous driving and medical imaging. By integrating language guidance into the segmentation process, FlowDIS opens avenues for more intuitive human-computer interaction and enhances the applicability of segmentation models in real-world scenarios. This research could inspire further exploration into the intersection of natural language processing and computer vision, potentially leading to more advanced multimodal models.

Authors: Andranik Sargsyan, Shant Navasardyan  
Source: arXiv cs.CV  
URL: https://arxiv.org/abs/2605.05077v1
