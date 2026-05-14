---
title: "JANUS: Anatomy-Conditioned Gating for Robust CT Triage Under Distribution Shift"
date: 2026-05-13 17:41:05 +0000
category: research
subcategory: other
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13813v1"
arxiv_id: "2605.13813"
authors: ["Lavsen Dahal", "Yubraj Bhandari", "Geoffrey Rubin", "Joseph Y. Lo"]
slug: janus-anatomy-conditioned-gating-for-robust-ct-triage-under-
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in automated CT triage systems that struggle with both accuracy across diverse pathologies and reliability under institutional distribution shifts. Existing models, particularly those based on Vision Transformers, often rely heavily on visual features, neglecting the importance of quantitative imaging biomarkers that are critical for clinical decision-making. The authors propose a solution that integrates anatomical context to enhance model performance in these challenging scenarios.

**Method**  
The core technical contribution is the JANUS architecture, which employs a dual-stream design that integrates visual embeddings with macro-radiomic priors through Anatomically Guided Gating. This approach conditions the visual features on physiological information, allowing the model to leverage quantitative imaging biomarkers effectively. The architecture is trained on the MERLIN dataset, which consists of 5,082 CT scans, and is evaluated on its ability to generalize to an external dataset of 2,000 scans. The authors do not disclose specific training compute details but emphasize the architecture's robustness under distribution shifts.

**Results**  
JANUS achieves a macro-AUROC of 0.88 and an AUPRC of 0.74 on the MERLIN test set, outperforming all reproduced baselines. On the external dataset, it maintains a high AUROC of 0.87. Notably, the model demonstrates significant improvements in performance for findings characterized by size and attenuation metrics. The authors introduce the Physiological Veto Rate (PVR) as a measure of prediction suppression, showing that JANUS reduces high-confidence false positives more effectively than true positives under domain shift conditions. These results indicate a substantial enhancement in both discrimination and reliability compared to existing methods.

**Limitations**  
The authors acknowledge that while JANUS shows improved performance, it may still be limited by the representativeness of the training datasets, which could affect generalizability to other clinical settings. Additionally, the reliance on anatomical priors may introduce biases if the priors are not well-calibrated or if they do not encompass the full range of pathologies encountered in practice. The paper does not discuss the computational efficiency of the model or its deployment feasibility in real-time clinical environments.

**Why it matters**  
The implications of this work are significant for the field of medical imaging and automated diagnostics. By integrating anatomical context into the triage process, JANUS not only enhances diagnostic accuracy but also improves the reliability of predictions in the face of distribution shifts, a common challenge in clinical settings. This approach could pave the way for more robust AI systems in healthcare, ultimately leading to better patient outcomes and more efficient use of medical resources. The public availability of the code and model weights further facilitates downstream research and application in clinical practice.

Authors: Lavsen Dahal, Yubraj Bhandari, Geoffrey Rubin, Joseph Y. Lo  
Source: arXiv:2605.13813  
URL: https://arxiv.org/abs/2605.13813v1
