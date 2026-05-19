---
title: "Pocket Foundation Models: Distilling TFMs into CPU-Ready Gradient-Boosted Trees"
date: 2026-05-18 17:00:20 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18654v1"
arxiv_id: "2605.18654"
authors: ["Aditya Tanna", "Nassim Bouarour", "Mohamed Bouadi", "Vinay kumar Sankarapu", "Pratinav Seth"]
slug: pocket-foundation-models-distilling-tfms-into-cpu-ready-grad
summary_word_count: 468
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the significant latency gap between state-of-the-art tabular foundation models (TFMs) and the real-time requirements of applications such as fraud scoring, which necessitates predictions in under 2 ms. Current TFMs, however, exhibit inference times ranging from 151 to 1,275 ms on GPU. The authors propose a method to distill these TFMs into CPU-ready gradient-boosted trees (GBTs), specifically XGBoost or CatBoost, to meet the stringent latency requirements. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution involves a novel distillation approach that mitigates the issue of label leakage during in-context learning (ICL) teacher scoring. The authors introduce a stratified out-of-fold (OOF) teacher labeling technique to preserve inter-class structure in the soft targets, which is critical for effective distillation. The distillation process is applied to the TabICLv2 model, resulting in a student model that operates efficiently on CPU. The evaluation is conducted across 153 classification datasets sourced from TALENT, OpenML-CC18, TabZilla, and TabArena. The distilled model achieves a macro-mean AUC of 0.882, representing 96.5% of the teacher's AUC, while maintaining an inference time of 1.9 ms on CPU.

**Results**  
The distilled XGBoost model demonstrates a remarkable speedup of 38x to 860x compared to the original TFM across various teacher-student pairs. The authors report a statistically significant advantage over a tuned CatBoost baseline, with a Wilcoxon p-value of 0.0008 and a 51% win rate in head-to-head comparisons. Additional findings indicate that the rank of the teacher model transfers directly to the student model, with performance gains being more pronounced on low-dimensional datasets (fewer than 21 features) where the distilled model outperforms CatBoost by +0.011, compared to a marginal gain of +0.001 on high-dimensional datasets. Furthermore, while multi-teacher averaging benefits MLP students (+0.006, p = 0.003), it contributes negligibly to tree-based students (<0.001). Notably, in high-dimensional tasks where the teacher underperforms relative to CatBoost, the distillation process can degrade performance.

**Limitations**  
The authors acknowledge that the distillation process may not yield improvements in high-dimensional scenarios where the teacher model itself is suboptimal. Additionally, the reliance on specific datasets may limit the generalizability of the findings. The paper does not address potential overfitting issues that could arise from the distillation process or the implications of using stratified OOF labeling in diverse real-world applications.

**Why it matters**  
This work has significant implications for deploying machine learning models in latency-sensitive environments, particularly in fraud detection and other real-time applications. By successfully distilling TFMs into efficient CPU-based models, the authors provide a pathway for leveraging advanced machine learning techniques without compromising on performance or speed. The open-sourcing of the full pipeline as part of the TabTune library further facilitates accessibility and encourages further research in this domain.

Authors: Aditya Tanna, Nassim Bouarour, Mohamed Bouadi, Vinay Kumar Sankarapu, Pratinav Seth  
Source: arXiv:2605.18654  
URL: [https://arxiv.org/abs/2605.18654v1](https://arxiv.org/abs/2605.18654v1)
