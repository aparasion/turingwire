---
title: "Post-Trained MoE Can Skip Half Experts via Self-Distillation"
date: 2026-05-18 16:50:48 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18643v1"
arxiv_id: "2605.18643"
authors: ["Xingtai Lv", "Li Sheng", "Kaiyan Zhang", "Yichen You", "Siyan Gao", "Xueheng Luo"]
slug: post-trained-moe-can-skip-half-experts-via-self-distillation
summary_word_count: 425
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the adaptation of fully trained Mixture-of-Experts (MoE) models to dynamic configurations without the need for extensive retraining. Existing dynamic MoE methods typically require either training from scratch or task-specific fine-tuning, which limits their practical applicability. The authors propose a novel approach to convert static MoE models into efficient dynamic ones post-training, thereby reducing inference costs by allowing easy tokens to bypass unnecessary experts during serving. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Zero-Expert Self-Distillation Adaptation (ZEDA), a framework that facilitates the transformation of post-trained static MoE models into dynamic ones. ZEDA incorporates parameter-free zero-output experts into each MoE layer to stabilize the conversion process. The adaptation is performed through a two-stage self-distillation approach, where the original MoE model serves as a frozen teacher. A group-level balancing loss is applied to ensure effective knowledge transfer. The authors do not disclose specific details regarding the training compute used for the adaptation process.

**Results**  
ZEDA is evaluated on two large models, Qwen3-30B-A3B and GLM-4.7-Flash, across 11 benchmarks that include tasks in mathematics, code generation, and instruction following. The results indicate that ZEDA can eliminate over 50% of expert FLOPs while maintaining a marginal accuracy loss. Specifically, it outperforms the strongest dynamic MoE baseline by 6.1 points on Qwen3-30B-A3B and 4.0 points on GLM-4.7-Flash. Additionally, ZEDA achieves approximately 1.20× end-to-end inference speedup, demonstrating significant efficiency improvements.

**Limitations**  
The authors acknowledge that the accuracy loss, while marginal, is a trade-off for the computational savings achieved. They do not discuss the potential impact of the zero-output experts on model interpretability or the generalizability of the method across different architectures or tasks. Furthermore, the reliance on a frozen teacher model may limit the adaptability of ZEDA to rapidly changing input distributions or tasks that diverge significantly from the original training data.

**Why it matters**  
The implications of this work are significant for the deployment of large language models in resource-constrained environments. By enabling the conversion of static MoE models into dynamic configurations post-training, ZEDA provides a practical solution to reduce inference costs without extensive retraining. This advancement could facilitate the broader adoption of MoE architectures in real-world applications, where efficiency and speed are critical. The framework also opens avenues for further research into self-distillation techniques and their application in optimizing other model architectures.

Authors: Xingtai Lv, Li Sheng, Kaiyan Zhang, Yichen You, Siyan Gao, Xueheng Luo, Yuxin Zuo, Yuchen Fan et al.  
Source: arXiv:2605.18643  
URL: https://arxiv.org/abs/2605.18643v1
