---
title: "Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models"
date: 2026-04-29 17:59:01 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26951v1"
arxiv_id: "2604.26951"
authors: ["Gongbo Zhang", "Wen Wang", "Ye Tian", "Li Yuan"]
slug: turning-the-tide-cross-architecture-distillation-for-diffusi
summary_word_count: 463
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in cross-architecture knowledge transfer for diffusion large language models (dLLMs). While existing distillation techniques focus on reducing inference steps within a single architecture, they do not facilitate the transfer of knowledge between models with differing architectures, attention mechanisms, and tokenizers. The authors propose TIDE, a novel framework for cross-architecture distillation, which is particularly relevant given the increasing complexity and parameter count of state-of-the-art dLLMs. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The TIDE framework consists of three modular components designed to enhance the distillation process across different architectures:  
1. **TIDAL**: This component modulates the distillation strength dynamically, taking into account both the training progress and the diffusion timestep. It addresses the varying reliability of the teacher model based on noise levels during training.  
2. **CompDemo**: This module enhances the teacher's contextual information by employing complementary mask splitting, which improves prediction accuracy in scenarios with significant input masking.  
3. **Reverse CALM**: This innovative cross-tokenizer objective inverts chunk-level likelihood matching, resulting in bounded gradients and dual-end noise filtering, which aids in stabilizing the training process.  

The authors distill a dense 8B parameter teacher and a 16B mixture of experts (MoE) teacher into a compact 0.6B student model using two heterogeneous pipelines.

**Results**  
The TIDE framework demonstrates significant performance improvements over baseline models. The distilled student model achieves an average increase of 1.53 points across eight benchmarks compared to the baseline. Notably, in code generation tasks, the student model scores 48.78 on the HumanEval benchmark, a substantial improvement over the 32.3 score achieved by the AR baseline. These results indicate that TIDE effectively leverages cross-architecture knowledge transfer to enhance model performance while significantly reducing parameter count.

**Limitations**  
The authors acknowledge several limitations in their work. First, the reliance on specific architectures for the teacher models may limit the generalizability of the approach to other architectures not considered in the study. Additionally, the performance gains are evaluated on a limited set of benchmarks, which may not fully capture the model's capabilities across diverse tasks. The authors also do not address potential issues related to the computational overhead introduced by the modular components of TIDE, which could impact training efficiency.

**Why it matters**  
The TIDE framework has significant implications for the development of more efficient dLLMs, particularly in scenarios where computational resources are constrained. By enabling effective cross-architecture distillation, TIDE allows for the creation of smaller, more efficient models without sacrificing performance, which is crucial for deploying AI systems in resource-limited environments. This work opens avenues for future research into distillation techniques that can further bridge the gap between different model architectures, potentially leading to more versatile and accessible AI applications.

Authors: Gongbo Zhang, Wen Wang, Ye Tian, Li Yuan  
Source: arXiv:2604.26951  
URL: [https://arxiv.org/abs/2604.26951v1](https://arxiv.org/abs/2604.26951v1)
