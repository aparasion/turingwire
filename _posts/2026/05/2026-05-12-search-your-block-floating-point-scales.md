---
title: "Search Your Block Floating Point Scales!"
date: 2026-05-12 17:50:08 +0000
category: research
subcategory: efficiency_inference
company: "Scale AI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12464v1"
arxiv_id: "2605.12464"
authors: ["Tanmaey Gupta", "Hayden Prairie", "Xiaoxia Wu", "Reyna Abhyankar", "Qingyang Wu", "Austin Silveria"]
slug: search-your-block-floating-point-scales
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing Block Floating Point (BFP) quantization techniques, which typically utilize a fixed scale based on the maximum magnitude of the block. The authors identify that this fixed scale can lead to suboptimal quantization errors, particularly in the context of generative models. The work aims to fill the gap in the literature regarding adaptive scale selection in BFP formats, leveraging the capabilities of modern GPU accelerators that support microscaling.

**Method**  
The core technical contribution is the introduction of ScaleSearch, a novel strategy for selecting scale factors in BFP quantization. ScaleSearch employs a fine-grained search mechanism that utilizes the mantissa bits in microscaling formats to minimize quantization error based on the distribution of the data. This method can be integrated with existing quantization techniques, such as Post Training Quantization (PTQ) and low-precision attention mechanisms. Additionally, the authors propose ScaleSearchAttention, an optimized attention algorithm based on NVFP4, which incorporates ScaleSearch to maintain performance while reducing quantization error. The training compute requirements are not explicitly disclosed, but the methods are designed to be computationally efficient.

**Results**  
The experimental results demonstrate that ScaleSearch reduces quantization error by 27% for NVFP4 compared to standard BFP methods. Furthermore, it enhances the performance of language model PTQ by up to 15 points on the MATH500 benchmark using the Qwen3-8B model. For the ScaleSearchAttention method, improvements of up to 0.77 points in perplexity (PPL) are observed on the Wikitext-2 dataset for the Llama 3.1 70B model. These results indicate that the proposed methods closely match baseline performance while significantly improving quantization accuracy.

**Limitations**  
The authors acknowledge that their approach may not generalize across all model architectures or datasets, as the effectiveness of ScaleSearch is contingent on the specific distribution of the data being quantized. Additionally, the paper does not address the potential overhead introduced by the fine-grained search process, which could impact inference speed in certain scenarios. The authors also do not explore the implications of their methods on model training dynamics or the potential trade-offs in other quantization settings.

**Why it matters**  
The implications of this work are significant for the deployment of generative models in resource-constrained environments, where efficient inference is critical. By improving quantization accuracy through adaptive scale selection, the proposed methods can enhance the performance of low-precision models, making them more viable for real-world applications. This research opens avenues for further exploration into adaptive quantization techniques and their integration with various model architectures, potentially leading to more efficient AI systems.

Authors: Tanmaey Gupta, Hayden Prairie, Xiaoxia Wu, Reyna Abhyankar, Qingyang Wu, Austin Silveria, Pragaash Ponnusamy, Jue Wang et al.  
Source: arXiv:2605.12464  
URL: [https://arxiv.org/abs/2605.12464v1](https://arxiv.org/abs/2605.12464v1)
