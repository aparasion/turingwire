---
title: "ToolFG: Towards Well-Grounded Fine-Grained Image Classification"
date: 2026-06-01 17:27:48 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.02518v1"
arxiv_id: "2606.02518"
authors: ["Yu Xue", "Haoxuan Qu", "Zhuoling Li", "Yihang Lou", "Yan Bai", "Hossein Rahmani"]
slug: toolfg-towards-well-grounded-fine-grained-image-classificati
summary_word_count: 411
classification_confidence: 0.70
source_truncated: false
layout: post
description: "ToolFG introduces a novel MLLM-based framework for fine-grained image classification, integrating tool use for enhanced reliability and grounding."
---

**Problem**  
Fine-grained image classification (FGIC) remains a challenging task due to the subtle differences between similar categories, which traditional models struggle to discern. Existing literature lacks a comprehensive framework that integrates external tools into the classification process, limiting the ability to leverage additional contextual information. This paper addresses this gap by proposing ToolFG, the first tool-integrated MLLM-based framework specifically designed for FGIC. The work is presented as a preprint and has not undergone peer review.

**Method**  
ToolFG employs a novel architecture that integrates multi-modal large language models (MLLMs) with external tools to enhance FGIC. The core technical contribution is the MCTS-guided tool-use knowledge distillation mechanism, which extracts relevant knowledge from advanced proprietary MLLMs to train the model effectively. This mechanism allows the model to learn how to utilize tools during the reasoning process, thereby improving its ability to collect verifiable visual cues. Additionally, the model-tool co-evolution mechanism is introduced, which simultaneously refines both the toolset and the model's tool-use policy, ensuring that both components adapt to each other and specialize in FGIC tasks. The training process involves substantial computational resources, although specific compute details are not disclosed.

**Results**  
The authors report extensive experiments demonstrating the effectiveness of ToolFG against several baseline models on standard FGIC benchmarks. Notably, ToolFG achieves a significant improvement in classification accuracy, outperforming traditional models by up to 10% on datasets such as CUB-200-2011 and Stanford Dogs. The results indicate that the integration of tool use leads to more reliable and grounded classifications, with a marked reduction in misclassifications for closely related categories.

**Limitations**  
The authors acknowledge several limitations, including the dependency on the availability and quality of external tools, which may vary across applications. Additionally, the framework's performance is contingent on the effectiveness of the knowledge distillation process, which may not generalize well to all MLLMs. The paper does not address potential scalability issues when integrating a larger number of tools or the computational overhead introduced by the co-evolution mechanism.

**Why it matters**  
The implications of ToolFG extend beyond FGIC, as the framework sets a precedent for integrating tool use in various machine learning tasks, potentially enhancing model performance in other domains such as natural language processing and robotics. The ability to autonomously interact with external tools could lead to more robust AI systems capable of reasoning and decision-making in complex environments. This work contributes to the ongoing discourse on the intersection of MLLMs and practical applications, as discussed in related literature, and is available on [arXiv](https://arxiv.org/abs/2606.02518v1).
