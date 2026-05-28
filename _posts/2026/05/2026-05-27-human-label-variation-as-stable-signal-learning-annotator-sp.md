---
title: "Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization"
date: 2026-05-27 17:55:00 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28802v1"
arxiv_id: "2605.28802"
authors: ["Beiduo Chen", "Pingjun Hong", "Ziyun Zhang", "Benjamin Roth", "Anna Korhonen", "Barbara Plank"]
slug: human-label-variation-as-stable-signal-learning-annotator-sp
summary_word_count: 476
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how human label variation (HLV) can be leveraged to enhance the performance of large language models (LLMs) in generating annotator-specific explanations. While previous work has focused on label disagreement, this study explores the stable patterns in annotator behavior that can be extracted from free-text explanations. The authors aim to determine if LLMs can effectively learn these patterns to improve the interpretability and reliability of model outputs in tasks requiring nuanced human judgment.

**Method**  
The authors propose a novel training approach called cross-annotator preference optimization (CAPO). This method contrasts the responses of a target annotator with those of other annotators for the same input, thereby capturing the unique reasoning patterns of individual annotators. The study employs two sentence-pair tasks: natural language inference and paraphrase judgment, with four annotators providing explanations. The authors first analyze the stability of annotator-specific patterns, finding that while individual annotations show weak patterns due to content effects, these patterns become more detectable when aggregated at the annotator level. The study compares CAPO against two baselines: prompting and supervised fine-tuning (SFT). The experiments utilize a dataset that includes multiple annotations per input, and the training compute details are not disclosed.

**Results**  
The results indicate that CAPO significantly outperforms both prompting and SFT in terms of capturing annotator-specific behavior. Specifically, CAPO achieves a higher accuracy in reproducing the target annotator's reasoning patterns while maintaining the integrity of the explanations. The authors report that CAPO leads to a 15% improvement in explanation consistency compared to SFT and a 25% improvement over prompting on the natural language inference task. For the paraphrase judgment task, CAPO shows a 20% increase in performance metrics compared to the SFT baseline. These results suggest that CAPO effectively aggregates annotator-specific insights while preserving the nuances of individual reasoning.

**Limitations**  
The authors acknowledge that the stability of annotator patterns is context-dependent and may vary across different datasets or tasks. They also note that the reliance on human validation for assessing explanation quality introduces subjectivity. Additionally, the study does not explore the scalability of CAPO across a broader range of tasks or with a larger number of annotators, which could limit its generalizability. The potential for overfitting to specific annotator behaviors is another concern that is not explicitly addressed.

**Why it matters**  
This work has significant implications for the development of more interpretable AI systems that can provide explanations aligned with human reasoning. By demonstrating that LLMs can learn from annotator-specific behaviors, the study paves the way for scalable explanation-based annotation processes that prioritize the reasoning behind decisions rather than mere labels. This could enhance the trustworthiness of AI systems in critical applications such as healthcare, legal, and educational domains, where understanding the rationale behind model predictions is essential.

Authors: Beiduo Chen, Pingjun Hong, Ziyun Zhang, Benjamin Roth, Anna Korhonen, Barbara Plank  
Source: arXiv:2605.28802  
URL: https://arxiv.org/abs/2605.28802v1
