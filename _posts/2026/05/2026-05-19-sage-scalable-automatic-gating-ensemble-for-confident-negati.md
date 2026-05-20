---
title: "SAGE: Scalable Automatic Gating Ensemble for Confident Negative Harvesting in Fraud Detection"
date: 2026-05-19 17:46:31 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20157v1"
arxiv_id: "2605.20157"
authors: ["Sudheer Tubati", "Amit Goyal"]
slug: sage-scalable-automatic-gating-ensemble-for-confident-negati
summary_word_count: 428
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of detecting music streaming fraud, where malicious actors inflate stream counts to manipulate rankings and royalty distributions. Traditional fraud detection methods often misclassify legitimate user behaviors—such as those of super-fans or users engaging in sleep-music sessions—as fraudulent due to their similarity in activity patterns to coordinated fraud. The authors propose SAGE, a preprint work, to tackle the limitations of existing Positive-Unlabeled (PU) learning frameworks, particularly the representation bias that arises from insufficient coverage of rare behavioral cohorts.

**Method**  
SAGE introduces a counterfactual-aware negative harvesting approach that integrates SimHash-based stratified sampling with a modular gating ensemble designed for confident negative identification from unlabeled data. The architecture features pluggable statistical gates, currently instantiated with Mahalanobis distance and k-nearest neighbors (k-NN) density estimators. These gates operate under configurable voting thresholds, allowing for adaptive precision-recall trade-offs. The method employs floor-constrained sampling to ensure comprehensive representation of rare behaviors, thereby enhancing the detection of fraudulent activities while minimizing false positives.

**Results**  
The authors report strong performance metrics on held-out datasets, achieving a precision of 0.92 and recall of 0.89 in customer-level fraud detection, and a precision of 0.90 and recall of 0.87 in artist-level fraud detection. These results significantly outperform traditional baselines, including standard PU learning methods and other heuristic-based approaches, which typically yield precision and recall values below 0.80. The generalizability of SAGE across different fraud detection domains is highlighted, demonstrating its robustness without requiring modifications to the core methodology.

**Limitations**  
The authors acknowledge several limitations, including the reliance on specific statistical gates that may not generalize to all types of fraud detection scenarios. Additionally, the performance of SAGE may be sensitive to the choice of sampling parameters and the underlying distribution of user behaviors. The paper does not extensively explore the computational overhead introduced by the modular gating ensemble, which could impact scalability in real-world applications. Furthermore, the evaluation is conducted on a limited set of datasets, which may not fully capture the diversity of fraud patterns across different streaming platforms.

**Why it matters**  
The implications of SAGE extend beyond music streaming fraud detection, as the methodology can be adapted to various domains where distinguishing between legitimate and fraudulent behaviors is critical. By addressing representation bias in PU learning, SAGE provides a framework that enhances the reliability of fraud detection systems, potentially leading to more accurate identification of fraudulent activities and better protection for legitimate users. This work opens avenues for further research into modular ensemble methods and their application in other areas of anomaly detection.

Authors: Sudheer Tubati, Amit Goyal  
Source: arXiv:2605.20157v1  
URL: https://arxiv.org/abs/2605.20157v1
