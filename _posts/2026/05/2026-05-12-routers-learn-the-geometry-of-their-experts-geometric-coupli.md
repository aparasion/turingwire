---
title: "Routers Learn the Geometry of Their Experts: Geometric Coupling in Sparse Mixture-of-Experts"
date: 2026-05-12 17:55:02 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12476v1"
arxiv_id: "2605.12476"
authors: ["Sagi Ahrac", "Noya Hochwald", "Mor Geva"]
slug: routers-learn-the-geometry-of-their-experts-geometric-coupli
summary_word_count: 449
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenges in training Sparse Mixture-of-Experts (SMoE) models, particularly the issues of routing collapse onto a limited number of experts and the detrimental effects of auxiliary load-balancing losses on expert specialization. The authors investigate the mechanistic formation of routing decisions, revealing a previously unexplored geometric relationship between routers and their corresponding experts. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a theoretical framework that elucidates the geometric coupling between routers and experts in SMoE models. They demonstrate that for a given token, the router weights for the selected expert and the expert weights processing that token receive gradients in the same input direction, differing only in scalar coefficients. This coupling is empirically validated through experiments on a 1 billion parameter SMoE model trained from scratch, where higher router scores correlate with stronger activations in the corresponding expert neurons. The authors also analyze the impact of auxiliary load-balancing losses, showing that these losses disrupt the geometric coupling by spreading input-directed gradients across router weights, leading to increased similarity among distinct router directions. To leverage this geometric coupling, they propose a parameter-free online K-Means router, where each expert maintains a running average of the hidden states routed to it, and tokens are assigned based on cosine similarity. This method is compared against traditional auxiliary-loss and loss-free balancing approaches.

**Results**  
The proposed K-Means router achieves the lowest load imbalance among the tested routing strategies, with only a modest increase in perplexity. Specifically, the K-Means router demonstrates a significant improvement in load distribution, outperforming the auxiliary-loss method by nearly three times in terms of maintaining distinct router directions. The empirical results indicate that the geometric coupling captures a substantial portion of the routing dynamics, providing a more effective division of labor among experts.

**Limitations**  
The authors acknowledge that their findings are based on a specific architecture and dataset, which may limit the generalizability of the results. They do not address potential scalability issues when applying the K-Means router to larger models or different tasks. Additionally, the impact of varying the number of experts on the routing dynamics is not explored in depth.

**Why it matters**  
This work has significant implications for the design and training of SMoE models, particularly in understanding the underlying mechanisms of routing decisions. By elucidating the geometric coupling between routers and experts, the findings provide a foundation for developing more effective routing strategies that enhance expert specialization and improve model performance. The proposed K-Means router offers a promising alternative to traditional load-balancing techniques, potentially influencing future research on efficient model scaling and expert utilization.

Authors: Sagi Ahrac, Noya Hochwald, Mor Geva  
Source: arXiv:2605.12476  
URL: https://arxiv.org/abs/2605.12476v1
