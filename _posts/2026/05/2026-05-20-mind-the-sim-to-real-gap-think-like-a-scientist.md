---
title: "Mind the Sim-to-Real Gap & Think Like a Scientist"
date: 2026-05-20 17:48:14 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21458v1"
arxiv_id: "2605.21458"
authors: ["Harsh Parikh", "Gabriel Levin-Konigsberg", "Dominique Perrault-Joncas", "Alexander Volfovsky"]
slug: mind-the-sim-to-real-gap-think-like-a-scientist
summary_word_count: 437
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how to effectively integrate simulation-based planning with real-world experimentation in sequential decision-making problems. Existing literature often overlooks the confounding effects and drift inherent in simulators, which can lead to suboptimal decision-making when transitioning from simulation to real-world applications. The authors aim to provide a framework for planners to determine when and how to supplement simulator outputs with real-world experiments, thereby bridging the sim-to-real gap.

**Method**  
The core technical contribution is the development of an extended simulation lemma that decomposes the simulator's value error into two components: a calibration-deployment shift, which can be identified through randomization, and a parametric residual that remains invariant to further interactions. The authors introduce a novel policy, Fisher-SEP (Simulation-Aided Experimental Policy), which minimizes the posterior predictive variance of a target policy's value. Fisher-SEP has two specializations: one focusing on reward-only data and the other on transition-only data. The methodology is evaluated through two case studies: a vending-machine supply chain and an HIV mobile-testing scenario, illustrating the practical application of the proposed framework.

**Results**  
In the vending-machine supply chain case study, the authors demonstrate that front-loaded experimentation becomes more beneficial than posterior updating once the planning horizon is sufficiently long to amortize the costs of the pilot experiments. In the HIV mobile-testing example, the designed exploration strategy successfully reaches poorly-surveilled regions, which would not be accessible through passive learning alone. While specific numerical results are not disclosed in the abstract, the qualitative findings suggest significant improvements in decision-making efficacy when employing the proposed methods compared to traditional simulation-only approaches.

**Limitations**  
The authors acknowledge that their framework relies on the assumption that the simulator's calibration data is representative of the real-world environment, which may not always hold true. Additionally, the effectiveness of Fisher-SEP is contingent on the ability to accurately model the posterior predictive variance, which may be challenging in complex environments. The paper does not address the computational overhead associated with implementing the proposed experimental policies, nor does it explore the scalability of the approach in high-dimensional state spaces.

**Why it matters**  
This work has significant implications for the design of decision-making systems that rely on both simulation and real-world experimentation. By providing a structured approach to quantify and mitigate the sim-to-real gap, the authors enable practitioners to make more informed decisions in uncertain environments. The insights gained from the case studies can inform future research on hybrid decision-making frameworks, particularly in fields such as robotics, healthcare, and supply chain management, where the integration of simulation and real-world data is critical for success.

Authors: Harsh Parikh, Gabriel Levin-Konigsberg, Dominique Perrault-Joncas, Alexander Volfovsky  
Source: arXiv:2605.21458  
URL: [https://arxiv.org/abs/2605.21458v1](https://arxiv.org/abs/2605.21458v1)
