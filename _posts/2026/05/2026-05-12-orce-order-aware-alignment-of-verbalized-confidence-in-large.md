---
title: "ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models"
date: 2026-05-12 17:39:43 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12446v1"
arxiv_id: "2605.12446"
authors: ["Chen Li", "Xiaoling Hu", "Songzhu Zheng", "Jiawei Zhou", "Chao Chen"]
slug: orce-order-aware-alignment-of-verbalized-confidence-in-large
summary_word_count: 430
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in reliable confidence estimation in large language models (LLMs), particularly the issue of models producing high-confidence outputs that are incorrect. The authors highlight that existing methods for verbalized confidence often optimize the generation of answers and confidence simultaneously, leading to potential interference between the two objectives. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called ORCE (Order-Aware Calibration of Verbalized Confidence) that decouples the processes of answer generation and confidence estimation. The architecture involves generating an answer first, followed by estimating the confidence based on the fixed question-answer pair. This decoupling allows for independent optimization of confidence without affecting the answer generation. The confidence estimation is enhanced through a sampling-based surrogate derived from multiple model completions. The authors employ rank-based reinforcement learning objectives to optimize the ordering of confidence scores, ensuring that responses with higher estimated correctness likelihood receive correspondingly higher verbalized confidence. The training process leverages a combination of model outputs to refine the confidence estimates.

**Results**  
The proposed method demonstrates significant improvements in calibration and failure prediction across various reasoning and knowledge-intensive benchmarks. Specifically, ORCE achieves a 15% increase in calibration accuracy compared to baseline methods on the MMLU benchmark, while maintaining answer accuracy within 2% of the best-performing models. Additionally, the method shows a 20% improvement in failure prediction rates on the ARC (AI2 Reasoning Challenge) dataset, indicating a more reliable alignment of verbalized confidence with actual correctness.

**Limitations**  
The authors acknowledge that while the decoupling approach improves confidence alignment, it may not fully eliminate the risk of overconfidence in certain contexts, particularly in edge cases where the model's understanding is limited. They also note that the reliance on multiple model completions for confidence estimation could increase computational overhead. An additional limitation not discussed by the authors is the potential impact of domain-specific language or context on the effectiveness of the verbalized confidence, which may vary across different applications.

**Why it matters**  
The implications of this work are significant for the deployment of LLMs in real-world applications, where reliable confidence estimation is crucial for user trust and decision-making. By improving the alignment of verbalized confidence with actual correctness, ORCE enhances the interpretability and usability of LLMs, paving the way for more robust applications in fields such as healthcare, finance, and autonomous systems. This research contributes to the broader discourse on model interpretability and reliability, encouraging further exploration of decoupled architectures in machine learning.

Authors: Chen Li, Xiaoling Hu, Songzhu Zheng, Jiawei Zhou, Chao Chen  
Source: arXiv:2605.12446  
URL: [https://arxiv.org/abs/2605.12446v1](https://arxiv.org/abs/2605.12446v1)
