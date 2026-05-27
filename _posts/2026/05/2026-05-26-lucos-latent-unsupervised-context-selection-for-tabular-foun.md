---
title: "LUCoS: Latent Unsupervised Context Selection for Tabular Foundation Models"
date: 2026-05-26 16:31:39 +0000
category: research
subcategory: training_methods
company: "Oracle"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27254v1"
arxiv_id: "2605.27254"
authors: ["Oroel Ipas", "Guillermo Gomez-Trenado", "Roc\u00edo Romero-Zaliz", "Isaac Triguero"]
slug: lucos-latent-unsupervised-context-selection-for-tabular-foun
summary_word_count: 460
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of instance selection for labeling in low-label tabular learning, particularly in the cold-start scenario where no labeled instances are available. The authors note that while recent Tabular Foundation Models (TFMs) like TabPFN have shown promise, the literature has largely overlooked the geometric nature of context selection in tabular data. Traditional methods rely on raw tabular space, which is inadequate due to the heterogeneous types and mixed scales of features, leading to unreliable distance metrics. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose LUCoS (Latent Unsupervised Context Selection), which leverages the latent geometry derived from embeddings produced by an unsupervised Prior-Fitted Network (PFN). Instead of operating in the original feature space, LUCoS selects representative medoids from the latent space to form context sets. The method involves a two-step process: first, it generates embeddings of the tabular data using the PFN, and second, it applies a medoid selection strategy to identify instances that best represent the underlying data distribution. The training compute details are not disclosed, but the method is evaluated across 67 datasets from the OpenML-CC18 benchmark.

**Results**  
LUCoS demonstrates superior performance compared to baseline methods across multiple metrics, including mean AUC, accuracy (ACC), and F1 score, under various low-label budgets. Specifically, LUCoS ranks first in all evaluated metrics, indicating robust performance across the datasets. The authors conduct a gain decomposition analysis, revealing that at smaller budgets, the primary advantage stems from enforcing coverage of the instance space, while at larger budgets, the effectiveness is attributed to the quality of the representation space used for measuring coverage. This indicates a clear shift in the mechanism of improvement as labeling budgets increase.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of tabular data, particularly those with extreme feature heterogeneity or non-standard distributions. They also do not address the computational overhead associated with generating embeddings via the PFN, which could be a limiting factor in real-time applications. Additionally, the reliance on unsupervised learning for context selection may not always yield optimal results in scenarios where labeled data is available.

**Why it matters**  
LUCoS has significant implications for the field of low-label learning in tabular data, particularly in scenarios where labeling is costly or impractical. By demonstrating that effective context selection can be achieved through latent space representations, this work opens avenues for further research into unsupervised methods for instance selection. It challenges the prevailing reliance on raw feature spaces and suggests that future TFMs could benefit from incorporating latent representations to enhance predictive performance. This could lead to more efficient labeling strategies and improved model performance in real-world applications.

Authors: Oroel Ipas, Guillermo Gomez-Trenado, Rocío Romero-Zaliz, Isaac Triguero  
Source: arXiv:2605.27254  
URL: https://arxiv.org/abs/2605.27254v1
