---
title: "Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs"
date: 2026-05-05 16:48:23 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03964v1"
arxiv_id: "2605.03964"
authors: ["Eszter Varga-Umbrich", "Shikha Surana", "Paul Duckworth", "Jules Tilly", "Olivier Peltre", "Zachary Weller-Davies"]
slug: pretrained-model-representations-as-acquisition-signals-for-
summary_word_count: 484
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of efficiently training machine learning interatomic potentials (MLIPs) for reactive chemistry, which is often hindered by the high computational cost of obtaining quantum chemical labels and the limited availability of transition state configurations. The authors highlight the limitations of traditional active learning (AL) methods that rely on auxiliary uncertainty heads, Bayesian training, fine-tuning, or committee ensembles, which can complicate the acquisition process. The paper proposes leveraging pretrained model representations as acquisition signals to streamline the active learning process.

**Method**  
The core technical contribution involves the introduction of two novel acquisition signals derived from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel based on features from the model's latent space. The NTK captures the local geometry of the model's output landscape, while the activation kernel utilizes the hidden features to inform acquisition decisions. The authors conduct experiments on reactive-chemistry benchmarks, comparing their approach against fixed-descriptor baselines, committee disagreement strategies, and random acquisition methods. The training compute details are not explicitly disclosed, but the focus is on the efficiency of the acquisition signals rather than extensive retraining of the model.

**Results**  
The proposed acquisition signals demonstrate significant improvements over the baselines. Specifically, the NTK and activation kernel reduce the data required to achieve performance targets by an average of 38% for energy error and 28% for force error. These results indicate that the pretrained model's latent space effectively captures the necessary information for guiding the active learning process, leading to more efficient training of MLIPs. The authors provide quantitative comparisons against fixed-descriptor methods and random acquisition, showcasing the superiority of their approach in terms of data efficiency and performance.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of MLIPs or chemical systems, as the effectiveness of the pretrained representations could depend on the specific training data and model architecture used. Additionally, the reliance on a single pretrained model may introduce biases that could affect the acquisition process. The paper does not address the potential computational overhead associated with the initial pretraining phase, which may be significant depending on the model size and dataset. Furthermore, the study does not explore the scalability of the proposed methods to larger or more complex chemical systems.

**Why it matters**  
This work has important implications for the field of computational chemistry and machine learning, particularly in the context of developing efficient MLIPs for reactive systems. By demonstrating that pretrained model representations can serve as effective acquisition signals, the authors provide a pathway to reduce the data requirements for training MLIPs, thereby lowering the computational costs associated with quantum chemical calculations. This approach could facilitate more rapid advancements in the design and optimization of chemical processes, making it a valuable contribution to both the ML and chemistry communities.

Authors: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies  
Source: arXiv:2605.03964  
URL: https://arxiv.org/abs/2605.03964v1
