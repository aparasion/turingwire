---
title: "From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression"
date: 2026-06-01 17:52:53 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02559v1"
arxiv_id: "2606.02559"
authors: ["Elia Cunegatti", "Marcus Vukojevic", "Erik Nielsen", "Giovanni Iacca"]
slug: from-layers-to-submodules-rethinking-granularity-in-replacem
summary_word_count: 364
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces SubFit, a novel method for post-training compression of LLMs that operates at the submodule level, enhancing efficiency and performance."
---

**Problem**  
This work addresses the limitations of existing replacement-based compression methods for Large Language Models (LLMs), which typically operate at full-layer granularity and require contiguous selection of components. The authors argue that these constraints are overly restrictive, as redundancy in pretrained transformers is not confined to contiguous regions and varies between Attention and FeedForward outputs. This paper is a preprint and has not undergone peer review.

**Method**  
The authors propose SubFit (Submodule-level Fitted residual replacement), a novel approach that allows for non-contiguous selection of submodules within LLMs. SubFit introduces lightweight fitted residual bypasses for each selected submodule, specifically targeting Attention and FeedForward components. The method operates post-training and requires only calibration data, making it efficient for deployment. The architecture leverages ten different LLMs, including five base models and five instruction-tuned variants, and evaluates performance across five sparsity levels ranging from 12.5% to 37.5%. 

**Results**  
SubFit demonstrates superior performance in terms of perplexity-accuracy trade-off compared to four established replacement-based baselines across the evaluated sparsity levels. At 25% sparsity, SubFit retains 84.6% of the dense downstream accuracy while incurring a perplexity degradation of 2.42x. In contrast, the strongest baseline achieves 81.6% accuracy retention with a 4.34x perplexity degradation. Additionally, SubFit provides measurable improvements in inference speed and KV-cache savings, indicating its practical advantages in real-world applications.

**Limitations**  
The authors acknowledge that their method may not generalize across all LLM architectures, as the effectiveness of submodule selection could vary depending on model design. They also do not address potential impacts on model interpretability or the trade-offs between compression and model robustness. Furthermore, the reliance on calibration data may limit applicability in scenarios where such data is scarce.

**Why it matters**  
The introduction of SubFit represents a significant advancement in the field of LLM compression, allowing for more flexible and efficient model optimization strategies. By enabling non-contiguous submodule selection, this method could lead to more effective deployment of LLMs in resource-constrained environments, enhancing their accessibility and usability. The findings have implications for future research in model compression and optimization techniques, as they suggest that a more granular approach can yield better performance outcomes. This work is relevant for ongoing developments in LLM efficiency and is available on [arXiv](https://arxiv.org/abs/2606.02559v1).
