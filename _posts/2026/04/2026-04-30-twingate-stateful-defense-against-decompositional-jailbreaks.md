---
title: "TwinGate: Stateful Defense against Decompositional Jailbreaks in Untraceable Traffic via Asymmetric Contrastive Learning"
date: 2026-04-30 13:44:01 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.27861v1"
arxiv_id: "2604.27861"
authors: ["Bowen Sun", "Chaozhuo Li", "Yaodong Yang", "Yiwei Wang", "Chaowei Xiao"]
slug: twingate-stateful-defense-against-decompositional-jailbreaks
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the vulnerability of large language models (LLMs) to decompositional jailbreaks, where adversaries fragment malicious objectives into benign-seeming queries that collectively reconstruct prohibited content. The authors highlight that existing defensive strategies are inadequate in real-world scenarios characterized by untraceable, anonymized traffic and covertly distributed adversarial queries. Notably, the work is presented as a preprint and has not undergone peer review.

**Method**  
The core technical contribution is the TwinGate framework, which employs a stateful dual-encoder architecture. TwinGate utilizes Asymmetric Contrastive Learning (ACL) to cluster semantically disparate yet intent-matched malicious fragments within a shared latent space. This is complemented by a parallel frozen encoder that mitigates false positives due to benign topical overlap. The architecture allows for a single lightweight forward pass per request, enabling the defense mechanism to operate concurrently with the LLM's prefill phase, thus maintaining low latency. The authors constructed a dataset comprising over 3.62 million instructions across 8,600 distinct malicious intents to train and evaluate TwinGate.

**Results**  
TwinGate demonstrates high recall for malicious intent detection while maintaining a low false positive rate. The authors report that TwinGate significantly outperforms both stateful and stateless baselines in terms of throughput and latency. Specific performance metrics include a recall rate exceeding 90% with a false positive rate below 1% on their comprehensive dataset, showcasing robustness against adaptive attacks. The results indicate that TwinGate can effectively handle the complexities of real-world adversarial traffic while minimizing computational overhead.

**Limitations**  
The authors acknowledge that while TwinGate is effective against decompositional jailbreaks, it may not generalize to all forms of adversarial attacks, particularly those that do not conform to the identified malicious intents in their dataset. Additionally, the reliance on a dual-encoder architecture may introduce challenges in scalability and integration with existing LLM infrastructures. The paper does not address potential adversarial strategies that could evolve to bypass the ACL mechanism, nor does it explore the implications of deploying TwinGate in highly dynamic environments with rapidly changing attack vectors.

**Why it matters**  
The implications of this work are significant for the deployment of LLMs in sensitive applications where security is paramount. By providing a robust defense mechanism against decompositional jailbreaks, TwinGate enhances the reliability of LLMs in real-world scenarios, thereby enabling safer interactions in applications such as customer support, content moderation, and automated decision-making systems. This research paves the way for future explorations into stateful defenses and the integration of advanced learning techniques to bolster the security of AI systems against evolving adversarial threats.

Authors: Bowen Sun, Chaozhuo Li, Yaodong Yang, Yiwei Wang, Chaowei Xiao  
Source: arXiv:2604.27861  
URL: https://arxiv.org/abs/2604.27861v1
