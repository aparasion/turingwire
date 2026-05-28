---
title: "OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning"
date: 2026-05-27 16:19:45 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28691v1"
arxiv_id: "2605.28691"
authors: ["Yunyang Ge", "Xianyi He", "Zezhong Zhang", "Bin Lin", "Bin Zhu", "Xinhua Cheng"]
slug: osp-next-efficient-high-quality-video-generation-with-sparse
summary_word_count: 418
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in video generation using diffusion transformers, particularly the quadratic computational cost associated with full attention mechanisms. The authors propose OSP-Next, a novel model that integrates sparse attention and parallelism to enhance efficiency while maintaining high-quality video generation. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
OSP-Next employs a hybrid architecture that combines full and sparse attention through a mechanism called Skiparse-2D Attention. This approach utilizes fixed-pattern token-wise and group-wise sparse attention along spatial dimensions, optimizing locality and ensuring compatibility with FlashAttention kernels. The authors introduce Sparse Sequence Parallelism (SSP), which partitions subsequences across computational ranks and facilitates the switching of sparse patterns via a single All-to-All communication, achieving a 75% reduction in communication volume compared to Ulysses Sequence Parallelism (SP). Additionally, OSP-Next incorporates HiF8 quantization, allowing for stable joint training with 8-bit quantization and sparse fine-tuning. The model also utilizes Mix-GRPO post-training to enhance the performance of the sparse model.

**Results**  
OSP-Next achieves a VBench total score of 83.73%, outperforming the Wan2.1 baseline. In terms of computational efficiency, the model demonstrates significant speed improvements: up to 1.64× speedup on a single NVIDIA H200 GPU and over 1.52× speedup when utilizing eight GPUs under the 5-second 720P and 5-second 768P settings. Furthermore, OSP-Next-HiF8, with a minimal 0.4% drop in VBench total score, achieves 1.69× and 2.27× speedups on a single Ascend 950PR across the same settings, indicating robust performance across different hardware platforms.

**Limitations**  
The authors acknowledge that while OSP-Next significantly improves efficiency and maintains high-quality video generation, the reliance on sparse attention may limit the model's performance in scenarios requiring full attention. Additionally, the impact of quantization on model fidelity, particularly in more complex video generation tasks, is not fully explored. The paper does not address potential challenges in scaling the model to larger datasets or more complex video generation tasks beyond the benchmarks tested.

**Why it matters**  
The introduction of OSP-Next has significant implications for the field of video generation, particularly in applications requiring real-time processing and resource efficiency. By reducing the computational burden associated with attention mechanisms, this work paves the way for deploying high-quality video generation models in resource-constrained environments. The integration of sparse attention and quantization techniques could inspire further research into optimizing transformer architectures for various multimedia applications, potentially leading to advancements in both efficiency and performance across diverse hardware platforms.

Authors: Yunyang Ge, Xianyi He, Zezhong Zhang, Bin Lin, Bin Zhu, Xinhua Cheng, Li Yuan  
Source: arXiv:2605.28691  
URL: [https://arxiv.org/abs/2605.28691v1](https://arxiv.org/abs/2605.28691v1)
