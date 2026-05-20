---
title: "Take It or Leave It: Intent-Controlled Partial Optimal Transport"
date: 2026-05-19 15:52:59 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20030v1"
arxiv_id: "2605.20030"
authors: ["Salil Parth Tripathi", "Bertrand Chapron", "Fabrice Collard", "Nicolas Courty", "Ronan Fablet"]
slug: take-it-or-leave-it-intent-controlled-partial-optimal-transp
summary_word_count: 444
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the optimal transport (OT) literature, specifically the limitations of traditional optimal transport methods that require exact matching of measures. While partial optimal transport (POT) allows for unmatched mass through global mechanisms, many applications necessitate more nuanced, pointwise rejection strategies. The authors propose a novel framework, intent-controlled partial optimal transport (IC-POT), which introduces structured rejection mechanisms based on side-specific reliability and external information. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the formulation of IC-POT, which generalizes POT by incorporating pointwise rejection costs for both measures involved in the transport problem. The optimization problem is reformulated to allow for local acceptance thresholds, enabling a more flexible approach to mass rejection. The authors demonstrate that this can be solved by transforming it into a balanced Kantorovich OT problem on an augmented support, which facilitates efficient computation. The paper does not disclose specific training compute requirements, but it emphasizes the theoretical underpinnings and practical implications of the proposed method.

**Results**  
The authors validate IC-POT through empirical evaluations in two primary applications: positive-unlabeled learning and open-partial domain adaptation. In both cases, the incorporation of pointwise rejection rules significantly enhances the performance of baseline models. For instance, in positive-unlabeled learning, IC-POT outperforms traditional POT methods, achieving a notable improvement in precision and recall metrics. In the context of open-partial domain adaptation, the method demonstrates superior adaptability to varying data distributions, leading to enhanced classification accuracy compared to established benchmarks. The paper provides quantitative results, although specific numerical values and baseline comparisons are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while IC-POT offers a more flexible rejection mechanism, it may introduce additional complexity in terms of computational overhead and parameter tuning. They also note that the method's performance is contingent on the quality of the side information used for rejection decisions. An obvious limitation not explicitly mentioned is the potential scalability issues when applied to high-dimensional data, which could affect the practical deployment of IC-POT in real-world scenarios.

**Why it matters**  
The introduction of IC-POT has significant implications for various downstream applications where optimal transport is utilized, particularly in scenarios requiring nuanced decision-making based on contextual information. By enabling pointwise rejection mechanisms, IC-POT enhances the flexibility and applicability of transport methods in fields such as machine learning, geophysics, and data science. This work paves the way for future research to explore more sophisticated transport frameworks that can leverage side information, potentially leading to improved performance in complex, real-world tasks.

Authors: Salil Parth Tripathi, Bertrand Chapron, Fabrice Collard, Nicolas Courty, Ronan Fablet  
Source: arXiv:2605.20030  
URL: https://arxiv.org/abs/2605.20030v1
