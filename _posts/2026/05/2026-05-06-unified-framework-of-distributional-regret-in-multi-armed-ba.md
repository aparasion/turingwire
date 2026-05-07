---
title: "Unified Framework of Distributional Regret in Multi-Armed Bandits and Reinforcement Learning"
date: 2026-05-06 16:38:30 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05102v1"
arxiv_id: "2605.05102"
authors: ["Harin Lee", "Min-hwan Oh"]
slug: unified-framework-of-distributional-regret-in-multi-armed-ba
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the understanding of distributional regret in stochastic multi-armed bandits (MAB) and episodic reinforcement learning (RL) by proposing a unified framework. The authors formalize a distributional regret bound that provides probabilistic guarantees uniformly across all confidence levels \( \delta \in (0,1] \). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of a UCBVI-style algorithm that incorporates an exploration bonus defined as \( \min\{c_{1,k}/N, c_{2,k}/\sqrt{N}\} \), where \( N \) is the visit count and \( (c_{1,k}, c_{2,k}) \) are user-defined parameters. The authors derive both gap-independent and gap-dependent distributional regret bounds, which characterize the trade-offs between expected performance, tail risk, and instance-dependent behavior. The bounds are optimal in both minimax and instance-dependent regimes. Specifically, for MABs with \( A \) arms and horizon \( T \), the distributional regret bound is shown to be \( \mathcal{O}(\sqrt{AT}\log(1/\delta)) \), confirming a conjecture by Lattimore & Szepesvári (2020).

**Results**  
The proposed algorithm demonstrates significant improvements in distributional regret bounds compared to existing methods. The derived bound of \( \mathcal{O}(\sqrt{AT}\log(1/\delta)) \) is optimal and provides a clear probabilistic guarantee across all confidence levels. The authors benchmark their results against traditional approaches, although specific baseline algorithms and their performance metrics are not detailed in the abstract. The implications of the results suggest a more nuanced understanding of the trade-offs involved in MAB and RL settings, particularly in terms of risk management and performance optimization.

**Limitations**  
The authors acknowledge that their framework may not account for all possible scenarios in MAB and RL, particularly in non-stochastic environments or those with complex state spaces. Additionally, the reliance on user-specified parameters \( (c_{1,k}, c_{2,k}) \) may introduce variability in performance that is not fully explored. The paper does not address the computational complexity of implementing the proposed algorithm in large-scale applications, which could limit practical applicability.

**Why it matters**  
This work has significant implications for the design of algorithms in MAB and RL, particularly in scenarios where understanding the distribution of regret is crucial for decision-making under uncertainty. By providing a unified framework, the authors pave the way for future research to explore more sophisticated algorithms that can leverage these distributional insights. The results may also influence the development of adaptive strategies that balance exploration and exploitation more effectively, thereby enhancing the robustness of learning systems in real-world applications.

Authors: Harin Lee, Min-hwan Oh  
Source: arXiv:2605.05102  
URL: [https://arxiv.org/abs/2605.05102v1](https://arxiv.org/abs/2605.05102v1)
