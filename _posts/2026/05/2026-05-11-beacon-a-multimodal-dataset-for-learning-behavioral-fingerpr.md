---
title: "BEACON: A Multimodal Dataset for Learning Behavioral Fingerprints from Gameplay Data"
date: 2026-05-11 17:17:02 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10867v1"
arxiv_id: "2605.10867"
authors: ["Ishpuneet Singh", "Gursmeep Kaur", "Uday Pratap Singh Atwal", "Guramrit Singh", "Gurjot Singh", "Maninder Singh"]
slug: beacon-a-multimodal-dataset-for-learning-behavioral-fingerpr
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of large-scale, multimodal datasets for continuous authentication in high-stakes digital environments, particularly in gaming contexts. Existing datasets are often limited by their small size, unimodal data collection, or insufficient synchronization with environmental context. The authors present BEACON (Behavioral Engine for Authentication & Continuous Monitoring), a comprehensive dataset designed to capture fine-grained behavioral signals during competitive gameplay in the tactical shooter game *Valorant*. This work is a preprint and has not yet undergone peer review.

**Method**  
BEACON comprises approximately 430 GB of synchronized multimodal data collected from 79 sessions involving 28 distinct players, totaling around 102.51 hours of active gameplay. The dataset includes high-frequency mouse dynamics, keystroke events, network packet captures, screen recordings, hardware metadata, and in-game configuration context. The authors utilize a combination of high-precision motor skills and cognitive load inherent in tactical shooters to create a robust environment for testing behavioral biometrics. The dataset is designed to facilitate research in continuous authentication, behavioral profiling, user drift, and multimodal representation learning. The authors provide the dataset and associated code on Hugging Face and GitHub, promoting reproducibility in future research.

**Results**  
While specific quantitative results comparing BEACON to existing benchmarks are not provided in the abstract, the dataset's design aims to enable significant advancements in behavioral fingerprinting and security models. The authors emphasize the dataset's potential to improve the robustness of continuous authentication systems by leveraging the complexity of gameplay data. The release of BEACON is expected to set a new standard for evaluating behavioral biometrics in high-fidelity esports settings.

**Limitations**  
The authors acknowledge that the dataset is limited to a single game (*Valorant*), which may restrict generalizability to other gaming contexts or applications outside of esports. Additionally, the dataset's reliance on a specific player population may introduce biases related to skill level and gameplay style. The authors do not discuss potential privacy concerns associated with collecting and sharing gameplay data, which could be a significant consideration in real-world applications of continuous authentication.

**Why it matters**  
The introduction of BEACON has substantial implications for the field of behavioral biometrics and continuous authentication. By providing a large-scale, multimodal dataset that captures the intricacies of player behavior in a competitive gaming environment, this work lays the groundwork for developing more effective and resilient authentication systems. The dataset's focus on high cognitive and motor demands presents a rigorous testing ground for future research, potentially leading to advancements in user profiling, adaptive security measures, and the understanding of user drift in behavioral models. The release of BEACON encourages further exploration of multimodal representation learning, which could enhance the performance of machine learning models in various applications beyond gaming.

Authors: Ishpuneet Singh, Gursmeep Kaur, Uday Pratap Singh Atwal, Guramrit Singh, Gurjot Singh, Maninder Singh  
Source: arXiv:2605.10867  
URL: [https://arxiv.org/abs/2605.10867v1](https://arxiv.org/abs/2605.10867v1)
