---
title: "PROMISE-AD: Progression-aware Multi-horizon Survival Estimation for Alzheimer's Disease Progression and Dynamic Tracking"
date: 2026-04-30 16:01:30 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28055v1"
arxiv_id: "2604.28055"
authors: ["Qing Lyu", "Jeremy Hudson", "Mohammad Kawas", "Yuming Jiang", "Chenyu You", "Christopher T Whitlow"]
slug: promise-ad-progression-aware-multi-horizon-survival-estimati
summary_word_count: 452
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in individualized Alzheimer's disease (AD) progression prediction, specifically the need for models that can handle irregular patient visit data, account for censoring, prevent diagnostic leakage, and provide calibrated risk estimates over multiple time horizons. Existing models often fail to integrate these aspects effectively, limiting their applicability in clinical settings.

**Method**  
The authors introduce PROMISE-AD, a novel survival framework designed for predicting the conversion from cognitively normal (CN) to mild cognitive impairment (MCI) and from MCI to AD dementia. The model processes pre-index visits by converting them into tokens that encapsulate standardized measurements, missingness masks, longitudinal changes, time-normalized slopes, visit timing, and non-diagnostic categorical attributes. A temporal Transformer architecture is employed to fuse global, attention-pooled, and latest-visit representations, which are then used to estimate a progression score and latent discrete-time mixture hazards. The training regimen incorporates a combination of survival likelihood, horizon-specific focal risk loss, progression ranking, hazard smoothness, and mixture-balance regularization. Post-training, isotonic calibration is applied to validate the risk estimates for 1-, 2-, 3-, and 5-year horizons.

**Results**  
In held-out testing across three random seeds, PROMISE-AD achieved an integrated Brier score (IBS) of 0.085 ± 0.012 and a concordance index (C-index) of 0.808 ± 0.015 for CN-to-MCI conversion, outperforming all compared methods in terms of IBS. For MCI-to-AD conversion, it achieved the highest C-index of 0.894 ± 0.018 and near-ceiling performance in 5-year discrimination with an area under the receiver operating characteristic curve (AUROC) of 0.997 ± 0.003 and area under the precision-recall curve (AUPRC) of 0.999 ± 0.001. While some baselines exhibited lower IBS, the overall performance metrics indicate that PROMISE-AD provides robust multi-horizon risk estimates.

**Limitations**  
The authors acknowledge that while PROMISE-AD demonstrates strong performance, it may still be sensitive to the quality and completeness of input data, particularly in the context of missing visits. Additionally, the model's reliance on historical data may limit its applicability in rapidly changing clinical scenarios. The study does not address the potential for overfitting, given the complexity of the model and the relatively small dataset size.

**Why it matters**  
The implications of this work are significant for the field of Alzheimer's research and clinical practice. By providing a framework that integrates multiple aspects of patient data and offers interpretable risk estimates, PROMISE-AD can enhance the precision of AD progression predictions. This could lead to improved patient management strategies and more personalized treatment plans, ultimately contributing to better outcomes in AD care. The model's ability to handle irregular visit data and provide calibrated risks over multiple horizons sets a new standard for future research in survival modeling for neurodegenerative diseases.

Authors: Qing Lyu, Jeremy Hudson, Mohammad Kawas, Yuming Jiang, Chenyu You, Christopher T Whitlow  
Source: arXiv:2604.28055  
URL: https://arxiv.org/abs/2604.28055v1
