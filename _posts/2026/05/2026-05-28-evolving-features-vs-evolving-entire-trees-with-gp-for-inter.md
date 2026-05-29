---
title: "Evolving Features vs Evolving Entire Trees with GP for Interpretable Survival Analysis"
date: 2026-05-28 15:52:14 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.30119v1"
arxiv_id: "2605.30119"
authors: ["Thalea Schlender", "Peter A. N. Bosman", "Tanja Alderliesten"]
slug: evolving-features-vs-evolving-entire-trees-with-gp-for-inter
summary_word_count: 413
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of traditional survival trees in survival analysis, particularly their tendency to grow large and complex, which compromises interpretability. Existing methods often utilize greedy algorithms for tree construction, potentially missing globally optimal splits and leading to suboptimal predictive performance. The authors aim to enhance both accuracy and interpretability by evolving feature sets and tree structures simultaneously.

**Method**  
The authors propose a genetic programming (GP) framework that evolves feature sets and survival tree structures in a multi-objective optimization context. The method involves two key components: (1) evolving higher-order feature combinations that are inherently interpretable, and (2) jointly optimizing the structure of the survival tree and the non-linear split logic. The evolutionary process allows for the exploration of various tree depths and induction strategies, enabling the generation of shallow survival trees that maintain interpretability while improving predictive accuracy. The specific implementation details regarding the GP algorithm, including selection, crossover, and mutation strategies, are not disclosed in the abstract.

**Results**  
The proposed method demonstrates significant improvements in predictive performance compared to baseline survival tree models across two real-world datasets. The authors report that the full joint evolution approach yields the best results, producing multiple shallow survival trees that balance interpretability and accuracy. While specific numerical results and comparisons to named baselines are not provided in the abstract, the findings suggest a marked enhancement in performance metrics, indicating that the evolutionary feature construction is effective across different tree induction strategies and depths.

**Limitations**  
The authors acknowledge that their approach may still be limited by the computational complexity associated with genetic programming, particularly as the size of the feature set and tree depth increases. Additionally, the reliance on evolutionary algorithms may introduce variability in results due to stochastic processes inherent in GP. The abstract does not discuss potential overfitting issues or the scalability of the method to larger datasets, which are common concerns in survival analysis.

**Why it matters**  
This work has significant implications for the field of survival analysis, particularly in domains such as healthcare, where both predictive accuracy and model interpretability are crucial. By providing a method that evolves both features and tree structures, the authors contribute to the development of more interpretable models that can be effectively utilized in clinical decision-making. The findings may also inspire further research into hybrid approaches that combine evolutionary algorithms with other machine learning techniques to enhance model performance while maintaining transparency.

Authors: Thalea Schlender, Peter A. N. Bosman, Tanja Alderliesten  
Source: arXiv:2605.30119  
URL: [https://arxiv.org/abs/2605.30119v1](https://arxiv.org/abs/2605.30119v1)
