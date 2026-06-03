---
title: "FlashbackCL: Mitigating Temporal Forgetting in Federated Learning"
date: 2026-06-02 17:28:21 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03939v1"
arxiv_id: "2606.03939"
authors: ["Mubarak A. Ojewale", "Adriana E. Chis", "Jorge M. Cortes-Mendoza", "Bernardo Pulido-Gaytan", "Horacio Gonzalez-Velez"]
slug: flashbackcl-mitigating-temporal-forgetting-in-federated-lear
summary_word_count: 414
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces FlashbackCL, a method to mitigate temporal forgetting in Federated Learning, enhancing model performance under data distribution shifts."
---

**Problem**  
The paper addresses the gap in Federated Learning (FL) methodologies that inadequately handle temporal forgetting, particularly in scenarios where client data distributions evolve over time. Existing forgetting-mitigation techniques, including the prominent Flashback method, assume stationary distributions across clients, which is not reflective of real-world applications. This work is a preprint and has not undergone peer review, highlighting the need for further validation of its findings.

**Method**  
The authors propose Flashback Continual Learning (FlashbackCL), an extension of the Flashback framework designed to counteract the effects of temporal distribution shifts. The core technical contributions include: 
1. **Temporally-decayed label counts**: This mechanism updates the label counts to reflect recent data distributions, preventing the model from being anchored to outdated class balances.
2. **Device-aware replay buffer with Class-Balanced Reservoir Sampling (CBRS)**: This component ensures that the replay buffer maintains a balanced representation of classes, which is crucial for effective learning in heterogeneous environments.
3. **Server-side active coreset curation**: This involves selecting a representative subset of the public distillation set to enhance the training process.

The training compute details are not explicitly disclosed, but the method is designed to be a drop-in replacement for existing Flashback implementations.

**Results**  
FlashbackCL demonstrates significant improvements over the original Flashback method, achieving a relative performance increase of 6.9% to 10.0% on the CIFAR-10 dataset with 50 clients across three controlled temporal shift scenarios. Additionally, it reduces temporal forgetting by up to 68%. An ablation study reveals that the CBRS replay mechanism is the most critical component contributing to these improvements. Furthermore, FlashbackCL also enhances performance on the stationary CIFAR-100 dataset by 3.5 points, indicating its effectiveness in addressing both spatial heterogeneity and temporal shifts.

**Limitations**  
The authors acknowledge that their approach may still be sensitive to the choice of hyperparameters and the specific characteristics of the data distributions. They do not address potential scalability issues when applied to larger client populations or more complex datasets. Additionally, the reliance on a public distillation set for coreset curation may introduce biases if the set is not representative of the evolving client distributions.

**Why it matters**  
The implications of this work are significant for the deployment of Federated Learning systems in dynamic environments, such as IoT applications and mobile devices, where data distributions can change over time. By effectively mitigating temporal forgetting, FlashbackCL enhances the robustness and adaptability of FL models, paving the way for more reliable applications in real-world scenarios. This research contributes to the ongoing discourse in the field, as published in [arXiv](https://arxiv.org/abs/2606.03939v1).
