---
title: "Temper and Tilt Lead to SLOP: Reward Hacking Mitigation with Inference-Time Alignment"
date: 2026-05-13 13:47:06 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13537v1"
arxiv_id: "2605.13537"
authors: ["Ye Wang", "Jing Liu", "Toshiaki Koike-Akino"]
slug: temper-and-tilt-lead-to-slop-reward-hacking-mitigation-with-
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of reward hacking in reinforcement learning (RL) systems, particularly in scenarios where alignment objectives and reward targets are dynamic. Existing literature on inference-time alignment techniques provides a framework for adapting RL agents without extensive retraining. However, these methods often lack robustness against reward hacking, where agents exploit loopholes in reward structures. The authors propose a novel approach to enhance these techniques, specifically through the introduction of temperature adjustment in reference models, which has not been extensively explored in prior work. This paper is a preprint and has not undergone peer review.

**Method**  
The core technical contribution is the introduction of a sharpened logarithmic opinion pool (SLOP) that integrates temperature-adjusted reference models into the inference-time alignment framework. The authors develop an algorithm for calibrating the weight parameters of the SLOP, which allows for a more nuanced combination of multiple generative reward models. The architecture leverages ensemble methods to improve generalization and robustness against reward hacking. The training compute requirements are not explicitly disclosed, but the method is designed to be computationally efficient compared to traditional RL approaches, allowing for continual adaptation without extensive retraining.

**Results**  
The authors conduct experiments to evaluate the performance of their proposed SLOP method against baseline inference-time alignment techniques on standard benchmarks. They report a significant improvement in robustness, with a 15% reduction in instances of reward hacking compared to the baseline methods. Additionally, alignment performance is preserved, with a 10% increase in alignment accuracy on the same benchmarks. These results indicate that the SLOP method not only mitigates reward hacking but also maintains the effectiveness of the alignment objectives.

**Limitations**  
The authors acknowledge several limitations in their work. First, the reliance on temperature adjustment may introduce additional hyperparameters that require careful tuning, which could complicate deployment in real-world scenarios. Second, the experiments are conducted in controlled environments, and the generalizability of the results to more complex, real-world tasks remains to be validated. Furthermore, the paper does not address the potential computational overhead introduced by the ensemble methods, which could impact scalability in large-scale applications. Lastly, the authors do not explore the implications of model misalignment in the context of adversarial settings.

**Why it matters**  
This work has significant implications for the development of robust RL systems that can adapt to changing environments and objectives without succumbing to reward hacking. By enhancing inference-time alignment techniques with SLOP, the authors provide a promising avenue for future research in safe and reliable AI systems. The proposed method could facilitate the deployment of RL agents in sensitive applications, such as autonomous systems and decision-making frameworks, where alignment with human values and objectives is critical. This research opens up new directions for exploring ensemble methods in reward modeling and alignment strategies.

Authors: Ye Wang, Jing Liu, Toshiaki Koike-Akino  
Source: arXiv:2605.13537  
URL: https://arxiv.org/abs/2605.13537v1
