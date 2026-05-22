---
title: "WorldKV: Efficient World Memory with World Retrieval and Compression"
date: 2026-05-21 16:55:04 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22718v1"
arxiv_id: "2605.22718"
authors: ["Jung Yi", "Minjae Kim", "Paul Hyunbin Cho", "Wooseok Jang", "Sangdoo Yun", "Seungryong Kim"]
slug: worldkv-efficient-world-memory-with-world-retrieval-and-comp
summary_word_count: 468
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of maintaining long-term consistency in autoregressive video diffusion models, particularly in the context of real-time, action-conditioned world generation. While existing methods like full KV-cache attention ensure consistency when revisiting viewpoints, they suffer from significant memory and computational overhead, as both the memory footprint and attention cost scale linearly with the rollout length. Conversely, sliding window inference improves throughput but sacrifices long-term consistency. The authors propose WorldKV as a training-free solution to bridge this gap, enabling efficient world memory management without the need for extensive fine-tuning.

**Method**  
WorldKV comprises two main components: World Retrieval and World Compression. 

1. **World Retrieval**: This component manages the storage of evicted KV-cache chunks in GPU/CPU memory. It selectively retrieves scene-relevant chunks based on camera and action correspondence, reintegrating them into the native attention window without the need for re-encoding. This approach allows for the efficient retrieval of previously stored information, enhancing the model's ability to maintain consistency across different viewpoints.

2. **World Compression**: This technique reduces the storage requirements of each chunk by pruning redundant tokens. It employs a key-key similarity measure against an anchor frame, effectively halving the per-chunk storage. This compression enables the model to accommodate twice as much historical data within a fixed memory budget, thereby enhancing the model's capacity to recall relevant information without incurring additional computational costs.

The authors do not disclose specific training compute requirements, as the framework is designed to be training-free.

**Results**  
WorldKV demonstrates competitive performance on the Matrix-Game-2.0 and LingBot-World-Fast benchmarks. It matches or exceeds the fidelity of full-KV memory while achieving approximately 2x the throughput. Additionally, it performs comparably to memory-trained baselines without requiring any fine-tuning, indicating its robustness and efficiency in real-time applications. The results suggest that WorldKV effectively balances the trade-off between memory fidelity and computational efficiency.

**Limitations**  
The authors acknowledge that while WorldKV improves throughput and maintains consistency, it may still be limited by the inherent constraints of the underlying autoregressive model architecture. Additionally, the reliance on camera/action correspondence for retrieval may not generalize well across all scenarios, particularly in highly dynamic environments. The paper does not address potential scalability issues when applied to larger or more complex scenes, nor does it explore the impact of varying action types on retrieval effectiveness.

**Why it matters**  
The development of WorldKV has significant implications for the field of real-time video generation and interactive environments. By providing a method to efficiently manage world memory, it opens avenues for more sophisticated applications in gaming, virtual reality, and simulation, where maintaining a coherent and consistent world is crucial. Furthermore, the training-free nature of WorldKV could facilitate broader adoption in scenarios where computational resources are limited or where rapid deployment is necessary.

Authors: Jung Yi, Minjae Kim, Paul Hyunbin Cho, Wooseok Jang, Sangdoo Yun, Seungryong Kim  
Source: arXiv:2605.22718  
URL: [https://arxiv.org/abs/2605.22718v1](https://arxiv.org/abs/2605.22718v1)
