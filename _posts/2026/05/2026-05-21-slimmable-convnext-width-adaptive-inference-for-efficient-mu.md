---
title: "Slimmable ConvNeXt: Width-Adaptive Inference for Efficient Multi-Device Deployment"
date: 2026-05-21 16:20:18 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22677v1"
arxiv_id: "2605.22677"
authors: ["Janek Haberer", "Jon Eike Wilhelm", "Olaf Landsiedel"]
slug: slimmable-convnext-width-adaptive-inference-for-efficient-mu
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of deploying vision models across devices with varying resource constraints, as well as the need for a single model to adapt to fluctuating compute resources on a single device. Traditional approaches necessitate training and maintaining separate models for different configurations, which is inefficient. The authors present Slimmable ConvNeXt, a novel architecture that enables width-adaptive inference without the normalization overhead associated with previous CNN-based methods, which relied on switchable batch normalization. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Slimmable ConvNeXt architecture, which leverages the modern design principles of ConvNeXt, specifically utilizing LayerNorm and inverted bottlenecks. This design facilitates channel-width slimming, allowing for the training of a single set of shared weights that encompass multiple nested subnetworks of varying capacities. The training process involves a straightforward pipeline, eliminating the complexities of normalization seen in classical slimmable networks. The model is trained from scratch for 600 epochs, with a focus on achieving efficient inference across different compute budgets.

**Results**  
On the ImageNet-1k benchmark, Slimmable ConvNeXt-T, which includes three subnetworks, achieves a top-1 accuracy of 80.8% at 4.5 GMACs and 77.4% at 1.2 GMACs. These results surpass the performance of the HydraViT model, which achieves 78.4% accuracy with a 6-head subnetwork at 4.6 GMACs, by 2.4 percentage points, and its 3-head configuration, which achieves 73.0% at 1.3 GMACs, by 4.4 percentage points. Additionally, Slimmable ConvNeXt-T outperforms MatFormer-S (78.6%) and SortedNet-S (78.2%) at comparable GMACs. Scaling the architecture to Slimmable ConvNeXt-B further enhances the maximum accuracy to 82.8% at 15.35 GMACs.

**Limitations**  
The authors acknowledge that while Slimmable ConvNeXt simplifies the training pipeline, it may still be limited by the inherent trade-offs between model capacity and computational efficiency. They do not discuss potential issues related to the generalization of the model across diverse datasets or the implications of using LayerNorm in various deployment scenarios. Additionally, the performance on edge devices or under real-world conditions is not evaluated, which could impact the practical applicability of the model.

**Why it matters**  
The implications of this work are significant for the deployment of vision models in resource-constrained environments. By enabling a single model to adapt to varying compute capabilities, Slimmable ConvNeXt can streamline the deployment process, reduce the need for multiple model versions, and enhance the efficiency of inference across devices. This approach could facilitate broader adoption of advanced vision models in mobile and edge computing applications, where resource constraints are a critical consideration.

Authors: Janek Haberer, Jon Eike Wilhelm, Olaf Landsiedel  
Source: arXiv:2605.22677  
URL: [https://arxiv.org/abs/2605.22677v1](https://arxiv.org/abs/2605.22677v1)
