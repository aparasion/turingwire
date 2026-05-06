---
title: "RD-ViT: Recurrent-Depth Vision Transformer for Semantic Segmentation with Reduced Data Dependence Extending the Recurrent-Depth Transformer Architecture to Dense Prediction"
date: 2026-05-05 17:21:18 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.03999v1"
arxiv_id: "2605.03999"
authors: ["Renjie He"]
slug: rd-vit-recurrent-depth-vision-transformer-for-semantic-segme
summary_word_count: 449
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the significant data dependence of Vision Transformers (ViTs) in semantic segmentation tasks, particularly in medical imaging, where labeled datasets are often limited. The authors propose RD-ViT, a Recurrent-Depth Vision Transformer that extends the Recurrent-Depth Transformer (RDT) architecture to dense prediction tasks, enabling effective segmentation with reduced training data. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
RD-ViT innovatively replaces the conventional deep stack of unique transformer blocks with a single shared block that is looped T times. This architecture incorporates several key components: 
- **LTI-stable state injection** ensures convergence during training.
- **Adaptive Computation Time (ACT)** allows for dynamic spatial compute allocation, optimizing resource usage based on input complexity.
- **Depth-wise LoRA adaptation** facilitates efficient parameter tuning across layers.
- **Mixture-of-Experts (MoE)** feed-forward networks are optionally integrated to enable category-specific specialization without explicit routing supervision. 

The model is evaluated on the ACDC cardiac MRI segmentation benchmark, both in 2D slice-level and 3D volumetric settings, using real experiments conducted on Google Colab.

**Results**  
In 2D segmentation, RD-ViT demonstrates superior performance with only 10% of the training data, achieving a Dice score of 0.774 compared to the standard ViT's 0.762. When trained on the full dataset, RD-ViT achieves a Dice score of 0.882, surpassing the standard ViT's score of 0.872. In the 3D setting, RD-ViT with MoE achieves a Dice score of 0.812 with only 3.0M parameters, reaching 99.4% of the standard ViT's performance (0.817) while utilizing just 53% of the parameter count. The analysis of MoE expert utilization reveals spontaneous specialization for different cardiac structures (right ventricle, myocardium, left ventricle). Additionally, ACT halting maps indicate higher compute allocation at cardiac boundaries, with mean ponder time decreasing from 2.6 to 1.4 iterations during training, showcasing learned computational efficiency.

**Limitations**  
The authors acknowledge that while RD-ViT reduces data dependence, it still requires careful tuning of hyperparameters such as the number of loops T and the configuration of MoE. The model's performance on other datasets beyond ACDC is not evaluated, which may limit generalizability. Furthermore, the reliance on a single shared block may introduce challenges in capturing complex features compared to fully independent layers in traditional ViTs.

**Why it matters**  
The development of RD-ViT has significant implications for the field of medical image segmentation, particularly in scenarios with limited labeled data. By demonstrating that a shared architecture can achieve competitive performance with fewer parameters, this work opens avenues for more efficient model designs in resource-constrained environments. The findings also suggest that adaptive mechanisms like ACT and MoE can enhance model efficiency and specialization, which could be beneficial for other dense prediction tasks in computer vision.

Authors: Renjie He  
Source: arXiv:2605.03999  
URL: https://arxiv.org/abs/2605.03999v1
