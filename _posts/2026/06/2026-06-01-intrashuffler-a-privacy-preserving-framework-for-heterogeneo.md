---
title: "IntraShuffler: A Privacy Preserving Framework for Heterogeneous DP Federated Learning"
date: 2026-06-01 17:54:10 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02563v1"
arxiv_id: "2606.02563"
authors: ["Farhin Farhad Riya", "Olivera Kotevska", "Jinyuan Stella Sun"]
slug: intrashuffler-a-privacy-preserving-framework-for-heterogeneo
summary_word_count: 393
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces IntraShuffler, a middleware framework that enhances privacy in heterogeneous differential privacy federated learning by mitigating inference risks."
---

**Problem**  
The paper addresses the gap in privacy protection within heterogeneous differential privacy (HDP) federated learning (FL) systems, particularly the vulnerability of gradient updates to privacy inference attacks. Existing HDP-FL systems utilize $\varepsilon$-aware server aggregation to optimize model utility, but this approach inadvertently exposes structural patterns in non-IID data, allowing an honest-but-curious server to infer sensitive client information. The authors highlight that while the Shuffle-Model has been proposed as a defense mechanism, it is incompatible with $\varepsilon$-aware aggregation. This work is a preprint and has not undergone peer review.

**Method**  
The authors propose IntraShuffler, a middleware framework that introduces a novel privacy-aware shuffling mechanism. This mechanism groups clients into privacy-compatible buckets and performs parameter-level shuffling within each bucket. This approach disrupts the persistent gradient structure that can be exploited for inference while still allowing for $\varepsilon$-aware aggregation. The framework is designed to maintain model utility while enhancing privacy. The experiments were conducted on four datasets, although specific details regarding the datasets, training compute, and exact architecture used for the FL system are not disclosed.

**Results**  
IntraShuffler demonstrates significant improvements in privacy protection metrics. The framework reduces gradient recoverability by over 60% compared to baseline methods. Additionally, it decreases surrogate inference accuracy from 0.78 to 0.33, indicating a substantial reduction in the server's ability to infer client attributes. Importantly, the model utility remains comparable across various FL aggregation rules, suggesting that the privacy enhancements do not come at the cost of performance.

**Limitations**  
The authors acknowledge that while IntraShuffler effectively mitigates privacy risks, it may introduce additional computational overhead due to the shuffling process. Furthermore, the framework's performance may vary depending on the specific characteristics of the datasets used, which could limit its generalizability. The paper does not explore the scalability of IntraShuffler in large-scale federated learning scenarios or its integration with other privacy-preserving techniques.

**Why it matters**  
IntraShuffler represents a significant advancement in the field of privacy-preserving federated learning, particularly in contexts where heterogeneous data and privacy budgets are prevalent. By effectively addressing the vulnerabilities associated with $\varepsilon$-aware aggregation, this framework enhances the security of client data against inference attacks, which is crucial for real-world applications in sensitive domains such as healthcare and finance. The implications of this work extend to future research on federated learning privacy, as it opens avenues for developing more robust privacy-preserving mechanisms. This work is available on [arXiv](https://arxiv.org/abs/2606.02563v1).
