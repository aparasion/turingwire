---
title: "Edge AI for Automotive Vulnerable Road User Safety: Deployable Detection via Knowledge Distillation"
date: 2026-04-29 16:24:45 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26857v1"
arxiv_id: "2604.26857"
authors: ["Akshay Karjol", "Darrin M. Hanna"]
slug: edge-ai-for-automotive-vulnerable-road-user-safety-deployabl
summary_word_count: 408
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of deploying accurate object detection models for Vulnerable Road User (VRU) safety on edge hardware, particularly under the constraints of INT8 quantization. Existing literature shows that while large models like YOLOv8-L achieve high accuracy, they suffer significant performance degradation when quantized for edge deployment. Conversely, smaller models, such as YOLOv8-S, compromise detection performance. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a knowledge distillation (KD) framework that trains a compact YOLOv8-S student model (11.2M parameters) to emulate a larger YOLOv8-L teacher model (43.7M parameters). The KD process involves transferring knowledge from the teacher to the student, focusing on precision calibration rather than raw detection capacity. The training utilizes the BDD100K dataset, which consists of 70,000 images, and employs Post-Training Quantization to convert the model weights to INT8 format. The KD student is designed to maintain robustness against quantization effects, achieving a 3.9x reduction in model size while preserving detection accuracy.

**Results**  
The results demonstrate that the teacher model experiences a catastrophic drop in mean Average Precision (mAP) of -23% when quantized to INT8, while the KD student only incurs a -5.6% mAP reduction. Specifically, the KD student achieves a precision of 0.748 at INT8, compared to 0.653 for a directly trained INT8 model, representing a 14.5% improvement at equivalent recall levels. Additionally, the KD student reduces false positives by 44% compared to the quantized teacher model. Notably, the KD student surpasses the teacher's FP32 precision (0.748 vs. 0.718) despite being 3.9x smaller, indicating a significant enhancement in performance through the KD approach.

**Limitations**  
The authors acknowledge that the study is limited to the BDD100K dataset and may not generalize to other datasets or real-world scenarios. They also do not address potential overfitting in the KD process or the scalability of the approach to other model architectures beyond YOLOv8. Furthermore, the impact of different quantization strategies on model performance is not explored in depth.

**Why it matters**  
This work has significant implications for the deployment of safety-critical AI systems in automotive applications, particularly for VRU detection. By demonstrating that knowledge distillation can effectively enhance the performance of smaller models under quantization constraints, the findings suggest a viable pathway for developing efficient edge AI solutions. This could lead to broader adoption of AI-driven safety systems in vehicles, ultimately improving road safety for vulnerable users.

Authors: Akshay Karjol, Darrin M. Hanna  
Source: arXiv:2604.26857  
URL: [https://arxiv.org/abs/2604.26857v1](https://arxiv.org/abs/2604.26857v1)
