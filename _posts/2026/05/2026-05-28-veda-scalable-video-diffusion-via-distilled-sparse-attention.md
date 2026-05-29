---
title: "Veda: Scalable Video Diffusion via Distilled Sparse Attention"
date: 2026-05-28 17:57:07 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.30325v1"
arxiv_id: "2605.30325"
authors: ["Shihao Han", "Hao Yang", "Xinting Hu", "Xiaofeng Mei", "Yi Jiang", "Xiaojuan Qi"]
slug: veda-scalable-video-diffusion-via-distilled-sparse-attention
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of scaling diffusion transformers for high-resolution, long video generation, which is hindered by the quadratic complexity of self-attention mechanisms. Existing sparse attention techniques often suffer from performance degradation at high sparsity levels. The authors highlight a gap in understanding how the alignment of sparse attention masks with the tile-wise geometry of full attention affects generation quality. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Veda, a distilled sparse attention framework that reformulates tile selection as a reconstruction problem derived from full attention. Veda employs a two-pronged approach: it utilizes statistics-aware tile scoring to prioritize tiles based on their contribution to the overall attention mechanism, and head-aware tiling to minimize estimation errors and structural mismatches. This allows for aggressive sparsity without compromising the quality of the generated outputs. Additionally, a hardware-efficient tile-skipping kernel is implemented to translate theoretical sparsity into practical speed improvements. The architecture is designed to optimize the attention computation, significantly reducing the overhead associated with self-attention.

**Results**  
Veda demonstrates substantial performance improvements on large video diffusion models, specifically Waver and Wan2.1. For generating 720P, 10-second videos using the Waver-T2V-12B model, Veda achieves a 5.1× end-to-end speedup and a 10.5× speedup in self-attention computation, effectively reducing the attention overhead from 92% to 50%. The results indicate that the performance gains are more pronounced with increased sequence lengths, suggesting that Veda scales effectively with spatiotemporal resolution. These results are benchmarked against standard diffusion models, showcasing Veda's ability to maintain generation quality while enhancing computational efficiency.

**Limitations**  
The authors acknowledge that while Veda significantly improves speed and maintains generation quality, the approach may still be sensitive to the specific configurations of the tile scoring and tiling mechanisms. They do not address potential limitations related to the generalizability of the method across different model architectures or the impact of varying sparsity levels on specific video content types. Additionally, the reliance on empirical validation raises questions about the robustness of the proposed method in diverse real-world applications.

**Why it matters**  
The implications of this work are significant for the field of video generation and diffusion models. By providing a scalable solution to the computational bottlenecks associated with self-attention, Veda opens avenues for generating higher-resolution videos more efficiently, which is crucial for applications in content creation, virtual reality, and real-time video processing. The insights gained regarding the alignment of sparse attention masks with full attention geometry could inform future research on optimizing attention mechanisms in various deep learning contexts.

Authors: Shihao Han, Hao Yang, Xinting Hu, Xiaofeng Mei, Yi Jiang, Xiaojuan Qi  
Source: arXiv:2605.30325  
URL: [https://arxiv.org/abs/2605.30325v1](https://arxiv.org/abs/2605.30325v1)
