---
title: "Compress Then Adapt? No, Do It Together via Task-aware Union of Subspaces"
date: 2026-05-04 17:05:45 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02829v1"
arxiv_id: "2605.02829"
authors: ["Jingze Ge", "Yun Liu", "Xue Geng", "Wanqi Dong", "Wang Zhe Mark", "Min Wu"]
slug: compress-then-adapt-no-do-it-together-via-task-aware-union-o
summary_word_count: 463
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing methods for adapting large pretrained models to diverse tasks, specifically the sequential approach of parameter-efficient fine-tuning (PEFT) followed by low-rank compression. This decoupled strategy can lead to misalignment between the compressed subspace and downstream objectives, potentially wasting the global parameter budget. The authors propose a novel framework, JACTUS (Joint Adaptation and Compression with a Task-aware Union of Subspaces), to unify these processes. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
JACTUS integrates compression and adaptation into a single framework. It begins with a small calibration set to estimate input and pre-activation gradient covariances. These covariances are then used to form an orthogonal union with the pretrained weight subspace. The method employs a projected low-rank approximation within this union, allowing for a more effective allocation of rank based on marginal gain per parameter. The training focuses on a compact core matrix, which explicitly aligns the directions preserved for compression with those necessary for adaptation. This approach enables the creation of a deployable low-rank model that avoids the need to retain full frozen weights while facilitating rapid and robust tuning.

**Results**  
On vision tasks, JACTUS achieves an average accuracy of 89.2% on the ViT-Base model across eight datasets while retaining 80% of the parameters. This performance surpasses strong 100% PEFT baselines, such as DoRA, which achieved 87.9%. In language tasks, JACTUS reaches an average accuracy of 80.9% on the Llama2-7B commonsense QA benchmark, again at the same 80% retained-parameter budget. This result outperforms the 100% PEFT baseline (DoRA at 79.7%) and exceeds the performance of prior compress-then-finetune pipelines under the same parameter retention constraints.

**Limitations**  
The authors acknowledge that the performance of JACTUS may be sensitive to the choice of the calibration set, as it directly influences the estimation of covariances. Additionally, the method's reliance on a low-rank approximation may not capture all the nuances of certain tasks, particularly those requiring high-dimensional representations. The paper does not address the computational overhead associated with the initial covariance estimation, which could be a concern in resource-constrained environments.

**Why it matters**  
The introduction of JACTUS has significant implications for the field of model adaptation and compression. By jointly optimizing compression and adaptation, this framework can lead to more efficient use of model parameters, potentially enabling the deployment of large models in environments with limited computational resources. The ability to achieve high performance with reduced parameter budgets may facilitate broader applications of large pretrained models in real-world scenarios, particularly in edge computing and mobile applications. Furthermore, the release of code will allow for further exploration and validation of the proposed method in various contexts.

Authors: Jingze Ge, Yun Liu, Xue Geng, Wanqi Dong, Wang Zhe Mark, Min Wu, Xulei Yang  
Source: arXiv:2605.02829  
URL: [https://arxiv.org/abs/2605.02829v1](https://arxiv.org/abs/2605.02829v1)
