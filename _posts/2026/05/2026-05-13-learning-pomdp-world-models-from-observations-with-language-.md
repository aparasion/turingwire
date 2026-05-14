---
title: "Learning POMDP World Models from Observations with Language-Model Priors"
date: 2026-05-13 16:18:15 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13740v1"
arxiv_id: "2605.13740"
authors: ["Valentin Six", "Frederik Panse", "Mathis Fajeau", "Lancelot Da Costa", "Mridul Sharma", "Alfonso Amayuelas"]
slug: learning-pomdp-world-models-from-observations-with-language-
summary_word_count: 436
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of learning internal models of environments using partially-observable Markov decision processes (POMDPs) from observation-action trajectories. Traditional methods require extensive interaction with the environment, which can be costly and inefficient. The authors propose a novel approach that leverages language-model priors to reduce the need for such interactions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of \emph{Pinductor} (POMDP-inductor), which utilizes a large language model (LLM) to propose candidate POMDP models based on a limited number of observation-action trajectories. The process involves an iterative refinement of these models to optimize a belief-based likelihood score. The architecture relies on the capabilities of the LLM to generate and evaluate POMDP structures, effectively integrating prior knowledge into the model learning process. The training compute specifics are not disclosed, but the method demonstrates significant sample efficiency improvements over traditional tabular POMDP approaches.

**Results**  
\emph{Pinductor} achieves performance metrics that match existing LLM-based POMDP learning methods, which typically assume access to hidden states, while using strictly less information. The authors report that \emph{Pinductor} significantly outperforms tabular POMDP baselines in terms of sample efficiency. The results indicate that performance scales positively with the capability of the LLM employed, and the model's robustness is highlighted by its graceful degradation in performance when semantic information about the environment is withheld. Specific numerical results and comparisons to named baselines are not provided in the abstract, but the implications suggest a substantial improvement in learning efficiency.

**Limitations**  
The authors acknowledge that while \emph{Pinductor} shows promise, it is still dependent on the quality and capability of the underlying LLM. Additionally, the method's performance may vary based on the complexity of the environment and the richness of the observation-action data. The paper does not address potential limitations related to the scalability of the approach in highly dynamic or complex environments, nor does it explore the computational overhead introduced by the iterative refinement process.

**Why it matters**  
This work has significant implications for the development of generalist agents capable of operating in real-world environments with limited interaction. By demonstrating that language-model priors can facilitate sample-efficient learning of POMDPs, the authors position \emph{Pinductor} as a practical tool for advancing the state of the art in world-model learning. This approach could lead to more robust and adaptable agents, reducing the reliance on extensive training data and interaction, which is crucial for applications in robotics, navigation, and interactive systems.

Authors: Valentin Six, Frederik Panse, Mathis Fajeau, Lancelot Da Costa, Mridul Sharma, Alfonso Amayuelas, Tim Z. Xiao, David Hyland et al.  
Source: arXiv cs.LG  
URL: https://arxiv.org/abs/2605.13740v1
