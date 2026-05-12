---
title: "DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices"
date: 2026-05-11 17:58:28 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10933v1"
arxiv_id: "2605.10933"
authors: ["Chenyang Song", "Weilin Zhao", "Xu Han", "Chaojun Xiao", "Yingfa Chen", "Zhiyuan Liu"]
slug: deco-sparse-mixture-of-experts-with-dense-comparable-perform
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional Mixture-of-Experts (MoE) architectures, which, while capable of scaling model capacity, suffer from significant storage and memory-access bottlenecks due to their large parameter footprints. These issues hinder efficient deployment on end-side devices that require high performance, low computational cost, and minimal storage overhead. The work presents DECO, a novel sparse MoE architecture that aims to achieve dense Transformer performance under equivalent parameter budgets and training tokens. This is a preprint and has not yet undergone peer review.

**Method**  
DECO employs a sparse MoE architecture that activates only 20% of its experts during inference, utilizing a differentiable ReLU-based routing mechanism enhanced by learnable expert-wise scaling. This approach allows for adaptive balancing between routed and shared experts, optimizing their contributions. The authors introduce NormSiLU, a new activation function that normalizes inputs before applying the SiLU operator, which stabilizes the routed-expert activation ratio and increases intrinsic sparsity. Additionally, the paper highlights the empirical benefits of using non-gated MLP experts in conjunction with ReLU-based routing, suggesting a simplification of the MoE architecture. The training process and compute requirements are not explicitly detailed, but the architecture is designed to maintain performance parity with dense models.

**Results**  
DECO demonstrates competitive performance against established MoE baselines, achieving dense model performance while activating only a fraction of its experts. The paper reports a 3.00× speedup in inference on real hardware compared to dense models, indicating significant efficiency gains. Specific performance metrics against named baselines and benchmarks are not disclosed in the abstract, but the results suggest that DECO effectively balances the trade-offs between model capacity and computational efficiency.

**Limitations**  
The authors acknowledge that while DECO achieves dense performance with reduced expert activation, the reliance on a specific routing mechanism and the introduction of new activation functions may limit generalizability across different tasks or datasets. Additionally, the empirical advantages of non-gated MLP experts are not thoroughly explored, leaving open questions about their applicability in broader contexts. The paper does not address potential challenges in scaling DECO beyond the tested configurations or its performance in highly diverse or dynamic environments.

**Why it matters**  
The development of DECO has significant implications for the deployment of large-scale models on resource-constrained devices, such as mobile phones and edge computing platforms. By achieving dense performance with a sparse architecture, DECO could facilitate the practical application of advanced AI models in real-world scenarios where computational resources are limited. This work may inspire further research into optimizing MoE architectures and exploring novel activation functions, potentially leading to more efficient and scalable AI solutions.

Authors: Chenyang Song, Weilin Zhao, Xu Han, Chaojun Xiao, Yingfa Chen, Zhiyuan Liu  
Source: arXiv:2605.10933  
URL: [https://arxiv.org/abs/2605.10933v1](https://arxiv.org/abs/2605.10933v1)
