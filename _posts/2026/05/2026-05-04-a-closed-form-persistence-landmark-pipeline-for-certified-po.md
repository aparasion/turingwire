---
title: "A Closed-Form Persistence-Landmark Pipeline for Certified Point-Cloud and Graph Classification"
date: 2026-05-04 17:15:01 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02836v1"
arxiv_id: "2605.02836"
authors: ["Sushovan Majhi", "Atish Mitra", "\u017diga Virk", "Pramita Bagchi"]
slug: a-closed-form-persistence-landmark-pipeline-for-certified-po
summary_word_count: 425
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the classification of point clouds and graphs using persistent homology, specifically focusing on the lack of a closed-form solution that provides quantitative guarantees without relying on learned weights or calibration datasets. The authors present PLACE (Persistence-Landmark Analytic Classification Engine) as a preprint, indicating that it has not yet undergone peer review.

**Method**  
PLACE employs a closed-form pipeline that utilizes persistent-homology signatures for classification tasks. The architecture is based on embedding point clouds and graphs through a sparse landmark grid, where the embedding sums Mitra-Virk single-point coordinate functions. The method derives three quantitative guarantees: (1) an $O(kR/(Δ\sqrt{m_{\min}}))$ margin bound, which is influenced by class-mean separation $Δ$ and embedding radius $R$, and is matched by a sample-starved minimax lower bound; (2) a closed-form descriptor-selection rule based on the Mahalanobis margin using Ledoit-Wolf-shrunk covariance, which demonstrates a mean Spearman correlation of approximately $ρ \approx +0.54$ across 10 benchmarks on a heterogeneous chemical-graph descriptor pool; (3) a per-prediction certificate that is determined during training, with no additional computational overhead during prediction, available in both non-asymptotic Pinelis and asymptotic Gaussian forms.

**Results**  
Empirical evaluations show that PLACE outperforms existing diagram-based methods on the Orbit5k benchmark and matches the strongest topology-based baseline on the MUTAG and COX2 datasets within statistical noise. The method exhibits descriptor blindness on the NCI1 and NCI109 datasets, indicating limitations in descriptor coverage. The margin bounds exceed the firing threshold $\hatΔ/2$ across all benchmarks at the specified training set sizes, with the multivariate-norm bound scaling as $\sqrt\ell$. The authors report that the per-prediction certificate is constructive but not yet operational at the current training sizes.

**Limitations**  
The authors acknowledge limitations related to descriptor blindness on specific datasets (NCI1/NCI109) and the coverage of descriptor pools in other contexts. They also note that while the per-prediction certificate is theoretically sound, it is not yet practical for deployment at the training sizes used in their experiments. Additionally, the reliance on closed-form solutions may limit flexibility compared to learned models.

**Why it matters**  
The introduction of PLACE has significant implications for the field of graph and point-cloud classification, particularly in scenarios where interpretability and theoretical guarantees are paramount. By providing a closed-form solution with quantifiable performance metrics, this work paves the way for future research that can build upon its framework, potentially leading to more robust and interpretable models in topological data analysis. The findings may also inspire further exploration into the integration of persistent homology with other machine learning paradigms.

Authors: Sushovan Majhi, Atish Mitra, Žiga Virk, Pramita Bagchi  
Source: arXiv:2605.02836  
URL: https://arxiv.org/abs/2605.02836v1
