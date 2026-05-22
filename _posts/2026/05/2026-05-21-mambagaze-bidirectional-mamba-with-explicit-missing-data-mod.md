---
title: "MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data"
date: 2026-05-21 17:33:41 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22775v1"
arxiv_id: "2605.22775"
authors: ["Amir Mousavi", "Mohammad Sadegh Sirjani", "Erfan Nourbakhsh", "Mimi Xie", "Rocky Slavin", "Leslie Neely"]
slug: mambagaze-bidirectional-mamba-with-explicit-missing-data-mod
summary_word_count: 400
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in real-time cognitive load assessment from eye-tracking data, specifically focusing on the challenges of frequent data missingness due to blinks and tracking failures, as well as the need for efficient modeling of long-range temporal dependencies. Existing methods often struggle with these issues, limiting their applicability in safety-critical applications such as driver vigilance monitoring and automated flight deck assistance.

**Method**  
The authors introduce MambaGaze, a novel framework that incorporates two key innovations: 1) **XMD encoding**, which enhances raw eye-tracking features by integrating observation masks and time-deltas to explicitly model uncertainty in the data, and 2) **bidirectional Mamba-2**, a temporal modeling architecture that captures dependencies with linear computational complexity. The architecture is designed to efficiently process sequences of eye-gaze data while maintaining performance in the presence of missing information. The training process and specific hyperparameters are not disclosed, but the framework is evaluated on two datasets: CLARE and CL-Drive, using a leave-one-subject-out evaluation strategy.

**Results**  
MambaGaze achieves an accuracy of 76.8% on the CLARE dataset and 73.1% on the CL-Drive dataset. These results represent an improvement of 4-12 percentage points over several established baselines, including CNN, Transformer, ResNet, and VGG architectures. Additionally, the framework demonstrates real-time inference capabilities on NVIDIA Jetson platforms, achieving frame rates between 43-68 FPS with power consumption below 7.5W, indicating its suitability for edge deployment in wearable cognitive load monitoring applications.

**Limitations**  
The authors acknowledge that the performance may vary with different datasets and that the leave-one-subject-out evaluation may not fully capture generalization across diverse populations. They also do not address potential limitations related to the scalability of the XMD encoding in more complex environments or the impact of varying gaze tracking quality on model performance. Furthermore, the computational efficiency, while linear, may still pose challenges with larger datasets or more complex temporal dependencies.

**Why it matters**  
The development of MambaGaze has significant implications for the field of cognitive load assessment and human-centered AI. By effectively addressing data missingness and long-range dependencies, this framework enhances the reliability of cognitive load monitoring systems, which are critical for applications in safety-sensitive domains. The ability to perform real-time assessments on edge devices opens avenues for practical implementations in wearable technology, potentially improving user experience and safety in various contexts, from automotive to aviation.

Authors: Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin, Leslie Neely, John Davis, John Quarles  
Source: arXiv:2605.22775  
URL: https://arxiv.org/abs/2605.22775v1
