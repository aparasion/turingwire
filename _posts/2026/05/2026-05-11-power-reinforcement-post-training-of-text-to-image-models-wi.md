---
title: "Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping"
date: 2026-05-11 17:59:25 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.10937v1"
arxiv_id: "2605.10937"
authors: ["Haoyuan Sun", "Jing Wang", "Yuxin Song", "Yu Lu", "Bo Fang", "Yifu Luo"]
slug: power-reinforcement-post-training-of-text-to-image-models-wi
summary_word_count: 430
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing post-training reinforcement learning methods for text-to-image (T2I) models, particularly focusing on Group Relative Policy Optimization (GRPO). The authors highlight the issue of reward hacking, where models exploit biases in reward functions rather than achieving true performance improvements. They also note that normalization techniques can lead to miscalibration, which complicates the separation of genuine signals from noise. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach called Super-Linear Advantage Shaping (SLAS), which re-evaluates the functional update mechanism through the lens of information geometry. SLAS modifies the Fisher-Rao information metric by incorporating advantage-dependent weighting, resulting in a non-linear geometric structure that reshapes the local policy space. This design allows for the relaxation of constraints in high-advantage directions, thereby amplifying informative updates, while tightening constraints in low-advantage regions to mitigate the impact of misleading gradients. Additionally, the authors implement batch-level normalization to stabilize training across varying reward scales. The architecture and specific training compute details are not disclosed, but the method is evaluated across multiple backbone models and benchmarks.

**Results**  
SLAS demonstrates significant improvements over the DanceGRPO baseline across various metrics. Key results include faster training dynamics and enhanced out-of-domain performance on benchmarks such as GenEval and UniGenBench++. The authors report that SLAS improves robustness to model scaling and effectively mitigates reward hacking, while maintaining semantic and compositional fidelity in generated outputs. Specific effect sizes and quantitative comparisons to baselines are provided, although exact numerical values are not detailed in the summary.

**Limitations**  
The authors acknowledge that while SLAS addresses several issues related to reward hacking and normalization, it may still be susceptible to other forms of bias inherent in reward functions. They do not discuss potential limitations related to the scalability of SLAS across different model architectures or the generalizability of their findings to other domains outside T2I. Additionally, the lack of peer review raises questions about the robustness of their claims.

**Why it matters**  
The implications of this work are significant for the advancement of T2I models, particularly in enhancing the reliability and fidelity of generated images. By addressing reward hacking and improving training stability, SLAS could pave the way for more effective post-training methods in reinforcement learning contexts. This research may influence future work in model optimization and the development of more robust reward functions, ultimately contributing to the broader field of generative models and their applications.

Authors: Haoyuan Sun, Jing Wang, Yuxin Song, Yu Lu, Bo Fang, Yifu Luo, Jun Yin, Pengyu Zeng et al.  
Source: arXiv:2605.10937  
URL: [https://arxiv.org/abs/2605.10937v1](https://arxiv.org/abs/2605.10937v1)
