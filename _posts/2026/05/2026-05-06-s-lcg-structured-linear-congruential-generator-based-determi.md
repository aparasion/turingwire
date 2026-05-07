---
title: "S-LCG: Structured Linear Congruential Generator-Based Deterministic Algorithm for Search and Optimization"
date: 2026-05-06 17:57:41 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.05198v1"
arxiv_id: "2605.05198"
authors: ["Ahmed Qasim Mohammed", "Haider Banka", "Anamika Singh"]
slug: s-lcg-structured-linear-congruential-generator-based-determi
summary_word_count: 388
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of conventional optimization algorithms, which typically operate within a search space without a structured approach to balancing exploration and exploitation. The authors propose a novel deterministic optimization algorithm, the Structured Linear Congruential Generator (S-LCG), to fill this gap. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The S-LCG algorithm employs a two-level architecture comprising an external loop for adaptive exploration-exploitation and an internal loop for solution evaluation. Key technical contributions include:  
1. **Memoryless Scheme**: Utilizes distinct seeds to generate non-overlapping sequences, eliminating evaluation redundancy.  
2. **Bit Splitting Representation**: Converts LCG states into multi-dimensional points, effectively mitigating the Marsaglia lattice effect.  
3. **Adaptive Exploration-Exploitation**: Dynamically adjusts the balance between exploration and exploitation, optimizing the surrogate smooth objective function.  
4. **Constant Information Gathering Speed**: Ensures consistent performance and avoids premature convergence.  
The algorithm was tested on 26 benchmark functions across dimensions ranging from 2 to 30, demonstrating its robustness and efficiency.

**Results**  
S-LCG achieved proximity to the global optimum in 83.3% of 138 test cases, with a perfect score of 100% at d = 2 and 81.2% at d = 30. In comparison, the Genetic Algorithm (GA), the nearest competitor, reached only 75.4% success. Additionally, S-LCG outperformed eight state-of-the-art binary optimization algorithms, as validated through statistical analysis. The practical applicability of S-LCG was further confirmed through testing on three constrained engineering design problems, showcasing its versatility across different optimization scenarios.

**Limitations**  
The authors acknowledge that the performance of S-LCG may vary with the choice of the single sensitive parameter that requires tuning. They do not discuss potential scalability issues or the algorithm's performance in high-dimensional spaces beyond the tested range. Furthermore, the reliance on a deterministic approach may limit its applicability in scenarios where stochastic methods are preferred.

**Why it matters**  
The introduction of S-LCG provides a structured framework for deterministic optimization that enhances the balance between exploration and exploitation, which is critical for solving complex optimization problems. Its reproducibility and minimal parameter tuning requirements make it an attractive option for researchers and practitioners in fields requiring optimization solutions. The findings could influence future work in algorithm design, particularly in developing hybrid approaches that integrate deterministic and stochastic methods for improved performance in diverse applications.

Authors: Ahmed Qasim Mohammed, Haider Banka, Anamika Singh  
Source: arXiv:2605.05198  
URL: [https://arxiv.org/abs/2605.05198v1](https://arxiv.org/abs/2605.05198v1)
