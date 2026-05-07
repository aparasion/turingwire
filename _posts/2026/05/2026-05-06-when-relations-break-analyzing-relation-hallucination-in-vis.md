---
title: "When Relations Break: Analyzing Relation Hallucination in Vision-Language Model Under Rotation and Noise"
date: 2026-05-06 15:41:24 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.05045v1"
arxiv_id: "2605.05045"
authors: ["Philip Wootaek Shin", "Ajay Narayanan Sridhar", "Sivani Devarapalli", "Rui Zhang", "Jack Sampson", "Vijaykrishnan Narayanan"]
slug: when-relations-break-analyzing-relation-hallucination-in-vis
summary_word_count: 442
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how visual perturbations, specifically rotation and noise, affect the relational reasoning capabilities of vision-language models (VLMs). Despite their strong performance in multimodal tasks, VLMs exhibit a tendency for relation hallucination, where they inaccurately infer relationships between objects. The authors highlight that existing literature has not sufficiently explored the robustness of VLMs under such visual distortions, which is critical for applications requiring precise inter-object reasoning.

**Method**  
The authors conducted a systematic analysis of VLMs under conditions of rotation and noise. They employed a variety of VLM architectures, although specific models are not named in the abstract. The study involved creating datasets with controlled visual perturbations to evaluate the models' performance on relational reasoning tasks. The authors also introduced prompt-based augmentation techniques, including orientation correction and denoising, to mitigate the effects of hallucination. The training compute used for these experiments is not disclosed, but the focus is on evaluating the models' robustness rather than on training new architectures.

**Results**  
The findings indicate that even mild visual distortions lead to significant degradation in relational reasoning performance across multiple VLMs and datasets. While specific quantitative results are not detailed in the abstract, the authors report that the implemented augmentation strategies yield only partial improvements, suggesting that the underlying issue of relation hallucination remains largely unresolved. The results underscore a notable gap between perceptual robustness and the ability to accurately reason about object relationships, indicating that current VLMs are not sufficiently geometry-aware.

**Limitations**  
The authors acknowledge that their proposed augmentation techniques do not fully eliminate relation hallucination, indicating a need for more comprehensive solutions. They do not discuss the potential limitations of their experimental setup, such as the generalizability of their findings across different VLM architectures or the specific datasets used. Additionally, the impact of varying levels of noise and rotation on different types of relational reasoning tasks is not explored in depth, which could provide further insights into the robustness of VLMs.

**Why it matters**  
This work has significant implications for the development of more robust VLMs that can maintain relational understanding in the presence of visual perturbations. The findings suggest that future research should focus on integrating geometry-aware mechanisms into VLM architectures to enhance their resilience against distortions. This could lead to improved performance in real-world applications where visual inputs are often imperfect, such as robotics, autonomous driving, and augmented reality. The study emphasizes the necessity for a deeper understanding of the interplay between perception and reasoning in multimodal models, paving the way for advancements in the field.

Authors: Philip Wootaek Shin, Ajay Narayanan Sridhar, Sivani Devarapalli, Rui Zhang, Jack Sampson, Vijaykrishnan Narayanan  
Source: arXiv:2605.05045  
URL: https://arxiv.org/abs/2605.05045v1
