---
title: "mdok-style at SemEval-2026 Task 10: Finetuning LLMs for Conspiracy Detection"
date: 2026-05-04 15:17:44 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02712v1"
arxiv_id: "2605.02712"
authors: ["Dominik Macko"]
slug: mdok-style-at-semeval-2026-task-10-finetuning-llms-for-consp
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of conspiracy belief detection in online discourse, specifically within Reddit comments. The task is part of the SemEval-2026 Task 10, which aims to classify comments as either expressing conspiracy beliefs or not. The authors highlight a significant gap in the literature regarding effective methodologies for this binary text classification task, particularly given the limited availability of labeled training data. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose a system based on the Qwen3-32B model, which is fine-tuned for the task using a combination of data augmentation and self-training techniques. Data augmentation is employed to artificially expand the training dataset, thereby enhancing the model's ability to generalize from a small number of labeled examples. Self-training is utilized to leverage unlabeled data, allowing the model to iteratively refine its predictions and improve performance. The architecture leverages the transformer-based Qwen3-32B, which is known for its large parameter count and capacity for contextual understanding. The training process involves standard optimization techniques, although specific hyperparameters and compute resources are not disclosed.

**Results**  
The mdok-style system achieved a competitive ranking, placing in the 85th percentile (8th out of 52 submissions) in the SemEval-2026 Task 10 competition. The authors report that their approach outperformed several baseline models, although specific metrics such as accuracy, F1-score, or AUC are not detailed in the summary. The results suggest that the methodologies adapted from machine-generated text detection are effective in the context of conspiracy detection, indicating a transferability of techniques across different text classification tasks.

**Limitations**  
The authors acknowledge the inherent limitations of their approach, primarily stemming from the small size of the training dataset, which may affect the robustness and generalizability of the model. Additionally, the reliance on data augmentation and self-training may introduce biases if the augmented data does not accurately represent the underlying distribution of conspiracy-related discourse. The paper does not address potential ethical implications of misclassifying comments or the challenges of defining conspiracy beliefs in a nuanced manner.

**Why it matters**  
This work has significant implications for the development of automated systems aimed at identifying and mitigating the spread of conspiracy theories in online platforms. By demonstrating the effectiveness of fine-tuning large language models for this specific task, the research opens avenues for further exploration into the application of advanced NLP techniques in social media monitoring and content moderation. The findings may also encourage additional research into the intersection of machine-generated text detection and belief classification, potentially leading to more robust models capable of addressing complex social phenomena.

Authors: Dominik Macko  
Source: arXiv:2605.02712  
URL: [https://arxiv.org/abs/2605.02712v1](https://arxiv.org/abs/2605.02712v1)
