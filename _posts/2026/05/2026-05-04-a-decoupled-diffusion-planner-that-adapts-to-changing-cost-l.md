---
title: "A decoupled diffusion planner that adapts to changing cost limits by using cost-conditioned generation for safety and reward gradients for performance"
date: 2026-05-04 16:19:42 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02777v1"
arxiv_id: "2605.02777"
authors: ["Rufeng Chen", "Zhaofan Zhang", "Zhejiang Yang", "Hechang Chen", "Sihong Xie"]
slug: a-decoupled-diffusion-planner-that-adapts-to-changing-cost-l
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of offline safe reinforcement learning (RL) where policies must adapt to varying safety budgets during deployment. Existing methods often struggle with balancing reward maximization and safety compliance, leading to unreliable performance under changing cost constraints. The authors present a novel approach to adaptive safe trajectory generation, framed as sampling from a constrained trajectory distribution, which has not been adequately explored in the literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Safe Decoupled Guidance Diffusion (SDGD) framework, which employs a two-pronged approach to trajectory generation. First, it utilizes cost-conditioned classifier-free guidance to bias the sampling of trajectories towards those that comply with specified cost limits. Second, it incorporates reward-gradient guidance to refine these trajectories for higher expected returns. A key innovation is the introduction of Feasible Trajectory Relabeling (FTR), which reshapes reward targets to mitigate the risk of steering trajectories towards higher cumulative costs while still maximizing rewards. The authors also provide a first-order sampling-time analysis demonstrating that FTR effectively suppresses reward-induced cost drift under a prefix-restorative alignment condition. The training process and computational resources used for the experiments are not explicitly detailed in the abstract.

**Results**  
The SDGD framework was evaluated on the DSRL benchmark, where it demonstrated superior performance compared to existing baselines. Notably, SDGD achieved a safety compliance rate of 94.7%, successfully satisfying the cost constraint in 36 out of 38 tasks. Additionally, it secured the highest reward among safe methods in 21 tasks, indicating a strong balance between safety and performance. These results suggest a significant improvement over prior methods, although specific baseline models and their performance metrics are not disclosed in the abstract.

**Limitations**  
The authors acknowledge that while SDGD shows strong safety compliance, the reliance on cost-conditioned guidance may still lead to challenges in environments with highly dynamic cost structures. They do not discuss potential scalability issues or the computational overhead introduced by the FTR mechanism. Furthermore, the generalizability of the approach to more complex environments or different types of cost constraints remains untested.

**Why it matters**  
This work has significant implications for the field of safe reinforcement learning, particularly in applications where safety constraints are critical, such as robotics and autonomous systems. By providing a robust method for balancing safety and reward, SDGD could enhance the deployment of RL policies in real-world scenarios where cost limits are not static. The insights gained from this research may also inform future studies on adaptive learning in dynamic environments, potentially leading to more resilient and reliable AI systems.

Authors: Rufeng Chen, Zhaofan Zhang, Zhejiang Yang, Hechang Chen, Sihong Xie  
Source: arXiv:2605.02777  
URL: [https://arxiv.org/abs/2605.02777v1](https://arxiv.org/abs/2605.02777v1)
