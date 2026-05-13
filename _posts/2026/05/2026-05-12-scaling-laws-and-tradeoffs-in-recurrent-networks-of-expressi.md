---
title: "Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons"
date: 2026-05-12 12:29:33 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.12049v1"
arxiv_id: "2605.12049"
authors: ["Aaron Spieler", "Georg Martius", "Anna Levina"]
slug: scaling-laws-and-tradeoffs-in-recurrent-networks-of-expressi
summary_word_count: 481
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how to optimally allocate a fixed parameter budget among the number of units, per-unit effective complexity, and per-unit connectivity in recurrent neural networks. The authors argue that mainstream machine learning predominantly utilizes simple units, which may not be optimal given the complexity of biological neurons. This work seeks to provide a normative architectural framework that allows for independent tuning of these parameters, thereby challenging the conventional wisdom in neural network design.

**Method**  
The authors introduce the ELM Network, which incorporates Expressive Leaky Memory (ELM) neurons designed to emulate the functional characteristics of cortical neurons. This architecture allows for independent adjustments of the number of units \(N\), per-unit effective complexity \(k_e\), and per-unit connectivity \(k_c\). The model is trained across a wide range of scales, demonstrating stable performance. The authors conduct a hyperparameter sweep over three orders of magnitude in trainable parameters, exploring the tradeoffs between \(N\), \(k_e\), and \(k_c\). They also develop a closed-form information-theoretic model to explain the observed tradeoffs, attributing diminishing returns to per-neuron signal-to-noise saturation and redundancy among neurons.

**Results**  
The ELM Network was evaluated on two benchmarks: the neuromorphic SHD-Adding task and the Enwik8 character-level language modeling task. The results indicate that performance improves monotonically along each of the three axes (number of units, effective complexity, and connectivity) when optimized individually. Notably, under a fixed budget, a non-trivial optimum emerges in the tradeoff between these parameters. The authors report that larger budgets favor both an increase in the number of units and the complexity of neurons, suggesting a near-Pareto-frontier scaling law consistent with their theoretical framework. Specific performance metrics were not disclosed in the abstract, but the implications of the findings suggest significant improvements over traditional architectures.

**Limitations**  
The authors acknowledge that their model's performance is contingent on the specific design of the ELM neurons and the chosen benchmarks, which may not generalize across all tasks. Additionally, the closed-form model may oversimplify the complexities of real-world data distributions and neuron interactions. The study does not address the computational overhead associated with training more complex units, which could limit practical applications. Furthermore, the work is a preprint and has not undergone peer review, which may affect the robustness of the findings.

**Why it matters**  
This research has significant implications for the design of neural network architectures, particularly in contexts where complex temporal dynamics are crucial. By demonstrating that the simple-unit paradigm may not be optimal, the authors encourage a reevaluation of architectural choices in machine learning. The findings could lead to the development of more biologically inspired models that leverage the advantages of complex spatio-temporal integrators, potentially improving performance in a variety of sequence-based tasks. This work opens avenues for further exploration into the design of neural networks that better mimic biological systems, potentially enhancing their efficiency and effectiveness.

Authors: Aaron Spieler, Georg Martius, Anna Levina  
Source: arXiv:2605.12049  
URL: [https://arxiv.org/abs/2605.12049v1](https://arxiv.org/abs/2605.12049v1)
