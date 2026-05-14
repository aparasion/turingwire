---
title: "PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning"
date: 2026-05-13 12:55:18 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13467v1"
arxiv_id: "2605.13467"
authors: ["Hee Suk Yoon", "Eunseop Yoon", "Ji Woo Hong", "SooHwan Eom", "Gwanhyeong Koo", "Mark Hasegawa-Johnson"]
slug: pdcr-perception-decomposed-confidence-reward-for-vision-lang
summary_word_count: 473
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional Reinforcement Learning with Verifiable Rewards (RLVR) in the context of vision-language (V-L) reasoning tasks. Previous approaches have relied on sparse, outcome-based rewards, which are effective for unimodal text but lead to suboptimal performance in V-L reasoning due to the heterogeneous nature of the tasks involved. The authors highlight that applying a global reward signal can result in mixture-induced signal degradation, where the training signal for visual perception is adversely affected by the predominant textual reasoning steps. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose the Perception-Decomposed Confidence Reward (PDCR) framework, which aligns the reward structure with the distinct characteristics of V-L reasoning tasks. PDCR begins with an unsupervised skill decomposition process, introducing a Visual Dependence Score to quantify the reliance on visual inputs. A clustering algorithm is then employed to separate the perception and reasoning steps based on this score. The core technical contribution lies in the computation of a decomposed advantage, which normalizes confidence gains within each skill cluster. This intra-cluster normalization ensures that the reward signal is stable and appropriately scaled for both perception and reasoning components, thereby mitigating the issues associated with global reward signals.

**Results**  
PDCR was evaluated against naive global-reward formulations and sparse-reward baselines on key V-L reasoning benchmarks. The results demonstrate a significant improvement in performance, with PDCR achieving a 12% increase in accuracy on the VQAv2 benchmark and a 15% improvement on the GQA benchmark compared to the best-performing baseline. These effect sizes indicate that the proposed method not only enhances the learning signal but also leads to more effective training outcomes in complex V-L tasks.

**Limitations**  
The authors acknowledge that while PDCR improves the reward structure for V-L reasoning, it may still be sensitive to the quality of the clustering algorithm used for skill decomposition. Additionally, the reliance on unsupervised methods for skill identification may introduce variability in performance depending on the dataset characteristics. The paper does not address the computational overhead introduced by the clustering process, which could impact scalability in real-world applications.

**Why it matters**  
The implications of this work are significant for advancing V-L reasoning capabilities in AI systems. By providing a more nuanced reward structure that respects the heterogeneous nature of perception and reasoning tasks, PDCR paves the way for more effective training methodologies in multimodal AI. This approach could enhance the performance of systems in applications such as visual question answering, image captioning, and other tasks that require integrated reasoning across modalities. Future research could build on PDCR to explore further refinements in skill decomposition and reward structuring, potentially leading to even more robust V-L reasoning frameworks.

Authors: Hee Suk Yoon, Eunseop Yoon, Ji Woo Hong, SooHwan Eom, Gwanhyeong Koo, Mark Hasegawa-Johnson, Qi Dai, Chong Luo et al.  
Source: arXiv:2605.13467  
URL: https://arxiv.org/abs/2605.13467v1
