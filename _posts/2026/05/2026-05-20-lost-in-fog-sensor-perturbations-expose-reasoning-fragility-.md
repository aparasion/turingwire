---
title: "Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs"
date: 2026-05-20 17:34:02 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21446v1"
arxiv_id: "2605.21446"
authors: ["Abhinaw Priyadershi", "Jelena Frtunikj"]
slug: lost-in-fog-sensor-perturbations-expose-reasoning-fragility-
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the robustness of Vision-Language-Action (VLA) systems in autonomous driving under real-world sensor perturbations. While existing literature emphasizes the importance of interpretable explanations in autonomous systems, there is limited empirical evidence on how these explanations hold up against various sensor degradations. The authors investigate the relationship between reasoning consistency, as measured by Chain-of-Causation (CoC) explanations, and trajectory reliability in the presence of sensor noise, lighting extremes, and fog.

**Method**  
The study employs a controlled perturbation framework to evaluate the Alpamayo R1 model, which has 10 billion parameters, across 1,996 driving scenarios. The authors introduce eight types of sensor perturbations: Gaussian noise at four intensities (σ = 10, 30, 50, 70), two lighting extremes, and two fog levels, resulting in approximately 18,000 inference trials. The core technical contribution is the analysis of CoC explanations and their correlation with trajectory deviations. The authors conduct a controlled ablation study to assess the impact of enabling CoC generation on trajectory accuracy, reporting an average improvement of 11.8% across conditions. The relationship between perturbation intensity and trajectory deviation is modeled, revealing a linear degradation pattern with an R² value of 0.957.

**Results**  
The findings indicate that when CoC explanations change due to sensor perturbations, trajectory deviation increases significantly, with a spike of 5.3 times (21.8m vs. 4.1m). The correlation coefficient across different attack types is r = 0.99, while the per-sample correlation is r_pb = 0.53, with a Cohen's d effect size of 1.12, indicating a large effect. The ablation study confirms that enabling CoC generation leads to statistically significant improvements in trajectory accuracy (p < 0.0001). Standard input preprocessing defenses were found to provide only marginal improvements, underscoring the need for more robust solutions.

**Limitations**  
The authors acknowledge that their study is limited to specific types of sensor perturbations and may not generalize to all real-world scenarios. Additionally, the reliance on a single model (Alpamayo R1) may restrict the applicability of the findings to other architectures. The controlled nature of the perturbations may not fully capture the complexities of real-world driving conditions, and the study does not explore the computational overhead associated with generating CoC explanations in real-time applications.

**Why it matters**  
This work has significant implications for the deployment of VLA systems in autonomous driving. By establishing CoC consistency as a quantitative proxy for planning safety, the authors advocate for the integration of reasoning-based runtime monitoring systems to enhance the reliability of autonomous vehicles under sensor degradation. This research paves the way for future studies aimed at developing more resilient autonomous systems that can maintain performance and safety in unpredictable environments.

Authors: Abhinaw Priyadershi, Jelena Frtunikj  
Source: arXiv:2605.21446  
URL: https://arxiv.org/abs/2605.21446v1
