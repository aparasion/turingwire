---
title: "Probing Cross-modal Information Hubs in Audio-Visual LLMs"
date: 2026-05-11 16:34:18 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10815v1"
arxiv_id: "2605.10815"
authors: ["Jihoo Jung", "Chaeyoung Jung", "Ji-Hoon Kim", "Joon Son Chung"]
slug: probing-cross-modal-information-hubs-in-audio-visual-llms
summary_word_count: 429
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding the internal mechanisms of audio-visual large language models (AVLLMs), which have not been as extensively studied as their text-only or vision-language counterparts. The authors highlight the need to investigate the cross-modal information flow between audio and visual modalities, particularly how information from one modality is represented in the token embeddings of the other. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors conduct a systematic analysis of multiple recent AVLLMs to probe the cross-modal information hubs. They identify two key findings: (1) integrated audio-visual information is primarily encoded in what they term "sink tokens," and (2) not all sink tokens uniformly store cross-modal information. They introduce the concept of "cross-modal sink tokens," a specific subset of sink tokens that specialize in encoding this information. To mitigate hallucinations in AVLLMs, the authors propose a training-free method that encourages models to rely on the integrated cross-modal information stored within these cross-modal sink tokens. The methodology does not disclose specific architectures, loss functions, or training compute details, focusing instead on the qualitative analysis of token representations.

**Results**  
The paper presents qualitative findings rather than quantitative benchmarks, emphasizing the structural insights gained from the analysis of AVLLMs. The authors demonstrate that cross-modal sink tokens are crucial for effective information encoding, although specific performance metrics against named baselines or benchmarks are not provided. The implications of their findings suggest that enhancing the reliance on cross-modal sink tokens could lead to improved model robustness and reduced hallucination rates in AVLLMs.

**Limitations**  
The authors acknowledge that their analysis is primarily qualitative and does not provide quantitative performance metrics or comparisons against established baselines. Additionally, the proposed hallucination mitigation method is training-free, which may limit its applicability in scenarios where fine-tuning is necessary for optimal performance. The exploration of only a subset of AVLLMs may also restrict the generalizability of their findings across different architectures or tasks.

**Why it matters**  
This work has significant implications for the development of more robust AVLLMs by elucidating the internal dynamics of cross-modal information processing. Understanding how audio and visual modalities interact can inform future model designs and training strategies, potentially leading to advancements in multimodal AI applications such as video understanding, audio-visual scene analysis, and human-computer interaction. The identification of cross-modal sink tokens as key information hubs opens avenues for targeted improvements in model architecture and training methodologies, which could enhance the performance and reliability of AVLLMs in practical applications.

Authors: Jihoo Jung, Chaeyoung Jung, Ji-Hoon Kim, Joon Son Chung  
Source: arXiv:2605.10815  
URL: [https://arxiv.org/abs/2605.10815v1](https://arxiv.org/abs/2605.10815v1)
