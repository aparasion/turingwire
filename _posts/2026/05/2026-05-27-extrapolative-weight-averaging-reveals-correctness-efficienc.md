---
title: "Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL"
date: 2026-05-27 17:09:30 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28751v1"
arxiv_id: "2605.28751"
authors: ["Kunhao Zheng", "Pierre Chambon", "Juliette Decugis", "Jonas Gehring", "Taco Cohen", "Benjamin Negrevergne"]
slug: extrapolative-weight-averaging-reveals-correctness-efficienc
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how extrapolative weight averaging can extend the correctness-efficiency frontier in reinforcement learning (RL) for competitive programming. While linear interpolation between fine-tuned checkpoints has been shown to trace Pareto fronts, the potential of extrapolation to yield new checkpoints that enhance inference performance without additional RL training remains unexplored.

**Method**  
The authors propose a novel approach that utilizes nested unit-test coverage to train RL agents. They define two reward structures: low-coverage rewards for passing smaller input tests and high-coverage rewards for progressively larger tests, culminating in a full suite of tests. This training methodology reveals a correctness-efficiency frontier, where higher coverage reduces optimization failures but increases correctness failures. The authors employ both interpolation and extrapolation techniques on checkpoints derived from this training. Extrapolative weight averaging is used to extend the frontier beyond the trained endpoints. The experiments are conducted across three inference settings—pure reasoning, tool use, and agentic coding—utilizing two model scales: 32B and 7B parameters. The training compute details are not disclosed, but the methodology emphasizes the importance of checkpoint selection and averaging strategies.

**Results**  
The study demonstrates that extrapolative weight averaging can significantly enhance performance. Specifically, ensembles created through this method improve the pass rate at 250 samples on the LCB/hard benchmark by 3.3% compared to the best single checkpoint under the same sample budget. The results indicate that moving along the correctness-efficiency frontier alters the set of problems that can be solved, suggesting that extrapolated checkpoints serve as complementary policies. The findings are consistent across the different inference settings and model scales, indicating robustness in the proposed approach.

**Limitations**  
The authors acknowledge that their approach may not generalize to all RL tasks outside competitive programming, as the specific structure of nested unit tests may not be applicable universally. Additionally, the reliance on extrapolation raises questions about the stability and reliability of the extended checkpoints, which are not fully addressed in the paper. The lack of detailed training compute metrics also limits reproducibility and understanding of the resource requirements for achieving the reported results.

**Why it matters**  
This work has significant implications for the field of code-based reinforcement learning, particularly in optimizing the trade-off between correctness and efficiency. By demonstrating that extrapolative weight averaging can effectively navigate and extend the correctness-efficiency frontier, the authors provide a new avenue for improving RL agents in competitive programming contexts. This could lead to advancements in automated coding systems, enhancing their ability to solve complex problems efficiently. Furthermore, the insights gained from this study may inform future research on checkpoint management and policy optimization in broader RL applications.

Authors: Kunhao Zheng, Pierre Chambon, Juliette Decugis, Jonas Gehring, Taco Cohen, Benjamin Negrevergne, Gabriel Synnaeve  
Source: arXiv:2605.28751  
URL: [https://arxiv.org/abs/2605.28751v1](https://arxiv.org/abs/2605.28751v1)
