---
title: "HPO: Hysteretic Policy Optimization for Stable and Efficient Training under Sparse-Reward Regime"
date: 2026-05-28 16:38:21 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30201v1"
arxiv_id: "2605.30201"
authors: ["Mohamed Sana", "Nicola Piovesan", "Antonio De Domenico", "Fadhel Ayed", "Haozhe Zhang"]
slug: hpo-hysteretic-policy-optimization-for-stable-and-efficient-
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a specific failure mode in Generalized Reinforcement Policy Optimization (GRPO) when applied to environments with sparse verifiable rewards. The authors identify that early updates in GRPO often contain a disproportionate number of negative advantage responses, which can destabilize training. Additionally, the existing per-response length normalization ties the update magnitude to output length, further complicating the learning process. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose Hysteretic Policy Optimization (HPO), which modifies GRPO by introducing a mechanism to reduce the weight of negative-advantage updates. Instead of using per-response length normalization, HPO employs mean-length normalization, which standardizes updates based on the average length of responses. Furthermore, they introduce Adaptive HPO (A-HPO), which dynamically adjusts the hysteretic weight based on batch-level advantage-sign statistics, eliminating the need for manual tuning of a fixed hysteretic weight. The architecture remains aligned with GRPO, but the training process is enhanced through these modifications.

**Results**  
In experiments conducted on the TeleLogs and Countdown benchmarks, A-HPO demonstrates significant improvements in reward per update compared to GRPO. Specifically, on the TeleLogs dataset, A-HPO achieves a final reward of 0.84, outperforming the following baselines: SAPO by 5%, GSPO by 11%, and GRPO by 15%. In the Countdown experiments, A-HPO shows the most substantial gains in initial and challenging configurations across models ranging from 1.5B to 7B parameters. Ablation studies confirm that the performance improvements of A-HPO stem from a more effective balance between positive and negative advantages, as opposed to using only positive advantages or symmetric updates.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of reinforcement learning environments, particularly those with dense rewards or different reward structures. They also note that the performance gains are primarily observed in early training stages, which may limit the applicability of A-HPO in later training phases. Additionally, the reliance on batch-level statistics for hysteretic weight adjustment could introduce variability depending on batch composition.

**Why it matters**  
The introduction of HPO and A-HPO provides a novel approach to mitigating the instability associated with sparse-reward training in reinforcement learning. By addressing the imbalance in advantage updates and normalizing response lengths, this work enhances the efficiency and stability of policy optimization methods. The implications of this research extend to various applications in reinforcement learning, particularly in scenarios where reward signals are infrequent or delayed. Future work could explore the integration of HPO techniques into other reinforcement learning frameworks and their performance across diverse environments.

Authors: Mohamed Sana, Nicola Piovesan, Antonio De Domenico, Fadhel Ayed, Haozhe Zhang  
Source: arXiv:2605.30201  
URL: https://arxiv.org/abs/2605.30201v1
