---
title: "Benchmarking Sensor-Fault Robustness in Forecasting"
date: 2026-05-11 16:41:14 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10822v1"
arxiv_id: "2605.10822"
authors: ["Alexander Windmann", "Philipp Wittenberg", "Gianluca Manca", "Marcel Dix", "Jens U. Brandt", "Oliver Niggemann"]
slug: benchmarking-sensor-fault-robustness-in-forecasting
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating forecasting models for cyber-physical systems (CPS) under sensor faults, such as noise, bias, missing data, and temporal misalignment. Traditional forecasting evaluations typically focus on nominal error metrics, failing to assess model robustness in the presence of these faults. The authors introduce SensorFault-Bench, a benchmarking protocol designed to systematically evaluate the robustness of forecasting architectures against various sensor faults. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the SensorFault-Bench protocol, which includes a comprehensive taxonomy for method comparison and a standardized severity model for fault scenarios. The evaluation framework utilizes four real-world datasets and eight distinct fault scenarios, measuring metrics such as worst-scenario degradation, clean mean squared error (MSE), and worst-scenario fault-time MSE. A disjoint fault-transfer split is employed, allowing fault-training methods to train on adjacent fault families while evaluating on separate benchmark scenarios. The study evaluates various forecasting architectures, including Chronos-2, a zero-shot foundation model, and assesses robustness-improvement methods like projected gradient descent adversarial training, randomized training, and fault augmentation.

**Results**  
The findings reveal that forecasting architectures optimized for clean MSE can experience significant degradation under fault conditions. For instance, Chronos-2 exhibits comparable or inferior performance to a naive last-value forecaster in clean MSE on single-target datasets, while demonstrating the largest degradation in worst-scenario fault-time MSE on the ETTh1 and Traffic datasets. The robustness-improvement methods show selective effectiveness: projected gradient descent adversarial training and randomized training are effective where value faults dominate, while fault augmentation is beneficial in scenarios dominated by availability faults. The paper provides detailed empirical results, including specific degradation metrics across the evaluated scenarios.

**Limitations**  
The authors acknowledge that their benchmarking protocol may not encompass all possible sensor fault scenarios, potentially limiting its generalizability. Additionally, the reliance on specific datasets may introduce biases that affect the robustness assessments. The paper does not address the computational overhead associated with implementing the robustness-improvement methods, which could be a concern for real-time applications.

**Why it matters**  
This work has significant implications for the development of robust forecasting models in CPS, as it provides a structured approach to evaluate and improve model resilience against sensor faults. By establishing a standardized benchmarking protocol, SensorFault-Bench enables researchers to compare different architectures and robustness-improvement techniques under consistent conditions, fostering advancements in the field. The open-source nature of the code and data access facilitates further research and experimentation, potentially leading to more reliable forecasting systems in critical applications.

Authors: Alexander Windmann, Philipp Wittenberg, Gianluca Manca, Marcel Dix, Jens U. Brandt, Oliver Niggemann  
Source: arXiv:2605.10822  
URL: [https://arxiv.org/abs/2605.10822v1](https://arxiv.org/abs/2605.10822v1)
