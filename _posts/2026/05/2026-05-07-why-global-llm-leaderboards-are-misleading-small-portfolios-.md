---
title: "Why Global LLM Leaderboards Are Misleading: Small Portfolios for Heterogeneous Supervised ML"
date: 2026-05-07 17:57:58 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06656v1"
arxiv_id: "2605.06656"
authors: ["Jai Moondra", "Ayela Chughtai", "Bhargavi Lanka", "Swati Gupta"]
slug: why-global-llm-leaderboards-are-misleading-small-portfolios-
summary_word_count: 501
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacies of current global leaderboards for large language models (LLMs) that rank models based on pairwise human feedback across diverse tasks and languages. The authors highlight that existing rankings, derived from approximately 89,000 comparisons across 116 languages and 52 LLMs, are misleading due to significant heterogeneity in user opinions. They demonstrate that nearly two-thirds of decisive votes cancel out, and even the top 50 models exhibit statistically indistinguishable performance, with pairwise win probabilities peaking at 0.53. This indicates a critical gap in understanding how language, task, and temporal factors influence model performance evaluations.

**Method**  
The authors propose a novel framework termed $(λ, ν)$-portfolios, which consists of small sets of models designed to minimize prediction error (at most $λ$) while covering a substantial fraction ($ν$) of user votes. This approach is formulated as a variant of the set cover problem, leveraging the VC dimension of the underlying set system to provide theoretical guarantees. The authors demonstrate that their algorithms can distill the Arena data into just five distinct Bradley-Terry rankings that cover over 96% of votes, significantly outperforming the global ranking's 21% coverage. Additionally, they construct a portfolio of six LLMs that captures twice as many votes as the top six models from the global ranking. The methodology is further extended to a classification task on the COMPAS dataset, utilizing fairness-regularized models to identify data blind spots.

**Results**  
The $(λ, ν)$-portfolio framework achieves a remarkable improvement in vote coverage, with five distinct rankings covering over 96% of votes compared to the global ranking's 21%. The constructed portfolio of six LLMs demonstrates a twofold increase in vote coverage relative to the top six models from the global ranking. The authors provide empirical evidence that grouping models by language significantly enhances ranking consistency, yielding two orders of magnitude higher spread in ELO scores. This indicates that the apparent global noise in model performance is actually a blend of coherent but conflicting subpopulations, which the proposed method effectively addresses.

**Limitations**  
The authors acknowledge that their approach may not generalize to all tasks or datasets beyond those analyzed, particularly in domains with less structured heterogeneity. They do not address potential computational overhead associated with maintaining multiple model portfolios or the implications of model selection bias. Additionally, the reliance on human feedback for ranking may introduce subjective biases that are not fully accounted for in their analysis.

**Why it matters**  
This work has significant implications for the evaluation and deployment of LLMs in real-world applications. By highlighting the limitations of global rankings and introducing a more nuanced approach to model selection, the authors pave the way for more effective and equitable use of LLMs across diverse user populations. The $(λ, ν)$-portfolio framework not only enhances model performance evaluation but also serves as a tool for identifying and mitigating blind spots in data, which is crucial for policymakers and practitioners aiming to ensure fairness and robustness in machine learning systems.

Authors: Jai Moondra, Ayela Chughtai, Bhargavi Lanka, Swati Gupta  
Source: arXiv:2605.06656  
URL: https://arxiv.org/abs/2605.06656v1
