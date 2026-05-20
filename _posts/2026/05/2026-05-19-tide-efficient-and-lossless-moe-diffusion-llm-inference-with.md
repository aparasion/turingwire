---
title: "TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload"
date: 2026-05-19 17:59:08 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20179v1"
arxiv_id: "2605.20179"
authors: ["Zhiben Chen", "Youpeng Zhao", "Yang Sui", "Jun Wang", "Yuzhang Shang"]
slug: tide-efficient-and-lossless-moe-diffusion-llm-inference-with
summary_word_count: 376
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of deploying diffusion large language models (dLLMs) with mixture-of-experts (MoE) architectures on resource-constrained devices. Existing autoregressive (AR) methods face significant I/O overhead and compute bottlenecks, which hinder efficient inference. The authors present TIDE, a preprint work that proposes a solution to optimize inference without requiring additional model training, thus filling a gap in the literature regarding efficient dLLM deployment.

**Method**  
TIDE introduces an interval-based expert refresh strategy that capitalizes on the temporal stability of expert activations during the diffusion process. This approach allows for dynamic expert placement that is aware of I/O constraints. The authors formulate the inference scheduling as a mathematical programming problem, optimizing the refresh intervals to minimize both I/O traffic and CPU computation. The system operates within a single GPU-CPU architecture, ensuring that the proposed method is both resource-efficient and scalable. Notably, TIDE is a lossless optimization, meaning it does not degrade model performance while enhancing throughput.

**Results**  
TIDE demonstrates significant performance improvements over existing baselines. Specifically, it achieves up to 1.4× throughput enhancement on the LLaDA2.0-mini model and 1.5× on the LLaDA2.0-flash model. These results indicate a substantial increase in efficiency for dLLM inference, showcasing TIDE's effectiveness in optimizing resource utilization without compromising the integrity of the model's outputs.

**Limitations**  
The authors acknowledge that TIDE's performance is contingent on the specific architecture of the dLLMs used, as demonstrated with LLaDA2.0 models. They do not address potential limitations related to the generalizability of the method across different model architectures or tasks. Additionally, the reliance on a single GPU-CPU system may restrict applicability in more distributed or heterogeneous computing environments. The paper does not explore the implications of varying expert configurations or the impact of different I/O systems on performance.

**Why it matters**  
The implications of TIDE are significant for the deployment of large-scale dLLMs in real-world applications, particularly in environments with limited computational resources. By providing a lossless optimization strategy, TIDE enables more efficient inference, which can facilitate broader accessibility and usability of advanced language models. This work paves the way for future research into optimizing dLLMs and MoE architectures, potentially influencing the design of next-generation models that prioritize efficiency alongside performance.

Authors: Zhiben Chen, Youpeng Zhao, Yang Sui, Jun Wang, Yuzhang Shang  
Source: arXiv:2605.20179  
URL: https://arxiv.org/abs/2605.20179v1
