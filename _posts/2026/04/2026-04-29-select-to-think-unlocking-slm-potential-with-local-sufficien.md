---
title: "Select to Think: Unlocking SLM Potential with Local Sufficiency"
date: 2026-04-29 17:51:39 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26940v1"
arxiv_id: "2604.26940"
authors: ["Wenxuan Ye", "Yangyang Zhang", "Xueli An", "Georg Carle", "Yunpu Ma"]
slug: select-to-think-unlocking-slm-potential-with-local-sufficien
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in reasoning capabilities between small language models (SLMs) and larger language models (LLMs). While SLMs are computationally efficient for deployment, they often lack the reasoning power of LLMs. Current methods typically involve invoking LLMs for token generation at points of reasoning divergence, which incurs latency and cost. Standard distillation techniques are also limited by the SLM's capacity to mimic the complex generative distribution of LLMs. The authors propose a novel approach to leverage the strengths of both model types without the drawbacks of existing methods.

**Method**  
The core technical contribution is the SELECT TO THINK (S2T) framework, which reframes the role of the LLM from generating tokens to selecting from the SLM's top-K predictions. This approach identifies a phenomenon termed "local sufficiency," where the LLM's preferred token is often found within the SLM's top-K candidates, even if it is not the top-1 choice. The authors introduce S2T-LOCAL, which distills the selection logic into the SLM, enabling it to autonomously re-rank its predictions without requiring LLM calls during inference. The architecture involves a 1.5B parameter SLM that utilizes a top-8 candidate selection process, achieving a 95% hit rate in capturing the LLM's preferred token. The training compute details are not disclosed, but the method emphasizes efficiency by improving greedy decoding performance.

**Results**  
S2T-LOCAL demonstrates a significant performance improvement, achieving a 24.1% average enhancement in greedy decoding across various benchmarks compared to baseline methods. This performance is comparable to that of 8-path self-consistency, which typically requires multiple trajectories for inference. The results indicate that the S2T-LOCAL approach effectively harnesses the reasoning capabilities of LLMs while maintaining the efficiency of SLMs, thus bridging the performance gap.

**Limitations**  
The authors acknowledge that while S2T-LOCAL improves SLM performance, it may still be limited by the inherent capacity of the SLM architecture. Additionally, the reliance on the top-K candidates may not generalize across all tasks or domains, potentially limiting the applicability of the method. The paper does not address the scalability of the approach to larger SLMs or the impact of varying K values on performance.

**Why it matters**  
This work has significant implications for the deployment of language models in resource-constrained environments. By enabling SLMs to leverage the reasoning capabilities of LLMs without incurring the associated costs and latencies, the S2T-LOCAL framework could facilitate more efficient applications in real-time systems, such as conversational agents and interactive AI. Furthermore, the concept of local sufficiency may inspire future research into hybrid model architectures that combine the strengths of both SLMs and LLMs, potentially leading to new methodologies in model training and inference.

Authors: Wenxuan Ye, Yangyang Zhang, Xueli An, Georg Carle, Yunpu Ma  
Source: arXiv:2604.26940  
URL: [https://arxiv.org/abs/2604.26940v1](https://arxiv.org/abs/2604.26940v1)
