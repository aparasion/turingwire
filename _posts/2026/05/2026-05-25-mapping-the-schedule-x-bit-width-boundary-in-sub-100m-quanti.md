---
title: "Mapping the Schedule x Bit-Width Boundary in Sub-100M Quantisation-Aware Training"
date: 2026-05-25 15:42:34 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.25966v1"
arxiv_id: "2605.25966"
authors: ["Christian Brandt Thomassen"]
slug: mapping-the-schedule-x-bit-width-boundary-in-sub-100m-quanti
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the relationship between learning-rate schedules and bit-width during quantisation-aware training (QAT) for sub-100M decoder language models. Prior work has not systematically explored how different bit-widths (FP16, INT8, INT6, and INT4) influence the optimal learning-rate schedule, particularly in the context of smaller model sizes. The authors aim to clarify whether distinct learning-rate schedules are necessary for lower precision training, specifically for INT6 and INT4.

**Method**  
The study employs a factorial grid search methodology across multiple dimensions: bit-width (FP16, INT8, INT6), warmdown fraction, learning rate magnitude, model size (15M-100M), and random seed, resulting in a total of 720 runs in Phase 2. The optimal warmdown fraction was consistently found to be 33% across all configurations. A follow-up Phase 5, consisting of 625 runs, further investigates the robustness of the initial findings by varying the optimizer (AdamW), schedule shape (cosine), training duration (up to 9x more iterations), and extending the model size range (5M-350M) while also including an INT4 sweep. The authors utilize a log-linear scaling law to analyze the INT6 penalty and validate predictions on held-out sizes. 

**Results**  
The findings indicate that the initial hypothesis—that INT6 QAT necessitates a different learning-rate schedule—was falsified across all tested bit-widths. For INT4, the results are more definitive: at model sizes of 50M and 100M, the wd33 schedule is optimal, with paired z-scores ranging from 12 to 15 across 10 seeds. Below 50M, no statistically significant preference for a specific schedule was observed, with mean penalties fluctuating within noise levels. The transition between noise-dominated performance and decisive scheduling occurs at the 50M threshold, rather than a clear demarcation at wd10. The weight-to-grid-distance analysis further refutes the rapid grid-snapping hypothesis, showing that INT6 weights are not significantly closer to the INT6 grid than FP16 weights.

**Limitations**  
The authors acknowledge that their findings are limited to sub-100M models and may not generalize to larger architectures. Additionally, the study does not explore the effects of other optimizers beyond AdamW, nor does it consider the impact of different training datasets. The reliance on a specific warmdown fraction (33%) may not be universally applicable across all tasks or model types.

**Why it matters**  
This work has significant implications for practitioners in the field of model quantization and training efficiency. By establishing that a single learning-rate schedule can be effectively applied across different bit-widths for sub-100M models, the study simplifies the training process and reduces the computational burden associated with hyperparameter tuning. The findings also provide a clearer understanding of the performance dynamics at lower model sizes, which is crucial for optimizing resource-constrained deployments in real-world applications.

Authors: Christian Brandt Thomassen  
Source: arXiv:2605.25966  
URL: https://arxiv.org/abs/2605.25966v1
