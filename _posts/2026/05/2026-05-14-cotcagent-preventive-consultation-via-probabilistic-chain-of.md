---
title: "COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion"
date: 2026-05-14 16:17:35 +0000
category: research
subcategory: agents_robotics
company: "Baichuan"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15016v1"
arxiv_id: "2605.15016"
authors: ["Zihan Deng", "Xiaozhen Zhong", "Chuanzhi Xu"]
slug: cotcagent-preventive-consultation-via-probabilistic-chain-of
summary_word_count: 403
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses significant gaps in the capability of large language models (LLMs) to reason with longitudinal electronic health records (EHRs). Current models struggle with fine-grained statistical reasoning, often leading to hallucinations of clinical trends and metrics when quantitative evidence is implied in text. Additionally, the non-uniformity of time series data and the scarcity of labeled instances in longitudinal EHRs hinder the models' ability to capture long-range temporal dependencies, which is crucial for reliable clinical reasoning.

**Method**  
The authors propose the Probabilistic Chain-of-Thought Completion Agent (COTCAgent), a hierarchical reasoning framework specifically designed for longitudinal EHR analysis. COTCAgent comprises three core modules: 

1. **Temporal-Statistics Adapter (TSA)**: This module translates analytical plans into executable code, facilitating standardized trend outputs.
2. **Chain-of-Thought Completion (COTC)**: This layer utilizes a symptom-trend-disease knowledge base, applying weighted scoring to assess disease risk based on the input data.
3. **Bounded Completion Module**: This component gathers structured evidence through standardized inquiries and iterative scoring constraints, ensuring rigorous reasoning.

By decoupling statistical computation, feature matching, and language generation, COTCAgent minimizes reliance on complex multi-modal inputs, thus enabling efficient analysis of longitudinal records with reduced computational overhead. The model is powered by Baichuan-M2, a large language model optimized for this task.

**Results**  
COTCAgent achieves a Top-1 accuracy of 90.47% on a self-constructed dataset and 70.41% on the HealthBench benchmark. These results demonstrate a significant performance improvement over existing medical agents and mainstream LLMs, indicating the effectiveness of the proposed framework in clinical decision support tasks.

**Limitations**  
The authors acknowledge that the model's performance is contingent on the quality and representativeness of the training data, which may not encompass all clinical scenarios. Additionally, the reliance on a specific knowledge base may limit generalizability across diverse healthcare settings. The paper does not address potential biases in the training data or the interpretability of the model's outputs, which are critical in clinical applications.

**Why it matters**  
COTCAgent's framework has substantial implications for the development of intelligent clinical decision support systems. By enhancing the ability of LLMs to reason with longitudinal EHRs, this work paves the way for more accurate and reliable clinical diagnostics. The decoupling of statistical reasoning from language generation could inspire future research into modular architectures that improve interpretability and robustness in healthcare applications. Furthermore, the findings may influence the design of future EHR systems and the integration of AI in clinical workflows.

Authors: Zihan Deng, Xiaozhen Zhong, Chuanzhi Xu  
Source: arXiv:2605.15016  
URL: [https://arxiv.org/abs/2605.15016v1](https://arxiv.org/abs/2605.15016v1)
