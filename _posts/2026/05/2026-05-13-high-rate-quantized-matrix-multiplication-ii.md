---
title: "High-Rate Quantized Matrix Multiplication II"
date: 2026-05-13 16:47:25 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13768v1"
arxiv_id: "2605.13768"
authors: ["Or Ordentlich", "Yury Polyanskiy"]
slug: high-rate-quantized-matrix-multiplication-ii
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing quantized matrix multiplication (MatMul) techniques, particularly in the context of weight-only post-training quantization for large language models (LLMs). The authors focus on the scenario where the covariance matrix \( \Sigma_X \) of the columns of the second factor is known, which is a significant gap in the literature as previous works primarily considered calibration-free quantization. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution involves leveraging the classical reverse waterfilling solution from weighted mean squared error (WMSE) source coding to optimize the quantization process. The authors propose a new quantization scheme, referred to as "WaterSIC," which utilizes scalar INT quantizers and allocates quantization rates based on the determinant of \( \Sigma_X \). This approach is characterized as basis-free, meaning it is invariant to random rotations of the input space, a significant improvement over existing methods that are sensitive to such transformations. The authors demonstrate that WaterSIC achieves performance within a multiplicative factor of \( \frac{2\pi e}{12} \) (approximately 0.25 bits per entry) of the information-theoretic distortion limit. They also analyze the performance of the GPTQ algorithm under random rotations, finding it to be within 0.1 bits of WaterSIC for various layer types in the Llama-3-8B model.

**Results**  
The results indicate that WaterSIC significantly outperforms traditional quantization methods, particularly in high-rate scenarios. The authors provide empirical evidence showing that WaterSIC's performance is robust across different configurations, achieving near-optimal quantization efficiency. Specifically, they report that GPTQ, when subjected to random rotations, remains competitive, with performance metrics closely aligning with those of WaterSIC. The paper does not disclose specific numerical results against named baselines but emphasizes the effectiveness of the proposed method in practical applications.

**Limitations**  
The authors acknowledge that their analysis is limited to the high-rate regime and may not generalize to low-rate scenarios where different quantization strategies might be necessary. Additionally, while the basis-free property is a significant advantage, the reliance on the covariance matrix \( \Sigma_X \) may limit applicability in cases where this information is not readily available. The paper does not address potential computational overheads associated with calculating \( \Sigma_X \) or the implications of using scalar quantizers in more complex architectures.

**Why it matters**  
This work has important implications for the field of model compression and quantization, particularly for LLMs where efficient deployment is critical. By improving the quantization process through a theoretically grounded approach, the authors provide a pathway for enhancing the performance of quantized models without sacrificing accuracy. The findings could influence future research on quantization techniques, particularly in scenarios where covariance information is accessible, and may lead to more efficient implementations in production environments.

Authors: Or Ordentlich, Yury Polyanskiy  
Source: arXiv:2605.13768  
URL: [https://arxiv.org/abs/2605.13768v1](https://arxiv.org/abs/2605.13768v1)
