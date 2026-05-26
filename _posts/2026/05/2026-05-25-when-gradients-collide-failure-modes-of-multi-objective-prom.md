---
title: "When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges"
date: 2026-05-25 17:08:55 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26046v1"
arxiv_id: "2605.26046"
authors: ["Parth Darshan", "Abhishek Divekar"]
slug: when-gradients-collide-failure-modes-of-multi-objective-prom
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing methods for optimizing prompts for large language model (LLM) judges across multiple evaluation criteria. While textual gradient methods have been effective for single-criterion optimization, they yield natural-language critiques rather than numerical gradients, making them incompatible with established multi-task learning conflict-resolution techniques like PCGrad and MGDA. The authors investigate the challenges of applying these methods in a multi-objective context, highlighting a gap in the literature regarding the performance of LLM judges when tasked with simultaneous multi-criteria evaluations.

**Method**  
The authors propose a systematic evaluation of five different decomposition modes for textual gradient optimizers, focusing on how cross-task information is shared among the loss, gradient, and optimizer LLMs. The configurations vary the degree of information sharing, allowing for a comparative analysis of optimization performance. The study employs a series of experiments to quantify the effects of these configurations on gradient specificity and overall optimization success. Key metrics include the gradient specificity score and Spearman's rho for correlation assessment, with a focus on how these metrics change under different optimization strategies.

**Results**  
The findings reveal that in 6 out of 10 configurations tested, the optimization process fails to improve upon the initial prompt, indicating a significant limitation in the effectiveness of the proposed methods. Specifically, the authors report a 59% drop in gradient specificity, from 9.0 to 3.7, when the gradient LLM is tasked with processing multiple criteria simultaneously. Additionally, the naive combination of per-task instructions into a single prompt results in a degradation of Spearman's rho by -5.3%, underscoring the detrimental effects of instruction interference during inference. These results highlight two distinct failure modes: optimization-time gradient dilution and inference-time instruction interference.

**Limitations**  
The authors acknowledge that their study is limited by the specific configurations tested and the reliance on textual gradient methods, which may not generalize to all LLM architectures or tasks. They also note that the observed failure modes may not encompass all potential issues in multi-objective prompt optimization. Furthermore, the study does not explore alternative optimization frameworks or the potential for hybrid approaches that could mitigate the identified limitations.

**Why it matters**  
This work has significant implications for the design and customization of LLM judges in multi-objective settings. By identifying the specific failure modes associated with current optimization techniques, the authors provide a clearer understanding of the constraints faced when attempting to optimize prompts for multiple evaluation criteria. This insight can guide future research towards developing more robust optimization strategies that can effectively handle multi-objective tasks, ultimately enhancing the performance and applicability of LLM judges in diverse domains.

Authors: Parth Darshan, Abhishek Divekar  
Source: arXiv:2605.26046  
URL: https://arxiv.org/abs/2605.26046v1
