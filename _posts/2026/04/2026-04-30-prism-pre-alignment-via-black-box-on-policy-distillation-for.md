---
title: "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning"
date: 2026-04-30 17:12:53 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28123v1"
arxiv_id: "2604.28123"
authors: ["Sudong Wang", "Weiquan Huang", "Xiaomin Yu", "Zuhao Yang", "Hehai Lin", "Keming Wu"]
slug: prism-pre-alignment-via-black-box-on-policy-distillation-for
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of the standard post-training approach for large multimodal models (LMMs), which typically involves supervised fine-tuning (SFT) followed by reinforcement learning with verifiable rewards (RLVR). The authors highlight that SFT can induce distributional drift, leading to a degradation of the model's original capabilities and a mismatch with the supervision distribution. This issue is particularly pronounced in multimodal reasoning tasks, where distinct drift patterns in perception and reasoning can compound during subsequent RL training. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose PRISM, a three-stage pipeline designed to mitigate distributional drift by introducing a distribution-alignment stage between SFT and RLVR. The core technical contribution is the use of on-policy distillation (OPD) framed as a black-box adversarial game. In this setup, a policy interacts with a Mixture-of-Experts (MoE) discriminator that includes specialized perception and reasoning experts. This architecture allows for disentangled corrective signals that guide the policy towards the supervision distribution without requiring access to teacher logits. The training process utilizes 1.26 million public demonstrations for SFT initialization, supplemented by an additional 113,000 high-fidelity demonstrations curated from Gemini 3 Flash, which focus on dense visual grounding and step-by-step reasoning for complex problems.

**Results**  
Experiments conducted on the Qwen3-VL benchmark demonstrate that PRISM significantly enhances the performance of downstream RLVR tasks across various reinforcement learning algorithms, including GRPO, DAPO, and GSPO. The results indicate an average accuracy improvement of +4.4 points for the 4B model and +6.0 points for the 8B model when compared to the SFT-to-RLVR baseline. These improvements are statistically significant and suggest that the proposed distribution-alignment stage effectively addresses the issues of drift and performance degradation.

**Limitations**  
The authors acknowledge that while PRISM improves performance, it relies on the availability of high-fidelity supervision, which may not be feasible for all applications. Additionally, the complexity of the MoE architecture may introduce overhead in terms of computational resources and training time. The paper does not discuss the potential scalability of the approach to larger models or different multimodal tasks beyond those tested.

**Why it matters**  
The implications of this work are significant for the field of multimodal reinforcement learning. By addressing the critical issue of distributional drift, PRISM provides a novel framework that enhances the robustness and performance of LMMs in complex reasoning tasks. This approach could pave the way for more effective training methodologies in multimodal AI systems, potentially leading to advancements in applications such as robotics, autonomous systems, and interactive AI agents. The availability of code, data, and model checkpoints further facilitates reproducibility and encourages further research in this area.

Authors: Sudong Wang, Weiquan Huang, Xiaomin Yu, Zuhao Yang, Hehai Lin, Keming Wu, Chaojun Xiao, Chen Chen et al.  
Source: arXiv:2604.28123  
URL: https://arxiv.org/abs/2604.28123v1
