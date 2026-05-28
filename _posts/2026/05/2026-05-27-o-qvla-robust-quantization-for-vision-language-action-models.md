---
title: "Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling"
date: 2026-05-27 17:55:01 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28803v1"
arxiv_id: "2605.28803"
authors: ["Xinyu Wang", "Mingze Li", "Sicheng Lyu", "Dongxiu Liu", "Kaicheng Yang", "Ziyu Zhao"]
slug: o-qvla-robust-quantization-for-vision-language-action-models
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of deploying Vision-Language-Action (VLA) models on-device, which is hindered by their large parameter sizes and the computational demands of their diffusion-based action heads. Previous quantization methods have inadequately addressed this issue, either compressing only the language model backbone while leaving the action head at full precision or employing mixed-precision schemes. The authors argue that the prevailing belief that uniformly quantizing the action head is unstable is unfounded. This work presents Omega-QVLA, a novel training-free post-training quantization framework that aims to compress both the language backbone and the action head uniformly to W4A4 precision.

**Method**  
Omega-QVLA introduces a composite quantization approach that integrates SVD-Hadamard rotation and per-step activation scaling. The SVD-Hadamard rotation is employed to equalize per-channel weight energy, effectively managing the distribution of weight magnitudes. This is complemented by a per-step DiT activation scaling mechanism that mitigates dynamic-range drift across the denoising steps of the diffusion process. The framework operates without the need for mixed-precision allocation, achieving uniform quantization across both the language and action components of the VLA model. The authors do not disclose specific training compute requirements, as the method is post-training and does not involve retraining.

**Results**  
On the LIBERO benchmark, Omega-QVLA demonstrates impressive performance, achieving task success rates of 98.0% and 87.8% for the Pi 0.5 and GR00T N1.5 models, respectively. These results not only match but exceed the performance of their FP16 counterparts, which achieved 97.1% and 87.0% task success rates. Additionally, Omega-QVLA reduces the static memory footprint by 71.3%, indicating significant efficiency gains. Real-world manipulation experiments further validate the method, showing that it enables smooth and accurate manipulation tasks where previous quantization methods have struggled.

**Limitations**  
The authors acknowledge that while Omega-QVLA effectively compresses VLA models, the method's performance may vary with different architectures or tasks not covered in their experiments. They do not discuss potential limitations related to the generalizability of the quantization approach across diverse datasets or the impact of quantization on model interpretability. Furthermore, the absence of a retraining phase may limit the adaptability of the quantized models to specific applications or environments.

**Why it matters**  
The implications of Omega-QVLA are significant for the deployment of VLA models in resource-constrained environments, such as mobile devices or edge computing scenarios. By enabling uniform quantization of both the language and action components, this work paves the way for more efficient and accessible AI applications in robotics, interactive systems, and beyond. The reduction in memory footprint and maintenance of high task success rates suggest that future research can build upon this framework to further enhance the performance and efficiency of multimodal models.

Authors: Xinyu Wang, Mingze Li, Sicheng Lyu, Dongxiu Liu, Kaicheng Yang, Ziyu Zhao, Yufei Cui, Xiao-Wen Chang et al.  
Source: arXiv:2605.28803  
URL: [https://arxiv.org/abs/2605.28803v1](https://arxiv.org/abs/2605.28803v1)
