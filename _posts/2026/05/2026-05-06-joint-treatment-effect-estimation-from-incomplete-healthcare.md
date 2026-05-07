---
title: "Joint Treatment Effect Estimation from Incomplete Healthcare Data: Temporal Causal Normalizing Flows with LLM-driven Evolutionary MNAR Imputation"
date: 2026-05-06 16:53:08 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05125v1"
arxiv_id: "2605.05125"
authors: ["Olivia Jullian Parra", "Sara Zoccheddu", "David Catalan Cerezo", "Tom Forzy", "Franziska Ulrich", "William Sutcliffe"]
slug: joint-treatment-effect-estimation-from-incomplete-healthcare
summary_word_count: 442
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing treatment effect estimation methods in the context of incomplete longitudinal electronic health records (EHRs), particularly when dealing with missing-not-at-random (MNAR) data and time-varying confounding. Traditional approaches often treat causal estimation, missing data, and temporal dynamics in isolation, which can lead to significant biases in causal inference. The authors propose a unified framework that integrates these components to enhance robustness in causal analysis.

**Method**  
The proposed methodology consists of a two-stage pipeline for treatment effect estimation. The first stage employs CausalFlow-T, a directed acyclic graph (DAG)-constrained normalizing flow architecture that incorporates long short-term memory (LSTM) networks to encode patient history. This design allows for exact invertible counterfactual inference, mitigating approximation errors typically associated with variational inference. The DAG constraints explicitly model causal relationships, enabling the separation of confounding factors. The second stage introduces an LLM-driven evolutionary imputer that generates executable imputation operators rather than filling in individual missing entries. This imputer is evaluated using three large language model (LLM) backends, including two open-source models, and is designed to handle varying degrees of MNAR missingness (30%–80%).

**Results**  
The pipeline was evaluated on four synthetic datasets and one semi-synthetic benchmark with known counterfactuals. The results indicate that the combination of DAG constraints and exact inference effectively addresses distinct failure modes in treatment effect estimation. The LLM-driven imputer outperformed statistical baselines in terms of point-wise accuracy and temporal extrapolation, while maintaining average treatment effect (ATE) recovery. Specifically, on Swiss primary-care EHRs for adults with type 2 diabetes, the pipeline estimated a per-protocol weight-loss difference of -0.98 kg [95% CI -1.01, -0.96] favoring GLP-1 receptor agonists, aligning with findings from randomized controlled trials.

**Limitations**  
The authors acknowledge that the performance of the proposed methods may be sensitive to the choice of LLM backend and the specific characteristics of the EHR data used. Additionally, while the pipeline shows promise in handling MNAR data, the generalizability of the results to other healthcare contexts or datasets remains to be established. The reliance on LLMs for imputation may also introduce biases based on the training data of the models used.

**Why it matters**  
This work has significant implications for causal inference in healthcare research, particularly in scenarios where RCTs are impractical. By effectively integrating causal modeling with advanced imputation techniques, the proposed framework enhances the reliability of treatment effect estimates derived from incomplete EHRs. This could lead to more accurate clinical decision-making and better understanding of treatment impacts in real-world settings, ultimately informing healthcare policies and practices.

Authors: Olivia Jullian Parra, Sara Zoccheddu, David Catalan Cerezo, Tom Forzy, Franziska Ulrich, William Sutcliffe, Jakob Martin Burgstaller, Oliver Senn et al.  
Source: arXiv:2605.05125  
URL: https://arxiv.org/abs/2605.05125v1
