---
title: "Bootstrap Your Generator: Unpaired Visual Editing with Flow Matching"
date: 2026-06-02 17:07:08 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.03911v1"
arxiv_id: "2606.03911"
authors: ["Yoad Tewel", "Yuval Atzmon", "Gal Chechik", "Lior Wolf"]
slug: bootstrap-your-generator-unpaired-visual-editing-with-flow-m
summary_word_count: 406
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Bootstrap Your Generator (ByG), a novel framework for unpaired visual editing using flow matching, enhancing scalability in generative models."
---

**Problem**  
The paper addresses the challenge of training generative models for image and video editing without the need for large datasets of paired examples, which is particularly problematic in video editing due to the high cost of data collection. The authors highlight that existing methods typically rely on supervised learning with extensive paired datasets, limiting their applicability in scenarios where such data is scarce or unavailable. This work is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The core contribution of this work is the Bootstrap Your Generator (ByG) framework, which enables unpaired training of flow matching editing models. ByG utilizes instruction-following cues extracted from a frozen base model, which provides semantic guidance without requiring external signals. The method incorporates a cycle-consistency mechanism to ensure structural preservation during the editing process. A novel gradient routing technique is introduced, allowing gradients from downstream losses to be propagated over clean predictions to noisy training states, effectively bridging the train-inference gap. The authors do not disclose specific details regarding the architecture or the amount of training compute used, focusing instead on the methodological innovations.

**Results**  
ByG achieves state-of-the-art performance in data-scarce image and video editing tasks, outperforming supervised baselines trained on millions of samples. The authors report significant improvements in editing quality and generalization to unseen domains, although specific quantitative metrics and comparisons to named baselines are not detailed in the abstract. User studies further validate the effectiveness of the proposed method, indicating that it provides a robust training signal that mitigates the need for external reward models.

**Limitations**  
The authors acknowledge that their approach may still be limited by the quality of the frozen base model from which cues are extracted. Additionally, while the method shows promise in unpaired settings, its performance in highly complex editing tasks or with highly diverse datasets remains to be fully evaluated. The paper does not discuss potential computational overhead introduced by the gradient routing mechanism, which could impact scalability in practice.

**Why it matters**  
The implications of this work are significant for the field of generative modeling, particularly in applications where paired data is difficult to obtain. By enabling effective unpaired training, ByG opens new avenues for research in visual editing, potentially leading to more accessible and scalable solutions in both image and video domains. This advancement could inspire further exploration of unpaired learning techniques in other areas of machine learning, as published in [arXiv cs.CV](https://arxiv.org/abs/2606.03911v1).
