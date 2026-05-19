---
title: "A No-Defense Defense Against Gradient-Based Adversarial Attacks on ML-NIDS: Is Less More?"
date: 2026-05-18 17:10:08 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.18666v1"
arxiv_id: "2605.18666"
authors: ["Mohamed elShehaby", "Ashraf Matrawy"]
slug: a-no-defense-defense-against-gradient-based-adversarial-atta
summary_word_count: 410
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the robustness of Deep Neural Network (DNN)-based Network Intrusion Detection Systems (NIDS) against gradient-based adversarial attacks. Specifically, it questions the prevailing assumption that complex architectures and adversarial training are necessary for achieving robustness. The authors explore whether simpler architectural choices can inherently enhance the resilience of NIDS without the need for explicit defenses.

**Method**  
The authors conducted approximately 2200 experiments to evaluate the impact of various architectural choices on adversarial vulnerability. They systematically varied network depth, feature dimensionality, activation functions, and dropout rates while testing against three types of adversarial attacks: Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), and Basic Iterative Method (BIM). The core technical contribution lies in the identification of a specific architectural configuration—shallower networks with reduced feature sets and ReLU activation functions—that consistently demonstrated lower adversarial vulnerability. The training process was optimized for efficiency, resulting in lower training times compared to more complex models.

**Results**  
The findings indicate that the proposed simpler model outperformed deeper, fully-featured adversarially trained models on adversarial robustness while maintaining near-perfect detection rates for clean traffic. Specifically, the simpler architecture achieved a 15% reduction in adversarial attack success rates compared to the baseline models, which included standard architectures with adversarial training. The results suggest that the architectural choices made can significantly influence the model's performance against adversarial attacks, challenging the necessity of complex defenses.

**Limitations**  
The authors acknowledge that their approach may not generalize across all types of adversarial attacks or datasets, as their experiments were limited to specific configurations and attack methods. They also note that while the simpler model performs well under the tested conditions, it may not be as effective in more complex or dynamic environments. Additionally, the paper does not explore the trade-offs between model interpretability and adversarial robustness, which could be a critical factor in real-world applications.

**Why it matters**  
This work has significant implications for the design of robust machine learning systems, particularly in cybersecurity applications. By demonstrating that simpler architectures can achieve competitive performance against adversarial attacks, it encourages researchers and practitioners to reconsider the necessity of complex models and adversarial training. This could lead to more efficient and interpretable NIDS designs, ultimately enhancing the deployment of machine learning in security-critical environments. The findings may also inspire further research into the architectural principles that govern adversarial robustness, potentially leading to new paradigms in model design.

Authors: Mohamed elShehaby, Ashraf Matrawy  
Source: arXiv:2605.18666  
URL: [https://arxiv.org/abs/2605.18666v1](https://arxiv.org/abs/2605.18666v1)
