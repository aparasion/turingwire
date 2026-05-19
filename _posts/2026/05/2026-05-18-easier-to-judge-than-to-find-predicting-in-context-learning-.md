---
title: "Easier to Judge than to Find: Predicting In-Context Learning Success for Demonstration Selection"
date: 2026-05-18 15:03:59 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18512v1"
arxiv_id: "2605.18512"
authors: ["Haochun Wang", "Chaofen Yang", "Jiatong Liu", "Jingbo Wang", "Zewen Qiang", "Sendong Zhao"]
slug: easier-to-judge-than-to-find-predicting-in-context-learning-
summary_word_count: 468
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of demonstration selection in in-context learning (ICL), which is crucial for optimizing model performance but computationally expensive due to the vast space of possible demonstration contexts. The authors argue that predicting the success of a specific query-context pair \((q,D)\) is more efficient than searching for an optimal demonstration set \(D^\star\). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce DiSP (Demonstration Selection via Prediction), a novel framework that stratifies queries based on their difficulty. The methodology consists of three main components: 
1. **Random Demonstration Trials**: DiSP conducts trials to estimate the success rate for each training query, allowing for empirical assessment of demonstration effectiveness.
2. **Lightweight Router**: A model is trained to predict the difficulty of queries based on their characteristics, enabling efficient routing of queries to appropriate demonstrations.
3. **Level-Specific Judges**: For each sampled demonstration, judges are trained to evaluate the suitability of the demonstration for the given query, facilitating a more targeted selection process.

During inference, DiSP employs a stop-on-acceptance strategy, which allows it to terminate the search for demonstrations once a suitable context is identified, thus adhering to a predefined computational budget. The framework is evaluated using Llama 3 (8B) and Qwen 2.5 (7B) models across five classification datasets.

**Results**  
DiSP demonstrates significant improvements over existing learned selection baselines, achieving an average accuracy increase of up to 3.4%. Additionally, it provides a remarkable end-to-end wall-clock speedup of up to 23 times compared to traditional methods. These results indicate that DiSP not only enhances accuracy but also optimizes computational efficiency, making it a compelling alternative for demonstration selection in ICL tasks.

**Limitations**  
The authors acknowledge that the effectiveness of DiSP may vary depending on the specific characteristics of the datasets used, and they do not explore the generalizability of the framework across diverse domains beyond classification tasks. Furthermore, the reliance on random trials for estimating success rates may introduce variability in performance, particularly in scenarios with limited data. The paper does not address potential biases in the selection process or the implications of using a lightweight router on model interpretability.

**Why it matters**  
The implications of this work are significant for the field of ICL, as it provides a more efficient mechanism for demonstration selection, which is critical for enhancing model performance without incurring prohibitive computational costs. By framing the problem as one of prediction rather than exhaustive search, DiSP opens avenues for further research into adaptive learning strategies and the development of more sophisticated routing mechanisms. This could lead to broader applications in various domains where ICL is employed, ultimately improving the usability and effectiveness of large language models.

Authors: Haochun Wang, Chaofen Yang, Jiatong Liu, Jingbo Wang, Zewen Qiang, Sendong Zhao, Bing Qin, Ting Liu  
Source: arXiv:2605.18512  
URL: https://arxiv.org/abs/2605.18512v1
