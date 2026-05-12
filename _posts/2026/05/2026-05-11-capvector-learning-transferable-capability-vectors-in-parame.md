---
title: "CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models"
date: 2026-05-11 17:41:54 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.10903v1"
arxiv_id: "2605.10903"
authors: ["Wenxuan Song", "Han Zhao", "Fuhao Li", "Ziyang Zhou", "Xi Wang", "Jing Lyu"]
slug: capvector-learning-transferable-capability-vectors-in-parame
summary_word_count: 448
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of pretrained Vision-Language-Action (VLA) models in effectively improving performance and reducing adaptation costs during standard supervised finetuning (SFT). Existing advanced finetuning methods that utilize auxiliary training objectives often lead to significant computational overhead due to the additional losses incurred. The authors propose a novel approach to decouple the objectives of auxiliary-objective SFT, aiming to enhance general capabilities while fitting task-specific action distributions without the associated computational burden. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of "capability vectors" derived from the parameter space of two distinct finetuned models. The authors first finetune a model on a small-scale task set using two separate training strategies: one focused on enhancing general capabilities and the other on fitting task-specific action distributions. The difference in parameters between these two models is interpreted as capability vectors. These vectors are then merged with the pretrained parameters to create a capability-enhanced meta model. Additionally, the authors incorporate a lightweight orthogonal regularization loss during standard SFT, which allows the merged model to achieve performance levels comparable to those of auxiliary finetuned baselines while significantly reducing computational overhead.

**Results**  
The proposed CapVector method demonstrates effectiveness across various models and tasks. The authors report that their capability vectors generalize well to novel environments and embodiments without requiring further adaptation. While specific numerical results and comparisons to named baselines are not detailed in the abstract, the internal and external experiments indicate that the performance of the capability-enhanced meta model is on par with that of models finetuned with auxiliary objectives, but with a marked reduction in computational costs.

**Limitations**  
The authors acknowledge that their approach may not fully eliminate the performance gap in all scenarios, particularly in highly specialized tasks where auxiliary objectives might still provide an advantage. They do not discuss potential limitations related to the scalability of their method to larger datasets or more complex tasks, nor do they address the potential impact of the choice of regularization loss on model performance.

**Why it matters**  
The implications of this work are significant for the field of VLA models, as it presents a method to enhance model capabilities without incurring the high computational costs typically associated with auxiliary training objectives. This could lead to more efficient training pipelines and broader applicability of VLA models in real-world scenarios, particularly in resource-constrained environments. The ability to generalize capability vectors across diverse models also opens avenues for future research into modular and transferable learning strategies in multimodal contexts.

Authors: Wenxuan Song, Han Zhao, Fuhao Li, Ziyang Zhou, Xi Wang, Jing Lyu, Pengxiang Ding, Yan Wang et al.  
Source: arXiv:2605.10903  
URL: https://arxiv.org/abs/2605.10903v1
