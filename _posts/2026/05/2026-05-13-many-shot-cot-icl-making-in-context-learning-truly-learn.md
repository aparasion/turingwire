---
title: "Many-Shot CoT-ICL: Making In-Context Learning Truly Learn"
date: 2026-05-13 13:30:12 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13511v1"
arxiv_id: "2605.13511"
authors: ["Tsz Ting Chung", "Lemao Liu", "Mo Yu", "Dit-Yan Yeung"]
slug: many-shot-cot-icl-making-in-context-learning-truly-learn
summary_word_count: 429
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of many-shot in-context learning (ICL) in large language models (LLMs), particularly in the context of reasoning tasks. While prior research has primarily focused on non-reasoning tasks, the authors highlight that the scaling behavior of many-shot CoT-ICL is not well understood, especially regarding its effectiveness across different types of LLMs and tasks. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach to many-shot CoT-ICL, emphasizing the importance of demonstration selection and ordering. They introduce Curvilinear Demonstration Selection (CDS), a method that organizes demonstrations to facilitate a coherent conceptual progression. The study examines the performance of various LLMs on reasoning and non-reasoning tasks, analyzing the effects of demonstration quantity and order on model performance. The experiments utilize a range of reasoning-oriented and non-reasoning-oriented LLMs, although specific architectures and training compute details are not disclosed. The authors identify three key phenomena: (i) a setting-dependent scaling effect, (ii) the inadequacy of similarity-based retrieval for reasoning tasks, and (iii) an order-scaling effect that increases performance variance with more demonstrations.

**Results**  
The authors report significant findings, including a maximum performance improvement of 5.42 percentage points on geometry tasks when employing CDS with 64 demonstrations. They demonstrate that while increasing the number of CoT demonstrations can be beneficial for reasoning-oriented LLMs, it can lead to instability in non-reasoning models. The results indicate that the effectiveness of many-shot CoT-ICL is contingent on the nature of the task and the model architecture, with CDS providing a structured approach that enhances reasoning capabilities.

**Limitations**  
The authors acknowledge that their findings are context-dependent and may not generalize across all LLMs or tasks. They note that the reliance on demonstration ordering may introduce additional complexity in practical applications. Furthermore, the study does not explore the impact of varying the quality of demonstrations or the potential for overfitting when using a large number of examples. The lack of peer review also raises questions about the robustness of the findings.

**Why it matters**  
This research has significant implications for the design and application of LLMs in reasoning tasks. By reframing many-shot CoT-ICL as a form of in-context test-time learning rather than mere pattern matching, the authors provide a framework that could enhance the interpretability and effectiveness of LLMs in complex reasoning scenarios. The principles outlined in this work could inform future research on demonstration selection and ordering, potentially leading to more efficient and effective training methodologies for LLMs in various applications.

Authors: Tsz Ting Chung, Lemao Liu, Mo Yu, Dit-Yan Yeung  
Source: arXiv:2605.13511  
URL: [https://arxiv.org/abs/2605.13511v1](https://arxiv.org/abs/2605.13511v1)
