---
title: "COOPO: Cyclic Offline-Online Policy Optimization Algorithm"
date: 2026-05-18 17:15:27 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18675v1"
arxiv_id: "2605.18675"
authors: ["Qisai Liu", "Zhanhong Jiang", "Joshua Russell Waite", "Aditya Balu", "Cody Fleming", "Soumik Sarkar"]
slug: coopo-cyclic-offline-online-policy-optimization-algorithm
summary_word_count: 468
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of offline reinforcement learning (RL), which suffers from distributional shift and constrained performance due to static datasets, and online RL, which requires extensive environment interactions. The authors identify a gap in hybrid offline-to-online methods that often experience distribution drift and catastrophic forgetting when transitioning between offline and online training. COOPO (Cyclic Offline-Online Policy Optimization) is proposed as a solution to these issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
COOPO introduces a cyclic framework that alternates between constrained offline training and online fine-tuning. The offline phase employs KL-regularized advantage-weighted updates to anchor the policy to the dataset, effectively minimizing distributional shift. This is followed by an online fine-tuning phase, where any policy optimization method can be utilized to enhance exploration stability. The cyclic nature of COOPO allows for periodic returns to offline training, which mitigates the risks of catastrophic forgetting and distribution drift while maximizing the reuse of the offline dataset. The authors theoretically demonstrate that COOPO achieves improved online sample efficiency compared to pure online RL, with guaranteed monotonic improvement under standard coverage assumptions.

**Results**  
COOPO was evaluated on extensive D4RL benchmarks, where it demonstrated a significant reduction in online interactions compared to state-of-the-art hybrid methods. Specifically, COOPO achieved a 20% improvement in final returns on the D4RL medium-expert benchmark compared to the best-performing hybrid method. Additionally, it maintained robustness across various offline algorithms and online optimizers, showcasing its versatility. The results indicate that COOPO sets new standards for efficiency and performance in adaptive RL, particularly in scenarios where dataset limitations are a concern.

**Limitations**  
The authors acknowledge that while COOPO effectively reduces distributional drift and catastrophic forgetting, the performance is still contingent on the quality and representativeness of the offline dataset. They also note that the theoretical guarantees are based on standard coverage assumptions, which may not hold in all practical scenarios. Furthermore, the cyclic nature of the algorithm may introduce additional computational overhead, which could be a concern in resource-constrained environments. The paper does not address the scalability of COOPO to very large datasets or complex environments, which could limit its applicability.

**Why it matters**  
The introduction of COOPO has significant implications for the field of reinforcement learning, particularly in bridging the gap between offline and online methods. By effectively leveraging offline datasets while minimizing the drawbacks associated with distributional shift and catastrophic forgetting, COOPO enhances sample efficiency and performance in adaptive RL. This framework could pave the way for more robust RL applications in real-world scenarios where data collection is expensive or impractical. The findings encourage further exploration of cyclic training methodologies in RL, potentially leading to new advancements in the field.

Authors: Qisai Liu, Zhanhong Jiang, Joshua Russell Waite, Aditya Balu, Cody Fleming, Soumik Sarkar  
Source: arXiv:2605.18675  
URL: [https://arxiv.org/abs/2605.18675v1](https://arxiv.org/abs/2605.18675v1)
