---
title: "Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics"
date: 2026-06-02 17:58:02 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.03982v1"
arxiv_id: "2606.03982"
authors: ["Mutsumi Sasaki", "Go kamoda", "Ryosuke Takahashi", "Kosuke Sato", "Kentaro Inui", "Keisuke Sakaguchi"]
slug: language-models-compare-quantities-using-number-specific-and
summary_word_count: 459
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper investigates how language models compare quantities with measurement units, revealing systematic errors and heuristic-based decision-making."
---

**Problem**  
This work addresses the gap in understanding how language models (LMs) handle comparisons of quantities with measurement units, such as centimeters and meters. Despite the growing use of LMs in quantitative reasoning tasks, there is limited literature on their ability to accurately compare values across different unit systems. The authors highlight that existing models may struggle with precision near comparison boundaries, where small numerical differences can lead to incorrect outputs. This study is a preprint and has not undergone peer review.

**Method**  
The authors conducted a series of controlled experiments to evaluate LMs' performance in comparing quantities with various measurement units. They employed linear surrogate models to analyze the decision-making process of LMs, focusing on two primary cues: numerical-difference and unit-scale-difference. The experiments involved manipulating these cues to observe how they influenced the LMs' outputs. The training data consisted of a diverse set of quantity comparisons across multiple unit systems, although specific details on the dataset size and training compute were not disclosed. The authors also performed causal interventions on subspaces aligned with the identified variables to assess the robustness of the LMs' heuristic-based reasoning.

**Results**  
The findings indicate that LMs exhibit systematic errors when comparing quantities, particularly near the comparison boundary. The accuracy of the models significantly degrades in these scenarios, suggesting that LMs rely on a bag of heuristics rather than a unified conversion to a shared scale. The study quantitatively demonstrates that linear surrogate models can predict LM preferences with a high degree of accuracy based on the identified cues. While specific numerical results and baseline comparisons were not detailed in the abstract, the implications of the findings suggest a clear trend in LM performance that warrants further investigation.

**Limitations**  
The authors acknowledge that their study is limited by the controlled nature of the experiments, which may not fully capture the complexities of real-world quantity comparisons. Additionally, the reliance on linear surrogate models may oversimplify the decision-making processes of LMs. The lack of detailed information regarding the dataset and training compute also limits the reproducibility of the results. Furthermore, the study does not explore the impact of different LM architectures or training paradigms on the observed behaviors.

**Why it matters**  
This research has significant implications for the development of LMs in quantitative reasoning tasks, particularly in applications requiring precise comparisons of measurements. Understanding the heuristic-based decision-making process of LMs can inform future model designs and training strategies to enhance their accuracy in handling quantities. The findings suggest that improving LMs' ability to convert and compare units could lead to better performance in various domains, including scientific computing and data analysis. This work contributes to the ongoing discourse on the limitations of LMs in reasoning tasks, as discussed in related literature, and is available on [arXiv](https://arxiv.org/abs/2606.03982v1).
