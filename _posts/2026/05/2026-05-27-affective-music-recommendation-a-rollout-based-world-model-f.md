---
title: "Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization"
date: 2026-05-27 17:58:46 +0000
category: research
subcategory: other
company: "LUCID"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28810v1"
arxiv_id: "2605.28810"
authors: ["Audrey Chan", "Aaron Labb\u00e9", "Jacob Lavoie", "Jordan Bannister", "Ars\u00e8ne Fansi Tchango", "Guillaume Lajoie"]
slug: affective-music-recommendation-a-rollout-based-world-model-f
summary_word_count: 441
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in affective music recommendation systems, particularly in contexts where online experimentation is ethically constrained, such as with clinical populations (e.g., older adults with neurocognitive conditions). The authors present the Affective Music Recommendation System (AMRS), which aims to optimize music recommendations based on the listener's emotional state without relying on real-time feedback, which is often impractical in sensitive environments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the rollout-based world model, which employs a causal transformer architecture trained on historical listening data. This model predicts three key outputs: user engagement, binary ratings, and self-reported emotional states (valence and arousal). The world model functions as both an in-silico simulator for offline policy training and a tool for stress-testing recommendations prior to deployment. The recommendation policy is initialized through behavior cloning and subsequently fine-tuned using Direct Preference Optimization (DPO), which optimizes a multi-objective utility function. The training process is conducted under a strict cold-start protocol, ensuring that the model can generalize effectively to new users.

**Results**  
The authors report that the world model achieves a high fidelity in predicting both behavioral and affective signals, outperforming the behavior-cloned baseline in terms of predicted valence and arousal. Specifically, DPO enhances these predictions while maintaining a similar diversity profile in recommendations, effectively avoiding the distributional collapse often associated with greedy optimization methods. While specific numerical results and effect sizes are not disclosed in the abstract, the qualitative improvements suggest a significant advancement over traditional recommendation approaches.

**Limitations**  
The authors acknowledge several limitations, including the reliance on historical data, which may not fully capture the dynamic nature of user preferences. Additionally, the model's performance in real-world settings remains to be validated, as the current evaluation is based on offline simulations. The cold-start protocol, while rigorous, may not reflect the complexities of user interactions in live environments. Furthermore, the ethical implications of deploying such systems in clinical settings warrant careful consideration, particularly regarding user autonomy and consent.

**Why it matters**  
This work has significant implications for the development of affective recommendation systems, particularly in sensitive applications where traditional online experimentation is not feasible. By demonstrating a methodology that leverages offline data to optimize recommendations based on emotional states, the authors pave the way for future research in ethical AI applications. The approach could be extended to other domains requiring nuanced understanding of user preferences, such as personalized therapy or adaptive learning environments, thereby enhancing user experience and engagement in various contexts.

Authors: Audrey Chan, Aaron Labbé, Jacob Lavoie, Jordan Bannister, Arsène Fansi Tchango, Guillaume Lajoie, Laurent Charlin  
Source: arXiv:2605.28810  
URL: https://arxiv.org/abs/2605.28810v1
