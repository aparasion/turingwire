---
title: "D$^3$-Subsidy: Online and Sequential Driver Subsidy Decision-Making for Large-Scale Ride-Hailing Market"
date: 2026-05-19 15:55:55 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20036v1"
arxiv_id: "2605.20036"
authors: ["Taijie Chen", "Rui Su", "Siyuan Feng", "Laoming Zhang", "Hongyang Zhang", "Haijiao Wang"]
slug: d-3-subsidy-online-and-sequential-driver-subsidy-decision-ma
summary_word_count: 416
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of optimizing driver-side subsidies in large-scale ride-hailing markets, specifically in the context of DiDi Chuxing. The authors identify a gap in existing literature regarding the simultaneous management of three critical constraints: responsiveness to stochastic demand shocks, adherence to strict subsidy-rate caps, and the necessity for low-latency execution across urban environments. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution is the D$^3$-Subsidy framework, which employs a hierarchical diffusion-based approach for city-wide subsidy control. The framework utilizes a prefix-conditioned diffusion model to generate plausible future trajectories based on historical data, effectively bridging the train-inference gap. This model ensures that the training process aligns with the fixed-history nature of online deployment. The generated plans are decoded into low-dimensional control signals through a context-conditioned inverse module. For scalable execution, the authors introduce a Lagrangian-dual-derived mapping that integrates subsidy-rate caps directly into order-driver incentives, eliminating the need for iterative optimization. Additionally, a multi-city pretraining strategy is employed, allowing for parameter-efficient fine-tuning and robust transfer learning across heterogeneous urban environments.

**Results**  
Extensive offline evaluations demonstrate that D$^3$-Subsidy significantly enhances key performance indicators, specifically completed rides (\texttt{Rides}) and gross merchandise value (\texttt{GMV}), while ensuring compliance with subsidy caps. The paper reports a notable uplift in both \texttt{Rides} and \texttt{GMV} during real-world A/B testing, with metrics indicating that budget-related violations remained within operational thresholds. While specific numerical improvements are not disclosed in the abstract, the qualitative results suggest a substantial impact compared to baseline subsidy strategies.

**Limitations**  
The authors acknowledge that the model's performance may vary across different urban environments due to heterogeneous demand patterns and driver behaviors. They also note the potential for overfitting during the pretraining phase if not managed properly. An additional limitation not explicitly mentioned is the reliance on historical data, which may not fully capture future demand dynamics, particularly in rapidly changing urban contexts.

**Why it matters**  
The implications of this work are significant for the optimization of ride-hailing platforms, particularly in enhancing operational efficiency and profitability through better subsidy management. By providing a scalable and responsive framework, D$^3$-Subsidy can serve as a foundational model for future research in dynamic pricing and resource allocation in on-demand service markets. The methodology may also inspire similar approaches in other domains requiring real-time decision-making under constraints, such as logistics and supply chain management.

Authors: Taijie Chen, Rui Su, Siyuan Feng, Laoming Zhang, Hongyang Zhang, Haijiao Wang, Zhaofeng Ma, Jintao Ke  
Source: arXiv:2605.20036  
URL: [https://arxiv.org/abs/2605.20036v1](https://arxiv.org/abs/2605.20036v1)
