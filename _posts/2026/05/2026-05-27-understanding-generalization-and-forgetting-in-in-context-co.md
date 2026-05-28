---
title: "Understanding Generalization and Forgetting in In-Context Continual Learning"
date: 2026-05-27 16:31:51 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28705v1"
arxiv_id: "2605.28705"
authors: ["Guangyu Li", "Meng Ding", "Lijie Hu"]
slug: understanding-generalization-and-forgetting-in-in-context-co
summary_word_count: 423
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the literature regarding in-context learning (ICL) in Large Language Models (LLMs), specifically the lack of understanding of how these models handle sequences of heterogeneous tasks during inference. While existing research has primarily focused on ICL in single-task scenarios, real-world applications often involve multiple tasks presented in a single prompt. The authors aim to establish a theoretical framework for in-context continual learning, exploring whether LLMs implicitly perform continual learning when processing such prompts.

**Method**  
The authors propose a theoretical framework that models the behavior of a pretrained Transformer when processing sequential tasks within a single prompt. They focus on linear and masked linear self-attention mechanisms to derive error expressions for model predictions. The framework includes a bias-variance-interference decomposition of prediction error, which allows for a detailed analysis of generalization and forgetting behaviors. The authors analyze how shared attention mechanisms lead to intertask interference, resulting in systematic biases in model predictions. The theoretical contributions include characterizing conditions under which historical in-context information can lead to either positive or negative transfer, thus providing insights into the limitations of attention-based continual inference.

**Results**  
The authors demonstrate that standard attention mechanisms induce intertask interference, which can lead to performance degradation in long prompts. They provide quantitative analyses of the bias-variance trade-offs and the conditions under which historical context can either enhance or hinder model performance. While specific numerical results are not disclosed in the abstract, the theoretical framework suggests that the performance of LLMs is sensitive to the order of tasks presented in prompts, with implications for generalization capabilities across sequential tasks.

**Limitations**  
The authors acknowledge that their theoretical framework is primarily focused on the behavior of attention mechanisms and may not encompass all aspects of LLMs' performance in practical applications. They do not address the empirical validation of their theoretical findings, which could limit the applicability of their conclusions. Additionally, the framework does not consider the potential impact of other architectural components or training paradigms that may influence continual learning in LLMs.

**Why it matters**  
This work has significant implications for the design and application of LLMs in real-world scenarios where tasks are presented sequentially. By elucidating the mechanisms of generalization and forgetting in in-context continual learning, the findings can inform the development of more robust models that mitigate intertask interference. Understanding the limits of attention-based inference can guide future research in improving task adaptability and performance consistency in LLMs, ultimately enhancing their utility in complex, multi-task environments.

Authors: Guangyu Li, Meng Ding, Lijie Hu  
Source: arXiv:2605.28705  
URL: [https://arxiv.org/abs/2605.28705v1](https://arxiv.org/abs/2605.28705v1)
