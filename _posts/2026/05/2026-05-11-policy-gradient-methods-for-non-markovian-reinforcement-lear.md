---
title: "Policy Gradient Methods for Non-Markovian Reinforcement Learning"
date: 2026-05-11 16:34:28 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10816v1"
arxiv_id: "2605.10816"
authors: ["Avik Kar", "Siddharth Chandak", "Rahul Singh", "Soumitra Sinhahajari", "Eric Moulines", "Shalabh Bhatnagar"]
slug: policy-gradient-methods-for-non-markovian-reinforcement-lear
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in reinforcement learning (RL) methods for non-Markovian decision processes (NMDPs), where the agent's observations and rewards depend on the entire history of interactions rather than solely on the current state. Existing literature primarily focuses on Markovian settings, leaving a significant void in effective policy gradient methods for NMDPs. The authors propose a novel approach to handle this complexity by maintaining an internal state that summarizes past interactions, which is not adequately covered in prior works. This is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Agent State-Markov (ASM) policies, which consist of two components: an agent state dynamics model and a control policy that maps the agent state to actions. The authors derive a new policy gradient theorem specifically for ASM policies, extending classical results from Markovian settings to both episodic and infinite-horizon discounted NMDPs. The proposed Agent State-Markov Policy Gradient (ASMPG) algorithm optimizes both the agent state dynamics and the control policy jointly, focusing on maximizing expected cumulative rewards. The algorithm leverages the recursive structure of the agent state dynamics for efficient optimization. Finite-time and almost sure convergence guarantees are established, ensuring the robustness of the proposed method.

**Results**  
Empirical evaluations demonstrate that ASMPG significantly outperforms baseline methods that utilize predictive objectives for learning state representations. The paper reports improvements across a range of non-Markovian tasks, although specific numerical results and effect sizes are not detailed in the abstract. The authors compare ASMPG against established baselines, showcasing its superior performance in terms of cumulative reward achieved in various experimental setups.

**Limitations**  
The authors acknowledge that their approach may be sensitive to the choice of the initial agent state and the complexity of the underlying dynamics. They also note that while ASMPG shows promise, its performance may vary depending on the specific characteristics of the NMDP being addressed. Additionally, the paper does not explore the scalability of the method to high-dimensional state spaces or the computational overhead associated with maintaining and updating the internal state.

**Why it matters**  
This work has significant implications for advancing RL methodologies in environments where historical context is crucial for decision-making. By providing a framework that effectively integrates past interactions into the learning process, the ASMPG algorithm opens avenues for more sophisticated applications in areas such as robotics, finance, and healthcare, where non-Markovian dynamics are prevalent. The findings encourage further exploration of reward-centric formulations in RL, potentially leading to more robust and efficient learning algorithms in complex environments.

Authors: Avik Kar, Siddharth Chandak, Rahul Singh, Soumitra Sinhahajari, Eric Moulines, Shalabh Bhatnagar, Nicholas Bambos  
Source: arXiv:2605.10816  
URL: https://arxiv.org/abs/2605.10816v1
