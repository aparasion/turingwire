---
title: "Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding"
date: 2026-04-29 15:11:48 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26779v1"
arxiv_id: "2604.26779"
authors: ["Hayate Iso", "Tiyasa Mitra", "Sudipta Mondal", "Rasoul Shafipour", "Venmugil Elango", "Terry Kong"]
slug: accelerating-rl-post-training-rollouts-via-system-integrated
summary_word_count: 428
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in reinforcement learning (RL) post-training rollouts for large language models, particularly the bottleneck caused by autoregressive generation during rollout. The authors highlight that existing methods to enhance throughput often compromise the model's output distribution or require significant changes to the rollout or optimization regimes. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of speculative decoding as a lossless acceleration technique for RL rollouts. Speculative decoding allows for the generation of rollouts without altering the target model's output distribution. The authors implement this technique within the NeMo-RL framework, utilizing a vLLM backend that supports both synchronous and asynchronous pipelines. The implementation leverages various speculation mechanisms, including pretrained MTP heads and smaller external draft models, as well as advanced techniques like Eagle3, which are typically applied post-RL phase. The authors provide a detailed description of the architecture and the integration of speculative decoding into the RL training process, although specific training compute resources are not disclosed.

**Results**  
In experiments conducted on an 8B parameter model under synchronous RL conditions, the authors report a 1.8x improvement in rollout throughput when employing speculative decoding. Furthermore, using a high-fidelity performance simulator, they project that integrating speculative decoding with asynchronous RL could yield up to a 2.5x end-to-end training speedup at a larger scale of 235B parameters. These results are significant when compared to traditional RL training methods, which do not utilize speculative decoding.

**Limitations**  
The authors acknowledge that while speculative decoding improves throughput, it may introduce complexities in the training pipeline that could affect model convergence or stability. They do not discuss potential limitations related to the scalability of the speculative decoding approach across different model architectures or the impact of varying rollout strategies on the final model performance. Additionally, the reliance on specific backend implementations (NeMo-RL and vLLM) may limit the generalizability of the findings to other frameworks.

**Why it matters**  
This work has important implications for the efficiency of RL training in large language models, particularly as model sizes continue to grow. By providing a method to accelerate rollouts without sacrificing output fidelity, the authors pave the way for more efficient training regimes that can handle larger models and more complex tasks. The integration of speculative decoding into RL training could lead to significant reductions in training time, enabling faster iterations and potentially accelerating advancements in AI capabilities.

Authors: Hayate Iso, Tiyasa Mitra, Sudipta Mondal, Rasoul Shafipour, Venmugil Elango, Terry Kong, Yuki Huang, Seonjin Na et al.  
Source: arXiv:2604.26779  
URL: https://arxiv.org/abs/2604.26779v1
