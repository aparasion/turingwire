---
title: "DEI: Diversity in Evolutionary Inference for Quality-Diversity Search"
date: 2026-05-26 15:00:57 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27130v1"
arxiv_id: "2605.27130"
authors: ["John Donaghy", "Shikhar Rastogi"]
slug: dei-diversity-in-evolutionary-inference-for-quality-diversit
summary_word_count: 413
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional homogeneous parallel search methods in Quality-Diversity (QD) optimization, particularly in the context of large language models (LLMs). The authors propose DEI: Diversity in Evolutionary Inference, a distributed QD search framework that leverages heterogeneous LLMs as mutation operators. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
DEI employs a distributed architecture where multiple nodes utilize different LLMs, each contributing unique inductive biases to the search process. The framework extends the Digital Red Queen model by enabling nodes to share local optimal solutions at the end of each iteration, thereby seeding the next generation's population. This approach fosters cross-model adversarial pressure, enhancing robustness beyond what is achievable through intra-model self-play. The authors evaluate DEI using a four-node ensemble comprising GPT-5.4-mini, Claude Sonnet 4.6, GPT-5.2, and Claude Haiku 4.5. The training process is designed to maintain an equal total LLM-call budget across nodes, ensuring a fair comparison with single-node and homogeneous ensemble baselines.

**Results**  
The DEI framework demonstrates significant performance improvements over baseline methods. Specifically, the heterogeneous ensemble achieves a merged-archive QD-Score of 45.90, which is 124% higher than the single-node baseline score of 20.46. Additionally, the heterogeneous ensemble exhibits 28% higher coverage, reaching 80.6% of cells compared to 63.0% for the single-node baseline. The heterogeneous ensemble also outperforms an equally-budgeted homogeneous ensemble across all metrics, including QD-Score, coverage, and held-out solution generality. These results provide empirical evidence that model diversity is a critical factor in enhancing the efficacy of distributed LLM-based QD search.

**Limitations**  
The authors acknowledge that their approach relies on the availability of diverse LLMs, which may not be feasible in all contexts. Additionally, the performance gains observed are contingent on the specific configurations of the models used, and the scalability of the method to larger ensembles or different problem domains remains to be explored. The paper does not address potential computational overhead associated with managing multiple models or the implications of model selection on performance.

**Why it matters**  
The findings from this research have significant implications for the field of evolutionary computation and QD search. By demonstrating that model diversity can drive substantial improvements in performance, this work encourages further exploration of heterogeneous model ensembles in various optimization tasks. It opens avenues for future research into the design of adaptive systems that can dynamically select and integrate diverse models to enhance robustness and solution quality in complex environments.

Authors: John Donaghy, Shikhar Rastogi  
Source: arXiv:2605.27130  
URL: [https://arxiv.org/abs/2605.27130v1](https://arxiv.org/abs/2605.27130v1)
