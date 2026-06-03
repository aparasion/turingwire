---
title: "Dynamic Short Convolutions Improve Transformers"
date: 2026-06-02 16:07:55 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.03825v1"
arxiv_id: "2606.03825"
authors: ["Oliver Sieberling", "Bharat Runwal", "Rameswar Panda", "Yoon Kim"]
slug: dynamic-short-convolutions-improve-transformers
summary_word_count: 399
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces dynamic short convolutions as a novel primitive to enhance Transformer architectures, demonstrating significant performance improvements."
---

**Problem**  
This work addresses the limitations of static short convolutions in Transformer architectures, which have become the standard for large language models. The authors identify a gap in the expressivity of convolutional layers when applied statically, particularly in the context of associative recall tasks. The paper is a preprint and has not undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
The core contribution of this paper is the introduction of dynamic short convolutions, which utilize input-dependent filters to enhance the locality bias of traditional convolutions while increasing their expressivity. The authors apply these dynamic convolutions to the key, query, and value representations within the Transformer architecture. They also explore the integration of dynamic convolutions after every linear layer. The experiments are conducted on language models ranging from 150M to 2B parameters, with custom Triton kernels developed to facilitate efficient training. The paper provides a detailed analysis of the compute advantages, reporting a 1.33× improvement over compute-matched Transformers and a 1.60× advantage when dynamic convolutions are applied after every linear layer.

**Results**  
The experimental results demonstrate that dynamic short convolutions consistently outperform both standard Transformers and those augmented with static short convolutions across various language modeling tasks. The authors report significant improvements in performance metrics on challenging associative recall tasks, although specific numerical results are not disclosed in the summary. The findings suggest that dynamic convolutions also enhance the performance of linear RNNs (Mamba-2/Gated DeltaNet) and mixture-of-experts architectures, indicating a broad applicability of the proposed method.

**Limitations**  
The authors acknowledge that the implementation of dynamic convolutions introduces additional complexity in model design and training. They do not discuss potential limitations related to the scalability of the custom Triton kernels or the generalizability of the results across different datasets and tasks. Furthermore, the reliance on specific hardware for efficient training may limit accessibility for some researchers.

**Why it matters**  
The introduction of dynamic short convolutions presents a promising avenue for enhancing the expressivity and efficiency of Transformer-based models, which are pivotal in natural language processing. The findings suggest that this new primitive could lead to more scalable and hardware-efficient architectures, potentially influencing future research in model design and optimization. The implications of this work are significant for advancing the state-of-the-art in language modeling, as highlighted in the paper's findings, and further exploration of dynamic convolutions could yield substantial benefits in various applications, as published in [arXiv](https://arxiv.org/abs/2606.03825v1).
