---
title: "MAdam: Metric-Aware Multi-Objective Adam"
date: 2026-06-02 17:00:15 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03904v1"
arxiv_id: "2606.03904"
authors: ["Fengbei Liu", "Rachit Saluja", "Sunwoo Kwak", "Ruibo Wang", "Ruining Deng", "Heejong Kim"]
slug: madam-metric-aware-multi-objective-adam
summary_word_count: 425
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces MAdam, a novel optimizer that addresses systematic gaps in multi-objective optimization when using Adam."
---

**Problem**  
The paper identifies two critical gaps in the application of Adam for multi-objective optimization (MOO) tasks, which are prevalent in various machine learning domains. The first gap, termed **weighting mismatch**, arises from Adam's second-moment denominator, which conflates the time-varying preference vector with gradient statistics. This results in a marginalization of the preference into a history average, leading to a collapse of distinct Pareto trade-offs into a near-uniform mixture. The second gap, referred to as **geometric mismatch**, occurs because Adam's adaptive metric distorts the Euclidean geometry that MOO solvers typically rely on, creating the illusion of conflicts among aligned objectives. The authors propose MAdam as a solution to these issues, providing a drop-in replacement for Adam without altering existing solvers. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
MADam operates by preconditioning the reconciled direction using the preference-conditioned curvature of the scalarized objective. This approach ensures that the input to Adam's second moment is whitened, effectively collapsing it to the identity matrix. Consequently, the updates are governed by a preference-conditioned metric, which aligns with the intended objectives of MOO solvers. The authors do not disclose specific details regarding the architecture or training compute used in their experiments, focusing instead on the theoretical underpinnings and practical implications of their method.

**Results**  
MADam demonstrates consistent improvements over the standard Adam optimizer across various benchmarks, including multi-task learning, Pareto-front recovery, physics-informed neural networks, and medical imaging tasks. The paper reports that MAdam outperforms Adam for every solver family tested, although specific numerical results and effect sizes are not detailed in the abstract. The authors emphasize that these improvements are significant enough to warrant consideration for practical applications in MOO scenarios.

**Limitations**  
The authors acknowledge that while MAdam addresses the identified mismatches, it may not fully resolve all potential issues inherent in multi-objective optimization. They do not discuss the computational overhead introduced by the preconditioning step, which could impact scalability in large-scale applications. Additionally, the paper does not explore the performance of MAdam in scenarios with highly non-convex objective landscapes, which may present unique challenges.

**Why it matters**  
The introduction of MAdam has significant implications for the field of multi-objective optimization, particularly in enhancing the performance of existing solvers that rely on Adam. By addressing the systematic gaps identified, MAdam provides a more robust framework for optimizing multiple objectives simultaneously, which is crucial in applications ranging from multi-task learning to medical imaging. This work lays the groundwork for future research into more effective optimization strategies in MOO contexts, as published in [arXiv](https://arxiv.org/abs/2606.03904v1).
