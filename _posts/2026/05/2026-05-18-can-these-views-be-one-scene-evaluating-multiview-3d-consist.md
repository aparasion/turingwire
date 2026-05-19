---
title: "Can These Views Be One Scene? Evaluating Multiview 3D Consistency when 3D Foundation Models Hallucinate"
date: 2026-05-18 17:59:58 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18754v1"
arxiv_id: "2605.18754"
authors: ["Soumava Paul", "Prakhar Kaushik", "Alan Yuille"]
slug: can-these-views-be-one-scene-evaluating-multiview-3d-consist
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in evaluating multiview 3D consistency, particularly in scenarios where neural volume synthesis (NVS) and sparse-view reconstruction are involved. Traditional evaluation methods assume that the input images represent a single static 3D scene, which can lead to misleading high consistency scores in the presence of artifacts, outlier frames, or noise. Existing reference-based metrics require ground truth data, while ground-truth-free metrics like MEt3R rely on learned reconstruction backbones whose limitations are not well understood. This paper investigates the reliability of these metrics and proposes a new benchmark to assess multiview 3D consistency more effectively.

**Method**  
The authors introduce a controlled robustness benchmark for multiview 3D consistency, referred to as \benchmark. They propose a parametric family of metrics that decomposes neural evaluation metrics into three components: backbone, residual, and aggregation. This decomposition allows for the recovery of MEt3R and the development of variants that are up to three times more robust. The study compares neural reconstruction priors against classical geometric verification methods. Additionally, the authors introduce COLMAP-based metrics that leverage matches, registration, dense support, and reconstruction failure as indicators of consistency, providing a failure-aware approach to evaluation.

**Results**  
The proposed COLMAP-based metrics demonstrate significant improvements in correlation with human judgments compared to MEt3R. Specifically, on real NVS outputs and a structured human study, these metrics achieve up to four times higher correlation with human assessments. The robustness of the new metrics is highlighted by their ability to handle scenarios involving unrelated scenes, repeated images, and random noise, outperforming existing methods such as VGGT, MASt3R, DUSt3R, and Fast3R, which can hallucinate dense geometry and cross-view support erroneously.

**Limitations**  
The authors acknowledge that their approach may still be sensitive to certain types of noise and artifacts that were not fully explored in the benchmark. They also note that while the new metrics improve correlation with human judgments, they do not eliminate the need for ground truth in all scenarios. Additionally, the reliance on COLMAP for metric computation may introduce biases based on its own limitations in scene reconstruction.

**Why it matters**  
This work has significant implications for the evaluation of 3D reconstruction methods, particularly in the context of neural networks that generate 3D scenes. By providing a more reliable framework for assessing multiview consistency, the proposed metrics can enhance the development of robust 3D models and improve the interpretability of neural network outputs. This research paves the way for future work in refining evaluation methodologies and understanding the failure modes of neural reconstruction systems, ultimately contributing to advancements in computer vision and graphics.

Authors: Soumava Paul, Prakhar Kaushik, Alan Yuille  
Source: arXiv:2605.18754  
URL: [https://arxiv.org/abs/2605.18754v1](https://arxiv.org/abs/2605.18754v1)
