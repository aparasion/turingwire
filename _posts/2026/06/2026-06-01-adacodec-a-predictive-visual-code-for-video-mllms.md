---
title: "AdaCodec: A Predictive Visual Code for Video MLLMs"
date: 2026-06-01 17:56:35 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02569v1"
arxiv_id: "2606.02569"
authors: ["Haowen Hou", "Zhen Huang", "Zheming Liang", "Qingyi Si", "Chenglin Li", "Shuai Dong"]
slug: adacodec-a-predictive-visual-code-for-video-mllms
summary_word_count: 399
classification_confidence: 0.80
source_truncated: false
layout: post
description: "AdaCodec introduces a predictive visual coding approach for video MLLMs, enhancing efficiency by reducing redundant visual token usage."
---

**Problem**  
This paper addresses the inefficiency in existing video multimodal large language models (video MLLMs) that treat each frame as an independent RGB image, leading to redundancy in visual token representation. The authors highlight that adjacent frames often share significant visual content, which is not optimally utilized in current models. This work is a preprint and has not undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
The core contribution of this work is the introduction of AdaCodec, a predictive visual coding mechanism designed for video MLLMs. AdaCodec operates by sending a full reference frame only when the conditional predictive cost is high, otherwise encoding inter-frame changes as compact P-tokens. This approach allows for a more efficient representation of video data by focusing on motion and prediction residuals rather than redundant visual information. The architecture leverages a token budget strategy, where the model can operate effectively even at reduced token counts, specifically demonstrating performance at $1/7$ of the visual-token budget compared to traditional methods.

**Results**  
AdaCodec was evaluated across eleven benchmarks, demonstrating significant improvements over the Qwen3-VL-8B baseline, which uses a per-frame RGB approach. Notably, with a budget of 32k tokens, AdaCodec outperformed the 224k token baseline on all long-video benchmarks. Additionally, on five general-video benchmarks, AdaCodec not only raised the average score but also reduced the time-to-first-token from 9.26 seconds to 1.62 seconds, showcasing its efficiency in processing video data.

**Limitations**  
The authors acknowledge that while AdaCodec shows substantial improvements, it may still face challenges in scenarios with highly dynamic scenes where prediction accuracy could be compromised. Additionally, the reliance on a predictive model may introduce latency in certain contexts, particularly when the model must frequently switch between full frame and P-token representations. The paper does not address potential limitations related to the scalability of the model or its performance on diverse video datasets outside the tested benchmarks.

**Why it matters**  
The implications of AdaCodec are significant for the development of more efficient video processing systems in multimodal applications. By reducing redundancy in visual token usage, AdaCodec paves the way for faster and more resource-efficient video MLLMs, which can be crucial for real-time applications such as video analysis, content generation, and interactive media. This work contributes to the ongoing discourse on optimizing model architectures for video data, as discussed in related literature on video representation learning and multimodal integration, and is available on [arXiv](https://arxiv.org/abs/2606.02569v1).
