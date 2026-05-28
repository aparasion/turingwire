---
title: "Learning to Assess the Reliability of Number-of-Runs Estimation in Stochastic Optimization"
date: 2026-05-27 11:08:19 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.28309v1"
arxiv_id: "2605.28309"
authors: ["Sara Gjorgjieva", "Eva Tuba", "Tome Eftimov"]
slug: learning-to-assess-the-reliability-of-number-of-runs-estimat
summary_word_count: 470
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of determining the sufficient number of runs required for reliable benchmarking of stochastic optimization algorithms. The existing literature primarily focuses on whether repeated runs are necessary, but lacks methodologies for efficiently estimating the required number of runs without incurring excessive computational costs. This work presents a learning-based approach to enhance the empirical online heuristic for estimating run numbers, which is particularly relevant given the increasing complexity of optimization problems and the need for efficient resource allocation in large-scale experiments. Notably, this is a preprint and has not yet undergone peer review.

**Method**  
The authors propose a learning-based extension of an empirical online heuristic that utilizes outlier handling and skewness-based symmetry checks to estimate the required number of runs. They leverage a dataset comprising 132,000 runs from the Nevergrad platform, which includes 24 optimization problems across 20 dimensions, with 10 instances per problem and 11 different optimizers. The core technical contribution involves training classifiers on 23 features, which encompass statistical properties, energy-free metrics, and shape and stability characteristics of the optimization runs. The classifiers are specifically designed to predict the reliability of run-number estimates, with a focus on maximizing minority-class recall to effectively identify incorrect estimates. The training and evaluation are conducted in a within-configuration setup, where models are trained and tested on data from the same optimizer.

**Results**  
The results indicate that the proposed method can successfully learn to predict run-number reliability within a configuration, achieving high minority-class recall. However, the performance is constrained by the limited diversity of data within fixed configurations. The paper does not provide specific numerical results or effect sizes against named baselines, which would have strengthened the evaluation of the proposed method's efficacy.

**Limitations**  
The authors acknowledge that the performance of their approach is limited by the restricted data diversity inherent in the within-configuration learning setup. This limitation may hinder the generalizability of the model to broader scenarios involving different optimizers or problem configurations. Additionally, the reliance on a single dataset from Nevergrad may not capture the full spectrum of stochastic optimization challenges, potentially affecting the robustness of the learned models. The lack of external validation on diverse datasets is another notable limitation.

**Why it matters**  
This work has significant implications for the field of stochastic optimization, particularly in the context of large-scale benchmarking. By providing a method to estimate the reliability of run-number predictions, it enables researchers and practitioners to optimize computational resources more effectively, thereby reducing unnecessary runs and associated costs. The approach could facilitate more efficient experimentation in various optimization tasks, leading to faster convergence on reliable solutions. Furthermore, the focus on minority-class recall highlights the importance of accurately identifying unreliable estimates, which is crucial for maintaining the integrity of benchmarking processes in optimization research.

Authors: Sara Gjorgjieva, Eva Tuba, Tome Eftimov  
Source: arXiv:2605.28309  
URL: https://arxiv.org/abs/2605.28309v1
