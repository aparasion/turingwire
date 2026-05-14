---
title: "Provable Quantization with Randomized Hadamard Transform"
date: 2026-05-13 17:38:18 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13810v1"
arxiv_id: "2605.13810"
authors: ["Ying Feng", "Piotr Indyk", "Michael Kapralov", "Dmitry Krachun", "Boris Prokhorov"]
slug: provable-quantization-with-randomized-hadamard-transform
summary_word_count: 424
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the theoretical understanding of vector quantization methods, particularly focusing on the limitations of existing techniques that utilize dense random rotations, which require $Θ(d^2)$ time complexity. The authors propose a novel approach using the randomized Hadamard transform (HD) to achieve efficient quantization with improved theoretical guarantees. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of dithered quantization using a single randomized Hadamard transform. The method involves applying the HD to the input vector, followed by the subtraction of a random scalar offset before quantization. This additional randomness is injected at a negligible computational cost. The authors provide a theoretical framework demonstrating that this approach is unbiased and derive mean squared error (MSE) bounds that asymptotically match those of truly random rotation matrices. Specifically, they show that the dithered version of TurboQuant achieves an MSE of $\bigl(π\sqrt{3}/2 + o(1)\bigr) \cdot 4^{-b}$ at $b$ bits per coordinate, where the $o(1)$ term diminishes uniformly across all unit vectors and dimensions as the number of quantization levels increases.

**Results**  
The proposed method is evaluated against traditional quantization techniques, demonstrating significant improvements in efficiency and theoretical guarantees. The authors report that their dithered quantization method achieves an MSE that asymptotically approaches the performance of optimal quantization methods, specifically matching the MSE bounds of random rotation matrices. While specific numerical results against named baselines are not provided in the abstract, the theoretical guarantees suggest a substantial effect size, particularly in high-dimensional settings where traditional methods become computationally prohibitive.

**Limitations**  
The authors acknowledge that while their method provides strong theoretical guarantees, the practical implementation may still face challenges related to the discrete nature of the Hadamard transform. Additionally, the performance in extremely high-dimensional spaces or under specific data distributions is not fully explored. The paper does not address potential limitations in terms of computational overhead when scaling to very large datasets or the impact of the random scalar offset on quantization performance in real-world applications.

**Why it matters**  
This work has significant implications for various applications in machine learning, including similarity search, federated learning, and KV cache compression. By providing a theoretically sound and computationally efficient quantization method, the authors pave the way for more scalable and effective machine learning systems that can handle high-dimensional data. The results may influence future research on quantization techniques, particularly in contexts where computational efficiency and theoretical guarantees are critical.

Authors: Ying Feng, Piotr Indyk, Michael Kapralov, Dmitry Krachun, Boris Prokhorov  
Source: arXiv:2605.13810  
URL: https://arxiv.org/abs/2605.13810v1
