---
title: "Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM"
date: 2026-05-05 16:32:11 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03945v1"
arxiv_id: "2605.03945"
authors: ["Tianyu Wang", "Luhao Zhang", "Rachel Cummings"]
slug: integrating-feature-correlation-in-differential-privacy-with
summary_word_count: 454
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the existing literature on differential privacy (DP) by proposing a framework that accounts for the heterogeneity of features in datasets. Standard DP enforces uniform privacy constraints across all features, which can be overly conservative, especially when certain features are insensitive to privacy concerns. The authors introduce a relaxed definition of differential privacy that allows for the treatment of specific features as insensitive, even when they are correlated with sensitive features. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of a correlation-aware framework, termed $\textsf{CorrDP}$, which integrates feature correlation into the differential privacy paradigm. The framework quantifies correlations using total variation distance, allowing for a nuanced application of privacy constraints. The authors propose algorithms for differentially private empirical risk minimization (DP-ERM) that incorporate distance-dependent noise into the gradient updates, enhancing the theoretical utility guarantees of the model. When the correlation distance is unknown, the framework includes a mechanism to estimate it from the dataset, ensuring that the privacy-utility trade-off remains favorable. The algorithms are designed to operate under the relaxed privacy constraints defined by $\textsf{CorrDP}$.

**Results**  
The experimental results demonstrate that the $\textsf{CorrDP}$-based DP-ERM algorithms significantly outperform standard DP methods, particularly in scenarios where insensitive features are present. The authors report improvements in utility metrics, although specific numerical results and effect sizes are not detailed in the abstract. The experiments are conducted on both synthetic datasets and real-world applications, showcasing the robustness of the proposed framework across different contexts. The results indicate that the $\textsf{CorrDP}$ framework can effectively leverage the presence of insensitive features to enhance model performance while maintaining differential privacy.

**Limitations**  
The authors acknowledge that the proposed framework relies on the accurate estimation of correlation distances, which may not always be feasible in practice. Additionally, the performance gains are contingent on the presence of insensitive features; thus, the utility improvements may not generalize to all datasets. The paper does not address potential computational overhead introduced by the correlation estimation process or the implications of feature selection on privacy guarantees. Furthermore, the theoretical guarantees provided are based on specific assumptions that may not hold in all real-world scenarios.

**Why it matters**  
This work has significant implications for the design of privacy-preserving machine learning systems, particularly in domains where feature sensitivity varies. By allowing for a more flexible application of differential privacy, the $\textsf{CorrDP}$ framework can lead to improved model performance without compromising privacy. This approach opens avenues for future research into feature-specific privacy mechanisms and could influence the development of more sophisticated privacy-preserving algorithms that better align with practical data characteristics.

Authors: Tianyu Wang, Luhao Zhang, Rachel Cummings  
Source: arXiv:2605.03945  
URL: https://arxiv.org/abs/2605.03945v1
