---
title: "Enabling AI-Native Mobility in 6G: A Real-World Dataset for Handover, Beam Management, and Timing Advance"
date: 2026-05-12 17:43:49 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12453v1"
arxiv_id: "2605.12453"
authors: ["Mannam Veera Narayana", "Rohit Singh", "Deepa M. R", "Radha Krishna Ganti"]
slug: enabling-ai-native-mobility-in-6g-a-real-world-dataset-for-h
summary_word_count: 402
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in realistic datasets for AI/ML applications in 5G and upcoming 6G networks, particularly concerning user equipment (UE) mobility. Existing datasets are predominantly simulated and fail to capture the complexities of real-world scenarios, leading to inefficiencies in AI/ML beam management and mobility procedures. The authors present a preprint work that provides a comprehensive dataset collected from a commercially deployed network, focusing on handover (HO) scenarios across various mobility modes and speeds.

**Method**  
The dataset was collected from a live network environment, encompassing multiple mobility scenarios: pedestrian, bike, car, bus, and train. The authors detail the experimental setup, data acquisition, and extraction processes, emphasizing the inclusion of timing advance (TA) measurements at critical signaling events such as Random Access Channel (RACH) triggers, MAC Control Element (MAC CE) transmissions, and Physical Downlink Control Channel (PDCCH) grants. This dataset aims to facilitate the training and evaluation of AI/ML models, particularly for TA prediction, which is crucial for minimizing HO interruption times and ensuring continuous throughput during HO execution.

**Results**  
While specific quantitative results are not provided in the abstract, the dataset is expected to enhance the performance of AI/ML models in real-world applications, particularly in reducing HO interruption times. The authors suggest that the dataset can be utilized to benchmark various AI/ML models against traditional methods, although exact performance metrics and comparisons to named baselines are not disclosed in the provided text.

**Limitations**  
The authors acknowledge that the dataset is limited to specific mobility scenarios and may not encompass all potential use cases in diverse environments. Additionally, the dataset's applicability may vary based on the deployment characteristics of different network operators. The exploratory analysis is preliminary, and further validation of the dataset's utility in training AI/ML models is necessary. The lack of detailed performance metrics in the results section is also a notable limitation.

**Why it matters**  
This work is significant as it provides a foundational dataset that can bridge the gap between simulated environments and real-world applications in 5G and 6G networks. By enabling more accurate training of AI/ML models, the dataset can lead to improved handover management, reduced interruption times, and enhanced user experience in high-speed mobility scenarios. The implications extend to the development of more robust AI-driven solutions for network management, paving the way for future advancements in mobile communication technologies.

Authors: Mannam Veera Narayana, Rohit Singh, Deepa M. R, Radha Krishna Ganti  
Source: arXiv:2605.12453  
URL: [https://arxiv.org/abs/2605.12453v1](https://arxiv.org/abs/2605.12453v1)
