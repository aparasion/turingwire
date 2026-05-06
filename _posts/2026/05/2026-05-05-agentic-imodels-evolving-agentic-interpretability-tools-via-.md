---
title: "Agentic-imodels: Evolving agentic interpretability tools via autoresearch"
date: 2026-05-05 14:35:47 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03808v1"
arxiv_id: "2605.03808"
authors: ["Chandan Singh", "Yan Shuo Tan", "Weijia Xu", "Zelalem Gero", "Weiwei Yang", "Michel Galley"]
slug: agentic-imodels-evolving-agentic-interpretability-tools-via-
summary_word_count: 415
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the capability of agentic data science (ADS) systems, which are increasingly tasked with autonomous data analysis and interpretation. Current ADS systems rely on statistical tools that prioritize human interpretability, which is inadequate for agentic contexts where models must be interpretable by other agents. The authors propose a novel framework, Agentic-imodels, to evolve data-science tools that are specifically designed for agentic interpretability. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of an autoresearch loop that generates a library of scikit-learn-compatible regressors optimized for both predictive performance and a new interpretability metric based on large language models (LLMs). The interpretability metric evaluates whether an LLM can simulate the model's behavior based solely on its string representation. The authors employ a suite of LLM-graded tests to assess this simulatable property. The training process involves iteratively refining the models based on performance metrics and interpretability scores, leveraging a diverse set of tabular datasets. The compute resources utilized for training are not explicitly disclosed.

**Results**  
The evolved models demonstrate significant improvements in both predictive performance and agent-facing interpretability. Specifically, the authors report performance enhancements of up to 73% on the BLADE benchmark when integrated into downstream ADS applications, including Copilot CLI, Claude Code, and Codex. These results are benchmarked against traditional models, although specific baseline models and their performance metrics are not detailed in the summary.

**Limitations**  
The authors acknowledge that the interpretability metric, while innovative, may not capture all dimensions of model behavior and could be limited by the capabilities of the LLMs used for evaluation. Additionally, the generalizability of the evolved models across diverse datasets and tasks remains to be fully validated. The paper does not address potential biases in the training data or the implications of using LLMs for interpretability, which could affect the robustness of the findings.

**Why it matters**  
The introduction of Agentic-imodels represents a significant step towards enabling ADS systems to autonomously interpret their own models, which is crucial for scaling data science tasks in an agentic context. By focusing on agent-facing interpretability, this work lays the groundwork for future research into more sophisticated and autonomous data analysis frameworks. The implications extend to enhancing the usability of ADS systems in practical applications, potentially transforming how data science is conducted in automated environments.

Authors: Chandan Singh, Yan Shuo Tan, Weijia Xu, Zelalem Gero, Weiwei Yang, Michel Galley, Jianfeng Gao  
Source: arXiv:2605.03808  
URL: [https://arxiv.org/abs/2605.03808v1](https://arxiv.org/abs/2605.03808v1)
