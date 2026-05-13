---
title: "Aligning Flow Map Policies with Optimal Q-Guidance"
date: 2026-05-12 17:12:29 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12416v1"
arxiv_id: "2605.12416"
authors: ["Christos Ziakas", "Alessandra Russo", "Avishek Joey Bose"]
slug: aligning-flow-map-policies-with-optimal-q-guidance
summary_word_count: 435
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the efficiency of generative policies for complex control tasks, particularly in the context of offline-to-online reinforcement learning (RL). While existing methods, such as diffusion and flow matching, exhibit high expressivity suitable for multimodal action distributions, they suffer from significant inference latency due to the need for extensive simulation steps during action generation. The authors propose a novel approach to mitigate this issue, which is particularly relevant for real-time applications where quick decision-making is critical. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of flow map policies, which facilitate rapid action generation by enabling arbitrary-size jumps within the generative dynamics of existing flow-based policies. The authors formulate a trust-region optimization problem for online adaptation, ensuring that the adapted policy remains close to the offline policy while improving the critic's Q-value. They derive FLOW MAP Q-GUIDANCE (FMQ), a closed-form learning target that optimally adapts offline flow map policies under the trust-region constraint. Additionally, they present Q-GUIDED BEAM SEARCH (QGBS), a stochastic sampling method that integrates renoising with beam search for iterative refinement during inference. The training process leverages a combination of offline datasets and online interactions, although specific compute resources are not disclosed.

**Results**  
The proposed FMQ method demonstrates state-of-the-art performance across 12 challenging robotic manipulation and locomotion tasks sourced from OGBench and RoboMimic. Notably, FMQ achieves a relative improvement of 21.3% in average success rate compared to the previous one-step policy, MVP. This performance enhancement is significant, indicating that the flow map policies can effectively bridge the gap between offline training and online execution in complex environments.

**Limitations**  
The authors acknowledge that the reliance on a trust-region optimization framework may impose constraints on the adaptability of the policy in highly dynamic environments. Additionally, the computational overhead associated with the QGBS method, particularly during the inference phase, is not fully explored. The paper does not address potential scalability issues when applied to larger state-action spaces or more complex environments beyond those tested.

**Why it matters**  
This work has substantial implications for the field of reinforcement learning, particularly in applications requiring real-time decision-making in complex environments. By improving the efficiency of generative policies, the proposed flow map policies can enhance the practicality of deploying RL systems in robotics and other domains where latency is a critical factor. The methodologies introduced, including FMQ and QGBS, provide a foundation for future research aimed at optimizing generative models for faster inference and better performance in online learning scenarios.

Authors: Christos Ziakas, Alessandra Russo, Avishek Joey Bose  
Source: arXiv:2605.12416  
URL: https://arxiv.org/abs/2605.12416v1
