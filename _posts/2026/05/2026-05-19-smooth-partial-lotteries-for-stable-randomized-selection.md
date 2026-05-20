---
title: "Smooth Partial Lotteries for Stable Randomized Selection"
date: 2026-05-19 16:22:51 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20069v1"
arxiv_id: "2605.20069"
authors: ["Alexander Goldberg", "Giulia Fanti", "Nihar B. Shah"]
slug: smooth-partial-lotteries-for-stable-randomized-selection
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the instability inherent in existing partial lottery designs used for competitive selection processes, such as scientific funding and hiring. The authors highlight that small perturbations in candidate scores can lead to significant fluctuations in selection probabilities, undermining the objective of lotteries to minimize the impact of marginal score differences. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel mechanism called the Clipped Linear Lottery, which incorporates smoothness as a design principle. This smoothness is formalized through a Lipschitz condition that governs the mapping from review scores to selection probabilities. The Clipped Linear Lottery operates by defining an upper threshold, above which candidates are always accepted, and a lower threshold, below which candidates are always rejected. The selection probabilities for candidates whose scores fall between these thresholds scale linearly with their estimated quality. The authors derive a theoretical guarantee that the worst-case regret of the Clipped Linear Lottery aligns with a lower bound for any smooth selection rule, adjusted by a factor of \( (1 - k/n) \), where \( k/n \) represents the acceptance rate. The paper also contrasts the smoothness of this lottery with other stability metrics, such as Individual Fairness and Differential Privacy, demonstrating that the Clipped Linear Lottery offers a superior smoothness-regret tradeoff.

**Results**  
The authors conducted experiments using real peer review data from ICLR 2025, NeurIPS 2024, and the Swiss National Science Foundation. Their findings reveal that existing lottery designs exhibit significant instability, with minor score perturbations leading to drastic changes in selection outcomes. The Clipped Linear Lottery not only adheres to the theoretical smoothness guarantees but also outperforms alternative mechanisms in terms of the smoothness-utility tradeoff. Specific numerical results indicate that the proposed lottery mechanism achieves a lower regret compared to traditional methods, although exact figures are not disclosed in the summary.

**Limitations**  
The authors acknowledge that their approach may not fully account for all forms of fairness and may require further exploration of the trade-offs between smoothness and other fairness criteria. Additionally, the empirical validation is limited to specific datasets, which may not generalize across all competitive selection contexts. The paper does not address potential computational complexities associated with implementing the Clipped Linear Lottery in large-scale applications.

**Why it matters**  
This work has significant implications for the design of selection mechanisms in various domains, including academia and industry. By introducing a stable lottery design that mitigates the effects of score perturbations, the Clipped Linear Lottery could enhance the fairness and reliability of selection processes. The theoretical foundations and empirical validation provided in this study pave the way for future research on smooth selection mechanisms, potentially influencing policy and practice in competitive evaluations.

Authors: Alexander Goldberg, Giulia Fanti, Nihar B. Shah  
Source: arXiv:2605.20069  
URL: [https://arxiv.org/abs/2605.20069v1](https://arxiv.org/abs/2605.20069v1)
