---
title: "Predicting Disagreement with Human Raters in LLM-as-a-Judge Difficulty Assessment without Using Generation-Time Probability Signals"
date: 2026-05-12 17:16:30 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12422v1"
arxiv_id: "2605.12422"
authors: ["Yo Ehara"]
slug: predicting-disagreement-with-human-raters-in-llm-as-a-judge-
summary_word_count: 432
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of predicting disagreement between difficulty ratings assigned by large language models (LLMs) and human raters in the context of educational material generation. While LLMs have been increasingly utilized for automatic content creation, the assignment of difficulty levels remains a labor-intensive task that often leads to inconsistencies between machine-generated and human-assigned ratings. Existing methods typically rely on generation-time probability signals, which are difficult to standardize across different LLMs and can complicate the evaluation of model performance.

**Method**  
The authors propose a novel approach that leverages the ordinal nature of difficulty ratings without relying on generation-time probability signals. Instead, they utilize a separate embedding space, specifically ModernBERT, to represent the difficulty ratings. The core of their method involves assessing the geometric consistency of the rating set to identify candidates for disagreement with human raters. This approach allows for a more robust prediction of which LLM-generated ratings are likely to diverge from human assessments. The training process and specific hyperparameters are not disclosed, but the method is evaluated on datasets derived from English CEFR-based sentence difficulty assessments using two LLMs: GPT-OSS-120B and Qwen3-235B-A22B.

**Results**  
The proposed method demonstrates superior performance in predicting disagreement with human raters compared to traditional probability-based baselines. The authors report an increase in the area under the curve (AUC) metric, although specific numerical values for AUC and comparisons to baseline models are not provided in the abstract. The experiments indicate that the method effectively identifies instances where LLM ratings may not align with human judgment, thereby facilitating targeted re-rating efforts.

**Limitations**  
The authors acknowledge that their method's reliance on ModernBERT as an embedding space may introduce biases inherent to that model. Additionally, the approach may not generalize well to other domains or languages outside of the English CEFR framework. The lack of detailed information regarding the training compute and dataset size limits the reproducibility of the results. Furthermore, the method's effectiveness in real-world applications, where human raters may have varying levels of expertise, is not addressed.

**Why it matters**  
This work has significant implications for the automation of educational content generation, particularly in enhancing the reliability of LLMs as evaluators of difficulty. By improving the prediction of disagreement with human raters, the proposed method can streamline the process of content validation, reducing the workload on human experts and potentially increasing the scalability of LLM applications in educational settings. Future research could build on this framework to explore its applicability across different LLM architectures and educational contexts, as well as to refine the embedding techniques used for difficulty assessment.

Authors: Yo Ehara  
Source: arXiv:2605.12422  
URL: [https://arxiv.org/abs/2605.12422v1](https://arxiv.org/abs/2605.12422v1)
