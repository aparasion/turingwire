---
title: "VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition"
date: 2026-05-04 17:11:16 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02834v1"
arxiv_id: "2605.02834"
authors: ["Tanush Yadav", "Mohammadreza Salehi", "Jae Sung Park", "Vivek Ramanujan", "Hannaneh Hajishirzi", "Yejin Choi"]
slug: videonet-a-large-scale-dataset-for-domain-specific-action-re
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in action recognition capabilities within modern vision-language models (VLMs), particularly due to the lack of diverse and challenging datasets. The authors highlight that existing VLMs have not been adequately evaluated on their action recognition performance, which is critical for video understanding. To tackle this issue, they introduce VideoNet, a large-scale dataset specifically designed for domain-specific action recognition, comprising 1,000 distinct actions across 37 domains. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the creation of the VideoNet dataset, which includes nearly 500,000 video question-answer pairs tailored for domain-specific actions. The authors employ a multiple-choice evaluation framework to assess VLMs, contrasting the performance of models like Gemini 3.1 Pro and Qwen3-VL-8B. They also explore binary evaluation settings and few-shot learning scenarios, providing $k \in \{1,2,3\}$ in-context examples to analyze model performance. The Molmo2-4B model is fine-tuned on the VideoNet dataset, demonstrating its effectiveness in surpassing all open-weight 8B models on the benchmark.

**Results**  
In the multiple-choice evaluation, Gemini 3.1 Pro achieves an accuracy of 69.9%, while Qwen3-VL-8B only reaches 45.0%. When the evaluation is relaxed to a binary setting, Qwen improves to 59.2%, still below the random chance baseline of 50%. In few-shot scenarios, Qwen shows a modest improvement of +7.0%, while Gemini declines by -4.8%. In contrast, non-expert human participants demonstrate a +13.6% improvement under similar conditions, indicating that VLMs struggle to leverage in-context examples effectively. The fine-tuned Molmo2-4B model outperforms all open-weight 8B models on the VideoNet benchmark, showcasing the dataset's potential for enhancing action recognition capabilities.

**Limitations**  
The authors acknowledge that the performance of VLMs on VideoNet is suboptimal, particularly in few-shot learning scenarios. They note that while some models excel, others do not, indicating variability in model capabilities. Additionally, the dataset's focus on domain-specific actions may limit its generalizability to broader action recognition tasks. The paper does not address potential biases in the dataset or the implications of model size on performance.

**Why it matters**  
The introduction of VideoNet revitalizes the focus on action recognition in the context of VLMs, providing a robust benchmark for evaluating model performance on domain-specific actions. This work has significant implications for future research in video understanding, as it encourages the development of more sophisticated models that can effectively leverage large-scale, diverse datasets. By highlighting the limitations of current VLMs, the authors pave the way for further exploration into improving action recognition capabilities, which is essential for applications in robotics, surveillance, and human-computer interaction.

Authors: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi et al.  
Source: arXiv:2605.02834  
URL: https://arxiv.org/abs/2605.02834v1
