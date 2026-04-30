---
title: "World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning"
date: 2026-04-29 17:48:01 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.26934v1"
arxiv_id: "2604.26934"
authors: ["Wanyue Zhang", "Wenxiang Wu", "Wang Xu", "Jiaxin Luo", "Helu Zhi", "Yibin Huang"]
slug: world2vlm-distilling-world-model-imagination-into-vlms-for-d
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of vision-language models (VLMs) to perform dynamic spatial reasoning, particularly in scenarios requiring the anticipation of scene evolution under egocentric motion. While previous approaches have attempted to enhance spatial reasoning through synthetic data or by coupling VLMs with world models during inference, they either lack explicit modeling of motion-conditioned state transitions or incur significant computational overhead. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce World2VLM, a training framework that distills spatial imagination from a generative world model into VLMs. The framework operates by synthesizing future views based on an initial observation and a parameterized camera trajectory using a view-consistent world model. This process generates geometrically aligned future views, which provide structured supervision for both forward (action-to-outcome) and inverse (outcome-to-action) spatial reasoning tasks. The VLM is subsequently post-trained using a two-stage recipe on a compact dataset generated through this pipeline. The architecture specifics, loss functions, and training compute details are not disclosed in the abstract.

**Results**  
World2VLM demonstrates consistent performance improvements over the baseline VLM across multiple spatial reasoning benchmarks, including SAT-Real, SAT-Synthesized, VSI-Bench, and MindCube. The paper reports that World2VLM outperforms existing methods that couple world models at test time, achieving superior results without the associated computational costs of inference-time generation. Specific effect sizes or quantitative metrics are not provided in the abstract, but the authors emphasize the effectiveness of their approach in enhancing spatial reasoning capabilities.

**Limitations**  
The authors acknowledge that their approach relies on the quality of the generative world model used for training, which may limit the generalizability of the learned spatial reasoning capabilities. Additionally, the compact dataset generated may not encompass the full diversity of real-world scenarios, potentially affecting the robustness of the VLM in varied contexts. The paper does not discuss the computational requirements for training the world model or the scalability of the approach to larger datasets.

**Why it matters**  
The implications of this work are significant for the development of VLMs capable of dynamic spatial reasoning, which is crucial for applications in robotics, autonomous navigation, and interactive AI systems. By demonstrating that world models can serve as effective training-time teachers, this research opens avenues for more efficient training methodologies that leverage generative models to enhance the internalization of spatial reasoning in VLMs. This could lead to advancements in AI systems that require a nuanced understanding of dynamic environments, ultimately improving their performance in real-world tasks.

Authors: Wanyue Zhang, Wenxiang Wu, Wang Xu, Jiaxin Luo, Helu Zhi, Yibin Huang, Shuo Ren, Zitao Liu et al.  
Source: arXiv:2604.26934  
URL: [https://arxiv.org/abs/2604.26934v1](https://arxiv.org/abs/2604.26934v1)
