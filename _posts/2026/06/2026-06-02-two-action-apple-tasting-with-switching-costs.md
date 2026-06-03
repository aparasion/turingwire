---
title: "Two-Action Apple Tasting with Switching Costs"
date: 2026-06-02 16:28:45 +0000
category: research
subcategory: theory
company: "Apple"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03851v1"
arxiv_id: "2606.03851"
authors: ["Tommaso Cesari", "Roberto Colomboni"]
slug: two-action-apple-tasting-with-switching-costs
summary_word_count: 398
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper establishes new bounds on regret for the two-action apple-tasting problem with switching costs, addressing a significant gap in the literature."
---

**Problem**  
The paper addresses the two-action apple-tasting problem with switching costs, a scenario where a learner must choose between a revealing action (which provides no reward but discloses the hidden value of a blind action) and a blind action (which yields a reward but reveals nothing). The challenge lies in minimizing regret against an oblivious adversary while incurring a cost for switching actions. Prior work established general feedback-graph algorithms with regret guarantees of $\widetilde O(T^{2/3})$, but a lower bound for this specific problem was previously unproven. This work is a preprint and has not undergone peer review.

**Method**  
The authors introduce a novel analysis of the two-action apple-tasting problem, focusing on the minimax expected regret. They derive bounds for the expected regret, showing that it lies between $\frac{1}{2\sqrt{3}}\cdot\sqrt{T}$ and $2\sqrt{3}\cdot\sqrt{T}$. The analysis leverages techniques from online learning theory, particularly in the context of switching costs, to establish these bounds. The authors utilize a combination of adversarial analysis and probabilistic methods to demonstrate that the previously conjectured lower bound does not hold for this specific feedback graph.

**Results**  
The paper presents a significant advancement in understanding the regret bounds for the two-action apple-tasting problem. The established bounds indicate that the minimax expected regret is tightly constrained, with the lower bound being $\frac{1}{2\sqrt{3}}\cdot\sqrt{T}$ and the upper bound being $2\sqrt{3}\cdot\sqrt{T}$. This result contrasts with the previously assumed $\Omega(T^{2/3})$ lower bound, thereby clarifying the landscape of regret bounds for this class of problems. The implications of these findings suggest that the two-action apple-tasting problem does not exhibit the same level of complexity as other unclassified feedback graphs.

**Limitations**  
The authors acknowledge that their results are specific to the two-action apple-tasting problem and may not generalize to other feedback graphs with switching costs. Additionally, the analysis assumes an oblivious adversary, which may not reflect more complex adversarial settings. The paper does not explore the implications of these bounds in practical applications or how they might influence algorithm design in real-world scenarios.

**Why it matters**  
This work contributes to the theoretical understanding of online learning with switching costs, providing clearer boundaries for expected regret in specific scenarios. The results have implications for the design of algorithms in environments where action switching incurs costs, potentially influencing future research in online learning and decision-making under uncertainty. The findings are particularly relevant for researchers exploring the complexities of feedback graphs in online learning, as published in [arXiv](https://arxiv.org/abs/2606.03851v1).
