---
title: "Parallel Scan Recurrent Neural Quantum States for Scalable Variational Monte Carlo"
date: 2026-05-13 17:36:32 +0000
category: research
subcategory: other
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13807v1"
arxiv_id: "2605.13807"
authors: ["Ejaaz Merali", "Mohamed Hibat-Allah", "Mohammad Kohandel", "Richard T. Scalettar", "Ehsan Khatami"]
slug: parallel-scan-recurrent-neural-quantum-states-for-scalable-v
summary_word_count: 419
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of recurrent neural network quantum states (RNN-QS) in the context of variational Monte Carlo (VMC) simulations for quantum many-body systems. Traditional RNN-QS are perceived as inherently sequential, which hampers their scalability compared to parallel architectures like transformers. The authors propose a novel approach to leverage modern recurrent architectures for efficient and scalable neural quantum state simulations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce the Parallel Scan Recurrent Neural Quantum States (PSR-NQS) framework, which utilizes autoregressive recurrent wave functions combined with advancements in parallelizable recurrence mechanisms. The architecture allows for the training of variational ansätze in both one and two spatial dimensions. The training process is integrated into the VMC framework, enabling efficient optimization of the neural quantum states. The authors do not disclose specific details regarding the compute resources used for training, but they emphasize the efficiency of their approach in handling larger lattice sizes.

**Results**  
The PSR-NQS framework demonstrates significant performance improvements over traditional RNN-QS. The authors benchmark their method against existing quantum Monte Carlo data, achieving accurate results for two-dimensional spin lattices up to sizes of \(52 \times 52\). The PSR-NQS maintains agreement with quantum Monte Carlo results, indicating its effectiveness in capturing the underlying quantum states. The paper highlights that iterative retraining further enhances the model's performance, although specific quantitative metrics (e.g., error rates or computational efficiency) are not provided in the abstract.

**Limitations**  
The authors acknowledge that while their approach shows promise, it is still limited by the inherent challenges of training neural networks for quantum systems, such as the potential for overfitting and the need for extensive hyperparameter tuning. Additionally, the scalability of the PSR-NQS framework may be constrained by the complexity of the quantum systems being modeled. The paper does not address the impact of noise in quantum measurements or the generalization of the model to other quantum systems beyond those tested.

**Why it matters**  
The development of PSR-NQS has significant implications for the field of quantum machine learning and quantum many-body physics. By demonstrating that recurrent architectures can be effectively parallelized, this work opens new avenues for scalable simulations of complex quantum systems with limited computational resources. The findings could facilitate more extensive studies of quantum phenomena and enhance the applicability of neural network approaches in quantum physics, potentially leading to breakthroughs in understanding quantum materials and many-body interactions.

Authors: Ejaaz Merali, Mohamed Hibat-Allah, Mohammad Kohandel, Richard T. Scalettar, Ehsan Khatami  
Source: arXiv:2605.13807  
URL: [https://arxiv.org/abs/2605.13807v1](https://arxiv.org/abs/2605.13807v1)
