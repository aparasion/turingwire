---
title: "Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"
date: 2026-05-25 17:42:59 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.26078v1"
arxiv_id: "2605.26078"
authors: ["Zhaoyu Zhu", "Rui Gao", "Shuang Li"]
slug: global-convergence-of-wasserstein-policy-gradient-for-entrop
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding the global convergence properties of Wasserstein Policy Gradient (WPG) in the context of entropy-regularized reinforcement learning (RL). While WPG is promising for continuous-control tasks, its convergence behavior has not been rigorously established, particularly due to the complexities introduced by the Bellman recursion in RL objectives. The authors present a theoretical framework to analyze WPG's convergence, which is particularly relevant as this work is a preprint and has not yet undergone peer review.

**Method**  
The authors develop a global convergence theory for WPG by leveraging the Bellman structure inherent in entropy-regularized RL. They introduce a statewise Kullback-Leibler (KL) representation of the soft Bellman residual concerning a Gibbs policy, which allows them to relate this residual to the global optimality gap through Bellman contraction. The analysis incorporates a Bellman resolvent identity that connects value improvement to relative Fisher information. To ensure convergence, the authors establish a uniform log-Sobolev inequality (LSI) for the evolving Gibbs family, which leads to a distributional Polyak–Łojasiewicz (PL) condition. They also provide regularity and uniform bounds to control discretization errors, resulting in geometric contraction despite the presence of discretization bias.

**Results**  
The theoretical contributions yield a geometric convergence rate for WPG under the entropy-regularized RL framework. The authors demonstrate that WPG achieves global convergence, which is a significant advancement over previous methods that lacked such guarantees. While specific numerical results are not provided in the abstract, the theoretical framework suggests that WPG can outperform traditional policy gradient methods that do not account for the Bellman structure, particularly in continuous action spaces.

**Limitations**  
The authors acknowledge that their analysis relies on the specific structure of the entropy-regularized RL objective and may not generalize to other forms of RL objectives that do not exhibit similar properties. Additionally, the reliance on uniform bounds and regularity conditions may limit the applicability of their results in more complex environments. The paper does not address empirical validation of the theoretical claims, which is a critical aspect for practical deployment.

**Why it matters**  
This work has significant implications for the development of robust policy optimization methods in RL, particularly in continuous control scenarios. By establishing a global convergence theory for WPG, the authors provide a theoretical foundation that could lead to more reliable and efficient algorithms in practice. The insights gained from the Bellman-based analysis may also inspire further research into other RL methods, potentially leading to new algorithms that leverage similar geometric properties for improved convergence guarantees.

Authors: Zhaoyu Zhu, Rui Gao, Shuang Li  
Source: arXiv:2605.26078  
URL: https://arxiv.org/abs/2605.26078v1
