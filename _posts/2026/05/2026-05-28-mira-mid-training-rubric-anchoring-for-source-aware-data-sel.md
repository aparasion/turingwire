---
title: "MIRA: Mid-training Rubric Anchoring for Source-Aware Data Selection"
date: 2026-05-28 17:40:40 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30288v1"
arxiv_id: "2605.30288"
authors: ["Haowen Wang", "Yaxin Du", "Jian Yang", "Jiajun Wu", "Shukai Liu", "Yuxuan Zhang"]
slug: mira-mid-training-rubric-anchoring-for-source-aware-data-sel
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in effective data selection during the mid-training phase of large language model (LLM) development. The authors highlight that existing methods either scale well but provide only implicit quality signals or rely on fixed rubrics that do not adapt to the heterogeneous nature of data sources. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is MIRA (Mid-training Rubric Anchoring), a source-aware filtering framework that integrates rubric discovery into the data selection process. MIRA operates in two main stages: first, it identifies evaluation criteria tailored to each source group, and second, it distills these criteria into scalable student scorers for comprehensive corpus filtering. The architecture leverages self-anchored rubric discovery, allowing for dynamic adaptation to the specific characteristics of the data sources. The authors do not disclose specific details regarding the loss function or the compute resources used for training, but they emphasize the framework's ability to handle large-scale data efficiently.

**Results**  
MIRA was evaluated on a code-oriented mid-training task involving 21 sources categorized into 5 source groups. It was benchmarked against several selection baselines across nine code-related benchmarks. The results indicate that MIRA outperforms these baselines significantly, achieving a performance level that matches the full-corpus run while utilizing only 50% of the tokens. Specific performance metrics are not provided in the summary, but the authors assert that the effect sizes are substantial, demonstrating MIRA's effectiveness in optimizing data selection.

**Limitations**  
The authors acknowledge that MIRA's performance is contingent on the quality of the rubric discovery process, which may vary based on the diversity and representativeness of the source data. They also note that while MIRA improves upon existing methods, it may still be limited by the inherent biases present in the source data. An additional limitation not explicitly mentioned by the authors is the potential computational overhead introduced by the rubric discovery phase, which could impact scalability in extremely large datasets.

**Why it matters**  
The implications of this work are significant for the field of LLM development, particularly in enhancing the efficiency and effectiveness of mid-training data selection. By introducing a framework that adapts to the nuances of diverse data sources, MIRA could lead to improved model performance on downstream tasks, particularly in scenarios where data quality and relevance are critical. This approach may also inspire further research into adaptive data selection methodologies, potentially influencing future architectures and training paradigms in the broader context of machine learning.

Authors: Haowen Wang, Yaxin Du, Jian Yang, Jiajun Wu, Shukai Liu, Yuxuan Zhang, Pingjie Wang, Siheng Chen et al.  
Source: arXiv:2605.30288  
URL: [https://arxiv.org/abs/2605.30288v1](https://arxiv.org/abs/2605.30288v1)
