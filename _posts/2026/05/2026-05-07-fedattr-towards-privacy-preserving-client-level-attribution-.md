---
title: "FedAttr: Towards Privacy-preserving Client-Level Attribution in Federated LLM Fine-tuning"
date: 2026-05-07 17:21:02 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06596v1"
arxiv_id: "2605.06596"
authors: ["Su Zhang", "Junfeng Guo", "Heng Huang"]
slug: fedattr-towards-privacy-preserving-client-level-attribution-
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in client-level attribution methods for federated learning (FL) in the context of fine-tuning large language models (LLMs) on private data. While watermark detection methods have been effective in centralized settings, their application in FL is underexplored. The challenge lies in maintaining privacy through secure aggregation (SA), which complicates the identification of clients that have trained on watermarked documents. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose FedAttr, a novel client-level attribution protocol designed for federated LLM fine-tuning. FedAttr operates through a three-step process: 
1. **Estimation of Client Updates**: It estimates each client's update by differencing two SA queries, allowing for the extraction of meaningful information while preserving privacy.
2. **Watermark Detection**: The estimated updates are scored using a watermark detector via differential scoring, which assesses the likelihood of each client having trained on watermarked data.
3. **Score Aggregation**: Scores across multiple rounds are combined using the Stouffer method, which aggregates p-values to enhance detection reliability.

The theoretical foundation of FedAttr demonstrates that it produces an unbiased estimator of each client's update with a bounded mutual information leakage of \(O(d^*/N)\) per round, where \(d^*\) is the dimensionality of the updates and \(N\) is the number of clients.

**Results**  
FedAttr achieves a 100% true positive rate (TPR) and a 0% false positive rate (FPR) in identifying clients that trained on watermarked data. It outperforms all baseline methods by at least 44.4% in TPR and 19.1% in FPR. The protocol incurs only a 6.3% overhead relative to the total federated learning training time, indicating its efficiency. The authors conducted ablation studies that confirm the robustness of FedAttr against variations in protocol parameters and configurations.

**Limitations**  
The authors acknowledge that while FedAttr effectively maintains privacy and achieves high attribution accuracy, the method's performance may be influenced by the specific characteristics of the watermarking technique used. Additionally, the reliance on SA may introduce limitations in scenarios with highly heterogeneous client data distributions. The paper does not address potential scalability issues when applied to a significantly larger number of clients or more complex watermarking schemes.

**Why it matters**  
FedAttr represents a significant advancement in the intersection of federated learning and watermark detection, providing a practical solution for privacy-preserving client-level attribution. This work has implications for the broader field of federated learning, particularly in applications where data ownership and model integrity are critical. By enabling effective attribution without compromising client privacy, FedAttr could facilitate more secure collaborative model training and enhance trust in federated systems.

Authors: Su Zhang, Junfeng Guo, Heng Huang  
Source: arXiv:2605.06596  
URL: [https://arxiv.org/abs/2605.06596v1](https://arxiv.org/abs/2605.06596v1)
