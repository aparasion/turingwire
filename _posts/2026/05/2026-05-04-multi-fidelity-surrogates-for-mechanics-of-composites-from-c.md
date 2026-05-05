---
title: "Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks"
date: 2026-05-04 17:45:47 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02871v1"
arxiv_id: "2605.02871"
authors: ["Haizhou Wen", "Elham Kiyani", "Gang Li", "Srikanth Pilla", "George Em Karniadakis", "Zhen Li"]
slug: multi-fidelity-surrogates-for-mechanics-of-composites-from-c
summary_word_count: 414
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in predictive modeling of composite materials, which are characterized by complex hierarchical and anisotropic properties influenced by various factors, including constituents, plies, laminates, and manufacturing history. Traditional modeling approaches require extensive high-fidelity simulations and experiments, making them computationally expensive and impractical for large design spaces. The authors propose multi-fidelity surrogate modeling as a solution to leverage abundant low-fidelity data alongside limited high-fidelity data to enhance predictive accuracy and efficiency.

**Method**  
The paper provides a comprehensive review of multi-fidelity surrogate modeling techniques applicable to composite mechanics. It covers various methodologies, including Gaussian-process-based methods (Kriging, co-Kriging), coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, and multi-fidelity deep Gaussian processes. The authors emphasize the distinctions among these methods in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. The review also discusses multi-fidelity neural networks, which integrate low-fidelity and high-fidelity data to improve model performance. The authors highlight the importance of selecting appropriate fidelity levels and the role of uncertainty quantification in enhancing model reliability.

**Results**  
While specific numerical results are not provided in the abstract, the paper discusses the application of multi-fidelity surrogates in various engineering problems, such as rapid exploration of material design spaces, inverse optimization for parameter identification, and workflow integration. The authors suggest that these methods can significantly reduce computational costs while maintaining predictive accuracy, although exact performance metrics against named baselines are not detailed in the summary.

**Limitations**  
The authors acknowledge several limitations, including the challenges of regime-dependent fidelity gaps that arise from nonlinear damage and manufacturing history, as well as mismatches between simulations and experimental data. They also note the complexities involved in uncertainty propagation across multi-fidelity models. However, the paper does not address potential scalability issues when applying these methods to very large datasets or the computational overhead associated with training multi-fidelity neural networks.

**Why it matters**  
This work is significant for advancing the field of composite material modeling by providing a structured overview of multi-fidelity approaches that can enhance predictive capabilities while reducing computational demands. The insights gained from this review can inform future research directions, particularly in the integration of heterogeneous data sources and the development of more robust models that account for the complexities inherent in composite materials. The discussion of open questions also highlights areas for further investigation, which could lead to improved methodologies and applications in engineering design and optimization.

Authors: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li  
Source: arXiv:2605.02871  
URL: [https://arxiv.org/abs/2605.02871v1](https://arxiv.org/abs/2605.02871v1)
