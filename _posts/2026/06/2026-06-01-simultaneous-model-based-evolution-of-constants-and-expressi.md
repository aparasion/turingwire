---
title: "Simultaneous Model-Based Evolution of Constants and Expression Structure in GP-GOMEA for Symbolic Regression"
date: 2026-06-01 13:29:30 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2606.02236v1"
arxiv_id: "2606.02236"
authors: ["Johannes Koch", "Tanja Alderliesten", "Peter A. N. Bosman"]
slug: simultaneous-model-based-evolution-of-constants-and-expressi
summary_word_count: 374
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces a novel method for simultaneous optimization of constants and expression structure in GP-GOMEA for enhanced symbolic regression performance."
---

**Problem**  
This work addresses the limitations of GP-GOMEA, a leading genetic programming (GP) algorithm for symbolic regression, which does not optimize real-valued constants effectively, relying instead on ephemeral random constants. The authors identify a gap in the literature regarding the simultaneous optimization of both expression structure and constants, which is crucial for improving the accuracy of symbolic expressions. This paper is a preprint and has not undergone peer review.

**Method**  
The authors propose a novel approach that integrates the real-valued variant of GOMEA with GP-GOMEA, allowing for the simultaneous optimization of constants and expression structures. This method leverages a model-based evolutionary algorithm framework, where both discrete (expression structure) and continuous (constants) components are optimized concurrently. The authors compare their approach against various strategies for handling constants in GP-GOMEA, including linear scaling, restarts, and post-optimization constant tuning. The training compute details are not explicitly disclosed, but the methodology emphasizes the importance of interaction between discrete and continuous optimization.

**Results**  
The proposed method demonstrates superior performance compared to traditional approaches in symbolic regression tasks. Specifically, it outperforms GP-GOMEA with ephemeral constants and other constant handling techniques across multiple benchmark datasets. The authors report significant improvements in accuracy, although specific numerical results and effect sizes are not detailed in the abstract. The findings suggest that simultaneous constant optimization leads to more compact and accurate symbolic expressions.

**Limitations**  
The authors acknowledge that their approach may require additional computational resources due to the complexity of simultaneous optimization. They also note that while their method shows promise, it may not generalize equally well across all types of symbolic regression problems. Furthermore, the lack of peer review means that the robustness of the results is yet to be validated by the community.

**Why it matters**  
This research has significant implications for the field of symbolic regression, particularly in enhancing the capabilities of genetic programming algorithms. By demonstrating the effectiveness of simultaneous optimization of constants and expression structures, the authors provide a pathway for future work to explore more integrated approaches in evolutionary algorithms. This could lead to advancements in various applications, such as automated machine learning and data-driven modeling, as highlighted in the context of existing literature on mixed discrete-continuous optimization. For further details, see the full paper available on [arXiv](https://arxiv.org/abs/2606.02236v1).
