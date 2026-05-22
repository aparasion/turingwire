---
title: "LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems"
date: 2026-05-21 17:42:12 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22786v1"
arxiv_id: "2605.22786"
authors: ["Sadia Asif", "Mohammad Mohammadi Amiri", "Momin Abbas", "Prasanna Sattigeri", "Karthikeyan Natesan Ramamurthy"]
slug: lcguard-latent-communication-guard-for-safe-kv-sharing-in-mu
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in safe communication protocols for multi-agent systems utilizing large language models (LLMs), specifically focusing on the latent communication through transformer key-value (KV) caches. While existing systems leverage natural language for agent coordination, the use of KV caches introduces risks of sensitive information leakage due to their ability to encode contextual inputs and agent-specific data. The authors propose LCGuard, a framework designed to mitigate these risks by ensuring that sensitive information does not propagate through KV caches without explicit disclosure. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
LCGuard operates by treating shared KV caches as latent working memory and employs representation-level transformations to secure the information before it is shared among agents. The core technical contribution is the formalization of sensitive information leakage through a reconstruction-based approach. An adversarial decoder is trained to reconstruct sensitive inputs from shared cache artifacts, and the LCGuard framework learns transformations that minimize the reconstructable information while preserving task-relevant semantics. The training involves an adversarial setup where the adversary aims to maximize reconstruction accuracy, while LCGuard aims to minimize it. The paper does not disclose specific details about the architecture of the models used or the compute resources required for training.

**Results**  
Empirical evaluations demonstrate that LCGuard significantly reduces the rates of sensitive information reconstruction and adversarial attack success compared to standard KV-sharing baselines. The authors report consistent performance improvements across multiple model families and multi-agent benchmarks, although specific numerical results and effect sizes are not detailed in the summary provided. The results indicate that LCGuard maintains competitive task performance while enhancing the security of KV-based communication.

**Limitations**  
The authors acknowledge that while LCGuard effectively reduces sensitive information leakage, the framework's performance may vary depending on the complexity of the tasks and the specific configurations of the multi-agent systems. They do not address potential scalability issues when applied to larger systems or the computational overhead introduced by the adversarial training process. Additionally, the reliance on adversarial training may limit the generalizability of the learned transformations to unseen tasks or environments.

**Why it matters**  
The implications of this work are significant for the development of secure multi-agent systems that utilize LLMs. By providing a framework for safe latent communication, LCGuard enables more efficient coordination among agents while safeguarding sensitive information. This advancement is crucial for applications in domains such as collaborative robotics, automated decision-making, and any scenario where agents must share information without compromising privacy. The findings could inform future research on secure communication protocols and the design of robust multi-agent systems.

Authors: Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Prasanna Sattigeri, Karthikeyan Natesan Ramamurthy  
Source: arXiv:2605.22786  
URL: [https://arxiv.org/abs/2605.22786v1](https://arxiv.org/abs/2605.22786v1)
