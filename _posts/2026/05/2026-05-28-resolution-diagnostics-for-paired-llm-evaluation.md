---
title: "Resolution Diagnostics for Paired LLM Evaluation"
date: 2026-05-28 17:54:09 +0000
category: research
subcategory: evaluation_benchmarks
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30315v1"
arxiv_id: "2605.30315"
authors: ["Anany Kotawala"]
slug: resolution-diagnostics-for-paired-llm-evaluation
summary_word_count: 455
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the evaluation of large language models (LLMs) by highlighting the inadequacy of conventional paired-test resolution in existing benchmarks. Specifically, the authors demonstrate that many pairwise rankings on the Open LLM Leaderboard v1 and MMLU-Pro do not meet the established resolution criteria (alpha, 1-beta) = (0.05, 0.8). They identify that 11 out of 40 comparisons on the Open LLM Leaderboard and 4 out of 9 adjacent-rank pairs in MMLU-Pro are unresolved, indicating a lack of statistical power in these evaluations. This work is crucial for ensuring that LLM comparisons are statistically valid and reliable.

**Method**  
The authors frame the paired LLM evaluation as a hypothesis-testing problem, introducing a novel diagnostic metric: the per-pair resolution ratio \( q = \frac{N}{N^*} \). Here, \( N \) represents the number of observed pairs, while \( N^* \) is the required sample size for adequate resolution. They propose a sharp small-effect expansion with a second-order constant, revealing that the commonly used unpaired Cohen's h-plus-(1-rho) shortcut underestimates \( N^* \) by approximately a factor of two in scenarios involving close comparisons. This discrepancy is inherited by three out of five popular statistical calculators (Cohen 1988, G*Power, R pwr) when users incorrectly adjust their outputs by (1-rho). The authors also discuss the persistence of unresolved pairs under multiplicity correction and sequential testing frameworks.

**Results**  
The findings indicate that the resolution of pairwise comparisons is significantly lower than expected. Specifically, the MMLU-Pro dataset shows that the unresolved pair count increases to 6 out of 9 when considering real subject-level clustering, and remains at 5-6 out of 9 in 99.9% of bootstrap resamples. This highlights a critical issue in the statistical robustness of LLM evaluations, as many comparisons fail to achieve the desired power levels, thereby undermining the validity of the rankings presented in these leaderboards.

**Limitations**  
The authors acknowledge that their analysis is limited to the datasets examined and may not generalize to all LLM evaluations. They do not address potential biases in the selection of models or the specific characteristics of the datasets used. Additionally, the reliance on conventional statistical methods may overlook other factors influencing model performance that are not captured in pairwise comparisons.

**Why it matters**  
This work has significant implications for the field of LLM evaluation, as it underscores the necessity for robust statistical methodologies in comparative studies. By revealing the inadequacies in current evaluation practices, the authors advocate for a reevaluation of how LLMs are benchmarked, which could lead to more reliable assessments of model performance. This could ultimately influence the development of future LLMs and the methodologies employed in their evaluation, fostering a more rigorous and scientifically sound approach to model comparison.

Authors: Anany Kotawala  
Source: arXiv:2605.30315  
URL: https://arxiv.org/abs/2605.30315v1
