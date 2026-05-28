---
title: "Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study"
date: 2026-05-27 16:33:58 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28710v1"
arxiv_id: "2605.28710"
authors: ["Irune Zubiaga", "Aitor Soroa", "Rodrigo Agerri"]
slug: towards-reliable-multilingual-llms-as-a-judge-an-empirical-s
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the use of large language models (LLMs) for automatic text evaluation in multilingual contexts, particularly focusing on low-resource languages. Most existing research has predominantly centered on English, leaving a significant void in methodologies applicable to other languages. The authors highlight the challenges of extending LLM-based evaluators to multilingual settings, especially when in-domain data is scarce. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a systematic empirical study that evaluates various strategies for developing multilingual LLMs-as-a-judge. They focus on three languages: English (high-resource), Spanish (mid-resource), and Basque (low-resource). The study investigates the impact of instruction translation, the choice between monolingual and multilingual supervision, and the influence of model size on performance. The evaluation framework is enhanced by extending two existing meta-evaluation datasets to include Basque and Spanish. The authors explore scenarios with and without in-domain data for fine-tuning, providing insights into the trade-offs between model size and data availability. The training compute details are not disclosed, but the findings emphasize the importance of model fine-tuning strategies in multilingual contexts.

**Results**  
The results indicate that when in-domain data is available, fine-tuned smaller models can achieve performance levels comparable to proprietary models. Specifically, the fine-tuned models demonstrated significant effectiveness in evaluating text in their respective languages. Conversely, in out-of-domain settings, larger models operating in a zero-shot manner outperformed smaller models, suggesting that model size plays a critical role in generalization capabilities. Notably, the authors found that fine-tuning on out-of-domain data could lead to performance degradation, underscoring the complexity of transfer learning in multilingual applications. The paper provides quantitative results, although specific numerical performance metrics against named baselines are not detailed in the summary.

**Limitations**  
The authors acknowledge several limitations, including the reliance on the availability of in-domain data, which may not always be feasible for all languages or applications. They also note that the performance of models can vary significantly based on the choice of training data and the specific language context. An additional limitation not explicitly mentioned is the potential for overfitting when fine-tuning on limited datasets, which could affect the generalizability of the models.

**Why it matters**  
This research has significant implications for the development of reliable multilingual evaluation systems, particularly in low-resource language contexts. By providing empirical evidence on the trade-offs between model size, data availability, and evaluation performance, the findings can guide future work in building efficient multilingual LLMs. The insights gained from this study can inform the design of evaluation pipelines that are both effective and resource-efficient, ultimately contributing to the broader goal of enhancing multilingual natural language processing capabilities.

Authors: Irune Zubiaga, Aitor Soroa, Rodrigo Agerri  
Source: arXiv:2605.28710  
URL: [https://arxiv.org/abs/2605.28710v1](https://arxiv.org/abs/2605.28710v1)
