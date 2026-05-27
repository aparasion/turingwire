---
title: "MobileMoE: Scaling On-Device Mixture of Experts"
date: 2026-05-26 17:58:24 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27358v1"
arxiv_id: "2605.27358"
authors: ["Yanbei Chen", "Hanxian Huang", "Ernie Chang", "Jacob Szwejbka", "Digant Desai", "Zechun Liu"]
slug: mobilemoe-scaling-on-device-mixture-of-experts
summary_word_count: 419
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the under-explored application of Mixture-of-Experts (MoE) architectures for on-device language models, particularly at sub-billion parameter scales. While MoE has been successfully utilized in large-scale models exceeding hundreds of billions of parameters, its efficacy and optimization for mobile deployment remain largely unexamined. The authors present MobileMoE, a family of on-device MoE models with active parameters ranging from 0.3 to 0.9 billion, aiming to establish a new Pareto frontier for on-device large language models (LLMs). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the formulation of an on-device MoE scaling law that optimizes the architecture under mobile memory and compute constraints. The authors identify an optimal configuration characterized by moderate sparsity, fine-grained, and shared experts, which balances memory usage and computational efficiency. MobileMoE is trained using a four-stage recipe: pre-training, mid-training, instruction fine-tuning, and quantization-aware training, leveraging open-source datasets. The architecture supports a total of 1.3 to 5.3 billion parameters while maintaining a sub-billion active parameter count, thus enabling efficient inference on mobile devices.

**Results**  
MobileMoE demonstrates competitive performance across 14 benchmarks, matching or exceeding leading on-device dense LLMs while requiring 2-4 times fewer inference FLOPs. Notably, it outperforms the state-of-the-art MoE model OLMoE-1B-7B with up to 60% fewer parameters. In terms of inference speed, MobileMoE-S achieves 1.8-3.8 times faster prefill and 2.2-3.4 times faster decoding compared to the dense baseline MobileLLM-Pro, all while maintaining comparable INT4 weight memory. These results indicate a significant advancement in the efficiency of on-device LLMs.

**Limitations**  
The authors acknowledge that the proposed MobileMoE architecture may still face challenges related to the trade-offs between model size, sparsity, and performance in real-world applications. They do not address potential limitations regarding the generalizability of the model across diverse tasks or the impact of varying mobile hardware capabilities. Additionally, the reliance on open-source datasets for training may limit the model's robustness in specialized domains.

**Why it matters**  
The implications of this work are substantial for the deployment of LLMs on mobile devices, as it provides a framework for achieving high performance with reduced computational overhead. By establishing a new frontier for on-device MoE architectures, MobileMoE paves the way for more efficient language processing applications in resource-constrained environments. This research could influence future work in optimizing model architectures for mobile deployment, potentially leading to broader adoption of advanced AI capabilities in everyday devices.

Authors: Yanbei Chen, Hanxian Huang, Ernie Chang, Jacob Szwejbka, Digant Desai, Zechun Liu, Vikas Chandra, Raghuraman Krishnamoorthi  
Source: arXiv:2605.27358  
URL: [https://arxiv.org/abs/2605.27358v1](https://arxiv.org/abs/2605.27358v1)
