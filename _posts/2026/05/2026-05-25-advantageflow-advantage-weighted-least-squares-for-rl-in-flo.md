---
title: "AdvantageFlow: Advantage-Weighted Least Squares for RL in Flow Models"
date: 2026-05-25 16:32:14 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26013v1"
arxiv_id: "2605.26013"
authors: ["Branislav Kveton", "Anup Rao", "Subhojyoti Mukherjee", "Krishna Kumar Singh", "Viet Dac Lai"]
slug: advantageflow-advantage-weighted-least-squares-for-rl-in-flo
summary_word_count: 424
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing reinforcement learning (RL) approaches in optimizing flow models, specifically focusing on the instability of optimizing the reverse process as seen in Flow-GRPO. The authors propose a novel forward-process RL algorithm, AdvantageFlow, which aims to improve the training stability and performance of rectified flow models. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
AdvantageFlow introduces an advantage-weighted forward-process prediction loss, which is designed to optimize the forward process of flow models. The core technical contribution lies in the stabilization of the optimization problem, which can become non-convex when the advantages are negative. To mitigate this issue, the authors implement rollout policy regularization, which reduces variance by fitting a local reward-improving target distribution. The architecture leverages the capabilities of rectified flow models, specifically targeting image generation tasks. The training compute details are not disclosed, but the evaluation is conducted using Stable Diffusion 3.5 Medium as the benchmark for performance comparison.

**Results**  
AdvantageFlow demonstrates superior performance over Flow-GRPO and a state-of-the-art forward-process RL baseline that employs negative-aware fine-tuning. While specific numerical results are not provided in the abstract, the authors claim that AdvantageFlow outperforms these baselines on image generation tasks, indicating a significant improvement in the quality of generated images. The effect sizes are implied to be substantial, although exact metrics such as FID scores or other quantitative measures are not detailed in the summary.

**Limitations**  
The authors acknowledge that the optimization problem can still be sensitive to the choice of hyperparameters, particularly in the context of the rollout policy regularization. They do not discuss the scalability of AdvantageFlow to more complex or high-dimensional environments, nor do they address potential limitations in generalization across different types of flow models. Additionally, the reliance on Stable Diffusion 3.5 Medium for evaluation may limit the applicability of the findings to other generative models or tasks.

**Why it matters**  
The introduction of AdvantageFlow has significant implications for the field of generative modeling and reinforcement learning. By providing a more stable and effective method for optimizing flow models, this work could enhance the performance of various applications in image generation and beyond. The approach may also inspire further research into the integration of RL techniques with generative models, potentially leading to advancements in areas such as unsupervised learning and model-based RL. The findings could pave the way for more robust algorithms that can handle the complexities of real-world data distributions.

Authors: Branislav Kveton, Anup Rao, Subhojyoti Mukherjee, Krishna Kumar Singh, Viet Dac Lai  
Source: arXiv:2605.26013  
URL: [https://arxiv.org/abs/2605.26013v1](https://arxiv.org/abs/2605.26013v1)
