---
title: "Self-Policy Distillation via Capability-Selective Subspace Projection"
date: 2026-05-21 16:18:41 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22675v1"
arxiv_id: "2605.22675"
authors: ["Guangya Hao", "Yitong Shang", "Yunbo Long", "Zhuokai Zhao", "Hanxue Liang"]
slug: self-policy-distillation-via-capability-selective-subspace-p
summary_word_count: 401
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing self-distillation methods for large language models (LLMs), which either depend on external signals for output curation or train on unfiltered raw outputs. The former is costly and often unavailable for cutting-edge models, while the latter is domain-specific and lacks generalizability. Additionally, both approaches fail to disentangle task-relevant capabilities from extraneous factors such as stylistic patterns and model-specific errors, which can dilute the training signal. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Self-Policy Distillation (SPD), a novel approach that enables capability-selective self-distillation without external signals. SPD operates by first extracting a low-rank capability subspace from the model's gradients on correctness-defining tokens. During the self-generation phase, key-value (KV) activations are projected into this subspace, effectively filtering out irrelevant information. The model is then fine-tuned on the resulting outputs using a standard next-token prediction loss. This method allows for a more focused improvement on specific capabilities, enhancing the model's performance across various tasks.

**Results**  
The experimental results demonstrate that SPD achieves significant performance improvements over existing self-distillation methods and pre-trained baselines. Specifically, SPD shows up to a 13% enhancement compared to state-of-the-art self-distillation techniques that do not utilize external signals. Furthermore, it outperforms pre-trained models by up to 16%. Notably, SPD exhibits superior generalizability, achieving a 15% performance increase in out-of-domain generalization scenarios, indicating its robustness across diverse tasks.

**Limitations**  
The authors acknowledge that while SPD improves capability selectivity, it may still be sensitive to the quality of the initial model and the specific tasks chosen for evaluation. Additionally, the reliance on correctness-defining tokens may limit the applicability of SPD to tasks where such tokens are not clearly defined. The paper does not address potential computational overhead introduced by the low-rank projection process, which could impact training efficiency.

**Why it matters**  
The implications of this work are significant for the field of self-distillation in LLMs. By providing a method that enhances capability selectivity without external signals, SPD opens avenues for more efficient training of LLMs in various applications, including code generation, mathematical reasoning, and question answering. The demonstrated improvements in generalizability suggest that SPD could be a valuable tool for developing models that perform well across a wider range of tasks and domains, potentially leading to more robust AI systems.

Authors: Guangya Hao, Yitong Shang, Yunbo Long, Zhuokai Zhao, Hanxue Liang  
Source: arXiv:2605.22675  
URL: [https://arxiv.org/abs/2605.22675v1](https://arxiv.org/abs/2605.22675v1)
