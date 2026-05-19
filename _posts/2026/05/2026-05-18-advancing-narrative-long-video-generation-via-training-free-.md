---
title: "Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory"
date: 2026-05-18 17:54:34 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18733v1"
arxiv_id: "2605.18733"
authors: ["Jinzhuo Liu", "Jiangning Zhang", "Wencan Jiang", "Yabiao Wang", "Dingkang Liang", "Zhucun Xue"]
slug: advancing-narrative-long-video-generation-via-training-free-
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of autoregressive video generation, particularly in maintaining long-term consistency and memory integrity across evolving prompts. Existing methods either compress historical frames using predefined strategies or rely on coarse implicit attention signals for keyframe retrieval, which leads to issues such as identity drift, character duplication, and attribute loss. The authors propose a novel approach, IAMFlow, which is a training-free identity-aware memory framework designed to explicitly model and track persistent entity identities, thereby improving the consistency of generated narratives. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
IAMFlow employs a two-pronged approach to enhance identity tracking in video generation. First, a large language model (LLM) extracts entities and their visual attributes from prompts, assigning unique global IDs to facilitate identity-aware memory. Second, a vision-language model (VLM) asynchronously verifies and refines these attributes from rendered frames, allowing for explicit entity tracking rather than relying on implicit similarity-based matching. The framework incorporates a systematic inference acceleration pipeline that includes asynchronous visual verification, adaptive prompt transitions, and model quantization, which collectively enhance computational efficiency. The authors do not disclose specific training compute requirements, as the method is training-free.

**Results**  
IAMFlow demonstrates superior performance on the newly introduced NarraStream-Bench, which consists of 324 multi-prompt scripts across six dimensions. The framework outperforms the strongest baseline by 2.56 points, achieving a notable performance improvement despite being training-free. Additionally, IAMFlow realizes a 1.39× speedup in generation time compared to the most efficient baseline in the 60-second multi-prompt setting. These results indicate a significant advancement in both the quality and efficiency of narrative long video generation.

**Limitations**  
The authors acknowledge that while IAMFlow is effective in maintaining identity consistency, it may still face challenges in scenarios with highly dynamic or complex narratives that require more nuanced understanding of context. Additionally, the reliance on LLMs and VLMs for entity extraction and verification may introduce biases based on the training data of these models. The paper does not address potential scalability issues when applied to larger datasets or more complex video generation tasks.

**Why it matters**  
The introduction of IAMFlow and the NarraStream-Bench benchmark represents a significant step forward in the field of narrative video generation. By addressing the critical issues of identity tracking and long-term consistency, this work lays the groundwork for future research that can build upon these advancements. The training-free nature of IAMFlow also opens avenues for more accessible implementations in real-world applications, potentially influencing areas such as interactive storytelling, gaming, and automated content creation.

Authors: Jinzhuo Liu, Jiangning Zhang, Wencan Jiang, Yabiao Wang, Dingkang Liang, Zhucun Xue, Ran Yi, Yong Liu  
Source: arXiv:2605.18733  
URL: https://arxiv.org/abs/2605.18733v1
