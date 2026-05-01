---
title: "Explainable Load Forecasting with Covariate-Informed Time Series Foundation Models"
date: 2026-04-30 17:36:24 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.28149v1"
arxiv_id: "2604.28149"
authors: ["Matthias Hertel", "Alexandra Nikoltchovska", "Sebastian P\u00fctz", "Ralf Mikut", "Benjamin Sch\u00e4fer", "Veit Hagenmeyer"]
slug: explainable-load-forecasting-with-covariate-informed-time-se
summary_word_count: 420
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the explainability of Time Series Foundation Models (TSFMs) in the context of load forecasting for critical infrastructure, specifically power grids. While TSFMs have shown promise as general-purpose forecasting models, their black-box nature poses challenges for transparency and trust in applications where interpretability is crucial. The authors propose a method to compute Shapley Additive Explanations (SHAP) tailored for TSFMs, enhancing their usability in operational energy forecasting.

**Method**  
The core technical contribution is an efficient algorithm for computing SHAP values specifically designed for TSFMs. The method exploits the flexibility of TSFMs regarding input context length and covariate inclusion, enabling temporal and covariate masking. This selective withholding of inputs allows for scalable explanations of model predictions. The authors evaluate two TSFMs—Chronos-2 and TabPFN-TS—on a day-ahead load forecasting task for a transmission system operator (TSO). The models are assessed in a zero-shot setting, meaning they are tested without prior training on the specific TSO data, which is a significant aspect of their evaluation.

**Results**  
Both Chronos-2 and TabPFN-TS demonstrate competitive predictive performance against a Transformer model that was trained on multiple years of TSO data. The authors report that the TSFMs achieve similar accuracy metrics, although specific numerical results are not disclosed in the abstract. The SHAP explanations generated align with established domain knowledge, indicating that the models effectively incorporate relevant covariates such as weather and calendar information into their predictions. This alignment suggests that the TSFMs not only perform well but also provide interpretable outputs that can be trusted by stakeholders.

**Limitations**  
The authors acknowledge that their approach is contingent on the inherent capabilities of TSFMs and may not generalize to all types of forecasting tasks or datasets. They do not discuss potential limitations related to the computational efficiency of the SHAP computation in larger-scale applications or the scalability of the method across different forecasting scenarios. Additionally, the zero-shot evaluation, while demonstrating competitive performance, may not fully capture the models' capabilities in a more traditional training and validation setup.

**Why it matters**  
This work has significant implications for the deployment of TSFMs in operational settings, particularly in energy systems where explainability is paramount. By providing a method for generating interpretable predictions, the authors enhance the trustworthiness of TSFMs, potentially leading to broader adoption in critical infrastructure applications. The ability to align model outputs with domain knowledge can facilitate better decision-making processes and improve stakeholder confidence in automated forecasting systems.

Authors: Matthias Hertel, Alexandra Nikoltchovska, Sebastian Pütz, Ralf Mikut, Benjamin Schäfer, Veit Hagenmeyer  
Source: arXiv:2604.28149  
URL: [https://arxiv.org/abs/2604.28149v1](https://arxiv.org/abs/2604.28149v1)
