---
title: "Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach"
date: 2026-05-13 17:52:19 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13830v1"
arxiv_id: "2605.13830"
authors: ["S. Akshay", "Chaitanya Garg", "Ashutosh Gupta", "Kuldeep S. Meel", "Ajinkya Naik"]
slug: quantifying-sensitivity-for-tree-ensembles-a-symbolic-and-co
summary_word_count: 390
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the quantitative assessment of sensitivity in Decision Tree Ensembles (DTEs), a critical aspect for models deployed in safety-critical applications. The authors highlight the lack of efficient methods to determine how small perturbations in input features can lead to misclassifications. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors propose a novel algorithmic technique that quantifies sensitivity by discretizing the input space of DTEs and identifying regions vulnerable to sensitivity. The core of their approach involves encoding the DTE as an Algebraic Decision Diagram (ADD), which allows for the decomposition of the sensitivity problem into smaller, manageable subproblems. This compositional method enhances computational efficiency and scalability. The algorithm operates within certified error and confidence bounds, ensuring reliable outputs. The authors do not disclose specific details regarding the training compute or the datasets used for benchmarking.

**Results**  
The proposed tool, XCount, demonstrates significant performance improvements over existing model counters when applied to various benchmarks characterized by differing numbers of trees and depths. The authors report that XCount achieves speedups of up to 10x compared to baseline methods, effectively handling larger ensembles without a degradation in performance. The results indicate that XCount can efficiently compute sensitivity metrics, making it a viable option for practitioners needing to verify DTEs in real-world applications.

**Limitations**  
The authors acknowledge that their method may be limited by the complexity of the DTEs being analyzed, particularly as the number of trees and depth increases. They also note that while their approach is efficient, it may not be optimal for all configurations of DTEs, especially those with highly intricate structures. Additionally, the paper does not address the potential impact of feature interactions on sensitivity, which could be a significant factor in certain applications.

**Why it matters**  
This work has important implications for the verification of DTEs in safety-critical domains, where understanding model sensitivity is crucial for ensuring reliability and robustness. By providing a scalable and efficient method for quantifying sensitivity, the authors contribute to the broader field of model interpretability and verification. This advancement can facilitate the deployment of DTEs in applications where misclassification due to minor input changes could have severe consequences, such as in healthcare or autonomous systems.

Authors: S. Akshay, Chaitanya Garg, Ashutosh Gupta, Kuldeep S. Meel, Ajinkya Naik  
Source: arXiv:2605.13830  
URL: https://arxiv.org/abs/2605.13830v1
