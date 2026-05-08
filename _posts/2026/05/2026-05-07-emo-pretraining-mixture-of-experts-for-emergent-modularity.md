---
title: "EMO: Pretraining Mixture of Experts for Emergent Modularity"
date: 2026-05-07 17:59:20 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06663v1"
arxiv_id: "2605.06663"
authors: ["Ryan Wang", "Akshita Bhagia", "Sewon Min"]
slug: emo-pretraining-mixture-of-experts-for-emergent-modularity
summary_word_count: 480
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional large language models (LLMs) that operate as monolithic systems, which necessitate the use of the entire model even for tasks requiring only specific capabilities. The authors highlight the inefficiencies of existing Mixture-of-Experts (MoE) architectures, which suffer from performance degradation when restricting inference to a subset of experts for particular domains. This issue is particularly pronounced in memory-constrained environments, especially as model sizes increase. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose EMO, a novel MoE architecture that emphasizes emergent modularity, allowing for the independent use and composition of expert subsets without the need for human-defined priors. The core technical contribution involves a mechanism that encourages tokens from similar domains to utilize similar experts. EMO achieves this by constraining tokens within a document to select experts from a shared pool, while permitting different documents to access distinct pools. This approach facilitates the emergence of coherent expert groupings during pretraining, which is conducted on a dataset of 1 trillion tokens. The model architecture consists of 1 billion active parameters and 14 billion total parameters. The training process leverages document boundaries to guide expert selection, resulting in a more efficient and modular deployment of large models.

**Results**  
EMO demonstrates competitive performance against standard MoE architectures. When retaining only 25% of experts, EMO incurs a mere 1% absolute drop in performance, and with 12.5% of experts, the drop is only 3%. In contrast, traditional MoEs experience significant performance degradation under similar conditions. The authors also report that expert subsets in EMO exhibit specialization at a semantic level, effectively handling domains such as mathematics and programming, as opposed to the low-level syntactic specialization typically observed in standard MoEs. These results suggest that EMO not only maintains performance but also enhances the modularity and efficiency of expert utilization.

**Limitations**  
The authors acknowledge that while EMO shows promise, it is still constrained by the inherent challenges of MoE architectures, such as the potential for overfitting and the need for careful tuning of expert selection mechanisms. Additionally, the reliance on document boundaries for expert grouping may limit the model's applicability in scenarios where such boundaries are not clearly defined. The paper does not address the scalability of EMO beyond the pretraining phase or its performance in real-world applications.

**Why it matters**  
The implications of this work are significant for the future of large-scale language models. By enabling modular and memory-efficient deployment of sparse models, EMO opens avenues for more flexible architectures that can adapt to specific tasks without the overhead of full model inference. This modularity could lead to advancements in composable AI systems, where different expert subsets can be dynamically selected based on the task at hand, ultimately enhancing the efficiency and effectiveness of LLMs in various applications.

Authors: Ryan Wang, Akshita Bhagia, Sewon Min  
Source: arXiv:2605.06663  
URL: https://arxiv.org/abs/2605.06663v1
