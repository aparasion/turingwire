---
title: "Causal Foundation Models with Continuous Treatments"
date: 2026-05-14 17:40:28 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15133v1"
arxiv_id: "2605.15133"
authors: ["Christopher Stith", "Medha Barath", "Vahid Balazadeh", "Jesse C. Cresswell", "Rahul G. Krishnan"]
slug: causal-foundation-models-with-continuous-treatments
summary_word_count: 487
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the literature regarding causal inference in the continuous treatment setting, which has been less explored compared to binary treatment scenarios. The authors highlight that existing causal models are primarily designed for binary interventions, limiting their applicability in domains where treatment variables can take on a continuous range. This work presents the first causal foundation model specifically tailored for continuous treatments, aiming to generalize across various unseen tasks without the need for additional training or fine-tuning. The paper is a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel causal foundation model that employs a meta-learning approach to predict causal effects across diverse tasks. The model is built on a transformer architecture, which is trained to reconstruct individual treatment-response curves from observational data. A key innovation is the introduction of a prior over data-generating processes that accommodates continuous treatment variables, enabling the generation of a rich corpus for training. The model leverages in-context learning to efficiently perform Bayesian posterior inference, thus amortizing the computational cost typically associated with this process. The training compute details are not explicitly disclosed, but the model's architecture and training methodology are central to its performance.

**Results**  
The proposed model demonstrates state-of-the-art performance in reconstructing individual treatment-response curves, outperforming existing causal models that are specifically trained for similar tasks. While specific numerical results and effect sizes are not provided in the abstract, the authors claim significant improvements over baseline models, indicating a robust capability in handling continuous treatment scenarios. The benchmarks used for evaluation are not explicitly named in the abstract, but the results suggest a substantial advancement in the field of causal inference.

**Limitations**  
The authors acknowledge that their model's performance may be contingent on the quality and representativeness of the observational data used for training. Additionally, the reliance on in-context learning may introduce limitations in scenarios where the data distribution significantly deviates from the training corpus. The paper does not address potential challenges related to the interpretability of the model's predictions or the implications of model assumptions on causal inference validity. Furthermore, the generalizability of the model across all domains requiring continuous treatment analysis remains to be validated.

**Why it matters**  
This work has significant implications for advancing causal inference methodologies, particularly in fields such as economics, healthcare, and social sciences, where interventions often involve continuous variables. By providing a framework that can generalize across tasks without extensive retraining, the model could facilitate more efficient causal analysis in real-world applications. The ability to reconstruct treatment-response curves from observational data enhances the potential for deriving actionable insights from complex datasets, thereby contributing to more informed decision-making processes. This research lays the groundwork for future explorations into continuous treatment settings and encourages further development of causal models that can adapt to diverse intervention types.

Authors: Christopher Stith, Medha Barath, Vahid Balazadeh, Jesse C. Cresswell, Rahul G. Krishnan  
Source: arXiv:2605.15133  
URL: [https://arxiv.org/abs/2605.15133v1](https://arxiv.org/abs/2605.15133v1)
