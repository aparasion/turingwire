---
title: "You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories"
date: 2026-05-20 17:53:20 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21468v1"
arxiv_id: "2605.21468"
authors: ["Zhepei Wei", "Xinyu Zhu", "Wei-Lin Chen", "Chengsong Huang", "Jiaxin Huang", "Yu Meng"]
slug: you-only-need-minimal-rlvr-training-extrapolating-llms-via-r
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a gap in the understanding of parameter trajectories in Reinforcement Learning with Verifiable Rewards (RLVR) for large language models (LLMs). While RLVR has been effective in enhancing reasoning capabilities, the geometric properties of the resulting weight trajectories have not been thoroughly investigated. The authors highlight that existing methods may not efficiently utilize the low-rank nature of these trajectories, which can lead to suboptimal training resource allocation.

**Method**  
The core technical contribution is the RELEX (REinforcement Learning EXtrapolation) method, which leverages the observation that RLVR weight trajectories can be approximated by a rank-1 subspace. RELEX estimates this subspace from a limited observation window and uses linear regression to extrapolate future checkpoints without requiring a learned model. The method operates on three models: Qwen2.5-Math-1.5B, Qwen3-4B-Base, and Qwen3-8B-Base. The authors report that RELEX can achieve performance comparable to or exceeding that of full RLVR training while utilizing only 15% of the training steps. The extrapolation capability is particularly notable, allowing predictions of checkpoints up to 10-20 times beyond the observed training steps. The authors also conduct ablation studies demonstrating that neither increasing the rank of the subspace nor employing non-linear models improves extrapolation performance, indicating the minimalist sufficiency of their approach.

**Results**  
RELEX achieves significant performance improvements over baseline RLVR training. Specifically, it matches or surpasses RLVR performance on both in-domain and out-of-domain benchmarks with only 15% of the training steps. For instance, extrapolating from just 50 training steps to 1000 steps yields continued performance gains. The authors provide quantitative results that demonstrate the effectiveness of RELEX, although specific numerical performance metrics against named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that RELEX's reliance on a rank-1 approximation may limit its applicability in scenarios where higher-dimensional dynamics are critical. They also note that the method's performance is contingent on the quality of the initial observation window, which may not generalize across all tasks or models. Additionally, the study does not explore the implications of varying the observation window size or the potential impact of different optimization algorithms on the extrapolation performance.

**Why it matters**  
The implications of this work are significant for the field of reinforcement learning and LLMs. By demonstrating that a simple, low-complexity method can achieve high performance with minimal training, RELEX opens avenues for more efficient training paradigms in LLMs. This could lead to reduced computational costs and faster iteration cycles in model development. Furthermore, the insights into the low-rank nature of RLVR trajectories may inspire future research into more sophisticated extrapolation techniques and optimization strategies that leverage this geometric understanding.

Authors: Zhepei Wei, Xinyu Zhu, Wei-Lin Chen, Chengsong Huang, Jiaxin Huang, Yu Meng  
Source: arXiv:2605.21468  
URL: [https://arxiv.org/abs/2605.21468v1](https://arxiv.org/abs/2605.21468v1)
