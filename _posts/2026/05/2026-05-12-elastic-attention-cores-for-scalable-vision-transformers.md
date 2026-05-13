---
title: "Elastic Attention Cores for Scalable Vision Transformers"
date: 2026-05-12 17:59:26 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12491v1"
arxiv_id: "2605.12491"
authors: ["Alan Z. Song", "Yinjie Chen", "Mu Nan", "Rui Zhang", "Jiahang Cao", "Weijian Mai"]
slug: elastic-attention-cores-for-scalable-vision-transformers
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the computational inefficiency of Vision Transformers (ViTs) when scaling to high-resolution images due to their reliance on all-to-all self-attention mechanisms, which exhibit quadratic complexity with respect to the number of image patches. The authors challenge the prevailing assumption that pairwise token interactions are essential for effective visual-semantic representation learning. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce the Visual Elastic Core Attention (VECA) architecture, which employs a core-periphery structured attention mechanism. In VECA, a small set of learned core tokens serves as a communication interface for patch tokens, allowing them to exchange information exclusively through these cores. This design reduces the complexity of attention from quadratic \(O(N^2)\) to linear \(O(N)\) with respect to the number of image patches \(N\), as the patch tokens interact only with a fixed number \(C\) of core embeddings. The core tokens are initialized from scratch and are iteratively updated across layers. The model also incorporates nested training along the core axis, enabling a flexible trade-off between computational cost and accuracy during inference.

**Results**  
VECA demonstrates competitive performance against state-of-the-art vision foundation models across various benchmarks, including classification and dense prediction tasks. The authors report that VECA achieves performance metrics comparable to existing models while significantly reducing computational costs. Specific numerical results are not disclosed in the abstract, but the authors claim that VECA's efficiency allows it to maintain high accuracy levels with reduced resource consumption compared to traditional ViT architectures.

**Limitations**  
The authors acknowledge that while VECA reduces computational complexity, the reliance on a fixed number of core tokens may limit the model's expressiveness in certain scenarios. Additionally, the paper does not explore the impact of varying the number of core tokens \(C\) on performance, which could provide insights into the trade-offs between model capacity and efficiency. The lack of extensive empirical validation across diverse datasets and tasks is also a potential limitation, as the results may not generalize universally.

**Why it matters**  
The introduction of elastic core-periphery attention in VECA presents a novel approach to scaling Vision Transformers, offering a promising alternative to traditional self-attention mechanisms. This work has significant implications for the design of future vision models, particularly in high-resolution applications where computational resources are constrained. By demonstrating that effective visual representations can be learned without direct patch-to-patch interactions, the authors open avenues for further research into efficient attention mechanisms that balance performance and resource utilization.

Authors: Alan Z. Song, Yinjie Chen, Mu Nan, Rui Zhang, Jiahang Cao, Weijian Mai, Muquan Yu, Hossein Adeli et al.  
Source: arXiv:2605.12491  
URL: https://arxiv.org/abs/2605.12491v1
