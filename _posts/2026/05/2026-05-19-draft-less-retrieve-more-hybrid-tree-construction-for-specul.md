---
title: "Draft Less, Retrieve More: Hybrid Tree Construction for Speculative Decoding"
date: 2026-05-19 16:55:48 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20104v1"
arxiv_id: "2605.20104"
authors: ["Yuhao Shen", "Tianyu Liu", "Xinyi Hu", "Quan Kong", "Baolin Zhang", "Jun Dai"]
slug: draft-less-retrieve-more-hybrid-tree-construction-for-specul
summary_word_count: 456
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing speculative decoding (SD) methods in large language model inference, particularly the inefficiencies associated with expansive draft tree construction. While recent approaches have focused on maximizing acceptance rates through larger trees, they suffer from significant VRAM bandwidth and computational overheads, which hinder overall inference speed. The authors propose a novel solution to overcome the tradeoff between pruning and retrieval, which has not been adequately explored in the literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Graft framework, which integrates pruning and retrieval in a synergistic manner. Graft employs a sequential "prune-then-graft" mechanism, where pruning reduces the computational load by eliminating less promising branches, thereby freeing up resources for retrieval. The retrieved tokens are then inserted into the pruned tree to compensate for any loss in coverage, effectively maintaining the quality of the output without incurring additional training costs. The method is designed to be lossless and does not require any retraining of the model. The authors provide a comprehensive evaluation across various deployment scenarios, including short-context and long-context generation, as well as large-scale models.

**Results**  
Graft demonstrates significant performance improvements over existing baselines. In short-context benchmarks, it achieves up to a 5.41× speedup compared to traditional methods. Specifically, on the large-scale Qwen3-235B model, Graft improves average speedup over the EAGLE-3 baseline by up to 21.8%. These results indicate that Graft not only enhances inference speed but also maintains or improves the quality of generated outputs, establishing a new Pareto frontier in the context of speculative decoding.

**Limitations**  
The authors acknowledge that while Graft effectively balances pruning and retrieval, it may not fully exploit the potential of more complex retrieval strategies or larger datasets. Additionally, the method's performance in highly diverse or specialized contexts remains to be evaluated. The paper does not address the potential impact of model size on the effectiveness of Graft, nor does it explore the implications of integrating Graft with other decoding paradigms beyond autoregressive models.

**Why it matters**  
The implications of this work are significant for the field of natural language processing, particularly in optimizing inference speed for large language models. By establishing a new framework that effectively combines pruning and retrieval, Graft opens avenues for further research into hybrid decoding strategies. This could lead to more efficient model architectures and deployment strategies, ultimately enhancing the usability of large language models in real-time applications. The preliminary exploration of applying Graft to DFlash-style block drafting suggests potential for broader applicability, encouraging future investigations into hybrid approaches in various contexts.

Authors: Yuhao Shen, Tianyu Liu, Xinyi Hu, Quan Kong, Baolin Zhang, Jun Dai, Jun Zhang, Shuang Ge et al.  
Source: arXiv:2605.20104  
URL: [https://arxiv.org/abs/2605.20104v1](https://arxiv.org/abs/2605.20104v1)
