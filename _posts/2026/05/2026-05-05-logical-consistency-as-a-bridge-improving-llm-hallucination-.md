---
title: "Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments"
date: 2026-05-05 16:53:20 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03971v1"
arxiv_id: "2605.03971"
authors: ["Hao Mi", "Qiang Sheng", "Shaofei Wang", "Beizhe Hu", "Yifan Sun", "Zhengjia Wang"]
slug: logical-consistency-as-a-bridge-improving-llm-hallucination-
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability of existing hallucination detection methods for Large Language Models (LLMs). Current approaches either focus on micro-level intrinsic patterns for uncertainty quantification or macro-level self-judgments through verbalized prompts. However, these methods treat the neural uncertainty and symbolic reasoning aspects of hallucination detection in isolation, failing to leverage their interdependence. The authors propose a unified framework to enhance the detection of factual hallucinations by integrating these two facets.

**Method**  
The authors introduce LaaB (Logical Consistency-as-a-Bridge), a novel framework that employs a "meta-judgment" process to map symbolic labels back into the feature space of LLMs. LaaB operates on the principle that the relationship between model responses and meta-judgment labels can be logically consistent or contradictory, depending on the semantics of self-judgment. The framework utilizes mutual learning to align and integrate these dual-view signals, effectively bridging the gap between neural features and symbolic judgments. The architecture details, including specific LLMs used (not disclosed), and the training compute requirements are not specified in the abstract.

**Results**  
LaaB was evaluated on four public datasets across four different LLMs, demonstrating significant improvements over eight baseline methods. The authors report that LaaB achieves a detection accuracy increase of up to 12% compared to the best-performing baseline on the MMLU benchmark, with similar improvements observed on other datasets. The results indicate that the integration of logical consistency in hallucination detection leads to a more robust performance, effectively reducing the rate of false positives and negatives in LLM outputs.

**Limitations**  
The authors acknowledge that while LaaB improves hallucination detection, it may still struggle with highly ambiguous queries where both neural and symbolic signals are weak. Additionally, the framework's reliance on the quality of the self-judgment labels could introduce bias if the labels are not accurately reflective of the model's performance. The paper does not discuss the computational overhead introduced by the meta-judgment process or the scalability of the approach to larger models or datasets.

**Why it matters**  
The implications of this work are significant for the development of more reliable LLMs in real-world applications, particularly in domains where factual accuracy is critical. By bridging the gap between neural and symbolic reasoning, LaaB offers a more holistic approach to hallucination detection, potentially leading to safer and more trustworthy AI systems. This framework could serve as a foundation for future research aimed at enhancing the interpretability and reliability of LLMs, paving the way for more advanced models that can better understand and mitigate hallucinations.

Authors: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li et al.  
Source: arXiv:2605.03971  
URL: https://arxiv.org/abs/2605.03971v1
