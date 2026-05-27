---
title: "Algorithmic Monocultures in Hiring"
date: 2026-05-26 17:59:55 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27371v1"
arxiv_id: "2605.27371"
authors: ["Rishi Bommasani", "Sarah H. Bana", "Kathleen A. Creel", "Dan Jurafsky", "Percy Liang"]
slug: algorithmic-monocultures-in-hiring
summary_word_count: 456
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the impact of algorithmic monoculture in hiring practices, specifically how reliance on a limited number of algorithm vendors can lead to systemic biases against certain racial groups. The authors investigate whether the use of similar screening algorithms results in homogeneous rejection patterns, disproportionately affecting Asian and Black applicants. The study is motivated by the lack of empirical evidence on the consequences of algorithmic hiring practices, particularly in terms of racial disparities.

**Method**  
The authors analyze a novel dataset comprising 3 million applicants who submitted 4 million applications, all screened by algorithms from a single vendor. They employ statistical analysis to identify disparities in applicant outcomes, focusing on rejection rates and the distribution of recommendations across racial groups. The study quantifies the adverse impact on applicants by comparing rejection rates against U.S. employment discrimination standards. Additionally, the authors utilize a deterministic approach to simulate outcomes for applicants had they applied to all available positions, thereby assessing the extent of homogeneity in rejection patterns.

**Results**  
The findings reveal significant racial disparities in hiring outcomes. Specifically, 14.74% of applications from Asian applicants and 25.87% from Black applicants were submitted to positions that adversely impacted these groups according to established discrimination standards. Furthermore, the study highlights that 4% of applicants who applied to 10 positions received rejections from all, a rate that exceeds what would be expected by chance. This suggests a concerning level of uniformity in rejection outcomes, indicating that applicants are not only facing systemic bias but also a lack of diversity in the decision-making process of the algorithms.

**Limitations**  
The authors acknowledge several limitations, including the focus on a single vendor's algorithms, which may not generalize to other hiring contexts or vendors. The dataset, while large, may not capture the full spectrum of hiring practices across different industries. Additionally, the study does not explore the underlying reasons for the observed disparities, such as the specific features or training data used in the algorithms. There is also a lack of longitudinal data to assess the long-term implications of these hiring practices on career trajectories.

**Why it matters**  
This research has significant implications for the development and deployment of algorithmic hiring tools. It underscores the need for greater transparency and accountability in algorithm design, particularly regarding the potential for systemic bias. The findings suggest that organizations should critically evaluate their reliance on a limited set of algorithms and consider diversifying their hiring practices to mitigate adverse impacts on underrepresented groups. Furthermore, this work opens avenues for future research into the mechanisms of bias in algorithmic decision-making and the development of more equitable hiring frameworks.

Authors: Rishi Bommasani, Sarah H. Bana, Kathleen A. Creel, Dan Jurafsky, Percy Liang  
Source: arXiv:2605.27371  
URL: [https://arxiv.org/abs/2605.27371v1](https://arxiv.org/abs/2605.27371v1)
