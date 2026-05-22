---
title: "FAME: Failure-Aware Mixture-of-Experts for Message-Level Log Anomaly Detection"
date: 2026-05-21 17:34:53 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22779v1"
arxiv_id: "2605.22779"
authors: ["Huanchi Wang", "Zihang Huang", "Yifang Tian", "Kristina Dzeparoska", "Hans-Arno Jacobsen", "Alberto Leon-Garcia"]
slug: fame-failure-aware-mixture-of-experts-for-message-level-log-
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in message-level log anomaly detection, which is often overlooked in favor of session or window-level approaches that aggregate log lines. Current methods fail to pinpoint specific anomalous messages, leading to inefficiencies as operators must sift through numerous routine logs per alert. The authors highlight the challenges of message-level detection, including the ambiguity of event templates that can represent both normal and anomalous messages, the complexity of heterogeneous subsystems, and the impracticality of large-scale line-level labeling. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose FAME (Failure-Aware Mixture-of-Experts), a novel framework that leverages a mixture-of-experts architecture to achieve label-efficient message-level anomaly detection. FAME employs a large language model (LLM) in an offline capacity to annotate a limited number of log lines (K) per template, generating binary normal/anomaly indicators and representative examples. The LLM is utilized to partition templates into distinct failure domains, which are subsequently validated through a certification step. The framework consists of a lightweight router and domain-specific experts that operate on-premise, producing both anomaly predictions and failure-domain labels. The training process is designed to minimize the annotation effort while maximizing detection accuracy.

**Results**  
FAME demonstrates impressive performance on benchmark datasets. On the BGL dataset, it achieves an F1 score of 98.16 with K set to 100, which represents a 76-fold reduction in annotation effort compared to traditional methods. Additionally, it successfully detects 86.3% of anomalies from previously unseen EventIDs. On the Thunderbird dataset, FAME reaches an F1 score of 99.95, achieving perfect recall. These results indicate that FAME not only enhances detection granularity but also significantly reduces the labeling burden.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a pre-trained LLM, which may not generalize well across all log types or domains. The method's performance is contingent on the quality of the initial K labeled lines, which could introduce bias if not representative. Furthermore, the certification step, while necessary for validating the LLM's partitioning, may introduce additional computational overhead. The authors do not address potential scalability issues when deploying the framework in extremely high-volume log environments or the implications of model drift over time.

**Why it matters**  
FAME's approach to message-level anomaly detection has significant implications for operational efficiency in production systems. By enabling precise identification of anomalous log messages, it reduces the cognitive load on operators and enhances incident response times. The framework's ability to operate with minimal labeled data opens avenues for further research into semi-supervised and unsupervised learning techniques in log analysis. Additionally, the integration of LLMs in a mixture-of-experts setup could inspire similar architectures in other domains requiring fine-grained anomaly detection.

Authors: Huanchi Wang, Zihang Huang, Yifang Tian, Kristina Dzeparoska, Hans-Arno Jacobsen, Alberto Leon-Garcia  
Source: arXiv:2605.22779  
URL: https://arxiv.org/abs/2605.22779v1
