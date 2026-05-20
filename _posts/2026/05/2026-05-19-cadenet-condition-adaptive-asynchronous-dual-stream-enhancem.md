---
title: "CADENet: Condition-Adaptive Asynchronous Dual-Stream Enhancement Network for Adverse Weather Perception in Autonomous Driving"
date: 2026-05-19 13:30:28 +0000
category: research
subcategory: agents_robotics
company: "Snowflake"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.19837v1"
arxiv_id: "2605.19837"
authors: ["Sherif Khairy", "Catherine M. Elias"]
slug: cadenet-condition-adaptive-asynchronous-dual-stream-enhancem
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of object detection in autonomous vehicles under adverse weather conditions (e.g., rain, fog, sand, and snow), which significantly degrades camera performance. Existing enhancement-then-detect methodologies introduce latency that violates real-time processing requirements critical for safety. Additionally, the authors highlight an evaluation ceiling in current benchmarks: ground truth annotations on degraded images do not account for the potential recovery of objects that annotators could not perceive, leading to misleadingly low performance metrics. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose CADENet, a training-free, three-thread system designed to enhance object detection in adverse weather conditions. The architecture consists of:

1. **Thread S**: Utilizes YOLOv11n for real-time object detection, achieving full frame rate performance (approximately 44 FPS) without added latency.
2. **Thread Q**: Implements Condition-Adaptive Enhancement (CAPE) to improve image quality based on the specific weather condition, followed by entropy-guided Non-Maximum Suppression (EG-NMS) for result fusion, ensuring that Thread S operates without interruption.
3. **Thread E**: Employs CLIP for zero-shot weather classification, allowing the system to adapt to new weather categories through text prompts without requiring additional labeled data or retraining.

The system's design emphasizes asynchronous processing, enabling simultaneous detection and enhancement.

**Results**  
CADENet was evaluated on the DAWN dataset, comprising 1327 images, using YOLOv11m with an Intersection over Union (IoU) threshold of 0.5 and a confidence threshold of 0.25. The reported performance metrics include:

- Recall: 0.0103 (micro) on snow
- F1 Score: 0.0230 on snow
- F1 Score: 0.0038 on rain

The authors argue that these F1 scores represent lower bounds due to the annotation completeness bias inherent in the DAWN-class data. They advocate for recall as a more reliable metric, as it is immune to the annotation gap.

**Limitations**  
The authors acknowledge the limitations of their approach, particularly the low F1 scores, which may not reflect the true performance gains due to the aforementioned annotation bias. They also note that the system's reliance on existing YOLO architectures may limit its adaptability to future advancements in object detection models. Furthermore, the lack of extensive real-world testing under diverse weather conditions is a potential concern.

**Why it matters**  
The implications of CADENet are significant for the field of autonomous driving, particularly in enhancing the robustness of perception systems under challenging environmental conditions. By decoupling enhancement from detection and enabling real-time processing, this work paves the way for more reliable autonomous systems that can operate safely in adverse weather. The zero-shot classification capability also suggests a flexible framework for adapting to new conditions without extensive retraining, which could accelerate deployment in varied operational environments.

Authors: Sherif Khairy, Catherine M. Elias  
Source: arXiv:2605.19837  
URL: https://arxiv.org/abs/2605.19837v1
