---
title: "Is Your Driving World Model an All-Around Player?"
date: 2026-05-11 17:05:49 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.10858v1"
arxiv_id: "2605.10858"
authors: ["Lingdong Kong", "Ao Liang", "Tianyi Yan", "Hongsi Liu", "Wesley Yang", "Ziqi Huang"]
slug: is-your-driving-world-model-an-all-around-player
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of driving world models, specifically the lack of comprehensive metrics that assess both visual fidelity and behavioral realism. Current models excel in generating photorealistic dash-cam videos but often fail to maintain physical consistency or perform well in closed-loop driving scenarios. The authors highlight that existing evaluations focus primarily on visual quality, neglecting the critical aspect of how these models behave in realistic driving contexts. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce WorldLens, a unified benchmark designed to evaluate world-model fidelity across five complementary aspects and 24 standardized dimensions. These dimensions encompass pixel quality, 4D geometric accuracy, closed-loop driving performance, and alignment with human perceptual standards. The evaluation framework is applied to six representative models, revealing that no single model excels across all metrics. To enhance the benchmark, the authors also present WorldLens-26K, a dataset containing 26,808 human-annotated preferences that pair numerical scores with textual rationales. Additionally, they introduce WorldLens-Agent, a vision-language evaluator that leverages these human judgments to facilitate scalable and explainable auto-assessment of generated worlds.

**Results**  
The evaluation of the six models indicates a clear divide in performance: texture-rich models often violate geometric constraints, while geometry-aware models struggle with behavioral fidelity. The strongest models achieve only 2-3 out of 10 on human realism ratings, underscoring the inadequacy of current approaches in delivering a holistic driving world model. The authors provide quantitative metrics across the benchmark dimensions, although specific numerical results against named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their benchmark may not capture all aspects of driving world fidelity, particularly in edge cases or rare driving scenarios. They also note that the reliance on human annotations introduces potential biases, as preferences may vary across different demographic groups. Furthermore, the paper does not address the computational efficiency of the models evaluated, which could impact their practical deployment in real-world applications.

**Why it matters**  
This work has significant implications for the development of more robust driving world models that not only generate visually appealing outputs but also adhere to the physical and behavioral constraints of real-world driving. By bridging the gap between algorithmic metrics and human perception, the WorldLens benchmark and its associated datasets provide a framework for future research to enhance the fidelity of generative models in autonomous driving. This could lead to improved safety and reliability in autonomous systems, as well as more effective training environments for reinforcement learning agents.

Authors: Lingdong Kong, Ao Liang, Tianyi Yan, Hongsi Liu, Wesley Yang, Ziqi Huang, Xian Sun, Wei Yin et al.  
Source: arXiv:2605.10858  
URL: [https://arxiv.org/abs/2605.10858v1](https://arxiv.org/abs/2605.10858v1)
