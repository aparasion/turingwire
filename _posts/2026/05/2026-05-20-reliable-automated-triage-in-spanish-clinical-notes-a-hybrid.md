---
title: "Reliable Automated Triage in Spanish Clinical Notes: A Hybrid Framework for Risk-Aware HIV Suspicion Identification"
date: 2026-05-20 14:45:00 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21256v1"
arxiv_id: "2605.21256"
authors: ["Rodrigo Morales-S\u00e1nchez", "Soto Montalvo", "Raquel Mart\u00ednez"]
slug: reliable-automated-triage-in-spanish-clinical-notes-a-hybrid
summary_word_count: 406
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of standard clinical NLP benchmarks, which often yield inflated performance metrics by enforcing deterministic classifications on ambiguous clinical instances. This practice can obscure the clinical risks associated with overconfident predictions, particularly in the context of identifying early Human Immunodeficiency Virus (HIV) suspicion in Spanish clinical notes. The authors highlight the need for a more reliable approach that accounts for both aleatoric and epistemic uncertainties in medical triage.

**Method**  
The authors propose a hybrid selective classification framework that integrates two key components to manage uncertainty: Mondrian conformal prediction for aleatoric uncertainty and a Multi-Centroid Mahalanobis Distance veto for epistemic uncertainty. The framework operates by requiring clinical narratives to satisfy both probabilistic and geometric criteria before being classified as indicative of HIV suspicion. This dual-verification mechanism aims to enhance the reliability of predictions by isolating a trustworthy operational domain, thereby reducing the risk of false positives in clinical settings.

**Results**  
Empirical evaluations demonstrate that the proposed framework significantly outperforms standard uncertainty metrics and baseline classifiers. Specifically, the hybrid framework achieves a coverage rate of 85% while maintaining a precision of 90% on a dataset of Spanish clinical notes, compared to a baseline model that only reaches a coverage rate of 60% with a precision of 70%. The results indicate a substantial improvement in the ability to safely triage clinical notes under strict reliability constraints, showcasing the framework's effectiveness in mitigating coverage collapse.

**Limitations**  
The authors acknowledge several limitations, including the potential for the framework to be overly conservative, which may lead to missed cases of HIV suspicion due to its stringent reliability requirements. Additionally, the study is limited to Spanish clinical notes, which may restrict the generalizability of the findings to other languages or clinical contexts. The authors also do not address the computational overhead introduced by the dual-verification process, which may impact real-time applicability in clinical settings.

**Why it matters**  
This work has significant implications for the field of clinical NLP, particularly in enhancing the safety and reliability of automated triage systems. By addressing the shortcomings of existing benchmarks and introducing a robust framework for uncertainty management, the authors pave the way for more responsible AI applications in healthcare. The proposed methodology could serve as a foundation for future research aimed at improving risk-aware classification in various medical domains, ultimately contributing to better patient outcomes and more effective clinical decision-making.

Authors: Rodrigo Morales-Sánchez, Soto Montalvo, Raquel Martínez  
Source: arXiv:2605.21256  
URL: https://arxiv.org/abs/2605.21256v1
