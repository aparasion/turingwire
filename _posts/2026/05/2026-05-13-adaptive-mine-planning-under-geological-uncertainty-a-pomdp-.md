---
title: "Adaptive mine planning under geological uncertainty: A POMDP framework for sequential decision-making"
date: 2026-05-13 15:52:29 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13702v1"
arxiv_id: "2605.13702"
authors: ["Hamza Khalifi", "Jef Caers", "Yassine Taha", "Mostafa Benzaazoua", "Abdellatif Elghali"]
slug: adaptive-mine-planning-under-geological-uncertainty-a-pomdp-
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of conventional mine production scheduling methods that treat geological uncertainty as a passive constraint. Traditional approaches utilize stochastic optimization to derive a fixed extraction sequence and routing decisions without considering how future observations can inform subsequent decisions. The authors propose a novel framework that reformulates mine scheduling as a Partially Observable Markov Decision Process (POMDP), allowing for sequential decision-making that actively incorporates the expectation of future belief updates. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of a hybrid SA-POMDP architecture that integrates simulated annealing (SA) for value approximation with ensemble-based belief updating through an ensemble smoother with multiple data assimilation (ES-MDA). The architecture allows for the evaluation of candidate actions based on their expected long-term value under the current belief state at each decision epoch. As mining observations are assimilated, the belief state is updated, enabling the formulation of an adaptive policy rather than a static plan. The authors detail the computational tractability of their approach, although specific training compute requirements are not disclosed.

**Results**  
The proposed SA-POMDP framework was evaluated on a copper-gold open-pit mining complex with multiple processing destinations. Under a statistically consistent prior, the expectation-reality gap was reduced from 22.3% to 4.6%, resulting in an increase in the net present value (NPV) of USD8.4 million compared to traditional one-shot stochastic optimization methods. In scenarios with a systematic prior misspecification of 10%, the adaptive framework demonstrated a significant advantage, outperforming static planning by up to USD44.6 million (36.9%). These results indicate that the adaptive approach not only mitigates the effects of uncertainty but also enhances value creation in mining operations.

**Limitations**  
The authors acknowledge that their framework relies on the accuracy of the initial belief state and the effectiveness of the ensemble smoother for belief updating. They do not address potential computational scalability issues when applied to larger or more complex mining operations. Additionally, the impact of varying degrees of geological uncertainty on the performance of the proposed method is not thoroughly explored, which could limit generalizability.

**Why it matters**  
This research has significant implications for the field of mining engineering and decision-making under uncertainty. By transforming geological uncertainty from a passive constraint into an active component of value creation, the proposed POMDP framework offers a more dynamic and responsive approach to mine planning. This could lead to improved economic outcomes and operational efficiencies in mining projects, encouraging further exploration of adaptive decision-making frameworks in other domains where uncertainty plays a critical role.

Authors: Hamza Khalifi, Jef Caers, Yassine Taha, Mostafa Benzaazoua, Abdellatif Elghali  
Source: arXiv:2605.13702  
URL: https://arxiv.org/abs/2605.13702v1
